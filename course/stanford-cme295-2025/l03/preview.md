# Lecture 3 · Large Language Models

- 课程日期：2025-10-10；视频时长：01:48:45。
- 来源：[官方 slides（125 页）](https://cme295.stanford.edu/slides/fall25-cme295-lecture3.pdf) · [Stanford Online 视频](https://www.youtube.com/watch?v=Q5baLehv5So)。
- 补充：[Lecture 3 readings](readings.md) · [全课 Guidance](../GUIDANCE.md)。

> 本预览依据课件与公开视频章节目录。技术解释若涉及论文或具体实现，建议沿补充阅读回到原文。

## 先抓住的问题

“Large Language Model”从架构到实际生成包含哪些步骤？本讲从 decoder-style LLM 和 sparse MoE 开始，走过 next-token prediction 与 decoding，再回到 prompt/in-context learning，最后讨论推理效率。

## 本讲主线

- **架构与 MoE**：Slides 7–31 讨论 LLM 定义、MoE layer、routing collapse 与 expert interpretation。需要区分总参数量和每 token 激活的参数量。
- **从 logits 到文本**：Slides 33–75 涵盖 next-token distribution、greedy、beam search、top-k/sampling、temperature 和 guided decoding。输出策略改变结果分布，不会改变底层模型参数。
- **上下文学习与推理优化**：Slides 76–85 介绍 prompting、ICL、CoT 和 self-consistency；slides 87–123 转向 KV cache、head sharing、PagedAttention、MLA、speculative decoding 与 multi-token prediction。

## 视频章节与课件定位

- [00:03:43 · LLM definition](https://www.youtube.com/watch?v=Q5baLehv5So&t=223s) — slides 7–22。
- [00:07:37 · Mixture of Experts](https://www.youtube.com/watch?v=Q5baLehv5So&t=457s) → [00:15:47 · MoE in LLMs](https://www.youtube.com/watch?v=Q5baLehv5So&t=947s) — slides 23–31。
- [00:36:35 · Response generation](https://www.youtube.com/watch?v=Q5baLehv5So&t=2195s) — slides 33–45。
- [00:38:34 · Greedy and beam search](https://www.youtube.com/watch?v=Q5baLehv5So&t=2314s) → [00:46:36 · Sampling](https://www.youtube.com/watch?v=Q5baLehv5So&t=2796s) — slides 46–64。
- [01:04:53 · Guided decoding](https://www.youtube.com/watch?v=Q5baLehv5So&t=3893s) — slides 65–75。
- [01:07:07 · Prompting](https://www.youtube.com/watch?v=Q5baLehv5So&t=4027s) → [01:18:35 · CoT / self-consistency](https://www.youtube.com/watch?v=Q5baLehv5So&t=4715s) — slides 76–85。
- [01:25:00 · KV cache](https://www.youtube.com/watch?v=Q5baLehv5So&t=5100s) → [01:33:09 · PagedAttention / MLA](https://www.youtube.com/watch?v=Q5baLehv5So&t=5589s) — slides 86–123。

## 学习时可以追问

1. Greedy、beam search、top-k 和 temperature sampling 优化的目标分别是什么？哪类“更高概率”不等同于“更好的答案”？
2. CoT、self-consistency 是输出策略；怎样设计评测，避免把更长的文字误认为更可靠的 reasoning？
3. KV cache、PagedAttention 与 speculative decoding 分别减少哪一部分 inference 成本？哪些优化互相正交？

## 术语与延伸阅读

保留 decoder-only、MoE、routing、next-token prediction、temperature、top-k、guided decoding、in-context learning、CoT、KV cache、PagedAttention、MLA、speculative decoding。课件引用的原始论文见 [补充阅读](readings.md)。
