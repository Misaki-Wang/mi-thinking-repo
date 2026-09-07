"""Resume the local YouTube-English -> Codex-Chinese study pipeline.

Downloaded captions, detailed manifests, and logs stay in the ignored .work
directory. Full translation requires explicit per-session rights evidence.
Public export additionally requires public_transcript_allowed=true.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import shutil
import subprocess
import tempfile
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import parse_qs, urlsplit

REPO = Path(__file__).resolve().parents[1]
COURSE = REPO / "course" / "mit-mmai-2026"
WORK = REPO / ".work" / "transcripts"
ARTIFACTS = ("transcript.en.md", "transcript.zh-CN.md", "transcript.bilingual.md")
TRANSLATION_POLICY = "translate-v2-technical-terms"
VIDEO_ID = re.compile(r"[A-Za-z0-9_-]{11}\Z")
SESSION_ID = re.compile(r"w\d{2}-\d+\Z")


def now() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def read_json(path: Path, default=None):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        return default


def write_json(path: Path, value) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile(
        mode="w",
        encoding="utf-8",
        dir=path.parent,
        prefix=path.name + ".",
        suffix=".tmp",
        delete=False,
    ) as handle:
        json.dump(value, handle, ensure_ascii=False, indent=2)
        handle.write("\n")
        temporary = Path(handle.name)
    temporary.replace(path)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def get_video_id(url: str) -> str:
    parts = urlsplit(url)
    if parts.scheme != "https" or parts.hostname not in {
        "youtu.be",
        "youtube.com",
        "www.youtube.com",
    }:
        raise ValueError(f"Not a supported YouTube URL: {url}")
    candidate = (
        parts.path.lstrip("/")
        if parts.hostname == "youtu.be"
        else parse_qs(parts.query).get("v", [""])[0]
    )
    if not VIDEO_ID.fullmatch(candidate):
        raise ValueError(f"Invalid video identifier: {candidate}")
    return candidate


def stage_valid(directory: Path, name: str) -> bool:
    manifest = read_json(directory / "manifest.json", {})
    stage = manifest.get("stages", {}).get(name, {})
    hashes = stage.get("output_hashes", {})
    if stage.get("status") != "complete" or not hashes:
        return False
    for relative, digest in hashes.items():
        path = directory / relative
        if (
            not path.is_file()
            or not path.resolve().is_relative_to(directory.resolve())
            or sha256(path) != digest
        ):
            return False
    return True


def seed_verified(directory: Path, source: Path | None, video_id: str) -> None:
    if source is None or directory.exists():
        return
    manifest = read_json(source / "manifest.json", {})
    if manifest.get("video_id") != video_id:
        return
    if all(
        stage_valid(source, stage) for stage in ("english", "translation", "render")
    ):
        shutil.copytree(source, directory)
        write_json(
            directory / "reuse-provenance.json",
            {
                "reused_at": now(),
                "source": str(source),
                "verified_stages": ["english", "translation", "render"],
            },
        )


def probe_license(python: Path, video_id: str) -> None:
    directory = WORK / video_id
    directory.mkdir(parents=True, exist_ok=True)
    target = directory / "license-observation.json"
    if target.exists():
        return
    command = [
        str(python),
        "-m",
        "yt_dlp",
        "--ignore-config",
        "--no-plugin-dirs",
        "--no-playlist",
        "--skip-download",
        "--js-runtimes",
        "node",
        "--socket-timeout",
        "20",
        "--retries",
        "1",
        "--print",
        "%(license)j",
        f"https://www.youtube.com/watch?v={video_id}",
    ]
    try:
        result = subprocess.run(  # Validated video ID, argv, and no shell.
            command, capture_output=True, text=True, timeout=180, check=False
        )
        license_value = None
        if result.returncode == 0:
            try:
                license_value = json.loads(result.stdout.strip().splitlines()[-1])
            except (ValueError, IndexError):
                pass
        payload = {
            "checked_at": now(),
            "video_id": video_id,
            "source": "yt-dlp video metadata license field",
            "license": license_value,
            "probe_exit_code": result.returncode,
            "note": "A missing license is not evidence of a permissive license.",
        }
        (directory / "license-probe.log").write_text(result.stderr, encoding="utf-8")
    except subprocess.TimeoutExpired:
        payload = {
            "checked_at": now(),
            "video_id": video_id,
            "license": None,
            "probe_error": "Timed out after 180 seconds",
        }
    write_json(target, payload)


def run_stage(python: Path, video_id: str, stage: str) -> dict:
    directory = WORK / video_id
    manifest = read_json(directory / "manifest.json", {})
    if stage == "english" and stage_valid(directory, "english"):
        return {
            "video_id": video_id,
            "stage": stage,
            "status": "reused",
            "ended_at": now(),
        }
    policy_current = (
        read_json(directory / "translation-policy.json", {}).get("prompt_version")
        == TRANSLATION_POLICY
    )
    if (
        stage == "translate"
        and policy_current
        and stage_valid(directory, "translation")
        and stage_valid(directory, "render")
        and manifest.get("translation_provider") == "codex"
        and manifest.get("translated_blocks") == manifest.get("total_blocks")
    ):
        return {
            "video_id": video_id,
            "stage": stage,
            "status": "reused",
            "ended_at": now(),
        }
    if stage == "translate" and not stage_valid(directory, "english"):
        return {
            "video_id": video_id,
            "stage": stage,
            "status": "blocked_missing_english",
            "ended_at": now(),
        }
    directory.mkdir(parents=True, exist_ok=True)
    command = [
        str(python),
        "-m",
        "ytlearn",
        "run",
        f"https://www.youtube.com/watch?v={video_id}",
        "--translator",
        "none" if stage == "english" else "codex",
        "--english-source",
        "youtube",
        "--transcriber",
        "none",
        "--keep-media",
        "none",
        "-o",
        str(WORK),
    ]
    started = now()
    progress = {
        "video_id": video_id,
        "stage": stage,
        "status": "running",
        "started_at": started,
    }
    write_json(directory / f"{stage}-run.json", progress)
    with (directory / f"{stage}.log").open("a", encoding="utf-8") as log:
        log.write(f"\n--- {started} ---\n")
        log.flush()
        try:
            result = subprocess.run(  # Validated video ID, argv, and no shell.
                command,
                stdout=log,
                stderr=subprocess.STDOUT,
                timeout=7200 if stage == "translate" else 600,
                check=False,
            )
            progress.update(
                exit_code=result.returncode,
                status="complete" if result.returncode == 0 else "incomplete",
            )
        except subprocess.TimeoutExpired:
            progress.update(
                status="timeout", error="Bounded subprocess time limit exceeded"
            )
    progress["ended_at"] = now()
    write_json(directory / f"{stage}-run.json", progress)
    if stage == "translate" and progress.get("exit_code") == 0:
        write_json(
            directory / "translation-policy.json",
            {
                "prompt_version": TRANSLATION_POLICY,
                "completed_at": now(),
                "terms": "Retain English technical terms, acronyms and named models; annotate ambiguous caption errors.",
            },
        )
    return progress


def build_status(sessions: list[dict]) -> dict:
    records = []
    for session in sessions:
        entry = {
            "session_id": session["id"],
            "title": session["title"],
            "video_url": session.get("video_url"),
            "instructional": session.get("instructional", True),
        }
        if not session.get("video_url"):
            if not session.get("instructional", True):
                source_status = "not_instructional"
            elif session.get("slides_status") == "acquired" and session.get(
                "slides_url"
            ):
                source_status = "slides_only"
            else:
                source_status = "sources_missing"
            entry.update(
                status=source_status,
                english_blocks=0,
                translated_blocks=0,
                public_transcripts=False,
            )
            records.append(entry)
            continue
        video_id = get_video_id(session["video_url"])
        directory = WORK / video_id
        manifest = read_json(directory / "manifest.json", {})
        english_valid = stage_valid(directory, "english")
        policy_current = (
            read_json(directory / "translation-policy.json", {}).get("prompt_version")
            == TRANSLATION_POLICY
        )
        translated_valid = (
            policy_current
            and stage_valid(directory, "translation")
            and stage_valid(directory, "render")
            and manifest.get("translation_provider") == "codex"
            and manifest.get("translated_blocks") == manifest.get("total_blocks")
        )
        publication_allowed = session.get("public_transcript_allowed") is True
        exported = (
            publication_allowed
            and translated_valid
            and all(
                (COURSE / session["id"] / filename).is_file()
                and sha256(COURSE / session["id"] / filename)
                == sha256(directory / filename)
                for filename in ARTIFACTS
            )
        )
        permission_present = session.get("full_translation_allowed") is True and bool(
            session.get("rights_evidence")
        )
        translation_run = read_json(directory / "translate-run.json", {})
        if translated_valid:
            translation_status = "complete"
        elif permission_present and translation_run.get("status") == "running":
            translation_status = "in_progress"
        elif permission_present:
            translation_status = "allowed"
        else:
            translation_status = "paused_permission_needed"
        entry.update(
            video_id=video_id,
            status="complete_local"
            if translated_valid
            else "english_ready"
            if english_valid
            else "failed"
            if manifest.get("status") == "failed"
            else "pending",
            source_kind=manifest.get("source_kind"),
            duration_ms=manifest.get("metadata", {}).get("duration_ms", 0),
            english_blocks=manifest.get("total_blocks", 0) if english_valid else 0,
            translated_blocks=manifest.get("translated_blocks", 0)
            if translated_valid
            else 0,
            translation_provider=manifest.get("translation_provider"),
            legacy_codex_complete=(
                not policy_current
                and stage_valid(directory, "translation")
                and stage_valid(directory, "render")
                and manifest.get("translation_provider") == "codex"
                and manifest.get("translated_blocks") == manifest.get("total_blocks")
            ),
            full_translation_status=translation_status,
            rights_evidence=session.get("rights_evidence"),
            terminology_policy=TRANSLATION_POLICY if policy_current else None,
            public_transcripts=exported,
            publication_status="exported"
            if exported
            else "allowed_pending_export"
            if publication_allowed
            else "withheld_pending_video_license",
            license_observation=read_json(directory / "license-observation.json", {}),
            error=manifest.get("error"),
            local_work_dir=f".work/transcripts/{video_id}",
            artifacts={
                filename: {
                    "sha256": sha256(directory / filename),
                    "bytes": (directory / filename).stat().st_size,
                }
                for filename in ARTIFACTS
                if (directory / filename).is_file()
            },
        )
        records.append(entry)
    videos = [record for record in records if record.get("video_id")]
    return {
        "schema_version": 1,
        "updated_at": now(),
        "english_source_policy": "YouTube English captions; no ASR on transport failures",
        "translation_policy": "Full translation requires video permission evidence. If permitted: Codex; at most two jobs per scheduler invocation, with cross-process per-video locks; retain English technical terms.",
        "publication_policy": "Full transcript export requires per-session video rights evidence; original study summaries may be public.",
        "counts": {
            "sessions": len(records),
            "instructional": sum(record["instructional"] for record in records),
            "videos": len(videos),
            "duration_ms": sum(record.get("duration_ms", 0) for record in videos),
            "english_blocks": sum(record["english_blocks"] for record in videos),
            "translated_blocks": sum(record["translated_blocks"] for record in videos),
            "english_ready": sum(
                record["status"] in {"english_ready", "complete_local"}
                for record in videos
            ),
            "codex_complete": sum(
                record["status"] == "complete_local" for record in videos
            ),
            "legacy_codex_complete": sum(
                record.get("legacy_codex_complete", False) for record in videos
            ),
            "translation_paused_permission_needed": sum(
                record.get("full_translation_status") == "paused_permission_needed"
                for record in videos
            ),
            "public_transcripts": sum(
                record["public_transcripts"] for record in videos
            ),
            "slides_only": sum(record["status"] == "slides_only" for record in records),
            "sources_missing": sum(
                record["status"] == "sources_missing" for record in records
            ),
        },
        "sessions": records,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--catalog", type=Path, default=COURSE / "catalog.json")
    parser.add_argument(
        "--python",
        type=Path,
        default=REPO.parent / "youtube-learning-toolchain" / ".venv" / "bin" / "python",
    )
    parser.add_argument(
        "--seed",
        type=Path,
        default=REPO.parent
        / "youtube-learning-toolchain"
        / "runs"
        / "mit-mmai-lecture-06"
        / "final",
    )
    parser.add_argument(
        "--stage",
        choices=("english", "translate", "all", "status", "export"),
        default="english",
    )
    parser.add_argument("--workers", type=int, choices=(1, 2), default=2)
    parser.add_argument(
        "--ids",
        nargs="*",
        help="Restrict execution to these session or video identifiers",
    )
    args = parser.parse_args()
    if args.stage in {"translate", "all"}:
        check = subprocess.run(  # Explicit local interpreter, fixed program.
            [
                str(args.python),
                "-c",
                "from ytlearn.translation.core import PROMPT_VERSION; from ytlearn.pipeline import PIPELINE_LOCK_VERSION; print(PROMPT_VERSION + ':' + str(PIPELINE_LOCK_VERSION))",
            ],
            capture_output=True,
            text=True,
            timeout=30,
            check=False,
        )
        if check.returncode or check.stdout.strip() != TRANSLATION_POLICY + ":1":
            parser.error(
                f"The ytlearn interpreter must provide translation prompt {TRANSLATION_POLICY} and cross-process video locks; update the local toolchain before translating."
            )
    sessions = read_json(args.catalog)["sessions"]
    for session in sessions:
        if not SESSION_ID.fullmatch(session["id"]):
            raise ValueError("Invalid session identifier")
    candidates = {
        get_video_id(session["video_url"]): session
        for session in sessions
        if session.get("video_url")
        and (
            not args.ids
            or session["id"] in args.ids
            or get_video_id(session["video_url"]) in args.ids
        )
    }
    if args.stage in {"translate", "all"}:
        missing_rights = [
            session["id"]
            for session in candidates.values()
            if session.get("full_translation_allowed") is not True
            or not session.get("rights_evidence")
        ]
        if missing_rights:
            parser.error(
                "Full translation requires explicit video permission evidence in the catalog; "
                "use downloaded captions to prepare original summaries for these sessions: "
                + ", ".join(missing_rights)
            )
    WORK.mkdir(parents=True, exist_ok=True)
    for video_id in candidates:
        seed_verified(WORK / video_id, args.seed, video_id)

    def refresh():
        status = build_status(sessions)
        write_json(COURSE / "transcript-status.json", status)
        print(json.dumps({"at": now(), **status["counts"]}), flush=True)

    refresh()
    if args.stage in {"english", "all"}:
        for video_id in candidates:
            probe_license(args.python, video_id)
            print(json.dumps(run_stage(args.python, video_id, "english")), flush=True)
            refresh()
    if args.stage in {"translate", "all"}:
        with ThreadPoolExecutor(max_workers=args.workers) as executor:
            futures = [
                executor.submit(run_stage, args.python, video_id, "translate")
                for video_id in candidates
            ]
            for future in as_completed(futures):
                print(json.dumps(future.result()), flush=True)
                refresh()
    if args.stage in {"export", "all"}:
        for video_id, session in candidates.items():
            source = WORK / video_id
            if session.get("public_transcript_allowed") is not True:
                continue
            if (
                read_json(source / "translation-policy.json", {}).get("prompt_version")
                != TRANSLATION_POLICY
            ):
                continue
            if not (
                stage_valid(source, "english")
                and stage_valid(source, "translation")
                and stage_valid(source, "render")
            ):
                continue
            destination = COURSE / session["id"]
            destination.mkdir(parents=True, exist_ok=True)
            for filename in ARTIFACTS:
                shutil.copy2(source / filename, destination / filename)
    refresh()
    selected = [
        item
        for item in build_status(sessions)["sessions"]
        if item.get("video_id") in candidates
    ]
    if args.stage in {"translate", "all"} and any(
        item["full_translation_status"] != "complete" for item in selected
    ):
        return 2
    if args.stage in {"export", "all"} and any(
        not item["public_transcripts"] for item in selected
    ):
        return 2
    if args.stage == "english" and any(
        item["status"] not in {"english_ready", "complete_local"} for item in selected
    ):
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
