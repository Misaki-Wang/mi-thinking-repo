# W03-2 · Reading guidance：从人类交互检查融合假设

课程表为本节列了两篇 multimodal interaction 阅读，但链接 Slides 实际是 HAIM 医疗应用，详见 [preview 的来源说明](preview.md)。这里保留全部官方 Reading，不把 HAIM 论文自行替换为课程要求。两篇都没有取得并逐页审阅论文全文，阅读计划相应保留证据边界。P1/P2 是本归档建议。

## P1 · Ten Myths of Multimodal Interaction

[ACM 论文入口](https://dl.acm.org/doi/pdf/10.1145/319382.319398) · Sharon Oviatt。

证据：论文题名、作者及 DOI 已通过出版商登记元数据核对；另取得[作者同主题 1999 年演讲的摘要](https://hci.stanford.edu/courses/cs547/abstracts/98-99/990226-oviatt.html)。**演讲摘要是补充背景，不等于已读论文全文，也不能据此重建“十条 myths”的完整清单。**

带着问题读：用户什么时候会同时使用多个输入模式，什么时候不会？已读作者演讲摘要关注 interactive maps 中说话与书写的组合、输入如何同步、不同模式携带什么内容，以及不同用户是否采用一致策略。因此可先围绕这些问题阅读论文的 empirical evidence，而不预设人类永远偏爱多模态输入。

提取与检查：从全文亲自选择两条 myth，分别记录原始假设、反例、实验任务和适用用户群。特别检查“多个输入同时发生”“携带冗余信息”“所有人采用相同策略”是否真的在实验中成立。此处是待核对的问题，不声称它们逐字对应文中的某条编号。

与课程联系：HAIM 汇集多类临床记录，而交互系统关心用户如何主动组合输入；两者的采集机制不同。可借此问：系统应要求每个样本都有所有模态，还是接受缺失与异步输入？这属于本归档的跨材料思考题。

## P2 · Multimodal interaction: A review

[出版商原文入口](https://www.sciencedirect.com/science/article/pii/S0167865513002584) · Matthew Turk。

证据：Crossref 核对题录，出版商摘要已核验；正文未审阅。摘要概述 multimodal HCI 的历史、机会与挑战，讨论人类同时或顺序使用多种感知渠道，以及移动设备和传感器带来的新交互条件；它也将 early/late integration 与生物感知整合联系起来。

带着问题读：一个 integration scheme 应根据哪些用户行为与时间条件选择？优先寻找 early integration、late integration、同步/顺序使用、robustness 和实际交互问题的讨论。由于没有全文证据，这里不提供猜测的小节号，也不引用未核对的实验数值。

提取与检查：用同一任务比较三种输入设定：仅语音、仅指向、语音＋指向。明确成功指标究竟是识别 accuracy、完成时间、纠错次数，还是用户负担；检验系统是否因某一通道故障而放大错误。

## 比较与短交付

Oviatt 帮你质疑关于用户 multimodal behavior 的假设，Turk 提供 integration 与 HCI 的更广视角。二者都提醒我们，模型性能只是系统评价的一部分；但它们不能单独证明现代大模型如何学习信息论意义上的 synergy，后者应接到 [W04-1 Readings](../w04-1/readings.md)。

交付一页交互设计说明：一个具体任务、用户可能使用的两个通道、输入何时发生、early/late integration 的选择理由、一个失效场景，以及一个同时测量模型错误与用户成本的小实验。将尚未核对的 paper claims 保留为待办，而不是写成事实。
