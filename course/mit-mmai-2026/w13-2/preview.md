# W13.2 · Multimodal & transportation

2026-04-30 · Jinhua Zhao 及合作者 · 约 3 分钟预览

## 来源与阅读范围

依据 86 页[Transportation 讲义](https://mit-mi.github.io/mmai-course/spring2026/schedule/lec13.2%20-%20transportation.pdf)整理；未找到本节公开 video。它接续上一节，主要覆盖 **bus dispatching、generative urban design、human agency**，并非一套 autonomous driving perception 教程。以下使用 PDF 页码，原讲义内编号从前一部分继续累加。

## 先抓住主线

同样的 AI 能力，放进真实交通系统后会受到执行者、公共目标和组织流程制约。讲义先看 RL 公交调度：系统给出建议，司机和运营人员决定如何落实；再看城市生成设计：模型逐阶段提出方案，规划师保留修改和评议空间；最后讨论 Autonomous Vehicles（AV）的控制权分配。共同问题是“算法做什么决定，人又在哪里介入”。

## 七个关键点

1. **Bus bunching 是连续决策问题。** 在 terminal 提前或延后发车会改变后续车距和乘客等待；Reinforcement Learning（RL）需要考虑行动的长期影响。讲义列出 demand、supply、traffic、compliance 和 information 五类 uncertainty。
2. **Human-in-the-loop 是实际信息流。** 实时车辆与预测信息进入系统，RL / rule-based 模块形成建议，经过 action filtering 和界面传给人员；评价既要看算法推荐，也要看执行发生了什么。
3. **Compliance 影响效果。** 讲义的 field study 中，激进程度与司机遵循建议有关，并按信息问题、non-compliant / compliant trips 分组报告结果。不能只引用总体等待改善值，而忽略这些不同执行条件。
4. **Generative planning 要保持空间约束。** 用文字指定 land-use ratios，同时用图像表达 roads、railways、water 等已有条件。ControlNet 提供空间条件控制；一张逼真图像还需检验是否满足指定比例和基础设施约束。
5. **分阶段生成提供人类决策点。** 讲义采用 road network / land use → building layout → detailed rendering。每一阶段的输出成为下一阶段条件，人在阶段之间可检查与修改，避免最后才发现上游规划错误。
6. **Evaluation 至少有四面。** Visual fidelity（如 FID）、instruction compliance、output diversity 和 user study 回答不同问题。FID 衡量生成图像分布接近程度，不是 zoning compliance；用户研究“无显著差异”也不是统计等价性证明。
7. **AV agency 跨越多层行动。** 加减速、route / departure time、destination / ownership 处在不同层级；消费者、运营方、车厂、公共机构在正常和紧急情境下的权限也可能不同。讲义用 agency frontier 与 command matrix 引导分析。

## 原文导航

- [pp1–18：公交 RL 调度、field deployment 与 compliance](https://mit-mi.github.io/mmai-course/spring2026/schedule/lec13.2%20-%20transportation.pdf#page=1)
- [pp23–42：规划师需求、ControlNet 与约束](https://mit-mi.github.io/mmai-course/spring2026/schedule/lec13.2%20-%20transportation.pdf#page=23)
- [pp47–54：三阶段生成与评价指标](https://mit-mi.github.io/mmai-course/spring2026/schedule/lec13.2%20-%20transportation.pdf#page=47)
- [pp62–73：用户研究、stepwise 对照与规划师角色](https://mit-mi.github.io/mmai-course/spring2026/schedule/lec13.2%20-%20transportation.pdf#page=62)
- [pp75–86：AV 控制权与沟通](https://mit-mi.github.io/mmai-course/spring2026/schedule/lec13.2%20-%20transportation.pdf#page=75)

## 易混点与边界

“Control”在 RL 中是环境动作，在 ControlNet 中是生成条件，两者概念不同。人能点击确认不代表拥有充分信息或真实的否决权。讲义的 field results、design experiments 与未来职业讨论也应分开：前两者是具体设置下的证据，后者是需要继续讨论的影响判断。

对照两个案例时，还要区分时间尺度：发车建议很快影响乘客等待，规划方案可能多年后才影响出行。它们都需要反馈，但适合的试验方式、错误恢复成本和公众参与形式并不相同。

## 自测与小练习

选一个 1 km² 的虚构街区，只做纸面方案。写明不能改变的河道与道路、目标 land-use ratios、建筑覆盖率；拆成三个生成阶段，给每阶段一个机械检查和一个 human judgment。然后做一张 command matrix：正常运行、目标冲突、紧急情况时，谁能修改方案、谁审批、谁承担错误？

接着看[阅读与复习 guidance](readings.md)。
