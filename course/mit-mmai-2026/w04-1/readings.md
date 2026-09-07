# W04-1 · Reading guidance：先量化交互，再比较融合模型

本节六项 Reading 分成两条线：前两篇帮助判断 dataset 和 model 中的 interaction，后四篇观察现代 MLLM 如何组织图像与文本。建议先读诊断再读架构。P1/P2/P3 是本归档建议，全部条目均来自课程表；本次证据主要是作者摘要与出版商摘要，**未逐页审阅全文，未复现实验**。

## P1 · Quantifying & Modeling Multimodal Interactions: An Information Decomposition Framework

[论文](https://arxiv.org/abs/2302.12247) · 证据：primary abstract。

带着问题读：任务需要 redundancy、uniqueness 还是 synergy，能不能在选模型前量化？摘要提出 PID statistics，以及用于高维分布的两个 estimator；它区分数据中需要的交互和模型实际捕捉的交互，并在已知 PID 的 synthetic data 与多模态 benchmark 上检验。

优先寻找 PID 定义、估计过程、synthetic sanity checks 与 model-selection case studies。提取与检查：画出 `输入模态 × target` 的三类信息关系，记录 estimator 依赖的数据量和假设；特别分开“真实任务有 synergy”与“训练模型学到 synergy”。如果更换 target，PID 也需要重新考虑。

## P1 · Does my multimodal model learn cross-modal interactions? It’s harder to tell than you might think!

[ACL Anthology](https://aclanthology.org/2020.emnlp-main.62/) · 证据：作者论文在官方 Anthology 的摘要与题录。

带着问题读：多模态模型超过 unimodal baseline，为什么还不能证明 interaction 有贡献？摘要说明 EMAP（empirical multimodally-additive function projection）消除已训练模型预测中的非加性交互，保留 additive unimodal structure；在论文研究的七类 image+text classification tasks 中，不少模型的性能变化很小。

优先检查 projection 如何构造、原模型与投影使用什么评价、如何在样本上计算近似。提取一个三列对照：unimodal、multimodal、EMAP。不要将特定任务结果推广成“多模态交互都没有用”；也不要把“投影后仍有高性能”误读成模型内部完全没有交互计算。

## P2 · Kosmos-2: Grounding Multimodal Large Language Models to the World

[论文](https://arxiv.org/abs/2306.14824) · 证据：primary abstract。

带着问题读：只会说对象名字的 MLLM 怎样表达对象位置？摘要介绍将 referring expressions 与 bounding boxes 相连的表示，以及 grounded image-text dataset GrIT。优先找 location tokens、训练数据构造，以及 referring expression comprehension 与 generation 的区别。

提取与检查：手写一个包含文本片段和坐标的模型输入/输出示例，标明坐标对应哪张图、使用何种尺度。比较“文本语义答对”与“框真的落在目标上”的评价。它对本周的价值是展示显式跨模态连接，而不能仅凭 grounding 能力推出模型掌握所有高阶 interaction。

## P2 · Chameleon: Mixed-modal early-fusion foundation models

[论文](https://arxiv.org/abs/2405.09818) · 证据：primary abstract。

带着问题读：当 image 和 text 可以在输入输出任意交错时，early fusion 带来什么训练要求？摘要描述 token-based mixed-modal family，可理解和生成混合序列，并强调稳定训练、alignment recipe 与 long-form mixed-modal generation。

优先寻找 image tokenization、混合序列组织、训练稳定性与评估设计。提取一个交错文档样例，写出每一步预测的是哪种 token。与只输入图像、只输出文字的系统比较，指出评估必须增加哪些 image generation 和跨段一致性检查。不要将“early fusion”与“比其他模型更懂 synergy”画等号。

## P2 · MM1: Methods, Analysis and Insights from Multimodal LLM Pre-training

[出版商论文入口](https://link.springer.com/chapter/10.1007/978-3-031-73397-0_18) · 证据：官方出版商摘要，全文为订阅内容，未审阅。

带着问题读：performance 改变来自 connector，还是 image encoder、resolution、image token count 和 data mixture？摘要报告对这些因素的 ablations，强调 image-caption、interleaved image-text、text-only 混合，以及在其设定下图像编码与输入规模因素的较大影响。

优先找 ablation 表格中保持不变的项目与实际变动的变量。提取一个“变量—预算—metric—观察”的表，检查数据量和 compute 是否同时改变。摘要中 connector 相对不重要的观察应限于论文比较的设计空间；不能推出任何 connector 都等价。

## P3 · MoMa: Efficient Early-Fusion Pre-training with Mixture of Modality-Aware Experts

[论文](https://arxiv.org/pdf/2407.21770) · 证据：primary abstract。

带着问题读：early-fusion 模型仍能否保留 modality-specific computation？MoMa 将专家分成 text/image groups，组内 learned routing；摘要报告相对于 dense 与标准 MoE 对照的 pre-training FLOPs 节约，并明确与 mixture-of-depths 组合虽进一步省算力，却增加 router 误差敏感性并损伤某些推理表现。

优先检查 token-to-expert routing、active parameters、training loss 对齐方式，以及 causal inference 时 routing 的条件。提取与检查：同时记录 total parameters、每 token 激活参数、FLOPs 与 downstream metric。不能把以 pre-training loss 衡量的 compute efficiency 直接当成所有下游任务的同倍速提升。

## 把六篇接成一个决策

| 你想证明的事 | 最直接的阅读入口 |
| --- | --- |
| 数据本身需要什么 interaction | PID framework |
| 当前模型的增益是否来自非加性关系 | EMAP |
| 如何显式表示词与区域的对应 | Kosmos-2 |
| 如何统一交错图文理解与生成 | Chameleon |
| 架构/data 配方中哪个变量重要 | MM1 |
| 如何按模态分配稀疏计算 | MoMa |

交付一页实验方案：选择一个任务，列出 unimodal、additive、复杂 fusion 三个 baseline；写出一个 interaction probe；再选一种现代架构，解释它改变的是输入表示、信息交换、训练目标还是资源分配。最后写一句目前证据能支持的结论和一句仍需实验的假设。[返回 preview](preview.md)
