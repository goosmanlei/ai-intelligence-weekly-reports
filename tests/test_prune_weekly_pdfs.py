import subprocess
import tempfile
import unittest
from pathlib import Path


SCRIPT = Path(__file__).resolve().parents[1] / "work" / "prune_weekly_pdfs.py"


class PruneWeeklyPdfsTest(unittest.TestCase):
    def test_keeps_latest_dates_across_filename_prefixes(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            target = Path(temp_dir)
            names = [
                "anthropic-claude-code-x-weekly-2026-06-22.pdf",
                "ai-frontiers-weekly-2026-07-06.pdf",
                "global-china-ai-weekly-2026-08-03.pdf",
            ]
            for name in names:
                (target / name).write_bytes(b"pdf")

            subprocess.run(
                ["python3", str(SCRIPT), "--dir", str(target), "--keep", "2"],
                check=True,
            )

            self.assertEqual(
                sorted(path.name for path in target.glob("*.pdf")),
                [
                    "ai-frontiers-weekly-2026-07-06.pdf",
                    "global-china-ai-weekly-2026-08-03.pdf",
                ],
            )


if __name__ == "__main__":
    unittest.main()
