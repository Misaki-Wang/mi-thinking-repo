# W04-2 · Reading guidance：alignment 的来源、收益与边界

本节八项 Reading 围绕四个问题：contrastive views 怎样选、图文究竟有哪些关系、retrieval 何时遗漏 compositionality、alignment 为什么会自然出现。P1/P2/P3 是本归档建议，不是官方 required/optional 标记。本次已核验作者原始摘要；semantic relations 论文使用官方出版商摘要。**未逐页审阅全文，未复现实验**；具体图表与定理条件留作精读任务。

## P1 · Learning Transferable Visual Models From Natural Language Supervision

[CLIP 论文](https://arxiv.org/pdf/2103.00020) · 证据：primary abstract。课程表标题末尾带问号，原论文标题没有问号，链接身份一致。

带着问题读：image-caption matching 为什么可以用于 zero-shot classification？摘要的核心是借自然语言提供比固定类别更广的监督，再以自然语言描述类别进行 transfer。先在正文找到 contrastive training 和 zero-shot classifier 构造，追踪图像、文本 encoder 与 similarity 的角色。

提取与检查：用三个 category prompts 手算一个图像的 similarity 排序，比较 prompt wording 改变结果的可能原因。报告 zero-shot 时写清模型仍使用了什么预训练数据，而不是说“没有训练”；也应分开 image classification 与关系理解。

## P1 · What Makes for Good Views for Contrastive Learning?

[论文](https://arxiv.org/abs/2005.10243) · 证据：primary abstract。

带着问题读：两个 views 应该越相似越好吗？摘要主张降低 views 之间的 mutual information，同时保留 task-relevant information，并用理论与经验分析研究 view selection 和 data augmentation。重点是两个条件同时成立；只让 views 差异变大可能删除任务信号。

优先寻找 InfoMin 思路、view construction、augmentation 和 downstream evaluation。提取与检查：为同一图像设计一个合理与一个过强的 augmentation，说明分别保留或破坏什么标签信息。将这套思路推广到 image/text 时，必须重新检查它们是否真拥有足够的 task redundancy。

## P2 · Characterization and classification of semantic image-text relations

[论文](https://link.springer.com/article/10.1007/s13735-019-00187-6) · 证据：官方出版商摘要。

带着问题读：图像与文字关系能否只用一个 similarity score 描述？摘要在 Cross-Modal Mutual Information 和 Semantic Correlation 之外引入 Status，构成三维度、八类 semantic image-text relations，并研究自动预测这些指标或类别。

优先去正文确认三维的操作定义和八类边界，不从标题猜测分类名。提取与检查：挑一条新闻、一幅广告、一张教学配图，问文字与图像谁提供主信息、谁补充、是否存在语义矛盾。将这些人工判断与“cosine 越高越好”的默认想法比较。

## P1 · When and why vision-language models behave like bags-of-words, and what to do about it?

[论文](https://arxiv.org/abs/2210.01936) · 证据：primary abstract。

带着问题读：标准 retrieval 为什么可能掩盖对属性、关系和顺序的不敏感？摘要介绍 ARO（Attribution, Relation, and Order）benchmark，并指出一些已有 retrieval 任务可以靠捷径获得高分，提出 composition-aware hard negative mining。

优先检查 ARO 三类任务、负样本构造与训练修改。提取与检查：用“红球在蓝箱内”与“蓝球在红箱内”设计 attribute binding 对照，再设计主客体交换的 relation 对照。比较 ordinary negatives 与 hard negatives 在监督什么；不要把某一次受控失败泛化成模型完全不理解语言。

## P2 · The Platonic Representation Hypothesis

[论文](https://arxiv.org/pdf/2405.07987) · 证据：primary abstract。

带着问题读：independently trained models 的表示怎样才算“趋同”？摘要观察到 vision/language models 变大时，样本间距离的度量更相似，并提出趋向共享现实统计模型的 hypothesis，同时讨论限制和 counterexamples。

优先寻找 representation similarity 的定义、样本配对方式、scale/performance 关系以及反例。提取与检查：区别“两个模型使用相同坐标”和“它们对哪些样本相近有相似判断”。把 hypothesis 与证据分栏记录，避免将“Platonic”解释成已证明存在唯一真实表示。

## P1 · Understanding the Emergence of Multimodal Representation Alignment

[论文](https://arxiv.org/pdf/2502.16282) · 证据：primary abstract。

带着问题读：alignment 与 downstream performance 的相关性是不是条件性的？摘要直接提出 when/why alignment emerges 与是否为可靠 performance indicator 两个问题，发现模态相似程度、task-redundant 与 unique information 的平衡等数据因素会改变关系。

优先寻找受控数据构造、alignment metric、performance metric 和条件化比较。提取与检查：写一个 task 主要依赖共享信息的例子，再写一个依赖独有信息的例子；预测加强 alignment 分别可能帮助还是损伤。不要跨 task 把不同条件的分数平均成一个“越对齐越好”的结论。

## P3 · Does equivariance matter at scale?

[论文](https://arxiv.org/abs/2410.23179) · 证据：primary abstract。

带着问题读：足够数据与 compute 能否替代 architecture 中的 symmetry prior？摘要在 rigid-body interactions benchmark 中比较 equivariant/non-equivariant networks，分别改变模型规模、训练步数和样本量；观察到 data efficiency、固定 compute 下的表现和预算分配存在区别。

优先找 scaling axes 与 compute-matched comparisons。提取与检查：画三个不同横轴——dataset size、training epochs、FLOPs——解释为什么某轴上追平不代表另一轴上也追平。这篇讨论结构先验的规模行为，不能直接当成跨模态 alignment 的普遍定理。

## P2 · Emerging Properties in Self-Supervised Vision Transformers

[DINO 论文](https://arxiv.org/pdf/2104.14294) · 证据：primary abstract。

带着问题读：不使用类别标签的训练，会让 ViT 出现哪些可观察表示性质？摘要介绍 DINO 作为 self-distillation with no labels，强调 momentum encoder、multi-crop 与 small patches，并观察 semantic segmentation 信息和 k-NN classification 能力。

优先找 teacher/student 训练、不同 crops、评价 protocol 与 ablations。提取与检查：区分“attention 或 feature 中含有 segmentation 信息”和“模型经过监督训练成为 segmentation system”。将它与 CLIP 比较：一个从同模态不同 views 学习，另一个从 image-text pairing 学习，监督信息来源不同。

## 读后比较与交付

推荐主线：CLIP 建立基本机制 → Good Views 检查共享信息假设 → ARO 暴露 compositional shortcut → Platonic 提出 emergent alignment 观察 → Emergence 论文检验它何时有益。Semantic relations 扩充“连接”的类型，DINO 和 equivariance 提供同模态与结构先验对照。

交付两页以内 Markdown：一张八篇论文的“监督来源—要保留的信息—评价终点”表；三个 relation/attribute hard negatives；一个“alignment 上升但任务可能下降”的条件化假设；一个能区分该假设与模型容量不足的实验。每个未读到正文的细节标记“待核对”。[返回 preview](preview.md)
