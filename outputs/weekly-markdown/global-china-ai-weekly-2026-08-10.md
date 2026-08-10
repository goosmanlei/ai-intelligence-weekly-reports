# 全球与国内 AI 情报周报（2026-08-10）

## 统计窗口

2026-08-03 11:02:19 至 2026-08-10 11:02:19（Asia/Shanghai，左闭右开）。

## 30 秒总览

- Claude Code 将把自动授权模式设为个人与团队套餐的默认选项，Agent 的核心竞争正从“少弹确认框”转向可量化的执行安全。
- Anthropic 同周补齐自托管执行环境和企业级实时 DLP，显示高权限 Agent 正进入企业基础设施与合规控制面。
- OpenAI 扩大 GPT-5.6 Luna 免费访问，并把 Codex 安全审查嵌入每个 GitHub PR，模型能力继续向低门槛分发和研发流程内置两端延伸。
- 国内高信号集中在 Agent：Qwen3.8-Max 扩大预览访问，Qwen-CUA 用原生截图、键鼠完成计算机操作，Kimi K3 则公开更多长任务训练细节。
- 本周没有发现落在窗口内且达到入选标准的芯片新品或国内正式政策文件；宁缺毋滥，不沿用窗口外新闻。

## 全球动态

### Claude Code 将自动授权模式设为默认

主题类别：Agent 与开发工具 / 安全

发生了什么：Anthropic 8 月 7 日宣布，从 8 月 14 日起，Claude Code 的 Pro、Max 和 Team 新会话默认使用 auto mode；其分类器逐次审查工具调用，分类器开销不再向这些套餐计费，官方受控实验称其拦截了 89% 的危险命令，而人工审查仅拦截 13.6%。

为什么重要：Agent 的权限设计开始用“自动执行加策略拦截”替代高频人工确认，但这些结果来自厂商测试，生产环境仍需保留最小权限、隔离环境和高风险操作复核。

### Claude Code 开放企业自托管执行环境

主题类别：Agent 与开发工具 / 企业基础设施

发生了什么：Anthropic 8 月 6 日发布 self-hosted environments 公测，Team 和 Enterprise 客户可把 Claude Code 会话运行在自有网络与计算资源中，让代码、构建产物和文件留在企业基础设施内；提示、响应和工具结果仍会发送给 Anthropic 推理。

为什么重要：这降低了 Agent 访问内网服务、私有仓库和定制工具链的集成成本，但也把 runner 镜像、调度、隔离和持续运维责任交给企业平台团队。

### Claude Enterprise 增加推理链路实时 DLP

主题类别：安全 / 企业治理

发生了什么：Anthropic 8 月 5 日推出 inference hooks 测试版，将聊天、Claude Code、Cowork、MCP、Skills 和 Plugins 的提示与工具返回先发送到企业控制的安全服务器，由其同步决定允许或拒绝。

为什么重要：企业可以把既有数据防泄漏规则放到模型调用的统一入口执行，Agent 治理由产品侧配置升级为可审计、可集中控制的基础设施能力。

### Millennium 与 Anthropic 共建数字风险分析员

主题类别：应用落地 / 金融

发生了什么：Anthropic 8 月 6 日披露，正与另类资产管理机构 Millennium 共建数字风险分析员，用企业专有数据解释跨资产风险变化、保留长期信息，并通过沙箱、日志和人工审批约束输出。

为什么重要：这是高风险知识工作从通用助手走向领域 Agent 的清晰案例，价值不只来自模型推理，还取决于私有数据接入、可追溯过程和专家最终负责。

### OpenAI 扩大 Luna 免费访问并更新 Sol

主题类别：模型与应用 / 商业化

发生了什么：OpenAI 8 月 6 日宣布向免费用户提供不限次数的 GPT-5.6 Luna 文本对话，并更新面向付费用户的 GPT-5.6 Sol；Axios 同日确认，Luna 将成为更广泛用户的默认模型，Sol 则面向日常复杂任务优化。

为什么重要：前沿模型竞争继续从单次发布转向分层分发，免费层承担规模与入口，付费层通过更强能力和任务完成率实现差异化。

### Codex 安全审查进入每个 GitHub PR

主题类别：Agent 与开发工具 / 软件安全

发生了什么：OpenAI 8 月 6 日宣布 Codex 可对每个 GitHub Pull Request 自动执行安全审查并留下行级发现；配套的 Codex Security 会构建仓库威胁模型、在隔离环境验证漏洞，并给出供人工审核的最小修复补丁。

为什么重要：安全扫描正从规则和签名扩展到基于代码上下文的 Agent 验证，潜在收益是减少误报并缩短修复闭环，但团队仍需验证覆盖率、隔离强度和补丁回归风险。

## 国内动态

### Qwen3.8-Max 扩大预览访问，开放权重进入倒计时

主题类别：模型与研究 / 开源生态

发生了什么：通义千问 8 月 3 日正式介绍 Qwen3.8-Max，并将 `qwen3.8-max-preview` 纳入 QwenCloud Token Plan；官方文档显示其支持 100 万 token 上下文、推理、函数调用和内置工具，同时预告 Qwen3.8-Max 与 27B 版本的开放权重将在下一周发布。

为什么重要：阿里把旗舰模型、长上下文和 Agent 工具调用放进统一开发套餐，但开放权重尚未实际落地，本期不把预告等同于已开源。

### Qwen-CUA 公开原生计算机操作技术报告

主题类别：Agent 与开发工具 / 模型研究

发生了什么：Qwen 团队 8 月 3 日提交 Qwen-CUA 技术报告，397B-A17B 模型只依赖截图并通过键盘、鼠标操作软件，不使用 DOM 或无障碍树；团队称训练使用约 4 万个可验证任务和大规模并发环境，Qwen-CUA-Max 扩展到万亿参数以上。

