# Large multimodal models · 从跨模态表示到 MLLM

2026-03-03 · Week 5.1 · 资料：36 页 slides + 公开视频英文字幕。视频开头继续上一讲的 alignment，随后才进入本讲新主题。

## 三分钟预览

这一讲把三件事串起来：先让视觉、声音和语言彼此提供上下文，再把非文本表示接入预训练 LLM，最后让输出端从纯文本扩展到图像检索和生成。学习重点是明确每个模块接收什么、输出什么、用哪些配对数据训练，以及哪些权重被冻结。

## 内容与原始材料对照

| 主题 | Slides | 视频入口 |
|---|---|---|
| 从语言模型扩展到 multimodal foundation model | [第 5–10 页](https://mit-mi.github.io/mmai-course/spring2026/schedule/lec5.1%20-%20large%20multimodal%20models.pdf#page=5) | [35:49 起](https://www.youtube.com/watch?v=H9nvkyTsrnI&t=2149s) |
| adapter 把视觉特征映射到 token embedding | [第 18–21 页](https://mit-mi.github.io/mmai-course/spring2026/schedule/lec5.1%20-%20large%20multimodal%20models.pdf#page=18) | [57:14 起](https://www.youtube.com/watch?v=H9nvkyTsrnI&t=3434s) |
| alignment pre-training 与 instruction tuning | [第 23–26 页](https://mit-mi.github.io/mmai-course/spring2026/schedule/lec5.1%20-%20large%20multimodal%20models.pdf#page=23) | [63:26 起](https://www.youtube.com/watch?v=H9nvkyTsrnI&t=3806s) |

时间链接定位到相关字幕段落起点，并非逐帧同步页码。

## 必须建立的模型图景

1. **cross-attention 是有方向的。** 语言提供 Query、视觉提供 Key/Value 时，输出长度跟随语言序列。第 11 页公式可写为 `Attention(Q,K,V) = softmax(QKᵀ / √d)V`。图文可以有不同数量的 token，注意力在两者之间建立软对应，不要求输入预先逐词对齐。
2. **aligned representation 和 fused representation 不同。** 两个 encoder 的输出可在相似度空间协调；进入 cross-attention 后，某个模态的表示又会依赖另一模态。ViLT 与 ALBEF（第 14–16 页）适合用来比较“对齐目标”和“融合结构”各自承担什么。
3. **连接层必须同时解决尺寸与语义问题。** adapter 可以把视觉 embedding 投到 LLM 的输入维度，但维度相同还不代表 LLM 理解它。需要训练信号让这些向量对后续文本生成有用。
4. **预训练与指令微调回答不同问题。** 图像描述配对让模型学习图文联系；instruction tuning 让模型适应问答、解释等用户任务。MiniGPT-4 的两阶段结构是本讲的具体例子，不应推广为所有 MLLM 的固定配方。
5. **冻结与更新是一张参数清单。** 读 Flamingo、prefix tuning 或 LLaMA-Adapter 时，分别标出 vision encoder、projector、LLM 和新增 attention 的可训练状态。“少量参数更新”不等于没有显存或数据成本。
6. **生成端还有另一套接口。** 第 27–34 页讨论图像检索和把语言表示接入生成模型。检索只能选择已有素材；生成扩大输出空间，也要额外评估内容与跨模态一致性。

## 容易混淆

“会描述图像”不证明模型进行了精细视觉 grounding；可能主要依赖语言先验。高质量数据筛选、训练阶段与评估集分布应同时记录。课中数据规模是本次讲义快照，不作为当前最大数据集的排行榜。

## 自测与动手

- 给定 20 个文本 token、196 个视觉 token，写出 cross-attention 权重矩阵与输出形状。
- 为冻结 LLM 的图像问答系统列出各模块的输入、输出、梯度流向。
- 设计“原图 / 图像打乱 / 无图”三组检查，判断输出是否真的使用视觉证据。

建议产物：一张参数冻结表，以及 5 个需要图像信息才能回答的问题。继续阅读 [本讲 Readings guidance](readings.md)。
