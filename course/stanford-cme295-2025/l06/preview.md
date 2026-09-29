# Lecture 6 · LLM Reasoning

- 课程日期：2025-11-07；视频时长：01:47:10。
- 来源：[官方 slides（148 页）](https://cme295.stanford.edu/slides/fall25-cme295-lecture6.pdf) · [Stanford Online 视频](https://www.youtube.com/watch?v=k5Fh-UgTuCo)。
- 补充：[Lecture 6 readings](readings.md) · [全课 Guidance](../GUIDANCE.md)。

> 本讲 slides 包含多代 reasoning model 与 RLVR 例子。具体模型展示属于 2025 课程材料，不应当作当前 leaderboard 或今天最新的模型结论。

## 先抓住的问题

LLM 在可验证任务上如何通过额外推理计算提升表现？从 prompting 到 test-time scaling，再到 RL with verifiable rewards，收益和新 failure modes 分别是什么？

## 本讲主线

- **Reasoning 证据与指标**：Slides 15–47 讨论 reasoning traces、benchmark 及 pass@k。区分答案通过率与推理过程正确性。
- **Test-time scaling / RLVR**：Slides 48–68 从增加推理预算走到以可验证结果设计 reward；reward 设计若只检查 CoT 格式，可能与任务正确性脱钩。
- **GRPO、PPO 与长度偏置**：Slides 69–115 比较 group-relative update 与 PPO，并讨论输出长度增长、reward design 与变体。
- **DeepSeek R1 案例与 distillation**：Slides 116–147 将 R1-Zero、R1 的训练路径和蒸馏放在同一段落，适合当作案例逐项追踪数据、reward 和模型变化。

## 视频章节与课件定位

- [00:12:43 · Reasoning models](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=763s) — slides 15–30。
- [00:27:49 · Benchmarks](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=1669s) → [00:32:04 · Pass@k](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=1924s) — slides 31–47。
- [00:48:07 · Scaling with RL](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=2887s) → [00:57:44 · GRPO](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=3464s) — slides 48–72。
- [01:06:03 · GRPO vs PPO](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=3963s) → [01:16:14 · Length bias](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=4574s) — slides 73–115。
- [01:25:00 · DAPO / Dr. GRPO](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=5100s) — slides 106–115。
- [01:29:38 · DeepSeek R1 recipe](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=5378s) — slides 116–147。

## 学习时可以追问

1. 对一个 math/coding task，哪些结果可验证？验证器不完善时会引入什么 reward hacking？
2. pass@k 衡量的是单次采样能力、搜索预算，还是二者混合？不同预算间如何公平比较？
3. GRPO 避免显式 value model 的系统成本与 PPO 的 critic 有何比较边界？
4. 输出变长可能意味着搜索更充分，也可能只是长度 reward；如何区分？

## 术语与延伸阅读

保留 reasoning model、RLVR、pass@k、test-time scaling、GRPO、PPO、length bias、DAPO、Dr. GRPO、distillation。论文入口见 [补充阅读](readings.md)。
