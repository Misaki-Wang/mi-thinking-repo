# Readings guidance · Multimodal generation

本讲两篇阅读分别强调生成系统的组合方式与大规模媒体生成工程。根据官方摘要整理；具体性能需继续核对论文实验设置。

## 1. Compositional Generative Modeling: A Single Model is Not All You Need

[论文](https://arxiv.org/pdf/2402.01103) · 建议核心阅读。

核心问题：复杂生成分布能否通过组合较小模型构成，并泛化到训练中没见过的组合？阅读方法部分时寻找“组合算子作用在什么量上”：模型分数、分布、条件或采样过程。不要把 compositional modeling 简化为依次调用几个 API。

记录三个对象：各 component 的训练数据覆盖、组合时加入的约束、新任务的验证集合。重点检查未见组合是否真的与训练组合分离，以及局部生成质量如何传递到整体结果。

## 2. Movie Gen: A Cast of Media Foundation Models

[论文](https://arxiv.org/abs/2410.13720) · 建议系统阅读。

核心问题：video generation、editing、personalization 与 synchronized audio 如何共享或分开建模？先读系统总览，再围绕 data curation、latent representation、evaluation protocol 各选一个问题深入。

阅读输出至少包含视频时长、帧率、分辨率、条件类型及评价方式。论文摘要中的模型规模或视频能力属于特定配置，不能把最佳展示样例当作平均表现，也不要把音频质量与音画同步合并成一个“好看”分数。

## 把两篇连接起来

| 比较轴 | 需要记录 |
|---|---|
| 系统边界 | 单模型、多组件，组件之间交换什么 |
| 数据覆盖 | 训练见过的条件组合与测试新组合 |
| 可控性 | 哪些条件能直接指定，哪些只能间接诱导 |
| 评估 | 单模态质量、跨模态一致性、编辑保真度分别测量 |
| 成本 | 训练、采样和组件协调的开销 |

自测：假设生成“海边狗叫”的短片，声音逼真但与画面动作错位，两个阅读视角分别会把问题归到哪里？为这种错误提出可重复的检查，而非只列指标名。

回到 [课程预览](preview.md) 的 latent variable、likelihood 与 sampling 区分。
