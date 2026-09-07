# W14.1 · Readings guidance

覆盖[课程表](https://mit-mi.github.io/mmai-course/spring2026/schedule/)全部 3 项。优先级由本学习仓库建议。Blog 已核对作者页面的概念段落；两篇论文已核对原始元数据及 abstract，未声称完成全文或代码审计。

## 1. Blog Post on Self-Evolving AI · 优先

[作者博客：The Compounding Loop](https://quao627.github.io/blog/self-evolving-agents/)

**来源说明：** 课程表用 “Blog Post on Self-Evolving AI” 作描述性标签，页面实际标题为 The Compounding Loop；这属于标签差异，不是指向另一主题的错误链接。

**为什么读：** 它把 model、harness、context、environment 拆开，并要求同时描述 evolving target 与 evolver。尤其有用的区分是：运行前固定的 prompt / code 属于 harness，当前运行中不断积累的 history / memory 属于 context。

**检查与提取：** 从 foundations 和 classification 段开始，给 AlphaEvolve、memory-writing agent、reward-design agent 分别标注改变对象。检查作者如何定义 grounding、retention 和长程改进的条件，并区分分类框架与已经得到实验验证的结论。

**输出：** 自己项目的一张四组件图：哪一项会改变，谁修改它，哪种反馈决定保留。证据状态：primary author page excerpt；本页只归纳已核对段落，不把整篇博客视为所有方法的实验依据。

## 2. AlphaEvolve · 优先

[AlphaEvolve: A Coding Agent for Scientific and Algorithmic Discovery](https://arxiv.org/abs/2506.13131)

**为什么读：** Abstract 描述由 LLM 修改候选代码、一个或多个 evaluators 持续反馈的 evolutionary coding pipeline。这是理解 solution evolution 的具体例子。

**检查与提取：** Candidate program、population / database、proposal 和 evaluator 各如何连接？Correctness 和 performance 是否分开验证？评估器对数学问题与系统优化问题是否不同？哪些模块固定，哪些对象发生变化？

**输出：** 画一轮 evolution，并追踪一个失败候选是否还提供有用知识。与普通 independent sampling 比较 evaluation budget。Abstract 中的矩阵乘法结果有 **4×4 complex-valued matrices** 等限定，不能去掉限定改写为推翻所有矩阵乘法结果。

证据状态：primary abstract + 本节视频 66:50–72:23；具体搜索策略和所有应用数值待全文核实。

## 3. CORAL · 核心

[CORAL: Towards Autonomous Multi-Agent Evolution for Open-Ended Discovery](https://arxiv.org/abs/2604.01658)

**为什么读：** Abstract 将 long-running agents、shared persistent memory、asynchronous execution、heartbeat interventions 作为框架组成，也明确提到 isolated workspaces、evaluator separation 和 resource management。

**检查与提取：** 什么触发 intervention？不同 agent 如何分享可复用发现，而不是复制冗余尝试？哪些 ablation 能区分多 agent 并行、更多计算、共享记忆和更高自主程度的贡献？Evaluator 与被优化产物如何隔离？

**输出：** 一张协作轨迹表，记录每个 agent 的尝试、发现、读到的他人证据以及后续改变。比较 matched compute / matched evaluations，而不只比较 wall-clock 或 best score。证据状态：primary abstract + slides pp61–63 / video 73:17 起；未对正文中机制分析作独立验证。

## 统一交付

把三份材料压缩成一页 **evolution specification**：目标、可变对象、冻结对象、proposal mechanism、feedback source、保存策略、预算、停止条件。能明确说出“改进发生在哪里”和“什么证据允许保留它”，比把所有自动迭代都称为 self-learning 更有用。
