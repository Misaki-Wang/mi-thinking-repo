# Lecture 6 · 补充阅读：Reasoning、RLVR 与 scaling

## 建议顺序

1. [Chain-of-Thought Prompting Elicits Reasoning in Large Language Models](https://arxiv.org/abs/2201.11903) · Wei et al., 2022。作为 prompting 入口，区分可见 rationale 与推理正确性的证据。
2. [DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models](https://arxiv.org/abs/2402.03300) · Shao et al., 2024。对应 GRPO 和 verifiable reward 的课件讨论。
3. [DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning](https://arxiv.org/abs/2501.12948) · DeepSeek-AI, 2025。配合 slides 116–141，分开看 recipe、reward、benchmark。
4. [DAPO: An Open-Source LLM Reinforcement Learning System at Scale](https://arxiv.org/abs/2503.14476) · Yu et al., 2025。对应课件中的 DAPO；关注训练系统、奖励设计与评测条件。

## 读后检查

给一项 reasoning benchmark 标注题型、样本、可验证答案、pass@k 预算和评分器。模型“多想”带来的增益可能来自搜索、训练改进或长度变化，应分别考察。
