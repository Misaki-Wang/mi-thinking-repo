#!/usr/bin/env python3
"""Estimate transcript paragraph/slide associations without inventing timestamps.

Uses PDF text, local English paragraphs, and an order-constrained lexical path.
This is retrieval guidance, not frame-level video alignment. Unsupported text,
visual-only pages, and indistinguishable slide builds deliberately remain null.
No external libraries, models, or network calls are required.
"""

import argparse
from collections import Counter
import hashlib
import html
import json
import math
from pathlib import Path
import re
import unicodedata
from urllib.parse import parse_qs, urlparse

VERSION = "lexical-sequence-v1"
STOP = set("""a an the and or of to in on with for from by as is are was were be been
being it its this that these those i we you he she they them our your their my his
her me us so if then than but not no yes can could will would should do does did
have has had having just about also how what which who when where why all any
each some more most very really right okay ok um uh like know think see say said
want going go get got let lets here there now one two three first second third
many much such both into out up down over even still thing things something
other same different example examples look looking shown show shows using use
used uses need needs make makes take taking given actually kind lot lots sort
able may might well good better point part bit time way new say come comes
et al pp page lecture course mit liang paul professor assistant media lab eecs
https http www com org edu github io doi original slide developed credit credits
work based essentially basically means mean question questions folks welcome
back today pretty sure instead little something sometimes already every across
only through because while whether either those e.g eg etc such itself themselves
""".split())
RECAP_DECKS = {"w04-2": ["w04-1"], "w05-1": ["w04-2"]}
# These are topic-navigation observations in the existing preview, not exact
# transition timestamps. Restrict only ranges explicitly absent from the video.
SLIDE_ONLY_AFTER = {"w14-2": 65}
# Start-page hints already present in each chapter's source-linked preview.
# They are deliberately coarse: a 90-second tolerance and one preceding page
# prevent treating these topic links as exact slide-transition timestamps.
TOPIC_HINTS = {
    "w01-1": [(2789, 40), (3099, 43), (4044, 54)],
    "w01-2": [(283, 3), (558, 7), (2867, 28), (3620, 37)],
    "w02-2": [(858, 15), (2015, 28), (2486, 32), (2595, 34), (2763, 36)],
    "w04-1": [(841, 10), (954, 14), (1288, 18), (1512, 19), (1816, 23)],
    "w04-2": [(2041, 4), (2345, 6), (3648, 13), (4048, 17)],
    "w05-1": [(2149, 5), (3434, 18), (3806, 23)],
    "w06-1": [(1378, 8), (3008, 20), (3221, 22)],
    "w06-2": [(3017, 24), (3946, 30)],
    "w09-1": [(642, 6), (2255, 20), (3393, 35), (3772, 39)],
    "w10-1": [(2016, 14), (2671, 21), (3402, 31), (3664, 36), (3904, 38), (4142, 49)],
    "w10-2": [(114, 3), (452, 6), (1622, 13), (3052, 22), (3431, 33)],
    "w14-1": [(482, 3), (1690, 24), (3295, 40), (4010, 53), (4397, 61)],
    "w14-2": [(284, 5), (1137, 12), (1626, 16), (2737, 57)],
}
MIN_SCORE = 0.13


