"""Audit transcript coverage and alignment; semantic flags need contextual review.

Only structural errors fail this check. Length, vocabulary, number, and negation
heuristics identify passages to read; none establishes translation correctness.
Uses Python's standard library and never rewrites source translations.
"""

from __future__ import annotations

import argparse
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import re
from urllib.parse import parse_qs, urlsplit

REPO = Path(__file__).resolve().parents[1]
ARTIFACTS = ("transcript.en.md", "transcript.zh-CN.md", "transcript.bilingual.md")
WORD = re.compile(r"[A-Za-z]+(?:['’-][A-Za-z]+)*|\d+(?:\.\d+)?")
CJK = re.compile(r"[\u3400-\u9fff]")
PROTECTED = re.compile(
    r"\b(?:CLIP|BERT|GPT(?:-\d[\w.-]*)?|LLaVA|Flamingo|ResNet|ViT|VAE|VQ-VAE|"
    r"ELBO|RLHF|PPO|GRPO|DPO|LoRA|Qwen(?:\d[\w.-]*)?|DALL[ -]?E|"
    r"LLM|VLM|MLLM|MoE|SFT|CoT|CFG|FID|OOD|InfoNCE|ImageNet|COCO)\b",
    re.IGNORECASE,
)
NEGATION = re.compile(r"\b(?:not|no|never|without|cannot|can't|don't|doesn't|isn't|aren't|won't)\b", re.I)
BOUNDARY_TERMS = re.compile(
    r"\b(?:early fusion|late fusion|tensor fusion|low-rank approximation|"
    r"cross-attention|self-attention|contrastive learning|reinforcement learning|"
    r"flow matching|tokenization|cross-entropy|dynamic time warping|"
    r"mutual information|joint distribution|marginal distribution)\b", re.I
)
HEADING = re.compile(r"^### \[[^\]]+\]\(([^)]+)\) · (b\d+)$", re.M)


def read_json(path):
    return json.loads(path.read_text(encoding="utf-8"))


def audit_blocks(english, chinese):
    errors, advisory = [], []
    if not isinstance(english, list) or not isinstance(chinese, list):
        return {"errors": ["Both block documents must contain arrays"], "advisories": []}
    if not english:
        errors.append("No English source blocks")
    for label, blocks in (("English", english), ("Chinese", chinese)):
        if any(not isinstance(block, dict) for block in blocks):
            return {"errors": [f"{label} contains a non-object block"], "advisories": []}
        ids = [block.get("block_id") for block in blocks]
        if any(not isinstance(value, str) or not value for value in ids):
            errors.append(f"{label} has a missing or invalid block ID")
        if len({str(value) for value in ids}) != len(ids):
            errors.append(f"{label} has duplicate block IDs")
    if [block.get("block_id") for block in english] != [block.get("block_id") for block in chinese]:
        errors.append("English and Chinese block IDs/order differ")
    translated = {block.get("block_id"): block for block in chinese if isinstance(block.get("block_id"), str)}
    previous_start = -1
    ratios = []
    filled = 0
    for position, block in enumerate(english):
        identifier = block.get("block_id")
        start, end = block.get("start_ms"), block.get("end_ms")
        valid_times = type(start) is int and type(end) is int and 0 <= start <= end
        if not valid_times:
            errors.append(f"{identifier}: invalid source timestamps")
        elif start < previous_start:
            errors.append(f"{identifier}: source start time regressed")
        if valid_times:
            previous_start = start
        target = translated.get(identifier, {})
        for field in ("start_ms", "end_ms"):
            if field in target and target[field] != block.get(field):
                errors.append(f"{identifier}: translated {field} differs from source")
        source_text, target_text = block.get("text"), target.get("text")
        if not isinstance(source_text, str) or not source_text.strip():
            errors.append(f"{identifier}: empty or invalid English text")
            continue
        if not isinstance(target_text, str) or not target_text.strip():
            errors.append(f"{identifier}: empty or invalid Chinese text")
            continue
        filled += 1
        words = WORD.findall(source_text)
        units = len(CJK.findall(target_text)) + len(WORD.findall(target_text))
        ratio = units / max(1, len(words))
        ratios.append(ratio)
        if len(words) >= 60 and not CJK.search(target_text):
            errors.append(f"{identifier}: long translated block contains no Chinese characters")
        if len(words) >= 60 and ratio < 0.65:
            advisory.append({"block_id": identifier, "kind": "possible_compression", "ratio": round(ratio, 3), "source_words": len(words)})
        missing = sorted({term for term in PROTECTED.findall(source_text) if term.casefold() not in target_text.casefold()})
        if missing:
            advisory.append({"block_id": identifier, "kind": "technical_names", "missing_literal_terms": missing})
        for term in sorted(set(BOUNDARY_TERMS.findall(source_text))):
            if term.casefold() in target_text.casefold():
                continue
            for adjacent in (position - 1, position + 1):
                if not 0 <= adjacent < len(english):
                    continue
                other = english[adjacent]
                other_translation = translated.get(other.get("block_id"), {}).get("text", "")
                if (
                    isinstance(other.get("text"), str)
                    and isinstance(other_translation, str)
                    and term.casefold() not in other["text"].casefold()
                    and term.casefold() in other_translation.casefold()
                ):
                    advisory.append({"block_id": identifier, "kind": "possible_boundary_shift", "term": term, "translated_in": other.get("block_id")})
        # Ignore one-digit integers, which are often written as Chinese numerals.
        number_pattern = r"(?<![A-Za-z0-9.])(?:\d{2,}|\d+\.\d+)(?![A-Za-z0-9.])"
        source_numbers = set(re.findall(number_pattern, source_text))
        target_numbers = set(re.findall(number_pattern, target_text))
        missing_numbers = sorted(source_numbers - target_numbers)
        if missing_numbers:
            advisory.append({"block_id": identifier, "kind": "numbers", "missing_literal_numbers": missing_numbers})
        if len(NEGATION.findall(source_text)) >= 3 and not re.search(r"不|没|无|未|非|否|别|难|避免|拒绝|排除|除外|以外|仅|只有", target_text):
            advisory.append({"block_id": identifier, "kind": "negation", "note": "Inspect whether negative qualifications were retained"})
    return {
        "english_blocks": len(english),
        "chinese_blocks": len(chinese),
        "nonempty_translations": filled,
        "minimum_length_ratio": round(min(ratios), 3) if ratios else None,
        "errors": errors,
        "advisories": advisory,
    }


