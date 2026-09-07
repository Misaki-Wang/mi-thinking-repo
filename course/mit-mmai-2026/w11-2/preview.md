# W11.2 · Multimodal & design

2026-04-16 · Sang-Gook Kim · 约 3 分钟预览

## 来源与阅读范围

依据 60 页 **AI for Design and Manufacturing, Part 2: Thinking Design** 整理。实际重点是 **Axiomatic Design 与 agent 的功能分解**，不只是生成设计图片。课程表链接有文件名空格错误，已找到[官方可访问版本](https://mit-mi.github.io/mmai-course/spring2026/schedule/lec%2011.2%20-%20design.pdf)。未找到本节公开课程视频，本页为 slides summary。

## 先抓住主线

“我要一个 multimodal agent”仍是在描述某种技术方案。讲义要求先说明系统必须完成什么，再决定用什么实现。功能需求 **Functional Requirements（FRs）** 属于 What；设计参数 **Design Parameters（DPs）** 属于 How。设计的关键不是堆出更多模块，而是让这些模块之间的影响关系与需求结构一致。这个视角可以直接用于学习工具、工业诊断系统和多 agent workflow。

## 七个关键点

1. **四个 design domains 连接需求与制造。** Customer domain 描述人的需要，functional domain 抽象功能，physical domain 选择实现，process domain 决定如何生产。跨域映射帮助发现“需求”是否偷偷预设了技术。
2. **先保持 solution-neutral。** “让用户找到证据”是功能；“用 vector database”是候选实现。过早写死 How，会掩盖更简单的方案，也会使需求分解跟着现有软件组织走。
3. **用 design matrix 检查 coupling。** 讲义以 `Aij = ∂FRi / ∂DPj` 表示参数变化对功能的影响。Diagonal 对应 uncoupled；合适顺序下的 triangular 结构对应 decoupled；彼此牵连的结构会增加协调和反复调整。
4. **Physical coupling 与 functional coupling 不同。** 一个物理零件可以承担多个功能，只要这些功能仍可按要求调节。把每个功能拆成独立物件，不是讲义主张的唯一设计原则。
5. **Top-down decomposition 要在 What / How 间 zig-zag。** 先定义上层目标，探索实现概念，再分解该概念需要的下层功能。只沿一棵物理部件树向下拆，可能永远没有说清需求。
6. **医院案例揭示目标混用。** 讲义中，按紧急程度排序和改善患者流动是两个 FR；把同一分类同时用于两者会造成 coupling。这个例子用于说明重新构造问题的价值，页中等待时间结果属于特定案例，不是普适收益率。
7. **Agent orchestration 可以沿 FR–DP graph 设计。** 故障发现、原因定位、恢复方案各有验收目标，orchestrator 再根据依赖决定顺序或补充查询。保存“发生什么、为什么、采取什么、学到什么”比只有对话记录更利于复用。

## 原文导航

- [pp2–5：design domains 与常见错误](https://mit-mi.github.io/mmai-course/spring2026/schedule/lec%2011.2%20-%20design.pdf#page=2)
- [pp18–26：FR、DP、coupling 与设计原则](https://mit-mi.github.io/mmai-course/spring2026/schedule/lec%2011.2%20-%20design.pdf#page=18)
- [pp27–34：医院 patient flow case](https://mit-mi.github.io/mmai-course/spring2026/schedule/lec%2011.2%20-%20design.pdf#page=27)
- [pp40–48：需求抽取、概念生成、设计知识](https://mit-mi.github.io/mmai-course/spring2026/schedule/lec%2011.2%20-%20design.pdf#page=40)
- [pp53–59：functional agents 与 orchestration](https://mit-mi.github.io/mmai-course/spring2026/schedule/lec%2011.2%20-%20design.pdf#page=53)

## 易混点与边界

FR 的独立性是定义和设计时要努力满足的要求，不是对所有现实目标“天然独立”的断言。把模块命名成 Planner、Retriever、Reviewer 也不等于已经得到功能图；需要可检验的职责和依赖。讲义中的“AI 能否按 axiomatic thinking 工作”包含研究问题，不能据此认定 LLM 已可靠完成系统设计。

## 自测与小练习

以本学习站为例，先写三个 FR：找到课程依据、理解关键概念、记录个人理解。再提出至少两套 DP 方案，画一个 3×3 影响矩阵：修改字幕清理规则，会不会无意改变来源定位或中文术语？选择一个耦合，提出接口或流程调整。最终交付一张 FR tree 和一次 coupling review，而非仅一张工具清单。

接着看[阅读与复习 guidance](readings.md)。
