#!/usr/bin/env python3
import argparse
import json
import subprocess
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, List, Optional, Tuple
from urllib.parse import urlencode


API_BASE_URL = "https://api.x.com/2"
TWEET_FIELDS = "created_at,author_id,public_metrics,attachments,referenced_tweets"
EXPANSIONS = "author_id,attachments.media_keys"
USER_FIELDS = "username,name,verified"
MEDIA_FIELDS = "type,url,preview_image_url,alt_text,duration_ms"
RETRYABLE_STATUSES = {0, 429, 500, 502, 503, 504}
MAX_FETCH_ATTEMPTS = 4
RETRY_BACKOFF_SECONDS = 2


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--window-start", required=True)
    parser.add_argument("--window-end", required=True)
    parser.add_argument("--output", required=True)
    parser.add_argument("--env-file", default=".env")
    parser.add_argument("--state-file", default="work/x_list_state.json")
    parser.add_argument("--max-results", type=int, default=20)
    return parser.parse_args()


def load_env_file(path: Path) -> Dict[str, str]:
    if not path.exists():
        raise RuntimeError(f"missing env file: {path}")
    env = {}
    for raw_line in path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        normalized = value.strip()
        if len(normalized) >= 2 and normalized[0] == normalized[-1] and normalized[0] in {'"', "'"}:
            normalized = normalized[1:-1]
        env[key.strip()] = normalized
    return env


def load_state_file(path: Path) -> Dict[str, object]:
    if not path.exists():
        return {}
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise RuntimeError(f"state file must contain a JSON object: {path}")
    return data


def save_state_file(path: Path, state: Dict[str, object]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(state, ensure_ascii=False, indent=2), encoding="utf-8")


def parse_iso(ts: str) -> datetime:
    return datetime.fromisoformat(ts.replace("Z", "+00:00")).astimezone(timezone.utc)


def parse_x_datetime(ts: str) -> datetime:
    return datetime.fromisoformat(ts.replace("Z", "+00:00")).astimezone(timezone.utc)


def run_curl_json(url: str, bearer_token: str) -> Tuple[int, dict]:
    cmd = [
        "curl",
        "-sS",
        "-L",
        "--max-time",
        "30",
        "-w",
        "\n%{http_code}",
        "-H",
        f"Authorization: Bearer {bearer_token}",
        url,
    ]
    proc = subprocess.run(cmd, capture_output=True, text=True)
    body = proc.stdout if proc.stdout else proc.stderr
    status = 500
    if proc.stdout:
        payload, sep, trailing = proc.stdout.rpartition("\n")
        if sep and trailing.isdigit():
            body = payload
            status = int(trailing)
    try:
        data = json.loads(body)
    except json.JSONDecodeError:
        data = {"raw": body}
    if status == 500:
        status = extract_status_code(proc, data)
    return status, data


def extract_status_code(proc: subprocess.CompletedProcess, data: dict) -> int:
    if isinstance(data, dict):
        if isinstance(data.get("status"), int):
            return int(data["status"])
        if isinstance(data.get("errors"), list) and data["errors"]:
            first = data["errors"][0]
            if isinstance(first, dict) and isinstance(first.get("code"), int):
                return int(first["code"])
    return 200 if proc.returncode == 0 else 500


def build_list_tweets_url(list_id: str, max_results: int, pagination_token: Optional[str]) -> str:
    params = {
        "max_results": str(max_results),
        "tweet.fields": TWEET_FIELDS,
        "expansions": EXPANSIONS,
        "user.fields": USER_FIELDS,
        "media.fields": MEDIA_FIELDS,
    }
    if pagination_token:
        params["pagination_token"] = pagination_token
    return f"{API_BASE_URL}/lists/{list_id}/tweets?{urlencode(params)}"


def fetch_page_with_retries(url: str, bearer_token: str) -> Tuple[int, dict]:
    last_status = 500
    last_page = {}
    for attempt in range(1, MAX_FETCH_ATTEMPTS + 1):
        status, page = run_curl_json(url, bearer_token)
        if status == 200:
            return status, page
        last_status = status
        last_page = page
        if status not in RETRYABLE_STATUSES or attempt == MAX_FETCH_ATTEMPTS:
            break
        time.sleep(RETRY_BACKOFF_SECONDS * attempt)
    return last_status, last_page


def build_post(tweet: dict, users_by_id: Dict[str, dict], media_by_key: Dict[str, dict]) -> dict:
    author = users_by_id.get(tweet.get("author_id"), {})
    username = author.get("username")
    media = []
    for media_key in tweet.get("attachments", {}).get("media_keys", []):
        item = media_by_key.get(media_key)
        if item:
            media.append(
                {
                    "media_key": media_key,
                    "type": item.get("type"),
                    "url": item.get("url"),
                    "preview_image_url": item.get("preview_image_url"),
                    "alt_text": item.get("alt_text"),
                    "duration_ms": item.get("duration_ms"),
                }
            )
    permalink = (
        f"https://x.com/{username}/status/{tweet['id']}"
        if username
        else f"https://x.com/i/web/status/{tweet['id']}"
    )
    return {
        "id": tweet["id"],
        "created_at": parse_x_datetime(tweet["created_at"]).isoformat(),
        "text": tweet.get("text", "").strip(),
        "permalink": permalink,
        "author": {
            "id": tweet.get("author_id"),
            "name": author.get("name"),
            "username": username,
            "verified": author.get("verified"),
        },
        "public_metrics": tweet.get("public_metrics", {}),
        "media": media,
        "referenced_tweets": tweet.get("referenced_tweets", []),
    }


