# Multimodal reasoning · 从问题结构到 RL

2026-03-31 · Week 9.1 · 来源：64 页 slides + 视频字幕。

## 三分钟预览

推理（reasoning）需要把知识和多个步骤联系起来。前半讲区分问题结构、中间概念、推断规则与外部知识；后半讲把语言模型视为策略，用 reward、baseline、advantage 来解释从 REINFORCE 到 PPO / GRPO 的训练思路。

## 来源导航

| 主题 | Slides | 视频 |
|---|---|---|
| 多步推理与组合泛化 | [第 6–19 页](https://mit-mi.github.io/mmai-course/spring2026/schedule/lec9.1%20-%20reasoning.pdf#page=6) | [10:42 起](https://www.youtube.com/watch?v=Vhe_bX8mV2s&t=642s) |
| state、action、policy 与 return | [第 20–26 页](https://mit-mi.github.io/mmai-course/spring2026/schedule/lec9.1%20-%20reasoning.pdf#page=20) | [37:35 起](https://www.youtube.com/watch?v=Vhe_bX8mV2s&t=2255s) |
| baseline 与 advantage | [第 35–38 页](https://mit-mi.github.io/mmai-course/spring2026/schedule/lec9.1%20-%20reasoning.pdf#page=35) | [56:33 起](https://www.youtube.com/watch?v=Vhe_bX8mV2s&t=3393s) |
| PPO / GRPO 的现代语言模型用法 | [第 39–49 页](https://mit-mi.github.io/mmai-course/spring2026/schedule/lec9.1%20-%20reasoning.pdf#page=39) | [62:52 起](https://www.youtube.com/watch?v=Vhe_bX8mV2s&t=3772s) |

## 理解顺序

1. **先定义什么算推理成功。** 同样对象更换关系或次序后，模型是否仍能区分？组合泛化（compositional generalization）比识别熟悉名词更接近本讲的问题。
2. **推理方法有不同监督条件。** prompting 不更新权重；SFT 需要示范；RL 依赖可评价结果的 reward。并非任何任务都有便宜、准确的 verifier。
3. **把 LLM 映射到序列决策。** state 是当前上下文，action 是下一 token 或工具行动，policy 给出行动分布，return 衡量累积奖励。这种映射帮助解释为什么只看当前 token 的局部质量不够。
4. **advantage 是相对基线的收益。** `A(s,a) = Q(s,a) - V(s)`。奖励绝对大小不直接告诉我们当前行动比通常选择好多少；baseline 有助于降低估计方差。
5. **PPO 约束更新幅度。** slides 将其概括为 clipping；严谨理解应聚焦 policy probability ratio 的 surrogate objective，不能把 PPO 等同于普通 gradient clipping。
6. **GRPO 用组内比较估计优势。** 一组回答的奖励提供相对标准，可免去单独训练 value critic。R1 例子使用规则验证，不意味着所有 GRPO 实现都必须弃用 reward model。
7. **DPO 是另一种偏好优化路径。** 第 49 页强调静态偏好对与较简洁的训练，不需要把在线采样、reward model 和 critic 都引入训练环。应比较数据覆盖与探索，而非只比较算法名字。

## 多模态案例与局限

第 50–61 页展示 clinical reasoning 的模态接入、奖励组成及 domain-aware weighting。重点是发现容易且丰富的样本可能主导训练，并检查稀缺模态是否有单独评估。学习案例不构成临床使用建议；也不能用长 reasoning trace 替代对答案和视觉证据的检查。

## 自测与练习

为一个图像计数任务定义 outcome reward、格式约束和 held-out evaluation。写出一种可能的 reward hacking，再说明如何修改评估发现它。另用同一组回答比较“绝对奖励排序”和“组内 advantage”，解释相同均值或全同奖励会发生什么。

继续阅读 [本讲 Readings guidance](readings.md)。
