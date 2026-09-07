# W02-2 · Data & Heterogeneity：让数据结构决定模型

预习本节时，把注意力放在“元素是什么、元素如何组合、哪些变化不该改变答案”上。课程用 modality profile 串起图像、语言、音频、传感器、set 与 graph，再把深度网络拆成表示构建和信息聚合。学会这套分析，比给每种模态背一个默认架构更有用。

整理依据为 Slides 与公开视频的英文自动字幕；时间链接定位到相关片段起点。下文另对 invariance/equivariance 等容易因课件简写产生误解的术语作学习性澄清。

## 七个核心概念

1. **Modality profile 是建模前的数据说明书。** 它包括元素表示与分布、granularity、structure、information、noise 和 task relevance。视频的 frame rate、语音的 sample rate、文本的 word rate 不同；将它们都裁成同样长度，不能保证对应同一事件。视频强调 granularity 还随数据收集方式改变。[Slides p15–21](https://mit-mi.github.io/mmai-course/spring2026/schedule/lec2.2%20-%20heterogeneity.pdf#page=15) · [视频 14:18](https://www.youtube.com/watch?v=CH2_US07OdA&t=858s)

2. **抽象表示会保留某些信息并压缩另一些信息。** Bag-of-words 便于固定维度处理，却丢掉词序；spectrogram 显示时间与频率结构；graph 用边表达关系，set 则没有给定的元素顺序。选择表示时，应问被丢掉的因素是否恰好决定标签。[Slides p7–14](https://mit-mi.github.io/mmai-course/spring2026/schedule/lec2.2%20-%20heterogeneity.pdf#page=7)

3. **Generalization 需要与部署条件匹配的划分。** Train 用于拟合参数，validation 用于选择超参数，test 用于最终检查。讲解在 33:35 区分 underfitting 与 overfitting，并强调不能只看 training accuracy。对多模态数据，按病人、场景或时间切分往往比随机分片更符合实际问题。[Slides p28–30](https://mit-mi.github.io/mmai-course/spring2026/schedule/lec2.2%20-%20heterogeneity.pdf#page=28) · [视频 33:35](https://www.youtube.com/watch?v=CH2_US07OdA&t=2015s)

4. **Representation + aggregation 是架构的共同语言。** 单个元素先经过可学习函数，再通过 sum、concat、convolution、self-attention 或 cross-attention 组合，最后计算 loss 并更新参数。不同架构的关键区别，是哪些元素共享参数、谁能够和谁交换信息。[Slides p34–35](https://mit-mi.github.io/mmai-course/spring2026/schedule/lec2.2%20-%20heterogeneity.pdf#page=34) · [视频 43:15](https://www.youtube.com/watch?v=CH2_US07OdA&t=2595s)

5. **Set 模型要满足 permutation invariance。** 同一组对象换个排列，集合分类不应变化。Deep Sets 的结构 `f(X) = ρ(Σᵢ φ(xᵢ))` 同时使用共享 encoder 和对称聚合；如果每个位置使用不同 encoder，或者用有序 concat，就破坏了这个保证。[Slides p36–39](https://mit-mi.github.io/mmai-course/spring2026/schedule/lec2.2%20-%20heterogeneity.pdf#page=36) · [视频 46:03](https://www.youtube.com/watch?v=CH2_US07OdA&t=2763s)

6. **Sequence、image 和 graph 选择不同的邻域。** RNN 沿时间传递状态；attention 用内容决定聚合权重；CNN 通过局部窗口与共享 filter 利用空间规律；GNN 按邻接边聚合。ViT 将 image patches 变成序列，继承 attention 的灵活性，也需要位置等信息表达空间关系。[Slides p46–70](https://mit-mi.github.io/mmai-course/spring2026/schedule/lec2.2%20-%20heterogeneity.pdf#page=46)

7. **Domain-specific 与 general-purpose 是一个连续选择。** 任务专用模型、预训练模型加 adaptation、直接调用通用模型，各自消耗不同的数据、算力与工程成本。视频把 semantic information、granularity、标注量、资源和 explainability 一起列为决策条件，而不是宣称存在通用最优架构。[Slides p32–33](https://mit-mi.github.io/mmai-course/spring2026/schedule/lec2.2%20-%20heterogeneity.pdf#page=32) · [视频 41:26](https://www.youtube.com/watch?v=CH2_US07OdA&t=2486s)

## 关键机制与术语校正

`Attention(Q,K,V) = softmax(QKᵀ / √dₖ)V`：Q 与 K 产生元素间权重，softmax 按行归一化，再对 V 做加权聚合。位置编码或 mask 会进一步约束序列结构。不要把 self-attention 本身理解为“自然知道词序”。

严格区分 `invariance: f(Tx)=f(x)` 与 `equivariance: f(Tx)=T′f(x)`。图像分类希望平移后类别不变；分割希望输出掩码一起平移。Slides 部分 CNN 页面使用了宽泛的“spatial invariance”措辞；更精确地说，共享卷积通常提供平移等变性，最终不变性还取决于聚合、边界与具体实现。

## 来源导航

| 问题 | 定位 |
| --- | --- |
| 如何写 modality profile | [Slides p15–21](https://mit-mi.github.io/mmai-course/spring2026/schedule/lec2.2%20-%20heterogeneity.pdf#page=15) · [14:18](https://www.youtube.com/watch?v=CH2_US07OdA&t=858s) |
| 为什么共享参数和聚合必须一起设计 | [Slides p36–41](https://mit-mi.github.io/mmai-course/spring2026/schedule/lec2.2%20-%20heterogeneity.pdf#page=36) · [46:03](https://www.youtube.com/watch?v=CH2_US07OdA&t=2763s) |
| 序列、空间、图模型的联系 | [Slides p46–70](https://mit-mi.github.io/mmai-course/spring2026/schedule/lec2.2%20-%20heterogeneity.pdf#page=46) |
| 延伸阅读 | [Reading guidance](readings.md) |

## 自测与动手

1. 把图像当成 set of pixels 会丢掉什么？加入坐标后又改变了什么？
2. 图分类与节点分类分别需要 permutation invariance 还是 equivariance？
3. 什么情况下，时间上相邻的样本不能被当成独立测试样本？

动手：为自己的两种模态各写一张 profile；再实现或手算一个共享 `φ` 加 sum 的 set encoder。打乱输入十次检查输出，随后换成 concat，说明区别来自哪一个设计选择。
