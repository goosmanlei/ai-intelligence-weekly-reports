# 全球与国内 AI 情报周报

本仓库保存每周一 11:00（Asia/Shanghai）生成的全球与国内 AI 中文周报，以及生成、验证和发布周报所需的脚本。

## 目录

- `outputs/weekly-pdf/`：历次 PDF 周报，永久保留。
- `outputs/weekly-markdown/`：PDF 对应的 Markdown 原稿。
- `work/`：信息采集、PDF 渲染和 GitHub 发布脚本。
- `docs/automation/`：Codex 自动化任务提示词。
- `tests/`：采集、清理和发布脚本测试。

## 自动发布

周报生成并通过 PDF 验收后，自动化运行：

```bash
python3 work/publish_weekly_report.py \
  --date YYYY-MM-DD \
  --pdf outputs/weekly-pdf/global-china-ai-weekly-YYYY-MM-DD.pdf \
  --markdown outputs/weekly-markdown/global-china-ai-weekly-YYYY-MM-DD.md \
  --state-file work/x_list_state.json
```

脚本只暂存指定的周报、Markdown 原稿和 X 增量游标，然后提交并推送到 `origin/main`。`.env` 和临时采集文件不会进入 Git。

## 本地配置

复制 `.env.example` 的变量到本地 `.env` 并填入 X API 凭据。不要提交 `.env`。
