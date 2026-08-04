# 全球与国内 AI 情报周报自动化提示词

Automation: Global & China AI Intelligence Weekly PDF

生成一份新的中文 PDF 周报，覆盖全球与国内最新 AI 进展。统计窗口按 Asia/Shanghai 计算，为触发时刻向前回溯 7 天，窗口为左闭右开；文件名日期使用窗口结束日 `YYYY-MM-DD`。

## 采集

1. 读取 `work/ai_weekly_sources.json`，优先覆盖其中列出的官方一手源。围绕模型与研究、Agent 与开发工具、芯片与算力、应用落地、开源生态、政策治理、资本与组织变动七类主题，分别检索全球和国内信息。
2. 继续把 X List `2068180761916977611` 作为实时信号源。运行：
   `python3 work/fetch_x_list_window.py --window-start <iso> --window-end <iso> --env-file .env --state-file work/x_list_state.json --max-results 20 --output tmp/weekly-YYYY-MM-DD-x.json`
3. X 抓取必须使用官方 `GET /2/lists/{id}/tweets` List Posts 接口，并利用 `work/x_list_state.json` 的已见 tweet 边界增量抓取，单页最多 20 条。
4. X 并非唯一来源。必须同时搜索官方博客、产品公告、研究论文或技术报告、开发者文档、芯片厂商公告、政府与监管机构网站；可信媒体只用于发现线索、补充影响和交叉验证。
5. 只纳入发布时间或事件发生时间落在统计窗口内的内容。每条候选信息必须核对发布日期、原始链接、主体和核心事实。高影响或争议信息尽量由一个一手源和一个独立来源交叉验证；无法证实的传闻不纳入。
6. X API 单点失败时继续完成其他来源采集，在“采集说明”中注明缺口。只有当全球和国内两部分都无法获得足够的可核实来源时才终止，不生成空白或沿用旧内容的 PDF。

## 筛选与去重

1. 以“事件”而不是“帖子或文章”为单位去重。同一发布被官网、X 和媒体重复报道时合并成一个条目，链接优先指向官网或论文原文。
2. 优先级依次为：影响面大且已发布的产品或模型、关键能力或成本变化、Agent 和应用的实质性落地、芯片与算力供给变化、重要开源项目、正式政策与治理文件、可信的资本和组织信号。
3. 降低营销稿、无新增事实的转发、简单观点、预告但未发布、重复融资报道和低质量榜单的权重。
4. 每个地区通常保留 5 至 8 条高信号事件；信息密集周可增加，但全文保持简洁。不要为了凑数降低标准。

## 中文周报结构

生成 `outputs/weekly-markdown/global-china-ai-weekly-YYYY-MM-DD.md`，必须使用简洁中文总结，不堆砌英文原文。Markdown 原稿与 PDF 一同永久保留。固定结构：

1. `# 全球与国内 AI 情报周报（YYYY-MM-DD）`
2. `## 统计窗口`：明确起止时间和时区。
3. `## 30 秒总览`：最多 5 个要点，每点一句话，直接写本周最重要的变化。
4. `## 全球动态`：按重要性排序。每条使用三级标题，正文只写“发生了什么”和“为什么重要”，通常各一句；标注主题类别。
5. `## 国内动态`：格式同上，单独成章，不把中国公司海外发布归入全球章节。
6. `## 趋势与影响`：最多 3 条，提炼跨事件趋势及其对开发者、企业或产业链的影响，清楚区分事实与判断。
7. `## 下周观察`：最多 3 条，只列有明确依据的待观察事项。
8. `## 来源索引`：按全球、国内分组，列出条目标题、来源名、发布日期和可访问的原始链接；二手来源需明确标注。
9. `## 采集说明`：列出数据缺口、失败源、去重前候选数、最终事件数，以及 X API 的页数和帖子数。

## 输出与验收

1. 使用以下命令生成 PDF：
   `/Users/bytedance/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3 work/render_weekly_digest_pdf.py --input outputs/weekly-markdown/global-china-ai-weekly-YYYY-MM-DD.md --output outputs/weekly-pdf/global-china-ai-weekly-YYYY-MM-DD.pdf`
2. 用 `/Users/bytedance/.cache/codex-runtimes/codex-primary-runtime/dependencies/bin/override/pdfinfo` 验证 PDF 可读取；再用 `/Users/bytedance/.cache/codex-runtimes/codex-primary-runtime/dependencies/bin/override/pdftoppm` 渲染全部页面并检查标题、分页、中文字符、链接文本和页尾没有裁切或重叠。
3. 不再清理历史周报；`outputs/weekly-pdf/` 和 `outputs/weekly-markdown/` 中的所有历史版本必须永久保留。
4. PDF 验收成功后运行：
   `python3 work/publish_weekly_report.py --date YYYY-MM-DD --pdf outputs/weekly-pdf/global-china-ai-weekly-YYYY-MM-DD.pdf --markdown outputs/weekly-markdown/global-china-ai-weekly-YYYY-MM-DD.md --state-file work/x_list_state.json`
   该命令必须成功提交并推送到 GitHub `origin/main`。禁止暂存或提交 `.env`、Bearer Token、临时抓取 JSON、渲染中间文件或其他凭据。若推送失败，保留本地 PDF 和 commit，并在最终回复中明确失败原因，不能声称发布成功。
5. 最终回复说明新 PDF 路径、统计窗口、全球/国内事件数、主要数据缺口、PDF 验收结果，以及 Git commit SHA 和 push 结果。不要把正文重复贴到回复中。
