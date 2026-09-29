# Lecture 5 · 补充阅读：偏好数据、RLHF 与 DPO

沿着 pipeline 阅读：先看偏好数据，再看 reward modeling 和 policy optimization。

## 建议顺序

1. [Training Language Models to Follow Instructions with Human Feedback](https://arxiv.org/abs/2203.02155) · Ouyang et al., 2022。对应 RLHF overview；留意 SFT、human preference modeling 和 PPO 的先后关系。
2. [Proximal Policy Optimization Algorithms](https://arxiv.org/abs/1707.06347) · Schulman et al., 2017。对应 PPO；读 clipped objective 限制 policy update 的动机。
3. [Direct Preference Optimization: Your Language Model Is Secretly a Reward Model](https://arxiv.org/abs/2305.18290) · Rafailov et al., 2023。对应 slides 93–106；确认 DPO 的 preference-pair/reference-policy 设定。
4. [RewardBench: Evaluating Reward Models for Language Modeling](https://arxiv.org/abs/2403.13787) · Lambert et al., 2024。课件用于 reward model evaluation；关注 benchmark 覆盖而非榜单排名。

## 读后检查

画出 RLHF 与 DPO 的训练组件图，列出每条路线需要的数据、模型、副本和 reward 信号。算法流程更简洁，不代表 preference data 的质量要求消失。
