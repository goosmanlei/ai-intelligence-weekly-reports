# 全球与国内 AI 情报周报（2026-09-14）

## 统计窗口

2026-09-07 11:53:50 至 2026-09-14 11:53:50（Asia/Shanghai，左闭右开）。

## 30 秒总览

- OpenAI 将 Codex 的托管运行框架以公开测试版 Agents API 交给开发者，并提供托管沙箱；长程 Agent 的基础设施开始产品化。
- OpenAI 同周更新全双工语音 GPT-Live-1 与 Images 2.5，实时交互和图像工作流都出现新的可调用能力。
- Google 同时把 Gemini 能力扩展到办公订阅产品，并宣布对芬兰 AI 基础设施投入 130 亿欧元。
- NVIDIA 发布 CUDA Rust 的两条 GPU 内核开发路径，Rust 进入 GPU 核函数编程的官方工具链。
- 国内方面，工信部发布“人工智能+软件”专项行动解读；腾讯云则出现模型下线迁移与新模型接入，生产调用的版本治理成为直接事项。

## 全球动态

### OpenAI 发布 Agents API 公测与托管沙箱

主题类别：Agent 与开发工具 / 应用落地

发生了什么：OpenAI 于 9 月 10 日发布公开测试版 Agents API，提供会话、工具、子 Agent、上下文压缩和运行环境选择，并推出 OpenAI 托管沙箱。

为什么重要：这把长程 Agent 所需的编排和环境管理变为平台能力；接入方可少建一层基础设施，但仍需独立评估权限、数据驻留、工具边界及计费。

### OpenAI 推出 GPT-Live-1 实时语音 API

主题类别：模型与研究 / 应用落地

发生了什么：OpenAI 于 9 月 10 日宣布 GPT-Live-1，支持全双工语音、打断、转写、工具调用与 WebRTC、WebSocket、电话/SIP 接入，并可把复杂推理委派给后端模型或 Agent。

为什么重要：语音 Agent 的难点从单向转写转为实时对话状态和后端任务协调；官方公布的基准和延迟均为厂商披露，部署前仍应以业务场景验证中断、权限与成本。

### ChatGPT Images 2.5 与两款 API 图像模型上线

主题类别：模型与研究 / 应用落地

发生了什么：OpenAI 于 9 月 8 日发布 ChatGPT Images 2.5，并在 API 中增加 GPT-Image-2.5 Flare 与 Sunburst；公告称更新覆盖更快生成、编辑一致性、评论式修改和更细粒度创作能力。

为什么重要：图像生成从一次性出图继续走向可编辑的创作流程；团队应在上线前复核模型标识、分辨率、内容安全和实际 token 消耗，而不只依据宣传能力。

### Google 更新 AI 订阅产品功能

主题类别：应用落地

发生了什么：Google 于 9 月 9 日公布 AI Plus、Pro 和 Ultra 的新功能，包括 Gmail、Docs、Keep 的语音能力，Workspace 内的 Google Pics 与 Sheets canvas，以及接入 Chrome 和 Photos 的 Gemini Spark；部分能力限特定套餐或美国地区。

为什么重要：AI 功能正被嵌入现有办公套件并按套餐、地区分层交付；企业评估应以实际可用范围、数据处理条款和协作流程为准。

### Google 宣布向芬兰 AI 基础设施投资 130 亿欧元

主题类别：芯片与算力 / 资本与组织变动

发生了什么：Google 于 9 月 9 日宣布未来两年向芬兰投入 130 亿欧元，扩展数据中心和相关数字基础设施，并同步说明核电延寿支持、风电与 94MW 电池项目等能源安排。

为什么重要：这是 Google 所称的欧洲最大单笔投资，说明 AI 算力竞争已同时受制于数据中心、供电和电网稳定性；金额和就业影响为公司预测，不能视为已实现结果。

### NVIDIA 推出 CUDA Rust 的 GPU 内核开发路径

主题类别：芯片与算力 / 开源生态

发生了什么：NVIDIA 于 9 月 8 日介绍 CUDA Rust：`cuda-oxide` 面向 SIMT 风格 Rust 内核编译到 PTX，`cutile-rs` 则面向 Tile 编程；官方称将支持与 CUDA C++、Python 的互操作。

为什么重要：对以 Rust 建设推理、服务与 Agent 运行时的团队，GPU 内核不再必然需要切换语言；但两个路径的稳定性、工具链约束和性能仍须按目标 GPU 与负载实测。

## 国内动态

### 工信部解读“人工智能+软件”专项行动实施方案

主题类别：政策治理 / Agent 与开发工具

发生了什么：工信部于 9 月 11 日发布解读，说明专项行动将以智能编程覆盖需求、代码、测试等研发流程，鼓励建设智能体软件产品和应用市场，并提出生成代码安全审查与上线前安全检测。

为什么重要：政策信号把“智能体软件”和生成代码安全同时放入软件业转型框架；软件企业需把提效试点与代码审查、数据安全和人员培训配套推进。

