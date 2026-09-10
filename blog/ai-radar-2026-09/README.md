# AI 研究与工程：近一个月值得读什么

时间窗口：**2026-08-10 至 2026-09-10**（含首尾日期）。按“研究与技术为主，兼顾产业”精选 **12 条核心资料＋7 条延伸阅读，来自 12 个信息源**。检索与核验日期：2026-09-10。

本页不是新闻全量搬运或全行业排名。优先选择有方法、实现、实验条件或一手讨论的内容；同一机构的多篇文章不算独立佐证。日期指文章／节目本身，不保证它谈到的论文、代码或事件也是本月首次出现。

[信息源目录与筛选原则](SOURCES.md) · [阅读路线与研究问题](GUIDANCE.md) · [返回 Blog](../README.md)

## 先读这三条

| 入口 | 推荐理由 | 读完留下什么 |
| --- | --- | --- |
| [R01：知识与 recall](#r01) | 把答错拆成不同失败类型 | 一张 fact-level 评估设计表 |
| [R02：data × recipe](#r02) | 学习分离混杂因素 | 一张变量、控制项与外推边界表 |
| [S02：hybrid cache](#s02) | 从模型状态理解系统正确性 | 一张状态类型与安全复用边界表 |

推荐次序和学习产物是本归档的编辑建议，不是论文结论，也不表示已执行实验。

## 核心精选

### R01

**知识被编码了，为什么仍然答不出来？** · 2026-08-12 · Google Research · 研究

作者／发布：Nitay Calderon; Gal Yona。[原文或原节目](https://research.google/blog/empty-shelves-or-lost-keys-recall-is-the-bottleneck-for-parametric-factuality/)。阅读依据：研究团队正文。

- **讲什么：**以 fact 而非单道题为单位，区分 encoding、recall 与 recognition，并用 WikiProfile 检查不同问法和 thinking 条件。
- **为什么读：**建立比单一 accuracy 更有诊断力的知识评估。
- **证据边界：**encoding 是行为操作化定义，不是直接读出参数中的事实；Wikipedia 子集与自动评分不能外推为掌握全部知识。
- **阅读定位：**Knowledge profiling → How we evaluate LLMs → Reverse questions；原文附论文和数据入口。

### R02

**把 data 与 model recipe 的贡献拆开测量** · 2026-09-08 · Dwarkesh · 研究

作者／发布：Dwarkesh Patel; Jerry Han。[原文或原节目](https://www.dwarkesh.com/p/pretraining-progress-is-mostly-data)。阅读依据：作者原创实验与方法附录。

- **讲什么：**组合不同时期的训练配方与数据集，在相同 tokenizer、context 和算力预算框架下比较 downstream 能力。
- **为什么读：**重点是 factorization、超参数控制和效应解释，而不是照抄标题。
- **证据边界：**最大预算为 10¹⁹ FLOPs；scaling curves 至少 3 seeds，但 7×7 grid 每格 1 seed。未覆盖 frontier scale、post-training 或 synthetic data。
- **阅读定位：**正文结果后读 Appendix: Methodology；不要推出“架构不重要”。

### R03

**从固定抽帧到主动检索视频片段** · 2026-09-01 · Google DeepMind · 研究

作者／发布：Rohan Doshi; Mario Lučić。[原文或原节目](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-agentic-video-in-gemini/)。阅读依据：团队技术与产品说明。

- **讲什么：**用原生视频工具按问题选择片段、采样速度及帧／音频／讲稿信息，而非始终按固定 FPS 处理全片。
- **为什么读：**思考怎样以检索降低长视频理解成本。
- **证据边界：**收益来自厂商特定 benchmark；不是任何视频都达到同样提升，也不是完整逐字转写的替代保证。
- **阅读定位：**How it works 与 Benchmarks；比较静态采样和查询驱动的信息遗漏风险。

### R04

**环境边界失效后，怎样分析模型行为？** · 2026-09-09 · Anthropic Research · 研究

作者／发布：Anthropic。[原文或原节目](https://www.anthropic.com/research/alignment-assessment-cybersecurity-incidents)。阅读依据：厂商事故分析相关章节。

- **讲什么：**复盘评估环境配置失误下的模型行为，讨论 biased reasoning、recklessness，以及评估与训练环境的不足。
- **为什么读：**区分基础设施、模型行为与证据解释，不只依赖模型 CoT 自述。
- **证据边界：**本月文章复盘更早事件；作者未找到单一训练根因。具体评估情境不能推广为全部部署模型行为。
- **阅读定位：**Alignment assessment summary 与 Discussion；区分实际事件、模拟复现和假说。

### S01

**真实 Agent workload 与单请求吞吐不一样** · 2026-09-08 · vLLM · 工程

作者／发布：vLLM Team; Inferact。[原文或原节目](https://vllm.ai/blog/2026-09-08-vllm-agentx)。阅读依据：项目团队技术正文。

- **讲什么：**用多轮 coding-agent traces 分析 prefix reuse、KV cache locality、parallelism 和调度的相互影响。
- **为什么读：**读“更均匀的负载也可能更慢”等反例，建立端到端延迟—成本视角。
- **证据边界：**total tokens/GPU-second 包含 cached tokens；成本比较不等于模型能力等价，收益依赖 workload。
- **阅读定位：**先读 workload characterization，再看失败配置及 cache locality。
- **继续进入：**[AgentX harness](https://github.com/SemiAnalysisAI/agentx-harness)

### S02

**Hybrid model 的缓存首先要复用正确** · 2026-08-11 · SGLang / LMSYS · 工程

作者／发布：Zhangheng Huang 等。[原文或原节目](https://www.lmsys.org/blog/2026-08-11-unified-radix-cache/)。阅读依据：项目团队技术正文。

- **讲什么：**在同一 radix topology 中组合 full-attention KV、sliding-window KV 与 recurrent state，保留不同的安全复用边界。
- **为什么读：**与 Kimi 架构领读配对：模型状态不同，cache correctness 也不同。
- **证据边界：**session-aware 对比同时改变实现与 eviction policy；Rust 版本是 L1-only 实验原型，不等同完整 HiCache。
- **阅读定位：**TreeComponent 与复用边界，再看多层存储和 session-aware eviction。
- **继续进入：**[实现 PR #21206](https://github.com/sgl-project/sglang/pull/21206)

### S03

**多模态服务何时值得拆开 encoder、prefill 与 decode？** · 2026-09-09 · NVIDIA Technical Blog · 工程

作者／发布：Jesse Gu; Ryan McCormick; Akshatha Kamath。[原文或原节目](https://developer.nvidia.com/blog/when-to-use-encode-prefill-decode-disaggregation-to-accelerate-multimodal-model-serving/)。阅读依据：团队技术正文，非顶部自动摘要。

- **讲什么：**比较聚合、同卡独立 encoder 与异构 GPU 分离布局，检查媒体输入量、输出长度、模型规模等条件。
- **为什么读：**正面与负面案例都有，适合学习 workload-conditioned benchmark。
- **证据边界：**存在分离后 goodput 下降的配置；最多倍数不是一般规律，必须带上 GPU、模型与输入输出条件。
- **阅读定位：**对照三种布局与反例，注意 TTFT、端到端延迟和 goodput 的差别。
- **继续进入：**[Dynamo EPD experiments](https://github.com/ai-dynamo/dynamo/tree/release/1.5.0/benchmarks/multimodal/sweep/experiments/epd)

### S04

**Online RL 的瓶颈可能在权重同步** · 2026-08-22 · vLLM · 工程

作者／发布：Aaron Hao 等。[原文或原节目](https://vllm.ai/blog/2026-08-22-rdt-weight-transfer)。阅读依据：项目团队技术正文。

- **讲什么：**通过 dry run 推导所需分片，用 RDT/NIXL 只传必要 shard，并重叠 gather、transfer 与后处理。
- **为什么读：**将 trainer→rollout 同步开销纳入系统分析，而不是只优化训练算子。
- **证据边界：**大模型低秒级结果使用大规模 H100 集群；当前不兼容 EPLB，destination buffers 另占显存。
- **阅读定位：**传输规划、故障恢复与 memory accounting；保留集群规模。
- **继续进入：**[SkyRL 示例](https://github.com/NovaSky-AI/SkyRL/tree/main/examples/train/megatron/sharded_rdt) · [vLLM 文档](https://docs.vllm.ai/en/latest/training/weight_transfer/sharded_rdt/)

### L01

**把 post-training 新闻放回技术框架** · 2026-08-10 · Interconnects · 解读

作者／发布：Nathan Lambert。[原文或原节目](https://www.interconnects.ai/p/5-useful-things-youll-learn-in-my)。阅读依据：作者教材导读正文。

- **讲什么：**以算法直觉、off-policy 与 throughput、RLHF 历史、distillation 和 evaluation 等入口组织学习。
- **为什么读：**先补框架再读系统实现与模型分析；原文链接免费在线教材及课程材料。
- **证据边界：**本月新的是导读，不是全部教材和课程；也需识别作者推广自己教材的立场。
- **阅读定位：**先读算法与系统权衡两节，再按问题进入教材。

### V01

**Kimi K3 架构领读：连接模型与系统** · 2026-08-26 · 张小珺商业访谈录 · 视频

作者／发布：张小珺商业访谈录。[原文或原节目](https://www.bilibili.com/video/BV1KZ8X6uEPL/)。阅读依据：作者简介与既有 ASR 片段抽查。

- **讲什么：**围绕 Attention、Normalization、MoE 与 Distillation 建立术语地图，再与 hybrid cache、推理服务文章对照。
- **为什么读：**中文长访谈入口，已有本站预览和时间位置讲稿，便于回看。
- **证据边界：**8 月 26 日是视频日期，不是全部被讨论论文的日期；ASR 初稿仍可能误识别专业术语。
- **阅读定位：**先看主题预览；技术结论回到原视频及报告核对。
- **继续进入：**[本站主题预览](../../video/bilibili-280780745/BV1KZ8X6uEPL/preview.md) · [已有自动讲稿](../../video/bilibili-280780745/BV1KZ8X6uEPL/transcript.zh-CN.md)

### V02

**用可解释性访谈提出研究问题** · 2026-08-27 · 硅谷101 · 视频

作者／发布：硅谷101；嘉宾 Aryaman Arora；主持 Yiwen。[原文或原节目](https://www.bilibili.com/video/BV1gyhF6wEDD/)。阅读依据：仅作者简介，未阅读全文讲稿或完整回看。

- **讲什么：**简介围绕内部表示干预、CoT、模型个性与可信度提出问题，是进入 interpretability 的讨论入口。
- **为什么读：**与知识 profiling 配对，区分行为测试、内部干预和模型自述。
- **证据边界：**本条是简介级筛选，不冒充精读；本站没有该期完整讲稿，也没有官方章节时间轴。
- **阅读定位：**先看中文导读，再观看原节目；不要从简介推断实验效果。
- **继续进入：**[本站简介预览](../../video/bilibili-508452265/BV1gyhF6wEDD/preview.md)

### I01

**用算力供给约束检查技术预期** · 2026-08-25 · Dwarkesh · 产业

作者／发布：Dwarkesh Patel；嘉宾 Dylan Patel。[原文或原节目](https://www.dwarkesh.com/p/dylan-patel-3)。阅读依据：官方讲稿相关章节。

- **讲什么：**讨论训练与推理资源分配、供应链扩产、融资和提前签约，提供需求之外的供给侧视角。
- **为什么读：**作为本期少量产业背景，识别技术可行性与现实供给的差别。
- **证据边界：**标题及未来算力份额是预测；营收、价格和债务数字未独立审计，不用于投资判断。
- **阅读定位：**优先读官方讲稿 00:07:01–00:33:27；完整节目 1:16:52。

## 延伸阅读

按当前问题挑选即可，不要求全部读完。以下日期均是本次窗口内的文章／访谈发布日期。

### E01

**[TimesFM-3：跨变量与时间的 Attention](https://research.google/blog/timesfm-3-a-zero-shot-foundation-model-for-multivariate-forecasting/)** · 2026-08-31 · Google Research

交替 temporal/variate attention 与单次预测，为多变量 foundation model 提供架构案例。 厂商排名有任务与 covariate 条件，不能推出任意预测场景都更好。

### E02

**[双盲评估：保护模型与测试集](https://deepmind.google/blog/piloting-the-worlds-first-double-blind-ai-evaluations/)** · 2026-08-27 · Google DeepMind

用 confidential computing 隔离权重与题目，讨论外部评估的信任边界。 这是试点和协议说明，不证明全部污染已消除，也不证明评估题本身有效。

### E03

**[CUDA Graph：动态形状、capture 与显存](https://www.lmsys.org/blog/2026-08-17-advanced-cuda-graph/)** · 2026-08-17 · SGLang / LMSYS

比较 full capture、Breakable CUDA Graph 与 piecewise capture，关注启动开销和 resident memory。 本月是系统讲解，BCG 首实现更早；prefill-only 加速不等于整服务吞吐提升。

[Breakable CUDA Graphs](https://github.com/meta-pytorch/breakable-cuda-graphs)

### E04

**[FP8 不只是低精度 GEMM](https://pytorch.org/blog/fp8-training-on-amd-gpus-with-torchtitan-and-torchao-upstreaming-performance-improvements/)** · 2026-08-13 · PyTorch Blog

把数值格式正确性、quantization fusion 与内存搬运纳入性能分析。 特定 MoE kernel 的倍数不是端到端训练倍数；更快也不一定明显省显存。

[TorchAO fusion PR](https://github.com/pytorch/ao/pull/4311)

### E05

**[把模型进步的解释当作待检验假说](https://www.interconnects.ai/p/glm-53-how-chinese-labs-keep-stride)** · 2026-08-14 · Interconnects

围绕 RL environments、训练基础设施和发布节奏提出解释线索。 内部能力和产业机制包含作者推断，应与原始发布材料对读，不能当控制实验结论。

### E06

**[AI 自动化研究的瓶颈在哪里？](https://www.dwarkesh.com/p/ryan-greenblatt)** · 2026-08-11 · Dwarkesh

围绕可验证性、专家数据、RL 环境和能力泛化展开辩论，可先读前 48 分钟。 self-improvement 的幅度与时间线是观点，不是已发生的结果；完整节目 2:12:31。

### E07

**[推荐稳定性与 prompt sensitivity 的测量案例](https://www.latent.space/p/aeo)** · 2026-09-07 · Latent.Space

结合 prompt 改写、search 工具和多模型推荐输出，学习条件化行为测量。 AEO score 是自定义指标，样本与错误排除影响解释；不等于通用模型能力或训练数据来源排名。

## 本期筛掉了什么

- 首次发布日期不在窗口内的旧文章；不拿抓取时间或代码更新时间充数。
- 只有标题、无法核实正文的信息，不写成技术总结。V02 明确保留为“简介级入口”，不冒充精读。
- 重复报道、缺乏方法依据的榜单，以及与本期研究技术重点关联较弱的医疗或投资消息。
- 付费或登录墙后的未读取部分；不绕过访问限制，也不把可读文章视为获准全文转载。

## 如何使用与核对

所有摘记均为原创摘要和导读，专业名称保留英文。技术实现入口来自所链接原文；本次没有运行 benchmark、重现实验或审计财务数据。厂商结果、作者推断、访谈预测与已核查的发布日期分别标注。

月报是静态快照，没有替你订阅、购买或设置自动监控。若继续整理下一期，应重新检查日期与可访问状态，并保留旧快照。元数据与筛选记录见 [manifest.json](manifest.json)。
