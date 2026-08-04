# Anthropic / Claude Code X 周报预览（截至 2026-06-26 11:11）

统计窗口：2026-06-22 10:00 至 2026-06-26 11:11（Asia/Shanghai）

## 本周总览

- 截至本次预览时点，通过官方 X List API 共确认 50 条窗口内公开更新，主要集中在 6 月 23 日至 6 月 26 日。
- 这一窗口的绝对主线是 Claude Tag：Claude 以 Slack 团队成员形态进入协作流，具备主动性、多线程上下文、记忆、权限控制和工具接入能力。
- 从公开信号看，Anthropic 正在把 Claude 从“单人对话工具”推进到“团队协作中的常驻代理”，而且底层明显复用了 Claude Code 的能力栈。
- 当前列表 API 返回中最活跃的账号是 @noahzweben、@trq212、@bcherny，其次是 @_catwu。几位账号从产品、工程、工作流、社交传播四个角度同时发声，说明这次发布是一次有组织的集中外宣。

## 逐账号摘要

### Boris Cherny

- Boris 的整组长帖是这次窗口里技术含量最高的一批信号。他明确说 Claude Tag 底层就是 Claude Code，因此它不是简单的 Slack 机器人，而是“把 Claude Code 的能力搬进协作场景”。
- 公开说明里提到了几个很关键的工程点：每个线程都会启动独立实例；实例有自己的 sandbox；能克隆仓库、写代码、测试、编译；任务结束后环境销毁。这说明 Anthropic 这次强调的是可执行代理，而不只是会聊天的助手。
- 他还反复强调 proactive 行为、分 channel 的记忆与权限、以及多层安全控制。对理解 Anthropic 的产品方向很关键：他们在把“长期运行代理”做成团队基础设施，而不是一次性问答。

### Thariq

- Thariq 主要提供的是“怎么把 Claude Tag 真正用起来”的一线 best practices。整串帖子更像内部工作流外放。
- 他给出的建议包括：给每个 channel 的 Claude 写固定说明并当成记忆的一部分；为个人工作建专属频道；让 Claude 维护 pinned 状态信息；用表情标记线程状态；甚至让 Claude 去做排期等带执行属性的任务。
- 这些内容的价值不在于单个技巧，而在于说明 Anthropic 内部已经把 Claude 当成“持续驻场协作者”，而不是一次一问一答的命令式工具。

### Noah Zweben

- Noah 是这个窗口里发帖最密集的人，承担了明显的 PM / launch narrator 角色。
- 他的内容主要覆盖三层：一是产品正式发布与定位，二是具体配置与使用方式，三是大量来自 Slack、企业用户、投资人和媒体的外部反馈转发。
- 其中比较关键的新增用法是 “Ambient Claude / Claude Tag without the Tag”：不需要每次显式 @Claude，也可以通过自然语言告诉它在频道里持续做什么，比如自动 triage bug、看到需要 legal review 的事项就提醒法务，甚至自动响应其他机器人产生的告警。
- 这批内容说明 Claude Tag 的真正卖点不是“在 Slack 里叫一下 Claude”，而是“把代理常驻在团队工作现场”。

### Cat Wu

- Cat 从产品负责人视角给出了最直接的定位：Claude Tag 是 Anthropic 产品交付方式的 paradigm shift，内部版本已经参与合并 65% 的产品 PR，而且它是原生 multi-player、proactive 的产品形态。
- 她还补了两类很重要的材料：一类是 agent permissions 的入门配置指南，另一类是“6 个典型工作流”的产品化用例。
- 这些信号很明确地说明，这次发布并不是一个单点功能，而是围绕权限、场景模板、团队 adoption 一起打包推出的。

### Andrej Karpathy

- Karpathy 这次最有价值的一条不是功能细节，而是他的定性判断：这是一种更 inline、深度嵌入组织日常协作的新交互范式。
- 这个评价本身很重要，因为它把 Claude Tag 从“Slack 集成”拉高到“组织级工作接口变化”的层面。

### Alex Albert

- Alex 的公开表态很短，但代表性很强：它不再像是在使用一个工具，而更像是在管理一个团队。
- 这句话基本概括了 Anthropic 这次对外想建立的产品心智。

### Jack Clark

- 本窗口内 Jack 只有一条转发，内容是 Chad Jones 将加入 Anthropic Institute。
- 它不属于 Claude Tag 主线，但能看出 Anthropic Institute 相关布局仍在推进。

### Dario Amodei

- 本窗口未确认公开更新。

### Mike Krieger

- 本窗口未确认公开更新。

## 重点信号

- 本周最重要的产品主题不是 Claude Code 的单点命令更新，而是“Claude Code 能力向团队协作代理形态外溢”。
- 多位员工反复提到 65% 的产品 PR、sandbox、主动执行、记忆、channel 级行为配置，这说明 Anthropic 正在把 agent 从个人使用场景推进到组织流程层。
- Noah 与 Cat 的帖子强调配置、权限、典型工作流；Boris 与 Thariq 的帖子强调底层能力和真实用法。这种组合非常像一次完整的新产品叙事，而不是零散更新。
- 从当前窗口公开信号看，后续值得重点追的方向有三个：Slack 内代理工作流、channel 级长期记忆与行为配置、Claude Code/Claude Tag 的底层统一能力栈。

## 原帖链接索引

- @noahzweben：https://x.com/noahzweben/status/2070270332674658814
- @noahzweben：https://x.com/noahzweben/status/2070265825437855760
- @noahzweben：https://x.com/noahzweben/status/2069608016098566359
- @bcherny：https://x.com/bcherny/status/2069474681749754272
- @trq212：https://x.com/trq212/status/2069474335656694003
- @_catwu：https://x.com/_catwu/status/2069473118742331608
- @_catwu：https://x.com/_catwu/status/2069484330938998993
- @_catwu：https://x.com/_catwu/status/2069486403696869555
- @karpathy：https://x.com/karpathy/status/2069547676849557725
- @alexalbert__：https://x.com/alexalbert__/status/2069470389391241314
- @jackclarkSF：https://x.com/jackclarkSF/status/2069417162725573034

## 抓取备注

- 本文件是“当前进行中窗口预览”，不是周一 10:00 的最终周报版本。
- 本次预览使用官方 X API 的 `GET /2/lists/{id}/tweets` 接口，页大小已限制为 20。
- 本次抓取共读取 3 页，扫描 58 条列表帖子，确认 50 条落入当前窗口。
- 由于官方 List API 返回集合与网页展示集合不完全一致，当前预览仍以 API 返回为准。
