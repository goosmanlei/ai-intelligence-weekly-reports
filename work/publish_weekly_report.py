#!/usr/bin/env python3
import argparse
import re
import subprocess
import sys
from pathlib import Path
from typing import Iterable, Optional


DATE_PATTERN = re.compile(r"^\d{4}-\d{2}-\d{2}$")


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--date", required=True)
    parser.add_argument("--pdf", required=True)
    parser.add_argument("--markdown", required=True)
    parser.add_argument("--state-file", default="work/x_list_state.json")
    parser.add_argument("--repo", default=".")
    parser.add_argument("--remote", default="origin")
    parser.add_argument("--branch", default="main")
    return parser.parse_args()


def run_git(repo: Path, args: Iterable[str], check: bool = True) -> subprocess.CompletedProcess:
    proc = subprocess.run(
        ["git", "-C", str(repo), *args],
        capture_output=True,
        text=True,
    )
    if check and proc.returncode != 0:
        detail = proc.stderr.strip() or proc.stdout.strip()
        raise RuntimeError(f"git {' '.join(args)} failed: {detail}")
    return proc


def resolve_repo_root(repo: Path) -> Path:
    proc = run_git(repo, ["rev-parse", "--show-toplevel"])
    return Path(proc.stdout.strip()).resolve()


def resolve_publish_path(root: Path, raw_path: str, required: bool = True) -> Optional[Path]:
    root = root.resolve()
    path = Path(raw_path)
    if not path.is_absolute():
        path = root / path
    path = path.resolve()
    try:
        relative = path.relative_to(root)
    except ValueError as exc:
        raise RuntimeError(f"publish path is outside the repository: {path}") from exc
    if ".env" in relative.parts:
        raise RuntimeError("refusing to publish an environment file")
    if not path.exists():
        if required:
            raise RuntimeError(f"publish file does not exist: {path}")
        return None
    return relative


def publish_report(
    repo: Path,
    report_date: str,
    pdf: str,
    markdown: str,
    state_file: str,
    remote: str = "origin",
    branch: str = "main",
) -> dict:
    if not DATE_PATTERN.fullmatch(report_date):
        raise RuntimeError("date must use YYYY-MM-DD")

    root = resolve_repo_root(repo)
    publish_paths = [
        resolve_publish_path(root, pdf),
        resolve_publish_path(root, markdown),
        resolve_publish_path(root, state_file, required=False),
    ]
    relative_paths = [str(path) for path in publish_paths if path is not None]
    run_git(root, ["add", "--", *relative_paths])

    staged = run_git(root, ["diff", "--cached", "--quiet"], check=False)
    if staged.returncode == 0:
        return {"committed": False, "pushed": False, "commit": None}
    if staged.returncode != 1:
        raise RuntimeError("unable to inspect staged report changes")

    run_git(root, ["commit", "-m", f"weekly report: {report_date}"])
    commit = run_git(root, ["rev-parse", "HEAD"]).stdout.strip()
    run_git(root, ["push", remote, f"HEAD:{branch}"])
    return {"committed": True, "pushed": True, "commit": commit}


def main():
    args = parse_args()
    result = publish_report(
        repo=Path(args.repo),
        report_date=args.date,
        pdf=args.pdf,
        markdown=args.markdown,
        state_file=args.state_file,
        remote=args.remote,
        branch=args.branch,
    )
    if result["committed"]:
        print(f"published commit {result['commit']}")
    else:
        print("no report changes to publish")


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        print(str(exc), file=sys.stderr)
        sys.exit(1)
