#!/usr/bin/env python3
"""Package an additive slide/transcript reader without modifying legacy pages.

Uses only committed Markdown, alignment JSON and rendered WebP assets. It can run
in GitHub Actions without raw PDFs, local transcript caches or third-party libs.
"""
from __future__ import annotations

import argparse
import hashlib
import html
import json
from pathlib import Path
import re
import shutil
from urllib.parse import parse_qs, urlsplit

COURSE = "mit-mmai-2026"
SESSION = re.compile(r"w\d{2}-\d+\Z")
HEADINGS = re.compile(r"^### \[[^\]]+\]\(([^)]+)\) · (b\d+)\s*$", re.M)
CONFIDENCE = {"estimated", "weak", "unmatched"}


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def read_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def safe_file(root: Path, relative: str) -> Path:
    path = root / relative
    if Path(relative).is_absolute() or not path.resolve().is_relative_to(root.resolve()):
        raise ValueError(f"Source path escapes reader: {relative}")
    if path.is_symlink() or not path.is_file():
        raise ValueError(f"Missing or symlinked source: {relative}")
    return path


def web_url(value: str) -> str:
    parts = urlsplit(value)
    if parts.scheme != "https" or not parts.hostname or parts.username or parts.password:
        raise ValueError("Source links must be public HTTPS URLs")
    return value


def parse_transcript(path: Path, video_id: str) -> list[dict]:
    text = path.read_text(encoding="utf-8")
    matches = list(HEADINGS.finditer(text))
    blocks = []
    for index, match in enumerate(matches):
        parts = urlsplit(html.unescape(match[1]))
        query = parse_qs(parts.query)
        if parts.scheme != "https" or parts.hostname != "www.youtube.com" or query.get("v") != [video_id]:
            raise ValueError(f"Wrong video link in {path.name}: {match[2]}")
        seconds = query.get("t", [""])[0]
        if not re.fullmatch(r"\d+s", seconds):
            raise ValueError(f"Invalid timestamp: {match[2]}")
        end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        body = text[match.end():end].strip()
        body = html.unescape(re.sub(r"\\([\\`*_{}\[\]|])", r"\1", body))
        if not body:
            raise ValueError(f"Empty transcript paragraph: {match[2]}")
        blocks.append({"id": match[2], "seconds": int(seconds[:-1]), "text": body})
    if not blocks or len({b["id"] for b in blocks}) != len(blocks):
        raise ValueError(f"Missing or duplicated transcript blocks: {path}")
    if any(a["seconds"] > b["seconds"] for a, b in zip(blocks, blocks[1:])):
        raise ValueError(f"Non-monotonic transcript: {path}")
    return blocks


def load_overrides(path: Path) -> dict[tuple[str, str], dict]:
    if not path.exists():
        return {}
    data = read_json(path)
    overrides = {}
    for item in data.get("overrides", []):
        key = (item["session_id"], item["block_id"])
        if key in overrides or not item.get("reason"):
            raise ValueError("Editorial links need unique IDs and a source-based reason")
        overrides[key] = item
    return overrides


