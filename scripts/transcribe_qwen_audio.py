#!/usr/bin/env python3
"""Transcribe a local 16 kHz mono PCM WAV using a local Qwen3-ASR model.

The caller decodes media with ffmpeg. Times are contiguous audio-chunk boundaries,
not word timestamps. Model libraries are imported only by the actual CLI run.
"""
from __future__ import annotations

import argparse
from collections import deque
from dataclasses import dataclass
from datetime import datetime, timezone
import hashlib
import json
import math
import os
from pathlib import Path
import re
import sys
import time
import wave


@dataclass(frozen=True)
class Span:
    start: int
    end: int
    depth: int = 0


def validate_partition(spans: list[Span], start: int, end: int) -> None:
    cursor = start
    for span in spans:
        if (not isinstance(span.start, int) or not isinstance(span.end, int)
                or span.start != cursor or span.end <= span.start or span.end > end):
            raise ValueError("Audio spans must cover the source exactly once without gaps or overlaps")
        cursor = span.end
    if cursor != end or not spans:
        raise ValueError("Incomplete audio span coverage")


def spans_from_chunks(parts, total_samples: int, sample_rate: int,
                      base_start: int = 0, depth: int = 0) -> list[Span]:
    """Convert official chunk offsets, excluding any padded tail samples."""
    spans = []
    for chunk, offset in parts:
        if not math.isfinite(offset) or offset < 0:
            raise ValueError("Invalid chunk offset")
        start = round(offset * sample_rate)
        end = min(total_samples, start + len(chunk))
        spans.append(Span(base_start + start, base_start + end, depth))
    validate_partition(spans, base_start, base_start + total_samples)
    return spans


def generation_check(token_ids: list[int], eos_ids: set[int], limit: int) -> dict:
    eos_position = next((index for index, token in enumerate(token_ids) if token in eos_ids), None)
    return {
        "generated_token_count": len(token_ids) if eos_position is None else eos_position + 1,
        "batch_padded_token_count": len(token_ids),
        "max_new_tokens": limit,
        "eos_found": eos_position is not None,
        "hit_token_limit": eos_position is None and len(token_ids) >= limit,
        "needs_retry": eos_position is None,
    }


def transcribe_partition(initial: list[Span], recognize, split_retry,
                         batch_size: int, on_attempt=lambda *args: None) -> list[dict]:
    """Replace failed spans by a checked partition, never duplicate failed text."""
    if not 1 <= batch_size <= 8:
        raise ValueError("batch_size must be between 1 and 8")
    if not initial:
        raise ValueError("No source audio spans")
    validate_partition(initial, initial[0].start, initial[-1].end)
    pending = deque(initial)
    accepted = []
    while pending:
        batch = [pending.popleft() for _ in range(min(batch_size, len(pending)))]
        results = recognize(batch)
        if len(results) != len(batch):
            raise ValueError("ASR result count does not match the audio batch")
        retries = []
        for span, result in zip(batch, results, strict=True):
            if not isinstance(result.get("text"), str):
                raise ValueError("Every ASR result must contain raw text, including empty strings")
            retry = result["generation"]["needs_retry"]
            on_attempt(span, result, not retry)
            if retry:
                children = split_retry(span)
                validate_partition(children, span.start, span.end)
                if len(children) < 2 or any(c.end - c.start >= span.end - span.start for c in children):
                    raise ValueError("Retry must split the failed interval into smaller pieces")
                retries.extend(children)
            else:
                accepted.append({"span": span, **result})
        pending.extendleft(reversed(retries))
    accepted.sort(key=lambda item: item["span"].start)
    validate_partition([item["span"] for item in accepted], initial[0].start, initial[-1].end)
    return accepted


def sha256_file(path: Path) -> str:
    hasher = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            hasher.update(block)
    return hasher.hexdigest()


