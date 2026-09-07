# Multimodal LLMs tutorial · 一次可检查的 LoRA 微调

2026-03-05 · Week 5.2 · 来源为 [官方 Colab notebook](https://colab.research.google.com/drive/1fgUtzrorkGT8FdIY77Y_V4vQRULPAC5d)，未发现本课公开视频。这里的“单元”指 notebook cell，不能当作 PDF 页码。

## 三分钟预览

教程使用 Qwen2.5-VL-3B-Instruct，把 slides 图片、问题与解说组织为 image–question–answer 数据，先建立 baseline，再进行 LoRA fine-tuning，最后比较同一组 held-out images 的输出。最有价值的不是跑出一段解说，而是检查模型学到了可迁移的视觉理解，还是仅模仿了授课语气。

## Notebook 导航

| 位置 | 学习任务 | 需要保存的证据 |
|---|---|---|
| Step 0，单元 3–4 | 确認 PyTorch / CUDA 环境 | GPU 型号、版本与运行配置 |
| Step 1，单元 5–14 | 构造图像、问题、回答与数据切分 | 样本清单、分组规则、训练与测试隔离 |
| Step 2，单元 15–18 | 加载基础 VLM 与 baseline inference | 固定测试样本、原始输出、prompt |
| Step 4，单元 20–22 | LoRA 训练 | 学习率、batch、梯度累积、目标层、adapter 文件 |
| Step 5，单元 23–29 | 重载 adapter 与对比评估 | 同图同问题的 baseline / fine-tuned 结果 |

## 阅读代码时抓住六件事

1. **数据单位要完整。** 一个样本包含 image、question、answer。相邻 slides 或同一讲视频中的近重复画面高度相关，按样本随机切分可能高估泛化能力；建议额外按 lecture 或主题分组切分。
2. **文字描述与代码要对照。** notebook 前文提到保留 20% 测试集，后面实现先划出 20%，再拆成 validation 与 test，最终约为 80/10/10。学习记录应写实际使用的切分，不能混写为 80/20。
3. **baseline 必须在同一 held-out set 上测量。** Step 2 的说明讲 held-out images，但一个代码单元实际引用 `TRAIN[0]`。复现时需改成固定 TEST 样本；否则前后结果不具可比性。这是对 notebook 的学习审查，不表示本档案已经执行了这次微调。
4. **LoRA 学习的是权重增量。** 基础模型与 adapter 分开保存，推理时要以正确的 base checkpoint 加载对应 adapter。训练参数量、峰值显存和输出长度都值得记录。
5. **风格与内容分开评分。** 解说“像老师”不等于 slide 中的图表、公式和箭头被正确理解。评估应分别覆盖术语准确性、视觉证据、遗漏和幻觉。
6. **前后比较保持控制变量。** 使用同样的图、问题、system prompt、最大输出长度与解码策略，保存未经挑选的全部结果。

## 适合自己的最小练习

选 20 张不同主题 slides，其中至少 5 张含图表。先写一份包含“关键术语、图中关系、不能从图中推断的内容”的参考要点，再比较基础模型和 adapter 输出。此处是建议的练习规模，并非官方指定数据集大小。

## 自测

- 为什么同一张 slide 的多个截图不应随机散落在 train 与 test？
- style imitation 与 visual grounding 应如何分别评分？
- adapter 文件能否脱离原 base model 独立完成推理？

继续阅读 [本讲 Readings guidance](readings.md)。
