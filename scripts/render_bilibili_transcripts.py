#!/usr/bin/env python3
"""Render local normalized ASR JSON as auditable, timestamped Chinese Markdown.

No network, inference, translation, speaker attribution, or publication occurs.
Raw segment text is never corrected, deduplicated, or discarded. The ignored
.work directory is the default destination; --output-root supports a separately
authorized export. Run from anywhere; default paths resolve from this repository.
"""

from __future__ import annotations

import argparse
from collections import Counter
from datetime import datetime, timezone
import hashlib
import html
import json
import math
from pathlib import Path
import re
import tempfile

REPO = Path(__file__).resolve().parents[1]
WORK = REPO / ".work" / "bilibili-280780745"
BVID = re.compile(r"BV[0-9A-Za-z]{10}\Z")
SENTENCE_END = re.compile(r"[。！？.!?][\s\"'”’）)]*\Z")
THRESHOLDS = {
    "minimum_paragraph_seconds": 30,
    "target_maximum_paragraph_seconds": 60,
    "gap_seconds": 30,
    # Only warning comparisons allow codec/resampling rounding; raw times never change.
    "timestamp_tolerance_seconds": 0.001,
    "compression_ratio": 2.4,
    "avg_logprob": -1.0,
    "no_speech_prob": 0.6,
}


def read_json(path: Path) -> object:
    def reject_constant(value: str) -> None:
        raise ValueError(f"Non-finite JSON value: {value}")

    def reject_duplicates(pairs: list[tuple[str, object]]) -> dict:
        result = {}
        for key, value in pairs:
            if key in result:
                raise ValueError(f"Duplicate JSON key: {key}")
            result[key] = value
        return result

    try:
        return json.loads(
            path.read_text(encoding="utf-8"),
            parse_constant=reject_constant,
            object_pairs_hook=reject_duplicates,
        )
    except (json.JSONDecodeError, UnicodeError, ValueError) as exc:
        raise ValueError(f"Invalid JSON in {path}: {exc}") from exc


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def finite_number(value: object, label: str) -> float:
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise ValueError(f"{label} must be a finite number")
    if not math.isfinite(value):
        raise ValueError(f"{label} must be a finite number")
    return float(value)


def validate_raw(raw: object) -> list[dict]:
    if not isinstance(raw, dict):
        raise ValueError("ASR JSON must be an object")
    for key in ("text", "language", "model", "timestamp_kind"):
        if key in raw and not isinstance(raw[key], str):
            raise ValueError(f"ASR {key} must be a string when present")
    if raw.get("timestamp_kind", "asr_segment") not in {"asr_segment", "audio_chunk"}:
        raise ValueError("ASR timestamp_kind must be asr_segment or audio_chunk")
    segments = raw.get("segments")
    if not isinstance(segments, list) or not segments:
        raise ValueError("ASR JSON must contain a nonempty segments list")
    for index, segment in enumerate(segments):
        if not isinstance(segment, dict) or not isinstance(segment.get("text"), str):
            raise ValueError(f"segments[{index}] must contain string text")
        if "id" in segment and (isinstance(segment["id"], bool)
                                or not isinstance(segment["id"], int) or segment["id"] < 0):
            raise ValueError(f"segments[{index}].id must be a nonnegative integer when present")
        if "padding_samples" in segment and (isinstance(segment["padding_samples"], bool)
                                             or not isinstance(segment["padding_samples"], int)
                                             or segment["padding_samples"] < 0):
            raise ValueError(f"segments[{index}].padding_samples must be a nonnegative integer when present")
        start = finite_number(segment.get("start"), f"segments[{index}].start")
        end = finite_number(segment.get("end"), f"segments[{index}].end")
        if end < start:
            raise ValueError(f"segments[{index}].end precedes its start")
        for key in ("avg_logprob", "compression_ratio", "no_speech_prob"):
            if key in segment:
                finite_number(segment[key], f"segments[{index}].{key}")
    return segments


