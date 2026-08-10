import subprocess
import tempfile
import unittest
from pathlib import Path

from work.publish_weekly_report import publish_report, resolve_publish_path


def git(repo: Path, *args: str) -> str:
    proc = subprocess.run(
        ["git", "-C", str(repo), *args],
        check=True,
        capture_output=True,
        text=True,
    )
    return proc.stdout.strip()


class PublishWeeklyReportTest(unittest.TestCase):
    def test_commits_and_pushes_only_report_and_state_files(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            base = Path(temp_dir)
            repo = base / "repo"
            remote = base / "remote.git"
            repo.mkdir()
            git(repo, "init", "-b", "main")
            git(repo, "config", "user.name", "Weekly Report Test")
            git(repo, "config", "user.email", "weekly-report@example.com")
            subprocess.run(["git", "init", "--bare", str(remote)], check=True, capture_output=True)
            git(repo, "remote", "add", "origin", str(remote))

            pdf = repo / "outputs/weekly-pdf/global-china-ai-weekly-2026-08-03.pdf"
            markdown = repo / "outputs/weekly-markdown/global-china-ai-weekly-2026-08-03.md"
            state = repo / "work/x_list_state.json"
            project_state = repo / "STATE.md"
            secret = repo / ".env"
            unrelated = repo / "notes.txt"
            for path, content in (
                (pdf, "pdf"),
                (markdown, "report"),
                (state, "{}"),
                (project_state, "current state"),
                (secret, "X_BEARER_TOKEN=secret"),
                (unrelated, "do not publish"),
            ):
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text(content, encoding="utf-8")

            result = publish_report(
                repo,
                "2026-08-03",
                str(pdf),
                str(markdown),
                str(state),
            )

            self.assertTrue(result["pushed"])
            tracked = set(git(repo, "ls-files").splitlines())
            self.assertEqual(
                tracked,
                {
                    "outputs/weekly-markdown/global-china-ai-weekly-2026-08-03.md",
                    "outputs/weekly-pdf/global-china-ai-weekly-2026-08-03.pdf",
                    "STATE.md",
                    "work/x_list_state.json",
                },
            )
            self.assertNotIn(".env", tracked)
            self.assertNotIn("notes.txt", tracked)
            self.assertEqual(git(repo, "rev-parse", "HEAD"), git(remote, "rev-parse", "refs/heads/main"))

    def test_rejects_environment_file(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            env_file = root / ".env"
            env_file.write_text("secret", encoding="utf-8")
            with self.assertRaisesRegex(RuntimeError, "environment file"):
                resolve_publish_path(root, str(env_file))


if __name__ == "__main__":
    unittest.main()
