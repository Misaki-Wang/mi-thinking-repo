# Readings guidance · Large multimodal models

阅读优先级为本学习档案的建议，不代表教师指定必读顺序。本页依据课表、论文官方摘要与作者教程页面整理；已核验来源身份，未把摘要级阅读写成全文复现实验结论。

## 建议顺序

先读 LoRA 与 LLaVA baseline，回答“怎样低成本接入新模态”；再读 instruction tuning 与 scaling；最后读 MoE、quantization、GLA 和 alignment 的社会影响。与 [课程预览](preview.md) 中的模块图一起记录。

## 逐项导读

| 课表项 | 优先级 | 阅读问题与记录内容 |
|---|---|---|
| 1. [Training Compute-Optimal Large Language Models](https://arxiv.org/abs/2203.15556) | 进阶 | 固定 compute 时，模型参数与训练 tokens 如何分配？检查 scaling 拟合范围、计算预算与 downstream 对比；不要把语言模型比例直接套到视觉 tokens。 |
| 2. [Super-NaturalInstructions](https://arxiv.org/abs/2204.07705) | 核心 | 模型泛化到新任务，还是同一任务的新样本？查 task-level train/test 分割、instruction 与 few-shot examples 的区别；记录适用于自己任务的评估单位。 |
| 3. [LoRA](https://arxiv.org/abs/2106.09685) | 核心 | 冻结原权重后，低秩增量放在哪里？画出基础权重与 trainable matrices，比较不同 rank、目标层和 full fine-tuning 的参数/显存条件。 |
| 4. [A Visual Guide to Mixture of Experts](https://newsletter.maartengrootendorst.com/p/a-visual-guide-to-mixture-of-experts) | 补基础 | 分清 router、expert、top-k、load balancing；说明总参数、active parameters、通信成本为何不是同一个指标。此项为作者教程。 |
| 5. [A Visual Guide to Quantization](https://newsletter.maartengrootendorst.com/p/a-visual-guide-to-quantization) | 补基础 | 量化哪个张量、用什么 scale、如何处理 outlier？记录权重存储减少与实际推理加速的区别。此项为作者教程。 |
| 6. [Improved Baselines with Visual Instruction Tuning](https://arxiv.org/abs/2310.03744) | 核心 | 一个相对简单的 vision-language connector 为什么足以构成强 baseline？重点查 projector、视觉分辨率、数据与 response formatting 的各自作用，不只看最终榜单。 |
| 7. [Gated Linear Attention Transformers with Hardware-Efficient Training](https://arxiv.org/abs/2312.06635) | 进阶 | 理论 linear complexity 是否变成真实吞吐？记录 sequence length、I/O、并行训练与 recurrent inference 的差别，比较 gating 的表达能力。 |
| 8. [Unintended Impacts of LLM Alignment on Global Representation](https://arxiv.org/abs/2402.15018) | 核心反思 | 此处 alignment 指偏好调优。分别检查 dialect、multilingualism、global opinions 的变化及偏好数据来源；不能以平均 instruction-following 分数代表所有群体。 |
| 9. A Visual Guide to Quantization | 重复项 | 与第 5 项同一链接；阅读一次即可，课表重复记录保留在 catalog。 |
| 10. Scaling Instruction-Finetuned Language Models | 错链待核对 | [课表链接](https://arxiv.org/abs/2106.09685) 实际仍为 LoRA。[同名论文候选](https://arxiv.org/abs/2210.11416) 已核验标题，但教师原意未另行确认。阅读候选时检查任务数量、模型规模与 instruction mixture 的扩展作用。 |

## 对比产物

做一张表，每行一个方案，填写“改训练数据 / 改模型结构 / 改更新参数 / 改数值精度”“是否冻结 LLM”“需要哪些监督”“真正报告的速度与显存环境”。LoRA 与 quantization 可以组合，MoE 与 dense model 则要分别比较 active compute。

## 读完自问

- 若预算相同，增加 adapter rank 和增加高质量数据应如何控制变量比较？
- task generalization 的测试集应如何避免训练任务泄漏？
- 为什么偏好 alignment 的改善可以伴随某些群体表现变差？

来源校验见 [reading-sources.json](../reading-sources.json)；术语见 [TERMS](../TERMS.md)。
