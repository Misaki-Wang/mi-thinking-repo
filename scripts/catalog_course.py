#!/usr/bin/env python3
"""Snapshot the public MIT MMAI schedule and acquire local source evidence.

Run with a Python environment containing pypdf only when using --slides.
Raw slides, notebooks, and channel metadata are kept under ignored .work/.
No course video or reading full text is published by this script.
"""

from __future__ import annotations

import argparse
import concurrent.futures
import datetime as dt
import hashlib
import html
from html.parser import HTMLParser
import json
from pathlib import Path
import re
import subprocess
import sys
from urllib.parse import quote, urljoin, urlparse
from urllib.request import Request, urlopen


ROOT = Path(__file__).resolve().parents[1]
WORK = ROOT / ".work" / "sources"
CATALOG = ROOT / "course" / "mit-mmai-2026" / "catalog.json"
SCHEDULE = "https://mit-mi.github.io/mmai-course/spring2026/schedule/"
CHANNEL = "https://www.youtube.com/@paulliang279/videos"
LICENSE_URL = "https://raw.githubusercontent.com/MIT-MI/mmai-course/main/LICENSE"
MAX_BYTES = 100 * 1024 * 1024


class Node:
    def __init__(self, tag: str, attrs=()):
        self.tag = tag
        self.attrs = dict(attrs)
        self.children: list[Node | str] = []

    def text(self):
        return " ".join(c.text() if isinstance(c, Node) else c for c in self.children)

    def find_all(self, tag):
        result = []
        for child in self.children:
            if isinstance(child, Node):
                if child.tag == tag:
                    result.append(child)
                result.extend(child.find_all(tag))
        return result


class Document(HTMLParser):
    VOID = {"area", "base", "br", "col", "embed", "hr", "img", "input", "link", "meta", "param", "source", "track", "wbr"}

    def __init__(self, source):
        super().__init__(convert_charrefs=True)
        self.root = Node("root")
        self.stack = [self.root]
        self.feed(source)

    def handle_starttag(self, tag, attrs):
        node = Node(tag, attrs)
        self.stack[-1].children.append(node)
        if tag not in self.VOID:
            self.stack.append(node)

    def handle_endtag(self, tag):
        for index in range(len(self.stack) - 1, 0, -1):
            if self.stack[index].tag == tag:
                del self.stack[index:]
                break

    def handle_data(self, value):
        self.stack[-1].children.append(value)


def clean(value):
    return re.sub(r"\s+", " ", html.unescape(value)).strip()


def fetch(url):
    if urlparse(url).scheme != "https":
        raise ValueError("Only public HTTPS source URLs are supported")
    # quote literal spaces in source-authored PDF paths without double encoding.
    url = quote(url, safe=":/?=&%+#@")
    request = Request(url, headers={"User-Agent": "MIT-MMAI-personal-study-archive/1.0"})
    with urlopen(request, timeout=90) as response:
        value = response.read(MAX_BYTES + 1)
        if len(value) > MAX_BYTES:
            raise ValueError("Source exceeds acquisition size limit")
        return value, response.headers.get_content_type(), response.url


