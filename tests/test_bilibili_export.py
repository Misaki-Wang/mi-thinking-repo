"""Authorized snapshot export must preserve rendered text and exclude private inputs."""

import contextlib
import copy
import hashlib
import importlib
import io
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest import mock

SCRIPTS = Path(__file__).resolve().parents[1] / "scripts"
with mock.patch.object(sys, "path", [str(SCRIPTS), *sys.path]):
    render = importlib.import_module("render_bilibili_transcripts")
    export = importlib.import_module("export_bilibili_transcripts")


class BilibiliExportTests(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        # macOS /var is a symlink; the production safety check intentionally rejects it.
        self.root = Path(temporary.name).resolve()
        self.transcripts = self.root / "transcripts"
        self.ids = ["BV1XNtJ6UEmm", "BV1KZ8X6uEPL"]
        self.videos = [
            {"bvid": bvid, "cid": 41286961556 + index,
             "title": f"示例 {index + 1}：中文、MoE 与 multi-teacher distillation",
             "uploader": "示例 UP 主", "uploader_id": "280780745",
             "published_at": f"2026-09-0{3 - index}T08:00:00+08:00",
             "duration": 65, "playback_duration": 65.25}
            for index, bvid in enumerate(self.ids)
        ]
        self.inventory = {
            "videos": self.videos, "latest_bvids": list(self.ids),
            "uploader": "示例 UP 主", "uploader_id": "280780745",
            "retrieved_at": "2026-09-10T17:11:56+08:00",
        }
        self.authorization = {
            "confirmed": True, "uploader_id": "280780745", "bvids": list(self.ids),
            "confirmed_at": "2026-09-10T18:00:00+08:00",
            "statement": "已获得这两期视频完整讲稿的翻译及公开再发布授权。",
        }
        for index, video in enumerate(self.videos):
            raw_path = self.root / "private-asr" / video["bvid"] / "source.json"
            raw_path.parent.mkdir(parents=True)
            raw = {"language": "zh", "segments": [
                {"id": 0, "start": 0, "end": 20, "text": f"第 {index + 1} 期讨论 MoE，"},
                {"id": 1, "start": 20, "end": 40, "text": "以及 multi-teacher distillation。"},
                {"id": 2, "start": 40, "end": 65.25, "text": "保留数字 0.25 与 x_1 < 2。"},
            ]}
            self.save(raw_path, raw)
            audio = raw_path.parent / "source.m4a"
            audio.write_bytes(b"synthetic fixture for provenance hashing")
            render.render_video(video, raw_path, self.transcripts / video["bvid"],
                                provider="qwen-asr", model="Qwen/Qwen3-ASR-1.7B", audio_path=audio)

    @staticmethod
    def save(path, value):
        path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    def paths(self, bvid=None):
        directory = self.transcripts / (bvid or self.ids[0])
        return (directory / "transcript.zh-CN.md", directory / "data/paragraphs.json",
                directory / "validation.json")

    def prepare(self, inventory=None, authorization=None):
        return export.prepare_export(self.inventory if inventory is None else inventory,
                                     self.authorization if authorization is None else authorization,
                                     self.transcripts)

    def cli_args(self, destination):
        inventory = self.root / "inventory.json"
        authorization = self.root / "authorization.json"
        self.save(inventory, self.inventory)
        self.save(authorization, self.authorization)
        return ["export_bilibili_transcripts.py", "--inventory", str(inventory),
                "--authorization", str(authorization), "--transcripts", str(self.transcripts),
                "--output", str(destination)]

    def rewrite_data(self, mutate):
        _, path, report_path = self.paths()
        data = json.loads(path.read_text())
        report = json.loads(report_path.read_text())
        mutate(data, report)
        self.save(path, data)
        report["output_hashes"]["data/paragraphs.json"] = hashlib.sha256(path.read_bytes()).hexdigest()
        self.save(report_path, report)

    def test_valid_snapshot_exports_exact_renderer_bytes_and_allowlisted_files(self):
        manifest, outputs = self.prepare()
        expected = {f"{bvid}/transcript.zh-CN.md" for bvid in self.ids} | {"manifest.json", "QUALITY.md"}
        self.assertEqual(set(outputs), expected)
        self.assertEqual(manifest["video_count"], 2)
        self.assertEqual(manifest["segment_count"], 6)
        self.assertEqual(manifest["paragraph_count"], 4)
        self.assertEqual(manifest["audio_duration_seconds"], 130.5)
        self.assertEqual([entry["bvid"] for entry in manifest["videos"]], self.ids)
        self.assertEqual(json.loads(outputs["manifest.json"]), manifest)
        for entry in manifest["videos"]:
            path, _, _ = self.paths(entry["bvid"])
            rendered_bytes = path.read_bytes()
            exported_bytes = outputs[f"{entry['bvid']}/transcript.zh-CN.md"].encode("utf-8")
            self.assertEqual(exported_bytes, rendered_bytes)
            self.assertEqual(hashlib.sha256(exported_bytes).hexdigest(), entry["transcript_sha256"])
            self.assertEqual(entry["provider"], "qwen-asr")
            self.assertEqual(entry["model"], "Qwen/Qwen3-ASR-1.7B")
            self.assertEqual(entry["semantic_accuracy"], "not_assessed")

    def test_cli_writes_exact_markdown_bytes_and_only_public_artifacts(self):
        destination = self.root / "public-export"
        stream = io.StringIO()
        with mock.patch.object(sys, "argv", self.cli_args(destination)), contextlib.redirect_stdout(stream):
            export.main()
        self.assertEqual(json.loads(stream.getvalue())["videos"], 2)
        written = {str(path.relative_to(destination)) for path in destination.rglob("*") if path.is_file()}
        self.assertEqual(written, {f"{bvid}/transcript.zh-CN.md" for bvid in self.ids}
                         | {"manifest.json", "QUALITY.md"})
        manifest = json.loads((destination / "manifest.json").read_text())
        for entry in manifest["videos"]:
            source, _, _ = self.paths(entry["bvid"])
            exported = destination / entry["bvid"] / "transcript.zh-CN.md"
            self.assertEqual(exported.read_bytes(), source.read_bytes())
            self.assertEqual(hashlib.sha256(exported.read_bytes()).hexdigest(), entry["transcript_sha256"])

    def test_cli_validates_all_videos_before_writing_any_public_output(self):
        source, _, _ = self.paths(self.ids[1])
        source.write_text("# Corrupted second transcript\n")
        destination = self.root / "public-export"
        with mock.patch.object(sys, "argv", self.cli_args(destination)), self.assertRaises(ValueError):
            export.main()
        self.assertFalse(destination.exists())

    def test_cli_does_not_overwrite_another_creators_collection(self):
        destination = self.root / "existing-collection"
        destination.mkdir()
        self.save(destination / "manifest.json", {"uploader_id": "508452265"})
        (destination / "QUALITY.md").write_text("Existing creator's quality record\n")
        before = {p.name: p.read_bytes() for p in destination.iterdir()}
        with mock.patch.object(sys, "argv", self.cli_args(destination)), self.assertRaisesRegex(ValueError, "creator"):
            export.main()
        self.assertEqual(before, {p.name: p.read_bytes() for p in destination.iterdir()})

    def test_cli_can_refresh_the_same_creators_collection(self):
        destination = self.root / "same-creator"
        with mock.patch.object(sys, "argv", self.cli_args(destination)), contextlib.redirect_stdout(io.StringIO()):
            export.main()
            export.main()
        self.assertEqual(json.loads((destination / "manifest.json").read_text())["uploader_id"], "280780745")

    def test_absent_partial_false_or_string_authorization_is_rejected(self):
        variants = [{}, dict(self.authorization, confirmed=False),
                    dict(self.authorization, confirmed="true"),
                    dict(self.authorization, bvids=self.ids[:1]),
                    dict(self.authorization, statement=""),
                    dict(self.authorization, confirmed_at="")]
        for key in self.authorization:
            partial = dict(self.authorization)
            del partial[key]
            variants.append(partial)
        for authorization in variants:
            with self.subTest(authorization=authorization), self.assertRaises(ValueError):
                self.prepare(authorization=authorization)

    def test_authorization_creator_and_order_must_match_snapshot(self):
        for authorization in (dict(self.authorization, uploader_id="999"),
                              dict(self.authorization, bvids=list(reversed(self.ids)))):
            with self.subTest(authorization=authorization), self.assertRaises(ValueError):
                self.prepare(authorization=authorization)
        for inventory in (dict(self.inventory, latest_bvids=list(reversed(self.ids))),
                          dict(self.inventory, videos=list(reversed(self.videos)))):
            with self.subTest(inventory=inventory), self.assertRaises(ValueError):
                self.prepare(inventory=inventory)

    def test_each_video_creator_must_match_authorized_creator(self):
        inventory = copy.deepcopy(self.inventory)
        inventory["videos"][0]["uploader_id"] = "999"
        with self.assertRaises(ValueError):
            self.prepare(inventory=inventory)

    def test_rendered_creator_mismatch_is_rejected_even_when_hashes_match(self):
        def mutate(data, report):
            data["metadata"]["author_id"] = "999"
            report["metadata"] = copy.deepcopy(data["metadata"])
        self.rewrite_data(mutate)
        with self.assertRaises(ValueError):
            self.prepare()

    def test_duplicate_inventory_is_rejected(self):
        inventory = copy.deepcopy(self.inventory)
        inventory["videos"] = [inventory["videos"][0], inventory["videos"][0]]
        inventory["latest_bvids"] = [self.ids[0], self.ids[0]]
        authorization = dict(self.authorization, bvids=list(inventory["latest_bvids"]))
        with self.assertRaises(ValueError):
            self.prepare(inventory=inventory, authorization=authorization)

    def test_corrupted_markdown_is_rejected_by_hash(self):
        markdown, _, _ = self.paths()
        markdown.write_text(markdown.read_text().replace("multi-teacher", "single-teacher"))
        with self.assertRaisesRegex(ValueError, "hash mismatch"):
            self.prepare()

    def test_rehashed_corrupt_markdown_is_rejected_by_independent_render_check(self):
        markdown, _, report_path = self.paths()
        markdown.write_text(markdown.read_text().replace("multi-teacher", "single-teacher"))
        report = json.loads(report_path.read_text())
        report["output_hashes"]["transcript.zh-CN.md"] = hashlib.sha256(markdown.read_bytes()).hexdigest()
        self.save(report_path, report)
        with self.assertRaises(ValueError):
            self.prepare()

    def test_corrupt_data_or_report_hashes_are_rejected(self):
        _, data, report_path = self.paths()
        original_report = report_path.read_bytes()
        report = json.loads(original_report)
        report["output_hashes"]["data/paragraphs.json"] = "0" * 64
        self.save(report_path, report)
        with self.assertRaisesRegex(ValueError, "hash mismatch"):
            self.prepare()
        report_path.write_bytes(original_report)
        data.write_bytes(data.read_bytes() + b" ")
        with self.assertRaisesRegex(ValueError, "hash mismatch"):
            self.prepare()

    def test_false_accounting_claims_are_rejected(self):
        _, _, report_path = self.paths()
        original = json.loads(report_path.read_text())
        for key in ("all_segments_accounted_once_in_original_order", "all_segment_fields_preserved",
                    "all_text_preserved_exactly"):
            for value in (False, "true", None):
                report = copy.deepcopy(original)
                report["accounting"][key] = value
                self.save(report_path, report)
                with self.subTest(key=key, value=value), self.assertRaisesRegex(ValueError, "accounting"):
                    self.prepare()

    def test_rehashed_corrupt_paragraph_text_fails_independent_accounting(self):
        def mutate(data, _report):
            data["paragraphs"][0]["text"] = "替换后的不真实内容。"
        self.rewrite_data(mutate)
        with self.assertRaisesRegex(ValueError, "accounting"):
            self.prepare()

    def test_rehashed_missing_segment_indices_fail_independent_accounting(self):
        def mutate(data, _report):
            data["paragraphs"][0]["raw_segment_indices"].pop()
        self.rewrite_data(mutate)
        with self.assertRaisesRegex(ValueError, "accounting"):
            self.prepare()

    def test_changed_report_counts_fail_independent_accounting(self):
        _, _, report_path = self.paths()
        original = json.loads(report_path.read_text())
        for key in ("paragraph_count", "raw_segment_count"):
            report = copy.deepcopy(original)
            report["accounting"][key] += 1
            self.save(report_path, report)
            with self.subTest(key=key), self.assertRaisesRegex(ValueError, "accounting"):
                self.prepare()

    def test_symlink_file_inside_transcript_root_is_rejected(self):
        markdown, _, _ = self.paths()
        backup = markdown.with_suffix(".original")
        markdown.rename(backup)
        markdown.symlink_to(backup)
        with self.assertRaisesRegex(ValueError, "unsafe input"):
            self.prepare()

    def test_symlink_video_directory_outside_transcript_root_is_rejected(self):
        directory = self.transcripts / self.ids[0]
        moved = self.root / "outside-video"
        directory.rename(moved)
        directory.symlink_to(moved, target_is_directory=True)
        with self.assertRaisesRegex(ValueError, "unsafe input"):
            self.prepare()

    def test_exported_manifest_excludes_raw_media_urls_and_private_paths(self):
        secret_url = "https://upos-sz-mirror.bilivideo.com/audio.m4a?deadline=999&token=PRIVATE_TOKEN"
        private_path = str(self.root / "private-asr" / self.ids[0] / "source.json")
        inventory = copy.deepcopy(self.inventory)
        inventory["raw_audio_url"] = secret_url
        inventory["private_cache"] = private_path
        inventory["videos"][0]["public_audio_formats"] = [{"url": secret_url}]
        inventory["videos"][0]["description"] = private_path
        authorization = dict(self.authorization, private_evidence_path=private_path)
        manifest, outputs = self.prepare(inventory=inventory, authorization=authorization)
        serialized = json.dumps(manifest, ensure_ascii=False)
        self.assertNotIn(secret_url, serialized)
        self.assertNotIn("PRIVATE_TOKEN", serialized)
        self.assertNotIn(private_path, serialized)
        self.assertNotIn(str(self.root), serialized)
        self.assertNotIn("private-asr", serialized)
        for entry in manifest["videos"]:
            self.assertEqual(len(entry["raw_asr_sha256"]), 64)
            self.assertEqual(len(entry["audio_sha256"]), 64)
            self.assertEqual(entry["source_url"], f"https://www.bilibili.com/video/{entry['bvid']}/")
        self.assertTrue(all(not name.endswith((".m4a", ".wav", ".log")) for name in outputs))


if __name__ == "__main__":
    unittest.main()
