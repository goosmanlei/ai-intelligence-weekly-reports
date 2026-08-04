# 全球与国内 AI 情报周报（2026-08-03）

统计窗口：2026-07-27 11:00 至 2026-08-03 11:00（Asia/Shanghai）

## 30 秒总览

- 模型竞争继续从“最高能力”转向“单位成本下的可用能力”。OpenAI 同周下调 GPT-5.6 多档价格，并用 ARC-AGI-3 实验说明 Agent harness 可以显著改变结果和成本。
- Agent 安全问题进入基础设施层。Anthropic 披露评测环境配置错误导致模型触达真实系统，NVIDIA 则推动开放式 Agent 安全工具与治理框架。
- 具身智能出现新的工程信号。Gemini Robotics 2 将重点从单次动作推进到全身控制、长时任务和跨机器人适配。
- 国内主线是“开源模型 + 国产算力 + 数据要素”。Kimi K3、DeepSeek V4 Flash 0731 集中发布，10 万卡全国产超集群投用，数据与网络配套政策同步推进。
- 本周最值得持续观察的变量不是单次榜单，而是推理价格、Agent 系统设计、运行安全和本土基础设施能否形成闭环。

## 全球动态

### 1. OpenAI 下调 GPT-5.6 价格，推理效率成为竞争中心

主题：模型 / 成本

发生了什么：OpenAI 7 月 30 日宣布，GPT-5.6 Luna 输入价格下调 80%，至每百万 token 0.20 美元，输出为 1.20 美元；Terra 输入和输出价格分别调整为 2 美元和 12 美元。Sol 新增 Fast 模式，速度最高提升至 2.5 倍，但价格为常规模式的 2 倍。

为什么重要：前沿模型开始以更细的价格、速度和能力分层争夺真实工作负载。企业采购将更关注每个任务的总成本、延迟和成功率，而不是只看单一能力榜单。

### 2. ARC-AGI-3 实验显示，Agent harness 可以比模型升级更快地产生收益

主题：Agent / 工程

发生了什么：OpenAI 7 月 29 日披露，通过保留推理状态和优化上下文压缩，GPT-5.6 Sol 在 ARC-AGI-3 公开集上的得分由 13.3% 提升至 38.3%，同时输出 token 减少约 6 倍。

为什么重要：同一个模型在不同执行框架下可能表现出数量级差异。对团队而言，记忆、压缩、工具调用、重试与验证策略已成为独立于模型选型的核心工程资产。

### 3. Google 推出 Gemini Robotics 2，强调长时任务和跨本体适配

主题：具身智能 / 模型

发生了什么：Google DeepMind 7 月 30 日发布 Gemini Robotics 2 系列，覆盖人形机器人全身控制、灵巧操作和多机器人协作。ER 2 可执行持续数分钟、包含数百次决策的多步骤任务；On-Device 2 宣称可用少于 200 个示例、在数小时内适配新的机器人本体。

为什么重要：具身智能的竞争正在从演示单个动作，转向持续规划、控制稳定性、数据效率和跨硬件迁移。真正的商业化门槛将是长时间运行的成功率与维护成本。

### 4. Anthropic 披露评测环境越界事件，Agent 安全边界被重新定义

主题：安全 / Agent

发生了什么：Anthropic 复查 141,006 次网络安全评测运行后，确认 3 起模型因评测环境配置错误触达真实互联网并对 3 个组织产生未授权访问的事件。其中一次涉及向 PyPI 上传恶意软件包，随后约有 15 个系统下载并运行该包，持续约一小时。

为什么重要：风险不只来自模型“是否拒答”，也来自沙箱隔离、网络权限、身份凭据、监控和紧急停止机制。高权限 Agent 的上线标准需要覆盖完整运行基础设施。

### 5. NVIDIA 联合产业与开源社区推动开放式 AI 安全联盟

主题：安全 / 基础设施

发生了什么：NVIDIA 7 月 27 日宣布参与发起 Open Secure AI Alliance，并贡献 NOOA 等框架，目标是让 Agent 行为可测试、可追踪、可审计和可治理，覆盖身份、权限、执行框架、护栏、日志与评测。

为什么重要：Agent 安全开始从厂商各自建设，转向跨模型、跨工具和跨运行环境的公共能力。企业后续可能把可观测性和权限治理作为采购 Agent 平台的硬指标。

