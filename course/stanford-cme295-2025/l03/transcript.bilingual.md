# Stanford CME295 Transformers &amp; LLMs \| Autumn 2025 \| Lecture 3 - Tranformers &amp; Large Language Models

_Bilingual transcript · 双语讲稿_

- Channel: Stanford Online
- Source: [YouTube](https://www.youtube.com/watch?v=Q5baLehv5So)
- Duration: 1:48:45
- Caption source: manual
- Status: complete
- Chinese translation: 217/217
- Translation provider: codex
- Generated: 2026-09-29T15:47:31+00:00

## Transcript · 讲稿

### [00:05](https://www.youtube.com/watch?v=Q5baLehv5So&t=5s) · b000001

**English**

Cool. Hello, everyone, and welcome to lecture 3 of CME 295. So today is a very exciting day, because we're going to finally introduce large language models. But I guess before we go into that I'm just going to start, traditionally, with some announcements. So some of you wanted to have the slides before the class. So just a heads up that in case you want to use the slides to do some annotations, they're on the website right now.

**中文**

好。大家好，欢迎来到 CME 295 的第 3 讲。今天是非常令人兴奋的一天，因为我们终于要介绍大语言模型（large language models）了。不过，在开始之前，我想还是照惯例，先宣布一些事情。有些同学希望在上课前拿到幻灯片。所以提醒一下，如果你们想用幻灯片做批注，现在它们已经放在网站上了。

### [00:37](https://www.youtube.com/watch?v=Q5baLehv5So&t=37s) · b000002

**English**

So feel free to get them. And with Shervin, we'll try to, just on a regular basis, every Thursday evening, have them publish on the website so that you can download them and annotate. Cool. So with that, let's start. And as usual, we're going to recap last week's episodes. So if you remember, lecture 1 and lecture 2 were all about introducing the concept of self-attention and linking them to the construct of the transformer.

**中文**

大家可以去下载。我和 Shervin 会尽量定期在每周四晚上把它们发布到网站上，这样你们就能下载并做批注了。好。那么，我们开始吧。像往常一样，我们来回顾一下上周的内容。如果你们还记得，第 1 讲和第 2 讲主要介绍了自注意力（self-attention）的概念，并将其与 transformer 的结构联系起来。

### [01:14](https://www.youtube.com/watch?v=Q5baLehv5So&t=74s) · b000003

**English**

And what we did last lecture was look at all the types of models that are out there and how they were all based on the transformer. So there are three categories, three main categories of models. So the first one that we saw was encoder-decoder model, which basically relies on the transformer. It has the encoder of the transformer, the decoder of the transformer. And typically, the tasks there are input text.

**中文**

上一讲，我们看了目前各种类型的模型，以及它们如何都以 transformer 为基础。模型有三类，三个主要类别。我们看到的第一类是编码器—解码器模型（encoder-decoder model），它基本上依赖 transformer。它有 transformer 的编码器（encoder），也有 transformer 的解码器（decoder）。通常，这类模型的任务是输入文本。

### [01:44](https://www.youtube.com/watch?v=Q5baLehv5So&t=104s) · b000004

**English**

So text in, text out. So we saw that one example was T5 and all the variations.

**中文**

也就是文本输入、文本输出。我们看到的一个例子是 T5 及其各种变体。

### [01:55](https://www.youtube.com/watch?v=Q5baLehv5So&t=115s) · b000005

**English**

The second type of model is where we remove the decoder from the transformer and we obtain an encoder-only model. So we went deeper into BERT, which is the typical encoder-only model. And I guess, we also saw that what BERT has is this nice property that it's encoded embeddings are very meaningful and expressive of the inputs. And so we saw the example of classification, sentiment extraction.

**中文**

第二类模型是把 transformer 中的 decoder 去掉，得到仅编码器模型（encoder-only model）。我们深入讨论了 BERT，它是典型的 encoder-only model。我想，我们还看到 BERT 有一个很好的特性：它编码得到的嵌入（embeddings）很有意义，能够充分表达输入。因此，我们看了分类（classification）、情感提取（sentiment extraction）的例子。

### [02:29](https://www.youtube.com/watch?v=Q5baLehv5So&t=149s) · b000006

**English**

So what we did was, in particular, take into consideration the encoded embedding of the CLS token. So I guess in real life, BERT is used to encode documents to encode sentences. And we're going to see later in the class how these models are useful. And then last but not least, we have the third category of models, which is decoder only.

**中文**

具体来说，我们考虑的是 CLS 词元（token）编码得到的 embedding。我想，在实际应用中，BERT 被用来编码文档、编码句子。我们会在课程后面看到这些模型有什么用。最后但同样重要的是第三类模型，也就是仅解码器模型（decoder-only）。

### [03:02](https://www.youtube.com/watch?v=Q5baLehv5So&t=182s) · b000007

**English**

So we only keep the decoder part of the transformer. And so here, we also do a little bit of a modification. So we remove the cross-attention because we don't need it anymore. We don't have an encoder. And these kinds of models are text in, text out. And so GPT is a very good example of such models. And actually, most models these days, they're decoder-only.

**中文**

也就是说，我们只保留 transformer 的 decoder 部分。在这里，我们还要稍作修改：去掉交叉注意力（cross-attention），因为我们不再需要它了。我们没有 encoder。这类模型也是文本输入、文本输出。GPT 就是这类模型非常好的一个例子。事实上，如今大多数模型都是 decoder-only。

### [03:33](https://www.youtube.com/watch?v=Q5baLehv5So&t=213s) · b000008

**English**

So these are the three main kinds of models that you can see out there. So far so good for everyone? Cool. So with that, I'm going to introduce the term LLM. So LLM stands for large language model. So what is a large language model? So first of all, a large language model is a language model. So a language model is a model that assigns probability to sequences of tokens.

**中文**

这就是大家能看到的三种主要模型。到这里大家都跟得上吗？好。接下来，我要介绍 LLM 这个术语。LLM 是大语言模型（large language model）的缩写。那么，什么是大语言模型？首先，大语言模型是一种语言模型（language model）。语言模型就是给 token 序列分配概率的模型。

### [04:08](https://www.youtube.com/watch?v=Q5baLehv5So&t=248s) · b000009

**English**

So in this case, our model always predicts the probability of the next token. So it's, in that sense, a language model. But also, a large language model is large. So why is it large? So we're going to see that these models, they are actually scaled up in terms of size. So first of all in terms of model size. So these days, it's not uncommon to see models on the order of hundreds of billions of parameters.

**中文**

在这里，我们的模型总是在预测下一个 token 的概率。从这个意义上说，它是语言模型。不过，大语言模型还很大。为什么说它大呢？我们会看到，这些模型确实在规模上进行了扩展。首先是模型规模。如今，参数量达到数千亿量级的模型并不少见。

### [04:42](https://www.youtube.com/watch?v=Q5baLehv5So&t=282s) · b000010

**English**

But typically, when we say LLM we say at least on the order of a billion. These models, they've also been trained on a huge amount of data and hereby amount of data, we quantify that by the number of tokens that they were pre-trained with. And this is on the order of magnitude of hundreds of billions of tokens or even trillions of tokens. So I think the biggest ones are like on the tens of trillions of tokens. So huge training sets.

**中文**

不过，通常我们说 LLM 时，指的至少是十亿参数量级。这些模型也在海量数据上训练过，这里的数据量，是用预训练（pre-training）所使用的 token 数量来衡量的。这个数量级是数千亿 token，甚至数万亿 token。我想，最大的那些大概达到了数十万亿 token。所以，训练集非常庞大。

### [05:17](https://www.youtube.com/watch?v=Q5baLehv5So&t=317s) · b000011

**English**

And they're also large because they need a lot of compute. So typically you need a bunch of GPUs to make them work. Although these days there's been a lot of optimizations to have them work on consumer based GPUs. So we're going to see that later on. But in LLM is large according to these categories. So another thing that I want to point out is that all these terminologies, they're relatively new.

**中文**

它们之所以大，还因为需要大量算力（compute）。通常，你需要一批 GPU 才能让它们运行。不过，如今已经有很多优化，让它们能在消费级 GPU 上运行。我们稍后会讲到。但 LLM 的大，就是根据这些方面来说的。我还想指出，所有这些术语都比较新。

### [05:47](https://www.youtube.com/watch?v=Q5baLehv5So&t=347s) · b000012

**English**

So I remember in 2018, '19, there was no real definition of an LLM. I think no one actually talked about LLMs. In the beginning, maybe people talked about LLMs. They included BERT. But Bert is an encoder-only model that does not produce text. So with the current definition of an LLM, which right now has been pretty well established, BERT would not be an LLM because it doesn't produce text.

**中文**

我记得在 2018 年、2019 年，还没有真正的 LLM 定义。我想，当时实际上没人谈论 LLM。最开始，也许有人谈到 LLM 时，会把 BERT 包括进去。但 Bert 是一个不生成文本的 encoder-only model。因此，按照现在已经相当明确的 LLM 定义，BERT 不算 LLM，因为它不生成文本。

### [06:18](https://www.youtube.com/watch?v=Q5baLehv5So&t=378s) · b000013

**English**

So here, we only consider language models that do text to text, that are very large in size, in terms of amount of data that have been trained on and in terms of compute. Cool. And as we saw before, these models are decoder-only. So here, what we do is we remove the encoder, we only keep the masked self-attention, the feedforward neural network, and then the addition and normalization.

**中文**

所以在这里，我们只考虑进行文本到文本处理的语言模型，它们在模型规模、训练数据量以及算力方面都非常大。好。正如我们之前看到的，这些模型是 decoder-only。这里我们去掉 encoder，只保留掩码自注意力（masked self-attention）、前馈神经网络（feedforward neural network），以及加法和归一化（normalization）。

### [06:51](https://www.youtube.com/watch?v=Q5baLehv5So&t=411s) · b000014

**English**

So we only keep this. And this is the backbone of LLMs. And so I mentioned GPT is kind of a good example. But it's not just that. You have plenty of other models. So you may have heard of LLaMA from Meta, Gemma from Google, DeepSeek, Mistral, Qwen, and so on. The list is long. I would say roughly--I mean, more than 90% of modern day LLMs, they're all decoder-only.

**中文**

我们只保留这些。这就是 LLM 的骨干结构（backbone）。我提到 GPT 是一个不错的例子，但不止它，还有很多其他模型。你们可能听说过 Meta 的 LLaMA、Google 的 Gemma，还有 DeepSeek、Mistral、Qwen 等等。名单很长。我想大概——我是说，如今超过 90% 的 LLM 都是 decoder-only。

### [07:26](https://www.youtube.com/watch?v=Q5baLehv5So&t=446s) · b000015

**English**

So I think that's something to keep in mind. Cool. OK. So now you how LLMs are made of. But there is something else that people these days also introduce to these models. And we're going to see that in a bit. So I mentioned that these models are huge in size, again, typically hundreds of billions of parameters. So it takes a lot of compute to just compute one inference, or also to train these models.

**中文**

我觉得这是需要记住的一点。好。好的。现在你们知道 LLM 是如何构成的了。不过，如今人们还会给这些模型引入其他东西。我们马上就会看到。我提过，这些模型规模巨大，通常有数千亿参数。所以，即使只做一次推理（inference）计算，也需要大量算力，训练这些模型也是如此。

### [08:05](https://www.youtube.com/watch?v=Q5baLehv5So&t=485s) · b000016

**English**

But you may wonder, do you really need to have all these parameters be activated during a forward pass, to make a simple prediction? So I'm going to have a little metaphor. So let's suppose you enter in a room. And in the room, there is a mathematician, a physicist, a chemist and a historian. So you come in this class, there's a bunch of people who are expert in what they do.

**中文**

不过你可能会想，为了做一个简单预测，真的需要在一次前向传播（forward pass）中激活所有这些参数吗？我来打个小比方。假设你走进一个房间，房间里有一位数学家、一位物理学家、一位化学家和一位历史学家。你来到这个班上，这里有一群各有所长的专家。

### [08:38](https://www.youtube.com/watch?v=Q5baLehv5So&t=518s) · b000017

**English**

And you have a question, you have a math question. So a question I have for you is, who would you ask your question? Would you ask the mathematician? Would you ask the chemist? Would you ask everyone? Well, right now, we ask everyone. We ask all parameters of the model to be involved in the computation of the generation. And so the idea here is given an input, maybe it's not necessary to ask everyone to be involved in the computation.

**中文**

你有一个问题，是一道数学题。我想问大家，你会向谁提问？你会问数学家吗？会问化学家吗？会问所有人吗？目前，我们是在问所有人。我们让模型的所有参数都参与生成计算。因此，这里的想法是，给定一个输入，也许没必要让所有人都参与计算。

### [09:17](https://www.youtube.com/watch?v=Q5baLehv5So&t=557s) · b000018

**English**

So the idea is let's actually just have a subset of the model be involved in the computation of the next token.

**中文**

所以，这个想法就是，实际上只让模型的一部分参与下一个 token 的计算。

### [09:30](https://www.youtube.com/watch?v=Q5baLehv5So&t=570s) · b000019

**English**

So I'm just introducing this idea of experts. So let's suppose we're introducing the following notation. So let's suppose we have n experts. So think of it as your mathematician, your chemist, historian, whatever. So these are your experts. And the idea is given an input x, you're going to ask yourself who should be involved in the generation of the outputs.

**中文**

我现在是在引入专家（experts）这个概念。假设我们引入下面的记号。假设有 n 个专家。你可以把他们想象成数学家、化学家、历史学家，等等。这些就是你的专家。这里的想法是，给定输入 x，你要问自己，应该让谁参与输出的生成。

### [10:05](https://www.youtube.com/watch?v=Q5baLehv5So&t=605s) · b000020

**English**

So you're going to have, let's say, another network. Where we're going to call it G like gates, but it's also sometimes called router. So let's suppose we have some gates that tells us which experts should be involved in the inference. So if we have that, so let's suppose here, the gate tells us OK, so actually, expert number 2 is well suited to answer your question.

**中文**

比如说，你会有另一个网络。我们把它叫作 G，取自门控（gates），但它有时也叫路由器（router）。假设我们有一些 gates，告诉我们哪些专家应该参与推理。如果有了这个，假设这里的 gate 告诉我们：好，实际上，2 号专家很适合回答你的问题。

### [10:37](https://www.youtube.com/watch?v=Q5baLehv5So&t=637s) · b000021

**English**

So here, the idea is that the input is just going to flow into that expert, but not the other experts. So this has a name. It's called mixture of experts. So it's denoted MoE. Everyone talks about MoE. So these are a mixture of experts. And so the formula that you will see a lot is this one. So the output y, which is denoted y hat is the sum of the expert output weighted by some quantity, which is the output of the gate, which tells you how important the output of each expert is.

**中文**

这里的想法是，输入只会流向这个专家，而不会流向其他专家。这个做法有个名字，叫混合专家（mixture of experts），记作 MoE。大家都在谈 MoE。这些就是混合专家。你会经常看到的公式就是这个。输出 y，记作 y hat，是各个专家输出的加权和，权重是某个量，也就是 gate 的输出，它告诉你每个专家的输出有多重要。

### [11:27](https://www.youtube.com/watch?v=Q5baLehv5So&t=687s) · b000022

**English**

Yeah.

**中文**

是的。

### [11:37](https://www.youtube.com/watch?v=Q5baLehv5So&t=697s) · b000023

**English**

Great question. So the question is, how do you train G? How do you train E. So typically, you train them jointly. So we're going to see that maybe in a little later. But you can think of it as just training as usual. You do your forward pass, you compute the loss and you backprop. And it's actually an interesting question because there is some challenges that come with training MoEs that we're going to see in a second. Yeah.

**中文**

好问题。问题是，如何训练 G？如何训练 E？通常，你会联合训练（jointly train）它们。我们可能稍后会讲到。但你可以把它理解为照常训练：做 forward pass，计算损失（loss），然后反向传播（backprop）。这确实是个有意思的问题，因为训练 MoE 会带来一些挑战，我们马上就会看到。是的。

### [12:09](https://www.youtube.com/watch?v=Q5baLehv5So&t=729s) · b000024

**English**

Question is, what are these E's. What is the architecture of these E's? So let's suppose right now that there's just some network. We're not specifying them for now, but we're going to see this in a second. Let's suppose for now, it's some network. Cool. OK. So I told you that what if we don't activate everyone. What if we activate a subset? But this formula, actually, I guess, assumes that we're actually considering all expert outputs.

**中文**

问题是，这些 E 是什么？这些 E 的架构是什么？我们先假设它们只是某种网络。暂时不具体说明，不过马上会讲到。目前先假设它是某个网络。好。好的。我刚才说，如果我们不激活所有专家呢？如果只激活其中一部分呢？但这个公式，我想，实际上假设我们考虑了所有专家的输出。

### [12:43](https://www.youtube.com/watch?v=Q5baLehv5So&t=763s) · b000025

**English**

So I just want to distinguish two kinds of MoEs. So there's one kind that is called a dense MoE. So a dense MoE actually does not have any constraints on the number of experts that are involved. So these weights, they can be anywhere between 0 and 1. So think of them as a probability distribution. But it's just going to put more weight towards some experts compared to others.

**中文**

因此，我想区分两种 MoE。一种叫稠密 MoE（dense MoE）。dense MoE 实际上对参与的专家数量没有任何限制。这些权重可以是 0 到 1 之间的任意值。你可以把它们看作一个概率分布（probability distribution）。不过，它只是给某些专家分配比其他专家更大的权重。

### [13:17](https://www.youtube.com/watch?v=Q5baLehv5So&t=797s) · b000026

**English**

So back to the example that I had, so let's suppose I have a math question. So I'm going to ask the mathematician, the chemist, the historian. So I'm probably going to add a higher weight to what the mathematician says compared to let's say, the historian. So this is the idea. But then the interesting thing is when we constrain the number of experts that are activated, because here, as we mentioned previously, what we're interested in is to not involve everyone is to make some savings in the amount of compute that we do.

**中文**

回到刚才的例子。假设我有一道数学题，我会问数学家、化学家和历史学家。那么，与历史学家说的话相比，我可能会给数学家说的话更高的权重。这就是这个想法。不过，有意思的地方在于，我们限制被激活的专家数量。因为正如前面提到的，我们感兴趣的是不让所有人都参与，从而节省一些计算量。

### [13:58](https://www.youtube.com/watch?v=Q5baLehv5So&t=838s) · b000027

**English**

So there's a second kind of MoE that's called the sparse MoE. And what it does is it only selects the quote unquote, "top k" experts. So k can be equal to 1. So one expert or even two. So it's a hyperparameter that you choose. And so here, the expression of the output becomes the sum over all the chosen experts of a G of x times E of x.

**中文**

因此，还有第二种 MoE，叫稀疏 MoE（sparse MoE）。它只选择所谓的“top k”个专家。k 可以等于 1，也就是一个专家，也可以是两个。这是你选择的一个超参数（hyperparameter）。在这里，输出表达式就变成了对所有被选中的专家，将 G of x 乘以 E of x 后求和。

### [14:36](https://www.youtube.com/watch?v=Q5baLehv5So&t=876s) · b000028

**English**

So far, so good? Cool. And of course, there's a lot more to it. So in case you are interested in learning more, feel free to go into the resources that are at the bottom of the slide. So one thing that I will say is that we have a unit of measure of the amount of compute that these models produce for each pass. So you will see the term FLOPS. So have you seen the term FLOPS out there?

**中文**

到这里都还好吗？好。当然，这里面还有很多内容。如果你有兴趣深入了解，可以查看幻灯片底部的资源。我想说的一点是，我们有一个衡量这些模型每次传播所产生计算量的单位。你会看到 FLOPS 这个术语。大家以前见过 FLOPS 这个术语吗？

### [15:09](https://www.youtube.com/watch?v=Q5baLehv5So&t=909s) · b000029

**English**

No, not really. So it stands for floating-point operations. So it quantifies how many operations. Think of it as additions, multiplications are involved in a forward pass let's say. And it basically quantifies how compute heavy is your task. So typically, what we say is when we go through a sparse MoE as opposed to a dense Moe, we have a lower amount of FLOPS.

**中文**

没有，不太熟悉。它代表浮点运算（floating-point operations）。它衡量有多少次运算，你可以把它理解成一次 forward pass 涉及的加法、乘法次数。它基本上衡量了你的任务计算负担有多重。因此，我们通常说，与 dense Moe 相比，使用 sparse MoE 时，FLOPS 更少。

### [15:44](https://www.youtube.com/watch?v=Q5baLehv5So&t=944s) · b000030

**English**

So this is the unit of measure that you will see. But back to your question, so what are these experts? So if you remember, I mean, 10 minutes ago, we said that LLMs, they are decoder-only models. So I have a question for you. Let's suppose we wanted to put some MoEs in our LLM. Where would we put it? So here, I guess, we have three choices.

**中文**

这就是你们会看到的计量单位。不过，回到你的问题：这些专家是什么？如果你们还记得，大概 10 分钟前，我们说 LLM 是 decoder-only model。我想问大家一个问题。假设我们想在 LLM 中加入一些 MoE，应该放在哪里？这里，我想我们有三个选择。

### [16:16](https://www.youtube.com/watch?v=Q5baLehv5So&t=976s) · b000031

**English**

We have the masked self-attention layer. We have the feedforward neural network. And then we have this normalization. So question for you, I guess, where would you put this?

**中文**

我们有 masked self-attention 层，有 feedforward neural network，还有这个 normalization。我想问大家，你们会把它放在哪里？

### [16:32](https://www.youtube.com/watch?v=Q5baLehv5So&t=992s) · b000032

**English**

I guess, where do you think is--I guess, the most complex parts of the network. Where is there a lot of operations? Feedforward? Yes. Yeah. Great answer. So it's indeed the feedforward neural network. And the reason for that is I think Shervin mentioned it, I think, in lecture 1. So if you remember, the feedforward neural network is a network such that you have the input, which is your D-dimensional input vector.

**中文**

我想，你们觉得网络中最复杂的部分在哪里？哪里有大量运算？Feedforward？是的。对，回答得很好。确实是 feedforward neural network。至于原因，我想 Shervin 在第 1 讲提过。如果你们还记得，feedforward neural network 是这样一个网络：首先有输入，也就是 D 维输入向量。

### [17:10](https://www.youtube.com/watch?v=Q5baLehv5So&t=1030s) · b000033

**English**

And then you have this being projected into, let's say, a DFF dimensional space. And then it goes back to the D-dimensional, I guess, space. So the DFF is typically larger than your dimension of, I guess, the inputs. When I say input, it's here. So it's typically larger. So the amount of parameters that you have in that feedforward neural network is something on the order of magnitude of D model times DFF times 2 plus some bias.

**中文**

然后，它会被投影到一个，比如说，DFF 维空间。接着，它又回到 D 维空间。所以，DFF 通常大于输入的维度。我说的输入，是这里这个。因此，它通常更大。所以，这个 feedforward neural network 的参数量，大致是 D model 乘以 DFF 再乘以 2，加上一些偏置（bias）。

### [17:52](https://www.youtube.com/watch?v=Q5baLehv5So&t=1072s) · b000034

**English**

So it's basically your order of magnitude. And the attention layer, if you remember, it's basically composed of the projection matrices, what is the dimension of the projection matrices. So it's D model times the dimension of keys to dimension of queries the dimension of values. And this dimension is typically much lower. So think of it over 100. So your D model is typically O over 100, O over 1,000.

**中文**

这基本上就是它的数量级。而注意力层（attention layer），如果你们还记得，基本上由投影矩阵（projection matrices）构成。投影矩阵的维度是多少？是 D model 乘以键（keys）的维度，到查询（queries）的维度、值（values）的维度。而这个维度通常小得多。可以把它想成 over 100 \[字幕疑误，可能指 100 的数量级\]。而 D model 通常是 O over 100、O over 1,000 \[字幕疑误，可能指 100、1,000 的数量级\]。

### [18:26](https://www.youtube.com/watch?v=Q5baLehv5So&t=1106s) · b000035

**English**

And then the projection here, the DFF is O over 1,000, O over 10,000. Cool. So is everyone now convinced that this is a good way, good place to put the mixture of experts? Yeah? Cool. So this is actually how it's done. So in modern day LLMs, this idea of not involving everyone in the computation of the next token prediction is such that you would put the mixture of experts where the fn is just basically here.

**中文**

然后，这里的投影，DFF 是 O over 1,000、O over 10,000 \[字幕疑误，可能指 1,000、10,000 的数量级\]。好。现在大家都相信这里是放 mixture of experts 的一个好位置了吗？是吗？好。实际上就是这么做的。在如今的 LLM 中，不让所有参数都参与下一个 token 预测计算的这个想法，就是把 mixture of experts 放到 fn \[字幕疑误，可能指 FFN\] 所在的位置，基本上就是这里。

### [19:12](https://www.youtube.com/watch?v=Q5baLehv5So&t=1152s) · b000036

**English**

And typically you would have a sparse mixture of experts. So back to your question, so these experts are actually feedforward neural network. So you would have several networks that you can train, but you would only activate one.

**中文**

通常会使用 sparse mixture of experts。回到你的问题，这些专家实际上就是 feedforward neural network。你会有多个可以训练的网络，但只激活其中一个。

### [19:32](https://www.youtube.com/watch?v=Q5baLehv5So&t=1172s) · b000037

**English**

So typically, k would be equal to 1. It can be also equal to 2 but it would only be a subset. So that's my point. And this routing would be done at the token level. So if you remember, the decoder, it basically takes something as inputs. So a bunch of tokens. And here, what I'm saying is that each token will be processed by an expert that may be different from the other token.

**中文**

通常，k 会等于 1，也可以等于 2，但只会是其中的一个子集。这就是我想说的。而且，这种路由（routing）是在 token 级别进行的。如果你们还记得，decoder 基本上会接收一些输入，也就是一组 token。我在这里说的是，每个 token 都会由一个专家处理，而这个专家可能与处理另一个 token 的专家不同。

### [20:05](https://www.youtube.com/watch?v=Q5baLehv5So&t=1205s) · b000038

**English**

So the router here would take the representation of the token as input and figure out which expert should be best for this token to flow towards. Does this idea make sense? So I have a little illustration later on that hopefully will help. So now back to your question about how you train this model. Do you train the router separately?

**中文**

这里的 router 会把 token 的表示（representation）作为输入，判断这个 token 最适合流向哪个专家。这个想法能理解吗？后面我有个小示意图，希望能帮助大家理解。现在回到你关于如何训练这个模型的问题。router 是单独训练的吗？

### [20:36](https://www.youtube.com/watch?v=Q5baLehv5So&t=1236s) · b000039

**English**

Do you train the experts separately? So one challenge that people have is when they train these MoE-based models, to make sure that all experts are, I guess, having a weight, are being used. Because it's very possible that you train your model and that somehow only, I don't know, one or two experts always get activated.

**中文**

专家是单独训练的吗？人们在训练这些基于 MoE 的模型时，一个挑战是确保所有专家都有权重、都被用到。因为很可能，你训练模型时，不知道为什么，总是只有一两个专家被激活。

### [21:07](https://www.youtube.com/watch?v=Q5baLehv5So&t=1267s) · b000040

**English**

And the other one, they always are inactive. They are never involved in the computation. So this problem is called routing collapse. So why is it called routing collapse? It's because the router always chooses some experts, but not others. So this is a challenge. And the way people try to mitigate this challenge is by changing the loss function and adding it some extra term, which is written here.

**中文**

而其他专家始终不活跃，从来不参与计算。这个问题叫路由坍塌（routing collapse）。为什么叫 routing collapse？因为 router 总是选择某些专家，而不选择其他专家。这是一个挑战。人们缓解这个挑战的方法，是修改损失函数（loss function），加上一个额外项，就是这里写的这个。

### [21:42](https://www.youtube.com/watch?v=Q5baLehv5So&t=1302s) · b000041

**English**

So it's basically some hyperparameter alpha times the number of experts times the sum of quantities that depend on whether or not tokens went to a certain expert's eye, and then summed over all experts. So it's not super important that you completely understand exactly how that formula works. The only thing that I think you should take away from this slide is that this extra loss allows these quantities to converge more towards uniform distributions.

**中文**

它基本上是某个超参数 alpha，乘以专家数量，再乘以一些量的和；这些量取决于 token 是否去了某个 expert's eye \[字幕疑误，可能指 expert i，即专家 i\]，然后对所有专家求和。完全理解这个公式具体如何运作，并不是特别重要。我觉得你们从这张幻灯片中唯一需要记住的是，这个额外的 loss 会让这些量更趋向于均匀分布（uniform distributions）。

### [22:27](https://www.youtube.com/watch?v=Q5baLehv5So&t=1347s) · b000042

**English**

So what are these quantities, just as a reminder. So f of I is the fraction of tokens that are routed to expert I. And P of I is the average routing probability for expert I. So when I say that all experts should be used the same, what I'm saying is I want this probability to be kind of uniform across experts.

**中文**

再提醒一下，这些量是什么。f of I 是被路由到专家 I 的 token 所占的比例。P of I 是专家 I 的平均路由概率。所以，当我说所有专家都应该被同等使用时，我的意思是，希望这个概率在各个专家之间大致均匀。

### [22:59](https://www.youtube.com/watch?v=Q5baLehv5So&t=1379s) · b000043

**English**

Yeah.

**中文**

是的。

### [23:20](https://www.youtube.com/watch?v=Q5baLehv5So&t=1400s) · b000044

**English**

So the question is, I guess, when do you compute these quantities? So yeah, you can think of it as a regular training process. You do some mini batch, you go through the model and then you compute all these quantities. And then what you do is you do your backpropagation based on that. And I guess what I want you to remember is that this incentivizes the probability, I guess, the choice of the writer to be more uniform across experts, which is something that mitigates this routing collapse phenomenon.

**中文**

问题是，你在什么时候计算这些量？对，你可以把它看作常规训练过程。取一个小批次（mini batch），通过模型，然后计算所有这些量。之后，你就基于这些量进行反向传播（backpropagation）。我想让大家记住的是，这会促使概率，也就是 writer \[字幕疑误，可能指 router\] 的选择，在各个专家之间更加均匀，从而缓解 routing collapse 现象。

### [24:05](https://www.youtube.com/watch?v=Q5baLehv5So&t=1445s) · b000045

**English**

Yeah.

**中文**

是的。

### [24:14](https://www.youtube.com/watch?v=Q5baLehv5So&t=1454s) · b000046

**English**

So the question is, can we use Dropout? Of course. You can always bundle that with some other techniques. So people have just kind of found this to be very helpful. So speaking of other techniques, there is something that I've not talked about, which is very similar to the Dropout idea. So it's called noisy gating. Noisy gating is basically you have your predictions from the gates, but then you add some noise to it.

**中文**

问题是，我们能用 Dropout 吗？当然可以。你随时可以把它和其他技术结合起来。人们只是发现这个方法很有帮助。说到其他技术，还有一个我没讲到的东西，它与 Dropout 的思路很相似，叫带噪声门控（noisy gating）。noisy gating 基本上就是，你得到 gates 的预测，然后往里面加一些噪声（noise）。

### [24:45](https://www.youtube.com/watch?v=Q5baLehv5So&t=1485s) · b000047

**English**

So basically, it's by pure chance, it just allows other experts to be involved in the computation. So it's also some other technique. There's a bunch of techniques. But yeah, Dropout is indeed quite useful for things like overfitting. And the idea can be reused in different settings. Yep. Yep.

**中文**

基本上，它通过纯粹的随机机会，让其他专家也能参与计算。这也是另一种技术。技术有很多种。不过，对，Dropout 对过拟合（overfitting）这类问题确实很有用。这个思路也可以复用到不同情境中。对。对。

### [25:13](https://www.youtube.com/watch?v=Q5baLehv5So&t=1513s) · b000048

**English**

So the question is, how can you--so do you mean differentiable? So here, I guess, how do you take the derivative. Is that your question? How is the derivative-- can you explain a bit more what your concern is?

**中文**

问题是，你怎么能——所以你指的是可微（differentiable）吗？我想，这里是问如何求导。是这个问题吗？导数是怎么——你能再详细解释一下你的疑虑吗？

### [25:43](https://www.youtube.com/watch?v=Q5baLehv5So&t=1543s) · b000049

**English**

So I guess, to this question, so the average routing probability. So that one is a function of the gate output. That's one. PI. So I guess, your question is for FI. For FI, OK. I don't have a good answer on top of my head, but I think people have some techniques. And these days, you just don't even have to do this by hand.

**中文**

关于这个问题，平均路由概率是 gate 输出的函数。这是其中一个，PI。我想，你的问题是针对 FI。针对 FI，好。我一时想不到一个好的回答，但我想人们有一些技术。而且如今，你甚至不需要手工做这些。

### [26:15](https://www.youtube.com/watch?v=Q5baLehv5So&t=1575s) · b000050

**English**

You have the built in thing. So maybe I can follow up with you for FI. But for P of I, do you see that this one is quite clean. It's just the average of the probabilities from the gates.

**中文**

有内置的东西可以用。所以，关于 FI，我之后也许可以再跟你讨论。但对于 P of I，你能看出它很直接吧？它就是 gates 输出概率的平均值。

### [26:35](https://www.youtube.com/watch?v=Q5baLehv5So&t=1595s) · b000051

**English**

Yeah. So basically the probability--the output probability from the gate, you can think of it as just the vector being projected on a space of n, where n corresponds to your number of experts. And then it's gone through Softmax. So your output is basically summing up to one. And each of these dimensions, they represent the value corresponding to what expert I would be, I guess, used for.

**中文**

对。基本上，gate 输出的概率，你可以把它理解为一个向量被投影到 n 维空间，n 对应专家的数量。然后它经过 Softmax。因此，输出各项加起来等于 1。每个维度表示的值，对应于专家 I 会被使用的情况，我想是这样。

### [27:08](https://www.youtube.com/watch?v=Q5baLehv5So&t=1628s) · b000052

**English**

For instance, the first dimension would be for expert 1, second dimension would be for expert 2, and so on. So you just take the average of this, and this one, you can express it from all the parameters. So I think you should be fine with that one. Yeah.

**中文**

比如，第一个维度对应专家 1，第二个维度对应专家 2，依此类推。所以，你只要取它的平均值，而且这个量可以用所有参数来表示。我想，这一个应该没有问题。对。

### [27:31](https://www.youtube.com/watch?v=Q5baLehv5So&t=1651s) · b000053

**English**

So the question is if we increase the number of MoEs, does it increase the number of model parameters? So it's a great question. So it's actually one of the ideas behind MoE-based models, which is that you can scale the model without having to incur the cost of having significantly more compute at inference time. So you can increase-- so people say capacity. Can increase the capacity of your model, but you will still keep some, I guess, like controlled amount of active parameters.

**中文**

问题是，如果增加 MoE 的数量，会增加模型参数量吗？这是个好问题。实际上，这就是基于 MoE 的模型背后的一个想法：你可以扩大模型，而不必付出推理时计算量显著增加的代价。你可以增加——人们把它叫作容量（capacity）。你可以增加模型的 capacity，同时仍然把激活参数（active parameters）的数量控制在一定范围内。

### [28:08](https://www.youtube.com/watch?v=Q5baLehv5So&t=1688s) · b000054

**English**

And active parameters are the parameters that are used for a forward pass. So yeah, people just use that. So yeah, it would just increase the number of parameters. So that's why you see some MoE-based models that are even bigger than the ones that we had on the order of hundreds of billions. We even have on the order of trillions of parameters. So for instance here, one reading I recommend is switch transformer, which scaled up to one point something trillion parameters.

**中文**

active parameters 就是一次 forward pass 中用到的参数。对，人们就是这样做的。对，它会增加参数总量。所以你会看到，有些基于 MoE 的模型，甚至比我们之前说的数千亿参数量级的模型还大，达到数万亿参数量级。比如这里，我推荐的一篇读物是 switch transformer，它扩展到了 1 点几万亿参数。

### [28:41](https://www.youtube.com/watch?v=Q5baLehv5So&t=1721s) · b000055

**English**

So yeah, it's definitely more. But that being said, so if you read the paper, you will also see that these models, there are more what they call sample efficient. So they take less time to be as good as what the model would have been with a lower number of parameters. So if you draw the training curve as a function of the training time, you see that these models are typically more sample efficient.

**中文**

所以，确实更多。不过，话虽如此，如果你读这篇论文，也会看到这些模型在他们所说的样本效率（sample efficient）方面更高。它们用更少的时间，就能达到参数量更少的模型本来能达到的效果。所以，如果把训练时间作为横轴画出训练曲线，就会看到这些模型通常更具 sample efficiency。

### [29:18](https://www.youtube.com/watch?v=Q5baLehv5So&t=1758s) · b000056

**English**

Sorry.

**中文**

抱歉。

### [29:25](https://www.youtube.com/watch?v=Q5baLehv5So&t=1765s) · b000057

**English**

Yeah. Yeah, exactly. Everything here is a trade off. Everything here is a trade off. Yeah. Cool. Yeah.

**中文**

对。对，完全正确。这里的一切都是权衡（trade off）。这里的一切都是权衡。对。好。对。

### [29:41](https://www.youtube.com/watch?v=Q5baLehv5So&t=1781s) · b000058

**English**

So the question is, each attention head will have a number of experts. So it's actually regardless of the attention heads. So the attention heads, you can think of them as being independent, something else. And the number of experts is independent of that.

**中文**

问题是，每个注意力头（attention head）都会有若干专家吗？实际上，这与 attention heads 无关。你可以把 attention heads 看作独立的另一回事。专家数量与它们无关。

### [29:59](https://www.youtube.com/watch?v=Q5baLehv5So&t=1799s) · b000059

**English**

Does that make sense?

**中文**

这样能理解吗？

### [30:04](https://www.youtube.com/watch?v=Q5baLehv5So&t=1804s) · b000060

**English**

Yeah. Right. All right. Yeah. The question is whether every block will have a number. The answer is yes. And typically those weights are not shared. So typically, you-- so actually, we're going to see an example. It can very well be that layer 1, there is the expert number at all. Three that was chosen, but layer 2, there is expert number 1, and, you know, it's all free. It's trainable.

**中文**

对。没错。好的。对。问题是，每个块（block）是否都会有一定数量的专家？答案是会。而且通常这些权重不共享。通常，你——实际上，我们马上会看一个例子。很可能第 1 层选中了 expert number at all. Three \[字幕疑误，可能指 3 号专家\]，但第 2 层选中了 1 号专家。你知道，这些都是自由的，都是可训练的。

### [30:43](https://www.youtube.com/watch?v=Q5baLehv5So&t=1843s) · b000061

**English**

So the question is we will decide where the expert will go to. So all of that is decided by the gates, which is this quantity. Everything is decided by the gates, which has trainable weights. So you can think of this as just some projection from the input x to an n dimensional space, where n is the number of experts.

**中文**

问题是，由我们决定专家会去哪里吗？所有这些都是由 gates 决定的，也就是这个量。一切都由 gates 决定，而 gates 有可训练的权重。你可以把它看作从输入 x 到 n 维空间的一次投影，n 是专家的数量。

### [31:10](https://www.youtube.com/watch?v=Q5baLehv5So&t=1870s) · b000062

**English**

So the question is, at what point during the inference is it decided? So let's suppose we're at inference time. I'm going to walk you through how it works. So you have your x. So you have this attention mechanism. So it interacts with all tokens from the past given that its decoder-only. So it's like the mask. It goes here. And at the beginning of the feedforward neural network block, the token is, of course, contextual. So it has the information from these other tokens because it's attended.

**中文**

问题是，在推理的哪个时刻做出决定？假设我们现在处于推理阶段，我来带你看它如何运作。你有 x，还有这个注意力机制（attention mechanism）。由于它是 decoder-only，它会与所有过去的 token 交互。就像这个 mask。它到这里。在 feedforward neural network block 的开头，这个 token 当然已经包含上下文了。它拥有其他 token 的信息，因为它对它们进行了注意力计算。

### [31:44](https://www.youtube.com/watch?v=Q5baLehv5So&t=1904s) · b000063

**English**

And what it does is it goes here. So x first goes into G. G computes this probability distribution over all experts. And given here that we are in a sparse MoE setting, we will only choose the top k. So let's suppose the top one, just the highest probability. And we know which experts this one will be. And so as a result of that, you will only compute the output value of the expert that the input was chosen.

**中文**

接下来，它到这里。x 首先进入 G。G 计算所有专家上的这个概率分布。由于这里采用的是 sparse MoE，我们只选择 top k。假设选 top one，就是概率最高的那个。这样我们就知道会选中哪个专家。因此，你只会计算为该输入选中的那个专家的输出值。

### [32:31](https://www.youtube.com/watch?v=Q5baLehv5So&t=1951s) · b000064

**English**

So can you elaborate on that actually?

**中文**

你能具体展开说一下吗？

### [32:35](https://www.youtube.com/watch?v=Q5baLehv5So&t=1955s) · b000065

**English**

Yeah.

**中文**

是的。

### [32:40](https://www.youtube.com/watch?v=Q5baLehv5So&t=1960s) · b000066

**English**

At what point exactly? So it's after the self-attention layer. Yeah.

**中文**

具体在哪个时刻？是在 self-attention 层之后。对。

### [32:51](https://www.youtube.com/watch?v=Q5baLehv5So&t=1971s) · b000067

**English**

So the question is, do we have different classification for different heads? No. So there's only one router. So I think I understand your question. So your question is, what do you do given that you have different attention computations going on in parallel with the heads? So if you remember, the attention layer has these different heads. But at the end of it, what it does is it concatenates all the results from each of these heads and then projects it once again in the D model space.

**中文**

问题是，不同的 head 会有不同的分类吗？不会。只有一个 router。我想我理解你的问题了。你是在问，既然不同的 head 在并行进行不同的注意力计算，那么该怎么处理？如果你还记得，attention layer 有这些不同的 head。但最后，它会把每个 head 的结果拼接（concatenate）起来，然后再次投影到 D model 空间。

### [33:33](https://www.youtube.com/watch?v=Q5baLehv5So&t=2013s) · b000068

**English**

Yeah.

**中文**

是的。

### [33:38](https://www.youtube.com/watch?v=Q5baLehv5So&t=2018s) · b000069

**English**

Yeah.

**中文**

是的。

### [33:46](https://www.youtube.com/watch?v=Q5baLehv5So&t=2026s) · b000070

**English**

Yeah.

**中文**

是的。

### [33:57](https://www.youtube.com/watch?v=Q5baLehv5So&t=2037s) · b000071

**English**

Yeah. So the question is, do we have different Gs? So the only thing I can tell you is that the G is just layer specific. It's layer specific. It's trainable. So it's basically going to learn how to process all these inputs. So the G, the only thing I can tell you for your question is going to be layer specific. So the G is going to be one G for let's say the first layer, another G for the second layer, and so on. And that one is going to be trained. Cool. Great.

**中文**

对。问题是，我们会有不同的 G 吗？我能告诉你的是，G 是每层特有的。每层特有，而且是可训练的。它基本上会学习如何处理所有这些输入。所以，针对你的问题，我能说的是，G 是每层特有的。比如，第 1 层有一个 G，第 2 层有另一个 G，依此类推。而这个 G 会被训练。好。很好。

### [34:28](https://www.youtube.com/watch?v=Q5baLehv5So&t=2068s) · b000072

**English**

Looking at the time. Do we have any other questions here?

**中文**

看一下时间。这里还有其他问题吗？

### [34:34](https://www.youtube.com/watch?v=Q5baLehv5So&t=2074s) · b000073

**English**

We're good. Perfect. So now I just wanted to show you a cool thing that I believe the Mistral team was showing in one of their papers. So what they're showing here was for a given piece of text, to show in which experts each token was rooted. So as we noted before, so experts are different from one layer to another.

**中文**

没有了。很好。现在我想给你们看一个很有意思的东西，我记得 Mistral 团队在他们的一篇论文中展示过。这里展示的是，对于一段给定文本，每个 token 被 rooted \[字幕疑误，可能指 routed，即路由\] 到了哪些专家。正如我们前面提到的，不同层的专家是不同的。

### [35:08](https://www.youtube.com/watch?v=Q5baLehv5So&t=2108s) · b000074

**English**

So I believe here, for layer 0, so it's like for one given layer. And we do see that roughly, these tokens, I guess, they leverage like a uniform amount of experts, more or less. What you would not want to see is to have every token be the same color. But luckily it is not. But yeah, so that's one cool way of just representing how the routing is done is to just have your input text and just represent where each token-- in which experts each token went.

**中文**

我想这里是第 0 层，也就是某个给定层。我们确实看到，这些 token 大致上比较均匀地使用了各个专家，差不多是这样。你不希望看到每个 token 都是同一种颜色。幸运的是，这里并不是。对，这是一种很有意思的路由可视化方式：把输入文本展示出来，再标出每个 token 去了哪里，也就是去了哪些专家。

### [35:50](https://www.youtube.com/watch?v=Q5baLehv5So&t=2150s) · b000075

**English**

Cool. OK. So what we just saw was one way that modern day LLMs changed their architecture to incorporate the fact that we may want to scale the model, but not increase the computation complexity for one forward pass. And we saw that with MoEs. So you will see a lot of MoE-based LLMs out there.

**中文**

好。好的。我们刚才看到的是，如今的 LLM 修改架构的一种方式，用来满足这样的需求：我们可能想扩大模型，但不增加一次 forward pass 的计算复杂度（computation complexity）。我们通过 MoE 看到了这一点。因此，你会看到很多基于 MoE 的 LLM。

### [36:21](https://www.youtube.com/watch?v=Q5baLehv5So&t=2181s) · b000076

**English**

And now what we will do is knowing that we have an LLM, we're going to focus on--don't worry. We're going to focus on how a response is being generated. So remember, when I told you that these modern day LLMs, what they do is they take some text in and they have some text out. So it's typically these task of next token prediction. So you have a token in.

**中文**

接下来，既然我们已经有了一个 LLM，我们要关注——别担心。我们要关注回答是如何生成的。还记得我说过，如今这些 LLM 接收一些文本作为输入，再输出一些文本。这通常就是下一个 token 预测（next token prediction）任务。你输入一个 token。

### [36:51](https://www.youtube.com/watch?v=Q5baLehv5So&t=2211s) · b000077

**English**

So let's say, beginning of sentence, you go through your LLM and it just generates the next word or the next token. So A, and then you take A, and then it goes to teddy. And then teddy bear is, et cetera, et cetera. But so far, we have never really dug into exactly how we chose the next token. So what we're going to do right now is to see exactly how we're generating the next token.

**中文**

比如，句子开头，经过 LLM，它就生成下一个词或下一个 token。比如 A，然后你把 A 输入进去，接着生成 teddy。然后是 teddy bear is，等等，等等。但到目前为止，我们还没有真正深入探讨，究竟如何选择下一个 token。现在我们就来具体看看，下一个 token 是如何生成的。

### [37:26](https://www.youtube.com/watch?v=Q5baLehv5So&t=2246s) · b000078

**English**

So as you know, here, our LLM is just a decoder-only architecture. So here, what you have is a decoder with your inputs here, and then your output there. So let's suppose for a second that everything that's happening in the middle. And we're just obtaining output probabilities that are going to look a little bit like this. So given a token or some sequence of tokens as inputs, you have an output probability distribution that represents what the model thinks is the likelihood that there will be a next token, let's say, that is equal to A, to airplane, to fluffy, et cetera.

**中文**

大家知道，这里的 LLM 就是 decoder-only 架构。这里有一个 decoder，输入在这里，输出在那里。我们暂且假设，中间发生的所有事情。然后，我们得到的输出概率看起来有点像这样。给定一个 token 或一段 token 序列作为输入，你会得到一个输出概率分布，表示模型认为下一个 token 比如等于 A、airplane、fluffy 等的可能性。

### [38:15](https://www.youtube.com/watch?v=Q5baLehv5So&t=2295s) · b000079

**English**

So this is what you have. So now my question to you is, if we told you we have some sequence as inputs and we want to choose the next token, and if I told you that our model is giving out actually a probability distribution, I guess, how would you choose the next token based on this?

**中文**

这就是你得到的东西。现在我想问大家，如果我们告诉你，有一段序列作为输入，我们想选择下一个 token，而且模型实际上给出的是一个概率分布，那么，你会如何依据它选择下一个 token？

### [38:41](https://www.youtube.com/watch?v=Q5baLehv5So&t=2321s) · b000080

**English**

Sorry. Great. The token with maximum probability. OK, great. So yes, the first idea. Let's just take the token with highest probability.

**中文**

抱歉。很好。概率最大的 token。好的，很好。对，第一个想法就是，直接取概率最高的 token。

### [38:55](https://www.youtube.com/watch?v=Q5baLehv5So&t=2335s) · b000081

**English**

So it's a very natural approach. But I'm not sure if you've been using things like ChatGPT or Gemini. Every time you ask something, it always responds something that is slightly different. So if you always choose the token with the highest probability, given that the computation here, we're going to see is all deterministic. What that means is you're always going to generate the same thing regardless of, I guess, with the same input.

**中文**

这是一个很自然的方法。不过，不知道你们有没有用过 ChatGPT 或 Gemini 之类的东西。每次你提问，它给出的回答总会略有不同。如果你总是选择概率最高的 token，而这里的计算，我们会看到，都是确定性的（deterministic），那么这意味着，对于相同的输入，你总会生成相同的内容。

### [39:33](https://www.youtube.com/watch?v=Q5baLehv5So&t=2373s) · b000082

**English**

So that's one limitation. So it's not very diverse. The second problem is if you choose the highest probability token on, I guess, iterative basis, your locally optimal, but you're not necessarily globally optimal. So what does that mean? So I guess, if you think about it, our objective is for us to produce a sequence, an output sequence of tokens that is, I guess, of a high probability.

**中文**

这是一个局限：不够多样。第二个问题是，如果你每一步都选择概率最高的 token，那么你得到的是局部最优（locally optimal），但未必是全局最优（globally optimal）。这是什么意思？仔细想想，我们的目标是生成一段序列，一段概率较高的输出 token 序列。

### [40:11](https://www.youtube.com/watch?v=Q5baLehv5So&t=2411s) · b000083

**English**

But the problem is, if you always choose the highest probability token, you will not necessarily obtain the highest probability sequence. Are you convinced of this statement, by the way? So let me give you an example. So let's suppose you have the next token where one token is 0.8, the other one is 0.7. And then you choose to go with the 0.8. No, actually, it's not 0.7 because it has to sum to 1. So let's say 0.2. So let's suppose if you go ahead with the sequence that starts with the 0.8, let's suppose all other token probabilities are very low.

**中文**

但问题是，如果你总是选择概率最高的 token，不一定会得到概率最高的序列。顺便问一下，大家认同这个说法吗？我来举个例子。假设下一个 token 的候选中，一个 token 的概率是 0.8，另一个是 0.7。然后你选择 0.8 的那个。不，实际上不能是 0.7，因为它们加起来必须等于 1。那么就说是 0.2。假设你沿着以 0.8 开头的那条序列继续，后面所有 token 的概率都很低。

### [40:52](https://www.youtube.com/watch?v=Q5baLehv5So&t=2452s) · b000084

**English**

Basically, you will have an output sequence that will have a lower probability than let's say, the other path, which would, let's suppose, have higher probability predictions in the later steps. So we're going to see this in a second. But this is the idea. So if you choose the highest predicted probability, it's a good first idea. But it's locally optimal, but not necessarily globally optimal. And this is the reason why we have a second method that is about keeping track of the k most probable path.

**中文**

那么，你得到的输出序列，概率基本上就可能低于另一条路径；假设那条路径后续步骤的预测概率更高。我们马上会看到这个例子。但思路就是这样。选择预测概率最高的 token，是个不错的初步想法。不过，它是局部最优，未必是全局最优。因此，我们有第二种方法，也就是跟踪概率最高的 k 条路径。

### [41:35](https://www.youtube.com/watch?v=Q5baLehv5So&t=2495s) · b000085

**English**

So I'm not sure if you've heard of beam search. So that's what beam search does. So here, k, is sometimes called the beam size or the beam width. So if you hear these terms, these are just names that are given to the number of paths that we keep track of. And so this works as follows. So let's suppose we start our generation with the beginning of sentence token. We want to figure out what the next token is.

**中文**

不知道你们是否听说过束搜索（beam search）。beam search 做的就是这个。这里的 k 有时被称为束大小（beam size）或束宽（beam width）。所以，如果听到这些术语，它们只是我们所跟踪的路径数量的名称。它的工作方式如下。假设我们从句首 token 开始生成，我们想确定下一个 token 是什么。

### [42:07](https://www.youtube.com/watch?v=Q5baLehv5So&t=2527s) · b000086

**English**

So let's suppose we have here, in this example, a very basic example like three tokens. And let's suppose the two highest probable tokens are A and the. So if we have k equal to 2, what we're going to do is to keep track of these two branches. So that's the first iteration. The second iteration is we're going to look at all the probabilities of next token prediction for these two tokens.

**中文**

假设在这个非常简单的例子中，只有三个 token。假设概率最高的两个 token 是 A 和 the。如果 k 等于 2，我们就跟踪这两个分支。这是第一次迭代。第二次迭代，我们会查看这两个 token 之后所有 next token prediction 的概率。

### [42:41](https://www.youtube.com/watch?v=Q5baLehv5So&t=2561s) · b000087

**English**

And we're going to always save the two most probable paths. And here, for instance, let's suppose if it's like the, and then fluffy and then A and cute. So back to what I was saying earlier, so what I was saying was here, if you were choosing the path that went along the highest probability token path, like the the, it's very much possible that the highest probability token after there would be a much lower probability than the one after A.

**中文**

我们始终保留概率最高的两条路径。比如这里，假设是 the 后面接 fluffy，以及 A 后面接 cute。回到我刚才说的，如果你选择了经过概率最高的 token 的路径，比如 the，那么它后面概率最高的 token，其概率很可能远低于 A 后面的那个。

### [43:21](https://www.youtube.com/watch?v=Q5baLehv5So&t=2601s) · b000088

**English**

And so this is what beam search tries to do. It tries to have a more globally optimal solution. So let's suppose we continue that. And then at the end of the day, we obtain, I guess, a number of potential, I guess, choices and the k potential choices. And then we pick the one that is the highest, likely, the sequence with the highest probability. So people typically what they do is they take the sum of the logarithm of the probabilities of the tokens.

**中文**

这就是 beam search 试图做的事。它试图找到更接近全局最优的解。假设我们继续下去，最后会得到若干个潜在选项，也就是 k 个候选。然后，我们选出概率最高的那个，也就是概率最高的序列。通常，人们会对各个 token 的概率取对数，再求和。

### [43:56](https://www.youtube.com/watch?v=Q5baLehv5So&t=2636s) · b000089

**English**

So what they say is they say, OK. So the log probability of the sequence is the sum of the log probability of each next token prediction. So it's the log probability of A, knowing BOS, and then cute, knowing BOS and A, and so on and so forth. But I just want to point out one limitation of this approach, which is that the more you generate tokens, the lower your, I guess, end sequence probability will be.

**中文**

也就是说，序列的对数概率（log probability），等于每次 next token prediction 的 log probability 之和。也就是已知 BOS 时 A 的 log probability，加上已知 BOS 和 A 时 cute 的 log probability，依此类推。不过，我想指出这种方法的一个局限：生成的 token 越多，最终序列的概率就越低。

### [44:37](https://www.youtube.com/watch?v=Q5baLehv5So&t=2677s) · b000090

**English**

Because if you think about it, all these probabilities are between 0 and 1. So think of it like in the multiplied sense. So let's suppose you have the probability of the whole sequence, which is just a multiplication of the probability of the next token. The more you add probabilities below, like less than 1, the more this quantity will go towards 0. So I guess this method, as is, will prioritize sequences that are shorter.

**中文**

因为仔细想想，这些概率都在 0 到 1 之间。你可以从乘法的角度来看。假设整个序列的概率，就是各个下一个 token 概率的乘积。你乘进去的小于 1 的概率越多，这个量就越趋向于 0。因此，这种方法照原样使用，会优先选择较短的序列。

### [45:14](https://www.youtube.com/watch?v=Q5baLehv5So&t=2714s) · b000091

**English**

And so for that reason, beam search has some additional term that basically counteracts that effects. So something on the order of 1 over number of tokens to the power of something. So in practice, there is some technique to make sure that things kind of work relatively well. OK. Let's suppose we figure out all these things.

**中文**

所以，beam search 会加入一些额外项，基本上用来抵消这种影响。大概是 1 除以 token 数量的某个次方这样的东西。因此，实践中会有一些技术，确保整体运作得比较好。好。假设我们已经解决了这些问题。

### [45:44](https://www.youtube.com/watch?v=Q5baLehv5So&t=2744s) · b000092

**English**

The problem is that we need to keep track of this most probable path. We need to do all this kind of saving, et cetera. And it requires a lot of computation. And the other thing is we're still interested in the most probable path, which basically will lead to a sequence that is very--that the model thinks is very likely. But sometimes what you want is for your output to be more diverse or more creative.

**中文**

问题在于，我们需要跟踪这些概率最高的路径，需要进行各种保存操作，等等。这需要大量计算。另一个问题是，我们仍然关注概率最高的路径，基本上会得到一个非常——模型认为非常可能的序列。但有时，你希望输出更多样，或者更有创造性。

### [46:19](https://www.youtube.com/watch?v=Q5baLehv5So&t=2779s) · b000093

**English**

So that's why beam search is actually not something that people typically use. People use beam search for things like machine translation, where you actually need to have something that is close to something being very likely. But actually, people use a third method. And this method is called also the sampling method. So I told you we have a probability distribution over tokens regarding what the next token should be.

**中文**

这就是为什么 beam search 实际上不是人们通常使用的方法。人们会把 beam search 用于机器翻译（machine translation）之类的任务，因为这些任务确实需要一个接近高概率结果的输出。但实际上，人们使用的是第三种方法，也叫采样方法（sampling method）。我说过，对于下一个 token 应该是什么，我们有一个覆盖各个 token 的概率分布。

### [46:53](https://www.youtube.com/watch?v=Q5baLehv5So&t=2813s) · b000094

**English**

And so what people do is they just sample the next token using that probability distribution.

**中文**

人们所做的，就是按照这个概率分布采样下一个 token。

### [47:04](https://www.youtube.com/watch?v=Q5baLehv5So&t=2824s) · b000095

**English**

Does this make sense? So in this example, fluffy, gentle, kind, and let's say smart will have a higher probability of being drawn as opposed to let's say airplane, that have a lower probability of occurring. Non-zero probability, but they have a probability of occurring. Cool? Any questions so far? Yeah.

**中文**

这样能理解吗？在这个例子中，fluffy、gentle、kind，以及比如 smart，被抽到的概率会更高；相比之下，比如 airplane，出现的概率更低。不是零概率，但它们有出现的概率。好？到目前为止有什么问题吗？对。

### [47:35](https://www.youtube.com/watch?v=Q5baLehv5So&t=2855s) · b000096

**English**

Right. So the question is it's not for training, it's for inference. Yes, correct. Think of it as a response generation. So let's suppose you have your model that is trained. What you want is to generate an output. So what would you do? Yeah. So I guess, just to complete my answer, so during training, what you would do is care about the output probabilities and then compare them with the actual label, which is, most of the time, like your hard label. And yeah, this is what you would compare.

**中文**

对。问题是，这不是用于训练，而是用于推理。对，没错。可以把它看作回答生成（response generation）。假设你有一个训练好的模型，你想生成一个输出。那么你会怎么做？对。补充一下我的回答，在训练过程中，你关心的是输出概率，然后将其与实际标签（label）比较，大多数时候就是硬标签（hard label）。对，你比较的就是这些。

### [48:06](https://www.youtube.com/watch?v=Q5baLehv5So&t=2886s) · b000097

**English**

So this one is let's suppose you have an LLM that is trained, how would you generate a response?

**中文**

而这里讨论的是，假设你有一个训练好的 LLM，你会如何生成回答？

### [48:12](https://www.youtube.com/watch?v=Q5baLehv5So&t=2892s) · b000098

**English**

Cool. Are on goods? Yeah.

**中文**

好。Are on goods? \[字幕疑误，可能是在问大家是否都跟上了\] 对。

### [48:26](https://www.youtube.com/watch?v=Q5baLehv5So&t=2906s) · b000099

**English**

Yeah. So the question is, how do you do sampling in this situation. So it's actually my next slides. But I just want to make sure everyone was on the same page regarding just the intuition. So highest probability is called greedy decoding. It's probably not something that we want. Beam search is a little bit better. It's more something that is globally optimal. It's not globally optimal but more towards that. So it's better but it lacks diversity. It lacks creativity. Which is why what we want to do is to actually sample each token.

**中文**

对。问题是，这种情况下如何进行 sampling？这实际上就是我接下来几张幻灯片的内容。不过，我想先确保大家对直观思路有一致的理解。选择最高概率的做法叫贪心解码（greedy decoding）。这可能不是我们想要的。beam search 稍好一点，更接近全局最优。它并不是全局最优，只是更朝那个方向靠近。因此它更好，但缺少多样性，缺少创造性。所以，我们想做的是对每个 token 进行 sampling。

### [49:02](https://www.youtube.com/watch?v=Q5baLehv5So&t=2942s) · b000100

**English**

And I guess, we have a few methods that also restrict the kinds of tokens that we want to sample from. Because I mentioned, these very low probability tokens, they can still, theoretically, be sampled. But it's not necessarily something that we want. So what people do is they typically restrict the highest probability tokens and only sample from them.

**中文**

我们还有几种方法，会限制参与 sampling 的 token 类型。因为我提到过，那些概率很低的 token 理论上仍然可能被采样到，但这不一定是我们想要的。因此，人们通常会把范围限制在概率最高的 token 中，只从它们里面 sampling。

### [49:35](https://www.youtube.com/watch?v=Q5baLehv5So&t=2975s) · b000101

**English**

So you may have heard of this term, Top-k sampling. Who has heard of this term? Yeah, a little bit. So what you do is you select the top highest probable k--so the top k highest probable tokens and you sample from them. So let's suppose if k is equal to 4, you take the four highest probable. And then you just sample with them. And there's something else that is quite similar in idea which is called Top-p.

**中文**

你们可能听说过 Top-k 采样（Top-k sampling）这个术语。谁听说过？对，有一些。做法是，选出概率最高的 k 个——也就是概率最高的 top k 个 token，然后从中 sampling。假设 k 等于 4，你就取概率最高的四个，再从它们中 sampling。还有一种思路很相似的方法，叫 Top-p。

### [50:06](https://www.youtube.com/watch?v=Q5baLehv5So&t=3006s) · b000102

**English**

So Top-p is that you limit yourself to the top to the highest probable tokens such that their cumulative probability is more than a threshold p. So again, it will do the same thing. It will select the highest probable tokens. But then there is a part that I still left out, which is how do you obtain these probabilities to start with?

**中文**

Top-p 是把范围限制在概率最高的一批 token 中，使它们的累积概率（cumulative probability）超过阈值 p。同样，它做的事情类似：选择概率最高的 token。不过，还有一部分我没讲，那就是，这些概率最初是如何得到的？

### [50:41](https://www.youtube.com/watch?v=Q5baLehv5So&t=3041s) · b000103

**English**

So if you remember, here, I had mentioned that we just assume we have the probabilities. We just have them and we want to choose what the next token is. But now the question that I'm asking is now that we know what we will do with these probabilities, I guess, one question is, how do you obtain these probabilities to start with.

**中文**

如果你们还记得，我在这里说过，我们先假设已经有这些概率。概率已经有了，我们想选择下一个 token。但现在我要问的是，既然我们已经知道如何使用这些概率，那么这些概率最初是如何得到的？

### [51:07](https://www.youtube.com/watch?v=Q5baLehv5So&t=3067s) · b000104

**English**

So if you remember, these transformer-based architecture basically computes an encoder representation of the input. And what you have is some final layers at the very top of the figure, which aims at projecting the vector into the space of the vocabulary.

**中文**

如果你们还记得，这些基于 transformer 的架构，基本上会计算输入的编码器表示（encoder representation）。图的最上方有一些最终层，它们的作用是把向量投影到词表（vocabulary）空间。

### [51:37](https://www.youtube.com/watch?v=Q5baLehv5So&t=3097s) · b000105

**English**

Because what you want to do is to have a probability number for how probable it is for you to sample a given token. So here, what you would do is at the very top of the architecture, have your input, which is your encoded embedding of the token. Go through a linear layer, which basically projects your D model vector into a space of dimension size of v.

**中文**

因为你想要为采样到某个给定 token 的可能性，得到一个概率值。所以，在架构最顶端，你会把输入，也就是 token 编码后的 embedding，送入线性层（linear layer），基本上将 D model 向量投影到一个维度大小为 v 的空间。

### [52:12](https://www.youtube.com/watch?v=Q5baLehv5So&t=3132s) · b000106

**English**

And of course, what you want is probabilities. So you would have a Softmax layer, which basically converts everything to probabilities such that everything sums to 1. And in order to compute the probabilities, this is the formula that you would use, which is the Softmax layer. So there is a hyperparameter that is quite important that I want to talk to you about, which is the temperature T. And so this is where it pops up.

**中文**

当然，你想得到的是概率。因此，你会有一个 Softmax 层，它基本上把所有值转换为概率，使它们的和等于 1。计算这些概率时，你会使用这个公式，也就是 Softmax 层。有一个相当重要的超参数，我想和大家讲一下，就是温度（temperature）T。它就在这里出现。

### [52:49](https://www.youtube.com/watch?v=Q5baLehv5So&t=3169s) · b000107

**English**

So you have the probability of the next token being a given word, which is equal to the exponential of the input with respect to the given word over temperature. And then you normalize that by the sum of all the other exponential of the quantity over t. And now what we're going to see is what that T is used for or what that T actually does in practice.

**中文**

下一个 token 是某个给定词的概率，等于该词对应的输入除以 temperature 后取指数（exponential）。然后，用其他所有对应量除以 t 后的指数之和对它归一化。现在我们要看的是，T 有什么用，或者说 T 在实践中究竟起什么作用。

### [53:23](https://www.youtube.com/watch?v=Q5baLehv5So&t=3203s) · b000108

**English**

So before we go into that, just one question. Has anyone heard about temperatures when it comes to response generation? Yeah. Cool. So hopefully that will give you a better idea of how the temperature kind of influences your output predictions. So I guess, the question that I want to ask you is, what would be the impact of having a low temperature versus a high temperature?

**中文**

开始之前，先问一个问题。有谁听说过回答生成中的 temperature？有。好。希望接下来的内容能让你们更好地理解 temperature 如何影响输出预测。我想问大家的是，低 temperature 和高 temperature 会分别产生什么影响？

### [54:04](https://www.youtube.com/watch?v=Q5baLehv5So&t=3244s) · b000109

**English**

So low temperature would correspond to a diverse of what?

**中文**

所以，低 temperature 会对应于什么样的多样……？

### [54:21](https://www.youtube.com/watch?v=Q5baLehv5So&t=3261s) · b000110

**English**

Yeah.

**中文**

是的。

### [54:26](https://www.youtube.com/watch?v=Q5baLehv5So&t=3266s) · b000111

**English**

Yeah.

**中文**

是的。

### [54:36](https://www.youtube.com/watch?v=Q5baLehv5So&t=3276s) · b000112

**English**

So we will come to that in a second. So yeah, do you have a--

**中文**

我们马上会讲到。对，你有没有一个——

### [54:42](https://www.youtube.com/watch?v=Q5baLehv5So&t=3282s) · b000113

**English**

a lower temperature? Increase in temperature. So I guess, back to the explanation about, I guess, lowering the temperature and what impact it will do to the--so I guess do you have a suggested response to that? I guess, lower temperature. Let's suppose you have a lower temperature, what happens?

**中文**

更低的 temperature？提高 temperature。我想，回到降低 temperature 的解释，以及它会对——产生什么影响。你有没有一个可能的回答？我想，较低的 temperature。假设 temperature 更低，会发生什么？

### [55:16](https://www.youtube.com/watch?v=Q5baLehv5So&t=3316s) · b000114

**English**

Yeah. So I guess-- so the long story short is low temperature will create a spiky distribution and then high temperature will create a uniform distribution. But I guess, I think you had the right intuition.

**中文**

对。我想——长话短说，低 temperature 会产生尖峰状分布（spiky distribution），而高 temperature 会产生均匀分布。不过，我觉得你的直觉是对的。

### [55:35](https://www.youtube.com/watch?v=Q5baLehv5So&t=3335s) · b000115

**English**

I'm going to maybe write this in more mathematical terms.

**中文**

我也许可以用更数学化的方式把它写出来。

### [55:41](https://www.youtube.com/watch?v=Q5baLehv5So&t=3341s) · b000116

**English**

OK. Let's suppose you have your probability, which is the exponential of xi over t, over the sum of exponential of xj over t. So just mathematically, you can actually prove what is happening here. So let's suppose you have the index of the highest xi.

**中文**

好。假设你的概率是 xi 除以 t 后取指数，再除以所有 xj 除以 t 后的指数之和。从数学上，你实际上可以证明这里会发生什么。假设你有最大的 xi 对应的索引。

### [56:17](https://www.youtube.com/watch?v=Q5baLehv5So&t=3377s) · b000117

**English**

So let's call that k. So let's suppose what I do is I will factor by this quantity. So actually, here, I don't have space. So let's do here. So it will be ae of k temperature. And then here, you have the sum of over all j of exponential of xj over t minus xk over t.

**中文**

我们把它叫作 k。假设我这样做，把这个量提出来。实际上，这里没地方了。那就写在这里。这里会是 ae of k temperature \[字幕疑误，可能指与 xk 除以 temperature 的指数有关的项\]。然后这里是对所有 j 求和，求和项是 xj 除以 t 减去 xk 除以 t 后的指数。

### [56:58](https://www.youtube.com/watch?v=Q5baLehv5So&t=3418s) · b000118

**English**

So what I did is I just multiplied the numerator and the denominator by exponential of xk over t. So I multiplied numerator and denominator. And of course, they cancel out. But then what I have here is xy minus xk over t. And here, xj minus k over t. So when i is equal to k, this term is 0. It's exactly 0, regardless of the temperature.

**中文**

我所做的，就是把分子和分母都乘以 xk 除以 t 的指数。我把分子和分母都乘了这个量。当然，它们会抵消。但这样，这里得到的是 xy 减去 xk，再除以 t \[字幕疑误，xy 可能指 xi\]。这里是 xj 减去 k，再除以 t \[字幕疑误，k 可能指 xk\]。当 i 等于 k 时，这一项是 0。无论 temperature 是多少，它都恰好是 0。

### [57:32](https://www.youtube.com/watch?v=Q5baLehv5So&t=3452s) · b000119

**English**

And here, xj minus xk is always negative or 0.

**中文**

而这里，xj 减去 xk 总是负数或 0。

### [57:44](https://www.youtube.com/watch?v=Q5baLehv5So&t=3464s) · b000120

**English**

So here, if i is equal to k, you have 0 over t. So here, it's 1. And then you have 1 plus--I guess, some quantity. So j minus xk over t, which is going to be negative. So the t going to 0. So that one will be, I guess, going to, let's say, minus infinity.

**中文**

所以在这里，如果 i 等于 k，就得到 0 除以 t。因此，这里是 1。然后是 1 加上——我想，是某个量。j 减去 xk，再除以 t \[字幕疑误，j 可能指 xj\]，这个量会是负数。当 t 趋于 0 时，这个量就会，我想，趋于负无穷。

### [58:22](https://www.youtube.com/watch?v=Q5baLehv5So&t=3502s) · b000121

**English**

So exponential of minus infinity is 0. So what you will end up with is something where for i equal to k, you will have a non-zero probability. But then for i not equal to k, you will have 0 over something that is not equal to 0, which is 0.

**中文**

所以，负无穷的指数是 0。最终得到的结果就是，当 i 等于 k 时，概率非零。但当 i 不等于 k 时，得到的是 0 除以一个不等于 0 的量，结果就是 0。

### [58:53](https://www.youtube.com/watch?v=Q5baLehv5So&t=3533s) · b000122

**English**

So just mathematically, if you factor by exponential of xk over t, where k is the index of the highest value, I guess, the highest logit or the highest activation vector, can actually show that for a small temperature, only the highest--so the index of the, I guess, highest value will be the one that will be highest probable with the spike there.

**中文**

所以，仅从数学上来说，如果你把 xk 除以 t 的指数提出来，其中 k 是最大值的索引，我想，也就是最大的 logit 或最大的激活向量（activation vector），实际上就能证明，当温度（temperature）较小时，只有最大的——也就是说，我想，最大值对应的索引会具有最高的概率，在那里形成一个尖峰。

### [59:30](https://www.youtube.com/watch?v=Q5baLehv5So&t=3570s) · b000123

**English**

And then when you have a high temperature, basically it will look like a uniform distribution because all these quantities, so when t tends to plus infinity, this tends to 0. So exponential of 0 is just e. Sorry, not e, 1. So 1. So it's 1 over the number of j. So it's 1. So just a uniform distribution across all the tokens of your vocabulary.

**中文**

而当温度较高时，基本上看起来就像均匀分布（uniform distribution），因为所有这些量，也就是说，当 t 趋于正无穷时，这个量趋于 0。所以 0 的指数就是 e。抱歉，不是 e，是 1。所以是 1。所以就是 1 除以 j 的数量。所以是 1。也就是说，在词表中的所有词元（token）上形成均匀分布。

### [1:00:04](https://www.youtube.com/watch?v=Q5baLehv5So&t=3604s) · b000124

**English**

Yeah.

**中文**

对。

### [1:00:16](https://www.youtube.com/watch?v=Q5baLehv5So&t=3616s) · b000125

**English**

So the question is, how can I interpret a small--

**中文**

所以问题是，我该如何理解一个较小的——

### [1:00:27](https://www.youtube.com/watch?v=Q5baLehv5So&t=3627s) · b000126

**English**

so the question is, can I interpret that as a Gaussian? I think. So it's kind of tough because Gaussian, you have some continuous quantities in the x-axis. So here, you have tokens. So it's kind of discrete. And it's not something that you can order. So I just probably interpret that as small temperature is very spiky. So you will really have a given set of tokens that are the highest probable that will appear more. And if you have a high temperature, then basically, tokens, even the ones that were not there to be the highest probable, will actually have an adjusted probability that will be higher.

**中文**

所以问题是，我能把它理解为高斯分布（Gaussian）吗？我想是这个问题。这有点难，因为对于 Gaussian，x 轴上是一些连续的量。而这里是 token，所以是离散的。而且它们也不是能够排序的东西。所以我大概只会把它理解为：温度较小时，分布的尖峰非常明显。也就是说，某一组概率最高的 token 会出现得更多。而如果温度较高，那么基本上，即使是那些原本概率并非最高的 token，调整后的概率也会更高。

### [1:01:15](https://www.youtube.com/watch?v=Q5baLehv5So&t=3675s) · b000127

**English**

Yes. So you can think of it as some kind of scaling in that sense. So long story short, what I want to tell you is if you have a small temperature, it will encourage the next token to be geared towards being the highest probable token. And then if you have a high temperature, I guess the distribution of probabilities will be kind of closer to a uniform if you're really increase that temperature by a lot.

**中文**

是的。所以从这个意义上，你可以把它看作某种缩放。长话短说，我想告诉你的是，如果温度较低，就会促使下一个 token 更倾向于概率最高的 token。而如果温度较高，我想，概率分布就会更接近均匀分布，尤其是你把温度提高很多的时候。

### [1:01:45](https://www.youtube.com/watch?v=Q5baLehv5So&t=3705s) · b000128

**English**

So your output will be more creative. You will have tokens that you would have not drawn that would be drawn. And so what that means in practice, if you're with your favorite LLM. And let's suppose you want to, I don't know, write something very creative. So which one would you use? Would you use a low temperature or high temperature? High temperature? Yes. So if you want something that is more deterministic, more, I guess, closer to something that is very, I guess, what you think would be high quality, will use more of a lower temperature.

**中文**

所以输出会更有创意。原本不会抽到的 token，现在可能会被抽到。那么在实践中，这意味着什么呢？假设你正在使用自己最喜欢的大语言模型（LLM）。再假设你想，我不知道，写一些非常有创意的东西。那么你会用哪一种？低温度还是高温度？高温度？对。所以，如果你想要更确定的结果，更接近于，我想，你认为质量很高的那种结果，就会使用更低的温度。

### [1:02:23](https://www.youtube.com/watch?v=Q5baLehv5So&t=3743s) · b000129

**English**

So one note here is that if you have a strictly positive temperature, every time you run your model over an input, you will obtain a different output.

**中文**

这里要注意一点，如果温度严格大于 0，那么每次你针对一个输入运行模型时，都会得到不同的输出。

### [1:02:42](https://www.youtube.com/watch?v=Q5baLehv5So&t=3762s) · b000130

**English**

So something I want to point out is nothing in the transformer architecture is probabilistic. Everything is deterministic. The only thing that is not deterministic is how you sample the next token. It's the only thing that is not deterministic. So what will you do to have a deterministic output? You have t equal to 0. T equal to 0, you know for sure that your output will be just one thing and nothing else.

**中文**

我想指出的是，transformer 架构里没有任何东西是概率性的。一切都是确定性的。唯一不确定的地方，是你如何采样下一个 token。只有这一点是不确定的。那么，要获得确定性的输出，你会怎么做？让 t 等于 0。T 等于 0 时，你就能确定输出只会是一种结果，不会是其他结果。

### [1:03:18](https://www.youtube.com/watch?v=Q5baLehv5So&t=3798s) · b000131

**English**

Well, that's what it's the theoretical property. But in practice, you have some stuff that is happening in the computation that introduces some non-deterministic operations. It's much more advanced than the scope of this class, much more advanced of the scope of this class. I just want to call out that in practice, t equal to 0, may lead to different results because of this kind of practical piece.

**中文**

嗯，这是它的理论性质。但在实践中，计算过程中会发生一些事情，引入某些非确定性操作。这远远超出了这门课的范围，远远超出了这门课的范围。我只是想指出，实际使用时，t 等于 0 也可能因为这些实际层面的问题而得到不同的结果。

### [1:03:52](https://www.youtube.com/watch?v=Q5baLehv5So&t=3832s) · b000132

**English**

So what I recommend. So there's a suggested reading in case you're completely optional. So there is a very recent article around defeating non-determinism in LM inference. So I recommend that you read it in case you're interested. So the high level idea is our GPUs, our hardware, when they reduce some of these operations, sometimes they are reducing numbers that are on really different scales.

**中文**

所以我推荐的是，这里有一篇推荐阅读，如果你——完全是选读。最近有一篇关于消除语言模型（LM）推理中非确定性的文章。如果你感兴趣，我建议读一读。大致的思路是，我们的图形处理器（GPU）、我们的硬件，在对某些操作做归约（reduction）时，有时会对量级差异非常大的数字进行归约。

### [1:04:26](https://www.youtube.com/watch?v=Q5baLehv5So&t=3866s) · b000133

**English**

So the order at which these operations are happening is actually quite important. So the idea is if these operations they happen in different order, it may lead to different results. Even if in theory, it should be exactly the same, in practice, it may not be the same. And this article actually does a great job at just explaining the intuition. So yeah, just if you're interested, completely optional. Cool. I know I'm kind of late, so I guess, last thing that I want to say is let's suppose, what you want to do is to generate an output in a very specific format.

**中文**

因此，这些操作发生的顺序其实相当重要。也就是说，如果这些操作以不同顺序发生，就可能得到不同结果。即使理论上应该完全一样，实际中也未必一样。这篇文章很好地解释了其中的直觉。所以，如果你感兴趣可以看看，完全是选读。好。我知道我有点超时了，所以我想，最后要说的是，假设你想以一种非常具体的格式生成输出。

### [1:05:10](https://www.youtube.com/watch?v=Q5baLehv5So&t=3910s) · b000134

**English**

Let's suppose a JSON format. So I guess, a very naive approach would be to tell your LLM, well, please generate this in JSON. And then it produces something. And then you try to see if it's a valid JSON. If it's not, you repeat--you just tell it to generate again until it does something well. So that's the first naive approach. Well, there is a second approach that is called guided decoding.

**中文**

假设是 JSON 格式。我想，一种非常朴素的方法就是告诉 LLM：请用 JSON 生成这个。然后它生成一些内容，你再检查是不是有效的 JSON。如果不是，就重复——让它重新生成，直到生成正确为止。这是第一种朴素的方法。还有第二种方法，叫作引导解码（guided decoding）。

### [1:05:45](https://www.youtube.com/watch?v=Q5baLehv5So&t=3945s) · b000135

**English**

And what that does is during the generation process, it filters out what it calls invalid next tokens. So here, let's suppose I want to generate this JSON. I know for sure that my first token must be something that opens the--I forgot what the English word was for this, but it just opens the brackets. Yeah. Open the brackets. So you can only have this and then you can only have the property name and so on and so forth.

**中文**

它的做法是在生成过程中，过滤掉所谓的无效后续 token。这里，假设我要生成这个 JSON。我能确定，第一个 token 必须是某种打开——我忘了这个东西的英文怎么说了，总之就是左括号。对，打开括号。所以你只能先有这个，然后只能是属性名，依此类推。

### [1:06:19](https://www.youtube.com/watch?v=Q5baLehv5So&t=3979s) · b000136

**English**

And sometimes you can have more than one permitted next token, in which case you would go back to our next token strategy. Yeah.

**中文**

有时允许的下一个 token 不止一个，这种情况下就回到我们的下一个 token 选择策略。对。

### [1:06:38](https://www.youtube.com/watch?v=Q5baLehv5So&t=3998s) · b000137

**English**

So the question is, how do you restrict the other tokens? So there's a bunch of papers that go into that. We will not cover this. But I can give you some pointers. Just type finite state machine FSM context grammar. So there's a bunch of papers that do that. We will not cover that here. Cool. And I think with that, we will go to the second part with Shervin. Great. Thank you, Afshin. So now, together, we're going to look at different prompting strategies.

**中文**

所以问题是，如何限制其他 token？有不少论文讨论这个问题。我们不会讲这部分，但我可以给你一些检索方向。直接输入有限状态机（finite state machine，FSM）、上下文文法（context grammar）\[字幕疑误，可能指 context-free grammar\]。有不少论文在做这个，我们这里就不讲了。好。我想，接下来我们就进入第二部分，由 Shervin 来讲。很好。谢谢你，Afshin。现在，我们一起来看看不同的提示策略（prompting strategies）。

### [1:07:13](https://www.youtube.com/watch?v=Q5baLehv5So&t=4033s) · b000138

**English**

So now that how responses are generated, we're going to see how to get responses and how to get great responses. So let's go back to our favorite example about our cute teddy bear. So just I want to introduce one piece of vocabulary. So when you have some kind of input, you have the length of your inputs measured in number of tokens. And you will see in the literature that it can have different names. So you can see it called context length, context size , window size.

**中文**

既然现在已经知道回答是如何生成的，我们就来看看如何得到回答，以及如何得到出色的回答。回到我们最喜欢的那个可爱泰迪熊的例子。我先介绍一个术语。当你有某种输入时，输入的长度是用 token 数量来衡量的。你会在文献里看到它有不同的名称。它可以叫上下文长度（context length）、上下文大小（context size）、窗口大小（window size）。

### [1:07:48](https://www.youtube.com/watch?v=Q5baLehv5So&t=4068s) · b000139

**English**

And I think the latest tools if you code on Cursor or any other code-assisted tool, I think they call it more context length, but all these terms are equivalent and denote the same thing. OK. So now I want to take some time to discuss what can be some orders of magnitude here. So like modern day LLMs, they tend to be in the order of magnitude of tens of thousands, hundreds of thousands or millions of input tokens as inputs.

**中文**

我想，最新的工具，比如你用 Cursor 或其他代码辅助工具编程时，我想它们更常称之为 context length，但这些术语都是等价的，指的是同一件事。好。现在我想花点时间讨论一下，这里可能涉及哪些数量级。比如，当今的 LLM，输入 token 的数量往往处于几万、几十万或者几百万的数量级。

### [1:08:27](https://www.youtube.com/watch?v=Q5baLehv5So&t=4107s) · b000140

**English**

So this is the kind of input it can take. So sometimes, you hear some new LLM boosts some number. And then that number of context length is exactly that. So it's how much tokens can it accommodate in a single pass. OK. Great. And then yeah, the models, you have seen maybe some advertisement of these models. So I think at Gemini and others that are in the million territory.

**中文**

这就是它能够接受的输入规模。有时，你会听到某个新 LLM 宣称某个数字。那个 context length 的数字指的就是这个，也就是单次处理能容纳多少 token。好，很好。然后，这些模型，你可能看过一些关于它们的宣传。我想 Gemini 以及其他一些模型已经达到了百万级。

### [1:08:56](https://www.youtube.com/watch?v=Q5baLehv5So&t=4136s) · b000141

**English**

Does that mean it's all nice and pretty? If we have more context length, is it going to solve everything? Actually not. There is a phenomenon that was recently dubbed as context rot in a paper from earlier this summer, where basically, the authors are experimenting the capacity of the model to retrieve some piece of information in a test called needle in a Haystack.

**中文**

这是不是意味着一切都很好了呢？如果 context length 更长，就能解决所有问题吗？其实不是。今年夏天早些时候的一篇论文把一种现象称为上下文腐化（context rot）。基本上，作者通过一项叫作 needle in a Haystack 的测试，研究模型检索某条信息的能力。

### [1:09:27](https://www.youtube.com/watch?v=Q5baLehv5So&t=4167s) · b000142

**English**

So basically, they ask some question. And in larger and larger pieces of text, they bury the answer. And they try to look at the capacity of the model to surface that answer. And then you can see that with respect to an increasing context length, that ability to ground the information with the answer that is in the context decreases. And the paper I think is a very interesting one. It controls with respect to what else is in the context.

**中文**

基本上，他们提出某个问题，然后把答案埋在越来越长的文本中，观察模型找到那个答案的能力。你可以看到，随着 context length 增加，模型依据上下文中的答案来为信息建立依据（grounding）的能力会下降。我觉得这篇论文很有意思。它对上下文中的其他内容做了控制。

### [1:09:59](https://www.youtube.com/watch?v=Q5baLehv5So&t=4199s) · b000143

**English**

There is a term of distractors, where they put some noise and then they see distractors basically contribute in decreasing the retrieval capability. So also, what is in your context matters. So this is why in general, when you have a retrieval problem, where you want to use your LLM to solve it, you have some good incentive to try to target as much as possible, the right piece of context for your LLM to see and predict on.

**中文**

其中有个术语叫干扰项（distractors），他们加入一些噪声，然后发现 distractors 基本上会使检索能力下降。所以，上下文里放了什么也很重要。这就是为什么一般来说，当你有一个检索问题，想用 LLM 来解决时，你很有理由尽可能准确地选取合适的上下文片段，让 LLM 看到这些内容并据此预测。

### [1:10:32](https://www.youtube.com/watch?v=Q5baLehv5So&t=4232s) · b000144

**English**

OK. Great. Yep.

**中文**

好。很好。对。

### [1:11:06](https://www.youtube.com/watch?v=Q5baLehv5So&t=4266s) · b000145

**English**

Yep. Yeah. So the question is, is the context length exactly what is shown during self-attention? Yes. Yeah. And then we're going to see-- so I think we saw last time that sometimes there are some tricks that are used for the complexity of the self-attention mechanism not to be n squared. So this is what is being used to manage basically the complexity of the computations as the context length grows. Yeah. But great call out to that.

**中文**

对。是的。问题是，context length 是否就是自注意力（self-attention）中所显示的那个长度？是的，对。接下来我们会看到——我想上次我们看过，有时会用一些技巧，让 self-attention 机制的复杂度不至于是 n 的平方。这些方法就是用来在 context length 增长时管理计算复杂度的。对。这个问题提得很好。

### [1:11:37](https://www.youtube.com/watch?v=Q5baLehv5So&t=4297s) · b000146

**English**

That's exactly what is it about. OK. Great. Any questions? Any other questions? OK. Great. So now, let's define what do prompts usually look like. So there is no formal theory on how to structure a given prompt. But these are the main lines that are usually found in prompts presented to models. So you can distinguish a part that is setting up the context where you just put the setting, you make it clear to the model, what kind of query you want to issue.

**中文**

它说的正是这个。好。很好。有什么问题吗？还有其他问题吗？好。很好。现在我们来定义一下，提示（prompt）通常是什么样的。对于如何组织一个 prompt，并没有正式的理论。不过，这些是给模型的 prompt 中通常会出现的主要部分。你可以区分出一个设置上下文的部分，在那里交代情境，让模型清楚你想提出什么样的查询。

### [1:12:21](https://www.youtube.com/watch?v=Q5baLehv5So&t=4341s) · b000147

**English**

Then let's say, if you have some tasks that you want the model to perform, you have instructions. And then these instructions are some of them function that take as input something. So you add some inputs. And in order to get what you want out of the model's response, you may want to add some constraints out of it. So here, we took our favorite example with a teddy bear. The context is what is the teddy bear--basically, what is the mood of the teddy bear?

**中文**

然后，假设你有一些任务想让模型执行，就会有指令。这些指令中的一些就像接收某些东西作为输入的函数，所以你会加入一些输入。为了从模型回答中得到你想要的结果，你可能还想加一些约束。这里我们用了最喜欢的泰迪熊例子。上下文是，这只泰迪熊是什么——基本上就是，这只泰迪熊的心情如何？

### [1:12:53](https://www.youtube.com/watch?v=Q5baLehv5So&t=4373s) · b000148

**English**

What do we want to do in order to make our teddy bear happy? And then we give some input regarding where the story that we want to generate is. And then we give some constraints. If you want some other example in the LLMs that you query every day, so the context could be some sentence that says, you are ChatGPT. We are October 10.

**中文**

为了让泰迪熊开心，我们想做什么？然后，我们给出一些输入，说明我们想生成的故事发生在哪里。接着给出一些约束。如果你想看看日常使用 LLM 时的其他例子，上下文可以是这样一句话：你是 ChatGPT。今天是 10 月 10 日。

### [1:13:23](https://www.youtube.com/watch?v=Q5baLehv5So&t=4403s) · b000149

**English**

It is 4:44 PM. So you set the setup. The instructions can be basically what the user queries alongside the inputs. And then constraints might be things that you don't see as a user, but that might be present in the prompts given to the LLM, such as safety instructions. For example, do not generate any contents that might lead to harm, or things like this. So every time you see an input being fed to an LLM, I think these projections, these four dimensions can be a good mental model of seeing which pieces correspond to what goal in that structure.

**中文**

现在是下午 4:44。这样就设定了情境。指令基本上可以是用户提出的请求以及相应输入。而约束可能是你作为用户看不到、但存在于给 LLM 的 prompt 中的东西，比如安全指令。例如，不要生成任何可能导致伤害的内容，或者类似的要求。所以每当你看到某个输入被送进 LLM，我想，这些投影、这四个维度，可以成为一个很好的心智模型，帮助你理解这个结构中各个部分对应什么目标。

### [1:14:06](https://www.youtube.com/watch?v=Q5baLehv5So&t=4446s) · b000150

**English**

Does that make sense? OK, great. So now that we know what kind of mindsets we might have for inputs to an LLM, let's see how we can get an LLM to do what we want. And let's see how we can get an LLM to do what we want without tuning any weights. And we can do so with a concept called in-context learning, where the learning is a bit of a term that is overloaded because you don't actually learn anything with respect to the weights of the LLM, but you can distill some knowledge inside of it as part of the context in order to do what you want.

**中文**

这样说清楚吗？好，很好。既然我们已经知道可以用什么思路来看待 LLM 的输入，现在来看看怎样让 LLM 做我们想让它做的事。并且看看，怎样在不调整任何权重的情况下做到这一点。我们可以使用一个叫作上下文学习（in-context learning）的概念。这里的“学习”有点一词多义，因为你实际上没有对 LLM 的权重进行任何学习，但你可以把一些知识作为上下文的一部分传递进去，让它完成你想要的事情。

### [1:14:50](https://www.youtube.com/watch?v=Q5baLehv5So&t=4490s) · b000151

**English**

So you distinguish two main categories of in-context learning. So there is one category that is very simple. In mindset, it's called zero-shot. It's basically you don't give anything other than your input, your input query. You just ask the LLM to do what you want to do. And then there is another school of thought called few-shot learning, where you give examples of inputs and outputs to the LLM before asking the input that you're interested in.

**中文**

in-context learning 主要分为两类。其中一类的思路很简单，叫作零样本（zero-shot）。基本上，除了输入，也就是你的输入查询，你不提供任何其他东西，只让 LLM 做你想做的事。另一种思路叫作少样本学习（few-shot learning），也就是在提出你关心的输入之前，先向 LLM 提供一些输入和输出的例子。

### [1:15:25](https://www.youtube.com/watch?v=Q5baLehv5So&t=4525s) · b000152

**English**

So in the case of a teddy bears and a bedtime stories, so you might name your teddy bears. So maybe you have teddy bear that's called Teddy. And you generated a story. So you put your query, you put the story that you want to generate, and you give multiple such examples. And let's say you have another teddy bear that's called Bob. And then you want to generate a story for Bob. So you put all of these examples, and you ask the LLM to generate the story that you're interested in.

**中文**

在泰迪熊和睡前故事这个例子里，你可能会给泰迪熊起名字。比如有一只泰迪熊叫 Teddy，你生成了一个故事。你放入查询，放入想要生成的故事，并提供多个这样的例子。再假设你还有一只泰迪熊叫 Bob，你想为 Bob 生成一个故事。那么你就放入所有这些例子，再让 LLM 生成你想要的故事。

### [1:15:57](https://www.youtube.com/watch?v=Q5baLehv5So&t=4557s) · b000153

**English**

And then this is basically what we call a few-shots setting.

**中文**

这基本上就是我们所说的 few-shots 设置。

### [1:16:04](https://www.youtube.com/watch?v=Q5baLehv5So&t=4564s) · b000154

**English**

OK. Great. So now, generally, when you look at the performance of the resulting task, giving examples tends to steer the LLM nicely into the task that you're interested in. Just because you have given an idea to the model of what you are looking for. And then it can use what it has learned during its training process to connect the dots and basically replicates.

**中文**

好。很好。一般来说，当你看最终任务的表现时，提供例子往往能很好地引导 LLM 完成你关心的任务。原因就在于，你已经让模型知道了你在寻找什么。然后，它就能利用训练过程中学到的东西，把这些联系起来，基本上进行复现。

### [1:16:39](https://www.youtube.com/watch?v=Q5baLehv5So&t=4599s) · b000155

**English**

But of course, you need to gather such examples. So this is costly. This will put some more tokens in the context window. So you will need to more compute. But there is an interesting trade off here that we see in recent models. So they are gaining more and more reasoning capabilities, which is why I put the generally nuance in italic here. So they are generally better, few-shots, but not always.

**中文**

但当然，你需要收集这些例子，这会产生开销。它会在上下文窗口（context window）中放入更多 token，所以你需要更多计算。不过，在最近的模型中，我们看到了一个有意思的权衡。它们的推理能力越来越强，所以我在这里把“一般来说”这个限定用斜体标出来。也就是说，few-shots 一般更好，但并非总是如此。

### [1:17:11](https://www.youtube.com/watch?v=Q5baLehv5So&t=4631s) · b000156

**English**

Because these days, with these better models, people have seen that with basically making the instruction better, you could make the performance of in-context learning on par, or even better than if you provide examples, because basically, when you think of it, when you provide examples, you constrain your model into given sets of examples that are finite. So when you are at inference time, let's say, you want to perform a task on a distribution of data that has not been seen, it is harder for the model to generalize because it will try to align on what it has seen in the context.

**中文**

因为如今，对于这些更强的模型，人们发现，基本上只要改进指令，就可以让 in-context learning 的表现与提供例子相当，甚至更好。因为仔细想想，当你提供例子时，就把模型限制在了某些有限的例子集合中。所以在推理时，假设你想对一种未见过的数据分布执行任务，模型就更难泛化，因为它会试图对齐上下文中见过的内容。

### [1:17:55](https://www.youtube.com/watch?v=Q5baLehv5So&t=4675s) · b000157

**English**

Whereas if you turn your instructions into something that is more reasoning based, you explain how to do the task with natural language, it can use its reasoning abilities to actually do it. And this is something that you see more and more these days. So the literature on this, I think, is still in progress, but you have some papers like a plan and solve that's I think came out recently. And that shows if you ask the LLM to plan itself and then solve something, it can have very good performance.

**中文**

相反，如果你把指令改成更侧重推理的形式，用自然语言解释如何完成任务，它就能利用推理能力来真正完成任务。如今这种情况越来越常见。我想，这方面的文献还在发展中，不过已经有一些论文，比如 plan and solve，我想是最近发表的。它表明，如果你让 LLM 自己先制定计划，再解决问题，就能获得非常好的表现。

### [1:18:31](https://www.youtube.com/watch?v=Q5baLehv5So&t=4711s) · b000158

**English**

So yeah, this is an interesting fact. OK. Great. So now that we have seen basically the kinds of learning that we have, now, we're going to see what we can do to improve the quality of the response. So there is this concept called chain of thought, where researchers have seen that if you force the model to come up with some rationale to some answer before actually giving it, it would give higher performance.

**中文**

所以，这是一个很有意思的事实。好。很好。既然我们已经基本了解了这些学习方式，现在来看看可以怎样提高回答的质量。有一个概念叫作思维链（chain of thought）。研究人员发现，如果你要求模型在真正给出答案之前，先给出得出该答案的一些推理依据，就能获得更好的表现。

### [1:19:05](https://www.youtube.com/watch?v=Q5baLehv5So&t=4745s) · b000159

**English**

So this is what people call as chain of thought. It's basically what led you to the answer. So here, for example, if you ask yourself, how old is this teddy bear? And if you force the model to respond directly with a number, it might not be able to do the connection as to exactly why the Teddy bear is a given age. Whereas when you give the full chain of reasoning, then it becomes clear as to what led to that response.

**中文**

这就是人们所说的 chain of thought，基本上就是你如何得出答案的过程。比如在这里，你问自己，这只泰迪熊几岁了？如果你强制模型直接用一个数字作答，它可能无法建立起联系，弄清楚为什么这只泰迪熊恰好是这个年龄。相反，如果给出完整的推理链，就能清楚地看到是什么推导出了这个回答。

### [1:19:37](https://www.youtube.com/watch?v=Q5baLehv5So&t=4777s) · b000160

**English**

So I think this is the main mindset behind this technique. And basically, this is something that can be used in in-context learning. So if you give few-shot examples, how old was this Teddy bear, you give some number and then you slightly change the query. And then based on the reasoning, formatting, and then the response, the LLM can adjust the reasoning and the response accordingly. And it will force the model to output some reasoning alongside the response, which shows an improvement in basically metrics.

**中文**

我想，这就是这项技术背后的主要思路。基本上，它可以用于 in-context learning。比如你给出 few-shot 例子：这只泰迪熊当时几岁？你给出一个数字，然后稍微改变查询。接着，LLM 就可以根据推理、格式和回答，相应地调整推理与回答。这样会促使模型在给出回答的同时输出一些推理，基本上能看到指标有所改善。

### [1:20:18](https://www.youtube.com/watch?v=Q5baLehv5So&t=4818s) · b000161

**English**

OK, great. And then yeah, something else that I want to say, let's say, you want to do a task and you want to do it well. m you will always have some samples that do not work. And then for them, you want to have debugging ability. And usually when you debug with LLMs, you don't debug like the old days. You don't look at weights at the intrinsics of the LLM. What you want is something more interpretable that comes out of it in terms of tokens.

**中文**

好，很好。然后，我还想说一点，假设你想完成一项任务，而且想把它做好。m \[字幕不明\] 你总会遇到一些表现不好的样本。对于这些样本，你希望能够调试。通常，调试 LLM 时，不像过去那样调试。你不会去查看权重、查看 LLM 内部的东西。你想要的是它以 token 形式输出一些更容易解释的内容。

### [1:20:51](https://www.youtube.com/watch?v=Q5baLehv5So&t=4851s) · b000162

**English**

And usually, with these techniques, you can see the reasoning that the model had before outputting a given response. And you can debug basically what went wrong. So if you ask how old will the bear be next year. And if in the chain of thought it says, hey, we're in 2019, you know that somehow in your context, oh, maybe I put the wrong dates in there. So you can trace back to--you can do some root causing very easily.

**中文**

通常，通过这些技术，你可以看到模型在输出某个回答之前的推理，基本上就能调试哪里出了问题。比如你问，这只熊明年会是几岁？如果 chain of thought 里说，嘿，现在是 2019 年，你就知道，你的上下文里可能有问题，哦，也许我把日期写错了。所以你可以追溯到——可以很容易地进行一些根因定位。

### [1:21:24](https://www.youtube.com/watch?v=Q5baLehv5So&t=4884s) · b000163

**English**

So it's also used for that. And, exactly, in the same way as other techniques that increase the number of tokens, this is a trade off that you have to manage, that it will, of course, take more time to infer because you need to generate more tokens. But typically, we're fine with it. Any questions on COT?

**中文**

所以它也有这个用途。而且，和其他增加 token 数量的技术完全一样，这也是你需要管理的一种权衡：当然，推理会花更多时间，因为你需要生成更多 token。但通常我们可以接受。关于 COT，有什么问题吗？

### [1:21:50](https://www.youtube.com/watch?v=Q5baLehv5So&t=4910s) · b000164

**English**

OK, great. So now let's take it one step further. So I want to introduce even to make COT even stronger, you can sample your model. Several times, look at the answers it generates, and then do some majority voting to select the answer that was predicted most of the times by a given LLM. And this is what we call self-consistency, where basically, you sample responses multiple times and then parse the actual answer.

**中文**

好，很好。现在再进一步。我想介绍一下，如何让 COT 更强：你可以对模型采样多次，查看它生成的答案，然后通过多数投票（majority voting），选出这个 LLM 预测次数最多的答案。这就是我们所说的自一致性（self-consistency）。基本上，就是多次采样回答，再解析出实际的答案。

### [1:22:27](https://www.youtube.com/watch?v=Q5baLehv5So&t=4947s) · b000165

**English**

So basically, you factor out the whole reasoning and then try to target the answer. And then by majority voting, you can come up to an answer in a more robust way. Yep.

**中文**

基本上，你把整段推理排除掉，专门关注答案。然后通过 majority voting，就能以更稳健的方式得到一个答案。对。

### [1:22:50](https://www.youtube.com/watch?v=Q5baLehv5So&t=4970s) · b000166

**English**

Yep. So the question is, do you need to have some benchmark to know if it's better? And yes, absolutely. I think the paper operates on top of all the arithmetic and then mathematical based ones. And I think one tangential question to yours is how can you locate the answer and then do measure majority voting on it. So typically, you can put into the context some instruction that says, put the actual answer last. So you can just extract the last. People, I think, use regex based techniques, otherwise, to extract the answer.

**中文**

对。问题是，你是否需要某种基准测试（benchmark），来判断它是不是更好？是的，当然需要。我想这篇论文是在那些算术类和数学类 benchmark 上进行的。我想，与这个问题相关的另一个问题是，如何定位答案，再对它进行 majority voting。通常，你可以在上下文中加入一条指令：把实际答案放在最后。这样你就可以只提取最后的内容。除此之外，我想人们也会用基于正则表达式（regex）的方法来提取答案。

### [1:23:24](https://www.youtube.com/watch?v=Q5baLehv5So&t=5004s) · b000167

**English**

Or you could even think of using some other LLM to extract the answer. So there is always a way to do it. But yeah, to your point, yes, we need some benchmark and then ground truth labels to assert that this is indeed better.

**中文**

或者，你甚至可以考虑用另一个 LLM 来提取答案。所以总有办法做到。但回到你的问题，是的，我们需要某种 benchmark 和真实标签（ground truth labels），才能确定这种方法确实更好。

### [1:23:53](https://www.youtube.com/watch?v=Q5baLehv5So&t=5033s) · b000168

**English**

Yeah. So the request here-- so the question is, is it going to be sent to the same request as example? So typically, you sample it in parallel. So basically, you ask your model exactly what Afshin just mentioned. You sample from the probability distribution of BOS and whatever tokens you had, the next token. And you do that in several other kind of branches. And you do that, all of that, in parallel. And then you parse the answer at the end of it.

**中文**

对。这里的请求——问题是，它会作为例子发送到同一个请求里吗？通常，你会并行采样。基本上，就是让模型执行 Afshin 刚才讲的那个过程。你从基于序列起始标记（BOS）以及已有 token 的概率分布中，采样下一个 token。然后在其他几个分支上也这么做。所有这些都并行进行。最后再解析答案。

### [1:24:25](https://www.youtube.com/watch?v=Q5baLehv5So&t=5065s) · b000169

**English**

So basically, the latency of this process is equal, roughly, to the maximum latency of either parallel generation. Because you can do all of this in parallel. So none of these go into the context of each other. They're all done in parallel. And then you get the final answer. OK, great. All good? OK, great. So now that we have seen a few prompting techniques, I want to cover together tricks that people have come up with at inference time to make the generation as efficient as possible.

**中文**

所以基本上，这个过程的延迟大致等于各路并行生成中的最大延迟，因为这一切都可以并行执行。因此，这些生成结果都不会进入彼此的上下文，它们都是并行完成的。然后你得到最终答案。好，很好。都清楚吗？好，很好。既然我们已经看过一些 prompting 技术，我想和大家一起介绍一些人们在推理时想出的技巧，尽可能提高生成效率。

### [1:25:08](https://www.youtube.com/watch?v=Q5baLehv5So&t=5108s) · b000170

**English**

And basically, yeah, so in modern day models, you have a lot of parameters. You want to generate a lot of tokens. How do you do it the most efficiently possible? So I want us to divide this thought process into two parts. So we're going to see what methods we can come up with that give us increased efficiency on an exact level. So you exactly do the same computations as you were supposed to do, but in a more efficient way.

**中文**

基本上，如今的模型有很多参数，你又想生成很多 token。怎样才能尽可能高效地做到呢？我想把这个思考过程分成两部分。我们会看看，有哪些方法能在保持精确的前提下提高效率。也就是，你执行的计算与原本应该执行的完全相同，但方式更高效。

### [1:25:40](https://www.youtube.com/watch?v=Q5baLehv5So&t=5140s) · b000171

**English**

And I put some hints as to what kind of techniques we're going to explore. So let's try to look for techniques that avoid redundancies. Let's try to see what we could do to manage the memory in the best way. And also, let's try to see if we can reformulate the equations inside the LLM in a way that could simplify the generation in practice. Then there is a second category that we're going to explore as well.

**中文**

我放了一些提示，说明我们要探索哪些技术。我们尝试寻找能够避免冗余的技术。看看怎样才能最好地管理内存。也看看能不能重新表述 LLM 内部的方程，从而在实践中简化生成。然后还有第二类，我们也会探索。

### [1:26:14](https://www.youtube.com/watch?v=Q5baLehv5So&t=5174s) · b000172

**English**

That is going to focus on what kind of approximations it might be fine to do, and get a high quality answer at a lesser cost, but to be approximate. So we have what kind of variations we could do on the architecture? Is there something we could do on the embeddings to make them more efficient? And then maybe on the token prediction side, is there something we could do to make it faster?

**中文**

这一类重点关注：哪些近似是可以接受的，能够以更低的成本得到高质量答案，但结果是近似的。我们可以对架构做哪些变动？能不能对嵌入（embeddings）做些什么，让它们更高效？还有在 token 预测方面，能不能做些什么让它更快？

### [1:26:48](https://www.youtube.com/watch?v=Q5baLehv5So&t=5208s) · b000173

**English**

Does that sound good? So we have approximately 22 minutes. We're going to try to go through all of them here. OK. So I grouped the categories of techniques into exact and approximate techniques. But actually, we're going to look at them in a grouped manner. First, looking at the attention layer, seeing what kind of techniques we could have there. And then in a second part, we're going to look at the output layer.

**中文**

听起来可以吗？我们大约还有 22 分钟。我们会尽量把这里所有内容都讲完。好。我把技术分成了精确技术和近似技术。不过，我们实际上会按模块来讲。先看注意力层（attention layer），看看那里能采用哪些技术。第二部分再来看输出层（output layer）。

### [1:27:21](https://www.youtube.com/watch?v=Q5baLehv5So&t=5241s) · b000174

**English**

And then see what we can do at the level of token generation to make things as good as possible. So let's start at the attention level. So we have seen that for every token, you need the current token to attend to the previous ones in this masked self-attention. So let's say you generate your sequence. You are at a given token.

**中文**

然后看看在 token 生成层面，可以怎样尽可能做好。我们先从 attention 层面开始。之前我们看到，对于每个 token，在这种带掩码的自注意力（masked self-attention）中，都需要当前 token 关注前面的 token。假设你正在生成序列，目前到了某个 token。

### [1:27:52](https://www.youtube.com/watch?v=Q5baLehv5So&t=5272s) · b000175

**English**

So let's say, you have generated a cute teddy bear. And then now you are at ease. Now you have the query ease. You will compute the key representation and the value representation of ease. Because of course, you have to do it. It's your current token. But we want to have a way to reuse the past computations we had done to compute the key representation of the previous tokens and the value representation of the previous tokens.

**中文**

假设你已经生成了 a cute teddy bear，现在到了 ease \[字幕疑误，可能指 is\]。现在你的查询（query）是 ease。你会计算 ease 的键表示（key representation）和值表示（value representation）。当然，你必须这样做，因为它是当前 token。但我们希望找到一种方式，复用过去为前面的 token 计算 key representation 和 value representation 时已经完成的计算。

### [1:28:26](https://www.youtube.com/watch?v=Q5baLehv5So&t=5306s) · b000176

**English**

Does that make sense as a goal? Does everyone agree?

**中文**

这个目标清楚吗？大家都同意吗？

### [1:28:33](https://www.youtube.com/watch?v=Q5baLehv5So&t=5313s) · b000177

**English**

OK. And more precisely, basically, we want to find a way for the key and value matrices to be saved. And I'm not underlining the Q part here because of course, the query corresponding to the previous tokens are not going to be of interest for the present token. So it's like the key and value part. OK. So there is this concept of KV cache, where the goal is to store this key and value matrices somewhere, and reuse them directly from the cache.

**中文**

好。更准确地说，我们想找到一种方法，把 key 和 value 矩阵保存下来。这里我没有给 Q 部分加下划线，因为前面那些 token 对应的 query，当然不是当前 token 所关心的。所以就是 key 和 value 部分。好。有一个概念叫键值缓存（KV cache），它的目标是把这些 key 和 value 矩阵存到某个地方，然后直接从缓存中复用它们。

### [1:29:18](https://www.youtube.com/watch?v=Q5baLehv5So&t=5358s) · b000178

**English**

So what I just mentioned here, when you want to compute a given token, you would reuse the key and the value directly from the cache instead of computing it again.

**中文**

正如刚才所说，当你想计算某个 token 时，可以直接从缓存中复用 key 和 value，而不用重新计算。

### [1:29:33](https://www.youtube.com/watch?v=Q5baLehv5So&t=5373s) · b000179

**English**

So this is basically, representation of what we just mentioned here. Does that make sense?

**中文**

这基本上就是刚才所讲内容的示意。这样清楚吗？

### [1:29:46](https://www.youtube.com/watch?v=Q5baLehv5So&t=5386s) · b000180

**English**

OK. Awesome. So what else could we do? Yeah.

**中文**

好。太好了。我们还能做什么呢？对。

### [1:29:59](https://www.youtube.com/watch?v=Q5baLehv5So&t=5399s) · b000181

**English**

Yeah. Great question. So during training, do we do KV caching? I would say during training, you have this concept of teacher forcing, where you put all your inputs and pass it all together at once. So this concept of KV caching doesn't even come up. Yeah. But great one. Yep. Yep.

**中文**

对。好问题。训练时会做 KV caching 吗？我会说，训练时有一个叫作教师强制（teacher forcing）的概念，你把所有输入放进去，一次性一起传入。所以 KV caching 这个概念根本不会出现。对。不过这个问题很好。对。对。

### [1:30:37](https://www.youtube.com/watch?v=Q5baLehv5So&t=5437s) · b000182

**English**

Yep. Yep. Yeah so the question was, what is the point of all this? We want to just reuse the computations that were already done. And then your answer is yes. Spot on. Any other questions?

**中文**

对。对。问题是，这一切有什么意义？我们只是想复用已经完成的计算。你的回答是对的，完全正确。还有其他问题吗？

### [1:30:54](https://www.youtube.com/watch?v=Q5baLehv5So&t=5454s) · b000183

**English**

OK, great. So now that we have seen that we could cache these quantities. So what else could we do? So is there something from last week's lecture that we could reuse, maybe something that reduces the amount of cache, the key and value? Do we have some techniques?

**中文**

好，很好。现在我们已经看到，可以缓存这些量。那么还能做什么？上周课上有没有什么可以复用的东西，或许能减少缓存的数量，也就是 key 和 value 的数量？我们有什么技术吗？

### [1:31:18](https://www.youtube.com/watch?v=Q5baLehv5So&t=5478s) · b000184

**English**

Sparse attention.

**中文**

稀疏注意力（Sparse attention）。

### [1:31:24](https://www.youtube.com/watch?v=Q5baLehv5So&t=5484s) · b000185

**English**

Yeah, that could be. That could be, but not here. Let's say you're attending to everyone and you focus on the number of keys and values. Is there a way to reduce this number? So just to recap, we have here, I'm operating in the context of multi-head attention, which is you have your h heads. So you have h number of query projections, h key projections, h value projections. These are any technique from last week that we could reuse that could reduce this number.

**中文**

对，可以是这个。可以，但这里不是。假设你仍然关注所有 token，并且把重点放在 key 和 value 的数量上。有没有办法减少这个数量？回顾一下，这里我讨论的是多头注意力（multi-head attention），也就是有 h 个头。所以你有 h 个 query 投影、h 个 key 投影和 h 个 value 投影。上周有没有什么技术可以复用，来减少这个数量？

### [1:32:00](https://www.youtube.com/watch?v=Q5baLehv5So&t=5520s) · b000186

**English**

Yeah. I heard it. Yeah. Group query attention. Yeah, exactly. So we had these concept of grouping keys and values together, where basically the general formulation is called group query attention, where you group these, and then the external values h and 1 denotes respectively the full multi-head attention, and then multi query attention. And then in modern day LLMs, a lot of papers, they use GQA, with some group that is sensible value.

**中文**

对，我听到了。对。分组查询注意力（Group query attention）\[字幕疑误，通常称为 grouped-query attention\]。对，完全正确。我们之前讲过把 key 和 value 分组的概念。基本上，一般形式叫作 group query attention，你把这些分组，而两个极端值 h 和 1，分别对应完整的 multi-head attention 和多查询注意力（multi query attention）。在如今的 LLM 中，很多论文都会使用 GQA，并选择一个合理的分组数量。

### [1:32:39](https://www.youtube.com/watch?v=Q5baLehv5So&t=5559s) · b000187

**English**

So this is also something we can do. OK, great. And now I'm going to go a little bit into the hardware side of things. So if we were to store the cache for all these values in a naive way, at inference time. So let's say you receive--so let's say I'm an inference server, I receive queries from multiple users. And let's say I receive a query one and I receive a query two, a naive way of storing the key and value matrices would be in reserving a portion of the memory at the beginning that correspond to the entire context length, because you don't where you're going to stop.

**中文**

这也是我们可以做的。好，很好。接下来我要稍微讲一点硬件方面的内容。如果我们在推理时，用一种朴素的方法存储所有这些值的缓存。假设你收到——假设我是一个推理服务器，收到来自多个用户的查询。假设我收到查询一，又收到查询二。一种朴素的 key 和 value 矩阵存储方式，是一开始就预留一块与整个 context length 对应的内存，因为你不知道自己会在哪里停止。

### [1:33:30](https://www.youtube.com/watch?v=Q5baLehv5So&t=5610s) · b000188

**English**

You're decoding because you stop your decoding when you hit the EOS token. So you would have this whole block of size context length, maximum context length that could be reserved. So one observation is that it leads to a lot of waste. So let's say if your context length is of size like 2k, you have 2k reserved for a given request 2k there. So at any given time, let's say, you want to get more requests, you want to serve more requests.

**中文**

你在进行解码，因为只有遇到序列结束标记（EOS token）时，才会停止解码。所以你可能会预留这样一整块空间，大小等于 context length，也就是最大 context length。一个明显的问题是，这会造成大量浪费。假设 context length 是 2k，你会为某个请求预留 2k，这里也预留 2k。那么在任意时刻，假设你想接收更多请求，想为更多请求提供服务。

### [1:34:03](https://www.youtube.com/watch?v=Q5baLehv5So&t=5643s) · b000189

**English**

Your memory will very quickly not have enough space to accommodate Does these constraints or this challenge make sense?

**中文**

内存很快就会没有足够空间来容纳。这些限制或者这个挑战，大家能理解吗？

### [1:34:19](https://www.youtube.com/watch?v=Q5baLehv5So&t=5659s) · b000190

**English**

Yeah. OK. And then there is this paper that is called PagedAttention. And it defines several quantities. So there is this reserved quantity internal fragmentation and external fragmentation. Internal fragmentation is basically the space that is being reserved by the model to complete the request. And the reserved spot is the subset of it that corresponds to tokens that were actually being used.

**中文**

对。好。有一篇论文叫作 PagedAttention，它定义了几个量：预留空间（reserved）、内部碎片（internal fragmentation）和外部碎片（external fragmentation）。internal fragmentation 基本上就是模型为了完成请求而预留的空间。而 reserved 的位置则是其中对应实际使用的 token 的那一部分。

### [1:34:52](https://www.youtube.com/watch?v=Q5baLehv5So&t=5692s) · b000191

**English**

So it's the kind of space that's actually used internal fragmentation. There is nothing in there, but it was reserved. And external fragmentation is the memory management system that doesn't necessarily put one block one after another, but has its own way of allocating memory blocks. So it might leave some other gaps. And they came up with a system that is called a PagedAttention that is powering one inference package called the vLLM that solves this issue by mapping, like the generation process by blocks of fixed size.

**中文**

所以，这是实际使用的那类空间；internal fragmentation 里没有任何东西，但它被预留了。external fragmentation 则是因为内存管理系统不一定把内存块一个接一个地放置，而是有自己分配内存块的方式，所以可能会留下其他空隙。他们提出了一个叫作 PagedAttention 的系统，它支撑着一个名为 vLLM 的推理软件包，通过把生成过程映射到固定大小的块上来解决这个问题。

### [1:35:36](https://www.youtube.com/watch?v=Q5baLehv5So&t=5736s) · b000192

**English**

So instead of allocating a whole portion of the memory to answer a given request, it breaks it down by smaller chunks. So I think the paper takes like a value of 16 for blocks. So as you can see, let's say you are in a generation process and you have used a given row, you would just start using another row without wasting more space than that. And then you have some dictionary that maps token position indices to basically their cache values.

**中文**

所以，它不会为回答某个请求分配一整片内存，而是把它拆成更小的块。我想论文中块大小取的是 16。你可以看到，假设你正在生成，已经用完某一行，就直接开始用另一行，不会再浪费更多空间。然后会有一个字典，把 token 的位置索引映射到相应的缓存值。

### [1:36:15](https://www.youtube.com/watch?v=Q5baLehv5So&t=5775s) · b000193

**English**

So there is a smart way of managing it. And they show that it reduces fragmentation by quite a lot. Yeah. OK, great. Now let's do something else with this KV cache. So we just saw that you have your internal representation of your token and you project it into query, key, and value. And then key and value is actually something that is of a dimension that is like non-negligible.

**中文**

所以，这是一种巧妙的管理方式。他们表明，它能大幅减少碎片。对。好，很好。现在我们再对 KV cache 做点别的。刚才我们看到，token 有一个内部表示，你把它投影成 query、key 和 value。而 key 和 value 的维度其实是不容忽视的。

### [1:36:51](https://www.youtube.com/watch?v=Q5baLehv5So&t=5811s) · b000194

**English**

And you need to store each copies of it in each transformer block. So you have many of these vectors that you need to keep track of. And is there a way to make that representation somehow more compact? And this is a topic that DeepSeek has tried to tackle in a concept called--I think it was called multi-latent attention.

**中文**

而且，你需要在每个 transformer 块中分别存储它们的一份副本。所以需要维护很多这样的向量。有没有办法让这种表示更紧凑一些？这是 DeepSeek 尝试解决的一个问题，使用的概念叫作——我想叫作多潜在注意力（multi-latent attention）\[字幕疑误，可能指 Multi-head Latent Attention\]。

### [1:37:24](https://www.youtube.com/watch?v=Q5baLehv5So&t=5844s) · b000195

**English**

We're going to see--so let's look at the vanilla case. If you are in multi-head attention, then for a given representation of a token, you have h projection matrices that turn it into a key. Does everyone agree with that? So the kind of self-attention formula, you have a projection matrix wk for keys, that will project the token representation into some key.

**中文**

我们来看——先看常规情况。如果使用 multi-head attention，那么对于某个 token 的表示，你有 h 个投影矩阵把它转换成 key。大家都认同吗？也就是说，在 self-attention 的公式中，有一个用于 key 的投影矩阵 wk，它会把 token 表示投影成某个 key。

### [1:37:56](https://www.youtube.com/watch?v=Q5baLehv5So&t=5876s) · b000196

**English**

And you have h heads. You have h such projections and you have h such resulting embeddings that you need to store in your cache. Because you have that for keys, you have that for values. That's a lot of vectors to store. And these keys and values, they are quite long as well. So let's see if we can make it smaller.

**中文**

你有 h 个头，因此就有 h 次这样的投影，以及 h 个由此得到、需要存进缓存的 embeddings。key 有这一套，value 也有这一套。这意味着要存储很多向量，而且这些 key 和 value 本身也相当长。所以我们来看看能不能把它变小。

### [1:38:27](https://www.youtube.com/watch?v=Q5baLehv5So&t=5907s) · b000197

**English**

What multi-latent attention does is that it factorizes these projection matrix into an intermediary space that is of lower dimension than the space of keys. You have a first transformation that reduces the dimension and then another one that decompresses it. So this is the first operation that they did in order to make the representation more compact.

**中文**

multi-latent attention 的做法是把这些投影矩阵分解，中间经过一个维度低于 key 空间的中间空间。先进行一次降低维度的变换，再进行另一次解压缩变换。这是他们为了使表示更紧凑而采取的第一步。

### [1:39:01](https://www.youtube.com/watch?v=Q5baLehv5So&t=5941s) · b000198

**English**

But they did something else that is very smart. They said that the compression matrix could be shared across keys and values, which says for a given token representation, the cache that you need to store for keys and for values is the same. And then you would have still different matrices here for the decompression part to actually learn different representations for a key and value.

**中文**

但他们还做了一件非常聪明的事。他们提出，key 和 value 可以共享压缩矩阵。这意味着，对于某个 token 表示，key 和 value 所需存储的缓存是相同的。然后在解压缩部分，这里仍然会有不同的矩阵，以便真正为 key 和 value 学到不同的表示。

### [1:39:39](https://www.youtube.com/watch?v=Q5baLehv5So&t=5979s) · b000199

**English**

But one simplification here has been to share it for across keys and values. And even better, share it across the h heads. So instead of having h such embeddings, you have just one. And then you do that for key. You do that for value. So at the end of it, for every transformer block, you have a single representation per token.

**中文**

所以，这里的一个简化就是让 key 和 value 共享它。更进一步，还在 h 个头之间共享。因此，你不再有 h 个这样的 embeddings，而是只有一个。key 这样做，value 也这样做。最终，对于每个 transformer 块，每个 token 都只有一个表示。

### [1:40:10](https://www.youtube.com/watch?v=Q5baLehv5So&t=6010s) · b000200

**English**

Does that make sense? So not only you have less things to store. The DeepSeek V2 paper also showed a performance improvement that it's kind of credited some regularization consequence of doing so. So it learns representations that are maybe more useful and shared across keys and values. So apparently there is also performance benefits to it that is not just hardware based.

**中文**

这样清楚吗？所以，不仅需要存储的东西变少了，DeepSeek V2 论文还展示了性能提升，并把这在一定程度上归因于这种做法带来的正则化（regularization）效果。也就是说，它学到了可能更有用、并由 key 和 value 共享的表示。看来它还有性能方面的好处，不只是硬件方面的收益。

### [1:40:46](https://www.youtube.com/watch?v=Q5baLehv5So&t=6046s) · b000201

**English**

OK, great. So now we have seen some--Yeah.

**中文**

好，很好。现在我们已经看过一些——对。

### [1:40:55](https://www.youtube.com/watch?v=Q5baLehv5So&t=6055s) · b000202

**English**

Yeah. So the question is, do you tune the low rank dimension? So the dimension itself is a design choice. It's fixed.

**中文**

对。问题是，低秩维度（low rank dimension）需要调节吗？维度本身是一项设计选择，它是固定的。

### [1:41:07](https://www.youtube.com/watch?v=Q5baLehv5So&t=6067s) · b000203

**English**

So the question is, is it the same lower dimension for everyone. So the dimension size is fixed and is the same for everyone. I think. But it's a design choice. You could have different ones, but I think in practice it might be the same one. Yeah. Any other questions? OK, great. So now we have less than 10 minutes. We are going to cover techniques that operate at the output token level. And then start with a concept called speculative decoding.

**中文**

问题是，所有部分使用的低维维度都一样吗？维度大小是固定的，而且所有部分都一样，我想是这样。不过这是一项设计选择。你可以选择不同的维度，但我想在实践中可能会用同一个。对。还有其他问题吗？好，很好。现在我们还剩不到 10 分钟。接下来讲作用于输出 token 层面的技术，先从一个叫作推测解码（speculative decoding）的概念开始。

### [1:41:39](https://www.youtube.com/watch?v=Q5baLehv5So&t=6099s) · b000204

**English**

That is a very interesting method that uses some smaller model to help the generation of a bigger model, and then uses some scheme that makes the distribution outputs match one of the target one. So it uses a combination of tricks of using a smaller model to generate things, and then gates it with some mathematical based properties to ensure we get a distribution that looks the one of the big model.

**中文**

这是一个非常有意思的方法，利用较小的模型来辅助较大模型的生成，再通过某种机制，使输出分布与目标分布匹配。它结合了几种技巧：先用较小的模型生成内容，然后利用一些数学性质进行筛选，确保得到的分布与大模型的分布相似。

### [1:42:17](https://www.youtube.com/watch?v=Q5baLehv5So&t=6137s) · b000205

**English**

So here's what is the lectures, the mindset of it. So let's just come back to our favorite example about teddy bears. So what you do is that you ask a smaller model, that the paper calls draft, to generate next words. So you have my teddy bear. What could be next words? So you have one pass. You find token is. You fit token is here again. You find cute and smart.

**中文**

下面是课上要讲的，它的基本思路。我们回到最喜欢的泰迪熊例子。你让一个较小的模型，论文称它为草稿模型（draft），生成后续的词。已有的是 my teddy bear。接下来可能是什么词？先运行一遍，得到 token is。把 token is 再送到这里，得到 cute 和 smart。

### [1:42:49](https://www.youtube.com/watch?v=Q5baLehv5So&t=6169s) · b000206

**English**

Since the LLM is small, this is typically done faster than with the big LLM. And then once you have all of these, you put the tokens that are predicted by the smaller LLM all as inputs to the target's LLM. That is like the bigger model, like the one that you use, to generate probability distributions for each of them. And then we're going to see that by having some rule on the output distribution of each of these tokens, you can simulate a probability distribution of each token of each next token that looks one of the target models.

**中文**

由于这个 LLM 很小，通常会比大 LLM 更快完成。得到这些之后，把小 LLM 预测出的所有 token 一起作为输入，送给目标 LLM，也就是那个较大的模型，你所使用的那个模型，为每个位置生成概率分布。接下来我们会看到，通过对这些 token 的输出分布应用某个规则，可以模拟出每个 token、每个后续 token 的概率分布，使其与目标模型的分布相似。

### [1:43:38](https://www.youtube.com/watch?v=Q5baLehv5So&t=6218s) · b000207

**English**

So here's basically how it goes. So it looks at the probability of the token that the draft model has predicted. So if the probability of the draft model is bigger than the one of the draft model in the draft model's output distribution, then you just accept the token. Otherwise, you have some acceptance rejection mechanism that either accepts the token or rejects it.

**中文**

基本过程如下。它会查看 draft model 预测的 token 的概率。如果 draft model 的概率大于 draft model 输出分布中 draft model 的概率 \[字幕疑误，此处概率比较对象重复，可能原意涉及 target model 与 draft model 的比较\]，就直接接受这个 token。否则，会有一个接受—拒绝机制（acceptance rejection mechanism），决定接受还是拒绝这个 token。

### [1:44:12](https://www.youtube.com/watch?v=Q5baLehv5So&t=6252s) · b000208

**English**

And let's say everything is accepted. Then in a single pass, you are able to advance by way more tokens. And then if it fails, then basically you resume the process of generation from that good token onwards with some adjustments on the distribution.

**中文**

假设所有 token 都被接受，那么一次运行就能向前推进更多 token。如果失败了，基本上就从那个好的 token 往后恢复生成过程，并对分布做一些调整。

### [1:44:35](https://www.youtube.com/watch?v=Q5baLehv5So&t=6275s) · b000209

**English**

So one question that you might ask from all of this, this looks like a recipe. Why is that matching the target distribution? So if you start from the law of total probability and write each term with these quantities. Then you will find the target distribution at the end. So it's an exercise that I encourage you to do. And the paper that is attached to the slide here demonstrates it in just a few lines.

**中文**

看到这些，你可能会问：这看起来像一套操作步骤，为什么它会匹配目标分布？如果你从全概率公式（law of total probability）出发，用这些量写出每一项，最后就会得到目标分布。我鼓励大家做一做这个练习。幻灯片这里附上的论文，只用了几行就证明了这一点。

### [1:45:06](https://www.youtube.com/watch?v=Q5baLehv5So&t=6306s) · b000210

**English**

So it's a very simple proof. And I think it's a very, very interesting one. Does that make sense? Yeah.

**中文**

所以这是一个非常简单的证明，我觉得也非常、非常有意思。这样清楚吗？对。

### [1:45:19](https://www.youtube.com/watch?v=Q5baLehv5So&t=6319s) · b000211

**English**

Yeah. Yeah. The question is, is that rejection sampling? Yeah. So some of you might be familiar with it already. Does that make sense?

**中文**

对。对。问题是，这是不是拒绝采样（rejection sampling）？是的。所以你们有些人可能已经熟悉它了。这样清楚吗？

### [1:45:33](https://www.youtube.com/watch?v=Q5baLehv5So&t=6333s) · b000212

**English**

Yeah. And then one thing that I didn't say is that why did we even put the last token here? We put all the draft tokens, but also the last one that was predicted because by doing a single forward pass with all these draft tokens, you get for free the probability distribution of the token that comes after that you can then just sample from Qk plus 1. So just to give some summary of the rationale.

**中文**

对。还有一点我没有说，为什么我们还要把最后一个 token 放在这里？我们放入了所有 draft token，也放入了最后预测出的那个 token。因为把所有这些 draft token 一起做一次前向传播（forward pass），就能顺带得到它们之后那个 token 的概率分布，然后直接从 Qk 加 1 中采样。这里简要说明一下这样做的理由。

### [1:46:07](https://www.youtube.com/watch?v=Q5baLehv5So&t=6367s) · b000213

**English**

Doing a single pass is as expensive as doing one pass at a time, because at inference time, you're memory bounds back. In other words, computations are not the limiting factor. It's basically the memory that will bottleneck your computation. So you want to do it on a smaller model. And then on the big model, you want to compute all of these probability distributions at once.

**中文**

做一次整体运行，和每次只运行一次的开销一样，因为在推理时，你是 memory bounds back \[字幕疑误，可能指 memory-bound\]。换句话说，计算不是限制因素，内存才会成为计算的瓶颈。所以你希望在较小的模型上做这件事，然后在大模型上，一次性计算所有这些概率分布。

### [1:46:35](https://www.youtube.com/watch?v=Q5baLehv5So&t=6395s) · b000214

**English**

Does that make sense? OK. Great. And then I want to talk about one last technique that is called multi-token prediction. It's the same-- so by the way, this previous technique was called speculative decoding. And then this one is basically doing the same. So it's doing slightly a different thing. But the draft model is embedded in the same model, which is very powerful.

**中文**

这样清楚吗？好。很好。然后，我想讲最后一项技术，叫作多 token 预测（multi-token prediction）。它也是——顺便说一下，前面那项技术叫 speculative decoding。而这一项基本上也在做同样的事。它的做法稍有不同，不过 draft model 被嵌入了同一个模型中，这很强大。

### [1:47:07](https://www.youtube.com/watch?v=Q5baLehv5So&t=6427s) · b000215

**English**

So basically, it's a model that attaches multiple heads on top of the representation of the last decoder. And the process here is that at training time, it doesn't do next word prediction. It does multi word prediction. And at test time, the draft model is all your heads. And your main model is just the first head. So you have all your draft tokens that you then feed back to the first head and then do acceptance rejection.

**中文**

基本上，这种模型会在最后一个解码器（decoder）的表示之上接上多个头。其过程是，训练时不做下一个词预测，而是做多个词预测。测试时，所有这些头构成 draft model，而主模型就是第一个头。这样，你得到所有 draft token，再把它们送回第一个头，进行接受—拒绝。

### [1:47:44](https://www.youtube.com/watch?v=Q5baLehv5So&t=6464s) · b000216

**English**

So the paper does it in a greedy way. So it doesn't do it with this formula. Because since the architecture and then the objective function has changed, you don't have this nice property of finding again, the next token predictions distribution. But you have a slight variation of it. And yeah. So like the interesting notes out of the multi token prediction is the change in objective function. And then second, the fact that the draft model and the target model are basically embedded in the same one.

**中文**

论文采用了贪心（greedy）的方式，所以没有使用这个公式。因为架构和目标函数都发生了变化，就不再具有那个很好的性质，也就是重新得到下一个 token 的预测分布。不过，它有一个略微变化的版本。对。所以 multi-token prediction 中有意思的几点，首先是目标函数的改变。其次是 draft model 和 target model 基本上嵌入了同一个模型中。

### [1:48:17](https://www.youtube.com/watch?v=Q5baLehv5So&t=6497s) · b000217

**English**

So don't have to separate the two. And yeah. So you do remember this slide? We have explored techniques that can remedy each of these aspects. So yeah. I highly recommend taking a look at the associated papers as well. And with that, thank you very much.

**中文**

所以不必把两者分开。对。还记得这张幻灯片吗？我们已经探索了能够改善这些方面的技术。我也非常推荐大家看看相关论文。最后，非常感谢大家。
