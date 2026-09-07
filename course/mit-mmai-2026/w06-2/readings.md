# Readings guidance · Diffusion 与 flow matching

建议阅读顺序：Flow Matching 原论文 → Guide and Code → latent space / DiT / rectified flow → text、motion、music 应用 → 统一理论。优先级为个人学习建议。本页使用官方摘要和来源核验，实验、证明条件需进入原文检查。

## 基础与架构

| Reading | 阅读任务 |
|---|---|
| [Flow Matching for Generative Modeling](https://arxiv.org/abs/2210.02747) | 核心。分清 conditional probability path 与 marginal path；解释为何训练可通过回归向量场进行，以及 simulation-free training 不等于 sampling 不用 ODE solver。原文明确允许 diffusion paths 作为实例。 |
| [Flow Matching Guide and Code](https://arxiv.org/abs/2412.06264) | 实践主线。按基础定义、设计选择、实现例子阅读；画出 noise、time、data、target velocity 的张量流。运行示例前核对代码版本与采样参数。 |
| [Scalable Diffusion Models with Transformers](https://arxiv.org/abs/2212.09748) | DiT 用 Transformer 替换 latent diffusion 的 U-Net。记录 patch size、tokens、depth/width、GFLOPs 如何变化；不要只按参数量解释 FID。 |
| [Flow Matching in Latent Space](https://arxiv.org/abs/2307.08698) | 看 pretrained autoencoder 带来的压缩成本与重建瓶颈；核对 NFE、分辨率、条件任务及误差界的假设，区分 latent modeling 与 pixel fidelity。 |
| [Scaling Rectified Flow Transformers for High-Resolution Image Synthesis](https://arxiv.org/abs/2403.03206) | 查噪声尺度采样、modality-specific weights 与双向图文交互。把 trajectory/objective、architecture、data 三类改动拆开，寻找可隔离贡献的实验。 |

## 跨模态应用

| Reading | 阅读任务 |
|---|---|
| [Large Language Diffusion Models](https://arxiv.org/pdf/2502.09992) | LLaDA 的 forward masking 和 reverse token prediction 怎样定义？比较 AR baseline 的训练预算、SFT、生成长度与采样步数；reversal task 优势不自动推广到所有推理任务。 |
| [FlowMotion](https://arxiv.org/abs/2504.01338) | 重点看 target-predictive CFM 与 jitter。区分运动平滑、动作语义匹配和分布质量；在 HumanML3D / KIT 等数据集上检查指标，而非只看视频流畅度。官方标题比课表版本更长。 |
| [MusFlow](https://arxiv.org/abs/2504.13535) | 多种条件如何映射到 CLAP embedding，再约束 VAE latent 中的 CFM？记录 image/story/caption 各自与组合的测试，以及自动标注数据可能引入的偏差。 |

## 统一理解与错链

[Exploring Diffusion and Flow Matching Under Generator Matching](https://arxiv.org/abs/2412.11024) 从统一的 generative Markov framework 比较两种方法。建议带着“确定性与随机性放在哪一层、哪些路径共享理论形式”阅读，逐条记录条件，不把统一形式误写成所有实现完全等价。

课表的 **Unraveling the Connections Between Flow Matching and Diffusion Probabilistic Models** 链到 [arXiv 2311.07625](https://arxiv.org/abs/2311.07625)，实际为 **Activity Sparsity Complements Weight Sparsity for Efficient RNN Inference**。这是错链，不应用 RNN sparsity 论文来支持 flow/diffusion 结论。

[arXiv 2411.07625v1](https://arxiv.org/abs/2411.07625v1) 是经核验的同名前缀候选，标题含 **in Training-free Conditional Generation**；该工作的后续版本改名为 **Flow Matching Posterior Sampling**。保留 v1 链接可解释课表标题，但教师原意尚未独立确认。阅读时特别留意其 conditional generation 范围。

## 最终产物

用一页表填写每种方法的 state space、noise path、training target、conditioning、solver、NFE、数据与指标。选一组相同 compute/NFE 的比较，再解释哪些结论受模型大小或数据混合影响。回到 [课程预览](preview.md) 检查“flow matching 必然更快”等过度概括。
