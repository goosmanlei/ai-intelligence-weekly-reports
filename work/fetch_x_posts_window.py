#!/usr/bin/env python3
import argparse
import json
import re
import subprocess
from datetime import datetime, timezone
from email.utils import parsedate_to_datetime
from html import unescape
from pathlib import Path
from typing import Optional


ACCOUNTS = [
    "DarioAmodei",
    "karpathy",
    "bcherny",
    "trq212",
    "_catwu",
    "noahzweben",
    "alexalbert__",
    "jackclarkSF",
    "mikeyk",
]

BEARER_TOKEN = (
    "AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D"
    "1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA"
)
USER_TWEETS_QUERY_ID = "CnSnoo277oTfdVQPIsRIbA"
SNOWFLAKE_EPOCH_MS = 1288834974657


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--window-start", required=True)
    parser.add_argument("--window-end", required=True)
    parser.add_argument("--output", required=True)
    parser.add_argument("--supplemental-url-file")
    parser.add_argument("--status-cache-dir")
    return parser.parse_args()


def run_curl(url: str, headers=None, method="GET") -> str:
    cmd = ["curl", "-sS", "-L", "--max-time", "30", url]
    if method != "GET":
        cmd.extend(["-X", method])
    for header in headers or []:
        cmd.extend(["-H", header])
    proc = subprocess.run(cmd, capture_output=True, text=True, check=True)
    return proc.stdout


def parse_iso(ts: str) -> datetime:
    return datetime.fromisoformat(ts).astimezone(timezone.utc)


def snowflake_datetime(status_id: str):
    try:
        value = int(status_id)
    except ValueError:
        return None
    ms = (value >> 22) + SNOWFLAKE_EPOCH_MS
    return datetime.fromtimestamp(ms / 1000, tz=timezone.utc)


def get_guest_token() -> str:
    payload = run_curl(
        "https://api.twitter.com/1.1/guest/activate.json",
        headers=[f"Authorization: Bearer {BEARER_TOKEN}"],
        method="POST",
    )
    return json.loads(payload)["guest_token"]


def graphql_variables(account: str, count: int = 100) -> str:
    return json.dumps({"screenName": account, "count": count, "cursor": None}, separators=(",", ":"))


def fetch_graphql_status_ids(account: str, guest_token: str) -> set[str]:
    variables = graphql_variables(account)
    url = (
        "https://api.twitter.com/graphql/"
        f"{USER_TWEETS_QUERY_ID}/UserTweets?variables="
        f"{quote(variables)}"
    )
    payload = run_curl(
        url,
        headers=[
            f"Authorization: Bearer {BEARER_TOKEN}",
            f"x-guest-token: {guest_token}",
        ],
    )
    data = json.loads(payload)
    timeline = (
        data.get("data", {})
        .get("user_result_by_screen_name", {})
        .get("result", {})
        .get("profile_timeline_v2", {})
        .get("timeline", {})
    )
    ids = set()
    for instruction in timeline.get("instructions", []):
        typename = instruction.get("__typename")
        if typename == "TimelinePinEntry":
            entry = instruction.get("entry")
            if entry:
                add_entry_id(entry, ids)
        elif typename == "TimelineAddEntries":
            for entry in instruction.get("entries", []):
                add_entry_id(entry, ids)
    return ids


def add_entry_id(entry: dict, target: set[str]):
    entry_id = entry.get("entry_id") or entry.get("entryId")
    if not isinstance(entry_id, str):
        return
    if entry_id.startswith("tweet-"):
        target.add(entry_id.removeprefix("tweet-"))


def fetch_syndication_status_ids(account: str) -> set[str]:
    html = run_curl(f"https://syndication.twitter.com/srv/timeline-profile/screen-name/{account}")
    match = re.search(r'<script id="__NEXT_DATA__" type="application/json">(.*?)</script>', html)
    if not match:
        return set()
    data = json.loads(match.group(1))
    entries = data.get("props", {}).get("pageProps", {}).get("timeline", {}).get("entries", [])
    ids = set()
    for entry in entries:
        if entry.get("type") != "tweet":
            continue
        tweet = entry.get("content", {}).get("tweet", {})
        status_id = tweet.get("id_str")
        if status_id:
            ids.add(status_id)
    return ids


def fetch_profile_status_ids(account: str) -> set[str]:
    html = run_curl(f"https://x.com/{account}")
    patterns = [
        rf'data-href="/{re.escape(account)}/status/(\d+)"',
        rf'href="/{re.escape(account)}/status/(\d+)"',
        rf'"https://x.com/{re.escape(account)}/status/(\d+)"',
    ]
    ids = set()
    for pattern in patterns:
        ids.update(re.findall(pattern, html))
    return ids


def load_supplemental_ids(path: Optional[str]) -> dict[str, set[str]]:
    result = {account: set() for account in ACCOUNTS}
    if not path:
        return result
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    if isinstance(data, dict):
        items = data.items()
        for account, urls in items:
            if account in result:
                result[account].update(ids_from_url_values(urls))
        return result
    if isinstance(data, list):
        for item in data:
            if isinstance(item, str):
                account, status_id = account_and_id_from_url(item)
                if account in result and status_id:
                    result[account].add(status_id)
            elif isinstance(item, dict):
                account = item.get("account")
                urls = item.get("urls") or item.get("url")
                if account in result:
                    result[account].update(ids_from_url_values(urls))
    return result


