# W10.2 · Readings guidance

覆盖[课程表](https://mit-mi.github.io/mmai-course/spring2026/schedule/)全部 5 项。优先级为个人建议。论文身份与 abstract 已通过原始 arXiv 元数据核实；尚未对全文方法和实验逐项验证，以下检查项是阅读任务。

## 1. HighMMT · 优先

[High-Modality Multimodal Transformer: Quantifying Modality & Interaction Heterogeneity for High-Modality Representation Learning](https://arxiv.org/abs/2203.01311)

**为什么读：** 它把 parameter sharing 建立在 heterogeneity quantification 上。Abstract 区分单个 modality 之间的 transfer 与 modality pairs 之间 interaction 的 transfer。

**检查与提取：** 两种 heterogeneity metric 的输入和输出分别是什么？如何从 transfer evidence 选择共享模块？新模态加入后需要哪些参数、数据和 fine-tuning？查找 ablation，区分“更多训练数据”与“更合理共享”带来的收益。

**输出：** 画一张 modality transfer matrix 和一张 interaction transfer matrix，解释两者为何不是同一件事。与统一 shared encoder 比较。证据：primary abstract + slides pp6–11。

## 2. MAPoRL2（原始记录标题：MAPoRL）· 核心

[课程链接：MAPoRL / Multi-Agent Post-Co-Training](https://arxiv.org/abs/2502.18439)

**来源差异：** 课程表写 MAPoRL2，链接当前原始元数据标题是 **MAPoRL: Multi-Agent Post-Co-Training for Collaborative Large Language Models with Reinforcement Learning**。保留两种标记，不假定它们是两个已核实的不同方法。

**为什么读：** Abstract 描述 independent responses → multi-turn discussion → verifier → multi-agent RL。它研究显式训练协作，而不只调用未经训练的多个模型相互聊天。

**检查与提取：** Verifier 如何分别衡量 answer correctness 与 corrective / persuasive discussion？哪些模型的 weights 更新？训练 agent 数量、模型能力和总预算是否与 baseline 对齐？

**输出：** 对比 single-agent post-training、frozen multi-agent debate、multi-agent co-training；逐项写参数更新位置及 reward 来源。证据：primary abstract；verifier 实现与 ablation 待全文。

## 3. LLaVA-Med 标题与 BiomedCLIP 链接冲突 · 优先澄清

课程指定标签为 **LLaVA-Med: Training a Large Language-and-Vision Assistant for Biomedicine in One Day**，但[课程原链接 2303.00915v3](https://arxiv.org/abs/2303.00915v3)实际指向 **BiomedCLIP: a multimodal biomedical foundation model pretrained from fifteen million scientific image-text pairs**。

与标题匹配、且已核实的候选链接是 [LLaVA-Med, 2306.00890](https://arxiv.org/abs/2306.00890)。这是编者提供的 correction candidate，尚不能证明教师当时想指定哪一篇；两者 abstract 均已核实。

**若按原链接读 BiomedCLIP：** 关注 biomedical image-text pretraining、domain-specific adaptation，以及 retrieval / classification / VQA 的 transfer。检查 paired data 怎样构成，跨医学图像类型泛化如何评价。

**若按标题读 LLaVA-Med：** 关注 figure-caption alignment 与生成的 instruction-following data 形成的 curriculum；检查 vocabulary alignment 与 conversational instruction tuning 两阶段分别带来什么。标题中的 “One Day” 有训练资源条件，不能理解为任意单卡都能复现。

**输出：** 做两行对照：pretraining objective、training data、model output、downstream evaluation。不要把 BiomedCLIP 的数据规模归给 LLaVA-Med，也不要把后者的 conversational behavior 归给前者。

## 4. DreamLLM · 核心

[DreamLLM: Synergistic Multimodal Comprehension and Creation](https://arxiv.org/abs/2309.11499)

**为什么读：** Abstract 把 multimodal comprehension 与 creation 的共同训练连接起来，并强调 raw interleaved image-text documents。

**检查与提取：** 理解与生成各用什么 objective？生成 raw modality 相比预测外部 encoder features 保留什么、付出什么成本？“Synergy”是否由相互改善的 ablation 支持，还是仅由联合性能表达？

**输出：** 画理解任务与生成任务之间的监督流，对照课堂把 secondary modality 当 auxiliary target 的 co-learning。记录 inference 时是否仍需要多模态输入。证据：primary abstract；网络与 loss 细节待全文。

## 5. PaLM-E · 扩展

[PaLM-E: An Embodied Multimodal Language Model](https://arxiv.org/abs/2303.03378)

**为什么读：** 它把 visual、continuous state estimation 与 textual encodings 编成交错的 multimodal sentences，并研究不同任务和模态的 positive transfer。

**检查与提取：** 连续 sensor state 如何进入语言模型？哪些 embodied tasks 使用 joint training？Robotic manipulation planning 的输出与 OpenVLA 的 low-level action 输出有什么区别？如何测量保留原有语言能力？

**输出：** 在训练 / 推理输入表中标出不同任务的 modalities，并注明 transfer direction。与 HighMMT 比较共享机制、与 OpenVLA 比较 action interface。证据：primary abstract；具体任务差异待正文。

## 统一交付

每篇填一行 `primary task → secondary information → training access → inference access → changed parameters → evidence of transfer`。先确认信息预算公平，再讨论效果，尤其避免将更多 inference input 的优势解释为更好的 cross-modal learning。