### 腾讯云 TokenHub 下线两款 Qwen 模型并执行迁移

主题类别：Agent 与开发工具 / 政策治理

发生了什么：腾讯云公告称，TokenHub、ADP 与 CloudBase 的 `qwen3.5-flash`、`qwen3.5-plus` 于 9 月 8 日下线；未完成迁移的调用将按产品线自动切换到 DeepSeek-V4-Flash、Kimi K2.6 或 hy3 等替代模型。

为什么重要：生产系统的模型名不应被视为长期稳定依赖；自动迁移会同时改变能力、计费和失败模式，调用方应保留版本锁定、回归测试、超时重试和可回滚的切换策略。

### 腾讯云 TokenHub 新增 DeepSeek-V4.1-Flash 原厂直供

主题类别：模型与研究 / Agent 与开发工具

发生了什么：腾讯云 TokenHub 产品动态显示，平台于 9 月 10 日新增支持 DeepSeek-V4.1-Flash 原厂直供模型。

为什么重要：多模型平台的供给更新增加了模型选择，但“可调用”不等于适配既有工作流；开发团队仍需验证上下文、工具调用、价格、限流和输出稳定性后再迁移。

## 趋势与影响

- 事实：OpenAI 将 Agent 编排、沙箱与语音交互同时推向 API，腾讯云则发生模型替换。判断：模型本身正成为可变组件，运行环境、版本治理与回归评测将更直接决定生产可靠性。
- 事实：Google 的办公 AI 更新和 NVIDIA 的 Rust 工具链分别面向终端工作流与底层开发。判断：AI 竞争的价值重心继续从“发布一个模型”向产品集成与工程效率扩展。
- 事实：工信部把智能编程、智能体软件和生成代码安全并置。判断：国内企业的 AI 软件改造需要把安全审查前置到研发流程，而非在上线后补充合规措施。

## 下周观察

- Agents API 公测期间的区域可用性、托管沙箱的数据处理边界和正式版定价。
- GPT-Live-1 与 Images 2.5 的 API 文档、配额和企业控制项是否进一步明确。
- 腾讯云自动迁移后各产品线的实际模型标识、价格、限流与回滚能力。

## 来源索引

### 全球

- [Introducing the Agents API](https://openai.com/index/introducing-the-agents-api/)｜OpenAI｜2026-09-10
- [Introducing GPT-Live-1 in the API](https://community.openai.com/t/introducing-gpt-live-1-in-the-api/1396471)｜OpenAI Developer Community｜2026-09-10
- [Introducing GPT Images 2.5 in the API and ChatGPT](https://community.openai.com/t/introducing-gpt-images-2-5-in-the-api-and-chatgpt/1395897)｜OpenAI Developer Community｜2026-09-08
- [Tackle your to-do list with new features in our Google AI plans](https://blog.google/products-and-platforms/products/google-one/fall-2026-ai-plan-updates/)｜Google｜2026-09-09
- [Google deepens its commitment to Finland with a €13 billion investment in AI infrastructure](https://blog.google/innovation-and-ai/infrastructure-and-cloud/global-network/google-ai-commitment-to-finland/)｜Google｜2026-09-09
- [Introducing CUDA Rust: Two Tracks for Writing GPU Kernels](https://developer.nvidia.com/blog/introducing-cuda-rust-two-tracks-for-writing-gpu-kernels/)｜NVIDIA｜2026-09-08

### 国内

- [七问+一图，读懂《“人工智能+软件”专项行动实施方案》](https://wap.miit.gov.cn/jgsj/xxjsfzs/gzdt/art/2026/art_45df9463e105446c996568f299e07bca.html)｜工业和信息化部｜2026-09-11
- [关于腾讯云 Qwen3.5-Flash、Qwen3.5-Plus 模型下线及切换升级的通知](https://cloud.tencent.com/announce/detail/2427)｜腾讯云｜2026-09-08 生效
- [大模型服务平台 TokenHub 产品动态](https://cloud.tencent.com/document/product/1823/130675)｜腾讯云｜2026-09-10

## 采集说明

- 去重前登记候选 67 条：官方博客、产品公告、开发者文档、芯片厂商公告、政府页面和平台规则 11 条，X List 增量窗口内 56 条；按事件合并后最终入选全球 6 条、国内 3 条。
- X API 使用官方 `GET /2/lists/2068180761916977611/tweets` 接口，共读取 3 页、扫描 56 条帖子；因到达已见帖子边界停止。X 用于发现和交叉核验，不作为入选事件的唯一事实来源。
- 数据缺口：窗口内可核验的国内一手模型/芯片新品有限，国内最终以正式政策和平台运行变更为主；未纳入传闻、预告、纯观点、转发或无法核验的性能与融资信息。
- 厂商的能力、基准、价格、投资与影响预测均按原始披露转述，未由本报告独立复现。
