# W04-1 · More multimodal fusion：联合输入到底增加了什么

本节用一个可解释的回归例子，把 additive fusion、multiplicative interaction、tensor fusion、low-rank fusion 和 gated fusion 连起来。预习时最重要的区分是：模型能够表达复杂交互，不代表训练后真的依赖这些交互。

整理依据为 Slides 与公开视频的英文自动字幕，时间链接定位到相关片段起点。视频/Slides 的进度差异在 EMAP 段落注明；手算推导与 toy experiment 是学习练习。

## 七个核心概念

1. **Fusion 的目标是联合表示中的任务信息。** Raw modalities 的差异大，可以先用各自 encoder 得到较抽象的特征。Early fusion 在预测前组合输入，late fusion 组合各自预测，intermediate fusion 介于其间；“early/late”描述组合位置，不直接规定函数是否线性。[Slides p4–9](https://mit-mi.github.io/mmai-course/spring2026/schedule/lec4.1%20-%20more%20fusion.pdf#page=4)

2. **Additive fusion 允许不同偏置，却不让一种模态改变另一种的效应。** 课堂例子用微笑比例 `xA` 与是否专业评论者 `xB` 预测评分。纯 additive 模型下，两类人的“微笑—评分”直线平行；差别只来自截距。它是解释融合收益时不可缺少的 baseline。[Slides p10–13](https://mit-mi.github.io/mmai-course/spring2026/schedule/lec4.1%20-%20more%20fusion.pdf#page=10) · [视频 14:01](https://www.youtube.com/watch?v=0SOieOIe4HI&t=841s)

3. **Multiplicative interaction 让条件关系改变。** 加入 `w3·xA·xB` 后，评论者身份会改变微笑的斜率。视频用直线旋转解释这个变化：现在不只是两种证据各加一票，而是 B 改变 A 应如何被理解。[Slides p14–17](https://mit-mi.github.io/mmai-course/spring2026/schedule/lec4.1%20-%20more%20fusion.pdf#page=14) · [视频 15:54](https://www.youtube.com/watch?v=0SOieOIe4HI&t=954s)

4. **Tensor fusion 一次容纳不同阶数的项。** 先给每个特征向量补常数 1，再做 outer product，就同时出现 bias、unimodal、bimodal 以及更高阶项。视频强调补 1 的作用；不补这个常数，就会只保留相应的乘积组合。维度随各模态维度的乘积增长，后续投影权重也会变大。[Slides p18](https://mit-mi.github.io/mmai-course/spring2026/schedule/lec4.1%20-%20more%20fusion.pdf#page=18) · [视频 21:28](https://www.youtube.com/watch?v=0SOieOIe4HI&t=1288s)

5. **Low-rank fusion 通过重排计算减少显式大张量。** 将融合权重写为少量低秩因子的和，再先对各模态投影、做逐元素乘积与求和，可以避免真的构造完整 outer-product tensor。Rank 控制表达能力和资源开销；它与 LoRA 共享低秩思想，但不是同一个训练设置。[Slides p19–22](https://mit-mi.github.io/mmai-course/spring2026/schedule/lec4.1%20-%20more%20fusion.pdf#page=19) · [视频 25:12](https://www.youtube.com/watch?v=0SOieOIe4HI&t=1512s)

6. **Gating 让权重随当前输入变化。** `z = gA(xA,xB)·xA + gB(xA,xB)·xB` 中 gate 本身依赖数据，因此形式上相加也可以存在非加性交互。Soft gate 可直接优化，hard gate 的离散选择更难处理。Modality-shifting fusion 则用语气或表情调整“wow”等歧义词的表示。[Slides p23–25](https://mit-mi.github.io/mmai-course/spring2026/schedule/lec4.1%20-%20more%20fusion.pdf#page=23) · [视频 30:16](https://www.youtube.com/watch?v=0SOieOIe4HI&t=1816s)

7. **EMAP 检查复杂模型中有多少性能可由加性函数解释。** 思路是将已训练的 `f(A,B)` 投影到最接近的 additive function，再比较任务表现。若差异很小，就不能把总成绩归因于复杂交互。这部分在本节 Slides p26–29，但本节视频讲到 modality shifting 后结束，讲解实际续在 W04-2 前半段。[Slides p26–29](https://mit-mi.github.io/mmai-course/spring2026/schedule/lec4.1%20-%20more%20fusion.pdf#page=26) · [下一节视频 13:56](https://www.youtube.com/watch?v=u-H43tRgYJg&t=836s)

## 手算机制

`ŷ = w0 + w1·xA + w2·xB + w3·xA·xB`。

当 `xB=0`，斜率是 `w1`；当 `xB=1`，斜率是 `w1+w3`。因此 `w3` 描述条件关系变化。注意这是对输入特征非线性、对待估参数线性的回归模型。Tensor fusion 将这个例子推广到所有特征坐标组合；它不自动解决样本量、噪声或 overfitting 问题。

## 来源导航

| 预习目标 | 定位 |
| --- | --- |
| 直观看懂 additive 与 multiplicative | [Slides p10–15](https://mit-mi.github.io/mmai-course/spring2026/schedule/lec4.1%20-%20more%20fusion.pdf#page=10) · [10:14](https://www.youtube.com/watch?v=0SOieOIe4HI&t=614s) |
| 补 1 与 low-rank 技巧 | [Slides p18–22](https://mit-mi.github.io/mmai-course/spring2026/schedule/lec4.1%20-%20more%20fusion.pdf#page=18) · [21:28](https://www.youtube.com/watch?v=0SOieOIe4HI&t=1288s) |
| 动态权重与交互检验 | [Slides p23–29](https://mit-mi.github.io/mmai-course/spring2026/schedule/lec4.1%20-%20more%20fusion.pdf#page=23) · [Reading guidance](readings.md) |

## 自测与动手

1. 为什么“最后用了加法”不足以判定整个模型是 additive？
2. 两种维度为 dA、dB 的输入补 1 后，outer product 有多少元素？
3. EMAP 表现接近原模型说明什么，又不能说明什么？

动手：生成一份含 `xA·xB` 项的二维 toy data，比较 unimodal、additive 与带乘积项的回归。随后去掉真实乘积项，重复实验。提交两张预测关系图、测试误差以及一句有证据边界的结论。
