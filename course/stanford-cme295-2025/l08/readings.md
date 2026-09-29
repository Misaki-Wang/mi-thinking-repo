# Lecture 8 · 补充阅读：LLM-as-a-Judge 与 benchmark

先看自动指标和人评的差异，再读 LLM judge，最后检查面向具体任务的 benchmarks。

## 建议顺序

1. 原始 [BLEU](https://aclanthology.org/P02-1040/)、[METEOR](https://aclanthology.org/W05-0909/) 和 [ROUGE](https://aclanthology.org/W04-1013/) 论文。对照 lexical overlap 指标和语义质量。
2. [Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena](https://arxiv.org/abs/2306.05685) · Zheng et al., 2023。对应 slides 的 judge bias 和 best practice。
3. [Measuring Massive Multitask Language Understanding](https://arxiv.org/abs/2009.03300) · Hendrycks et al., 2020。课件以 MMLU 展示知识 benchmark。
4. [SWE-bench](https://arxiv.org/abs/2310.06770) · Jimenez et al., 2023；[τ-bench](https://arxiv.org/abs/2406.12045) · Yao et al., 2024。比较 coding issue 修复与交互式 tool-use 评估。

课件还展示 AIME、PIQA、HarmBench。选读时回到 benchmark 原始论文或项目，确认版本、数据、判分方式和污染风险。

## 读后检查

区分 reference-based、pairwise preference、LLM judge、execution-based 和 human rating。再问：benchmark 成功是否能预测你关心的部署任务？
