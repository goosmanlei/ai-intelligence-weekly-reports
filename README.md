# 全球与国内 AI 情报周报

本项目每周生成一份中文 AI 情报周报，分别覆盖全球与国内的模型与研究、Agent 与开发工具、芯片与算力、应用落地、开源生态、政策治理、资本与组织变动，并将 Markdown、PDF 和采集游标持久化到 GitHub。

本项目根目录是长期任务唯一的 Source of Truth。Codex Thread 只是可替换的执行窗口，不得依赖旧 Thread 或旧工作目录恢复任务。

## 新 Thread 启动顺序

进入项目根目录后，依次读取：

1. `README.md`：项目入口和恢复方式。
2. `AGENTS.md`：长期稳定规则和验收标准。
3. `STATE.md`：当前配置、最近进展和下一步。
4. `docs/automation/ai-frontiers-weekly-prompt.md`：每周自动化的完整执行流程。
5. `work/ai_weekly_sources.json` 与 `work/x_list_state.json`：信息源策略和 X 增量边界。

随后执行：

```bash
pwd
git status --short
git pull --ff-only
test -s .env
python3 -m unittest discover -s tests -p 'test_*.py'
```

`.env` 只应检查存在性，不得打印内容。若工作区存在不明改动，先判断归属，不得覆盖或回滚。

## 长期目标

- 每周一 11:00（Asia/Shanghai）生成过去 7 天的全球与国内 AI 中文周报。
- 优先使用官方一手源，以 X List 作为补充实时信号，而非唯一来源。
- 以事件为单位筛选、交叉验证和去重，突出少量高影响变化。
- 永久保留每期 Markdown 和 PDF，并在验收后提交、推送到 GitHub `origin/main`。
- 让任意新 Codex Thread 仅依赖项目文件即可继续运行和维护任务。

## 目录结构

- `AGENTS.md`：长期稳定规则。
- `STATE.md`：可变的当前项目状态。
- `docs/automation/`：自动化执行 Prompt。
- `work/ai_weekly_sources.json`：官方源和可信二手源清单。
- `work/x_list_state.json`：X List 已见帖子的增量边界。
- `work/fetch_x_list_window.py`：官方 X List Posts API 采集器。
- `work/render_weekly_digest_pdf.py`：PDF 渲染器。
- `work/publish_weekly_report.py`：受控 Git 提交与推送脚本。
- `outputs/weekly-markdown/`：所有历史 Markdown 周报，永久保留。
- `outputs/weekly-pdf/`：所有历史 PDF 周报，永久保留。
- `tests/`：采集、渲染和发布测试。
- `tmp/`：可删除的本次运行中间产物，禁止提交。

## 恢复当前工作

`STATE.md` 记录当前自动化、最近成功周期和待处理事项；`work/x_list_state.json` 记录 X API 增量游标。两者用途不同，均不得用聊天记忆替代。

每周运行的具体命令、报告结构、筛选标准和 PDF 验收要求，以 `docs/automation/ai-frontiers-weekly-prompt.md` 为准。稳定规则变化时同步更新 `AGENTS.md` 和自动化 Prompt；运行状态变化时替换更新 `STATE.md`，不要追加历史流水账。

## 明确不继承

新 Thread 不需要读取或继承旧聊天记录、旧工作目录、RSS/Nginx 服务、单账号抓取方案、手工 status 页面、临时 JSON、PDF 渲染图片、缓存、调试日志和已完成 Case 的讨论过程。历史周报本身保留，旧过程材料不进入长期上下文。
