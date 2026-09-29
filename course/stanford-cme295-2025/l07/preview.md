# Lecture 7 · Agentic LLMs

- 课程日期：2025-11-14；视频时长：01:49:23。
- 来源：[官方 slides（151 页）](https://cme295.stanford.edu/slides/fall25-cme295-lecture7.pdf) · [Stanford Online 视频](https://www.youtube.com/watch?v=h-7S6HNq0Vg)。
- 补充：[Lecture 7 readings](readings.md) · [全课 Guidance](../GUIDANCE.md)。

> 预览依据课件和公开视频章节目录。课件把 RAG、tool calling、MCP、ReAct/A2A 放在“agents”主题下，概念相连但不是同一技术层。

## 先抓住的问题

LLM 何时需要外部资料，何时需要调用工具？RAG 改善 retrieval-grounded response；tool calling 连接外部函数；agent loop 则反复观察、规划和行动。把这些层次拆开，才容易定位失败点。

## 本讲主线

- **RAG 与检索评估**：Slides 10–77 从知识库构建、candidate retrieval、BM25/embeddings、reranking 到 RR@k 等检索指标。
- **Function calling 与 protocol**：Slides 78–115 说明函数 schema、tool selection、MCP 的标准接口动机。
- **ReAct、多 Agent 与安全**：Slides 116–150 进入 observation/action loop、跨 agent 协议 A2A、hallucination 和安全风险。

## 视频章节与课件定位

- [00:06:38 · RAG overview](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=398s) — slides 10–35。
- [00:27:39 · SBERT retrieval](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=1659s) → [00:34:25 · BM25](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=2065s) — slides 36–47。
- [00:37:54 · HyDE and contextual retrieval](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=2274s) → [00:47:49 · Retrieval metrics](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=2869s) — slides 48–77。
- [00:59:28 · Tool calling](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=3568s) — slides 78–106。
- [01:26:22 · Tool selection](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=5182s) → [01:29:17 · MCP](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=5357s) — slides 107–115。
- [01:31:56 · ReAct agents](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=5516s) → [01:42:16 · Safety](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=6136s) — slides 116–150。

## 学习时可以追问

1. Retrieval 评价里的 recall@k、MRR、NDCG 分别奖励什么？它们与最终回答正确率是否相同？
2. Tool calling 如何约束模型输出与真实函数 schema？错误可发生在选择工具、构造参数、执行工具或解释返回值的哪一步？
3. MCP 标准化了何种 client/server 交互？它本身是否定义了 agent 的任务规划？
4. ReAct trace 能显示外显行动序列；它对模型内部“真正推理”能说明到什么程度？

## 术语与延伸阅读

保留 RAG、BM25、SBERT、HyDE、reranking、MRR、NDCG、function calling、MCP、ReAct、A2A。推荐入口见 [补充阅读](readings.md)。