def group_segments(segments: list[dict]) -> list[dict]:
    """Use original segment boundaries; even empty segments remain attributable."""
    groups: list[dict] = []
    pending: list[tuple[int, dict]] = []

    def flush() -> None:
        if not pending:
            return
        groups.append({
            "block_id": f"b{len(groups) + 1:06d}",
            "start": pending[0][1]["start"],
            "end": max(segment["end"] for _, segment in pending),
            "start_ms": round(pending[0][1]["start"] * 1000),
            "end_ms": round(max(segment["end"] for _, segment in pending) * 1000),
            "text": "".join(segment["text"] for _, segment in pending),
            "raw_segment_indices": [index for index, _ in pending],
            "raw_segment_ids": [segment.get("id") for _, segment in pending],
            "segments": [dict(segment) for _, segment in pending],
        })
        pending.clear()

    for index, segment in enumerate(segments):
        if pending:
            span = segment["end"] - pending[0][1]["start"]
            gap = segment["start"] - pending[-1][1]["end"]
            if span > 60 or gap >= THRESHOLDS["gap_seconds"]:
                flush()
        pending.append((index, segment))
        span = segment["end"] - pending[0][1]["start"]
        if span >= 60 or (span >= 30 and SENTENCE_END.search(segment["text"])):
            flush()
    flush()
    return groups


def audit_accounting(segments: list[dict], paragraphs: list[dict]) -> dict:
    indices = [index for item in paragraphs for index in item["raw_segment_indices"]]
    recovered = [segment for item in paragraphs for segment in item["segments"]]
    raw_text = "".join(segment["text"] for segment in segments)
    grouped_text = "".join(item["text"] for item in paragraphs)
    exact = indices == list(range(len(segments))) and recovered == segments
    return {
        "raw_segment_count": len(segments),
        "accounted_segment_count": len(indices),
        "all_segments_accounted_once_in_original_order": exact,
        "all_segment_fields_preserved": recovered == segments,
        "all_text_preserved_exactly": raw_text == grouped_text,
        "raw_text_sha256": hashlib.sha256(raw_text.encode("utf-8")).hexdigest(),
        "paragraph_text_sha256": hashlib.sha256(grouped_text.encode("utf-8")).hexdigest(),
        "paragraph_count": len(paragraphs),
    }


