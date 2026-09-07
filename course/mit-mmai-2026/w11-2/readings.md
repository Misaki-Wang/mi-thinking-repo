# W11.2 · Readings guidance

## 官方安排与证据

[课程表](https://mit-mi.github.io/mmai-course/spring2026/schedule/)没有指定本节 Readings。已核对[Thinking Design 讲义](https://mit-mi.github.io/mmai-course/spring2026/schedule/lec%2011.2%20-%20design.pdf)。讲义 p34 提到 Canvas reading material，但课程公开表中没有可核实的指定阅读入口，本页不把它补写成已取得的阅读材料。

## 建议顺序

1. **优先：pp2–5、18–26。** 搞清 FR、DP、design domain、uncoupled / decoupled / coupled。提取三个自己的 What / How 配对，并检查 What 是否偷带具体解法。
2. **核心案例：pp27–34。** 阅读医院流程改进时，先画“紧急程度”与“流转效率”两个目标，再找同一 DP 同时服务两个 FR 的位置。关注问题重构，不把案例改善百分比迁移到自己的项目。
3. **实践：pp40–48、53–59。** 检查 recursive question answering 如何抽取需求与实现关系。将一个 agent 系统拆成 FR tree，再把工具或模型放进对应 DP；记录无法判断 coupling 的位置。

## 本节交付物

完成一页设计评审：用户需要、约束、FR tree、两个候选 concept、FR–DP matrix、执行顺序。给每个 agent 写一个能够失败的验收标准，例如“找到与结论直接相关的原始段落”，而不是“负责搜索”。

自测：一个 physical component 承担两个 FR 是否一定是坏设计？三角形依赖矩阵为何需要适当的执行顺序？如果无法用不含具体模型名的语言描述功能，说明设计仍缺少什么？以上优先级是本学习仓库的建议。
