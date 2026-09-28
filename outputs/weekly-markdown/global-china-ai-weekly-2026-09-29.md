# 全球与国内 AI 情报周报（2026-09-29）

## 统计窗口

2026-09-22 03:28:25 至 2026-09-29 03:28:25（Asia/Shanghai，左闭右开）。

## 30 秒总览

- OpenAI 推出 GPT-6 Sol、Luna，Anthropic 接连推出 Claude Opus 5.5、Sonnet 5.5；本周前沿模型竞争明显转向不同任务档位的速度与单位任务成本。
- ChatGPT Voice 开始接入插件和工作任务，Google 则公布可跨设备保留上下文的隐私计算方案；持续工作的助手正同时触及工具权限与个人记忆边界。
- Anthropic 公布由 Claude 辅助发现、经实验室初步验证的新酶系统；这是科研 Agent 的早期实例，生物学功能仍未确定。
- 国内阿里发布从芯片、云到模型和手机 Agent 的一揽子方案；Qwen Code 与火山引擎则推进远程工作流、断点恢复和技能治理。
- 中美公布建立 AI 对话与事件沟通渠道，国家互联网应急中心发布智能体漏洞通报；治理焦点进一步落到跨境沟通和具体系统风险。

## 全球动态

### OpenAI 推出 GPT-6 Sol 和 Luna

主题类别：模型与研究 / Agent 与开发工具

发生了什么：OpenAI 于 9 月 22 日将 GPT-6 Sol 和 Luna 加入 ChatGPT Work、Codex 与 API，分别面向较复杂工作和更高频的低成本任务；官方开发者公告称，两者 API 价格较 GPT-5.6 同档促销价低约 50%。

为什么重要：开发者可以按任务难度分配模型，而非让全部工作使用同一高价档；价格比较来自厂商公告，实际单位任务成本仍取决于质量、重试率和推理用量。

### Anthropic 发布 Claude Opus 5.5

主题类别：模型与研究 / Agent 与开发工具

发生了什么：Anthropic 于 9 月 22 日发布 Opus 5.5，API 输入、输出分别定价每百万 token 4、20 美元，并称典型任务成本比 Opus 5 低约 40%、生成速度提升逾 30%；模型也接受外部机构发布前评测。

为什么重要：高能力模型的采购比较开始同时看模型表现、缓存和完成任务的总成本；速度、成本和基准表现仍主要是厂商测试结果，生产迁移需用自有任务复核。

### Anthropic 发布 Claude Sonnet 5.5

主题类别：模型与研究 / Agent 与开发工具

发生了什么：Anthropic 于 9 月 28 日发布 Sonnet 5.5，API 输入、输出分别定价每百万 token 2、10 美元；官方称其输出比 Sonnet 5 快逾 30%，并减少完成同类任务所需的 token。

为什么重要：同一家厂商在旗舰与常用任务档同时降本，企业更容易把代码修复、文档制作等日常工作放入较低成本模型；其任务成本和基准仍需按具体提示、工具链和工作负载验证。

### ChatGPT Voice 接入插件并进入 Work

主题类别：Agent 与开发工具 / 应用落地

发生了什么：OpenAI 9 月 23 日更新说明称，Voice 已可在网页、iOS 和 Android 对话中使用账户可用的插件及连接应用，并在 Work 中以语音发起文档、演示文稿、表格及浏览器任务；未完成的任务可在语音结束后转入文字继续。

为什么重要：语音从问答入口扩展为多工具任务入口，工作流可以跨语音与文字延续；企业部署时仍受既有连接授权、工作区权限和用量限制约束。

### Anthropic 公布 Claude 辅助发现的新酶系统

主题类别：模型与研究 / 应用落地

发生了什么：Anthropic 9 月 23 日公布其生命科学团队的早期研究：约 950 个 Agent 在约 21 小时内搜索 DNA 数据，提出与重复序列相关的逆转录酶系统线索，随后由人类研究人员在实验室进行初步测试，并公开预印本。

为什么重要：AI 在科研中的角色已能从文献整理延伸到候选发现与实验假设；该系统的主要生物学功能尚未确定，现阶段不能把它写成可用的基因编辑技术。

### Google 公布可跨设备保留记忆的隐私计算设计

主题类别：模型与研究 / 政策治理

发生了什么：Google DeepMind 9 月 23 日公布 Private AI Compute 的服务端持久记忆设计，计划通过设备掌握的密钥、隔离执行环境和加密存储，让个人上下文可在设备之间延续，并同步公开技术说明与服务器软件验证机制。

为什么重要：持续型助手需要长期记忆，也会增加隐私和审计要求；这是一项架构与验证材料更新，不能据此认定跨设备记忆已向所有用户上线或已独立证明零风险。

### NVIDIA 发布 Isaac ROS 5.0

主题类别：开源生态 / 芯片与算力

