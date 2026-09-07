# W14.2 · AI for new senses

2026-05-07 · Paul Liang，含 Jas Brooks 等人的研究材料 · 约 3 分钟预览

## 来源与阅读范围

已核对 87 页[**Human-AI Interaction** 讲义](https://mit-mi.github.io/mmai-course/spring2026/schedule/lec14.2%20-%20human.pdf)，并对照[视频](https://www.youtube.com/watch?v=UJra8aMCHXg)英文自动字幕。**视频约 50:24，在 OpenTouch 后结束；slides pp66–87 的 HAI guidelines、safety、quantification 没有对应讲授段落，下面明确作为 slide-only extension。** pp31–34、55 是视觉演示页，不能把文字提取为空误认成空白。

## 先抓住主线

多模态可以走出 image、text、audio，形成 **sensing → representation / alignment → generation → human feedback** 的循环。感知 smell 需要稳定的 sensor signals；生成 smell 要把语义映射到可释放的气味组合；touch 连接接触压力、hand pose 与 egocentric vision。人的体验也不是模型输出的附属评价，而是系统目标和闭环反馈的一部分。

## 七个关键点

1. **Machine olfaction 先面对真实数据。** SmellNet 用传感器记录物质相关的时间序列；视频说明绝对读数会随环境条件变化，relative temporal change 可能更有用。ScentFormer 结合 temporal differencing 和 sliding windows，而不是仅对单点数值分类。
2. **Co-learning 可连接弱 sensor 与强测量。** 视频将气味信号与更强辅助信息的 alignment 联系到 W10.2：训练获得额外监督，推理仍可使用目标 sensor。应核对辅助信息是否在 test-time 可得，避免不公平比较。
3. **AromaGen 把语言理解变成受约束的生成。** Text / image inputs 映射成 base odorants 的混合，用户用自然语言迭代修正。它体现 alignment、generation 和 personalization，但有限气味基底的组合不等于可以复现任何气味。
4. **Sensory rendering 包含人的生理时序。** Slides 展示 smell 的姿态、气流、呼吸同步与刺激调度，以及 taste / temperature 的 perception engineering。这里是不同研究原型的例子，不把所有演示都归为同一训练好的 AI 模型。
5. **Touch 提供接触相关的互补证据。** Full-hand tactile sensing 观察哪里接触、如何施力；egocentric video 提供场景，3D hand pose 提供运动结构。OpenTouch 把这些信号同步，用于研究 retrieval、classification 与 embodied interaction。
6. **人类使用质量需要独立评价。** 讲义中 personalized gloves 关注重复测量稳定性和用户阻碍感；AromaGen 关注感知相似度与修正体验。一个系统的 recognition accuracy 更高，并不能代替舒适性、可控性或实际帮助程度。
7. **Slide-only extension：quantification 应落到可验证用途。** pp66–87 补充 HAI guidelines、bias、missing-modality robustness 和解释评价。MultiViz 的例子关注人能否模拟模型预测、发现错误、再用 targeted examples 改善模型；可视化“看起来有解释”不是最终验收条件。

## Slides × video 导航

| 主题 | Slides（PDF 页码） | 视频定位 |
| --- | --- | --- |
| SmellNet 与 sensor modeling | [pp5–11](https://mit-mi.github.io/mmai-course/spring2026/schedule/lec14.2%20-%20human.pdf#page=5) | [04:44](https://www.youtube.com/watch?v=UJra8aMCHXg&t=284s)、[15:06](https://www.youtube.com/watch?v=UJra8aMCHXg&t=906s) |
| AromaGen 与语言反馈 | [pp12–15](https://mit-mi.github.io/mmai-course/spring2026/schedule/lec14.2%20-%20human.pdf#page=12) | [18:57](https://www.youtube.com/watch?v=UJra8aMCHXg&t=1137s)、[25:25](https://www.youtube.com/watch?v=UJra8aMCHXg&t=1525s) |
| Smell / taste / temperature interfaces | [pp16–56](https://mit-mi.github.io/mmai-course/spring2026/schedule/lec14.2%20-%20human.pdf#page=16) | [27:06](https://www.youtube.com/watch?v=UJra8aMCHXg&t=1626s) |
| Touch 与 OpenTouch | [pp57–65](https://mit-mi.github.io/mmai-course/spring2026/schedule/lec14.2%20-%20human.pdf#page=57) | [45:37](https://www.youtube.com/watch?v=UJra8aMCHXg&t=2737s)、[47:28](https://www.youtube.com/watch?v=UJra8aMCHXg&t=2848s) |
| HAI、safety、quantification | [pp66–87](https://mit-mi.github.io/mmai-course/spring2026/schedule/lec14.2%20-%20human.pdf#page=66) | Slides only；视频 [48:48](https://www.youtube.com/watch?v=UJra8aMCHXg&t=2928s) 起收尾 |

## 易混点与边界

Smell recognition、odor mixture generation、trigeminal stimulation 是不同任务。Sensor measurement 也不能直接等同于人的主观体验。Slides 的 SmellNet 数量描述与当前论文 abstract 不完全相同，应保留版本与任务划分，见 readings。解释工具展示的 feature importance 不是因果解释，更不能用当前 benchmark 结果保证现实使用安全。

这也提示一种新的对齐难点：同一个词在不同人的记忆中可能对应不同体验，而传感器记录的是物理信号。用户说“更清新”时，系统需要把这种相对偏好转成可调输出；是否成功，最终仍须由人的反馈和明确任务共同判断。

## 自测与小练习

任选 smell 或 touch，画出 raw signal、采样频率、同步方式、representation、task、human outcome 六项。设计一次环境变化或传感器错位测试，再提出一个模型指标与一个 user-study 指标。若模型分类正确而用户体验不相似，错误可能在哪条映射？本练习只做数据与评价设计，不要求重建化学或电刺激硬件。

接着看[逐篇 Readings guidance](readings.md)。
