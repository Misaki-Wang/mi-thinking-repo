# Stanford CME295 Transformers &amp; LLMs \| Autumn 2025 \| Lecture 9 - Recap &amp; Current Trends

_Bilingual transcript · 双语讲稿_

- Channel: Stanford Online
- Source: [YouTube](https://www.youtube.com/watch?v=Q86qzJ1K1Ss)
- Duration: 1:51:31
- Caption source: manual
- Status: complete
- Chinese translation: 203/203
- Translation provider: codex
- Generated: 2026-09-29T16:19:24+00:00

## Transcript · 讲稿

### [00:05](https://www.youtube.com/watch?v=Q86qzJ1K1Ss&t=5s) · b000001

**English**

Hello, everyone, and welcome to lecture 9 of CME 295. So as today is a kind of a special day because we're having the last lecture of the entire course. So the menu for today will be a little different compared to usual. We're going to try to divide the lecture in three parts. So in the first part, we're going to recap actually what we did in the entire class just to see how different pieces kind of fit together.

**中文**

大家好，欢迎来到 CME 295 第 9 讲。今天算是个特别的日子，因为这是整门课程的最后一讲。所以今天的安排会和平时稍有不同。我们会试着把这堂课分为三个部分。第一部分，我们会回顾整门课学过的内容，看看不同部分是如何相互衔接的。

### [00:44](https://www.youtube.com/watch?v=Q86qzJ1K1Ss&t=44s) · b000002

**English**

In the second part, we'll look at some topics that are particularly trending in 2025 and what we think are going to be trending in the near future. And then the third part will be more way for us to just conclude and next steps for all of you. Does that sound good? Cool. So with that, we're going to start with the first part, which what I mentioned is about recapping what we did this entire quarter.

**中文**

第二部分，我们会看看 2025 年特别热门的一些话题，以及我们认为在不久的将来会热门的话题。第三部分主要是做个总结，并谈谈你们接下来可以做什么。这样安排可以吗？好。那么，我们先从第一部分开始，也就是我刚才提到的，回顾这一整个学季学过的内容。

### [01:19](https://www.youtube.com/watch?v=Q86qzJ1K1Ss&t=79s) · b000003

**English**

So nothing new here is just a way for us to piece everything together. So if you remember a lot of weeks ago, I believe it's like maybe 10 weeks ago, we had lecture 1, which was focused on understanding what transformers were. So at the very beginning of the class, we didn't even how we could process text. So I guess the first step that we saw was this tokenization step, which consists of dividing the input into atomic units.

**中文**

这里没有新内容，只是把所有内容串起来。如果你们还记得，很多周以前，我想可能是 10 周以前，我们上了第 1 讲，重点是理解 transformer 是什么。在课程刚开始的时候，我们甚至还不……如何处理文本 \[原文缺词\]。所以，我想我们看到的第一步就是分词（tokenization），也就是把输入划分成原子单元。

### [01:55](https://www.youtube.com/watch?v=Q86qzJ1K1Ss&t=115s) · b000004

**English**

And so here, the way we divide the text is something that is arbitrary in some sense. So we have different algorithms that allow us to do that. And we saw that the most common tokenization algorithm is the subword level tokenizer. And we saw that some of the advantages were that roots of words could be reused and leveraged, especially when it came to representing those tokens.

**中文**

这里，我们如何划分文本，在某种意义上是人为决定的。所以我们有不同的算法来做这件事。我们看到，最常见的 tokenization 算法是子词级分词器（subword level tokenizer）。它的一些优点是可以复用和利用词根，尤其是在表示这些词元（tokens）时。

### [02:30](https://www.youtube.com/watch?v=Q86qzJ1K1Ss&t=150s) · b000005

**English**

And speaking of representation, once we were able to divide the input text into atomic units, a.k.a. tokens, the next step for us was to learn how to represent these embeddings. So if you remember, we saw some methods that were very popular back then. So one of them was called word2vec. And the representation was learned from a proxy task, which was something like predicting the center word or predicting the context words.

**中文**

说到表示，当我们能够把输入文本划分成原子单元，也就是 tokens 之后，下一步就是学习如何表示这些嵌入（embeddings）。如果你们还记得，我们介绍过一些当时非常流行的方法。其中一个叫 word2vec。它通过代理任务（proxy task）来学习表示，例如预测中心词，或者预测上下文词。

### [03:08](https://www.youtube.com/watch?v=Q86qzJ1K1Ss&t=188s) · b000006

**English**

But then we saw that this way of learning representations had some limitations, one of which was that these representations were not context aware, meaning that if a word is in a given sentence or in another sentence, that word will have the same representation in both sentences. And so for that reason, we saw some other methods that were popular in the 2010s, one of which was RNNs, if you remember.

**中文**

但后来我们看到，这种学习表示的方法有一些局限，其中之一是这些表示不具备上下文感知能力（context aware）。也就是说，一个词无论出现在这个句子里还是另一个句子里，在两个句子中的表示都相同。因此，我们介绍了其他一些在 2010 年代流行的方法，其中之一就是循环神经网络（RNNs），如果你们还记得的话。

### [03:45](https://www.youtube.com/watch?v=Q86qzJ1K1Ss&t=225s) · b000007

**English**

So RNNs had this recurrent structure, which processed tokens one at a time and kept an internal representation of the sequence so far. But then we saw that a big limitation of this problem of long range dependency, and in particular, the fact that tokens that were encoded far in the past were not quantities that were able to be kept I guess, as the sequence got longer.

**中文**

RNNs 具有这种循环结构，每次处理一个 token，并保留截至当前的序列的内部表示。但随后我们看到，一个很大的局限就是长距离依赖（long range dependency）问题，尤其是很早之前编码的 tokens，我想，随着序列变长，它们的信息无法一直保留下来。

### [04:18](https://www.youtube.com/watch?v=Q86qzJ1K1Ss&t=258s) · b000008

**English**

And this is the reason why we saw the central idea of this whole class, which is the idea of self-attention, where tokens can actually attend to one another regardless of where they are placed in the sequence. So you can think of this as a direct link. And so this, for instance, is what we saw. We saw that there are three main terminologies that people use.

**中文**

这就是为什么我们介绍了整门课的核心思想，也就是自注意力（self-attention）：tokens 可以相互关注，无论它们位于序列中的什么位置。你可以把它看作直接连接。比如，这就是我们看到的内容。我们介绍了大家使用的三个主要术语。

### [04:48](https://www.youtube.com/watch?v=Q86qzJ1K1Ss&t=288s) · b000009

**English**

So query, key, and value. So typically want to how similar a query is compared to the keys in the sequence. And you quantify that by taking some dot products that's kind of scaled and softmax. And then you have the corresponding value that is taken. So at the end of the day, we obtain some kind of weighted average of all the tokens that are in the sequence.

**中文**

也就是查询（query）、键（key）和值（value）。通常，我们想要……一个 query 与序列中的 keys 有多相似 \[原文缺词\]。我们通过做一些点积（dot products）、缩放，再经过 softmax 来量化这种相似性。然后取对应的 value。所以最终，我们得到的是序列中所有 tokens 的某种加权平均。

### [05:22](https://www.youtube.com/watch?v=Q86qzJ1K1Ss&t=322s) · b000010

**English**

And then you may also be familiar now with this formula. So softmax of qk transpose over square root of k times v. So this is the matrix formulation of what I mentioned here, which is able to process these computations in a very efficient way. And it's something that today's hardware is well equipped to do. And then we finished the first lecture by going through the architecture that is the foundation of modern day LLMs, which is the transformer.

**中文**

现在你们可能也熟悉这个公式了：qk 的转置除以 k 的平方根，再取 softmax，乘以 v。这就是我在这里提到的内容的矩阵形式，能够非常高效地完成这些计算。如今的硬件也很擅长做这件事。随后，我们在第 1 讲的最后介绍了现代大型语言模型（large language models，LLMs）的基础架构，也就是 transformer。

### [06:01](https://www.youtube.com/watch?v=Q86qzJ1K1Ss&t=361s) · b000011

**English**

And we saw that there are two notable parts in the transformer. So one was the encoder in the left part of the figure. And then the right part is the decoder. And we saw how this was applied in the case of translation. So at the end of the first lecture, we saw what motivated us to end up with the transformer. And we saw that transformer was working quite well in the case of translation.

**中文**

我们看到，transformer 有两个值得注意的部分。一个是图左侧的编码器（encoder），右侧则是解码器（decoder）。我们介绍了它在翻译中的应用。所以在第 1 讲结束时，我们了解了是什么促使我们最终采用 transformer，也看到 transformer 在翻译任务中表现相当不错。

### [06:36](https://www.youtube.com/watch?v=Q86qzJ1K1Ss&t=396s) · b000012

**English**

And so in the next lecture, what we saw what were the little improvements that people have made to this architecture since it was released. And if you remember, it remember, it was in 2017 that it was published. So one particular improvement that people have made is in the way we consider positions, because in the original transformer, paper, positions were encoded in an absolute way, as in each position had its own embedding.

**中文**

接下来的那一讲，我们介绍了这个架构发布以后，人们对它做过哪些小改进。如果你们还记得，还记得的话，它是在 2017 年发表的。其中一项改进是处理位置的方式，因为在最初的 transformer 论文中，位置是以绝对方式编码的，也就是每个位置都有自己的 embedding。

### [07:16](https://www.youtube.com/watch?v=Q86qzJ1K1Ss&t=436s) · b000013

**English**

And this embedding was added to the token embedding. But then if we think about it, positions, actually, we don't really care about the absolute position. We care about the relative position between tokens. And in particular, we care about how far tokens are in the self-attention computation, which is why we saw this method that is now quite popular called rotary position embeddings, a.k.a., rope that is now quite used.

**中文**

这个 embedding 会加到 token embedding 上。但仔细想想，对于位置，我们其实并不太关心绝对位置，而是关心 tokens 之间的相对位置。尤其是在 self-attention 计算中，我们关心 tokens 相距多远。这就是为什么我们介绍了如今相当流行的旋转位置嵌入（rotary position embeddings），也叫 rope，现在用得相当多。

### [07:51](https://www.youtube.com/watch?v=Q86qzJ1K1Ss&t=471s) · b000014

**English**

And it is a method that rotates query and keys, both of which happen in the self-attention computation. And so here what is quantified here is purely a function of the relative distance between two tokens. And not only that, it is something that is taken care of in the self-attention layer, which is what we care about.

**中文**

这种方法会旋转 query 和 keys，而两者都出现在 self-attention 计算中。所以这里量化的内容，纯粹是两个 tokens 之间相对距离的函数。不仅如此，这件事是在 self-attention 层中处理的，而这正是我们关心的地方。

### [08:24](https://www.youtube.com/watch?v=Q86qzJ1K1Ss&t=504s) · b000015

**English**

So this was one big improvement. And then we saw some other improvements, especially when it came to how the multi-head attention layer-- multi-head attention layer was composed of. And in particular, we saw that it was possible for us to have some groupings of the matrices that we learn. So we don't need to have one matrix, one projection matrix per head for, let's say, keys and values.

**中文**

这是一个很大的改进。随后我们还介绍了其他改进，尤其是多头注意力层（multi-head attention layer）——multi-head attention layer 的组成方式。具体来说，我们看到，可以对要学习的矩阵进行分组。也就是说，比如对于 keys 和 values，我们不必为每个头都配一个矩阵、一个投影矩阵。

### [08:56](https://www.youtube.com/watch?v=Q86qzJ1K1Ss&t=536s) · b000016

**English**

We can actually group them. So this is for instance, what is mentioned here. So group query attention. And then we also saw some other techniques that I have not represented here, for instance, the normalization layer in the transformer which here happens after each sublayer. But I guess nowadays people have tried moving the normalization piece before the sublayer. So here it's the post-norm version.

**中文**

我们实际上可以把它们分组。例如，这里提到的就是分组查询注意力（group query attention）。我们还介绍了其他一些没有画在这里的技术，比如 transformer 中的归一化层（normalization layer），在这张图里，它位于每个子层之后。但我想，现在人们已经尝试把归一化部分移到子层之前。所以这里是 post-norm 版本。

### [09:29](https://www.youtube.com/watch?v=Q86qzJ1K1Ss&t=569s) · b000017

**English**

And then before the sublayer part is called the pre-norm version. And then the last thing that we saw was that from this transformer former architecture, there are a lot of derived models that were based from that. So we saw that if we only keep the encoder part, we could compute very meaningful embeddings. If you remember, there was this kind of landmark paper on encoder only model, which is BERT, which was heavily used in the context of classification because it relied on the encoder embedding of the CLS token.

**中文**

而放在子层之前的形式叫 pre-norm 版本。最后我们看到，基于这个 transformer former \[字幕疑误，可能是 transformer 的重复\] 架构，衍生出了很多模型。我们看到，如果只保留 encoder 部分，就能计算出很有意义的 embeddings。如果你们还记得，有一篇关于仅编码器模型（encoder only model）的里程碑式论文，就是 BERT。它被大量用于分类，因为它依赖 CLS token 的 encoder embedding。

### [10:14](https://www.youtube.com/watch?v=Q86qzJ1K1Ss&t=614s) · b000018

**English**

So that was one. But then we also saw that there was a number of other kinds of models, all more or less derived from the transformer. So you could only keep the encoder, which was for BERT. You could only keep the decoder just, for instance, for GPT. And you could also have both, which is for instance, the case of T5. And one particular aspect of each of these models is that encoder only is not able-- in the way that we saw-- is not able to generate text, but it's able to generate embeddings which can be used for downstream tasks.

**中文**

这是其中一种。我们还看到，另有不少其他类型的模型，或多或少都衍生自 transformer。可以只保留 encoder，比如 BERT；也可以只保留 decoder，比如 GPT；还可以两者都保留，比如 T5。这些模型各自有一个特别的方面：仅 encoder 的模型不能——按照我们介绍的方式——不能生成文本，但能生成 embeddings，供下游任务（downstream tasks）使用。

### [10:57](https://www.youtube.com/watch?v=Q86qzJ1K1Ss&t=657s) · b000019

**English**

But then encoder decoder models like T5 or decoder only models like GPT, they can be autoregressive and generate texts. The paradigm can be text in, text out.

**中文**

而像 T5 这样的 encoder decoder 模型，或者像 GPT 这样的仅 decoder 模型，可以采用自回归（autoregressive）方式生成文本。它们的范式可以是文本输入、文本输出。

### [11:16](https://www.youtube.com/watch?v=Q86qzJ1K1Ss&t=676s) · b000020

**English**

And with that, we then focused on what now everyone calls large language models, which are transformer based models, specifically text to text models. So decoder only transformer based models. And we saw that people have come up with a lot of new tricks now because these models, as the name indicates, people have scaled them up.

**中文**

接着，我们把重点转向了现在大家所说的大型语言模型，它们是基于 transformer 的模型，具体来说是文本到文本模型。也就是基于仅 decoder transformer 的模型。我们看到，人们现在想出了很多新技巧，因为顾名思义，人们已经把这些模型的规模扩大了。

### [11:46](https://www.youtube.com/watch?v=Q86qzJ1K1Ss&t=706s) · b000021

**English**

But then one question was kind of thrown, which is do you actually need all these parameters to just do a forward pass. So we saw one kind of variant which was based on a mixture of experts. So what mixture of experts are is instead of running everything through the whole entire model, you're going to instead have a number of experts that you're going to activate in a sparse way.

**中文**

但随后有人提出了一个问题：仅仅做一次前向传播（forward pass），真的需要所有这些参数吗？于是我们介绍了一种基于混合专家（mixture of experts）的变体。mixture of experts 的意思是，不让所有输入都经过整个模型，而是设置多个专家，以稀疏的方式激活它们。

### [12:27](https://www.youtube.com/watch?v=Q86qzJ1K1Ss&t=747s) · b000022

**English**

So for instance, for one input, you're going to just activate just a subset. And then for another input you're going to activate another subset so that you don't need to do all the computations all the time. And we saw that this mixture of experts, they were used in LLMs, in particular in the feedforward neural network layer. So here you would have experts as being different feedforward neural networks. And you would have a gating mechanism that would reroute to the correct feedforward neural network.

**中文**

比如，对于一个输入，只激活其中一个子集；对于另一个输入，则激活另一个子集，这样就不必每次都做所有计算。我们看到，mixture of experts 被用在 LLMs 中，尤其是前馈神经网络层（feedforward neural network layer）。这里，不同的专家就是不同的 feedforward neural networks，并通过门控机制（gating mechanism）把输入路由到合适的 feedforward neural network。

### [13:07](https://www.youtube.com/watch?v=Q86qzJ1K1Ss&t=787s) · b000023

**English**

And then we also saw that some papers were also able to produce some nice visualization in terms, I guess, which token gets routed to which expert, because this routing, we saw that it was done at the token level. And so one reason why it's done at the token level is to be able to, I guess, smartly put the experts on different pieces of hardware, different GPUs, and then parallelize the computation a little bit more.

**中文**

我们还看到，有些论文给出了很好的可视化，我想，是展示哪些 token 被路由到哪些专家。因为我们看到，这种路由是在 token 层面进行的。我想，在 token 层面路由的一个原因，是能够巧妙地把专家放在不同的硬件、不同的 GPU 上，进一步并行化计算。

### [13:40](https://www.youtube.com/watch?v=Q86qzJ1K1Ss&t=820s) · b000024

**English**

And then we also saw that these LLMs, they always are tasked with predicting the next token. And in order to predict the next token we were interested in, I guess, how we were doing this. And so one particular method that people use is just sample. Sample from the output distribution. So you have let's say given an input you have a distribution of probabilities of what the next token would be.

**中文**

我们还看到，这些 LLMs 始终承担着预测下一个 token 的任务。为了预测下一个 token，我们关心的是，我想，我们具体如何做这件事。其中一种方法就是采样（sample），从输出分布中采样。比如，给定一个输入，你会得到一个关于下一个 token 是什么的概率分布。

### [14:13](https://www.youtube.com/watch?v=Q86qzJ1K1Ss&t=853s) · b000025

**English**

That is output by the model. And what you do is instead of let's say taking the highest probability, which is called the greedy kind of decoding, you actually sample. So it introduces some randomness and allows the model to produce kind of a bigger variety of kinds of outputs. And we saw that you could adjust how much, I guess, a variety you want in your outputs by tweaking a hyperparameter called temperature.

**中文**

这个分布由模型输出。你所做的，不是比如取概率最高的那个，也就是所谓的贪心解码（greedy decoding），而是进行采样。这样会引入一些随机性，让模型能够生成更多样的输出。我们看到，可以通过调整一个叫温度（temperature）的超参数，来控制输出的多样性程度。

### [14:52](https://www.youtube.com/watch?v=Q86qzJ1K1Ss&t=892s) · b000026

**English**

So very low temperature leads to very spiky distribution. So more deterministic outputs and higher temperatures are, I guess, a bit more random, a bit more creative.

**中文**

很低的 temperature 会产生非常尖锐的分布，因此输出更加确定；而较高的 temperature，我想，会让输出更随机一些、更有创造性一些。

### [15:07](https://www.youtube.com/watch?v=Q86qzJ1K1Ss&t=907s) · b000027

**English**

So until then, we saw what LLMs were, how they were based on the transformer, how they connected to the architecture that we saw in the first lecture. And then in lecture 4, we saw how people actually trained those LLMs because as I mentioned, these LLMs are large. And so you cannot naively fit them in your hardware. You need to be a little bit smart about it.

**中文**

到这里，我们了解了 LLMs 是什么、它们如何基于 transformer，以及它们与第 1 讲介绍的架构有什么联系。随后在第 4 讲，我们介绍了人们实际上如何训练这些 LLMs，因为正如我提到的，这些 LLMs 很大。所以你不能简单地把它们塞进你的硬件里，必须稍微动动脑筋。

### [15:38](https://www.youtube.com/watch?v=Q86qzJ1K1Ss&t=938s) · b000028

**English**

So in particular, what people have noticed in the early 2020s is that the bigger your model is, the better your performance. And so people just started building bigger and bigger models. So here in the illustration we saw that-- so on the y-axis is the Teslas. So the lower the better. So we saw that the more compute you use, the better your test performance.

**中文**

具体来说，人们在 2020 年代初注意到，模型越大，性能越好。于是大家开始构建越来越大的模型。我们在这张图中看到——纵轴是 Teslas \[字幕疑误，可能指 test loss，测试损失\]，越低越好。我们看到，使用的计算量越多，测试性能就越好。

### [16:12](https://www.youtube.com/watch?v=Q86qzJ1K1Ss&t=972s) · b000029

**English**

And same with increasing the data set size. And same with increasing the number of parameters. But then as you know compute is not infinite. So there was a natural question that came out of the community which was if we give you a given budget, a given compute budget, can you choose, I guess some, quote unquote, optimal number of parameters and data set size on which you want to train your model.

**中文**

增大数据集规模也是如此，增加参数数量也是如此。但你们知道，计算资源并非无限。因此，社区自然提出了一个问题：如果给你一定的预算、一定的计算预算，你能不能选择一个，我想，加引号的“最优”参数数量，以及用于训练模型的数据集规模？

### [16:50](https://www.youtube.com/watch?v=Q86qzJ1K1Ss&t=1010s) · b000030

**English**

And so we saw that there was this paper that was published in the early 2020s, which actually studied the relationship between, I guess, if you vary the data set size and the size of your model and the performance on the test set. And then we saw that actually, most models at the time were what we say undertrained because they were too big compared to the data set that they were trained on.

**中文**

我们介绍过一篇发表于 2020 年代初的论文，它研究了数据集规模、模型规模的变化与测试集性能之间的关系。随后我们看到，当时大多数模型实际上都处于所谓的训练不足（undertrained）状态，因为相对于训练它们的数据集来说，它们太大了。

### [17:22](https://www.youtube.com/watch?v=Q86qzJ1K1Ss&t=1042s) · b000031

**English**

The data set that they were trained on was not as big as they should have been. And so in particular, there was a kind of a rule of thumb that came out of this, which was if you have a given number of parameters in your model, you should at least train it on 20 times the number of parameters in terms of tokens. So for instance, if you have a 100 billion parameter model, you should train it on at least 2 trillion tokens because the 2 trillion is 100 billion times 20.

**中文**

训练它们的数据集没有达到应有的规模。尤其是，由此得出了一条经验法则：如果模型有一定数量的参数，训练它所用的 token 数量至少应该是参数数量的 20 倍。例如，如果你有一个 1000 亿参数的模型，就应该用至少 2 万亿个 tokens 来训练它，因为 2 万亿就是 1000 亿乘以 20。

### [17:59](https://www.youtube.com/watch?v=Q86qzJ1K1Ss&t=1079s) · b000032

**English**

So that's the rule of thumb that people have used. And then as I mentioned previously, these models are huge. So people have tried to also make the computation more efficient. And so there was this method that we saw, which is actually quite important called flash attention. And flash attention is a method it that leverages the strength of the underlying hardware.

**中文**

这就是大家采用的经验法则。而且，正如前面提到的，这些模型非常庞大。所以人们也尝试让计算更高效。我们介绍过一种实际上相当重要的方法，叫 flash attention。flash attention 是一种利用底层硬件优势的方法。

### [18:31](https://www.youtube.com/watch?v=Q86qzJ1K1Ss&t=1111s) · b000033

**English**

And in particular, it looks at-- so GPUs, more particularly-- it looks at the kinds of memories that a GPU has. So it has a big, but slow memory and a small, but fast memory. So the HBM and SRAM respectively. And we saw that this method tries to minimize the number of reads and writes to the big and slow memory, to the HBM.

**中文**

具体来说，它关注的是——更准确地说，是 GPU——GPU 拥有哪些类型的存储器。它有容量大但速度慢的存储器，也有容量小但速度快的存储器，分别是高带宽内存（HBM）和静态随机存取存储器（SRAM）。我们看到，这种方法试图尽量减少对容量大、速度慢的 HBM 的读写次数。

### [19:05](https://www.youtube.com/watch?v=Q86qzJ1K1Ss&t=1145s) · b000034

**English**

And so the way it was doing this was to divide the computation in little bits that it would send to the SRAM, which is the small but fast memory, so that it can do the end to end computation and then send it back to where it was in order to do the full end to end computation. So that method is an exact method, meaning that we're not doing any approximations to the results.

**中文**

它的做法是把计算划分成小块，发送到 SRAM，也就是容量小但速度快的存储器，以便完成端到端计算，再把结果传回原来的位置，从而完成整个端到端计算过程。这是一种精确方法（exact method），意味着我们没有对结果做任何近似。

### [19:39](https://www.youtube.com/watch?v=Q86qzJ1K1Ss&t=1179s) · b000035

**English**

But it led to significant speedups. And in particular, there was this second idea from the paper, which is a kind of an important one as well, which was that sometimes it's OK for you to not store results. It's OK for you to just throw them out and then recompute when you need them again. So there is this idea of computation using what I described, which led to faster runtimes, even though we were doing more computations.

**中文**

但它带来了显著的加速。尤其是，论文还有第二个同样很重要的想法：有时候，你可以不保存结果。可以直接丢掉它们，等再次需要时重新计算。所以，采用我刚才描述的这种计算思路，即使做了更多计算，运行时间也反而更短。

### [20:16](https://www.youtube.com/watch?v=Q86qzJ1K1Ss&t=1216s) · b000036

**English**

So that was flash attention. And we also saw a number of other methods that were meant to, I guess, parallelize the computation. So we saw data parallelism, which was this idea of not having all your data be processed on a single GPU, but instead divide it into multiple places. And then we had the second method, which was model parallelism, where even for a given forward pass, you would actually involve multiple GPUs.

**中文**

这就是 flash attention。我们还介绍了其他一些旨在并行化计算的方法。我们介绍了数据并行（data parallelism），其想法是不让所有数据都在单个 GPU 上处理，而是把它们分配到多个地方。第二种方法是模型并行（model parallelism），即便只是一次前向传播，也会实际用到多个 GPU。

### [20:56](https://www.youtube.com/watch?v=Q86qzJ1K1Ss&t=1256s) · b000037

**English**

So anyway, there were a lot of very interesting techniques, a lot of different ideas about how to train this model in an efficient way. And in particular, so what I described here is mostly important for the first step of the training process of an LLM, which is called the pre-training, which is meant to teach the model about the structure of language about the structure of codes.

**中文**

总之，关于如何高效地训练这个模型，有很多非常有趣的技术和不同的想法。尤其是，我在这里描述的内容，主要对 LLM 训练过程的第一步很重要，这一步叫预训练（pre-training），目的是让模型学习语言的结构和代码的结构。

### [21:29](https://www.youtube.com/watch?v=Q86qzJ1K1Ss&t=1289s) · b000038

**English**

And in particular, this model was trained with huge amounts of data. So think about trillions of tokens or even tens of trillions of tokens. And so that first step goes from an initialized model to a model that is able to autocomplete because it is trained with an objective of predicting the next token. So at the end of this first stage, you have a model that knows how to autocomplete, but you have a model that is not very helpful because it only knows how to complete things.

**中文**

具体来说，这个模型会用海量数据进行训练，比如数万亿个 tokens，甚至数十万亿个 tokens。第一步会把一个初始化的模型变成能够自动补全的模型，因为它的训练目标是预测下一个 token。因此，在第一阶段结束时，你得到一个知道如何自动补全的模型，但它还不太有用，因为它只知道如何续写内容。

### [22:11](https://www.youtube.com/watch?v=Q86qzJ1K1Ss&t=1331s) · b000039

**English**

So in order to have the model be useful for our use cases, we had this second step, which is called the fine tuning step, where we teach the model on the kinds of input/output pairs that we wanted to perform well. So this is also called the SFT stage supervised fine tuning stage. And at the end of this second step, we have a model that not only knows the structure of text and codes, but also is able to behave in the way you want.

**中文**

为了让模型在我们的使用场景中有用，我们还有第二步，叫微调（fine tuning）。在这一步，我们用希望模型表现良好的那些输入／输出对来训练它。这也叫监督微调阶段（supervised fine tuning，SFT）。第二步结束时，我们得到的模型不仅知道文本和代码的结构，还能够按照你希望的方式行动。

### [22:50](https://www.youtube.com/watch?v=Q86qzJ1K1Ss&t=1370s) · b000040

**English**

But so far, up until step number 2, we have only taught our model what to do. We have not taught it what to not do. And this is why we had our third step, which was the preference tuning step, where we took our model that went through the pre-training stage, that went to the SFT stage. And now we want to inject some negative signal as well as in I want you to prefer this compared to this output.

**中文**

但到目前为止，到第 2 步为止，我们只教了模型该做什么，还没有教它不该做什么。因此我们有第三步，也就是偏好调优（preference tuning）。我们拿到一个已经经过 pre-training 和 SFT 的模型，现在还希望注入一些负面信号，例如，希望它相对于这个输出来说，更偏好另一个输出。

### [23:26](https://www.youtube.com/watch?v=Q86qzJ1K1Ss&t=1406s) · b000041

**English**

And this third step uses preference data. So like the name suggests, so preference tuning uses preference data which is typically pairwise data where humans say I prefer this output compared to that output. And typically, the model here is able to align the kind of output it produces with human preferences that could be along the dimension of usefulness, of safety, friendliness, tone.

**中文**

第三步使用偏好数据（preference data）。顾名思义，preference tuning 使用的通常是成对数据（pairwise data），由人类指出：相比那个输出，我更喜欢这个输出。通常，这一步能够让模型生成的输出与人类偏好对齐，而这些偏好可能涉及有用性、安全性、友好程度、语气等维度。

### [24:01](https://www.youtube.com/watch?v=Q86qzJ1K1Ss&t=1441s) · b000042

**English**

There's a bunch of different dimensions. But yeah, so that's what is happening in this third step. And in this third step, it's actually in lecture 5 that we dug into what that third step was about. So if you remember, we had drawn a parallel between the way our LLM produces tokens. And I guess what people in the reinforcement learning field, I guess, consider how a given policy is interacting with some environments and performing some action and being in some states.

**中文**

还有很多不同维度。对，这就是第三步在做的事。实际上，我们在第 5 讲深入讨论了这第三步。如果你们还记得，我们把 LLM 生成 tokens 的方式，与强化学习（reinforcement learning）领域中策略（policy）如何与环境（environments）交互、执行动作（action）、处于某些状态（states）的方式作了类比。

### [24:44](https://www.youtube.com/watch?v=Q86qzJ1K1Ss&t=1484s) · b000043

**English**

And the reason why we drew that parallel was to be able to leverage some RL-based techniques in order to train our model. So in this case, we said our LLM is a little bit like a policy. So given some state, which is the input it has received so far, it can perform the next action. And in this case, it is to predict the next token. And this prediction is made in the environment of tokens.

**中文**

我们作这个类比，是为了利用一些基于强化学习（RL）的技术来训练模型。在这里，我们说 LLM 有点像一个 policy。给定某个 state，也就是它截至当前接收到的输入，它可以执行下一个 action。在这里，这个 action 就是预测下一个 token。而这个预测是在 tokens 构成的 environment 中进行的。

### [25:20](https://www.youtube.com/watch?v=Q86qzJ1K1Ss&t=1520s) · b000044

**English**

And when we predict a completion, what we do is, at the end of the day, we have some signal, some reward, which can be the human preference. So this is the parallel we drew with the RL world. And with that in mind, we talked about rewards. But the problem is that rewards are only available for a limited set of data, which is why we saw how to model rewards.

**中文**

当我们预测一段补全内容（completion）时，最终会得到某种信号、某种奖励（reward），它可以是人类偏好。这就是我们与 RL 领域作的类比。在这个思路下，我们讨论了 rewards。但问题是，只有有限的一部分数据带有 rewards，因此我们介绍了如何对 rewards 建模。

### [25:52](https://www.youtube.com/watch?v=Q86qzJ1K1Ss&t=1552s) · b000045

**English**

So we saw this formula. If you remember it's called the Bradley-Terry formulation, which models how the probability of an output being better. Another one is as a function of, I guess, two scores, like the score of output I and the score of output J. And we saw that reward models, they are typically trained by having this formulation in mind in a pairwise fashion.

**中文**

我们介绍过这个公式。如果你们还记得，它叫 Bradley-Terry formulation。它把一个输出优于另一个输出的概率，建模为两个分数的函数，比如输出 I 的分数和输出 J 的分数。我们看到，奖励模型（reward models）通常就是依据这个公式，以成对的方式训练的。

### [26:25](https://www.youtube.com/watch?v=Q86qzJ1K1Ss&t=1585s) · b000046

**English**

So what this means is a reward model, you give it two outputs. You say this one is good, this one is bad. And then I want you to say this one is good. You train it in a pairwise fashion. But then your model is actually predicting always two scores. It's always predicting the score RI for output I, RJ for output J. And so at inference time you're only giving it one output.

**中文**

也就是说，对于一个 reward model，你给它两个输出，告诉它这个好、那个不好，然后希望它能判断出这个好。你以成对的方式训练它。但模型实际上始终在预测两个分数：输出 I 的分数 RI，以及输出 J 的分数 RJ。因此，在推理时，你只需要给它一个输出。

### [26:57](https://www.youtube.com/watch?v=Q86qzJ1K1Ss&t=1617s) · b000047

**English**

So I think that's one subtlety. We train it in a pairwise way. But at inference time, we're using it in an individual way, if that makes sense. And so once we trained our reward model using this formulation, then we were able to use it to steer our LLM towards the direction that we care about. So if you remember, the way we steer our LLM in the direction of human preferences is to give it a prompt so that it can produce a completion, a.k.a., a rollout.

**中文**

我觉得这是一个细节：训练时是成对训练的，但在推理时，我们是单独使用它的，希望这样说能明白。通过这个公式训练好 reward model 后，我们就可以用它把 LLM 引导到我们关心的方向。如果你们还记得，要让 LLM 朝人类偏好的方向调整，我们会给它一个提示（prompt），让它生成一个 completion，也就是一次 rollout。

### [27:40](https://www.youtube.com/watch?v=Q86qzJ1K1Ss&t=1660s) · b000048

**English**

Or in simpler terms, an answer. And then we take this prompt, we take this answer. We put them both in the reward model that tells us how good the model response is. And depending on what the reward model says, we can tune the weights of the LLM in a way that maximizes human or the reward that we saw, which is trained on human preferences.

**中文**

或者简单来说，就是一个回答。然后，我们把这个 prompt 和这个回答一起放进 reward model，让它告诉我们模型的回复有多好。根据 reward model 给出的结果，我们可以调整 LLM 的权重，以最大化人类——或者说，最大化我们刚才看到的那个根据人类偏好训练出来的 reward。

### [28:10](https://www.youtube.com/watch?v=Q86qzJ1K1Ss&t=1690s) · b000049

**English**

And the last function of this RL setup is typically something that tries to maximize rewards, but also keep the model close to the base model. And here, by base model, we mean the SFT model. And the reason why we want that is because this reward is imperfect. So we saw this phenomenon of reward hacking where your reward can be imperfect.

**中文**

这个 RL 设置中的 last function \[字幕疑误，可能指 loss function，损失函数\]，通常既要尽量最大化 rewards，又要让模型保持接近基础模型（base model）。这里说的 base model，是指 SFT 模型。之所以这样做，是因为这个 reward 并不完美。因此我们介绍了奖励投机（reward hacking）现象，也就是 reward 可能存在缺陷。

### [28:45](https://www.youtube.com/watch?v=Q86qzJ1K1Ss&t=1725s) · b000050

**English**

And the LLM can exploit its imperfect nature to tune it in a way that actually does not align with what you want it to be. So you want the LLM to not be too far from the base model, which is actually already a good model. So it's a way to regularize that if you want. And you also want the iteration updates to not be too big either.

**中文**

LLM 可以利用它不完美的地方，以实际上不符合你预期的方式进行调整。因此，你希望 LLM 不要偏离 base model 太远，因为 base model 本来就已经是一个不错的模型。如果你愿意这样理解，这也是一种正则化（regularization）方式。同时，你也不希望每次迭代更新的幅度太大。

### [29:15](https://www.youtube.com/watch?v=Q86qzJ1K1Ss&t=1755s) · b000051

**English**

So you typically have these two constraints. You don't want it to deviate too much from the base model, but you don't want it to deviate too much from the previous RL iteration. And then just as a reminder, I think this was lecture 5 I think was the most technically challenging of the whole class. So completely fine if the first time you were like, what's happening. But hopefully now, it should be a little bit more clear. Cool. And then after lecture 5, we're like, OK, we've done a lot of hard work.

**中文**

所以通常有这两个约束：不希望它偏离 base model 太多，也不希望它偏离上一次 RL 迭代太多。另外提醒一下，我觉得第 5 讲大概是整门课中技术上最难的一讲。所以，如果你们第一次听的时候觉得“这是在干什么”，完全没关系。但希望现在已经稍微清楚一些了。好。第 5 讲之后，我们就想，好，我们已经做了很多艰难的工作。

### [29:47](https://www.youtube.com/watch?v=Q86qzJ1K1Ss&t=1787s) · b000052

**English**

So the good thing is we're in 2025. And in the past 12 months, or now 14 months, we've seen a lot of models that were being released with these reasoning capabilities. And the way they were trained to exhibit these advanced reasoning capabilities was actually leveraging a lot of the techniques that we saw in lecture 5, just like RL based techniques.

**中文**

好消息是，现在是 2025 年。在过去 12 个月，或者说现在已经是 14 个月里，我们看到很多具备这些推理能力（reasoning capabilities）的模型发布了。训练它们展现这些高级推理能力的方法，实际上大量利用了我们在第 5 讲介绍的技术，比如基于 RL 的技术。

### [30:19](https://www.youtube.com/watch?v=Q86qzJ1K1Ss&t=1819s) · b000053

**English**

And in particular, what we want our LLM to do is to output a reasoning chain before producing the final answer. And the reason why we wanted to do that is because people have seen that it improves the performance of the model. And so it's actually relying on this idea of chain of thoughts, which I believe we saw at lecture 3, which is a prompting technique to have your model output the reasoning before outputting the response.

**中文**

具体来说，我们希望 LLM 在给出最终答案之前，先输出一条推理链（reasoning chain）。之所以希望这样做，是因为人们发现这能提高模型性能。它实际上依赖于思维链（chain of thoughts）这个想法，我记得我们是在第 3 讲介绍的。这是一种提示技术（prompting technique），让模型先输出推理过程，再输出回答。

### [30:55](https://www.youtube.com/watch?v=Q86qzJ1K1Ss&t=1855s) · b000054

**English**

So long story short, up until lecture 6 our LLM was having a prompt as input, directly outputting the output. But in lecture 7, we said--sorry, in lecture 6 we said, well, let's have our LLM actually first output a reasoning chain that the user may or may not have access to before outputting the final answer. So you want to teach the LLM to do that.

**中文**

长话短说，在第 6 讲之前，我们的 LLM 接收一个 prompt，然后直接输出结果。但在第 7 讲，我们说——抱歉，是第 6 讲——我们说，先让 LLM 输出一条用户可能看得到、也可能看不到的 reasoning chain，然后再输出最终答案。所以，你要教会 LLM 这样做。

### [31:26](https://www.youtube.com/watch?v=Q86qzJ1K1Ss&t=1886s) · b000055

**English**

So how do you do that? Well, first before doing this, I just want to show you this chart, which we saw, which is the performance of the model as we're teaching it to produce these reasoning chains. So people have typically measured the improvement in performance by comparing it to, I guess, certain benchmarks. And this one is a popular one, the aim benchmark, which is a math benchmark.

**中文**

怎么做到呢？首先，在讲这个之前，我想给大家看一下我们之前见过的这张图，它展示了我们教模型生成这些 reasoning chains 时，模型的性能。人们通常通过某些基准测试（benchmarks）来衡量性能提升。这里是一个很流行的基准，aim benchmark \[字幕疑误，可能指 AIME benchmark\]，它是一个数学基准。

### [31:58](https://www.youtube.com/watch?v=Q86qzJ1K1Ss&t=1918s) · b000056

**English**

And we saw that as the training progresses, the accuracy number of guess what the LLM outputs is increasing. But back to what I was saying. The key technique that we use to teach the model how to output these reasoning chains is leveraging the RL techniques that we saw in lecture 5. And in particular, up until now, we saw PPO was the main RL algorithm that people were using up to maybe last year.

**中文**

我们看到，随着训练推进，LLM 输出的准确率在提升。不过回到刚才的话题，教模型输出这些 reasoning chains 的关键技术，是利用我们在第 5 讲介绍的 RL 技术。具体来说，此前我们看到，PPO 是人们直到大概去年还主要使用的 RL 算法。

### [32:40](https://www.youtube.com/watch?v=Q86qzJ1K1Ss&t=1960s) · b000057

**English**

And now people are kind of prioritizing GRPO as an RL algorithm in order to teach the model to be better at reasoning tasks. And there are several reasons to that I will explicit right now. So we saw this illustration that compared how GRPO was differing with PPO. And if you can see in the graph, there are a few things that are different.

**中文**

而现在，人们更倾向于使用 GRPO 这个 RL 算法，来让模型更擅长推理任务。原因有几个，我马上解释。我们看过这张图，它比较了 GRPO 与 PPO 的区别。如果你们看图，就能看到有几处不同。

### [33:12](https://www.youtube.com/watch?v=Q86qzJ1K1Ss&t=1992s) · b000058

**English**

The first thing is that GRPO does not rely on a value model. So who remembers what the value model is?

**中文**

第一点是，GRPO 不依赖价值模型（value model）。谁还记得 value model 是什么？

### [33:28](https://www.youtube.com/watch?v=Q86qzJ1K1Ss&t=2008s) · b000059

**English**

Yep.

**中文**

对。

### [33:35](https://www.youtube.com/watch?v=Q86qzJ1K1Ss&t=2015s) · b000060

**English**

Yes, exactly. So the value function is trying to predict what the reward would be if you were to follow the policy of the LLM. And I guess it's a way to have some baseline as to how good some predictions are. You want to make it more relative. So the value function is a way for us to make these rewards a little bit more relative to one another.

**中文**

对，完全正确。价值函数（value function）尝试预测，如果遵循 LLM 的 policy，会得到什么 reward。我想，它提供了一个基准，用来衡量某些预测有多好。你希望这种评价更具相对性。所以，value function 是让这些 rewards 能够更相对地相互比较的一种方式。

### [34:09](https://www.youtube.com/watch?v=Q86qzJ1K1Ss&t=2049s) · b000061

**English**

And so that's how PPO was doing this. So it was having a value model that was making these predictions. And then we had these generalized advantage estimation method that was combining the rewards predictions with the value function predictions in order to have what we call advantages. So advantages is how good's your output is compared to some baseline.

**中文**

PPO 就是这样做的：它有一个 value model 来进行这些预测。然后，我们还有广义优势估计（generalized advantage estimation）方法，把 reward 预测与 value function 预测结合起来，得到所谓的优势（advantages）。advantages 就是你的输出相对于某个基准有多好。

### [34:40](https://www.youtube.com/watch?v=Q86qzJ1K1Ss&t=2080s) · b000062

**English**

But then in contrast to that, GRPO said, OK, today, we don't need a value function because it's too expensive to train to maintain what we're going to do instead. Is generate several completions, and then have some formula that compares the rewards of these completions to one another.

**中文**

相比之下，GRPO 说，好，现在我们不需要 value function，因为训练和维护它成本太高。我们改为生成多个 completions，再用某个公式比较这些 completions 的 rewards。

### [35:12](https://www.youtube.com/watch?v=Q86qzJ1K1Ss&t=2112s) · b000063

**English**

So it's going to have some relative effect in a sense that it will make things more relative. And in doing so you're actually not needed to maintain and train a value function. And that's one big difference compared to PPO. And the second big difference, which is not represented in this illustration, is that GRPO is typically an algorithm that people have used in the context of teaching your model to be better at reasoning tasks.

**中文**

这样就会产生某种相对效果，也就是让评价更具相对性。这样做，你实际上就不需要维护和训练一个 value function。这是它与 PPO 的一个重大区别。第二个重大区别没有体现在这张图里，那就是人们通常使用 GRPO 来训练模型，使其更擅长推理任务。

### [35:55](https://www.youtube.com/watch?v=Q86qzJ1K1Ss&t=2155s) · b000064

**English**

And so we saw that these kinds of problems have a verifiable reward because when you complete a math problem, you actually know the answer you need to get to. So you don't need to train a reward model to tell you how good your final answer is, because you already know the answer. And so we saw that GRPO was in particular used in the context of when you actually don't even need reward model, when you actually have a verifiable reward.

**中文**

我们看到，这类问题具有可验证奖励（verifiable reward），因为当你解一道数学题时，你实际上知道最终应该得到什么答案。因此，你不需要训练 reward model 来告诉你最终答案有多好，因为你已经知道答案了。所以我们看到，GRPO 尤其适用于这样的场景：你甚至不需要 reward model，而是拥有 verifiable reward。

### [36:30](https://www.youtube.com/watch?v=Q86qzJ1K1Ss&t=2190s) · b000065

**English**

So at the end of the day, the only two models you need to keep are the policy model and the reference model to be able to just compare how far you are from the reference model.

**中文**

所以最终，你只需要保留两个模型：策略模型（policy model）和参考模型（reference model），以便比较当前模型距离 reference model 有多远。

### [36:49](https://www.youtube.com/watch?v=Q86qzJ1K1Ss&t=2209s) · b000066

**English**

Cool? I know this one was also a challenging class. I guess, so far so good. And this is also on the final. So which is why I'm taking things more slowly for this second part of the recap. So is everything good so far? Yeah? Perfect. We also saw some extensions of GRPO. So if you remember, there was some kind of bias that was a result of the loss function of GRPO having some normalization term that penalized tokens that were in shorter outputs.

**中文**

可以吗？我知道这一讲也挺有挑战性。我想，到目前为止还好吧。这些内容也会出现在期末考试里，所以在回顾的这第二部分，我讲得慢一些。到这里都没问题吗？没问题？很好。我们还介绍了 GRPO 的一些扩展。如果你们还记得，GRPO 的损失函数中有一个归一化项，会对较短输出中的 tokens 施加惩罚，由此产生某种偏差。

### [37:38](https://www.youtube.com/watch?v=Q86qzJ1K1Ss&t=2258s) · b000067

**English**

So we saw that if you use GRPO in its original case, in its original form, we saw that after a certain point, the algorithm will incentivize your model to produce longer and longer answers. Longer and longer incorrect answers. And the reason why it does that is because relative to short, incorrect answers, it penalizes less long incorrect answers.

**中文**

我们看到，如果使用原始形式的 GRPO，在某个阶段之后，算法会激励模型生成越来越长的答案，越来越长的错误答案。它之所以这样做，是因为相比短的错误答案，它对长的错误答案惩罚更轻。

### [38:12](https://www.youtube.com/watch?v=Q86qzJ1K1Ss&t=2292s) · b000068

**English**

And so this is the reason why there are some extensions that people have worked on this year, one of which was GRPO done right. So we saw that they basically removed the normalization term. And there was another method that we saw which was called DAPO, D-A-P-O, which also had some variants.

**中文**

因此，今年人们研究了一些扩展方法，其中一个叫 GRPO done right。我们看到，他们基本上去掉了归一化项。我们还介绍了另一个方法，叫 DAPO，D-A-P-O，它也有一些变体。

### [38:36](https://www.youtube.com/watch?v=Q86qzJ1K1Ss&t=2316s) · b000069

**English**

And that's for reasoning models. And then lecture 7, we had a model that we knew how to train it. We knew how to use it for reasoning tasks, how to train it to be better. But now we wanted the model to be useful and interacting with outside systems. So we saw one technique that is kind of an essential technique called RAG, short for retrieval augmented generation, that is meant for you to be able to fetch relevant documents from some knowledge base in order to answer a question, or answer a prompt.

**中文**

以上是推理模型（reasoning models）的内容。接着到了第 7 讲，我们有了一个知道如何训练的模型，知道如何把它用于推理任务，也知道如何训练得更好。但现在，我们希望模型能发挥作用，并与外部系统交互。于是我们介绍了一种很关键的技术，叫检索增强生成（retrieval augmented generation，RAG），它让你可以从某个知识库中获取相关文档，用来回答问题，或响应一个 prompt。

### [39:26](https://www.youtube.com/watch?v=Q86qzJ1K1Ss&t=2366s) · b000070

**English**

And the reason why you want to do that is that the knowledge of your LLM is including up to the data that is up to the knowledge cutoff date, which is the max dates of what your LLM has been trained on. And from a practical standpoint, I guess from what we see nowadays, you're typically not training your LLM daily or continuously.

**中文**

你之所以要这样做，是因为 LLM 的知识只覆盖到知识截止日期（knowledge cutoff date）之前的数据，也就是 LLM 训练数据所覆盖的最晚日期。从实际情况来看，我想，根据我们现在看到的做法，通常并不会每天训练 LLM，也不会持续不断地训练它。

### [39:58](https://www.youtube.com/watch?v=Q86qzJ1K1Ss&t=2398s) · b000071

**English**

And so in cases where you need your LLM to about things that happened recently or about things that happened that were not in your LLM training data. You want your LLM to have access to such information. And so that's how RAG is very useful. So we saw that RAG depended very heavily on the way it retrieves data. So we saw that the retrieval part was mainly composed of two steps.

**中文**

因此，当你需要 LLM……最近发生的事，或者训练数据中没有包含的事时 \[原文缺词\]，你希望它能够访问这些信息。这就是 RAG 非常有用的地方。我们看到，RAG 非常依赖检索数据的方式。检索部分主要由两个步骤组成。

### [40:33](https://www.youtube.com/watch?v=Q86qzJ1K1Ss&t=2433s) · b000072

**English**

So the first one was candidate retrieval, which uses bye encoder kind of setup where air. You're basically doing some semantic search. So you're computing the embedding of the query. You have some pre-computed embeddings of the documents in your knowledge base, and you're taking the ones that maximize some similarity score. Let's say some cosine similarity.

**中文**

第一步是候选检索（candidate retrieval），采用 bye encoder \[字幕疑误，可能指 bi-encoder，双编码器\] 这种设置，其中 air \[字幕疑误，含义不明\]。基本上，你是在做语义搜索（semantic search）：计算 query 的 embedding，知识库中的文档则已经有预先计算好的 embeddings，然后选出使某种相似度分数最大的文档，比如余弦相似度（cosine similarity）。

### [41:05](https://www.youtube.com/watch?v=Q86qzJ1K1Ss&t=2465s) · b000073

**English**

So this first step is allowing you to retrieve, I guess, a filtered version of the potential documents. And then typically, you have a second step, which is called ranking--or reranking because the first step already gives you a ranking--which has typically a more sophisticated setup. So it's a cross encoder kind of setup where you have your query and your document that are both fed to some model and produces a more precise score.

**中文**

第一步让你检索到一批经过筛选的潜在相关文档。通常还会有第二步，叫排序（ranking）——或者重排序（reranking），因为第一步已经给出了一个排序——这一阶段的设置通常更复杂。它采用交叉编码器（cross encoder）的设置，把 query 和文档一起输入某个模型，生成一个更精确的分数。

### [41:45](https://www.youtube.com/watch?v=Q86qzJ1K1Ss&t=2505s) · b000074

**English**

And then you use this final score to rank the final results. And you typically choose the top, let's say, k. And then you add them to your prompts. So it's the augmented part. So retrieval is everything I mentioned so far. And then once you have the relevant documents, you add them in your prompt, which is the augmented part. And you generate the answer. So the reason why I'm taking so much time on RAG is RAG is such an important concept.

**中文**

然后，用这个最终分数对结果排序。通常会选择排名最前面的，比如 k 个，再把它们加入 prompts。这就是增强（augmented）的部分。检索（retrieval）就是我到目前为止提到的所有步骤。得到相关文档后，把它们加进 prompt，这就是 augmented 部分，然后生成答案。我在 RAG 上花这么多时间，是因为它是一个非常重要的概念。

### [42:18](https://www.youtube.com/watch?v=Q86qzJ1K1Ss&t=2538s) · b000075

**English**

Also, if you were to have interviews or also maybe in the exam who knows. So I think it's an important concept to have in mind. The second one that we saw was tool calling. And tool calling is allowing your LLM to leverage tools. The way it does that is in two steps.

**中文**

此外，如果你要参加面试，或者也许考试会考，谁知道呢。所以我觉得这是一个需要记住的重要概念。我们介绍的第二个概念是工具调用（tool calling）。tool calling 让 LLM 能够利用工具，具体分两步进行。

### [42:48](https://www.youtube.com/watch?v=Q86qzJ1K1Ss&t=2568s) · b000076

**English**

The first step is for your model to which API there is out there, at the end of which your LLM says, OK, I want to use this API and I want to use it with these arguments. And then you have an intermediary step, which is you just run your API with these arguments. And then the second step is you feed the results of this operation back to the LLM, which then produces a final answer.

**中文**

第一步是让模型……有哪些 API 可用 \[原文缺词\]。这一步结束时，LLM 会说，好，我想使用这个 API，并传入这些参数。然后有一个中间步骤，也就是用这些参数实际运行 API。第二步则是把这次操作的结果反馈给 LLM，让它生成最终答案。

### [43:22](https://www.youtube.com/watch?v=Q86qzJ1K1Ss&t=2602s) · b000077

**English**

So that's how tool calling works. So if you say to your LLM, you can use this API, this is how your LLM would leverage that. And then we saw that modern day agentic workflows we're leveraging both RAG and tool calling as key methods to perform actions. And we saw an example, data example, which was such that you had some inputs.

**中文**

这就是 tool calling 的工作方式。所以，如果你告诉 LLM，你可以使用这个 API，它就会以这种方式使用。接着我们看到，如今的智能体工作流（agentic workflows）会把 RAG 和 tool calling 都作为执行操作的关键方法。我们看过一个例子，一个 data example \[字幕疑误，可能指该例子的名称\]，其中你有一些输入。

### [43:54](https://www.youtube.com/watch?v=Q86qzJ1K1Ss&t=2634s) · b000078

**English**

And then your LLM had a series of different calls in order to perform some action. And then at the end of it, it retrieves-- sorry, it returns an answer.

**中文**

然后，LLM 进行一系列不同的调用，以执行某项操作。最后，它会检索——抱歉，是返回一个答案。

### [44:09](https://www.youtube.com/watch?v=Q86qzJ1K1Ss&t=2649s) · b000079

**English**

Cool. And then last lecture, we saw how we could evaluate LLMs, which is a much tougher thing to do now that LLMs can do a bunch of different things. So we first saw that there was some rule based metrics that people were using before LLMs came into play, metrics that you may have heard like BLEU, ROUGE, METEOR, and so on.

**中文**

好。上一讲，我们介绍了如何评估 LLMs。如今 LLMs 能做很多不同的事情，所以评估也难得多。我们先介绍了在 LLMs 出现之前，人们使用的一些基于规则的指标（rule based metrics），你们可能听说过，比如 BLEU、ROUGE、METEOR 等。

### [44:42](https://www.youtube.com/watch?v=Q86qzJ1K1Ss&t=2682s) · b000080

**English**

But the main limitation was that they were not considering how language could differ, but still be correct. And so this key idea that we saw was why not leverage LLMs to evaluate outputs. And so there is this key idea of LLM as a judge where you receive as input the prompts. The model response along with the criteria that you want the response to be evaluated on.

**中文**

但它们的主要局限是，没有考虑到语言表达即使不同，也仍然可能是正确的。所以，我们介绍了一个关键想法：为什么不利用 LLMs 来评估输出呢？这就是用 LLM 作为评判者（LLM as a judge）的核心想法：输入包括 prompts、模型回复，以及你希望据以评价回复的标准。

### [45:19](https://www.youtube.com/watch?v=Q86qzJ1K1Ss&t=2719s) · b000081

**English**

And then you want your LLMs to output two things. The first one is a rationale for why a given score is outputs along with that score. So nowadays, LLM as the judges are typically outputting a binary response, either pass or fail, true or false, just because it's easier. And we're also having the rationale be output before the score, because in practice it's something that also improves the performance of the LLM as a judge.

**中文**

然后，你希望 LLMs 输出两样东西。第一个是给出某个分数的理由，以及这个分数本身。如今，LLM as a judge 通常会输出一个二元结果，要么通过、要么不通过，要么真、要么假，因为这样更简单。我们还会让它先输出理由，再输出分数，因为实践中，这也能提高 LLM as a judge 的表现。

### [46:00](https://www.youtube.com/watch?v=Q86qzJ1K1Ss&t=2760s) · b000082

**English**

A little bit if you want, like reasoning models do, by outputting the reasoning chain before they output the answer.

**中文**

你可以理解为，这有点像 reasoning models 在输出答案之前，先输出 reasoning chain。

### [46:09](https://www.youtube.com/watch?v=Q86qzJ1K1Ss&t=2769s) · b000083

**English**

But then we also saw that there were some biases that came with this approach. We saw a position bias, which is the way you present the LLMs to compare matters. So if you present something first, then maybe the LLM will just prioritize that first. So there's position bias. There was verbosity bias, which is your LLM just preferring longer outputs. And self-enhancement bias was another one where it prefers its own outputs.

**中文**

但我们也看到，这种方法会带来一些偏差。我们介绍了位置偏差（position bias），也就是你把待比较内容呈现给 LLMs 的方式会产生影响。如果先呈现某个内容，LLM 可能就会优先选择它。这就是 position bias。还有冗长偏差（verbosity bias），也就是 LLM 偏好更长的输出。另一个是自我增强偏差（self-enhancement bias），指模型更喜欢自己的输出。

### [46:42](https://www.youtube.com/watch?v=Q86qzJ1K1Ss&t=2802s) · b000084

**English**

And then we also saw a number of benchmarks that people use nowadays in order to say how great their LLM is. So if you see the releases that come out, there are typically a bunch of metrics across a number of different benchmarks that people know about. So that spans knowledge, the ability to reason coding, which is very important because a lot of applications are coding related, and then safety.

**中文**

我们还介绍了如今人们用来说明自己的 LLM 有多强的一系列 benchmarks。如果你们看发布的模型，通常都会有一系列知名 benchmarks 上的指标。这些涵盖知识、推理能力、编程——编程非常重要，因为很多应用都与编程有关——以及安全性。

### [47:13](https://www.youtube.com/watch?v=Q86qzJ1K1Ss&t=2833s) · b000085

**English**

And then this is not an extensive list. So there's actually many more dimensions.

**中文**

这并不是一个详尽的列表，实际上还有更多维度。

### [47:23](https://www.youtube.com/watch?v=Q86qzJ1K1Ss&t=2843s) · b000086

**English**

So yeah, I think that's where we stopped. And it was last lecture. And this is all you're expected to know for the final. Everything after that is not going to be part of the final.

**中文**

对，我想我们就讲到这里，这就是上一讲的内容。期末考试要求你们掌握的就是这些，后面的所有内容都不属于期末考试范围。

### [47:44](https://www.youtube.com/watch?v=Q86qzJ1K1Ss&t=2864s) · b000087

**English**

Any questions on this so far?

**中文**

到这里，大家有什么问题吗？

### [47:54](https://www.youtube.com/watch?v=Q86qzJ1K1Ss&t=2874s) · b000088

**English**

Cool. I'm expecting 100 for everyone for the final. But yeah, I would say, what I went through is going to be foundational for the final. So I guess if you understood everything I said, I think you're going to be ready for the final. So, yeah. But if you have any questions, Shervine and I are always here to--oh, yeah. You have a question.

**中文**

好。我期待大家期末都考 100 分。对，我想说，刚才回顾的内容是期末考试的基础。所以，如果你们理解了我讲的所有内容，我觉得就已经为期末做好准备了。对。但如果还有任何问题，Shervine 和我一直都在，可以——哦，对，你有个问题。

### [48:29](https://www.youtube.com/watch?v=Q86qzJ1K1Ss&t=2909s) · b000089

**English**

Yes, so the question is the scope for the final lecture 5 to lecture 8. Yes. So for midterm, it was lectures 1, 2, 3, 4. And this one is 5, 6, 7, 8. So I guess it's equal size.

**中文**

对，问题是期末考试范围是不是第 5 讲到第 8 讲。是的。期中考试是第 1、2、3、4 讲，这次是第 5、6、7、8 讲。所以我想，范围大小是一样的。

### [48:45](https://www.youtube.com/watch?v=Q86qzJ1K1Ss&t=2925s) · b000090

**English**

Cool? OK, great. So with that said, we just finished recapping this entire quarter worth of lectures. And now we're going to go to the second item of today's menu, which is looking at some trending topics. And so I'm going to start with the first one. And I'm going to introduce it as follows. So if you remember, we saw that the transformer was a concept and an architecture that was first introduced in the context of machine translation.

**中文**

可以吗？好，非常好。这样，我们就回顾完了整个学季的课程。现在进入今天的第二项安排，也就是看看一些热门话题。我先讲第一个，会这样引入。如果你们还记得，我们看到，transformer 这个概念和架构最初是在机器翻译（machine translation）领域提出的。

### [49:26](https://www.youtube.com/watch?v=Q86qzJ1K1Ss&t=2966s) · b000091

**English**

So it performed great. People said, OK, it performs great on machine translation, why not try it on other text tasks. So they tried it. Performed great. But now the question is, can you not use it for things other than texts. It's a natural question. So in order to answer that question, I just want us to remind ourselves that this architecture is relying on this concept of self attention.

**中文**

它的表现很好。人们就说，好，它在 machine translation 上表现这么好，为什么不试试其他文本任务呢？于是大家试了，表现也很好。但现在的问题是，能不能把它用于文本以外的东西？这是个很自然的问题。为了回答这个问题，我想先提醒大家，这个架构依赖的是 self attention 这个概念。

### [50:01](https://www.youtube.com/watch?v=Q86qzJ1K1Ss&t=3001s) · b000092

**English**

And this is what is making the transformer work so well. So if we just recap what self-attention is--this illustration kind of does the job quite well--you have a query, and then you have a bunch of other elements, which are represented by your keys and your values. And you want to know which other elements are actually relevant in order to compute the embedding for that query.

**中文**

正是它让 transformer 表现如此出色。我们简单回顾一下 self-attention——这张图解释得相当清楚——你有一个 query，还有一组其他元素，分别由 keys 和 values 表示。你想知道，为了计算这个 query 的 embedding，哪些其他元素实际上与它相关。

### [50:37](https://www.youtube.com/watch?v=Q86qzJ1K1Ss&t=3037s) · b000093

**English**

So right now, we have only used tokens, text tokens. But text tokens, they're actually vectors. So if you take those vectors, and you actually represent something else than text--like for instance, parts of an image--the question is, would the transformer based on that kind of input also perform well.

**中文**

到目前为止，我们只用过 tokens，也就是文本 tokens。但文本 tokens 实际上是向量。所以，如果你用这些向量去表示文本以外的东西，比如图像的不同部分，问题就是：基于这种输入的 transformer，是否也能表现良好？

### [51:14](https://www.youtube.com/watch?v=Q86qzJ1K1Ss&t=3074s) · b000094

**English**

And so here the key question that I want to ask is, how can we adapt our transformer to work on non-text input. And for instance, here we can think of image understanding input. So you have some image. And so it's a traditional computer vision task where you want to in which class this image belongs to. So you want to know if having some transformer based architecture would work well in that situation.

**中文**

这里我想提出的关键问题是，如何调整 transformer，使它能够处理非文本输入？例如，我们可以考虑图像理解的输入。你有一张图像，这是一个传统的计算机视觉（computer vision）任务，你想……这张图像属于哪个类别 \[原文缺词\]。你想知道，基于 transformer 的架构在这种情况下能否表现良好。

### [51:49](https://www.youtube.com/watch?v=Q86qzJ1K1Ss&t=3109s) · b000095

**English**

Well, the answer to that is, well, first, in order to adapt it to this task, you would take the encoder parts of the transformer because in order to understand what is in an image, you need to classify that image in some sense. So if you remember, if there is a one model--and what we saw that was working very well for classification was BERT, because BERT is encoder only.

**中文**

答案是，首先，为了让它适应这个任务，你会采用 transformer 的 encoder 部分，因为为了理解图像里有什么，从某种意义上说，你需要对图像分类。如果你们还记得，我们看到过一个在分类上表现非常好的模型，就是 BERT，因为 BERT 是仅 encoder 的模型。

### [52:22](https://www.youtube.com/watch?v=Q86qzJ1K1Ss&t=3142s) · b000096

**English**

It computes meaningful embeddings that can then be used for projection purposes or for classification purposes. So it's a very natural choice that here we would have. So here, we would just keep the encoder part of the transformer and then have the self-attention mechanism come into play and compute meaningful embeddings that we could then project for our relevant task.

**中文**

它能够计算有意义的 embeddings，然后用于投影或分类。所以，这对我们来说是一个非常自然的选择。在这里，我们只保留 transformer 的 encoder 部分，让 self-attention 机制发挥作用，计算出有意义的 embeddings，再把它们投影到相关任务所需的空间。

### [52:55](https://www.youtube.com/watch?v=Q86qzJ1K1Ss&t=3175s) · b000097

**English**

And this is exactly what a group of researchers did back in 2020. So have you heard of VIT, vision transformer. Yeah, no, yeah? So what I described here is exactly what they did. So they took an image. They divided that image into patches. Those patches were represented by some vectors.

**中文**

这正是一组研究人员在 2020 年所做的事。你们听说过 VIT，也就是视觉 transformer（vision transformer）吗？听过，没听过，听过？我刚才描述的就是他们的做法：取一张图像，把它分割成图像块（patches），再用一些向量来表示这些 patches。

### [53:26](https://www.youtube.com/watch?v=Q86qzJ1K1Ss&t=3206s) · b000098

**English**

And of course, you have some kind of position information that allows you to know where your patches in the image. And then you just put it through the transformer encoder. So the encoder part of the transformer. And you compute the representation corresponding to the CLS class, very similar to BERT. And you would just project that representation over some classes of interest.

**中文**

当然，还需要某种位置信息，让你知道各个 patches 在图像中的位置。然后，把它们送入 transformer encoder，也就是 transformer 的 encoder 部分。接着计算对应于 CLS class 的表示，与 BERT 非常相似，再把这个表示投影到你关心的若干类别上。

### [53:57](https://www.youtube.com/watch?v=Q86qzJ1K1Ss&t=3237s) · b000099

**English**

And then you would perform your, I guess, computation like this. So what that paper found was that if you train such a model on a lot of image data, a lot of image data, you then outperform these is traditional convolutional neural network kind of methods. And it was kind of remarkable because.

**中文**

然后，我想，你就这样进行计算。那篇论文发现，如果用大量图像数据、大量图像数据来训练这样的模型，它就能胜过传统的卷积神经网络（convolutional neural network）类方法。这有点令人惊讶，因为。

### [54:28](https://www.youtube.com/watch?v=Q86qzJ1K1Ss&t=3268s) · b000100

**English**

So why is it remarkable. Because in the vision case. So there is this concept of inductive bias where you want to gear your model towards looking at certain things in order to deduce the results. So convolutional neural networks are a kind of model that are designed in a way for you to look at the image in some sliding way.

**中文**

为什么令人惊讶呢？因为在视觉领域，有一个叫归纳偏置（inductive bias）的概念，你希望引导模型关注某些东西，以便推导出结果。convolutional neural networks 就是这样一类模型，其设计让它以某种滑动的方式查看图像。

### [55:02](https://www.youtube.com/watch?v=Q86qzJ1K1Ss&t=3302s) · b000101

**English**

You look at your image a little bit like you would look at it in practice as a human. And people had hypothesized that such a bias, such an inductive bias would actually make sense for something like a vision task. So you contrast that with the vision transformer, which is actually letting all parts of the image attend to one another, which has, on the other side, very low inductive bias.

**中文**

它查看图像的方式，有点像人类实际查看图像的方式。人们曾经假设，对于视觉任务，这样的偏置、这样的 inductive bias 应该是合理的。而与之相比，vision transformer 让图像的所有部分彼此关注，相对来说，它的 inductive bias 很弱。

### [55:33](https://www.youtube.com/watch?v=Q86qzJ1K1Ss&t=3333s) · b000102

**English**

So what this paper showed was if you give your model enough data, then it will actually learn how to classify, I guess, your images in these classes. So this was kind of a remarkable result. So I think this was pretty remarkable and a nice extension of everything we saw. So with that in mind, I want us to just go through an end to end example of how you would process an image and go through that VIT, so vision transformer, in order to make your prediction.

**中文**

这篇论文表明，只要给模型足够的数据，它就能学会把图像分到这些类别中。这是一个相当了不起的结果。我觉得这非常了不起，也是我们所学内容的一个很好的延伸。带着这个想法，我想和大家一起走一遍端到端的例子，看看如何处理一张图像，让它经过 VIT，也就是 vision transformer，来完成预测。

### [56:15](https://www.youtube.com/watch?v=Q86qzJ1K1Ss&t=3375s) · b000103

**English**

So here, you would take your favorite image that you would just split into patches. So here, you can think of you predefining some fixed size patches. So here, I would say 3 by 3, let's say. And then each patch has some fixed number of pixels. And then what you do is for each patch, you try to have some vector representation.

**中文**

这里，你可以拿一张最喜欢的图像，把它切成 patches。你可以预先定义固定大小的 patches。比如这里，我会说是 3 乘 3，假设如此。每个 patch 都有固定数量的像素。然后，对每个 patch，你都尝试得到某种向量表示。

### [56:45](https://www.youtube.com/watch?v=Q86qzJ1K1Ss&t=3405s) · b000104

**English**

So you can think of each patch as--so what is the patch. So it's composed of pixels. So if each pixel has three values which correspond to red, green, and blue, then you can find a way to project those on some lower dimensional flattened space. And you can learn how you would project that through some kind of linear layer. So long story short, you just find a way to associate a vector to each of these patches, which you then represent every single one of your input.

**中文**

你可以把每个 patch 看作——patch 是什么呢？它由像素组成。如果每个像素有三个值，分别对应红、绿、蓝，那么你就可以找一种方法，把它们投影到某个更低维的展平空间中。你可以通过某种线性层（linear layer）来学习这种投影。长话短说，就是想办法为每个 patch 配上一个向量，用它们表示每一个输入。

### [57:31](https://www.youtube.com/watch?v=Q86qzJ1K1Ss&t=3451s) · b000105

**English**

And then you have, of course, a special embedding for the CLS token, which you can also learn, and you add the position embedding. So you do the same for all of your inputs. And then very similar to BERT, Just put that through your encoder. Let everyone interact with everyone. And then at the end of the day, what you care about is a representation of the input that is meaningful.

**中文**

当然，你还会为 CLS token 准备一个特殊的 embedding，它也可以学习，然后加上位置嵌入（position embedding）。对所有输入都这样做。接着，与 BERT 非常相似，把它们送进 encoder，让每个元素都与其他所有元素交互。最终，你关心的是获得一个有意义的输入表示。

### [58:01](https://www.youtube.com/watch?v=Q86qzJ1K1Ss&t=3481s) · b000106

**English**

So typically, people take the encoder embedding of the CLS token. So the reason why they take that is one, because it's a convention. But the second one is this CLS token. So the encoded embedding is actually an embedding that has interacted with all other tokens through this self-attention mechanism. So it has seen everything. And then you would project that CLS token encoded embedding onto some class through a feed forward neural network in order to predict your final class.

**中文**

通常，人们会采用 CLS token 的 encoder embedding。一个原因是这是一种惯例。另一个原因是，这个 CLS token 编码后的 embedding，实际上已经通过 self-attention 机制与所有其他 tokens 交互过。所以它看到了全部内容。然后，通过一个 feed forward neural network，把 CLS token 编码后的 embedding 投影到某个类别上，以预测最终类别。

### [58:45](https://www.youtube.com/watch?v=Q86qzJ1K1Ss&t=3525s) · b000107

**English**

So in this case, we know it's a picture of a Teddy bear. So here, we would want the model to classify this as a Teddy bear.

**中文**

在这个例子里，我们知道这是一张泰迪熊的照片。所以，我们希望模型把它分类为泰迪熊。

### [58:54](https://www.youtube.com/watch?v=Q86qzJ1K1Ss&t=3534s) · b000108

**English**

So far so good? Does that make sense?

**中文**

到这里还好吗？能理解吗？

### [59:00](https://www.youtube.com/watch?v=Q86qzJ1K1Ss&t=3540s) · b000109

**English**

Cool. So now we know how to process image input right now. So another question is, how would you have your LLM answer questions about your image, which is something that you can do actually nowadays. If you open ChatGPT, you can input an image and ask it questions. So you would have two kinds of inputs.

**中文**

好。现在我们已经知道如何处理图像输入。另一个问题是，如何让 LLM 回答关于图像的问题？这其实是如今已经可以做到的事。如果你打开 ChatGPT，就可以输入一张图像，并就它提出问题。这时会有两种输入。

### [59:32](https://www.youtube.com/watch?v=Q86qzJ1K1Ss&t=3572s) · b000110

**English**

So you would have an image which we can find a way to represent, and then the text, which you now know very well how to represent with tokens. So the way you would allow the model or let the model process all of this is typically as follows-- so there are a couple of methods. The first one is the most common one, which is you just feed everything as input.

**中文**

一种是图像，我们可以找到方法来表示它；另一种是文本，现在你们已经很熟悉如何用 tokens 表示文本了。通常，让模型处理所有这些输入的方法如下——有几种方法。第一种也是最常见的，就是把所有内容都作为输入送进去。

### [1:00:03](https://www.youtube.com/watch?v=Q86qzJ1K1Ss&t=3603s) · b000111

**English**

So the image token as input, the text tokens as inputs. And you have some representation to have the model just know that these are image tokens and this is text token. And then you let it generate an answer in a decoder only fashion, autoregressive fashion exactly like you would do it. The first method and a lot of such models are designed that way. So there is, for instance, a very popular open weight, I believe vision language model, VLM--that's what they are called a model called LAVA--And this is how they do it.

**中文**

图像 token 作为输入，文本 tokens 也作为输入。你会用某种表示方式，让模型知道这些是图像 tokens，那些是文本 tokens。然后，让它以仅 decoder、自回归的方式生成答案，就和你原来做的一样。这是第一种方法，很多这样的模型都是这样设计的。比如，有一个很流行的开放权重模型，我记得是一种视觉语言模型（vision language model，VLM）——这类模型就是这么叫的——叫 LAVA \[字幕疑误，可能指 LLaVA\]，它就是这样做的。

### [1:00:47](https://www.youtube.com/watch?v=Q86qzJ1K1Ss&t=3647s) · b000112

**English**

So they have some encoder on the image parts that produces some tokens that are then concatenated with text tokens that are inputs into the LLM. So that's one method. The second method, which is less common, is to have the images be inputs at the cross-attention layer. So here, what you would do is you have your text inputs.

**中文**

它们用某个 encoder 处理图像部分，生成一些 tokens，再把这些 tokens 与文本 tokens 拼接起来，输入 LLM。这是一种方法。第二种方法没那么常见，是在交叉注意力层（cross-attention layer）输入图像。在这里，你会有文本输入。

### [1:01:19](https://www.youtube.com/watch?v=Q86qzJ1K1Ss&t=3679s) · b000113

**English**

And then your image inputs, you don't put it in the inputs. You actually let it interact with the text tokens within the cross-attention layer. And this is something that, for instance, Llama 3 had represented in their paper. This technique is typically less common. The first one is more common. So I guess what I want to say is CME 295 focused on the transformer specifically in the case of text to text problems.

**中文**

而图像输入，你不会把它放在输入端，而是让它在 cross-attention 层内与文本 tokens 交互。例如，Llama 3 的论文里就展示了这种做法。这种技术通常没那么常见，第一种更常见。我想说的是，CME 295 重点讲的是 transformer，具体来说，是文本到文本问题中的 transformer。

### [1:01:58](https://www.youtube.com/watch?v=Q86qzJ1K1Ss&t=3718s) · b000114

**English**

So text generation is all this class. But we also have the transformer that was used for non-text applications. So here, we saw image understanding. So vision understanding with VIT. And then we will not have the time to see this now. But also for image generation tasks, we can also have parts of the transformer be used in that architecture.

**中文**

所以，这门课讲的都是文本生成。但 transformer 也被用于非文本应用。这里，我们看到了图像理解，也就是用 VIT 进行视觉理解。现在我们没有时间讲了，不过在图像生成任务中，也可以把 transformer 的某些部分用在相应架构里。

### [1:02:29](https://www.youtube.com/watch?v=Q86qzJ1K1Ss&t=3749s) · b000115

**English**

And so you may hear about diffusion transformer or multimodal diffusion transformer that actually rely on the self-attention mechanism. And this is actually not an exhaustive list. This is also something that has been used in other domains like recommendation speech and so on. So I guess what I want you to remember from this is that transformers was an architecture that performed very well for machine translation tasks.

**中文**

你们可能会听到扩散 transformer（diffusion transformer）或多模态扩散 transformer（multimodal diffusion transformer），它们实际上都依赖 self-attention 机制。这也不是一个完整的列表，它还被用在推荐、语音等其他领域。我希望你们记住的是，transformers 是一种最初在机器翻译任务上表现非常好的架构。

### [1:03:08](https://www.youtube.com/watch?v=Q86qzJ1K1Ss&t=3788s) · b000116

**English**

But then it proved to perform very well for other text related tasks. And it was then reused in a bunch of other domains, which also proved to be quite successful. So I would just encourage you, after this class, to also keep an open mind for non-text related transformer applications. And the ones that I mentioned here are maybe just a few first few pointers into the kind of papers that you can look at.

**中文**

但后来证明，它在其他文本相关任务上也表现很好。之后，它被复用到很多其他领域，同样取得了相当不错的成功。所以，我鼓励你们在这门课结束之后，也对非文本的 transformer 应用保持开放的态度。我在这里提到的这些，也许只是你们可以阅读的相关论文的一些初步线索。

### [1:03:41](https://www.youtube.com/watch?v=Q86qzJ1K1Ss&t=3821s) · b000117

**English**

Cool. So here, we said that transformer was something that came from the text world that's also useful and used in other worlds. Now I want to tell you about something else that was, I guess, used and useful in the non-text worlds that may be useful in the text world. And I want to tell you about diffusion-based LLMs.

**中文**

好。刚才我们说，transformer 来自文本领域，但在其他领域也有用，也得到了应用。现在，我想介绍另一个东西，它原本在非文本领域被使用、也很有用，而现在可能在文本领域同样有用。我想讲的是基于扩散的 LLMs（diffusion-based LLMs）。

### [1:04:11](https://www.youtube.com/watch?v=Q86qzJ1K1Ss&t=3851s) · b000118

**English**

So who has heard the term diffusion? Who knows about diffusion? Yeah. Cool. So we will see how we can apply that to LLMs. So this is a very trendy topic. I believe the first paper started in the early 2020s, but I guess it's only now that people are starting to have this really work. I just want to start with the motivation, which is that up until now, we have taken for granted the fact that our LLM is an autoregressive LLM.

**中文**

谁听说过扩散（diffusion）这个词？谁了解 diffusion？有，好。我们会看看如何把它应用到 LLMs。这是一个非常热门的话题。我记得最早的论文出现在 2020 年代初，但我想，直到现在，人们才开始让它真正发挥作用。我想先从动机讲起：到目前为止，我们一直理所当然地认为，LLM 是一个自回归 LLM。

### [1:04:50](https://www.youtube.com/watch?v=Q86qzJ1K1Ss&t=3890s) · b000119

**English**

And by autoregressive, what do I mean by that? So it takes some input. And what the LLM tries to do is to predict the next token. So given everything so far, we predict the next token. We do that, and then we take that token that we just predicted, along with everything that we have predicted so far. And then we, again, predict the next token.

**中文**

自回归是什么意思呢？它接收一些输入，然后 LLM 尝试预测下一个 token。也就是，给定截至当前的全部内容，预测下一个 token。完成之后，把刚预测出的这个 token，与此前已经预测出的所有内容放在一起，然后再次预测下一个 token。

### [1:05:22](https://www.youtube.com/watch?v=Q86qzJ1K1Ss&t=3922s) · b000120

**English**

We predict it and we go again and again, up until finishing the sequence with that end of sequence token, which makes the generation stop. So this is a true autoregressive generation, as in we take the input so far in order to predict the next token. And then we repeat this process until the end.

**中文**

预测出来之后，就这样一遍又一遍地重复，直到通过序列结束 token（end of sequence token）结束序列，让生成停止。这就是真正的自回归生成：用截至当前的输入预测下一个 token，然后重复这个过程，直到结束。

### [1:05:49](https://www.youtube.com/watch?v=Q86qzJ1K1Ss&t=3949s) · b000121

**English**

So it's something that people now try to give it a name, which is like autoregressive model kind of model. So ARM, if you see this notation, that's what it means. The problem with that kind of paradigm is that inference time generation is actually not something you can parallelize, because you always need what's before in order to predict the next one.

**中文**

所以，现在大家试着给它起个名字，叫自回归模型（autoregressive model）这一类模型。所以，如果你看到 ARM 这个记号，它指的就是这个。这种范式的问题是，推理时的生成（inference time generation）实际上无法并行化，因为你总是需要前面的内容才能预测下一个。

### [1:06:24](https://www.youtube.com/watch?v=Q86qzJ1K1Ss&t=3984s) · b000122

**English**

But I just want to say that inference time generation is not parallelizable, but training is parallelizable. So if you remember, the way we do training is we input all the tokens that we want our model to predict and then we let the model generate tokens out of this. So basically in a decoder only setting you have this causal mask which lets your model not cheat if you want and not use the future ones.

**中文**

不过我想说的是，推理时的生成无法并行化，但训练可以并行化。如果你们还记得，我们训练时的做法是，输入所有希望模型预测的词元（token），然后让模型据此生成 token。所以，基本上，在仅解码器（decoder only）的设置中，有一个因果掩码（causal mask），它让模型不能作弊，如果你愿意这么说的话，也就是不能利用未来的 token。

### [1:07:04](https://www.youtube.com/watch?v=Q86qzJ1K1Ss&t=4024s) · b000123

**English**

So I just want to say that when I say that this paradigm is not parallelizable, I just want to emphasize on the fact that it's an inference time that I'm saying. Training time, you can actually parallelize that quite well.

**中文**

所以，我想说，当我说这种范式无法并行化时，我想强调的是，我指的是推理阶段。训练阶段实际上可以很好地并行化。

### [1:07:18](https://www.youtube.com/watch?v=Q86qzJ1K1Ss&t=4038s) · b000124

**English**

So as I mentioned, that's one of the reasons why people have tried to look at other paradigms. And in particular, so if you know about diffusion, you know that it works very well for the vision domain. And so people have tried adapting this paradigm for the text generation case. And so this is a bunch of screenshots we took from an announcement that happened this year. So for instance, earlier this year, there was an experimental text diffusion model from Google that they presented during the I/O event, which was very impressive because it led to a lot of speed ups.

**中文**

正如我提到的，这也是大家尝试探索其他范式的原因之一。具体来说，如果你了解扩散（diffusion），你就知道它在视觉领域效果非常好。因此，大家尝试把这种范式用于文本生成。这里是我们从今年的一次发布中截取的一些截图。例如，今年早些时候，Google 在 I/O 活动上展示了一个实验性的文本 diffusion 模型，非常令人印象深刻，因为它带来了很大的速度提升。

### [1:08:00](https://www.youtube.com/watch?v=Q86qzJ1K1Ss&t=4080s) · b000125

**English**

And then we have some different startups. So Inception is one of them that made headlines I believe a couple of weeks ago, or last week. No, sorry, a month ago. That also are pursuing this route. So all of that to say that this direction is a very trendy and hot direction that potentially has a lot of promise. But the key issue with this is that text is discrete, whereas images are continuous.

**中文**

此外，还有一些不同的初创公司。Inception 就是其中之一，我记得它在几周前，或者上周，登上了新闻头条。不，抱歉，是一个月前。它们也在探索这条路线。说这些是想说明，这是一个非常流行、非常热门的方向，可能很有前景。但这里的关键问题是，文本是离散的，而图像是连续的。

### [1:08:37](https://www.youtube.com/watch?v=Q86qzJ1K1Ss&t=4117s) · b000126

**English**

And we're going to see why that distinction that I just made matters. So I'm going to try to explain to you what diffusion is in two minutes. So in the image world, in order to generate an image, what people typically do is they start from noise, and then they try to generate some image. Now you may wonder, OK, why noise.

**中文**

接下来我们会看到，我刚才说的这种区别为什么重要。我会试着用两分钟向你们解释什么是 diffusion。在图像领域，为了生成图像，大家通常从噪声开始，然后尝试生成某个图像。你可能会想，好吧，为什么是噪声？

### [1:09:09](https://www.youtube.com/watch?v=Q86qzJ1K1Ss&t=4149s) · b000127

**English**

Well, you cannot do something autoregressive because I guess, if you were to say, OK, let's predict the pixels one at a time, it's just not tractable because there are many pixels in an image. And this is typically not how you would produce an image. But some other reasons are that noise is just something that you can model very well with some very popular distributions. So Gaussian distribution, if you about it, it has very nice properties.

**中文**

嗯，你没法采用自回归的做法，因为我想，如果你说，好吧，我们一次预测一个像素，这就不可行了，因为一张图像中有很多像素。而且这通常也不是你生成图像的方式。不过还有一些原因，噪声可以用一些非常常见的分布很好地建模。例如高斯分布（Gaussian distribution），如果你了解它的话，它有一些非常好的性质。

### [1:09:43](https://www.youtube.com/watch?v=Q86qzJ1K1Ss&t=4183s) · b000128

**English**

Also, noise is very easy to sample. So it's very easy to start with that. Noise is also a way for you to introduce randomness, because you don't necessarily want to always produce the same image. You want to have, I guess, choice of generating images that are slightly different from one another. And just mathematically, it works quite well. And speaking of that, the goal is to learn some transformation that would allow you to go from noise to the target image distribution.

**中文**

此外，噪声很容易采样，因此很容易从它开始。噪声也是引入随机性的一种方式，因为你不一定总想生成同一张图像。我想，你希望能够选择生成彼此略有不同的图像。而且从数学上来说，它也很有效。说到这一点，目标就是学习某种变换，让你能从噪声到达目标图像分布。

### [1:10:26](https://www.youtube.com/watch?v=Q86qzJ1K1Ss&t=4226s) · b000129

**English**

So all of what I said here is just reasons for me to tell you noise is actually a choice that is quite natural to start with in order to generate an image. And to give you an analogy, let's suppose you're a sculptor. So the person who does sculptures. So if you want to do a sculpture, you typically start with some rock.

**中文**

所以，我这里说的这些，都是为了告诉你：为了生成图像，选择从噪声开始其实非常自然。打个比方，假设你是一位雕塑家，也就是做雕塑的人。如果你想做一件雕塑，通常会从一块石头开始。

### [1:10:57](https://www.youtube.com/watch?v=Q86qzJ1K1Ss&t=4257s) · b000130

**English**

But then rocks are different from one another. They always have things that are unique to them. And still, you would focus on what to remove in order to obtain the end sculpture. So you can think of the rock as being your noise, and your end result as being your target data distribution. So I just want to have this quote by Michelangelo.

**中文**

但石头彼此不同，总有各自独特的地方。即便如此，你关注的仍然是，要去掉哪些部分才能得到最终的雕塑。所以，你可以把石头看作噪声，把最终结果看作目标数据分布。我想引用一下 Michelangelo 的这段话。

### [1:11:29](https://www.youtube.com/watch?v=Q86qzJ1K1Ss&t=4289s) · b000131

**English**

So the sculpture is already complete within the marble block. Before I start my work, it is already there. I just have to chisel away the superfluous material. The reason why I'm reading that is you can have a nice analogy between what Michelangelo said and the process of de-noising the noise to get an image. So this is all just motivating how image generation is done. So you start from noise, and you want to generate an image.

**中文**

雕塑早已完整地存在于大理石块之中。在我开始工作之前，它就已经在那里了。我只需要凿掉多余的材料。我读这段话，是因为 Michelangelo 所说的内容，与通过去噪（de-noising）得到图像的过程之间，有一个很贴切的类比。这些都是为了说明图像生成的思路：从噪声开始，然后希望生成一张图像。

### [1:12:03](https://www.youtube.com/watch?v=Q86qzJ1K1Ss&t=4323s) · b000132

**English**

So the way you do that for diffusion is to learn some transformation that would allow you to go from noise to image.

**中文**

在 diffusion 中，实现这一点的方法就是学习某种变换，让你能从噪声得到图像。

### [1:12:16](https://www.youtube.com/watch?v=Q86qzJ1K1Ss&t=4336s) · b000133

**English**

So you have two steps. I mean, you have more than two steps, but we have these two main steps for diffusion models where you first want to start from clean images. And you add noise gradually until you obtain some very noisy image. And then from that, what diffusion models try to do is to predict the noise to remove in order to obtain the image.

**中文**

所以，有两个步骤。我是说，实际不止两个步骤，但对于扩散模型（diffusion models），有这两个主要步骤：首先从干净的图像开始，逐渐添加噪声，直到得到噪声很重的图像。然后，diffusion models 尝试做的就是预测要移除的噪声，从而得到图像。

### [1:12:51](https://www.youtube.com/watch?v=Q86qzJ1K1Ss&t=4371s) · b000134

**English**

So it's a little bit like you're the sculpture person. And you have your rock. You just want to learn what pieces of rock you need to remove in order to obtain your final piece of art. So this is what diffusion is. So it works pretty well because noise, as I mentioned, is typically something that people draw from a Gaussian distribution. Gaussian distributions are mathematically very well defined, have a lot of nice properties.

**中文**

这有点像你是那个做雕塑的人，手里有一块石头。你想学会需要去掉石头的哪些部分，才能得到最终的艺术品。这就是 diffusion。它效果很好，因为正如我提到的，噪声通常是从 Gaussian distribution 中采样得到的。Gaussian distributions 在数学上有非常明确的定义，也有很多很好的性质。

### [1:13:25](https://www.youtube.com/watch?v=Q86qzJ1K1Ss&t=4405s) · b000135

**English**

So that's why they work so well. But now the question is, how would you adapt this to the text world. Because in the text world, as you know, we're talking about tokens. Tokens are discrete. So there's not this concept adding noise. You cannot have that. So what people have tried to do was to find a text equivalent that would make sense.

**中文**

所以它们才如此有效。但现在的问题是，如何把它用于文本领域？因为你们知道，在文本领域，我们讨论的是 token。token 是离散的，所以这里没有添加噪声这个概念，不能这样做。因此，大家尝试寻找一种在文本中合理的对应形式。

### [1:13:56](https://www.youtube.com/watch?v=Q86qzJ1K1Ss&t=4436s) · b000136

**English**

And this is what the current research points to which is that noise is to images what the mask token is to text.

**中文**

而当前研究指向的就是：噪声之于图像，就如掩码词元（mask token）之于文本。

### [1:14:11](https://www.youtube.com/watch?v=Q86qzJ1K1Ss&t=4451s) · b000137

**English**

So mask is just a way for us to just not have the information coming from one part of the sequence. And I just want to go through the revised 2-step process that we saw here for text. So here, for the forward process, instead of noising your input, you would just have more and more inputs that would be masked.

**中文**

所以，掩码（mask）只是让我们无法获得序列某一部分信息的一种方式。我想讲一下，把这里看到的两步过程调整到文本上之后会是什么样。对于正向过程（forward process），你不是给输入加噪声，而是让越来越多的输入被 mask。

### [1:14:44](https://www.youtube.com/watch?v=Q86qzJ1K1Ss&t=4484s) · b000138

**English**

So that's the full process. And at the end, you would just obtain a sequence full of masked tokens. So what you want to do is to learn some model that allows you to unmask these masked tokens in a way that reconstructs the original sentence. So there's some math that goes into it. Obviously, in a few minutes, we will not have time to go into that.

**中文**

这就是完整的过程。最后，你会得到一个全是被掩码 token 的序列。因此，你要做的是学习某个模型，让它能够解除这些 token 的掩码，从而重建原来的句子。这里涉及一些数学。显然，几分钟内我们没有时间深入讲解。

### [1:15:15](https://www.youtube.com/watch?v=Q86qzJ1K1Ss&t=4515s) · b000139

**English**

But I just want to emphasize on the key idea, which is you want to do diffusion, but in a way that makes sense for text inputs. And the way it would make sense is to consider the noise for images as being mask tokens for text input.

**中文**

不过我想强调核心思路：你希望做 diffusion，但要采用适合文本输入的方式。而这种合理的方式，就是把图像中的噪声对应为文本输入中的 mask token。

### [1:15:41](https://www.youtube.com/watch?v=Q86qzJ1K1Ss&t=4541s) · b000140

**English**

Cool. And so with that in mind, you have a bunch of models that are being released these days which are called masked diffusion models, MDM. So whenever you see MDM, now you know what kind of model we're talking about. So notations are still not very well defined. So it may change in the future. But one other term you will see out there is also DLLM, diffusion based LLM.

**中文**

好。有了这个认识，最近发布了不少模型，称为掩码扩散模型（masked diffusion models，MDM）。所以，以后看到 MDM，你就知道我们说的是哪类模型。目前这些记号还没有非常明确的定义，将来可能会变。不过，你还会看到另一个术语 DLLM，也就是基于扩散的大语言模型（diffusion based LLM）。

### [1:16:18](https://www.youtube.com/watch?v=Q86qzJ1K1Ss&t=4578s) · b000141

**English**

And this is what it's doing. So instead of predicting a token in an autoregressive fashion one at a time, what it does is that at inference time, it goes from a completely masked input sequence. And it tries to predict what tokens were behind these mask tokens. So of course, in a real life setting, you would have some prompts here.

**中文**

这就是它的做法。它不再以自回归方式一次预测一个 token，而是在推理时从一个完全被 mask 的输入序列开始，尝试预测这些 mask token 背后原本是什么 token。当然，在实际应用中，这里会有一些提示词（prompts）。

### [1:16:49](https://www.youtube.com/watch?v=Q86qzJ1K1Ss&t=4609s) · b000142

**English**

You would have some prompts. So of course, in order to predict these answer, you would have some conditioning. So you would tell your model, OK, given this prompts you're going to start with all these mask tokens. Just try to predict what the answer is. So in case you're having trouble with the intuition--so I also had trouble in the beginning. Why would it make sense for texts to be solved in a diffusion manner.

**中文**

你会有一些 prompts。因此，为了预测这些答案，当然会有一些条件信息（conditioning）。你会告诉模型，好，给定这些 prompts，你从所有这些 mask token 开始，试着预测答案是什么。如果你觉得这个直觉不太好理解——我一开始也觉得难理解——为什么用 diffusion 的方式处理文本会是合理的？

### [1:17:20](https://www.youtube.com/watch?v=Q86qzJ1K1Ss&t=4640s) · b000143

**English**

Because typically, when you write, you write one word at a time. So one helpful way to think about this is let's suppose you want to write a speech. So you would not directly write your speech in a linear way. You would first have a rough plan. You say, OK, I'm going to talk about this in the first place, second, third. You have some kind of drafts. And then you try to refine what is in each of these sections.

**中文**

因为通常写作时，你是一个词一个词地写。有一种有助于理解的方式：假设你想写一篇演讲稿。你不会直接从头到尾线性地写下来，而是先有个粗略计划。你会说，好，我首先讲这个，其次讲那个，然后讲第三点。你会有某种草稿，然后再尝试细化各个部分的内容。

### [1:17:53](https://www.youtube.com/watch?v=Q86qzJ1K1Ss&t=4673s) · b000144

**English**

So you can think of diffusion as kind of working like this. So it tries to have a coarse to find refinement of the outputs so it can predict things that are after a certain token that has not been predicted. But you can think of this as being something that goes from a very drafty version to a very refined version. So that's what I think about this process.

**中文**

你可以把 diffusion 想象成类似这样的工作方式。它尝试对输出进行 coarse to find 的细化 \[字幕疑误，可能指 coarse-to-fine，即由粗到细\]，因此，即使某个 token 还没有被预测出来，它也可以预测那个 token 之后的内容。你可以把它看作一个从非常粗糙的草稿版本，逐步变成非常精细版本的过程。这就是我对这个过程的理解。

### [1:18:24](https://www.youtube.com/watch?v=Q86qzJ1K1Ss&t=4704s) · b000145

**English**

Hopefully, that's helpful. And the key advantage here is that the decoding is now done in much fewer forward passes, because previously you had to do as many forward passes as there are tokens to predict. But here for diffusion, you only need to do as many passes as there are steps in your diffusion process, and the number of steps is something you can fix.

**中文**

希望这有帮助。这里的关键优势是，现在解码（decoding）所需的前向传播（forward passes）次数少得多，因为以前有多少个 token 要预测，就得做多少次 forward passes。而在 diffusion 中，你只需要做与 diffusion 过程步数一样多的 forward passes，而这个步数是可以固定的。

### [1:18:57](https://www.youtube.com/watch?v=Q86qzJ1K1Ss&t=4737s) · b000146

**English**

So the higher the step, the more high quality your output is, but it's typically much lower than the length of your output. So that is the core reason why this model is so much faster than the autoregressive one. And of course, we don't have that much time. But in case you're curious, in case you're interested, after the final, once you're completely freed in terms of things to think of, just put some references that could be helpful.

**中文**

所以，步数越多，输出质量越高，但步数通常远小于输出长度。这就是这种模型比自回归模型快得多的核心原因。当然，我们时间不多。不过，如果你们好奇、感兴趣，期末考试结束后，等你们完全不用再操心那些事情时，我放了一些可能有帮助的参考资料。

### [1:19:36](https://www.youtube.com/watch?v=Q86qzJ1K1Ss&t=4776s) · b000147

**English**

There's a paper that came out earlier this year called LLaDA, large language diffusion model with masking. Actually, I don't remember the full acronym. But it is actually going through the math and why the thing that I just mentioned works. And then there's a bunch of other papers that would also be helpful. So the links are at the bottom of the slide in case you're interested. And I just want to go through two last things before giving it to Shervine.

**中文**

今年早些时候有一篇论文，叫 LLaDA，带掩码的大语言扩散模型（large language diffusion model with masking）。其实我不记得这个缩写的完整展开了。不过，它确实详细介绍了其中的数学，以及我刚才说的做法为什么有效。还有一些其他论文也会有帮助。如果感兴趣，链接就在幻灯片底部。在交给 Shervine 之前，我还想讲最后两件事。

### [1:20:12](https://www.youtube.com/watch?v=Q86qzJ1K1Ss&t=4812s) · b000148

**English**

So first on the advantages of this new paradigm. So the first one is the speed. So as we mentioned, it's going to be much faster than traditional autoregressive models, especially for outputs that are longer. And so some benchmarks, they even say that it's something along the lines of 10x faster. So for cases like coding, it can be very powerful because you may have to do several model calls.

**中文**

首先是这种新范式的优势。第一个是速度。正如我们所说，它会比传统自回归模型快得多，尤其是输出较长的时候。一些基准测试（benchmarks）甚至称速度大约快了 10 倍。所以，对于编程这样的场景，它可能非常有用，因为你可能需要调用模型多次。

### [1:20:48](https://www.youtube.com/watch?v=Q86qzJ1K1Ss&t=4848s) · b000149

**English**

And you as a user, you're just waiting for that code to happen. And just having a lower latency makes a lot of difference. The other thing is that the nature of this approach is actually considering the text as a whole in order to make the predictions. And so there is a category of coding tasks that are called fill in the middle, which is about trying to figure out-- you have a bunch of codes, and you want to know what's missing in the middle.

**中文**

而作为用户，你就在等代码生成。更低的延迟（latency）会带来很大区别。另一个方面是，这种方法本质上会把文本作为一个整体来考虑，然后进行预测。有一类编程任务叫中间补全（fill in the middle），也就是试着弄清楚——你有一段代码，想知道中间缺了什么。

### [1:21:28](https://www.youtube.com/watch?v=Q86qzJ1K1Ss&t=4888s) · b000150

**English**

And so fill in the middle. And diffusion models are typically better formulated for these kinds of tasks because they can consider, I guess, input from multiple directions. And that's why this approach can be probably something that can be useful for some applications. So in terms of the current work, so these models, they look great. What I mentioned to you looks great. But the performance was not on par with the current frontier models, at least for some time.

**中文**

这就是 fill in the middle。而 diffusion models 通常在形式上更适合这类任务，因为我想，它们可以考虑来自多个方向的输入。因此，这种方法可能对某些应用有用。至于目前的工作，这些模型看起来很好，我向你们介绍的内容看起来也很好。但至少有一段时间，它们的性能还没有达到当前前沿模型（frontier models）的水平。

### [1:22:06](https://www.youtube.com/watch?v=Q86qzJ1K1Ss&t=4926s) · b000151

**English**

But it's something that may change. So the papers that I mentioned, they are actually posting performance that is kind of catching up with the models that are autoregressive. So there is some promise in there. And then the other line of work is just to adapt all the techniques that people have come up with. Like for instance, reasoning chains, how do you adapt that for diffusion, and so on.

**中文**

但这种情况可能会改变。我提到的那些论文报告的性能，实际上正在逐渐追上自回归模型，所以这里有一些希望。另外一个研究方向，就是适配大家已经提出的各种技术。比如推理链（reasoning chains），如何把它适配到 diffusion 上，等等。

### [1:22:36](https://www.youtube.com/watch?v=Q86qzJ1K1Ss&t=4956s) · b000152

**English**

There are so many techniques that are intrinsically more better suited for autoregressive kinds of models that can be adapted for that. And that's what people are working on. So long story short, what we saw was that things we saw in this class could be used in other domains. For instance, we saw the vision transformer that was boring the transformer for vision related tasks.

**中文**

有很多技术本来更适合自回归这类模型，也可以适配到这里。这就是大家正在研究的内容。长话短说，我们看到，这门课讲过的东西可以用于其他领域。例如，我们看到了视觉 transformer（vision transformer），它把 transformer boring 到视觉相关任务中 \[字幕疑误，boring 可能指 borrowing，即借用\]。

### [1:23:12](https://www.youtube.com/watch?v=Q86qzJ1K1Ss&t=4992s) · b000153

**English**

But we also saw that things from other domains could also be used in the text world. And that's what we saw with diffusion LLMs. And so this is probably, of course, a subset of everything that's happening. And so with that, I think we're concluding our second item of our menu. And I'm going to just give it to Shervine.

**中文**

但我们也看到，其他领域的东西同样可以用于文本领域。这就是我们在 diffusion LLMs 中看到的。当然，这大概只是所有正在发生的事情中的一部分。到这里，我想我们就讲完了菜单上的第二项。接下来交给 Shervine。

### [1:23:42](https://www.youtube.com/watch?v=Q86qzJ1K1Ss&t=5022s) · b000154

**English**

Thank you, Afshine. And with that, welcome to the last part of the season finale of CME 295. And as Afshine mentioned, now is the time for some closing thoughts and see what we can get away from this class and the concepts that are neighboring to it. So first, Afshine went through the concept of diffusion and images. And we saw some similarities. We could draw with text.

**中文**

谢谢你，Afshine。欢迎来到 CME 295 季终篇的最后一部分。正如 Afshine 所说，现在该做一些结束前的思考，看看我们能从这门课以及与它相邻的概念中收获什么。首先，Afshine 讲解了 diffusion 和图像的概念，我们看到了一些可以与文本作类比的相似之处。

### [1:24:14](https://www.youtube.com/watch?v=Q86qzJ1K1Ss&t=5054s) · b000155

**English**

And now we're going to see what kinds of inspirations have both modalities taken from each other. And we're going to see that actually, a lot of things can be reused. So the first thing that I want to mention in terms of what has been reused is the architecture part. So Afshine mentioned these diffusion concept that was born in the field of images, but that was taken for text, and was able to yield a lower latency like higher speed ups, which is great when you're an user.

**中文**

现在我们要看看，这两种模态（modalities）相互借鉴了哪些灵感。我们会看到，实际上很多东西都可以复用。关于复用，我首先想讲的是架构（architecture）部分。Afshine 提到了 diffusion 这个诞生于图像领域的概念，它后来被用于文本，实现了更低延迟，也就是更高的速度提升。对用户来说，这很棒。

### [1:24:54](https://www.youtube.com/watch?v=Q86qzJ1K1Ss&t=5094s) · b000156

**English**

So this was one example of a win. And then on the other direction, traditionally, images have been dealing with convolutions mostly as model architecture type. But these papers saw that replacing convolutions with transformers was very good, even yielding better results. So all these latest diffusion-based papers in the field of images typically use transformers.

**中文**

这是一个成功的例子。另一个方向上，传统上图像领域的模型架构主要采用卷积（convolutions）。但这些论文发现，用 transformers 替换 convolutions 效果很好，甚至能得到更好的结果。因此，图像领域最新的这些基于 diffusion 的论文，通常都使用 transformers。

### [1:25:29](https://www.youtube.com/watch?v=Q86qzJ1K1Ss&t=5129s) · b000157

**English**

And here, I'm linking one of the papers that Afshine already briefly went through. But not only is it the architecture side that is the subject of pollination between these modalities, you could even think of other kinds of components like the input. And for this one, I want to mention the example of DeepSeek OCR. So I don't know if you've heard of this paper.

**中文**

这里我链接了 Afshine 已经简要介绍过的一篇论文。但这些模态之间相互借鉴的不只是架构，你还可以考虑其他组成部分，比如输入。说到这一点，我想提一下 DeepSeek OCR 这个例子。不知道你们有没有听过这篇论文。

### [1:25:59](https://www.youtube.com/watch?v=Q86qzJ1K1Ss&t=5159s) · b000158

**English**

It just came out very recently. And contrary to what the name suggests, so OCR stands for optical character recognition. And it's usually a field that tries to converts some scanned image into text. But actually, that paper doesn't boast some improvements on the OCR task itself. Rather, it showed that you could learn some function that reconstructs text tokens based on vision tokens.

**中文**

它是最近刚发表的。而且与名字给人的印象不同，OCR 指光学字符识别（optical character recognition），通常是一个尝试把扫描图像转换成文本的领域。但实际上，那篇论文并不是在宣称 OCR 任务本身有了什么提升。它展示的是，你可以学习某个函数，根据视觉 token 重建文本 token。

### [1:26:40](https://www.youtube.com/watch?v=Q86qzJ1K1Ss&t=5200s) · b000159

**English**

And not only on vision tokens. On very few vision tokens. So it showed that the representation power of patches of images as tokens was very strong. And you have some researchers that bring some rationale to it like Hey Tokenizers are not the best tool anyway. And the things in patches convey the meaning of texts already with the example of emojis and so on that you would otherwise need to represent with way more tokens in text.

**中文**

而且不只是根据视觉 token，而是根据非常少的视觉 token。它表明，把图像块（patches）作为 token，具有很强的表示能力（representation power）。一些研究人员也为此提出了某些解释，比如，嘿，分词器（Tokenizers）本来就不是最好的工具。patches 中的内容本身就已经传达了文本的含义，例如表情符号（emojis）等等，否则你用文本来表示，就需要多得多的 token。

### [1:27:17](https://www.youtube.com/watch?v=Q86qzJ1K1Ss&t=5237s) · b000160

**English**

And then another example I want to mention is even when you look inside the architectures, some of the tricks can be reused and adapted in each field. So here, I'm mentioning the example of rope, which Afshine mentioned in the recap that was used in texts to represent the relative position of tokens. And in the case of images or even multi-modal setting, where you have the presence of both text and image within the architecture, you're able to adapt that trick by reformulating it in 2D.

**中文**

我还想举另一个例子：即使深入到架构内部，有些技巧也能在各个领域中复用和适配。这里我举的是 rope \[字幕疑误，可能指 RoPE\]，Afshine 在回顾时提到过，它在文本中用于表示 token 的相对位置。而对于图像，甚至是多模态（multi-modal）场景，也就是架构中同时存在文本和图像的情况，你可以通过把这个技巧重新表述为二维（2D）形式来进行适配。

### [1:27:59](https://www.youtube.com/watch?v=Q86qzJ1K1Ss&t=5279s) · b000161

**English**

So here the figure shows how you can attribute rope positions in the two degrees, and how you could place text tokens such that the relative computation of position still makes sense.

**中文**

这里的图展示了，如何在两个维度上分配 rope 位置，以及如何放置文本 token，使位置的相对计算仍然合理。

### [1:28:17](https://www.youtube.com/watch?v=Q86qzJ1K1Ss&t=5297s) · b000162

**English**

And even beyond that, I would say that the ongoing research for transformers is very much alive and people are still figuring out all the details that we're working with today. And you see refinements all the time coming in terms of new papers. So it's something that is still developing. And you can look at it from multiple angles. One is each of these design decisions that we've had, they are still being iterated on.

**中文**

除此之外，我还想说，围绕 transformers 的研究仍然非常活跃，大家还在弄清楚我们今天所使用的这些细节。你会不断看到新论文带来改进。所以，这仍然是一个发展中的领域。你可以从多个角度看待它。其中一个角度是，我们做过的每一项设计决策，都还在不断迭代。

### [1:28:53](https://www.youtube.com/watch?v=Q86qzJ1K1Ss&t=5333s) · b000163

**English**

So I'm listing a few items here as an example. So one is the optimizer side. You might be familiar with the Adam optimizer and its update rule, which has been popular for quite some time. And it seems that state is being challenged with newer papers. So I referenced here the Kimi K2 paper that came out a few months ago that introduces a new kind of optimizer called Muon.

**中文**

我在这里列了几项作为例子。第一项是优化器（optimizer）。你可能熟悉 Adam optimizer 及其更新规则，它已经流行很长时间了。但新的论文似乎正在挑战这种局面。我在这里引用了几个月前发表的 Kimi K2 论文，它介绍了一种名为 Muon 的新型 optimizer。

### [1:29:25](https://www.youtube.com/watch?v=Q86qzJ1K1Ss&t=5365s) · b000164

**English**

And the latest version of that MuonClip seems to be a potential candidate for this optimizer to become the new standard. So this field, even as basic as it can be, is still developing. But it's not only the optimizer side. You also have the topic of normalization, where Afshine mentioned that the difference between the original transformer paper and what you see today in LLM papers, you don't have the same kind of normalization anymore.

**中文**

而它的最新版本 MuonClip，似乎有望成为推动这种 optimizer 成为新标准的候选方案。所以，这个领域即便看起来如此基础，仍然在发展。但不只是 optimizer。还有归一化（normalization）这个话题，Afshine 提到，最初的 transformer 论文与今天的 LLM 论文之间有一个区别：所用的 normalization 类型已经不一样了。

### [1:30:01](https://www.youtube.com/watch?v=Q86qzJ1K1Ss&t=5401s) · b000165

**English**

In the past, you had post norm. But now you have pre norm, which brings the normalization earlier on in the layer. But beyond that design choice of the location of normalization, you even have the type of normalization that changes. So the transformer paper used layer norm. But these days, you might see other kinds of normalization techniques like RMS norm which uses less parameters and others.

**中文**

以前用的是后置归一化（post norm），现在用的是前置归一化（pre norm），它把 normalization 放到层中更靠前的位置。但除了 normalization 位置这个设计选择，normalization 的类型本身也在变化。transformer 论文使用的是层归一化（layer norm），而如今你可能会看到其他 normalization 技术，比如参数更少的均方根归一化（RMS norm），以及其他方法。

### [1:30:36](https://www.youtube.com/watch?v=Q86qzJ1K1Ss&t=5436s) · b000166

**English**

So the theory behind it is not set just yet. So you have other kinds of parameters. I've seen mentioned the grouped query attention paper. And you see these days in LLM papers, not a fixed design. Rather every paper adopts their own technique. Sometimes you see one kind of attention used as a given layer, but then it switches, and different papers take different design decisions.

**中文**

所以，它背后的理论还没有定下来。还有其他类型的参数。我看到有人提到了分组查询注意力（grouped query attention）那篇论文。而如今在 LLM 论文中，你看到的并不是固定的设计，每篇论文都会采用自己的技术。有时你会看到某一层使用一种注意力（attention），但随后又换成另一种，不同论文会做出不同的设计决策。

### [1:31:10](https://www.youtube.com/watch?v=Q86qzJ1K1Ss&t=5470s) · b000167

**English**

So it's not set in stone. Then you also have activation functions. So traditionally, in deep learning, a lot of emphasis was put on ReLU, which is a very simple and used worked very well. But in the world of LLMs, the shift was towards ReLU like activation functions, but not exactly ReLU. So you had a Gaussian error, linear units you had other kinds.

**中文**

所以，这并非一成不变。还有激活函数（activation functions）。传统上，深度学习非常重视修正线性单元（ReLU），它非常简单，而且用起来效果很好。但在 LLM 领域，趋势转向了类似 ReLU、但又不完全是 ReLU 的 activation functions。比如高斯误差线性单元（Gaussian error linear units），还有其他类型。

### [1:31:42](https://www.youtube.com/watch?v=Q86qzJ1K1Ss&t=5502s) · b000168

**English**

And the research there is still ongoing. So you still see new activation functions coming in now and then. And then you have also whether to take the design option of considering the LLM as an MOE or not. And even the number of layers of your LLM and other hyperparameters like number of heads. Size of the number of units in the FFN, all of that is still up for debate in terms of design decisions.

**中文**

这方面的研究仍在继续，所以你仍会不时看到新的 activation functions 出现。此外，你还需要选择是否将 LLM 设计为混合专家模型（MOE）。甚至包括 LLM 的层数，以及其他超参数（hyperparameters），比如注意力头的数量、前馈网络（FFN）中单元数量的大小，所有这些设计决策都仍有讨论空间。

### [1:32:16](https://www.youtube.com/watch?v=Q86qzJ1K1Ss&t=5536s) · b000169

**English**

So it's not fixed. And then another area of research I want to mention is the data part, which is crucial. So the first LLMs, they enjoyed a relatively clean state of things because you could scrape the internet and hope for a lot of data that was for sure human generated. So you could learn these patterns from, quote unquote, a high quality source, even though it's not in high quality format when you look at typical internet data, but it was still generated by human.

**中文**

所以，这些都没有固定下来。我还想提到另一个至关重要的研究领域，就是数据。最初的 LLM 处在一个相对干净的环境中，因为你可以抓取互联网，并且有望获得大量确定由人类生成的数据。因此，你可以从一个所谓的“高质量”来源中学习这些模式。虽然看典型的互联网数据，它的格式并不算高质量，但它终究是由人类生成的。

### [1:32:57](https://www.youtube.com/watch?v=Q86qzJ1K1Ss&t=5577s) · b000170

**English**

So these days, the state has changed. You type anything you want in your favorite search browser. Chances are the first results are 80% LLM generated. So are we doomed? Maybe not, because actually you see the development more and more work in data curation. So in the past, you would just scrape the whole internet and train next token prediction on it. But now, you have more and more of this work of curating data sets of interest.

**中文**

如今，情况变了。你在最喜欢的搜索浏览器里输入任何想查的内容，最前面的结果很可能有 80% 是 LLM 生成的。那我们是不是没救了？也许不是，因为你确实可以看到，数据整理（data curation）方面的工作越来越多。以前，你只需抓取整个互联网，然后在这些数据上训练下一个 token 预测（next token prediction）。现在，围绕特定需求整理数据集的工作越来越多。

### [1:33:29](https://www.youtube.com/watch?v=Q86qzJ1K1Ss&t=5609s) · b000171

**English**

And you have companies that work on it. And you have the emergence of newer fine tuning modes. So in the past, you had pre-training and then fine tuning. Now you have pre-training, mid training, and fine tuning. And the mid training part trains still on a large corpus of data, but higher quality. So people are finding ways around it. And I would say the picture is not all grim, but it's just that we need to do more work in order to have meaningful data at hand.

**中文**

有公司专门做这件事，也出现了更新的微调（fine tuning）模式。以前是预训练（pre-training），然后 fine tuning。现在则是 pre-training、中期训练（mid training），再到 fine tuning。mid training 仍然在大规模数据语料上训练，但数据质量更高。所以，大家正在寻找应对办法。我想说，前景并非一片黯淡，只是为了获得有意义的数据，我们需要付出更多工作。

### [1:34:05](https://www.youtube.com/watch?v=Q86qzJ1K1Ss&t=5645s) · b000172

**English**

And the paper that is linked at the bottom of the slide is dealing with the phenomenon of what if you were training on LLM generated data and it's talking about a concept called model collapse. And it says that LLM generated text is typically less diverse. So the data distribution that you would see at training time changes and it leads to less meaningful learning at training time, which is why it's typically bad.

**中文**

幻灯片底部链接的论文讨论了这样一种现象：如果用 LLM 生成的数据训练，会怎样？它讨论了一个叫模型崩溃（model collapse）的概念。论文指出，LLM 生成的文本通常多样性较低，所以训练时看到的数据分布会发生变化，导致训练中的学习更缺乏意义，这就是这种做法通常不好的原因。

### [1:34:39](https://www.youtube.com/watch?v=Q86qzJ1K1Ss&t=5679s) · b000173

**English**

And it motivates the need for more work on the data part. OK, nice. And then even taking a step back on the very architecture we've been using all along. Is it the best one? it's not clear. So that itself is an area of research. And future breakthroughs might come from redesigning this architecture.

**中文**

这也说明，有必要在数据方面投入更多工作。好。再退一步，看看我们一直在使用的架构本身：它是最好的架构吗？目前还不清楚。所以，这本身也是一个研究领域。未来的突破可能来自对这个架构的重新设计。

### [1:35:11](https://www.youtube.com/watch?v=Q86qzJ1K1Ss&t=5711s) · b000174

**English**

So in the past few years, a lot of the research that we have seen has been on improving benchmarks even more each time. So you have a set of benchmarks. Everyone tries to get the best results. So it's a natural trend because you want to have more and more powerful models that fulfill all your use cases. But let's say we reach a point where all the use cases we care about are solved.

**中文**

过去几年，我们看到的大量研究都在不断进一步提高 benchmark 成绩。你有一组 benchmarks，每个人都在努力取得最好的结果。这是一个自然的趋势，因为你希望模型越来越强，能满足所有使用场景。但假设我们到达了这样一个阶段：所有我们关心的使用场景都已经解决了。

### [1:35:42](https://www.youtube.com/watch?v=Q86qzJ1K1Ss&t=5742s) · b000175

**English**

Then what? So I think we're going to see the emergence of these second border of the Pareto frontier, where we care most about making predictions from LLM cost effective and still very high quality. So we see this emergence of smaller and smaller LLMs. I think it has been dubbed small language models, SLM, in the literature.

**中文**

然后呢？我想，我们会看到帕累托前沿（Pareto frontier）的第二个边界逐渐显现，在那里，我们最关心的是让 LLM 的预测具有成本效益，同时仍保持很高的质量。所以，我们看到越来越小的 LLM 出现。我想，文献中已经把它们称为小语言模型（small language models，SLM）。

### [1:36:16](https://www.youtube.com/watch?v=Q86qzJ1K1Ss&t=5776s) · b000176

**English**

And typically, you hear sometimes LLM providers say that they lose money even on the highest tier plans. So I think it reflects the fact that you need to be smarter in the compute that you spend for serving LLM queries at test time. And I think this will motivate more and more this line of research in the coming years. And then there is another area that we've not touched on at all in this class, which is the hardware part.

**中文**

有时你会听到 LLM 提供商说，即使是最高档的套餐，他们也在亏钱。我想，这反映出，在测试时为 LLM 查询提供服务，你需要更聪明地分配计算资源。我认为，这将在未来几年越来越多地推动这一研究方向。另外，还有一个我们这门课完全没有涉及的领域，就是硬件。

### [1:36:51](https://www.youtube.com/watch?v=Q86qzJ1K1Ss&t=5811s) · b000177

**English**

So typically, the kind of device that you use to train these LLMs are GPUs, which are great at one thing--matrix multiply. But the thing is, we've kept these kinds of architectures to train our models, even though the architecture doesn't only need matrix multiplies as a foundational atomic unit of compute, the self-attention world and the transformer world has all these special needs.

**中文**

通常，用来训练这些 LLM 的设备是图形处理器（GPUs），它们特别擅长一件事——矩阵乘法（matrix multiply）。但问题是，我们一直保留着这类架构来训练模型，尽管模型架构所需的基础原子计算单元并不只有矩阵乘法，自注意力（self-attention）和 transformer 还有各种特殊需求。

### [1:37:28](https://www.youtube.com/watch?v=Q86qzJ1K1Ss&t=5848s) · b000178

**English**

The qk transpose part we saw was actually very expensive, which has motivated papers such as flash attention to, as I've seen mentioned, actually forego of some of the data for the sake of not doing too much movements on the memory side, even if it meant recomputing the same things afterwards. And then a lot of work has been on optimizing where the flow of memory within the GPU resides.

**中文**

我们看到的 qk transpose，也就是 qk 转置部分，实际上开销很大，这促成了 flash attention \[字幕疑误，可能指 FlashAttention\] 这样的论文。正如我看到有人提到的，它们实际上会舍弃部分数据，以免在内存侧进行过多的数据搬移，即便这意味着之后要重新计算相同的内容。还有很多工作是在优化 GPU 内部内存数据流所处的位置。

### [1:38:00](https://www.youtube.com/watch?v=Q86qzJ1K1Ss&t=5880s) · b000179

**English**

And this shows that maybe you need a more optimized hardware architecture in order to solve these use cases. So there is a recent paper that came out that actually encodes all of these operations as part of the hardware. So in the past, the core operation that the GPU was great at is matrix multiply.

**中文**

这表明，或许你需要一种优化得更好的硬件架构，才能解决这些使用场景。最近有一篇论文，实际上把所有这些运算都编码成了硬件的一部分。过去，GPU 最擅长的核心运算是矩阵乘法。

### [1:38:32](https://www.youtube.com/watch?v=Q86qzJ1K1Ss&t=5912s) · b000180

**English**

And based on it, you try to build all of the input output that you want. But here this paper that came out, I think, in September shows a proof of concept where you can do all of these computations as a side effect of implementing input and outputs with analog signals. So you have all of these computations that are embedded as part of the hardware. And based on pulses as input that simulates your array values, these hardware architectures have some physical properties, you could think of a Kirchhoff law in the field of, I think, intensity.

**中文**

你在此基础上，尝试构建所需的所有输入和输出。但这里这篇论文，我记得是 9 月发表的，展示了一种概念验证（proof of concept）：通过模拟信号（analog signals）实现输入和输出，就能顺带完成所有这些计算。也就是说，这些计算都被嵌入为硬件的一部分。输入是模拟数组数值的脉冲，而这些硬件架构具有某些物理性质，你可以想到 Kirchhoff 定律，我想是在电流强度方面。

### [1:39:20](https://www.youtube.com/watch?v=Q86qzJ1K1Ss&t=5960s) · b000181

**English**

You can add them up. And it uses properties like this to have what you need as inputs and just read out the results as output. So when the paper simulated this kind of architecture, they observed, without too much surprise quite a bit of improvement both on the latency and energy saving parts both explained because you don't need to do the computations yourself.

**中文**

你可以把它们加起来。它利用这类性质，把所需的内容作为输入，然后直接读取输出结果。因此，论文在模拟这类架构时，观察到延迟和节能方面都有相当大的改善，这并不太令人意外。两方面的原因都在于，你不需要自己执行这些计算。

### [1:39:54](https://www.youtube.com/watch?v=Q86qzJ1K1Ss&t=5994s) · b000182

**English**

You just get them as a side effect of your hardware.

**中文**

它们会作为硬件运作的附带结果直接产生。

### [1:40:01](https://www.youtube.com/watch?v=Q86qzJ1K1Ss&t=6001s) · b000183

**English**

Now I want to take a step back and look at our users, at our use cases of LLMs today and what could lie ahead, what could be the most exciting for you. So today, we've seen that in just a few years, I think it has become quite important to know how to use them if you want to speed up everything you do in your daily life. So a few lectures ago, we talked about the coding case where do you have all these AI systems coding tools that enable you to turn into code, some natural language prompts.

**中文**

现在我想退一步，看看我们的用户，看看如今 LLM 的使用场景，以及未来可能出现什么、什么最可能让你们兴奋。今天我们已经看到，仅仅几年间，我想，如果你希望加快日常生活中所做的一切，知道如何使用它们已经变得相当重要。几节课前，我们讨论了编程场景，那些 AI 系统、编程工具可以让你把一些自然语言提示转化为代码。

### [1:40:43](https://www.youtube.com/watch?v=Q86qzJ1K1Ss&t=6043s) · b000184

**English**

So you just ask for something and it will help you do that task with a so-called agent mode. And this is just something that you would do as an engineer. But even beyond that, other use cases are deeply impacted by it because you have a lot of problems that today can be turned into a text to query or text to code problem. So you could think of even the visualization world, you could--So for example, there was a launch from Google recently that showed that you could generate visualizations on the fly based on some principles.

**中文**

你只要提出需求，它就会用所谓的智能体模式（agent mode）帮你完成任务。这是你作为工程师会做的事情。但除此之外，其他使用场景也受到深刻影响，因为如今很多问题都可以转化为文本转查询（text to query）或文本转代码（text to code）的问题。甚至可以想想可视化领域，你可以——例如，Google 最近的一次发布就展示了，你可以根据一些原理即时生成可视化内容。

### [1:41:26](https://www.youtube.com/watch?v=Q86qzJ1K1Ss&t=6086s) · b000185

**English**

And this is already changing quite a bit the picture of what you can do today. Something else that I think is used by most people actually today when using these chatbots is like being a general assistant, so you ask about common facts and all the facts that it has learned at training time becomes useful. It browses the web more efficiently than you and converts into natural language the things that you care about.

**中文**

这已经在很大程度上改变了如今你能做什么的局面。另一个我认为现在大多数人使用这些聊天机器人时都会用到的功能，是把它当作通用助手。你询问一些常见事实，它在训练时学到的所有事实就派上用场了。它比你更高效地浏览网页，并把你关心的内容转化为自然语言。

### [1:41:59](https://www.youtube.com/watch?v=Q86qzJ1K1Ss&t=6119s) · b000186

**English**

But then there are also other domains that were impacted by it. So you could think creativity where a lot of jobs such as marketing or others rely on getting something out of a blank page. And usually, if you start from a draft, it's much easier to get something done rather than just thinking of it from scratch. So it's used as a net here. And also, one use case that I've seen in class that I think is great that some of you do--sometimes I talk about something, or I've seen talks about something, and I see people typing on ChatGPT related concepts.

**中文**

还有其他领域也受到了影响。比如创意领域，营销等许多工作都需要从一张白纸开始创造内容。通常，如果从一份草稿开始，完成事情会比完全从零构思容易得多。所以，它在这里就像一张网。还有一种使用场景，是我在课堂上看到你们一些人在做的，我觉得很棒——有时我讲到某个内容，或者我看过讲座讲到某个内容，就会看到有人在 ChatGPT 中输入相关概念。

### [1:42:40](https://www.youtube.com/watch?v=Q86qzJ1K1Ss&t=6160s) · b000187

**English**

And I think it's very smart to do that because brainstorming the concepts that you learn is great for actually grasping the concepts of interest. And getting that early feedback loop is very useful for learning. So I have a lot of hopes regarding how great of a time it is for you to learn as opposed to maybe having a nice time maybe 10 years ago. So yeah, keep doing that. And I think it will be a growing use case.

**中文**

我觉得这么做很聪明，因为围绕学到的概念进行头脑风暴（brainstorming），非常有助于真正理解你关心的概念。尽早获得这样的反馈循环（feedback loop）对学习非常有用。因此，相比可能 10 年前也算不错的学习时光，我对你们如今所处的这个学习时代寄予很大希望。所以，继续这样做吧。我想，这会成为一个不断增长的使用场景。

### [1:43:11](https://www.youtube.com/watch?v=Q86qzJ1K1Ss&t=6191s) · b000188

**English**

So looking forward. So I said, tomorrow on the slide, but actually two days ago, there was a launch that went in the direction of what I was thinking about, which is all the agentic things that we talked about, there are still very much confined into people that about the field. Everyday people, they wouldn't typically use, quote unquote, agentic workflows.

**中文**

再向前看。我在幻灯片上写了“明天”，但实际上，两天前就有一次发布，朝着我设想的方向迈进了。也就是说，我们讨论过的所有这些智能体相关（agentic）的东西，目前仍然很大程度上局限于了解这个领域的人。普通人通常不会使用所谓的智能体工作流（agentic workflows）。

### [1:43:43](https://www.youtube.com/watch?v=Q86qzJ1K1Ss&t=6223s) · b000189

**English**

So I think one field of development that we will see more and more is all these use cases being democratized. So people can now create things that can be useful to them with easier mediums, just natural language, no need to code moving forward to later. So all these AI assisted coding that I was mentioning, you could think of it as helping you browse the internet in a very natural fashion.

**中文**

所以，我想，我们会越来越多地看到一个发展方向：让所有这些使用场景普及到大众。这样，人们就能通过更简单的媒介，只用自然语言，创造对自己有用的东西，以后不再需要编程。所以，我刚才提到的所有这些 AI 辅助编程，你可以把它理解为帮助你以非常自然的方式浏览互联网。

### [1:44:14](https://www.youtube.com/watch?v=Q86qzJ1K1Ss&t=6254s) · b000190

**English**

So it seems, right now, when you just execute tasks, you're way too microscopic in what you do. And this is typically what AI assistant could help you do. So there are recent product launches that reflect this growing interest, such as ChatGPT's Atlas. So I think it launched in October. I don't know if they released some public number on usage. I suspect it's still timid because you still have challenges when it comes to security.

**中文**

现在看来，当你执行任务时，所做的操作往往过于细碎。而这正是 AI 助手通常可以帮忙的地方。最近一些产品发布反映了这种日益增长的兴趣，比如 ChatGPT 的 Atlas。我记得它是 10 月发布的。不知道他们有没有公布使用量。我猜目前还比较有限，因为在安全方面仍然存在挑战。

### [1:44:47](https://www.youtube.com/watch?v=Q86qzJ1K1Ss&t=6287s) · b000191

**English**

Anyone could inject some bad prompt in there and maybe exfiltrate things from you. But I'm sure the community will come up with more ways to get around it. So in the past, you had HTTPS, for example, to say that the connection was secure. Maybe tomorrow, you'll have some certificate that will guarantee that a site website is safe for AI assistant browsing and looking even at a higher level, maybe just browsing on your desktop or your mobile phone at the LLM level.

**中文**

任何人都可能往里面注入恶意提示词（prompt），甚至把你的信息窃取出去。但我相信，社区会想出更多应对方法。过去，例如有 HTTPS 来表示连接是安全的。也许未来会有某种证书，保证一个网站适合 AI 助手安全浏览。再从更高层面看，也许只是由 LLM 层面来浏览你的桌面或手机。

### [1:45:24](https://www.youtube.com/watch?v=Q86qzJ1K1Ss&t=6324s) · b000192

**English**

At the OS level, might be something that the LLM can help. So when we talked about agents, we mentioned how non-reliable it could be because as you have more and more steps, the probability for a failure increases. And stabilizing predictions is something of interest. And even in the longer run, I think one test that we can have in mind as to how far we've come is whether the common use case of having a customer service that is served by AI is truly useful.

**中文**

在操作系统（OS）层面，也可能有 LLM 能帮忙的地方。我们讨论智能体（agents）时提过，它可能很不可靠，因为步骤越多，失败概率就越高。让预测稳定下来，是一个值得研究的问题。再看更长远一点，我想，可以用一个检验标准来衡量我们走了多远：由 AI 提供客户服务这个常见使用场景，是否真的有用。

### [1:46:02](https://www.youtube.com/watch?v=Q86qzJ1K1Ss&t=6362s) · b000193

**English**

So I don't about you, but every time I have a problem, and I'm on the phone, and I hear some AI assistant, maybe LLM powered robot, I'm kind of quick, quick, quick, I want a human, I don't want that. And I think it shows how hard this space is, the space of problems is because human has way more dimensions of value that an LLM could bring. So empathy, groundedness, there are some things that you and we perceive as things that make sense, even though they're not in our system prompts.

**中文**

我不知道你们怎样，但每次我遇到问题，打电话时听到某个 AI 助手，也许是 LLM 驱动的机器人，我就会想，快点，快点，快点，我要人工，我不想要这个。我想，这说明这个领域、这类问题有多难，因为人类能够提供的价值维度，远比 LLM 多。比如共情（empathy）、立足实际（groundedness），有些东西，你们和我们都觉得是合理的，即使它们并没有写在我们的系统提示词（system prompts）里。

### [1:46:36](https://www.youtube.com/watch?v=Q86qzJ1K1Ss&t=6396s) · b000194

**English**

So I think there are hard problems to solve there. And even moving forward, there are some key challenges that we have with the current architecture. So we saw during the class that you had to go through a training process that went to fix some weights. But these weights are not changing afterwards. And we use tricks such as RAG or tools to get around this issue.

**中文**

所以，我认为这里有一些难题需要解决。进一步看，当前架构也存在一些关键挑战。我们在课上看到，你需要经历一个训练过程，把某些权重（weights）确定下来。但这些 weights 之后就不再变化了。我们会用检索增强生成（RAG）或工具等技巧来绕过这个问题。

### [1:47:08](https://www.youtube.com/watch?v=Q86qzJ1K1Ss&t=6428s) · b000195

**English**

But could we think of a system that learns continuously? I think that is an open question. Then there is a topic of hallucinations which I put into quotation marks because I'm not sure if it's fair to say that the LLM hallucinates just because we've trained the LLM to predict the next token by nature, not map statements to facts. So hallucinating is, in some sense, a core design choice of these LLMs.

**中文**

但我们能否设想一个持续学习的系统？我认为这是一个开放问题。还有幻觉（hallucinations）这个话题，我给它加了引号，因为我不确定说 LLM 产生幻觉是否公平：毕竟我们训练 LLM，本质上是让它预测下一个 token，而不是把陈述映射到事实。所以，从某种意义上说，产生幻觉是这些 LLM 的一个核心设计选择。

### [1:47:40](https://www.youtube.com/watch?v=Q86qzJ1K1Ss&t=6460s) · b000196

**English**

Personalization, interpretability, safety the list goes on.

**中文**

个性化（personalization）、可解释性（interpretability）、安全性（safety），这样的清单还可以继续列下去。

### [1:47:46](https://www.youtube.com/watch?v=Q86qzJ1K1Ss&t=6466s) · b000197

**English**

Now I want to briefly cover how you can exercise this muscle of staying up to date from now. So you have archive that usually contains all these greatest and latest papers that you can take a look at. Of course, the venues like NeurIPS right now are great to highlight some papers. And then I highly encourage you, besides the papers, looking at the associated codebases that the authors provide.

**中文**

现在我想简要讲讲，从现在开始，你们可以如何锻炼持续跟进最新进展的能力。有 archive \[字幕疑误，可能指 arXiv\]，里面通常有这些最新、最好的论文，可以去看看。当然，像当前的 NeurIPS 这样的学术会议，也非常适合发现一些值得关注的论文。此外，除了论文，我强烈建议你们看看作者提供的相关代码库。

### [1:48:21](https://www.youtube.com/watch?v=Q86qzJ1K1Ss&t=6501s) · b000198

**English**

So right now, it's a commonplace to just provide the implementation of what you're proposing. And I think it's very insightful to learn the concepts. And there is a paper with code that existed in the past. And that has been replaced by HuggingFace trending papers, which I think is a good place to take a look at the latest methods. And then on the social network side, Twitter or X has a lot of the latest that is often discussed.

**中文**

现在，提供所提出方法的实现已经很常见了。我认为，这对学习概念很有启发。过去有一个 paper with code \[字幕疑误，可能指 Papers with Code\]，如今已经被 HuggingFace trending papers 取代了。我觉得那里很适合了解最新方法。社交网络方面，Twitter 或 X 上也经常讨论很多最新进展。

### [1:48:57](https://www.youtube.com/watch?v=Q86qzJ1K1Ss&t=6537s) · b000199

**English**

So you have a strong community there. And if you have an account on that social media, you have a lot of great people to follow to stay updated. But also, you have resources on YouTube, which highlight on Yannic Kilcher, which I think was the first YouTuber to cover the transformer paper back in 2017 in great detail. And I think some of these YouTubers, they're very good at talking through papers in great detail.

**中文**

那里有一个很强大的社区。如果你在那个社交媒体上有账号，可以关注很多优秀的人来保持了解最新动态。此外，YouTube 上也有资源。我想特别提一下 Yannic Kilcher，我认为他是第一个在 2017 年就非常详细地讲解 transformer 论文的 YouTuber。我觉得，其中一些 YouTuber 非常擅长详细讲解论文。

### [1:49:28](https://www.youtube.com/watch?v=Q86qzJ1K1Ss&t=6568s) · b000200

**English**

And another highlight is Andrej Karpathy, who was at Stanford about 10 years ago. And he's, I think, one of the best educators out there. So I highly recommend his videos. And you have company blogs that are also great. And this study guide that we associated with the class, so we've had it for this year. And what we'll try to do in the coming years is try to keep it updated at least on a yearly basis.

**中文**

另一个要特别提到的是 Andrej Karpathy，大约 10 年前他在 Stanford。我认为，他是最优秀的教育者之一。所以，我非常推荐他的视频。公司的博客也很不错。还有我们为这门课配套的学习指南，今年已经提供了。未来几年，我们会争取至少每年更新一次。

### [1:50:00](https://www.youtube.com/watch?v=Q86qzJ1K1Ss&t=6600s) · b000201

**English**

So you can consider this resource as maybe some companion. And we've got the chance to collaborate with experts around the world to make it available in other languages, in case you're interested. And taking a step back, just want to say that Afshine and I were very grateful to teach this class this quarter. Thank you so much for coming here on Friday evening, which is quite telling, because Friday evening is usually a time for fun, not for lectures.

**中文**

所以，你们可以把这个资源当作某种学习伙伴。我们也有机会与世界各地的专家合作，把它提供为其他语言版本，如果你们感兴趣的话。退一步说，我只想说，Afshine 和我非常感激能在这个季度教授这门课。非常感谢你们周五晚上来到这里，这很能说明问题，因为周五晚上通常是娱乐时间，而不是上课时间。

### [1:50:33](https://www.youtube.com/watch?v=Q86qzJ1K1Ss&t=6633s) · b000202

**English**

And also now, I think it's probably your last lecture of the whole quarter because next week is finals. So yeah, thank you for coming and for asking all these great questions. You were one of the reasons why this class was so great and interactive. Also, thank you to the folks who are watching online from home. I was one of you eight years ago. I would almost never go to class, always watching lectures from home, from a cozy place. I hope the lectures were entertaining and that you got something from it.

**中文**

而且我想，这可能是你们整个季度的最后一堂课，因为下周就是期末考试了。所以，谢谢你们来上课，也谢谢你们提出这么多很棒的问题。这门课如此精彩、互动如此丰富，你们是其中的原因之一。也感谢在家在线观看的朋友们。8 年前，我也是你们中的一员。我几乎从不去课堂，总是在家里、在一个舒适的地方看课程录像。希望这些课很有趣，也希望你们有所收获。

### [1:51:09](https://www.youtube.com/watch?v=Q86qzJ1K1Ss&t=6669s) · b000203

**English**

And I couldn't conclude without bringing our favorite Teddy bear one last time. Thanking you all for your attention and wishing you all the best. Thank you. \[APPLAUSE\]

**中文**

结束前，当然还要最后一次请出我们最喜欢的 Teddy bear。感谢大家的聆听，祝你们一切顺利。谢谢。\[掌声\]
