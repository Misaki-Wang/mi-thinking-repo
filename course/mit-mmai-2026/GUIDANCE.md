# GUIDANCE · 如何学完 MIT Multimodal AI

这门课程适合沿着一个真实任务学：先判断不同模态包含什么信息，再设计表示与交互方式，最后考虑模型如何生成、推理、行动并接受可靠评估。以下路线是本学习档案的建议，不替代 [官方课表](https://mit-mi.github.io/mmai-course/spring2026/schedule/)。

## 每讲的使用方法

1. **先用 3–5 分钟读 preview。** 抓住本讲解决的问题、关键术语和模块关系，写下一个现在无法回答的问题。
2. **沿页码或时间入口检查原始材料。** Slides 提供公式与图示，视频提供解释、例子和问题讨论；两者覆盖范围不完全一致，预览页已标出重要差异。
3. **按 readings guidance 挑核心阅读。** 第一遍查问题、方法图、主要评估与限制；第二遍才读与自己任务有关的推导、消融和实现。这里的阅读优先级是建议，非教师的必读标记。
4. **完成一个可检查的产物。** 模态资料表、模块图、实验对照表、错误分析或简短实现，至少选一种；完成自测后再进入下一组主题。
5. **写自己的判断。** 将“作者展示的证据”“我认为能迁移的结论”“尚未验证的假设”分开。适合独立成文的观点放入 [Blog](../../blog/README.md)，论文详读放入 [Paper](../../paper/README.md)。

## 建议的八阶段路线

| 阶段 | 单元 | 应交付的学习产物 |
|---|---|---|
| 1. 定义问题与数据 | [1.1](w01-1/preview.md)、[1.2](w01-2/preview.md)、[2.1](w02-1/preview.md)、[2.2](w02-2/preview.md) | 一份 modality profile：采样、结构、噪声、缺失、标签、隐私与数据划分 |
| 2. 理解信息交互 | [3.2](w03-2/preview.md)、[4.1](w04-1/preview.md)、[4.2](w04-2/preview.md) | unimodal、late fusion、带交互 fusion 的对照设计；说明 alignment 是否保留任务独有信息 |
| 3. 使用基础模型 | [5.1](w05-1/preview.md)、[5.2](w05-2/preview.md) | encoder / projector / LLM 参数冻结图；固定 held-out set 的 baseline 与 LoRA 评价方案 |
| 4. 学习生成分布 | [6.1](w06-1/preview.md)、[6.2](w06-2/preview.md)、[7.1](w07-1/preview.md) | VAE / diffusion / flow matching 的训练、采样、条件与指标对照表 |
| 5. 推理与解释 | [9.1](w09-1/preview.md)、[9.2](w09-2/preview.md) | reward specification、三个 reward hacking 反例、claim–evidence 表 |
| 6. 行动与迁移 | [10.1](w10-1/preview.md)、[10.2](w10-2/preview.md)、[12.2 准备页](w12-2/preview.md) | observation → action → feedback 的 agent trace，以及训练/测试模态可用性矩阵 |
| 7. 在领域中落地 | [11.1](w11-1/preview.md)、[11.2](w11-2/preview.md)、[12.1](w12-1/preview.md)、[13.1](w13-1/preview.md)、[13.2](w13-2/preview.md) | 任务指标、部署约束、决策成本、失败恢复与 domain shift 检查 |
| 8. 形成研究问题 | [14.1](w14-1/preview.md)、[14.2](w14-2/preview.md) | 一个可证伪的小问题：数据来源、最小 baseline、关键消融与预期反例 |

如果每周能投入 4–6 小时，可以每阶段安排约一周；应用阶段资料较多，可拆成两周。时间是个人学习建议。已有 ML 基础者可先预览全部课程，再集中精读与自己项目相关的路径。

## 用一个项目贯穿全课

示例任务：把图表、文本与时间序列结合，回答需要跨模态证据的问题。例子只用于说明组织方式，选择自己的数据更有价值。

- 开始时明确为什么单模态不足。若答案完全写在文本里，增加视觉不自动成为多模态能力证据。
- 建立简单且公平的 baseline。固定数据划分、输入预算、训练预算和评估问题，分别记录每种模态的贡献。
- 做模型适配前，先看原模型会错在哪里。使用所有测试样本，不仅保留好看的例子。
- 引入生成时，分别测量真实性、条件遵循、跨模态同步与失败频率。
- 引入 RL 或 agents 时，把 reward、权限、停止条件和失败恢复写清楚，记录完整观察与行动轨迹。
- 最后选择最能解释现象的实验，不必把每一种课中模型都训练一次。

## 专业术语与公式的记录方式

按 [TERMS](TERMS.md) 保留英文原词和缩写。首次出现可写“中文（English, 缩写）”；CLIP、LoRA、GRPO、Qwen、MIMIC 等保持原名。公式要同时写变量含义、维度、条件与优化方向。自动字幕出现疑似术语误识别时，回看 slides 与原视频，保留可追溯来源。

特别区分：

- 跨模态 alignment 与人类偏好 alignment；
- fusion、grounding 与 representation similarity；
- LoRA、projector、prefix tuning 与 quantization；
- VAE 的重建与生成，diffusion 的训练与采样；
- 可见 reasoning trace、正确答案与解释忠实性；
- benchmark 提升、domain transfer 与真实部署效果。

## Readings 的统一笔记框架

每篇论文写七项：研究问题；关键假设；输入/输出与方法机制；监督和数据；控制条件下的主要证据；局限与反例；对我的任务最值得检验的一点。记录原始链接与版本，不把本文未读到的细节凭题目补齐。

资料核验只证明某个链接对应某项工作。官网摘要、作者博客、full paper 与可运行 notebook 的证据粒度不同，各讲 guidance 已说明。课表错链及可确认的候选集中在 [SOURCES](SOURCES.md)。

## 当前资料状态

所有 13 个公开视频的英文字幕已获取并验证；23 份教学材料用于原创中文预览。完整中文逐字译稿及公开再分发待内容授权确认，网站公开的是原创摘要与阅读 guidance。Week 12.2 没有可获取 slides/video，保留准备页，不能视为该讲已经完成转写。

完成一讲的标准：可以用自己的话解释核心机制，能定位原材料，做出一个可检查的产物，并能说出一个该方法可能失败的情况。
