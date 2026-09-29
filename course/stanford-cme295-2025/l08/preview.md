# Lecture 8 · LLM Evaluation

- 课程日期：2025-11-21；视频时长：01:49:25。
- 来源：[官方 slides（170 页）](https://cme295.stanford.edu/slides/fall25-cme295-lecture8.pdf) · [Stanford Online 视频](https://www.youtube.com/watch?v=8fNP4N46RRo)。
- 补充：[Lecture 8 readings](readings.md) · [全课 Guidance](../GUIDANCE.md)。

> 预览依据官方课件和 Stanford Online 视频章节。评估规则需要配合目标任务与判定流程，单个 benchmark 分数不能代表完整系统质量。

## 先抓住的问题

当系统没有唯一标准答案时，怎么评价模型？本讲从人评与 lexical overlap metrics 走到 LLM-as-a-Judge，再讨论 position/verbosity/self-enhancement bias、factuality、agent evaluation 和 benchmark coverage。

## 本讲主线

- **评价指标有取舍**：Slides 8–38 讨论 human ratings、METEOR/BLEU/ROUGE 及其与语义质量的落差。
- **LLM-as-a-Judge 的条件**：Slides 39–83 讲结构化输出、judge variants、常见偏差和 workflow best practices。
- **从答案到 Agent**：Slides 84–135 讨论 factuality、tool/agent failure modes；slides 136–169 用 MMLU、AIME、PIQA、SWE-bench、HarmBench、τ-bench 等示例说明基准覆盖。

## 视频章节与课件定位

- [00:07:08 · Inter-rater agreement](https://www.youtube.com/watch?v=8fNP4N46RRo&t=428s) → [00:18:24 · Rule-based metrics](https://www.youtube.com/watch?v=8fNP4N46RRo&t=1104s) — slides 8–38。
- [00:28:00 · LLM-as-a-Judge](https://www.youtube.com/watch?v=8fNP4N46RRo&t=1680s) → [00:38:47 · Judge biases](https://www.youtube.com/watch?v=8fNP4N46RRo&t=2327s) — slides 39–72。
- [00:47:22 · Best practices](https://www.youtube.com/watch?v=8fNP4N46RRo&t=2842s) — slides 73–83。
- [00:54:06 · Factuality](https://www.youtube.com/watch?v=8fNP4N46RRo&t=3246s) → [01:00:15 · Agent evaluation](https://www.youtube.com/watch?v=8fNP4N46RRo&t=3615s) — slides 84–135。
- [01:23:50 · Benchmarks](https://www.youtube.com/watch?v=8fNP4N46RRo&t=5030s) — slides 136–169。

## 学习时可以追问

1. BLEU/ROUGE 这类 reference-overlap metrics 在哪些任务上与人类判断相关？何时会惩罚合理的改写？
2. Judge 的 position bias、verbosity bias 和 self-enhancement bias 如何设计对照来发现？
3. Benchmark 名称覆盖 knowledge、math、coding、safety、agents；你的目标系统最可能漏掉哪类真实使用风险？
4. Agent evaluation 为什么需要记录 tool failure 与环境结果，而不只是模型最后的文字回答？

## 术语与延伸阅读

保留 inter-rater agreement、BLEU、ROUGE、METEOR、LLM-as-a-Judge、position bias、verbosity bias、factuality、benchmark contamination、SWE-bench、HarmBench、τ-bench。原论文/benchmark 入口见 [补充阅读](readings.md)。
