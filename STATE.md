# 当前状态

## 项目阶段

生产运行中。项目已从长期 Pin 会话迁移为独立目录项目，后续 Thread 应只依赖本目录中的持久化文件。

## 当前配置

- 项目根目录：`/Users/bytedance/codex-path/1003.routine/WeeklyAIReport`
- 自动化 ID：`ai-brief-models-produc-weekly-pdf`
- 自动化迁移状态：自动化已更新为当前目录的独立本地 cron，不再依赖旧 Thread 或旧工作目录。
- 计划：每周一 11:00，时区 Asia/Shanghai
- Git 远端：`git@github.com:goosmanlei/ai-intelligence-weekly-reports.git`
- 发布分支：`main`
- X List ID：`2068180761916977611`
- X API：官方 List Posts 接口，单页最多 20 条
- 凭据：项目根目录 `.env`，已被 `.gitignore` 排除
- X 增量游标：`work/x_list_state.json`
- 来源策略：`work/ai_weekly_sources.json`
- PDF 渲染：矢量文字、嵌入中文字体、来源标题可点击；2026-09-14 周报已通过文字、嵌入字体、链接和全页渲染验收。

## 最近成功周期

- 周报日期：2026-09-14
- 统计窗口：2026-09-07 11:53:50 至 2026-09-14 11:53:50（Asia/Shanghai，左闭右开）
- 最终事件：全球 6 条，国内 3 条
- X 采集：3 页、56 条 API 帖子、窗口内 56 条
- 报告提交：`39d1afcc5dbe593371845cd99a688a39ef78bf01`（已推送）
- PDF：已通过 `pdfinfo` 可读性验证、`pypdf` 可搜索文字和链接注释核验及全部 3 页渲染视觉验收；中文字体已嵌入，标题、中文、分页、来源文本与页尾均无裁切或重叠

## 当前有效决策

- X 只承担实时信号补充；官方公开源是主要信息来源。
- 所有历史 Markdown 和 PDF 永久保留，不再只保留最近 10 份。
- 全球和国内分章，保持简洁、高信号、事件级去重。
- 每周成功运行后必须同步更新本文件中的“最近成功周期”和必要的当前配置，再与周报一起提交。

## 下一步

- 下一计划运行：2026-09-21 11:00（Asia/Shanghai）。
- 运行前确认 Git 工作区干净、`.env` 存在、测试通过。
- 若自动化、来源、X List、运行时间或发布策略变化，替换更新本文件对应项。

## 新 Thread 接手检查

1. 确认当前目录与 README 中的固定项目根目录一致。
2. 读取 `AGENTS.md` 和自动化 Prompt，不从聊天历史补规则。
3. 检查 `git status --short`、远端和 `.env` 存在性。
4. 从本文件和 `work/x_list_state.json` 恢复当前进度。
