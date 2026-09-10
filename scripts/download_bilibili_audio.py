#!/usr/bin/env python3
"""Download a bounded public Bilibili inventory as audio, with local provenance.

Run with the Python environment containing yt-dlp. Uses anonymous access only;
all audio, logs, and manifests stay under the ignored .work directory.
"""

from __future__ import annotations

import argparse
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime
import hashlib
import json
import math
from pathlib import Path
import re
import shutil
import subprocess
import sys
from urllib.parse import urlsplit, urlunsplit
from zoneinfo import ZoneInfo


def stamp() -> str:
    return datetime.now(ZoneInfo("Asia/Shanghai")).isoformat()


def save(path: Path, value: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def sanitized_log(message: str) -> str:
    def clean(match: re.Match[str]) -> str:
        url = urlsplit(match.group())
        return urlunsplit((url.scheme, url.hostname or "", url.path, "", ""))

    return re.sub(r"https?://[^\s\"<>]+", clean, message)


def verify(path: Path, expected_duration: float) -> dict:
    probe = subprocess.run(
        ["ffprobe", "-v", "error", "-show_entries",
         "format=duration,format_name:stream=codec_type,codec_name,sample_rate,channels",
         "-of", "json", str(path)],
        text=True, capture_output=True, check=True, timeout=60,
    )
    info = json.loads(probe.stdout)
    streams = info.get("streams", [])
    if not streams or any(stream.get("codec_type") != "audio" for stream in streams):
        raise RuntimeError("Downloaded file must contain audio streams only")
    duration = float(info["format"]["duration"])
    if abs(duration - expected_duration) > 2:
        raise RuntimeError(f"Duration mismatch: {duration} vs {expected_duration}")
    with path.open("rb") as source:
        digest = hashlib.file_digest(source, "sha256").hexdigest()
    return {"local_path": str(path.resolve()), "size_bytes": path.stat().st_size,
            "duration_seconds": duration, "expected_duration_seconds": expected_duration,
            "sha256": digest, "ffprobe": info}


def recorded_format(record: object) -> str:
    """Read format evidence, including manifests made before the explicit field."""
    if not isinstance(record, dict):
        raise ValueError("Existing manifest must be a JSON object")
    selected = record.get("requested_audio_format")
    if selected is None:
        command = record.get("command")
        if isinstance(command, list) and command.count("-f") == 1:
            index = command.index("-f") + 1
            if index < len(command):
                selected = command[index]
    if selected not in ("bestaudio", "30216", "30232", "30280"):
        raise ValueError("Existing manifest has no usable audio format evidence")
    return selected


def download(video: dict, root: Path, timeout: int, version: str,
             format_selector: str = "bestaudio", output_root: Path | None = None) -> dict:
    bvid = video["bvid"]
    folder = (output_root or root / "audio") / bvid
    folder.mkdir(parents=True, exist_ok=True)
    url = f"https://www.bilibili.com/video/{bvid}/"
    output = folder / "source.%(ext)s"
    command = [sys.executable, "-m", "yt_dlp", "--ignore-config", "--no-plugin-dirs",
               "--no-playlist", "--socket-timeout", "20", "--retries", "1",
               "--fragment-retries", "1", "--extractor-retries", "1",
               "--limit-rate", "8M", "--no-progress", "--no-color",
               "-f", format_selector, "-o", str(output), url]
    result = {"bvid": bvid, "title": video["title"], "source_url": url,
              "uploader_id": str(video["uploader_id"]), "started_at": stamp(),
              "access": "anonymous public audio; no cookies or login",
              "yt_dlp_version": version, "command": command,
              "requested_audio_format": format_selector,
              "source_audio_reencoded_for_transfer": False}
    candidates = [file for file in folder.glob("source.*")
                  if file.suffix in {".m4a", ".webm", ".ogg", ".mp3", ".opus"}]
    # Validate reuse before any writes. Rejection must not replace source evidence
    # with a new failed manifest, and successful reuse retains the original log.
    try:
        old_manifest = folder / "manifest.json"
        old = None
        if old_manifest.exists():
            old = json.loads(old_manifest.read_text(encoding="utf-8"))
            if recorded_format(old) != format_selector:
                raise RuntimeError("Existing output uses another audio format; choose a separate output root")
            if (old.get("bvid") != bvid or old.get("source_url") != url
                    or str(old.get("uploader_id")) != str(video["uploader_id"])):
                raise RuntimeError("Existing manifest does not identify this video and uploader")
        if old is None and any(folder.glob("source.*")):
            raise RuntimeError("Existing media or partial download has no source manifest")
        if candidates:
            if len(candidates) != 1 or old is None or old.get("status") != "complete":
                raise RuntimeError("Existing media requires one completed, verifiable source manifest")
            if (not isinstance(old.get("sha256"), str)
                    or not re.fullmatch(r"[0-9a-f]{64}", old["sha256"])
                    or type(old.get("size_bytes")) is not int
                    or not isinstance(old.get("duration_seconds"), (int, float))
                    or not math.isfinite(old["duration_seconds"])):
                raise RuntimeError("Existing manifest is missing usable checksum, size, or duration evidence")
            checked = verify(candidates[0], float(video.get("playback_duration", video["duration"])))
            if (checked["sha256"] != old["sha256"] or checked["size_bytes"] != old["size_bytes"]
                    or abs(checked["duration_seconds"] - old["duration_seconds"]) > 0.001):
                raise RuntimeError("Existing media no longer matches its recorded checksum, size, or duration")
            result = {**old, **checked, "requested_audio_format": format_selector,
                      "reused_existing": True, "reuse_verified_at": stamp()}
            print(json.dumps(result, ensure_ascii=False), flush=True)
            return result
    except Exception as error:
        result.update(status="failed", reused_existing=False, error=sanitized_log(str(error)),
                      finished_at=stamp())
        print(json.dumps(result, ensure_ascii=False), flush=True)
        return result

    log = ""
    try:
        process = subprocess.run(command, text=True, capture_output=True, timeout=timeout)
        log = process.stdout + process.stderr
        result["download_exit_code"] = process.returncode
        if process.returncode:
            raise RuntimeError(f"yt-dlp failed with exit code {process.returncode}")
        candidates = [file for file in folder.glob("source.*")
                      if file.suffix in {".m4a", ".webm", ".ogg", ".mp3", ".opus"}]
        if len(candidates) != 1:
            raise RuntimeError(f"Expected one completed audio file, got {len(candidates)}")
        result.update(verify(candidates[0], float(video.get("playback_duration", video["duration"]))))
        result.update(status="complete", reused_existing=False)
    except subprocess.TimeoutExpired as error:
        log += str(error)
        result.update(status="failed", error=f"Download exceeded {timeout} second limit")
    except Exception as error:
        result.update(status="failed", error=sanitized_log(str(error)))
    result["finished_at"] = stamp()
    (folder / "download.log").write_text(sanitized_log(log), encoding="utf-8")
    save(folder / "manifest.json", result)
    print(json.dumps(result, ensure_ascii=False), flush=True)
    return result


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(".work/bilibili-280780745"))
    parser.add_argument("--output-root", type=Path,
                        help="Separate private audio directory; defaults to ROOT/audio")
    parser.add_argument("--format", dest="format_selector", default="bestaudio",
                        choices=("bestaudio", "30216", "30232", "30280"))
    parser.add_argument("--workers", type=int, default=2, choices=(1, 2))
    parser.add_argument("--timeout", type=int, default=900)
    parser.add_argument("--sample-only", action="store_true")
    parser.add_argument("--remaining-only", action="store_true")
    args = parser.parse_args()
    if not shutil.which("ffprobe"):
        parser.error("ffprobe must be installed")
    if args.sample_only and args.remaining_only:
        parser.error("Choose sample-only or remaining-only")
    if not 60 <= args.timeout <= 1800:
        parser.error("Timeout must be between 60 and 1800 seconds")
    root = args.root.resolve()
    if ".work" not in root.parts:
        parser.error("Private output root must be under .work")
    output_root = args.output_root.resolve() if args.output_root else None
    if output_root and ".work" not in output_root.parts:
        parser.error("Private audio output root must be under .work")
    inventory = json.loads((root / "inventory.json").read_text(encoding="utf-8"))
    videos = inventory["videos"]
    ids = [video["bvid"] for video in videos]
    if not 1 <= len(ids) <= 10 or len(set(ids)) != len(ids):
        parser.error("Inventory must contain 1–10 unique videos")
    for video in videos:
        if not re.fullmatch(r"BV[0-9A-Za-z]{10}", video["bvid"]):
            parser.error("Inventory contains an invalid BVID")
        if str(video["uploader_id"]) != str(inventory["uploader_id"]):
            parser.error("Inventory contains another uploader")
        if len(video.get("parts", [])) != 1:
            parser.error("This downloader expects single-part videos")
        existing = (output_root or root / "audio") / video["bvid"] / "manifest.json"
        if existing.exists():
            try:
                prior = json.loads(existing.read_text(encoding="utf-8"))
                previous_format = recorded_format(prior)
            except (OSError, ValueError) as error:
                parser.error(f"Existing manifest cannot be reused: {error}")
            if previous_format != args.format_selector:
                parser.error("Existing output uses another audio format; choose a separate --output-root")
    sample = next(video for video in videos if video["bvid"] == inventory["sample_bvid"])
    version = subprocess.run([sys.executable, "-m", "yt_dlp", "--version"],
                             check=True, capture_output=True, text=True, timeout=30).stdout.strip()
    results = []
    if not args.remaining_only:
        results.append(download(sample, root, args.timeout, version, args.format_selector, output_root))
    if not args.sample_only:
        remaining = [video for video in videos if video["bvid"] != sample["bvid"]]
        with ThreadPoolExecutor(max_workers=args.workers) as executor:
            jobs = [executor.submit(download, video, root, args.timeout, version,
                                    args.format_selector, output_root) for video in remaining]
            results.extend(job.result() for job in as_completed(jobs))
    summary = (output_root / ("sample-manifest.json" if args.sample_only else "download-manifest.json")
               if output_root else
               root / ("audio-sample-manifest.json" if args.sample_only else "audio-download-manifest.json"))
    save(summary,
         {"generated_at": stamp(), "inventory_path": str(root / "inventory.json"),
          "results": results, "complete": sum(row["status"] == "complete" for row in results),
          "failed": sum(row["status"] != "complete" for row in results)})
    return int(any(row["status"] != "complete" for row in results))


if __name__ == "__main__":
    raise SystemExit(main())
