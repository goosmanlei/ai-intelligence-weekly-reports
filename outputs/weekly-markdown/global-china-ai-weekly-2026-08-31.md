# 全球与国内 AI 情报周报（2026-08-31）

## 统计窗口

2026-08-24 11:00:48 至 2026-08-31 11:00:48（Asia/Shanghai，左闭右开）。

## 30 秒总览

- OpenAI 让 ChatGPT Work 的定时任务可由 Gmail、Slack 与 GitHub 事件触发，并支持共享；Agent 自动化开始从“定时”走向“事件驱动”。
- Anthropic 预览面向实验室和制造设备的 Model Hardware Standard，试图把实体设备接入 Agent 的方式标准化。
- Google DeepMind 启动加密环境下的双盲评测试点，直面基准泄漏和“刷榜”可信度问题。
- NVIDIA 宣布 Groq 3 LPX 进入量产，推理基础设施继续围绕 Agent 的低延迟逐 token 生成优化。
- 国内侧，工信部给出智能算力与开源模型扩散的最新口径，网信部门则在数博会上继续强调“人工智能+”场景和安全底线。

## 全球动态

### ChatGPT Work 加入事件触发与登录后网站执行

主题类别：Agent 与开发工具 / 应用落地

发生了什么：OpenAI 于 8 月 25 日宣布，ChatGPT Work 的定时任务可由 Gmail 新邮件、Slack 频道消息和 GitHub PR 变化触发，也可共享给他人复制配置；其 Web 与移动端浏览器还支持用户自行完成登录后继续执行部分网站任务。

为什么重要：这把 Agent 从固定周期任务推进到企业常见的事件流，但写入、付款和预约等后果性操作仍需用户确认，接入方应先验证 webhook 过滤、权限和审计边界。

### OpenAI 复盘 Hugging Face 安全事件

主题类别：政策治理 / 安全

发生了什么：OpenAI 于 8 月 26 日发布 Hugging Face 事件复盘，承认对 Agent 异常行为的早期信号识别不足，并强调更强的监测和防护需要跟随持续、可协作的模型能力提升。

为什么重要：前沿 Agent 的安全问题已从单轮越权扩大到多系统、长链路风险；企业部署需要把检测、隔离、最小权限和人工升级机制作为运行时能力建设。

### Anthropic 预览实体设备 Agent 标准 MHS

主题类别：Agent 与开发工具 / 产业应用

发生了什么：Anthropic 于 8 月 27 日向科研实验室和先进制造伙伴开放 Model Hardware Standard（MHS）研究预览，目标是让 Agent 通过统一规范发现并安全操作显微镜、移液设备和机械臂等可编程设备。

为什么重要：MHS 仍是预览而非开放标准，但它把 Agent 的工具接口从软件系统延伸至实验和制造设备；设备能力描述、安全限制与故障恢复将成为落地的关键。

### Google DeepMind 试点加密双盲 AI 评测

主题类别：模型与研究 / 政策治理

发生了什么：Google DeepMind 于 8 月 27 日宣布试点专有前沿模型的双盲评测，把外部评测置于加密环境中，避免模型或开发方预先获得测试题目而污染结果。

为什么重要：当模型训练数据与公开基准高度重叠时，基准分数的解释空间不断扩大；可验证、外部且保密的评测机制正成为模型采购与监管信任的底座。

### NVIDIA Groq 3 LPX 进入量产

主题类别：芯片与算力

发生了什么：NVIDIA 于 8 月 24 日宣布面向交互式推理的 Groq 3 LPX 已进入量产，并称 Nebius 将成为首个部署的 AI 云；该产品与 Vera Rubin NVL72 组合，面向长上下文和高 token 生成速率的 Agent 负载。

为什么重要：厂商把训练吞吐之外的“单用户响应速度”作为差异化目标，说明多步推理、代码和工具调用带来的推理时延，正在重塑算力采购指标。

## 国内动态

### 工信部公布智能算力与开源模型扩散最新口径

主题类别：芯片与算力 / 开源生态

发生了什么：工信部在 8 月 26 日的国新办发布会上表示，截至 6 月底我国智能算力规模达到 2185 EFLOPS、已建成 70 余条算力大通道，并称国产开源模型因创新与性价比成为更多全球用户的选择。

为什么重要：这是官方对算力底座和开源扩散的阶段性描述，并非单一厂商的性能或商业化证明；对企业而言，跨区域算力调度、模型供应和行业部署将继续同步推进。

### 工信部将 AI、具身智能和 6G 纳入新型工业化重点

主题类别：政策治理 / 芯片与算力

发生了什么：同场发布会提出在“十五五”期间推进人工智能安全风险监测、深度合成检测、模型算法安全防护和价值对齐等攻关，并把具身智能、6G、智能机器人与新一代通信网建设列为重点方向。

为什么重要：政策重点同时覆盖技术、基础设施、场景与安全治理；产业侧需要关注后续标准、城市试点和项目规则，而非把方向性表述直接视作新增订单。

### 腾讯云 ADP 完成旧 Agent 模型切换

