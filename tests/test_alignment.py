"""Behavioral fixtures for conservative paragraph/slide association."""
import importlib.util
from pathlib import Path
import unittest

SPEC = importlib.util.spec_from_file_location("align_slides", Path(__file__).resolve().parents[1] / "scripts/align_slides.py")
alignment = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(alignment)


def pages(*texts, deck="current"):
    return [{"deck_id": deck, "slide_id": f"{deck}-p{i:03}", "page": i, "text": text}
            for i, text in enumerate(texts, 1)]


def blocks(*texts):
    return [{"block_id": f"b{i:06}", "text": text} for i, text in enumerate(texts, 1)]


class AlignmentTests(unittest.TestCase):
    def test_content_not_fraction_of_running_time_drives_pages(self):
        slides = pages("Linear regression minimizes squared errors with coefficients and intercepts.",
                       "Support vector machines maximize the classification margin with support vectors.",
                       "Gaussian mixture models use latent components and expectation maximization.",
                       "Convolution kernels have local receptive fields and shared image weights.")
        matched, _ = alignment.align(blocks(
            "Gaussian mixture models use latent components and expectation maximization.",
            "Expectation maximization estimates latent components in Gaussian mixture models.",
            "Convolution kernels have local receptive fields and shared image weights."), slides)
        self.assertEqual([item["slide_id"] for item in matched], ["current-p003", "current-p003", "current-p004"])

    def test_recap_can_begin_in_different_deck_then_switch(self):
        slides = pages("Tensor fusion computes multiplicative outer products across representations.",
                       "EMAP measures non additive interactions by additive projection.", deck="prior")
        slides += pages("Contrastive learning pulls positive pairs together and pushes negatives apart.",
                        "Optimal transport uses marginal constraints and soft matching distributions.")
        matched, _ = alignment.align(blocks(
            "EMAP measures non additive interactions by additive projection.",
            "Contrastive learning pulls positive pairs together and pushes negatives apart.",
            "Optimal transport uses marginal constraints and soft matching distributions."), slides)
        self.assertEqual([item["slide_id"] for item in matched], ["prior-p002", "current-p001", "current-p002"])

    def test_questions_and_visual_only_pages_not_filled_by_interpolation(self):
        slides = pages("Bayesian inference combines prior probability with observed likelihood.",
                       "Diagram", "Convolution kernels have local receptive fields and shared image weights.")
        matched, _ = alignment.align(blocks(
            "Bayesian inference combines prior probability with observed likelihood.",
            "Can everybody hear the microphone? The next homework deadline is tomorrow.",
            "Convolution kernels have local receptive fields and shared image weights."), slides)
        self.assertIsNone(matched[1]["slide_id"])
        self.assertEqual(matched[1]["confidence"], "unmatched")
        self.assertNotIn("current-p002", [item["slide_id"] for item in matched])

    def test_duplicate_builds_do_not_claim_exact_page(self):
        slide = "Mutual information measures the shared statistical dependence between paired variables."
        matched, _ = alignment.align(blocks(slide), pages(slide, slide))
        self.assertIsNone(matched[0]["slide_id"])
        self.assertEqual(matched[0]["ambiguity_slide_ids"], ["current-p001", "current-p002"])
        self.assertEqual(len(matched[0]["candidates"]), 2)

    def test_slide_only_extension_never_gets_automatic_match(self):
        slide = "Quantification examines robustness fairness and reliability of multimodal systems."
        data = pages(slide)
        data[0]["slide_only"] = True
        matched, _ = alignment.align(blocks(slide), data)
        self.assertIsNone(matched[0]["slide_id"])
        self.assertEqual(matched[0]["candidates"], [])

    def test_out_of_order_topic_is_unmatched_not_wrongly_assigned(self):
        data = pages("Convolution kernels preserve local receptive fields within natural image tensors.",
                     "Markov chains describe discrete states and transition probabilities.")
        matched, _ = alignment.align(blocks(data[1]["text"], data[1]["text"], data[0]["text"]), data)
        self.assertEqual(matched[0]["slide_id"], "current-p002")
        self.assertIsNone(matched[-1]["slide_id"])
        self.assertEqual(matched[-1]["candidates"][0]["slide_id"], "current-p001")

    def test_coarse_topic_hint_cannot_invent_unrelated_association(self):
        data = pages("Gaussian mixture models use latent components and expectation maximization.",
                     "Convolution kernels have local receptive fields and shared image weights.")
        paragraph = blocks(data[0]["text"])[0]
        paragraph["start_ms"] = 600000
        matched, _ = alignment.align([paragraph], data, "current", [(100, 3)])
        self.assertIsNone(matched[0]["slide_id"])
        self.assertEqual(matched[0]["candidates"][0]["slide_id"], "current-p001")

    def test_reference_citation_does_not_make_an_image_page_informative(self):
        data = pages("Diagram [Liang et al., Contrastive Representation Learning With Neural Networks.]")
        matched, slides = alignment.align(blocks("Contrastive representation learning trains neural networks."), data)
        self.assertEqual(slides[0]["text_quality"], "sparse-text")
        self.assertIsNone(matched[0]["slide_id"])


if __name__ == "__main__":
    unittest.main()
