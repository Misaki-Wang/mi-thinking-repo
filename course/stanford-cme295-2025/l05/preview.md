# Lecture 5 · LLM Tuning

- 课程日期：2025-10-31；视频时长：01:47:42。
- 来源：[官方 slides（111 页）](https://cme295.stanford.edu/slides/fall25-cme295-lecture5.pdf) · [Stanford Online 视频](https://www.youtube.com/watch?v=PmW_TMQ3l0I)。
- 补充：[Lecture 5 readings](readings.md) · [全课 Guidance](../GUIDANCE.md)。

> 预览依据 slides 与官方视频章节。重点是区分偏好数据、reward model、policy optimization 和直接偏好目标各自承担什么功能。

## 先抓住的问题

SFT 之后的模型已经会按指令生成，但用户偏好并非普通 next-token label。RLHF 如何把成对偏好变成 reward 再优化 policy？DPO 又怎样将偏好学习改写为直接训练目标？

## 本讲主线

- **Preference data**：Slides 6–22 从偏好 tuning 动机讲到成对比较数据，需关注标注对象、提示上下文和偏好判断边界。
- **RLHF 与 PPO**：Slides 23–82 讲 RL formulation、Bradley–Terry reward modeling、policy update、advantages、PPO-Clip/KL penalty 及 on/off-policy 问题。
- **不用显式 RL 的路线**：Slides 83–110 介绍 Best-of-N 和 DPO，并以何时选择 PPO 或 DPO 收尾；简单并不意味着没有数据或 reference-model 依赖。

## 视频章节与课件定位

- [00:04:50 · Preference tuning](https://www.youtube.com/watch?v=PmW_TMQ3l0I&t=290s) → [00:11:31 · Data collection](https://www.youtube.com/watch?v=PmW_TMQ3l0I&t=691s) — slides 6–22。
- [00:17:43 · RLHF overview](https://www.youtube.com/watch?v=PmW_TMQ3l0I&t=1063s) → [00:28:24 · Reward model](https://www.youtube.com/watch?v=PmW_TMQ3l0I&t=1704s) — slides 23–43。
- [00:46:02 · Reinforcement learning](https://www.youtube.com/watch?v=PmW_TMQ3l0I&t=2762s) → [00:53:54 · PPO](https://www.youtube.com/watch?v=PmW_TMQ3l0I&t=3234s) — slides 44–65。
- [01:03:39 · PPO variants](https://www.youtube.com/watch?v=PmW_TMQ3l0I&t=3819s) → [01:16:20 · Challenges](https://www.youtube.com/watch?v=PmW_TMQ3l0I&t=4580s) — slides 66–82。
- [01:19:58 · On-policy vs off-policy](https://www.youtube.com/watch?v=PmW_TMQ3l0I&t=4798s) → [01:22:43 · Best-of-N](https://www.youtube.com/watch?v=PmW_TMQ3l0I&t=4963s) — slides 83–92。
- [01:29:47 · DPO](https://www.youtube.com/watch?v=PmW_TMQ3l0I&t=5387s) — slides 93–110。

## 学习时可以追问

1. Preference labels 对应比较关系，不是客观效用值。Bradley–Terry modeling 加入了哪些假设？
2. PPO 中 reward model、reference policy、value function 分别是什么角色？KL penalty 缓和哪类偏离？
3. DPO 省去了显式 reward-model/RL loop，但依赖哪些 preference-pair 和 reference-policy 条件？
4. 当 preference data 有偏、reward 被投机或 response 分布变化时，指标应该如何监测？

## 术语与延伸阅读

保留 preference tuning、RLHF、reward model、Bradley–Terry、PPO、advantage、KL penalty、on-policy/off-policy、Best-of-N、DPO。补充原文见 [readings.md](readings.md)。
