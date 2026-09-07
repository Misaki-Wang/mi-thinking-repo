# Readings guidance · Explainable reasoning

官方课表本讲没有单独指定 Readings。以下使用本讲实际 xHAIM slides 作为主阅读材料，不把演示稿里的参考文献自动升级成官方必读。

## 逐段精读

1. **问题与 baseline，PDF 第 2–6 页。** 分开记录原始 HAIM 的 embedding fusion 与 zero-shot LLM；两者缺什么监督、在哪里压缩数据？不要以模型名称代替数据路径。
2. **任务相关信息处理，第 7–13 页。** 画出 task query、检索片段、各模态摘要、ClinicalBERT/其他 embedding、分类器。给每条箭头写一个可能的信息损失或 leakage 风险。
3. **解释生成，第 14、19 页。** 对照一个例子，将解释中的每个事实链接回带日期的原始片段；寻找反证与遗漏。引用真实片段只是必要条件，还要检查结论是否被支持。
4. **评价，第 15–18 页。** 区分 pathology extraction 与 future outcome prediction；分别记录 ROC AUC、citation、factuality、quality。核对人工评价样本与 LLM judge 的使用范围。

[打开官方 slides](https://mit-mi.github.io/mmai-course/spring2026/schedule/lec9.2%20-%20explainable.pdf)

## 阅读时的关键分界

“解释引用正确”“解释符合事实”“解释反映预测器真实决策依据”是三个问题。前两项好并不自动证明第三项。应提出移除证据、替换关键内容、保留反证等有控制的检查，而非仅让同一个 LLM 再评价自己的解释。

建议产物：一张 claim–evidence 表、一个时间线、一个预测模型与解释模型的分工图，以及尚未验证的 fidelity 假设。回到 [本讲预览](preview.md)。
