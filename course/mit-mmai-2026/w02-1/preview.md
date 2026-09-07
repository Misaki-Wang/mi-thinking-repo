# W02-1 · AI tutorial：先把数据与调试流程做扎实

本节目前没有课程表视频，以下依据实际 68 页 Slides 整理。材料包含项目构思、数据采集与特征提取、PyTorch/Hugging Face 入门入口及调试建议；它不是逐行展示训练代码的讲稿。预习目标是搭建一个可检查、可复现的小流程，并理解每一步改变了什么信息。

## 六个预习重点

1. **同一技术练习可以服务不同项目。** 前半部分展示脑到文字、情绪理解、点云、图表、绘画、代理与机器人案例。共同结构是把数据集、融合、模型适配、推理和行动逐步接到一个明确问题上。Slides 也明确允许最终成果是新数据集、应用或实证发现，不必强行为一个项目发明新网络。[Slides p5–6、41–43](https://mit-mi.github.io/mmai-course/spring2026/schedule/lec2.1%20-%20AI%20tutorial.pdf#page=41)

2. **先定义任务，再找数据。** 采集前写清总目标和需要的模态，优先检查已有数据是否含有所需观测。如果从视频提取音频、文字或面部特征，要记录这些输出来自同一源，而不能把它们误当成独立采集的证据。[Slides p49–51](https://mit-mi.github.io/mmai-course/spring2026/schedule/lec2.1%20-%20AI%20tutorial.pdf#page=49)

3. **复用成熟提取工具，但仍需检查输出。** Slides 列出 FFmpeg、OpenCV、MediaPipe、OpenFace、Whisper 等入口，并提醒使用隔离环境。工具可以节省工程时间，却不能替你决定采样率、片段边界和错误处理。字幕里的否定词丢失、音视频不同步，都可能直接改变标签判断。[Slides p53–57](https://mit-mi.github.io/mmai-course/spring2026/schedule/lec2.1%20-%20AI%20tutorial.pdf#page=53)

4. **从长视频提取中间特征是一种建模选择。** ADOS 案例把长会话分片，再提取音频、文本、面部特征、摘要和中层属性。其动机是让细微动作、音高与表情更容易进入模型，而不是假定所有内容都能被一个长视频输入准确保留。分片也可能丢失跨片段背景，应该作为误差来源检查。[Slides p59–64](https://mit-mi.github.io/mmai-course/spring2026/schedule/lec2.1%20-%20AI%20tutorial.pdf#page=59)

5. **模型生成的摘要或标签是派生特征。** Slides 展示借助已有模型生成视频摘要和限定选项的中层属性。学习时应把“模型判断”与人工标注分开保存，记录提示词和模型版本，抽查幻觉与重复信息。课堂案例是研究流程示例，不构成医疗诊断建议。[Slides p62–63](https://mit-mi.github.io/mmai-course/spring2026/schedule/lec2.1%20-%20AI%20tutorial.pdf#page=62)

6. **根据现象缩小故障范围。** 输入标签错误、只预测一个类别、NaN、loss 不动、loss 波动以及 train/validation 差距，对应不同检查路径。先看数据与输出，再查数值、梯度与超参数；简单低维数据可以从浅层模型开始，视觉和语言可先试预训练模型。[Slides p66–68](https://mit-mi.github.io/mmai-course/spring2026/schedule/lec2.1%20-%20AI%20tutorial.pdf#page=66)

## 最小机制：把每个转换变成可审计边界

`原始视频 → 固定边界片段 → 音频 / 字幕 / 特征 → 按样本 ID 对齐 → 简单模型 → 留出集评价`。给每个样本保存原文件 ID、起止时间和处理参数，就能把异常预测追溯到原始片段。这个过程也适用于本课程学习工具链：自动字幕或 Whisper 是英文来源，中文翻译和摘要是后续派生层。

## 来源导航

| 你要做的事 | 定位 |
| --- | --- |
| 确定最终项目可以交付什么 | [Slides p41–46](https://mit-mi.github.io/mmai-course/spring2026/schedule/lec2.1%20-%20AI%20tutorial.pdf#page=41) |
| 选择数据与提取工具 | [Slides p49–57](https://mit-mi.github.io/mmai-course/spring2026/schedule/lec2.1%20-%20AI%20tutorial.pdf#page=49) |
| 理解长视频派生特征 | [Slides p59–64](https://mit-mi.github.io/mmai-course/spring2026/schedule/lec2.1%20-%20AI%20tutorial.pdf#page=59) |
| 入门与调试 | [Slides p65–68](https://mit-mi.github.io/mmai-course/spring2026/schedule/lec2.1%20-%20AI%20tutorial.pdf#page=65) · [Reading guidance](readings.md) |

## 容易混淆的地方

“loss 不变”并不能单凭曲线诊断欠拟合，还可能是梯度断开、参数未更新或掩码错误；“train 和 validation 都接近满分”也只是泄漏警报，不是泄漏已被证实。课件中的学习率、数值精度和优化器建议应作为待验证操作，不应一次全部更改。Slides p9、26、44 没有可提取文字，部分项目演示仅保留题目或图像，因此这里不补写未观察到的演示细节。

## 自测与动手

1. 自动语音转写与人工文本标签，在数据表里如何区分？
2. 为什么应先证明模型能拟合少量样本，再解释整套数据上的失败？
3. 随机切分同一段长视频的片段可能导致什么问题？

动手：准备 10 个短视频或音频样本，输出带时间戳的英文文本与中文预览，人工记录三类错误：源字幕错误、翻译错误、摘要遗漏。写一份样本清单和失败日志，再扩大数据量。
