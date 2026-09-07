# W04-2 · Multimodal alignment：相似表示不等于充分理解

Alignment 研究模态之间哪些元素相互对应，以及如何利用对应关系学习表示。视频前约 34 分钟续讲 fusion 的量化，之后进入本节主题。预习时先理解 contrastive learning 的正负配对，再问“它保留了什么、忽略了什么”，最后区分显式训练的 alignment 与 independently trained models 中观察到的 emergent alignment。

整理依据为 Slides 与公开视频的英文自动字幕；时间链接定位到相关片段起点。只有 Slides 定位的后续主题按课件整理，公式中的标准化写法另有说明。

## 七个核心概念

1. **Alignment 可以是目标，也可以是中间步骤。** Grounding 直接要求指出词对应的图像区域；contextualized representation 则利用对应关系形成更有用的特征。Video 和 sensor 的语义边界通常不像词边界那样清晰，因此 continuous alignment 还涉及 segmentation 与时间变形。[Slides p4–6、29–34](https://mit-mi.github.io/mmai-course/spring2026/schedule/lec4.2%20-%20alignment.pdf#page=4) · [视频 35:54](https://www.youtube.com/watch?v=u-H43tRgYJg&t=2154s)

2. **Correspondence 不一定是一对一对象匹配。** 视频讨论“a woman reading newspaper”：woman 和 newspaper 可以对应区域，但 reading 涉及人、报纸与姿态之间的关系。这解释了为什么只做 object matching 可能不足以表达动作或关系词。[Slides p6](https://mit-mi.github.io/mmai-course/spring2026/schedule/lec4.2%20-%20alignment.pdf#page=6) · [视频 39:05](https://www.youtube.com/watch?v=u-H43tRgYJg&t=2345s)

3. **Specialized encoders 与 similarity function 各负其责。** Encoder 处理模态异构性，alignment function 约束表示之间的关系。Cosine similarity、kernel、CCA、order/hierarchy 捕捉的关系不同；同维向量或高 cosine 值都不意味着两个 representation spaces 完全相同。[Slides p7–12](https://mit-mi.github.io/mmai-course/spring2026/schedule/lec4.2%20-%20alignment.pdf#page=7)

4. **Contrastive learning 将配对变成训练信号。** CLIP 对一批图像和文本编码后，构造两两相似度矩阵，匹配样本在对角线上，其他样本作为 negatives。训练让正确配对相对其他候选更容易被找回。视频由这个矩阵说明 retrieval 和 zero-shot classification 的联系。[Slides p13–16](https://mit-mi.github.io/mmai-course/spring2026/schedule/lec4.2%20-%20alignment.pdf#page=13) · [视频 1:00:48](https://www.youtube.com/watch?v=u-H43tRgYJg&t=3648s)

5. **Shared information 不一定等于全部 task-relevant information。** InfoNCE 与 mutual information 的联系帮助解释对比学习偏向跨视图共性。但如果目标需要某模态独有的纹理、语法或细节，过度压缩到共享部分可能有害。Slides 随后介绍 representation fission 与 factorized contrastive learning，分别照顾 shared 和 unique information。[Slides p17–25](https://mit-mi.github.io/mmai-course/spring2026/schedule/lec4.2%20-%20alignment.pdf#page=17) · [视频 1:07:28](https://www.youtube.com/watch?v=u-H43tRgYJg&t=4048s)

6. **Global 和 continuous alignment 放宽简单配对。** Assignment problem 的初始条件是相同数量元素、一对一、全部匹配；optimal transport 用带边际约束的软分配处理更一般的对应。时间信号还可以通过 warping 或 segmentation 对齐。HuBERT、VQ-VAE 展示把连续信号转成离散单位的思路，不应把这些单位直接等同于人工语义词。[Slides p26–36](https://mit-mi.github.io/mmai-course/spring2026/schedule/lec4.2%20-%20alignment.pdf#page=26)

7. **Emergent alignment 是可检验观察，不是普遍保证。** 独立训练的 vision/text models 可能在样本间距离关系上越来越相似。比较这类表示时，kernel similarity 衡量的是样本关系的相似性，不要求坐标逐项相等。课程也专门留下 limitations；本节 readings 将进一步检验 alignment 与 performance 的关系是否依赖数据和任务。[Slides p37–41](https://mit-mi.github.io/mmai-course/spring2026/schedule/lec4.2%20-%20alignment.pdf#page=37)

## 关键机制：读懂一个方向的 InfoNCE

`Lᵢ = −log[ exp(sim(zAᵢ,zBᵢ)/τ) / Σⱼ exp(sim(zAᵢ,zBⱼ)/τ) ]`。

分子是正确配对，分母包括整个候选 batch；`τ` 是 temperature。CLIP 还使用反向的 text-to-image loss。这里补出 exponent 与 temperature，避免将 Slides 的简写误读成可以直接对正负 cosine 值取概率。`log N − L` 在相应采样与建模条件下给出 mutual information 的下界；这不意味着有限 batch 和有限模型精确恢复全部互信息。

## 来源导航

| 问题 | 定位 |
| --- | --- |
| 上一节 fusion 的 EMAP 续讲 | [视频 13:56](https://www.youtube.com/watch?v=u-H43tRgYJg&t=836s) · [W04-1](../w04-1/preview.md) |
| Alignment 正式开始 | [Slides p4](https://mit-mi.github.io/mmai-course/spring2026/schedule/lec4.2%20-%20alignment.pdf#page=4) · [视频 34:01](https://www.youtube.com/watch?v=u-H43tRgYJg&t=2041s) |
| CLIP 的 batch 配对与信息边界 | [Slides p15–25](https://mit-mi.github.io/mmai-course/spring2026/schedule/lec4.2%20-%20alignment.pdf#page=15) · [1:00:48](https://www.youtube.com/watch?v=u-H43tRgYJg&t=3648s) |
| 从显式到隐式 alignment | [Slides p26–41](https://mit-mi.github.io/mmai-course/spring2026/schedule/lec4.2%20-%20alignment.pdf#page=26) · [Reading guidance](readings.md) |

## 自测与动手

1. 为什么同一个 batch 中的“负样本”也可能语义正确？
2. Retrieval 很强但分不清“狗追人”和“人追狗”，可能遗漏了什么训练信号？
3. 两个 representation spaces 更相似，为什么不必然提升某项下游任务？

动手：准备六组图文，加入两组仅交换关系或属性的 hard negatives。记录图文相似度矩阵，比较普通 retrieval 与关系辨别。将“共享对象”“关系”“模态独有细节”分开评价，写出一种可能改善目标能力的配对策略。
