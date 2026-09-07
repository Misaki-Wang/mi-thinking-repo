# W10.1 · Readings guidance

以下覆盖[课程表](https://mit-mi.github.io/mmai-course/spring2026/schedule/)全部 7 项阅读。优先级是个人学习建议。已核实每篇的 arXiv 标题、作者元数据及 abstract；未将未读全文中的节号、算法细节或 ablation 结果写成已确认事实。下面的“检查”是阅读全文时的任务。

## 1. VisualWebArena · 优先

[VisualWebArena: Evaluating Multimodal Agents on Realistic Visual Web Tasks](https://arxiv.org/abs/2401.13649)

**为什么读：** 先建立本节 agent 成功的定义。Abstract 确认它关注需要视觉信息的真实风格网页任务，联合 image-text 输入与网站操作。

**带着问题检查：** 哪些任务真正不能靠 text alone 完成？Observation、action space、functional evaluator 如何定义？哪些失败是 grounding，哪些是 planning？把一个任务改成 text-only 后，任务含义是否改变？

**输出：** 一张 benchmark card，记录环境、输入、动作、成功判据、失败类别；与 Mind2Web 比较 evaluation unit。证据状态：primary abstract + 本节 slides，方法细节待全文核对。

## 2. OS-ATLAS · 核心

[OS-ATLAS: A Foundation Action Model for Generalist GUI Agents](https://arxiv.org/abs/2410.23218)

**为什么读：** 把“能看懂 screenshot”进一步拆为可迁移的 GUI grounding。Abstract 将 cross-platform data construction 与 action-model training 作为关键。

**带着问题检查：** GUI element supervision 如何获得？跨 web / desktop / mobile 的共同 action representation 是什么？OOD interface 与已见元素如何隔离？Grounding benchmark 的提升是否也带来端到端 task success？

**输出：** 画 screenshot → target localization → action 的接口，与 SoM representation 对照。证据状态：primary abstract；数据清洗、切分和训练配方待正文。

## 3. Mind2Web · 核心

[Mind2Web: Towards a Generalist Agent for the Web](https://arxiv.org/abs/2306.06070)

**为什么读：** 理解真实网站多样性与 generalization。Abstract 强调真实网站、crowdsourced action sequences，以及用小模型先筛选过长 HTML 的做法。

**带着问题检查：** Cross-task、cross-website、cross-domain 测试分别排除了什么捷径？标注 action sequence 与在可变环境中实际执行有什么区别？HTML filtering 丢掉关键信息时，下游 LLM 是否还有恢复机会？

**输出：** 与 VisualWebArena 并排填写 data collection / observation / evaluation 三项；不要直接比较不一致设置中的数字。证据状态：primary abstract。

## 4. Tree Search for Language Model Agents · 优先

[Tree Search for Language Model Agents](https://arxiv.org/abs/2407.01476)

**为什么读：** Abstract 明确提出在 actual environment space 中进行 best-first tree search，把规划与环境反馈连接起来。

**带着问题检查：** Node 存储什么状态？如何评估和恢复分支？Value estimate 的训练或提示来自哪里？与更多独立重试相比，search 的额外收益是否在相同预算下仍存在？

**输出：** 画一棵含成功、误操作、无进展分支的小树，记录 branching budget 与终止条件。证据状态：primary abstract + slides；不要把 abstract 中的 relative increase 写成百分点提升，也不要当成当前 SOTA。

## 5. A Survey of Reinforcement Learning from Human Feedback · 扩展

[A Survey of Reinforcement Learning from Human Feedback](https://arxiv.org/abs/2312.14925)

**为什么读：** 将课堂 human clarification 放进更广的 human feedback 图景。RLHF 从人类反馈学习，而不是仅依赖手工定义 reward；综述也覆盖 control / robotics。

**带着问题检查：** Feedback 是 preference、demonstration、correction 还是评价？反馈进入 reward learning 还是直接进入当前上下文？人类反馈的成本、偏差和不一致如何处理？

**输出：** 做 feedback taxonomy，并明确“一次提示澄清”不等于“已经对模型做 RLHF”。证据状态：primary abstract；当前已读元数据版本更新至 2025，不假定与最初课程引用版本逐字相同。

## 6. MEM1 · 优先

[MEM1: Learning to Synergize Memory and Reasoning for Efficient Long-Horizon Agents](https://arxiv.org/abs/2506.15841)

**为什么读：** 这是把 memory consolidation 纳入端到端 RL 的具体路线。Abstract 确认紧凑 internal state 每轮结合旧信息与新 observation，并丢弃冗余信息。

**带着问题检查：** State update 和 action 如何联合生成？Reward 是否只依赖 outcome？长任务由哪些现有任务组合而来？保持 context 大小与保留必要事实之间如何取舍？

**输出：** 跟踪一个两目标任务的每轮 state，标出删除什么、留下什么、为何足够。与 full-history 和普通 summarization baseline 比较。证据状态：primary abstract + slides + 视频 65:04–69:02；不把紧凑上下文当成所有外部 storage 都常数。

## 7. OpenVLA · 扩展

[OpenVLA: An Open-Source Vision-Language-Action Model](https://arxiv.org/abs/2406.09246)

**为什么读：** 将网页 action 扩展到 visuomotor control。Abstract 描述 vision-language backbone、robot demonstrations 和有效适配新任务的研究。

**带着问题检查：** Action 如何编码及解码？观察频率、robot embodiment、fine-tuning data 怎样影响迁移？视觉预训练与机器人 demonstration 各提供什么？Quantization 的结果在哪些任务与硬件条件下测得？

**输出：** 一张 web agent vs VLA 对照表：输入、动作、反馈时延、训练数据、evaluation。证据状态：primary abstract + slides；不能把具体机器人的成功率泛化到任意机器人。

## 读完后的统一交付

用一页图串起 **grounding → planning/search → memory → action → evaluation**。每个方法填入它改善的环节、需要的监督、适用预算和仍未解决的错误；它们多数是互补关系，而非一组能简单按总分排序的替代品。
