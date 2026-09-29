# Lecture 9 · 补充阅读：ViT、VLM 与 Diffusion

本讲用课程回顾连接视觉输入与 diffusion。下面是 slides 提及的代表性论文，并非对所有视觉或生成架构的全面比较。

## 建议顺序

1. [An Image Is Worth 16×16 Words: Transformers for Image Recognition at Scale](https://arxiv.org/abs/2010.11929) · Dosovitskiy et al., 2020。对应 patch embedding 和 ViT 流程。
2. [Flamingo: a Visual Language Model for Few-Shot Learning](https://arxiv.org/abs/2204.14198) · Alayrac et al., 2022。作为视觉语言模型 cross-attention 路线的例子。
3. [Denoising Diffusion Probabilistic Models](https://arxiv.org/abs/2006.11239) · Ho et al., 2020。对应 image forward/reverse process。
4. [Discrete Diffusion Modeling by Estimating the Ratios of the Data Distribution](https://arxiv.org/abs/2310.16834) · Lou et al., 2023；[Simple and Effective Masked Diffusion Language Models](https://arxiv.org/abs/2406.07524) · Sahoo et al., 2024。对应文本 masking / iterative unmasking 的两个路线。

Slides 还引用 [Large Language Diffusion Models](https://arxiv.org/abs/2502.09992) · Nie et al., 2025，可作为额外模型案例。

## 读后检查

并排画出 autoregressive 与 diffusion 生成流程，标出生成顺序、每步可访问上下文、并行机会与推理成本。比较时注意质量设置和生成预算。
