# Stanford CME295 Transformers &amp; LLMs \| Autumn 2025 \| Lecture 7 - Agentic LLMs

_中文讲稿_

- Channel: Stanford Online
- Source: [YouTube](https://www.youtube.com/watch?v=h-7S6HNq0Vg)
- Duration: 1:49:22
- Caption source: manual
- Status: complete
- Chinese translation: 218/218
- Translation provider: codex
- Generated: 2026-09-29T16:03:01+00:00

## 讲稿

### [00:05](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=5s) · b000001

大家好，欢迎来到 CME 295 第 7 讲。今天，我们将重点讨论一些实用技术，让我们的大语言模型（LLM）能够与外部世界、与其他系统交互。因为到目前为止，我们的 LLM 都是独立运行的。我们训练了它，也看到了它如何对问题、数学、编程数学、编程问题进行推理。

### [00:38](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=38s) · b000002

现在，我们想要把 LLM 放到其他系统的环境中使用。因此，今天的课程将重点介绍你们可能听说过的 RAG、工具调用（tool calling）和智能体（agents）。不过，在开始之前，和往常一样，我先回顾一下上次的内容。如果你们还记得，上次我们重点讲了推理模型（reasoning models），也看到了推理模型与我们所说的普通 LLM（vanilla LLM）之间的区别。

### [01:14](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=74s) · b000003

具体来说，直到上上讲，我们看到的都是向 LLM 输入一个提示词（prompt），它就直接给出回答。但上次我们看到，如果让 LLM 在输出回答之前先进行推理，那么在数学和编程等推理任务上，就能获得一些性能提升。具体来说，推理模型接收一个 prompt 作为输入，然后既输出一条通常对用户隐藏的推理链（reasoning chain），又输出一个回答。

### [02:02](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=122s) · b000004

由此，我们看了如何训练模型，让它更像一个推理模型。具体来说，我们介绍了一种核心的强化学习（RL）算法，叫作 GRPO，全称是组相对策略优化（Group Relative Policy Optimization）。我们看到，这个算法与之前介绍的那些算法有一些区别。其中一个值得注意的方面是，它没有——它不训练价值函数（value function）。

### [02:37](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=157s) · b000005

这里的示意图大致展示了 GRPO 是如何训练的。它接收一个查询（query）作为输入，然后计算同一个 prompt 的不同补全结果（completions）的奖励，并据此计算每个输出的优势（advantage）。接着计算的这个量，也就是 advantage，是相对于这一组补全结果中其他奖励而言的。

### [03:09](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=189s) · b000006

然后我们看到，如果应用 GRPO，并仔细选择奖励：第一，奖励模型输出推理链；第二，奖励模型生成好的回答。我们看到，随着 RL 训练推进，模型在这些推理任务上的表现有所提高。

### [03:40](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=220s) · b000007

我们看到，其中一项任务是数学题。在左边的图中，你们可以看到模型在 aim \[字幕疑误，可能指 AIME\] 数据集上的性能变化，这是一个有挑战性的数学问题。我们看到了这一点，同时也看到模型不断输出越来越长的回答。

### [04:10](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=250s) · b000008

具体来说，我们看到，尽管上方图表接近末尾时性能已经趋于平稳，输出长度仍然在增加。于是，我们回头查看了 GRPO 使用的损失函数表达式（loss formulation），发现其中有一项会让一个 token 的贡献因它处于短回答还是长回答中而有所不同。

### [04:49](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=289s) · b000009

这种现象叫作长度偏差（length bias）。我们看了过去几个月发表的一些论文所探索的缓解策略。一种是 DAPO，它使用的归一化因子（normalization factor）不依赖于 token 所在的位置，也不依赖于它位于哪个句子中。另一种是名为“GRPO Done Right”的论文，它实际上直接去掉了归一化项。

### [05:27](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=327s) · b000010

这些都明白了吗？好。这就是上次的内容。上次，在开始讲推理之前，我们先列举了 vanilla LLMs 的优点和缺点。因此，上一讲主要聚焦于如何改善 vanilla LLMs 有限的推理能力。而在这一讲中，我们将做两件事。

### [06:01](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=361s) · b000011

第一，看看如何将 LLM 连接到不断演变的知识库（knowledge base），具体来说，就是如何获取最新信息。第二，看看 LLM 如何帮助我们执行操作。我们将和 Shervine 一起，通过 tool calling 和智能体工作流（agentic workflows）等内容来了解这一点。

### [06:33](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=393s) · b000012

好，那我们先从第一件事开始。先介绍一下你们可能听说过的 RAG 方法。假设你已经训练好了一个模型。但问题在于，训练这个模型所用的预训练数据（pre-training data），假设是一个月前的数据。

### [07:04](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=424s) · b000013

现在，假设你想向模型询问几周前举行的选举中谁获胜了。那么，模型将无法回答，或者会输出错误答案，因为到目前为止，我们的 LLM 与外部来源没有任何连接。它只依赖在训练过程中获得的知识。因此，它给出的回答只会基于截止日期之前用于训练的数据，在这个例子中就是一个月前。

### [07:45](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=465s) · b000014

所以我们有一个很大的限制，就是 LLM 只知道它训练过的内容。你会看到，市面上所有模型都是这样。这里我用 OpenAI GPT-5 举例。如果你查看它们的模型卡（model cards），总会在某处看到写明的知识截止日期（knowledge cutoff dates）。例如，GPT-5 的知识截止日期是 2024 年 9 月 30 日，这意味着，如果你以非常朴素的方式询问那之后发生的任何事情，基础模型（base model）本身将无法直接回答。

### [08:30](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=510s) · b000015

你可能会说，为什么不直接用那之后的数据继续训练模型呢？问题在于——其实，这里有几个问题。第一个问题是，要改变 LLM 的知识，同时不导致其他方面的能力退化，是非常棘手的。因此，这通常是人们会尽量避免做的一项任务。

### [09:01](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=541s) · b000016

第二，这不太实用，因为你的应用场景很可能要求你对这个模型进行微调（fine tune）。假设你有应用场景一，你基于这个模型进行微调。然后，你又想更新模型权重来注入一些知识。那么，你就得以某种方式对所有正在使用的应用场景都做这件事，这基本上会增加大量额外开销，也会增加大量维护工作。

### [09:37](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=577s) · b000017

因此，人们通常更倾向于不通过额外训练来注入知识。一个想法是，拿到 prompt 后，把截止日期之后发生的所有事情都加进去，让模型知道发生了什么。但这种朴素方法的问题在于，正如你们所知，上下文长度（context length）是有限的。

### [10:12](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=612s) · b000018

通常，模型的 context length 在数十万 token 这个数量级。你们知道这大致——大致相当于多少内容吗？

### [10:34](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=634s) · b000019

对，一个 token 相当于四个字符。因此，按照这个粗略估算，数十万 token 大致相当于几百页，也就是一本很厚的书。

### [10:50](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=650s) · b000020

这很大，但还不足以让我们采取那种非常朴素的做法。还是回到 GPT-5，如果你查看模型卡，会看到知识截止日期是 2024 年 9 月。还有上下文窗口（context window），这里是 400,000 token。现在，假设上下文其实不是问题，它实际上是无限的。

### [11:21](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=681s) · b000021

设想我们真的把所有东西都放进上下文里。那么，问题在于，人们注意到，如果向 LLM 输入大量无关信息，LLM 的性能反而会下降。也就是说，例如，你问它，我想，比如上次选举谁获胜了？然后给它输入一大堆不相关的信息，LLM 就容易感到困惑。

### [11:58](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=718s) · b000022

人们做过这样的测试，叫作大海捞针测试（needle in a haystack test）。其思路是，给 LLM 一个很长的 prompt，也就是你的“干草堆”，然后在 prompt 中放入一个事实，再问模型那个事实是什么。因此，其目的就是让 LLM 找出，我想，在那个巨大的 prompt 中，相关信息在哪里，也就是那根“针”在哪里。

### [12:37](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=757s) · b000023

当人们尝试不同长度的 prompt，并把事实放在不同位置时，他们发现，prompt 的长度和事实放置的位置都很重要。这张幻灯片上是针对 GPT-4 测试得到的一张热力图（heat map），我想大概是一两年前的。

### [13:10](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=790s) · b000024

测试者把这个事实放在文档中的不同位置。因此，这里是文档深度（document depth），而 x 轴是 prompt 的长度。我们看到，当 prompt 超过一定数量的 token 时，LLM 实际上很难检索到正确的信息。尤其是当事实位于 prompt 前半部分的某个位置时，它很难做到这一点。

### [13:44](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=824s) · b000025

这说明，即使假设 context length 是无限的，直接采用这种朴素方法仍然会有问题。这是另一个原因。现在，假设 context length 是无限的，也假设我刚才提到的问题不存在。那么，另一个问题就是你要付费。具体来说，这些调用，这些 LLM 调用，是按 token 收费的。

### [14:20](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=860s) · b000026

所以，输入的 prompt 越大，你付的钱就越多。仅从这个角度出发，你就有理由不要往 prompt 里放太多内容。例如，还是回到 GPT-5，费用的数量级大约是每百万 token 1 美元。我想，这不算很贵，但如果所有 prompt 都这样做，费用就会累积起来。

### [14:50](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=890s) · b000027

出于所有这些原因，希望我已经说服你们，我们需要一种更聪明的方法：不是一次性把所有新信息都放进 prompt，而是设法只找到相关信息，再把它放进 prompt。这就是 RAG 背后的想法。RAG 的全称是检索增强生成（Retrieval Augmented Generation）。

### [15:22](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=922s) · b000028

这里的思路是用相关信息来增强 prompt。我在这里把“相关”加粗了。我想，这项技术的核心就是：如何只把相关部分放进 prompt？我们马上会看到。从很高层次来看，假设你输入一个问题。在这个例子中，问题是，比如，地方选举的获胜者是谁？

### [15:56](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=956s) · b000029

这里的思路是设法获取正确或相关的信息，然后在这里用它进行增强，从而输出答案。

### [16:11](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=971s) · b000030

这就是大致思路。到目前为止，这个方法能理解吗？能。好，很好。这就是 RAG 背后的想法。现在我们要进一步讨论细节。刚才讲的是大致思路，这里我想强调 RAG 的三个主要步骤。首先，你有一个 prompt，然后你想设法检索到一条相关信息，帮助你回答这个 prompt。

### [16:48](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=1008s) · b000031

这里，第一步是检索相关文档。你可以把 prompt 看作一个实体，然后还可以有另一个空间，比如，我不知道，一个存放所有文档的知识库。因此，思路就是设法获取相关文档。这就是检索（retrieve）步骤。第二步是在获取相关信息后，增强（augment）你的 prompt。

### [17:21](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=1041s) · b000032

你拿到检索出的信息，把它放进 prompt，然后提出问题。以地方选举为例，就好像我在问：这次选举的获胜者是谁？然后，我检索到相关信息。现在，prompt 就变成了：这次选举的获胜者是谁？顺便说一下，这次选举举行于，诸如此类。这就是获胜者。这就是我们输入给 LLM 的内容。

### [17:53](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=1073s) · b000033

换句话说，我们在 prompt 中给出了答案。第三步是把这个 prompt 输入给 LLM，让它生成（generate）回答。嗯？

### [18:20](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=1100s) · b000034

完全正确。问题是，你在检索阶段很可能做得不好，是的。因此，检索阶段才如此重要。我们将重点讨论如何确保这一部分做得好。

### [18:41](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=1121s) · b000035

我们会看看如何评估我们的配置和不同方法。不过，谈到 RAG 时，我们主要关注的是尽可能把检索部分做好。好。我还想再强调一次，为什么它叫 RAG：检索、增强、生成——retrieve、augment、generate，RAG。

### [19:13](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=1153s) · b000036

好。正如你指出的，第一步，也就是检索步骤，非常重要，所以我们会在这里花一些时间。我想，第一步是设法清理我们可能需要的文档集合。我说过，我们可能想查看外部信息，但需要对这些信息进行某种整理、排序，再把它们放在某个地方。

### [19:48](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=1188s) · b000037

这一整套东西通常叫作知识库。为了构建知识库，我们通常会收集一组有用或可能有用的文档。完成后，我们会把它们划分成所谓的文本块（chunks）。你可以把一个 chunk 理解为文档的一个子集，它有给定的最大长度，以 token 数量衡量，通常在几百个 token 的数量级。

### [20:29](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=1229s) · b000038

这里的思路是，每当听到检索，你就应该想到嵌入（embeddings）。在这里，我们会为每一个 chunk 计算对应的 embedding。创建知识库时，有几个超参数（hyperparameters）需要调整。第一个显然是 embedding 的维度。通常，如果你的文档可能更加细腻、更加复杂，你会希望维度更大。

### [21:07](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=1267s) · b000039

但如果维度更高，可能就会占用更多空间，在推理时也可能需要更多计算。所以我想，这是一个权衡。你不一定希望 embedding 的维度过大。这里，embedding 的维度通常在几千这个数量级，比如 1,500 左右。然后是 chunk 大小，也就是这里这些小片段有多大。

### [21:39](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=1299s) · b000040

你不希望它们太小，否则文本可能会脱离上下文。你也不希望它们太大，因为 embedding 可能无法有意义地表示其中的内容。所以，这同样是一个权衡。不过，人们通常会选择大约 500 token 的 chunk 大小，也就是几百 token 这个数量级。然后还有一个——哦，对，你有问题。请说？

### [22:10](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=1330s) · b000041

问题是，你会为此训练一个 embedding 模型吗？你有两个选择：可以使用预训练的 embedding 模型，这也是人们通常的做法；也可以训练自己的模型。再过几张幻灯片，我们会稍微详细地介绍。

### [22:34](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=1354s) · b000042

问题是，embedding 模型的作用是什么？我们马上会看到。简单来说，它试图表示这些 chunks，以实现你的最终目标，也就是获取相关文档。我们会稍微了解一下它们是如何训练的。这就是总体思路。

### [22:58](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=1378s) · b000043

好，这部分就是这样。然后还有第三个超参数，即你希望 chunks 之间有多少重叠。如果采用非常朴素的划分方式，所有片段都是相互独立的，彼此之间没有重叠。但通常，前一个 chunk 中的某些内容与理解当前 chunk 有关，所以我们希望有一些重叠，这也是人们通常会设置重叠的原因。

### [23:35](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=1415s) · b000044

它通常是一百多个到几百个 token，处于几百这个数量级的较低范围。

### [23:41](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=1421s) · b000045

好。假设你已经有了知识库。现在的问题是，给定一个 prompt，如何检索相关文档？答案是，我们通常分两步进行。不知道你们有没有人有推荐系统（recommendation systems）或搜索方面的背景？有吗？有。这里介绍的方法与那个领域非常相似。

### [24:12](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=1452s) · b000046

我想，LLM 社区的人借鉴了一些想法，并利用了那个领域中的一些技术。这也是推荐问题中通常会出现的一种设置。我们有两个阶段。第一阶段通常叫作候选检索（candidate retrieval）。这里的目标是从非常、非常、非常多的 chunks 中，筛选出一个小得多、可能相关的候选集合。

### [24:49](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=1489s) · b000047

在这个阶段，我们试图尽可能提高召回率（recall），只是进行一个粗略操作，以便获得尽可能多的潜在相关候选。然后是第二阶段，这一步有时是可选的。但这个阶段是为了真正确保排在最前面的文档确实是相关的。这个阶段叫作排序（ranking）。

### [25:21](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=1521s) · b000048

这里的思路是，根据可能相关的文档列表，对它们进行排序，让真正相关的文档排在最前面，依此类推。通常，在这个阶段，我们会使用一个计算量稍大的模型或方法，因为与第一阶段相比，需要排序的候选集合小得多。

### [25:52](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=1552s) · b000049

回到你刚才的问题，我们希望 embeddings 是什么样的？它主要影响第一阶段，我们马上会看到。不过，第二阶段也非常重要。

### [26:08](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=1568s) · b000050

好，到目前为止都明白吗？大家都清楚这个两阶段方法了吗？嗯。

### [26:27](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=1587s) · b000051

非常好的问题。问题是，我们是否以朴素的方式划分 chunks，也就是说，不管内容如何，只按 token 数量划分？这是个很好的问题。答案是，我们会介绍一些扩展方法，来缓解朴素划分导致片段不合理的问题，你希望设法为它补上上下文。我们会介绍一种能做到这一点的方法。再过几张幻灯片就会讲到。

### [26:57](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=1617s) · b000052

不过，我觉得你的问题也很好，因为这取决于文档类型。比如，如果我们有，我不知道，比如一个 JSON 文件或者 markdown，或者取决于你需要切分的文件，你还需要注意这些文件内部的结构。所以这里还有一些细微之处，我们不会详细展开，但我想特别指出这一点。是的，很好的问题。还有其他问题吗？

### [27:29](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=1649s) · b000053

好，很好。现在我们已经清楚了检索的两个主要阶段，接下来分别讨论每一步。正如我提到的，第一步是 candidate retrieval。我们想从这个可能非常庞大的知识库中，设法筛选出，比如，100 多个可能相关的候选。

### [28:02](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=1682s) · b000054

在这里，我们会利用知识库初始化时计算出的 embeddings，并通过语义相似度搜索（semantic similarity search）来获取可能相关的候选。你们还记得如何比较 embeddings 吗？

### [28:31](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=1711s) · b000055

对，余弦相似度（cosine similarity）通常是一种比较 embeddings 的好方法。这里的思路是用一个 embedding 表示查询。我们已经拥有所有 chunks 的 embeddings，因此可以通过相似度搜索找到最相关的 chunks，并筛选出排在最前面的那些。

### [29:03](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=1743s) · b000056

这里的思路是，你有查询，也有 chunk，为两者分别得到一个 embedding。然后进行相似度运算，大多数情况下是 cosine similarity，得到一个相似度分数。然后只保留前面，比如，我不知道，100 个，再继续处理。我想指出，这个阶段有一定的复杂性，因为你的知识库可能非常庞大。

### [29:40](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=1780s) · b000057

人们通常会使用所谓的近似最近邻（approximate nearest neighbor）方法。你们可能听说过一些实现这类方法的库。这些通常会在这里派上用场。我们不会深入细节，但我想指出这一点。这里的思路是，在构建知识库时，以某种方式对 embeddings 进行分区，从而避免——就是让你避免直接进行朴素的线性搜索。

### [30:18](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=1818s) · b000058

这就是思路。你可能会看到一些技术，比如 ANN 技术，也就是 approximate nearest neighbor 技术。这些技术通常就在这里使用。我还想指出另一点，就是这里通常使用的架构名称，你们也可能听说过。为此，我们需要回忆一下，这些 embeddings 实际上是通过模型处理得到的。

### [30:50](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=1850s) · b000059

通常是仅编码器（encoder only）模型。你们可能会听到双编码器（BI encoder）这个术语。它指的是，我们把查询输入一个 encoder，再把 chunk 输入一个 encoder。两者相互独立，然后比较 embeddings。

### [31:16](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=1876s) · b000060

这也是我想问你们的另一个问题，但我想我还没来得及问。如果你们还记得，我想是在第二讲或第三讲，我们介绍过 BERT 模型。通常，你会使用类似 BERT 的模型来编码这些文档。回到你的问题，如何计算这些 embeddings？有一篇论文，我非常推荐阅读。

### [31:47](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=1907s) · b000061

它叫作 Sentence BERT。这篇论文解释了——首先，正如名字所示，它是 BERT 的扩展。这个扩展让你能够为查询、为文档中的每个，比如，序列计算一个 embedding，并专门使它适用于相似度搜索。

### [32:17](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=1937s) · b000062

这里的思路是，使用一个损失函数（loss function），鼓励相关实体之间具有较高的 cosine similarity，而不相关实体之间具有较低的 cosine similarity。对，欢迎看看这篇论文。如果你了解 BERT，我知道你们现在已经了解了，那么这篇论文读起来相当容易。非常推荐。到目前为止都明白吗？嗯？

### [32:48](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=1968s) · b000063

嗯？

### [32:54](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=1974s) · b000064

问题是，默认用什么方式计算相似度？对，就是 cosine similarity。不过，你会在不同实现中看到，人们也会使用其他距离。我鼓励你们思考这些距离之间的关系。比如，你会看到 L2 距离。但如果所有向量的范数都是 1，就会出现很多可以简化的地方。因此，你可能会看到一些变体，但我会说，它们或多或少都相当于 cosine similarity。

### [33:29](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=2009s) · b000065

对，很好的问题。好，我们仍然在 candidate retrieval 阶段。刚才看到的是从相似度——抱歉，从语义相似度的角度检索文档的一种方法。顺便问一下，语义相似度是什么意思？它意味着找到含义相同或相关的文档或实体。但我们计算这些 embeddings 时，并没有强制要求任何关键词匹配。用这种方式检索文档时，匹配到的文档完全可能没有任何共同的词，但表达的意思相同。

### [34:26](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=2066s) · b000066

有时，你希望确保查找、搜索到的内容确实包含 prompt 中的关键词。这种情况下，你就会希望有第二种处理方式。你可能在其他地方看到过 BM25。BM25 是一种相关性分数，实际上是启发式分数（heuristic score）。它基于查询内容与文档内容之间重叠部分的某种函数。

### [35:09](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=2109s) · b000067

在某些情况下，它非常方便，比如你有一个查询，并且一定要找到包含该查询关键词的文档。这里有一个例子，前面讲上一种方法时，我实际上非常简略地带过了，稍后还会回来讨论。假设我们有两只泰迪熊，一只叫 Cuddly，另一只叫 Huggy。

### [35:40](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=2140s) · b000068

你想弄清楚 Cuddly 在哪里。这就是你的查询。如果使用 BM25，那么按照定义，你得到的答案会包含与你查询中某些词的重叠。因此，这里你会得到，比如，包含 cuddly 在哪里这类内容的文档。但如果只使用 semantic similarity search，就没有这种保证。

### [36:20](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=2180s) · b000069

你只会得到语义相似的文档，而这些文档不保证包含 prompt 中的关键词。举个例子，Huggy 和 Cuddly 可以被认为在语义上是相似的。因此，里面可能不会有 cuddly——不一定会有 cuddly。只是用这个来说明一下。

### [36:51](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=2211s) · b000070

这就是为什么现在人们会根据自己的应用场景，考虑在相关性分数中也加入一些启发式因素，是否对这个应用场景有用。有些人会把基于 embedding 的搜索和基于启发式的搜索混合起来。也就是以某种方式结合 embeddings 和 BM25，在这种情况下，你可能会得到。

### [37:26](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=2246s) · b000071

更加相关的文档，具体取决于你的应用场景。

### [37:32](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=2252s) · b000072

这样能理解吗？嗯。现在我回到你刚才提到的问题：朴素地切分 chunks 是否一定能得到连贯的内容？你说得完全正确，有时候不能。但在回答这个问题之前，我们先讨论另一个问题：通常，当人们想向 LLM 询问某件事时，输入的查询与知识库中的内容在性质上有所不同。

### [38:17](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=2297s) · b000073

查询通常可能比较短，也可能是一个问题。但文档中的内容通常更长，是一句接一句的文本。因此，仔细想想，如果用同一个 encoder 来嵌入查询和文档，那么这两个 embeddings 并不是特别具有可比性，因为一个对应问题，另一个对应文档。

### [38:50](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=2330s) · b000074

有一种扩展方法试图缓解这个问题，我在下面放了论文链接。它叫作 height \[字幕疑误，可能指 HyDE\]。它不是直接计算 prompt 对应的 embedding，而是先生成一篇虚构文档。也就是调用一次 LLM，根据这个 prompt 生成一篇虚构文档，再对这篇虚构文档进行嵌入，以寻找相关 chunks。

### [39:27](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=2367s) · b000075

它可能有效，也可能无效，并不是所有人都会一直使用。我会说，它是一种值得尝试、看看是否有效的方法。这是缓解问题的一种方式。另一种方式是，分别使用专门训练的 encoders，一个编码查询，另一个编码文档。换句话说，不使用同一个 encoder。人们通常不会这样做，主要是出于维护方面的考虑。

### [40:00](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=2400s) · b000076

不过，这也可以是另一种解决方案。

### [40:04](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=2404s) · b000077

现在，终于回到你关于如何让这些 chunks 有意义的问题。如果脱离上下文，它们可能就没有意义。因此，这里的思路是在前面加上一段文本，简要概括理解这个 chunk 所需的内容。这里，假设你拥有所有文档。

### [40:34](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=2434s) · b000078

假设你有一篇文档，把它划分成 n 个 chunks。这里的思路是，不再孤立地看待这些 chunks，而是基于整篇文档，为每个 chunk 计算一些与它相关的上下文。

### [40:59](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=2459s) · b000079

那要怎么做呢？还是调用 LLM。通常，你会提供，比如，整篇文档，再提供你想补充上下文的 chunk。然后问模型：请给我一段简短、精炼的上下文，让这个 chunk 能够被理解。现在你可能会说，这需要很多次 LLM 调用，你可能有大量 chunks，这会非常昂贵。

### [41:31](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=2491s) · b000080

有一种策略可以降低费用，不知道你们是否听说过这个选项。它叫作提示词缓存（prompt caching）。既然你们现在已经很了解 LLM 的工作原理，知道它们通常是仅解码器（decoder only）模型等等，那么你们就知道，如果所有 prompt 都使用相同的前缀，就会一遍又一遍地执行相同的计算。

### [42:10](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=2530s) · b000081

这里的思路是，只计算一次，保存所有相关的激活值（activations）。之后不再重新计算，而是直接查找，只做一次查找，再解码剩余部分。

### [42:30](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=2550s) · b000082

能理解吗？嗯。问题是，来自语言模型的 activation 吗？对，因为当你向模型输入一个 prompt，并要求它生成回答时，模型需要处理全部输入，计算所有层的 activations，然后在生成过程中，对所有这些其他组成部分进行注意力（attention）计算。既然它是 decoder only，也就是说，它只从左向右处理。

### [43:07](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=2587s) · b000083

如果输入的内容相同，就会产生相同的 activations。对。

### [43:20](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=2600s) · b000084

问题是，如果你用的是一个封闭模型怎么办？prompt caching——我马上会用一张幻灯片讲到——是封闭模型或提供商提供的一个选项。他们会告诉你：你的所有 prompt 都有相同的前缀，因此，我们会为你降低费用。如果你查看模型定价页面，就会看到常规输入的价格。

### [43:56](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=2636s) · b000085

也就是未缓存输入的价格。然后还有每个已缓存输入 token 的价格。这里你可以看到，比如 OpenAI 模型，价格是原来的 110th \[字幕疑误，可能指 1/10\]。那么，我想借此告诉你们什么呢？就是尽量聪明地组织 prompts，把那些可能在不同 prompts 中重复出现的内容集中放在开头，这样就能利用这个不错的折扣。

### [44:32](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=2672s) · b000086

能理解吗？好，很好。到目前为止，我们已经看到了如何从可能有数千、甚至数百万个 chunks，增加到——或者说减少到——数百个可能相关的 chunks。现在，我们希望以更有意义的方式对它们排序。第二部分更偏向可选，因为有时第一轮筛选可能已经足够好了。不过，我想，第二步是更有针对性地给出最终分数，以便真正选出最终的，比如，前 k 个 chunks。

### [45:24](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=2724s) · b000087

第二阶段叫作 ranking，或者重排序（re-ranking）。叫 re-ranking，是因为第一步已经有了某种排序，所以我们是在重新排序。我们不再使用已计算好的 embeddings 之间那种非常快速的相似度运算，而是使用一种可能稍微复杂一点的方法。我们不再分别考虑查询和 chunk，而是把它们两个一起输入 encoder，并由此得到相关性分数。

### [46:11](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=2771s) · b000088

这样做可能更有意义，是因为模型会同时查看查询和 chunk，再给出一个分数。而在第一步中，查询有一个 embedding，chunk 有另一个 embedding，缺少模型能够捕捉到的那种交互。你也会看到，这种设置被称为交叉编码器（cross-encoder）设置，因为两个输入都会一起送入 encoder。

### [46:52](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=2812s) · b000089

因此，两者之间会有一些交叉交互。如果你还记得，第一种方法是 bi-encoder 设置，而这一种是 cross-encoder。

### [47:09](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=2829s) · b000090

对。问题是，实际上会计算两者之间的 attention 吗？对，完全正确。这里，sentence there \[字幕疑误，可能指 Sentence Transformers\] 有很多不错的文档。我非常推荐阅读它们的文档，链接就在幻灯片底部。好。你会对所有可能相关的 chunks 进行这一操作，因此，每个 chunk 都会结合 prompt 计算出一个分数。

### [47:42](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=2862s) · b000091

然后，你最终得到排序。现在的问题是，你对这个排序满意吗？为了回答这个问题，你需要一种量化性能的方法。接下来五分钟，我们就来看看，通常用哪些指标来做这件事。还是那句话，这与搜索或推荐非常相似。如果你有这方面的背景，就会看到一些共同之处。

### [48:18](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=2898s) · b000092

具体设置是这样：你有一批 chunks，执行第一步和第二步。最终，会有 k 个 chunks 排在最前面，你会把它们判定为相关。然后，你想把这些结果与真正相关的 chunks 进行比较。可以把它理解为，你有标签，就和二分类（binary classification）一样。

### [48:49](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=2929s) · b000093

有相关和不相关两种标签，你预测其中一些是相关的，并想知道自己做得怎么样。这就是设置。对于排序来说，你还需要以某种方式纳入“把内容排在多靠前的位置”这一信息。这里，假设你已经把这 n 个 chunks 按照从最重要到最不重要的顺序排好了。

### [49:21](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=2961s) · b000094

假设有第一、第二、第三，依此类推。你只关心前 k 个，因为在 rack \[字幕疑误，可能指 RAG\] 设置中，你通常会检索相关的前 k 个，并把这前 k 个都放进 prompt。那么，你很可能会使用的第一个指标叫作 NDCG。

### [49:49](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=2989s) · b000095

字母有点多，我来解释它的含义。NDCG 会考虑你把相关文档排在什么位置，试图以此量化排序的好坏。这里有个公式，看起来可能有些吓人，但它要做的事其实很简单。它希望在这种情况下让分数更高。

### [50:23](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=3023s) · b000096

就是当你把相关文档排得更接近第一名时。它会对排序中的前 k 个位置求和，并查看每个位置上的内容是否相关。例如，它检查第一个位置，看第一个位置的内容是否不相关。那么相关性——如果相关，就是 1。

### [50:55](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=3055s) · b000097

于是就是 1 除以某个与排名有关的量。它会对所有排名都这样计算。因此，如果你把相关文档排得靠前，分数就会更高。这基本上就是这个指标的目标。这部分叫作折损累计增益（discounted cumulative gain，DCG）。之所以是累计增益，是因为你基本上在查看前 k 个位置中是否有相关文档，这是累计的部分。之所以是折损，是因为对你来说，把相关文档放在第 1 位，比放在第 k 位更好。

### [51:42](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=3102s) · b000098

这一点可以从分母中看出来。那么，为什么叫 NDCG？归一化的部分是什么？这个指标可能取很多不同的值，取决于有多少相关文档。因此，人们会针对给定查询，计算你能够获得的所谓“理想、最优或者上界”DCG，称为理想 DCG（ideal DCG，IDCG），再用 DCG 除以 IDCG 进行归一化。

### [52:23](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=3143s) · b000099

这样做的原因是，他们希望当你的排序与最优排序一致时，你能得到 1 分。他们基本上是想让这个分数具有意义。

### [52:39](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=3159s) · b000100

这样能理解吗？嗯？

### [52:52](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=3172s) · b000101

问题是，相关性分数是如何计算的？你可以把第一步和第二步看作一个两步流程，用来决定你认为哪些文档相关。完成这两个阶段后，你认为相关的文档就在这里。通常，每个检索出的 chunk 都会有一个分数，然后你会对这些 chunks 排序。

### [53:25](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=3205s) · b000102

你会按分数从高到低排序。而这里要使用的相关性，是实际标签。也就是说，这个 chunk 到底是否相关？你要查看检索出的 k 个 chunks，然后问自己：好，第一个 chunk 实际上相关吗？你有标签，知道哪些相关，哪些不相关。公式中使用的就是这些标签。

### [53:58](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=3238s) · b000103

对，那就是真实标签（ground truth）。完全正确。对。

### [54:04](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=3244s) · b000104

好。能理解吗？嗯，好，很好。还有其他一些指标。另一个叫作倒数排名（reciprocal rank）。这个简单得多，它取所有相关文档中最靠前名次的倒数。例如，假设在前 k 个文档中，第一个相关文档排在第 2 位。

### [54:40](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=3280s) · b000105

那么 rank 就等于 2。它基本上不关心第一个相关文档之后的任何相关文档。这是一个更简单的指标，通常有很好的相关性，所以人们会使用它。当然，你们也熟悉经典的分类指标——recall 和精确率（precision）。如果你们还记得，当有两个类别时，有正类，也有负类。

### [55:14](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=3314s) · b000106

recall 会查看所有实际上为正的观测，并问：在所有实际正样本中，哪些是你确实预测为正的？这就是你们熟悉的 recall。我想，排序中也有一个对应版本：在所有相关、实际相关的文档中，也就是相当于正类，哪些被你预测为相关？

### [55:55](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=3355s) · b000107

这基本上就是问，哪些位于前 k 个中？同样，也有 precision 的对应版本。如果你还记得，precision 是在所有预测为正的样本中，有多少实际上为正？这里也是一样。哪些是你预测为正的？也就是，你选入前 k 个的是哪些？

### [56:26](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=3386s) · b000108

在这些里面，哪些实际上为正？也就是，哪些实际相关？

### [56:35](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=3395s) · b000109

能理解吗？我想，这四个指标——NDCG、MRR、precision at k、recall at k——在很多论文中都会出现。因此，我非常建议你们熟悉它们的思路，或许也熟悉一下公式。你会使用这些指标，量化检索器（retriever）做得好不好。现在有很多基准测试（benchmarks），其中有一个相当流行。

### [57:05](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=3425s) · b000110

它叫作 massive text embedding benchmark。如果想测试 retriever 的表现好不好，通常会把它拿来，在这个 benchmark 上进行评估，然后计算所有这些指标。如果你有不同的解决方案，通常就会比较这个指标。

### [57:29](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=3449s) · b000111

讲到这里，希望我们对如何构建 RAG 系统，尤其是如何拥有一个好的 retriever，有了更清楚的认识。我们大概还剩一分钟。关于第一部分，有什么问题吗？嗯？

### [57:58](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=3478s) · b000112

问题是，对于 re-ranking，我们使用一个输出相关性分数的 encoder。通常，我们会训练一个能完成这件事的模型。一般来说——我相信已经有一些预训练模型，但你完全也可以使用自己的定制模型。相比第一步，这个模型通常会稍微复杂一些。因为这里你可以花更多时间来生成这个分数，毕竟处理的是，比如，100 多个可能的候选，而不是多得多的数百万或数十万个候选。

### [58:38](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=3518s) · b000113

这就是思路。嗯？

### [58:46](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=3526s) · b000114

问题是，用对比损失（contrastive loss）进行训练怎么样？这是一个我们在这里，我想，不会展开的细节。不过，为了训练这些模型，你可以使用很多不同类型的 loss function。我非常推荐阅读 S-BERT 论文，因为那篇论文尝试比较了几种 loss function，而这就是其中之一。所以，这是个很好的问题。我非常推荐为此阅读 S-BERT 论文。

### [59:17](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=3557s) · b000115

好，接下来交给 Shervine。谢谢你，Afshine。非常感谢你介绍 RAG 方法。现在，来到这节课中我最喜欢的部分。我们将了解 tool calling 和智能体的世界，很快就会看到你的 LLMs 将变得多么强大。Afshine 刚才介绍的是，如何把非结构化数据作为 prompt 的一部分输入 LLM。

### [59:53](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=3593s) · b000116

现在，我们要看看还能做些什么，针对的是我们想注入的数据具有结构的情况。在 RAG 中，你有一些满是文字、文字、文字的文档，只想获取相关文档来回答 prompt。但在这里，假设你的数据中存在某种结构，决定了输入与输出。通常，你也许可以把它表示为一张表。

### [1:00:23](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=3623s) · b000117

表中有不同的列，根据某些列的值，会有一个给定的输出。因此，我们大概可以把这种设置重新表述为一个函数、一种设置。我们提到了 tool calling，而这种重新表述叫作函数调用（function calling）。在这一部分接下来的内容中，假设你通过一个函数获得这种输入和输出之间的关系。

### [1:00:55](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=3655s) · b000118

这里，如果我要把给定 ID、字段和其他参数所对应的结果换一种形式表示，你可以把它理解为一个以这些内容为参数的函数。输出就是这个函数所给出的输出。

### [1:01:16](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=3676s) · b000119

在 tool calling 和 function calling 的领域中，你经常会看到 LLMs 倾向于使用 Python 作为语言，因为它读起来非常简单。因此，我们也将使用 Python 作为示例。不过，没有任何东西要求我们一定使用 Python。你完全可以使用其他语言进行 tool calling。

### [1:01:42](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=3702s) · b000120

只是补充说明一下。关于这个设置有什么问题吗？好，很棒。tool calling 本身没有什么有争议的地方，不过我还是会给出一个完整定义，确保大家的理解一致。我到处浏览了一下，试图找到一个权威来源。在 IBM 这个网站上，有一篇文章定义了——试图定义什么是 tool calling。

### [1:02:12](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=3732s) · b000121

所以从现在起，我会以他们的定义为依据。我来大声读一下。工具调用（tool calling）使自主系统能够通过动态访问外部资源，并可能对这些资源采取行动，来完成复杂任务。我希望大家从中理解两点。首先，是完成某个任务这个概念。也就是，给定一个输入，你必须完成某个任务，然后是可能会依赖外部资源。

### [1:02:49](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=3769s) · b000122

所以，它不一定非得是外部的。你不一定要依赖外部资源。但这是一个潜在的特性，可以帮助你弥补 Afshine 在讲座开头提到的差距，也就是弥补预训练的大语言模型（LLM）所存在的知识缺口。几分钟后，我们会看一些例子，说明这可能意味着什么。不过，是的，这是其中一个神奇之处。

### [1:03:22](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=3802s) · b000123

好。很好。为了让这些说法切实对应现实应用，我们来看看，在一个非常具体的例子中，一次工具调用（tool call）能给我们带来什么。假设你很喜欢泰迪熊。你现在就在 Stanford，想在附近找一只泰迪熊。如果你拿出手机，直接问：找一只我附近的泰迪熊，会怎么样？

### [1:03:55](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=3835s) · b000124

那么，你现在的 LLM 如果没有任何工具，就不会知道你附近哪里有泰迪熊的现实情况，或者实时更新的信息。所以，它很可能会回答类似于“我不知道”或“不确定”的内容。我想说的是，借助工具，我们来看看如何做到注入必要的信息，让 LLM 知道该如何回应你的查询。

### [1:04:31](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=3871s) · b000125

接下来几分钟的目标，就是弄清楚两件事：我们能做什么——能在 LLM 的前置说明（preamble）里注入什么？以及，为了完成这样的请求，我们可以经历哪些步骤？

### [1:04:52](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=3892s) · b000126

到目前为止都明白吗？嗯？

### [1:05:02](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=3902s) · b000127

问题是，这些函数 API 是预先计算好的吗？这是个很好的问题。是的，你要事先定义它们。你有一些 API。我们马上就会看到。它们不是由 LLM 即时生成的。

### [1:05:19](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=3919s) · b000128

好。很好。关于这个设定，还有其他问题吗？我知道需要消化的内容会很多。

### [1:05:28](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=3928s) · b000129

好。很好。为了对应现实情况，我们来看一个完整的例子，看看函数定义（function definition）可以是什么样。在寻找泰迪熊这个例子里，你可以设想一个名为 find teddy bear 的函数定义。它会根据你的位置调用某个 API，并检索出可能的候选对象。

### [1:05:58](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=3958s) · b000130

我会介绍函数调用（function call）所包含的主要特征，并把它们与定义联系起来。首先，当我们想把这样的 API 展示给模型时，需要为它以及它的输入和输出编写文档，让模型知道这个函数是做什么的。所以，通常在 Python 示例中，某个函数下面的描述，对于模型理解它的用途至关重要。

### [1:06:34](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=3994s) · b000131

然后，我们在刚才给出的 tool call 定义中看到，我们能够发起后端调用（backend calls）。这正是寻找你周围的泰迪熊时需要做的事情。你需要查询某个 API，获取可获得的泰迪熊。然后根据你的位置，返回最近的那些。这正是这个函数实现所做的事。

### [1:07:08](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=4028s) · b000132

它会返回结构清晰的内容。你们可以看到，也许从你们的位置看有点小，不过这里有一个类定义（class definition），为输出赋予某种结构，让它可以被解释。我们很快就会看到，模型将以这个输出为依据，给出最终回答。

### [1:07:36](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=4056s) · b000133

好。很好。我还想说一点，我们在这里看到的这些，都是你实现的内容。你不会看到所有这些——如果你是一个 LLM，你不会看到全部内容。作为 LLM，你只关心函数 API、输入和输出，以及文档的主要内容。所以，这些实现细节都会放在你的代码库（code base）里。

### [1:08:07](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=4087s) · b000134

但 LLM 不会看到它们。好。很好。现在，我们一步一步来看，怎样让它运行起来。第一个阶段是，当你提出一个与函数有关的问题时，你会在 preamble 的开头插入函数 API。正如我提到的，不包含它的实现。所以只有函数本身，以及完整的文档。

### [1:08:43](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=4123s) · b000135

在这里，你希望 LLM 根据用户查询，把正确的参数（arguments）传给函数。对应你刚才说的，这里 LLM 的目标不是推断任何函数的实现，而只是确定应该传入哪些参数。嗯？

### [1:09:19](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=4159s) · b000136

问题是，这到底要怎么训练？再过几张幻灯片，我们就会看到。问得很好。这正是接下来需要问自己的问题。

### [1:09:33](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=4173s) · b000137

我们会看到如何训练这些能力。不过在这里，先假设它已经训练好了。LLM 从上下文（context）中可能已经知道我们的位置，因为假设你开启了位置权限，LLM 知道你在哪里。所以，它知道你在 Stanford。这些就是提供给 LLM 的坐标。然后，第二个阶段就是真正执行那次 function call。

### [1:10:04](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=4204s) · b000138

这与 LLM 无关。你只需要拿到函数和参数，执行它，然后得到某个答案。正如我们提到的，这个答案以一种可以理解的方式组织起来。所以，在那个函数实现中，你会返回一个对象，说明返回的泰迪熊有哪些特征。例如，它的名字，也许还有位置，等等。

### [1:10:34](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=4234s) · b000139

然后，你把这个响应反馈给 LLM，以得到最终回答。当你向 LLM 提出某个问题时，你不想得到这种类似 JSON 的响应，而是想要自然语言的回答。这正是最后这个阶段的目的。我在这里暂停一下，确认大家都理解这个三阶段机制。

### [1:11:09](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=4269s) · b000140

好。很好。你刚才提到的，正是我们接下来要关注的重点。这究竟怎么训练？让我问大家一个问题。如果你要训练一个 LLM 来使用这个工具，需要重点关注哪些步骤？

### [1:11:36](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=4296s) · b000141

所以，回答是你会输入 API 的实现。是的。你需要让第一次 LLM 调用以某种方式识别函数实现与查询的模式，并将其与要传入函数的参数联系起来。是的。很好。所以，就是工具预测（tool prediction）。那你还需要第二组监督微调（supervised fine-tuning，SFT）样本对吗？

### [1:12:11](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=4331s) · b000142

最后这个阶段仍然由 LLM 驱动：你拿到工具的回答，需要输出最终响应。

### [1:12:22](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=4342s) · b000143

你可能会说，好吧，LLM 已经见过很多结构化数据，也知道怎样把看到的内容用语言表达出来，这个说法有道理。但通常，你可能希望回答采用特定的格式。所以，你可能也希望有一些 SFT 样本对，按你想要的方式完成这种映射。这就是为什么通常会有这两种 SFT 样本对。如果说得更准确一点，第二种样本对并不只是把 JSON 响应映射成最终回答，而是实际关联截至目前的全部对话历史，让它知道最初的查询是有人想找一只泰迪熊。

### [1:13:06](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=4386s) · b000144

它知道已经发生了一次 tool call，也知道这些结果对应那次 tool call。所以，这个 SFT 样本对的输入会稍微长一点。这样说清楚吗？好。很好。嗯？

### [1:13:29](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=4409s) · b000145

是的。说得很好。问题是，如果我们有更多工具，是不是需要某种工具选择（tool selection），或者更多例子？这是个很好的话题。再过几张幻灯片就会讲到。是的。这种做法会稍微复杂一些。不过，如果你想要一个非常简短的回答：如果采用 SFT 的方式，可以展示包含多个工具的输入。也就是说，你可以把这些都放进 SFT 数据集里。但我们很快就会讲 tool selection。

### [1:14:03](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=4443s) · b000146

很好。还有其他问题吗？

### [1:14:08](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=4448s) · b000147

好。太好了。这就是我刚才提到的。是的，截至目前的对话历史始终是输入的一部分。然后，输出就是你希望 LLM 在那个阶段预测的内容。而且，由于你这里做的是 SFT，所以不会只有一个，而是会有多个这样的例子。你希望这些例子具有多样性，并能代表典型的用户分布。比如，我刚才问的是：找一只我附近的熊。

### [1:14:40](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=4480s) · b000148

这个例子向模型展示了，即使用户没有给出位置，也可以根据用户所在的位置，让位置信息获得依据（grounding）。在其他例子中，你可以给模型其他类型的指令，直接说：我想要那个位置的一只熊。以此教模型去查看——也就是从不同地方为参数寻找依据。你还可以通过改变输入的类型来扩充这些集合，所以不必按那种方式来 worried \[字幕疑误，可能指 worded，即措辞\]。

### [1:15:13](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=4513s) · b000149

你可以采用多轮对话（multi-turn），比如在对话中间提出想要一只熊，等等。好。很好。但这并不是训练模型做到这一点的唯一方式。如今，LLM 的推理（reasoning）能力越来越强。而它们在预训练（pre-training）和初始指令微调（instruction tuning）阶段使用的数据，通常就包含这类代码数据。

### [1:15:44](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=4544s) · b000150

所以，完成这些之后，它们就很擅长操作 Python 代码了。你可能会问自己：我真的有必要教模型如何把查询映射成 function call 吗？这是一个很有意思的观察。如今你会看到，可以省去专门的 SFT 训练，尝试仅通过训练（training）\[字幕疑误，结合下文可能指 prompting\] 来解决这个问题。

### [1:16:15](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=4575s) · b000151

所以，在这里，我们会看到，你实际上可以只用一段说明来代替编写 SFT 内容、然后重新训练模型这件事。有人知道，我们可以怎样得到这样一段说明吗？

### [1:16:38](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=4598s) · b000152

假设我有一个新工具。我有 API。我想让模型使用它。你会怎么做？

### [1:16:52](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=4612s) · b000153

是的，这个想法很好。一种方法是少样本学习（few shot learning）。你只需要在上下文窗口（context window）中展示输入／输出样例。这个想法很好。你完全可以这么做，而且这通常是一种被接受的做法。不过，如果我告诉你，few shot learning 在泛化（generalization）方面存在挑战，因为你需要提供具体的输入／输出样例。所以，它可能适用于某些情况，却未必能泛化到人类语言的整个范围。

### [1:17:29](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=4649s) · b000154

还有其他方法可以解决这个问题吗？

### [1:17:39](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=4659s) · b000155

是的。回答是，让它进行 reasoning。这个想法很好。而要写出一段能让它以合理方式推理的提示词（prompt），非常困难。所以在实践中，你不会自己写。你会拿这些 SFT 样本对，也就是你想要强化的行为，把它们用作某种评估集（evaluation set）。你可以说，好，如果我问这个问题，我希望得到那个 stool call \[字幕疑误，可能指 tool call\]。

### [1:18:13](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=4693s) · b000156

你有一组这样的样本对。然后，你可以运行目前已有的说明，用评估集来评估这些 prompt。这样你会得到一些成功和失败的结果。比如，在 Paris 找一只熊，效果不好。其他一些 prompt 则有效。于是，你得到了一份列表，每个样本都有一个分数。然后，通常可以把这些反馈给一个推理模型（reasoning model），让它替你编写说明。

### [1:18:49](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=4729s) · b000157

这是一个帮你省去这项困难工作的技巧。基本上，就是向模型展示：看，使用当前的 prompt，我们得到了这些结果。为了改善评估结果，你会做哪些修改？通过这个过程，你就能迭代那份详细说明。如果你看看实际结果，会惊讶于它替你编写说明的效果有多好。

### [1:19:19](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=4759s) · b000158

所以，这里要记住的是，我不建议你从头到尾自己写。也许只写个草稿，然后让某个拥有出色逻辑知识、能力很强的模型替你完成。嗯？

### [1:19:51](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=4791s) · b000159

是的。问题是，你刚才提到的属于训练（training），还是推理执行（inference）？它属于训练。也就是你在最开始做这件事。你想要一段固定的 prompt，向 LLM 解释如何使用它，如何使用那个函数。所以，通常你会离线（offline）完成这件事。你离线迭代那段说明，明确说明如何使用 prompt、如何使用函数。然后，在 inference 时，把那段固定说明和函数 API 放在一起，让它对于任何查询都知道该做什么。

### [1:20:24](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=4824s) · b000160

这样说清楚吗？好。很好。这里还有其他问题吗？

### [1:20:35](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=4835s) · b000161

好。太好了。

### [1:20:38](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=4838s) · b000162

我刚才举了一个泰迪熊的例子，它大概属于信息类（informational）。

### [1:20:48](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=4848s) · b000163

也就是，你有一个问题，想请求某个外部 API 来获取相关信息。实际上，你还会看到更多使用场景。刚才有人提到过，模型有知识截止日期（cutoff dates）。假设你向 LLM 询问当天的新闻，通常模型本身无法提供这些内容。你会有一个 API，通过一个也许叫 Search 的工具来获取它。不过，在信息类中，还有其他类型的工具可用。

### [1:21:20](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=4880s) · b000164

例如，whether \[字幕疑误，可能指 weather，即天气\]、股票，还有，让我看看，不过你也有其他类别。例如，如果你想让模型替你做一些计算，可以让模型通过某种推理链（reasoning chain）来算出来。但另一种解决方法是把查询转换成代码，执行代码，然后读出答案。

### [1:21:51](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=4911s) · b000165

这就是为什么 tool call 在计算领域有着广泛的应用。你可以做计算。这里还有另一类可以举出来，就是代表用户采取行动。假设你有一个发送电子邮件的工具，你可以让模型替你发送一封邮件，它能把正确的内容填入邮件头和正文，甚至替你点击 Send，因为 tool API 中包含了与外部世界交互的组件。

### [1:22:33](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=4953s) · b000166

是的。这些只是几个例子，但我想说的是，tool calling 这个领域非常强大。你可以做任何想做的事。实际上，正如你刚才提到的，上下文中不会只有一个 tool API，而是会有多个，因为你的 LLM 并不只是一个用来找熊的 LLM。你可能还想让它做其他事情。也许你想拥抱一只泰迪熊，或者查看泰迪熊的心情，给泰迪熊送礼物，以及其他事情。

### [1:23:11](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=4991s) · b000167

所以，还有很多可能相关的函数可以加入 preamble。只是因为你不知道会需要哪个函数，所以只能把这些全都放进去，以备不时之需。

### [1:23:28](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=5008s) · b000168

这个设定正是你提到的那种：你拥有的不只是一个 API，而是多个。

### [1:23:36](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=5016s) · b000169

有人看出这样做有什么问题吗？

### [1:23:43](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=5023s) · b000170

刚才的意见是，工具太多了。你说得对。通常，如果工具太多，就会出现 Afshine 开头提到的大海捞针（needle in a haystack）问题：某个 tool API 可能会淹没在上下文中，你不太清楚应该使用什么。也许会有很多相互冲突的 API，我们很快就会看到如何克服这个问题。好。很好。我想在这里暂停一下，总结目前讲到的内容，以及存在的一些缺点，一起看看可以怎样弥补这些缺点。

### [1:24:27](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=5067s) · b000171

首先，我们看到，LLM 从只能用普通文字回复你，发展到能够真正与外部世界交互、获取实时信息，甚至扩展计算能力。而且，它以不同于检索增强生成（retrieval-augmented generation，RAG）的方式，克服了 Afshine 提到的知识截止问题。

### [1:24:58](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=5098s) · b000172

所以，你可以把这两种方法看作互补的。是的，从某种意义上说，它们都在尝试做同一件事。但正如这里有人提到的，如果工具更多，上下文窗口中可能就会包含不需要的内容。而且，如果你试图支持太多场景，最终可能在所有场景中的表现都很平庸。这是一个问题。

### [1:25:30](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=5130s) · b000173

即使这不是问题，上下文窗口仍然是有限的。假设有数亿用户使用你的 LLM，想用它做很多事情。你无法同时支持所有人的使用场景，因为你根本不可能把所有这些工具都放进上下文里。

### [1:25:55](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=5155s) · b000174

最后，我提到的这些工具，都是我手写的。每个 LLM 可能都有自己定义和使用工具的方式。稍后我们会看看，是否有办法把工具的定义和使用方式标准化。这些缺点都能理解吗？是的。好。很好。接下来讲 tool selection。

### [1:26:26](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=5186s) · b000175

我们来看看，可以怎样让工具使用（tool use）更具可扩展性。这里我要引用 Google DeepMind 的一篇技术论文，其中使用了一个工具选择器（tool selector）系统。它分两步运行。首先，你有查询，以及一个工具列表，这个列表可以任意大。工具列表只包含 API 名称，也许再加上一两个词说明它的作用。

### [1:27:03](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=5223s) · b000176

你有这个 prompt 和工具列表，然后让 LLM 选择可能相关的工具。这就是为什么那篇技术论文把这个系统称为 tool selector。你甚至可能在文献中看到路由器（router）这个术语。tool selection 和路由（routing）是相似的概念。这里的目标，就是把工具数量限制为那些可能有用的工具。

### [1:27:38](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=5258s) · b000177

第二个阶段，你把所有选中的 tool API 与查询一起放入上下文，只提供这些 API。这是一种可以用来克服同时存在过多工具这一问题的方法。

### [1:28:01](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=5281s) · b000178

大家都认同 tool selection 可能是解决这里这个问题的好方法吗？

### [1:28:14](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=5294s) · b000179

问题是，这基本上不就是 RAG 吗？你可以用 RAG 来做。这个观点很好。但不一定非得用它。你可以让一个 LLM 来完成这项工作，只负责选择正确的工具。你给 LLM 一些指令，让它输出正确答案。你当然可以用 RAG 来做。这确实是个很好的观点。是的。

### [1:28:40](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=5320s) · b000180

大家都理解吗？好。很好。我发现时间过得很快，所以我们会快速讲一下标准化问题。正如我提到的，每个工具的实现，比如你指定工具实现的方式，都可能是针对某个 LLM 定制的。你不会希望这样，因为对于每个 LLM，你可能都得一遍又一遍地重新实现这些工具。

### [1:29:14](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=5354s) · b000181

重复工作并不是你想要的。这就是为什么有一个叫 MCP 的标准，我知道很多人都在谈论它。这是 Anthropic 团队推出的东西，用来标准化向模型开放工具的方式。它是一种协议，叫作模型上下文协议（model context protocol，MCP）。它定义了展示这些工具的标准方式。我只会介绍它的大致内容，让大家了解 MCP 中的这类术语。

### [1:29:53](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=5393s) · b000182

你有一个 MCP 服务器（MCP server），它是提供工具的实例。工具（tools）则是你希望人们使用的函数的实现。提示词（prompts）是一些模板，可以向用户展示如何使用这些工具。然后，所有这些都可以依托资源（resources），也就是可用于完成任务的外部数据库。

### [1:30:25](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=5425s) · b000183

当你使用 MCP server 时，它与你的 LLM 宿主（LLM host）中一块称为 MCP 客户端（MCP clients）的基础设施建立一对一连接。不过，这些可能属于基础设施细节。我想把刚才提到的内容对应到现实例子。我们知道，我们的泰迪熊喜欢读诗。那么，在向泰迪熊推荐诗集这个场景中，你可以设想一个 MCP server，它提供与图书有关的工具。

### [1:30:59](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=5459s) · b000184

这里的 LLM host——既然 MCP 来自 Anthropic，我们就以 Claude 为例。Claude 就是你的 LLM host。你的 MCP server 可能由图书提供方来实现，因为通常他们最擅长提供这类内容。我们可以假设，图书提供方的 MCP server 有查找或推荐图书的工具。这里的 prompts 则可以展示如何查找某个书名，或者根据某种风格，也许根据用户的 test taste \[字幕疑误，可能指 taste，即喜好\] 来推荐它。

### [1:31:42](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=5502s) · b000185

这里的 resources 可以是泰迪熊的个人藏书，也可以是大家购买最多的图书，只是举个例子。好。太好了。现在，我要讲今天这堂课中可能最令人兴奋的部分，也就是智能体（agents）。我们看到了，工具可以让 LLM 变得强大得多。agents 可以看作是在此基础上更高的一层。

### [1:32:16](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=5536s) · b000186

我会先给出一个定义，让我们对这里 agent 的含义达成一致。它是一个代表用户自主追求目标并完成任务的系统。所以，与工具相比，你不仅能执行任务，其中还涉及一些 reasoning。因此，你可以有多轮迭代循环。

### [1:32:47](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=5567s) · b000187

简单来说，这就是 agent 与工具的区别。通常，人们谈到 agents 时，指的就是其中内置了这种循环，或者更高层次的 reasoning。接下来，我会把智能体式（agentic）的世界，与我们已经看到的、可能会多次调用工具的世界作比较。这些新的 agentic 框架与此前介绍的那些并不一定互不相交。

### [1:33:25](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=5605s) · b000188

其中完全可以包含 reasoning chains。所以，它们可能存在重叠。但其结构由 tool calls 和迭代组成。好。很好。现在我要介绍一篇标志性的论文，叫 ReAct，也就是推理加行动（reason plus acts），它把可能的循环拆分成不同阶段。

### [1:33:58](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=5638s) · b000189

很多时候，当你有一个查询，想要达成一个目标时，无法一次完成。你需要以某种方式把目标拆解成可执行的子步骤，逐一执行这些步骤，然后得出答案。这正是 ReAct 的核心：把复杂任务拆解成由可作为原子操作执行的事项构成的循环。

### [1:34:31](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=5671s) · b000190

这里我想说明一点。我们把这些步骤分为观察（observe）、规划（plan）和行动（act）。但它们不一定非得这样命名，也不一定按这个顺序。例如，我记得 ReAct 论文引入的术语是思考（think）、observe、act。不同论文中的用语可能会有些变化，但高层次的直觉是一致的。

### [1:35:02](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=5702s) · b000191

我们来看一个非常具体的例子。为了贴合这几天的天气，天气开始变得有点冷，我们的泰迪熊在家里可能会觉得冷。就把这个作为输入：我的泰迪熊很冷。请做点什么。我们来看看，agentic 工作流（agentic workflow）能对此做些什么。首先，是 observe 阶段，把用户查询转换成一种可执行的表述。

### [1:35:38](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=5738s) · b000192

当你说泰迪熊很冷，并像这里这样要求它做点什么时，在 observe 阶段，你会把这件事关联到温度这个概念。用户的泰迪熊很冷，可能是因为房间当前的温度，而这个温度目前未知。所以，一开始你就知道，需要针对温度做些什么。这把我们带到下一步，叫 Plan：某件事尚不明确，而你需要把它弄清楚。

### [1:36:12](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=5772s) · b000193

Plan 会把它明确表达出来。这里，你想确定房间的温度。幸运的是，在你的工具中，可能有某个工具能完成类似的事情。这就是使用它的时候。所以，Act 阶段就是使用上下文中可能存在的这些 API。例如这里，如果你有 get current room temperature，这就是使用它的方式。正如我提到的，当这些工具把 LLM 能够解释的信息输出回给它时，它们才对 LLM 有用。

### [1:36:47](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=5807s) · b000194

这个工具会返回温度。现在，你需要解释这个温度意味着什么。这就是为什么要回到 observed 阶段 \[字幕疑误，可能指 observe 阶段\]。

### [1:37:02](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=5822s) · b000195

你描述世界现在是什么样，以及应该对此做什么。这里，你可以读到房间温度偏冷，是 65 华氏度，observed 阶段 \[字幕疑误，可能指 observe 阶段\] 可能会指出，这比预期更冷。所以，你需要规划一些事情。然后，在 Plan 阶段，你会想：这，这比预期更冷，所以我需要提高温度。接着，你又回到 Act 阶段。

### [1:37:32](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=5852s) · b000196

幸运的是，如何提高温度。它有一个函数，可以接收温度增量参数，把参数传进去，就能调节温度。完成之后，observed 阶段 \[字幕疑误，可能指 observe 阶段\] 得出结论：温度尚未设为正确温度 \[字幕疑误，原文为 not，结合下文可能指 now，即现在已设为正确温度\]。这时，就可以退出循环，把响应返回给用户。

### [1:38:06](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=5886s) · b000197

这里，我们把温度提高了 5 度。然后，输出会向用户说明这件事，希望已经满足用户的查询。我在循环中描述的这些，就是让一个工作流成为 agentic 工作流的原因。你有一个初始查询，有一些可以执行的动作。然后，在每个阶段，LLM 都会尝试判断自己是否已经达成目标。

### [1:38:39](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=5919s) · b000198

如果达成了，就会进入输出阶段。否则，它可能还会经历更多 reasoning 循环，继续做更多工作。我在这里提出的 agent 定义，大家能理解吗？

### [1:39:00](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=5940s) · b000199

好。很好。再往前一步，你可以设想不止一个 agent。你可以有一个负责设置恒温器的 agent。但在家里，你也许还想管理能源如何分配，或者空气质量，如果有一些设置可以调节的话。所以，你可以有不同的 agents。一个有意思的使用场景是，让用户对一个 agent 说些什么，然后可能让所有 agents 相互交流。

### [1:39:33](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=5973s) · b000200

这就带来了对 agents 之间通信进行标准化的潜在需求，类似于我们看到的 LLM hosts 与工具之间的标准化。这也促使 Google 在今年早些时候发布了 Agent2Agent 协议。是的，非常推荐大家去看看它的规范文档。不过，简单介绍一下，它对 agent 可以开放哪些内容做了一些标准化。

### [1:40:12](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=6012s) · b000201

通常，它会开放一组技能（skills），也就是它能做哪些事情。然后，它会给出相关示例，让其他 agents 了解这些能力。作为开发者，你需要做的就是定义这些 skills。另外一个关键点，是定义 agent 如何执行给定的请求。例如，当你执行某个查询时，会向其他 agents 发出什么状态？

### [1:40:44](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=6044s) · b000202

此外，还有一个 cancel 方法。假设某个 agent 说：停止你正在做的事。那么，取消某个动作的流程是什么？这些就是 Agent2Agent 协议要求人们填写的一些主要函数。嗯？

### [1:41:14](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=6074s) · b000203

问题是，每个 agent 是否都是带有一些上下文、用于完成某些任务的 LLM？你完全可以这样设想。通常，在我这里举的例子中，是这样的。而且，这些 agents 独立运行，各自有自己的 reasoning 循环。而其他 agency \[字幕疑误，可能指 agents see，即其他 agents 所看到的\] 就是输入和输出。

### [1:41:51](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=6111s) · b000204

是的。这里的意见是，你的 token 预算可能会变得难以控制。你可以设置一些预算限制。这个观点很好。但这些 agents 不会消耗彼此的预算。它们可能会消耗你的金钱预算，但这确实是一个需要关注的问题。接下来我要转向安全（safety）这个话题，目前还没有提到过。

### [1:42:23](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=6143s) · b000205

但这非常重要，因为这些新能力会带来一整串新的潜在问题。你们已经看到，这些模型现在能够替你执行动作。所以，你可以想象，某个恶意行为者可能会做一些你不希望发生的事。这里我举一个可能令人担忧的例子：数据外传（data exfiltration）。假设你可以使用一个工具，它能以公开可见的方式写入数据。

### [1:43:00](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=6180s) · b000206

假设你有一个，比如说，电子邮件 agent。如果有一个 prompt，例如说，把我的密码——工具可能能够访问它——写入一封发往那个地址的电子邮件，那么就可能把属于用户的数据外传出去。这通常是你可能面临的一种风险。还可能有其他安全风险。我在这里链接了一篇论文，介绍了其中一些风险。就是 tool sort \[字幕疑误，可能指 ToolSword\]。

### [1:43:32](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=6212s) · b000207

所以，我推荐读一下。

### [1:43:36](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=6216s) · b000208

现在，你可能会问，可以怎样解决这个问题？通常有两类缓解措施（remediations）。一类可以在训练阶段实施。如果你还记得 R1 或其他模型的训练过程，其中包含无害性（harmlessness）部分。所以，在 SFT 和强化学习（reinforcement learning）的训练数据混合中，通常会有一些涵盖安全问题的数据。

### [1:44:11](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=6251s) · b000209

你可以在这里缓解这些问题。还有另一种选择。假设某个查询已经突破了你的防线，也就是训练阶段的防线，你还可以设置推理阶段防护措施（inference safeguards）。例如，安全分类器（safety classifier）会查看截至目前的对话，判断 LLM 的输出是否安全。所以，这也可以作为一道防护。

### [1:44:42](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=6282s) · b000210

另外，提供一个参考方向，我想提一下 agent safety bench \[字幕疑误，可能指 AgentSafetyBench\]，它总结了各种可能的安全隐患，并提供了一个基准测试（benchmark），一整套测试。人们可以参考这些 benchmarks，了解自己的 LLM 是否安全。

### [1:45:08](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=6308s) · b000211

这是一个非常重要的话题。就在昨天，Anthropic 披露，他们遭受了一场通过 Claude 发起的大规模网络攻击。所以，这是一个问题——那次攻击也使用了工具和 agentic 能力。他们发布了一份非常详细的报告，明确说明攻击者做了什么，并逐步介绍可能采取的缓解措施。

### [1:45:40](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=6340s) · b000212

这只是为了强调，在能力更强的这个世界里，安全有多重要。攻击者和防御手段都可能变得越来越复杂。所以，这并不是一场已经输掉的战斗，只是我们用来防御基于工具的攻击的工具需要——也就是说，我们需要落实这类措施。有了这些措施，也许情况就会没问题。

### [1:46:11](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=6371s) · b000213

我想，这就是那篇文章的整体思路，我强烈推荐大家阅读。

### [1:46:21](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=6381s) · b000214

最后再说几句。当你谈论 agents 时，会存在这样一种风险：在思考过程的每一步，都可能偏离到某条行不通的路径上。这是一个大问题。比如，模型没有正确以输出为依据（grounding），或者在预测某次 tool call 的参数时出错，这都是严重问题。这也是为什么我们现在还没有看到大规模 agents 统治世界，因为我们确实受到了这些后果的限制。

### [1:47:01](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=6421s) · b000215

然后，我要谈谈模型不断发展的能力，这些能力让 agentic 能力成为可能。这是可以用 SFT 修复的事情。但理想情况下，你不会希望用 SFT 来弥补 reasoning 上的缺口，而是希望利用模型本身。下周我们会看看评估领域的情况，所以我把这个留到下周。再给大家几句关于构建工具或 agents 的建议：始终从一个非常简单的小场景开始。

### [1:47:41](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=6461s) · b000216

例如，找到最近的熊。先看看你当前的实现和 prompt 是否有效，然后再从那里出发。所以，先从小处着手，再聪明地起步。先使用能力最强的模型，让你知道当前模型能达到的上限，然后再尝试改善延迟等方面。先做正确，从小处开始，之后再优化。

### [1:48:15](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=6495s) · b000217

说到可调试性（debuggability），这些 LLM 会输出 reasoning 链。所以，查看这些内容、看看哪里出了问题，总是有帮助的。最后，我想用一点感想结束这堂课。目前，我最喜欢的 agents 使用场景是作为 AI 编程助手。如果你的项目需要做复杂的衔接工作，我非常推荐这种方式。把其中一些任务委派出去，可以减轻你的脑力负担。

### [1:48:49](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=6529s) · b000218

你会在现实世界中看到，这种方式现在已经得到广泛使用。但要提醒一点：请务必学习代码的基础，知道如何正确编程，因为从现在起，你的判断品味会最重要。生成代码很便宜，但判断代码是否正确、是否做了该做的事，才是困难的部分。就到这里，谢谢大家。\[掌声\]
