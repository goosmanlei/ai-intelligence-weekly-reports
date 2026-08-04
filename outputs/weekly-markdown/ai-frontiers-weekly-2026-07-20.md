# AI Frontiers Weekly（2026-07-20）

统计窗口：2026-07-13 11:00 至 2026-07-20 11:00（Asia/Shanghai）

## 本周总览

- 本窗口内共确认 10 条公开更新，量不大，但信号比较集中，主题主要是 Fable / Sol / Kimi 的模型比较、Claude Cowork 的个人工作流，以及数学与机器人方向的能力外溢。
- 内容密度最高的是 Ethan Mollick，他连续用同一批提示测试不同模型，强调模型质量波动并不线性，说明“某一代异常强、下一代回归均值”的情况仍会反复出现。
- Anthropic 侧最值得保留的是 Cat Wu 的一条实用工作流：直接用 Claude Cowork 做每周日程约束和冲突整理，说明产品定位已明显超出纯问答。

## Top Stories

- 模型比较继续从跑分转向“可感知产出”。Ethan Mollick 用同一首诗歌创作任务比较 Fable、Sol Pro、Kimi K3，判断这次是 Fable 胜出。
- 他同时指出，AI 模型并不会单调变强，历史上就存在某个版本异常优秀、后续版本回归平均的情况，这对企业选型和提示模板固化都是风险提示。
- Cat Wu 分享了自己使用 Claude Cowork 管理周历的完整提示约束，重点不在单条 prompt，而在把会议时长、冲突去重和历史习惯一起交给 agent 处理。

## Labs

- Yann LeCun 转发 latent actions 在机器人方向走热的讨论，反映出世界模型和行动抽象仍是 Meta 系阵营的重要研究主线。
- Garry Tan 级别的“数学突破近在眼前”式表达继续升温，说明外部观察者已经把 AI 在数学上的进展视为接近实际科学产出的拐点。

## Products

- Claude Cowork 的日程管理案例说明，Anthropic 产品线正在把 Claude 从回答器推向“个人工作代理”，尤其适合重复但有约束的办公室任务。
- Ethan Mollick 对 Fable 的连发比较也说明，模型选择正在越来越像具体产品选择，而不是抽象的“哪个实验室更强”。

## Engineering Signals

- 这周最有价值的工程信号，是把 prompt 从一次性指令改造成“带业务约束的工作说明书”。
- Cat Wu 的日历管理示例同时包含目标上限、冲突处理和历史回看，这类结构化约束比单句命令更接近真实 agent 工作流。

## Policy / Compute

- Dean Ball 转发有关中国 AI 路线的分析；Nat Lambert 也提到与中国实验室的高频接触其实早已常态化。两者合起来看，前沿模型竞争已经越来越离不开地缘与产业政策语境。

## 原帖链接索引

- @emollick：https://x.com/emollick/status/2077794752219150667
- @emollick：https://x.com/emollick/status/2077791147416039885
- @emollick：https://x.com/emollick/status/2077788766276104320
- @_catwu：https://x.com/_catwu/status/2077775308704874569
- @emollick：https://x.com/emollick/status/2077758652066842959
- @deanwball：https://x.com/deanwball/status/2077741984653248627
- @gdb：https://x.com/gdb/status/2077725337334947868
- @natolambert：https://x.com/natolambert/status/2077718570840326311
- @emollick：https://x.com/emollick/status/2077714619856251184
- @ylecun：https://x.com/ylecun/status/2077708045955647622

## 抓取备注

- 数据源：官方 X API `GET /2/lists/{id}/tweets`
- List ID：`2068180761916977611`
- 本次为历史补抓，未使用增量边界截断
- 共读取 41 页，扫描 786 条列表帖子，确认 10 条落入本统计窗口
- 停止原因为 `no_more_pages`，说明当前 API 时间线恰好在本窗口之前就已结束
