# Lecture 3 · 补充阅读：MoE、decoding 与 inference

这些论文来自 slides 引用，帮助把“语言模型如何生成”与“系统如何服务”分开。

## 建议顺序

1. [Switch Transformers: Scaling to Trillion Parameter Models with Simple and Efficient Sparsity](https://arxiv.org/abs/2101.03961) · Fedus et al., 2021。对应 sparse MoE 与 routing；区分总参数量、每 token 激活参数和通信开销。
2. [Chain-of-Thought Prompting Elicits Reasoning in Large Language Models](https://arxiv.org/abs/2201.11903) · Wei et al., 2022，以及 [Self-Consistency Improves Chain of Thought Reasoning](https://arxiv.org/abs/2203.11171) · Wang et al., 2022。比较 prompting 与多路径采样/聚合策略，并保留其任务和采样预算。
3. [Efficient Memory Management for Large Language Model Serving with PagedAttention](https://arxiv.org/abs/2309.06180) · Kwon et al., 2023。配合 slides 的 KV cache / PagedAttention 图，关注碎片、共享和 batching。
4. [DeepSeek-V2](https://arxiv.org/abs/2405.04434) · DeepSeek-AI, 2024。对应 Multi-head Latent Attention（MLA），看低秩 latent KV 的设计目标和报告条件。

## 读后检查

用同一个 prompt 画出 greedy、beam 和 sampling 流程；另画 KV cache 随序列长度增长的示意。注明哪些方法改输出搜索，哪些减少模型调用或缓存成本。