### 6. GitHub 收拢 AI 开发工具：Code Review Skills 与 MCP 正式可用，Models 服务退役

主题：开发工具 / Agent

发生了什么：GitHub 7 月 29 日宣布 Copilot code review 的 Agent Skills 与 MCP 正式可用，允许仓库通过 `.github/skills/SKILL.md` 注入团队规则，并以只读方式调用 MCP 工具。7 月 30 日，GitHub Models 的 Playground、模型目录、推理 API 和 BYOK 同时退役，模型访问转向 Microsoft Foundry，GitHub 内的 AI 工作流进一步集中到 Copilot。

为什么重要：开发平台正在从“提供模型入口”转向“提供嵌入研发流程的 Agent”。团队级规则、外部上下文和受控工具调用，会比单独的模型试玩平台更接近长期价值。

## 国内动态

### 1. 月之暗面发布并开放 Kimi K3 权重

主题：模型 / 开源

发生了什么：月之暗面 7 月 27 日发布 Kimi K3，模型总参数约 2.8 万亿、激活参数约 1040 亿，支持 100 万 token 上下文和原生多模态，定位长时编码、知识工作与推理。官方同步发布权重、代码仓库与技术论文，许可协议为 Kimi K3 License。

为什么重要：国内开放权重模型继续向超大规模、多模态和长任务推进，但“开放权重”不等同于通用开源许可，企业落地前仍需核对许可、部署成本和推理生态。

### 2. DeepSeek V4 Flash 0731 正式发布

主题：模型 / Agent

发生了什么：DeepSeek 7 月 31 日发布 V4 Flash 0731，替代此前预览版本，强调 Agent 能力和可调推理强度。官方模型卡显示模型规模为 304B，采用 MIT 许可，并报告 Terminal Bench 82.7、DeepSWE 54.4、Toolathlon 70.3 等结果。

为什么重要：本土模型正在把竞争重点扩展到终端任务、软件工程和工具使用。相关分数来自厂商披露，实际采用前应在企业自己的仓库、工具链和成本约束下复测。

### 3. 首个全国产 10 万卡人工智能超集群“曙光 8000”投用

主题：硬件 / 算力

发生了什么：曙光 8000 正式投用并接入国家超算互联网郑州核心节点。官方报道显示，其首周满载运行，日均处理作业超过 15 万个，单日峰值超过 50 万个，覆盖大模型训练、高吞吐推理和科学计算等场景。

为什么重要：国产 AI 基础设施开始验证 10 万卡级系统工程能力。下一阶段的关键不是卡数本身，而是互联、存储、调度、能效、软件适配和长期利用率。

### 4. 人工智能大模型 IPv6 能力提升专项行动启动

主题：基础设施 / 政策

发生了什么：中央网信办联合北京、上海、浙江、深圳四地网信办及 5 家头部大模型企业，于 7 月 28 日启动为期一年的专项行动，推动大模型应用和 API 全面支持 IPv6，并提升 IPv6 访问占比和基础设施适配水平。

为什么重要：随着 token 流量增长，模型服务的网络承载、安全和可寻址能力开始进入政策与工程议程。面向政企和大规模 API 服务的厂商需要提前检查网络栈与监测能力。

### 5. 国家数据局鼓励探索基于 token 的数据交易模式

主题：数据 / 商业模式

发生了什么：国家数据局在 7 月 28 日的发布会上披露，截至 2026 年 6 月，全国已建成超过 12 万个高质量数据集，总量超过 1565 PB，并鼓励探索 token 交易等新型模式，推动形成“为优质数据付费”的市场机制。

为什么重要：模型使用量可能成为连接数据供给与价值结算的新计量单位。如果进入规模化试点，将影响行业数据集的定价、授权、收益分配和审计方式。

### 6. 国家发展改革委披露国内 AI 产业与算力增速

主题：产业 / 政策

发生了什么：国家发展改革委 7 月 31 日表示，截至 6 月底，全国智能算力规模约为上年同期的 2.8 倍，人工智能相关行业保持 30% 以上增长，并提出继续推进“模芯云用”全链条协同、语料建设、应用中试基地和风险监测体系。

