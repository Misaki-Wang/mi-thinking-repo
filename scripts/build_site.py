#!/usr/bin/env python3
"""Build the learning notebook with Python's standard library; no network access."""

from __future__ import annotations

import argparse
import hashlib
import html
from html.parser import HTMLParser
import json
import posixpath
from pathlib import Path, PurePosixPath
import re
from urllib.parse import quote, unquote, urlsplit, urlunsplit

REPOSITORY = "https://github.com/Misaki-Wang/mi-thinking-repo"
DOCUMENT_NAMES = {
    "preview.md": "课程预览",
    "readings.md": "阅读指引",
    "transcript.en.md": "英文讲稿",
    "transcript.zh-CN.md": "中文讲稿",
    "transcript.bilingual.md": "双语讲稿",
    "GUIDANCE.md": "学习指南",
    "TRANSCRIPTS.md": "讲稿目录",
    "TRANSLATION.md": "翻译说明",
    "TERMS.md": "专业术语",
}
TRANSCRIPT_FORMATS = (
    ("transcript.en.md", "英文"),
    ("transcript.zh-CN.md", "中文"),
    ("transcript.bilingual.md", "双语"),
)
VIDEO_STYLES = """/* Loaded only when the video collection is present. */
@media(max-width:680px){.top-nav{gap:12px}}
@media(max-width:480px){.brand>span:last-child{display:none}}
"""


def esc(value: object) -> str:
    return html.escape(str(value), quote=True)


def normalize_base(value: str) -> str:
    if not re.fullmatch(r"/?[A-Za-z0-9_/-]*", value) or ".." in value:
        raise ValueError("base must be a site path, such as /mi-thinking-repo/")
    return "/" + value.strip("/") + "/" if value.strip("/") else "/"


def page_path(source: PurePosixPath) -> PurePosixPath:
    if source == PurePosixPath("README.md"):
        return PurePosixPath("about.html")
    if source.name.lower() == "readme.md":
        return source.with_name("index.html")
    return source.with_suffix(".html")


def site_url(base: str, path: str | PurePosixPath = "") -> str:
    return base + quote(str(path).lstrip("/"), safe="/-._~")


def clean_text(markdown: str) -> str:
    text = re.sub(r"!?\[([^\]]+)\]\([^\n]+?\)", r"\1", markdown)
    return re.sub(r"\s+", " ", re.sub(r"[`#*_>|]", "", text)).strip()


def safe_link(value: str, source: PurePosixPath, base: str) -> str | None:
    """Allow web links and published relative documents; never active URL schemes."""
    value = html.unescape(value.strip().strip("<>"))
    if any(ord(char) < 32 for char in value) or value.startswith("//"):
        return None
    parts = urlsplit(value)
    if parts.scheme:
        return value if parts.scheme.lower() in {"https", "http", "mailto"} else None
    if not parts.path:
        return value
    raw = unquote(parts.path)
    path = posixpath.normpath(raw.lstrip("/") if raw.startswith("/") else str(source.parent / raw))
    if path.startswith("../") or path == ".." or any(p.startswith(".") for p in PurePosixPath(path).parts):
        return None
    target = PurePosixPath(path)
    if target.suffix.lower() == ".md":
        target = page_path(target)
    elif parts.path.endswith("/") or not target.suffix:
        target = target / "index.html"
    elif target.suffix.lower() not in {".html", ".css", ".js", ".png", ".jpg", ".jpeg", ".svg", ".webp"}:
        # Source data and code remain visible in the repository, not in the Pages artifact.
        return REPOSITORY + "/blob/main/" + quote(path, safe="/-._~")
    return urlunsplit(("", "", site_url(base, target), parts.query, parts.fragment))


