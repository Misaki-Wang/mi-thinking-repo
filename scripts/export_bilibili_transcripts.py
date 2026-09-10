#!/usr/bin/env python3
"""Export an explicitly authorized, fully validated Bilibili snapshot, without media.

Inputs remain private. This copies only Markdown and an allowlisted manifest;
signed media URLs, local paths, raw model logs and credentials are never exported.
All inputs are checked before any output is written. No network or git operation.
"""

from __future__ import annotations

import argparse
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import re

from render_bilibili_transcripts import read_json, render_markdown, serialize, timestamp, write_atomic

ROOT = Path(__file__).resolve().parents[1]
WORK = ROOT / ".work" / "bilibili-280780745"
ID = re.compile(r"BV[0-9A-Za-z]{10}\Z")


def digest(content: bytes) -> str:
    return hashlib.sha256(content).hexdigest()


def contained_file(root: Path, relative: str) -> Path:
    path = root / relative
    if (not path.is_file() or not path.resolve().is_relative_to(root.resolve())
            or any(parent.is_symlink() for parent in (path, *path.parents))):
        raise ValueError(f"Missing or unsafe input: {relative}")
    return path


def prepare_export(inventory: dict, authorization: dict, transcripts: Path) -> tuple[dict, dict[str, str]]:
    videos = inventory.get("videos", [])
    if not videos or not all(isinstance(v, dict) and ID.fullmatch(str(v.get("bvid", ""))) for v in videos):
        raise ValueError("Inventory requires valid video IDs")
    ids = [video["bvid"] for video in videos]
    if len(set(ids)) != len(ids) or inventory.get("latest_bvids") != ids:
        raise ValueError("Inventory ordering or uniqueness mismatch")
    if (authorization.get("confirmed") is not True
            or authorization.get("uploader_id") != inventory.get("uploader_id")
            or authorization.get("bvids") != ids
            or not authorization.get("confirmed_at")
            or not authorization.get("statement")):
        raise ValueError("Explicit authorization for this exact ordered snapshot is required")
    outputs: dict[str, str] = {}
    entries = []
    total_segments = total_paragraphs = total_characters = 0
    total_seconds = 0.0
    for video in videos:
        bvid = video["bvid"]
        if str(video.get("uploader_id")) != str(inventory["uploader_id"]):
            raise ValueError(f"{bvid}: video creator differs from authorized creator")
        transcript = contained_file(transcripts, f"{bvid}/transcript.zh-CN.md").read_bytes()
        paragraphs_bytes = contained_file(transcripts, f"{bvid}/data/paragraphs.json").read_bytes()
        report = read_json(contained_file(transcripts, f"{bvid}/validation.json"))
        accounting = report.get("accounting", {})
        if not all(accounting.get(key) is True for key in (
            "all_segments_accounted_once_in_original_order", "all_segment_fields_preserved",
            "all_text_preserved_exactly",
        )):
            raise ValueError(f"{bvid}: incomplete segment accounting")
        hashes = report.get("output_hashes", {})
        if (digest(transcript) != hashes.get("transcript.zh-CN.md")
                or digest(paragraphs_bytes) != hashes.get("data/paragraphs.json")):
            raise ValueError(f"{bvid}: rendered output hash mismatch")
        data = json.loads(paragraphs_bytes)
        metadata = report.get("metadata", {})
        if (metadata.get("bvid") != bvid or metadata.get("cid") != video["cid"]
                or data.get("metadata") != metadata
                or str(metadata.get("author_id")) != str(inventory["uploader_id"])):
            raise ValueError(f"{bvid}: metadata mismatch")
        paragraphs = data.get("paragraphs", [])
        text = "".join(p["text"] for p in paragraphs)
        segments = [segment for p in paragraphs for segment in p["segments"]]
        indices = [index for p in paragraphs for index in p["raw_segment_indices"]]
        if (len(paragraphs) != accounting.get("paragraph_count")
                or len(segments) != accounting.get("raw_segment_count")
                or indices != list(range(len(segments)))
                or text != "".join(s["text"] for s in segments)
                or digest(text.encode()) != accounting.get("raw_text_sha256")):
            raise ValueError(f"{bvid}: independent text accounting failed")
        if render_markdown(metadata, paragraphs, report).encode("utf-8") != transcript:
            raise ValueError(f"{bvid}: Markdown differs from a fresh lossless render")
        entry = {
            "bvid": bvid, "cid": video["cid"], "title": video["title"],
            "published_at": video["published_at"],
            "source_url": f"https://www.bilibili.com/video/{bvid}/",
            "public_transcripts": True, "transcript_sha256": digest(transcript),
            "provider": metadata["asr_provider"], "model": metadata["asr_model"],
            "timestamp_kind": metadata.get("timestamp_kind", "asr_segment"),
            "duration_seconds": metadata["duration_seconds"],
            "segments": len(segments), "paragraphs": len(paragraphs), "characters": len(text),
            "quality_status": report["status"], "semantic_accuracy": "not_assessed",
            "automatic_advisory_count": len(report["advisories"]),
            "raw_asr_sha256": metadata["raw_provenance"]["sha256"],
            "audio_sha256": (metadata.get("audio_provenance") or {}).get("sha256"),
        }
        entries.append(entry)
        outputs[f"{bvid}/transcript.zh-CN.md"] = transcript.decode("utf-8")
        total_segments += len(segments)
        total_paragraphs += len(paragraphs)
        total_characters += len(text)
        total_seconds += metadata["duration_seconds"]
    manifest = {
        "schema_version": 1, "uploader": inventory["uploader"],
        "uploader_id": inventory["uploader_id"],
        "source_url": f"https://space.bilibili.com/{inventory['uploader_id']}",
        "snapshot_at": inventory["retrieved_at"],
        "publication_authorized": True,
        "authorization": {"basis": "user attestation", "confirmed_at": authorization["confirmed_at"],
                          "statement": authorization["statement"],
                          "scope": "Full transcripts of the exact videos listed below"},
        "exported_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "video_count": len(entries), "audio_duration_seconds": round(total_seconds, 6),
        "segment_count": total_segments, "paragraph_count": total_paragraphs,
        "character_count": total_characters,
        "quality_note": "Complete ASR outputs, not a claim of perfect speech recognition or human proofreading.",
        "videos": entries,
    }
    rows = ["# 转写与质量记录", "",
            f"本次快照包含 {len(entries)} 期，参考音频合计 {timestamp(total_seconds)}。"
            f"保留 {total_segments:,} 个原始识别片段，整理为 {total_paragraphs:,} 个阅读段落。", "",
            "完整指所选音频均经过识别、所有输出片段保留；不代表每个发音都被正确识别。"
            "全文未逐句人工校对。中英混合术语、人名、数字、重复和静音幻觉仍需结合原视频确认。", "",
            "| 视频 | ASR 模型 | 阅读段落 | 自动提示 |", "| --- | --- | ---: | ---: |"]
    for entry in entries:
        rows.append(f"| [{entry['bvid']}]({entry['bvid']}/transcript.zh-CN.md) | "
                    f"{entry['model']} | {entry['paragraphs']} | {entry['automatic_advisory_count']} |")
    rows += ["", "## 可追溯与公开范围", "",
             "- 自动提示包括低能量分块稍长于 60 秒的边界记录，不是已确认错误的总数。",
             "- 时间定位方式记录在各稿与 manifest 中；audio_chunk 表示连续音频分块起点，不是逐字强制对齐。",
             "- 每段时间戳可跳回原视频；未猜测发言者身份，未把弹幕当字幕。",
             "- 音频、原始 ASR JSON、模型日志与逐段检查记录保留本地，不上传 GitHub。",
             "- 仓库 manifest.json 记录 Markdown、原始 ASR 与音频的 SHA-256，网站只发布经校验的讲稿。",
             f"- 发布依据：用户于 {authorization['confirmed_at']} 明确确认已获得授权，可发布完整讲稿。原作者与原视频链接保留。",
             "- 时间戳覆盖率及自动提示数量都不是准确率；未进行人工标注的 WER/CER 评估。", "",
             "[可复用工具链与运行说明](https://github.com/Misaki-Wang/mi-thinking-repo/blob/main/scripts/BILIBILI_WORKFLOW.md)", ""]
    outputs["QUALITY.md"] = "\n".join(rows)
    outputs["manifest.json"] = serialize(manifest)
    return manifest, outputs


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--inventory", type=Path, default=WORK / "inventory.json")
    parser.add_argument("--authorization", type=Path, required=True)
    parser.add_argument("--transcripts", type=Path, default=WORK / "transcripts")
    parser.add_argument("--output", type=Path, default=ROOT / "video" / "bilibili-280780745")
    args = parser.parse_args()
    manifest, outputs = prepare_export(read_json(args.inventory), read_json(args.authorization), args.transcripts)
    if any(parent.is_symlink() for parent in (args.output, *args.output.parents)):
        raise ValueError("Symlink export destination rejected")
    for relative in outputs:
        path = args.output / relative
        if any(parent.is_symlink() for parent in (path, *path.parents)):
            raise ValueError(f"Symlink export destination rejected: {relative}")
    for relative, content in outputs.items():
        write_atomic(args.output / relative, content)
    print(json.dumps({"videos": manifest["video_count"], "paragraphs": manifest["paragraph_count"],
                      "output": str(args.output)}, ensure_ascii=False))


if __name__ == "__main__":
    main()