def build(root: Path, output: Path) -> dict:
    root, output = root.resolve(), output.resolve()
    if output == root or root.is_relative_to(output):
        raise ValueError("Build output cannot be the source root or an ancestor")
    source = root / "reader" / COURSE
    course = root / "course" / COURSE
    destination = output / "reader" / COURSE
    if not destination.resolve().is_relative_to(output):
        raise ValueError("Reader destination escapes build output")
    catalog = read_json(course / "catalog.json")
    statuses = {s["session_id"]: s for s in read_json(course / "transcript-status.json")["sessions"]}
    slide_index = read_json(source / "slides-index.json")
    decks = {d["id"]: d for d in slide_index["decks"]}
    overrides = load_overrides(source / "alignment-review.json")
    used_overrides = set()
    generated = {}
    copied_images = set()
    manifest = {
        "schema_version": 1,
        "course_id": COURSE,
        "course_title": catalog["title"],
        "default_session": "w01-1",
        "sessions": [],
        "note": "对应关系依据讲稿与幻灯片文本估计，并非逐帧视频识别。可在本机校正。",
        "attribution_url": "./slides/ATTRIBUTION.md",
    }

    def write(relative: str, value) -> None:
        path = destination / relative
        if not path.resolve().is_relative_to(destination.resolve()):
            raise ValueError("Generated path escapes reader destination")
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(value, ensure_ascii=False, separators=(",", ":")) + "\n", encoding="utf-8")
        generated[relative] = digest(path)

    def copy(path: Path, relative: str) -> None:
        target = destination / relative
        if not target.resolve().is_relative_to(destination.resolve()):
            raise ValueError("Asset target escapes reader destination")
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(path, target)
        generated[relative] = digest(target)

    total_blocks = associated_blocks = editorial_blocks = 0
    for session in catalog["sessions"]:
        if not session.get("video_url"):
            continue
        sid = session["id"]
        if not SESSION.fullmatch(sid) or not statuses[sid].get("public_transcripts"):
            raise ValueError(f"Transcript publication not enabled: {sid}")
        status = statuses[sid]
        alignment = read_json(safe_file(source, f"alignments/{sid}.json"))
        if alignment.get("session_id") != sid:
            raise ValueError(f"Alignment identity mismatch: {sid}")
        en_path, zh_path = course / sid / "transcript.en.md", course / sid / "transcript.zh-CN.md"
        for name, path in (("transcript.en.md", en_path), ("transcript.zh-CN.md", zh_path)):
            if digest(path) != status["artifacts"][name]["sha256"]:
                raise ValueError(f"Transcript hash changed: {sid}/{name}")
        expected_en = alignment.get("provenance", {}).get("english_markdown_sha256")
        if expected_en and expected_en != digest(en_path):
            raise ValueError(f"Alignment must be refreshed for changed English: {sid}")
        en, zh = parse_transcript(en_path, status["video_id"]), parse_transcript(zh_path, status["video_id"])
        if [b["id"] for b in en] != [b["id"] for b in zh] or [b["id"] for b in en] != [b["block_id"] for b in alignment["blocks"]]:
            raise ValueError(f"Block IDs/order mismatch: {sid}")
        slides, lesson_decks = [], []
        for deck_id in alignment["deck_ids"]:
            deck = decks[deck_id]
            lesson_decks.append({"id": deck_id, "title": deck["title"], "source_url": web_url(deck["source_url"])})
            for page in deck["pages"]:
                image_path = safe_file(source, page["image"])
                if image_path.suffix != ".webp" or digest(image_path) != page["sha256"]:
                    raise ValueError(f"Slide image integrity failed: {image_path.name}")
                slide_id = f"{deck_id}-p{page['page']:03d}"
                if page["image"] not in copied_images:
                    copy(image_path, page["image"])
                    copied_images.add(page["image"])
                slides.append({
                    "id": slide_id, "deck_id": deck_id, "page": page["page"],
                    "title": page.get("text_excerpt", "").strip()[:150] or f"{deck['title']} · 第 {page['page']} 页",
                    "image_url": "./" + page["image"],
                    "source_url": web_url(page["source_url"]), "width": page["width"], "height": page["height"],
                    "block_ids": [],
                })
        by_slide = {s["id"]: s for s in slides}
        if len(by_slide) != len(slides):
            raise ValueError(f"Duplicated deck/slide IDs: {sid}")
        blocks = []
        for original, translated, match in zip(en, zh, alignment["blocks"]):
            key = (sid, original["id"])
            selected = overrides.get(key, match)
            if key in overrides:
                used_overrides.add(key)
                editorial_blocks += 1
            slide_id = selected.get("slide_id")
            if slide_id is not None and slide_id not in by_slide:
                raise ValueError(f"Invalid matched slide: {sid}/{original['id']}")
            start, end = match["start_ms"], match["end_ms"]
            if type(start) is not int or type(end) is not int or not 0 <= start <= end or start // 1000 != original["seconds"] or translated["seconds"] != original["seconds"]:
                raise ValueError(f"Timestamp drift: {sid}/{original['id']}")
            confidence = selected.get("confidence", "estimated") if slide_id else "unmatched"
            if confidence not in CONFIDENCE:
                raise ValueError("Unknown alignment confidence label")
            candidates = []
            for candidate in match.get("candidates", [])[:5]:
                if candidate["slide_id"] not in by_slide:
                    raise ValueError(f"Invalid candidate slide: {sid}")
                candidates.append({"slide_id": candidate["slide_id"], "score": candidate.get("score")})
            blocks.append({
                "id": original["id"], "start_ms": start, "end_ms": end,
                "en": original["text"], "zh": translated["text"], "slide_id": slide_id,
                "confidence": confidence, "score": selected.get("score", match.get("score")),
                "candidates": candidates, "reason": selected.get("reason", ""),
                "match_source": "editorial_text_review" if key in overrides else "automatic_text_sequence",
            })
            if slide_id:
                by_slide[slide_id]["block_ids"].append(original["id"])
                associated_blocks += 1
        total_blocks += len(blocks)
        lesson = {
            "schema_version": 1, "session_id": sid, "title": session["title"],
            "video_url": f"https://www.youtube.com/watch?v={status['video_id']}",
            "blocks": blocks, "slides": slides, "decks": lesson_decks,
            "alignment_method": alignment["method"],
            "source_hashes": {"en": digest(en_path), "zh": digest(zh_path)},
        }
        write(f"data/{sid}.json", lesson)
        manifest["sessions"].append({"id": sid, "title": session["title"], "data_url": f"./data/{sid}.json", "blocks_count": len(blocks), "slide_count": len(slides)})
    if set(overrides) != used_overrides:
        raise ValueError("Editorial correction refers to an unknown session/block")
    for filename in ("index.html", "reader.css", "reader.js"):
        copy(safe_file(root / "reader" / "app", filename), filename)
    copy(safe_file(source, "slides-index.json"), "slides-index.json")
    for relative in (slide_index.get("attribution"), slide_index.get("source_license")):
        if relative:
            copy(safe_file(source, relative), relative)
    write("manifest.json", manifest)
    report = {"sessions": len(manifest["sessions"]), "blocks": total_blocks, "associated_blocks": associated_blocks, "editorial_blocks": editorial_blocks, "images": len(copied_images), "files": generated}
    write("build-manifest.json", report)
    return {k: v for k, v in report.items() if k != "files"}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    print(json.dumps(build(args.root, args.output or args.root / "docs"), ensure_ascii=False))


if __name__ == "__main__":
    main()
