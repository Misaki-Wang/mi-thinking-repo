# Lecture 2 · 补充阅读：位置、归一化与 attention 变体

以下由 slides 的引用和讨论主题引出，不是 syllabus 指定必读。

## 建议顺序

1. [RoFormer: Enhanced Transformer with Rotary Position Embedding](https://arxiv.org/abs/2104.09864) · Su et al., 2021。配合 RoPE 推导，观察旋转如何把相对位置信息带入 attention。
2. [Train Short, Test Long: Attention with Linear Biases Enables Input Length Extrapolation](https://arxiv.org/abs/2108.12409) · Press et al., 2021。作为 ALiBi 代表，核对训练长度、测试长度和模型规模条件。
3. [Longformer: The Long-Document Transformer](https://arxiv.org/abs/2004.05150) · Beltagy et al., 2020。对应 local window 与 task-motivated global attention。
4. [GQA: Training Generalized Multi-Query Transformer Models from Multi-Head Checkpoints](https://arxiv.org/abs/2305.13245) · Ainslie et al., 2023。区分 MHA、MQA、GQA 中 query heads 与 KV heads 的数量和推理取舍。

## 读后检查

挑选一种 position method、一种 normalization 选择和一种 attention/cache 优化，分别说明它主要改变模型表示、训练稳定性还是推理资源。不要把“更高效”当作单一、跨硬件的指标。
