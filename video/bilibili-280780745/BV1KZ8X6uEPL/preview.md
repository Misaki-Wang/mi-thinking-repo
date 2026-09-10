# Kimi K3 技术报告领读：架构、Attention 与 MoE

- 作者：张小珺商业访谈录。
- 原题：领读Kimi K3技术报告：从架构创新聊起，注意力美学、多教师蒸馏和开源MoE。
- 发布：2026-08-26；时长：02:04:20；本次指定样例，目录快照第 2 期。
- 来源：[Bilibili 原视频](https://www.bilibili.com/video/BV1KZ8X6uEPL/)。
- 阅读：[中文讲稿](transcript.zh-CN.md) · [系列目录](../README.md) · [学习指引](../GUIDANCE.md)。

> 预览依据视频简介与官方分段，非全文人工校对。本期简介实际提供的是参考文献列表，没有官方分段时间；下面按文献主题组织导航，不表示视频先后顺序，也不补造时间戳。各项技术解释以视频原话及对应论文为准。

## 先抓住的问题

领读标题把架构创新、注意力、多教师蒸馏与开源 MoE 放在一起。简介提供了继续检索的文献链，可以先建立概念清单，再用讲稿确认讲解怎样连接这些工作。

## 按简介文献组织的主题导航

- **Linear Attention 与递归形式**：简介列出 RetNet、Gated DeltaNet、Kimi Linear，以及 Flash Linear Attention。阅读时追踪 `data-independent decay`、`chunk-recurrent`、`gated delta rule`、`fine-grained decay` 与 `KDA kernel`。
- **Attention Gating 与稳定性**：简介列出 Gated Attention for Large Language Models；把 gating 的讨论与训练稳定性相关表述对应起来。
- **Normalization 与 Residual Connections**：对照 On Layer Normalization in the Transformer Architecture、Hyper-Connections、Attention Residuals；记录 `Pre-LN`、`Post-LN` 与跨深度聚合的各自语境。
- **MoE 与负载、通信成本**：简介列出 LatentMoE、《MoE 环游记：6、最优分配促均衡》和 DeepSeek-V3 Technical Report；留意 `latent expert space`、`Quantile Balancing`、`DualPipe` 与 `communication–computation overlap`。
- **优化与激活值**：简介通过 Moonlight / Muon 与 GPT-OSS 指向 `activation outlier`、`clamped SwiGLU` 等词，读时核对它们分别出现在哪个模型与讨论环节。
- **训练日程与长上下文**：MiniCPM 与 RNoPE 对应简介中的 `WSD`、`RoPE`、`NoPE` 线索；先记录问题，再查技术细节。
- **Rollout、预算与 Reward Model**：Kimi K1.5、Kimi K2.5 对应 `partial rollout`、`CoT`、`reasoning-effort budget control`、`Agentic Generative Reward Model`。
- **Distillation**：标题提示多教师蒸馏，简介列出 MiniLLM 与 `student-generated samples`、`on-policy distillation`；两者在本期中的实际联系需要从讲稿核对。

## 学习时可以追问

1. 哪些设计改变了模型表达方式，哪些主要针对数值稳定、内存、通信或推理效率？请分别找到原始依据。
2. 讲解如何区分 Attention、Residual Connections 与 MoE 的作用？哪些词只是相似，实际处理的是不同问题？
3. 蒸馏使用什么样的教师与学生数据？简介不足以回答的部分，能否在讲稿和报告中定位？

## 继续阅读的方法

原视频简介保留了上述论文和项目的链接。先选一个主题，从视频中的具体表述进入原文，不必一次通读全部文献。本预览没有对这些论文进行独立逐篇核查，也不据标题推断 Kimi K3 的最终配置、训练结果或性能。