def quality_report(segments: list[dict], duration: float, *, timestamp_kind: str = "asr_segment") -> dict:
    advisories: list[dict] = []

    def flag(kind: str, message: str, indices: list[int] | None = None, **details) -> None:
        item = {"kind": kind, "message": message, **details}
        if indices is not None:
            item["raw_segment_indices"] = indices
        advisories.append(item)

    normalized = []
    seen_ids: dict[int, int] = {}
    for index, segment in enumerate(segments):
        if "id" in segment:
            if segment["id"] in seen_ids:
                flag("duplicate_segment_id", "原始片段 ID 重复，以原始数组位置区分保留。",
                     [seen_ids[segment["id"]], index], source_id=segment["id"])
            else:
                seen_ids[segment["id"]] = index
        text = segment["text"]
        cleaned = re.sub(r"[\W_]+", "", text, flags=re.UNICODE)
        normalized.append(cleaned)
        if not text.strip():
            flag("empty_segment", "片段未识别出文字，原记录保留。", [index])
        tolerance = THRESHOLDS["timestamp_tolerance_seconds"]
        if segment["start"] < -tolerance or segment["end"] > duration + tolerance:
            flag("timestamp_outside_audio", "时间戳超出参考音频范围（已允许 1 毫秒编码/重采样舍入误差），未截断。", [index],
                 start=segment["start"], end=segment["end"], duration=duration)
        if (timestamp_kind == "audio_chunk" and segment["end"] - segment["start"] < 1
                and segment.get("padding_samples", 0) > 0 and text.strip()):
            flag("padded_short_audio_text",
                 "极短音频经过补零，以下识别文字可能是静音幻觉，未确认为原视频发言。",
                 [index], duration_seconds=segment["end"] - segment["start"],
                 padding_samples=segment["padding_samples"])
        if segment["start"] == segment["end"] and text.strip():
            flag("zero_duration_text", "有文字的片段时长为零。", [index])
        if segment["end"] - segment["start"] > 60:
            if timestamp_kind == "audio_chunk":
                flag("intended_chunk_duration_over60",
                     "音频分块超过 60 秒；按低能量位置分块时边界可适当延长，此提示不代表模型识别错误。",
                     [index], duration_seconds=segment["end"] - segment["start"])
            else:
                flag("long_segment", "原始片段超过 60 秒，未人为拆分时间戳。", [index])
        if index and segment["start"] < segments[index - 1]["start"]:
            flag("nonmonotonic_timestamps", "时间戳发生回退，仍保持原始片段顺序。", [index - 1, index])
        if index and segment["start"] < segments[index - 1]["end"] - 0.5:
            flag("overlapping_timestamps", "相邻片段时间戳重叠超过 0.5 秒。", [index - 1, index])
        if (re.search(r"(.{2,60}?)\1{3,}", cleaned[:20000]) or
                re.search(r"(.)\1{14,}", cleaned[:20000])):
            flag("repetition_within_segment", "片段包含长串重复，可能为 ASR 重复，需回听。", [index])
        for key, comparison, message in (
            ("avg_logprob", lambda value: value < THRESHOLDS["avg_logprob"],
             "Whisper 平均 log probability 偏低。"),
            ("compression_ratio", lambda value: value > THRESHOLDS["compression_ratio"],
             "Whisper compression ratio 偏高，可能存在重复。"),
            ("no_speech_prob", lambda value: value > THRESHOLDS["no_speech_prob"] and bool(text.strip()),
             "Whisper no-speech probability 偏高，但输出了文字。"),
        ):
            if key in segment and comparison(segment[key]):
                flag(f"suspicious_{key}", message, [index], value=segment[key])

    run_start = 0
    for index in range(1, len(normalized) + 1):
        if index < len(normalized) and normalized[index] == normalized[run_start]:
            continue
        if index - run_start >= 3 and len(normalized[run_start]) >= 4:
            flag("repeated_consecutive_segments", "连续三个或更多片段文字相同，需回听。",
                 list(range(run_start, index)))
        run_start = index

    # Interval coverage describes timestamps, not speech accuracy or completeness.
    intervals = sorted((max(0.0, float(item["start"])), min(duration, float(item["end"])))
                       for item in segments if item["text"].strip()
                       and item["end"] > 0 and item["start"] < duration)
    merged: list[list[float]] = []
    for start, end in intervals:
        if end <= start:
            continue
        if merged and start <= merged[-1][1]:
            merged[-1][1] = max(merged[-1][1], end)
        else:
            merged.append([start, end])
    cursor = 0.0
    gaps = []
    for start, end in merged + [[duration, duration]]:
        if start - cursor >= THRESHOLDS["gap_seconds"]:
            gap = {"start": cursor, "end": start, "seconds": start - cursor}
            gaps.append(gap)
            flag("uncovered_interval", "无文字时间区间可能是静音、音乐或漏识别；尚未回听。", **gap)
        cursor = max(cursor, end)
    covered = sum(end - start for start, end in merged)
    return {
        "advisories": advisories,
        "thresholds": dict(THRESHOLDS),
        "interval_coverage": {
            "reference_duration_seconds": duration,
            "nonempty_segment_union_seconds": round(covered, 6),
            "ratio": round(covered / duration, 6),
            "gaps_at_least_30_seconds": gaps,
            "interpretation": "Timestamp coverage only; silence and missing speech are not distinguished.",
        },
        "semantic_accuracy": "not_assessed",
        "speaker_attribution": "not_performed",
        "technical_term_correction": "not_performed; original ASR spelling retained",
    }


def markdown_text(text: str) -> str:
    escaped = html.escape(text, quote=False)
    # Keep text literal when fed into the existing website's Markdown renderer.
    escaped = re.sub(r"([\\`*_{}\[\]#!|~])", r"\\\1", escaped)
    escaped = re.sub(r"(?m)^(\s*)([-+])(?=\s)", r"\1\\\2", escaped)
    return re.sub(r"(?m)^(\s*\d+)\.(?=\s)", r"\1\\.", escaped)


def timestamp(seconds: float) -> str:
    sign = "−" if seconds < 0 else ""
    total = math.floor(abs(seconds))
    hours, remainder = divmod(total, 3600)
    minutes, seconds = divmod(remainder, 60)
    return f"{sign}{hours:02d}:{minutes:02d}:{seconds:02d}"


