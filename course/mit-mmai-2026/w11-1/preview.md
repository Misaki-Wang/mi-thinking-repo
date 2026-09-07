# W11.1 · Multimodal & manufacturing

2026-04-14 · Sang-Gook Kim · 约 3 分钟预览

## 来源与阅读范围

依据已核对的 49 页讲义 **AI for Design and Manufacturing, Part 1: Manufacturing** 整理。课程表原 PDF 地址因文件名空格错误返回 404；这里链接至已核实的[官方同名讲义](https://mit-mi.github.io/mmai-course/spring2026/schedule/lec%2011.1%20-%20manufacturing.pdf)。未找到本节公开课程视频，因此本页是 slides summary，不是课堂逐字转写。

## 先抓住主线

制造业里的 Multimodal AI 应从“哪个生产决策需要改善”开始。设备已经数字化、传感器已经联网，并不意味着工程师的诊断经验、设计理由和跨部门知识也进入了系统。讲义把两条线连接起来：一条是把视觉、声学、温度和工艺日志对齐，识别过程状态；另一条是把人做过的决策及其理由组织成可检索知识，支持下一次判断。模型性能最终应反映到质量、生产速率、成本和柔性等制造目标。

## 七个关键点

1. **Data availability 比模型大小更早构成瓶颈。** 故障事件稀少、标签常在事后获得，各公司数据不容易互换；跨厂复用的可能是决策逻辑而非原始记录。普通随机划分还可能把同一工况泄漏到训练和测试两侧。
2. **Predictive maintenance 是一个决策流程。** 时间序列帮助发现异常，维护报告提供情境，融合结果支持维修优先级和后续动作。仅把异常分数做得更准，还没有证明停机损失减少。
3. **Digital twin 是持续更新的动态映射。** 讲义把它放在设备、工厂、供应链的多层系统中；单台设备的最佳策略可能与整条产线的维护或排程目标冲突。
4. **LPBF 的多模态需求来自物理机制。** Laser Powder Bed Fusion 中，laser power、scan speed、hatch spacing、layer thickness 共同影响热输入。讲义给出 `VED = P / (v × h × t)`；它是工艺描述量，不能独自代表熔池动态或所有缺陷机制。
5. **不同 sensor 看见不同过程。** 熔池图像、IR、acoustic emission 和 process logs 对温度、形态、振荡及控制参数提供互补观察。过高能量相关的 keyhole porosity 与能量不足相关的 lack of fusion，需要结合具体工况区分。
6. **Fusion 先解决时空对应。** 讲义以 voxel / scan vector 为对齐单位，随后比较 separate encoders 的 representation-level fusion、手工特征拼接、以及 defect scores 的 decision-level fusion。对齐误差会让“多传感器”变成彼此矛盾的证据。
7. **Agent architecture 应围绕功能组织。** Trouble detection、cause finding、solution reasoning 有不同输入和验收条件。把过去案例、专家经验和实时传感数据连接起来，是讲义提出的 research direction；此处不把架构草图当成已完成的工业验证。

## 原文导航

- [pp10–17：数据可用性、部署问题、系统集成层级](https://mit-mi.github.io/mmai-course/spring2026/schedule/lec%2011.1%20-%20manufacturing.pdf#page=10)
- [pp23–29：LPBF、缺陷机制、传感器与 fusion](https://mit-mi.github.io/mmai-course/spring2026/schedule/lec%2011.1%20-%20manufacturing.pdf#page=23)
- [pp37–38：从功能需求分解 agent](https://mit-mi.github.io/mmai-course/spring2026/schedule/lec%2011.1%20-%20manufacturing.pdf#page=37)
- [pp41–49：制造目标与 decision knowledge](https://mit-mi.github.io/mmai-course/spring2026/schedule/lec%2011.1%20-%20manufacturing.pdf#page=41)

## 易混点与边界

Multisensor 不自动意味着信息增益；应与 **best unimodal baseline** 比较。Digital twin、知识检索和闭环控制也不是同一个模块。讲义中的产业案例与进行中项目用于说明方向，不能替代跨机器泛化测试。公开讲义含带有 Confidential 标记的外部演示页，本笔记不转载其图片或内部数据明细。

## 自测与小练习

选择“提前识别一次设备异常”，写一张五列表：`决策 → 可观测信号 → 对齐单位 → 错误代价 → 验收指标`。比较仅振动、仅视觉、二者融合三个方案；增加一次时间偏移和一次 sensor missing 的反例。若 fusion 的 accuracy 更高，却产生更多误停机，应如何改写评价目标？

接着看[阅读与复习 guidance](readings.md)。
