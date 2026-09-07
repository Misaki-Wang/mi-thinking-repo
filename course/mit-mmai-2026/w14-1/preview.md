# W14.1 · Self-evolving AI

2026-05-05 · Paul Liang · 约 3 分钟预览

## 来源与阅读范围

已核对 64 页[**Advanced Topics** 讲义](https://mit-mi.github.io/mmai-course/spring2026/schedule/lec14.1%20-%20advanced%20topics.pdf)，并对照[视频](https://www.youtube.com/watch?v=FhcHTSjvuKk)英文自动字幕。实际范围包含课程回顾、native multimodal models、MoE、fusion optimization，最后进入 self-evolving agents；不能仅凭课程表标题把整节当成 continual learning 专讲。

## 先抓住主线

这节把“更强的 multimodal model”与“能持续改善的 agent system”连接起来。前半部分讨论表示与优化：多模态从何时一起训练、专家共享什么、如何避免某一模态主导。后半部分讨论 **self-evolution**：系统产生候选、通过 evaluator 获得信号、保存试验、据此选择下一步。理解每种方法，首先需要说清**究竟什么在改变**——candidate solution、harness、context，还是 model weights。

## 七个关键点

1. **核心定义仍是 heterogeneous、connected、interacting。** Representation、alignment、reasoning、generation、transference、quantification 是六类互相关联的挑战。把感知输入拼在一起，尚未说明学到了 redundancy、unique information 或 synergy。
2. **Native multimodal training 与 architecture 需要分开描述。** 从一开始联合训练多模态，和先训练 LLM 再接 adapter，是训练路径的区别；有无 image encoder 是另一项设计选择。讲义中的 early / late fusion 用于当前比较，不应无条件套用到所有论文的术语。
3. **Mixture of Experts（MoE）有不同的 specialization 单位。** 有的按 token route 到稀疏 experts，有的按 redundant / unique / synergistic interaction 组织专家。不能把“模态专属专家在一个实验中较差”推成“任何专家分工都无效”。
4. **Multimodal training 会出现不均衡。** 不同模态以不同速度 generalize / overfit，易学模态可能成为 shortcut。讲义介绍 overfitting-to-generalization ratio（OGR）与 reweighting；视频补充同时训练 unimodal reference models 会增加成本，扩展性需另行考虑。
5. **AlphaEvolve 的演化对象是候选程序。** 模型根据任务、历史候选及 evaluator feedback 修改代码，数据库保留效果证据。视频 71:27 明确此类例子中基础 model weights 固定；程序越来越好不等于模型参数在每轮训练。
6. **Test-time training 是另一条路线。** 讲义提及 TTT-Discover / ThetaEvolve，将 improvement score 用作参数更新信号。必须区分搜索带来的改进与 weight update 带来的改进，并核对额外计算和评价数据使用。
7. **CORAL 关注协作过程如何延续。** Specialized agents、shared persistent memory、asynchronous work 与 heartbeat interventions 支持持续探索。日志不仅存最终解，也存失败尝试和可复用发现；多 agent 数量本身不是效果保证，关键是信息是否被后续搜索利用。

## Slides × video 导航

| 主题 | Slides（PDF 页码） | 视频定位 |
| --- | --- | --- |
| 本节结构与课程回顾 | [pp3–23](https://mit-mi.github.io/mmai-course/spring2026/schedule/lec14.1%20-%20advanced%20topics.pdf#page=3) | [08:02](https://www.youtube.com/watch?v=FhcHTSjvuKk&t=482s) |
| Native multimodal 与 MoE | [pp24–35](https://mit-mi.github.io/mmai-course/spring2026/schedule/lec14.1%20-%20advanced%20topics.pdf#page=24) | [28:10](https://www.youtube.com/watch?v=FhcHTSjvuKk&t=1690s)、[42:00](https://www.youtube.com/watch?v=FhcHTSjvuKk&t=2520s) |
| 模态训练不均衡与代价 | [pp40–44](https://mit-mi.github.io/mmai-course/spring2026/schedule/lec14.1%20-%20advanced%20topics.pdf#page=40) | [54:55](https://www.youtube.com/watch?v=FhcHTSjvuKk&t=3295s)、[56:48](https://www.youtube.com/watch?v=FhcHTSjvuKk&t=3408s) |
| Candidate / harness / weights 的区别 | [pp53–60](https://mit-mi.github.io/mmai-course/spring2026/schedule/lec14.1%20-%20advanced%20topics.pdf#page=53) | [66:50](https://www.youtube.com/watch?v=FhcHTSjvuKk&t=4010s)、[71:27](https://www.youtube.com/watch?v=FhcHTSjvuKk&t=4287s) |
| CORAL 与共享记忆 | [pp61–63](https://mit-mi.github.io/mmai-course/spring2026/schedule/lec14.1%20-%20advanced%20topics.pdf#page=61) | [73:17](https://www.youtube.com/watch?v=FhcHTSjvuKk&t=4397s) |

## 易混点与自测

一个不断刷新 best score 的曲线只说明已观察到的最佳候选改善，不证明系统对所有新任务持续变强。Evaluator 必须测量实际目标，且不能让候选通过修改评分逻辑“进步”。讲义中的规模和 SOTA 表述属于讲授时引用的材料，不作为当前模型推荐。

判断长期知识是否积累，可以检查后来的尝试有没有利用早先发现，以及重复犯错是否减少。只保存最优结果会丢掉失败条件；保存所有历史又可能淹没有用信息。因此记忆组织本身也是需要评价的设计选择，不能仅按文件数量判断。

练习：在纸上设计一个字符串处理函数优化任务：固定 correctness tests 和 runtime metric，记录 `candidate / change / score / failure / next hypothesis`。分别标出冻结模型搜索、修改 harness、更新 weights 三种方案允许修改的对象。提出一个会让分数变好却损害真实目标的 counterexample，并说明怎样发现它。

接着看[逐篇 Readings guidance](readings.md)。
