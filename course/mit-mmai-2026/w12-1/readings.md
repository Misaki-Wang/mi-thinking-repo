# W12.1 · Readings guidance

## 官方安排与证据

[课程表](https://mit-mi.github.io/mmai-course/spring2026/schedule/)没有为本节指定 Readings。已核对[PNN 讲义](https://mit-mi.github.io/mmai-course/spring2026/schedule/lec12.1%20-%20prescriptive.pdf)；其参考文献是追溯方法的线索，不在这里扩写为官方必读清单。

## 建议顺序

1. **优先：pp3–10，定义 counterfactual gap。** 把 observed outcome 与 estimated counterfactual 分开标记，写明 `x / t / y / Γ`。回答：为什么普通 regression 的好预测不能直接保证 intervention 的好效果？
2. **核心：pp12–16，复算 policy loss。** 对照 indicator policy 与 softmax relaxation，手算讲义小表中的一个样本贡献。记录 optimization 使用的 Γ 从何而来、输出概率如何转换为动作；连续 action 的具体实现若源中未说明，应标成待查。
3. **审读实验：pp17–23。** 只选一个案例，保留 estimator × modality × model 条件，抄出评价目标及 train/test procedure。检查 outcome 的正负方向、relative improvement 的分母，以及 uncertainty 表示什么；源中没有定义的细节不自行补齐。

## 本节交付物

一张 evidence chain：`观察数据 → outcome/propensity models → Γ → policy → test evaluation`。每条箭头写一种误差传播方式。再对 Mirrored OCT 写两个独立指标：对 PNN 的 agreement 与 estimated policy outcome；不要用其中一个替代另一个。

自测：如果一个 treatment 几乎从未用于某类人群，Γ 的该列有什么风险？如果树完美模仿 PNN，是否证明了 causal validity？以上顺序为个人学习建议，适用于理解方法，不构成实际治疗决策流程。
