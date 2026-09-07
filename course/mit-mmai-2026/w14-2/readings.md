# W14.2 · Readings guidance

覆盖[课程表](https://mit-mi.github.io/mmai-course/spring2026/schedule/)全部 7 项，顺序与优先级为个人建议。ArXiv 论文已核对 primary abstract；两项 ACM 阅读已核对 DOI 身份及作者页面说明，未声称读到 ACM 全文。阅读时保留 paper / slides / video 的覆盖区别。

## 1. Interactive Sketchpad · 核心

[Interactive Sketchpad: A Multimodal Tutoring System for Collaborative, Visual Problem-Solving](https://arxiv.org/abs/2503.16434)

**为什么读：** 它与本学习工具最直接相关：将 language explanations、interactive visualizations 与 code execution 结合，支持 visual problem-solving。

**检查与提取：** 图由模型直接生成还是经代码执行？如何保证 diagram 与文字推导一致？User study 区分 comprehension、problem-solving accuracy、engagement 吗？查看 baseline 是否有相同内容、时长和互动机会。

**输出：** 给一个数学概念设计文字、图形、交互三种呈现，并写各自的学习目标；不要假定 engagement 增加就等于长期学习效果。证据：primary abstract；本节 video 未专门展开该论文。

## 2. AromaGen · 优先

[AromaGen: Interactive Generation of Rich Olfactory Experiences with Multimodal Language Models](https://arxiv.org/abs/2604.01650)

**为什么读：** 从语义输入到气味混合，再从人的反馈回到模型，构成完整的 human-AI loop。Abstract 明确其基于 12 种 base odorants 和迭代 natural-language feedback。

**检查与提取：** 混合表示如何连接到实际输出？In-context refinement 如何处理用户个体差异？区分 zero-shot、iterative refinement、human-composed mixtures 的比较；确认 similarity 与 artificiality 的测量方法。

**输出：** 写一个输入—输出—反馈表，标出“真实气味”“生成混合”“用户评分”三个不同证据对象。证据：primary abstract + slides pp12–15 + video；用户研究结果不能外推到所有人或所有 odor domains。

## 3. SmellNet · 优先

[SmellNet: A Large-scale Dataset for Real-world Smell Recognition](https://arxiv.org/abs/2506.00239)

**为什么读：** 理解新模态研究首先需要怎样的数据和 benchmark。Abstract 区分 SmellNet-Base 的 classification 与 SmellNet-Mixture 的 distribution prediction，并描述 ScentFormer 的 temporal differencing / sliding-window augmentation。

**检查与提取：** Sensor drift、环境变化、substance / mixture 划分怎样进入 test splits？GC-MS supervision 在训练或推理的哪一侧？窗口划分是否可能把相邻时间点泄漏到测试中？

**版本说明：** Slides p7 写超过 50 小时、超过 300,000 datapoints；本次核实的 arXiv v5 abstract 写约 828,000 points、68 小时，并包含 mixtures。它们属于不同来源的记录，本页不合并为单一课程数值。

**输出：** 数据卡中逐项写 source version、task、split、unit、metric。证据：primary abstract v5 + slides / video；不把 Top-1 classification 和 mixture prediction 的指标直接比较。

## 4. OpenTouch · 核心

[OPENTOUCH: Bringing Full-Hand Touch to Real-World Interaction](https://arxiv.org/abs/2512.16842)

**为什么读：** 把 egocentric vision 与 full-hand touch、pose、text annotations 连接起来。Abstract 确认其 retrieval / classification benchmarks，支持研究 contact-rich interaction。

**检查与提取：** 视频、手部姿态和压力如何同步？Classification 目标是什么，retrieval query 与 candidate 又是什么？跨人、物体、动作和场景泛化如何切分？

**输出：** 为一个抓取片段列出“视觉可见但触觉不直接提供”的信息与反向情况；设计视觉遮挡下的对照。证据：primary abstract + slides pp60–65 + video 47:28 起；视频提到 robotics 潜力，不等于本文已经验证任意机器人控制。

## 5. Stereo-Smell via Electrical Trigeminal Stimulation · 扩展

[课程 DOI](https://dl.acm.org/doi/abs/10.1145/3411764.3445300) · [作者实验室项目说明](https://lab.plopes.org/)

**为什么读：** 作者说明聚焦用 trigeminal sensations 传递气味来源方向，并与 olfactory perception 结合。它说明 sensory augmentation 可以改变信息通道，不只是释放更多气味。

**检查与提取：** 区分 odor identity、intensity、direction 三种信号；原文的 perception experiment 如何证明用户能利用方向信息？与 AromaGen 的 chemical generation 在目标与输出介质上有何不同？

**输出：** 一张 perception mapping：外部 sensor → 编码 → 刺激 → 主观知觉 → task outcome。证据：DOI metadata + author lab project excerpt，非全文；硬件参数及完整实验 protocol 待正式论文核对。

## 6. ArtPrompt · 扩展，连接 slide-only safety

[ArtPrompt: ASCII Art-based Jailbreak Attacks against Aligned LLMs](https://arxiv.org/abs/2402.11753)

**为什么读：** Abstract 指出文本输入也可以承载视觉结构，语义层面的 safety alignment 未必覆盖这些表示形式；同时提出 Vision-in-Text Challenge（ViTC）。

**检查与提取：** 区分“读不懂 ASCII art”的感知问题与“生成不当回答”的 safety outcome。检查威胁模型、black-box 条件、测试模型版本、成功判定和 benign control，避免把旧模型上的结果当成所有当前模型结论。

**输出：** 设计无害的 format robustness 测试：同一普通词以文字与 ASCII 排列给出，比较识别而非尝试获得危险输出。证据：primary abstract；slides p72 引用，公开视频没有讲到该页。

## 7. Guidelines for Human-AI Interaction · 优先，连接 slide-only HAI

[课程 DOI](https://dl.acm.org/doi/abs/10.1145/3290605.3300233) · [Microsoft Research 作者出版页](https://www.microsoft.com/en-us/research/publication/guidelines-for-human-ai-interaction/)

**为什么读：** 作者页面说明提出 18 条设计 guidelines，并通过多轮评价和设计从业者研究检验适用性。它为学习工具提供可操作的界面评审方向。

**检查与提取：** 阅读原 guideline 的适用情境，检查用户开始使用、正常交互、系统出错和长期使用时分别需要哪些信息与控制。不要根据标题自行补出“论文原文的 18 条”。

**输出：** 挑 3 条已读原文的 guideline，映射到本网站的来源状态、字幕质量说明、纠错入口，并记录具体 UI 证据和未满足项。证据：DOI metadata + author publication abstract；slides pp67–69 仅作导航，video 未覆盖。

## 统一交付

做一页 **multimodal interaction study card**：输入模态、输出模态、人的目标、模型指标、体验指标、反馈如何影响后续行为、原始研究未覆盖的使用条件。把 recognition、generation、interaction 分开评价，才能知道改进来自哪一环。
