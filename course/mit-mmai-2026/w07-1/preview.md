# Midterm review · 把概念串成可解释的系统

2026-03-17 · Week 7.1 · 48 页复习 slides，未发现本课公开视频。

## 三分钟预览

复习重点不是背模型清单，而是从数据特性推到表示结构，再从训练目标推到能验证的能力。把此前的概念压缩成“输入是什么 → 模态如何相连 → 哪些信息需保留 → 如何生成或预测 → 如何证明有效”五步。

## 按 Slides 回顾

| 页码 | 复习主题 | 自己应能做什么 |
|---|---|---|
| [4–15](https://mit-mi.github.io/mmai-course/spring2026/schedule/lec7.1%20-%20midterm%20review.pdf#page=4) | modality、heterogeneity、modality profile | 描述结构、分布、噪声、信息与任务相关性 |
| [16–23](https://mit-mi.github.io/mmai-course/spring2026/schedule/lec7.1%20-%20midterm%20review.pdf#page=16) | invariance、fusion、tensor 与 gating | 根据任务选择不变性并标出交互项 |
| [24–28](https://mit-mi.github.io/mmai-course/spring2026/schedule/lec7.1%20-%20midterm%20review.pdf#page=24) | alignment、CLIP、multi-view redundancy | 解释正负对与任务信息的保留 |
| [29–37](https://mit-mi.github.io/mmai-course/spring2026/schedule/lec7.1%20-%20midterm%20review.pdf#page=29) | cross-attention、MLLM、适配与生成 | 追踪模块、参数与监督来源 |
| [38–46](https://mit-mi.github.io/mmai-course/spring2026/schedule/lec7.1%20-%20midterm%20review.pdf#page=38) | VAE、diffusion、flow matching | 区分训练目标、latent 与采样过程 |

## 五项检查

1. **概念能否用于新模态。** 用环境声音与温度序列替换图文，重新写 modality profile，而非机械套用 image encoder。
2. **模型中有没有交互。** 加性项、乘性交互项和输入相关的 gating 是不同机制。解释 tensor fusion 中附加常数 1 为什么能保留低阶项，并估算维度膨胀。
3. **目标函数偏好哪些信息。** 对比学习强调共享联系；当任务依赖某个模态独有的信息时，说明为什么仅提高跨模态相似度可能不足。
4. **输入与输出接口能否追踪。** 为 MLLM 标出 Q/K/V 的来源、adapter 的尺寸变化、冻结参数以及 instruction data。
5. **指标是否检验目标能力。** 能重建样本、能随机采样、能服从条件、能保持跨模态一致性，是需要分别测量的能力。

## 60 分钟自测建议

前 10 分钟闭卷定义 fusion、alignment、grounding、transfer；接着用 15 分钟推一个双模态 fusion 的形状与参数量；再用 15 分钟解释一个冻结 LLM 的视觉适配流程；最后 20 分钟比较 VAE / diffusion / flow matching 的训练与采样。这是个人复习建议，非官方试题。

Slides 第 3、47 页同时出现“6 problems”和“5 problems”，随后列出五类主问题及 bonus。此处保留该来源差异，不把它写成确定的考试规则；实际考试安排应以教师通知为准。

完成后查看 [复习 guidance](readings.md)。
