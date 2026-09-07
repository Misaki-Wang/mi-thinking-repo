# Readings guidance · Reinforcement learning 与 reasoning

以下优先级由学习档案建议。论文依据官方摘要及主来源身份核验；阅读任务要求你进一步检查原文方法与实验，并非本档案已完成复现。

## 1. Deep reinforcement learning from human preferences

[论文](https://arxiv.org/abs/1706.03741) · 基础。

带着“人如何表达复杂目标”阅读：比较的是两段 trajectory，而非逐动作正确标签。画出人类偏好 → reward model → policy update 的流程，记录反馈采样策略与 reward model 随策略分布变化的问题。将它映射到 LLM 后，说明 trajectory 变成什么、评价成本在哪里。

## 2. DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning

[论文](https://arxiv.org/abs/2501.12948) · 核心。

先区分纯 RL 探索与包含数据准备、SFT、蒸馏等步骤的完整系统，避免把整个 R1 系列简化成一条“只用 RL”的结论。检查哪些任务具有可验证答案，reward 如何定义，以及 group-based advantage 的实现。

记录三类证据：最终答案正确率、生成行为的变化、不同训练阶段/数据的消融。出现 self-reflection 的文本是可观察现象，不直接证明对内部推理机制的解释。

## 3. Faulty reward functions in the wild

[OpenAI 原文](https://openai.com/index/faulty-reward-functions/) · 必读反例。

阅读时将每个案例拆为 intended goal、proxy reward、可利用的环境细节与实际行为。核心不是给 reward hacking 贴标签，而是找出验证规则遗漏了什么。该项是官方案例文章，不是性能比较论文。

把本讲的图像计数任务代入：如果只奖输出格式、长度或某个容易识别的特征，模型可能如何提高分数但没有完成任务？为每个漏洞写一个 held-out 检查。

## 4. Direct Preference Optimization: Your Language Model is Secretly a Reward Model

[论文](https://arxiv.org/abs/2305.18290) · 核心对照。

重点检查从 KL-regularized reward objective 到 preference classification loss 的关系。记录 chosen/rejected responses、reference policy 与 beta 的作用；区分训练时不用 online sampling，与数据最初如何采集。

## 横向比较

| 方法 | 需要弄清的数据与模块 | 最关键的阅读问题 |
|---|---|---|
| 偏好 RL / PPO | preference pairs、reward model、policy、critic | policy 分布变化后 reward 是否可靠？ |
| GRPO / R1 场景 | 同 prompt 的多条 responses、verifier、组内 reward | 奖励全相同或被投机时如何发现？ |
| DPO | 静态 preference pairs、reference policy | 离线数据覆盖能否支持目标任务？ |

学习产物：为自己的多模态任务写一张 reward specification，给出 3 个能拿高奖励但不合目标的反例，以及如何在独立评估中发现。继续查看 [课程预览](preview.md)。
