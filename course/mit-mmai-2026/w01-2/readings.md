# W01-2 · Reading guidance：从数据与结构出发选题

本节的四项 Reading 不需要都从第一页读到最后。建议先确定一个研究任务，再分别用它们检查问题设定、representation、multimodal challenges 和结构先验。P1/P2/P3 仅为本归档的学习建议，课程表没有为这些条目逐一标记优先级。

## P2 · Machine learning: Trends, Perspectives, and Prospects

[Science 原文入口](https://www.science.org/doi/abs/10.1126/science.aaa8415) · 证据：publisher-registered abstract；出版商全文未审阅。

带着问题读：你希望系统通过哪一种 experience 改善哪一项行为？已核验摘要把 machine learning 定位在计算机科学与统计学交叉处，并将进展同时联系到算法/理论、数据和计算资源。优先读对学习问题与应用边界的整体讨论，不把它当成当前模型排行榜。

提取与检查：给自己的任务分别列出 data、learning algorithm、evaluation 三个要素；找出“增加数据”与“改变方法”可能被混淆的地方。该文提供历史性全景，关于今日产品或模型能力的结论需要另外验证。

## P2 · Representation Learning: A Review and New Perspectives

[论文](https://arxiv.org/abs/1206.5538) · 证据：primary abstract，未逐页审阅全文。

本周换一个问题读：数据集中的哪些因素是真正任务信号，哪些只是采集条件？摘要强调 representation 会纠缠或隐藏 explanatory factors，并综述 auto-encoders、probabilistic models、manifold learning 等路线。优先寻找目标函数和先验如何控制这些因素的讨论。

提取与检查：为 10 个样本记录内容因素、背景因素和标签，提出一个 representation 应当保留的因素与一个应当抑制的捷径。不要仅凭 embedding 可视化中“看起来分开”就认定泛化问题已解决。

## P1 · Foundations and Trends in Multimodal Machine Learning: Principles, Challenges, and Open Questions

[论文](https://arxiv.org/abs/2209.03430) · 证据：primary abstract，未逐页审阅全文。

带着问题读：你的数据集主要考查哪个 multimodal challenge？摘要明确六大挑战及三原则，因此可用它给课件中的任务分类：retrieval 首先检查对齐，generation 检查跨模态一致性，agent 任务还涉及推理与行动中的信息使用。这里的任务映射是本归档的组织方式，不是声称每项任务只有一种挑战。

提取与检查：选择两个候选数据集，写出 modalities、connections、interactions、label 和评估终点；再找每个数据集中一种可能让 unimodal shortcut 获得高分的机制。把这两个潜在捷径变成未来 baseline。

## P3 · Geometric Deep Learning: Grids, Groups, Graphs, Geodesics, and Gauges

[论文](https://arxiv.org/abs/2104.13478) · 证据：primary abstract，未逐页审阅全文。

带着问题读：哪些数据变化不应改变标签，哪些变化应使输出同步变化？摘要的核心是通过几何规律统一 CNN、RNN、GNN、Transformer，并将先验结构纳入 architecture。第一次阅读先找 symmetry、invariance、equivariance 的基本概念，以及与你的数据最接近的一类结构，不必立刻展开所有群论细节。

提取与检查：为集合乱序、图像平移、时间偏移各写出一个输入变换与预期输出。验证“分类不变”和“分割等变”不是同一个约束。下一节 [W02-2](../w02-2/preview.md) 会把这个问题接到具体模型。

## 读后比较与交付

Science 全景提醒你数据、算力与方法共同作用；representation review 提醒你观察会被编码方式改变；multimodal survey 给出任务地图；geometric view 让结构先验进入架构选择。四者一起约束选题，避免从“我想用 Transformer”直接跳到实验。

交付一页项目草案：明确的 research question、可被否定的 hypothesis、两种候选数据集比较、一个简单 baseline、一种数据结构先验，以及一种可能污染评价的划分方式。每个判断标明来自论文摘要、课件还是自己的假设。[返回预览](preview.md)