def render_markdown(metadata: dict, paragraphs: list[dict], report: dict) -> str:
    advisories = report["advisories"]
    counts = Counter(item["kind"] for item in advisories)
    padded_short_indices = {index for item in advisories if item["kind"] == "padded_short_audio_text"
                            for index in item.get("raw_segment_indices", [])}
    lines = [
        f"# {markdown_text(metadata['title'])}", "",
        "> 原始 ASR 自动转写初稿，尚未逐句人工校对。ASR 可能误识别人名、英文名称、专业术语与数字。", "",
        *(["> 时间戳为连续音频分块起点（约1分钟），不是逐字对齐；点击回到该片段开始。", ""]
          if metadata.get("timestamp_kind") == "audio_chunk" else []),
        f"- UP 主：{markdown_text(metadata['author'])}",
        f"- 发布日期：{markdown_text(str(metadata['published_at']))}",
        f"- 原视频：[Bilibili · {metadata['bvid']}]({metadata['source_url']})",
        f"- BVID：`{metadata['bvid']}`；CID：`{metadata['cid']}`",
        f"- 参考时长：{timestamp(metadata['duration_seconds'])}"
        f"（{metadata['duration_source']}）",
        f"- 识别：{markdown_text(metadata['asr_provider'])} / "
        f"{markdown_text(str(metadata['asr_model']))}；语言：{markdown_text(str(metadata['language']))}",
        f"- 原始片段：{report['accounting']['raw_segment_count']}；"
        f"阅读段落：{len(paragraphs)}；全部原始片段按原顺序保留。", "",
        "专业术语保留 ASR 原始写法；未根据标题猜测改写，未推测发言者身份。"
        "下列质量提示是自动检查信号，不代表已确认错误；时间戳覆盖率不代表转写准确率。", "",
        "## 自动质量检查", "",
    ]
    if counts:
        for kind, count in sorted(counts.items()):
            line = f"- `{kind}`：{count} 处"
            if kind == "intended_chunk_duration_over60":
                line += "。音频按低能量位置分块，边界可适当延长；这些是分块时长记录，不是已确认的识别错误。"
            lines.append(line)
    else:
        lines.append("未触发当前规则的质量提示；这不等于语义已经校验。")
    lines += ["", "详细时间区间、片段编号与校验值保存在本地 `validation.json`；公开稿不附原始识别日志。", "",
              "## 时间戳讲稿", ""]
    for paragraph in paragraphs:
        start = paragraph["start"]
        # Never generate a negative playback offset; original timestamp is retained above.
        jump = max(0, math.floor(start))
        url = f"{metadata['source_url']}?t={jump}&cid={metadata['cid']}"
        lines += [f"### [{timestamp(start)}]({url}) · {paragraph['block_id']}", ""]
        text = markdown_text(paragraph["text"])
        flagged_indices = sorted(padded_short_indices.intersection(paragraph["raw_segment_indices"]))
        if flagged_indices:
            lines += [f"> 编辑风险提示（原始片段索引 {', '.join(map(str, flagged_indices))}）："
                      "极短音频经过补零，以下识别文字可能是静音幻觉，未确认为原视频发言。", ""]
        lines += [text if text.strip() else "> [编辑标记：本段原始 ASR 文本为空。]", ""]
    return "\n".join(lines).rstrip() + "\n"


