"""Catch missing, displaced, truncated, and mislinked transcript content."""

import importlib.util
from pathlib import Path
import tempfile
import unittest

SPEC = importlib.util.spec_from_file_location("check_transcripts", Path(__file__).resolve().parents[1] / "scripts/check_transcripts.py")
check = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(check)


class TranscriptAuditTests(unittest.TestCase):
    def setUp(self):
        self.en = [
            {"block_id": "b000001", "start_ms": 1200, "end_ms": 2000, "text": "CLIP compares an image and text."},
            {"block_id": "b000002", "start_ms": 2000, "end_ms": 3000, "text": "This is not a lossless representation."},
        ]
        self.zh = [
            {"block_id": "b000001", "text": "CLIP 比较图像与文本。"},
            {"block_id": "b000002", "text": "这不是无损表示。"},
        ]

    def test_complete_translation_without_duplicate_times_passes(self):
        self.assertEqual(check.audit_blocks(self.en, self.zh)["errors"], [])

    def test_missing_reordered_duplicate_and_empty_are_failures(self):
        for translation in (self.zh[:1], list(reversed(self.zh)), [self.zh[0], self.zh[0]], [self.zh[0], {"block_id": "b000002", "text": "   "}]):
            with self.subTest(translation=translation):
                self.assertTrue(check.audit_blocks(self.en, translation)["errors"])

    def test_bad_time_and_translated_time_drift_are_failures(self):
        for key, value in (("start_ms", -1), ("end_ms", 0), ("start_ms", 1200.5)):
            altered = [dict(self.en[0], **{key: value}), self.en[1]]
            self.assertTrue(check.audit_blocks(altered, self.zh)["errors"])
        altered = [dict(self.zh[0], start_ms=1300), self.zh[1]]
        self.assertTrue(check.audit_blocks(self.en, altered)["errors"])

    def test_compression_and_missing_technical_names_are_advisory(self):
        self.en[0]["text"] = "CLIP uses 512 dimensions and LoRA adapters. " * 15
        self.zh[0]["text"] = "这里介绍图文模型。"
        report = check.audit_blocks(self.en, self.zh)
        self.assertFalse(report["errors"])
        kinds = {item["kind"] for item in report["advisories"]}
        self.assertEqual(kinds, {"possible_compression", "technical_names", "numbers"})

    def test_raw_english_copy_is_not_a_chinese_translation(self):
        self.en[0]["text"] = "This is a long passage about machine learning. " * 12
        self.zh[0]["text"] = self.en[0]["text"]
        self.assertTrue(check.audit_blocks(self.en, self.zh)["errors"])

    def test_numbers_next_to_chinese_characters_are_retained(self):
        self.en[0]["text"] = "Use 512 dimensions and a rate of 0.25."
        self.zh[0]["text"] = "使用512维，速率为0.25。"
        self.assertFalse(check.audit_blocks(self.en, self.zh)["advisories"])

    def test_method_moved_to_neighboring_timestamp_is_flagged_for_review(self):
        self.en[0]["text"] = "You will implement early fusion in your"
        self.en[1]["text"] = "homework. Any questions?"
        self.zh[0]["text"] = "你们会在"
        self.zh[1]["text"] = "作业中实现 early fusion。有什么问题吗？"
        advisory = check.audit_blocks(self.en, self.zh)["advisories"]
        self.assertTrue(any(item["kind"] == "possible_boundary_shift" and item["translated_in"] == "b000002" for item in advisory))

    def test_published_content_and_links_are_verified_beyond_counts(self):
        video_id = "abcdefghijk"
        with tempfile.TemporaryDirectory() as temporary:
            directory = Path(temporary)
            for name in check.ARTIFACTS:
                parts = ["# Lecture\n"]
                for en, zh in zip(self.en, self.zh):
                    parts.append(f"### [00:01](https://www.youtube.com/watch?v={video_id}&t={en['start_ms'] // 1000}s) · {en['block_id']}\n\n")
                    if name != "transcript.zh-CN.md":
                        parts.append(en["text"] + "\n\n")
                    if name != "transcript.en.md":
                        parts.append(zh["text"] + "\n\n")
                (directory / name).write_text("".join(parts), encoding="utf-8")
            self.assertFalse(check.audit_artifacts(directory, self.en, self.zh, video_id)["errors"])
            target = directory / "transcript.zh-CN.md"
            original = target.read_text()
            target.write_text(original.replace("这不是无损表示。", "这是无损表示。"))
            self.assertTrue(check.audit_artifacts(directory, self.en, self.zh, video_id)["errors"])
            target.write_text(original.replace("&t=2s", "&t=99s"))
            self.assertTrue(check.audit_artifacts(directory, self.en, self.zh, video_id)["errors"])

    def test_markdown_escaping_is_not_reported_as_semantic_change(self):
        self.en = [{"block_id": "b000001", "start_ms": 0, "end_ms": 2000, "text": r"x_1 < 2 & [value] \alpha"}]
        self.zh = [{"block_id": "b000001", "text": r"变量 x_1 < 2 & [value] \alpha"}]
        with tempfile.TemporaryDirectory() as temporary:
            directory = Path(temporary)
            for name in check.ARTIFACTS:
                content = "# Lecture\n\n### [00:00](https://www.youtube.com/watch?v=abcdefghijk&t=0s) · b000001\n\n"
                content += r"x\_1 &lt; 2 &amp; \[value\] \\alpha" + "\n\n"
                content += r"变量 x\_1 &lt; 2 &amp; \[value\] \\alpha" + "\n"
                (directory / name).write_text(content)
            self.assertFalse(check.audit_artifacts(directory, self.en, self.zh, "abcdefghijk")["errors"])


if __name__ == "__main__":
    unittest.main()
