# Readings guidance · Multimodal LLMs tutorial

本讲课表提供 12 篇扩展论文。建议先完成 notebook 的数据与 baseline 检查，再选择架构问题阅读。本页依据官方摘要核对主题与身份；下列“检查”是阅读任务，不表示已经复现或通读所有实验。

## 逐篇路线

| Reading | 建议优先级 | 带着什么问题读 |
|---|---|---|
| [Multimodal Transformer for Unaligned Multimodal Language Sequences](https://arxiv.org/abs/1906.00295) | 核心基础 | MulT 的 directional pairwise crossmodal attention 如何处理不同采样率？画 Query 与 Key/Value 的方向，核对 aligned 与 unaligned 的评估设定。 |
| [Masked Autoencoders Are Scalable Vision Learners](https://arxiv.org/abs/2111.06377) | 核心基础 | MAE 为什么只把可见 patches 送进 encoder？画不对称 encoder/decoder，检查 masking ratio 与下游迁移；区分 MAE 与概率生成模型 VAE。 |
| [Scaling Laws for Native Multimodal Models](https://arxiv.org/abs/2504.07951) | 进阶 | 固定什么条件后比较 early/late fusion？记录训练 mixture、参数范围与 compute，把架构结论限制在实验范围。课表将标题重复拼接了两次。 |
| [Transfer between Modalities with MetaQueries](https://arxiv.org/abs/2504.06256) | 核心拓展 | learnable queries 如何连接 MLLM latent 与 diffusion decoder？标出冻结组件、训练目标与配对数据，比较“保持理解能力”与“提升生成能力”的评估。 |
| [LLaMA-Adapter](https://arxiv.org/pdf/2303.16199) | 核心实践 | zero-init attention 和 gating 怎样注入新信息？与 notebook 的 LoRA 比较新增参数位置，而不是把两者都泛称 adapter。 |
| [Cobra](https://arxiv.org/pdf/2403.14520) | 架构拓展 | Mamba 骨干如何接入视觉？阅读时同时记录参数量、序列长度、推理设置和任务表现，检验 linear complexity 是否带来实际收益。 |
| [ModaVerse](https://arxiv.org/abs/2401.06395) | 生成拓展 | 用自然语言 I/O 对接生成模型，与对齐 latent features 有什么差异？列出跨模块接口以及可能丢失的精细视觉信息。 |
| [Spider: Any-to-Many Multimodal LLM](https://arxiv.org/pdf/2411.09439) | 生成拓展 | 一次响应输出多种模态需要什么 instruction template 与 decoder controller？除了各模态质量，还应验证同时生成内容的一致性。 |
| [SPHINX-X](https://arxiv.org/pdf/2402.05935) | 数据与规模 | 为什么去除冗余 vision encoders、跳过 padded sub-images、合并训练阶段？把这些变更与数据扩展分开列出，并寻找消融证据。 |
| [How Far Are We to GPT-4V?](https://arxiv.org/pdf/2404.16821) | 数据与规模 | 本文实际介绍 InternVL 1.5。检查强 vision encoder、dynamic high-resolution tiling、双语数据的贡献；“接近 GPT-4V”须落到具体 benchmark。 |
| [NExT-GPT](https://arxiv.org/pdf/2309.05519) | 核心拓展 | 多模态 adapters、LLM、diffusion decoders 如何连接？记录 modality-switching instruction tuning 的输入/输出格式，再与 ModaVerse、MetaQueries 对比接口。 |
| [Learning to Rebalance Multi-Modal Optimization by Adaptively Masking Subnetworks](https://arxiv.org/pdf/2404.08347) | 优化拓展 | AMSS 如何用模态重要性选择参数子网络更新？区分 modal-level 与 element-wise 控制；检查是否改善弱模态而不仅改善 overall score。 |

## 一次有效的阅读输出

选择 LLaMA-Adapter、MetaQueries、NExT-GPT、ModaVerse 中的两篇，完成“输入模态 → 共享骨干 → 输出模态”的模块图，旁边列出 trainable parameters、数据配对要求、训练阶段与两个可能失败的接口。然后解释：如果只做 slides narration，哪些组件可以省去，哪些评估不能省？

全部 12 篇无需一次读完；建议第一轮每篇看摘要与结构图，第二轮精读一条与你的项目有关的路径。回到 [notebook 预览](preview.md) 检查数据切分和 baseline 的具体问题。
