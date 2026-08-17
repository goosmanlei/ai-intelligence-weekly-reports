# 当前状态

## 项目阶段

生产运行中。项目已从长期 Pin 会话迁移为独立目录项目，后续 Thread 应只依赖本目录中的持久化文件。

## 当前配置

- 项目根目录：`~/codex-path/1003.例行/全球与国内 AI 情报周报`
- 自动化 ID：`ai-brief-models-produc-weekly-pdf`
- 自动化迁移状态：项目文件迁移完成；Codex UI 尚未把本目录注册为项目，因此现有自动化暂仍为绑定旧 Thread 的 heartbeat。注册项目后需将同一自动化 ID 更新为本地目录 cron，再解除旧 Thread 依赖。
- 计划：每周一 11:00，时区 Asia/Shanghai
- Git 远端：`git@github.com:goosmanlei/ai-intelligence-weekly-reports.git`
- 发布分支：`main`
- X List ID：`2068180761916977611`
- X API：官方 List Posts 接口，单页最多 20 条
- 凭据：项目根目录 `.env`，已被 `.gitignore` 排除
- X 增量游标：`work/x_list_state.json`
- 来源策略：`work/ai_weekly_sources.json`

## 最近成功周期

- 周报日期：2026-08-17
- 统计窗口：2026-08-10 11:02:50 至 2026-08-17 11:02:50（Asia/Shanghai，左闭右开）
- 最终事件：全球 5 条，国内 3 条
- X 采集：2 页、35 条 API 帖子、窗口内 34 条
- 报告提交：待本次发布脚本完成后写入
- PDF：已通过 `pdfinfo` 可读性验证及全部 4 页渲染视觉验收；标题、中文、分页、来源文本与页尾均无裁切或重叠

## 当前有效决策

- X 只承担实时信号补充；官方公开源是主要信息来源。
- 所有历史 Markdown 和 PDF 永久保留，不再只保留最近 10 份。
- 全球和国内分章，保持简洁、高信号、事件级去重。
- 每周成功运行后必须同步更新本文件中的“最近成功周期”和必要的当前配置，再与周报一起提交。

## 下一步

- 在 Codex UI 中将 `~/codex-path/1003.例行/全球与国内 AI 情报周报` 添加或打开为项目。
- 项目注册后，把自动化 `ai-brief-models-produc-weekly-pdf` 更新为该项目的独立本地 cron；使用 `docs/automation/ai-frontiers-weekly-prompt.md`，保持周一 11:00 和 ACTIVE。
- 下一计划运行：2026-08-24 11:00（Asia/Shanghai）。
- 运行前确认 Git 工作区干净、`.env` 存在、测试通过。
- 若自动化、来源、X List、运行时间或发布策略变化，替换更新本文件对应项。

## 新 Thread 接手检查

1. 确认当前目录与 README 中的固定项目根目录一致。
2. 读取 `AGENTS.md` 和自动化 Prompt，不从聊天历史补规则。
3. 检查 `git status --short`、远端和 `.env` 存在性。
4. 从本文件和 `work/x_list_state.json` 恢复当前进度。
