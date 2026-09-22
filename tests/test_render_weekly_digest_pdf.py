import importlib.util
import unittest
from pathlib import Path


def load_module():
    path = Path(__file__).resolve().parents[1] / "work" / "render_weekly_digest_pdf.py"
    spec = importlib.util.spec_from_file_location("render_weekly_digest_pdf", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class RenderWeeklyDigestPdfTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.mod = load_module()

    def test_extract_report_date_from_chinese_title(self):
        blocks = self.mod.parse_blocks("# 全球与国内 AI 情报周报（2026-08-10）")
        self.assertEqual(self.mod.extract_report_date(blocks), "2026-08-10")

    def test_extract_report_date_rejects_missing_date(self):
        blocks = self.mod.parse_blocks("# 全球与国内 AI 情报周报")
        with self.assertRaisesRegex(ValueError, "YYYY-MM-DD"):
            self.mod.extract_report_date(blocks)

    def test_inline_markup_renders_named_links_without_raw_url(self):
        markup = self.mod.inline_markup("[官方发布](https://example.com/a?b=1&c=2)｜来源")
        self.assertIn('href="https://example.com/a?b=1&amp;c=2"', markup)
        self.assertIn("<u>官方发布</u>", markup)
        self.assertNotIn("](", markup)


if __name__ == "__main__":
    unittest.main()