def normalize_page(
    page: dict,
    start: datetime,
    end: datetime,
    stop_at_tweet_id: Optional[str] = None,
) -> Tuple[List[dict], Optional[datetime], bool]:
    includes = page.get("includes", {})
    users_by_id = {user["id"]: user for user in includes.get("users", []) if "id" in user}
    media_by_key = {media["media_key"]: media for media in includes.get("media", []) if "media_key" in media}
    posts = []
    oldest = None
    hit_boundary = False
    for tweet in page.get("data", []):
        if stop_at_tweet_id and tweet.get("id") == stop_at_tweet_id:
            hit_boundary = True
            break
        created = parse_x_datetime(tweet["created_at"])
        if oldest is None or created < oldest:
            oldest = created
        if start <= created < end:
            posts.append(build_post(tweet, users_by_id, media_by_key))
    return posts, oldest, hit_boundary


def raise_api_error(status: int, data: dict):
    detail = data.get("detail") if isinstance(data, dict) else None
    title = data.get("title") if isinstance(data, dict) else None
    if status == 401:
        raise RuntimeError("x api unauthorized: check X_BEARER_TOKEN")
    if status == 402:
        raise RuntimeError(f"x api credits depleted: {detail or title or 'CreditsDepleted'}")
    if status == 403:
        raise RuntimeError(f"x api forbidden: {detail or title or 'Forbidden'}")
    if status == 404:
        raise RuntimeError(f"x api list not found: {detail or title or 'Not Found'}")
    raise RuntimeError(f"x api request failed with status {status}: {detail or title or data}")


def fetch_window(
    list_id: str,
    bearer_token: str,
    start: datetime,
    end: datetime,
    max_results: int,
    state: Dict[str, object],
) -> dict:
    pagination_token = None
    state_last_seen_tweet_id = str(state.get("last_seen_tweet_id") or "").strip() or None
    state_last_seen_created_at = str(state.get("last_seen_created_at") or "").strip() or None
    stop_at_tweet_id = state_last_seen_tweet_id
    boundary_ignored_reason = None
    if stop_at_tweet_id and state_last_seen_created_at:
        if parse_iso(state_last_seen_created_at) >= start:
            stop_at_tweet_id = None
            boundary_ignored_reason = "last_seen_created_at_not_before_window_start"
    pages_fetched = 0
    api_posts_seen = 0
    posts = []
    seen_ids = set()
    newest_seen_tweet_id = None
    newest_seen_created_at = None
    stop_reason = "no_more_pages"

    while True:
        status, page = fetch_page_with_retries(
            build_list_tweets_url(list_id, max_results, pagination_token),
            bearer_token,
        )
        if status != 200:
            raise_api_error(status, page)

        page_data = page.get("data", [])
        if newest_seen_tweet_id is None:
            for tweet in page_data:
                created_at = tweet.get("created_at")
                if not created_at:
                    continue
                created = parse_x_datetime(created_at)
                if created < end:
                    newest_seen_tweet_id = tweet.get("id")
                    newest_seen_created_at = created.isoformat()
                    break

        pages_fetched += 1
        api_posts_seen += len(page_data)
        page_posts, oldest, hit_boundary = normalize_page(page, start, end, stop_at_tweet_id=stop_at_tweet_id)
        for post in page_posts:
            if post["id"] not in seen_ids:
                seen_ids.add(post["id"])
                posts.append(post)

        if hit_boundary:
            stop_reason = "reached_last_seen_tweet_id"
            break

        next_token = page.get("meta", {}).get("next_token")
        if not next_token:
            stop_reason = "no_more_pages"
            break
        if oldest is not None and oldest < start:
            stop_reason = "reached_window_start"
            break
        pagination_token = next_token

    posts.sort(key=lambda item: item["created_at"], reverse=True)
    return {
        "window_start": start.isoformat(),
        "window_end": end.isoformat(),
        "source": {
            "type": "x_list_api",
            "list_id": list_id,
            "pages_fetched": pages_fetched,
            "api_posts_seen": api_posts_seen,
            "stop_reason": stop_reason,
            "newest_seen_tweet_id": newest_seen_tweet_id,
            "newest_seen_created_at": newest_seen_created_at,
            "last_seen_tweet_id_before_run": state_last_seen_tweet_id,
            "incremental_boundary_applied": stop_at_tweet_id is not None,
            "boundary_ignored_reason": boundary_ignored_reason,
        },
        "posts": posts,
    }


def build_next_state(previous_state: Dict[str, object], result: dict) -> Dict[str, object]:
    source = result.get("source", {})
    next_state = dict(previous_state)
    next_state["list_id"] = source.get("list_id")
    next_state["last_success_window_start"] = result.get("window_start")
    next_state["last_success_window_end"] = result.get("window_end")
    next_state["updated_at"] = datetime.now(timezone.utc).isoformat()
    if source.get("newest_seen_tweet_id"):
        next_state["last_seen_tweet_id"] = source["newest_seen_tweet_id"]
    if source.get("newest_seen_created_at"):
        next_state["last_seen_created_at"] = source["newest_seen_created_at"]
    return next_state


def main():
    args = parse_args()
    start = parse_iso(args.window_start)
    end = parse_iso(args.window_end)
    env = load_env_file(Path(args.env_file))
    state_path = Path(args.state_file)
    state = load_state_file(state_path)
    bearer_token = env.get("X_BEARER_TOKEN")
    list_id = env.get("X_LIST_ID")
    if not bearer_token:
        raise RuntimeError("missing X_BEARER_TOKEN in env file")
    if not list_id:
        raise RuntimeError("missing X_LIST_ID in env file")

    result = fetch_window(list_id, bearer_token, start, end, args.max_results, state=state)
    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    save_state_file(state_path, build_next_state(state, result))


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        print(str(exc), file=sys.stderr)
        sys.exit(1)
