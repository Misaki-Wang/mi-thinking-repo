# Lecture 9 · Recap & Current Trends

- 课程日期：2025-12-05；视频时长：01:51:31。
- 来源：[官方 slides（128 页）](https://cme295.stanford.edu/slides/fall25-cme295-lecture9.pdf) · [Stanford Online 视频](https://www.youtube.com/watch?v=Q86qzJ1K1Ss)。
- 补充：[Lecture 9 readings](readings.md) · [全课 Guidance](../GUIDANCE.md)。

> 本讲是一场课程回顾与趋势讨论。视频与课件中的产品发布/排行榜信息都有时间戳，应按 2025 年末的语境理解。

## 先抓住的问题

Transformer 能否超越文本？本讲把 Vision Transformer、Vision-Language Model 和 diffusion 纳入同一条架构讨论，并以硬件优化、数据、能力边界和 research directions 收束课程。

## 本讲主线

- **从 Transformer recap 到视觉输入**：Slides 3–62 回顾核心机制，介绍把 image patch 作为 token 的 ViT，并以 end-to-end 分类示例展开。
- **VLM 架构与 diffusion**：Slides 63–99 对比 decoder-only 路径与 cross-attention 融合，再讨论 image/text diffusion 直觉与 masked diffusion。
- **当前限制与研究方向**：Slides 100–128 回看 cross-modal transfer、硬件/成本和 research frontier；课程结尾提醒仍有 hallucination、personalization、interpretability、安全等问题。

## 视频章节与课件定位

- [00:01:12 · Transformer recap](https://www.youtube.com/watch?v=Q86qzJ1K1Ss&t=72s) → [00:11:17 · LLM overview](https://www.youtube.com/watch?v=Q86qzJ1K1Ss&t=677s) — slides 3–42。
- [00:15:05 · LLM training](https://www.youtube.com/watch?v=Q86qzJ1K1Ss&t=905s) → [00:44:09 · Evaluation](https://www.youtube.com/watch?v=Q86qzJ1K1Ss&t=2649s) — course-wide recap.
- [00:48:57 · Vision Transformer](https://www.youtube.com/watch?v=Q86qzJ1K1Ss&t=2937s) — slides 43–62。
- [01:04:02 · Diffusion-based LLMs](https://www.youtube.com/watch?v=Q86qzJ1K1Ss&t=3842s) — slides 63–99。
- [01:23:38 · Closing thoughts](https://www.youtube.com/watch?v=Q86qzJ1K1Ss&t=5018s) — slides 100–128。

## 学习时可以追问

1. ViT 把图像切成 patches 后，哪些结构信息保留在 token sequence？和文本 token 有哪些不同？
2. VLM 的 projection 与 cross-attention 路线在训练数据、信息交换和计算成本上有何区别？
3. Diffusion LLM 的 iterative denoising，与 autoregressive next-token generation 的推理顺序有何取舍？
4. 跨模态迁移哪些 inductive bias，什么时候可能负迁移？

## 术语与延伸阅读

保留 ViT、VLM、patch embedding、cross-attention、diffusion、masked diffusion、non-autoregressive generation、cross-modal transfer。选读方向见 [补充阅读](readings.md)。
