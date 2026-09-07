# W02-1 · Reading guidance：把 notebook 当作可检查的实验

本节三项 Reading 已全部核对身份：Karpathy 作者网页可读，两份 Colab notebook 已取得并检查正文与代码。本页没有执行这些训练 notebook。建议顺序是 PyTorch 基础 → training recipe → Code LLM adaptation；P1/P2 是本归档建议，不是官方 required/optional 划分。

## P1 · A Recipe for Training Neural Networks

[作者原文](https://karpathy.github.io/2019/04/25/recipe/) · 证据：作者网页正文。

带着问题读：如何在复杂模型之前建立对 pipeline 的信任？优先读 “Become one with the data”“Set up the end-to-end training/evaluation skeleton & get dumb baselines”“Overfit”“Regularize”。文中将数据理解、简单对照、单 batch 拟合、可视化网络前的实际 tensor，放在扩大模型之前。

提取与检查：建立四个断言：输入与标签正确；input-independent baseline 低于有效模型；少量样本可以被拟合；变动只影响预期计算路径。随后才讨论 regularization 与 tuning。文章发表于 2019 年，其中关于当时 self-supervised learning 或优化器经验的判断具有时代背景，不能机械当成 2026 年结论。

读后产物：一个 10 项以内的 debug checklist，其中至少有一项可以发现 batch 维度被错误混合，一项可以发现预处理导致的标签错位。

## P1 · MAS.S60 Pytorch Introduction

[课程 Colab](https://colab.research.google.com/drive/1SoTu6gvYcLNDqPwNPTWmsSYF-l-UfHPx?usp=sharing) · 证据：已取得完整 notebook 并核读下述相关 cells，未执行；cell 编号按下载版本顺序。

带着问题读：一个短训练循环在 CPU、GPU、autograd 与 optimizer 之间做了什么？先读 cells 2–17 的 tensor 与 runtime 说明，再跟随 SmellNet 示例：cells 28–37 检查传感器 state、分段平均和 substance-minus-ambient 差分；cells 49–59 检查标准化、划分、MLP、training loop 与评价；cells 63–71 比较 Random Forest。

提取与检查：把每一步 tensor 的 shape、dtype、device 写出来，并解释 `zero_grad → forward → loss → backward → step`。代码 cell 50 在完整 `X` 上 `fit_transform` StandardScaler，cell 52 才 `random_split`；这是测试集分布进入预处理的 leakage 风险，正式实验应先划分，再只在 train 上 fit。另需按原始采集 session 保留分组信息，检查相邻测量是否跨集合。

比较注意：NN 使用 `random_split`，Random Forest 使用另一个 `train_test_split`，原样输出不保证来自相同留出样本；示例中显示的 accuracy 也不是本归档重跑结果。cell 58 打印的是当轮最后一个 batch 的 loss，不是完整 epoch 的均值。可把这些细节改造成你自己的代码审查练习。

## P2 · Fine-tuning a Code LLM on Custom Code on a single GPU

[课程 Colab](https://colab.research.google.com/drive/1EDsjYRrAiujUew0GRJ_hyVoNMsSDnlnx?usp=sharing) · 证据：完整 notebook 静态检查，未执行。

带着问题读：quantization、LoRA、gradient accumulation、gradient checkpointing 分别节省什么？该 notebook 使用 `bigcode/starcoderbase-1b`、代码数据 `smangrul/hf-stack-v1`、4-bit NF4 与 LoRA，并包含 fill-in-the-middle（FIM）变换。优先读 cells 8–17 的 streaming、固定长度切块与 FIM；cells 18–24 的量化/LoRA；cells 26–40 的训练与 adapter inference。

提取与检查：画出“原始代码 → tokenizer → FIM/packing → causal LM loss”的路径，解释为什么 `labels=input_ids` 仍需检查模型内部的 shift。配置中 `MAX_STEPS=40`、`EVAL_FREQ=1000`，所以默认短跑不会触发每 1000 步的 periodic evaluation；单个 completion 看起来正确不能替代评估。训练段设置了 `push_to_hub=True` 并显式调用上传，执行前应把输出目的地改成自己的选择，不能把这些教学默认值当成本地训练必需步骤。

“single GPU”是带具体模型、序列长度和硬件条件的演示；notebook 文字提到 A100 High-RAM，不代表任意显卡都能原样运行。保存 trainable parameter count、实际 VRAM 与版本信息，才可复现资源结论。

## 比较与交付

PyTorch notebook 解释计算是怎样发生的，recipe 解释怎样确认它正确，Code LLM notebook 展示如何把同样原则扩展到预训练模型。交付一份 Markdown 实验记录：训练流程图、一个发现并修正的评价问题、统一 split 下的两个 baseline、资源配置，以及一次失败案例。使用本节 [preview](preview.md) 的样本清单作为输入。
