# W11.1 · Readings guidance

## 官方安排与证据

[课程表](https://mit-mi.github.io/mmai-course/spring2026/schedule/)没有为本节指定 Readings。下列内容是个人复习建议，不是新增的官方论文清单。已核对本节[Manufacturing 讲义](https://mit-mi.github.io/mmai-course/spring2026/schedule/lec%2011.1%20-%20manufacturing.pdf)；讲义中列举的论文和产业案例也不自动等于课程指定阅读。

## 建议顺序

1. **优先：问题定义，pp10–17。** 提取制造场景里的数据稀缺、跨部门信息隔离、alignment 和 deployment constraints。回答：添加另一模态后，改善的是哪个可测决策？输出一份 best unimodal baseline 的定义。
2. **核心：LPBF case，pp23–29。** 分别记录 process parameter、physical phenomenon、sensor measurement、defect 四层，避免把测量当成原因。画出视觉和声学各自补充什么信息，并写出时间同步失败时的一个反例。
3. **扩展：knowledge threading，pp37–49。** 区分事件日志与 decision rationale。设计一条案例记录，包含当时证据、判断、采取的动作、结果，以及下次复用的条件；不要只保存最终答案。

## 本节交付物

一页 manufacturing decision card：明确目标、数据单位、primary modality、secondary modality、融合位置、跨机器测试及真实成本。用“不加第二模态”“故意错位第二模态”“缺失第二模态”三个对照检验项目是否真正需要 multimodal modeling。

自测：Digitalization 为什么可能未带来系统生产率优势？为什么 defect label 的事后生成会影响训练集构造？设备层的最优 maintenance action 为什么可能不是工厂层的最优 decision？
