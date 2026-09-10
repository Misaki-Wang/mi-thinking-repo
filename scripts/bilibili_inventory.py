#!/usr/bin/env python3
"""Snapshot a bounded, publication-sorted public Bilibili video inventory.

Uses anonymous, normal yt-dlp/API access. This does not download media or
attempt to access login-only subtitles. Raw evidence stays in ignored .work/.
"""

from __future__ import annotations

import argparse
from datetime import datetime
import json
from pathlib import Path
import re
import time
from urllib.request import Request, urlopen
from zoneinfo import ZoneInfo

from yt_dlp import YoutubeDL


def save(path: Path, value: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


class Logger:
    def __init__(self) -> None:
        self.warnings: list[str] = []

    def debug(self, message: str) -> None:
        pass

    def warning(self, message: str) -> None:
        self.warnings.append(message)

    def error(self, message: str) -> None:
        self.warnings.append(message)


def view_api(bvid: str) -> dict:
    url = f"https://api.bilibili.com/x/web-interface/view?bvid={bvid}"
    request = Request(url, headers={
        "User-Agent": "Mozilla/5.0",
        "Referer": f"https://www.bilibili.com/video/{bvid}/",
    })
    with urlopen(request, timeout=30) as response:
        data = json.load(response)
    if data.get("code") != 0:
        raise RuntimeError(f"View API rejected {bvid}: {data.get('code')} {data.get('message')}")
    return data


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--uid", default="280780745")
    parser.add_argument("--sample", default="BV1KZ8X6uEPL")
    parser.add_argument("--limit", type=int, default=10)
    parser.add_argument("--output", type=Path, default=Path(".work/bilibili-280780745"))
    parser.add_argument("--channel-snapshot", type=Path,
                        help="Reuse an already acquired yt-dlp channel JSON after a transient API failure")
    args = parser.parse_args()
    if not args.uid.isdecimal() or not re.fullmatch(r"BV[0-9A-Za-z]{10}", args.sample):
        parser.error("UID/BVID must be canonical Bilibili identifiers")
    if not 1 <= args.limit <= 10:
        parser.error("Inventory is bounded to 1–10 latest videos")
    stamp = datetime.now(ZoneInfo("Asia/Shanghai")).isoformat()
    output = args.output
    channel_url = f"https://space.bilibili.com/{args.uid}/video?order=pubdate"
    logger = Logger()
    if args.channel_snapshot:
        playlist = json.loads(args.channel_snapshot.read_text(encoding="utf-8"))
        if playlist.get("id") != args.uid:
            raise RuntimeError("Saved channel snapshot has a different UID")
    else:
        with YoutubeDL({"quiet": True, "logger": logger, "extract_flat": True,
                        "playlistend": args.limit, "skip_download": True}) as downloader:
            playlist = downloader.extract_info(channel_url, download=False)
            playlist = downloader.sanitize_info(playlist)
    save(output / "evidence/channel-latest10.json", playlist)
    ids = [entry["id"] for entry in playlist["entries"]]
    if len(ids) != args.limit or len(set(ids)) != len(ids):
        raise RuntimeError("Channel did not provide the requested number of unique videos")
    targets = ids + ([] if args.sample in ids else [args.sample])
    by_id = {}
    # Fetch the requested sample first, then only the bounded latest-video set.
    for bvid in [args.sample] + [key for key in targets if key != args.sample]:
        raw = view_api(bvid)
        save(output / f"evidence/{bvid}.view.json", raw)
        data = raw["data"]
        if str(data["owner"]["mid"]) != args.uid:
            raise RuntimeError(f"Unexpected owner for {bvid}")
        video_logger = Logger()
        with YoutubeDL({"quiet": True, "logger": video_logger, "skip_download": True,
                        "noplaylist": True, "listsubtitles": True}) as downloader:
            info = downloader.extract_info(f"https://www.bilibili.com/video/{bvid}/", download=False)
            info = downloader.sanitize_info(info)
        save(output / f"evidence/{bvid}.info.json", info)
        save(output / f"evidence/{bvid}.warnings.json", video_logger.warnings)
        subtitle_languages = [key for key in info.get("subtitles", {}) if key != "danmaku"]
        login_required = any("Subtitles are only available when logged in" in warning
                             for warning in video_logger.warnings)
        published = datetime.fromtimestamp(data["pubdate"], ZoneInfo("Asia/Shanghai"))
        rights = data.get("rights", {})
        item = {
            "bvid": bvid,
            "cid": data.get("cid"),
            "title": data["title"],
            "uploader": data["owner"]["name"],
            "uploader_id": str(data["owner"]["mid"]),
            "published_at": published.isoformat(),
            "upload_date": published.date().isoformat(),
            "timestamp": data["pubdate"],
            "duration": data["duration"],
            "playback_duration": info.get("duration"),
            "source_url": f"https://www.bilibili.com/video/{bvid}/",
            "parts": [{"cid": part["cid"], "page": part["page"],
                       "title": part["part"], "duration": part["duration"],
                       "asr_language": part.get("asr_language"),
                       "source_url": f"https://www.bilibili.com/video/{bvid}/?p={part['page']}"}
                      for part in data.get("pages", [])],
            "subtitle_availability": {
                "public_transcript_languages": subtitle_languages,
                "login_required_reported": login_required,
                "danmaku_only": not subtitle_languages and "danmaku" in info.get("subtitles", {}),
                "note": "Danmaku is viewer commentary, not a speech transcript.",
            },
            "public_audio_formats": [{key: fmt.get(key) for key in
                                     ("format_id", "ext", "acodec", "abr", "filesize_approx")}
                                    for fmt in info.get("formats", [])
                                    if fmt.get("vcodec") == "none" and fmt.get("acodec") != "none"],
            "observed_rights": {"copyright": data.get("copyright"),
                                "download": rights.get("download"),
                                "no_reprint": rights.get("no_reprint"),
                                "no_share": rights.get("no_share"),
                                "license_interpretation": "No blanket republication license inferred from these flags."},
            "description": data.get("desc", ""),
        }
        by_id[bvid] = item
        print(json.dumps({"bvid": bvid, "title": item["title"], "upload_date": item["upload_date"],
                          "duration": item["duration"], "parts": len(item["parts"]),
                          "subtitles": item["subtitle_availability"],
                          "audio_formats": len(item["public_audio_formats"])}, ensure_ascii=False), flush=True)
        time.sleep(0.5)
    timestamps = [by_id[bvid]["timestamp"] for bvid in ids]
    if timestamps != sorted(timestamps, reverse=True):
        raise RuntimeError("Channel inventory is not descending by publication timestamp")
    inventory = {
        "schema_version": 1,
        "retrieved_at": stamp,
        "uploader": by_id[args.sample]["uploader"],
        "uploader_id": args.uid,
        "channel_url": channel_url,
        "ordering": "Bilibili space API order=pubdate; descending timestamps verified",
        "latest_count": len(ids),
        "sample_bvid": args.sample,
        "sample_in_latest": args.sample in ids,
        "sample_latest_rank": ids.index(args.sample) + 1 if args.sample in ids else None,
        "latest_bvids": ids,
        "total_duration_seconds": sum(by_id[bvid]["duration"] for bvid in targets),
        "videos": [by_id[bvid] for bvid in targets],
        "acquisition": "Anonymous yt-dlp and public Bilibili view API; no login/cookies or media downloads.",
    }
    save(output / "inventory.json", inventory)
    print(json.dumps({"inventory": str(output / "inventory.json"), "count": len(targets),
                      "duration_seconds": inventory["total_duration_seconds"], "sample_rank": inventory["sample_latest_rank"]}))


if __name__ == "__main__":
    main()
