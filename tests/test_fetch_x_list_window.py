import unittest
from datetime import datetime, timezone
from pathlib import Path
import importlib.util
from types import SimpleNamespace
from unittest import mock


def load_module():
    path = Path(__file__).resolve().parents[1] / "work" / "fetch_x_list_window.py"
    spec = importlib.util.spec_from_file_location("fetch_x_list_window", path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


class FetchXListWindowTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.mod = load_module()

    def test_load_env_file_reads_expected_keys(self):
        env_path = Path("/tmp/test_x_list_env.env")
        env_path.write_text(
            "X_BEARER_TOKEN=test-token\nX_LIST_ID=12345\n# comment\n",
            encoding="utf-8",
        )
        try:
            env = self.mod.load_env_file(env_path)
        finally:
            env_path.unlink(missing_ok=True)
        self.assertEqual(env["X_BEARER_TOKEN"], "test-token")
        self.assertEqual(env["X_LIST_ID"], "12345")

    def test_load_env_file_strips_wrapping_quotes(self):
        env_path = Path("/tmp/test_x_list_env_quoted.env")
        env_path.write_text(
            'X_BEARER_TOKEN="quoted-token"\nX_LIST_ID=\'2068180761916977611\'\n',
            encoding="utf-8",
        )
        try:
            env = self.mod.load_env_file(env_path)
        finally:
            env_path.unlink(missing_ok=True)
        self.assertEqual(env["X_BEARER_TOKEN"], "quoted-token")
        self.assertEqual(env["X_LIST_ID"], "2068180761916977611")

    def test_load_state_file_returns_empty_when_missing(self):
        state = self.mod.load_state_file(Path("/tmp/does-not-exist-x-list-state.json"))
        self.assertEqual(state, {})

    def test_save_and_load_state_file_round_trip(self):
        state_path = Path("/tmp/test_x_list_state.json")
        payload = {
            "list_id": "2068180761916977611",
            "last_seen_tweet_id": "200",
            "last_seen_created_at": "2026-06-24T02:26:17+00:00",
        }
        try:
            self.mod.save_state_file(state_path, payload)
            loaded = self.mod.load_state_file(state_path)
        finally:
            state_path.unlink(missing_ok=True)
        self.assertEqual(loaded, payload)

    def test_normalize_page_extracts_posts_authors_and_media(self):
        page = {
            "data": [
                {
                    "id": "1",
                    "text": "hello world",
                    "author_id": "u1",
                    "created_at": "2026-06-24T02:26:17.000Z",
                    "public_metrics": {
                        "like_count": 5,
                        "reply_count": 1,
                        "retweet_count": 2,
                        "quote_count": 0,
                    },
                    "attachments": {"media_keys": ["m1"]},
                }
            ],
            "includes": {
                "users": [
                    {
                        "id": "u1",
                        "name": "Noah Zweben",
                        "username": "noahzweben",
                        "verified": False,
                    }
                ],
                "media": [
                    {
                        "media_key": "m1",
                        "type": "photo",
                        "url": "https://example.com/image.jpg",
                        "alt_text": "diagram",
                    }
                ],
            },
            "meta": {"result_count": 1},
        }
        start = datetime(2026, 6, 22, 2, 0, 0, tzinfo=timezone.utc)
        end = datetime(2026, 6, 29, 2, 0, 0, tzinfo=timezone.utc)
        posts, oldest, hit_boundary = self.mod.normalize_page(page, start, end)
        self.assertEqual(len(posts), 1)
        post = posts[0]
        self.assertEqual(post["id"], "1")
        self.assertEqual(post["author"]["username"], "noahzweben")
        self.assertEqual(post["permalink"], "https://x.com/noahzweben/status/1")
        self.assertEqual(post["media"][0]["type"], "photo")
        self.assertEqual(oldest.isoformat(), "2026-06-24T02:26:17+00:00")
        self.assertFalse(hit_boundary)

    def test_normalize_page_filters_out_of_window_posts(self):
        page = {
            "data": [
                {
                    "id": "1",
                    "text": "old post",
                    "author_id": "u1",
                    "created_at": "2026-06-20T02:26:17.000Z",
                }
            ],
            "includes": {"users": [{"id": "u1", "name": "Test", "username": "test"}]},
            "meta": {"result_count": 1},
        }
        start = datetime(2026, 6, 22, 2, 0, 0, tzinfo=timezone.utc)
        end = datetime(2026, 6, 29, 2, 0, 0, tzinfo=timezone.utc)
        posts, oldest, hit_boundary = self.mod.normalize_page(page, start, end)
        self.assertEqual(posts, [])
        self.assertEqual(oldest.isoformat(), "2026-06-20T02:26:17+00:00")
        self.assertFalse(hit_boundary)

    def test_normalize_page_stops_at_last_seen_tweet_id(self):
        page = {
            "data": [
                {
                    "id": "3",
                    "text": "new post",
                    "author_id": "u1",
                    "created_at": "2026-06-24T02:26:17.000Z",
                },
                {
                    "id": "2",
                    "text": "already seen",
                    "author_id": "u1",
                    "created_at": "2026-06-23T02:26:17.000Z",
                },
                {
                    "id": "1",
                    "text": "older post",
                    "author_id": "u1",
                    "created_at": "2026-06-22T02:26:17.000Z",
                },
            ],
            "includes": {"users": [{"id": "u1", "name": "Test", "username": "test"}]},
            "meta": {"result_count": 3},
        }
        start = datetime(2026, 6, 22, 0, 0, 0, tzinfo=timezone.utc)
        end = datetime(2026, 6, 29, 0, 0, 0, tzinfo=timezone.utc)
        posts, oldest, hit_boundary = self.mod.normalize_page(
            page,
            start,
            end,
            stop_at_tweet_id="2",
        )
        self.assertEqual([post["id"] for post in posts], ["3"])
        self.assertEqual(oldest.isoformat(), "2026-06-24T02:26:17+00:00")
        self.assertTrue(hit_boundary)

    def test_run_curl_json_parses_trailing_http_status(self):
        proc = SimpleNamespace(
            stdout='{"title":"Unsupported Authentication","detail":"client app is not configured with the appropriate oauth1 app permissions"}\n403',
            stderr="",
            returncode=0,
        )
        with mock.patch.object(self.mod.subprocess, "run", return_value=proc):
            status, data = self.mod.run_curl_json("https://api.x.com/test", "token")
        self.assertEqual(status, 403)
        self.assertEqual(data["title"], "Unsupported Authentication")

    def test_fetch_page_with_retries_recovers_after_transient_errors(self):
        responses = iter(
            [
                (0, {"raw": ""}),
                (503, {"title": "Service Unavailable"}),
                (200, {"data": [], "meta": {"result_count": 0}}),
            ]
        )

        def fake_run_curl_json(url, bearer_token):
            return next(responses)

        with mock.patch.object(self.mod, "run_curl_json", side_effect=fake_run_curl_json):
            with mock.patch.object(self.mod.time, "sleep") as sleep_mock:
                status, data = self.mod.fetch_page_with_retries("https://api.x.com/test", "token")

        self.assertEqual(status, 200)
        self.assertEqual(data["meta"]["result_count"], 0)
        self.assertEqual(sleep_mock.call_count, 2)

    def test_fetch_page_with_retries_returns_last_error_when_budget_exhausted(self):
        responses = iter(
            [
                (503, {"title": "Service Unavailable"}),
                (503, {"title": "Service Unavailable"}),
                (503, {"title": "Service Unavailable"}),
                (503, {"title": "Service Unavailable"}),
            ]
        )

        def fake_run_curl_json(url, bearer_token):
            return next(responses)

        with mock.patch.object(self.mod, "run_curl_json", side_effect=fake_run_curl_json):
            with mock.patch.object(self.mod.time, "sleep") as sleep_mock:
                status, data = self.mod.fetch_page_with_retries("https://api.x.com/test", "token")

        self.assertEqual(status, 503)
        self.assertEqual(data["title"], "Service Unavailable")
        self.assertEqual(sleep_mock.call_count, 3)

    def test_fetch_window_collects_posts_for_list(self):
        start = datetime(2026, 6, 22, 2, 0, 0, tzinfo=timezone.utc)
        end = datetime(2026, 6, 29, 2, 0, 0, tzinfo=timezone.utc)
        responses = iter(
            [
                (
                    200,
                    {
                        "data": [
                            {
                                "id": "t1",
                                "text": "alice update",
                                "author_id": "u1",
                                "created_at": "2026-06-24T02:26:17.000Z",
                            }
                        ],
                        "includes": {
                            "users": [
                                {
                                    "id": "u1",
                                    "name": "Alice",
                                    "username": "alice",
                                    "verified": False,
                                }
                            ]
                        },
                        "meta": {"result_count": 1},
                    },
                ),
            ]
        )

        def fake_run_curl_json(url, bearer_token):
            return next(responses)

        with mock.patch.object(self.mod, "run_curl_json", side_effect=fake_run_curl_json):
            result = self.mod.fetch_window(
                "2068180761916977611",
                "token",
                start,
                end,
                max_results=100,
                state={},
            )

        self.assertEqual(result["source"]["type"], "x_list_api")
        self.assertEqual(result["source"]["list_id"], "2068180761916977611")
        self.assertEqual(len(result["posts"]), 1)
        self.assertEqual(result["posts"][0]["author"]["username"], "alice")
        self.assertEqual(result["source"]["newest_seen_tweet_id"], "t1")
        self.assertEqual(result["source"]["stop_reason"], "no_more_pages")

    def test_fetch_window_stops_when_last_seen_tweet_id_is_encountered(self):
        start = datetime(2026, 6, 22, 0, 0, 0, tzinfo=timezone.utc)
        end = datetime(2026, 6, 29, 0, 0, 0, tzinfo=timezone.utc)
        responses = iter(
            [
                (
                    200,
                    {
                        "data": [
                            {
                                "id": "t3",
                                "text": "new post",
                                "author_id": "u1",
                                "created_at": "2026-06-24T02:26:17.000Z",
                            },
                            {
                                "id": "t2",
                                "text": "seen post",
                                "author_id": "u1",
                                "created_at": "2026-06-23T02:26:17.000Z",
                            },
                        ],
                        "includes": {
                            "users": [
                                {
                                    "id": "u1",
                                    "name": "Alice",
                                    "username": "alice",
                                    "verified": False,
                                }
                            ]
                        },
                        "meta": {"result_count": 2, "next_token": "next"},
                    },
                )
            ]
        )

        def fake_run_curl_json(url, bearer_token):
            return next(responses)

        with mock.patch.object(self.mod, "run_curl_json", side_effect=fake_run_curl_json):
            result = self.mod.fetch_window(
                "2068180761916977611",
                "token",
                start,
                end,
                max_results=100,
                state={"last_seen_tweet_id": "t2"},
            )

        self.assertEqual([post["id"] for post in result["posts"]], ["t3"])
        self.assertEqual(result["source"]["stop_reason"], "reached_last_seen_tweet_id")


if __name__ == "__main__":
    unittest.main()
