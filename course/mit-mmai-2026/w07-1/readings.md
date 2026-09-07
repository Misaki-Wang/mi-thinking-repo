# Readings guidance · Midterm review

官方课表没有为本次复习指定新的 Readings。本页给出针对已有课程资料的复习路线；以下练习是本档案建议，不是新增加的官方必读论文或真实试题。

## 从问题反推阅读

- 不能区分 redundancy / uniqueness / synergy：回到 [导论](../w01-1/preview.md) 与其 survey 导读，给同一个目标任务分别举例。
- 无法选择模型结构：回到 [heterogeneity](../w02-2/preview.md)，写出输入的空间/时间结构与所需 invariance / equivariance。
- 不理解 fusion 的收益：回到 [fusion](../w04-1/preview.md)，比较 additive、multiplicative、gating，并解释 ablation 的控制条件。
- 把所有 alignment 当成同一件事：回到 [alignment](../w04-2/preview.md)，区分显式对应、对比表示和上下文化表示。
- 搞不清冻结 LLM 如何接入视觉：回到 [MLLM readings](../w05-1/readings.md)，把 LoRA、projector、instruction tuning 分开。
- 把 VAE、diffusion、flow matching 的流程混在一起：回到 [generative AI readings](../w06-2/readings.md)，分别写训练、采样两条路径。

## 一份可复用的检查单

对任一论文或模型，在空白纸上回答：输入/输出、关键假设、监督来源、模块边界、训练目标、对比基线、失败情形、可迁移的结论。答不出的项就是下一轮精读位置。

建议输出一页“我能解释的概念”和一页“尚不能推出的结论”。不要只收集高亮段落；用新模态重讲一遍，才能检查是否理解。回到 [本讲预览](preview.md)。
