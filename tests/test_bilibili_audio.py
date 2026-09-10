"""Source provenance survives rejected or unverifiable audio reuse."""

import contextlib
import copy
import hashlib
import importlib.util
import io
import json
from pathlib import Path
import subprocess
import tempfile
import unittest
from unittest import mock


SPEC = importlib.util.spec_from_file_location(
    "download_bilibili_audio",
    Path(__file__).resolve().parents[1] / "scripts/download_bilibili_audio.py",
)
audio = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(audio)


class BilibiliAudioTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name) / ".work" / "audio-test"
        self.video = {"bvid": "BV1KZ8X6uEPL", "title": "Example", "uploader_id": "280780745",
                      "duration": 60, "playback_duration": 60.125, "parts": [{"page": 1}]}
        self.folder = self.root / "audio" / self.video["bvid"]
        self.folder.mkdir(parents=True)
        self.source = self.folder / "source.m4a"
        self.source.write_bytes(b"synthetic-audio-fixture")
        self.log = self.folder / "download.log"
        self.log.write_text("Original download provenance.\n")
        self.manifest = self.folder / "manifest.json"
        self.checked = {"local_path": str(self.source), "size_bytes": self.source.stat().st_size,
                        "sha256": hashlib.sha256(self.source.read_bytes()).hexdigest(),
                        "duration_seconds": 60.125, "expected_duration_seconds": 60.125,
                        "ffprobe": {"streams": [{"codec_type": "audio", "codec_name": "aac"}]}}
        self.record = {**self.checked, "bvid": self.video["bvid"], "uploader_id": "280780745",
                       "source_url": f"https://www.bilibili.com/video/{self.video['bvid']}/",
                       "status": "complete", "requested_audio_format": "bestaudio",
                       "started_at": "original-start", "finished_at": "original-finish"}
        self.write_record()

    def write_record(self, record=None):
        self.manifest.write_text(json.dumps(self.record if record is None else record))

    def snapshot(self):
        return {path.name: path.read_bytes() for path in self.folder.iterdir() if path.is_file()}

    def invoke(self, selector="bestaudio", checked=None):
        with contextlib.redirect_stdout(io.StringIO()), \
                mock.patch.object(audio, "verify", return_value=self.checked if checked is None else checked), \
                mock.patch.object(audio.subprocess, "run") as command:
            result = audio.download(self.video, self.root, 60, "fixture", selector)
        command.assert_not_called()
        return result

    def assert_rejected_without_changes(self, selector="bestaudio", checked=None):
        before = self.snapshot()
        result = self.invoke(selector, checked)
        self.assertEqual(result["status"], "failed")
        self.assertFalse(result.get("reused_existing", False))
        self.assertEqual(self.snapshot(), before)

    def test_different_format_preserves_manifest_log_and_media(self):
        self.assert_rejected_without_changes("30216")

    def test_different_format_preserves_records_even_when_media_is_missing(self):
        self.source.unlink()
        self.assert_rejected_without_changes("30216")

    def test_media_without_manifest_is_not_assigned_requested_format(self):
        self.manifest.unlink()
        self.assert_rejected_without_changes("30216")
        self.assertFalse(self.manifest.exists())

    def test_unknown_partial_download_is_not_resumed_under_another_format(self):
        self.source.rename(self.folder / "source.m4a.part")
        self.manifest.unlink()
        self.assert_rejected_without_changes("30216")

    def test_malformed_or_nonobject_manifest_is_preserved(self):
        for value in ("not json", "[]", "null"):
            with self.subTest(value=value):
                self.manifest.write_text(value)
                self.assert_rejected_without_changes()

    def test_failed_or_incomplete_record_does_not_authorize_reuse(self):
        for field in ("sha256", "size_bytes", "duration_seconds", "source_url", "bvid", "uploader_id"):
            with self.subTest(field=field):
                record = copy.deepcopy(self.record)
                del record[field]
                self.write_record(record)
                self.assert_rejected_without_changes()
        self.write_record({**self.record, "status": "failed"})
        self.assert_rejected_without_changes()

    def test_reuse_rejects_changed_checksum_size_or_duration(self):
        for changed in ({"sha256": "f" * 64}, {"size_bytes": 1}, {"duration_seconds": 59.0}):
            with self.subTest(changed=changed):
                self.write_record()
                self.assert_rejected_without_changes(checked={**self.checked, **changed})

    def test_record_for_another_source_is_not_reused(self):
        for changed in ({"bvid": "BV1XNtJ6UEmm"}, {"uploader_id": "123"},
                        {"source_url": "https://www.bilibili.com/video/BV1XNtJ6UEmm/"}):
            with self.subTest(changed=changed):
                self.write_record({**self.record, **changed})
                self.assert_rejected_without_changes()

    def test_verified_same_format_reuse_preserves_original_provenance(self):
        before = self.snapshot()
        result = self.invoke()
        self.assertEqual(result["status"], "complete")
        self.assertTrue(result["reused_existing"])
        self.assertEqual(result["sha256"], self.record["sha256"])
        self.assertEqual(result["started_at"], "original-start")
        self.assertEqual(result["finished_at"], "original-finish")
        self.assertEqual(self.snapshot(), before)

    def test_verified_explicit_format_reuses_without_relabeling_bestaudio(self):
        self.write_record({**self.record, "requested_audio_format": "30216"})
        before = self.snapshot()
        result = self.invoke("30216")
        self.assertEqual(result["status"], "complete")
        self.assertTrue(result["reused_existing"])
        self.assertEqual(result["requested_audio_format"], "30216")
        self.assertEqual(self.snapshot(), before)

    def test_failed_media_verification_preserves_existing_evidence(self):
        before = self.snapshot()
        with contextlib.redirect_stdout(io.StringIO()), \
                mock.patch.object(audio, "verify", side_effect=RuntimeError("ffprobe rejected source")), \
                mock.patch.object(audio.subprocess, "run") as command:
            result = audio.download(self.video, self.root, 60, "fixture")
        self.assertEqual(result["status"], "failed")
        self.assertEqual(self.snapshot(), before)
        command.assert_not_called()

    def test_legacy_format_requires_evidence_from_recorded_command(self):
        record = copy.deepcopy(self.record)
        del record["requested_audio_format"]
        self.write_record(record)
        self.assert_rejected_without_changes()
        record["command"] = ["python", "-m", "yt_dlp", "-f", "bestaudio", self.record["source_url"]]
        self.write_record(record)
        before = self.snapshot()
        result = self.invoke()
        self.assertEqual(result["status"], "complete")
        self.assertTrue(result["reused_existing"])
        self.assertEqual(self.snapshot(), before)

    def test_new_download_records_explicit_format_and_isolated_output(self):
        output_root = self.root / "audio30216"
        target = output_root / self.video["bvid"] / "source.m4a"
        old_snapshot = self.snapshot()

        def fake_download(command, **kwargs):
            self.assertEqual(command[command.index("-f") + 1], "30216")
            self.assertIn(str(target.with_name("source.%(ext)s")), command)
            target.write_bytes(b"synthetic-audio-fixture")
            return subprocess.CompletedProcess(command, 0, "downloaded", "")

        with contextlib.redirect_stdout(io.StringIO()), \
                mock.patch.object(audio.subprocess, "run", side_effect=fake_download), \
                mock.patch.object(audio, "verify", return_value={**self.checked, "local_path": str(target)}):
            result = audio.download(self.video, self.root, 60, "fixture", "30216", output_root)
        self.assertEqual(result["status"], "complete")
        self.assertFalse(result["reused_existing"])
        self.assertEqual(result["requested_audio_format"], "30216")
        self.assertEqual(self.snapshot(), old_snapshot)
        self.assertEqual(json.loads((target.parent / "manifest.json").read_text())["status"], "complete")

    def test_workers_cannot_exceed_two_or_be_zero(self):
        for workers in ("0", "3"):
            with self.subTest(workers=workers), \
                    mock.patch.object(audio.sys, "argv", ["download", "--workers", workers]), \
                    contextlib.redirect_stderr(io.StringIO()), \
                    mock.patch.object(audio.subprocess, "run") as command:
                with self.assertRaises(SystemExit) as raised:
                    audio.main()
                self.assertEqual(raised.exception.code, 2)
                command.assert_not_called()

    def test_default_cli_retains_bestaudio_and_two_worker_limit(self):
        videos = [self.video, {**self.video, "bvid": "BV1XNtJ6UEmm"}]
        (self.root / "inventory.json").write_text(json.dumps({"videos": videos,
            "uploader_id": "280780745", "sample_bvid": self.video["bvid"]}))
        with mock.patch.object(audio.sys, "argv", ["download", "--root", str(self.root)]), \
                mock.patch.object(audio.shutil, "which", return_value="ffprobe"), \
                mock.patch.object(audio.subprocess, "run", return_value=subprocess.CompletedProcess([], 0, "fixture", "")), \
                mock.patch.object(audio, "download", side_effect=lambda video, *args: {"status": "complete", "bvid": video["bvid"]}) as download, \
                mock.patch.object(audio, "ThreadPoolExecutor", wraps=audio.ThreadPoolExecutor) as pool:
            self.assertEqual(audio.main(), 0)
        pool.assert_called_once_with(max_workers=2)
        self.assertEqual(download.call_count, 2)
        for call in download.call_args_list:
            self.assertEqual(call.args[4], "bestaudio")
            self.assertIsNone(call.args[5])


if __name__ == "__main__":
    unittest.main()
