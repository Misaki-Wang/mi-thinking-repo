# W13.1 · Multimodal & cities

2026-04-28 · Jinhua Zhao · 约 3 分钟预览

## 来源与阅读范围

依据 78 页[**AI for Cities and Mobility** 讲义](https://mit-mi.github.io/mmai-course/spring2026/schedule/lec13.1%20-%20cities.pdf)整理。未找到本节公开课程 video，因此本页是 slides summary。实际材料比课程表的 “spatial and temporal fusion” 更宽，重点在城市目标、交通行为、Grounded AI 和模型解释。

## 先抓住主线

城市 AI 的成功必须先由人的出行需求和公共目标定义。技术进步不自动转化为更安全、更公平、更低排放的 mobility system。讲义用 **Behavior + Computation** 连接行为选择与数据计算：同一个城市可以被表示成 images、language、graphs、numbers，但这些只是同一现实的不同投影。融合它们的目的，是支持具体的预测、解释、控制、创造与公共沟通，而不是单纯追求统一表示。

## 七个关键点

1. **先问 What is success。** 拥堵、道路安全、交通排放和可负担性对应不同目标；单一速度指标可能无法覆盖它们。讲义中的历史统计有明确年份，应理解为问题动机，不当成当前实时统计。
2. **Transportation system 包含利益相关者。** Individuals、business、government、civil society 与 vehicles、energy、infrastructure 一起构成系统。预测乘客需求时，票价、制度和行为偏好并不是可以忽略的背景。
3. **Data fusion 跨越测量过程。** Smart-card transactions、vehicle location、mobile traces、surveys、complaints 各记录不同人群和行为切面。以 TfL 为例，讲义讨论从 manual survey 到 Oyster-centric analytics，再到 multimodal fusion，以及从 historical 到 real-time / predictive 的转变。
4. **GLIN 是认识城市的入口。** Graphs 表示交通或基础设施网络，language 承载历史和意见，images 展示空间形态，numbers 记录人口和经济量。能把它们放进 DNN，不代表各种信息的价值、噪声和分辨率已经一致。
5. **城市规划具有 wicked problem 特征。** 问题表述可能变化，方案没有简单的对错和终止准则，一次实施会改变城市本身。因此不能把 planning 等同于固定 benchmark 上寻找最高分答案。
6. **Grounded AI 把部署情境写进方法。** 讲义强调真实需求、institutional context、human agency、可部署性及与 stakeholders 迭代合作。对一个模型要追问：谁受益、谁承担错误、谁保有决定权？
7. **Domain theory 与 ML 可形成互补。** Discrete Choice Models（DCM）提供行为结构，Deep Neural Networks（DNN）增加表达能力；讲义以 Theory-Based Residual Neural Network（TB-ResNet）说明连接方向。预测、解释、robustness、sparsity 和 practicality 都是模型评价维度。

## 原文导航

- [pp7–23：成功标准与 Behavior + Computation](https://mit-mi.github.io/mmai-course/spring2026/schedule/lec13.1%20-%20cities.pdf#page=7)
- [pp27–39：stakeholders、交通数据与融合](https://mit-mi.github.io/mmai-course/spring2026/schedule/lec13.1%20-%20cities.pdf#page=27)
- [pp40–49：GLIN、城市多视角与 wicked problem](https://mit-mi.github.io/mmai-course/spring2026/schedule/lec13.1%20-%20cities.pdf#page=40)
- [pp60–64：AI function / human role 与 Grounded AI](https://mit-mi.github.io/mmai-course/spring2026/schedule/lec13.1%20-%20cities.pdf#page=60)
- [pp68–77：domain models 与 ML 的 tension / synergy](https://mit-mi.github.io/mmai-course/spring2026/schedule/lec13.1%20-%20cities.pdf#page=68)

## 易混点与边界

这里 multimodal 既涉及数据模态，也涉及多种交通方式，两者要按语境区分。城市的 image realism 不等于规划合理性；individualized service 也不天然带来公平。讲义中 DNN 与 DCM 的对比是教学概括，不应推断每种 DNN 都不可解释或每种理论模型都稳健。

阅读时可用同一个例子检查目标：模型预测某站客流少，是关于既有供给条件下的观察；据此取消服务，则会改变居民未来可选择的出行方式。前一个结果不能独自决定后一个动作，需要把行为响应和受影响人群带回分析。

## 自测与小练习

选择本地一条公交线路，做一张 GLIN evidence card：线路 graph、站点 image、投诉 language、客流 numbers。为每类源写出一项覆盖偏差。再选择“减少等待”或“改善弱势人群可达性”中的一个目标，说明谁定义它、哪些数据不足、谁能否决模型建议，以及怎样检验部署后的副作用。

接着看[阅读与复习 guidance](readings.md)。
