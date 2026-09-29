# Stanford CME295 Transformers &amp; LLMs \| Autumn 2025 \| Lecture 3 - Tranformers &amp; Large Language Models

_中文讲稿_

- Channel: Stanford Online
- Source: [YouTube](https://www.youtube.com/watch?v=Q5baLehv5So)
- Duration: 1:48:45
- Caption source: manual
- Status: complete
- Chinese translation: 217/217
- Translation provider: codex
- Generated: 2026-09-29T15:47:31+00:00

## 讲稿

### [00:05](https://www.youtube.com/watch?v=Q5baLehv5So&t=5s) · b000001

好。大家好，欢迎来到 CME 295 的第 3 讲。今天是非常令人兴奋的一天，因为我们终于要介绍大语言模型（large language models）了。不过，在开始之前，我想还是照惯例，先宣布一些事情。有些同学希望在上课前拿到幻灯片。所以提醒一下，如果你们想用幻灯片做批注，现在它们已经放在网站上了。

### [00:37](https://www.youtube.com/watch?v=Q5baLehv5So&t=37s) · b000002

大家可以去下载。我和 Shervin 会尽量定期在每周四晚上把它们发布到网站上，这样你们就能下载并做批注了。好。那么，我们开始吧。像往常一样，我们来回顾一下上周的内容。如果你们还记得，第 1 讲和第 2 讲主要介绍了自注意力（self-attention）的概念，并将其与 transformer 的结构联系起来。

### [01:14](https://www.youtube.com/watch?v=Q5baLehv5So&t=74s) · b000003

上一讲，我们看了目前各种类型的模型，以及它们如何都以 transformer 为基础。模型有三类，三个主要类别。我们看到的第一类是编码器—解码器模型（encoder-decoder model），它基本上依赖 transformer。它有 transformer 的编码器（encoder），也有 transformer 的解码器（decoder）。通常，这类模型的任务是输入文本。

### [01:44](https://www.youtube.com/watch?v=Q5baLehv5So&t=104s) · b000004

也就是文本输入、文本输出。我们看到的一个例子是 T5 及其各种变体。

### [01:55](https://www.youtube.com/watch?v=Q5baLehv5So&t=115s) · b000005

第二类模型是把 transformer 中的 decoder 去掉，得到仅编码器模型（encoder-only model）。我们深入讨论了 BERT，它是典型的 encoder-only model。我想，我们还看到 BERT 有一个很好的特性：它编码得到的嵌入（embeddings）很有意义，能够充分表达输入。因此，我们看了分类（classification）、情感提取（sentiment extraction）的例子。

### [02:29](https://www.youtube.com/watch?v=Q5baLehv5So&t=149s) · b000006

具体来说，我们考虑的是 CLS 词元（token）编码得到的 embedding。我想，在实际应用中，BERT 被用来编码文档、编码句子。我们会在课程后面看到这些模型有什么用。最后但同样重要的是第三类模型，也就是仅解码器模型（decoder-only）。

### [03:02](https://www.youtube.com/watch?v=Q5baLehv5So&t=182s) · b000007

也就是说，我们只保留 transformer 的 decoder 部分。在这里，我们还要稍作修改：去掉交叉注意力（cross-attention），因为我们不再需要它了。我们没有 encoder。这类模型也是文本输入、文本输出。GPT 就是这类模型非常好的一个例子。事实上，如今大多数模型都是 decoder-only。

### [03:33](https://www.youtube.com/watch?v=Q5baLehv5So&t=213s) · b000008

这就是大家能看到的三种主要模型。到这里大家都跟得上吗？好。接下来，我要介绍 LLM 这个术语。LLM 是大语言模型（large language model）的缩写。那么，什么是大语言模型？首先，大语言模型是一种语言模型（language model）。语言模型就是给 token 序列分配概率的模型。

### [04:08](https://www.youtube.com/watch?v=Q5baLehv5So&t=248s) · b000009

在这里，我们的模型总是在预测下一个 token 的概率。从这个意义上说，它是语言模型。不过，大语言模型还很大。为什么说它大呢？我们会看到，这些模型确实在规模上进行了扩展。首先是模型规模。如今，参数量达到数千亿量级的模型并不少见。

### [04:42](https://www.youtube.com/watch?v=Q5baLehv5So&t=282s) · b000010

不过，通常我们说 LLM 时，指的至少是十亿参数量级。这些模型也在海量数据上训练过，这里的数据量，是用预训练（pre-training）所使用的 token 数量来衡量的。这个数量级是数千亿 token，甚至数万亿 token。我想，最大的那些大概达到了数十万亿 token。所以，训练集非常庞大。

### [05:17](https://www.youtube.com/watch?v=Q5baLehv5So&t=317s) · b000011

它们之所以大，还因为需要大量算力（compute）。通常，你需要一批 GPU 才能让它们运行。不过，如今已经有很多优化，让它们能在消费级 GPU 上运行。我们稍后会讲到。但 LLM 的大，就是根据这些方面来说的。我还想指出，所有这些术语都比较新。

### [05:47](https://www.youtube.com/watch?v=Q5baLehv5So&t=347s) · b000012

我记得在 2018 年、2019 年，还没有真正的 LLM 定义。我想，当时实际上没人谈论 LLM。最开始，也许有人谈到 LLM 时，会把 BERT 包括进去。但 Bert 是一个不生成文本的 encoder-only model。因此，按照现在已经相当明确的 LLM 定义，BERT 不算 LLM，因为它不生成文本。

### [06:18](https://www.youtube.com/watch?v=Q5baLehv5So&t=378s) · b000013

所以在这里，我们只考虑进行文本到文本处理的语言模型，它们在模型规模、训练数据量以及算力方面都非常大。好。正如我们之前看到的，这些模型是 decoder-only。这里我们去掉 encoder，只保留掩码自注意力（masked self-attention）、前馈神经网络（feedforward neural network），以及加法和归一化（normalization）。

### [06:51](https://www.youtube.com/watch?v=Q5baLehv5So&t=411s) · b000014

我们只保留这些。这就是 LLM 的骨干结构（backbone）。我提到 GPT 是一个不错的例子，但不止它，还有很多其他模型。你们可能听说过 Meta 的 LLaMA、Google 的 Gemma，还有 DeepSeek、Mistral、Qwen 等等。名单很长。我想大概——我是说，如今超过 90% 的 LLM 都是 decoder-only。

### [07:26](https://www.youtube.com/watch?v=Q5baLehv5So&t=446s) · b000015

我觉得这是需要记住的一点。好。好的。现在你们知道 LLM 是如何构成的了。不过，如今人们还会给这些模型引入其他东西。我们马上就会看到。我提过，这些模型规模巨大，通常有数千亿参数。所以，即使只做一次推理（inference）计算，也需要大量算力，训练这些模型也是如此。

### [08:05](https://www.youtube.com/watch?v=Q5baLehv5So&t=485s) · b000016

不过你可能会想，为了做一个简单预测，真的需要在一次前向传播（forward pass）中激活所有这些参数吗？我来打个小比方。假设你走进一个房间，房间里有一位数学家、一位物理学家、一位化学家和一位历史学家。你来到这个班上，这里有一群各有所长的专家。

### [08:38](https://www.youtube.com/watch?v=Q5baLehv5So&t=518s) · b000017

你有一个问题，是一道数学题。我想问大家，你会向谁提问？你会问数学家吗？会问化学家吗？会问所有人吗？目前，我们是在问所有人。我们让模型的所有参数都参与生成计算。因此，这里的想法是，给定一个输入，也许没必要让所有人都参与计算。

### [09:17](https://www.youtube.com/watch?v=Q5baLehv5So&t=557s) · b000018

所以，这个想法就是，实际上只让模型的一部分参与下一个 token 的计算。

### [09:30](https://www.youtube.com/watch?v=Q5baLehv5So&t=570s) · b000019

我现在是在引入专家（experts）这个概念。假设我们引入下面的记号。假设有 n 个专家。你可以把他们想象成数学家、化学家、历史学家，等等。这些就是你的专家。这里的想法是，给定输入 x，你要问自己，应该让谁参与输出的生成。

### [10:05](https://www.youtube.com/watch?v=Q5baLehv5So&t=605s) · b000020

比如说，你会有另一个网络。我们把它叫作 G，取自门控（gates），但它有时也叫路由器（router）。假设我们有一些 gates，告诉我们哪些专家应该参与推理。如果有了这个，假设这里的 gate 告诉我们：好，实际上，2 号专家很适合回答你的问题。

### [10:37](https://www.youtube.com/watch?v=Q5baLehv5So&t=637s) · b000021

这里的想法是，输入只会流向这个专家，而不会流向其他专家。这个做法有个名字，叫混合专家（mixture of experts），记作 MoE。大家都在谈 MoE。这些就是混合专家。你会经常看到的公式就是这个。输出 y，记作 y hat，是各个专家输出的加权和，权重是某个量，也就是 gate 的输出，它告诉你每个专家的输出有多重要。

### [11:27](https://www.youtube.com/watch?v=Q5baLehv5So&t=687s) · b000022

是的。

### [11:37](https://www.youtube.com/watch?v=Q5baLehv5So&t=697s) · b000023

好问题。问题是，如何训练 G？如何训练 E？通常，你会联合训练（jointly train）它们。我们可能稍后会讲到。但你可以把它理解为照常训练：做 forward pass，计算损失（loss），然后反向传播（backprop）。这确实是个有意思的问题，因为训练 MoE 会带来一些挑战，我们马上就会看到。是的。

### [12:09](https://www.youtube.com/watch?v=Q5baLehv5So&t=729s) · b000024

问题是，这些 E 是什么？这些 E 的架构是什么？我们先假设它们只是某种网络。暂时不具体说明，不过马上会讲到。目前先假设它是某个网络。好。好的。我刚才说，如果我们不激活所有专家呢？如果只激活其中一部分呢？但这个公式，我想，实际上假设我们考虑了所有专家的输出。

### [12:43](https://www.youtube.com/watch?v=Q5baLehv5So&t=763s) · b000025

因此，我想区分两种 MoE。一种叫稠密 MoE（dense MoE）。dense MoE 实际上对参与的专家数量没有任何限制。这些权重可以是 0 到 1 之间的任意值。你可以把它们看作一个概率分布（probability distribution）。不过，它只是给某些专家分配比其他专家更大的权重。

### [13:17](https://www.youtube.com/watch?v=Q5baLehv5So&t=797s) · b000026

回到刚才的例子。假设我有一道数学题，我会问数学家、化学家和历史学家。那么，与历史学家说的话相比，我可能会给数学家说的话更高的权重。这就是这个想法。不过，有意思的地方在于，我们限制被激活的专家数量。因为正如前面提到的，我们感兴趣的是不让所有人都参与，从而节省一些计算量。

### [13:58](https://www.youtube.com/watch?v=Q5baLehv5So&t=838s) · b000027

因此，还有第二种 MoE，叫稀疏 MoE（sparse MoE）。它只选择所谓的“top k”个专家。k 可以等于 1，也就是一个专家，也可以是两个。这是你选择的一个超参数（hyperparameter）。在这里，输出表达式就变成了对所有被选中的专家，将 G of x 乘以 E of x 后求和。

### [14:36](https://www.youtube.com/watch?v=Q5baLehv5So&t=876s) · b000028

到这里都还好吗？好。当然，这里面还有很多内容。如果你有兴趣深入了解，可以查看幻灯片底部的资源。我想说的一点是，我们有一个衡量这些模型每次传播所产生计算量的单位。你会看到 FLOPS 这个术语。大家以前见过 FLOPS 这个术语吗？

### [15:09](https://www.youtube.com/watch?v=Q5baLehv5So&t=909s) · b000029

没有，不太熟悉。它代表浮点运算（floating-point operations）。它衡量有多少次运算，你可以把它理解成一次 forward pass 涉及的加法、乘法次数。它基本上衡量了你的任务计算负担有多重。因此，我们通常说，与 dense Moe 相比，使用 sparse MoE 时，FLOPS 更少。

### [15:44](https://www.youtube.com/watch?v=Q5baLehv5So&t=944s) · b000030

这就是你们会看到的计量单位。不过，回到你的问题：这些专家是什么？如果你们还记得，大概 10 分钟前，我们说 LLM 是 decoder-only model。我想问大家一个问题。假设我们想在 LLM 中加入一些 MoE，应该放在哪里？这里，我想我们有三个选择。

### [16:16](https://www.youtube.com/watch?v=Q5baLehv5So&t=976s) · b000031

我们有 masked self-attention 层，有 feedforward neural network，还有这个 normalization。我想问大家，你们会把它放在哪里？

### [16:32](https://www.youtube.com/watch?v=Q5baLehv5So&t=992s) · b000032

我想，你们觉得网络中最复杂的部分在哪里？哪里有大量运算？Feedforward？是的。对，回答得很好。确实是 feedforward neural network。至于原因，我想 Shervin 在第 1 讲提过。如果你们还记得，feedforward neural network 是这样一个网络：首先有输入，也就是 D 维输入向量。

### [17:10](https://www.youtube.com/watch?v=Q5baLehv5So&t=1030s) · b000033

然后，它会被投影到一个，比如说，DFF 维空间。接着，它又回到 D 维空间。所以，DFF 通常大于输入的维度。我说的输入，是这里这个。因此，它通常更大。所以，这个 feedforward neural network 的参数量，大致是 D model 乘以 DFF 再乘以 2，加上一些偏置（bias）。

### [17:52](https://www.youtube.com/watch?v=Q5baLehv5So&t=1072s) · b000034

这基本上就是它的数量级。而注意力层（attention layer），如果你们还记得，基本上由投影矩阵（projection matrices）构成。投影矩阵的维度是多少？是 D model 乘以键（keys）的维度，到查询（queries）的维度、值（values）的维度。而这个维度通常小得多。可以把它想成 over 100 \[字幕疑误，可能指 100 的数量级\]。而 D model 通常是 O over 100、O over 1,000 \[字幕疑误，可能指 100、1,000 的数量级\]。

### [18:26](https://www.youtube.com/watch?v=Q5baLehv5So&t=1106s) · b000035

然后，这里的投影，DFF 是 O over 1,000、O over 10,000 \[字幕疑误，可能指 1,000、10,000 的数量级\]。好。现在大家都相信这里是放 mixture of experts 的一个好位置了吗？是吗？好。实际上就是这么做的。在如今的 LLM 中，不让所有参数都参与下一个 token 预测计算的这个想法，就是把 mixture of experts 放到 fn \[字幕疑误，可能指 FFN\] 所在的位置，基本上就是这里。

### [19:12](https://www.youtube.com/watch?v=Q5baLehv5So&t=1152s) · b000036

通常会使用 sparse mixture of experts。回到你的问题，这些专家实际上就是 feedforward neural network。你会有多个可以训练的网络，但只激活其中一个。

### [19:32](https://www.youtube.com/watch?v=Q5baLehv5So&t=1172s) · b000037

通常，k 会等于 1，也可以等于 2，但只会是其中的一个子集。这就是我想说的。而且，这种路由（routing）是在 token 级别进行的。如果你们还记得，decoder 基本上会接收一些输入，也就是一组 token。我在这里说的是，每个 token 都会由一个专家处理，而这个专家可能与处理另一个 token 的专家不同。

### [20:05](https://www.youtube.com/watch?v=Q5baLehv5So&t=1205s) · b000038

这里的 router 会把 token 的表示（representation）作为输入，判断这个 token 最适合流向哪个专家。这个想法能理解吗？后面我有个小示意图，希望能帮助大家理解。现在回到你关于如何训练这个模型的问题。router 是单独训练的吗？

### [20:36](https://www.youtube.com/watch?v=Q5baLehv5So&t=1236s) · b000039

专家是单独训练的吗？人们在训练这些基于 MoE 的模型时，一个挑战是确保所有专家都有权重、都被用到。因为很可能，你训练模型时，不知道为什么，总是只有一两个专家被激活。

### [21:07](https://www.youtube.com/watch?v=Q5baLehv5So&t=1267s) · b000040

而其他专家始终不活跃，从来不参与计算。这个问题叫路由坍塌（routing collapse）。为什么叫 routing collapse？因为 router 总是选择某些专家，而不选择其他专家。这是一个挑战。人们缓解这个挑战的方法，是修改损失函数（loss function），加上一个额外项，就是这里写的这个。

### [21:42](https://www.youtube.com/watch?v=Q5baLehv5So&t=1302s) · b000041

它基本上是某个超参数 alpha，乘以专家数量，再乘以一些量的和；这些量取决于 token 是否去了某个 expert's eye \[字幕疑误，可能指 expert i，即专家 i\]，然后对所有专家求和。完全理解这个公式具体如何运作，并不是特别重要。我觉得你们从这张幻灯片中唯一需要记住的是，这个额外的 loss 会让这些量更趋向于均匀分布（uniform distributions）。

### [22:27](https://www.youtube.com/watch?v=Q5baLehv5So&t=1347s) · b000042

再提醒一下，这些量是什么。f of I 是被路由到专家 I 的 token 所占的比例。P of I 是专家 I 的平均路由概率。所以，当我说所有专家都应该被同等使用时，我的意思是，希望这个概率在各个专家之间大致均匀。

### [22:59](https://www.youtube.com/watch?v=Q5baLehv5So&t=1379s) · b000043

是的。

### [23:20](https://www.youtube.com/watch?v=Q5baLehv5So&t=1400s) · b000044

问题是，你在什么时候计算这些量？对，你可以把它看作常规训练过程。取一个小批次（mini batch），通过模型，然后计算所有这些量。之后，你就基于这些量进行反向传播（backpropagation）。我想让大家记住的是，这会促使概率，也就是 writer \[字幕疑误，可能指 router\] 的选择，在各个专家之间更加均匀，从而缓解 routing collapse 现象。

### [24:05](https://www.youtube.com/watch?v=Q5baLehv5So&t=1445s) · b000045

是的。

### [24:14](https://www.youtube.com/watch?v=Q5baLehv5So&t=1454s) · b000046

问题是，我们能用 Dropout 吗？当然可以。你随时可以把它和其他技术结合起来。人们只是发现这个方法很有帮助。说到其他技术，还有一个我没讲到的东西，它与 Dropout 的思路很相似，叫带噪声门控（noisy gating）。noisy gating 基本上就是，你得到 gates 的预测，然后往里面加一些噪声（noise）。

### [24:45](https://www.youtube.com/watch?v=Q5baLehv5So&t=1485s) · b000047

基本上，它通过纯粹的随机机会，让其他专家也能参与计算。这也是另一种技术。技术有很多种。不过，对，Dropout 对过拟合（overfitting）这类问题确实很有用。这个思路也可以复用到不同情境中。对。对。

### [25:13](https://www.youtube.com/watch?v=Q5baLehv5So&t=1513s) · b000048

问题是，你怎么能——所以你指的是可微（differentiable）吗？我想，这里是问如何求导。是这个问题吗？导数是怎么——你能再详细解释一下你的疑虑吗？

### [25:43](https://www.youtube.com/watch?v=Q5baLehv5So&t=1543s) · b000049

关于这个问题，平均路由概率是 gate 输出的函数。这是其中一个，PI。我想，你的问题是针对 FI。针对 FI，好。我一时想不到一个好的回答，但我想人们有一些技术。而且如今，你甚至不需要手工做这些。

### [26:15](https://www.youtube.com/watch?v=Q5baLehv5So&t=1575s) · b000050

有内置的东西可以用。所以，关于 FI，我之后也许可以再跟你讨论。但对于 P of I，你能看出它很直接吧？它就是 gates 输出概率的平均值。

### [26:35](https://www.youtube.com/watch?v=Q5baLehv5So&t=1595s) · b000051

对。基本上，gate 输出的概率，你可以把它理解为一个向量被投影到 n 维空间，n 对应专家的数量。然后它经过 Softmax。因此，输出各项加起来等于 1。每个维度表示的值，对应于专家 I 会被使用的情况，我想是这样。

### [27:08](https://www.youtube.com/watch?v=Q5baLehv5So&t=1628s) · b000052

比如，第一个维度对应专家 1，第二个维度对应专家 2，依此类推。所以，你只要取它的平均值，而且这个量可以用所有参数来表示。我想，这一个应该没有问题。对。

### [27:31](https://www.youtube.com/watch?v=Q5baLehv5So&t=1651s) · b000053

问题是，如果增加 MoE 的数量，会增加模型参数量吗？这是个好问题。实际上，这就是基于 MoE 的模型背后的一个想法：你可以扩大模型，而不必付出推理时计算量显著增加的代价。你可以增加——人们把它叫作容量（capacity）。你可以增加模型的 capacity，同时仍然把激活参数（active parameters）的数量控制在一定范围内。

### [28:08](https://www.youtube.com/watch?v=Q5baLehv5So&t=1688s) · b000054

active parameters 就是一次 forward pass 中用到的参数。对，人们就是这样做的。对，它会增加参数总量。所以你会看到，有些基于 MoE 的模型，甚至比我们之前说的数千亿参数量级的模型还大，达到数万亿参数量级。比如这里，我推荐的一篇读物是 switch transformer，它扩展到了 1 点几万亿参数。

### [28:41](https://www.youtube.com/watch?v=Q5baLehv5So&t=1721s) · b000055

所以，确实更多。不过，话虽如此，如果你读这篇论文，也会看到这些模型在他们所说的样本效率（sample efficient）方面更高。它们用更少的时间，就能达到参数量更少的模型本来能达到的效果。所以，如果把训练时间作为横轴画出训练曲线，就会看到这些模型通常更具 sample efficiency。

### [29:18](https://www.youtube.com/watch?v=Q5baLehv5So&t=1758s) · b000056

抱歉。

### [29:25](https://www.youtube.com/watch?v=Q5baLehv5So&t=1765s) · b000057

对。对，完全正确。这里的一切都是权衡（trade off）。这里的一切都是权衡。对。好。对。

### [29:41](https://www.youtube.com/watch?v=Q5baLehv5So&t=1781s) · b000058

问题是，每个注意力头（attention head）都会有若干专家吗？实际上，这与 attention heads 无关。你可以把 attention heads 看作独立的另一回事。专家数量与它们无关。

### [29:59](https://www.youtube.com/watch?v=Q5baLehv5So&t=1799s) · b000059

这样能理解吗？

### [30:04](https://www.youtube.com/watch?v=Q5baLehv5So&t=1804s) · b000060

对。没错。好的。对。问题是，每个块（block）是否都会有一定数量的专家？答案是会。而且通常这些权重不共享。通常，你——实际上，我们马上会看一个例子。很可能第 1 层选中了 expert number at all. Three \[字幕疑误，可能指 3 号专家\]，但第 2 层选中了 1 号专家。你知道，这些都是自由的，都是可训练的。

### [30:43](https://www.youtube.com/watch?v=Q5baLehv5So&t=1843s) · b000061

问题是，由我们决定专家会去哪里吗？所有这些都是由 gates 决定的，也就是这个量。一切都由 gates 决定，而 gates 有可训练的权重。你可以把它看作从输入 x 到 n 维空间的一次投影，n 是专家的数量。

### [31:10](https://www.youtube.com/watch?v=Q5baLehv5So&t=1870s) · b000062

问题是，在推理的哪个时刻做出决定？假设我们现在处于推理阶段，我来带你看它如何运作。你有 x，还有这个注意力机制（attention mechanism）。由于它是 decoder-only，它会与所有过去的 token 交互。就像这个 mask。它到这里。在 feedforward neural network block 的开头，这个 token 当然已经包含上下文了。它拥有其他 token 的信息，因为它对它们进行了注意力计算。

### [31:44](https://www.youtube.com/watch?v=Q5baLehv5So&t=1904s) · b000063

接下来，它到这里。x 首先进入 G。G 计算所有专家上的这个概率分布。由于这里采用的是 sparse MoE，我们只选择 top k。假设选 top one，就是概率最高的那个。这样我们就知道会选中哪个专家。因此，你只会计算为该输入选中的那个专家的输出值。

### [32:31](https://www.youtube.com/watch?v=Q5baLehv5So&t=1951s) · b000064

你能具体展开说一下吗？

### [32:35](https://www.youtube.com/watch?v=Q5baLehv5So&t=1955s) · b000065

是的。

### [32:40](https://www.youtube.com/watch?v=Q5baLehv5So&t=1960s) · b000066

具体在哪个时刻？是在 self-attention 层之后。对。

### [32:51](https://www.youtube.com/watch?v=Q5baLehv5So&t=1971s) · b000067

问题是，不同的 head 会有不同的分类吗？不会。只有一个 router。我想我理解你的问题了。你是在问，既然不同的 head 在并行进行不同的注意力计算，那么该怎么处理？如果你还记得，attention layer 有这些不同的 head。但最后，它会把每个 head 的结果拼接（concatenate）起来，然后再次投影到 D model 空间。

### [33:33](https://www.youtube.com/watch?v=Q5baLehv5So&t=2013s) · b000068

是的。

### [33:38](https://www.youtube.com/watch?v=Q5baLehv5So&t=2018s) · b000069

是的。

### [33:46](https://www.youtube.com/watch?v=Q5baLehv5So&t=2026s) · b000070

是的。

### [33:57](https://www.youtube.com/watch?v=Q5baLehv5So&t=2037s) · b000071

对。问题是，我们会有不同的 G 吗？我能告诉你的是，G 是每层特有的。每层特有，而且是可训练的。它基本上会学习如何处理所有这些输入。所以，针对你的问题，我能说的是，G 是每层特有的。比如，第 1 层有一个 G，第 2 层有另一个 G，依此类推。而这个 G 会被训练。好。很好。

### [34:28](https://www.youtube.com/watch?v=Q5baLehv5So&t=2068s) · b000072

看一下时间。这里还有其他问题吗？

### [34:34](https://www.youtube.com/watch?v=Q5baLehv5So&t=2074s) · b000073

没有了。很好。现在我想给你们看一个很有意思的东西，我记得 Mistral 团队在他们的一篇论文中展示过。这里展示的是，对于一段给定文本，每个 token 被 rooted \[字幕疑误，可能指 routed，即路由\] 到了哪些专家。正如我们前面提到的，不同层的专家是不同的。

### [35:08](https://www.youtube.com/watch?v=Q5baLehv5So&t=2108s) · b000074

我想这里是第 0 层，也就是某个给定层。我们确实看到，这些 token 大致上比较均匀地使用了各个专家，差不多是这样。你不希望看到每个 token 都是同一种颜色。幸运的是，这里并不是。对，这是一种很有意思的路由可视化方式：把输入文本展示出来，再标出每个 token 去了哪里，也就是去了哪些专家。

### [35:50](https://www.youtube.com/watch?v=Q5baLehv5So&t=2150s) · b000075

好。好的。我们刚才看到的是，如今的 LLM 修改架构的一种方式，用来满足这样的需求：我们可能想扩大模型，但不增加一次 forward pass 的计算复杂度（computation complexity）。我们通过 MoE 看到了这一点。因此，你会看到很多基于 MoE 的 LLM。

### [36:21](https://www.youtube.com/watch?v=Q5baLehv5So&t=2181s) · b000076

接下来，既然我们已经有了一个 LLM，我们要关注——别担心。我们要关注回答是如何生成的。还记得我说过，如今这些 LLM 接收一些文本作为输入，再输出一些文本。这通常就是下一个 token 预测（next token prediction）任务。你输入一个 token。

### [36:51](https://www.youtube.com/watch?v=Q5baLehv5So&t=2211s) · b000077

比如，句子开头，经过 LLM，它就生成下一个词或下一个 token。比如 A，然后你把 A 输入进去，接着生成 teddy。然后是 teddy bear is，等等，等等。但到目前为止，我们还没有真正深入探讨，究竟如何选择下一个 token。现在我们就来具体看看，下一个 token 是如何生成的。

### [37:26](https://www.youtube.com/watch?v=Q5baLehv5So&t=2246s) · b000078

大家知道，这里的 LLM 就是 decoder-only 架构。这里有一个 decoder，输入在这里，输出在那里。我们暂且假设，中间发生的所有事情。然后，我们得到的输出概率看起来有点像这样。给定一个 token 或一段 token 序列作为输入，你会得到一个输出概率分布，表示模型认为下一个 token 比如等于 A、airplane、fluffy 等的可能性。

### [38:15](https://www.youtube.com/watch?v=Q5baLehv5So&t=2295s) · b000079

这就是你得到的东西。现在我想问大家，如果我们告诉你，有一段序列作为输入，我们想选择下一个 token，而且模型实际上给出的是一个概率分布，那么，你会如何依据它选择下一个 token？

### [38:41](https://www.youtube.com/watch?v=Q5baLehv5So&t=2321s) · b000080

抱歉。很好。概率最大的 token。好的，很好。对，第一个想法就是，直接取概率最高的 token。

### [38:55](https://www.youtube.com/watch?v=Q5baLehv5So&t=2335s) · b000081

这是一个很自然的方法。不过，不知道你们有没有用过 ChatGPT 或 Gemini 之类的东西。每次你提问，它给出的回答总会略有不同。如果你总是选择概率最高的 token，而这里的计算，我们会看到，都是确定性的（deterministic），那么这意味着，对于相同的输入，你总会生成相同的内容。

### [39:33](https://www.youtube.com/watch?v=Q5baLehv5So&t=2373s) · b000082

这是一个局限：不够多样。第二个问题是，如果你每一步都选择概率最高的 token，那么你得到的是局部最优（locally optimal），但未必是全局最优（globally optimal）。这是什么意思？仔细想想，我们的目标是生成一段序列，一段概率较高的输出 token 序列。

### [40:11](https://www.youtube.com/watch?v=Q5baLehv5So&t=2411s) · b000083

但问题是，如果你总是选择概率最高的 token，不一定会得到概率最高的序列。顺便问一下，大家认同这个说法吗？我来举个例子。假设下一个 token 的候选中，一个 token 的概率是 0.8，另一个是 0.7。然后你选择 0.8 的那个。不，实际上不能是 0.7，因为它们加起来必须等于 1。那么就说是 0.2。假设你沿着以 0.8 开头的那条序列继续，后面所有 token 的概率都很低。

### [40:52](https://www.youtube.com/watch?v=Q5baLehv5So&t=2452s) · b000084

那么，你得到的输出序列，概率基本上就可能低于另一条路径；假设那条路径后续步骤的预测概率更高。我们马上会看到这个例子。但思路就是这样。选择预测概率最高的 token，是个不错的初步想法。不过，它是局部最优，未必是全局最优。因此，我们有第二种方法，也就是跟踪概率最高的 k 条路径。

### [41:35](https://www.youtube.com/watch?v=Q5baLehv5So&t=2495s) · b000085

不知道你们是否听说过束搜索（beam search）。beam search 做的就是这个。这里的 k 有时被称为束大小（beam size）或束宽（beam width）。所以，如果听到这些术语，它们只是我们所跟踪的路径数量的名称。它的工作方式如下。假设我们从句首 token 开始生成，我们想确定下一个 token 是什么。

### [42:07](https://www.youtube.com/watch?v=Q5baLehv5So&t=2527s) · b000086

假设在这个非常简单的例子中，只有三个 token。假设概率最高的两个 token 是 A 和 the。如果 k 等于 2，我们就跟踪这两个分支。这是第一次迭代。第二次迭代，我们会查看这两个 token 之后所有 next token prediction 的概率。

### [42:41](https://www.youtube.com/watch?v=Q5baLehv5So&t=2561s) · b000087

我们始终保留概率最高的两条路径。比如这里，假设是 the 后面接 fluffy，以及 A 后面接 cute。回到我刚才说的，如果你选择了经过概率最高的 token 的路径，比如 the，那么它后面概率最高的 token，其概率很可能远低于 A 后面的那个。

### [43:21](https://www.youtube.com/watch?v=Q5baLehv5So&t=2601s) · b000088

这就是 beam search 试图做的事。它试图找到更接近全局最优的解。假设我们继续下去，最后会得到若干个潜在选项，也就是 k 个候选。然后，我们选出概率最高的那个，也就是概率最高的序列。通常，人们会对各个 token 的概率取对数，再求和。

### [43:56](https://www.youtube.com/watch?v=Q5baLehv5So&t=2636s) · b000089

也就是说，序列的对数概率（log probability），等于每次 next token prediction 的 log probability 之和。也就是已知 BOS 时 A 的 log probability，加上已知 BOS 和 A 时 cute 的 log probability，依此类推。不过，我想指出这种方法的一个局限：生成的 token 越多，最终序列的概率就越低。

### [44:37](https://www.youtube.com/watch?v=Q5baLehv5So&t=2677s) · b000090

因为仔细想想，这些概率都在 0 到 1 之间。你可以从乘法的角度来看。假设整个序列的概率，就是各个下一个 token 概率的乘积。你乘进去的小于 1 的概率越多，这个量就越趋向于 0。因此，这种方法照原样使用，会优先选择较短的序列。

### [45:14](https://www.youtube.com/watch?v=Q5baLehv5So&t=2714s) · b000091

所以，beam search 会加入一些额外项，基本上用来抵消这种影响。大概是 1 除以 token 数量的某个次方这样的东西。因此，实践中会有一些技术，确保整体运作得比较好。好。假设我们已经解决了这些问题。

### [45:44](https://www.youtube.com/watch?v=Q5baLehv5So&t=2744s) · b000092

问题在于，我们需要跟踪这些概率最高的路径，需要进行各种保存操作，等等。这需要大量计算。另一个问题是，我们仍然关注概率最高的路径，基本上会得到一个非常——模型认为非常可能的序列。但有时，你希望输出更多样，或者更有创造性。

### [46:19](https://www.youtube.com/watch?v=Q5baLehv5So&t=2779s) · b000093

这就是为什么 beam search 实际上不是人们通常使用的方法。人们会把 beam search 用于机器翻译（machine translation）之类的任务，因为这些任务确实需要一个接近高概率结果的输出。但实际上，人们使用的是第三种方法，也叫采样方法（sampling method）。我说过，对于下一个 token 应该是什么，我们有一个覆盖各个 token 的概率分布。

### [46:53](https://www.youtube.com/watch?v=Q5baLehv5So&t=2813s) · b000094

人们所做的，就是按照这个概率分布采样下一个 token。

### [47:04](https://www.youtube.com/watch?v=Q5baLehv5So&t=2824s) · b000095

这样能理解吗？在这个例子中，fluffy、gentle、kind，以及比如 smart，被抽到的概率会更高；相比之下，比如 airplane，出现的概率更低。不是零概率，但它们有出现的概率。好？到目前为止有什么问题吗？对。

### [47:35](https://www.youtube.com/watch?v=Q5baLehv5So&t=2855s) · b000096

对。问题是，这不是用于训练，而是用于推理。对，没错。可以把它看作回答生成（response generation）。假设你有一个训练好的模型，你想生成一个输出。那么你会怎么做？对。补充一下我的回答，在训练过程中，你关心的是输出概率，然后将其与实际标签（label）比较，大多数时候就是硬标签（hard label）。对，你比较的就是这些。

### [48:06](https://www.youtube.com/watch?v=Q5baLehv5So&t=2886s) · b000097

而这里讨论的是，假设你有一个训练好的 LLM，你会如何生成回答？

### [48:12](https://www.youtube.com/watch?v=Q5baLehv5So&t=2892s) · b000098

好。Are on goods? \[字幕疑误，可能是在问大家是否都跟上了\] 对。

### [48:26](https://www.youtube.com/watch?v=Q5baLehv5So&t=2906s) · b000099

对。问题是，这种情况下如何进行 sampling？这实际上就是我接下来几张幻灯片的内容。不过，我想先确保大家对直观思路有一致的理解。选择最高概率的做法叫贪心解码（greedy decoding）。这可能不是我们想要的。beam search 稍好一点，更接近全局最优。它并不是全局最优，只是更朝那个方向靠近。因此它更好，但缺少多样性，缺少创造性。所以，我们想做的是对每个 token 进行 sampling。

### [49:02](https://www.youtube.com/watch?v=Q5baLehv5So&t=2942s) · b000100

我们还有几种方法，会限制参与 sampling 的 token 类型。因为我提到过，那些概率很低的 token 理论上仍然可能被采样到，但这不一定是我们想要的。因此，人们通常会把范围限制在概率最高的 token 中，只从它们里面 sampling。

### [49:35](https://www.youtube.com/watch?v=Q5baLehv5So&t=2975s) · b000101

你们可能听说过 Top-k 采样（Top-k sampling）这个术语。谁听说过？对，有一些。做法是，选出概率最高的 k 个——也就是概率最高的 top k 个 token，然后从中 sampling。假设 k 等于 4，你就取概率最高的四个，再从它们中 sampling。还有一种思路很相似的方法，叫 Top-p。

### [50:06](https://www.youtube.com/watch?v=Q5baLehv5So&t=3006s) · b000102

Top-p 是把范围限制在概率最高的一批 token 中，使它们的累积概率（cumulative probability）超过阈值 p。同样，它做的事情类似：选择概率最高的 token。不过，还有一部分我没讲，那就是，这些概率最初是如何得到的？

### [50:41](https://www.youtube.com/watch?v=Q5baLehv5So&t=3041s) · b000103

如果你们还记得，我在这里说过，我们先假设已经有这些概率。概率已经有了，我们想选择下一个 token。但现在我要问的是，既然我们已经知道如何使用这些概率，那么这些概率最初是如何得到的？

### [51:07](https://www.youtube.com/watch?v=Q5baLehv5So&t=3067s) · b000104

如果你们还记得，这些基于 transformer 的架构，基本上会计算输入的编码器表示（encoder representation）。图的最上方有一些最终层，它们的作用是把向量投影到词表（vocabulary）空间。

### [51:37](https://www.youtube.com/watch?v=Q5baLehv5So&t=3097s) · b000105

因为你想要为采样到某个给定 token 的可能性，得到一个概率值。所以，在架构最顶端，你会把输入，也就是 token 编码后的 embedding，送入线性层（linear layer），基本上将 D model 向量投影到一个维度大小为 v 的空间。

### [52:12](https://www.youtube.com/watch?v=Q5baLehv5So&t=3132s) · b000106

当然，你想得到的是概率。因此，你会有一个 Softmax 层，它基本上把所有值转换为概率，使它们的和等于 1。计算这些概率时，你会使用这个公式，也就是 Softmax 层。有一个相当重要的超参数，我想和大家讲一下，就是温度（temperature）T。它就在这里出现。

### [52:49](https://www.youtube.com/watch?v=Q5baLehv5So&t=3169s) · b000107

下一个 token 是某个给定词的概率，等于该词对应的输入除以 temperature 后取指数（exponential）。然后，用其他所有对应量除以 t 后的指数之和对它归一化。现在我们要看的是，T 有什么用，或者说 T 在实践中究竟起什么作用。

### [53:23](https://www.youtube.com/watch?v=Q5baLehv5So&t=3203s) · b000108

开始之前，先问一个问题。有谁听说过回答生成中的 temperature？有。好。希望接下来的内容能让你们更好地理解 temperature 如何影响输出预测。我想问大家的是，低 temperature 和高 temperature 会分别产生什么影响？

### [54:04](https://www.youtube.com/watch?v=Q5baLehv5So&t=3244s) · b000109

所以，低 temperature 会对应于什么样的多样……？

### [54:21](https://www.youtube.com/watch?v=Q5baLehv5So&t=3261s) · b000110

是的。

### [54:26](https://www.youtube.com/watch?v=Q5baLehv5So&t=3266s) · b000111

是的。

### [54:36](https://www.youtube.com/watch?v=Q5baLehv5So&t=3276s) · b000112

我们马上会讲到。对，你有没有一个——

### [54:42](https://www.youtube.com/watch?v=Q5baLehv5So&t=3282s) · b000113

更低的 temperature？提高 temperature。我想，回到降低 temperature 的解释，以及它会对——产生什么影响。你有没有一个可能的回答？我想，较低的 temperature。假设 temperature 更低，会发生什么？

### [55:16](https://www.youtube.com/watch?v=Q5baLehv5So&t=3316s) · b000114

对。我想——长话短说，低 temperature 会产生尖峰状分布（spiky distribution），而高 temperature 会产生均匀分布。不过，我觉得你的直觉是对的。

### [55:35](https://www.youtube.com/watch?v=Q5baLehv5So&t=3335s) · b000115

我也许可以用更数学化的方式把它写出来。

### [55:41](https://www.youtube.com/watch?v=Q5baLehv5So&t=3341s) · b000116

好。假设你的概率是 xi 除以 t 后取指数，再除以所有 xj 除以 t 后的指数之和。从数学上，你实际上可以证明这里会发生什么。假设你有最大的 xi 对应的索引。

### [56:17](https://www.youtube.com/watch?v=Q5baLehv5So&t=3377s) · b000117

我们把它叫作 k。假设我这样做，把这个量提出来。实际上，这里没地方了。那就写在这里。这里会是 ae of k temperature \[字幕疑误，可能指与 xk 除以 temperature 的指数有关的项\]。然后这里是对所有 j 求和，求和项是 xj 除以 t 减去 xk 除以 t 后的指数。

### [56:58](https://www.youtube.com/watch?v=Q5baLehv5So&t=3418s) · b000118

我所做的，就是把分子和分母都乘以 xk 除以 t 的指数。我把分子和分母都乘了这个量。当然，它们会抵消。但这样，这里得到的是 xy 减去 xk，再除以 t \[字幕疑误，xy 可能指 xi\]。这里是 xj 减去 k，再除以 t \[字幕疑误，k 可能指 xk\]。当 i 等于 k 时，这一项是 0。无论 temperature 是多少，它都恰好是 0。

### [57:32](https://www.youtube.com/watch?v=Q5baLehv5So&t=3452s) · b000119

而这里，xj 减去 xk 总是负数或 0。

### [57:44](https://www.youtube.com/watch?v=Q5baLehv5So&t=3464s) · b000120

所以在这里，如果 i 等于 k，就得到 0 除以 t。因此，这里是 1。然后是 1 加上——我想，是某个量。j 减去 xk，再除以 t \[字幕疑误，j 可能指 xj\]，这个量会是负数。当 t 趋于 0 时，这个量就会，我想，趋于负无穷。

### [58:22](https://www.youtube.com/watch?v=Q5baLehv5So&t=3502s) · b000121

所以，负无穷的指数是 0。最终得到的结果就是，当 i 等于 k 时，概率非零。但当 i 不等于 k 时，得到的是 0 除以一个不等于 0 的量，结果就是 0。

### [58:53](https://www.youtube.com/watch?v=Q5baLehv5So&t=3533s) · b000122

所以，仅从数学上来说，如果你把 xk 除以 t 的指数提出来，其中 k 是最大值的索引，我想，也就是最大的 logit 或最大的激活向量（activation vector），实际上就能证明，当温度（temperature）较小时，只有最大的——也就是说，我想，最大值对应的索引会具有最高的概率，在那里形成一个尖峰。

### [59:30](https://www.youtube.com/watch?v=Q5baLehv5So&t=3570s) · b000123

而当温度较高时，基本上看起来就像均匀分布（uniform distribution），因为所有这些量，也就是说，当 t 趋于正无穷时，这个量趋于 0。所以 0 的指数就是 e。抱歉，不是 e，是 1。所以是 1。所以就是 1 除以 j 的数量。所以是 1。也就是说，在词表中的所有词元（token）上形成均匀分布。

### [1:00:04](https://www.youtube.com/watch?v=Q5baLehv5So&t=3604s) · b000124

对。

### [1:00:16](https://www.youtube.com/watch?v=Q5baLehv5So&t=3616s) · b000125

所以问题是，我该如何理解一个较小的——

### [1:00:27](https://www.youtube.com/watch?v=Q5baLehv5So&t=3627s) · b000126

所以问题是，我能把它理解为高斯分布（Gaussian）吗？我想是这个问题。这有点难，因为对于 Gaussian，x 轴上是一些连续的量。而这里是 token，所以是离散的。而且它们也不是能够排序的东西。所以我大概只会把它理解为：温度较小时，分布的尖峰非常明显。也就是说，某一组概率最高的 token 会出现得更多。而如果温度较高，那么基本上，即使是那些原本概率并非最高的 token，调整后的概率也会更高。

### [1:01:15](https://www.youtube.com/watch?v=Q5baLehv5So&t=3675s) · b000127

是的。所以从这个意义上，你可以把它看作某种缩放。长话短说，我想告诉你的是，如果温度较低，就会促使下一个 token 更倾向于概率最高的 token。而如果温度较高，我想，概率分布就会更接近均匀分布，尤其是你把温度提高很多的时候。

### [1:01:45](https://www.youtube.com/watch?v=Q5baLehv5So&t=3705s) · b000128

所以输出会更有创意。原本不会抽到的 token，现在可能会被抽到。那么在实践中，这意味着什么呢？假设你正在使用自己最喜欢的大语言模型（LLM）。再假设你想，我不知道，写一些非常有创意的东西。那么你会用哪一种？低温度还是高温度？高温度？对。所以，如果你想要更确定的结果，更接近于，我想，你认为质量很高的那种结果，就会使用更低的温度。

### [1:02:23](https://www.youtube.com/watch?v=Q5baLehv5So&t=3743s) · b000129

这里要注意一点，如果温度严格大于 0，那么每次你针对一个输入运行模型时，都会得到不同的输出。

### [1:02:42](https://www.youtube.com/watch?v=Q5baLehv5So&t=3762s) · b000130

我想指出的是，transformer 架构里没有任何东西是概率性的。一切都是确定性的。唯一不确定的地方，是你如何采样下一个 token。只有这一点是不确定的。那么，要获得确定性的输出，你会怎么做？让 t 等于 0。T 等于 0 时，你就能确定输出只会是一种结果，不会是其他结果。

### [1:03:18](https://www.youtube.com/watch?v=Q5baLehv5So&t=3798s) · b000131

嗯，这是它的理论性质。但在实践中，计算过程中会发生一些事情，引入某些非确定性操作。这远远超出了这门课的范围，远远超出了这门课的范围。我只是想指出，实际使用时，t 等于 0 也可能因为这些实际层面的问题而得到不同的结果。

### [1:03:52](https://www.youtube.com/watch?v=Q5baLehv5So&t=3832s) · b000132

所以我推荐的是，这里有一篇推荐阅读，如果你——完全是选读。最近有一篇关于消除语言模型（LM）推理中非确定性的文章。如果你感兴趣，我建议读一读。大致的思路是，我们的图形处理器（GPU）、我们的硬件，在对某些操作做归约（reduction）时，有时会对量级差异非常大的数字进行归约。

### [1:04:26](https://www.youtube.com/watch?v=Q5baLehv5So&t=3866s) · b000133

因此，这些操作发生的顺序其实相当重要。也就是说，如果这些操作以不同顺序发生，就可能得到不同结果。即使理论上应该完全一样，实际中也未必一样。这篇文章很好地解释了其中的直觉。所以，如果你感兴趣可以看看，完全是选读。好。我知道我有点超时了，所以我想，最后要说的是，假设你想以一种非常具体的格式生成输出。

### [1:05:10](https://www.youtube.com/watch?v=Q5baLehv5So&t=3910s) · b000134

假设是 JSON 格式。我想，一种非常朴素的方法就是告诉 LLM：请用 JSON 生成这个。然后它生成一些内容，你再检查是不是有效的 JSON。如果不是，就重复——让它重新生成，直到生成正确为止。这是第一种朴素的方法。还有第二种方法，叫作引导解码（guided decoding）。

### [1:05:45](https://www.youtube.com/watch?v=Q5baLehv5So&t=3945s) · b000135

它的做法是在生成过程中，过滤掉所谓的无效后续 token。这里，假设我要生成这个 JSON。我能确定，第一个 token 必须是某种打开——我忘了这个东西的英文怎么说了，总之就是左括号。对，打开括号。所以你只能先有这个，然后只能是属性名，依此类推。

### [1:06:19](https://www.youtube.com/watch?v=Q5baLehv5So&t=3979s) · b000136

有时允许的下一个 token 不止一个，这种情况下就回到我们的下一个 token 选择策略。对。

### [1:06:38](https://www.youtube.com/watch?v=Q5baLehv5So&t=3998s) · b000137

所以问题是，如何限制其他 token？有不少论文讨论这个问题。我们不会讲这部分，但我可以给你一些检索方向。直接输入有限状态机（finite state machine，FSM）、上下文文法（context grammar）\[字幕疑误，可能指 context-free grammar\]。有不少论文在做这个，我们这里就不讲了。好。我想，接下来我们就进入第二部分，由 Shervin 来讲。很好。谢谢你，Afshin。现在，我们一起来看看不同的提示策略（prompting strategies）。

### [1:07:13](https://www.youtube.com/watch?v=Q5baLehv5So&t=4033s) · b000138

既然现在已经知道回答是如何生成的，我们就来看看如何得到回答，以及如何得到出色的回答。回到我们最喜欢的那个可爱泰迪熊的例子。我先介绍一个术语。当你有某种输入时，输入的长度是用 token 数量来衡量的。你会在文献里看到它有不同的名称。它可以叫上下文长度（context length）、上下文大小（context size）、窗口大小（window size）。

### [1:07:48](https://www.youtube.com/watch?v=Q5baLehv5So&t=4068s) · b000139

我想，最新的工具，比如你用 Cursor 或其他代码辅助工具编程时，我想它们更常称之为 context length，但这些术语都是等价的，指的是同一件事。好。现在我想花点时间讨论一下，这里可能涉及哪些数量级。比如，当今的 LLM，输入 token 的数量往往处于几万、几十万或者几百万的数量级。

### [1:08:27](https://www.youtube.com/watch?v=Q5baLehv5So&t=4107s) · b000140

这就是它能够接受的输入规模。有时，你会听到某个新 LLM 宣称某个数字。那个 context length 的数字指的就是这个，也就是单次处理能容纳多少 token。好，很好。然后，这些模型，你可能看过一些关于它们的宣传。我想 Gemini 以及其他一些模型已经达到了百万级。

### [1:08:56](https://www.youtube.com/watch?v=Q5baLehv5So&t=4136s) · b000141

这是不是意味着一切都很好了呢？如果 context length 更长，就能解决所有问题吗？其实不是。今年夏天早些时候的一篇论文把一种现象称为上下文腐化（context rot）。基本上，作者通过一项叫作 needle in a Haystack 的测试，研究模型检索某条信息的能力。

### [1:09:27](https://www.youtube.com/watch?v=Q5baLehv5So&t=4167s) · b000142

基本上，他们提出某个问题，然后把答案埋在越来越长的文本中，观察模型找到那个答案的能力。你可以看到，随着 context length 增加，模型依据上下文中的答案来为信息建立依据（grounding）的能力会下降。我觉得这篇论文很有意思。它对上下文中的其他内容做了控制。

### [1:09:59](https://www.youtube.com/watch?v=Q5baLehv5So&t=4199s) · b000143

其中有个术语叫干扰项（distractors），他们加入一些噪声，然后发现 distractors 基本上会使检索能力下降。所以，上下文里放了什么也很重要。这就是为什么一般来说，当你有一个检索问题，想用 LLM 来解决时，你很有理由尽可能准确地选取合适的上下文片段，让 LLM 看到这些内容并据此预测。

### [1:10:32](https://www.youtube.com/watch?v=Q5baLehv5So&t=4232s) · b000144

好。很好。对。

### [1:11:06](https://www.youtube.com/watch?v=Q5baLehv5So&t=4266s) · b000145

对。是的。问题是，context length 是否就是自注意力（self-attention）中所显示的那个长度？是的，对。接下来我们会看到——我想上次我们看过，有时会用一些技巧，让 self-attention 机制的复杂度不至于是 n 的平方。这些方法就是用来在 context length 增长时管理计算复杂度的。对。这个问题提得很好。

### [1:11:37](https://www.youtube.com/watch?v=Q5baLehv5So&t=4297s) · b000146

它说的正是这个。好。很好。有什么问题吗？还有其他问题吗？好。很好。现在我们来定义一下，提示（prompt）通常是什么样的。对于如何组织一个 prompt，并没有正式的理论。不过，这些是给模型的 prompt 中通常会出现的主要部分。你可以区分出一个设置上下文的部分，在那里交代情境，让模型清楚你想提出什么样的查询。

### [1:12:21](https://www.youtube.com/watch?v=Q5baLehv5So&t=4341s) · b000147

然后，假设你有一些任务想让模型执行，就会有指令。这些指令中的一些就像接收某些东西作为输入的函数，所以你会加入一些输入。为了从模型回答中得到你想要的结果，你可能还想加一些约束。这里我们用了最喜欢的泰迪熊例子。上下文是，这只泰迪熊是什么——基本上就是，这只泰迪熊的心情如何？

### [1:12:53](https://www.youtube.com/watch?v=Q5baLehv5So&t=4373s) · b000148

为了让泰迪熊开心，我们想做什么？然后，我们给出一些输入，说明我们想生成的故事发生在哪里。接着给出一些约束。如果你想看看日常使用 LLM 时的其他例子，上下文可以是这样一句话：你是 ChatGPT。今天是 10 月 10 日。

### [1:13:23](https://www.youtube.com/watch?v=Q5baLehv5So&t=4403s) · b000149

现在是下午 4:44。这样就设定了情境。指令基本上可以是用户提出的请求以及相应输入。而约束可能是你作为用户看不到、但存在于给 LLM 的 prompt 中的东西，比如安全指令。例如，不要生成任何可能导致伤害的内容，或者类似的要求。所以每当你看到某个输入被送进 LLM，我想，这些投影、这四个维度，可以成为一个很好的心智模型，帮助你理解这个结构中各个部分对应什么目标。

### [1:14:06](https://www.youtube.com/watch?v=Q5baLehv5So&t=4446s) · b000150

这样说清楚吗？好，很好。既然我们已经知道可以用什么思路来看待 LLM 的输入，现在来看看怎样让 LLM 做我们想让它做的事。并且看看，怎样在不调整任何权重的情况下做到这一点。我们可以使用一个叫作上下文学习（in-context learning）的概念。这里的“学习”有点一词多义，因为你实际上没有对 LLM 的权重进行任何学习，但你可以把一些知识作为上下文的一部分传递进去，让它完成你想要的事情。

### [1:14:50](https://www.youtube.com/watch?v=Q5baLehv5So&t=4490s) · b000151

in-context learning 主要分为两类。其中一类的思路很简单，叫作零样本（zero-shot）。基本上，除了输入，也就是你的输入查询，你不提供任何其他东西，只让 LLM 做你想做的事。另一种思路叫作少样本学习（few-shot learning），也就是在提出你关心的输入之前，先向 LLM 提供一些输入和输出的例子。

### [1:15:25](https://www.youtube.com/watch?v=Q5baLehv5So&t=4525s) · b000152

在泰迪熊和睡前故事这个例子里，你可能会给泰迪熊起名字。比如有一只泰迪熊叫 Teddy，你生成了一个故事。你放入查询，放入想要生成的故事，并提供多个这样的例子。再假设你还有一只泰迪熊叫 Bob，你想为 Bob 生成一个故事。那么你就放入所有这些例子，再让 LLM 生成你想要的故事。

### [1:15:57](https://www.youtube.com/watch?v=Q5baLehv5So&t=4557s) · b000153

这基本上就是我们所说的 few-shots 设置。

### [1:16:04](https://www.youtube.com/watch?v=Q5baLehv5So&t=4564s) · b000154

好。很好。一般来说，当你看最终任务的表现时，提供例子往往能很好地引导 LLM 完成你关心的任务。原因就在于，你已经让模型知道了你在寻找什么。然后，它就能利用训练过程中学到的东西，把这些联系起来，基本上进行复现。

### [1:16:39](https://www.youtube.com/watch?v=Q5baLehv5So&t=4599s) · b000155

但当然，你需要收集这些例子，这会产生开销。它会在上下文窗口（context window）中放入更多 token，所以你需要更多计算。不过，在最近的模型中，我们看到了一个有意思的权衡。它们的推理能力越来越强，所以我在这里把“一般来说”这个限定用斜体标出来。也就是说，few-shots 一般更好，但并非总是如此。

### [1:17:11](https://www.youtube.com/watch?v=Q5baLehv5So&t=4631s) · b000156

因为如今，对于这些更强的模型，人们发现，基本上只要改进指令，就可以让 in-context learning 的表现与提供例子相当，甚至更好。因为仔细想想，当你提供例子时，就把模型限制在了某些有限的例子集合中。所以在推理时，假设你想对一种未见过的数据分布执行任务，模型就更难泛化，因为它会试图对齐上下文中见过的内容。

### [1:17:55](https://www.youtube.com/watch?v=Q5baLehv5So&t=4675s) · b000157

相反，如果你把指令改成更侧重推理的形式，用自然语言解释如何完成任务，它就能利用推理能力来真正完成任务。如今这种情况越来越常见。我想，这方面的文献还在发展中，不过已经有一些论文，比如 plan and solve，我想是最近发表的。它表明，如果你让 LLM 自己先制定计划，再解决问题，就能获得非常好的表现。

### [1:18:31](https://www.youtube.com/watch?v=Q5baLehv5So&t=4711s) · b000158

所以，这是一个很有意思的事实。好。很好。既然我们已经基本了解了这些学习方式，现在来看看可以怎样提高回答的质量。有一个概念叫作思维链（chain of thought）。研究人员发现，如果你要求模型在真正给出答案之前，先给出得出该答案的一些推理依据，就能获得更好的表现。

### [1:19:05](https://www.youtube.com/watch?v=Q5baLehv5So&t=4745s) · b000159

这就是人们所说的 chain of thought，基本上就是你如何得出答案的过程。比如在这里，你问自己，这只泰迪熊几岁了？如果你强制模型直接用一个数字作答，它可能无法建立起联系，弄清楚为什么这只泰迪熊恰好是这个年龄。相反，如果给出完整的推理链，就能清楚地看到是什么推导出了这个回答。

### [1:19:37](https://www.youtube.com/watch?v=Q5baLehv5So&t=4777s) · b000160

我想，这就是这项技术背后的主要思路。基本上，它可以用于 in-context learning。比如你给出 few-shot 例子：这只泰迪熊当时几岁？你给出一个数字，然后稍微改变查询。接着，LLM 就可以根据推理、格式和回答，相应地调整推理与回答。这样会促使模型在给出回答的同时输出一些推理，基本上能看到指标有所改善。

### [1:20:18](https://www.youtube.com/watch?v=Q5baLehv5So&t=4818s) · b000161

好，很好。然后，我还想说一点，假设你想完成一项任务，而且想把它做好。m \[字幕不明\] 你总会遇到一些表现不好的样本。对于这些样本，你希望能够调试。通常，调试 LLM 时，不像过去那样调试。你不会去查看权重、查看 LLM 内部的东西。你想要的是它以 token 形式输出一些更容易解释的内容。

### [1:20:51](https://www.youtube.com/watch?v=Q5baLehv5So&t=4851s) · b000162

通常，通过这些技术，你可以看到模型在输出某个回答之前的推理，基本上就能调试哪里出了问题。比如你问，这只熊明年会是几岁？如果 chain of thought 里说，嘿，现在是 2019 年，你就知道，你的上下文里可能有问题，哦，也许我把日期写错了。所以你可以追溯到——可以很容易地进行一些根因定位。

### [1:21:24](https://www.youtube.com/watch?v=Q5baLehv5So&t=4884s) · b000163

所以它也有这个用途。而且，和其他增加 token 数量的技术完全一样，这也是你需要管理的一种权衡：当然，推理会花更多时间，因为你需要生成更多 token。但通常我们可以接受。关于 COT，有什么问题吗？

### [1:21:50](https://www.youtube.com/watch?v=Q5baLehv5So&t=4910s) · b000164

好，很好。现在再进一步。我想介绍一下，如何让 COT 更强：你可以对模型采样多次，查看它生成的答案，然后通过多数投票（majority voting），选出这个 LLM 预测次数最多的答案。这就是我们所说的自一致性（self-consistency）。基本上，就是多次采样回答，再解析出实际的答案。

### [1:22:27](https://www.youtube.com/watch?v=Q5baLehv5So&t=4947s) · b000165

基本上，你把整段推理排除掉，专门关注答案。然后通过 majority voting，就能以更稳健的方式得到一个答案。对。

### [1:22:50](https://www.youtube.com/watch?v=Q5baLehv5So&t=4970s) · b000166

对。问题是，你是否需要某种基准测试（benchmark），来判断它是不是更好？是的，当然需要。我想这篇论文是在那些算术类和数学类 benchmark 上进行的。我想，与这个问题相关的另一个问题是，如何定位答案，再对它进行 majority voting。通常，你可以在上下文中加入一条指令：把实际答案放在最后。这样你就可以只提取最后的内容。除此之外，我想人们也会用基于正则表达式（regex）的方法来提取答案。

### [1:23:24](https://www.youtube.com/watch?v=Q5baLehv5So&t=5004s) · b000167

或者，你甚至可以考虑用另一个 LLM 来提取答案。所以总有办法做到。但回到你的问题，是的，我们需要某种 benchmark 和真实标签（ground truth labels），才能确定这种方法确实更好。

### [1:23:53](https://www.youtube.com/watch?v=Q5baLehv5So&t=5033s) · b000168

对。这里的请求——问题是，它会作为例子发送到同一个请求里吗？通常，你会并行采样。基本上，就是让模型执行 Afshin 刚才讲的那个过程。你从基于序列起始标记（BOS）以及已有 token 的概率分布中，采样下一个 token。然后在其他几个分支上也这么做。所有这些都并行进行。最后再解析答案。

### [1:24:25](https://www.youtube.com/watch?v=Q5baLehv5So&t=5065s) · b000169

所以基本上，这个过程的延迟大致等于各路并行生成中的最大延迟，因为这一切都可以并行执行。因此，这些生成结果都不会进入彼此的上下文，它们都是并行完成的。然后你得到最终答案。好，很好。都清楚吗？好，很好。既然我们已经看过一些 prompting 技术，我想和大家一起介绍一些人们在推理时想出的技巧，尽可能提高生成效率。

### [1:25:08](https://www.youtube.com/watch?v=Q5baLehv5So&t=5108s) · b000170

基本上，如今的模型有很多参数，你又想生成很多 token。怎样才能尽可能高效地做到呢？我想把这个思考过程分成两部分。我们会看看，有哪些方法能在保持精确的前提下提高效率。也就是，你执行的计算与原本应该执行的完全相同，但方式更高效。

### [1:25:40](https://www.youtube.com/watch?v=Q5baLehv5So&t=5140s) · b000171

我放了一些提示，说明我们要探索哪些技术。我们尝试寻找能够避免冗余的技术。看看怎样才能最好地管理内存。也看看能不能重新表述 LLM 内部的方程，从而在实践中简化生成。然后还有第二类，我们也会探索。

### [1:26:14](https://www.youtube.com/watch?v=Q5baLehv5So&t=5174s) · b000172

这一类重点关注：哪些近似是可以接受的，能够以更低的成本得到高质量答案，但结果是近似的。我们可以对架构做哪些变动？能不能对嵌入（embeddings）做些什么，让它们更高效？还有在 token 预测方面，能不能做些什么让它更快？

### [1:26:48](https://www.youtube.com/watch?v=Q5baLehv5So&t=5208s) · b000173

听起来可以吗？我们大约还有 22 分钟。我们会尽量把这里所有内容都讲完。好。我把技术分成了精确技术和近似技术。不过，我们实际上会按模块来讲。先看注意力层（attention layer），看看那里能采用哪些技术。第二部分再来看输出层（output layer）。

### [1:27:21](https://www.youtube.com/watch?v=Q5baLehv5So&t=5241s) · b000174

然后看看在 token 生成层面，可以怎样尽可能做好。我们先从 attention 层面开始。之前我们看到，对于每个 token，在这种带掩码的自注意力（masked self-attention）中，都需要当前 token 关注前面的 token。假设你正在生成序列，目前到了某个 token。

### [1:27:52](https://www.youtube.com/watch?v=Q5baLehv5So&t=5272s) · b000175

假设你已经生成了 a cute teddy bear，现在到了 ease \[字幕疑误，可能指 is\]。现在你的查询（query）是 ease。你会计算 ease 的键表示（key representation）和值表示（value representation）。当然，你必须这样做，因为它是当前 token。但我们希望找到一种方式，复用过去为前面的 token 计算 key representation 和 value representation 时已经完成的计算。

### [1:28:26](https://www.youtube.com/watch?v=Q5baLehv5So&t=5306s) · b000176

这个目标清楚吗？大家都同意吗？

### [1:28:33](https://www.youtube.com/watch?v=Q5baLehv5So&t=5313s) · b000177

好。更准确地说，我们想找到一种方法，把 key 和 value 矩阵保存下来。这里我没有给 Q 部分加下划线，因为前面那些 token 对应的 query，当然不是当前 token 所关心的。所以就是 key 和 value 部分。好。有一个概念叫键值缓存（KV cache），它的目标是把这些 key 和 value 矩阵存到某个地方，然后直接从缓存中复用它们。

### [1:29:18](https://www.youtube.com/watch?v=Q5baLehv5So&t=5358s) · b000178

正如刚才所说，当你想计算某个 token 时，可以直接从缓存中复用 key 和 value，而不用重新计算。

### [1:29:33](https://www.youtube.com/watch?v=Q5baLehv5So&t=5373s) · b000179

这基本上就是刚才所讲内容的示意。这样清楚吗？

### [1:29:46](https://www.youtube.com/watch?v=Q5baLehv5So&t=5386s) · b000180

好。太好了。我们还能做什么呢？对。

### [1:29:59](https://www.youtube.com/watch?v=Q5baLehv5So&t=5399s) · b000181

对。好问题。训练时会做 KV caching 吗？我会说，训练时有一个叫作教师强制（teacher forcing）的概念，你把所有输入放进去，一次性一起传入。所以 KV caching 这个概念根本不会出现。对。不过这个问题很好。对。对。

### [1:30:37](https://www.youtube.com/watch?v=Q5baLehv5So&t=5437s) · b000182

对。对。问题是，这一切有什么意义？我们只是想复用已经完成的计算。你的回答是对的，完全正确。还有其他问题吗？

### [1:30:54](https://www.youtube.com/watch?v=Q5baLehv5So&t=5454s) · b000183

好，很好。现在我们已经看到，可以缓存这些量。那么还能做什么？上周课上有没有什么可以复用的东西，或许能减少缓存的数量，也就是 key 和 value 的数量？我们有什么技术吗？

### [1:31:18](https://www.youtube.com/watch?v=Q5baLehv5So&t=5478s) · b000184

稀疏注意力（Sparse attention）。

### [1:31:24](https://www.youtube.com/watch?v=Q5baLehv5So&t=5484s) · b000185

对，可以是这个。可以，但这里不是。假设你仍然关注所有 token，并且把重点放在 key 和 value 的数量上。有没有办法减少这个数量？回顾一下，这里我讨论的是多头注意力（multi-head attention），也就是有 h 个头。所以你有 h 个 query 投影、h 个 key 投影和 h 个 value 投影。上周有没有什么技术可以复用，来减少这个数量？

### [1:32:00](https://www.youtube.com/watch?v=Q5baLehv5So&t=5520s) · b000186

对，我听到了。对。分组查询注意力（Group query attention）\[字幕疑误，通常称为 grouped-query attention\]。对，完全正确。我们之前讲过把 key 和 value 分组的概念。基本上，一般形式叫作 group query attention，你把这些分组，而两个极端值 h 和 1，分别对应完整的 multi-head attention 和多查询注意力（multi query attention）。在如今的 LLM 中，很多论文都会使用 GQA，并选择一个合理的分组数量。

### [1:32:39](https://www.youtube.com/watch?v=Q5baLehv5So&t=5559s) · b000187

这也是我们可以做的。好，很好。接下来我要稍微讲一点硬件方面的内容。如果我们在推理时，用一种朴素的方法存储所有这些值的缓存。假设你收到——假设我是一个推理服务器，收到来自多个用户的查询。假设我收到查询一，又收到查询二。一种朴素的 key 和 value 矩阵存储方式，是一开始就预留一块与整个 context length 对应的内存，因为你不知道自己会在哪里停止。

### [1:33:30](https://www.youtube.com/watch?v=Q5baLehv5So&t=5610s) · b000188

你在进行解码，因为只有遇到序列结束标记（EOS token）时，才会停止解码。所以你可能会预留这样一整块空间，大小等于 context length，也就是最大 context length。一个明显的问题是，这会造成大量浪费。假设 context length 是 2k，你会为某个请求预留 2k，这里也预留 2k。那么在任意时刻，假设你想接收更多请求，想为更多请求提供服务。

### [1:34:03](https://www.youtube.com/watch?v=Q5baLehv5So&t=5643s) · b000189

内存很快就会没有足够空间来容纳。这些限制或者这个挑战，大家能理解吗？

### [1:34:19](https://www.youtube.com/watch?v=Q5baLehv5So&t=5659s) · b000190

对。好。有一篇论文叫作 PagedAttention，它定义了几个量：预留空间（reserved）、内部碎片（internal fragmentation）和外部碎片（external fragmentation）。internal fragmentation 基本上就是模型为了完成请求而预留的空间。而 reserved 的位置则是其中对应实际使用的 token 的那一部分。

### [1:34:52](https://www.youtube.com/watch?v=Q5baLehv5So&t=5692s) · b000191

所以，这是实际使用的那类空间；internal fragmentation 里没有任何东西，但它被预留了。external fragmentation 则是因为内存管理系统不一定把内存块一个接一个地放置，而是有自己分配内存块的方式，所以可能会留下其他空隙。他们提出了一个叫作 PagedAttention 的系统，它支撑着一个名为 vLLM 的推理软件包，通过把生成过程映射到固定大小的块上来解决这个问题。

### [1:35:36](https://www.youtube.com/watch?v=Q5baLehv5So&t=5736s) · b000192

所以，它不会为回答某个请求分配一整片内存，而是把它拆成更小的块。我想论文中块大小取的是 16。你可以看到，假设你正在生成，已经用完某一行，就直接开始用另一行，不会再浪费更多空间。然后会有一个字典，把 token 的位置索引映射到相应的缓存值。

### [1:36:15](https://www.youtube.com/watch?v=Q5baLehv5So&t=5775s) · b000193

所以，这是一种巧妙的管理方式。他们表明，它能大幅减少碎片。对。好，很好。现在我们再对 KV cache 做点别的。刚才我们看到，token 有一个内部表示，你把它投影成 query、key 和 value。而 key 和 value 的维度其实是不容忽视的。

### [1:36:51](https://www.youtube.com/watch?v=Q5baLehv5So&t=5811s) · b000194

而且，你需要在每个 transformer 块中分别存储它们的一份副本。所以需要维护很多这样的向量。有没有办法让这种表示更紧凑一些？这是 DeepSeek 尝试解决的一个问题，使用的概念叫作——我想叫作多潜在注意力（multi-latent attention）\[字幕疑误，可能指 Multi-head Latent Attention\]。

### [1:37:24](https://www.youtube.com/watch?v=Q5baLehv5So&t=5844s) · b000195

我们来看——先看常规情况。如果使用 multi-head attention，那么对于某个 token 的表示，你有 h 个投影矩阵把它转换成 key。大家都认同吗？也就是说，在 self-attention 的公式中，有一个用于 key 的投影矩阵 wk，它会把 token 表示投影成某个 key。

### [1:37:56](https://www.youtube.com/watch?v=Q5baLehv5So&t=5876s) · b000196

你有 h 个头，因此就有 h 次这样的投影，以及 h 个由此得到、需要存进缓存的 embeddings。key 有这一套，value 也有这一套。这意味着要存储很多向量，而且这些 key 和 value 本身也相当长。所以我们来看看能不能把它变小。

### [1:38:27](https://www.youtube.com/watch?v=Q5baLehv5So&t=5907s) · b000197

multi-latent attention 的做法是把这些投影矩阵分解，中间经过一个维度低于 key 空间的中间空间。先进行一次降低维度的变换，再进行另一次解压缩变换。这是他们为了使表示更紧凑而采取的第一步。

### [1:39:01](https://www.youtube.com/watch?v=Q5baLehv5So&t=5941s) · b000198

但他们还做了一件非常聪明的事。他们提出，key 和 value 可以共享压缩矩阵。这意味着，对于某个 token 表示，key 和 value 所需存储的缓存是相同的。然后在解压缩部分，这里仍然会有不同的矩阵，以便真正为 key 和 value 学到不同的表示。

### [1:39:39](https://www.youtube.com/watch?v=Q5baLehv5So&t=5979s) · b000199

所以，这里的一个简化就是让 key 和 value 共享它。更进一步，还在 h 个头之间共享。因此，你不再有 h 个这样的 embeddings，而是只有一个。key 这样做，value 也这样做。最终，对于每个 transformer 块，每个 token 都只有一个表示。

### [1:40:10](https://www.youtube.com/watch?v=Q5baLehv5So&t=6010s) · b000200

这样清楚吗？所以，不仅需要存储的东西变少了，DeepSeek V2 论文还展示了性能提升，并把这在一定程度上归因于这种做法带来的正则化（regularization）效果。也就是说，它学到了可能更有用、并由 key 和 value 共享的表示。看来它还有性能方面的好处，不只是硬件方面的收益。

### [1:40:46](https://www.youtube.com/watch?v=Q5baLehv5So&t=6046s) · b000201

好，很好。现在我们已经看过一些——对。

### [1:40:55](https://www.youtube.com/watch?v=Q5baLehv5So&t=6055s) · b000202

对。问题是，低秩维度（low rank dimension）需要调节吗？维度本身是一项设计选择，它是固定的。

### [1:41:07](https://www.youtube.com/watch?v=Q5baLehv5So&t=6067s) · b000203

问题是，所有部分使用的低维维度都一样吗？维度大小是固定的，而且所有部分都一样，我想是这样。不过这是一项设计选择。你可以选择不同的维度，但我想在实践中可能会用同一个。对。还有其他问题吗？好，很好。现在我们还剩不到 10 分钟。接下来讲作用于输出 token 层面的技术，先从一个叫作推测解码（speculative decoding）的概念开始。

### [1:41:39](https://www.youtube.com/watch?v=Q5baLehv5So&t=6099s) · b000204

这是一个非常有意思的方法，利用较小的模型来辅助较大模型的生成，再通过某种机制，使输出分布与目标分布匹配。它结合了几种技巧：先用较小的模型生成内容，然后利用一些数学性质进行筛选，确保得到的分布与大模型的分布相似。

### [1:42:17](https://www.youtube.com/watch?v=Q5baLehv5So&t=6137s) · b000205

下面是课上要讲的，它的基本思路。我们回到最喜欢的泰迪熊例子。你让一个较小的模型，论文称它为草稿模型（draft），生成后续的词。已有的是 my teddy bear。接下来可能是什么词？先运行一遍，得到 token is。把 token is 再送到这里，得到 cute 和 smart。

### [1:42:49](https://www.youtube.com/watch?v=Q5baLehv5So&t=6169s) · b000206

由于这个 LLM 很小，通常会比大 LLM 更快完成。得到这些之后，把小 LLM 预测出的所有 token 一起作为输入，送给目标 LLM，也就是那个较大的模型，你所使用的那个模型，为每个位置生成概率分布。接下来我们会看到，通过对这些 token 的输出分布应用某个规则，可以模拟出每个 token、每个后续 token 的概率分布，使其与目标模型的分布相似。

### [1:43:38](https://www.youtube.com/watch?v=Q5baLehv5So&t=6218s) · b000207

基本过程如下。它会查看 draft model 预测的 token 的概率。如果 draft model 的概率大于 draft model 输出分布中 draft model 的概率 \[字幕疑误，此处概率比较对象重复，可能原意涉及 target model 与 draft model 的比较\]，就直接接受这个 token。否则，会有一个接受—拒绝机制（acceptance rejection mechanism），决定接受还是拒绝这个 token。

### [1:44:12](https://www.youtube.com/watch?v=Q5baLehv5So&t=6252s) · b000208

假设所有 token 都被接受，那么一次运行就能向前推进更多 token。如果失败了，基本上就从那个好的 token 往后恢复生成过程，并对分布做一些调整。

### [1:44:35](https://www.youtube.com/watch?v=Q5baLehv5So&t=6275s) · b000209

看到这些，你可能会问：这看起来像一套操作步骤，为什么它会匹配目标分布？如果你从全概率公式（law of total probability）出发，用这些量写出每一项，最后就会得到目标分布。我鼓励大家做一做这个练习。幻灯片这里附上的论文，只用了几行就证明了这一点。

### [1:45:06](https://www.youtube.com/watch?v=Q5baLehv5So&t=6306s) · b000210

所以这是一个非常简单的证明，我觉得也非常、非常有意思。这样清楚吗？对。

### [1:45:19](https://www.youtube.com/watch?v=Q5baLehv5So&t=6319s) · b000211

对。对。问题是，这是不是拒绝采样（rejection sampling）？是的。所以你们有些人可能已经熟悉它了。这样清楚吗？

### [1:45:33](https://www.youtube.com/watch?v=Q5baLehv5So&t=6333s) · b000212

对。还有一点我没有说，为什么我们还要把最后一个 token 放在这里？我们放入了所有 draft token，也放入了最后预测出的那个 token。因为把所有这些 draft token 一起做一次前向传播（forward pass），就能顺带得到它们之后那个 token 的概率分布，然后直接从 Qk 加 1 中采样。这里简要说明一下这样做的理由。

### [1:46:07](https://www.youtube.com/watch?v=Q5baLehv5So&t=6367s) · b000213

做一次整体运行，和每次只运行一次的开销一样，因为在推理时，你是 memory bounds back \[字幕疑误，可能指 memory-bound\]。换句话说，计算不是限制因素，内存才会成为计算的瓶颈。所以你希望在较小的模型上做这件事，然后在大模型上，一次性计算所有这些概率分布。

### [1:46:35](https://www.youtube.com/watch?v=Q5baLehv5So&t=6395s) · b000214

这样清楚吗？好。很好。然后，我想讲最后一项技术，叫作多 token 预测（multi-token prediction）。它也是——顺便说一下，前面那项技术叫 speculative decoding。而这一项基本上也在做同样的事。它的做法稍有不同，不过 draft model 被嵌入了同一个模型中，这很强大。

### [1:47:07](https://www.youtube.com/watch?v=Q5baLehv5So&t=6427s) · b000215

基本上，这种模型会在最后一个解码器（decoder）的表示之上接上多个头。其过程是，训练时不做下一个词预测，而是做多个词预测。测试时，所有这些头构成 draft model，而主模型就是第一个头。这样，你得到所有 draft token，再把它们送回第一个头，进行接受—拒绝。

### [1:47:44](https://www.youtube.com/watch?v=Q5baLehv5So&t=6464s) · b000216

论文采用了贪心（greedy）的方式，所以没有使用这个公式。因为架构和目标函数都发生了变化，就不再具有那个很好的性质，也就是重新得到下一个 token 的预测分布。不过，它有一个略微变化的版本。对。所以 multi-token prediction 中有意思的几点，首先是目标函数的改变。其次是 draft model 和 target model 基本上嵌入了同一个模型中。

### [1:48:17](https://www.youtube.com/watch?v=Q5baLehv5So&t=6497s) · b000217

所以不必把两者分开。对。还记得这张幻灯片吗？我们已经探索了能够改善这些方面的技术。我也非常推荐大家看看相关论文。最后，非常感谢大家。
