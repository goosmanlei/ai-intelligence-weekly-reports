# X List API Weekly Digest Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Replace anonymous X scraping with the official X List API so the weekly Monday 10:00 digest reliably summarizes the configured list into a Chinese PDF, with the digest positioned as a broader AI-frontiers weekly rather than an Anthropic-only report.

**Architecture:** Add a new fetcher that reads `X_BEARER_TOKEN` and `X_LIST_ID` from local `.env`, calls `GET /2/lists/:id/tweets` with expansions, paginates until the time window is covered, and emits normalized JSON. Keep the existing markdown-to-PDF and retention scripts, and update the weekly automation to use the new fetcher.

**Tech Stack:** Python 3, curl-based HTTP access, local `.env`, Codex cron automation, Pillow PDF renderer

---

### Task 1: Validate API Access

**Files:**
- Modify: `none`
- Verify: `.env`

- [ ] **Step 1: Verify required env keys exist**

Run:

```bash
python3 - <<'PY'
from pathlib import Path
p = Path('.env')
assert p.exists(), '.env missing'
keys = {
    line.split('=', 1)[0].strip()
    for line in p.read_text(encoding='utf-8').splitlines()
    if '=' in line and not line.strip().startswith('#')
}
assert 'X_BEARER_TOKEN' in keys, 'X_BEARER_TOKEN missing'
assert 'X_LIST_ID' in keys, 'X_LIST_ID missing'
print('env ok')
PY
```

- [ ] **Step 2: Verify List API authentication succeeds**

Run:

```bash
python3 - <<'PY'
from pathlib import Path
env = {}
for line in Path('.env').read_text(encoding='utf-8').splitlines():
    if '=' in line and not line.strip().startswith('#'):
        k, v = line.split('=', 1)
        env[k.strip()] = v.strip()
print(env['X_LIST_ID'])
PY
```

Then run:

```bash
set -a
. ./.env
set +a
curl -sS -o /tmp/x_list_probe.json -w '%{http_code}\n' \
  "https://api.x.com/2/lists/${X_LIST_ID}/tweets?max_results=5&tweet.fields=created_at,author_id,public_metrics&expansions=author_id&user.fields=username,name,verified" \
  -H "Authorization: Bearer $X_BEARER_TOKEN"
```

Expected: `200`

### Task 2: Add List Fetcher

**Files:**
- Create: `work/fetch_x_list_window.py`

- [ ] **Step 1: Write the fetcher**

Implement a Python script that:

- parses `--window-start`, `--window-end`, and `--output`
- loads `.env`
- calls `GET /2/lists/:id/tweets`
- requests `tweet.fields`, `user.fields`, `media.fields`, and `expansions`
- paginates with `next_token`
- stops when posts are older than the window
- writes normalized JSON

- [ ] **Step 2: Verify the fetcher on the current window**

Run:

```bash
python3 work/fetch_x_list_window.py \
  --window-start '2026-06-22T10:00:00+08:00' \
  --window-end '2026-06-29T10:00:00+08:00' \
  --output tmp/weekly-2026-06-29-api.json
```

Expected: JSON file exists and contains `posts`

### Task 3: Remove Old Anonymous Primary Source

**Files:**
- Modify: `work/fetch_x_posts_window.py` or leave unused
- Modify: `work/manual-status-urls.json` only if no longer needed

- [ ] **Step 1: Keep old script out of the automation path**

Do not delete immediately if not necessary, but ensure the automation no longer depends on it.

### Task 4: Regenerate Weekly Markdown and PDF

**Files:**
- Modify: `tmp/weekly-2026-06-22.md` only as regenerated output
- Reuse: `work/render_weekly_digest_pdf.py`
- Reuse: `work/prune_weekly_pdfs.py`

- [ ] **Step 1: Generate markdown summary from fetched JSON**

Write a concise Chinese markdown report with:

- title
- time window
- weekly overview
- top stories
- grouped summaries for labs, products, engineering signals, and policy / compute
- key signals
- source links

- [ ] **Step 2: Render PDF**

Run:

```bash
/Users/bytedance/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3 \
  work/render_weekly_digest_pdf.py \
  --input tmp/weekly-2026-06-29.md \
  --output outputs/weekly-pdf/ai-frontiers-weekly-2026-06-29.pdf
```

- [ ] **Step 3: Retain latest 10 PDFs**

Run:

```bash
python3 work/prune_weekly_pdfs.py --dir outputs/weekly-pdf --keep 10
```

### Task 5: Update Automation

**Files:**
- Modify: Codex automation `anthropic-claude-code-x-digest-feed`

- [ ] **Step 1: Switch the automation prompt to the List API fetcher**

Update the cron prompt so it:

- uses `work/fetch_x_list_window.py`
- reads `.env`
- writes JSON to `tmp/weekly-YYYY-MM-DD.json`
- writes Chinese markdown to `tmp/weekly-YYYY-MM-DD.md`
- renders PDF to `outputs/weekly-pdf/ai-frontiers-weekly-YYYY-MM-DD.pdf`
- prunes old PDFs
- summarizes the window as AI-frontiers news rather than fixed Anthropic-account coverage

### Task 6: Verification

**Files:**
- Verify: `tmp/weekly-2026-06-29-api.json`
- Verify: `outputs/weekly-pdf/ai-frontiers-weekly-2026-06-29.pdf`

- [ ] **Step 1: Validate fetched post count**

Run:

```bash
python3 - <<'PY'
import json
from pathlib import Path
data = json.loads(Path('tmp/weekly-2026-06-29-api.json').read_text(encoding='utf-8'))
print('posts', len(data.get('posts', [])))
PY
```

- [ ] **Step 2: Validate PDF exists**

Run:

```bash
/Users/bytedance/.cache/codex-runtimes/codex-primary-runtime/dependencies/bin/pdfinfo \
  outputs/weekly-pdf/ai-frontiers-weekly-2026-06-29.pdf
```

Expected: `Pages:` appears and exit code is `0`
