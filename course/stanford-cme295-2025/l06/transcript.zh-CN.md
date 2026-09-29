# Stanford CME295 Transformers &amp; LLMs \| Autumn 2025 \| Lecture 6 - LLM Reasoning

_中文讲稿_

- Channel: Stanford Online
- Source: [YouTube](https://www.youtube.com/watch?v=k5Fh-UgTuCo)
- Duration: 1:47:10
- Caption source: manual
- Status: complete
- Chinese translation: 184/184
- Translation provider: codex
- Generated: 2026-09-29T16:13:49+00:00

## 讲稿

### [00:05](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=5s) · b000001

大家好。再次欢迎来到 CME 295 第 6 讲。今天其实是令人兴奋的一天，因为我们要讨论一个过去一年左右一直很热门的话题，也就是大语言模型推理（LLM reasoning）。它也很好地承接了我们上次讨论的偏好调优（preference tuning），因为我们在第 5 讲中用到的许多方法，将成为本讲所使用的基础。

### [00:40](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=40s) · b000002

开始之前，和往常一样，我们先快速回顾上一讲的内容。如果大家还记得，第 4 讲和第 5 讲都是在学习如何训练模型。在第 4 讲，我们讲了第一部分，也就是预训练（pre-training）。这是计算最密集的步骤，我们基本上是在教模型文本的结构、代码的结构。

### [01:16](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=76s) · b000003

我们进行这种非常大、大规模的训练。所以，在第一步，也就是预训练结束时，我们得到一个懂代码、懂语言的模型，但它只知道如何自动补全一个序列。因此，我们还讲了第二步，也就是微调（fine tuning）：拿到预训练模型，尝试让它变得有用。

### [01:46](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=106s) · b000004

例如，我们讲过的一种用例是助手。我们尝试对它进行调优，让它能够回答问题。这里就需要准备监督微调（supervised fine-tuning，SFT）数据，也就是我们所说的 SFT 数据。这是经过精心整理的高质量数据集，可以用来教模型如何表现。因此，在第二步结束时，我们得到的是针对某项特定任务调优过的模型，比如回答查询。

### [02:22](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=142s) · b000005

然后在上一讲，我们讲了第三步，也就是 preference tuning。这里的目标是让模型与人类偏好对齐。具体来说，我们讲了基于人类反馈的强化学习（reinforcement learning from human feedback，RLHF），这是一种常用方法。我们看到它分为两步。第一部分是利用人类偏好数据学习区分好坏，然后第二步是强化学习（reinforcement learning，RL）阶段，这个阶段今天会派上用场。

### [03:05](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=185s) · b000006

具体来说，如果大家还记得，我们做过一个对比，一边是大家可能在本课程之外熟悉的 RL 设置：有一个与环境交互的智能体（agent）。它的交互方式是，在所处的给定状态下，按照某个策略（policy）采取一个动作，而策略其实就是动作上的概率分布。

### [03:41](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=221s) · b000007

所以，在给定状态下，智能体可以按照这个策略采取动作，随后获得某种奖励（reward）。上一讲我们看到，传统 RL 设置与 LLM 设置之间可以做一个很好的对照。这里，我们所谓的“智能体”就是 LLM。它交互的环境，就是它可以在其上进行预测的一组词元（tokens）。

### [04:18](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=258s) · b000008

因此，根据目前收到的输入，它可以预测下一个 token 可能是什么，这就是动作。它利用的概率分布，可以说就是 LLM 预测的结果。我们还看到，可以针对每个补全（completion）获得人类偏好。

### [04:49](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=289s) · b000009

也就是说，你有一个提示（prompt），有一个 completion，然后得到相应的人类偏好。接着，你就用这些偏好来调优 LLM。因为这里这一步的目的，就是让模型与人类偏好对齐。这里，人类偏好体现在奖励中。我们看到，RL 阶段的损失函数（loss function）由两部分组成。

### [05:21](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=321s) · b000010

第一部分是优势最大化（advantage maximization）。我们看到，这个优势（advantage）基于奖励，并带有一个基线（baseline），用于降低梯度的方差。这是一部分。但我们还讲了另一部分：我们不希望模型偏离上一次迭代太多，也就是说，不希望模型在相邻迭代之间变化太大；同时，我们也不希望模型相对于初始模型，比如基础模型（base model），变化太大。

### [06:06](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=366s) · b000011

在这里，它就是 SFT 模型。我们不希望变化太大的原因是，模型已经学到了很多东西，在它所做的事情上已经有相当不错的表现。我们只是想让它与人类偏好对齐，并不希望为此让模型发生彻底的改变。我想，那部分可能有一点吓人，也就是实际的损失函数。

### [06:37](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=397s) · b000012

如果大家还记得，RLHF 设置中通常使用的主要算法是 PPO，全称是近端策略优化（proximal policy optimization）。它有一个变体叫 PPO CLIP，会对相邻迭代之间的更新进行裁剪（clip）。这里，如果大家还记得，R 实际上不是奖励，而是比值。

### [07:09](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=429s) · b000013

这个记号有些容易让人混淆。它是当前策略与旧策略之间的比值。这里的旧策略，就是上一次 RL 迭代时的策略。我们的做法是使用一种裁剪机制，使这个比值不能超出某些阈值，从而避免激励模型做出过大的更新。

### [07:44](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=464s) · b000014

我们还讲了 PPO 的另一个变体，叫 PPO-KL penalty。这个变体使用 KL 散度（KL divergence）来惩罚模型过大的变化。如果大家还记得，在原始 PPO 论文中，我们使用的是所谓的“旧版”模型，也就是上一次 RL 迭代时的模型。

### [08:14](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=494s) · b000015

但在现在的 RLHF 训练中，这个 KL divergence 通常是相对于基础模型，也就是 SFT 模型来应用的。所以，简单来说，我们有这两个 PPO 变体，它们都是原始 PPO 论文中提出的。但在现在的 RLHF 训练中，我们通常会组合、混合使用这两个损失函数。

### [08:50](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=530s) · b000016

可以吗？到目前为止，我们看到的都是我想称为普通 LLM（vanilla LLMs）的模型：接收某个输入，比如一个 prompt，然后直接给出回答。这些 vanilla LLMs 有很多优点。首先，我们已经看到，这些 LLM 非常了解文本的结构，也非常了解代码。具体来说，如果你想调试代码，我想它们很擅长找出错误在哪里。

### [09:25](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=565s) · b000017

它们很擅长生成代码，也很擅长生成文章或诗歌，在这些方面真的非常、非常出色。但我也想指出一些弱点。第一个我想指出的 vanilla LLMs 的弱点，是它们所谓的“推理能力有限”。通常，如果你给出一个复杂的，比如数学问题，它不一定能得出解答，因为它可能会在途中迷失。毕竟到目前为止，我们对模型的训练，主要是在给定 prompt 后，用下一词元预测（next token prediction）来回应。

### [10:18](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=618s) · b000018

所以，我想这里其实没有很充分的理由，能让它具备解决复杂问题的能力。这是一点。第二个弱点是，我们的 LLM 在大量数据上进行了预训练，而这些数据是静态的。这意味着，LLM 学到的知识受限于一个截止日期（cutoff date），也就是我们截取并形成预训练数据时的日期。

### [10:53](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=653s) · b000019

我知道几天前我们举行了一场选举。那么，假如我们的 LLM 是用选举之前的数据训练的，而今天我们问它，比如 X 的当选官员是谁，它就无法回答，因为它无法获取那个日期之后的知识。第三个弱点是，到目前为止，它只会说，不会做。你只是给 LLM 一个 prompt。

### [11:24](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=684s) · b000020

但我想，如果你想，比如说，我不知道，下一个订单，或者不做某个动作，你就有点自己去做了。然后，最后一个弱点——顺便说一下，这并不是一份穷尽所有情况的列表——是，与传统的自然语言处理（natural language processing，NLP）模型相反，LLM 生成的是自由形式的文本。很难用我们——这里的“我们”指机器学习（machine learning，ML）社区——直到几年前一直采用的框架来评估它们。

### [11:59](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=719s) · b000021

如果大家熟悉这方面，比如你做过翻译工作，就会使用 BLEU 这样的基于规则的指标；做摘要时，则用 ROUGE 来评估输出。但这里的 LLM 真正能做的远不止这些，因此很难评估。我想说的是，这只是 LLM 所有可能弱点中的一部分。最后三点，会是我们在下一讲和第 8 讲讨论的话题。

### [12:36](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=756s) · b000022

正如我之前提到的，今天的重点是推理。我们会看看如何改善 LLM 的推理方式。好。再强调一下，这是一个非常新的话题。我说的“新”，是指大约一年。因此，我们将看到的几乎所有内容，都来自 2024 年或 2025 年。我想我们很幸运，因为现在已经有足够的回顾视角，知道哪些部分比其他部分更重要。

### [13:13](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=793s) · b000023

今天的目标是了解什么是推理模型（reasoning models）。第二个主要目标，是了解它们如何训练。希望本讲结束时，如果你能很好地回答这两个问题，就说明我们做得不错。那就从推理模型开始。它们是什么？要回答这个问题，我们首先需要定义一下什么是推理。

### [13:47](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=827s) · b000024

坏消息是，对于什么是推理，目前并没有一个普遍认可的定义。所以，我会尽我所能尝试定义它。这里，我们将推理定义为解决问题的能力。这里所说的问题，通常更多是指数学问题，或者编程问题。不过，希望这些能力也能扩展到其他领域。

### [14:24](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=864s) · b000025

为了解决这个问题，我们通常需要一个多步骤的推理过程。这有点像考试时，遇到一个并不简单的问题，你通常会把它拆成几个步骤，逐步完成，最后得到答案。我想，所谓的推理问题，大致就会有这样的模式。

### [14:56](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=896s) · b000026

为了说明这一点，我们先确保大家想的差不多。一个非推理问题可以是：Stanford 的 transformers 和 LLM 课程的课程代码是什么？这个问题属于知识问题。大家都知道是 CME 295。相对而言，一个基于推理的问题，可能是数学问题。例如，假设有一只熊出生于 2020 年。

### [15:27](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=927s) · b000027

现在是 2025 年，这只熊多大了？这就是我们要研究的那类问题。当然，这个问题非常简单。你可以想一个比它难得多的问题，那也属于这一类。好。现在我们对什么是推理有了一点了解，接下来就看看如何获得一个能够处理这类 prompt 的模型。

### [15:59](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=959s) · b000028

这里的核心想法，是利用我们在课程前面讲过的一个概念。不知道大家还记不记得，大概在第 2 讲或第 3 讲，我们讲过一种叫思维链（chain of thought）的技术。谁还记得 chain of thought 是什么？嗯？好，你愿意说说吗？

### [16:32](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=992s) · b000029

对，完全正确。答案就是分步骤思考，而不是只给出一个笼统的答案。回答得很好。这里，为了说明一下——嗯。

### [16:58](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=1018s) · b000030

哦，对。很好的观点。问题是，有些问题需要一些上下文。例如在这里，你需要让 LLM 知道今年，我不知道，今天是 2025 年 11 月 7 日。对，说得很好。这涉及两部分。对于这个具体问题，LLM 通常有一种我们称为前导信息（preamble）的东西，用来提供一些上下文。

### [17:28](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=1048s) · b000031

日期通常就是我们放进 preamble 的信息。因此，在这个非常具体的例子里，日期是 LLM 已经可以获取的信息。但对于其他一些问题，确实可能存在你没有的信息或上下文。在第 7 讲，我们会看看如何获取这些信息。这肯定会非常有用。不过就今天而言，我们会更多地把它看作推理模型的一种扩展，而不是其工作原理的基础。

### [18:09](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=1089s) · b000032

这一部分，我们下一讲会回答。好。这里我们正要说明 chain of thought 是什么样的。正如你刚才提到的，我们不想只有一个笼统的答案，还想解释推理过程。chain of thought 的做法，是提供一些上下文学习（in-context learning）示例，在示例中明确呈现推理，以鼓励模型在给出答案之前也这样做。

### [18:49](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=1129s) · b000033

这就是大致——不是大致想法，而是 chain of thought 背后的想法。这里，我们想做同样的事，但规模要大得多。我想先建立一个直觉，说明为什么这可能有帮助。LLM 基本上是以 next token prediction 为目标来训练的。

### [19:20](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=1160s) · b000034

因此，它们回答我们提出的问题时，通常会让回答听起来合理，以最大化或优化所要生成的 tokens 出现的概率。如果你向 LLM 提出一个非常难的问题，这个问题出现在训练集中的可能性很小。所以，这里的想法是让 LLM 把问题拆解成可处理的问题，然后依靠训练期间见过的模式，解决所有这些更容易处理的问题。

### [20:06](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=1206s) · b000035

这有点像你们，或者我们当学生的时候。给你一个问题，你会尝试把它与自己知道的、在训练时见过的东西联系起来，比如学习时见过的内容，借此解决问题并找到答案。我想这就是直觉。另一个可以想到的原因是，仔细想想，当你让 LLM 生成更多 tokens 时，其实就是给它更多计算量，因为每一步生成都有一次完整的前向传播（forward pass）。

### [20:47](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=1247s) · b000036

你让它多做几次，就是给它更多计算量。我们还会看到一个叫计算预算（compute budgets）的术语，我想它就是你希望 LLM 在生成回答时拥有的预算，后面会讲到。对，这也有作用。大家对推理模型的整体想法都清楚了吗？嗯？

### [21:19](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=1279s) · b000037

很好。再次确认一下，确保大家都理解：到目前为止，我们所谓的 Vanilla LLMs 以问题为输入，再给出某个输出。而在这里，我们想要的是，给定一个问题作为输入后，不要直接生成答案，而是先思考。

### [21:53](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=1313s) · b000038

这里，可以说我们是通过先输出一条推理链（reasoning chain）来思考，然后再给出答案。因此，LLM 的输出不只是答案，而是推理加答案。正如我刚才说的，这个话题在过去一年非常热门。

### [22:24](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=1344s) · b000039

这里简单预览一下推理模型的发展时间线。推理本身已经被研究了不止一年，但推理模型开始涌现，是从 OpenAI 发布 01 preview \[字幕疑误，可能指 o1-preview\] 开始的。那是在 2024 年 9 月。此后，基本上所有人都在琢磨 OpenAI 是怎么做到的。

### [22:56](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=1376s) · b000040

于是，各家 AI 实验室都在尝试探索，能做些什么来提高模型的推理能力。大家都在研究这个。接着，Google 推出了 Gemini 2.0 flash thinking，我记得是在 12 月发布的。到了 2025 年，DeepSeek R1 论文在 1 月发表，引起了很大轰动，因为他们用一种在论文中实际描述出来的方法，达到了与 OpenAI 相当的推理能力表现。

### [23:44](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=1424s) · b000041

所以，2025 年 1 月是一个重要时刻。此后，其他这些模型也都加入了推理能力。比如 xAI 的一些模型、Anthropic 的 Claudes，以及其他实验室的模型，也包括 Mistral。这条时间线并不完整，只是想让大家看看这些模型有多新。有一点要记住：它基本上始于 2024 年底。

### [24:22](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=1462s) · b000042

好。我知道你们很多人，如果不是所有人，每天都在把 LLM 当聊天机器人使用，比如 ChatGPT 或 Gemini。我想让大家知道，什么时候与你交互的模型是推理模型。所以，我有个问题。前几天我在和 ChatGPT 聊天，我在想：这里用的是推理模型吗？

### [24:52](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=1492s) · b000043

大家怎么看？看着这张截图。嗯？为什么？对，完全正确。这里的关键词是“thinking”。事实上，他们到处都放了这个词。但当这些用户界面（user interfaces，UIs）向你展示思考过程时，他们实际上——并不会展示完整的推理过程。我们后面会讲为什么。不过，他们会告诉你，模型花了时间思考。

### [25:26](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=1526s) · b000044

这个思考时间，实际上就是生成推理链所需的时间。我想，这可能或多或少会花一些时间。比如在 ChatGPT 里，有这个 thinking 选项，还可以从 standard 改成 extended，等等。其他模型也有类似选项。特别要注意，你看到的所谓“思考摘要”（thought summary）并不是原始推理链。

### [25:59](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=1559s) · b000045

它是推理链的摘要。他们这样做的原因——我是说，这只是我的推测——第一，原始推理链从人类角度看，可能并不完全容易理解。第二，作为用户，你可能不想读一页又一页的内容。第三，这也是我们后面会讲的，如果你获得了这些推理链，或许就能用它们训练一个模型，让它也基本上模仿这些能力。

### [26:40](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=1600s) · b000046

所以，这些可能就是通常不展示原始推理链的原因。说到定价，我们已经看到，推理模型的输出不仅是答案，还包括推理本身。因此，你会看到，所有这些应用程序编程接口（application programming interfaces，APIs）实际上也会对此收费。你不一定能拿到完整推理链，但如果查看文档，总会有一两句话说明，实际上会按输出 tokens 向你收费。

### [27:18](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=1638s) · b000047

这些输出 tokens 也包含推理词元（reasoning tokens）。我觉得这一点也值得了解。从用户的角度看，这也会促使我们希望用最少的 reasoning tokens 获得最强的推理能力，因为你不想花太多钱。后面我们会看看如何处理这个问题。

### [27:51](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=1671s) · b000048

这只是一个值得注意的点。好。我们讨论了什么是推理，至少给出了一个尝试性的定义，也看到了推理模型背后的核心想法。现在，我们要讨论人们用来量化推理能力的一些基准（benchmarks）。正如我之前提到的，第一个方面是评估编程能力。这里的目标通常是解决编程问题，或者修复一个 bug。

### [28:27](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=1707s) · b000049

通常的设置如下：给定一个问题，你想生成一个能够通过测试用例（test cases）的解法。如果一个解法通过了所有测试用例，那么它就是一个能用的解法。这就是我们验证生成的回答是否正确的方式。

### [29:01](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=1741s) · b000050

这是编程方面。简单介绍一下有哪些基准。我们有 HumanEval，就是这里的截图、这些截图。我记得它包含 100 多道由人类编写的编程题，这也是它叫 HumanEval 的原因。还有 CodeForces，它来自一个竞技编程网站，你们有些人可能知道。另外还有 SWE-bench，我记得它是一组从 GitHub issues 中提取出来的问题。

### [29:38](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=1778s) · b000051

所以，这些都是真实的实际问题。你会看到，这些推理模型的报告中，通常会给出在这些基准上的结果。这是编程方面。对于数学，目标是解决一个问题。这里的做法是，给定问题，你想得到答案。当然，你会让模型生成一些推理。

### [30:12](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=1812s) · b000052

这里，验证解法是否正确的方法，是像这样解析出答案，然后与某个标准答案（ground truth）比较。通过比较两者，我们确实可以知道模型给出的答案是否正确。你可能会问，好，那怎么解析呢？你可以强制模型——这里的“强制”是指在 prompt 中要求——以一种可解析的方式输出答案。

### [30:49](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=1849s) · b000053

有时，人们会把答案放在某个框里，放在方框括号中。有很多不同的做法。题目大致就是这样：你有一道题，然后可以让模型生成一条推理链和答案。这里还有一个答案，可供比较。我还想补充，现有这些基准中的题目，通常实际上并不那么简单。

### [31:25](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=1885s) · b000054

你会经常看到一个名字，aim \[字幕疑误，可能指 AIME\]。不知道大家是否熟悉，它是一项用于取得美国数学奥林匹克竞赛资格的数学考试。有不少模型会基于它来量化自身表现。还有 GSM 8-K \[字幕疑误，可能指 GSM8K\]，是一类小学水平的数学问题。我想你现在可能会问，好，我们有了这些基准，这很好，但要用什么指标量化我们做得好不好呢？

### [32:09](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=1929s) · b000055

有一个指标你会经常看到，我们现在就来讲，因为它并不那么直观。这个指标叫 pass@k。按照定义，pass@k 试图估计 k 次尝试中至少一次成功的概率。也就是说，假设我们有一道编程题。

### [32:45](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=1965s) · b000056

我们让模型生成 k 个答案。pass@k 就是这 k 个答案中至少有一个通过测试的概率。这样讲明白吗？顺便问一下，为什么要有 pass@k？它为什么有意义？这并不是特别显而易见。你可能会遇到一些用例，能够接受花更多时间生成更多答案。

### [33:26](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=2006s) · b000057

如果你知道这样会增加答对的机会，就可以花更多时间生成更多答案，以得到正确答案。编程这类问题的好处是，你可以检查答案是否正确。因此，这里的想法是，如果某些场景允许你不只生成一个答案，而是生成多个答案，那么多花一点时间、多花一些计算量来生成更多答案，可能是值得的，只要这样能提高其中某个答案正确的概率。

### [34:06](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=2046s) · b000058

我们上一讲讲过一种与此有些相似的技术，Best of n。大家还记得吗？嗯，大概记得。Best of n 是我们上周讲的方法：生成 n 个答案，用奖励模型（reward model）给所有答案打分，然后选出最好的一个。这里可以把它看成同样的做法，只不过我们没有 reward model，而是有一种确定性的、可验证的方法来检查答案是否正确。

### [34:47](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=2087s) · b000059

所以，两者非常相似。接下来我们花几分钟，统一一下对如何估计这个量的理解。嗯。

### [35:07](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=2107s) · b000060

这是个很好的问题。问题是，要不要选择一个特定的温度（temperature）。我有一页幻灯片会讲这个，所以先把你的问题留到几页之后。好。顺便说，如果还有其他问题，我很乐意——关于这个还有其他问题吗？大家都非常清楚了吗？好。我们这里想做的是估计这个概率。但你可能会说，直接生成 k 次尝试，再数一数其中正确的尝试有多少，不就可以估计了吗？

### [35:47](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=2147s) · b000061

但问题是，如果只做 k 次，估计的噪声可能很大，因为纯粹出于偶然，可能一个实例中 5 次有 3 次正确，另一个只有 1 次。所以，你希望估计的方差不要那么大。通常的做法是，不生成 k 个，而是生成 n 个答案。这 n 个答案里，会有 c 个成功，n 减 c 个不成功。

### [36:29](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=2189s) · b000062

这里要问的问题是，在这 n 次尝试中，你想量化 k 次尝试中至少一次正确的概率。也就是说，如果你有这 n 个观测结果，从中选出，比如 k 个，这 k 个中至少有一个通过的概率是多少？

### [37:03](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=2223s) · b000063

这就是问题。时间有点紧，我现在直接推导一下。我想这么做，是因为这个答案不一定显而易见。我不希望大家在不知道它从何而来的情况下，对它的形式感到太意外。所以我们来推导。我们想推导的是，从这 n 个样本中选出的 k 次尝试中，至少有一次正确的概率。

### [37:43](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=2263s) · b000064

为此，我先把它写下来。pass that k \[字幕疑误，可能指 pass@k\]。我们想求它的估计值。它就是 k 次尝试中至少有一次正确的概率。

### [38:14](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=2294s) · b000065

如果你学过概率，有一个很常见的技巧：如果要求至少有一次的概率，可以用 1 减去全部不正确的概率。大家都知道这个技巧吗？我们会用到它。所以，就是 1 减去 k 次尝试全部不正确的概率。

### [38:53](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=2333s) · b000066

到这里都没问题吧？嗯？现在我们来尝试量化这个概率。在这 n 次尝试中找到一次不成功的尝试，概率是多少？你有 n 减 C 次不成功的尝试，总共有 n 个观测结果，所以就是 n 减 C 除以 n。

### [39:29](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=2369s) · b000067

这是第一次，这是第一次不成功的尝试。那么，在已知这一次的情况下，再得到一次不成功尝试的概率是多少？还有 n 减 c 减 1 次不成功的尝试，除以 n 减 1，因为你已经取走了一次。

### [40:01](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=2401s) · b000068

继续这样做 k 次，n 减 c 减 k 加 1，除以 n 减 k 加 1。大家都同意吗？这里，我们量化的是：如果从这 n 个中随机取 k 个样本，所有 k1's \[字幕疑误，可能指 k 个样本\] 都不正确的概率。

### [40:36](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=2436s) · b000069

这里的计算方式，是先计算第一次尝试不正确的概率，再计算已知第一次不正确时第二次也不正确的概率，依此类推，于是就有了这个公式。如果你在概率课上见过，这基本上就是无放回抽样（sampling without replacement）。

### [41:06](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=2466s) · b000070

现在，它的好处是可以用一个很简洁的数学记号表达。对于了解这个记号的人，n choose k 等于 n 的阶乘、k 的阶乘、n 减 k 的阶乘 \[字幕疑漏运算符\]。这是这个量的定义。

### [41:36](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=2496s) · b000071

我们在这里就要用到它。这里有一连串乘积，可以表示成一个阶乘除以另一个阶乘。这里是 n 减 c 的阶乘，除以 n 减 c 减 k 的阶乘。然后这个量也可以用阶乘表示。

### [42:10](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=2530s) · b000072

这里是 n 的阶乘，分子是 n 减 k 的阶乘。大家都认可这里的数学推导吗？我就当大家都认可了。接下来，我们要想办法把上面的表达式凑出来。所以，它等于 1 减去，n 减 c 的阶乘，除以 n 减 c 减 k 的阶乘。

### [42:49](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=2569s) · b000073

再加上 k 的阶乘。然后这里，我们说是这个，k 的阶乘、k 的阶乘除以 n 的阶乘 \[字幕疑误，口述公式可能存在重复或省略\]。这里我用了一个技巧：基本上就是把分子和分母同时乘以 k 的阶乘。于是这里有 1 减去——这是 n 减 c 除以 n。

### [43:28](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=2608s) · b000074

所以，是 n 减 c 选——抱歉，是 n 减 c 选 k，除以 n 选 k。这就是我们对 path at k \[字幕疑误，可能指 pass@k\] 的估计。大家都同意吗？嗯？

### [44:01](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=2641s) · b000075

我推导它的原因是，这个公式看起来可能有点吓人。但它其实很自然，因为只用到了无放回抽样的一些考虑。因此，你会在论文里看到人们使用 pass@k 指标。如果要计算它，这就是应当使用的公式。

### [44:33](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=2673s) · b000076

好。pass@k 的一个特殊 k 情况是 pass@1。pass@1 定义为单次尝试成功的概率。这就是大家熟悉的东西。假设有一个模型生成了一个答案，它正确的概率是多少？如果把 k 替换为 1，你会发现这个公式大大简化。

### [45:07](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=2707s) · b000077

它就只是成功尝试所占的比例，直觉上也很合理。大家都清楚了吗？嗯？很好。现在回答你的问题：温度该怎么设？你说得完全对。当你多次生成这些解答时，一个会影响结果的因素，就是所生成解答的多样性。

### [45:40](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=2740s) · b000078

这确实就是 temperature 的用途。那么，temperature 与 pass@k 之间是什么关系？我们想要低温度、高温度，还是介于两者之间？如果采用非常低的温度，你知道生成的解答会比较好，但不会有多样性。

### [46:11](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=2771s) · b000079

因此，即使增加生成的样本数量，这个量也不会变化。图中 T 等于 0 的曲线就体现了这一点，它没有变化。但当 T 等于 0.2 时，它开始上升，因为有了一些多样性。不过，如果温度升得过高，虽然会得到想要的多样性，却也会损害预测性能，因为原本不太可能出现的 tokens，可能会变得更容易出现。

### [46:46](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=2806s) · b000080

另一端是这里 t 等于 1.2，在这个例子中属于极端情况，并不是最好的。因此，回答你的问题，通常会选择一个不太大也不太小的温度。我记得在这个例子里，t 等于 0.8 在样本数较大时，似乎产生了最好的结果。但这里我觉得不太清楚，也可能是 0.4。所以，你会看到论文中总会注明，为得到基准结果，他们选择了什么温度。

### [47:28](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=2848s) · b000081

因此，记住这一点很有用。这些是人们使用的主要指标，但不是仅有的指标。你还可能看到另一个，叫 consensus at k，也就是选择你生成的结果中出现次数最多的答案。你可以认为，自一致性（self-consistency）技术与它非常相关。

### [48:02](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=2882s) · b000082

所以，你可能会看到它。然后，这些基准里的其他指标，通常就是你熟悉的那些，比如准确率（accuracy）、精确匹配（exact match）等等。第一部分我花了很多时间，我想得加快一点了。不过，到目前为止，大致都明白吗？嗯？现在，希望大家已经了解什么是推理模型。接下来进入本讲最有意思的部分：如何构建这样一个推理模型。

### [48:39](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=2919s) · b000083

我们知道，希望推理模型生成一条推理链。但目前，我们还不太知道如何大规模地做到这一点。这将是这一部分的重点。这里的想法是，通过某种方式激励模型在回答之前生成 chain of thought，也就是推理链。问题在于，编写推理链是一项非常艰巨的任务，尤其是很长的推理链。

### [49:22](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=2962s) · b000084

对于这一点，假如我们翻一翻目前学过的技术工具箱，可能会想，好，可以用 SFT。但 SFT 的问题在于，需要高质量数据，尤其需要把这些推理链全部写出来。假设你没有这些推理链，该怎么办？通常就得从头编写。但这很难。所以，如果我们没有任何推理链，这算是不采用 SFT 的一个理由。

### [50:00](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=3000s) · b000085

第二个原因，或者说第二个事实，是模型的推理方式可能与我们的推理方式不同。因此，人类编写的推理可能并不是教模型推理的最佳方式。这是第二个事实，也是不支持将人类编写的推理链用作 SFT 数据的一个理由。

### [50:34](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=3034s) · b000086

第三个我想说的事实是，我们刚刚看到，这些推理任务有一种非常自然的奖励，而且实际上是可验证的。对于编程，你可以知道它是否能运行、是否通过某些测试用例、是否能够编译。对于数学，如果答案与 ground truth 相同，你就知道它是否正确。因此，你自然就拥有了奖励信号（reward signal）。

### [51:05](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=3065s) · b000087

我们看到有奖励信号，而 SFT 并不是从零开始的好方法。那么怎么办？试试 RL 吧。好在上周我们已经讲了 RL 在 LLM 场景下如何工作，我觉得时机正好。那么，具体怎么做？先提醒一下，我们想教模型解决这些更复杂的问题。

### [51:42](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=3102s) · b000088

我们还想教它在这之前先推理。为此，首先需要一个检查推理链是否存在的奖励。这里，只要检查模型是否生成了推理链即可。比如，可以检查 think 的起始和结束 token 是否存在；你可以指示模型使用这些 tokens 来插入推理链。

### [52:18](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=3138s) · b000089

然后，第二个想要的奖励，是检查它生成的解法是否真的有效。正如我们提到的，对于我们关注的基准，这实际上是可以做到的。对于代码，要检查它是否在所有情况中都能运行。对于数学，只需验证答案是否与 ground truth 相同。这一点也具备了。总之，我们会运行 RL，使用的奖励会结合两项检查：thing tokens \[字幕疑误，可能指 think tokens\] 是否存在，以及最终结果是否正确。

### [53:08](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=3188s) · b000090

我们已经看到，这两项都很容易做到，不需要模型。假设你这么做，假设你基于 search rewards \[字幕疑误，可能指 such rewards，即这样的奖励\] 进行 RL。那么，你会看到一个很好的现象：如果画出模型在我刚才提到的某个基准上的性能，这里是 aim \[字幕疑误，可能指 AIME\]，如果大家还记得，它是数学基准，你会发现，随着 RL 步骤推进，模型在这些基准上的性能确实会提高。

### [53:46](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=3226s) · b000091

而且提高得相当显著。这里的图实际上来自 DeepSeek R1 的训练——准确说，这里是 R1-Zero。我们会和 Shervine 一起更详细地看看它到底如何工作。但你可以看到，只要激励模型思考并给出正确答案，它就能仅凭这两个可验证奖励，学到相当有意义的东西。

### [54:19](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=3259s) · b000092

但你可能会想，假设我在教模型思考，可并非所有 prompt 都一样。有些 prompt 不需要模型思考太多，而另一些则需要一些思考。所以，社区里已经有很多工作在研究如何控制模型的思考量。

### [54:51](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=3291s) · b000093

你会看到动态预算（dynamic budget）之类的工作：如何确保模型在不需要太多思考的问题上不过度思考？为此，可以使用一个快速分类器（classifier），对 prompt 进行判断，告诉你它属于需要大量思考的问题，还是只需少量思考的问题。不过，这更多还是一个开放问题。但这可以是一种解决方案。

### [55:24](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=3324s) · b000094

第二点是，这些 LLM 的上下文窗口（context window）是有限的。因此，LLM 思考时，还需要意识到剩余的上下文长度有多少。由于这个限制，它也不能思考太多。所以，还需要这种上下文感知能力。已经有一些工作尝试强制模型多思考一些，或者停止思考。

### [56:00](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=3360s) · b000095

有一个术语叫预算强制（budget forcing），我记得是在 S1 这篇论文中提出的。这里的想法是，如果希望模型继续思考，就在中途插入一些 tokens，迫使它多想一会儿。例如，这样的 tokens 可以是 weights \[字幕疑误，可能指 wait\]。“我觉得还有另一种解法。”实际上，有一页幻灯片我还没有真正讲过。看看这条推理链，有时模型会输出类似这样的话：“哦，等等，等等，等等，我想我发现了别的东西。”

### [56:36](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=3396s) · b000096

通常，模型就会再次沿着另一种推理路径走下去。这可以是激励模型多思考的一种方式。或者也可以用另一句话：“好，时间到了。现在我的答案是”，这样就会强制模型回答。另外，仔细想想，模型在推理链中给出 tokens，但模型也可能在其他空间里思考，未必是在语言空间里。

### [57:16](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=3436s) · b000097

因此，还有一条研究路线是连续思维（continuous thoughts）。基本上，就是让这些思考 token 实际上不再是 tokens，而是隐藏表示（hidden representations），它们可能更有意义，也更紧凑。相关论文有不少。我们链接了一篇，实际上来自 2024 年。但我想，就在几天前，我还看到另一篇相关论文。所以，这是一个非常活跃的研究领域。

### [57:49](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=3469s) · b000098

就这样，我们看到，想要扩展模型能力，可以使用 RL。大家都被说服了吗？这些论点说服大家了吗，还是有人对此有问题？这里，我希望大家记住一点：如果从零开始，也就是没有推理链，我们希望用 RL 来激励模型更多地思考。

### [58:27](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=3507s) · b000099

大家对此都没问题吗？嗯？算是吧，嗯。那我就当大家同意了。现在我们来看执行这个 RL 步骤所用的算法。你可能经常听到这个缩写。我们要讲的算法叫 GRPO。GRPO 于 2024 年发布。

### [58:58](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=3538s) · b000100

它已经成为所有这些推理任务，或者说推理训练任务的首选 RL 算法。那么，什么是 GRPO？GRPO 的全称是组相对策略优化（group relative policy optimization）。它是一种 RL 算法，与 PPO 很相似，目标是完成我们讨论过的两件事。

### [59:29](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=3569s) · b000101

第一件事是最大化 advantage。如果大家还记得，advantage 会告诉你，所生成的答案是否比预期更好。这是第一部分。第二部分是，你不希望偏离旧模型太多，也就是上一次迭代时的模型；也不希望偏离基础模型太多，也就是 SFT 阶段的模型。

### [1:00:10](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=3610s) · b000102

因此，从这个意义上说，GRPO 与 PPO 做的是同样的事。但有一个关键差异，差异在于它如何计算 advantage。如果大家还记得，PPO 估计 advantage 时，会使用 completion 级别的奖励。也就是说，你有 prompt，然后有一个回答，一个完整的回答。

### [1:00:40](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=3640s) · b000103

接着，根据这两个元素，得到一个奖励。PPO 会考虑这个奖励，同时考虑另一个在训练时联合训练的东西，叫价值函数（value function）。value function 的目标，是尝试预测：如果继续按照策略生成 tokens，奖励会是多少。

### [1:01:14](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=3674s) · b000104

如果大家还记得，在 PPO 中，advantage 实际上是根据一个非常复杂的公式得到的，我们其实没有讲那个公式。它叫广义优势估计（generalized advantage estimation），是一种估计这些 advantage 的方法。它的一个重大局限是，你必须把 value function 与策略一起训练。这是一个很大的瓶颈。

### [1:01:45](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=3705s) · b000105

相比之下，GRPO 说，我们不这么做。我们拿一个 completion，计算各自的奖励，再把它与同一个 prompt 下各个 completion 的平均奖励进行比较。我举个例子。假设有一道数学题。这里的做法是，为同一个 prompt 生成多个 completions。

### [1:02:25](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=3745s) · b000106

然后，对每组 prompt 和 completion——prompt 是共享的——也就是说，对每个 completion，我们要衡量其奖励相对于其他所有 completions 奖励的某种相对量。这就能让我们知道，它比组内其余结果好多少或差多少。

### [1:02:56](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=3776s) · b000107

这就会成为我们的 advantage。这里最大的好处是，不使用 value functions。我们不用它。我们唯一要做的，就是不只采样一个，而是采样多个 completions，以计算这一组奖励的平均值。这样讲明白吗？

### [1:03:29](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=3809s) · b000108

哦，对。那你会怎么做？问题是，为什么要这样做？供大家参考，传统 RL 算法是在这些 LLM 兴起之前开发出来的。比如，PPO 我记得是 2017 年的方法。

### [1:04:03](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=3843s) · b000109

所以，这些量在某些设置中可能很有意义，但在语言领域未必如此。这里的想法是，尝试找一个量，仅从相对意义上告诉你 completion 有多好。我想，作者在这里希望避免训练一个代价非常高的联合模型，转而寻找另一种相对的做法。

### [1:04:36](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=3876s) · b000110

我认为，这就是高层次的直觉。这里的想法是，多次采样，看看一个回答与其他回答相比如何，然后把这用作某种 baseline，为奖励提供参照。例如，你可能有一道比较简单的数学题。如果它得到了很高的奖励，可能只是因为题目本来就简单。

### [1:05:11](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=3911s) · b000111

但如果是一道非常难的题，而你得到了正确答案，那么你就希望确保激励模型，更大幅度地提高这些 tokens 的权重，因为找到的是难题的一个好解法。所以，你希望把这一点以某种方式纳入 advantage。这就是直觉。GRPO 是一年前开发的，而一年前，LLM 已经无处不在了。

### [1:05:43](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=3943s) · b000112

因此，从某种意义上说，它也考虑了我们要激励 LLM 去做什么。对，我会这样理解。有帮助吗？好，好。对此还有其他问题吗？即使有问题也不用担心，因为我们会一步步讲解它具体如何工作。这里，我们会再次讲同样的过程，不过用图来说明。

### [1:06:15](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=3975s) · b000113

在 GRPO 中，我们拿到一个查询（query），把它传给策略模型（policy model），也就是正在尝试训练的 LLM。我们刚才说过，要生成的不是一个，而是多个 completions。假设是 g 个 completions。每个查询与 completion——因此，你有 g 个这样的配对。

### [1:06:49](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=4009s) · b000114

把它们传给 reward model，就会得到 g 个奖励。你想计算 advantage，让这些奖励都有相对的参照。我们说过，基本上是奖励减去平均值，但实际上并不完全如此。他们的定义是，奖励减去平均值，再除以这些奖励的标准差（standard deviation）。顺便说，我们会看到，这可能不是最好的做法，不过稍后再讲。

### [1:07:22](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=4042s) · b000115

然后，我们用这些 advantage 来调优 policy model。在这个过程中，当然也不希望偏离参考模型（reference model）太多。因此，这里也有一个 KL divergence 项。这就是 GRPO。现在，我们来看看 PPO 中具体是怎么做的。对于 PPO，如果大家还记得，你有一个 prompt。

### [1:07:55](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=4075s) · b000116

你有一个 query，把它传给 policy model，只得到一个 completion。然后把 prompt 和 completion，也就是这一对，传给 reward model，就会得到针对整个 completion 的奖励。这里有一点上次没讲，更偏向实现细节：我们还有一个 KL divergence 项，用来比较每个 token 的概率与 reference model 给出的该 token 概率。

### [1:08:39](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=4119s) · b000117

从实现角度来说，我们通常也会把它纳入奖励。因此，会有一种逐词元奖励（per token rewards），其中只有最后一个 token 带有整个 completion 的奖励，但每个 token 也都有一个 KL divergence 项。这里不必特别记住这一点，不过知道大家是这样实现的也有好处。

### [1:09:10](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=4150s) · b000118

得到这些奖励之后，你还有一个 value function，它也是逐 token 的。它试图量化：如果继续按照策略生成序列的剩余部分，奖励会是多少。我们还提到过一种不会展开讲的方法，叫 generalized advantage estimation，它接收这两个量并计算 advantage。

### [1:09:45](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=4185s) · b000119

你可以把它看成某个复杂公式。得到 advantage 后，就用它来调优策略。就是这样，相比这个方法要复杂一些。因此，在 GRPO 中，使用的 advantage 来自这种组内计算；而在 PPO 中，advantage 来自奖励和 value function，是逐 token 的。

### [1:10:20](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=4220s) · b000120

嗯？那么，这里涉及哪些模型？我们用到的一些模型是所谓“冻结”（frozen）的，也就是不参与训练的模型。对于 GRPO，有一个用于计算 KL divergence 的 reference model，还有一个之前已经训练好的 reward model。PPO 也是如此。

### [1:10:52](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=4252s) · b000121

现在，有一点要注意，在推理（reasoning）的情况下，我们实际上不训练奖励模型（reward model），因为我们知道如何判断一个解答是否正确。我们实际上有可验证奖励（verifiable reward）。所以在推理的情况下，我们实际上完全没有奖励模型。两者在这一点上相同。不同的是我们训练的模型。在 GRPO 的情况下，我们只训练策略模型（policy model）；而在 PPO 的情况下，我们训练策略模型和价值函数（value function），也就是价值模型（value model）。

### [1:11:36](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=4296s) · b000122

这就是关键区别。到目前为止，我们看到的都只是图画和示意图。现在来看一些数学。上面是 GRPO 的损失函数（loss function），下面是 PPO 的损失函数。它们看起来很吓人。但我们会一起看看其中的一些相似之处和不同之处。

### [1:12:07](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=4327s) · b000123

那么，相似之处是什么？两者都作用于当前策略（current policy）的概率与旧策略（old policy）的概率之比。这是第一个共同点。第二个共同点是，两者都试图把更新限制在某个范围内，不要太宽。

### [1:12:40](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=4360s) · b000124

它们通过我们上一讲看到的裁剪机制（clipping mechanism）来做到这一点。所以我建议你们再看看我们一起看过的这些图。当优势（advantage）为正时，损失是什么样子。以及当 advantage 为负时又是什么样子。这个裁剪函数就是让你不要做出太大、幅度太宽的更新。但现在，区别是什么？

### [1:13:11](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=4391s) · b000125

在 JPO \[字幕疑误，可能指 GRPO\] 的情况下，KL 散度（KL divergence）实际上是目标函数（objective function）的显式组成部分。而在 PPO 的情况下，KL divergence 通常是 advantage 的一部分。这更多是一个技术细节。但几分钟前我提到过，从实现角度来看，我们通常把 KL divergence 纳入计算 advantage 时所考虑的奖励中。

### [1:13:51](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=4431s) · b000126

这是一个区别。第二个区别是计算 advantage 的方式。我们看到，在 GRPO 中，我们通常为每个补全（completion）计算奖励，然后将它们与组内其他 completions 进行比较。而对于 PPO，我们使用奖励和价值模型。到目前为止都还好吗？我想我还有一些其他内容要讲。

### [1:14:23](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=4463s) · b000127

但在那之前，我想先让大家提问，看看有没有人有问题。顺便说一句，这部分技术性很强。非常强，可能是整门课最难的部分。所以，我想，花一些时间来消化是完全正常的。如果没有人有问题，我反而会觉得这对我来说更像是个警报，因为这可能——我不知道。所以让我……看看有没有关于这部分的问题。

### [1:14:54](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=4494s) · b000128

对，任何问题都完全可以提。一切都非常清楚了吗？非常清楚？你们只要告诉自己，这些算法就是用来在强化学习（reinforcement learning，RL）阶段调整模型的。PPO 在偏好调优（preference tuning）框架中被大量使用，在这个框架里，你会尝试调整模型，使它与人类偏好对齐，而且也常用于这些基于推理的训练。

### [1:15:36](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=4536s) · b000129

所以我觉得，如果你这样告诉自己，就算理解了一些东西。然后，你需要告诉自己的第二点是，GRPO 与 PPO 的区别在于 GRPO 不需要价值函数。它实际上通过将奖励与其他 completions 的奖励进行比较来计算 advantage。而 PPO 则接收奖励，接收价值，然后比较两者来得到 advantage。

### [1:16:08](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=4568s) · b000130

如果这些能理解，我觉得就已经很好了。所以这些能理解吗？可以吗？

### [1:16:20](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=4580s) · b000131

我也建议大家回看录像。我们正在录制这节课。这部分内容很繁重，也可能很技术化。所以我觉得多回看几次会有帮助。我们还有 11 分钟，然后就交给 Shervine。现在我们要看的是，大家在过去几个月里对去年完成的 GRPO 工作做出的一些扩展。

### [1:16:50](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=4610s) · b000132

这项研究可以追溯到 2025 年初，不过它已经获得了足够多的关注，值得我们在这门课上讨论。如果你们还记得我在这节课开头说过的内容，作为用户，你们需要为推理词元（reasoning tokens）付费。所以你不想付很多钱。不想付太多。你希望模型做你想让它做的事情，但又不希望它生成太多内容，以至于你要为这些内容付费。

### [1:17:26](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=4646s) · b000133

而且从提供方的角度来看，我想，效率更高也好得多。所以大家有动力去看看，从输出长度的角度能优化什么。如果你观察这些模型的训练，你会注意到一点：随着 RL 阶段的训练进行，输出长度会增加。

### [1:17:56](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=4676s) · b000134

这张图展示了每条回复的平均长度随 RL 步数的变化。所以从经验观察来看，大语言模型（large language model，LLM）输出的回答越来越长。这主要源于推理链（reasoning chain）变得越来越复杂。当你把这张图与模型性能的提升情况作比较时，会看到这里的长度增加实际上与性能提升相关。

### [1:18:40](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=4720s) · b000135

你可能会说，好啊，这很好。但接着会到达这里的某个阶段，性能——也就是左边的图——模型的性能趋于稳定，但输出长度仍在继续增加。因此，很多人看了这些图后会说，好，这里面有些情况。所以接下来，我们要看看这种现象，以及人们如何尝试缓解它。

### [1:19:19](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=4759s) · b000136

先小小提醒一下——这部分也有一点技术性。请大家耐心跟着我。有一个公式，我会尽我所能解释清楚。但这里确实会涉及一些数学。为了理解发生了什么，我们需要看看 GRPO 的损失。这个损失就是我刚才在这里提到的那个。它看起来像一个很复杂的公式，但其实并不复杂。我会用通俗的话解释它的意思。

### [1:19:53](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=4793s) · b000137

GRPO 的 J——J 表示目标函数。GRPO 的目标函数就是最大化这个量，它取决于你的模型相对于旧模型改变了多少。也就是幻灯片上看到的这些比值。然后有这个 clipping 机制，防止更新幅度太大。右边还有 KL divergence，防止你的模型偏离基础模型（base model）太远。

### [1:20:32](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=4832s) · b000138

也就是参考模型（reference model）。然后这里和这里有这些求和。它们对应于对组内所有 completions 都执行这个过程。因为请记住，如果有一个提示（prompt），你会多次采样，得到多个 completions，然后对输出中的每个 token 都执行这个过程。所以这里，第一个求和遍历组内的索引。

### [1:21:05](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=4865s) · b000139

第二个求和遍历序列中 token 编号对应的索引。那么这里，我想我们先想一下，如果我们交换——我不确定你们有没有看清我刚才做了什么。我只是把 1 除以第 I 个输出的长度这一项移了一下。把它移到了这里。我会解释为什么这样做。如果你看这里，这个因子只取决于你处于哪个输出中。

### [1:21:45](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=4905s) · b000140

如果你处于一个很长的输出中，这就是 1 除以一个很长的输出长度。它会是一个很小的数。如果输出很短，就是 1 除以一个很小的数。它会是一个很大的数。

### [1:22:04](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=4924s) · b000141

而它右边的这一项是特定于 token 的。换句话说，一个 token 对目标函数的贡献取决于它所在的输出。因此，如果这个 token 在一个短句中，它的权重就会比在一个长句中更高、更大。

### [1:22:36](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=4956s) · b000142

到目前为止，大家都同意我说的吗？是吗？那么，我再换个说法重复一下刚才的话：如果你在一个短句中，你的权重就会比在一个更长的句子中更大。现在我们试着从 advantage 的角度想一想。

### [1:23:08](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=4988s) · b000143

如果一个 token 所在输出的 advantage 为正，这意味着我们希望提高这个 token 再次出现的概率，而且短句中的提高幅度要远大于长句。同时，你希望，在 advantage 为负时——其实不是说你希望。

### [1:23:40](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=5020s) · b000144

只是这个公式会让短输出中的 tokens 相比于长输出中的 tokens 被更大幅度地下调权重。这就是问题所在。这是一种不好的激励，因为你实际上在告诉模型，一个短的糟糕句子比一个长的糟糕句子更糟。

### [1:24:16](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=5056s) · b000145

这就是这里的意思。我再换个说法重复一下我们到目前为止说的内容。除以输出长度这件事，会激励模型对 tokens 进行更大幅度的降权。如果 token 在一个短输出中，相比于它在一个长输出中，它会被更大幅度地降权。换句话说，你这样做会更偏好较长的糟糕输出，而不是较短的糟糕输出。

### [1:24:51](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=5091s) · b000146

人们猜测，这正是让输出长度越来越长的原因。我们马上就会看到。所以人们采取了措施。对于这个 1 除以 o 的长度，人们想做点什么。3 月有一篇论文发表，叫 DAPO——现在相当热门的一篇论文——它实际上让这些 token 层面的贡献变得一致。

### [1:25:26](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=5126s) · b000147

这里，这个归一化因子（normalization factor）现在对所有 tokens 都是相同的。还有另一篇论文，叫作——我记得是 GRPO done right。但它叫 Dr. GRPO，所以我不确定应该怎么念。那篇论文实际上提出把这个因子完全去掉。当你这样做时，如果比较 GRPO 和让 token 层面的贡献一致的方法，你会看到，如果把奖励画成输出长度的函数，模型就会停止不断增加输出长度。

### [1:26:14](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=5174s) · b000148

如果再深入看看，正确样本的长度实际上与 GRPO 的相当。但对于错误解答，这里经过修正的策略所产生的平均长度远低于 GRPO。也就是右下角的图。这实际上产生了——这个调整实际上产生了预期的效果。

### [1:26:51](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=5211s) · b000149

所以这是一个非常重要——我觉得非常重要——一个大家通常会采用的重要修改。我看一下时间。接下来一分钟里，我会简单讲讲大家做的其他一些修改。有一种修改针对 advantage 公式里的标准差（standard deviation），它会在题目难度方面产生偏差。

### [1:27:26](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=5246s) · b000150

因为假设你有一道很难的题，大多数 completions 可能都会失败。因此，标准差不会特别大。这可能造成问题。还有另一种人们通常也会考虑的修改，就是使用不同的 epsilon。如果你们还记得，epsilon 会影响从一次迭代到下一次迭代时，策略能够改变多少。

### [1:28:03](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=5283s) · b000151

这里的想法是，如果 token 的概率非常低，只给它一个很小的 epsilon 来增长，就有点不公平，因为这个 epsilon 是以乘法方式起作用的。我把它写下来。然后就交给 Shervine——这个在哪儿？

### [1:28:30](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=5310s) · b000152

我们实际上希望 pi 除以 pi all \[字幕疑误，可能指 pi old\] 的比值大致处于这些边界之间，大致如此。换句话说，就是 1 加 epsilon，再乘以旧的 pi。如果这一项很低，你就无法让数值改变太多。

### [1:29:02](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=5342s) · b000153

而你又不希望 epsilon 太高，因为你不希望很大的概率突然变成 0。所以你要让下界和上界之间存在不对称。这部分内容很多。对此有什么问题吗？我们时间不多了。课后还会有一些时间，大家有问题可以问。那么，我把时间交给 Shervine。

### [1:29:40](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=5380s) · b000154

谢谢 Afshine 讲完了所有难的部分。接下来会稍微容易一点，因为我们会看看所有这些内容如何结合起来。具体来说，我们会重点看 DeepSeek 的论文，以及他们究竟如何使用 Afshine 讲过的这些技术来构建推理模型。我们在前几讲中看到的，是所谓的“传统”LLMs。你从一个预训练的基础模型开始，在大量互联网文本上进行下一个 token 预测（next token prediction）。

### [1:30:17](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=5417s) · b000155

然后在此基础上，继续进行对齐（alignment），其中包括监督微调（supervised fine-tuning，SFT），再接着是 RL。这里不是推理式的 RL，而是常规的 RL。其中 SFT 就是指令微调（instruction tuning）。我们会看看这些较新的模型是如何训练的。我觉得 DeepSeek R1 论文是一个很好的例子，因为他们分了多个阶段。首先展示，如果应用 Afshine 提到的可验证奖励，RL 阶段可以有多强大。

### [1:30:57](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=5457s) · b000156

然后，根据观察到的性能，设计一套完整的流水线（pipeline），得到一个他们称为 R1 的超级强大的模型。也就是分别做一个概念验证（proof of concept），再做一个完整的推理模型。这样可以吗？好，很好。现在就从 DeepSeek 团队用于 R1-Zero 模型的方案开始。

### [1:31:28](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=5488s) · b000157

他们首先从一个预训练模型开始，这个模型采用最新的架构，配备各种功能，通过 next token prediction 进行训练。回想前几讲，我们讨论过混合专家（mixture of experts）。他们采用了这个架构，还复用了一个叫 multi-latent attention、MLA \[字幕疑误，可能指 Multi-head Latent Attention\] 的技巧，这是他们在 DeepSeek V2 中引入的。我们也讨论过它。

### [1:32:01](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=5521s) · b000158

你们可以看到，在他们的架构中，Transformer 块使用了前置归一化（pre norm）。所以他们有一个典型的 Bayes LLM \[字幕疑误，可能指 base LLM\]。他们对它进行 next token prediction。然后，有趣的部分就开始了。他们没有继续采用包含 SFT 的对齐策略，而是直接从这个仅通过 next token prediction 训练的预训练模型开始。到这时，它还没有接受过任何监督。

### [1:32:32](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=5552s) · b000159

他们在推理数据上应用了 Afshine 刚才提到的技术。他们关注奖励。他们对模型的全部激励，就是根据输出，比如模型给出的输入答案，以及格式，来提高奖励。如果你有 Afshine 提到的 think tokens，那么就会获得格式方面的奖励。

### [1:33:09](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=5589s) · b000160

论文给出了他们用于训练模型的确切模板。这个模板非常简单。开头几句话设定场景，说，嘿，你正在和用户讨论，你是一个助手。然后用普通文本解释我刚才提到的格式奖励。它说，你想思考什么就尽管思考，但要把它放进 think 框里。

### [1:33:42](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=5622s) · b000161

当你准备好给出答案时，应该把它包在类似 answer 的——基本上就是你的 answer 块里。这里红色的内容，就是要用示例 prompts 替换的部分。最后，给模型一个回应的机会。这样能理解吗？好，很好。

### [1:34:13](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=5653s) · b000162

我会再给大家看一张 Afshine 展示过的图。这是在 R1-Zero 上做的实验，他们表示，不需要任何先前的监督，只用这些作为奖励，就能提高基于推理的基准测试（benchmarks）分数。我记得这个是在 AIM \[字幕疑误，可能指 AIME\] 上，是那个数学测试。你会看到准确率随时间提高。你可能会想，一切都解决了，太好了，不需要 SFT，我们就已经达到了可能的最佳性能。

### [1:34:48](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=5688s) · b000163

但事情没那么简单，因为作者查看推理链时，发现了两类问题。首先，当模型在思考——在输出 distinct tokens \[字幕疑误，可能指 think tokens\] 时，有时会混用语言。还存在语法问题。你可以猜测，这可能是因为在此之前，它没有真正接受过任何强监督。

### [1:35:20](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=5720s) · b000164

你给模型机会，让它优化任何它想优化的东西，但它实际上没有一个强监督信号作为背景依托。这是一个关键挑战，我们会一起看看他们如何尝试解决它。R1-Zero 的流程能理解吗？太好了。

### [1:35:51](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=5751s) · b000165

现在我们已经看到了 R1-Zero 想证明什么，也就是仅用 RL 就能获得推理层面的性能，接下来看看如何针对我们看到的挑战进行调整，形成一套完整的 pipeline。他们把它叫作 R1。他们从同样的基础开始，也就是从 V3 base 开始，这是 DeepSeek 在 V3 论文工作期间训练的预训练模型。

### [1:36:22](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=5782s) · b000166

这是该模型的非推理版本。他们从它开始。然后，他们没有直接进入我们讨论过的 RL 阶段，而是尝试以一种能够较好缓解上述问题的方式对它进行对齐。首先使用他们所谓的冷启动数据（cold start data）。他们生成了思维链（chains of thought，CoTs）。

### [1:36:57](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=5817s) · b000167

这些 CoTs 是在 R1-Zero 阶段生成的，而且有时存在问题。因此，他们让人工重写其中一些，使这些 CoTs 在格式和语言一致性方面都符合要求。然后，他们使用这些配对，也就是 prompts 和重写后的 prompts \[字幕疑误，可能指重写后的回答或 CoTs\]，作为数据来进行 SFT。我记得没有给出这一阶段所用样本的数量。

### [1:37:33](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=5853s) · b000168

但从论文的措辞来看，它可能比我们看到的其他一些阶段少几个数量级。所以输入输出对的数量可能在 \[听不清\] 的情况。这个阶段准备好之后，他们继续执行 R1 0 所进行的 RL 阶段。接下来我们会探讨他们使用的奖励函数（reward function）。

### [1:38:04](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=5884s) · b000169

我们不仅有基于推理模型输出的、我们所希望得到的回答的可验证奖励，还有格式奖励。他们还引入了一个新东西，用来应对思考内容可读性差的问题。它叫语言一致性奖励（language consistency reward），他们用一个非常简单的启发式方法（heuristic）来评估模型是否确实没有混用语言。

### [1:38:43](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=5923s) · b000170

我记得它是输出思维链中目标语言 tokens 的比例。他们加入这一项，是为了最大化正确语言的 tokens 数量。

### [1:39:00](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=5940s) · b000171

很好。在第一轮 RL 之后，他们用一个非常有意思的策略继续做 SFT。这次的规模比冷启动阶段更大。现在他们把推理数据和非推理数据混合起来，让模型能够处理用户可能请求它完成的各种场景。对于非推理数据，他们复用了一部分曾用于 V3 非推理版本模型的数据。

### [1:39:42](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=5982s) · b000172

大约有 200k 对数据。它覆盖了我们在 instruction tuning 那一讲中提到的领域，也就是很广泛的主题。然后，他们又加入了大量面向推理的数据对。比例是 3 比 1。其中，推理数据是用一种叫拒绝采样（rejection sampling）的方法生成的。

### [1:40:13](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=6013s) · b000173

他们选取了一些覆盖这些推理领域的 prompts，并使用训练到当前阶段的模型生成回复。然后，根据输出，并借助某种评判者（judge），保留一些答案，拒绝另一些答案，让最终得到的数据集质量非常高。这就是他们所说的 rejection sampling。

### [1:40:44](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=6044s) · b000174

也就是把所有不完美的答案过滤掉。我想，他们使用一些 LLM 评判者（LLM judges）等来自动完成这件事，是考虑到数据规模——而这些启发式方法在这方面效果相当不错——你有问题吗？没有？完成这些之后，他们进入最后一个阶段，这个阶段可能会让你想起非推理模型训练 pipeline 中的那些阶段。

### [1:41:30](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=6090s) · b000175

这次他们不仅混合了推理数据，也混合了非推理数据。对于推理数据，使用与我们见过的相同类型的奖励。但对于非推理数据，会尝试让模型对齐那些使 LLM 成为有帮助且无害的助手的特征。因此，这部分奖励包含有帮助性（helpfulness）和无害性（harmlessness）两个组成部分。

### [1:42:01](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=6121s) · b000176

无害性奖励应用于所有输出的 tokens，而不只是输出答案，因为你确实希望答案中 think 部分的思维链也是无害的。而有帮助性奖励则更关注用户层面看到的内容。好，很好。为了让大家对他们得到的结果有个概念，首先，你会注意到，

### [1:42:40](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=6160s) · b000177

在基于推理的 benchmarks 上，会出现两簇结果。所有这些非推理模型都有一定的性能。而推理模型的性能要高得多，这并不令人意外。我们从这些结果中观察到的第二点是，相比那些声称基于推理的闭源模型，R1 相当有竞争力。

### [1:43:10](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=6190s) · b000178

正如 Afshine 提到的，能够复现这样一个性能水平，是一个相当有意思的时刻。好，很好。我想用一个有趣的话题结束这节课：假设你手头没有一个 600B MOE。假设你有一个较小的模型，但你想让它拥有这些大型推理模型的能力。

### [1:43:43](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=6223s) · b000179

你会怎么做？我想提醒大家，几讲之前讨论蒸馏（distillation）时，我们是如何处理这个问题的。那时我们只是在讨论预训练（pre-training）和 instruction tuning，我们处理的数据是固定的。比如，对于 next token prediction，你知道希望模型拟合哪些文本。对于 SFT，你有固定的数据对。你确切知道想要学习什么。

### [1:44:14](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=6254s) · b000180

当时的做法是，对于每一次 next token prediction，查看教师模型（teacher model）的输出概率分布。然后对于学生模型（student model），不是去拟合下一个 token 的硬标签（hard label），而是去拟合教师模型的整个概率分布，从而把教师模型的知识蒸馏到学生模型中。

### [1:44:44](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=6284s) · b000181

大家都还记得吗？记得？那么，在这种情况下，该如何进行呢？正如你们看到的，我们不一定有现成的基于推理的 SFT 数据对。因此，如果想在这里蒸馏教师模型的知识，作者采取了一条很有意思的路线，它仍然叫 distillation，但属于另一种形式。这里使用教师模型 R1 生成一些包含思考 tokens 的示例回复。

### [1:45:25](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=6325s) · b000182

这一步是离线完成的。然后在第二阶段，你进行 SFT，在你的蒸馏模型上拟合一个较小的模型 \[原文表述不清\]，它的权重数量通常比教师模型少得多。因此，你不是去拟合下一个 token 的概率分布，而是拟合整个序列。你只是尝试预测教师模型输出的同一个 token 序列。

### [1:45:59](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=6359s) · b000183

这里这种 distillation 的表述能理解吗？可以？太好了。最后，我们来看看结果。你们可以看到，这些结果同样非常有竞争力，可以媲美那些声称是较小版本推理模型的闭源替代方案。比如 o1-mini，你可以看到这里的数值与它相比很有竞争力。然后你也可能会想，既然可以直接采用同样的 RL 技术，为什么还要费劲去做 distillation 呢？

### [1:46:41](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=6401s) · b000184

实际上，作者发现，在较小的模型规模下，从性能角度来看，蒸馏知识比直接从头学习更有效。都理解了吗？那么，祝大家周末愉快。
