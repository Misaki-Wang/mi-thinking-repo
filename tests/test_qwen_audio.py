"""Model-free coverage, truncation and raw-text accounting checks."""
import importlib.util
from pathlib import Path
import sys
import unittest

spec = importlib.util.spec_from_file_location("qwen_audio", Path(__file__).resolve().parents[1] / "scripts/transcribe_qwen_audio.py")
core = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = core
spec.loader.exec_module(core)


class QwenAudioTests(unittest.TestCase):
    def test_tail_padding_clamped_and_real_audio_partitioned(self):
        parts = [(list(range(6)), 0), (list(range(6)), 0.6), (list(range(5)), 1.2)]
        spans = core.spans_from_chunks(parts, 13, 10)
        self.assertEqual(spans, [core.Span(0, 6), core.Span(6, 12), core.Span(12, 13)])

    def test_gap_overlap_and_missing_tail_rejected(self):
        for spans in ([core.Span(0, 4), core.Span(5, 10)],
                      [core.Span(0, 6), core.Span(5, 10)], [core.Span(0, 9)]):
            with self.assertRaises(ValueError):
                core.validate_partition(spans, 0, 10)

    def test_offset_roundoff_maps_to_exact_samples(self):
        parts = [([0] * 3, 0), ([0] * 4, 0.30000000000000004)]
        self.assertEqual(core.spans_from_chunks(parts, 7, 10), [core.Span(0, 3), core.Span(3, 7)])

    def test_eos_before_batch_padding_is_complete(self):
        check = core.generation_check([10, 11, 99, 0, 0], {99}, 5)
        self.assertFalse(check["needs_retry"])
        self.assertEqual(check["generated_token_count"], 3)
        self.assertFalse(check["hit_token_limit"])

    def test_cap_and_early_stop_without_eos_require_retry(self):
        self.assertTrue(core.generation_check([1, 2, 3], {99}, 3)["hit_token_limit"])
        self.assertTrue(core.generation_check([1, 2], {99}, 3)["needs_retry"])
        self.assertFalse(core.generation_check([1, 2, 99], {99}, 3)["hit_token_limit"])

    def test_capped_middle_interval_replaced_once_in_order_empty_text_preserved(self):
        initial = [core.Span(0, 10), core.Span(10, 20), core.Span(20, 30)]
        attempts = []
        def recognize(spans):
            return [{"text": "" if span.start == 20 else f" raw {span.start} ",
                     "generation": {"needs_retry": span.start == 10 and span.depth == 0}}
                    for span in spans]
        def split(span):
            return [core.Span(10, 15, 1), core.Span(15, 20, 1)]
        result = core.transcribe_partition(initial, recognize, split, 3,
                                          lambda *args: attempts.append(args))
        self.assertEqual([row["span"] for row in result],
                         [core.Span(0, 10), core.Span(10, 15, 1), core.Span(15, 20, 1), core.Span(20, 30)])
        self.assertEqual([row["text"] for row in result], [" raw 0 ", " raw 10 ", " raw 15 ", ""])
        self.assertEqual(len(attempts), 5)
        self.assertEqual(sum(row[0].end - row[0].start for row in attempts if row[2]), 30)

    def test_retry_must_be_smaller_and_cover_failed_range(self):
        def recognize(spans):
            return [{"text": "rejected", "generation": {"needs_retry": True}} for _ in spans]
        for retry in (lambda span: [span], lambda span: [core.Span(0, 3, 1), core.Span(4, 10, 1)]):
            with self.assertRaises(ValueError):
                core.transcribe_partition([core.Span(0, 10)], recognize, retry, 1)

    def test_result_count_mismatch_rejected(self):
        with self.assertRaises(ValueError):
            core.transcribe_partition([core.Span(0, 10)], lambda spans: [], lambda span: [], 1)

    def test_invalid_chunk_offset_rejected(self):
        for offset in (-1, float("nan"), float("inf")):
            with self.assertRaises(ValueError):
                core.spans_from_chunks([([0], offset)], 1, 1)


if __name__ == "__main__":
    unittest.main()