def write_atomic(path: Path, value: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile(mode="w", encoding="utf-8", dir=path.parent,
                                     prefix=path.name + ".", suffix=".tmp", delete=False) as handle:
        temporary = Path(handle.name)
        try:
            handle.write(value)
        except BaseException:
            temporary.unlink(missing_ok=True)
            raise
    try:
        temporary.replace(path)
    finally:
        temporary.unlink(missing_ok=True)


def serialize(value: object) -> str:
    return json.dumps(value, ensure_ascii=False, indent=2, allow_nan=False) + "\n"


def provenance_path(path: Path) -> str:
    try:
        return str(path.resolve().relative_to(REPO))
    except ValueError:
        return str(path.resolve())


def render_video(video: dict, raw_path: Path, output: Path, *, model: str | None = None,
                 provider: str = "openai-whisper",
                 audio_path: Path | None = None, audio_duration: float | None = None) -> dict:
    if not isinstance(provider, str) or not provider.strip():
        raise ValueError("ASR provider must be a nonempty string")
    if model is not None and (not isinstance(model, str) or not model.strip()):
        raise ValueError("ASR model must be a nonempty string when provided")
    bvid = video.get("bvid")
    if not isinstance(bvid, str) or not BVID.fullmatch(bvid):
        raise ValueError("Invalid BVID in inventory")
    cid = video.get("cid")
    if isinstance(cid, bool) or not isinstance(cid, int) or cid <= 0:
        raise ValueError(f"{bvid}: inventory CID must be a positive integer")
    if not isinstance(video.get("title"), str) or not video["title"].strip():
        raise ValueError(f"{bvid}: inventory requires a title")
    parts = video.get("parts", [])
    if len(parts) > 1:
        raise ValueError(f"{bvid}: multipart video requires one CID-specific input per part")
    duration_value = audio_duration if audio_duration is not None else video.get("playback_duration")
    if duration_value is None:
        duration_value = video.get("duration")
    duration = finite_number(duration_value, f"{bvid} duration")
    if duration <= 0:
        raise ValueError(f"{bvid}: duration must be positive")
    raw = read_json(raw_path)
    segments = validate_raw(raw)
    if "provider" in raw and raw["provider"] != provider:
        raise ValueError(f"{bvid}: --provider does not match the provider recorded in ASR JSON")
    recorded_audio = raw.get("audio_provenance", {})
    recorded_audio_hash = None
    if isinstance(recorded_audio, dict) and "source_sha256" in recorded_audio:
        recorded_audio_hash = recorded_audio["source_sha256"]
        if (not isinstance(recorded_audio_hash, str)
                or not re.fullmatch(r"[0-9a-fA-F]{64}", recorded_audio_hash)):
            raise ValueError(f"{bvid}: recorded audio source_sha256 must be a valid SHA-256")
    actual_audio_hash = sha256(audio_path) if audio_path is not None and audio_path.is_file() else None
    if recorded_audio_hash is not None:
        if actual_audio_hash is None:
            raise ValueError(f"{bvid}: audio file is required to verify recorded source_sha256")
        if actual_audio_hash != recorded_audio_hash.lower():
            raise ValueError(f"{bvid}: audio file hash does not match recorded source_sha256")
    timestamp_kind = raw.get("timestamp_kind", "asr_segment")
    paragraphs = group_segments(segments)
    accounting = audit_accounting(segments, paragraphs)
    if not (accounting["all_segments_accounted_once_in_original_order"] and
            accounting["all_text_preserved_exactly"]):
        raise RuntimeError("Internal accounting failure; refusing to render incomplete text")
    report = quality_report(segments, duration, timestamp_kind=timestamp_kind)
    report["accounting"] = accounting
    asr_model = model or raw.get("model") or "not recorded"
    if asr_model == "not recorded":
        report["advisories"].append({"kind": "model_not_recorded", "message": "原始 JSON 不含模型名称，请提供 --model。"})
    language = raw.get("language", "not recorded")
    if language not in {"zh", "Chinese", "chinese", "cmn", "zh-CN"}:
        report["advisories"].append({"kind": "unexpected_or_missing_language", "message": "原始 JSON 的语言不是已知中文标记。"})
    if isinstance(raw.get("text"), str) and raw["text"].strip() != "".join(item["text"] for item in segments).strip():
        report["advisories"].append({"kind": "top_level_text_mismatch", "message": "JSON 顶层 text 与片段拼接结果不同；以有时间戳片段为准，原 JSON 保留。"})
    metadata = {
        "schema_version": 1,
        "bvid": bvid,
        "cid": cid,
        "title": video["title"],
        "author": video.get("uploader", "not recorded"),
        "author_id": str(video.get("uploader_id", "")),
        "published_at": video.get("published_at", video.get("upload_date", "not recorded")),
        "publication_timestamp": video.get("timestamp"),
        "source_url": f"https://www.bilibili.com/video/{bvid}/",
        "duration_seconds": duration,
        "duration_source": "measured audio duration" if audio_duration is not None else "upstream playback/video metadata",
        "asr_provider": provider,
        "asr_model": asr_model,
        "language": language,
        "timestamp_kind": timestamp_kind,
        "generated_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "raw_provenance": {"path": provenance_path(raw_path), "sha256": sha256(raw_path)},
        "audio_provenance": ({"path": provenance_path(audio_path), "sha256": actual_audio_hash}
                             if actual_audio_hash is not None else None),
        "text_policy": "verbatim ASR segment text; no rewriting, translation, deduplication, or inferred speakers",
    }
    report["metadata"] = metadata
    report["schema_version"] = 1
    report["status"] = "review_required" if report["advisories"] else "structurally_valid_unreviewed"
    paragraphs_json = serialize({"schema_version": 1, "metadata": metadata, "paragraphs": paragraphs})
    markdown = render_markdown(metadata, paragraphs, report)
    report["output_hashes"] = {
        "transcript.zh-CN.md": hashlib.sha256(markdown.encode("utf-8")).hexdigest(),
        "data/paragraphs.json": hashlib.sha256(paragraphs_json.encode("utf-8")).hexdigest(),
    }
    write_atomic(output / "data" / "paragraphs.json", paragraphs_json)
    write_atomic(output / "transcript.zh-CN.md", markdown)
    write_atomic(output / "validation.json", serialize(report))
    return report


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--inventory", type=Path, default=WORK / "inventory.json")
    parser.add_argument("--asr-root", type=Path, default=WORK / "asr")
    parser.add_argument("--audio-root", type=Path, default=WORK / "audio")
    parser.add_argument("--output-root", type=Path, default=WORK / "transcripts")
    parser.add_argument("--bvid", action="append", help="Render selected BVIDs; repeatable. Default: entire inventory.")
    parser.add_argument("--provider", default="openai-whisper",
                        help="Actual ASR provider/engine, default: openai-whisper")
    parser.add_argument("--model", help="Actual model recorded by the ASR execution, e.g. turbo")
    parser.add_argument("--audio-duration", type=float,
                        help="Measured duration in seconds; only valid with one --bvid")
    args = parser.parse_args(argv)
    if args.audio_duration is not None and (not args.bvid or len(args.bvid) != 1):
        parser.error("--audio-duration requires exactly one --bvid")
    try:
        inventory = read_json(args.inventory)
        if not isinstance(inventory, dict) or not isinstance(inventory.get("videos"), list):
            raise ValueError("Inventory must contain a videos list")
        videos = inventory["videos"]
        if any(not isinstance(video, dict) or not isinstance(video.get("bvid"), str)
               or not BVID.fullmatch(video["bvid"]) for video in videos):
            raise ValueError("Inventory contains invalid BVID records")
        ids = [video["bvid"] for video in videos]
        if len(ids) != len(set(ids)):
            raise ValueError("Inventory contains duplicate BVIDs")
        selected = args.bvid or ids
        if not selected or len(selected) != len(set(selected)):
            raise ValueError("Select at least one unique BVID")
        if any(bvid not in ids for bvid in selected):
            raise ValueError("Requested BVID is absent from inventory")
    except (OSError, ValueError) as exc:
        parser.error(str(exc))
    failures = []
    by_id = {video["bvid"]: video for video in videos}
    for bvid in selected:
        try:
            report = render_video(by_id[bvid], args.asr_root / bvid / "source.json",
                                  args.output_root / bvid, model=args.model, provider=args.provider,
                                  audio_path=args.audio_root / bvid / "source.m4a",
                                  audio_duration=args.audio_duration)
            print(json.dumps({"bvid": bvid, "status": report["status"],
                              "segments": report["accounting"]["raw_segment_count"],
                              "paragraphs": report["accounting"]["paragraph_count"],
                              "advisories": len(report["advisories"]),
                              "output": str(args.output_root / bvid)}, ensure_ascii=False))
        except (OSError, ValueError) as exc:
            failures.append(bvid)
            print(json.dumps({"bvid": bvid, "status": "failed", "error": str(exc)}, ensure_ascii=False))
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
