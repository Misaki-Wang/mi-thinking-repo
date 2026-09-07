# W13.2 · Readings guidance

## 官方安排与证据

[课程表](https://mit-mi.github.io/mmai-course/spring2026/schedule/)没有为本节指定 Readings。已核对[Transportation 讲义](https://mit-mi.github.io/mmai-course/spring2026/schedule/lec13.2%20-%20transportation.pdf)。下述为个人复习路径，讲义引用的研究不自动列为额外必读论文。

## 建议顺序

1. **优先：pp1–18，公交调度。** 提取 state、action、长期目标、现实 uncertainty。画出 AI recommendation 到 driver execution 的路径，再按 compliance 分组阅读结果；记录研究条件，不只记录改善百分比。
2. **核心：pp47–63，生成设计。** 对照三阶段 pipeline 的输入输出及人工介入。分别解释 FID、land-use ratio error、diversity、expert rating 能支持什么结论，不能支持什么结论。
3. **扩展：pp70–86，agency。** 将 planner 的 creator / critique / communicator / negotiator 角色与 AV 的 decision levels 并排看。回答：系统自动化更多之后，人保留的是操作权、目标设定权，还是仅承担责任？

## 本节交付物

一份 human-in-the-loop evaluation sheet：每个阶段写出模型输出、可执行性检查、人工修改入口、日志、结果指标。再为一项失败写出“数据问题、算法问题、执行不遵循、组织协调”四种不同解释，以及区分它们所需的证据。

自测：为什么 bus dispatch 的 recommendation quality 与 deployed outcome 不一样？为什么 no statistically significant difference 不能改写为“效果完全相同”？为什么生成 urban image 的视觉多样性不能保证政策选项具有多样性？