class Markdown:
    """Deliberately small, HTML-escaped Markdown renderer for trusted layout/untrusted text."""

    def __init__(self, source: PurePosixPath, base: str):
        self.source = source
        self.base = base
        self.headings: list[tuple[int, str, str]] = []
        self.slugs: dict[str, int] = {}

    def inline(self, text: str, depth: int = 0) -> str:
        if depth > 8:
            return esc(text)
        output: list[str] = []
        i = 0
        while i < len(text):
            if text[i] == "\\" and i + 1 < len(text):
                output.append(esc(text[i + 1]))
                i += 2
                continue
            if text[i] == "`":
                end = text.find("`", i + 1)
                if end != -1:
                    output.append("<code>" + esc(text[i + 1:end]) + "</code>")
                    i = end + 1
                    continue
            if text[i] == "$":
                marker = "$$" if text.startswith("$$", i) else "$"
                end = text.find(marker, i + len(marker))
                if end != -1:
                    output.append(esc(text[i:end + len(marker)]))
                    i = end + len(marker)
                    continue
            if text[i] == "&":
                entity = re.match(r"&(?:#[xX][0-9a-fA-F]{1,8}|#[0-9]{1,8}|[A-Za-z][A-Za-z0-9]{1,31});", text[i:])
                if entity:
                    output.append(esc(html.unescape(entity.group())))
                    i += len(entity.group())
                    continue
            image = text.startswith("![", i)
            if text[i] == "[" or image:
                start = i + (2 if image else 1)
                middle = text.find("](", start)
                if middle != -1:
                    end, balance = middle + 2, 1
                    while end < len(text) and balance:
                        if text[end] == "(":
                            balance += 1
                        elif text[end] == ")":
                            balance -= 1
                        end += 1
                    if balance == 0:
                        label = text[start:middle]
                        url = safe_link(text[middle + 2:end - 1], self.source, self.base)
                        if url:
                            # Images are links: lecture sources stay with their original publisher.
                            output.append(f'<a href="{esc(url)}">{self.inline(label, depth + 1)}</a>')
                        else:
                            output.append(self.inline(label, depth + 1))
                        i = end
                        continue
            matched = False
            for marker, tag in (("**", "strong"), ("__", "strong"), ("~~", "del"), ("*", "em"), ("_", "em")):
                if text.startswith(marker, i):
                    if marker.startswith("_") and ((i and (text[i - 1].isalnum() or text[i - 1] == "_")) or i + len(marker) == len(text) or text[i + len(marker)].isspace()):
                        continue
                    end = text.find(marker, i + len(marker))
                    if marker.startswith("_"):
                        while end != -1 and (text[end - 1].isspace() or (end + len(marker) < len(text) and (text[end + len(marker)].isalnum() or text[end + len(marker)] == "_"))):
                            end = text.find(marker, end + len(marker))
                    if end > i + len(marker):
                        content = self.inline(text[i + len(marker):end], depth + 1)
                        output.append(f"<{tag}>{content}</{tag}>")
                        i = end + len(marker)
                        matched = True
                        break
            if matched:
                continue
            if text.startswith("<https://", i) or text.startswith("<http://", i):
                end = text.find(">", i)
                if end != -1:
                    value = text[i + 1:end]
                    output.append(f'<a href="{esc(value)}">{esc(value)}</a>')
                    i = end + 1
                    continue
            output.append(esc(text[i]))
            i += 1
        return "".join(output)

    def heading(self, level: int, title: str) -> str:
        plain = clean_text(title)
        slug = re.sub(r"[^\w\s-]", "", plain.lower(), flags=re.UNICODE).strip()
        slug = re.sub(r"\s", "-", slug) or "section"
        count = self.slugs.get(slug, 0)
        self.slugs[slug] = count + 1
        if count:
            slug += f"-{count}"
        self.headings.append((level, plain, slug))
        return f'<h{level} id="{esc(slug)}">{self.inline(title)}<a class="heading-anchor" href="#{quote(slug)}" aria-label="链接到此段">#</a></h{level}>'

    @staticmethod
    def cells(line: str) -> list[str]:
        return [cell.strip().replace("\\|", "|") for cell in re.split(r"(?<!\\)\|", line.strip().strip("|"))]

    def render(self, text: str) -> str:
        lines = text.replace("\r\n", "\n").splitlines()
        output: list[str] = []
        paragraph: list[str] = []
        lists: list[tuple[int, str]] = []

        def flush() -> None:
            if paragraph:
                output.append("<p>" + self.inline(" ".join(paragraph)) + "</p>")
                paragraph.clear()

        def close_lists(min_indent: int = -1) -> None:
            while lists and lists[-1][0] >= min_indent:
                _, kind = lists.pop()
                output.append(f"</li></{kind}>")

        i = 0
        while i < len(lines):
            line = lines[i]
            stripped = line.strip()
            if not stripped:
                flush()
                i += 1
                continue
            fence = re.match(r"^\s*(`{3,}|~{3,})(.*)$", line)
            if fence:
                flush()
                close_lists()
                marker = fence.group(1)
                language = re.sub(r"[^a-zA-Z0-9_-]", "", fence.group(2).strip())
                code: list[str] = []
                i += 1
                while i < len(lines) and not lines[i].strip().startswith(marker):
                    code.append(lines[i])
                    i += 1
                output.append(f'<pre><code class="language-{esc(language)}">{esc(chr(10).join(code))}</code></pre>')
                i += 1
                continue
            heading = re.match(r"^(#{1,6})\s+(.+?)\s*#*$", stripped)
            if heading:
                flush()
                close_lists()
                output.append(self.heading(len(heading.group(1)), heading.group(2)))
                i += 1
                continue
            if re.match(r"^(?:-{3,}|\*{3,}|_{3,})$", stripped):
                flush()
                close_lists()
                output.append("<hr>")
                i += 1
                continue
            if i + 1 < len(lines) and "|" in line and re.match(r"^\s*\|?\s*:?-{3,}:?\s*(?:\|\s*:?-{3,}:?\s*)+\|?\s*$", lines[i + 1]):
                flush()
                close_lists()
                headers = self.cells(line)
                output.append('<div class="table-scroll"><table><thead><tr>' + "".join("<th>" + self.inline(v) + "</th>" for v in headers) + "</tr></thead><tbody>")
                i += 2
                while i < len(lines) and "|" in lines[i] and lines[i].strip():
                    cells = self.cells(lines[i])
                    output.append("<tr>" + "".join("<td>" + self.inline(v) + "</td>" for v in cells) + "</tr>")
                    i += 1
                output.append("</tbody></table></div>")
                continue
            if stripped.startswith(">"):
                flush()
                close_lists()
                block: list[str] = []
                while i < len(lines) and lines[i].lstrip().startswith(">"):
                    block.append(re.sub(r"^\s*> ?", "", lines[i]))
                    i += 1
                nested = Markdown(self.source, self.base)
                output.append("<blockquote>" + nested.render("\n".join(block)) + "</blockquote>")
                continue
            item = re.match(r"^(\s*)([-+*]|\d+[.)])\s+(.+)$", line)
            if item:
                flush()
                indent = len(item.group(1).expandtabs(4))
                kind = "ol" if item.group(2)[0].isdigit() else "ul"
                while lists and (lists[-1][0] > indent or (lists[-1][0] == indent and lists[-1][1] != kind)):
                    close_lists(lists[-1][0])
                if lists and lists[-1] == (indent, kind):
                    output.append("</li><li>")
                else:
                    lists.append((indent, kind))
                    number = re.match(r"\d+", item.group(2))
                    start = f' start="{int(number.group())}"' if number else ""
                    output.append(f"<{kind}{start}><li>")
                content = item.group(3)
                task = re.match(r"^\[([ xX])\] (.*)", content)
                if task:
                    output.append(f'<span class="task-box" aria-label="{"已完成" if task.group(1).lower() == "x" else "未完成"}">{"☑" if task.group(1).lower() == "x" else "☐"}</span> ')
                    content = task.group(2)
                output.append(self.inline(content))
                i += 1
                continue
            if lists and len(line) - len(line.lstrip()) > lists[-1][0]:
                output.append(" " + self.inline(stripped))
                i += 1
                continue
            close_lists()
            paragraph.append(stripped)
            i += 1
        flush()
        close_lists()
        return "\n".join(output)