发生了什么：NVIDIA 9 月 22 日在 ROSCon 发布 Isaac ROS 5.0，为机器人开发加入 Agent 技能与新的开发流程，并更新 GPU 加速组件和 Jetson 部署支持；ROS 是机器人软件常用的开源框架。

为什么重要：编程 Agent 开始进入机器人软件栈，可能缩短感知与控制组件的移植和验证流程；真实机器人仍需单独检查硬件兼容、实时性和安全测试。

## 国内动态

### 阿里公布芯片、模型与 Agent 云的一揽子进展

主题类别：芯片与算力 / 模型与研究 / Agent 与开发工具

发生了什么：阿里在 9 月 22 日开幕的云栖大会公布真武 V900 AI 芯片、AgentCore 和企业上下文服务，称 Qwen 4 正在训练；真武 V900 计划于 2027 年第一季度量产商用，后续 Qwen 4.5/5 的规模仍属路线图。

为什么重要：国内厂商正将模型、芯片与 Agent 运行平台打包供应，但已发布服务、在训模型和未来硬件不能混为同等可采购能力；芯片性能、节省成本等数字均为厂商披露。

### 阿里推出面向手机厂商的 Qwen Intelligence

主题类别：Agent 与开发工具 / 应用落地

发生了什么：阿里在云栖大会推出 Qwen Intelligence，提供移动端模型、任务规划、跨应用操作和创作 Agent 等组件，并宣布荣耀为首批合作伙伴，计划将其用于 Magic9 系列和 Robot Phone。

为什么重要：手机 Agent 从单个语音助手转向系统级任务编排；跨应用操作的真实成功率、用户授权与隐私边界仍需在量产设备上验证，厂商公布的评测结果不能直接代表所有使用场景。

### Qwen Code 增加远程项目编辑和工作流恢复

主题类别：Agent 与开发工具 / 开源生态

发生了什么：Qwen 团队 9 月 24 日发布 v0.24.1 至 v0.24.4，加入上下文占用来源查看、通过 SSH 读写远程项目，以及被中断工作流的续跑能力。

为什么重要：编码 Agent 的长任务交付更依赖可观察的上下文、远程执行边界和恢复能力；远程项目仍需按实际 SSH 身份、文件权限和任务状态逐项验收。

### 火山引擎 AgentKit 更新技能测试与用量治理

主题类别：Agent 与开发工具 / 应用落地

发生了什么：火山引擎 9 月 23 日的 AgentKit 更新增加技能在线测试、自然语言创建技能，以及模型网关按 Credits 控制用量；文档注明新能力按地域陆续发布，Credits 仅用于企业内部用量治理。

为什么重要：企业 Agent 平台正把技能交付、测试和多模型预算管理做成产品能力；这些功能的可用地域与 Credits 口径需在接入前核对，不能把内部用量单位当作账户余额或模型价格。

### 国家互联网应急中心发布智能体漏洞通报

主题类别：政策治理 / Agent 与开发工具

发生了什么：国家互联网应急中心 9 月 23 日发布针对 9 月 15 日安全众测结果的详细通报：对 25 家厂商的 54 款模型及智能体应用共发现 873 个漏洞，其中 608 个为大模型与智能体应用特有漏洞，并列出提示注入、身份权限滥用和非预期代码执行等典型风险。

为什么重要：通报把安全关注点从模型输出延伸到工具权限、委托链和代码执行；873 个是该次众测发现数，不能外推为行业漏洞率，也不能认为通报日才完成测试。

### 中美同意建立 AI 对话与事件沟通渠道

主题类别：政策治理

发生了什么：中方 9 月 26 日公布的访问成果与美方 9 月 25 日白宫说明均确认，双方将就 AI 相关风险与收益开展对话，并建立 AI 事件沟通渠道；中方说明下一次对话计划在 11 月举行。

为什么重要：两大 AI 经济体形成了正式沟通安排，但渠道的触发条件、信息共享范围和执行规则尚待明确，不能视为已形成统一监管标准。

## 趋势与影响

- 事实：OpenAI 和 Anthropic 本周都推出不同档位的新模型，并强调速度或成本。判断：企业模型选型会更重视“完成一个合格任务花多少钱”，需要把失败重试、工具调用和人工复核纳入同一评测口径。
- 事实：Voice、Qwen Intelligence、Qwen Code 和 AgentKit 分别把工具、设备、远程工作流和技能治理接入 Agent。判断：下一阶段产品差异将更多体现在权限传播、任务恢复和跨端状态管理。
- 事实：Google 公布隐私记忆架构，国内发布漏洞通报，中美建立对话渠道。判断：持续型 Agent 的扩张会使记忆、身份、事件报告和审计能力成为落地条件；目前各项机制的实际效果仍需验证。

## 下周观察

- Claude Sonnet 5.5 与 GPT-6 Sol/Luna 在公开 API 的实际可用性、限流和单位任务成本，以及独立任务评测结果。
- 荣耀 Magic9 上 Qwen Intelligence 的实际跨应用能力、权限提示与失败恢复机制。
- 中美 AI 对话及事件沟通渠道的实施细节，以及国内漏洞通报后是否出现可核验的修复进展。

