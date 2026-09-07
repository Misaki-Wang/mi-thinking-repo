# W10.1 · Multimodal interaction

2026-04-07 · Paul Liang · 约 3 分钟预览

## 来源与阅读范围

已核对 54 页[Interactive Agents 讲义](https://mit-mi.github.io/mmai-course/spring2026/schedule/lec10.1%20-%20interaction.pdf)，并用[课程视频](https://www.youtube.com/watch?v=Sk_TYpA6DWA)的英文字幕定位核心段落。PDF 封面误写 Lecture 10.2；此处按官方课程表保留 W10.1。字幕属于 YouTube 自动字幕，专名以 slides / paper 标题校正，不视为人工审校稿。

## 先抓住主线

Interactive agent 不只预测一个答案，还要在环境里行动、观察变化、修订后续计划。讲义把 GUI grounding、high-level planning、low-level action generation、human clarification、search 和 memory 串成一个闭环。最关键的转变是：评价目标从“输出是否像正确答案”变成“环境中的任务是否完成”。多模态的价值在于补足网页颜色、图片和空间布局等纯 HTML 不充分表达的信息。

## 七个关键点

1. **Model、workflow、interaction 是不同维度。** 基础 LLM / VLM 提供能力，tools、APIs、memory 构成外部 workflow；与人的分工从人工参与到更高自治程度。不能仅凭用了多个工具就判断系统具有可靠 planning。
2. **HTML 不是完整的视觉环境。** 原始源码可能冗长，布局与动态呈现也难以直接获得。VisualWebArena 的任务要求联合 image-text observation；成功应通过 execution-based evaluation 检查实际状态。
3. **Set-of-Marks（SoM）将视觉定位连接到动作。** 给可交互对象附上标记，使 agent 可以选择对应目标。它减少“我看到了按钮”和“我能可靠操作正确按钮”之间的距离，但不解决所有 visual recognition error。
4. **High-level plan 要能落成操作。** “找耳机价格范围”仍太抽象；分别排序并读取最低、最高值才是可执行分解。视频展示一步 human clarification 如何改变后续计划，但这不是保证每次澄清都会成功。
5. **Search 的增益依赖评价和预算。** 多次尝试可以探索不同 trajectories，value function 帮助选择与剪枝。理想 best-of-N 中“只要有一次成功就算成功”与真实系统能否识别正确轨迹不同；比较方法应匹配 test-time compute。
6. **Memory consolidation 是主动更新与丢弃。** MEM1 每轮把旧 internal state 和新 observation 合并，保留支持下一步推理的紧凑状态。视频问答明确原始 internal state 是 context 中的 text，并不天然等于 Markdown 文件或外部 vector database。
7. **Vision-Language-Action（VLA）改变输出空间。** OpenVLA 将视觉和语言条件转向机器人控制输出。网页点击与连续物理动作共享感知—行动结构，但 action representation、执行频率与误差后果有明显差别。

## Slides × video 导航

| 主题 | Slides（PDF 页码） | 视频定位 |
| --- | --- | --- |
| HTML 的局限与视觉观察 | [pp14–20](https://mit-mi.github.io/mmai-course/spring2026/schedule/lec10.1%20-%20interaction.pdf#page=14) | [33:36](https://www.youtube.com/watch?v=Sk_TYpA6DWA&t=2016s) |
| SoM 与 GUI grounding | [pp21–29](https://mit-mi.github.io/mmai-course/spring2026/schedule/lec10.1%20-%20interaction.pdf#page=21) | [44:31](https://www.youtube.com/watch?v=Sk_TYpA6DWA&t=2671s) |
| Clarification 与 uncertainty | [pp31–35](https://mit-mi.github.io/mmai-course/spring2026/schedule/lec10.1%20-%20interaction.pdf#page=31) | [56:42](https://www.youtube.com/watch?v=Sk_TYpA6DWA&t=3402s) |
| Search 与 value function | [pp36–37](https://mit-mi.github.io/mmai-course/spring2026/schedule/lec10.1%20-%20interaction.pdf#page=36) | [61:04](https://www.youtube.com/watch?v=Sk_TYpA6DWA&t=3664s) |
| MEM1 与 state 表示问答 | [pp38–48](https://mit-mi.github.io/mmai-course/spring2026/schedule/lec10.1%20-%20interaction.pdf#page=38) | [65:04](https://www.youtube.com/watch?v=Sk_TYpA6DWA&t=3904s)、[68:05](https://www.youtube.com/watch?v=Sk_TYpA6DWA&t=4085s) |
| OpenVLA | [pp49–52](https://mit-mi.github.io/mmai-course/spring2026/schedule/lec10.1%20-%20interaction.pdf#page=49) | [69:02](https://www.youtube.com/watch?v=Sk_TYpA6DWA&t=4142s) |

## 易混点与自测

重复采样答案一致只是一种 uncertainty proxy；模型可能稳定地犯错。多模态 benchmark 的历史成功率也不是对当前产品的排名。不要把“任务做对后又撤销”归为识别错误，它提示 state tracking 与 stopping criterion 出了问题。

读这一节时可以把每次失败定位到一条边：看错商品图片属于观察问题，选错对应链接属于定位问题，遗漏检查订单属于计划问题，重复累计属于记忆问题。这样的错误分解比只保存一个“任务失败”标签更能指导下一轮改进。

练习：为“统计某商品历次购买次数”写出 observation、high-level steps、action、success criterion；构造一个误点 wish list 的分支，说明 value function 需要哪些证据才能剪枝。再设计一个 internal state，只保留累计计数、已检查订单和待查项，检查会不会重复计数。

接着看[逐篇 Readings guidance](readings.md)。
