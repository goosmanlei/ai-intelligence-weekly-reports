# 全球与国内 AI 情报周报（2026-10-05）

## 统计窗口

2026-09-28 11:02:10 至 2026-10-05 11:02:10，Asia/Shanghai（北京时间），左闭右开。按本次实际运行时刻回溯 7 天；与上期窗口有约 16 小时重叠，已排除上期报道且没有新增事实的事件。

## 30 秒总览

- OpenAI 发布 GPT-6.1 Sol，标准输入、输出单价分别为每百万 token 2、10 美元，缓存读取单价降至 0.10 美元。
- Dots 开始向符合条件的用户开放，持续运行的云端 Agent 从单次问答走向承接长期任务。
- Google 的 Gemini 4 Argon 已向部分可信网络安全合作方开放，普通开发者和消费者仍需等待。
- DeepSeek 开源昇腾计算与通信组件，国产算力的模型部署路径获得更多可直接检查的工程代码。
- 国内短视频专项整治明确覆盖 AI 冒充人物和虚假代言，标注 AI 生成不能免除内容治理要求。

## 全球动态

### 1. GPT-6.1 Sol 发布，缓存上下文的成本继续下降

主题类别：模型与研究

发生了什么：OpenAI 9 月 29 日发布 GPT-6.1 Sol，供 API、Codex 和 ChatGPT Work 使用；在标准 API、输入不超过 272K token 的价格档，输入、输出分别为每百万 token 2、10 美元，缓存读取为 0.10 美元，较 GPT-6 Sol 的缓存读取单价降低一半。

为什么重要：重复使用上下文的开发工作流有了更低的计费起点；“接近 Astra”是厂商的能力概括，独立评测机构 Artificial Analysis 也已登记新模型，但综合榜单成绩不能直接代表企业任务的成功率或总成本。

### 2. Dots 开始开放，Agent 可持续处理长期任务

主题类别：Agent 与开发工具、应用落地

发生了什么：OpenAI 9 月 29 日推出由 GPT-6 Astra 驱动、拥有云端电脑的 Dots，在符合条件的市场逐步开放；Pro 和 Business Premium 可用，Enterprise 等工作区的试用由管理员开启，承担组织专责的 specialist dots 仍属企业试点。

为什么重要：持续执行、连接应用和保留反馈让 Agent 能承接跨天工作；实际采用仍取决于任务权限和人工审阅，而默认后台主动研究限于已连接应用的只读工具，不能据此理解为无限制自动写入。

### 3. Gemini 4 Argon 进入受限开放

主题类别：模型与研究、政策治理

发生了什么：Google 9 月 30 日公布 Gemini 4 Argon，已经通过 Fairwind 计划向部分可信网络安全防御合作方开放，并在扩大访问前继续进行安全测试；普通开发者、企业和消费者的广泛开放尚未完成。

为什么重要：前沿模型的能力发布与大众可用开始出现更明确的阶段划分；企业选型应以拿到的访问权限和真实任务验证为准，不能把已宣布的未来价格当成当前可采购的公开 API。

### 4. NVIDIA 发布 Agent 安全参考架构与 OpenShell 实践

主题类别：Agent 与开发工具、芯片与算力、开源生态

发生了什么：NVIDIA 9 月 28 日公布开放 Agent 安全平台参考设计及 OpenShell 使用指南，以开源运行时执行文件、网络和工具访问策略，并提出由 BlueField-4 上的 Sentry 提供独立硬件监控层。

为什么重要：把权限执行放在 Agent 无法随意修改的运行环境中，为长期任务提供可检查的约束；已可试用的 OpenShell 与硬件参考设计应分开评估，不能把架构说明等同于所有硬件上的完整量产交付。

### 5. AMD 公布收购 World Labs 的最终协议

主题类别：资本与组织变动、芯片与算力

发生了什么：AMD 9 月 28 日宣布签署收购李飞飞创办的 World Labs 的最终协议，交易约 82 亿美元、以股票支付，预计年底前完成，仍须监管批准等条件；交割后李飞飞将出任执行副总裁兼首席科学家。

为什么重要：芯片厂商开始更直接地结合空间智能模型研发与算力路线规划，可能影响机器人和仿真所需的软硬件生态；交易公告尚不能证明并购已经完成或已带来产品收益。

### 6. Microsoft 发布实时转写与多语言语音模型

主题类别：模型与研究、应用落地

发生了什么：Microsoft 10 月 1 日发布 MAI-Transcribe-2-Streaming，支持 60 种语言及连续语言检测，并同步推出支持 23 种语言的 MAI-Voice-2.1 与 Flash 版本，可通过 Microsoft Foundry 等入口使用。

为什么重要：边说边转写、跨语言保留同一声音，为客服和教学语音 Agent 提供更完整的输入输出链路；官方展示的延迟与性能结果仍需在实际网络、音频和并发条件下验证。

### 7. Quine 将生物模型、科研工具与实验反馈连接起来

主题类别：模型与研究、应用落地