## 来源索引

### 全球

- [GPT-6 Sol and Luna in Work and Codex](https://help.openai.com/en/articles/6825453-chatgpt-release-notes)｜OpenAI Help Center｜2026-09-22
- [Announcing GPT-6 Sol and GPT-6 Luna](https://community.openai.com/t/announcing-gpt-6-sol-and-gpt-6-luna/1399925)｜OpenAI Developer Community 官方公告｜2026-09-22
- [OpenAI API Changelog](https://developers.openai.com/api/docs/changelog)｜OpenAI｜2026-09-22 条目
- [Claude Opus 5.5](https://www.anthropic.com/claude-opus-5-5)｜Anthropic｜2026-09-22
- [Claude Sonnet 5.5](https://www.anthropic.com/claude-sonnet-5-5)｜Anthropic｜2026-09-28
- [Anthropic launches Claude Sonnet 5.5](https://venturebeat.com/technology/anthropic-launches-claude-sonnet-5-5-with-30-cost-reduction-per-task-due-to-faster-speeds-and-fewer-tool-calls)｜VentureBeat（二手交叉核验）｜2026-09-28
- [Use plugins in Voice and get work done by speaking](https://help.openai.com/en/articles/6825453-chatgpt-release-notes)｜OpenAI Help Center｜2026-09-23
- [Claude discovers a novel enzyme system with CRISPR-like repeats](https://www.anthropic.com/news/claude-discovers-novel-enzyme-system)｜Anthropic｜2026-09-23
- [Advancing Private AI Compute with secure, server-side memory](https://deepmind.google/blog/advancing-private-ai-compute-with-secure-server-side-memory/)｜Google DeepMind｜2026-09-23
- [NVIDIA Isaac ROS 5.0 Advances Agentic, Open Source Robotics Development](https://blogs.nvidia.com/blog/isaac-ros-5-0-agentic-open-source-robotics/)｜NVIDIA｜2026-09-22

### 国内

- [Alibaba Cloud's 2026 Apsara Conference: Full-Stack AI Roadmap](https://www.alibabacloud.com/blog/alibaba-clouds-2026-apsara-conference-full-stack-ai-roadmap-along-with-global-market-expansion-plan_603598)｜阿里云｜2026-09-25，涉及 9 月 22 日起的大会发布
- [Alibaba Launches Qwen Intelligence](https://www.alibabacloud.com/blog/alibaba-launches-qwen-intelligence-to-power-next-generation-agentic-smartphones_603597)｜阿里云｜2026-09-25，涉及 9 月 22 日发布
- [Qwen Code 功能更新](https://qwenlm.github.io/qwen-code-docs/zh/blog/updates/)｜Qwen Team｜2026-09-24
- [AgentKit 新功能发布记录](https://docs.volcengine.com/docs/agentkit/New_feature_release_notes?lang=zh)｜火山引擎｜2026-09-23
- [关于 2026 年人工智能大模型安全众测活动典型漏洞风险的通报](https://www.cert.org.cn/publish/main/12/2026/20260923204240484168806/20260923204240484168806_.html)｜国家互联网应急中心｜2026-09-23
- [中美达成八点成果共识](https://us.china-embassy.gov.cn/chn/zgyw/202609/t20260926_12031616.htm)｜中国驻美大使馆｜2026-09-26
- [Fact Sheet: U.S.-China State Visit](https://www.whitehouse.gov/fact-sheets/2026/09/fact-sheet-president-donald-j-trump-advances-a-fair-and-reciprocal-relationship-with-china-while-hosting-historic-state-visit/)｜白宫（独立官方交叉核验）｜2026-09-25

## 采集说明

- 去重前登记候选 105 条：本次逐条核验的官网、产品公告和官方机构材料对应 20 个候选事件，加上 X List 在统计窗口内的 85 条帖子；以事件为单位合并后，最终入选全球 7 条、国内 6 条。官网候选的筛选台账仅保存在本次临时目录，不进入发布物。
- X 使用官方 `GET /2/lists/2068180761916977611/tweets`，每页最多 20 条，共读取 5 页、扫描 92 条 API 帖子，85 条落在本期窗口。因本期窗口与上次成功运行有少量重叠，脚本按时间窗抓取并在事件层去重，未把窗口内全部帖子视作新事件。
- 数据缺口：本次 X 请求在受限网络环境首次失败，获网络访问后重试成功；未发现需要用旧周报填补的来源缺口。国内可核验的独立模型新品较少，本期更多是平台、终端及治理进展；未纳入窗口外发布、预告、传闻和低信号更新。
- 厂商披露的基准、成本降幅、硬件指标与未来计划未经本报告独立复现；已发布能力与尚在训练或计划量产的事项在正文中分别表述。
