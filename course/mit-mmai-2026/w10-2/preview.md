# W10.2 · Cross-modal transfer

2026-04-09 · Paul Liang · 约 3 分钟预览

## 来源与阅读范围

已核对 46 页[Cross-modal Transfer 讲义](https://mit-mi.github.io/mmai-course/spring2026/schedule/lec10.2%20-%20crossmodal.pdf)，并对照[视频](https://www.youtube.com/watch?v=IDaMEG_zY6A)英文自动字幕。Readings 中 LLaVA-Med 标题与链接不一致，详见[逐篇 guidance](readings.md)，不将其混写为同一篇论文。

## 先抓住主线

**Cross-modal transfer / transference** 的目标，是利用相关模态帮助真正关心的 primary modality，尤其在低资源、噪声或缺失数据下。最先要固定的是 training 与 inference 各能看见什么。课堂明确提醒：若一个方法在测试时获得额外模态，另一个没有，性能差异就不能单纯归因于训练过程更好。本节三条路线是 pretrained transfer、co-learning、model induction。

## 七个关键点

1. **Transfer 通过共享知识而非共享任务名发生。** Pretrained parameters、共同 architecture 和 representation 允许不同 modalities / tasks 交换信息。HighMMT 讨论如何依据 modality heterogeneity 与 interaction heterogeneity 决定共享。
2. **“都转成 sequence”是一组假设。** 顺序化可能损失图结构或几何关系；modality embeddings 也未必表达所有噪声、分辨率和统计差异。讲义把这些作为 unified high-modality models 的待解决问题。
3. **Co-learning 的 secondary modality 只在训练期帮助。** 它既可作为 auxiliary input，也可作为 auxiliary prediction target。推理只保留 primary modality，才符合这一节强调的使用场景。
4. **Fusion-based co-learning 要处理缺失输入。** 讲义展示训练时 A+B、测试时将 B 填零的实例。视频中学生立即追问 distribution shift：从未在训练见过全零输入为何能可靠推理？填零是一种案例做法，不是通用稳健保证。
5. **Alignment 与 translation 提供不同监督。** Alignment 将相关表示靠近；translation 把另一模态作为目标，cyclic translation 再约束往返信息。它们都是为了改善最终 representation，不意味着推理时必须真实获得或重建全部辅助模态。
6. **辅助任务可以补充 dense supervision。** 课堂例子是很长的 breathing signal 对应一个疾病标签；预测配对 EEG 可提供更密集的时间序列训练信号。这里强调监督结构，不据此推断任何个体的医学状态。
7. **Model induction 保持模型边界并交换输出。** Self-training 从高置信 pseudo-labels 扩充训练集；co-training 让两种 view 的 classifier 互相提供标签。经典保证依赖 view 的信息条件，不能直接迁移为“多 LLM debate 一定会变好”。

## Slides × video 导航

| 主题 | Slides（PDF 页码） | 视频定位 |
| --- | --- | --- |
| 定义、训练 / 测试信息边界 | [pp3–5、12](https://mit-mi.github.io/mmai-course/spring2026/schedule/lec10.2%20-%20crossmodal.pdf#page=3) | [01:54](https://www.youtube.com/watch?v=IDaMEG_zY6A&t=114s) |
| 共享参数与 sequence assumptions | [pp6–11](https://mit-mi.github.io/mmai-course/spring2026/schedule/lec10.2%20-%20crossmodal.pdf#page=6) | [07:32](https://www.youtube.com/watch?v=IDaMEG_zY6A&t=452s)、[19:57](https://www.youtube.com/watch?v=IDaMEG_zY6A&t=1197s) |
| Fusion 与 missing modality 讨论 | [pp13–15](https://mit-mi.github.io/mmai-course/spring2026/schedule/lec10.2%20-%20crossmodal.pdf#page=13) | [27:02](https://www.youtube.com/watch?v=IDaMEG_zY6A&t=1622s)、[32:28](https://www.youtube.com/watch?v=IDaMEG_zY6A&t=1948s) |
| Cyclic translation 与 dense supervision | [pp22–30](https://mit-mi.github.io/mmai-course/spring2026/schedule/lec10.2%20-%20crossmodal.pdf#page=22) | [50:52](https://www.youtube.com/watch?v=IDaMEG_zY6A&t=3052s)、[52:56](https://www.youtube.com/watch?v=IDaMEG_zY6A&t=3176s) |
| Self-training / co-training | [pp33–44](https://mit-mi.github.io/mmai-course/spring2026/schedule/lec10.2%20-%20crossmodal.pdf#page=33) | [57:11](https://www.youtube.com/watch?v=IDaMEG_zY6A&t=3431s)、[63:31](https://www.youtube.com/watch?v=IDaMEG_zY6A&t=3811s) |

## 易混点与自测

Co-learning 不等于 co-training；前者强调辅助模态怎样改善 primary representation，后者是多 view 模型交换监督的一类算法。视频末尾将 API-level exchange 和训练例子并列概括，应逐个方法核对是否更新 weights：模型架构保持分开，不代表参数始终冻结。视觉 co-learning 在某些 lexical grounding / commonsense task 上只有很小改善，说明额外信息是否与目标相关仍需验证。

可以把三条路线看成三种知识入口：继承参数，改变训练时表示受到的约束，或交换模型输出形成的监督。它们有可能组合使用。判断一种新方法属于哪一类时，追踪信息真正进入哪里，比根据作者采用的名称分类更可靠。

练习：为 text-only inference 设计三个版本：text baseline、训练时 image-text alignment、训练时 text→image auxiliary prediction。保持主任务数据与测试输入一致，写明新增监督和成本；再加入打乱配对图像的对照。若打乱配对仍然同样有效，你会怎样解释结果？
