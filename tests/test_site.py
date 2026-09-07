"""Behavioral tests for the zero-dependency site builder."""

import importlib.util
import json
from pathlib import Path, PurePosixPath
import shutil
import tempfile
import unittest

REPO = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("build_site", REPO / "scripts/build_site.py")
site = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(site)


class MarkdownTests(unittest.TestCase):
    def render(self, content):
        return site.Markdown(PurePosixPath("course/demo/w01-1/preview.md"), "/notebook/").render(content)

    def test_active_html_and_urls_are_inert(self):
        result = self.render('# Title <script>alert(1)</script>\n\n<img src=x onerror=alert(1)>\n\n[bad](javascript:alert(1)) [bad2](data:text/html,test) [encoded](jav&#97;script:alert(1))')
        self.assertNotIn("<script>", result)
        self.assertNotIn("<img", result)
        self.assertNotIn('href="javascript:', result)
        self.assertNotIn('href="data:', result)
        self.assertIn("&lt;script&gt;", result)

    def test_relative_documents_readme_and_fragments(self):
        result = self.render('[next](../w01-2/preview.md#核心概念) [overview](../README.md) [guide](../GUIDANCE.md)')
        self.assertIn('/notebook/course/demo/w01-2/preview.html#核心概念', result)
        self.assertIn('/notebook/course/demo/index.html', result)
        self.assertIn('/notebook/course/demo/GUIDANCE.html', result)

    def test_nested_parentheses_links_escaping_and_inline(self):
        result = self.render('[paper](https://example.com/a_(b)?x=1&y=2) **focus** `a < b`')
        self.assertIn('href="https://example.com/a_(b)?x=1&amp;y=2"', result)
        self.assertIn("<strong>focus</strong>", result)
        self.assertIn("<code>a &lt; b</code>", result)

    def test_tables_nested_lists_code_and_duplicate_headings(self):
        result = self.render('# T\n\n## 核心概念\n\n## 核心概念\n\n| Name | Value |\n| --- | --- |\n| **A** | 1 |\n\n- parent\n  - child\n- second\n\n```html\n<script>unsafe()</script>\n```')
        self.assertIn('id="核心概念"', result)
        self.assertIn('id="核心概念-1"', result)
        self.assertIn("<table>", result)
        self.assertIn("<th>Name</th>", result)
        self.assertIn("<td><strong>A</strong></td>", result)
        self.assertIn("<ul><li>\nparent\n<ul><li>\nchild", result)
        self.assertIn("&lt;script&gt;unsafe()&lt;/script&gt;", result)

    def test_url_boundaries(self):
        source = PurePosixPath("README.md")
        for url in ("//evil.test", "../../../secret.md", ".work/log.md", "https:\n//evil.test"):
            self.assertIsNone(site.safe_link(url, source, "/"), url)
        self.assertEqual(site.safe_link("https://example.com", source, "/"), "https://example.com")
        with self.assertRaises(ValueError):
            site.normalize_base("https://example.com/")
        with self.assertRaises(ValueError):
            site.normalize_base("../private")


class BuildTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.root = Path(self.temporary.name).resolve()
        shutil.copytree(REPO / "assets", self.root / "assets")
        self.write("README.md", "# Notebook\n\n[Course](course/demo/README.md)\n")
        self.write("course/demo/README.md", "# Demo course\n\n[Guidance](GUIDANCE.md)\n")
        self.write("course/demo/GUIDANCE.md", "# 学习指南\n\n## 学习路径\n\n[第一课](w01-1/preview.md#核心概念)\n")
        self.write("course/demo/w01-1/preview.md", "# 课程一\n\n## 核心概念\n\n融合 representation。\n\n[Readings](readings.md)\n")
        self.write("course/demo/w01-1/readings.md", "# 阅读指引\n\n**Evidence** from the paper.\n")
        self.write("blog/README.md", "# Blog\n")
        self.write("paper/README.md", "# Paper\n")
        self.write("course/demo/catalog.json", json.dumps({"title": "Demo course", "source_url": "https://example.com/course", "sessions": [
            {"id": "w01-1", "date": "2026-02-03", "title": "Representation", "topics": ["Fusion"], "video_url": "https://youtube.com/watch?v=example", "slides_url": "https://example.com/broken.pdf", "slides_resolved_url": "https://example.com/fixed.pdf", "instructional": True},
            {"id": "w02-1", "title": "No materials", "instructional": True},
            {"id": "break", "title": "Holiday", "instructional": False}
        ]}))

    def tearDown(self):
        self.temporary.cleanup()

    def write(self, name, text):
        path = self.root / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")

    def build(self, base="/notebook/"):
        report = site.Site(self.root, self.root / "docs", base).build()
        return report, self.root / "docs"

    def test_complete_build_rewrites_links_and_indexes_text(self):
        report, output = self.build()
        self.assertEqual(report["documents"], 7)
        self.assertEqual(site.validate_links(output, "/notebook/"), [])
        page = (output / "course/demo/w01-1/preview.html").read_text()
        self.assertIn('/notebook/assets/site.css', page)
        self.assertIn('href="https://example.com/fixed.pdf"', page)
        self.assertNotIn('href="https://example.com/broken.pdf"', page)
        index = json.loads((output / "search-index.json").read_text())
        self.assertTrue(any("融合 representation" in item["text"] for item in index))
        self.assertTrue(any("核心概念" in item["headings"] for item in index))
        self.assertTrue((output / "markdown/course/demo/w01-1/preview.md").is_file())

    def test_root_base_and_subpath_both_work(self):
        _, output = self.build("/")
        self.assertEqual(site.validate_links(output, "/"), [])
        self.assertIn('href="/assets/site.css"', (output / "index.html").read_text())
        _, output = self.build("/mi-thinking-repo/")
        self.assertEqual(site.validate_links(output, "/mi-thinking-repo/"), [])

    def test_unavailable_slides_have_no_toolbar_button_but_keep_provenance(self):
        self.write("course/demo/w01-1/readings.md", "# 阅读指引\n\n[原始来源（已失效）](https://example.com/broken.pdf)")
        catalog_path = self.root / "course/demo/catalog.json"
        catalog = json.loads(catalog_path.read_text())
        for state in ("unavailable", "missing", "failed"):
            with self.subTest(slides_status=state):
                catalog["sessions"][0]["slides_status"] = state
                self.write("course/demo/catalog.json", json.dumps(catalog))
                _, output = self.build()
                page = (output / "course/demo/w01-1/readings.html").read_text()
                toolbar = page.split('<div class="document-tools">', 1)[1].split("</div>", 1)[0]
                self.assertNotIn("Slides ↗", toolbar)
                self.assertIn("Video ↗", toolbar)
                self.assertIn('href="https://example.com/broken.pdf"', page)
        catalog["sessions"][0]["slides_status"] = "acquired"
        self.write("course/demo/catalog.json", json.dumps(catalog))
        _, output = self.build()
        page = (output / "course/demo/w01-1/readings.html").read_text()
        self.assertIn('href="https://example.com/fixed.pdf">Slides ↗', page)

    def test_public_copy_distinguishes_preparation_and_published_material(self):
        self.write("course/demo/w02-1/preview.md", "# 学习准备\n\n本章节资料尚未公开。")
        catalog_path = self.root / "course/demo/catalog.json"
        catalog = json.loads(catalog_path.read_text())
        catalog["description"] = "Personal study archive catalog; internal metadata."
        self.write("course/demo/catalog.json", json.dumps(catalog))
        _, output = self.build()
        home = (output / "index.html").read_text()
        course = (output / "course/demo/index.html").read_text()
        self.assertIn("课程预览 · Readings 指引 · 术语表", home)
        self.assertNotIn("中英讲稿", home)
        self.assertNotIn("Personal study archive catalog", course)
        self.assertIn("结合课堂材料与论文", course)
        self.assertIn("章节入口", course)
        self.assertIn("资料待补充 · 学习准备", course)
        missing_card = course.split('id="session-w02-1"', 1)[1].split("</article>", 1)[0]
        self.assertNotIn("按公开资料整理", missing_card)
        self.assertNotIn("开始预览", missing_card)

    def test_raw_material_and_unapproved_transcripts_are_not_exported(self):
        self.write(".work/transcripts/private.md", "private transcript")
        self.write(".env", "private-secret")
        self.write("course/demo/.work/note.md", "hidden nested note")
        self.write("course/demo/w01-1/transcript.en.md", "# Full transcript\nprivate-transcript-text")
        self.write("course/demo/w01-1/audio.wav", "raw-audio")
        report, output = self.build()
        self.assertEqual(report["documents"], 7)
        all_text = "\n".join(path.read_text() for path in output.rglob("*") if path.is_file())
        for secret in ("private-secret", "private-transcript-text", "raw-audio", "hidden nested note"):
            self.assertNotIn(secret, all_text)
        self.assertFalse(any("transcript.en" in name for name in report["files"]))

    def test_explicit_per_session_transcript_publication_and_stale_cleanup(self):
        self.write("course/demo/w01-1/transcript.en.md", "# Full transcript\nPublished speech.")
        self.write("course/demo/transcript-status.json", json.dumps({"sessions": [{"session_id": "w01-1", "public_transcripts": True}]}))
        _, output = self.build()
        self.assertTrue((output / "course/demo/w01-1/transcript.en.html").is_file())
        self.assertIn("英文讲稿", (output / "course/demo/w01-1/preview.html").read_text())
        self.write("course/demo/transcript-status.json", json.dumps({"sessions": [{"session_id": "w01-1", "public_transcripts": False}]}))
        _, output = self.build()
        self.assertFalse((output / "course/demo/w01-1/transcript.en.html").exists())
        self.assertFalse((output / "markdown/course/demo/w01-1/transcript.en.md").exists())

    def test_blog_auto_listing_empty_paper_and_no_fake_posts(self):
        self.write("blog/first-thought.md", "# 一个真实的问题\n\nPersonal observation.")
        _, output = self.build()
        blog = (output / "blog/index.html").read_text()
        paper = (output / "paper/index.html").read_text()
        self.assertIn("一个真实的问题", blog)
        self.assertIn('/notebook/blog/first-thought.html', blog)
        self.assertIn("尚未发布独立笔记", paper)
        self.assertNotIn("note-card", paper)

    def test_missing_local_document_fails_build(self):
        self.write("course/demo/w01-1/readings.md", "# Reading\n\n[Missing](not-here.md)")
        with self.assertRaisesRegex(ValueError, "Broken local links"):
            self.build()

    def test_missing_heading_fails_build(self):
        self.write("course/demo/w01-1/readings.md", "# Reading\n\n[Missing anchor](preview.md#not-here)")
        with self.assertRaisesRegex(ValueError, "missing anchor"):
            self.build()


if __name__ == "__main__":
    unittest.main()