def audit_artifacts(directory, english, chinese, video_id):
    errors, hashes = [], {}
    translations = {block["block_id"]: block["text"] for block in chinese}
    expected_ids = [block["block_id"] for block in english]
    expected_seconds = [block["start_ms"] // 1000 for block in english]
    for name in ARTIFACTS:
        path = directory / name
        if not path.is_file():
            errors.append(f"Missing published artifact: {path}")
            continue
        content = path.read_text(encoding="utf-8")
        hashes[name] = hashlib.sha256(path.read_bytes()).hexdigest()
        headings = HEADING.findall(content)
        if [identifier for _, identifier in headings] != expected_ids:
            errors.append(f"{name}: heading block IDs/order differ from source")
        for (url, identifier), seconds in zip(headings, expected_seconds):
            query = parse_qs(urlsplit(url).query)
            if query.get("v") != [video_id] or query.get("t") != [f"{seconds}s"]:
                errors.append(f"{name}: wrong video/timestamp link for {identifier}")
        # The renderer escapes HTML metacharacters; compare normalized text per
        # section so duplicated text or a wrong translation cannot pass by count.
        import html
        sections = re.split(HEADING, content)[1:]
        for offset in range(0, len(sections), 3):
            _, identifier, section = sections[offset:offset + 3]
            normalized = html.unescape(re.sub(r"\\([\\`*_{}\[\]|])", r"\1", section))
            block = next((item for item in english if item["block_id"] == identifier), None)
            if block is None:
                continue
            if name != "transcript.zh-CN.md" and block["text"] not in normalized:
                errors.append(f"{name}: source text missing or changed in {identifier}")
            if name != "transcript.en.md" and translations.get(identifier, "") not in normalized:
                errors.append(f"{name}: translation missing or changed in {identifier}")
    return {"errors": errors, "artifact_sha256": hashes}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", type=Path, default=REPO)
    parser.add_argument("--video-id", action="append")
    parser.add_argument("--require-artifacts", action="store_true")
    parser.add_argument("--report", type=Path)
    args = parser.parse_args()
    course = args.repo / "course/mit-mmai-2026"
    sessions = read_json(course / "catalog.json")["sessions"]
    results = []
    for session in sessions:
        url = session.get("video_url")
        if not url:
            continue
        parts = urlsplit(url)
        video_id = parts.path.lstrip("/") if parts.hostname == "youtu.be" else parse_qs(parts.query)["v"][0]
        if args.video_id and video_id not in args.video_id:
            continue
        directory = args.repo / ".work/transcripts" / video_id
        try:
            english = read_json(directory / "data/blocks.en.json")
            chinese = read_json(directory / "data/blocks.zh-CN.json")
            result = audit_blocks(english, chinese)
            if args.require_artifacts and not result["errors"]:
                published = audit_artifacts(course / session["id"], english, chinese, video_id)
                result["errors"].extend(published["errors"])
                result["artifact_sha256"] = published["artifact_sha256"]
        except (OSError, ValueError, KeyError, TypeError) as error:
            result = {"errors": [str(error)], "advisories": []}
        result.update(session_id=session["id"], video_id=video_id)
        results.append(result)
    report = {
        "checked_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "scope": "Structural checks plus semantic-review heuristics; not a semantic correctness certificate",
        "sessions": results,
        "error_count": sum(len(result["errors"]) for result in results),
        "advisory_count": sum(len(result["advisories"]) for result in results),
    }
    if not results:
        report["error_count"] += 1
        report["error"] = "No matching video sessions"
    rendered = json.dumps(report, ensure_ascii=False, indent=2) + "\n"
    if args.report:
        args.report.parent.mkdir(parents=True, exist_ok=True)
        args.report.write_text(rendered, encoding="utf-8")
    print(rendered)
    return 1 if report["error_count"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
