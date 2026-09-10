"""Behavioral tests for the zero-dependency site builder."""

import importlib.util
import hashlib
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

    def test_text_entities_are_decoded_once_and_remain_inert(self):
        result = self.render("&gt;&gt; Speaker &amp; guest. &#62; &#x3e; &lt;script&gt;unsafe()&lt;/script&gt; &amp;lt;script&amp;gt;")
        self.assertIn("&gt;&gt; Speaker &amp; guest.", result)
        self.assertNotIn("&amp;gt;&amp;gt; Speaker", result)
        self.assertIn("&lt;script&gt;unsafe()&lt;/script&gt;", result)
        self.assertNotIn("<script>", result)
        self.assertIn("&amp;lt;script&amp;gt;", result)

    def test_underscore_emphasis_preserves_identifiers_math_and_code(self):
        result = self.render(r"_Bilingual transcript · 双语讲稿_ __bold__ foo_bar_baz x_i + y_j $x_i + \alpha_j$ $_i_ + x_{j}$ `_code_ &gt;`" + "\n\n```text\n_emphasis_ &gt;\n```")
        self.assertIn("<em>Bilingual transcript · 双语讲稿</em>", result)
        self.assertIn("<strong>bold</strong>", result)
        self.assertIn("foo_bar_baz x_i + y_j", result)
        self.assertIn(r"$x_i + \alpha_j$ $_i_ + x_{j}$", result)
        self.assertIn("<code>_code_ &amp;gt;</code>", result)
        self.assertIn('_emphasis_ &amp;gt;', result)

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

    def test_transcript_cards_tabs_and_counts_follow_allowed_existing_files(self):
        self.write("course/demo/transcript-status.json", json.dumps({"sessions": [{"session_id": "w01-1", "public_transcripts": True}]}))
        self.write("course/demo/w01-1/transcript.en.md", "# English transcript\n\nComplete English text.")
        _, output = self.build()
        course = (output / "course/demo/index.html").read_text()
        self.assertIn("英文 1 讲 · 中文 0 讲 · 双语 0 讲", course)
        self.assertIn("英文讲稿已归档", course)
        self.assertNotIn("transcript.bilingual.html", course)
        self.assertNotIn("transcript.zh-CN.html", course)

        self.write("course/demo/w01-1/transcript.zh-CN.md", "# 中文讲稿\n\n完整的中文译文。")
        self.write("course/demo/w01-1/transcript.bilingual.md", "# 双语讲稿\n\nComplete English text.\n\n完整的中文译文。")
        _, output = self.build()
        course = (output / "course/demo/index.html").read_text()
        self.assertIn("英文 1 讲 · 中文 1 讲 · 双语 1 讲", course)
        for name, label in site.TRANSCRIPT_FORMATS:
            target = f'/notebook/course/demo/w01-1/{name[:-3]}.html'
            self.assertIn(f'href="{target}">{label}讲稿 ↗', course)
            page = (output / f"course/demo/w01-1/{name[:-3]}.html").read_text()
            tabs = page.split('<nav class="document-tabs"', 1)[1].split("</nav>", 1)[0]
            for tab_name, tab_label in site.TRANSCRIPT_FORMATS:
                self.assertIn(tab_name[:-3] + ".html", tabs)
                self.assertIn(tab_label + "讲稿", tabs)
            self.assertIn('class="prose transcript-prose"', page)
        self.assertEqual(site.validate_links(output, "/notebook/"), [])

        self.write("course/demo/transcript-status.json", json.dumps({"sessions": [{"session_id": "w01-1", "public_transcripts": False}]}))
        _, output = self.build()
        course = (output / "course/demo/index.html").read_text()
        preview = (output / "course/demo/w01-1/preview.html").read_text()
        self.assertNotIn("已公开讲稿", course)
        for name, _ in site.TRANSCRIPT_FORMATS:
            self.assertNotIn(name[:-3] + ".html", course)
            self.assertNotIn(name[:-3] + ".html", preview)

    def test_long_transcript_is_fully_searchable_and_html_escaped(self):
        content = "English and 中文 multimodal details. " * 4000 + "末尾的独特检索词 <script>unsafe()</script>"
        self.write("course/demo/w01-1/transcript.bilingual.md", "# 双语讲稿\n\n" + content)
        self.write("course/demo/transcript-status.json", json.dumps({"sessions": [{"session_id": "w01-1", "public_transcripts": True}]}))
        _, output = self.build()
        index = json.loads((output / "search-index.json").read_text())
        transcript = next(item for item in index if item["kind"] == "双语讲稿")
        self.assertGreater(len(transcript["text"]), 100000)
        self.assertIn("末尾的独特检索词", transcript["text"])
        page = (output / "course/demo/w01-1/transcript.bilingual.html").read_text()
        self.assertNotIn("<script>unsafe()", page)
        self.assertIn("&lt;script&gt;unsafe()&lt;/script&gt;", page)

    def test_transcript_metadata_is_collapsed_without_changing_markdown_or_notes(self):
        content = "# Transcript\n\n_Bilingual transcript · 双语讲稿_\n\n- Channel: Teacher\n- Source: [Video](https://example.com/video)\n- Status: complete\n\n## Transcript · 讲稿\n\n&gt;&gt; First aligned passage."
        self.write("course/demo/w01-1/transcript.bilingual.md", content)
        self.write("course/demo/w01-1/readings.md", content)
        self.write("course/demo/transcript-status.json", json.dumps({"sessions": [{"session_id": "w01-1", "public_transcripts": True}]}))
        _, output = self.build()
        page = (output / "course/demo/w01-1/transcript.bilingual.html").read_text()
        self.assertIn('<details class="transcript-metadata"><summary>讲稿来源与处理信息</summary>', page)
        self.assertNotIn('<details class="transcript-metadata" open', page)
        metadata = page.split('<details class="transcript-metadata">', 1)[1].split("</details>", 1)[0]
        self.assertIn("Channel: Teacher", metadata)
        self.assertNotIn("First aligned passage", metadata)
        self.assertIn("&gt;&gt; First aligned passage", page)
        self.assertNotIn("&amp;gt;", page)
        self.assertNotIn('class="transcript-metadata"', (output / "course/demo/w01-1/readings.html").read_text())
        self.assertEqual((output / "markdown/course/demo/w01-1/transcript.bilingual.md").read_text(), content)

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

    def video_fixture(self):
        self.write("video/README.md", "# Video\n\n[创作者视频](bilibili-280780745/README.md)\n")
        self.write("video/bilibili-280780745/README.md", "# 创作者视频\n\n[本期预览](BV1KZ8X6uEPL/preview.md)\n")
        self.write("video/bilibili-280780745/BV1KZ8X6uEPL/preview.md", "# 本期视频预览\n\n原创学习笔记，保留 MoE 专业术语。\n")
        transcript = "# 中文讲稿\n\n## 00:00\n\n视频讲稿的独特检索词 <script>unsafe()</script>。\n"
        self.write("video/bilibili-280780745/BV1KZ8X6uEPL/transcript.zh-CN.md", transcript)
        return {
            "publication_authorized": True,
            "videos": [{"bvid": "BV1KZ8X6uEPL", "public_transcripts": True,
                        "transcript_sha256": hashlib.sha256(transcript.encode()).hexdigest()}],
        }

    def test_video_without_root_readme_preserves_baseline_bytes(self):
        _, output = self.build()
        before = {str(path.relative_to(output)): path.read_bytes() for path in output.rglob("*") if path.is_file()}
        aggregate = hashlib.sha256()
        for name, content in sorted(before.items()):
            aggregate.update(name.encode())
            aggregate.update(b"\0")
            aggregate.update(content)
            aggregate.update(b"\0")
        # Captured from the existing site builder before video support was added.
        self.assertEqual(aggregate.hexdigest(), "87a20c85f5d8b241ca4dfa4262821ca27ae4ffabaff30e7efa153678b53578cc")
        self.write("video/unlisted/README.md", "# Not enabled\n")
        self.write("video/unlisted/BV1KZ8X6uEPL/transcript.zh-CN.md", "Unlisted transcript.")
        _, output = self.build()
        after = {str(path.relative_to(output)): path.read_bytes() for path in output.rglob("*") if path.is_file()}
        self.assertEqual(after, before)
        self.assertNotIn("video/index.html", (output / "index.html").read_text())

    def test_video_transcripts_withheld_by_default_and_both_permission_flags(self):
        manifest = self.video_fixture()
        self.write("video/bilibili-280780745/BV1KZ8X6uEPL/transcript.draft.md", "PRIVATE DRAFT")
        self.write("video/bilibili-280780745/BV1KZ8X6uEPL/audio.wav", "PRIVATE AUDIO")
        self.write("video/bilibili-280780745/.work/raw.md", "PRIVATE RAW")
        for authorization, public in ((None, None), (False, True), (True, False), ("true", True), (True, "true")):
            with self.subTest(authorization=authorization, public=public):
                manifest["publication_authorized"] = authorization
                manifest["videos"][0]["public_transcripts"] = public
                if authorization is not None:
                    self.write("video/bilibili-280780745/manifest.json", json.dumps(manifest))
                _, output = self.build()
                all_text = "\n".join(path.read_text() for path in output.rglob("*") if path.is_file())
                for secret in ("视频讲稿的独特检索词", "PRIVATE DRAFT", "PRIVATE AUDIO", "PRIVATE RAW"):
                    self.assertNotIn(secret, all_text)
                self.assertIn("原创学习笔记", all_text)
                self.assertTrue((output / "video/index.html").is_file())
                self.assertFalse((output / "video/bilibili-280780745/BV1KZ8X6uEPL/transcript.zh-CN.html").exists())

    def test_authorized_video_is_searchable_downloadable_and_not_a_course(self):
        manifest = self.video_fixture()
        self.write("video/bilibili-280780745/manifest.json", json.dumps(manifest))
        self.write("video/bilibili-280780745/BV1KZ8X6uEPL/transcript.en.md", "UNLISTED FORMAT")
        _, output = self.build()
        page = (output / "video/bilibili-280780745/BV1KZ8X6uEPL/transcript.zh-CN.html").read_text()
        self.assertIn('/notebook/video/index.html', page)
        self.assertIn('/notebook/video/bilibili-280780745/index.html', page)
        self.assertIn('aria-label="本期视频材料"', page)
        self.assertIn("视频预览", page)
        self.assertNotIn("MMAI 2026", page)
        self.assertNotIn("课程预览", page.split('<main id="main">', 1)[1].split("</main>", 1)[0])
        self.assertNotIn("<script>unsafe()", page)
        self.assertIn("&lt;script&gt;unsafe()&lt;/script&gt;", page)
        self.assertNotIn("UNLISTED FORMAT", page)
        self.assertFalse((output / "video/bilibili-280780745/BV1KZ8X6uEPL/transcript.en.html").exists())
        download = output / "markdown/video/bilibili-280780745/BV1KZ8X6uEPL/transcript.zh-CN.md"
        self.assertEqual(download.read_bytes(), (self.root / "video/bilibili-280780745/BV1KZ8X6uEPL/transcript.zh-CN.md").read_bytes())
        index = json.loads((output / "search-index.json").read_text())
        self.assertTrue(any(item["kind"] == "中文讲稿" and "视频讲稿的独特检索词" in item["text"] for item in index))
        self.assertTrue(any(item["kind"] == "视频预览" for item in index))
        home = (output / "index.html").read_text()
        self.assertIn('>视频</a>', home)
        self.assertIn('03 / VIDEO', home)
        self.assertIn('/notebook/assets/video.css', home)
        self.assertTrue((output / "assets/video.css").is_file())
        self.assertEqual(site.validate_links(output, "/notebook/"), [])

    def test_public_video_hash_missing_file_and_unsafe_path_fail_closed(self):
        manifest = self.video_fixture()
        self.write("video/bilibili-280780745/manifest.json", json.dumps(manifest))
        self.write("video/bilibili-280780745/BV1KZ8X6uEPL/transcript.zh-CN.md", "Tampered source")
        with self.assertRaisesRegex(ValueError, "SHA-256 mismatch"):
            self.build()
        manifest["videos"][0]["transcript_sha256"] = "invalid"
        self.write("video/bilibili-280780745/manifest.json", json.dumps(manifest))
        with self.assertRaisesRegex(ValueError, "Missing or invalid video transcript SHA-256"):
            self.build()
        manifest["videos"][0].pop("transcript_sha256")
        self.write("video/bilibili-280780745/manifest.json", json.dumps(manifest))
        with self.assertRaisesRegex(ValueError, "Missing or invalid video transcript SHA-256"):
            self.build()
        manifest["videos"][0]["bvid"] = "../../private"
        self.write("video/bilibili-280780745/manifest.json", json.dumps(manifest))
        with self.assertRaisesRegex(ValueError, "Invalid or duplicate public video ID"):
            self.build()
        manifest["videos"][0]["bvid"] = "BV1KZ8X6uEPL"
        self.write("video/bilibili-280780745/manifest.json", json.dumps(manifest))
        transcript = self.root / "video/bilibili-280780745/BV1KZ8X6uEPL/transcript.zh-CN.md"
        transcript.unlink()
        with self.assertRaisesRegex(ValueError, "Missing or unsafe public video transcript"):
            self.build()
        transcript.symlink_to(self.root / "README.md")
        with self.assertRaisesRegex(ValueError, "Missing or unsafe public video transcript"):
            self.build()

    def test_video_publication_revocation_removes_html_downloads_and_search(self):
        manifest = self.video_fixture()
        self.write("video/bilibili-280780745/manifest.json", json.dumps(manifest))
        _, output = self.build()
        self.assertTrue((output / "video/bilibili-280780745/BV1KZ8X6uEPL/transcript.zh-CN.html").is_file())
        manifest["publication_authorized"] = False
        self.write("video/bilibili-280780745/manifest.json", json.dumps(manifest))
        _, output = self.build()
        self.assertFalse(any(path.name.startswith("transcript") for path in output.rglob("*")))
        self.assertNotIn("视频讲稿的独特检索词", (output / "search-index.json").read_text())
        (self.root / "video/README.md").unlink()
        _, output = self.build()
        self.assertFalse((output / "video/index.html").exists())
        self.assertFalse((output / "assets/video.css").exists())
        self.assertNotIn("video/index.html", (output / "index.html").read_text())

    def second_video_fixture(self):
        # Reuse the ID deliberately: publication must be scoped to the collection.
        self.write("video/README.md", "# Video\n\n[创作者视频](bilibili-280780745/README.md)\n\n[第二创作者](bilibili-508452265/README.md)\n")
        self.write("video/bilibili-508452265/README.md", "# 第二创作者测试集\n\n[第二期预览](BV1KZ8X6uEPL/preview.md)\n")
        self.write("video/bilibili-508452265/BV1KZ8X6uEPL/preview.md", "# 第二创作者预览\n\nSynthetic study notes.\n")
        transcript = "# 第二创作者中文讲稿\n\n## 00:00\n\n第二系列独有测试讲稿。\n"
        self.write("video/bilibili-508452265/BV1KZ8X6uEPL/transcript.zh-CN.md", transcript)
        return {
            "publication_authorized": True,
            "videos": [{"bvid": "BV1KZ8X6uEPL", "public_transcripts": True,
                        "transcript_sha256": hashlib.sha256(transcript.encode()).hexdigest()}],
        }

    def test_two_video_collections_require_independent_publication_permissions(self):
        manifests = {"bilibili-280780745": self.video_fixture(),
                     "bilibili-508452265": self.second_video_fixture()}
        permission_cases = ((True, True, False, True), (True, True, True, False),
                            (False, True, True, True), (True, False, True, True),
                            (True, True, True, True))
        for flags in permission_cases:
            with self.subTest(permissions=flags):
                for index, (collection, manifest) in enumerate(manifests.items()):
                    manifest["publication_authorized"] = flags[2 * index]
                    manifest["videos"][0]["public_transcripts"] = flags[2 * index + 1]
                    self.write(f"video/{collection}/manifest.json", json.dumps(manifest))
                _, output = self.build()
                search = json.loads((output / "search-index.json").read_text())
                for index, collection in enumerate(manifests):
                    public = flags[2 * index] and flags[2 * index + 1]
                    relative = f"video/{collection}/BV1KZ8X6uEPL/transcript.zh-CN"
                    self.assertEqual((output / f"{relative}.html").is_file(), public)
                    self.assertEqual((output / f"markdown/{relative}.md").is_file(), public)
                    self.assertEqual(any(item["url"] == f"/notebook/{relative}.html" for item in search), public)
                self.assertEqual(site.validate_links(output, "/notebook/"), [])

    def test_two_video_collections_cannot_borrow_each_others_transcript_hash(self):
        manifests = {"bilibili-280780745": self.video_fixture(),
                     "bilibili-508452265": self.second_video_fixture()}
        hashes = {collection: manifest["videos"][0]["transcript_sha256"] for collection, manifest in manifests.items()}
        for collection, manifest in manifests.items():
            self.write(f"video/{collection}/manifest.json", json.dumps(manifest))
        _, output = self.build()
        published = {str(path.relative_to(output)): path.read_bytes() for path in output.rglob("*") if path.is_file()}
        for collection, manifest in manifests.items():
            with self.subTest(tampered_collection=collection):
                other_collection = next(name for name in manifests if name != collection)
                manifest["videos"][0]["transcript_sha256"] = hashes[other_collection]
                self.write(f"video/{collection}/manifest.json", json.dumps(manifest))
                with self.assertRaisesRegex(ValueError, "Video transcript SHA-256 mismatch"):
                    self.build()
                self.assertEqual({str(path.relative_to(output)): path.read_bytes() for path in output.rglob("*") if path.is_file()}, published)
                manifest["videos"][0]["transcript_sha256"] = hashes[collection]
                self.write(f"video/{collection}/manifest.json", json.dumps(manifest))

    def test_second_video_collection_links_and_revocation_preserve_existing_content(self):
        first_manifest = self.video_fixture()
        self.write("video/bilibili-280780745/manifest.json", json.dumps(first_manifest))
        self.write("reader/demo/index.html", "<!doctype html><html><body>Original reader source</body></html>")
        self.write("docs/reader/demo/index.html", "<!doctype html><html><body>Original published reader</body></html>")
        self.write("docs/reader/demo/data.json", '{"original":true}')
        _, output = self.build()
        protected_sources = {str(path.relative_to(self.root)): path.read_bytes()
                             for folder in ("course", "reader")
                             for path in (self.root / folder).rglob("*") if path.is_file()}
        protected_outputs = {str(path.relative_to(output)): path.read_bytes()
                             for folder in ("course", "markdown/course", "reader", "video/bilibili-280780745", "markdown/video/bilibili-280780745")
                             for path in (output / folder).rglob("*") if path.is_file()}
        first_search = [item for item in json.loads((output / "search-index.json").read_text())
                        if item["url"].startswith("/notebook/video/bilibili-280780745/")]

        second_manifest = self.second_video_fixture()
        self.write("video/bilibili-508452265/manifest.json", json.dumps(second_manifest))
        for authorized in (True, False):
            with self.subTest(second_collection_authorized=authorized):
                second_manifest["publication_authorized"] = authorized
                self.write("video/bilibili-508452265/manifest.json", json.dumps(second_manifest))
                _, output = self.build()
                for name, content in protected_sources.items():
                    self.assertEqual((self.root / name).read_bytes(), content, name)
                for name, content in protected_outputs.items():
                    self.assertEqual((output / name).read_bytes(), content, name)
                search = json.loads((output / "search-index.json").read_text())
                self.assertEqual([item for item in search if item["url"].startswith("/notebook/video/bilibili-280780745/")], first_search)
                second = "video/bilibili-508452265/BV1KZ8X6uEPL"
                self.assertEqual((output / second / "transcript.zh-CN.html").is_file(), authorized)
                self.assertEqual((output / "markdown" / second / "transcript.zh-CN.md").is_file(), authorized)
                self.assertEqual(any("第二系列独有测试讲稿" in item["text"] for item in search), authorized)
                preview = (output / second / "preview.html").read_text()
                self.assertIn('href="/notebook/video/bilibili-508452265/index.html">第二创作者测试集</a>', preview)
                self.assertIn(f'href="/notebook/{second}/preview.html"', preview)
                self.assertNotIn("bilibili-280780745", preview)
                self.assertEqual("transcript.zh-CN.html" in preview, authorized)
                if authorized:
                    transcript = (output / second / "transcript.zh-CN.html").read_text()
                    self.assertIn('href="/notebook/video/bilibili-508452265/index.html">第二创作者测试集</a>', transcript)
                    self.assertIn(f'href="/notebook/{second}/preview.html"', transcript)
                    self.assertIn(f'href="/notebook/markdown/{second}/transcript.zh-CN.md" download', transcript)
                    self.assertNotIn("bilibili-280780745", transcript)
                self.assertEqual(site.validate_links(output, "/notebook/"), [])


if __name__ == "__main__":
    unittest.main()
