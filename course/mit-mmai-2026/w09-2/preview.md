# Explainable reasoning · xHAIM 的证据链

2026-04-02 · Week 9.2 · 实际资料为 20 页 xHAIM 演示稿，未发现本课公开视频。这里按 PDF 页序导航，页脚编号并不总与 PDF 页数一致。

## 三分钟预览

本讲用多模态医疗预测展示“预测性能”和“解释质量”如何分别改进。xHAIM 先检索与任务相关的原始片段，再形成各模态摘要与 embedding；分类器负责预测，生成模型结合原始证据、摘要与预测组织解释。

## Slides 导航

| 页码 | 重点 | 预览问题 |
|---|---|---|
| [2–6](https://mit-mi.github.io/mmai-course/spring2026/schedule/lec9.2%20-%20explainable.pdf#page=2) | HAIM 与 zero-shot LLM 的局限 | 哪些信息被压缩或淹没？ |
| [7–13](https://mit-mi.github.io/mmai-course/spring2026/schedule/lec9.2%20-%20explainable.pdf#page=7) | 检索、摘要、embedding 与分类 | 每一步如何连接到目标任务？ |
| [14–19](https://mit-mi.github.io/mmai-course/spring2026/schedule/lec9.2%20-%20explainable.pdf#page=14) | 引证解释、预测与人工/LLM 评价 | 解释是否能追溯到原始证据？ |

## 六个关键点

1. **多模态输入不只包含图像与语言。** 表格、time series、影像和临床 notes 有不同信息密度。把它们全部拼接或全部写成文本，都可能把任务相关信息淹没在噪声中。
2. **retrieval 以任务为条件。** 第 9 页结合 embedding similarity 与 BM25 筛选文本片段。需要记录检索的目标句、候选池和 top-k，而不能把检索出的内容默认当成全面证据。
3. **摘要是有损表示。** 它可以过滤噪声，也可能遗漏否定、时间变化或相互矛盾的记录。保留摘要与原始片段的映射，才能审查信息损失。
4. **预测器与解释生成器职责不同。** 第 11–14 页将可训练的表示与分类器用于预测，再用生成模型组织解释。解释流畅本身不是分类器决策的因果证据。
5. **任务性质影响结果。** 第 15 页区分从当前记录可直接抽取的 pathology 与未来 outcome。更难的未来预测不能用已有诊断是否被引用来替代验证，且必须检查 prediction time 之后的信息泄漏。
6. **解释评价要分维度。** 引用质量、事实正确性、整体表达质量分别检查。人工标注与 LLM-as-a-Judge 的一致性需要在具体样本和 rubric 上衡量，不能保证跨任务长期有效。

## 如何读结果图

PDF 第 16 页显示多项任务的 ROC AUC；例如 Length of Stay 的 HAIM 为 75.5、zero-shot LLM 为 44.7、xHAIM 为 77.7。这里的对比提示“能生成解释”不保证预测强。数字只代表该讲义中的实验；不要跨任务平均后宣称通用改进，也不要把 ROC AUC 当准确率。该页柱状图已经视觉核对。

## 自测与练习

给一段包含互相矛盾时间记录的虚构 notes，制作“结论 → 引用片段 → 时间 → 支持/反对”的证据表。分别判断结论是否准确、引用是否有效、解释是否忠实于模型依据。此练习只用于方法理解。

本讲课表没有指定 Readings，见 [复习 guidance](readings.md)。