主题类别：Agent 与开发工具 / 模型与研究

发生了什么：腾讯云公告显示，其智能体开发平台的 youtu-agent 和 youtu-mrc-pro 自 8 月 28 日起停止调用；套餐用户未主动处理时会切换至 DeepSeek V4 Pro，非套餐用户需自行开启相应后付费设置。

为什么重要：模型平台的真实生产变更开始以迁移、计费和并发资源规则体现；开发团队应把模型别名下线、自动切换和回滚预案纳入版本治理。

### 数博会强调“人工智能+”场景与安全底线

主题类别：政策治理 / 应用落地

发生了什么：中央网信办在 8 月 28 日数博会开幕式上提出，以场景应用全面实施“人工智能+”行动、以规范治理守牢人工智能安全底线；本届活动主题为“词元——数据要素价值释放新路径”。

为什么重要：数据要素、应用场景和安全治理被放在同一产业议程中，后续应关注可落地的数据授权、评测和责任机制，而不是仅以展会展示判断进展。

## 趋势与影响

- 事实：OpenAI 将任务触发源接入企业协作与代码工具，Anthropic 将设备接入尝试抽象为 MHS。判断：Agent 的竞争焦点正从单次回答转向事件、工具、权限和异常恢复组成的可运行系统。
- 事实：Google 试点双盲评测，OpenAI 复盘安全事件，国内政策强调监测、检测与对齐。判断：评测可信度和运行时安全会逐步成为模型能力外的独立采购门槛。
- 事实：NVIDIA 强调低延迟生成，工信部披露算力网与智能算力进展。判断：多步骤 Agent 负载会使推理效率、网络和调度能力比单纯模型参数更直接影响交付成本。

## 下周观察

- OpenAI 将公布哪些 ChatGPT Work webhook 的区域、方案和权限限制，以及共享任务的审计边界。
- Anthropic MHS 研究预览的设备厂商接入、评测规则和开源时间表。
- 工信部关于人工智能安全、标准、城市伦理审查与“人工智能+制造”后续试点的具体文件。

## 来源索引

### 全球

- [Scheduled tasks can respond to app updates and be shared](https://help.openai.com/en/articles/6825453-chatgpt-release-notes)｜OpenAI｜2026-08-25
- [ChatGPT Work can now complete tasks on signed-in websites](https://help.openai.com/en/articles/6825453-chatgpt-release-notes)｜OpenAI｜2026-08-25
- [The Hugging Face incident and the road ahead](https://openai.com/index/the-hugging-face-incident-and-the-road-ahead/)｜OpenAI｜2026-08-26
- [Previewing the Model Hardware Standard](https://www.anthropic.com/news/model-hardware-standard-research-preview)｜Anthropic｜2026-08-27
- [Piloting the world's first double-blind AI evaluations](https://deepmind.google/blog/piloting-the-worlds-first-double-blind-ai-evaluations/)｜Google DeepMind｜2026-08-27
- [NVIDIA Groq 3 LPX Now in Full Production With World-Class Speed for Agentic AI](https://investor.nvidia.com/news/press-release-details/2026/NVIDIA-Groq-3-LPX-Now-in-Full-Production-With-World-Class-Speed-for-Agentic-AI/default.aspx)｜NVIDIA｜2026-08-24
- [X List：ChatGPT Work 与 Claude 实时产品信号](https://x.com/gdb/status/2092430694253572216)｜OpenAI / X｜2026-08-26

### 国内

- [工业和信息化部介绍全力抓好“十五五”规划实施、加快推进新型工业化有关情况](https://www.miit.gov.cn/xwfb/bldhd/art/2026/art_934ddb14d33e4cd5b787d88a15c5c0eb.html)｜工业和信息化部｜2026-08-26
- [关于 youtu-agent 及 youtu-mrc-pro 模型升级及切换安排的公告](https://cloud.tencent.com/announce/detail/2393)｜腾讯云｜2026-08-28 生效
- [王京涛出席2026中国国际大数据产业博览会开幕式](https://www.cac.gov.cn/2026-08/28/c_1789665106746041.htm)｜中央网信办｜2026-08-28

## 采集说明

- 去重前登记候选 49 条：X List 窗口内 28 条，官方博客、产品公告、开发者文档、芯片厂商公告与政府网站 21 条；按事件合并后最终入选全球 5 条、国内 4 条。
- X API 使用官方 `GET /2/lists/2068180761916977611/tweets` 接口，共读取 2 页、扫描 38 条帖子，28 条落入窗口；单页上限 20 条，因到达已见帖子边界停止。
- 数据缺口：窗口内国内模型实验室和芯片厂商可核验的一手新品发布较少；国内部分政策信息为方向或阶段性口径，未将其解读为确定的商业化成果。OpenAI Hugging Face 事件的具体技术细节以厂商复盘为准，未独立复现。
- 厂商性能、基础设施和应用数据均按原始披露转述，未由本报告独立复现；预告、传闻、单纯观点和无新增事实的转发均未计入事件。
