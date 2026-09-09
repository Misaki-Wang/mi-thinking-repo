"""Reader packaging protects original pages and exact transcript/source identity."""
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest

SPEC = importlib.util.spec_from_file_location("build_sync_reader", Path(__file__).resolve().parents[1] / "scripts/build_sync_reader.py")
reader = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(reader)


class ReaderBuildTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.course = self.root / "course/mit-mmai-2026"
        self.source = self.root / "reader/mit-mmai-2026"
        self.output = self.root / "docs"
        self.output.mkdir()
        (self.output / "index.html").write_bytes(b"existing homepage unchanged")
        for name in ("index.html", "reader.js", "reader.css"):
            path = self.root / "reader/app" / name
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text("app fixture", encoding="utf-8")
        self.json(self.course / "catalog.json", {"title": "Test course", "sessions": [{"id": "w01-1", "title": "Intro", "video_url": "https://youtu.be/abcdefghijk"}]})
        artifacts = {}
        for name, body in (("transcript.en.md", "CLIP compares x &gt; 1."), ("transcript.zh-CN.md", "CLIP 比较 x &gt; 1。")):
            path = self.course / "w01-1" / name
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(f"# Lecture\n\n### [00:01](https://www.youtube.com/watch?v=abcdefghijk&t=1s) · b000001\n\n{body}\n", encoding="utf-8")
            artifacts[name] = {"sha256": reader.digest(path)}
        self.json(self.course / "transcript-status.json", {"sessions": [{"session_id": "w01-1", "video_id": "abcdefghijk", "public_transcripts": True, "artifacts": artifacts}]})
        image = self.source / "slides/w01-1-p001.webp"
        image.parent.mkdir(parents=True, exist_ok=True)
        image.write_bytes(b"fixture-image")
        self.index = {"decks": [{"id": "w01-1", "title": "Intro", "source_url": "https://example.com/slides.pdf", "pages": [{"page": 1, "image": "slides/w01-1-p001.webp", "sha256": reader.digest(image), "width": 1280, "height": 720, "source_url": "https://example.com/slides.pdf#page=1", "text_excerpt": "Test diagram"}]}]}
        self.json(self.source / "slides-index.json", self.index)
        self.alignment = {"session_id": "w01-1", "deck_ids": ["w01-1"], "method": {"id": "test"}, "provenance": {"english_markdown_sha256": artifacts["transcript.en.md"]["sha256"]}, "blocks": [{"block_id": "b000001", "start_ms": 1120, "end_ms": 2200, "slide_id": "w01-1-p001", "confidence": "estimated", "score": 0.4, "candidates": []}]}
        self.json(self.source / "alignments/w01-1.json", self.alignment)

    def json(self, path, data):
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(data), encoding="utf-8")

    def build(self):
        return reader.build(self.root, self.output)

    def lesson(self):
        return json.loads((self.output / "reader/mit-mmai-2026/data/w01-1.json").read_text())

    def test_additive_build_exact_text_and_reverse_mapping(self):
        result = self.build()
        self.assertEqual((self.output / "index.html").read_bytes(), b"existing homepage unchanged")
        self.assertEqual(result["blocks"], 1)
        lesson = self.lesson()
        self.assertEqual(lesson["blocks"][0]["en"], "CLIP compares x > 1.")
        self.assertEqual(lesson["blocks"][0]["start_ms"], 1120)
        self.assertEqual(lesson["slides"][0]["block_ids"], ["b000001"])
        self.assertNotIn(".work", json.dumps(lesson))
        self.assertEqual((self.output / "reader/mit-mmai-2026/slides-index.json").read_bytes(), (self.source / "slides-index.json").read_bytes())

    def test_unmatched_does_not_invent_reverse_association(self):
        self.alignment["blocks"][0].update(slide_id=None, confidence="unmatched")
        self.json(self.source / "alignments/w01-1.json", self.alignment)
        self.build()
        self.assertEqual(self.lesson()["slides"][0]["block_ids"], [])
        self.assertIsNone(self.lesson()["blocks"][0]["slide_id"])

    def test_hash_or_timestamp_drift_fails(self):
        for mutate in ("time", "hash"):
            with self.subTest(mutate=mutate):
                data = json.loads(json.dumps(self.alignment))
                if mutate == "time":
                    data["blocks"][0]["start_ms"] = 900
                else:
                    data["provenance"]["english_markdown_sha256"] = "bad"
                self.json(self.source / "alignments/w01-1.json", data)
                with self.assertRaises(ValueError):
                    self.build()

    def test_outside_source_assets_and_damaged_images_fail(self):
        for image in ("../secret.webp", "slides/w01-1-p001.webp"):
            with self.subTest(image=image):
                data = json.loads(json.dumps(self.index))
                data["decks"][0]["pages"][0].update(image=image, sha256="damaged")
                self.json(self.source / "slides-index.json", data)
                with self.assertRaises(ValueError):
                    self.build()

    def test_editorial_override_is_evidenced_and_updates_reverse_mapping(self):
        self.json(self.source / "alignment-review.json", {"overrides": [{"session_id": "w01-1", "block_id": "b000001", "slide_id": None, "reason": "Speech is not represented in this deck"}]})
        self.build()
        self.assertEqual(self.lesson()["blocks"][0]["match_source"], "editorial_text_review")
        self.assertEqual(self.lesson()["slides"][0]["block_ids"], [])
        self.json(self.source / "alignment-review.json", {"overrides": [{"session_id": "w01-1", "block_id": "unknown", "slide_id": None, "reason": "Unknown paragraph"}]})
        with self.assertRaises(ValueError):
            self.build()

    def test_output_symlinks_cannot_overwrite_outside_files(self):
        outside = self.root / "outside"
        outside.mkdir()
        destination = self.output / "reader/mit-mmai-2026"
        destination.mkdir(parents=True)
        (destination / "slides").symlink_to(outside, target_is_directory=True)
        with self.assertRaises(ValueError):
            self.build()
        self.assertEqual(list(outside.iterdir()), [])


if __name__ == "__main__":
    unittest.main()
