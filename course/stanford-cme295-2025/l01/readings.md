# Lecture 1 · 补充阅读：从词表示到 self-attention

syllabus 没有列出逐讲指定 reading。本页从官方 slides 引用的论文中挑选入门材料，属于自学建议。

## 建议顺序

1. [Efficient Estimation of Word Representations in Vector Space](https://arxiv.org/abs/1301.3781) · Mikolov et al., 2013。对应 slides 37–49。看 context prediction 如何训练连续 word vectors；它衡量的是表示与相似性，不是句子级推理。
2. [Neural Machine Translation by Jointly Learning to Align and Translate](https://arxiv.org/abs/1409.0473) · Bahdanau et al., 2014。对应 slides 65–69。关注 soft alignment 如何放松 fixed-length encoder representation 的瓶颈。
3. [Attention Is All You Need](https://arxiv.org/abs/1706.03762) · Vaswani et al., 2017。对应 slides 70–89。建议看 encoder/decoder、scaled dot-product attention 和 positional encoding 图。

## 读后检查

画出 token IDs → embeddings → contextual representations → output probabilities 的路径。标明哪些组件处理顺序、哪些负责跨 token 交互，并对比 RNN 与 Transformer 的并行性差异。
