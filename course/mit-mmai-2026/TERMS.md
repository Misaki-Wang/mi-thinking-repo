# 术语表与翻译约定

本课程笔记以中文解释为主，保留论文、slides 和视频中便于检索的专业英文术语。首次出现采用“中文（English, 缩写）”；后文可直接使用英文术语或缩写。模型名、论文名、数据集名、代码变量、公式符号不翻译。

## 数据、表示与对齐

| English | 本课程用法 | 阅读时区分 |
|---|---|---|
| modality | 模态（modality） | 感知/表达形式，不等同于一个文件或一个传感器 |
| heterogeneity | 异质性（heterogeneity） | 结构、分布、噪声和任务相关性都可能不同 |
| representation learning | 表示学习 | 学习任务有用的信息表示 |
| multimodal fusion | 多模态融合（fusion） | 汇合多种输入来构建联合表示或预测 |
| early / late fusion | 早期 / 后期融合 | 在特征级或决策级进行组合 |
| cross-modal interaction | 跨模态交互 | 联合使用带来的依赖，不只是把向量拼接 |
| redundancy / uniqueness / synergy | 冗余 / 独有信息 / 协同信息 | 都需要指定目标任务或随机变量 |
| alignment | 对齐（alignment） | 本课通常指跨模态对应；不自动等于人类偏好 alignment |
| grounding | grounding（与感知或环境证据建立对应） | 不统一替换成泛化的“理解” |
| contrastive learning | 对比学习（contrastive learning） | 正负样本、相似度、温度与采样共同决定目标 |
| self-attention / cross-attention | 自注意力 / 交叉注意力 | Query 与 Key/Value 的来源是否相同 |
| Query / Key / Value | Query / Key / Value（Q/K/V） | 保留符号以便追踪矩阵尺寸 |
| contextualized representation | 上下文化表示 | 表示随另一个输入或上下文变化 |
| invariance / equivariance | 不变性 / 等变性 | 输入变换后输出不变，或随之按规则变换 |
| co-learning / transfer | 协同学习 / 迁移 | 训练和测试可用模态必须分开说明 |

## 模型与生成

| English | 本课程用法 | 阅读时区分 |
|---|---|---|
| foundation model | 基础模型（foundation model） | 预训练复用能力，不保证所有领域可靠 |
| LLM / VLM / MLLM | 保留 LLM / VLM / MLLM | 大语言模型 / 视觉语言模型 / 多模态大语言模型 |
| adapter / projector | adapter / 投影层（projector） | 接口或适配参数，不统一写成 LoRA |
| prefix tuning | 前缀调优（prefix tuning） | 输入侧连续表示与模型权重更新不同 |
| instruction tuning / SFT | 指令微调 / 监督微调（SFT） | 训练数据和监督目标应明确 |
| LoRA | 低秩适配（LoRA） | 低秩权重增量；不等于量化 |
| quantization | 量化（quantization） | 权重量化与 visual token 的向量量化不同 |
| MoE | 混合专家（Mixture of Experts, MoE） | 总参数与每个 token 激活参数不同 |
| autoregressive | 自回归（autoregressive） | 按条件链式分解逐步生成 |
| latent variable | 潜变量（latent variable） | 未观测变量不必天然对应人类语义 |
| VAE / VQ-VAE | 保留 VAE / VQ-VAE | 连续潜变量与离散码本机制不同 |
| ELBO | 证据下界（ELBO） | 常见 VAE 优化目标，不是精确 log-likelihood |
| diffusion | 扩散模型（diffusion） | 明确噪声过程、预测参数化与采样器 |
| score | score（对数密度关于输入的梯度） | 在 diffusion 中不是任意评分指标 |
| flow matching | 流匹配（flow matching） | 学习向量场；不等于一次网络调用就完成生成 |
| rectified flow | rectified flow | 保留原名，与一般 normalizing flow 区分 |
| classifier-free guidance / CFG | 无分类器引导（CFG） | guidance scale 改变条件遵循与多样性的权衡 |
| FID / CLIP Score | 保留 FID / CLIP Score | 分布距离与图文相似度不代表全面质量 |

## 推理、智能体与评估

| English | 本课程用法 | 阅读时区分 |
|---|---|---|
| reasoning / Chain-of-Thought | 推理 / 思维链（CoT） | 可见推理文本不自动证明真实决策机制 |
| policy / value / advantage | 策略 / 价值 / 优势（advantage） | 行动分布、预期回报、相对基线改进 |
| RLHF / PPO / GRPO / DPO | 保留缩写 | 偏好学习、在线 RL、组内奖励标准化等机制分别说明 |
| reward hacking | 奖励投机（reward hacking） | 提高代理奖励却没有实现真实目标 |
| agent / tool use | 智能体（agent）/ 工具使用 | 观察、行动、反馈与停止条件组成闭环 |
| memory / context window | 记忆 / 上下文窗口 | 长上下文不等于可靠的长期记忆机制 |
| train / validation / test | 训练 / 验证 / 测试集 | test 不用于选超参数或选择最佳案例 |
| ablation | 消融实验（ablation） | 控制其他条件后改变单一组件 |
| calibration | 校准（calibration） | 置信度与实际正确率是否匹配 |
| explanation faithfulness | 解释忠实性 | 解释是否反映决策依据，而非仅合理、流畅 |
| compositional generalization | 组合泛化 | 熟悉元素的新组合，不仅是新样本 |
| distribution shift / OOD | 分布偏移 / 分布外（OOD） | 与同分布测试分开报告 |
| leakage | 信息泄漏（leakage） | 标签、未来信息、近重复样本进入训练或输入 |
| prescriptive modeling | 决策建议建模（prescriptive modeling） | 从预测转向约束下的行动选择 |

## 自动字幕处理

英文稿保留来源的用词。中文可按上下文识别明显的专业术语误识别，但需保留可回查的英文段落；存在歧义时注明“原字幕疑似误识别”。不要把 LLM、LLS、multimodel 等自动字幕拼写错误无条件当作新的模型名称。中文稿是学习辅助译稿，不能替代对原始 slides、公式和论文的核对。
