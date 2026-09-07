# W01-1 · Course introduction：先建立多模态问题的地图

这门课把多模态 AI 看成对“异构、相互连接、共同影响任务的数据”的研究。预习时先回答三个问题：输入有哪些不同结构？它们共享什么？联合观察究竟增加了什么任务信息？这个视角能帮助你判断一个新模型解决的是表示、对齐、推理还是其他问题，而不只记住模型名字。

整理依据为 Slides 与公开视频的英文自动字幕；时间链接定位到相关字幕片段起点，技术名词结合 Slides 校对。自测、例子延伸和实验建议属于本归档的学习整理。

## 六个值得带走的概念

1. **模态既可以接近传感器，也可以高度抽象。** 音频波形、像素是原始观测；识别出的词、对象与情感强度是抽象表示。把视频转成文字会改变可用信息：内容更方便检索，但语气、节奏、空间关系可能丢失。因此，“统一成 token”不等于原始差异消失。[Slides p39–41](https://mit-mi.github.io/mmai-course/spring2026/schedule/lec1.1%20-%20introduction.pdf#page=39)

2. **Heterogeneity、connections、interactions 是三个不同的问题。** 异构性描述数据的分布和结构差异；连接性描述两种观测之间的对应；交互性必须相对于任务讨论。一张图和一句话可以有关联，却未必都对当前标签有帮助。视频强调 heterogeneity 是一个连续谱：两台相机虽同属视觉，也因视角不同保留不同信息。[Slides p40–46](https://mit-mi.github.io/mmai-course/spring2026/schedule/lec1.1%20-%20introduction.pdf#page=40) · [视频 46:29](https://www.youtube.com/watch?v=Xm2crsD5ngA&t=2789s)

3. **Redundancy、uniqueness、synergy 解释“为什么需要多模态”。** 两种模态都表达正面态度是冗余；只有文字给出具体评价理由是独有信息；同一句赞美搭配反讽语气才暴露真实态度，是协同。视频用“wow”与生气表情的冲突具体说明 synergy；协同不是“拼接后分数变高”的同义词，需要证明模型确实利用了联合关系。[Slides p43–45](https://mit-mi.github.io/mmai-course/spring2026/schedule/lec1.1%20-%20introduction.pdf#page=43) · [视频 51:39](https://www.youtube.com/watch?v=Xm2crsD5ngA&t=3099s)

4. **Representation、alignment、reasoning 对应三个层次。** 表示决定信息如何被编码；对齐决定词、对象、时间片如何关联；推理利用这些结构和知识做多步推断。Fusion 把多种输入合成联合表示，coordination 保留多个但可比较的表示，fission 则将共享与独有因素分开。[Slides p48–53](https://mit-mi.github.io/mmai-course/spring2026/schedule/lec1.1%20-%20introduction.pdf#page=48)

5. **Generation、transference、quantification 拓宽了任务边界。** 生成关注跨模态一致的输出；迁移关注如何让数据少、噪声大的目标模态受益；量化研究模型究竟学到了什么、什么时候失败。视频把 quantification 比作研究方法的“放大镜”，强调对有效条件与失败原因的理解；这使它成为选择模型和构造实验的依据。[Slides p54–58](https://mit-mi.github.io/mmai-course/spring2026/schedule/lec1.1%20-%20introduction.pdf#page=54) · [视频 1:07:24](https://www.youtube.com/watch?v=Xm2crsD5ngA&t=4044s)

6. **课程项目是一条连续研究线。** 数据处理、融合、适配多模态模型、推理、代理逐步叠加到同一问题上。第一周就值得选一个可获得、可检查的数据集，并保留最简单基线；期末成果可以是方法，也可以是可靠的实证发现。[Slides p17–20](https://mit-mi.github.io/mmai-course/spring2026/schedule/lec1.1%20-%20introduction.pdf#page=17)

## 用一个机制串起来

以讽刺识别为例：`文字 x_text + 语音 x_audio → 各自编码 → 对齐到同一句话 → 联合判断 y`。若文字“真棒”单看偏正面，而语气让它变成负面，就应专门检查“相同文字、不同语气”的配对。这个受控比较比只报告总准确率，更能回答模型是否依赖跨模态关系。这里是学习用的实验推导，不是课程已完成的实验结果。

## 来源导航

| 想解决的问题 | 定位 |
| --- | --- |
| 如何规划整个学期的练习 | [Slides p13–20](https://mit-mi.github.io/mmai-course/spring2026/schedule/lec1.1%20-%20introduction.pdf#page=13) |
| 多模态的工作定义与三类交互 | [Slides p39–46](https://mit-mi.github.io/mmai-course/spring2026/schedule/lec1.1%20-%20introduction.pdf#page=39) |
| 六大挑战如何区分 | [Slides p48–59](https://mit-mi.github.io/mmai-course/spring2026/schedule/lec1.1%20-%20introduction.pdf#page=48) |
| 对照原始讲解 | [官方视频](https://www.youtube.com/watch?v=Xm2crsD5ngA) · [本节 Reading guidance](readings.md) |

## 容易混淆的地方

“两份数据”不自动构成有用的多模态任务；“有 cross-attention”不自动证明学到了 synergy；“统一表示”也不意味着应该抹掉模态独有信息。另一个来源差异是，导论 p21 写有不录课的早期说明，而讲师在 [视频 28:52](https://www.youtube.com/watch?v=Xm2crsD5ngA&t=1732s) 明确说明会录制并发布到 YouTube；本归档采用后者与实际公布的视频链接。

## 自测与动手

1. 同一张图的两个裁剪，与图像加传感器序列，异构性可能有什么差别？
2. 为冗余、独有、协同各设计一个输入和标签都明确的例子。
3. 图文检索与图像问答分别最直接涉及哪些挑战？为什么不完全相同？

动手：选一个自己的学习或研究场景，写一页“模态卡”：输入、任务、共享信息、独有信息、可能协同、最小基线、一个能推翻自己直觉的测试。后续每周修改这一页，形成项目的研究轨迹。
