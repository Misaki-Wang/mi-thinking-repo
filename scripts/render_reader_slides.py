#!/usr/bin/env python3
"""Render local course PDFs for the independent synchronized reader.

Requires pypdfium2 and Pillow. Run with the bundled workspace Python runtime.
Only the reader's rendered assets and provenance index are written; the original
PDFs stay under .work/sources and are never copied into the public site.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import re
from urllib.parse import quote, urlsplit, urlunsplit

import PIL
from PIL import Image
import pypdfium2 as pdfium


ROOT = Path(__file__).resolve().parents[1]
COURSE_ID = "mit-mmai-2026"
CATALOG = ROOT / "course" / COURSE_ID / "catalog.json"
SOURCES = ROOT / ".work" / "sources"
OUTPUT = ROOT / "reader" / COURSE_ID
INDEX = OUTPUT / "slides-index.json"
SLIDES = OUTPUT / "slides"
ID_RE = re.compile(r"w\d{2}-[12]\Z")


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def public_url(url: str) -> str:
    parts = urlsplit(url)
    return urlunsplit((parts.scheme, parts.netloc, quote(parts.path, safe="/%"), parts.query, ""))


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, data: dict) -> None:
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    temporary.replace(path)


def page_is_current(page: dict, session_id: str) -> bool:
    number = page.get("page")
    if not isinstance(number, int) or number < 1:
        return False
    expected = f"slides/{session_id}-p{number:03d}.webp"
    if page.get("image") != expected:
        return False
    image_path = OUTPUT / expected
    if not image_path.is_file() or image_path.stat().st_size != page.get("bytes"):
        return False
    if sha256(image_path) != page.get("sha256"):
        return False
    with Image.open(image_path) as image:
        return image.size == (page.get("width"), page.get("height")) and image.format == "WEBP"


def render_deck(session: dict, previous: dict | None, config: dict, rebuild: bool) -> dict:
    session_id = session["id"]
    source_pdf = SOURCES / session_id / "slides.pdf"
    source_text = SOURCES / session_id / "slides-pages.json"
    if not source_pdf.is_file() or not source_text.is_file():
        raise FileNotFoundError(f"Local PDF and page text are required for {session_id}")
    pdf_hash = sha256(source_pdf)
    text_hash = sha256(source_text)
    pages_text = {page["page"]: page.get("text", "") for page in load_json(source_text)["pages"]}
    source_url = public_url(session.get("slides_resolved_url") or session["slides_url"])
    document = pdfium.PdfDocument(source_pdf)
    page_count = len(document)
    if len(pages_text) != page_count:
        document.close()
        raise ValueError(f"PDF/text page count mismatch for {session_id}")
    old_pages = {}
    if previous and not rebuild and previous.get("source_pdf_sha256") == pdf_hash and previous.get("render") == config:
        old_pages = {page["page"]: page for page in previous.get("pages", [])}
    deck = {
        "id": session_id,
        "title": session["title"],
        "source_url": source_url,
        "source_pdf_sha256": pdf_hash,
        "source_text_sha256": text_hash,
        "source_kind": "pdf",
        "page_count": page_count,
        "render": config,
        "pages": [],
    }
    rendered = 0
    resumed = 0
    try:
        for index in range(page_count):
            number = index + 1
            image_relative = f"slides/{session_id}-p{number:03d}.webp"
            image_path = OUTPUT / image_relative
            page = old_pages.get(number)
            if page and page_is_current(page, session_id):
                page = dict(page)
                resumed += 1
            else:
                pdf_page = document[index]
                try:
                    pdf_width, pdf_height = pdf_page.get_size()
                    scale = config["width"] / pdf_width
                    bitmap = pdf_page.render(scale=scale)
                    try:
                        image = bitmap.to_pil().convert("RGB")
                        try:
                            # PDFium rounds dimensions upward. Resample only the
                            # occasional rounding pixel, preserving the aspect ratio.
                            size = (config["width"], round(config["width"] * pdf_height / pdf_width))
                            if image.size != size:
                                resized = image.resize(size, Image.Resampling.LANCZOS)
                                image.close()
                                image = resized
                            temporary = image_path.with_suffix(".webp.tmp")
                            image.save(temporary, format="WEBP", quality=config["quality"], method=6)
                            temporary.replace(image_path)
                            width, height = image.size
                        finally:
                            image.close()
                    finally:
                        bitmap.close()
                finally:
                    pdf_page.close()
                page = {
                    "page": number,
                    "image": image_relative,
                    "width": width,
                    "height": height,
                    "bytes": image_path.stat().st_size,
                    "sha256": sha256(image_path),
                }
                rendered += 1
            page.update({
                "source_page": number,
                "source_url": f"{source_url}#page={number}",
                "text_excerpt": " ".join(pages_text[number].split())[:300],
            })
            deck["pages"].append(page)
    finally:
        document.close()
    deck["total_bytes"] = sum(page["bytes"] for page in deck["pages"])
    print(f"{session_id}: {page_count} pages, {rendered} rendered, {resumed} verified/resumed, {deck['total_bytes']:,} bytes", flush=True)
    return deck


def write_attribution(catalog: dict) -> None:
    upstream_license = SOURCES / "upstream-LICENSE"
    if not upstream_license.is_file():
        raise FileNotFoundError("Expected locally acquired upstream-LICENSE")
    (SLIDES / "SOURCE-LICENSE.txt").write_bytes(upstream_license.read_bytes())
    (SLIDES / "ATTRIBUTION.md").write_text(
        "# Slide image sources\n\n"
        "These WebP images are faithful, uncropped page renderings of the publicly linked "
        "MIT Modeling: MultiModal AI, Spring 2026 lecture PDFs by Paul Liang and the "
        "individual presenters credited in each deck. Original page credits are retained.\n\n"
        f"- Official schedule: [{catalog['source_url']}]({catalog['source_url']})\n"
        "- Upstream course repository: [MIT-MI/mmai-course](https://github.com/MIT-MI/mmai-course)\n"
        "- Per-deck PDF URLs, source hashes, and page-level provenance: [slides-index.json](../slides-index.json)\n"
        "- Upstream repository license, copied verbatim: [SOURCE-LICENSE.txt](SOURCE-LICENSE.txt)\n\n"
        "The upstream repository declares the MIT License, copyright (c) 2026 MIT-MI. "
        "That repository-level declaration does not independently establish the licensing "
        "of third-party figures, papers, or YouTube videos. The study archive's requested "
        "transcription, translation, and publication also rely on the user's authorization "
        "attestation recorded in the course catalog on 2026-09-07. No blanket license for "
        "third-party material is asserted here. Original PDFs remain outside the public "
        "reader assets.\n",
        encoding="utf-8",
    )


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--ids", nargs="+", help="Session IDs (space or comma separated); default: every PDF session with a video")
    parser.add_argument("--width", type=int, default=1280, help="Image width in pixels, default 1280")
    parser.add_argument("--quality", type=int, default=85, help="WebP quality, default 85")
    parser.add_argument("--rebuild", action="store_true", help="Render requested decks even when source and output hashes match")
    args = parser.parse_args()
    if not 320 <= args.width <= 2400 or not 1 <= args.quality <= 100:
        parser.error("width must be 320..2400 and quality must be 1..100")
    catalog = load_json(CATALOG)
    sessions = {session["id"]: session for session in catalog["sessions"]}
    requested = sorted(set(part for value in args.ids for part in value.split(","))) if args.ids else [
        session["id"] for session in catalog["sessions"] if session.get("video_url") and session.get("slides_kind") == "pdf"
    ]
    for session_id in requested:
        if not ID_RE.fullmatch(session_id) or session_id not in sessions:
            parser.error(f"Unknown session ID: {session_id}")
        if sessions[session_id].get("slides_kind") != "pdf":
            parser.error(f"Session does not have a PDF: {session_id}")
    config = {
        "format": "webp", "width": args.width, "quality": args.quality,
        "method": 6, "renderer": "pypdfium2", "pdfium_version": str(pdfium.PDFIUM_INFO),
        "pillow_version": PIL.__version__, "cropped": False,
    }
    previous = load_json(INDEX) if INDEX.is_file() else {}
    decks = {deck["id"]: deck for deck in previous.get("decks", [])}
    SLIDES.mkdir(parents=True, exist_ok=True)
    write_attribution(catalog)
    for session_id in requested:
        decks[session_id] = render_deck(sessions[session_id], decks.get(session_id), config, args.rebuild)
        # Checkpoint after each deck so interrupted runs can resume safely.
        document = {
            "schema_version": 1,
            "course_id": COURSE_ID,
            "source_schedule_url": catalog["source_url"],
            "attribution": "slides/ATTRIBUTION.md",
            "source_license": "slides/SOURCE-LICENSE.txt",
            "decks": [decks[key] for key in sorted(decks)],
            "total_decks": len(decks),
            "total_pages": sum(deck["page_count"] for deck in decks.values()),
            "total_bytes": sum(deck["total_bytes"] for deck in decks.values()),
        }
        write_json(INDEX, document)
    print(f"TOTAL: {document['total_decks']} decks, {document['total_pages']} pages, {document['total_bytes']:,} bytes", flush=True)


if __name__ == "__main__":
    main()
