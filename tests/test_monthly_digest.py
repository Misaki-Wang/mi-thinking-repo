"""Keep the editorial monthly snapshot dated, attributable and non-automated."""

import json
import unittest
from datetime import date
from pathlib import Path
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parents[1] / "blog" / "ai-radar-2026-09"


class MonthlyDigestTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data = json.loads((ROOT / "manifest.json").read_text())
        cls.markdown = (ROOT / "README.md").read_text()

    def test_all_publication_dates_are_in_the_declared_window(self):
        start = date.fromisoformat(self.data["window_start"])
        end = date.fromisoformat(self.data["window_end"])
        self.assertLessEqual(start, end)
        for item in self.data["items"]:
            with self.subTest(item=item["id"]):
                published = date.fromisoformat(item["date"])
                self.assertLessEqual(start, published)
                self.assertLessEqual(published, end)
                self.assertLessEqual(published, date.fromisoformat(item["verified_on"]))
                self.assertTrue(item["publication_date_basis"])

    def test_unique_items_sources_and_tier_counts(self):
        items = self.data["items"]
        self.assertEqual(len(items), 19)
        self.assertEqual(len({item["id"] for item in items}), len(items))
        self.assertEqual(len({item["url"] for item in items}), len(items))
        for tier, key in (("core", "core_count"), ("extra", "extra_count")):
            self.assertEqual(sum(item["tier"] == tier for item in items), self.data[key])
        self.assertEqual(self.data["core_count"], 12)
        self.assertEqual(self.data["extra_count"], 7)
        sources = {item["source_id"] for item in items}
        self.assertEqual(sources, set(self.data["source_ids"]))
        self.assertEqual(len(sources), self.data["source_count"])

    def test_every_item_has_attribution_public_link_and_visible_entry(self):
        for item in self.data["items"]:
            with self.subTest(item=item["id"]):
                self.assertTrue(item["author"] and item["title"] and item["basis"])
                self.assertEqual(urlsplit(item["url"]).scheme, "https")
                self.assertTrue(urlsplit(item["url"]).hostname)
                self.assertIn("### " + item["id"] + "\n", self.markdown)
                self.assertIn(item["url"], self.markdown)
                self.assertIn(item["date"], self.markdown)

    def test_review_depth_and_static_scope_stay_explicit(self):
        self.assertIs(self.data["automatic_updates"], False)
        self.assertEqual(self.data["mode"], "static_curated_snapshot")
        preview = next(item for item in self.data["items"] if item["id"] == "V02")
        self.assertIn("仅作者简介", preview["basis"])
        self.assertIn("不冒充精读", self.markdown)
        self.assertIn("本月文章复盘更早事件", self.markdown)
        self.assertIn("7×7 grid 每格 1 seed", self.markdown)

    def test_guidance_links_only_to_existing_item_ids(self):
        import re
        links = re.findall(r"README\.md#([a-z][0-9]{2})", (ROOT / "GUIDANCE.md").read_text())
        known = {item["id"].lower() for item in self.data["items"]}
        self.assertTrue(links)
        self.assertTrue(set(links).issubset(known))


if __name__ == "__main__":
    unittest.main()