为什么重要：计算机操作 Agent 正从浏览器专用接口转向跨软件的视觉原生控制，真实落地的关键将是长任务可靠性、操作延迟、权限边界和对界面变化的鲁棒性；论文指标尚未由本报告独立复现。

### Kimi K3 更新技术报告，披露长任务训练与系统协同

主题类别：模型与研究 / Agent

发生了什么：月之暗面 8 月 7 日更新 Kimi K3 技术报告，进一步披露 2.8 万亿总参数、1040 亿激活参数、原生视觉和 100 万 token 上下文，以及 Kimi Delta Attention、Stable LatentMoE、百万 token Agent 强化学习和持久化沙箱状态等设计。

为什么重要：超长上下文的竞争正在从窗口数字转向训练、推理和 Agent 状态管理的系统协同；Kimi K3 权重已在上一周期发布，本周事件是技术信息增量，不重复计作模型首发。

## 趋势与影响

- 事实：Anthropic 同周发布默认自动授权、自托管执行和实时 DLP；判断：企业 Agent 平台的最小完备集正在形成，即执行环境、权限决策、数据控制和审计闭环。
- 事实：Qwen-CUA 和 Kimi K3 都强调长时任务、环境交互与状态保留；判断：下一阶段模型评测需要从静态问答转向真实软件环境中的连续成功率、恢复能力和总成本。
- 事实：OpenAI 同时扩大免费模型覆盖并把安全 Agent 植入 PR；判断：模型厂商正在用“低门槛入口 + 高价值工作流”建立分层商业化，而非只依靠 API token 售卖。

## 下周观察

- Claude Code auto mode 在 8 月 14 日成为默认后，真实用户是否出现误拦截、权限绕过或新的提示注入案例。
- Qwen 是否按预告发布 Qwen3.8-Max 与 Qwen3.8-27B 权重，以及实际许可、部署需求和第三方评测结果。
- OpenAI 对下一代 Astra 的安全评估是否完成并转为正式发布；本期只有预告，因此未列入动态。

## 来源索引

### 全球

- [Auto mode is now the default in Claude Code for Pro, Max, and Team plans](https://claude.com/blog/auto-mode-default-in-claude-code)｜Anthropic｜2026-08-07
- [Boris Cherny：auto mode 与间接提示注入防护](https://x.com/bcherny/status/2085860677990883454)｜X / Anthropic 工程负责人｜2026-08-07
- [Run Claude Code sessions on your own compute](https://claude.com/blog/run-claude-code-sessions-on-your-own-compute)｜Anthropic｜2026-08-06
- [Inference hooks: inline data loss prevention for Claude Enterprise](https://claude.com/blog/claude-enterprise-inference-hooks)｜Anthropic｜2026-08-05
- [Millennium and Anthropic are building a digital risk analyst with Claude](https://claude.com/blog/millennium-and-anthropic-are-building-a-digital-risk-analyst-with-claude)｜Anthropic｜2026-08-06
- [OpenAI：Luna 免费访问与 Sol 更新](https://x.com/OpenAI/status/2085434712429052386)｜OpenAI / X｜2026-08-06
- [OpenAI expands free ChatGPT access to latest model](https://www.axios.com/2026/08/06/openai-chatgpt-upgrades-luna-free-paid)｜Axios，二手交叉验证｜2026-08-06
- [OpenAI Developers：Codex 自动审查 GitHub PR](https://x.com/OpenAIDevs/status/2085482310636560830)｜OpenAI / X｜2026-08-06
- [Codex Security](https://help.openai.com/en/articles/20001107)｜OpenAI Help Center｜访问于 2026-08-10

### 国内

- [Qwen：Meet Qwen3.8-Max](https://x.com/Alibaba_Qwen/status/2084100707423289643)｜通义千问 / X｜2026-08-03
- [Text generation models](https://docs.qwencloud.com/developer-guides/getting-started/text-generation-models)｜QwenCloud 官方文档｜访问于 2026-08-10
- [Qwen Token Plan](https://docs.qwencloud.com/token-plan/overview)｜QwenCloud 官方文档｜访问于 2026-08-10
- [Qwen-CUA: Native Computer Use for (almost) Everything](https://arxiv.org/abs/2608.02352)｜Qwen 团队 / arXiv｜2026-08-03
- [Kimi K3: Open Frontier Intelligence](https://arxiv.org/abs/2607.24653)｜Kimi Team / arXiv v2｜2026-08-07
- [Kimi K3 模型卡](https://huggingface.co/moonshotai/Kimi-K3)｜月之暗面 / Hugging Face｜访问于 2026-08-10

## 采集说明

- 去重前登记候选 56 条：X List 34 条，官方博客、产品公告、开发文档、论文与可信媒体 22 条；按事件合并后最终入选全球 6 条、国内 3 条。
- X API 使用官方 `GET /2/lists/2068180761916977611/tweets` 接口，共读取 2 页、扫描 36 条帖子，34 条落入窗口；单页上限 20 条，因到达窗口起点停止。
- 本次发现上期状态边界晚于本期窗口起点，已安全忽略该异常边界并按时间窗口重新抓取；状态只推进到本期窗口结束前最新帖子，避免后续漏抓。
- 数据缺口：X List 本期 6 个账号有活动，但内容明显偏 Anthropic 与 OpenAI；国内一手源在窗口内较少，最终只保留 3 个可核实高信号事件。未发现符合窗口和质量要求的芯片新品、国内正式政策或监管文件。
- 厂商基准、事故拦截率与生产效率数据均按原始披露转述，未由本报告独立复现；预告但尚未发布的 Astra 与 Qwen 开放权重仅列入下周观察或事件补充，不计作已发布成果。
