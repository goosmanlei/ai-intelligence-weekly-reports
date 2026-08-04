# X List API Weekly Digest Design

## Goal

Replace the current unreliable anonymous X scraping flow with an official X API based pipeline that reads a public X List and generates the same weekly Chinese PDF digest.

The target outcome is:

- read posts from the configured public X List via official API
- filter posts into the weekly time window
- generate a Chinese markdown summary
- render a dated PDF
- retain the latest 10 PDFs
- keep secrets only in local `.env`

## Scope

This change replaces only the data acquisition layer.

It does not redesign:

- the PDF rendering style
- the weekly schedule cadence
- the output directory layout

It does change:

- the fetch script
- the automation prompt
- the source-of-truth from account scraping to List timeline API

## Proposed Approach

### Recommended

Use `GET /2/lists/:id/tweets` as the primary source, with the Bearer token loaded from local `.env`.

Why this is the right choice:

- it is the official API for this exact List-based use case
- it avoids login walls and unstable anonymous timeline behavior
- it naturally matches the user's curated list, which is the actual source they want monitored

### Alternatives Considered

1. Keep improving anonymous scraping.

This was rejected because the root cause is not parser quality. X serves incomplete and inconsistent public data to anonymous clients, so reliability remains structurally poor.

2. Use a signed-in browser session.

This was rejected as the long-term solution because it depends on interactive local state, is harder to automate safely, and is more fragile than official API access.

## Architecture

### Inputs

- `.env`
  - `X_BEARER_TOKEN`
  - `X_LIST_ID`
- time window
  - `window_start`
  - `window_end`

### New Script

Add `work/fetch_x_list_window.py`.

Responsibilities:

- read `.env`
- call X List Tweets API
- handle pagination up to the posts needed for the requested window
- normalize author and media expansions
- filter posts by `created_at`
- emit stable JSON for downstream summarization

### Existing Scripts Kept

- `work/render_weekly_digest_pdf.py`
- `work/prune_weekly_pdfs.py`

These stay in place and continue to operate on markdown and PDF files.

## Output Contract

The new fetcher should output JSON shaped similarly to the current pipeline so downstream summary generation stays simple.

Recommended structure:

```json
{
  "window_start": "2026-06-22T10:00:00+08:00",
  "window_end": "2026-06-29T10:00:00+08:00",
  "source": {
    "type": "x_list_api",
    "list_id": "2068180761916977611"
  },
  "posts": [
    {
      "id": "123",
      "created_at": "2026-06-24T02:26:17+00:00",
      "text": "post text",
      "permalink": "https://x.com/user/status/123",
      "author": {
        "id": "456",
        "name": "Noah Zweben",
        "username": "noahzweben",
        "verified": false
      },
      "public_metrics": {
        "like_count": 0,
        "reply_count": 0,
        "retweet_count": 0,
        "quote_count": 0
      },
      "media": [
        {
          "type": "photo",
          "url": "https://..."
        }
      ]
    }
  ]
}
```

## Data Flow

1. automation computes weekly Monday-to-Monday time window
2. fetcher loads `.env`
3. fetcher calls List Tweets API with tweet, user, and media fields
4. fetcher paginates until posts are older than the requested window or no more pages exist
5. fetcher writes normalized JSON to `tmp/weekly-YYYY-MM-DD.json`
6. summarization step writes Chinese markdown to `tmp/weekly-YYYY-MM-DD.md`
7. PDF renderer converts markdown to `outputs/weekly-pdf/ai-frontiers-weekly-YYYY-MM-DD.pdf`
8. prune script keeps latest 10 PDFs

## Error Handling

The fetcher should fail loudly and specifically for these cases:

- missing `.env`
- missing `X_BEARER_TOKEN`
- missing `X_LIST_ID`
- `401 Unauthorized`
- `403 Forbidden`
- `404 List not found`
- malformed API response

Expected behavior:

- exit non-zero
- print a short actionable error
- never silently fall back to anonymous scraping

## Security

- do not print the token
- do not write the token into JSON, markdown, logs, or PDFs
- keep `.env` ignored by git
- keep `.env.example` as the only committed template

## Automation Changes

Update the existing weekly automation to:

- stop using `fetch_x_posts_window.py`
- run `fetch_x_list_window.py`
- summarize the returned posts into Chinese
- write PDFs using the broader AI digest naming convention
- keep the same retention policy

The automation should no longer mention manual status URL supplementation as its primary recovery path.

## Testing

### Verification Targets

- the new fetcher can authenticate successfully with valid `.env`
- the fetcher returns posts from the configured List
- posts are filtered correctly by the requested window
- generated JSON is valid and stable
- markdown still renders to PDF
- old PDF retention still works

### Minimal Verification Commands

```bash
python3 work/fetch_x_list_window.py --window-start '2026-06-22T10:00:00+08:00' --window-end '2026-06-29T10:00:00+08:00' --output tmp/weekly-2026-06-29.json
/Users/bytedance/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3 work/render_weekly_digest_pdf.py --input tmp/weekly-2026-06-29.md --output outputs/weekly-pdf/ai-frontiers-weekly-2026-06-29.pdf
python3 work/prune_weekly_pdfs.py --dir outputs/weekly-pdf --keep 10
```

## Constraints

- official API only
- public List timeline only
- no browser-session dependency
- no user-interactive weekly workflow

## Success Criteria

- weekly digest source is the configured X List
- the pipeline captures active posts that were previously missed by anonymous scraping
- the weekly PDF is still generated on schedule
- the system remains local, simple, and maintainable
