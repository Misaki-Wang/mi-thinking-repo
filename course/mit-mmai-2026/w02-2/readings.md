# W02-2 · Reading guidance：架构如何编码数据结构

这六篇 Reading 可以围绕同一个问题阅读：**哪些信息交换应该被允许，哪些对称性应该被保留？** 本次核对了六篇作者原始 arXiv 摘要与题录；没有逐页审核全文。下面对方法主旨的陈述由摘要支持，正文定位以“找什么”为主，不虚构页码或小节编号。P1/P2 是个人学习建议。

## P1 · Geometric Deep Learning: Grids, Groups, Graphs, Geodesics, and Gauges

[论文](https://arxiv.org/abs/2104.13478) · 证据：primary abstract。

带着问题读：现实任务为什么不需要学习任意高维函数？摘要强调 representation learning 与 gradient-based learning 两个原则，并用物理世界的低维规律与结构解释架构先验。先找 symmetry、invariance、equivariance 的概念，再阅读与你的数据对应的 grid、sequence、set 或 graph 示例。

提取与检查：用 `f(Tx)=f(x)` 和 `f(Tx)=T′f(x)` 写出两种约束；说明哪一种适合分类、哪一种适合分割。记录这种先验节省的学习负担，以及错误先验可能丢掉的任务信息。这篇提供地图，后五篇是可对照的具体实例。

## P1 · Deep Sets

[论文](https://arxiv.org/abs/1703.06114) · 证据：primary abstract。

带着问题读：为什么 set prediction 应与输入排列无关？摘要明确研究 permutation-invariant objectives，并给出相关函数结构和 permutation equivariance 条件。结合 [Slides p37–39](https://mit-mi.github.io/mmai-course/spring2026/schedule/lec2.2%20-%20heterogeneity.pdf#page=37)，追踪共享 `φ` 与对称 aggregation 各自的作用。

提取与检查：手算 `ρ(Σᵢφ(xᵢ))` 在两种排列下的输出；再分别取消参数共享、改用有序 concat。阅读全文时检查主定理的输入域和函数条件，不要将一句“sum 可以表示一切”无限推广到所有连续集合与维度设置。交付一个 permutation test。

## P1 · Attention Is All You Need

[论文](https://arxiv.org/abs/1706.03762) · 证据：primary abstract。

带着问题读：去掉 recurrence 和 convolution 后，sequence transduction 如何交换信息？摘要将 Transformer 描述为基于 attention 的架构，并强调并行性。进入正文后优先追踪 Q/K/V、scaled dot-product attention、multi-head attention、positional information、encoder/decoder mask；这些具体定位是阅读任务，不能只凭摘要完成。

提取与检查：标出一个 self-attention 层的输入输出 shape，解释 causal mask 阻断了哪些连接。再问：没有 position information 的 attention 为什么不能区分任意排列造成的语义变化？把并行训练与 autoregressive generation 的逐步输出区分开。

## P2 · Neural Machine Translation by Jointly Learning to Align and Translate

[论文](https://arxiv.org/abs/1409.0473) · 证据：primary abstract。

带着问题读：将整句压缩成固定长度向量为什么会形成 bottleneck？摘要提出在生成目标词时 soft-search 相关源句部分，避免预先做 hard segmentation。优先找 decoder 每一步如何构造 context，以及 alignment weights 如何参与端到端训练。

提取与检查：画出一个目标词依赖哪些源词，而不是只画 encoder→decoder 的一条箭头。与 Transformer 对比：两者都有 attention，但这篇的核心改进不是去掉所有 recurrence。不要把“出现可解释的 soft alignment”直接提升为因果解释。

## P2 · An Image is Worth 16x16 Words: Transformers for Image Recognition at Scale

[论文](https://arxiv.org/abs/2010.11929) · 证据：primary abstract。

带着问题读：怎样把 image 变成 Transformer 可以处理的元素序列？摘要确认方法直接使用 image patches，并强调 large-scale pre-training 与 transfer 的条件。正文优先检查 patch embedding、position representation、classification readout，以及训练数据规模改变后与 CNN 的比较。

提取与检查：为一个固定分辨率图像计算 patch 数量，并推导减半 patch 边长如何影响 attention matrix 的大小。比较时同时记录训练数据与计算预算，避免从一个规模条件下的结果推出“ViT 总优于 CNN”。

## P2 · Graph Attention Networks

[论文](https://arxiv.org/abs/1710.10903) · 证据：primary abstract。

带着问题读：如果节点只应访问 graph neighborhood，如何让不同邻居有不同权重？摘要描述 masked self-attentional layers，让每个 node 对邻居特征加权，并覆盖 inductive 与 transductive settings。优先在正文找到 neighborhood mask、attention coefficient 和多层信息传播。

提取与检查：对一个四节点 graph 写下每个节点能接收哪些消息，再打乱节点编号检查输出如何对应。Inductive 是面对未见 graph 或 node 的泛化设定，不是“不需要输入 graph 结构”；阅读时务必写明训练与测试能看见哪些节点和边。

## 横向比较与交付

| 方法 | 核心检查问题 |
| --- | --- |
| Deep Sets | 共享 encoder 与对称聚合是否保证 set-level invariance？ |
| Bahdanau attention | 目标端状态如何选择源序列的相关部分？ |
| Transformer / ViT | 全局交换信息后，顺序或空间信息来自哪里？ |
| GAT | 邻接约束和内容权重分别由什么决定？ |

交付一页 architecture card：元素、允许的邻域、共享参数、aggregation、期望 invariance/equivariance、训练/测试设定。为自己的数据选两种候选架构，明确一种交换顺序或改变邻域的测试，并说明测试通过与失败各意味着什么。[返回 preview](preview.md)
