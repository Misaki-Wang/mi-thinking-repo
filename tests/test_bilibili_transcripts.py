"""Lossless ASR grouping and honest failure/quality reporting for Bilibili."""

import contextlib
import copy
import hashlib
import importlib.util
import io
import json
from pathlib import Path
import tempfile
import unittest

SPEC = importlib.util.spec_from_file_location(
    "render_bilibili_transcripts",
    Path(__file__).resolve().parents[1] / "scripts/render_bilibili_transcripts.py",
)
render = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(render)


class BilibiliTranscriptTests(unittest.TestCase):
    def setUp(self):
        self.video = {
            "bvid": "BV1KZ8X6uEPL", "cid": 41286961556,
            "title": "Kimi K3：architecture 与 MoE", "uploader": "示例 UP 主",
            "uploader_id": "280780745", "published_at": "2026-08-26T17:40:17+08:00",
            "duration": 95, "playback_duration": 95.25,
        }
        self.raw = {
            "language": "zh",
            "segments": [
                {"id": 0, "start": 0.0, "end": 18.5, "text": "这里讨论 MoE，", "tokens": [10, 20]},
                {"id": 1, "start": 18.5, "end": 35.0, "text": "以及 multi-teacher distillation。"},
                {"id": 2, "start": 35.0, "end": 62.0, "text": "\n x_1 < 2 & [value]，"},
                {"id": 3, "start": 62.0, "end": 95.25, "text": "原话并没有说 Kimi K3。"},
            ],
        }

    def run_render(self, directory, raw=None, video=None, **kwargs):
        directory = Path(directory)
        source = directory / "source.json"
        source.write_text(json.dumps(self.raw if raw is None else raw, ensure_ascii=False), encoding="utf-8")
        report = render.render_video(self.video if video is None else video, source,
                                     directory / "output", model="turbo", **kwargs)
        data = json.loads((directory / "output/data/paragraphs.json").read_text())
        markdown = (directory / "output/transcript.zh-CN.md").read_text()
        return report, data, markdown

    def test_grouping_preserves_every_character_field_and_original_index(self):
        paragraphs = render.group_segments(render.validate_raw(self.raw))
        self.assertEqual([item["raw_segment_indices"] for item in paragraphs], [[0, 1], [2], [3]])
        audit = render.audit_accounting(self.raw["segments"], paragraphs)
        self.assertTrue(audit["all_segments_accounted_once_in_original_order"])
        self.assertTrue(audit["all_segment_fields_preserved"])
        self.assertTrue(audit["all_text_preserved_exactly"])
        self.assertEqual(audit["raw_text_sha256"], audit["paragraph_text_sha256"])
        self.assertEqual(paragraphs[0]["segments"][0]["tokens"], [10, 20])

    def test_accounting_catches_dropped_reordered_and_rewritten_content(self):
        good = render.group_segments(self.raw["segments"])
        for paragraphs in (good[:-1], list(reversed(good))):
            with self.subTest(paragraphs=paragraphs):
                self.assertFalse(render.audit_accounting(self.raw["segments"], paragraphs)
                                 ["all_segments_accounted_once_in_original_order"])
        changed = copy.deepcopy(good)
        changed[0]["text"] = "更正为 Kimi K3。"
        self.assertFalse(render.audit_accounting(self.raw["segments"], changed)["all_text_preserved_exactly"])

    def test_render_has_canonical_source_timestamps_cid_and_no_guessed_speakers(self):
        with tempfile.TemporaryDirectory() as directory:
            report, data, markdown = self.run_render(directory)
        self.assertIn("https://www.bilibili.com/video/BV1KZ8X6uEPL/?t=35&cid=41286961556", markdown)
        self.assertIn("multi-teacher distillation", markdown)
        self.assertIn(r"x\_1 &lt; 2 &amp; \[value\]", markdown)
        self.assertEqual(data["metadata"]["asr_provider"], "openai-whisper")
        self.assertEqual(data["metadata"]["asr_model"], "turbo")
        self.assertEqual(data["metadata"]["timestamp_kind"], "asr_segment")
        self.assertNotIn("时间戳为连续音频分块起点", markdown)
        self.assertEqual(report["semantic_accuracy"], "not_assessed")
        self.assertEqual(report["speaker_attribution"], "not_performed")
        self.assertEqual(report["status"], "structurally_valid_unreviewed")

    def test_generic_provider_uses_recorded_model_and_does_not_invent_metrics(self):
        self.raw["model"] = "Qwen/Qwen3-ASR-1.7B"
        with tempfile.TemporaryDirectory() as directory:
            directory = Path(directory)
            source = directory / "source.json"
            source.write_text(json.dumps(self.raw, ensure_ascii=False), encoding="utf-8")
            report = render.render_video(self.video, source, directory / "output", provider="qwen-asr")
            data = json.loads((directory / "output/data/paragraphs.json").read_text())
            markdown = (directory / "output/transcript.zh-CN.md").read_text()
        self.assertEqual(data["metadata"]["asr_provider"], "qwen-asr")
        self.assertEqual(data["metadata"]["asr_model"], "Qwen/Qwen3-ASR-1.7B")
        self.assertIn("qwen-asr / Qwen/Qwen3-ASR-1.7B", markdown)
        self.assertIn("原始 ASR 自动转写初稿", markdown)
        self.assertIn("尚未逐句人工校对", markdown)
        self.assertIn("英文名称、专业术语", markdown)
        self.assertNotIn("Whisper", markdown)
        self.assertFalse(any(item["kind"].startswith("suspicious_") for item in report["advisories"]))
        recovered = [segment for paragraph in data["paragraphs"] for segment in paragraph["segments"]]
        self.assertEqual(recovered, self.raw["segments"])
        self.assertTrue(report["accounting"]["all_text_preserved_exactly"])

    def test_audio_chunk_mode_discloses_coarse_timing_and_preserves_exact_boundaries(self):
        self.raw["timestamp_kind"] = "audio_chunk"
        self.raw["segments"] = [
            {"id": 0, "start": 0.0, "end": 64.625, "text": "第一块介绍 mixture of experts。"},
            {"id": 1, "start": 64.625, "end": 126.125, "text": "第二块讨论多教师蒸馏。"},
        ]
        with tempfile.TemporaryDirectory() as directory:
            report, data, markdown = self.run_render(directory, provider="qwen-asr", audio_duration=126.125)
        self.assertEqual(data["metadata"]["timestamp_kind"], "audio_chunk")
        self.assertEqual(report["metadata"]["timestamp_kind"], "audio_chunk")
        self.assertIn("时间戳为连续音频分块起点（约1分钟），不是逐字对齐；点击回到该片段开始", markdown)
        self.assertEqual([paragraph["start"] for paragraph in data["paragraphs"]], [0.0, 64.625])
        self.assertEqual([paragraph["end"] for paragraph in data["paragraphs"]], [64.625, 126.125])
        self.assertIn("?t=64&cid=", markdown)
        recovered = [segment for paragraph in data["paragraphs"] for segment in paragraph["segments"]]
        self.assertEqual(recovered, self.raw["segments"])
        self.assertTrue(all("words" not in segment and "word_timestamps" not in segment for segment in recovered))
        chunk_advisories = [item for item in report["advisories"] if item["kind"] == "intended_chunk_duration_over60"]
        self.assertEqual(len(chunk_advisories), 2)
        self.assertTrue(all("不代表模型识别错误" in item["message"] for item in chunk_advisories))
        self.assertIn("这些是分块时长记录，不是已确认的识别错误", markdown)
        self.assertFalse(any(item["kind"] == "long_segment" for item in report["advisories"]))
        self.assertTrue(report["accounting"]["all_text_preserved_exactly"])

    def test_legacy_long_segment_advisory_remains_unchanged(self):
        report = render.quality_report([{"start": 0, "end": 65, "text": "未拆分的原始片段。"}], 65)
        kinds = {item["kind"] for item in report["advisories"]}
        self.assertIn("long_segment", kinds)
        self.assertNotIn("intended_chunk_duration_over60", kinds)

    def test_submillisecond_boundary_rounding_does_not_flag_or_change_raw_times(self):
        self.raw["segments"] = [{"id": 124, "start": 7459.566, "end": 7459.665875, "text": "嗯。"}]
        with tempfile.TemporaryDirectory() as directory:
            report, data, _ = self.run_render(directory, audio_duration=7459.665850)
        self.assertFalse(any(item["kind"] == "timestamp_outside_audio" for item in report["advisories"]))
        self.assertEqual(data["paragraphs"][0]["segments"], self.raw["segments"])
        self.assertEqual(data["paragraphs"][0]["end"], 7459.665875)
        self.assertEqual(report["thresholds"]["timestamp_tolerance_seconds"], 0.001)

    def test_one_millisecond_tolerance_has_a_real_boundary(self):
        for start, end, expected_flag in ((-0.001, 10.001, False), (-0.000025, 10.000025, False),
                                           (-0.001001, 10, True), (0, 10.001001, True),
                                           (-0.1, 10, True), (0, 10.1, True)):
            with self.subTest(start=start, end=end):
                segments = [{"start": start, "end": end, "text": "保留原时间。"}]
                report = render.quality_report(segments, 10)
                self.assertEqual(any(item["kind"] == "timestamp_outside_audio" for item in report["advisories"]),
                                 expected_flag)
                self.assertEqual(segments[0]["start"], start)
                self.assertEqual(segments[0]["end"], end)

    def test_padded_short_chunk_is_flagged_with_separate_note_before_unchanged_text(self):
        self.raw["timestamp_kind"] = "audio_chunk"
        self.raw["segments"] = [{"id": 124, "start": 7459.566, "end": 7459.665875,
                                 "text": "嗯。", "padding_samples": 6402}]
        with tempfile.TemporaryDirectory() as directory:
            report, data, markdown = self.run_render(directory, provider="qwen-asr", audio_duration=7459.665850)
        risk = [item for item in report["advisories"] if item["kind"] == "padded_short_audio_text"]
        self.assertEqual(len(risk), 1)
        self.assertEqual(risk[0]["padding_samples"], 6402)
        self.assertEqual(risk[0]["raw_segment_indices"], [0])
        note = "极短音频经过补零，以下识别文字可能是静音幻觉，未确认为原视频发言。"
        self.assertIn(note + "\n\n嗯。\n", markdown)
        self.assertIn("> 编辑风险提示（原始片段索引 0）", markdown)
        self.assertEqual(data["paragraphs"][0]["text"], "嗯。")
        self.assertEqual(data["paragraphs"][0]["segments"], self.raw["segments"])
        self.assertTrue(report["accounting"]["all_text_preserved_exactly"])
        self.assertFalse(any(item["kind"] == "timestamp_outside_audio" for item in report["advisories"]))

    def test_padded_short_advisory_requires_all_conditions(self):
        base = {"start": 0, "end": 0.1, "text": "嗯。", "padding_samples": 6402}
        variants = [(base, "asr_segment"), (dict(base, end=1), "audio_chunk"),
                    (dict(base, end=1.2), "audio_chunk"), (dict(base, padding_samples=0), "audio_chunk"),
                    (dict(base, text="  "), "audio_chunk"),
                    ({key: value for key, value in base.items() if key != "padding_samples"}, "audio_chunk")]
        for segment, kind in variants:
            with self.subTest(segment=segment, kind=kind):
                report = render.quality_report([segment], 10, timestamp_kind=kind)
                self.assertFalse(any(item["kind"] == "padded_short_audio_text" for item in report["advisories"]))
        report = render.quality_report([dict(base, end=0.999)], 10, timestamp_kind="audio_chunk")
        self.assertTrue(any(item["kind"] == "padded_short_audio_text" for item in report["advisories"]))

    def test_unknown_or_nonstring_timestamp_kind_is_rejected(self):
        for value in (None, 12, "word_aligned"):
            with self.subTest(value=value), self.assertRaisesRegex(ValueError, "timestamp_kind"):
                render.validate_raw(dict(self.raw, timestamp_kind=value))

    def test_empty_provider_and_model_are_rejected_without_output(self):
        with tempfile.TemporaryDirectory() as directory:
            directory = Path(directory)
            source = directory / "source.json"
            source.write_text(json.dumps(self.raw))
            for kwargs in ({"provider": "  "}, {"provider": None}, {"model": ""}):
                with self.subTest(kwargs=kwargs), self.assertRaises(ValueError):
                    render.render_video(self.video, source, directory / "output", **kwargs)
            self.assertFalse((directory / "output").exists())

    def test_empty_text_is_flagged_and_accounted_not_silently_deleted(self):
        self.raw["segments"][1]["text"] = ""
        with tempfile.TemporaryDirectory() as directory:
            report, data, _ = self.run_render(directory)
        self.assertIn("empty_segment", {item["kind"] for item in report["advisories"]})
        self.assertTrue(report["accounting"]["all_text_preserved_exactly"])
        self.assertEqual(sum(len(item["segments"]) for item in data["paragraphs"]), 4)

    def test_all_empty_still_has_explicit_editorial_placeholder_and_coverage_gap(self):
        for segment in self.raw["segments"]:
            segment["text"] = ""
        with tempfile.TemporaryDirectory() as directory:
            report, _, markdown = self.run_render(directory)
        self.assertIn("编辑标记：本段原始 ASR 文本为空", markdown)
        self.assertEqual(report["interval_coverage"]["ratio"], 0)
        self.assertTrue(report["accounting"]["all_segments_accounted_once_in_original_order"])

    def test_repetition_and_whisper_quality_signals_are_preserved_and_flagged(self):
        self.raw["segments"] = [
            {"id": index, "start": index * 10, "end": (index + 1) * 10,
             "text": "谢谢观看" * 10, "avg_logprob": -2, "compression_ratio": 4.2,
             "no_speech_prob": 0.8} for index in range(3)
        ]
        with tempfile.TemporaryDirectory() as directory:
            report, _, markdown = self.run_render(directory)
        kinds = {item["kind"] for item in report["advisories"]}
        self.assertTrue({"repetition_within_segment", "repeated_consecutive_segments",
                         "suspicious_avg_logprob", "suspicious_compression_ratio",
                         "suspicious_no_speech_prob"}.issubset(kinds))
        self.assertEqual(markdown.count("谢谢观看"), 30)
        self.assertTrue(report["accounting"]["all_text_preserved_exactly"])

    def test_coverage_uses_interval_union_and_flags_gaps_without_guessing_silence(self):
        segments = [
            {"start": 35, "end": 50, "text": "a"},
            {"start": 45, "end": 60, "text": "b"},
            {"start": 100, "end": 110, "text": "c"},
        ]
        report = render.quality_report(segments, 150)
        self.assertEqual(report["interval_coverage"]["nonempty_segment_union_seconds"], 35)
        self.assertEqual(len(report["interval_coverage"]["gaps_at_least_30_seconds"]), 3)
        self.assertIn("overlapping_timestamps", {item["kind"] for item in report["advisories"]})
        self.assertEqual(report["semantic_accuracy"], "not_assessed")

    def test_outside_audio_and_out_of_order_are_flagged_not_clamped_or_sorted(self):
        self.raw["segments"][0]["start"] = -2
        self.raw["segments"][2]["start"] = 10
        self.raw["segments"][-1]["end"] = 110
        with tempfile.TemporaryDirectory() as directory:
            report, data, markdown = self.run_render(directory)
        kinds = {item["kind"] for item in report["advisories"]}
        self.assertTrue({"timestamp_outside_audio", "nonmonotonic_timestamps"}.issubset(kinds))
        self.assertEqual(data["paragraphs"][0]["start"], -2)
        self.assertIn("?t=0&cid=", markdown)
        self.assertNotIn("?t=-2", markdown)
        self.assertTrue(report["accounting"]["all_segment_fields_preserved"])

    def test_malformed_json_and_duplicate_keys_are_rejected(self):
        for content in ('{', '{"segments":NaN}', '{"segments":[],"segments":[]}'):
            with self.subTest(content=content), tempfile.TemporaryDirectory() as directory:
                path = Path(directory) / "source.json"
                path.write_text(content)
                with self.assertRaises(ValueError):
                    render.read_json(path)

    def test_malformed_segments_types_times_and_nonfinite_values_are_rejected(self):
        invalid = [[], {}, {"segments": []}, {"segments": ["text"]},
                   dict(self.raw, language={"bad": True}), dict(self.raw, text=["bad"])]
        for key, value in (("start", True), ("end", "30"), ("text", None),
                           ("end", -1), ("start", float("inf")), ("avg_logprob", "bad"),
                           ("id", "unstructured"), ("padding_samples", -1),
                           ("padding_samples", "6402"), ("padding_samples", True)):
            altered = copy.deepcopy(self.raw)
            altered["segments"][0][key] = value
            invalid.append(altered)
        for raw in invalid:
            with self.subTest(raw=raw), self.assertRaises(ValueError):
                render.validate_raw(raw)

    def test_duplicate_raw_ids_are_flagged_but_each_source_position_is_retained(self):
        self.raw["segments"][1]["id"] = 0
        with tempfile.TemporaryDirectory() as directory:
            report, data, _ = self.run_render(directory)
        self.assertIn("duplicate_segment_id", {item["kind"] for item in report["advisories"]})
        self.assertEqual(data["paragraphs"][0]["raw_segment_indices"], [0, 1])
        self.assertEqual(data["paragraphs"][0]["raw_segment_ids"], [0, 0])
        self.assertTrue(report["accounting"]["all_segments_accounted_once_in_original_order"])

    def test_output_hashes_and_raw_audio_provenance_can_be_reverified(self):
        with tempfile.TemporaryDirectory() as directory:
            directory = Path(directory)
            audio = directory / "source.m4a"
            audio.write_bytes(b"test audio provenance, not actual audio")
            report, data, _ = self.run_render(directory, audio_path=audio, audio_duration=96)
            for relative, expected in report["output_hashes"].items():
                actual = hashlib.sha256((directory / "output" / relative).read_bytes()).hexdigest()
                self.assertEqual(actual, expected)
            self.assertEqual(data["metadata"]["audio_provenance"]["sha256"], render.sha256(audio))
            self.assertEqual(data["metadata"]["raw_provenance"]["sha256"], render.sha256(directory / "source.json"))
            self.assertEqual(data["metadata"]["duration_seconds"], 96)
            self.assertEqual(data["metadata"]["duration_source"], "measured audio duration")

    def test_recorded_provider_and_source_audio_hash_must_match_actual_inputs(self):
        with tempfile.TemporaryDirectory() as directory:
            directory = Path(directory)
            audio = directory / "source.m4a"
            audio.write_bytes(b"actual 30216 input fixture")
            self.raw["provider"] = "qwen-asr"
            self.raw["audio_provenance"] = {"source_sha256": render.sha256(audio)}
            report, data, _ = self.run_render(directory, provider="qwen-asr", audio_path=audio)
            self.assertEqual(data["metadata"]["audio_provenance"]["sha256"], self.raw["audio_provenance"]["source_sha256"])
            self.assertEqual(data["metadata"]["asr_provider"], "qwen-asr")
            self.assertTrue(report["accounting"]["all_text_preserved_exactly"])

    def test_mismatching_or_malformed_recorded_provenance_fails_before_output(self):
        variants = [
            ({"provider": "qwen-asr"}, {}),
            ({"provider": "qwen-asr"}, {"provider": "openai-whisper"}),
            ({"audio_provenance": {"source_sha256": "0" * 64}}, {}),
            *[({"audio_provenance": {"source_sha256": value}}, {})
              for value in (None, "", "invalid", "g" * 64)],
        ]
        for fields, kwargs in variants:
            with self.subTest(fields=fields, kwargs=kwargs), tempfile.TemporaryDirectory() as directory:
                directory = Path(directory)
                audio = directory / "source.m4a"
                audio.write_bytes(b"other source e.g. bestaudio fixture")
                raw = dict(self.raw, **fields)
                with self.assertRaises(ValueError):
                    self.run_render(directory, raw=raw, audio_path=audio, **kwargs)
                self.assertFalse((directory / "output").exists())

    def test_recorded_audio_hash_requires_an_existing_audio_file(self):
        self.raw["audio_provenance"] = {"source_sha256": "a" * 64}
        for missing_path in (None, "absent.m4a"):
            with self.subTest(missing_path=missing_path), tempfile.TemporaryDirectory() as directory:
                directory = Path(directory)
                audio_path = None if missing_path is None else directory / missing_path
                with self.assertRaisesRegex(ValueError, "audio file is required"):
                    self.run_render(directory, audio_path=audio_path)
                self.assertFalse((directory / "output").exists())

    def test_legacy_json_without_recorded_provider_or_audio_hash_remains_compatible(self):
        with tempfile.TemporaryDirectory() as directory:
            report, data, _ = self.run_render(directory)
        self.assertNotIn("provider", self.raw)
        self.assertNotIn("audio_provenance", self.raw)
        self.assertEqual(data["metadata"]["asr_provider"], "openai-whisper")
        self.assertIsNone(data["metadata"]["audio_provenance"])
        self.assertTrue(report["accounting"]["all_text_preserved_exactly"])

    def test_model_language_and_top_level_disagreements_are_explicit(self):
        self.raw["language"] = "en"
        self.raw["text"] = "different top-level text"
        with tempfile.TemporaryDirectory() as directory:
            directory = Path(directory)
            source = directory / "source.json"
            source.write_text(json.dumps(self.raw))
            report = render.render_video(self.video, source, directory / "output")
        kinds = {item["kind"] for item in report["advisories"]}
        self.assertTrue({"model_not_recorded", "unexpected_or_missing_language",
                         "top_level_text_mismatch"}.issubset(kinds))

    def test_multipart_or_path_like_identifiers_cannot_be_misattributed(self):
        for video in (dict(self.video, bvid="../../outside"),
                      dict(self.video, parts=[{"cid": 1}, {"cid": 2}]),
                      dict(self.video, cid=True), dict(self.video, duration=0, playback_duration=0)):
            with self.subTest(video=video), tempfile.TemporaryDirectory() as directory:
                with self.assertRaises(ValueError):
                    self.run_render(directory, video=video)
                self.assertFalse((Path(directory) / "output/transcript.zh-CN.md").exists())

    def test_cli_reports_missing_source_as_failure_and_does_not_create_transcript(self):
        with tempfile.TemporaryDirectory() as directory:
            directory = Path(directory)
            inventory = directory / "inventory.json"
            inventory.write_text(json.dumps({"videos": [self.video]}))
            stream = io.StringIO()
            with contextlib.redirect_stdout(stream):
                status = render.main(["--inventory", str(inventory), "--asr-root", str(directory / "asr"),
                                      "--output-root", str(directory / "output"), "--model", "turbo"])
            self.assertEqual(status, 1)
            self.assertEqual(json.loads(stream.getvalue())["status"], "failed")
            self.assertFalse((directory / "output").exists())

    def test_cli_provider_and_model_are_used_in_artifact_metadata(self):
        with tempfile.TemporaryDirectory() as directory:
            directory = Path(directory)
            inventory = directory / "inventory.json"
            inventory.write_text(json.dumps({"videos": [self.video]}))
            asr_dir = directory / "asr" / self.video["bvid"]
            asr_dir.mkdir(parents=True)
            (asr_dir / "source.json").write_text(json.dumps(self.raw))
            with contextlib.redirect_stdout(io.StringIO()):
                status = render.main(["--inventory", str(inventory), "--asr-root", str(directory / "asr"),
                                      "--output-root", str(directory / "output"), "--provider", "qwen-asr",
                                      "--model", "Qwen/Qwen3-ASR-1.7B"])
            self.assertEqual(status, 0)
            report = json.loads((directory / "output" / self.video["bvid"] / "validation.json").read_text())
            self.assertEqual(report["metadata"]["asr_provider"], "qwen-asr")
            self.assertEqual(report["metadata"]["asr_model"], "Qwen/Qwen3-ASR-1.7B")


if __name__ == "__main__":
    unittest.main()