发生了什么：Microsoft Research 9 月 29 日公布 Quine 研究系统，以多模态生物学模型配合科研工具和文献；团队称与 Broad Institute 合作筛选的部分化合物已通过多项湿实验验证，并将通过 Fellows 计划提供研究访问。

为什么重要：AI 科研的价值开始以“计算建议能否通过真实实验”衡量；该系统属于实验性研究技术，现有结果不等于药物临床疗效或可直接使用的医疗产品。

## 国内动态

### 1. DeepSeek 开源昇腾计算与通信组件

主题类别：芯片与算力、开源生态

发生了什么：DeepSeek 9 月 30 日公开面向华为昇腾的基础组件，官方仓库可核验 DeepGEMM-Ascend 的首次发布与 Ascend 950 支持，以及 DeepEP-Ascend 的跨设备通信实现。

为什么重要：矩阵计算与专家间通信是大型模型部署的关键环节，公开代码让国产平台的适配和复现更具体；仓库性能表属于指定硬件配置下的项目方测试，也不能单独证明某个模型已全程用昇腾训练。

### 2. DeepSeek Harness 发布 0.2.0 候选版本

主题类别：Agent 与开发工具、开源生态

发生了什么：DeepSeek Harness 9 月 28、29 日发布 0.2.0-rc.1、rc.2，桌面端提供 dsh 命令和插件管理，改善工具运行环境加载及异常处理；整个系列仍标记为预发布版本。

为什么重要：开源 Agent 的实用性越来越取决于桌面环境、插件和任务恢复能力；候选版可以用于评估，但模型目录调整及配置兼容性仍需核对，不应当作稳定版升级承诺。

### 3. 荣耀 Magic9 开售，YOYO 任务和记忆能力进入新机

主题类别：应用落地

发生了什么：荣耀 9 月 28 日发布并开售 Magic9 系列，搭载 MagicOS 11，提供 YOYO 记忆、音视频高光记录及协调受支持服务的多步骤任务能力。

为什么重要：手机成为 Agent 功能面向普通用户的交付入口；这一事件的新增事实是设备上市，MagicOS 11 本身此前已发布，跨应用能力仍受支持服务和授权范围限制。

### 4. 短视频专项整治覆盖 AI 仿冒人物与虚假代言

主题类别：政策治理

发生了什么：中央网信办 9 月 30 日发布为期两个月的专项行动公告，将利用 AI 合成音视频假冒公众人物、虚假代言和营销列为整治内容，并要求平台加强审核、标注和推荐管理。

为什么重要：AI 内容产品和营销团队需要同时检查人物授权与内容真实性；公告明确，标注“AI 生成”或“虚构演绎”本身不能用来规避治理要求。

### 5. 深圳人工智能联合基金重大专项发布年度指南

主题类别：模型与研究、政策治理

发生了什么：国家自然科学基金委员会 9 月 30 日公告，深圳人工智能联合基金重大专项 2026 年度指南已在科学基金网络信息系统发布，申请单位和研究者需登录查看。

为什么重要：这为科研团队提供了明确的项目申报入口；公开通告未列出完整研究方向、额度或截止时间，本期不据此推断新增投入规模。

## 趋势与影响

- 判断：模型竞争之外，运行环境和权限治理正成为 Agent 的核心组成。依据是 Dots 的长期任务机制、OpenShell 的独立权限执行，以及 Harness 的桌面与插件迭代；开发团队应把任务恢复与可审阅结果纳入验收。
- 判断：成本优化需要同时看单价、上下文复用和任务完成质量。Sol 的缓存降价是已公布事实，但本期没有同条件业务测量，不能据此计算企业实际节省比例。
- 判断：AI 从屏幕输出进入科研实验、芯片软件栈和手机任务后，验证对象也需改变：科研看实验复现，算力看相同配置下的性能，终端看可用服务中的真实任务完成情况。

## 下周观察

- Gemini 4 Argon 是否扩大 Fairwind 以外的访问，以及正式可用范围和开发者价格；依据是 Google 公告中的分阶段开放安排，本期未给出确定日期。
- Dots 的工作区试用和 specialist dots 企业试点是否公布更多权限、管理与效果证据；依据是 OpenAI 已披露的管理员开关及试点安排。
- 昇腾开源组件是否出现可复现实验和更多硬件适配反馈，以及 Harness 候选版本的后续稳定性修复；依据是新发布的官方仓库与预发布版本。

## 来源索引

### 全球

