# W03-2 · Multimodal fusion：从实际 HAIM Slides 学习医疗融合

**来源差异：** 课程表把本节列为 “Multimodal fusion / Early and late fusion / Explainable fusion”，但实际链接的 27 页 PDF 是 Dimitris Bertsimas 的 **HAIM: Holistic AI for Medicine**。没有找到本节课程表视频。本页按真实 PDF 预习医疗多模态应用，融合机制的系统推导见 [W04-1](../w04-1/preview.md)，不将目录主题补写成不存在的讲稿。

## 六个预习重点

1. **从医生使用的证据类型出发定义 multimodal input。** 医疗判断可能同时参考影像、radiology reports、临床 notes、tabular EHR、time series 和 genomic information。HAIM 的动机是将不同观测转为可以联合建模的 patient representation。需要先问每类数据何时可获得、对应哪次就诊，而不仅是是否存在。[Slides p3–7](https://mit-mi.github.io/mmai-course/spring2026/schedule/lec3.2%20-%20fusion.pdf#page=3)

2. **专门的 encoder 将异构输入转成特征。** Slides 分别介绍结构化记录、time series、文本与图像；文本示例把临床事件组织成字符串，再产生 embedding。p10–11 同时出现 ClinicalBERT 标题与 BioBERT embedding 标签，因此不能仅凭这两页确定实际使用的 checkpoint。预习时应保留这个待核对点。[Slides p8–13](https://mit-mi.github.io/mmai-course/spring2026/schedule/lec3.2%20-%20fusion.pdf#page=8)

3. **同一患者表示服务多个 prediction targets。** 本节列举 mortality prediction、disease classification、length of stay，以及部署中的未来 24/48 小时出院或 ICU 风险。每个 target 的 label、预测时点与评价窗口都不同；若特征包含预测时点之后的信息，漂亮的离线成绩也不说明可部署性。[Slides p14–15、20](https://mit-mi.github.io/mmai-course/spring2026/schedule/lec3.2%20-%20fusion.pdf#page=14)

4. **融合增益与解释性需要分别检查。** p16 报告 HAIM 相对 single modality 的改善区间，p17 展示 SHAP analysis。前者描述预测比较，后者描述模型内的特征归因；SHAP 值不自动等于临床因果效应，也不能单独证明跨模态 synergy。具体百分比的基线和分母应返回原研究核对。[Slides p16–17](https://mit-mi.github.io/mmai-course/spring2026/schedule/lec3.2%20-%20fusion.pdf#page=16)

5. **Ranking、calibration 与行动规则是不同层。** p21 分医院列出 AUC，p22 讨论概率校准，p24 再把出院概率转换为颜色提示。AUC 衡量排序；calibration 检查预测概率是否与发生频率一致；threshold 决定触发哪些工作流程。即使排序不变，校准偏移也会改变固定阈值下的报警数量。[Slides p21–24](https://mit-mi.github.io/mmai-course/spring2026/schedule/lec3.2%20-%20fusion.pdf#page=21)

6. **部署相关性不等于已证实的因果收益。** p25 的预测比较与 p26 的 length-of-stay 变化属于不同证据。p26 明确标为 preliminary descriptive analysis，并写出 parallel trend 假设和后续严格分析需求。这里应保留“初步描述”的边界，不能改写为模型已被随机实验证明缩短住院时间。[Slides p25–26](https://mit-mi.github.io/mmai-course/spring2026/schedule/lec3.2%20-%20fusion.pdf#page=25)

## 一个值得手算的机制

学习用的 calibration 检查：把预测概率接近 0.7 的患者分成一组，比较该组平均预测值与实际事件比例。如果实际发生率只有 0.4，模型仍可能拥有不错 AUC，却不能把“0.7”直接当成可靠概率。再检查不同医院、时间窗口与 patient subgroups，避免总体平均掩盖差异。这是由 p21–24 引出的学习练习，不是对真实病人的判断。

## 来源导航

| 你想看什么 | 定位 |
| --- | --- |
| HAIM 如何组织多类输入 | [Slides p7–13](https://mit-mi.github.io/mmai-course/spring2026/schedule/lec3.2%20-%20fusion.pdf#page=7) |
| 预测任务与特征归因 | [Slides p14–17](https://mit-mi.github.io/mmai-course/spring2026/schedule/lec3.2%20-%20fusion.pdf#page=14) |
| 部署指标和行为规则 | [Slides p20–26](https://mit-mi.github.io/mmai-course/spring2026/schedule/lec3.2%20-%20fusion.pdf#page=20) |
| 课程表原列的交互阅读 | [Reading guidance](readings.md) |

## 自测与动手

1. 临床 notes 与影像独立有用，是否足以证明模型捕捉了 cross-modal interactions？
2. 为什么同一模型在不同医院需要分别检查 calibration？
3. “患者住院时间减少”要支持因果结论，还需要排除哪些替代解释？

动手：用虚构数据做一个 20 行表格，包含预测时点、特征最晚时间、真实 outcome 和预测概率。标记潜在 leakage，计算一个概率区间的 calibration gap，再写出部署前要验证的三条假设。不要使用真实患者隐私数据。