class Site:
    def __init__(self, root: Path, output: Path, base: str):
        self.root = root.resolve()
        self.output = output.resolve()
        self.base = normalize_base(base)
        self.sources: dict[PurePosixPath, str] = {}
        self.catalogs: dict[str, dict] = {}
        self.public_transcripts: set[tuple[str, str]] = set()
        self.public_video_transcripts: set[PurePosixPath] = set()
        self.generated: set[str] = set()
        self.search: list[dict] = []

    def url(self, path: str | PurePosixPath = "") -> str:
        return site_url(self.base, path)

    def write(self, path: str | PurePosixPath, text: str) -> None:
        destination = self.output / path
        if not destination.resolve().is_relative_to(self.output):
            raise ValueError(f"output escapes destination: {path}")
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_text(text, encoding="utf-8")
        self.generated.add(str(path))

    def collect(self) -> None:
        for path in sorted((self.root / "course").glob("*/transcript-status.json")):
            if path.is_symlink() or not path.resolve().is_relative_to(self.root):
                continue
            data = json.loads(path.read_text(encoding="utf-8"))
            for session in data.get("sessions", []):
                if session.get("public_transcripts") is True:
                    self.public_transcripts.add((path.parent.name, session["session_id"]))
        candidates = [self.root / "README.md"]
        for section in ("course", "blog", "paper"):
            candidates.extend(sorted((self.root / section).glob("**/*.md")))
        video_index = self.root / "video" / "README.md"
        if self.video_source_allowed(video_index):
            self.collect_video_transcripts()
            candidates.extend(sorted((self.root / "video").glob("**/*.md")))
        for path in candidates:
            if path.is_file() and not path.is_symlink() and path.resolve().is_relative_to(self.root):
                relative = PurePosixPath(path.relative_to(self.root).as_posix())
                if relative.name.startswith("transcript.") and relative.parts[0] == "course":
                    if len(relative.parts) < 4 or (relative.parts[1], relative.parts[2]) not in self.public_transcripts:
                        continue
                if relative.parts[0] == "video":
                    if not self.video_source_allowed(path):
                        continue
                    if relative.name.startswith("transcript") and relative not in self.public_video_transcripts:
                        continue
                if not any(part.startswith(".") for part in relative.parts):
                    self.sources[relative] = path.read_text(encoding="utf-8")
        for path in sorted((self.root / "course").glob("*/catalog.json")):
            if path.is_symlink() or not path.resolve().is_relative_to(self.root):
                continue
            data = json.loads(path.read_text(encoding="utf-8"))
            if isinstance(data, list):
                data = {"title": path.parent.name, "sessions": data}
            self.catalogs[path.parent.name] = data

    def video_source_allowed(self, path: Path) -> bool:
        return (path.is_file() and path.resolve().is_relative_to(self.root)
                and not any(part.is_symlink() for part in (path, *path.parents) if part != self.root))

    def collect_video_transcripts(self) -> None:
        """Publish only the exact Chinese artifact declared by each video entry."""
        for path in sorted((self.root / "video").glob("*/manifest.json")):
            if not self.video_source_allowed(path) or path.parent.name.startswith("."):
                continue
            data = json.loads(path.read_text(encoding="utf-8"))
            if not isinstance(data, dict) or data.get("publication_authorized") is not True:
                continue
            entries = data.get("videos", [])
            if not isinstance(entries, list):
                raise ValueError(f"Video manifest videos must be a list: {path}")
            seen = set()
            for entry in entries:
                if not isinstance(entry, dict):
                    raise ValueError(f"Invalid video manifest entry: {path}")
                if entry.get("public_transcripts") is not True:
                    continue
                bvid = entry.get("bvid")
                if not isinstance(bvid, str) or not re.fullmatch(r"BV[0-9A-Za-z]{10}", bvid) or bvid in seen:
                    raise ValueError(f"Invalid or duplicate public video ID: {bvid!r}")
                seen.add(bvid)
                transcript = path.parent / bvid / "transcript.zh-CN.md"
                if not self.video_source_allowed(transcript):
                    raise ValueError(f"Missing or unsafe public video transcript: {transcript}")
                expected = entry.get("transcript_sha256")
                if not isinstance(expected, str) or not re.fullmatch(r"[0-9a-fA-F]{64}", expected):
                    raise ValueError(f"Missing or invalid video transcript SHA-256: {bvid}")
                if hashlib.sha256(transcript.read_bytes()).hexdigest() != expected.lower():
                    raise ValueError(f"Video transcript SHA-256 mismatch: {bvid}")
                self.public_video_transcripts.add(PurePosixPath(transcript.relative_to(self.root).as_posix()))

    def has(self, path: str | PurePosixPath) -> bool:
        return PurePosixPath(path) in self.sources

    def session_path(self, course: str, session: dict, name: str = "preview.md") -> PurePosixPath:
        return PurePosixPath("course", course, str(session["id"]), name)

    def transcript_paths(self, course: str, session: dict) -> list[tuple[PurePosixPath, str]]:
        return [(self.session_path(course, session, name), label) for name, label in TRANSCRIPT_FORMATS
                if self.has(self.session_path(course, session, name))]

    def session_link(self, course: str, session: dict) -> str:
        for name in ("preview.md", "readings.md", "README.md"):
            path = self.session_path(course, session, name)
            if self.has(path):
                return self.url(page_path(path))
        return self.url(PurePosixPath("course", course, "index.html")) + "#session-" + quote(str(session["id"]))

    def section_nav(self, current: str) -> str:
        links = [("", "首页", "home"), ("course/index.html", "Course", "course"), ("blog/index.html", "Blog", "blog"), ("paper/index.html", "Paper", "paper")]
        if self.has("video/README.md"):
            links.append(("video/index.html", "视频", "video"))
        return "".join(f'<a href="{self.url(path)}" class="{"active" if key == current else ""}">{name}</a>' for path, name, key in links)

    def shell(self, title: str, body: str, section: str = "home", sidebar: str = "", toc: str = "") -> str:
        layout = "reading-layout" if sidebar else "wide-layout"
        video_style = f'\n<link rel="stylesheet" href="{self.url("assets/video.css")}">' if self.has("video/README.md") else ""
        return f'''<!doctype html>
<html lang="zh-CN">
<head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="description" content="Misaki 的学习笔记：课程预览、阅读指引与术语表。">
<meta http-equiv="Content-Security-Policy" content="default-src 'self'; script-src 'self'; style-src 'self'; img-src 'self' data:; connect-src 'self'; object-src 'none'; base-uri 'self'">
<meta name="color-scheme" content="light"><title>{esc(title)} · MI Thinking</title>
<link rel="icon" href="{self.url('assets/favicon.svg')}" type="image/svg+xml">
<link rel="stylesheet" href="{self.url('assets/site.css')}">{video_style}
<script src="{self.url('assets/site.js')}" defer></script>
</head>
<body data-base="{esc(self.base)}">
<a class="skip-link" href="#main">跳到内容</a>
<header class="site-header"><div class="header-inner">
<a class="brand" href="{self.url()}"><span class="brand-mark">mi<span>·</span></span><span>THINKING REPO<small>Misaki’s learning notebook</small></span></a>
<nav class="top-nav" aria-label="主导航">{self.section_nav(section)}</nav>
<button class="search-open" aria-label="搜索全站" aria-haspopup="dialog"><span>⌕</span><span class="search-label">搜索笔记</span><kbd>/</kbd></button>
<a class="github-link" href="{REPOSITORY}" aria-label="GitHub 仓库">GitHub ↗</a>
</div></header>
<div class="{layout}">{sidebar}<main id="main">{body}</main>{toc}</div>
<footer class="site-footer"><span>MI THINKING REPO <span class="footer-dot">·</span> 学习，在连接中发生。</span><a href="{REPOSITORY}">在 GitHub 阅读 Markdown ↗</a></footer>
<dialog id="search-dialog" aria-labelledby="search-title"><div class="search-top"><label id="search-title" for="site-search">搜索学习笔记</label><button id="search-close" aria-label="关闭搜索">Esc</button></div><input id="site-search" type="search" placeholder="课程、概念、论文或讲稿中的一句话…" autocomplete="off"><p id="search-status" role="status">输入关键词，搜索全部课程与笔记。</p><div id="search-results"></div></dialog>
</body></html>'''

    def sidebar(self, course: str, current: PurePosixPath) -> str:
        catalog = self.catalogs.get(course, {})
        overview = PurePosixPath("course", course, "README.md")
        guidance = PurePosixPath("course", course, "GUIDANCE.md")
        links = [f'<a class="sidebar-overview" href="{self.url(page_path(overview))}">← 课程总览</a>']
        if self.has(guidance):
            links.append(f'<a class="sidebar-guide {"active" if current == guidance else ""}" href="{self.url(page_path(guidance))}">◈ 学习指南</a>')
        transcript_index = PurePosixPath("course", course, "TRANSCRIPTS.md")
        if self.has(transcript_index):
            links.append(f'<a class="sidebar-guide {"active" if current == transcript_index else ""}" href="{self.url(page_path(transcript_index))}">◈ 全部讲稿</a>')
        for session in catalog.get("sessions", []):
            if not session.get("instructional", True):
                continue
            active = current.parent.name == session["id"]
            links.append(f'<a class="lesson-nav {"active" if active else ""}" href="{self.session_link(course, session)}"><span>{esc(str(session["id"]).upper())}</span>{esc(session["title"])}</a>')
        return f'<aside class="sidebar"><details class="lesson-menu" open><summary>课程导航 <span>⌄</span></summary><div class="sidebar-inner"><p class="eyebrow">{esc(catalog.get("title", course))}</p>{"".join(links)}</div></details></aside>'

    def cards(self, course: str) -> str:
        cards = []
        for session in self.catalogs[course].get("sessions", []):
            if not session.get("instructional", True):
                continue
            topics = session.get("topics") or []
            if isinstance(topics, str):
                topics = [topics]
            video = bool(session.get("video_url"))
            slides = bool(session.get("slides_url")) and session.get("slides_status") not in {"unavailable", "missing", "failed"}
            available = self.has(self.session_path(course, session))
            transcripts = self.transcript_paths(course, session)
            transcript_links = ""
            if transcripts:
                transcript_links = '<nav class="transcript-links" aria-label="本章讲稿">' + "".join(
                    f'<a href="{self.url(page_path(path))}">{label}讲稿 ↗</a>' for path, label in reversed(transcripts)
                ) + "</nav>"
            transcript_status = " / ".join(label for _, label in transcripts) + "讲稿已归档" if transcripts else ""
            label = "视频 + Slides" if video and slides else "视频" if video else "Slides" if slides else "来源待补充"
            tags = "".join(f"<span>{esc(topic)}</span>" for topic in topics[:3])
            searchable = " ".join([str(session.get("title", "")), str(session["id"]), *map(str, topics)])
            reading_path = self.session_path(course, session, "readings.md")
            reading_link = f'<a class="text-link" href="{self.url(page_path(reading_path))}">阅读指引 ↗</a>' if self.has(reading_path) else ""
            cards.append(f'''<article class="lesson-card" id="session-{esc(session['id'])}" data-search="{esc(searchable.lower())}" data-kind="{'video' if video else 'slides' if slides else 'missing'}">
<div class="card-meta"><span>{esc(str(session['id']).upper())} <span class="meta-dot">·</span> {esc(session.get('date', ''))}</span><span class="source-badge {'badge-video' if video else ''}">{label}</span></div>
<h3><a href="{self.session_link(course, session)}">{esc(session['title'])}</a></h3><div class="topic-tags">{tags}</div>
<div class="card-bottom"><a class="preview-link" href="{self.session_link(course, session)}">{'学习准备' if available and not (video or slides) else '开始预览' if available else '查看资料状态'} <span>→</span></a>{reading_link}</div>
{transcript_links}<span class="transcript-status">{transcript_status or ('资料待补充 · 学习准备' if not (video or slides) else '按公开资料整理' if available else '资料状态见课程记录')}</span></article>''')
        return "".join(cards)

    def course_landing(self, course: str, intro: str = "") -> str:
        catalog = self.catalogs[course]
        sessions = [s for s in catalog.get("sessions", []) if s.get("instructional", True)]
        videos = sum(bool(s.get("video_url")) for s in sessions)
        previews = sum(self.has(self.session_path(course, s)) for s in sessions)
        readings = sum(self.has(self.session_path(course, s, "readings.md")) for s in sessions)
        transcript_counts = [(label, sum(self.has(self.session_path(course, s, filename)) for s in sessions))
                             for filename, label in TRANSCRIPT_FORMATS]
        transcript_summary = ""
        if any(count for _, count in transcript_counts):
            transcript_summary = '<p class="transcript-summary">已公开讲稿：' + " · ".join(
                f"{label} {count} 讲" for label, count in transcript_counts
            ) + "</p>"
        guidance = PurePosixPath("course", course, "GUIDANCE.md")
        action = f'<a class="button" href="{self.url(page_path(guidance))}">从学习指南开始 <span>→</span></a>' if self.has(guidance) else ""
        transcript_index = PurePosixPath("course", course, "TRANSCRIPTS.md")
        if self.has(transcript_index):
            action += f'<a class="quiet-link" href="{self.url(page_path(transcript_index))}">全部讲稿 →</a>'
        source = safe_link(str(catalog.get("source_url", "")), PurePosixPath("README.md"), self.base)
        source_link = f'<a class="quiet-link" href="{esc(source)}">官方课程 ↗</a>' if source else ""
        description = catalog.get("reader_description") or catalog.get("description_zh") or "围绕多模态数据、融合、对齐、生成、推理与交互，结合课堂材料与论文，建立一条可回看的学习路径。"
        details = f'<details class="archive-details"><summary>关于这份课程归档</summary><div class="prose">{intro}</div></details>' if intro else ""
        return f'''<div class="breadcrumb"><a href="{self.url('course/index.html')}">Course</a><span>/</span><span>课程归档</span></div>
<section class="course-hero"><div class="hero-copy"><p class="eyebrow">COURSE NOTEBOOK <span> / </span> SPRING 2026</p><h1>{esc(catalog.get('title', course))}</h1><p class="hero-description">{esc(description)}</p><div class="hero-actions">{action}{source_link}</div></div><div class="course-emblem" aria-hidden="true"><div class="orbit orbit-one"></div><div class="orbit orbit-two"></div><div class="orbit orbit-three"></div><span>m<span>×</span>m</span><small>CONNECT THE MODALITIES</small></div></section>
<div class="course-stats"><div><strong>{len(sessions):02d}</strong><span>学习章节</span></div><div><strong>{previews:02d}</strong><span>章节入口</span></div><div><strong>{videos:02d}</strong><span>公开视频</span></div><div><strong>{readings:02d}</strong><span>阅读指引</span></div></div>
{transcript_summary}
<section class="library-section" aria-labelledby="chapters-heading"><div class="section-heading"><div><p class="eyebrow">THE LEARNING PATH</p><h2 id="chapters-heading">从一个问题，到下一层理解。</h2></div><p>预览 → Slides / Video → Readings → 自己的笔记</p></div>
<div class="library-toolbar"><label class="filter-input"><span>⌕</span><input id="lesson-filter" type="search" placeholder="筛选章节、主题…" aria-label="筛选课程章节"></label><div class="filter-buttons" aria-label="课程资料类型"><button class="selected" data-filter="all" aria-pressed="true">全部</button><button data-filter="video" aria-pressed="false">有视频</button><button data-filter="slides" aria-pressed="false">仅 Slides</button></div><span id="lesson-count" aria-live="polite">{len(sessions)} 个章节</span></div>
<div class="lesson-grid">{self.cards(course)}</div><p id="filter-empty" class="empty-message" hidden>没有匹配的章节，试试另一个关键词。</p></section>{details}'''

    def document(self, source: PurePosixPath, markdown: str) -> None:
        renderer = Markdown(source, self.base)
        rendered = renderer.render(markdown)
        if source.name.startswith("transcript."):
            header, divider, body = rendered.partition("<h2")
            if divider:
                header = re.sub(r"<ul>.*?</ul>", lambda match: '<details class="transcript-metadata"><summary>讲稿来源与处理信息</summary>' + match.group() + "</details>", header, count=1, flags=re.S)
                rendered = header + divider + body
        heading = next((text for level, text, _ in renderer.headings if level == 1), source.stem)
        section = source.parts[0] if len(source.parts) > 1 else "home"
        document_kind = "视频预览" if section == "video" and source.name == "preview.md" else DOCUMENT_NAMES.get(source.name, section.title())
        course = source.parts[1] if section == "course" and len(source.parts) > 2 else None
        output = page_path(source)
        downloads = PurePosixPath("markdown") / source
        self.write(downloads, markdown)
        if course in self.catalogs and source.name == "README.md" and len(source.parts) == 3:
            body = self.course_landing(course, rendered)
            page = self.shell(heading, body, section)
        else:
            tabs = ""
            session = next((s for s in self.catalogs.get(course, {}).get("sessions", []) if s["id"] == source.parent.name), None)
            if session:
                links = []
                for filename, label in DOCUMENT_NAMES.items():
                    target = source.with_name(filename)
                    if self.has(target):
                        links.append(f'<a class="{"active" if target == source else ""}" href="{self.url(page_path(target))}">{label}</a>')
                tabs = '<nav class="document-tabs" aria-label="本章材料">' + "".join(links) + "</nav>"
            elif section == "video" and len(source.parts) == 4:
                links = []
                for filename, label in (("preview.md", "视频预览"), ("transcript.zh-CN.md", "中文讲稿")):
                    target = source.with_name(filename)
                    if self.has(target):
                        links.append(f'<a class="{"active" if target == source else ""}" href="{self.url(page_path(target))}">{label}</a>')
                if links:
                    tabs = '<nav class="document-tabs" aria-label="本期视频材料">' + "".join(links) + "</nav>"
            source_links = []
            if session:
                for key, label in (("slides_url", "Slides ↗"), ("video_url", "Video ↗")):
                    if key == "slides_url" and session.get("slides_status") in {"unavailable", "missing", "failed", "not_listed"}:
                        continue
                    value = (session.get("slides_resolved_url") or session.get("resolved_url") or session.get(key)) if key == "slides_url" else session.get(key)
                    url = safe_link(str(value or ""), source, self.base)
                    if url:
                        source_links.append(f'<a href="{esc(url)}">{label}</a>')
            source_links.append(f'<a href="{self.url(downloads)}" download>下载 Markdown ↓</a>')
            breadcrumbs = f'<div class="breadcrumb"><a href="{self.url(section + "/index.html") if section != "home" else self.url()}">{esc(section.title())}</a>'
            if course:
                breadcrumbs += f'<span>/</span><a href="{self.url(PurePosixPath("course", course, "index.html"))}">MMAI 2026</a>'
            if section == "video" and len(source.parts) > 3:
                collection = PurePosixPath(*source.parts[:2], "README.md")
                if self.has(collection):
                    collection_title = next((line.lstrip("# ") for line in self.sources[collection].splitlines() if line.startswith("# ")), source.parts[1])
                    breadcrumbs += f'<span>/</span><a href="{self.url(page_path(collection))}">{esc(collection_title)}</a>'
            breadcrumbs += f'<span>/</span><span>{esc(document_kind if section == "video" else DOCUMENT_NAMES.get(source.name, "笔记"))}</span></div>'
            article_class = "prose transcript-prose" if source.name.startswith("transcript.") else "prose"
            body = breadcrumbs + tabs + '<div class="document-tools">' + "".join(source_links) + f'</div><article class="{article_class}">' + rendered + "</article>"
            toc_links = "".join(f'<a class="toc-level-{level}" href="#{quote(slug)}">{esc(text)}</a>' for level, text, slug in renderer.headings if 2 <= level <= 3)
            toc = f'<aside class="toc" aria-label="本页目录"><p>ON THIS PAGE</p>{toc_links}</aside>' if toc_links and course else ""
            page = self.shell(heading, body, section, self.sidebar(course, source) if course in self.catalogs else "", toc)
        self.write(output, page)
        self.search.append({"title": heading, "kind": document_kind, "url": self.url(output), "headings": " · ".join(h[1] for h in renderer.headings), "text": clean_text(markdown)})

    def course_tiles(self) -> str:
        tiles = []
        for course, catalog in self.catalogs.items():
            sessions = [s for s in catalog.get("sessions", []) if s.get("instructional", True)]
            tiles.append(f'''<a class="course-tile" href="{self.url(PurePosixPath('course', course, 'index.html'))}"><div class="tile-symbol" aria-hidden="true"><span>m</span><span>×</span><span>m</span></div><div class="tile-copy"><p class="eyebrow">MIT <span> / </span> SPRING 2026</p><h2>{esc(catalog.get('title', course))}</h2><p>课程预览 · Readings 指引 · 术语表</p><span class="tile-meta">{len(sessions)} 个章节 <span>↗</span></span></div></a>''')
        return "".join(tiles)

    def landing_pages(self) -> None:
        tiles = self.course_tiles()
        body = f'''<section class="home-hero"><p class="eyebrow"><span class="live-dot"></span> A NOTEBOOK IN PROGRESS</p><h1>Learning, one<br><em>connection</em> at a time.</h1><p>把课程里的问题、论文中的洞见，<br>和自己的思考，慢慢连在一起。</p><a class="button" href="{self.url('course/index.html')}">进入课程笔记 <span>↗</span></a><div class="hero-coordinate" aria-hidden="true">READ.<br>THINK.<br>CONNECT.</div></section>
<section class="home-courses"><div class="section-heading"><div><p class="eyebrow">CURRENTLY EXPLORING</p><h2>沿着课程，建立理解。</h2></div><a class="quiet-link" href="{self.url('course/index.html')}">所有课程 ↗</a></div>{tiles}</section>
<section class="notebook-spaces"><a href="{self.url('blog/index.html')}"><span class="space-number">01 / BLOG</span><h2>想法的草稿纸 <span>↗</span></h2><p>记录学习中的观察、问题与阶段性思考。</p></a><a href="{self.url('paper/index.html')}"><span class="space-number">02 / PAPER</span><h2>论文的边注 <span>↗</span></h2><p>留住值得重读的方法、实验和未解的问题。</p></a></section>'''
        if self.has("video/README.md"):
            body += f'<section class="notebook-spaces"><a href="{self.url("video/index.html")}"><span class="space-number">03 / VIDEO</span><h2>视频里的思考 <span>↗</span></h2><p>按主题回看视频笔记、预览与讲稿。</p></a></section>'
        self.write("index.html", self.shell("学习，在连接中发生", body))
        if not self.has("course/README.md"):
            body = f'<section class="collection-hero"><p class="eyebrow">THE COURSE SHELF</p><h1>Course</h1><p>系统地学习，也留出自己的思考空间。</p></section>{tiles}'
            self.write("course/index.html", self.shell("Course", body, "course"))
        for course in self.catalogs:
            if not self.has(PurePosixPath("course", course, "README.md")):
                self.write(PurePosixPath("course", course, "index.html"), self.shell(self.catalogs[course].get("title", course), self.course_landing(course), "course"))
        for section, title, copy in (("blog", "Blog", "这里会记录学习中的问题、观察和阶段性思考。"), ("paper", "Paper", "这里会收藏独立的论文阅读笔记；课程配套阅读见各章的阅读指引。")):
            posts = [(source, text) for source, text in self.sources.items() if source.parts[0] == section and source.name.lower() != "readme.md"]
            cards = "".join(f'<a class="note-card" href="{self.url(page_path(source))}"><h2>{esc(next((line.lstrip("# ") for line in text.splitlines() if line.startswith("# ")), source.stem))}</h2><p>{esc(clean_text(text)[:150])}</p><span>阅读笔记 →</span></a>' for source, text in posts)
            empty = '<div class="empty-state"><span aria-hidden="true">＋</span><h2>为下一次思考留一页。</h2><p>尚未发布独立笔记。</p></div>'
            body = f'<section class="collection-hero"><p class="eyebrow">PERSONAL NOTEBOOK</p><h1>{title}</h1><p>{copy}</p></section><div class="note-grid">{cards}</div>' if posts else f'<section class="collection-hero"><p class="eyebrow">PERSONAL NOTEBOOK</p><h1>{title}</h1><p>{copy}</p></section>{empty}'
            if self.has(PurePosixPath(section, "README.md")):
                body += f'<p class="collection-footnote"><a href="{self.url(PurePosixPath("markdown", section, "README.md"))}" download>目录说明 · Markdown ↓</a></p>'
            self.write(PurePosixPath(section, "index.html"), self.shell(title, body, section))
        self.write("404.html", self.shell("页面未找到", f'<section class="collection-hero"><p class="eyebrow">404 / A MISSING CONNECTION</p><h1>这页笔记还没找到。</h1><p>可以回到课程列表，或用搜索找到相关内容。</p><a class="button" href="{self.url()}">回到首页 →</a></section>'))

    def build(self) -> dict:
        self.collect()
        self.output.mkdir(parents=True, exist_ok=True)
        for source, markdown in self.sources.items():
            self.document(source, markdown)
        self.landing_pages()
        for name in ("site.css", "site.js", "favicon.svg"):
            path = self.root / "assets" / name
            if not path.is_file() or path.is_symlink():
                raise ValueError(f"missing asset: {path}")
            self.write(PurePosixPath("assets", name), path.read_text(encoding="utf-8"))
        if self.has("video/README.md"):
            self.write("assets/video.css", VIDEO_STYLES)
        self.write("search-index.json", json.dumps(self.search, ensure_ascii=False, separators=(",", ":")))
        self.write(".nojekyll", "")
        previous_manifest = self.output / "build-manifest.json"
        if previous_manifest.is_file():
            old_files = json.loads(previous_manifest.read_text(encoding="utf-8")).get("files", [])
            for old in old_files:
                candidate = self.output / old
                if old not in self.generated and candidate.resolve().is_relative_to(self.output) and candidate.is_file():
                    candidate.unlink()
        report = {"base": self.base, "documents": len(self.sources), "courses": len(self.catalogs), "search_documents": len(self.search), "files": sorted(self.generated)}
        self.write("build-manifest.json", json.dumps(report, ensure_ascii=False, indent=2) + "\n")
        problems = validate_links(self.output, self.base)
        if problems:
            raise ValueError("Broken local links:\n" + "\n".join(problems[:50]))
        return report


class LinkParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links: list[str] = []
        self.ids: set[str] = set()

    def handle_starttag(self, tag, attrs):
        values = dict(attrs)
        if values.get("id"):
            self.ids.add(values["id"])
        for key in ("href", "src"):
            if values.get(key):
                self.links.append(values[key])


def validate_links(output: Path, base: str) -> list[str]:
    """Validate every site-local target, including document fragments."""
    documents: dict[Path, LinkParser] = {}
    for page in output.rglob("*.html"):
        parser = LinkParser()
        parser.feed(page.read_text(encoding="utf-8"))
        documents[page.resolve()] = parser
    problems = []
    for page, parser in documents.items():
        for link in parser.links:
            parts = urlsplit(link)
            if parts.scheme or parts.netloc:
                continue
            raw = unquote(parts.path)
            if not raw:
                target = page
            elif raw.startswith(base):
                target = output / raw[len(base):]
            elif raw.startswith("/"):
                problems.append(f"{page.relative_to(output)}: outside base: {link}")
                continue
            else:
                target = page.parent / raw
            if target.is_dir():
                target = target / "index.html"
            target = target.resolve()
            if not target.is_relative_to(output.resolve()) or not target.is_file():
                problems.append(f"{page.relative_to(output)}: missing: {link}")
            elif parts.fragment and target in documents and unquote(parts.fragment) not in documents[target].ids:
                problems.append(f"{page.relative_to(output)}: missing anchor: {link}")
    return problems


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--output", type=Path, help="default: ROOT/docs")
    parser.add_argument("--base", default="/mi-thinking-repo/", help="use / for a local HTTP preview")
    args = parser.parse_args()
    root = args.root.resolve()
    output = (args.output or root / "docs").resolve()
    if output == root or root.is_relative_to(output):
        parser.error("output must not be the source root or an ancestor")
    report = Site(root, output, args.base).build()
    print(f"Built {report['documents']} Markdown documents, {report['courses']} courses → {output}")
    print("Verified: all local links and section anchors resolve.")


if __name__ == "__main__":
    main()
