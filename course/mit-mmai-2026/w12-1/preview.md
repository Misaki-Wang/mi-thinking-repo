# W12.1 · Prescriptive modeling

2026-04-21 · Dimitris Bertsimas / Lisa Everest / Vasiliki Stoumpou · 约 3 分钟预览

## 来源与阅读范围

依据已核对的 25 页[**Prescriptive Neural Networks** 讲义](https://mit-mi.github.io/mmai-course/spring2026/schedule/lec12.1%20-%20prescriptive.pdf)整理。课程表没有视频链接，频道匹配未找到本节录像。页码均为 PDF 页码，比讲义内印刷编号大 1。

## 先抓住主线

Predictive modeling 估计结果；**Prescriptive modeling** 要选择能够改善结果的行动。讲义中的核心难点是：每个样本只接受过一种 treatment，我们没有直接观察它接受其他 treatment 的结果。PNN 先构造各候选行动的 counterfactual outcome estimate，再训练一个 policy，让它在这个估计矩阵上的平均结果更好。因此，神经网络只是整条链路的一环；counterfactual estimation 的可靠性决定下游优化究竟在追逐什么。

## 六个关键点

1. **把输入、行动、结果分开。** `x` 可以含 tabular data、notes、images、time series；`t` 是可选 treatment；`y` 是要最小化或最大化的 outcome。标签分类准确率并不是最终的 policy objective。
2. **四阶段 framework。** 讲义顺序为 embedding extraction → counterfactual estimation → PNN training → mirrored Optimal Classification Tree（OCT）。图像与文本 embedding 用于承载非结构化信息，不能自动把观测研究变成随机试验。
3. **Γ 是估计矩阵。** `Γ[i,t]` 表示样本 i 在 treatment t 下的估计 outcome。Direct method 用 outcome regression；讲义还引入 propensity score 与 doubly robust estimation 的思路。矩阵中填满数字，只意味着模型做了估计，并非所有 treatment 结果都被观察到了。
4. **用 softmax 松弛选择问题。** 以最小化为例，训练目标可写为 `L = mean_i Σ_t pθ(t|xi) Γ[i,t]`。这使离散 prescription 的优化可微。阅读时区分训练用概率分布与部署时如何选取最终行动；讲义的连续 treatment 案例不等于这一个离散公式已经解释所有实现细节。
5. **Mirrored OCT 学的是 PNN 的处方。** 它以原始 features 为输入、PNN prescriptions 为目标类别，形成更容易检查的近似 policy。这是行为蒸馏，不是对黑箱内部机制的完整解释；应同时检查 agreement 和 policy outcome。
6. **结果依赖评价条件。** 讲义报告多次随机 50%/50% train/test split，并列出不同 counterfactual estimator、输入类型和模型类别。比较时必须保留这些条件，不能把 TAVR、创伤、血糖管理和商品定价的 improvement 混为一项“PNN 效果”。

## 原文导航

- [pp3–6：问题定义与四阶段流程](https://mit-mi.github.io/mmai-course/spring2026/schedule/lec12.1%20-%20prescriptive.pdf#page=3)
- [pp8–10：反事实缺口与 Γ](https://mit-mi.github.io/mmai-course/spring2026/schedule/lec12.1%20-%20prescriptive.pdf#page=8)
- [pp12–16：policy objective、softmax、Mirrored OCT](https://mit-mi.github.io/mmai-course/spring2026/schedule/lec12.1%20-%20prescriptive.pdf#page=12)
- [pp17–23：评价设计与多个应用案例](https://mit-mi.github.io/mmai-course/spring2026/schedule/lec12.1%20-%20prescriptive.pdf#page=17)

## 易混点与边界

这里是机器学习方法学习笔记，不提供个人 treatment 建议。需要追问的因果识别条件包括 confounding、overlap 和数据生成过程；讲义并没有在这 25 页中完整证明这些条件成立。较低的 estimated policy loss 不足以证明真实 intervention 有效。把复杂 policy 转成树也不能修复最初 counterfactual estimate 的偏差。

复述时要能解释为什么它看上去像分类网络，却不是在拟合历史动作标签：输出层仍然给各行动一个概率，但优化目标由估计结果加权决定。若原有行动选择偏向某类样本，直接模仿原标签可能复制这种选择，未必实现目标结果的改善。

## 自测与小练习

手写一个 3 个样本、2 个行动的 Γ 矩阵，分别计算 uniform policy、argmin policy 和一组 softmax probabilities 的 objective。再故意把一个未观察 treatment 的估计改错，观察最优推荐如何翻转。最后写出两个必须与最终 policy 测试集隔离的模型训练环节，并比较“模仿历史医生的动作”与“优化估计结果”的差别。

接着看[阅读与复习 guidance](readings.md)。
