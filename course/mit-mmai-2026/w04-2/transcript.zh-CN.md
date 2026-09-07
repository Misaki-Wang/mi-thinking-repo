# Lecture 5 – Multimodal Alignment (MIT How to AI Almost Anything/Multimodal AI, Spring 2026)

_中文讲稿_

- Channel: Paul Liang
- Source: [YouTube](https://www.youtube.com/watch?v=u-H43tRgYJg)
- Duration: 1:23:04
- Caption source: automatic
- Status: complete
- Chinese translation: 103/103
- Translation provider: codex
- Generated: 2026-09-07T07:53:12+00:00

## 讲稿

### [00:00](https://www.youtube.com/watch?v=u-H43tRgYJg&t=0s) · b000001

欢迎回来。我们开始吧。那么，开始之前先通知几件事，呃。谢谢大家提交项目提案。呃，我们正在整理所有项目提案，制作一个电子表格，并会为每个项目分配几位导师。呃，要么是我，要么是助教（TAs），希望我们每周至少能和大家见一次面，跟踪项目进度。呃，这些项目导师会在本周通知各个小组。呃，希望大家每周都能和我们见面，帮助大家实际推进项目。呃，另外也是为了方便规划，正如我提过的，我们有一些额度。嗯，你们可以试着使用其中一些 KI 模型 \[字幕疑误，可能指 Kimi\]。他们声称这些是相当先进的多模态模型（multimodal models）。我们有 40 个小组，每组大约有 $50 的 Kimi 使用额度，另外还有 40 个小组，每组有 $40 的额度，可以用于你们

### [00:56](https://www.youtube.com/watch?v=u-H43tRgYJg&t=56s) · b000002

课程所需的其他任何东西，包括计算用的 GPU 或其他 API 调用。好吗？另外，记得继续完成作业 2。呃，截止时间是下周三。嗯，之后我们会发布作业三。好。大家对这些通知有什么问题吗？请说。&gt;&gt; 这些额度，呃，只分配给项目使用，对吧？还是说应该大致……？&gt;&gt; 呃，如果你们想用在作业上，也可以用，但我想这就是我们能提供的最高额度了。好。那么，我快速回顾一下多模态融合（multimodal fusion）。嗯，我觉得周二讲得有点快。在进入下一个要讨论的话题，也就是对齐（alignment）之前，我先用几张幻灯片回顾一下。不过大家应该记得，融合（fusion）就是接收不同的数据

### [01:52](https://www.youtube.com/watch?v=u-H43tRgYJg&t=112s) · b000003

模态（modalities），并学习某种联合表示（joint representation）。理想情况下，这种 joint representation 概括了这些不同数据模态彼此交互的方式。我们看到了一个连续谱：首先，你可以采用适合某个模态的非常好的编码器（encoders），例如把图像送入视觉编码器（vision encoder），把文本送入文本编码器（text encoder），来得到特征，对吧？这些特征概括了一些语义内容，所以已经相当同质了。那么 fusion 需要承担的工作就更少，可以更加轻量。我们学习不相交的表示（disjoint representation）\[字幕疑误，可能指 joint representation\]，我们称之为抽象模态融合（fusion with abstract modalities）。与此同时，另一种范式是直接对原始模态进行融合（fusion with raw modalities）：不再为每个模态定义编码器，而是从模态的原始数据开始，这些数据更具异质性，表示学习（representation learning）和模态间的 fusion 一起完成。因此，这时 fusion 承担了更多工作。呃，这些也可以

### [02:50](https://www.youtube.com/watch?v=u-H43tRgYJg&t=170s) · b000004

称为比较偏后期融合（late fusion）的方式，也就是先提取特征，再在模型较后的位置做 fusion；或者称为早期融合（early fusion），也就是 fusion 发生在模型较早、离数据更近的位置，fusion 如何运作也有更多空间。呃，两者各有一些优缺点。late fusion 通常意味着 fusion 更轻量，也可能更具可解释性，呃，但表达能力没那么强。early fusion 让 fusion 有机会具备更强的表达能力，但通常 fusion 更大、更复杂，也更难理解。再快速回顾一下，我们还看到了融合不同表示的几个基本概念。呃，我们看了基本概念，先只关注单变量（univariate）的情况，我们看了线性融合（linear fusion）。linear fusion 通常包含一个常数、某个误差项，以及加性项，也就是模态一的加权函数，加上模态

### [03:47](https://www.youtube.com/watch?v=u-H43tRgYJg&t=227s) · b000005

2 的加权函数。这是一种简单的 fusion 方式，同时仍然很强大，因为不同模态会被赋予不同权重。乘法融合（multiplicative fusion）进一步推广了这一点，现在开始考虑 A 和 B 之间的乘性交互，对吧？我们看了一个例子，可以把它看作 B 的权重是 W3 \* X A。因此，模态 B 在 fusion 中占有的权重实际上取决于 X A；反过来，X A 的权重是 W3 \* X of B。A 的权重取决于 B。因此，在 multiplicative fusion 中就得到了这些非线性关系。通常，一个不错的指导原则是既保留低阶项，也就是加性函数，呃，也保留乘法项。这些就是模态之间的高阶交互（higher order interactions）。我们看了扩展到更高维的情况，呃，这样可以变得更有

### [04:43](https://www.youtube.com/watch?v=u-H43tRgYJg&t=283s) · b000006

表达能力，但也更复杂。你们看到了这个技巧：在模态向量末尾添加一个 1，然后做外积（outer product），基本上就是向量转置乘以一个向量。所以 5x 1 \* 1x 5 得到这个 5x5 矩阵，其中 4x4 是成对的，呃，biodal \[字幕疑误，可能指 bimodal，双模态\] 交互。有两个 4x1，分别是两个单模态（unimodal）交互，还有一个 1x1，是偏置（bias）。对吧？所以，把这个 1 作为常数加入向量，然后做 outer product，是一种同时获取数据中高阶和低阶交互的技巧。而在三个模态的情况下，我们可以构建这个，呃，相当漂亮的张量（tensor），其中有一个由 4x4x4 的 trrimodal \[字幕疑误，可能指 trimodal，三模态\] 交互组成的立方体，还有各个面，它们是 4x4 的成对

### [05:38](https://www.youtube.com/watch?v=u-H43tRgYJg&t=338s) · b000007

biodal \[字幕疑误，可能指 bimodal，双模态\]，分别位于 AB、AC 和 BC 之间。有三个 unit modal \[字幕疑误，可能指 unimodal，单模态\] 向量，还有那个，呃，藏在后面的 1 向量。对吧？这很好，但有时它也会变得很大、计算代价很高。所以，这些是五维向量，这就变成了 5x 5x 51 125 \[字幕疑误，可能指 5x5x5，125\]，对吧？所以这个 tensor 本身可能很大，而且在数据之间做的乘性交互越多，显然维度就越……呃，得到的因子的维度就越高。这就是我们看到的低秩融合（low rank fusion）这一思路的由来。其想法是，你希望进行这些乘性交互并形成这些高阶 tensor，但不必保留全部维度。可以做低秩近似（low rank approximations）。呃，因此你可以近似表示

### [06:33](https://www.youtube.com/watch?v=u-H43tRgYJg&t=393s) · b000008

这些高阶交互，同时仍然保持相当高的效率。我们看了这个动画：假设有两个模态，加入那个 1 后做 outer product，得到你的 Z 表示。不仅 Z 很大，另一个大的瓶颈是 Z 上方的权重矩阵 W，它把 Z 映射到下一个维度 H，对吧？所以，如果 Z 是 5x5，就是 25。如果这个 H 是三，那么 W 就是 5x5x3，对吧？所以更大。我们看了如何使用 low rank approximations：不学习整个 W，而是把 W 看成这些小向量彼此进行 out of product \[字幕疑误，可能指 outer product，外积\] 后的求和。所以，其中每一个都是 5x3 与 5x3 做 outer product，得到 5x5x3，对吧？

### [07:29](https://www.youtube.com/watch?v=u-H43tRgYJg&t=449s) · b000009

你把多少个这样的小向量加起来，基本上就是那个 tensor 的秩（rank）。对吧？两个意味着你只考虑这些 tensor，或者说秩为二。三个意味着你只考虑秩为三的 tensor。呃，基本上在机器学习的大多数情况下，尽管矩阵的维度非常高，但在实践中优化这些矩阵和参数时，最终得到的解往往秩很低。因此，这是一种降低维度、提升效率，同时仍然保持相当不错精度的简单方法。这就是 low rank fusion 能带来的：基本上可以用这些低秩因子乘以数据。你们可以阅读这些论文，里面说明，呃，这种计算是等价的。因此，你获得了这些高阶交互的所有好处，同时只用这些

### [08:23](https://www.youtube.com/watch?v=u-H43tRgYJg&t=503s) · b000010

呃，低秩因子来近似它们。好。你们会在作业中做一些练习。嗯，这可以在 PyTorch 中以可微（differentiable）的方式实现。你可以优化这个 rank。对吧？这个 rank 达到矩阵的完整维度时，就恢复了所有可能的权重矩阵，但在实践中，通常低秩就足够了。大家对这些高阶交互的 fusion，以及这些 low rank approximations，有什么问题吗？

### [09:04](https://www.youtube.com/watch?v=u-H43tRgYJg&t=544s) · b000011

好。然后我们看到，嗯，到目前为止，这些方法中学到的每个权重，也就是决定一个模态对 fusion 贡献多少的权重，都是静态的（static）。这意味着，始终把同一个权重 w1 应用于 x，再把同一个权重 w2 应用于 xb，对吧？所以接下来我们看到，把这些权重扩展得更加动态（dynamic），我们称之为 ga fusion \[字幕疑误，可能指 gated fusion，门控融合\]。也许 XA 的权重本身应该取决于 XA 是什么，而 XB 的权重本身应该取决于 W XB 是什么，对吧？它也可以取决于另一个模态。因此，这给出了一种在加性设定下进行 fusion 的形式。输出 Z 仍然是某个权重函数乘以 X A，只不过它

### [09:59](https://www.youtube.com/watch?v=u-H43tRgYJg&t=599s) · b000012

不再是对所有 XA 都相同的静态权重 W1，而是一个取决于当前 X A 和 XB 的函数。对吧？因此可以学习这个函数，根据 X A 和 XB 是什么，其输出可能不同。呃，同样，XB 的权重也可以取决于另一个学到的函数 G of B，这个函数取决于当前 A 和 B 是什么。所以这里的直觉是，视具体情况而定，有时 A 更重要，有时 B 更重要。我们不应该给它们各自分配全局权重，而是希望权重取决于这些，呃，GA 和 GB 模型评出的当前重要性。因此，这些 A 和 G 和 GB 可以看作注意力函数（attention functions），而门控（gating）不再是单一权重，现在会随着输入模型的每一个数据点而变化。

### [10:56](https://www.youtube.com/watch?v=u-H43tRgYJg&t=656s) · b000013

顺便说一下，有人问了个问题。嗯，所有这些幻灯片都在 Canvas 上，呃，基本上课前就会上传。所以这些在 Canvas 上。另外简单说明一下网站。网站是面向公众的，呃，所以不会那么零散地更新，而且我必须先编辑所有视频，才能公开发布。因此，所有幻灯片、录像、教学大纲和作业都在 canvas 上。那会是我们的主要媒介，呃，所有内容都集中在那里。

### [11:29](https://www.youtube.com/watch?v=u-H43tRgYJg&t=689s) · b000014

很好。大家对动态融合（dynamic fusion）有什么问题吗？请说。学习这些时，这个，呃，建立像 GB 这样的东西，会涉及领域知识（domain knowledge）吗？比如前几天做报告的那个人，讲了，呃，海洋动力学之类的内容。这是否需要事先对那个函数的作用有些了解，还是基本上就像 attention 那样决定，不需要，嗯，像 adop knowledge \[字幕疑误，含义不明\]？&gt;&gt; 是的，我想两者都可以。两者都可以，嗯，完全由数据驱动。所以，正如你已经指出的，这可以涵盖我们今天看到的一些 attention functions。它也可以依赖，嗯，一些 domain knowledge。呃，周二，我这里只是在回顾，但周二我们还进一步举过例子，GA 和 GB 不必是对称的，对吧？你可以有一个主要模态 A。如今，语言非常

### [12:25](https://www.youtube.com/watch?v=u-H43tRgYJg&t=745s) · b000015

占主导。我们有非常好的语言模型（language models）和语言表示（language representations）。所以我不会过多修改语言，而只针对音频和视频模态修改并学习 GA 和 GB，对吧？这就是某种 domain knowledge，基于语言在交流中非常占主导这一事实，我只想为非语言的音频和视频学习这些门控。是的，所以它不必对称，也不必完全由数据驱动。这里绝对有融入一些 domain knowledge 的空间。

### [12:58](https://www.youtube.com/watch?v=u-H43tRgYJg&t=778s) · b000016

好，这些都是，嗯，关于我们如何注入、如何仔细设计这些 fusion 方法的例子。当然，嗯，我们也看到了另一个极端，也就是 early fusion。很早就把数据或特征混杂起来，让 fusion 和预测模型承担大部分工作，并尝试设计一些你希望能捕获这种 fusion 的模型。呃，这也是一种非常直接、容易实现的方法，你们做任何应用时大概都应该尝试一下。呃，所以在数据层面或特征层面做拼接（concatenate），然后设计……基本上从此把它们当作一个单一模态，设计能融合并预测它们的最佳模型。当然，接下来一个大问题就是：这个模型到底学到了什么，对吧？我们希望模型能学到一些有意思的东西，以及一些

### [13:56](https://www.youtube.com/watch?v=u-H43tRgYJg&t=836s) · b000017

关于模态如何交互的非线性内容。呃，但我们如何衡量模型是否真的成功做到了这一点？所以，我想重点介绍一篇我非常喜欢的论文，它属于这样一类工作：不仅开发新方法，而是真正尝试探查和理解现有方法的表现。这篇论文讲的是，如何衡量模型学到了哪些非加性交互（non-additive interactions）。它假设你有某个函数 f，也就是已经在 a 和 b 上学到的 fusion 函数，函数 f 用来预测标签，对吧？要分析这个模型学到了多少非加性的复杂交互，目标就是把这个模型投影到最简单、最接近的加性函数（additive function）上。

### [15:02](https://www.youtube.com/watch?v=u-H43tRgYJg&t=902s) · b000018

那边在开舞会。所以，如何投影这个任意函数 f？它可以是你学到的任何东西：neuronet networks \[字幕疑误，可能指 neural networks，神经网络\]、transformers、巨大的基础模型（foundation models）。我们如何找到这个函数最接近的近似，而且只是一个加性组合，即作用于 x a 的 f of a，加上作用于 xb 的 f of b？对吧？如果我能找到这个最近的加性函数，并测量与该函数的差异，就能概括我的函数有多少只是纯加性的，也就是这个 f of a 加 f of b，又有多少是非加性的，真正学习了模态之间的这些复杂 tensor 或 dynamic fusions。结果是，在统计学中，实际上有一种非常简单的方法来寻找这个最近的加性函数，它看起来就是这样。最近的加性函数当然是两项之和，因为它是

### [15:58](https://www.youtube.com/watch?v=u-H43tRgYJg&t=958s) · b000019

加性的。第一项是，取 fusion f of x a plus xb，呃，抱歉，是 f of xa and xb，然后对 xb 取期望（expectation）。expectation 基本上就是把数据集中所有可能的 xb 输入这个模型，再对所有 xb 的结果取平均，对吧？根据定义，对 xb 取 expectation 会把 xb B 边缘化掉（marginalize），这样就得到一个关于 f of a 和 x of a 的函数。呃，同样，对于另一项，我会对 fusion 关于所有 x of a 取 expectation，对吧？输入所有可能的 x a，看看输出是什么，然后对所有 xa 的结果取平均。再说一次，根据定义，这会从函数中边缘化掉 x a，从而得到只关于模态 b 的函数 f of b。对吧？所以实际上可以证明，这是最近的，呃，加性函数

### [16:54](https://www.youtube.com/watch?v=u-H43tRgYJg&t=1014s) · b000020

它适用于你所……的任何输入函数 f。直观上，它看起来像这样，对吧？它可以接收各种复杂函数，比如 neuron nets \[字幕疑误，可能指 neural networks，神经网络\]、预训练模型（pre-trained models），比如多模态 vert \[字幕疑误，可能指 BERT\] 预训练模型或语言模型，甚至也可以接收 svms 和其他核函数（kernel functions），本质上把它们投影到纯加性函数 f of a 加 f of b 所构成的函数空间。所以他们把这个叫作 emap，或者 empirically multimodal additive projection \[字幕疑误，可能指 empirical multimodal additive projection，经验多模态加性投影\]。请说。

### [17:29](https://www.youtube.com/watch?v=u-H43tRgYJg&t=1049s) · b000021

&gt;&gt; 你计算什么……？&gt;&gt; 嗯，这取决于距离函数（distance function），但你可以把它理解为最近，也就是函数 f 产生的 yhat 与这个加性函数空间产生的 yhat 之间的平方距离。&gt;&gt; 所以这个论断是说，对所有距离函数，这个映射都会给出……&gt;&gt; 是的，我的意思是，我没有……我不知道是不是适用于所有距离函数，但论文包含了一些证明，对吧，针对某些距离函数。

### [18:00](https://www.youtube.com/watch?v=u-H43tRgYJg&t=1080s) · b000022

所以这意味着，在实践中，我们可以拿一个你学到的、很花哨或者声称很好的 fusion 函数，对它进行 EMAP 投影，得到 f of a 加 f of b，其中每一项都是对另一个模态取 expectation。当然会有一些差异，会有某个差异 mu，也就是这种加性投影没有捕获到的预测差异。另一个问题是，这些模型有多少能被加性函数捕获，又有多少不能？也就是有多少是新的？于是他们拿了一批模型，呃，其中一些非常复杂，结果发现，令人惊讶的是，只用加性近似就能捕获相当多的内容。衡量方法是原始 fusion 模型与加性投影之间的性能差异，这里的这一行叫作 EMAP。所以

### [18:56](https://www.youtube.com/watch?v=u-H43tRgYJg&t=1136s) · b000023

有时你会看到 91.3 降到 91.1。有时会看到 74.4 降到 74.2。还有，呃，53.4 降到 51.0。因此，开始做这种加性近似时，确实会看到一些性能下降。但令人惊讶的是，有时下降并不大。对吧？所以这是，嗯，一个残酷的事实，对吧？有时你尝试设计真的很 complexion \[字幕疑误，可能指 complex，复杂的东西\]。你觉得自己成功了，觉得有了一个漂亮的 fusion 算法。不过，最好始终检查一下，它有多少只是在学习数据中良好的加性模型，又有多少真正超越了加性，学到了这些复杂交互。对吧？我的意思是，它没能成功学到这些复杂交互，有两个原因。一种可能是，数据中本来就不存在这些复杂交互

### [19:52](https://www.youtube.com/watch?v=u-H43tRgYJg&t=1192s) · b000024

而在你的数据集上预测标签，基本上用 adequate combinations \[字幕疑误，可能指 additive combinations，加性组合\] 就能解决。这是一种假设：数据本身不够复杂。第二种假设是，数据足够复杂，但你设计或训练模型的方式，使得模型没能成功捕获那些复杂交互。呃，从性能数字中也能得到一些直觉，对吧？在这个例子里，我想，嗯，我不知道为什么这个 INT 数据集，我不记得它是什么了，但这里性能已经是 91.3，降到了 91.1，这意味着这个数据集可能没有复杂交互，因此多模态模型和加性模型都已经非常好，超过 90%。另一个数据集，比如 TV vis，嗯，最好的加性模型是 51，最好的多模态模型是 53.4，更可能

### [20:48](https://www.youtube.com/watch?v=u-H43tRgYJg&t=1248s) · b000025

意味着这个数据集包含复杂交互，但，呃，这些人没能成功训练出捕获这些交互的模型，否则性能应该达到 80、90%，而不是 53%。

### [21:07](https://www.youtube.com/watch?v=u-H43tRgYJg&t=1267s) · b000026

好。因此，这类，嗯，这类合理性检查（sanity checks）、诊断工具（diagnostic tools）总是很有用，呃，因为我们不仅想训练模型，还想真正理解这些模型在学习什么。大家对此有什么问题吗？

### [21:30](https://www.youtube.com/watch?v=u-H43tRgYJg&t=1290s) · b000027

请说。

### [21:36](https://www.youtube.com/watch?v=u-H43tRgYJg&t=1296s) · b000028

嗯，加性融合（additive fusions）本身也可以很强大，对吧？它们提供了这种 late fusion 方法：把 A 输入一个分类器（classifier），把 B 输入一个 classifier，然后相加。如果效果很好，比如这些例子里性能达到 91%，那么是的，我们当然应该使用它们。它们高效、可解释。嗯，当然，在某些场景中它们效果不好。所以这是一方面，对吧？有时它们不好用。但我认为这里更大、更重要的一点是，我们不应该只设计表面上看起来复杂、效果不错的模型，却不真正理解它们内部到底在学什么。因此，我喜欢这类挑战假设、回过头精确量化模型究竟学到了什么的工作。在这个例子中，它挑战了你需要所有这些复杂交互的假设，因为实际上，这些交互在实践中似乎并不很突出。请说。

### [22:30](https://www.youtube.com/watch?v=u-H43tRgYJg&t=1350s) · b000029

&gt;&gt; 这是否意味着我们应该先从这个开始，或者先从 additive fusion 开始，然后再……&gt;&gt; 是的，它始终是一个很好的基线（baseline）。early fusion、late fusion、additive fusion，或者只是拼接，始终都是很好的 baseline。这也是我们督促大家在作业中也做这些的原因。同样，期中项目中大家必须运行，你们所有人都必须运行强 baseline，然后再开始，呃，增加复杂度。

### [23:01](https://www.youtube.com/watch?v=u-H43tRgYJg&t=1381s) · b000030

请说。

### [23:15](https://www.youtube.com/watch?v=u-H43tRgYJg&t=1395s) · b000031

&gt;&gt; 这些是准确率（accuracies）。这些是 accuracies。嗯，要点在于，理想情况下，他们应该在所有这些实验中报告置信区间（confidence intervals），并做交叉验证（cross validation），但要点是，有时一个正规的复杂模型与一个只做线性组合的模型之间，差异并没有那么大。嗯，当然，有时候这 2% 可能会产生影响。呃，但这取决于你，也取决于具体领域。

### [23:54](https://www.youtube.com/watch?v=u-H43tRgYJg&t=1434s) · b000032

因此，由此延伸出的一种方法，是为了真正迫使模型，嗯，开始学习这些交互，不是同时完成所有 fusion，而是分阶段进行 fusion，对吧？fusion 也可以按阶段进行。呃，看看这是什么意思。你可以采用的一种方法，在这项工作的后续研究中也有，就是你有两个或三个模态，首先推动模型尽可能学习单模态信息。对吧？基本上就是训练 unimodal classifiers，分别用 XA 预测标签，用 XB 预测标签，用 XC 预测标签，然后把它们加起来。对吧？这样就得到最好的单模态模型，而把它们加起来时，就得到最好的加性模型

### [24:51](https://www.youtube.com/watch?v=u-H43tRgYJg&t=1491s) · b000033

对吧？先训练这个，这是第一阶段。训练完后，再训练第二阶段，开始考虑 B 和 C 的组合，B，呃，A 和 C、B 和 C、A 和 B 的组合，并开始添加这些 biodal \[字幕疑误，可能指 bimodal，双模态\]。然后开始把三者全都组合起来，学习这个三角形。这三个阶段的学习方式是，先取标签 Y，测量目标标签与最好的加性函数学到的结果之间的差异，对吧？所以尽量推动加性函数逼近标签。然后计算差异，也就是加性模型没有捕获到的差异。把它称为残差（residual），用这个 residual，并尝试用 biodal ver \[字幕疑误，可能指 bimodal 部分\] 来学习它。对吧？所以 residual 是 y 减 y unimodal。再计算这个 residual 与 y

### [25:47](https://www.youtube.com/watch?v=u-H43tRgYJg&t=1547s) · b000034

biodal \[字幕疑误，可能指 bimodal，双模态\] 之间的差异，也就是使用成对模态预测的输出。然后你看到又有一些误差。呃，再把它作为 residual，也就是 y 减 unimodal 减 biodal。然后使用三个模态的项来拟合这个 residual。所以，也可以把 fusion 分阶段处理。呃，这非常好，因为现在你保证每个阶段都会越来越好，因为你只用下一个模态去拟合 residual。因此，要么变得更好，residual 减小；要么什么都没学到，误差保持不变。所以保证只会变好，不会变差。这很好。而且，你可以在任何想停的地方停下。对吧？如果你觉得一开始 residual 是 10，太大了，那我就用 biodal 去拟合。如果我拟合 bodal \[字幕疑误，可能指 bimodal\] 后，residual 变成二，呃，这就够好了，那么就不必再做这一步。所以你基本上可以做这种

### [26:44](https://www.youtube.com/watch?v=u-H43tRgYJg&t=1604s) · b000035

分阶段融合（stage wise fusion），自行决定在哪里停下，并在所使用的内容和误差之间找到合适的平衡。

### [26:57](https://www.youtube.com/watch?v=u-H43tRgYJg&t=1617s) · b000036

好。这就是 stage wise fusion。呃，这是处理数据非常复杂的问题的一种好方法。你希望分阶段做 fusion，希望决定何时停止，也不希望 fusion 让事情变得更糟，因为有时 fusion 确实会让事情变糟。有时，呃，三模态 fusion 会占用大量参数，而这些参数很难优化。有时会看到，增加更多模态也会让效果变差。

### [27:31](https://www.youtube.com/watch?v=u-H43tRgYJg&t=1651s) · b000037

好，总结一下，呃，既回顾了周二的内容，也补充了一点周二没来得及讲的内容。multimodal fusion 的目的是学习一个 joint representation，用来建模两个不同模态如何交互，对吧？目标其实是尽量建模数据中所有必要的交互，不多也不少，同时仍然保持合理的紧凑性、效率，以及对下游用户而言的可理解性。我们看了两个连续谱。一端是先从模态中提取特征，对吧？使用良好的 unimodal encoders，以及语义上更有意义、本质上更可能同质的特征。而在另一个极端，也有一种范式：你有原始数据，在数据更异质时更早地做 fusion。不过这样也有好处，因为现在 fusion 和 representation learning 可以

### [28:27](https://www.youtube.com/watch?v=u-H43tRgYJg&t=1707s) · b000038

一起端到端（end to end）学习。我们看了这个连续谱上的不同方法，一个极端是 late fusion：已经在预测标签，然后以某种方式组合这些标签。我们看了 additive fusion，嗯，超越加性的一阶交互后，看了 multiplicative，三个模态时是 tensor，还可以进一步扩展到模态之间更高阶的 polomials \[字幕疑误，可能指 polynomials，多项式\]。呃，其中一些计算可能非常昂贵。所以我们看了它们的 low rank approximations。所有这些仍然对各个模态使用相同的权重，对吧？对 X A 使用同一个 W1，对 XB 使用同一个 W2。然后我们看了权重根据当前 A 和 B 动态变化的设定。这些就是门控融合（gated fusion）、动态融合（dynamic fusion）以及模态转移融合（modality shifting fusion）。

### [29:24](https://www.youtube.com/watch?v=u-H43tRgYJg&t=1764s) · b000039

之后，本学期后面还会看一些更偏 early fusion 的方法，届时我们会讨论如何使用 transformers 和多模态 transformers 来更早地进行 fusion。对吧？关于 fusion，还有最后的问题吗？请说。

### [29:54](https://www.youtube.com/watch?v=u-H43tRgYJg&t=1794s) · b000040

所以，比如这里的问题是分类，类别可能像猫……&gt;&gt; 可以用交叉熵（cross entropy），cross entropy 误差的差异。嗯，很好，你可以用任何均方误差（mean square error）、cross entropy 误差，以及你使用的任何其他损失函数（loss function），都可以用来做。请说。很好。请说。&gt;&gt; 关于这张幻灯片的问题。是的，不是，是你现在这张。&gt;&gt; 好。&gt;&gt; 嗯，你简要谈到了这些不同方法的计算量。嗯，我们是否很好地理解，当逐渐走向更

### [30:50](https://www.youtube.com/watch?v=u-H43tRgYJg&t=1850s) · b000041

异质的模态时，这些方法之间计算量的数量级差异？&gt;&gt; 呃，我们是否有很好的理解？如果你指的是是否有很好的理论理解和保证，答案是没有，因为在深度学习（deep learning）或者任何涉及 neuronets \[字幕疑误，可能指 neural networks，神经网络\]\[吸鼻声\] 和非凸优化（non-convex optimization）的领域中，这些都很难获得。我们是否有不错的直觉？嗯，我想这来自实践，对吧？来自……我的意思是，这就是这门课的目的，你们会在作业二中尝试很多不同的 fusion 方法，如果项目侧重 fusion，也可能在项目中尝试。嗯，然后你就会开始看到，比如把计算量画出来，对吧？大致来说，很多方法从这里到这里时，会需要越来越多的计算量，呃，因为 fusion 的参数更多。然后你可以自己观察性能是变好还是变差，对吧？所以性能不一定总是变好，但有时这些

### [31:45](https://www.youtube.com/watch?v=u-H43tRgYJg&t=1905s) · b000042

根本不起作用，你就必须开始用大型模型做 early fusion，对吧？嗯，我的意思是，有一些一般性的指导原则：简单 baseline 总是很有帮助，简单的 early fusion、late fusion baseline，嗯，基于 pre-trained models 的简单 baseline 总是很有帮助。然后还有具体任务的要求，比如需要多少计算量，或者你愿意在多大程度上使用黑箱（black box），就是某种真正告诉你这一阶段发生了哪些 fusion、这里有哪些交互的东西。所以也有很多需要考虑的因素。

### [32:29](https://www.youtube.com/watch?v=u-H43tRgYJg&t=1949s) · b000043

我们正在尝试建立，嗯，我的意思是，我们所做的一些工作中，一个关键愿景就是建立对这些问题更形式化的理解。所以你们可以搜索我们的一些论文。嗯，我们基本上能够说明的是，如果你有一些数据，对吧，X1、X2 和 Y，有一些样本，就可以先量化数据中的一些统计量。这些统计量可能会告诉你，在某些元素上，模态之间有这么多协同信息（synergy），对吧？我们正在朝着建立这样一个框架的方向前进，而且已经有一些早期证据表明它存在。然后根据这些知识，例如有这么多 bit 的 synergy 需要融合，就可以大致给出哪一种 fusion 方法最有用的建议，对吧？所以有时你会发现，呃，量化之后，大部分

### [33:25](https://www.youtube.com/watch?v=u-H43tRgYJg&t=2005s) · b000044

信息是 X1 独有的，这种情况下就不需要所有这些花哨方法，对吧？只使用 X1 这个单模态即可。有时你量化后发现 A 和 B 之间，呃，一和二之间有很多 synergy，那么可能就必须使用更复杂的 fusion 方法。这不是一个完美的映射，但，呃，可以帮助你形成一些直觉，而这方面还需要更多工作。所以，如果你想在这个方向做项目，也非常鼓励。也就是更加严谨、更加、更加基础性的原则。

### [34:01](https://www.youtube.com/watch?v=u-H43tRgYJg&t=2041s) · b000045

好。关于 fusion，还有最后的问题吗？好。很好。现在进入今天这节课原本计划的内容，也就是讨论 alignment。呃，fusion 和 alignment 可能是多模态中两个最大的核心概念，对吧？我们会介绍多模态对齐（multimodal alignment）的基础。我们会介绍对比学习（contrastive learning），作为在离散设定中显式强制 alignment 的一种常见方法。我们会稍微介绍连续对齐（continuous alignment），然后介绍一个很新的主题，也就是所谓的隐式对齐（implicit alignment），对吧？alignment 会在训练模型时涌现，而不需要通过 contrastive learning 这样的目标函数显式强制实现。那么，什么是 alignment？alignment 的目标是识别并建模不同

### [34:57](https://www.youtube.com/watch?v=u-H43tRgYJg&t=2097s) · b000046

模态中的不同元素彼此连接的各种方式。我们会给出“连接”更形式化的定义，但直观上可以把它理解为重叠信息，或者表示某种底层的相似概念。alignment 有三个子挑战。第一种情况最简单，你可以把模态分割成离散元素（discrete elements）。对吧？比如一个人说的话语、图像中被指代的物体，呃，以及一个人在某种过程中做出的面部表情。所以，一旦能显式地把模态分成元素，就可以把 alignment 基本上视为一个匹配问题（matching problem）。例如，描述中的哪个词指代图像中的这把椅子，另一个词又指代图像的另一个部分。很多时候，alignment 就是两个

### [35:54](https://www.youtube.com/watch?v=u-H43tRgYJg&t=2154s) · b000047

模态之间语义相似元素的 matching problem。因此，离散对齐（discrete alignment），或者学习这些离散连接，是最简单的情况。当元素更加连续、分辨率更高且连续时，这个问题就更具挑战性，因为粒度（granularity）并不明确。对吧？例如，把视频与文本对齐，或者把传感器数据与文本对齐，就更困难，因为视频和传感器数据中的语义边界并不十分明确。它不像“这是我在句子里说的一个词”那样清楚。所以今天我们会介绍这两种情况。呃，我还想把整个脉络补充完整，指出在这两种设定中，alignment 是最终目标，目的是找出哪个词指代图像的哪一部分，或者哪个词指代视频的哪一部分。alignment 是最终目标。还有第三个子挑战，alignment 被用作

### [36:51](https://www.youtube.com/watch?v=u-H43tRgYJg&t=2211s) · b000048

中间步骤，以学习更好的下游表示，我们称之为上下文化表示（contextualized representations）或 line representations \[字幕疑误，可能指 aligned representations，对齐表示\]。这里我画的这些 alignment 大多是灰色的。如何使用 alignment 来学习更好的表示？例如，大家都见过今天的语言模型，我们有这些词，并且知道它们如何与上下文中的其他词对齐、如何在上下文中得到表示。这对学习更强大的句子表示至关重要，对吧？在多模态大语言模型（multimodal LLMs）中，所有这些词和问题都会结合前面的词，也会根据 alignment 的情况结合图像的部分内容进行上下文化。正是这种 alignment 和上下文化，让你能训练出更好的 multimodal LLMs。所以，这里 alignment 被隐式地用作中间步骤，以学习更好的表示。接下来两周会更详细地介绍这些内容，届时会讲这些

### [37:46](https://www.youtube.com/watch?v=u-H43tRgYJg&t=2266s) · b000049

multimodal transformers 和 foundation models。今天我们只讨论，嗯，把 alignment 作为目标，学习模态之间离散和连续 alignment 的情况。大家对这个路线图有什么问题吗？

### [38:08](https://www.youtube.com/watch?v=u-H43tRgYJg&t=2288s) · b000050

好。从 discrete alignment 开始。这里的目标是识别并建模模态之间离散元素的连接，对吧？可以把这些连接理解为它们之间共享的一定量信息，具有相似的语义含义。我还是用这些，呃，这些三角形和圆形 A 和 B。你应该把这些连接理解为捕获共享的东西，同时基本上忽略独有的东西，对吧？一旦开始做 alignment，任何独有的信息基本上都会被丢弃。请说。&gt;&gt; 嗯，能否为每个挑战提供一些实际例子？比如，我想在这个例子里，模态 a 可以是 laby pictures \[字幕疑误，含义不明\]。所以，嗯，模态，比如每一个独有的特征，可以是一张 CT 图像。

### [39:05](https://www.youtube.com/watch?v=u-H43tRgYJg&t=2345s) · b000051

&gt;&gt; 下一张幻灯片就会讲到。嗯，一个例子，我的意思是，比较简单的例子就是视觉和文本，呃，图像和文本。这是一张图像，描述可以是“一个女人在读报纸”，对吧？图像被分割成不同物体的边界框（bounding boxes），女人、报纸；描述被分割成词元（tokens）。嗯，woman 这个文本对应图像的那一部分，newspaper 这个文本对应图像的那一部分。呃，有意思的是，reading 这个词与 MHV \[字幕疑误，可能指 image，图像\] 之间是什么 alignment？有人知道吗？请说。&gt;&gt; 可能是眼睛、手，或者二者的组合？&gt;&gt; 也许？还有其他人吗？reading 这个词会映射到什么？请说。&gt;&gt; 比如头向下倾斜。&gt;&gt; 也许。但即使头向下倾斜、有眼睛，如果看不到报纸是什么，

### [40:02](https://www.youtube.com/watch?v=u-H43tRgYJg&t=2402s) · b000052

也就是目标，你也不知道这个人是在阅读，还是只是在盯着某样东西，或者快睡着了，对吧？&gt;&gt; 什么像素的颜色？&gt;&gt; 哦，报纸。所以如果 red \[字幕疑误，可能指所读的对象\] 是手机，可能会比较暗。如果是报纸，可能更亮。&gt;&gt; 嗯哼。&gt;&gt; 有意思。嗯，简单说，它是有歧义的。呃，这不是一对一映射（one-to-one mapping）。reading 大概应该对齐到某个函数，它当然涉及女人的脸和视线方向，同时也涉及报纸，也许还有颜色。报纸必须在那里，才能知道有一个被阅读的目标。所以 alignment 往往不只是一对一。在女人、报纸的例子中是一对一；有时是一对多，一个词映射到许多东西，也可能是不同东西之间的关系。在这个例子中，就是

### [40:57](https://www.youtube.com/watch?v=u-H43tRgYJg&t=2457s) · b000053

与报纸之间的关系，对吧？不过，这就是我本来打算给的一个例子。这里我还想强调几个直觉：为什么这些 alignment、这些连接存在，以及我们如何发现它们。一个是从更偏统计学的角度，通过关联（association）来理解。如果我总是在这些描述中看到 newspaper 这个词，同时在不同的、存在报纸的图像中看到各种报纸，那么有了足够多的数据，就能识别这种 association：所有描述中共同的词 newspaper，映射到所有这些图像中共同的物体，也就是报纸的照片。呃，这就是从相关性（correlation）和共现（co-occurrence）的角度，理解如何发现 alignment。呃，同时这也赋予了某种语义含义，也就是说，这个 newspaper，newspaper 这个词实际上

### [41:53](https://www.youtube.com/watch?v=u-H43tRgYJg&t=2513s) · b000054

有某种意义，而报纸的图像实际上也有某种意义。因此，这识别出了两者之间含义相同的对应关系，只不过一个用文本表达，一个用图像表达。呃，除了这些单独的 co-occurrences，比如我们看到的女人和报纸的一对一映射，还有其他成对或高阶交互，也就是一个模态与另一个模态之间的高阶连接。所以我们看到了 reading 的例子，对吧？文本中的 reading 这个概念，实际上映射到这样的依赖关系：有眼睛，还有指向报纸的定向映射。对吧？同样，从语义角度看，眼睛与报纸之间存在某种关系，表明眼睛的功能，也就是阅读。所以，这些连接存在于不同的层次

### [42:48](https://www.youtube.com/watch?v=u-H43tRgYJg&t=2568s) · b000055

一对一关联最简单、最明确，但与此同时，还有一些高阶的、成对的功能关系，需要在 alignment 过程中捕获。好，但究竟如何捕获呢？呃，一种通用方法是使用所谓的配对数据（paired data），对吧？如果你有大量 paired data，在这里就是图像与文本之间的 paired data。配对基本上意味着，这张图像对应这段描述，图像二对应另一段描述。然后我就可以开始学习这些表示，其中 A 和 B 分别由 F of A 和 F of B 编码。这会把它们编码为表示 Z A 和 ZB。目标是定义一个相似度函数（similarity function）G

### [43:43](https://www.youtube.com/watch?v=u-H43tRgYJg&t=2623s) · b000056

来捕获 ZA 和 ZB 彼此连接，而其他 ZA 和 ZB 可能没有连接这一事实。所以，这就是捕获 alignment 的通用方式，对吧？输入 A 和 B，各自对应一个编码器 F of A、F of B，得到特征 Z of A、Z of B，再由某个 similarity function G 评估它们是否对齐，或者对齐程度有多高。好。呃，你会发现，这与 fusion 不同，对吧？在 fusion 中，你有 A 和 B，把它们合成一个 joint representation Z。而在 alignment 中，你有 A 和 B，学习两个独立的表示 Z of A 和 Z of B，再计算它们之间的某种 alignment 或 similarity function。请说。&gt;&gt; attention 是否会利用这些统计上的 co-occurrences，

### [44:39](https://www.youtube.com/watch?v=u-H43tRgYJg&t=2679s) · b000057

比如 reading 与数据之间的共现？&gt;&gt; 呃，是的，是的，alignment 会捕获其中一些内容。所以，下周讨论这个话题时，我们会讲如何用 attention 学习这种 alignment，以及如何利用它进一步学习这些下游表示。是的。不过，是的，attention 是学习它的一种方式。好。关于这个范式，以及它和 fusion 的区别，有什么问题吗？现在我们不是在学习一个融合我们的 joint representation，而是在学习并保留独立的表示 Z of A、Z and B，再通过这个 similarity function 让它们保持一致。

### [45:28](https://www.youtube.com/watch?v=u-H43tRgYJg&t=2728s) · b000058

好。你可以把这些编码器理解为，或者按你想要的方式定义它们。这些编码器旨在捕获异质性（heterogeneity）。它们适配不同的数据模态及其各自的结构。但一旦学到了 Z of A、Z of B，这个，呃，协调函数（coordination function）G 基本上就捕获了它们之间的连接。学习这个 alignment 函数的一种通用方式，是定义一个 loss function。呃，这个 loss function 首先把 f of a，嗯，应用于 madata da \[字幕疑误，可能指模态数据 da\]，然后把 f of b 应用于 madata db \[字幕疑误，可能指模态数据 db\]，得到表示，再用 g 给它们打分，对吧？g 就是衡量它们之间相似度的函数。有哪些可训练参数呢？可训练参数

### [46:23](https://www.youtube.com/watch?v=u-H43tRgYJg&t=2783s) · b000059

是这个 g 函数里的 data \[字幕疑误，可能指 theta\]，因此 similarity function 本身实际上也可以有可训练参数。好，呃，然后当然还有 f of a，也就是 A 的编码器，以及 f of b，也就是 B 的编码器中的可训练参数 data \[字幕疑误，可能指 theta\]。对吧？这些就是可训练参数，你会优化它们，呃，在这里，如果 g 是相似度，就最大化 g；如果 g 是某个 distance function，就最小化它。

### [46:55](https://www.youtube.com/watch?v=u-H43tRgYJg&t=2815s) · b000060

那么 g 有哪些例子？嗯，G 可以是余弦相似度（cosine similarity），对吧？G 接收 Z 和 ZB，可以采用 cosine similarity，基本上是对 A 和 B 做点积（dot product），呃，也许再用它们的模长归一化。对吧？这样就很好理解，范围在负 1 到正一之间，呃，通过模长归一化，捕获一种线性的相似性概念。也就是这两个向量在表示空间（representation space）中是否指向同一方向。还可以扩展到核相似度（kernel similarities）。学过机器学习的同学见过核（kernels）。kernels 是给定这两个向量、对它们之间某种距离进行评分的函数，对吧？这些 kernels 可以是线性的，此时就恢复为这两个向量之间的 dot product，也就是它们是否

### [47:51](https://www.youtube.com/watch?v=u-H43tRgYJg&t=2871s) · b000061

指向同一个方向，但也可以是 polomial \[字幕疑误，可能指 polynomial，多项式\]、指数型（exponential）、RBF。这些其他 kernel functions 的区别仅在于计算相似度所处的空间：你是先把它们变换到某个 polinomial \[字幕疑误，可能指 polynomial，多项式\] 空间再计算相似度，还是保留在原始空间中，在原始空间里计算相似度。呃，把它们变换到不同的 representation spaces 有一些好处，基本上可以理解为在向量的某种非线性函数中学习相似性，而不是在它们最初所在的空间中。因此，任何 kernel function 都可以用来衡量相似度，correlation 也可以。在这种情况下，我可能不只是关心这两个点本身，对吧？这两个点是否接近，或者是否指向同一方向；我关心的是整个分布（distribution），对吧？我关心这个完整的

### [48:48](https://www.youtube.com/watch?v=u-H43tRgYJg&t=2928s) · b000062

第一模态中的点分布，以及第二模态中的分布，还有它们是否彼此相关，对吧？这可以是一种相似性概念。同样，我也可能关心……请说。

### [49:09](https://www.youtube.com/watch?v=u-H43tRgYJg&t=2949s) · b000063

是的，我会给一些例子。不过，呃，在讲 distribution 之前，先说这个。先讲成对（pairwise）的情况。嗯，有时我不关心，比如我是苹果、橙子，以及苹果、橙子，对吧？文本中的苹果、橙子，和视觉中的苹果、橙子。我可能不关心苹果的词嵌入（word embedding）是否接近苹果的图像嵌入（image embedding）。它们在哪里并不重要。我可能关心的是，苹果与橙子的 word embeddings 之间的关系，是否与苹果和橙子的 image embeddings 之间的关系一致。对吧？具体来说，这个变换表示保持形状、改变颜色。对吧？对吧？所以我可能不关心各个点自身的位置，但关心它们的顺序，或者成对关系、距离，比如文本中的苹果、橙子与，嗯，

### [50:04](https://www.youtube.com/watch?v=u-H43tRgYJg&t=3004s) · b000064

图像中的苹果、橙子。呃，如果扩展到三个点的情况，我可能关心，在 word embeddings 中，苹果和橙子彼此接近，但与桌子相距很远；同样，在视觉嵌入（visual embeddings）中，苹果和橙子彼此接近，但与桌子相距很远。对吧？现在你就开始看到，有时候，点之间这些成对和三元关系，比各个点本身的具体位置更重要。明白吗？请说。

### [50:55](https://www.youtube.com/watch?v=u-H43tRgYJg&t=3055s) · b000065

仍然可以训练。嗯，我的意思是，这个范式仍然适用，对吧？把文本输入文本模型，得到 text embeddings。把 B 图像输入图像模型，得到 image embeddings。现在我有一组表示苹果、橙子和桌子的 text embeddings，也有表示苹果、橙子和桌子的 image embeddings。我要做的只是计算这个可微函数，也就是文本中苹果、橙子和桌子之间的 pairwise distances，以及图像中苹果、橙子和桌子之间的 pairwise distances，并尝试以某种一致的方式组织它们，对吧？这就是你的函数 jeep \[字幕疑误，可能指 G\]。嗯，实际上后面有一张幻灯片讲这个。我的意思是，它看起来就是这样，对吧？我可能关心苹果、橙子和大象的 image embeddings 按这种方式组织：苹果和橙子靠近，大象离得远，而且

### [51:52](https://www.youtube.com/watch?v=u-H43tRgYJg&t=3112s) · b000066

text embedding 中也一样，苹果和橙子接近，大象离得远。怎么做到呢？嗯，我不展开细节，但可以分别定义 kernels，对吧？这个函数基本上是说，我要查看所有 image embeddings 两两之间的距离。这个则是说，我要查看所有 word embeddings 两两之间的距离。两者各自以某种 kernel 的形式给出一个概括，而我的相似度就是看这两个 kernels 有多相似，它们基本上就是成对距离的图，对吧？你可以最大化这一点来保证相似性。

### [52:33](https://www.youtube.com/watch?v=u-H43tRgYJg&t=3153s) · b000067

我看到了。请说。&gt;&gt; 真值标签（ground truth label）在某种程度上是隐式的。我觉得那个函数只是在使用两个模态的 embeddings，但我们实际上没有……它难道不也在最后……但是

### [53:07](https://www.youtube.com/watch?v=u-H43tRgYJg&t=3187s) · b000068

呃，我想这里问了两个问题。一个问题是，loss 必须定义，对吧？在这里，loss 必须事先定义。它不会自动学到，有时你关心 pairwise losses，有时关心 correlation，有时关心 cosine similarity。你必须指定 loss 是什么，也就是必须指定 G 是什么。嗯，但 G 可以是任何东西，可以是我们刚才讨论的任何一种。&gt;&gt; 是的。&gt;&gt; 还有一个不同之处，实际上，当它们

### [53:49](https://www.youtube.com/watch?v=u-H43tRgYJg&t=3229s) · b000069

以监督方式时，图像与 Apple 文本应该是一个正样本。&gt;&gt; 是的，是的。我们一开始就说，你有 paired data，对吧？苹果图像、苹果文本，橙子图像、橙子文本。所以至少在当前设定中，你需要 paired data，监督来自 paired data。呃，但注意，哪些东西需要配对，取决于 similarity function。如果 similarity function 要求苹果必须相似、橙子必须相似，那么配对就必须落实到这些单独的物体上。比如，如果我只关心整体结构相同，例如这三个 pairwise distances 相同，那么实际上我不需要……之间的 paired data，我只需要一侧有苹果、橙子、

### [54:46](https://www.youtube.com/watch?v=u-H43tRgYJg&t=3286s) · b000070

大象的三个 embeddings，另一侧可以有橙子、苹果、大象的三个 embeddings。如果用这种三元相似度函数（triplet wise similarity function），就不需要这三者之间的配对。但如果我关心苹果和苹果必须靠近，那么我就需要：是的，这是苹果，这是橙子，这是大象。那就需要这些。

### [55:18](https://www.youtube.com/watch?v=u-H43tRgYJg&t=3318s) · b000071

好。还有其他问题吗？很好。呃，我们看到了几个方面，similarity function 有很多不同选择。很多不同函数已经在……中被提出，实际上取决于具体设定：你是关心各个点对齐，还是关心全局结构，对吧？另一种情况是更全局的结构对齐，或者关心成对关系对齐。这些都会改变 similarity function，也会改变对监督数据的要求，对吧？基本上，你需要的监督数据分辨率，要与希望 similarity function 实现配对的分辨率一致。另外还想再次强调，所有这些都是端到端学习（end to end learning）的。你试图优化的 loss function

### [56:14](https://www.youtube.com/watch?v=u-H43tRgYJg&t=3374s) · b000072

是作用在两个 embeddings ZA 和 ZB 上的 similarity function G，但这两个 embeddings 本身也分别是 unit model encoders \[字幕疑误，可能指 unimodal encoders，单模态编码器\] 的函数，F of A modala TA、F of B or Madala TB \[字幕疑误，可能指带参数的模态编码器\]。所以，这一切都可以反向传播（backpropagate）并端到端训练。当然，如果预训练 f of a 和 f of b 有好处，也可以这么做。基于这一点，我们来给出具体算法，也就是现在大家所说的 contrastive learning。呃，不过还是那句话，similarity functions 比 contrastive learning 所用的要广泛得多。做法是先从一些 paired data 开始，比如图像和文本。呃，在标准版 contrastive learning 中，要求每对图像与文本表示彼此非常接近。要做到这一点，就需要

### [57:08](https://www.youtube.com/watch?v=u-H43tRgYJg&t=3428s) · b000073

每张图像及其文本的 paired data，对吧？这里举个例子，有这样一张图像，文本描述是蓝色汽车；还有黄色公交车的图像、飞机，以及这张描述为“一碗猫”的图像。嗯，使用这些 paired data，你会把每个对应关系定义为正样本对（positive pairs）。呃，这里有四个 positive pairs，而任何不是 positive pair 的组合，也就是随机排列产生的组合，都是负样本对（negative pair）。好。所以这里有，嗯，12 个 negative pairs。positive pairs 用绿色表示，negative pairs 用红色表示。然后在 contrasted learning \[字幕疑误，可能指 contrastive learning\] 中，思路还是对模态之间的 alignment 打分，让有连接的 positive pairs 靠近，并把相距较远的 negative pairs 推到一起 \[原字幕如此，可能指推开\]

### [58:04](https://www.youtube.com/watch?v=u-H43tRgYJg&t=3484s) · b000074

好。它可能看起来像这样，使用这种合页损失（hinge loss）的形式来最大化这个函数。其中 G，也就是 similarity，作用于 ZA 和 ZB plus，也就是 positive pairs。呃，这会是一个正向依赖关系。因此你要最大化相似度，同时最大化一个负值。换句话说，就是最小化 ZA 与 ZB minus 之间的 G 相似度，它们是 negative pairs。所以四个项相加，得到 positive pairs 的相似度之和，并最大化它；12 个项相加，得到 negative pairs 的这些 similarity functions，并最小化它们。

### [58:52](https://www.youtube.com/watch?v=u-H43tRgYJg&t=3532s) · b000075

而在，嗯，contrastive learning 中，这些 coordination functions 是 cosign similarity \[字幕疑误，可能指 cosine similarity，余弦相似度\]。虽然如今 contrasted learning \[字幕疑误，可能指 contrastive learning\] 随着 clip 流行起来，但早在大约 20、2010 年代，人们就在做这个，只是规模更小。一旦开始这样对齐数据，就会观察到一些很有意思的现象，对吧？基本上可以做检索（retrieval）。呃，这些 alignment 方法很强大的一点是，你可以对一个特征或图像打分，然后检索文本中最接近的内容。呃，可以做这种 crossodal retrieval \[字幕疑误，可能指 cross-modal retrieval，跨模态检索\]。还可以做 crossodal arithmetic \[字幕疑误，可能指 cross-modal arithmetic，跨模态算术\]。这里发生的是，取一张蓝色汽车的图像，把它嵌入特征空间，减去 blue 文本的 feature embedding，再加上，呃，red 这个词

### [59:49](https://www.youtube.com/watch?v=u-H43tRgYJg&t=3589s) · b000076

red 的 feature embedding，对吧？这样就得到一个新特征，可以计算最近的相似度，检索最接近的红色汽车图像，对吧？只有当这两个表示空间很好地对齐时，这种算术，也就是减去某个概念、加上某个概念，才有可能实现。对吧？因此，blue 文本在图像的语境中确实有意义，red 这个词在图像的语境中也确实有意义。你可以用一张蓝色图像减去 blue 这个词，再加上 yellow 这个词，得到黄色汽车。也可以从黄色公交车变成红色公交车。呃，还可以拿飞机照片减去 flying 这个词，再加上 sailing，检索到帆船图像，甚至用这张可爱的“一碗猫”减去 bowl 这个词，再加上 box 这个词，得到“一箱猫”。

### [1:00:48](https://www.youtube.com/watch?v=u-H43tRgYJg&t=3648s) · b000077

所以，这是 contrastive learning 的早期迹象。当然，当时只用小型低分辨率图像，文本也只是一个词，或者一个词，或者一个形容词加一个物体。现在，人们通过 clip 和其他形式的 free training \[字幕疑误，可能指 pre-training，预训练\]，真正把它扩展到了大规模，可以获取海量图像，以及海量对应描述，对吧？可以从 Wikipedia 获取，也可以从 Instagram、Flickr 和其他图像检索数据集获取。有了一个庞大的库，把它们放进一个批次（batch）。对角线上的所有内容基本上都是 positive pairs，对吧？也就是图像确实对应描述的例子；非对角线上的内容基本上都是 negative pairs。对吧？在这个大的 batch 乘 batch 矩阵中，每个条目显然

### [1:01:44](https://www.youtube.com/watch?v=u-H43tRgYJg&t=3704s) · b000078

都是把图像输入图像编码器，得到 n 个 image embeddings。呃，把描述输入 text encoder，得到 n 个 text embeddings。每个条目都是 image embedding I 与 text embedding J 之间的 cosine similarity。对吧？对角线上的所有 cosine similarities 表示 positive pairs；非对角线上的所有条目表示 negative pairs。contrastive learning loss 基本上不再是这个 hinge loss，而是这个比值：分子是你要最大化的，因为 loss 前面有负号，所以实际上你是在最大化这一项，也就是 positive pairs 的相似度；分母则是你要最小化的相似度。呃，严格来说，只应该对 negative pairs 最小化，但出于实现效率的原因，会最小化

### [1:02:39](https://www.youtube.com/watch?v=u-H43tRgYJg&t=3759s) · b000079

所有 negative pairs 加上那一个 positive pair 的相似度之和。在 GPU kernels 上，这样更容易高效实现，而且即使在分母中增加一个 positive pair，实践中也不会造成什么差别。它仍然会主要由 negative pair losses 主导。好。而 similarity function 仍然是 cosine similarity。所以每一项都只是图像的 I，呃，I embedding 与文本 embedding 的 dot product。

### [1:03:12](https://www.youtube.com/watch?v=u-H43tRgYJg&t=3792s) · b000080

好。人们发现，一旦以这种方式训练模型，所训练的编码器，也就是语言编码器和视觉编码器，会成为非常适合下游任务（downstream tasks）的编码器。再说一次，关键思想是，这些 embeddings 已对齐，但保持独立，对吧？这不是 fusion，而是让它们保持独立、同时彼此对齐。当然，现在使用这些更大的模型，可以做效果更好的 crossal retrieval \[字幕疑误，可能指 cross-modal retrieval，跨模态检索\]。比如，给它一张图像，这张图像看起来像一个电视演播室。再给它一组可能的描述，对吧？“电视演播室的照片”“讲台的照片”“会议室的照片”“教室的照片”等等。把图像嵌入，得到一个特征；再分别嵌入这些可能的描述，得到一个

### [1:04:09](https://www.youtube.com/watch?v=u-H43tRgYJg&t=3849s) · b000081

特征，然后基本上逐一计算 cosign similarity \[字幕疑误，可能指 cosine similarity，余弦相似度\]。用这个来排序，判断哪个描述最有可能。所以它确实给出了“电视演播室的照片”。呃，这里甚至可以找到最接近的描述，即“西伯利亚哈士奇的照片”，尽管它看起来不像现实中的哈士奇。呃，不过我想它有时仍会犯错，对吧？这里，在 clip 刚发布时，给它这些不同形状和大小物体的图像，它还不太擅长计数。所以，比如它认为“三个物体的照片”最有可能，而不是四个物体。呃，但现在这些模型的计数能力又强了很多。所以，基本上可以学习这些对齐表示，得到对 downstream tasks 很有用的优质特征。可以通过 alignment function 对跨模态相似度打分来做 retrieval。而且不仅

### [1:05:05](https://www.youtube.com/watch?v=u-H43tRgYJg&t=3905s) · b000082

可以做 retrieval，还可以做这种分类：给它一组可能的类别，让它选择与图像相似度排名最高的类别来分类。这也是为什么一些人可能见过，clip 刚出现时，在所谓开放集分类（open set classification）或开放域分类（open domain classification）方面取得了很大成功，对吧？传统上，如果想把图像分到不同类别，必须预先指定类别是什么，对吧？10 种数字，或者 50 种猫和狗。必须预先指定这些类别。呃，这意味着类别集合可能太大，很多类别用不到，浪费参数；有时又太小，无法对新类别进行分类。所以这些模型的一个强大之处是，基本上可以给它一张图像、任意数量的类别，只要为每个类别写一段描述，数量任意、类别任意，仍然可以

### [1:06:02](https://www.youtube.com/watch?v=u-H43tRgYJg&t=3962s) · b000083

计算相似度，并在这组类别上做分类。关于 clip 和 contrastive learning，有什么问题吗？&gt;&gt; 是否可以用各种 similarity functions，做类似分类打分的评分？哦，还是这只是……&gt;&gt; 嗯，可以，任何 similarity function 都可以打分，对吧？取一张图像，得到 embedding，现在用的是 cosign similarity \[字幕疑误，可能指 cosine similarity，余弦相似度\]，也可以是，嗯，kernel similarity，对吧？这些计算也都非常快。如果我不关心对单张图像打分和分类，也可以做我们讨论过的 pairwise 方法：给它两张图像，让它找出两者之间的差异，它仍然可以给出一组类别。所以

### [1:06:56](https://www.youtube.com/watch?v=u-H43tRgYJg&t=4016s) · b000084

现在，你有一个针对图像对的 distance function，而不是针对一张图像。再说一次，这个函数，对吧，这个 G 函数可以非常通用，只要能用 PyTorch 之类的工具实现，只要能够对它求导，就可以用来优化，也可以用于 retrieval。

### [1:07:28](https://www.youtube.com/watch?v=u-H43tRgYJg&t=4048s) · b000085

好，我来，嗯，最后深入一点，看看 clip 和其他类似 alignment 的方法究竟学到了什么，以此结束这一部分。嗯，还记得我们有这种图，A 和 B 构成一个 vin diagram \[字幕疑误，可能指 Venn diagram，维恩图\]，它们之间有一些共享信息，与各自独有的信息相对。我会给出一个直觉，不会深入太多数学细节。理解共享信息的一种方式，是互信息（mutual information）这个概念。mutual information 是一种形式化度量，基本上是说，查看两个模态，计算两项的比值。一项是它们之间的联合分布（joint distribution）。这个分布告诉我，模态中的哪些元素可能一起出现。数值较高的具有更高的联合似然（joint likelihood），不会一起出现的则具有

### [1:08:25](https://www.youtube.com/watch?v=u-H43tRgYJg&t=4105s) · b000086

更低的 joint likelihood。这就是 joint distribution。我要把它与边缘分布的乘积（product of marginal distributions）比较。product of marginal distributions 可以理解为：我拥有 X 中所有东西、Y 中所有东西，然后随机把它们配对，对吧？所以它不会捕获任何 joint distribution，只是随机配对。因此，mutual information 可以理解为，数据中的实际配对，也就是这个对应那个的实际配对，与随机组合、随机配对方式之间的差异。所以，对信息非常多的数据集，呃，这个比值也会非常大。对完全独立的数据集，两个圆不重叠、完全独立，这基本上意味着，即使你观察到的 paired data，与从数据中随机配对得到的数据，也会一样，对吧？直观上，mutual information 为零。呃，你们可以阅读

### [1:09:20](https://www.youtube.com/watch?v=u-H43tRgYJg&t=4160s) · b000087

数学细节。可以证明，嗯，这些类似 clip 的 losses，具体来说是这种 clip loss，呃，确实专注于捕获共享信息；更正式地说，可以证明它会学习这些模态之间的 mutual information，对吧？我可以给你们一个简短证明，嗯，但不要求掌握，不会出现在作业或考试中。不过，想一下这个 info inc loss \[字幕疑误，可能指 InfoNCE loss\] 的形式，它是在对这个函数 f 打分，对吧？这个 f 就是你使用 cosine similarity 学习的函数。函数 f 会给 positive pairs 很高的分数，对吧？positive pairs 的相似度应该非常高，而给 negative pairs 很低的分数，对吧？negative pairs 的相似度应该非常低，对吧？好，

### [1:10:17](https://www.youtube.com/watch?v=u-H43tRgYJg&t=4217s) · b000088

所以实际上可以把它看作一个评判函数（critic function），接收两个模态 A 和 B。它们要么是 true parents \[字幕疑误，可能指 true pairs，真实配对\]，此时输出应该尽可能高；要么是随机采样的一对，也就是 negative pair，此时输出应该尽可能低。换句话说，可以把它看成一个分类器，一个输出介于零和一之间的分类器。如果是 positive pair，就输出一；如果是 negative pair，就输出零。对吧？根据我们对这些正负样本对的了解，也可以认为，它对从 A 和 B 的 joint distribution 采样的 positive pairs 输出一，因为 joint distributions 恰恰给这些 positive pairs 较高的似然。否则，对从 product of marginalss \[字幕疑误，可能指 product of marginals，边缘分布乘积\] 中采样的 A 和 B，模型会输出零，也就是很低的分数。对吧？P of A 乘 P of B。

### [1:11:15](https://www.youtube.com/watch?v=u-H43tRgYJg&t=4275s) · b000089

因为，把这两个边缘分布相乘的定义，就是从 A 随机采样一个东西，再从 B 随机采样一个东西，把它们配对，而不考虑是否为实际配对。这就是 negative pair 的定义。所以，呃，可以把 contrastive learning 中学到的函数理解为，基本上训练一个二分类器（binary classifier），给来自 joint distribution 的样本，也就是 positive pairs，很高的分数；给来自 product of marginalss \[字幕疑误，可能指 product of marginals，边缘分布乘积\] 的样本，也就是 negative pairs，很低的分数。而且可以证明，当它被最优地训练时，这个 classifier 最终必须学到的，恰好就是那个比值，对吧？给定某个 A 和 B，它估计其来自 joint distribution 与来自这些 product of marginal distributions 的比值。呃，所以这实际上就是这些模型最终学到的东西

### [1:12:13](https://www.youtube.com/watch?v=u-H43tRgYJg&t=4333s) · b000090

当你用 contrastive learning 训练它时。然后可以把这个 far \[字幕疑误，可能指 f\*\]，也就是学到的函数，代回目标函数 law，呃，L \[字幕疑误，可能指 loss L\]，基本上得到这个方程：L-star，也就是收敛后的目标函数，基本上至少等于这个 expectation 项。你会看到这个似然比，对吧？P of A 乘 P of B，除以 A 和 B 的 joint distribution。我们看到，它实际上与刚才看到的 mutual information 非常相似，对吧？因此，实际上可以证明，这个 loss 至少等于负 mutual information 加 log n，其中 n 是 batch size，也就是样本数量。换句话说，mutual information 至少等于 loss，对吧？或者说负 loss，也就是你的目标。嗯，这意味着

### [1:13:07](https://www.youtube.com/watch?v=u-H43tRgYJg&t=4387s) · b000091

基本上，NCE 在最大化 mutual information 的一个下界（lower bound）。所以，呃，你能学到的最好结果，就是模态 A 和 B 之间 mutual information 的总量。呃，再说一次，作业或期中考试不要求掌握，但知道这一点很好。关键要点是，实际上可以证明，这些 contrastive learning 方法在学习某个 classifier，它把 joint distribution 中的数据样本，也就是 positive pairs，与 product of marginal distributions 中的数据样本，也就是 negative pairs 区分开。这个比值是统计学和机器学习中非常重要、影响很大的东西，称为 mutual information。这基本上意味着，contrastive learning 能学到的最佳内容，受数据中 mutual information 总量的限制。

### [1:14:05](https://www.youtube.com/watch?v=u-H43tRgYJg&t=4445s) · b000092

但这也有非常重要的含义：如果想用 alignment 学习更好的表示，数据中有多少 mutual information、多少共享信息，就非常重要。理想情况下，如果这是一个完美场景，模态 A 和 B 恰好重叠，因此 alignment 捕获中间这部分，而中间的信息正是你在 downstream tasks 中关心的，无论是 retrieval、classification 还是其他任务，那就很完美，对吧？contrasted learning \[字幕疑误，可能指 contrastive learning\] 学到中间的重叠部分，不多不少，恰好是任务所需的全部。嗯，换句话说，这就是多视图冗余假设（multiv-view redundancy assumption）\[字幕疑误，可能指 multi-view redundancy assumption\]：X1 和 X2 之间的 mutual information，也就是这些基于 alignment 的 contrasted learning

### [1:15:03](https://www.youtube.com/watch?v=u-H43tRgYJg&t=4503s) · b000093

方法学到的内容，恰好等于 X1 与 Y 之间的信息，也等于 X2 与 Y 之间的信息。但 why \[字幕疑误，可能指 Y\] 是你关心的任务。呃，这就意味着麻烦：你关心的、对 downstream task 重要的学习内容，呃，远远多于它们实际共享的信息。对吧？这很麻烦，因为信号不够。alignment 和 contrasted learning \[字幕疑误，可能指 contrastive learning\] 会学到那里那一点重叠，但这不够。如果做 alignment 和 contrasted learning，你会丢失很多对任务重要的信息。所以这里会遇到问题。而在另一种设定中，也会遇到问题，因为数据中的重叠太多，使得 contrasted learning 和 alignment 学得太多，呃，学得太多，学到了过多冗余特征，却不够有针对性，无法用于你关心的 downstream tasks。所以，那是恰到好处的情况。也存在一些极端情况，信息不

### [1:15:59](https://www.youtube.com/watch?v=u-H43tRgYJg&t=4559s) · b000094

足，或者信息太多、噪声太多。人们

### [1:16:11](https://www.youtube.com/watch?v=u-H43tRgYJg&t=4571s) · b000095

也可以，呃，人们也在实践中展示了这一点：基本上可以构造重叠程度不同的合成数据（synthetic data），并设计任务的位置，然后得到像这里这样很有意思的图，对吧？先逐渐增加信息。这里左侧没有重叠，mutual information 为零，所以两个变量独立，不重叠。然后逐渐增加 x1 与 x2 之间的重叠，对吧？它们越来越近，重叠越来越多。最初它们完全独立、不重叠，随着你让它们靠近、彼此重叠，性能会提高，对吧？这个区间就是从重叠不足，到重叠越来越多，最终通过 alignment 学到非常好的表示。之后，如果继续让它们更多地重叠，就会进入这个区间，那里有太多

### [1:17:08](https://www.youtube.com/watch?v=u-H43tRgYJg&t=4628s) · b000096

噪声。所以，当这些表示被用于 downstream tasks 时，就会开始看到性能下降。好，真正总结一下这部分，嗯，这个信息，呃，抱歉，这个 multimodal alignment 实际上依赖这样一个假设：共享信息才是重要的，也就是它们之间的重叠。例如，同时存在于图像和描述中的内容，可以通过 mutual information 形式化。嗯，这基本上意味着，如果它是对 downstream tasks 重要的表示，那就非常理想，对吧？它学习 mutual information，帮助你学习更好的表示。呃，否则，你可能会遇到问题，要么学得太多，要么学得太少。

### [1:18:01](https://www.youtube.com/watch?v=u-H43tRgYJg&t=4681s) · b000097

好，今天就到这里。时间到了。嗯，有……请说，有问题。&gt;&gt; 就是

### [1:18:22](https://www.youtube.com/watch?v=u-H43tRgYJg&t=4702s) · b000098

比如你在做这个？那似乎是这里的……&gt;&gt; 是的。&gt;&gt; 哦，我想那是个笔误。那里应该写 alignment。抱歉。是的。呃，但我想你问了一个很好的、更广泛的问题，就是 fusion 和 alignment 这两个概念如何相互作用，对吧？嗯，正如我们讨论的，fusion 是学习一个 joint representation。alignment 则是保持独立，嗯，同时用这些 similarity functions 进行对齐。嗯，有几个方面。首先，作业二里，我相信一些人已经看到了一项阅读任务，有一篇关于 a line before a fuse \[字幕疑误，可能指 Align Before Fuse\] 的论文。我相信也有其他论文说 fuse before a line \[字幕疑误，可能指 fuse before align\]。所以一种思考方式是，先做什么，对吧？是先获取这些数据，得到对齐的特征，让它们在语义上

### [1:19:19](https://www.youtube.com/watch?v=u-H43tRgYJg&t=4759s) · b000099

相似，在 embedding space 中接近，然后在此基础上做 fusion，对吧？这是一种非常可行的选择。也可以先做 fusion，然后开始做 contrastive learning，也许作用于融合后的特征。嗯，当然，也有做 fusion 而不做 alignment，以及做 alignment 而不做 fusion 的设定，反过来也一样。嗯，所以我会说，这有点像……我没有答案。我认为这是一个开放问题。呃，每种方式确实都有优缺点。有时二者必须在同一个系统中完成，有时则不需要。&gt;&gt; 你可以直接取你的 online \[字幕疑误，可能指 aligned 表示\]

### [1:19:59](https://www.youtube.com/watch?v=u-H43tRgYJg&t=4799s) · b000100

然后……&gt;&gt; 是的，也可以这么做，对吧？呃，可以像我们讨论的这里这样，对齐你的特征。如果对齐后的特征很好地捕获了 mutual information，而任务 Y 又恰好位于这个共享空间中，那么 alignment 实际上就是 downstream tasks 非常好的训练信号，对吧？这就是为什么，嗯，我们看到 clip，这些 clip 表示实际上是很有用的训练信号，因为大多数时候，我在图像中关心的东西，也正是别人会在描述中提到的东西，对吧？它刻意丢弃背景、纹理和一天中的时间，因为这些东西并不那么重要，而真正关注所有人物、物体和类别。所以，当这个假设成立时，它确实可以得到非常强大的

### [1:20:54](https://www.youtube.com/watch?v=u-H43tRgYJg&t=4854s) · b000101

表示；但如果不成立，就需要做更多 fusion。是的，是的。另外，这实际上也没有捕获任何 synergy，对吧？当存在 synergy、存在独有信息时，它只关注信息空间中的重叠，不关注我们也讨论过的其他可能信息来源，也就是独有性和 synergy。&gt;&gt; 是的。比如右边的图，假设它们有过多 mutual information，但任务只使用其中一个子集，那么有什么方法可以减少，嗯，减少它们的重叠，让我们能更高效地使用这些信息？&gt;&gt; 呃，好问题。

### [1:21:48](https://www.youtube.com/watch?v=u-H43tRgYJg&t=4908s) · b000102

一种方法是数据增强（data augmentation）。嗯，实际上，很多这些内容可以去看一些论文。呃，很多原则，很多 data augmentation 的原则，就是围绕这一点设计的。比如，我取一张图像，对吧，想做一些分类。我知道可以旋转它、变成灰度图、裁剪、丢掉一些像素。为什么能这样做？所有这些 augmentations 基本上都是在提供数据的不同视图（views），对吧？这些不同 views 中，一些信息在外面，一些与原图重叠。我假设与原图重叠的部分，就是所关注的物体，对吧？可以变成灰度图，物体仍然在那里，还有这边其他一些东西。我可以旋转它，比如用另一个 vend diagram \[字幕疑误，可能指 Venn diagram，维恩图\]，但同时仍然与这里重叠。我们是在尝试让数据更集中到重叠部分。&gt;&gt; 对。&gt;&gt; 对，对。

### [1:22:45](https://www.youtube.com/watch?v=u-H43tRgYJg&t=4965s) · b000103

&gt;&gt; 呃，不过，这不是……这是很好的直觉，但在实践中也不容易做到，对吧？因为有时你无法……你不知道什么会留在中间，也不知道什么可能变得太多或太少。很好。好，谢谢。大家可以走了，还有
