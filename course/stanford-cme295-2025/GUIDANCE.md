# CME 295 Autumn 2025 · 全课学习路线

这门课适合沿着一条 LLM 生命周期主线来学：**表示输入 → 组织 Transformer 计算 → 预训练与适配 → 对齐偏好 → 扩展 reasoning → 连接工具与外部信息 → 评估可靠性 → 看向多模态与新架构**。

[回课程目录](README.md) · [官方 syllabus](https://cme295.stanford.edu/syllabus/2025/) · [Stanford Online playlist](https://www.youtube.com/playlist?list=PLoROMvodv4rOCXd21gf0CF4xr35yINeOy)

## 建议的四段学习路径

| 阶段 | 课程 | 关键问题 | 留下的笔记 |
|---|---|---|---|
| 1 · 表示与生成 | [Lecture 1](l01/preview.md), [2](l02/preview.md), [3](l03/preview.md) | token 如何变成向量与上下文表示？架构和 decoding 又如何决定输出？ | Attention 图解、RoPE/normalization 对照表、decoding 策略表 |
| 2 · 训练与偏好 | [Lecture 4](l04/preview.md), [5](l05/preview.md) | compute、数据和显存如何约束训练？偏好信号如何变成 policy update？ | 训练生命周期图、SFT/LoRA/QLoRA 对照、RLHF 与 DPO 数据流 |
| 3 · Reasoning 与行动 | [Lecture 6](l06/preview.md), [7](l07/preview.md) | 什么证据能说明 reasoning 变好？模型如何检索、调用工具并处理反馈？ | reward 设计风险表、RAG 指标表、tool-call / ReAct trace |
| 4 · 评估与边界 | [Lecture 8](l08/preview.md), [9](l09/preview.md) | 评测如何失真？模型如何扩展到视觉与 diffusion？ | Judge 偏差检查单、benchmark coverage matrix、期末概念图 |

Midterm 位于第 4 讲后，课件写明覆盖 Lectures 1–4；Final 在第 9 讲后，课件写明覆盖 Lectures 5–9。它们是 2025 syllabus 的历史安排，可用作自测分界。

## 每讲的观看与阅读方式

1. 先读预览中的“先抓住的问题”和术语，写下一个具体疑问。
2. 从视频章节链接跳到相关段落，同时打开同讲 slides；时间按 YouTube 播放位置。
3. 先尝试画出机制，再看 slides 中的图或公式检查。若文字层没有提取出某页内容，以 PDF 视觉内容为准。
4. 从 readings.md 选 1 篇补充阅读。syllabus 未提供逐讲指定书目，阅读优先级是本归档的建议。
5. 用一个失败案例收尾：写出方法会在哪个输入、计算约束或评估条件下失效。

整套录像约 16 小时；可以按四阶段推进，也可按每周 2–3 讲安排。时间规划是自学建议，不是 Stanford 官方进度。

## 术语记录建议

首次出现时保留英文原词并补中文解释，后续沿用同一拼写：MHA/MQA/GQA、RoPE、MoE、SFT、RLHF、PPO、DPO、GRPO、RAG、MCP、LLM-as-a-Judge、ViT。区分“训练目标”“推理策略”“系统优化”和“评估指标”，不要仅因名称相近就视为同一类方法。

## 可复用的每讲笔记

课程 / 讲次 / 日期：
我想回答的问题：
视频章节时间：
slides 页码：
机制图或关键公式：
这讲的最小例子：
方法依赖的假设：
可能失败的情况：
补充阅读及尚未核实的问题：

完成标准：能不看 slides 解释核心流程，能从原始资料定位术语，并能说出一个有效性边界。不要把 lecture preview 当成逐字讲稿。
