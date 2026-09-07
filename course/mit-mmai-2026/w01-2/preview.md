# W01-2 · Multimodal datasets：把兴趣变成可检验的问题

本节的重点不是背诵数据集名单，而是让任务、数据、假设和评价互相匹配。Slides 先讨论如何提出研究问题，再用医疗、感知、推理、网页代理、社会智能和具身任务展示不同实验条件，最后落到一个可运行的最小研究流程。

整理依据为 Slides 与公开视频的英文自动字幕；时间链接定位到相关字幕片段起点，技术名词结合 Slides 校对。条件化实验与自测是学习建议，并非课程已经验证的结果。

## 七个预习重点

1. **研究可以从失败出发，也可以从能力目标出发。** Bottom-up discovery 先运行已有模型、分类错误，再提出改进；top-down design 先问希望系统具备什么能力，再寻找能检验它的数据。视频具体区分“解决一个现存短板”和“从较大愿景拆成步骤”的取舍。前者容易局部优化，后者容易离开可实现条件，好的项目让两条路径反复相遇。[Slides p3–6](https://mit-mi.github.io/mmai-course/spring2026/schedule/lec1.2%20-%20data.pdf#page=3) · [视频 04:43](https://www.youtube.com/watch?v=zlTCAER4z9A&t=283s)

2. **“加 X 是否更好”还不够可诊断。** Research hypothesis 应包含机制及失败条件。例如“音频能帮助文本模糊的情绪样本”比“音频提高准确率”更具体：如果文本已经足够，收益理应较小；如果音频错配，收益应下降。视频将 hypothesis 定义为实验前的潜在答案，并要求存在可以否定它的实验。这样的条件预测帮助区分模型问题和假设错误。[Slides p7–10](https://mit-mi.github.io/mmai-course/spring2026/schedule/lec1.2%20-%20data.pdf#page=7) · [视频 09:18](https://www.youtube.com/watch?v=zlTCAER4z9A&t=558s)

3. **新模态首先带来测量问题。** 嗅觉、触觉、临床记录与制造传感器的价值，来自它们能观察到不同的物理或行为因素；同时也改变采集成本、隐私、侵入性与时间分辨率。Slides 中的 SmellNet、OpenTouch 和工业案例应被当成“任务如何由传感方式塑造”的例子。[Slides p15–23](https://mit-mi.github.io/mmai-course/spring2026/schedule/lec1.2%20-%20data.pdf#page=15)

4. **数据集决定能否检验 compositionality。** 普通 caption 或 VQA 可能允许依赖常见对象；Winoground 用词相同、顺序不同的图文组合检验关系；视频举出“植物围住灯泡”与“灯泡围住植物”的交换。PuzzleWorld 将视觉识别、外部知识与文字操作连接成解题步骤。选 benchmark 时要追问：失败可以定位到哪一步？[Slides p28–36](https://mit-mi.github.io/mmai-course/spring2026/schedule/lec1.2%20-%20data.pdf#page=28) · [视频 47:47](https://www.youtube.com/watch?v=zlTCAER4z9A&t=2867s)

5. **Agent 任务把输出从答案变成行动。** WebQA 需要选择证据并回答，WebArena 还要改变环境；VisualWebArena 增加视觉条件，VideoWebArena 再增加视频理解。HTML 不一定保留实际布局、动态交互与视觉线索，视频进一步解释截图与 accessibility tree 的作用，评价也必须检查最终环境状态。[Slides p37–46](https://mit-mi.github.io/mmai-course/spring2026/schedule/lec1.2%20-%20data.pdf#page=37) · [视频 1:00:20](https://www.youtube.com/watch?v=zlTCAER4z9A&t=3620s)

6. **社会与具身任务需要明确观察范围。** 情绪片段、多人对话、跨场景意图和机器人控制所需的时间跨度不同。MimeQA 的对象、场景和全局判断说明，答对一个局部问题不能推出长期社会理解；具身模型还必须将感知连接到动作及其后果。[Slides p47–62](https://mit-mi.github.io/mmai-course/spring2026/schedule/lec1.2%20-%20data.pdf#page=47)

7. **最小流程要先于大规模实验。** 本节建议先完成数据读取、基础模型、评价与可视化，再一次改变一个组件，最后做规模扩展、消融和定性比较。视频数据还受磁盘、内存与特征提取时间约束，小子集能先暴露流程错误。[Slides p65–69](https://mit-mi.github.io/mmai-course/spring2026/schedule/lec1.2%20-%20data.pdf#page=65)

## 将假设翻译成实验

一个学习用结构是：`H：模态 B 能补充 A 缺失的信息 → 分组：A 足够 / A 模糊 → 对照：A、B、A+B、A+错配 B → 检查各组表现和错误`。总体增益可以写成 `Δ = score(A+B) − score(A)`，但这个差值本身不能说明协同，也不能排除数据量、参数量或泄漏的作用；因此需要上述分组和对照。

## 来源导航

| 预习目标 | 定位 |
| --- | --- |
| 写一个可证伪的研究问题 | [Slides p3–10](https://mit-mi.github.io/mmai-course/spring2026/schedule/lec1.2%20-%20data.pdf#page=3) |
| 按能力选择数据集 | [Slides p15–64](https://mit-mi.github.io/mmai-course/spring2026/schedule/lec1.2%20-%20data.pdf#page=15) |
| 将想法接到最小实现 | [Slides p65–69](https://mit-mi.github.io/mmai-course/spring2026/schedule/lec1.2%20-%20data.pdf#page=65) |
| 对照讲解和文献 | [官方视频](https://www.youtube.com/watch?v=zlTCAER4z9A) · [Reading guidance](readings.md) |

## 容易混淆的地方

更大数据集不一定更适合回答问题；一个更真实的环境也不一定更容易定位错误。课件中的数据集规模和模型表现是讲课时引用的背景，不能直接当成当前 leaderboard。选择项目时，要同时记录观察单位、划分单位和部署单位，尤其避免把同一人的相邻视频片段随机分到训练与测试。

## 自测与动手

1. “模型 X 在数据集 Y 上更好”缺少哪些信息，才成为研究假设？
2. 如果只提高了常见样本准确率，能否支持“组合推理增强”的结论？
3. 一个视频问答系统与一个视频网页代理，评价终点分别是什么？

动手：从课件中选两个数据集，制作一张比较表，写明模态、样本与标签粒度、预期任务、可能的捷径、资源成本。选一个完成 20 个样本的人工检查，并写出一个反例驱动的假设。