- [GPT-6.1 Sol 发布](https://openai.com/index/introducing-gpt-6-1-sol/)｜OpenAI｜2026-09-29
- [API 更新日志及价格档](https://developers.openai.com/api/docs/changelog)｜OpenAI｜2026-09-29 对应条目
- [GPT-6.1 Sol 独立测评](https://artificialanalysis.ai/models/gpt-6-1-sol)｜Artificial Analysis（独立评测一手材料）｜模型发布 2026-09-29，页面核验 2026-10-05
- [Introducing dots](https://openai.com/index/introducing-dots/)｜OpenAI｜2026-09-29
- [OpenAI launches Dots](https://techcrunch.com/2026/09/29/openai-launches-dots-its-bubbly-agentic-avatar/)｜TechCrunch（二手交叉核验）｜2026-09-29
- [Gemini 4 Argon](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-4-argon/)｜Google｜2026-09-30
- [Google unveils Gemini 4](https://www.axios.com/2026/09/30/google-gemini-4)｜Axios（二手交叉核验）｜2026-09-30
- [NVIDIA Agent 安全参考设计](https://developer.nvidia.com/blog/nvidia-open-agent-safety-platform-a-reference-for-continuous-in-silicon-agent-monitoring/)｜NVIDIA｜2026-09-28
- [OpenShell 运行时控制指南](https://developer.nvidia.com/blog/add-runtime-controls-to-ai-agents-with-nvidia-openshell/)｜NVIDIA｜2026-09-28
- [AMD 收购 World Labs 协议](https://ir.amd.com/news-events/press-releases/detail/1299/amd-to-acquire-world-labs-to-advance-the-future-of-ai-compute)｜AMD｜2026-09-28
- [AMD will acquire World Labs](https://techcrunch.com/2026/09/28/amd-will-acquire-fei-fei-lis-world-labs-for-8-2-billion/)｜TechCrunch（二手交叉核验）｜2026-09-28
- [Microsoft 实时转写与语音模型](https://microsoft.ai/news/our-first-streaming-transcription-model/)｜Microsoft AI｜2026-10-01
- [Quine 生物学研究系统](https://www.microsoft.com/en-us/research/blog/introducing-quine-an-ai-research-system-designed-for-the-complexity-of-biology/)｜Microsoft Research｜2026-09-29

### 国内

- [DeepGEMM-Ascend](https://github.com/deepseek-ai/DeepGEMM-Ascend/blob/main/README.md)｜DeepSeek 官方仓库｜2026-09-30 首发记录
- [DeepEP-Ascend](https://github.com/deepseek-ai/DeepEP-Ascend)｜DeepSeek 官方仓库｜配套材料，本期核验 2026-10-05
- [DeepSeek 开源昇腾基础组件](https://t.cj.sina.com.cn/articles/view/3996876140/ee3b7d6c001017sw4)｜机器之心／新浪转载（二手交叉核验）｜2026-09-30
- [Harness 0.2.0-rc.1](https://github.com/deepseek-ai/deepseek-harness/releases/tag/dsh-v0.2.0-rc.1)｜DeepSeek 官方仓库｜2026-09-28
- [Harness 0.2.0-rc.2](https://github.com/deepseek-ai/deepseek-harness/releases/tag/dsh-v0.2.0-rc.2)｜DeepSeek 官方仓库｜2026-09-29
- [Magic9 系列国内发布](https://www.honor.com/cn/news/honor-magic9-launch/)｜荣耀｜2026-09-28
- [Magic9 功能与可用范围](https://www.honor.com/global/news/honor-magic9-launch/)｜荣耀｜2026-09-28，中国公司海外语言公告归入国内
- [短视频虚假人设专项行动](https://www.cac.gov.cn/2026-09/30/c_1792520301987752.htm)｜中央网信办｜2026-09-30
- [深圳人工智能联合基金重大专项通告](https://www.nsfc.gov.cn/p1/3381/2824/143118.html)｜国家自然科学基金委员会｜2026-09-30

## 采集说明

- 登记的网页候选线索为 20 个，加上窗口内 X 帖子 47 条，去重前共 67 条候选材料；它们不是 67 个独立事件。按事件合并、核验日期并筛选后，最终入选全球 7 条、国内 5 条。
- 官方 X List API 使用 GET /2/lists/2068180761916977611/tweets，单页上限 20 条；读取 3 页、扫描 59 条帖子、窗口内 47 条。上期已见游标位于本期窗口内，因此按时间窗抓取并在事件层去重，避免漏收；Sonnet 5.5 等已报道事件未重复列入。
- 首次 X 网络请求失败，获得联网权限后重试成功，本期无 X API 采集缺口；该 List 的账号覆盖有限，不能代表全部国内或全球发布。
- 网页检索覆盖模型、Agent、算力、应用、开源、治理、资本与组织七类主题；未对来源清单中每个站点做全量扫描。智谱博客入口返回错误，部分 AP 页面及基金指南链接读取失败；其他官方来源仍可核验，未用失败源支撑正文。
- 排除 DeepSeek V5 传闻、阿里安全模型缺乏可核验发布材料的线索，以及年份不符、窗口外和上期无新增事实的发布；不将未来开放、未来价格或计划交割写成已经完成。
- 国内基金指南正文需要登录，本期只能确认通告；NVIDIA、Google、Microsoft 及 DeepSeek 的性能与科研效果主要是项目方披露，除 Sol 的独立评测页面外，未取得同条件独立复现证据。