def write_json(path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    temporary.replace(path)


def read_catalog():
    return json.loads(CATALOG.read_text(encoding="utf-8"))


def fetch_notebook(url):
    drive = re.search(r"/drive/([^?/#]+)", url)
    if not drive:
        raise ValueError("Unsupported notebook URL")
    candidates = [f"https://drive.google.com/uc?export=download&id={drive[1]}", f"https://colab.research.google.com/drive/{drive[1]}?format=ipynb"]
    errors = []
    for candidate in candidates:
        try:
            raw, mime, resolved = fetch(candidate)
            notebook = json.loads(raw)
            if not isinstance(notebook.get("cells"), list):
                raise ValueError("Response is not a notebook")
            return raw, mime, resolved, notebook
        except Exception as error:
            errors.append(f"{type(error).__name__}: {error}")
    raise ValueError("Public notebook download unavailable: " + "; ".join(errors))


def build_catalog():
    raw, _, _ = fetch(SCHEDULE)
    WORK.mkdir(parents=True, exist_ok=True)
    (WORK / "schedule.html").write_bytes(raw)
    doc = Document(raw.decode("utf-8"))
    sessions = []
    for row in doc.root.find_all("tr"):
        cells = [x for x in row.children if isinstance(x, Node) and x.tag in {"th", "td"}]
        if len(cells) < 2:
            continue
        match = re.search(r"Week\s+(\d+)\.(\d+)", cells[1].text())
        if not match:
            continue
        week, slot = map(int, match.groups())
        strong = cells[1].find_all("strong")
        title = clean(strong[0].text()) if strong else clean(cells[1].text())
        links = {clean(x.text()): urljoin(SCHEDULE, x.attrs.get("href", "")) for x in cells[1].find_all("a")}
        date = clean(cells[0].text())
        month, day = map(int, date.split("/"))
        readings = [{"title": clean(x.text()), "url": urljoin(SCHEDULE, x.attrs["href"])} for x in (cells[2].find_all("a") if len(cells) > 2 else []) if x.attrs.get("href")]
        issues = []
        seen = {}
        for reading in readings:
            if reading["url"] in seen:
                issues.append({"kind": "duplicate_reading_url", "url": reading["url"], "titles": [seen[reading["url"]], reading["title"]]})
            seen[reading["url"]] = reading["title"]
        instructional = not any(s in title.lower() for s in ("no class", "no lectures", "in-class midterm", "project presentations"))
        sessions.append({
            "id": f"w{week:02d}-{slot}", "week": week, "slot": slot,
            "date": f"2026-{month:02d}-{day:02d}", "title": title,
            "topics": [clean(x.text()) for x in cells[1].find_all("li")],
            "slides_url": links.get("[slides]"), "video_url": links.get("[video]"),
            "video_source": "official_schedule" if links.get("[video]") else None,
            "readings": readings, "instructional": instructional,
            "source_issues": issues,
            "slides_status": "not_acquired" if links.get("[slides]") else "not_listed",
            "video_status": "linked" if links.get("[video]") else "not_listed_on_schedule",
        })
    if len(sessions) < 20 or len({x["id"] for x in sessions}) != len(sessions):
        raise ValueError("Schedule parsing failed its row count or identity validation")
    license_raw, _, _ = fetch(LICENSE_URL)
    (WORK / "upstream-LICENSE").write_bytes(license_raw)
    data = {
        "title": "MIT Modeling: MultiModal AI — Spring 2026",
        "description": "Personal study archive catalog; source links and availability are preserved from the official schedule.",
        "source_url": SCHEDULE, "channel_url": CHANNEL,
        "retrieved_at": dt.datetime.now(dt.timezone.utc).isoformat(),
        "schedule_sha256": hashlib.sha256(raw).hexdigest(),
        "upstream_license": {"url": LICENSE_URL, "repository": "https://github.com/MIT-MI/mmai-course", "declared_spdx": "MIT", "copyright_line": next((line for line in license_raw.decode().splitlines() if "Copyright" in line), ""), "scope_note": "Repository-level MIT license is present; this does not independently establish licensing of YouTube videos or third-party papers/images. Raw materials are local-only."},
        "sessions": sessions,
    }
    write_json(CATALOG, data)
    print(json.dumps({"catalog": str(CATALOG), "sessions": len(sessions), "instructional": sum(x["instructional"] for x in sessions), "schedule_videos": sum(bool(x["video_url"]) for x in sessions)}, ensure_ascii=False), flush=True)
    return data


def acquire_slide(session):
    url = session.get("slides_resolved_url") or session.get("slides_url")
    if not url:
        return {"id": session["id"], "slides_status": "not_listed"}
    dest = WORK / session["id"]
    dest.mkdir(parents=True, exist_ok=True)
    try:
        if "colab.research.google.com" in url:
            raw, mime, resolved, notebook = fetch_notebook(url)
            (dest / "slides.ipynb").write_bytes(raw)
            pages = [{"page": i + 1, "cell_type": c.get("cell_type"), "text": "".join(c.get("source", []))} for i, c in enumerate(notebook["cells"])]
            kind = "notebook"
        else:
            from pypdf import PdfReader
            path = dest / "slides.pdf"
            if path.exists() and path.read_bytes()[:5] == b"%PDF-":
                raw = path.read_bytes()
                mime, resolved = "application/pdf", quote(url, safe=":/?=&%+#@")
            else:
                raw, mime, resolved = fetch(url)
                if not raw.startswith(b"%PDF-"):
                    raise ValueError(f"Expected PDF, got {mime}")
                path.write_bytes(raw)
            reader = PdfReader(path)
            pages = [{"page": i + 1, "text": page.extract_text() or ""} for i, page in enumerate(reader.pages)]
            kind = "pdf"
        write_json(dest / "slides-pages.json", {"source_url": url, "kind": kind, "pages": pages})
        (dest / "slides.txt").write_text("\n\n".join(f"=== PAGE {x['page']} ===\n{x['text']}" for x in pages) + "\n", encoding="utf-8")
        evidence = {"id": session["id"], "slides_status": "acquired", "slides_kind": kind, "slides_pages": len(pages), "slides_text_characters": sum(len(x["text"]) for x in pages), "slides_sha256": hashlib.sha256(raw).hexdigest(), "slides_resolved_url": resolved, "empty_text_pages": [x["page"] for x in pages if not x["text"].strip()]}
        write_json(dest / "source-evidence.json", evidence)
        return evidence
    except Exception as error:
        evidence = {"id": session["id"], "slides_status": "unavailable", "slides_error": f"{type(error).__name__}: {error}"}
        write_json(dest / "source-evidence.json", evidence)
        return evidence


def acquire_all(data):
    by_id = {x["id"]: x for x in data["sessions"]}
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
        for result in pool.map(acquire_slide, data["sessions"]):
            by_id[result["id"]].update(result)
            write_json(CATALOG, data)
            print(json.dumps(result, ensure_ascii=False), flush=True)


def repair_slide_links(data):
    """Resolve whitespace-only broken filenames against an observed upstream tree."""
    tree_url = "https://api.github.com/repos/MIT-MI/mmai-course/git/trees/main?recursive=1"
    raw, _, _ = fetch(tree_url)
    tree = json.loads(raw)
    write_json(WORK / "upstream-tree.json", tree)
    paths = [x["path"] for x in tree["tree"] if x["type"] == "blob" and x["path"].lower().endswith(".pdf")]
    for session in data["sessions"]:
        if session.get("slides_status") != "unavailable" or not session.get("slides_url"):
            continue
        expected = urlparse(session["slides_url"]).path.removeprefix("/mmai-course/")
        matches = [x for x in paths if re.sub(r"\s+", "", x) == re.sub(r"\s+", "", expected)]
        if len(matches) == 1:
            resolved = "https://mit-mi.github.io/mmai-course/" + quote(matches[0])
            session["source_issues"].append({"kind": "broken_schedule_slide_link", "schedule_url": session["slides_url"], "resolved_url": resolved, "evidence_url": tree_url, "upstream_tree_sha": tree["sha"], "matching_rule": "Unique path match after removing whitespace only"})
            session["slides_resolved_url"] = resolved
            session.update(acquire_slide(session))
            if session["slides_status"] == "acquired":
                session.pop("slides_error", None)
            print(json.dumps({"repaired": session["id"], "url": resolved, "status": session["slides_status"]}), flush=True)
        else:
            session["source_issues"].append({"kind": "unresolved_slide_link", "schedule_url": session["slides_url"], "evidence_url": tree_url, "upstream_tree_sha": tree["sha"], "matching_candidates": matches})
    write_json(CATALOG, data)


def acquire_reading_notebooks(data):
    records = []
    for session in data["sessions"]:
        for index, reading in enumerate(session["readings"], 1):
            if "colab.research.google.com/drive/" not in reading["url"]:
                continue
            dest = WORK / session["id"] / "readings" / f"{index:02d}"
            dest.mkdir(parents=True, exist_ok=True)
            record = {"session_id": session["id"], "reading_index": index, **reading}
            try:
                raw, _, resolved, notebook = fetch_notebook(reading["url"])
                (dest / "notebook.ipynb").write_bytes(raw)
                cells = [{"cell": i + 1, "cell_type": c.get("cell_type"), "text": "".join(c.get("source", []))} for i, c in enumerate(notebook["cells"])]
                write_json(dest / "notebook-cells.json", cells)
                (dest / "notebook.txt").write_text("\n\n".join(f"=== CELL {x['cell']} ({x['cell_type']}) ===\n{x['text']}" for x in cells), encoding="utf-8")
                record.update({"status": "acquired", "resolved_url": resolved, "sha256": hashlib.sha256(raw).hexdigest(), "cells": len(cells), "notebook_name": notebook.get("metadata", {}).get("colab", {}).get("name"), "markdown_headings": [line.strip() for c in cells if c["cell_type"] == "markdown" for line in c["text"].splitlines() if line.startswith("#")][:12], "local_path": str(dest.relative_to(ROOT))})
            except Exception as error:
                record.update({"status": "unavailable", "error": f"{type(error).__name__}: {error}"})
            write_json(dest / "evidence.json", record)
            records.append(record)
            print(json.dumps(record, ensure_ascii=False), flush=True)
    write_json(WORK / "reading-notebooks.json", records)


def list_videos(data, executable):
    proc = subprocess.run([str(executable), "--ignore-config", "--flat-playlist", "--dump-single-json", "--no-warnings", CHANNEL], capture_output=True, text=True, timeout=180, check=True)
    raw = json.loads(proc.stdout)
    write_json(WORK / "channel-videos.json", raw)
    entries = [{k: x.get(k) for k in ("id", "title", "url", "duration", "view_count", "description")} for x in raw.get("entries", []) if x]
    write_json(WORK / "channel-video-index.json", entries)
    # Preserve a candidate list; no fuzzy title match silently changes the schedule.
    schedule_ids = {re.search(r"youtu\.be/([^?]+)", x["video_url"])[1] for x in data["sessions"] if x.get("video_url") and "youtu.be/" in x["video_url"]}
    candidates = [x for x in entries if re.search(r"MMAI|multi.?modal|2026", x.get("title") or "", re.I)]
    data["channel_discovery"] = {"retrieved_at": dt.datetime.now(dt.timezone.utc).isoformat(), "total_videos": len(entries), "spring2026_count": sum("Spring 2026" in x.get("title", "") for x in entries), "course_candidates": [{**x, "on_official_schedule": x["id"] in schedule_ids, "spring2026_title_match": "Spring 2026" in x.get("title", "")} for x in candidates], "matching_policy": "Candidate metadata only. Videos absent from the schedule require explicit title/date/lecture evidence before association."}
    write_json(CATALOG, data)
    print(json.dumps(data["channel_discovery"], ensure_ascii=False), flush=True)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--refresh", action="store_true", help="Rebuild schedule catalog from the source")
    parser.add_argument("--slides", action="store_true", help="Acquire and extract public slide PDFs/notebooks")
    parser.add_argument("--repair-slide-links", action="store_true", help="Check unavailable slides against exact upstream filenames")
    parser.add_argument("--reading-notebooks", action="store_true", help="Acquire publicly downloadable Colab reading notebooks")
    parser.add_argument("--yt-dlp", type=Path, help="Existing yt-dlp executable for channel discovery")
    args = parser.parse_args()
    data = build_catalog() if args.refresh or not CATALOG.exists() else read_catalog()
    for session in data["sessions"]:
        if "resolved_url" in session:
            session.setdefault("slides_resolved_url", session.pop("resolved_url"))
    if "channel_discovery" in data:
        discovery = data["channel_discovery"]
        for candidate in discovery["course_candidates"]:
            candidate["spring2026_title_match"] = "Spring 2026" in candidate.get("title", "")
        discovery["spring2026_count"] = sum(x["spring2026_title_match"] for x in discovery["course_candidates"])
    write_json(CATALOG, data)
    if args.yt_dlp:
        list_videos(data, args.yt_dlp)
    if args.slides:
        acquire_all(data)
    if args.repair_slide_links:
        repair_slide_links(data)
    if args.reading_notebooks:
        acquire_reading_notebooks(data)


if __name__ == "__main__":
    main()
