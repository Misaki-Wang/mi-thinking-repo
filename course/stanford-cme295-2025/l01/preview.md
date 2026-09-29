# Lecture 1 · Transformer

- 课程日期：2025-09-26；视频时长：01:41:59。
- 来源：[官方 slides（135 页）](https://cme295.stanford.edu/slides/fall25-cme295-lecture1.pdf) · [Stanford Online 视频](https://www.youtube.com/watch?v=Ub3GoFaUcds)。
- 补充：[Lecture 1 readings](readings.md) · [全课 Guidance](../GUIDANCE.md)。

> 本页依据官方 slides 的章节结构、文字层和 Stanford Online 的公开视频章节编写；是学习预览，不是完整视频转录。

## 先抓住的问题

为什么 Transformer 选择 attention，而不是沿着 RNN 的时间步逐个读取 token？本讲先回顾 NLP 任务与表示方式，再从 tokenization、embedding、Word2vec、RNN/LSTM 推进到 self-attention 和 encoder–decoder Transformer。

## 本讲主线

- **输入如何变成 token 与向量**：tokenization 决定词表切分方式；embedding 将离散 token 映射到可计算的向量空间。Slides 28–49 从 tokenization 过渡到 word representation 和 Word2vec。
- **序列结构如何建模**：RNN/LSTM 逐步传递状态；attention 允许当前位置直接参考相关 token。Slides 51–78 连接 recurrent models 与 attention。
- **Transformer 怎样端到端工作**：结合 positional information、encoder/decoder、shifted-right targets 与 output generation。Slides 80–134 用较长 worked example 串起计算流程。

## 视频章节与课件定位

- [00:09:40 · NLP overview](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=580s) — slides 16–27。
- [00:22:57 · Tokenization](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=1377s) — slides 28–33。
- [00:30:28 · Word representation](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=1828s) — slides 35–49。
- [00:53:23 · RNNs](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=3203s) — slides 51–64。
- [01:06:47 · Self-attention](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=4007s) → [01:13:53 · Transformer architecture](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=4433s) — slides 65–89。
- [01:29:53 · Detailed example](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=5393s) — slides 90–134。

## 学习时可以追问

1. Word2vec 训练目标怎样让向量携带上下文信息？它学到的表示为何不等同于句子理解？
2. RNN 的顺序状态传递，和 self-attention 的跨位置交互在并行计算与长依赖方面各有什么取舍？
3. Encoder–decoder 中 query、key、value 从哪里来？positional information 缺失时，模型还能区分 token 顺序吗？

## 术语与延伸阅读

保留 NLP、tokenization、embedding、Word2vec、RNN、LSTM、self-attention、query/key/value、encoder–decoder 等英文名称。课件引用的论文入口见 [补充阅读](readings.md)。
