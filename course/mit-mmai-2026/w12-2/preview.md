# W12.2 · Agents tutorial

2026-04-23 · 来源缺失说明与预习卡

## 已确认的范围

[官方课程表](https://mit-mi.github.io/mmai-course/spring2026/schedule/)列出的主题是 **Multimodal agent pipelines** 与 **Agent evaluation**。其 [agents.pdf 链接](https://mit-mi.github.io/mmai-course/spring2026/schedule/lec12.2%20-%20agents.pdf)返回 404；已检查的官方仓库文件列表没有对应 PDF，课程表及指定频道也未找到可匹配的公开录像。

因此目前无法核实 tutorial 的代码、演示、课堂步骤或结论。本页不充当 lecture summary 或 transcript。下方是基于课程主题和前面已公开材料整理的**个人预习练习**，不是对缺失课程内容的重建。若后续源文件公开，应优先替换此预习卡并保留来源状态记录。

## 三分钟预习：把 agent 变成可验收流程

可以先用一个小型网页检索任务整理概念：用户提出目标，agent 读取 observation，生成 action，在 environment 中执行，获取 feedback，再决定继续或停止。这个闭环需要记录足够的证据，才能区分“输出看起来合理”与“环境中确实完成了目标”。前置材料可复习 [W10.1 Interactive Agents](../w10-1/preview.md) 的 grounding / planning / memory，以及 [W11.2 Thinking Design](../w11-2/preview.md) 的 Functional Requirements（FRs）和 Design Parameters（DPs）。

## 六个个人准备问题

1. **Observation boundary：** Agent 实际看见 screenshot、DOM、accessibility tree 中的哪些部分？截图中的按钮存在，不代表它可点击；文本提到某个对象，也不代表已经定位到界面元素。
2. **Action contract：** 每个动作允许什么参数，失败时返回什么？把类型、对象标识、执行结果和下一步 observation 记清楚，才能定位失败发生在识别还是执行。
3. **State / memory：** 哪些证据需要跨步骤保存，哪些只是当前页面状态？尝试把“已经完成的事项”“待验证事实”“下一步”分开；不要把过去页面状态当成现在仍然成立。
4. **Completion criterion：** 任务何时算完成？先写环境可以检验的后置条件，再设计 agent。对一个查找任务，可要求答案同时含原始来源链接和支持片段；对一个编辑任务，则需要核对修改后的状态。
5. **Budget：** 除 success rate 外，记录动作次数、总耗时、模型调用和人工接管。两个方法若预算不同，不能直接把成功率差异归因于 reasoning 方法。
6. **Failure taxonomy：** 将错误分成 perception / grounding、planning、tool execution、memory、evaluation。为每类保留一个最小失败轨迹；更换模型之前，先确认评估器有没有把失败误判成成功。

## 可做的小练习

在你控制的静态测试网页中安排三个只读问题：读取一个数值、跨两页核对事实、遇到不存在的信息时说明缺失。先手工执行并记录正确轨迹，再运行同一 agent 配置。输出一张表：`任务 / 证据 / success criterion / 实际结果 / 失败类别 / 成本`。随后仅改变 observation 格式，比较结果；这是一项个人练习，不是课程原作业。

自测：一次 action 返回成功为什么不等于 task 完成？更多上下文为什么可能保存更多过期状态？为什么只看最终答案不足以定位 pipeline bug？

本节没有可以根据公开源归纳的“课程关键结论”。所有待补材料和阅读情况见[readings guidance](readings.md)。

完成练习后保留三个尚未确认的问题：原 tutorial 用的环境是什么、评分依赖哪些真实状态、是否允许人工介入。这些问题只能由后续原始资料回答，不能用本预习卡中的示例替代。