def ids_from_url_values(value) -> set[str]:
    if isinstance(value, str):
        _, status_id = account_and_id_from_url(value)
        return {status_id} if status_id else set()
    ids = set()
    if isinstance(value, list):
        for item in value:
            ids.update(ids_from_url_values(item))
    return ids


def account_and_id_from_url(url: str):
    match = re.search(r"x\.com/([^/]+)/status/(\d+)", url)
    if not match:
        return None, None
    return match.group(1), match.group(2)


def cache_path(cache_dir: Optional[Path], account: str, status_id: str):
    if not cache_dir:
        return None
    cache_dir.mkdir(parents=True, exist_ok=True)
    return cache_dir / f"{account}-{status_id}.status.html"


def fetch_status_html(account: str, status_id: str, cache_dir: Optional[Path]):
    path = cache_path(cache_dir, account, status_id)
    if path and path.exists():
        return path.read_text(encoding="utf-8", errors="ignore")
    html = run_curl(f"https://x.com/{account}/status/{status_id}")
    if path:
        path.write_text(html, encoding="utf-8")
    return html


def extract_target_slice(html: str, status_id: str) -> str:
    needles = [
        f"TweetResults:{status_id}",
        f'"rest_id":"{status_id}"',
        f'"rest_id":"{status_id}"'.replace('"', ""),
        f"twitter://status?id={status_id}",
    ]
    for needle in needles:
        idx = html.find(needle)
        if idx != -1:
            start = max(0, idx - 4000)
            end = min(len(html), idx + 30000)
            return html[start:end]
    return html


def decode_json_string(text: str) -> str:
    try:
        return json.loads(f'"{text}"')
    except json.JSONDecodeError:
        return unescape(text.replace('\\"', '"').replace("\\n", "\n"))


def extract_status_details(account: str, status_id: str, html: str):
    slice_text = extract_target_slice(html, status_id)
    created_at_ms = None
    for pattern in [r"created_at_ms[:\"]+(\d{10,})", r'"created_at_ms":"?(\d{10,})"?']:
        match = re.search(pattern, slice_text)
        if match:
            created_at_ms = int(match.group(1))
            break
    if created_at_ms is None:
        snowflake_time = snowflake_datetime(status_id)
        created_at = snowflake_time.isoformat() if snowflake_time else None
    else:
        created_at = datetime.fromtimestamp(created_at_ms / 1000, tz=timezone.utc).isoformat()

    text = None
    match = re.search(r'"full_text":"((?:\\.|[^"\\])*)"', slice_text)
    if match:
        text = decode_json_string(match.group(1))
    if not text:
        match = re.search(r'<meta property="og:description" content="([^"]*)"', html)
        if match:
            text = unescape(match.group(1))
    if not text:
        match = re.search(r"<title>.*? on X: &quot;(.*?)&quot; / X</title>", html)
        if match:
            text = unescape(match.group(1))
    if not text or not created_at:
        return None
    return {
        "id": status_id,
        "created_at": created_at,
        "full_text": text.strip(),
        "permalink": f"https://x.com/{account}/status/{status_id}",
    }


def quote(value: str) -> str:
    return subprocess.run(
        ["python3", "-c", "import sys, urllib.parse; print(urllib.parse.quote(sys.stdin.read()))"],
        input=value,
        text=True,
        capture_output=True,
        check=True,
    ).stdout.strip()


def collect_ids(account: str, guest_token: str, supplemental_ids: dict[str, set[str]]) -> dict[str, list[str]]:
    sources = {
        "graphql": sorted(fetch_graphql_status_ids(account, guest_token)),
        "syndication": sorted(fetch_syndication_status_ids(account)),
        "profile": sorted(fetch_profile_status_ids(account)),
        "supplemental": sorted(supplemental_ids.get(account, set())),
    }
    return sources


def ids_in_window(ids: set[str], start: datetime, end: datetime) -> set[str]:
    result = set()
    for status_id in ids:
        created_at = snowflake_datetime(status_id)
        if created_at and start <= created_at < end:
            result.add(status_id)
    return result


def main():
    args = parse_args()
    start = parse_iso(args.window_start)
    end = parse_iso(args.window_end)
    output_path = Path(args.output)
    cache_dir = Path(args.status_cache_dir) if args.status_cache_dir else None
    supplemental_ids = load_supplemental_ids(args.supplemental_url_file)
    guest_token = get_guest_token()

    result = {
        "window_start": args.window_start,
        "window_end": args.window_end,
        "accounts": [],
    }

    for account in ACCOUNTS:
        source_ids = collect_ids(account, guest_token, supplemental_ids)
        merged_ids = set()
        for ids in source_ids.values():
            merged_ids.update(ids)
        candidate_ids = ids_in_window(merged_ids, start, end)
        posts = []
        for status_id in sorted(candidate_ids, key=int, reverse=True):
            try:
                html = fetch_status_html(account, status_id, cache_dir)
                details = extract_status_details(account, status_id, html)
            except subprocess.CalledProcessError:
                details = None
            if details:
                posts.append(details)
        result["accounts"].append(
            {
                "account": account,
                "posts": posts,
                "debug_sources": {name: len(ids) for name, ids in source_ids.items()},
            }
        )

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")


if __name__ == "__main__":
    main()
