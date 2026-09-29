# Lecture 2 · Transformer-Based Models & Tricks

- 课程日期：2025-10-03；视频时长：01:47:20。
- 来源：[官方 slides（109 页）](https://cme295.stanford.edu/slides/fall25-cme295-lecture2.pdf) · [Stanford Online 视频](https://www.youtube.com/watch?v=yT84Y5zCnaA)。
- 补充：[Lecture 2 readings](readings.md) · [全课 Guidance](../GUIDANCE.md)。

> 本页由官方 slides 与 Stanford Online 视频章节整理，是学习预览，不是完整转录。

## 先抓住的问题

Transformer 本身不带 token 顺序，架构设计如何注入位置信息、稳定深层训练、减少注意力开销，并形成 encoder-only、decoder-only 或 encoder–decoder 等模型家族？

## 本讲主线

- **Position representation**：从 sinusoidal / learned absolute embeddings，走向 relative bias（T5 bias、ALiBi）与 rotary position embeddings（RoPE）。Slides 12–35。
- **Normalization 与 attention 变体**：比较 LayerNorm 位置和类型，再看 Longformer 的 local/global attention 及共享 attention heads。Slides 37–54。
- **模型家族与 BERT**：Slides 56–108 对比 Transformer-based models，深入 BERT、masked language modeling、next sentence prediction、fine-tuning，并以 DistilBERT/RoBERTa 讨论效率和训练改进。

## 视频章节与课件定位

- [00:10:37 · Position embeddings overview](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=637s) — slides 12–24。
- [00:25:56 · T5 bias and ALiBi](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=1556s) → [00:31:02 · RoPE](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=1862s) — slides 24–35。
- [00:43:42 · Layer normalization](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=2622s) — slides 37–44。
- [00:50:39 · Sparse attention](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=3039s) → [00:55:38 · Sharing attention heads](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=3338s) — slides 46–54。
- [01:02:42 · Transformer-based models](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=3762s) → [01:11:38 · BERT deep dive](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=4298s) — slides 56–82。
- [01:33:24 · BERT fine-tuning](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=5604s) — slides 83–108。

## 学习时可以追问

1. RoPE 将位置影响放进 query/key 的旋转；这和在 token embedding 上直接加 positional vector 有什么不同？
2. GQA/MQA 减少 KV heads 的方式，具体改变了 inference cache 的什么资源需求？
3. BERT 的 masked-token objective 与 decoder-only next-token objective 分别适合什么任务？微调数据又引入哪些新假设？

## 术语与延伸阅读

建议保留 absolute/relative position、RoPE、ALiBi、LayerNorm、RMSNorm、Longformer、MHA/MQA/GQA、BERT、MLM、DistilBERT、RoBERTa。精选的课件引用见 [补充阅读](readings.md)。