def sha256(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def tokens(text):
    text = unicodedata.normalize("NFKC", html.unescape(text)).lower()
    text = re.sub(r"https?://\S+", " ", text)
    text = re.sub(r"\[[^\]\n]{3,}\]", " ", text)
    for old, new in ((r"multi[ -]+modal", "multimodal"),
                     (r"cross[ -]+modal", "crossmodal"),
                     (r"co[ -]+learning", "colearning"),
                     (r"info[ -]+nce", "infonce")):
        text = re.sub(old, new, text)
    words = re.findall(r"[a-z][a-z0-9]*", text)
    result = []
    for word in words:
        if word in STOP or len(word) < 3:
            continue
        # Only light, transparent inflection normalization; keep acronyms.
        if word.endswith("ies") and len(word) > 5:
            word = word[:-3] + "y"
        elif word.endswith("s") and not word.endswith(("ss", "is", "us")) and len(word) > 4:
            word = word[:-1]
        if word not in STOP:
            result.append(word)
    return result


def features(words):
    result = Counter(words)
    for left, right in zip(words, words[1:]):
        result[left + " " + right] += 0.7
    return result


def is_frontmatter(text):
    return bool(re.search(r"assignments for|today.?s lecture|lecture outline|multimodal ai\s+lecture", text, re.I))


def vectorize(counts, idf):
    vector = {term: (1 + math.log(value)) * idf.get(term, 1)
              for term, value in counts.items() if value > 0}
    norm = math.sqrt(sum(value * value for value in vector.values()))
    return {term: value / norm for term, value in vector.items()} if norm else {}


def build_retrieval(blocks, pages):
    page_words = [tokens(page["text"]) for page in pages]
    page_features = [features(words) for words in page_words]
    frequency = Counter(term for counts in page_features for term in counts)
    idf = {term: 1 + math.log((len(pages) + 1) / (count + 1))
           for term, count in frequency.items()}
    page_vectors = [vectorize(counts, idf) for counts in page_features]
    # Very frequent content words should not make a short generic heading an
    # apparently precise match. Terms still remain available as evidence.
    common = {term for term, count in frequency.items()
              if " " not in term and count > max(8, len(pages) * 0.55)}
    block_words = [tokens(block["text"]) for block in blocks]
    block_vectors = [vectorize(features(words), idf) for words in block_words]
    scores = []
    for vector in block_vectors:
        scores.append([sum(weight * vector.get(term, 0) for term, weight in slide.items())
                       for slide in page_vectors])
    evidence = []
    for words in block_words:
        found = set(words)
        evidence.append([sorted((found & set(slide)) - common,
                                key=lambda word: (-idf.get(word, 1), word))[:12]
                         for slide in page_words])
    return scores, evidence, page_words


def sequence_path(scores, eligible, minimum=MIN_SCORE):
    """Best supported nondecreasing page path with optional unmatched blocks.

    State is the last associated slide, not elapsed time. Arbitrary page skips
    cost no more than any other page transition; staying is legal. A null block
    does not move the slide frontier. No duration/proportional page assumption.
    """
    width = len(eligible) + 1
    previous = [0.0] + [-math.inf] * (width - 1)
    backtrace = []
    for row in scores:
        current = previous.copy()
        parents = [(index, None) for index in range(width)]
        prefix_value, prefix_state = previous[0], 0
        for index, allowed in enumerate(eligible):
            state = index + 1
            # A small continuity preference breaks weak local ties, but is
            # intentionally below a meaningful lexical score difference.
            from_value, from_state = prefix_value - 0.015, prefix_state
            if previous[state] > from_value:
                from_value, from_state = previous[state], state
            if allowed and row[index] >= minimum:
                value = from_value + row[index] - minimum
                if value > current[state]:
                    current[state] = value
                    parents[state] = (from_state, index)
            if previous[state] > prefix_value:
                prefix_value, prefix_state = previous[state], state
        previous = current
        backtrace.append(parents)
    state = max(range(width), key=lambda index: previous[index])
    path = []
    for parents in reversed(backtrace):
        state, selected = parents[state]
        path.append(selected)
    return list(reversed(path))


def align(blocks, pages, session_id=None, topic_hints=()):
    scores, evidence, page_words = build_retrieval(blocks, pages)
    qualities = []
    for page, words in zip(pages, page_words):
        if page.get("slide_only"):
            qualities.append("slide-only")
        elif is_frontmatter(page["text"]):
            qualities.append("frontmatter")
        elif len(set(words)) < 5:
            qualities.append("sparse-text")
        else:
            qualities.append("text")
    duplicate_groups = {}
    for index, words in enumerate(page_words):
        signature = tuple(sorted(set(words)))
        duplicate_groups.setdefault(signature, []).append(index)
    duplicate_ids = {index: group for group in duplicate_groups.values()
                     if len(group) > 1 for index in group}
    allowed = [quality == "text" and index not in duplicate_ids
               for index, quality in enumerate(qualities)]
    # Disqualify local low-evidence matches before sequence optimization, so
    # unrelated paragraphs cannot ratchet the frontier forward accidentally.
    local_scores = [[score if len(evidence[bi][pi]) >= 3 else 0.0
                     for pi, score in enumerate(row)] for bi, row in enumerate(scores)]
    for bi, block in enumerate(blocks):
        elapsed = block.get("start_ms", 0) / 1000
        lower = max((page - 1 for seconds, page in topic_hints if elapsed >= seconds + 90), default=0)
        if lower:
            for pi, page in enumerate(pages):
                if page["deck_id"] != session_id or page["page"] < lower:
                    local_scores[bi][pi] = 0.0
    path = sequence_path(local_scores, allowed)
    aligned = []
    for bi, (block, selected) in enumerate(zip(blocks, path)):
        row = scores[bi]
        ranking = sorted((i for i, p in enumerate(pages) if not p.get("slide_only")),
                         key=lambda i: (-row[i], i))
        candidate_indices = ranking[:4]
        if selected is not None and selected not in candidate_indices:
            candidate_indices.append(selected)
        candidates = [{"slide_id": pages[index]["slide_id"],
                       "score": round(row[index], 4),
                       "evidence_terms": evidence[bi][index],
                       "text_quality": qualities[index]}
                      for index in candidate_indices if row[index] >= 0.07]
        confidence, reason = "unmatched", "No supported sequential text match."
        ambiguous = []
        if selected is not None:
            score = row[selected]
            others = [i for i in ranking if i != selected and qualities[i] == "text"]
            near = [i for i in others if abs(row[i] - score) <= 0.022
                    and (abs(i - selected) <= 3 or
                         len(set(page_words[i]) & set(page_words[selected])) /
                         max(1, len(set(page_words[i]) | set(page_words[selected]))) >= 0.7)]
            # A sequence tie cannot resolve indistinguishable slide builds.
            for index in near:
                distinctive = (set(page_words[selected]) - set(page_words[index])) & set(tokens(block["text"]))
                if len(distinctive) < 2:
                    ambiguous.append(pages[index]["slide_id"])
            if ranking and ranking[0] in duplicate_ids and row[ranking[0]] >= score + 0.035:
                ambiguous = [pages[i]["slide_id"] for i in duplicate_ids[ranking[0]]]
                selected, reason = None, "Duplicate slide builds have stronger evidence than the sequence candidate."
            elif ambiguous:
                ambiguous.append(pages[selected]["slide_id"])
                selected, reason = None, "Similar adjacent/build slides; text cannot identify one page."
            elif ranking and score < row[ranking[0]] * 0.65:
                selected, reason = None, "Sequence candidate conflicts with substantially stronger text evidence."
            else:
                margin = score - max((row[i] for i in others), default=0)
                confidence = "estimated" if score >= 0.23 and margin >= 0.025 and len(evidence[bi][selected]) >= 5 else "weak"
                reason = "Lexical evidence with page-order context; not video-frame verification."
        if selected is None and ranking and ranking[0] in duplicate_ids:
            ambiguous = [pages[i]["slide_id"] for i in duplicate_ids[ranking[0]]]
            reason = "Duplicate extracted text; exact slide build is unsupported."
        aligned.append({"block_id": block["block_id"],
                        "start_ms": block.get("start_ms"), "end_ms": block.get("end_ms"),
                        "slide_id": pages[selected]["slide_id"] if selected is not None else None,
                        "score": round(row[selected], 4) if selected is not None else None,
                        "confidence": confidence,
                        "evidence_terms": evidence[bi][selected] if selected is not None else [],
                        "reason": reason,
                        "ambiguity_slide_ids": sorted(set(ambiguous)),
                        "candidates": candidates})
    slide_info = [{"slide_id": page["slide_id"], "deck_id": page["deck_id"],
                   "page": page["page"], "text_quality": qualities[index],
                   "duplicate_group": [pages[i]["slide_id"] for i in duplicate_ids.get(index, [])]}
                  for index, page in enumerate(pages)]
    return aligned, slide_info


def video_id(url):
    parsed = urlparse(url)
    return parsed.path.strip("/") if parsed.netloc == "youtu.be" else parse_qs(parsed.query)["v"][0]


def run(root, only=None):
    catalog_path = root / "course/mit-mmai-2026/catalog.json"
    catalog = json.loads(catalog_path.read_text())
    directory = root / "reader/mit-mmai-2026/alignments"
    directory.mkdir(parents=True, exist_ok=True)
    report = []
    for session in catalog["sessions"]:
        sid = session["id"]
        if not session.get("video_url") or (only and sid not in only):
            continue
        block_path = root / ".work/transcripts" / video_id(session["video_url"]) / "data/blocks.en.json"
        if not block_path.exists():
            raise FileNotFoundError(block_path)
        blocks = json.loads(block_path.read_text())
        decks = RECAP_DECKS.get(sid, []) + [sid]
        pages, sources = [], []
        for deck in decks:
            source = root / ".work/sources" / deck / "slides-pages.json"
            content = json.loads(source.read_text())
            sources.append({"deck_id": deck, "path": str(source.relative_to(root)),
                            "sha256": sha256(source), "source_url": content["source_url"]})
            for page in content["pages"]:
                pages.append({**page, "deck_id": deck,
                              "slide_id": f"{deck}-p{page['page']:03}",
                              "slide_only": deck == sid and page["page"] > SLIDE_ONLY_AFTER.get(sid, math.inf)})
        hints = TOPIC_HINTS.get(sid, [])
        aligned, slide_info = align(blocks, pages, sid, hints)
        preview = root / "course/mit-mmai-2026" / sid / "preview.md"
        summary = dict(Counter(item["confidence"] for item in aligned))
        summary.update({"total_blocks": len(blocks), "total_slides": len(pages),
                        "associated_slides": len({item["slide_id"] for item in aligned if item["slide_id"]}),
                        "recap_blocks": sum(bool(item["slide_id"] and not item["slide_id"].startswith(sid)) for item in aligned)})
        result = {"schema_version": 1, "session_id": sid, "deck_ids": decks,
                  "method": {"id": VERSION, "description": "TF-IDF word/term-bigram cosine retrieval with optional unmatched paragraphs, monotonic slide-order context, and coarse source-linked preview topic hints; no proportional time mapping.",
                             "topic_hints": [{"start_seconds": second, "start_page": page} for second, page in hints],
                             "topic_hint_tolerance_seconds": 90,
                             "confidence_note": "Estimated and weak are qualitative evidence labels, not calibrated probabilities or verified video timestamps.",
                             "synchronization_note": "Only non-null slide_id associations drive automatic synchronization; candidate pages are suggestions for manual inspection.",
                             "limits": ["A paragraph may span multiple slides.", "Image-only, duplicate builds, questions, and unlectured pages can be unmatched.", "Monotonic content order may leave revisited pages unmatched."]},
                  "provenance": {"transcript_path": str(block_path.relative_to(root)),
                                 "transcript_sha256": sha256(block_path), "video_url": session["video_url"],
                                 "english_markdown_path": f"course/mit-mmai-2026/{sid}/transcript.en.md",
                                 "english_markdown_sha256": sha256(root / "course/mit-mmai-2026" / sid / "transcript.en.md"),
                                 "catalog_sha256": sha256(catalog_path), "slides": sources,
                                 "preview_path": str(preview.relative_to(root)), "preview_sha256": sha256(preview),
                                 "script_sha256": sha256(Path(__file__))},
                  "summary": summary, "blocks": aligned, "slides": slide_info}
        (directory / f"{sid}.json").write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n")
        report.append({"session_id": sid, **summary,
                       "spot_checks": [{"block_id": block["block_id"], "start_seconds": round(block["start_ms"] / 1000, 1),
                                        "text_excerpt": block["text"][:200],
                                        "slide_id": item["slide_id"], "confidence": item["confidence"],
                                        "candidates": item["candidates"][:2]}
                                       for block, item in zip(blocks, aligned)
                                       if int(block["block_id"][1:]) % 12 == 1]})
        print(sid, json.dumps(summary))
    (root / ".work/alignment-qa.json").write_text(json.dumps({"method": VERSION, "sessions": report}, ensure_ascii=False, indent=2) + "\n")
    return report


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--session", action="append")
    args = parser.parse_args()
    run(args.root.resolve(), args.session)
