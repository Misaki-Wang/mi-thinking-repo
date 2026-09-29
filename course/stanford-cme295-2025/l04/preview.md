# Lecture 4 · LLM Training

- 课程日期：2025-10-17；视频时长：01:47:27。
- 来源：[官方 slides（128 页）](https://cme295.stanford.edu/slides/fall25-cme295-lecture4.pdf) · [Stanford Online 视频](https://www.youtube.com/watch?v=VlA_jt_3Qc4)。
- 补充：[Lecture 4 readings](readings.md) · [全课 Guidance](../GUIDANCE.md)。

> 预览依据官方 slides 及 Stanford Online 的视频章节导航，重点按模型生命周期和课件页码组织；不等同逐字转录。

## 先抓住的问题

从随机初始化到可用的任务模型，要经过哪些训练阶段？这些阶段分别受数据、compute、GPU memory、通信和可训练参数数量什么约束？

## 本讲主线

- **Pretraining 与 scaling**：Slides 8–27 介绍 next-token objective、compute 记法、scaling laws 与训练挑战；比较训练数据量、模型规模和预算时，需要明确是哪种经验规律。
- **训练系统效率**：Slides 29–71 从 memory bottleneck 讲到 data parallelism、ZeRO、model parallelism 和 FlashAttention。优化数据移动与分片不会改变训练目标，但会改变可用规模与成本。
- **从预训练到任务适配**：Slides 82–105 转向 behavior gap、SFT 和 instruction tuning；slides 106–127 讲 LoRA/QLoRA 的低秩适配与量化取舍。

## 视频章节与课件定位

- [00:07:19 · Pretraining](https://www.youtube.com/watch?v=VlA_jt_3Qc4&t=439s) → [00:16:34 · Scaling laws / Chinchilla](https://www.youtube.com/watch?v=VlA_jt_3Qc4&t=994s) — slides 8–27。
- [00:24:49 · Training optimizations](https://www.youtube.com/watch?v=VlA_jt_3Qc4&t=1489s) — slides 29–37。
- [00:31:09 · Data parallelism / ZeRO](https://www.youtube.com/watch?v=VlA_jt_3Qc4&t=1869s) → [00:35:51 · Model parallelism](https://www.youtube.com/watch?v=VlA_jt_3Qc4&t=2151s) — slides 38–44。
- [00:38:26 · FlashAttention](https://www.youtube.com/watch?v=VlA_jt_3Qc4&t=2306s) — slides 45–71。
- [00:52:37 · Quantization](https://www.youtube.com/watch?v=VlA_jt_3Qc4&t=3157s) → [00:56:00 · Mixed precision](https://www.youtube.com/watch?v=VlA_jt_3Qc4&t=3360s) — slides 72–81。
- [01:02:31 · SFT](https://www.youtube.com/watch?v=VlA_jt_3Qc4&t=3751s) → [01:09:21 · Instruction tuning](https://www.youtube.com/watch?v=VlA_jt_3Qc4&t=4161s) — slides 82–105。
- [01:37:53 · LoRA](https://www.youtube.com/watch?v=VlA_jt_3Qc4&t=5873s) → [01:45:16 · QLoRA](https://www.youtube.com/watch?v=VlA_jt_3Qc4&t=6316s) — slides 106–127。

## 学习时可以追问

1. FLOPs、FLOPS、tokens、parameter count 是不同量纲；每个 scaling comparison 固定了什么？
2. ZeRO、model parallelism、FlashAttention 分别减少冗余状态、拆分计算，还是优化 memory IO？不要把它们都笼统叫“并行”。
3. LoRA 只训练低秩更新，QLoRA 进一步量化基础权重；两者省下的资源来自不同部分。
4. SFT 改善指令行为，但是否能保证 preference alignment？哪些问题留给下一讲？

## 术语与延伸阅读

保留 pretraining、compute-optimal、ZeRO、data/model parallelism、FlashAttention、mixed precision、SFT、instruction tuning、LoRA、QLoRA。原始参考链接见 [补充阅读](readings.md)。