def write_json(path: Path, data: dict) -> None:
    temporary = path.with_name(path.name + ".tmp")
    temporary.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    temporary.replace(path)


def isolate_caches(cache: Path) -> dict[str, str]:
    locations = {
        "HF_HOME": "huggingface", "TRANSFORMERS_CACHE": "transformers",
        "XDG_CACHE_HOME": ".", "NUMBA_CACHE_DIR": "numba", "TMPDIR": "tmp",
        "TORCH_HOME": "torch", "MODELSCOPE_CACHE": "modelscope",
        "CUDA_CACHE_PATH": "cuda", "TORCHINDUCTOR_CACHE_DIR": "inductor",
        "TRITON_CACHE_DIR": "triton",
    }
    values = {}
    for key, relative in locations.items():
        destination = cache / relative
        destination.mkdir(parents=True, exist_ok=True)
        values[key] = str(destination.resolve())
    values.update(HF_HUB_OFFLINE="1", HF_HUB_DISABLE_IMPLICIT_TOKEN="1",
                  PYTHONDONTWRITEBYTECODE="1", OMP_NUM_THREADS="4")
    os.environ.update(values)
    sys.dont_write_bytecode = True
    return values


def parse_args(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--bvid", required=True)
    parser.add_argument("--gpu", type=int, required=True)
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--model", type=Path, required=True)
    parser.add_argument("--source-sha256", required=True, help="SHA-256 of original compressed media, verified by caller")
    parser.add_argument("--input-sha256", help="Optional expected hash of this decoded WAV")
    parser.add_argument("--expected-duration", type=float, required=True)
    parser.add_argument("--cache-dir", type=Path)
    parser.add_argument("--batch-size", type=int, default=8, choices=range(1, 9))
    args = parser.parse_args(argv)
    if not re.fullmatch(r"BV[0-9A-Za-z]{10}", args.bvid) or args.gpu < 0:
        parser.error("A valid BV identifier and non-negative GPU index are required")
    if not math.isfinite(args.expected_duration) or args.expected_duration <= 0:
        parser.error("Expected duration must be finite and positive")
    for value in (args.source_sha256, args.input_sha256):
        if value is not None and not re.fullmatch(r"[0-9a-fA-F]{64}", value):
            parser.error("SHA-256 values must be 64 hexadecimal characters")
    return args


def run(args) -> dict:
    started = time.monotonic()
    output = args.output_dir.resolve()
    output.mkdir(parents=True, exist_ok=True)
    if any((output / filename).exists() for filename in ("source.json", "provenance.json", "generation-checks.jsonl")):
        raise FileExistsError("Use a fresh output directory to preserve previous run evidence")
    cache = (args.cache_dir or output / "cache").resolve()
    env = isolate_caches(cache)
    os.environ["CUDA_VISIBLE_DEVICES"] = str(args.gpu)
    input_path = args.input.resolve(strict=True)
    model_path = args.model.resolve(strict=True)
    if not model_path.is_dir():
        raise ValueError("--model must refer to a fully downloaded local model directory")
    model_config = json.loads((model_path / "config.json").read_text())
    text_config = model_config.get("thinker_config", {}).get("text_config", {})
    if (model_config.get("model_type") != "qwen3_asr"
            or (text_config.get("hidden_size"), text_config.get("num_hidden_layers")) != (2048, 28)):
        raise ValueError("This runner requires the Qwen3-ASR-1.7B architecture")
    wav_hash = sha256_file(input_path)
    if args.input_sha256 and wav_hash != args.input_sha256.lower():
        raise ValueError("Decoded WAV checksum mismatch")
    with wave.open(str(input_path), "rb") as reader:
        sr, total, channels, width = (reader.getframerate(), reader.getnframes(),
                                      reader.getnchannels(), reader.getsampwidth())
        if (sr, channels, width, reader.getcomptype()) != (16000, 1, 2, "NONE"):
            raise ValueError("Input must be uncompressed PCM16LE, mono, 16000 Hz")
        if total <= 0:
            raise ValueError("Empty audio")
        pcm_bytes = reader.readframes(total)
    if len(pcm_bytes) != total * width:
        raise ValueError("WAV data is shorter than its declared sample count")
    duration = total / sr
    if abs(duration - args.expected_duration) > 0.5:
        raise ValueError("Decoded WAV duration differs from expected source duration by more than 0.5 seconds")
    provenance = {
        "schema_version": 1, "status": "running", "bvid": args.bvid,
        "provider": "qwen-asr", "model": "Qwen/Qwen3-ASR-1.7B",
        "timestamp_kind": "audio_chunk", "started_at": datetime.now(timezone.utc).isoformat(),
        "input": {"sha256": wav_hash, "sample_rate": sr, "sample_count": total,
                  "duration_seconds": duration, "channels": channels, "sample_width_bytes": width,
                  "source_sha256": args.source_sha256.lower(),
                  "source_sha256_verification": "declared_by_caller", "expected_duration": args.expected_duration},
        "config": {"context": "", "language": "Chinese", "dtype": "bfloat16", "attention": "sdpa",
                   "batch_size": args.batch_size, "max_new_tokens": 4096, "do_sample": False,
                   "chunk_target_seconds": 60, "boundary_search_expand_seconds": 5,
                   "boundary_min_window_ms": 100, "retry_max_depth": 6, "retry_min_seconds": 2},
        "environment": env, "gpu_index": args.gpu,
        "model_config_sha256": sha256_file(model_path / "config.json"),
    }
    write_json(output / "provenance.json", provenance)
    try:
        # Deliberately lazy: --help and unit tests need no model packages or GPU.
        import importlib.metadata
        import numpy as np
        import torch
        from qwen_asr import Qwen3ASRModel
        from qwen_asr.inference.utils import MIN_ASR_INPUT_SECONDS, split_audio_into_chunks

        torch.set_num_threads(4)
        waveform = np.frombuffer(pcm_bytes, dtype="<i2").astype(np.float32) / 32768.0
        del pcm_bytes
        initial = spans_from_chunks(split_audio_into_chunks(waveform, sr, 60, 5, 100), total, sr)
        asr = Qwen3ASRModel.from_pretrained(str(model_path), dtype=torch.bfloat16,
                                           device_map="cuda:0", attn_implementation="sdpa",
                                           max_inference_batch_size=args.batch_size, max_new_tokens=4096)
        asr.model.generation_config.do_sample = False
        eos = asr.model.generation_config.eos_token_id
        eos_ids = {eos} if isinstance(eos, int) else set(eos or [])
        if not eos_ids:
            raise ValueError("Model must declare EOS tokens for completion checks")
        collected_checks = []
        original_generate = asr.model.generate

        def observed_generate(*positional, **kwargs):
            generated = original_generate(*positional, **kwargs)
            prompt_length = kwargs["input_ids"].shape[1]
            token_rows = generated.sequences[:, prompt_length:].detach().cpu().tolist()
            collected_checks.extend(generation_check(tokens, eos_ids, kwargs["max_new_tokens"])
                                    for tokens in token_rows)
            return generated

        asr.model.generate = observed_generate
        minimum_samples = math.ceil(MIN_ASR_INPUT_SECONDS * sr)

        def recognize(spans):
            collected_checks.clear()
            audio = []
            padding = []
            for span in spans:
                chunk = waveform[span.start:span.end]
                pad = max(0, minimum_samples - len(chunk))
                audio.append((np.pad(chunk, (0, pad)) if pad else chunk, sr))
                padding.append(pad)
            then = time.monotonic()
            results = asr.transcribe(audio=audio, context="", language="Chinese", return_time_stamps=False)
            torch.cuda.synchronize()
            elapsed = time.monotonic() - then
            if len(results) != len(spans) or len(collected_checks) != len(spans):
                raise ValueError("Unexpected internal chunking or missing generation checks")
            return [{"text": result.text, "language": result.language, "generation": check,
                     "padding_samples": pad, "batch_elapsed_seconds": round(elapsed, 6)}
                    for result, check, pad in zip(results, collected_checks, padding, strict=True)]

        def split_retry(span):
            seconds = (span.end - span.start) / sr
            if span.depth >= 6 or seconds <= 2:
                raise RuntimeError("ASR did not produce EOS after bounded smaller-chunk retries")
            target = min(30, seconds / 2)
            parts = split_audio_into_chunks(waveform[span.start:span.end], sr, target,
                                           min(5, target / 4), 100)
            return spans_from_chunks(parts, span.end - span.start, sr, span.start, span.depth + 1)

        accepted_samples = attempts = 0
        with (output / "generation-checks.jsonl").open("w", encoding="utf-8") as log:
            def on_attempt(span, result, accepted):
                nonlocal accepted_samples, attempts
                attempts += 1
                if accepted:
                    accepted_samples += span.end - span.start
                row = {"attempt": attempts, "start_sample": span.start, "end_sample": span.end,
                       "depth": span.depth, "accepted": accepted, **result}
                log.write(json.dumps(row, ensure_ascii=False) + "\n")
                log.flush()
                progress = {"status": "running", "attempts": attempts, "accepted_samples": accepted_samples,
                            "total_samples": total, "fraction": accepted_samples / total,
                            "elapsed_seconds": round(time.monotonic() - started, 3)}
                write_json(output / "progress.json", progress)
                print(json.dumps(progress), flush=True)

            recognized = transcribe_partition(initial, recognize, split_retry, args.batch_size, on_attempt)
        segments = []
        for index, item in enumerate(recognized):
            span = item.pop("span")
            segments.append({"id": index, "start": span.start / sr, "end": span.end / sr,
                             "start_sample": span.start, "end_sample": span.end,
                             "retry_depth": span.depth, **item})
        source = {"schema_version": 1, "bvid": args.bvid, "provider": "qwen-asr",
                  "model": "Qwen/Qwen3-ASR-1.7B", "language": "zh", "timestamp_kind": "audio_chunk",
                  "duration_seconds": duration, "text": "".join(item["text"] for item in segments),
                  "audio_provenance": provenance["input"], "segments": segments,
                  "coverage": {"complete": True, "sample_count": total, "no_gaps_or_overlaps": True}}
        write_json(output / "source.json", source)
        provenance.update(status="complete", finished_at=datetime.now(timezone.utc).isoformat(),
                          elapsed_seconds=round(time.monotonic() - started, 6),
                          segment_count=len(segments), attempts=attempts,
                          all_final_segments_have_eos=all(s["generation"]["eos_found"] for s in segments),
                          source_json_sha256=sha256_file(output / "source.json"),
                          generation_checks_sha256=sha256_file(output / "generation-checks.jsonl"),
                          peak_allocated_mib=round(torch.cuda.max_memory_allocated() / 1048576, 3),
                          packages={name: importlib.metadata.version(name) for name in
                                    ("qwen-asr", "transformers", "torch", "accelerate")},
                          torch_runtime_version=torch.__version__)
        write_json(output / "provenance.json", provenance)
        write_json(output / "progress.json", {"status": "complete", "fraction": 1,
                                              "segments": len(segments), "attempts": attempts})
        return provenance
    except Exception as error:
        provenance.update(status="failed", error=f"{type(error).__name__}: {error}",
                          elapsed_seconds=round(time.monotonic() - started, 6))
        write_json(output / "provenance.json", provenance)
        raise


def main():
    result = run(parse_args())
    print(json.dumps({"status": result["status"], "segments": result["segment_count"],
                      "elapsed_seconds": result["elapsed_seconds"]}), flush=True)


if __name__ == "__main__":
    main()
