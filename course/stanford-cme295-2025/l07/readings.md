# Lecture 7 · 补充阅读：RAG、检索与 Agent

建议从检索开始，再读 tool use，最后看 agent 行动循环。

## 建议顺序

1. [Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks](https://arxiv.org/abs/2005.11401) · Lewis et al., 2020。对应 RAG 原始结构，区分 parametric 与 non-parametric memory。
2. [Sentence-BERT](https://arxiv.org/abs/1908.10084) · Reimers & Gurevych, 2019。对应课件的 dense retrieval / bi-encoder 表示。
3. [Precise Zero-Shot Dense Retrieval without Relevance Labels](https://arxiv.org/abs/2212.10496) · Gao et al., 2022（HyDE）。检查假设文档如何帮助 retrieval，以及假设本身的错误风险。
4. [ReAct: Synergizing Reasoning and Acting in Language Models](https://arxiv.org/abs/2210.03629) · Yao et al., 2022。对应 agent loop，区分 reasoning text、action 与 observation。
5. [Model Context Protocol: Architecture](https://modelcontextprotocol.io/docs/learn/architecture) · 官方协议文档。核对 client/server/host 边界；协议本身不是 agent 规划算法。

## 读后检查

画一条 RAG trace：query → retrieve → rank → context → answer；再画 tool-use trace：select → call → observe → respond。为每步写一个可能失败的检查点和指标。