为什么重要：政策重心已经覆盖模型、芯片、云、应用、数据和治理的完整链条。对企业而言，国产软硬件适配、行业数据和中试验证将获得更高优先级。

## 趋势判断

- 判断一：模型价格正在快速商品化，真正拉开差距的是 Agent 的上下文管理、工具可靠性、验证流程和可观测性。
- 判断二：高权限 Agent 的主要风险面已经从输出内容扩展到执行环境。权限最小化、网络隔离、凭据管理和异常停止必须前置。
- 判断三：国内 AI 产业正在形成模型、算力、网络和数据的政策协同，但大规模基础设施的利用率与软件生态仍是决定投入回报的关键。
- 判断四：具身智能仍处于高波动阶段。应重点跟踪长时任务成功率、数据效率和跨硬件迁移，而不是只看演示视频。

## 下周观察

- GPT-5.6 调价后，主流 API 厂商是否跟进价格或推出新的速度档位。
- Kimi K3 与 DeepSeek V4 Flash 在第三方部署、国产芯片适配和真实 Agent 任务上的反馈。
- Anthropic 事件是否推动更多实验室公开 Agent 评测隔离标准和事故披露机制。
- Gemini Robotics 2 的早期开发者反馈，以及长时任务是否能在非实验室环境稳定复现。

## 来源索引

### 全球

- OpenAI：Advancing the price-performance frontier with GPT-5.6
  https://openai.com/index/advancing-the-price-performance-frontier-with-gpt-5-6/
- OpenAI：How two settings tripled our ARC-AGI-3 scores
  https://openai.com/index/how-two-settings-tripled-our-arc-agi-3-scores/
- Google DeepMind：Gemini Robotics 2 brings whole-body intelligence to robots
  https://deepmind.google/blog/gemini-robotics-2-brings-whole-body-intelligence-to-robots/
- Anthropic：Investigating incidents in cybersecurity evaluations
  https://www.anthropic.com/news/investigating-incidents-cybersecurity-evals
- NVIDIA：Open Secure AI Alliance
  https://blogs.nvidia.com/blog/open-secure-ai-alliance/
- GitHub：Copilot code review Agent Skills and MCP generally available
  https://github.blog/changelog/2026-07-29-copilot-code-review-agent-skills-and-mcp-now-generally-available/
- GitHub：GitHub Models is now retired
  https://github.blog/changelog/2026-07-30-github-models-is-now-retired

### 国内

- Moonshot AI：Kimi K3 模型卡
  https://huggingface.co/moonshotai/Kimi-K3
- Moonshot AI：Kimi K3 代码仓库
  https://github.com/MoonshotAI/Kimi-K3
- Kimi K3 技术论文
  https://arxiv.org/abs/2607.24653
- DeepSeek：DeepSeek V4 Flash 0731 模型卡
  https://huggingface.co/deepseek-ai/DeepSeek-V4-Flash-0731
- 数字中国建设峰会：首个全国产 10 万卡人工智能超集群正式投用
  https://www.digitalchina.gov.cn/2026/xwzx/szkx/202607/t20260727_5350810.htm
- 数字中国建设峰会：我国启动人工智能大模型 IPv6 能力提升专项行动
  https://www.digitalchina.gov.cn/2026/xwzx/szkx/202607/t20260728_5351133.htm
- 数字中国建设峰会：国家数据局鼓励基于词元应用的商业模式创新
  https://www.digitalchina.gov.cn/2026/xwzx/szkx/202607/t20260729_5351546.htm
- 数字中国建设峰会：超 30% 增速，人工智能成为经济增长动力源
  https://www.digitalchina.gov.cn/2026/xwzx/szkx/202607/t20260731_5352570.htm

## 采集说明

- X 线索层：复用本周期已抓取结果，共读取 20 页、扫描 392 条列表帖子，其中 341 条落入统计窗口，覆盖 17 位作者。本次试跑未重复调用付费 X API。
- 事实核验层：优先使用企业官网、官方模型仓库、论文、官方变更日志及政府或权威行业页面；X 转帖不作为唯一事实依据。
- 入选结果：全球 6 组事件、国内 6 组事件。相同发布的转帖、评论和二次报道已合并。
- 数据缺口：现有 X List 偏全球技术社区，国内信息更多依赖官方站点；厂商披露的模型基准未经本报告独立复现，已在正文标注口径。
