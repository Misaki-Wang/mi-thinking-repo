# Stanford CME295 Transformers &amp; LLMs \| Autumn 2025 \| Lecture 2 - Transformer-Based Models &amp; Tricks

_Bilingual transcript · 双语讲稿_

- Channel: Stanford Online
- Source: [YouTube](https://www.youtube.com/watch?v=yT84Y5zCnaA)
- Duration: 1:47:19
- Caption source: manual
- Status: complete
- Chinese translation: 217/217
- Translation provider: codex
- Generated: 2026-09-29T15:39:24+00:00

## Transcript · 讲稿

### [00:05](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=5s) · b000001

**English**

Cool. Hello everyone. Welcome to lecture 2 of CME 295. So before we start, I wanted to give you a heads up about two logistical things. So the first one is with Shervine, we reviewed the recording of lecture 1. And we couldn't help but notice that the audio was suboptimal. So what we're doing for this lecture is to have another setup.

**中文**

好。大家好。欢迎来到 CME 295 第 2 讲。开始之前，我想先提醒大家两件安排上的事情。第一件是，我和 Shervine 回看了第 1 讲的录像。我们实在没法忽视音频效果不太理想的问题。所以这次课我们会换一套设备配置。

### [00:35](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=35s) · b000002

**English**

But then one issue is my voice will not be propagated in the room. So I guess I have one question. Can everyone hear me very well, even from the back? OK, cool. Great. So that's point number 1. Point number 2 is about the final exam. So the final exam right now has a placeholder date for Wednesday, I think, December the 10th. But just a heads up that we're trying to see if there is a way to move that to earlier in the week.

**中文**

不过这样有一个问题，就是我的声音不会通过扩音设备传到教室各处。所以我想问一下。大家都能听清楚我说话吗，包括后面的同学？好的，很好。太好了。这是第 1 点。第 2 点是关于期末考试。目前期末考试暂定的日期是星期三，我记得是 12 月 10 日。不过先提醒大家，我们正在看看有没有办法把它移到那一周早一些的时候。

### [01:06](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=66s) · b000003

**English**

So we'll let when that's finalized. But for now, this is still TBD. But we'll make sure to let you know. Cool. So with that aside, let's go into today's topic. But before we do that, as always, what we will do is we'll just quickly recap what we saw in the previous episodes. So if you remember, lecture 1 was all about introducing the concept of self-attention.

**中文**

所以等确定下来，我们会……但目前这件事仍然待定（TBD）。不过我们一定会通知大家。好。先把这些放到一边，我们进入今天的主题。不过在这之前，和往常一样，我们先快速回顾一下前面几期讲过的内容。如果大家还记得，第 1 讲主要介绍了自注意力（self-attention）的概念。

### [01:38](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=98s) · b000004

**English**

And if you remember, what self-attention is that each token is attending to all other tokens in the sequence through this mechanism of attention. So you have these notations of queries, keys, and values. So here the idea is that the query is going to ask which other tokens are most similar to itself by comparing query and key.

**中文**

如果大家还记得，self-attention 就是每个词元（token）都通过注意力（attention）机制关注序列中所有其他 token。我们用到了查询（query）、键（key）和值（value）这些记号。这里的想法是，query 通过与 key 比较，来询问哪些其他 token 与自己最相似。

### [02:09](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=129s) · b000005

**English**

And then once that's done, basically we will be taking the associated value. So we saw that the self-attention mechanism can be expressed with this formula, so softmax of query times key transpose over square root of dk times v. So I hope this formula is familiar for you. So just know that this formula is highly optimized. These are big matrix multiplications, or hardware, is very capable of doing, it's very optimized in doing that.

**中文**

然后完成这一步以后，基本上我们就会取对应的 value。我们看到，self-attention 机制可以用这个公式表示，也就是 softmax(query × key 的转置 / √dk) × v。我希望大家对这个公式已经比较熟悉了。要知道，这个公式经过了高度优化。这些都是大型矩阵乘法，而硬件非常擅长做这些运算，针对这些运算的优化也非常充分。

### [02:48](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=168s) · b000006

**English**

And all of that to say that we also introduced the architecture of the transformer, which you can see on the right. So here, if you remember, the transformer is composed of two main components. So the encoder on the left side and the decoder on the right side. And the transformer was initially introduced in the context of machine translation. So you can think of the left side as processing the input text in the source language, say English.

**中文**

说这些是为了说明，我们还介绍了 transformer 的架构，大家可以在右边看到。如果大家还记得，transformer 由两个主要部分组成：左边的编码器（encoder）和右边的解码器（decoder）。transformer 最初是在机器翻译（machine translation）的背景下提出的。所以你可以把左边理解为处理源语言的输入文本，比如英语。

### [03:25](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=205s) · b000007

**English**

And the right side is responsible for decoding the translation in a target language, let's say in French. And this multi-head attention layer is where the self-attention mechanism happens. And I remember there was a lot of questions regarding-- it's called multi-head attention layer. So there are several heads. What does that correspond to?

**中文**

右边则负责解码出目标语言的译文，比如法语。而这个多头注意力（multi-head attention）层就是执行 self-attention 机制的地方。我记得当时有很多问题是关于——它叫 multi-head attention 层，所以里面有多个头（head）。这些 head 对应什么呢？

### [03:55](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=235s) · b000008

**English**

So in the transformer paper, which is the "Attention is All You Need" paper, you have this figure, which actually represents each of these heads. And you can think of each head as an opportunity for the model to learn one way of projecting the input into being a query, a key, or a value. So just being a bit more clear, so for instance, for the query and the key, so this is like each head.

**中文**

在 transformer 论文，也就是《Attention is All You Need》这篇论文里，有这样一幅图，它实际上表示的就是这些 head。你可以把每个 head 看成模型学习一种投影方式的机会，用这种方式把输入投影成 query、key 或 value。再说清楚一点，比如对于 query 和 key，这就相当于每一个 head。

### [04:29](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=269s) · b000009

**English**

So the number of these little boxes is basically the number of heads. And to better visualize and understand what this means, I also wanted to show I guess what is being shown in the paper, which is a way to interpret what each of these heads do. So we have this concept called attention map, which basically tries to represent the value of each of these query, dot product query.

**中文**

所以这些小方框的数量基本上就是 head 的数量。为了更直观地理解这是什么意思，我还想展示一下论文里展示的内容，也就是一种解释各个 head 在做什么的方式。我们有一个叫注意力图（attention map）的概念，它基本上试图表示每个 query 的值，点积 query 的值。

### [05:10](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=310s) · b000010

**English**

So in this example, what we're interested in is to see which other token is being most similar to token its. And so what we do is we take a look at the quantities, the query that is representing its, dot product, all other keys. And we look at what are the keys are leading to a high value of the dot product query times key.

**中文**

在这个例子中，我们关心的是，哪个其他 token 与 token its 最相似。所以我们要查看这些量：代表 its 的 query，与所有其他 key 做点积（dot product）。然后看看哪些 key 会让 query 乘以 key 的点积取得较高的值。

### [05:47](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=347s) · b000011

**English**

And when you do that, basically what you see or what the paper sees is you have these two words, so application and law, which are highlighted as being with the high-attention weight. So attention weight here being the dot product of the query its, and the key for each of these tokens. And I guess there is also a way to interpret those. And here you can see that the tokens that are being highlighted are law and application, which basically makes sense because the token its is referring to law.

**中文**

这样做之后，你看到的，或者说论文里观察到的，就是 application 和 law 这两个词被突出显示，因为它们具有较高的注意力权重（attention weight）。这里的 attention weight 指的是 its 的 query 与这些 token 各自的 key 的点积。我想也有一种解释这些结果的方式。这里你可以看到，被突出显示的 token 是 law 和 application，这基本上是合理的，因为 token its 指的是 law。

### [06:28](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=388s) · b000012

**English**

So basically, the model needs to learn how to associate these words with what happened before. And its is also referring to application, which is also another way of explaining why that is the case. And so here what the authors chose to do was to show these values as a function of these different heads. So for instance, on the left side, these are the intensity for heads, for let's say the first heads.

**中文**

所以，模型基本上需要学会如何把这些词与前面出现的内容联系起来。而 its 也指向 application，这也是解释为什么会出现这种情况的另一种方式。这里作者选择展示这些数值在不同 head 下的情况。例如，左边这些是 head 的强度，比如说第一个 head 的强度。

### [07:00](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=420s) · b000013

**English**

And then the second heads shows that the intensity is very high for law. So basically, long story short, these heads may learn, I guess, different ways of figuring out what words matters. Yeah.

**中文**

然后第二个 head 显示，law 的强度非常高。所以简单来说，我想这些 head 可能会学到不同的方式，来判断哪些词比较重要。嗯。

### [07:30](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=450s) · b000014

**English**

Great question. So the question is, when we're doing all these computations, are they going through different MLPs. The answer is that we're going to have different projection matrices for each of them.

**中文**

问得很好。问题是，我们进行所有这些计算时，它们是否会经过不同的多层感知机（MLPs）。答案是，我们会为它们分别设置不同的投影矩阵（projection matrices）。

### [07:48](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=468s) · b000015

**English**

So we had this detailed example that actually went through that where each head is going to have its own projection. And in parallel, you're going to have that computation that's going to happen. So each head is going to have one result here, that is then going to be concatenated and then projected once again when the output matrix. So yeah, long story short, it's highly parallelized.

**中文**

之前我们有一个详细例子，实际讲过这一过程，每个 head 都会有自己的投影。这些计算会并行进行。所以每个 head 都会在这里得到一个结果，然后将这些结果拼接（concatenate）起来，再通过输出矩阵进行一次投影。是的，简单来说，它的并行程度很高。

### [08:20](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=500s) · b000016

**English**

And it's basically just like projections. And here you have some matrix multiplication and softmax. Does that make sense? Cool. Any other questions on this?

**中文**

基本上就是一些投影。这里有一些矩阵乘法和 softmax。这样讲清楚了吗？好。关于这个还有其他问题吗？

### [08:38](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=518s) · b000017

**English**

Cool. So I guess this is just a way to illustrate the conversation we had for lecture 1. There was some questions about these attention heads, what they do. And I guess looking at the attention maps is one way of making sense of what they mean. Cool. With that, I highly recommend that you read the transformers paper, so "Attention is All You Need."

**中文**

好。我想这只是用来说明一下我们在第 1 讲中的讨论。当时有一些关于这些 attention head 以及它们作用的问题。我想，查看 attention map 是理解它们含义的一种方式。好。说到这里，我强烈建议大家读一下 transformers 论文，也就是《Attention is All You Need》。

### [09:09](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=549s) · b000018

**English**

So it's a very dense paper. It's just a few pages long. But I hope that what you've seen in lecture 1, you'll be able to digest the content in a way that will make sense to you. Cool. So with that, we're going to start the actual meat of what we're going to discuss today. So surprisingly, this transformer architecture, which was introduced in 2017, is actually an architecture that has still stayed relevant along the years.

**中文**

这篇论文的信息密度非常高，只有几页。但我希望借助第 1 讲学到的内容，大家能够消化其中的内容，并理解它。好。接下来我们正式开始今天要讨论的核心内容。令人有些惊讶的是，这个在 2017 年提出的 transformer 架构，多年来一直保持着重要地位。

### [09:47](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=587s) · b000019

**English**

And there are a few components that have slightly changed. And we're going to see which ones they are. So there are some slight variations. But overall, today's models are, we're going to see, all more or less based on the initial transformer architecture. So we're going to try to divide the class in two parts. So the first one is what I'm going to cover, which is what are the parts of the transformer that are important and that had some variation.

**中文**

其中有几个组件发生了一些小变化。我们会看看具体是哪些。所以确实有一些细微的变体。不过总体而言，我们将会看到，今天的模型或多或少都基于最初的 transformer 架构。我们打算把这节课分成两部分。第一部分由我来讲，内容是 transformer 中哪些部分比较重要，以及这些部分发生了哪些变化。

### [10:20](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=620s) · b000020

**English**

And in the second part, Shervine is going to talk about, I guess, the nomenclature of today's models and how they relate to the original transformer. Cool. OK, so let's start with the first important concept that's in this architecture. And this is the position embedding. So if you remember, here we're letting tokens interact with all other tokens in a direct fashion.

**中文**

第二部分，Shervine 会讲一下，我想是当今模型的命名体系，以及它们与原始 transformer 的关系。好。我们先从这个架构中的第一个重要概念开始，也就是位置嵌入（position embedding）。如果大家还记得，这里我们让各个 token 以直接的方式与所有其他 token 交互。

### [10:54](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=654s) · b000021

**English**

So they have direct links. But contrary to things like RNNs, where you have a sequential dependency where you process each token one at a time, here you're basically losing this idea of a token being processed before another one. So you lose this position information. So as a result of that, we need to somehow quantify tokens at each position and try to inject that information when the transformer is processing the inputs.

**中文**

也就是说，它们之间有直接连接。但与循环神经网络（RNNs）之类的结构不同，RNNs 存在顺序依赖，每次处理一个 token，而在这里，基本上就失去了一个 token 先于另一个 token 被处理的概念。因此你会丢失这种位置信息。所以，我们需要以某种方式量化各个位置上的 token，并尝试在 transformer 处理输入时注入这些信息。

### [11:40](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=700s) · b000022

**English**

So how are we going to do that? So the original transformer paper authors, they chose to have a dedicated embedding. And when I say dedicated, what that means is each position has one embedding. So position 1 has one embedding, position 2 has one embedding, et cetera, et cetera. And what they chose to do is to add that embedding to the input-token embedding.

**中文**

那要怎么做呢？原始 transformer 论文的作者选择设置专门的嵌入（embedding）。我说专门的，意思就是每个位置都有一个 embedding。位置 1 有一个 embedding，位置 2 有一个 embedding，以此类推。他们选择把这个 embedding 加到输入 token 的 embedding 上。

### [12:14](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=734s) · b000023

**English**

So for instance, if I say a cute teddy bear is reading, which is position number 1, representing the token a, plus the embedding representing the first position. Yeah.

**中文**

例如，如果我说 a cute teddy bear is reading（一只可爱的泰迪熊正在阅读），这是位置 1，表示 token a，再加上表示第一个位置的 embedding。嗯。

### [12:39](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=759s) · b000024

**English**

It's a great question. So the question is, are the position embeddings learned or static? Both, as in the authors have tried both. And we're going to see what the second one is. But I guess here let's suppose that they are learned. So what does that mean? So that means that basically you need to learn embeddings for each position. And the problem with this approach is that you're very much dependent on what is in your training set.

**中文**

这是个很好的问题。问题是，position embedding 是学习得到的，还是静态的？两种都有，也就是说，作者两种都试过。我们马上会看第二种是什么。不过这里先假设它们是学习得到的。这是什么意思呢？意思就是你基本上需要为每个位置学习 embedding。而这种方法的问题在于，你会非常依赖训练集中的内容。

### [13:16](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=796s) · b000025

**English**

So for instance, like here, if you have somehow a text that always has something that is happening at position number 2, your learned embeddings will have that bias kind of learned. So that's one limitation of that. Second limitation is you can only learn positions up to the max number of position that is in your training set. So let's suppose you train your transformer on sequences that are up to, let's say, 512, let's say.

**中文**

例如，像这里，如果你有一些文本，其中某种内容总是出现在位置 2，那么学到的 embedding 就会把这种偏差也学进去。这是它的一个局限。第二个局限是，你只能学习到训练集中出现的最大位置。假设你用长度最多为，比如说 512 的序列来训练 transformer。

### [13:51](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=831s) · b000026

**English**

You can only learn position embeddings up to that position. Right?

**中文**

那你只能学习到这个位置为止的 position embedding。对吧？

### [14:06](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=846s) · b000027

**English**

Yeah. So the question is, I guess, how do you parameterize that? So I guess what you do is you have a placeholder of a learnable position embedding, let's say between position 1 and 512. And basically, when you do your training, you're just letting these weights be learned through the regular gradient descent, all these things. So yeah, so this is like the first method. But as I was mentioning, it has its limitations, because you can only learn embeddings of positions up to the max position that is present in the training set.

**中文**

是的。问题是，我想，如何对它进行参数化？我想做法是，先为可学习的 position embedding 留出占位，比如位置 1 到 512。然后在训练时，让这些权重通过常规的梯度下降（gradient descent）之类的方法学习。所以这就是第一种方法。但正如我刚才提到的，它有局限，因为你只能学习训练集中最大位置以内的位置的 embedding。

### [14:48](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=888s) · b000028

**English**

So for instance, if you have at inference time a position that is beyond the position that was in the training set, well, you have not learned that. So you need to find a way to infer the value. So that's the second limitation. But yeah, but on the pro side, I guess you're just letting your model learn. And we've seen that the gradient descent does wonders when it comes to just learning from the data.

**中文**

例如，在推理（inference）时，如果出现了一个超出训练集所包含位置的位置，那么你没有学过它。所以需要想办法推断它的值。这就是第二个局限。不过从优点来看，我想你就是让模型去学习。我们也已经看到，在从数据中学习这件事上，gradient descent 能发挥很大的作用。

### [15:19](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=919s) · b000029

**English**

So yeah. And for these reasons, these methods was something that the authors said that was performing well, along with the second method, which is different, which is around having an arbitrary formula for each dimension corresponding to a position embedding. And we're going to see that now. So first method was you have one embedding per position, and you just learn that.

**中文**

是的。基于这些原因，作者表示，这些方法表现不错，另一种方法也表现不错。第二种方法有所不同，它为 position embedding 的每个维度设定一个人为指定的公式。我们现在就来看。第一种方法是，每个位置有一个 embedding，然后直接学习它。

### [15:56](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=956s) · b000030

**English**

Second method is you have one embedding per position, but you're not going to learn that. You're going to have something that is predetermined that you're going to use. And we're going to see that what the authors choose was a formulation using sine and cosine. So it can feel weird, why did they choose this. But we're going to see why that makes sense. So the idea here is for a given position, let's say m, have a vector of size d model.

**中文**

第二种方法是，每个位置也有一个 embedding，但不去学习它，而是使用预先确定的内容。我们会看到，作者选择的是使用正弦（sine）和余弦（cosine）的表达式。你可能觉得很奇怪，他们为什么这么选？不过我们会看到这样做为什么合理。这里的思路是，对于某个给定位置，比如 m，设置一个大小为 d model 的向量。

### [16:36](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=996s) · b000031

**English**

So d needs to match the dimension of your token embeddings, because of course you're adding them. And what you're going to do is, for every index you're going to compute the corresponding value with respect to these formulas. So what are these formulas? So it's basically sine of something times m. And we're going to see what that something means. And then the second one is cosine of something times m.

**中文**

所以 d 需要与 token embedding 的维度一致，因为你要把它们相加。接下来，对于每个索引，都根据这些公式计算相应的值。那么这些公式是什么呢？基本上就是某个量乘以 m 的 sine。我们会看看那个量是什么意思。第二个则是某个量乘以 m 的 cosine。

### [17:11](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=1031s) · b000032

**English**

So who remembers trigonometry formulas?

**中文**

有谁还记得三角函数公式？

### [17:17](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=1037s) · b000033

**English**

Cool. Everyone. So before we go into that, let's just simplify the notations. Let's just assume that this big quantity that you saw is actually something like omega. So let's suppose it's omega as a function of i times m. And you note omega i as being this quantity, so 10,000 to the power of minus 2i over d model. Let's suppose you construct your embeddings to have this way.

**中文**

好。大家都记得。那么在深入之前，我们先简化一下记号。假设你刚才看到的那个很大的量实际上就是类似 omega 的东西。假设它是作为 i 的函数的 omega，再乘以 m。把 omega i 记作这个量，也就是 10,000 的负 2i 除以 d model 次方。假设你按这种方式构造 embedding。

### [17:50](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=1070s) · b000034

**English**

Then, I guess I want us to think about why that would make sense. Because if you think about it, what you want is to represent positions in a way that reflects the following fact--words that are close together are likely to be more relevant, as opposed to words that are further together. So if you have two words that are like just one position apart versus 10,000 position apart, what you want is that the one that is one position apart is more similar than the other one.

**中文**

接下来，我想让大家思考一下，这为什么合理。因为仔细想想，你希望位置的表示方式能反映这样一个事实：距离较近的词，比距离较远的词更可能相关。所以，如果两个词只相隔一个位置，而另外两个词相隔 10,000 个位置，你希望相隔一个位置的那一对比另一对更相似。

### [18:34](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=1114s) · b000035

**English**

So let's see if the formula makes sense. So let's suppose you have two position embeddings, so one at position m and the other one at position n. And let's suppose you compute in all the values from this predetermined formula. Well, it turns out, if you remember your trigonometry formulas, so cosine of a minus b is equal to cosine of a cosine of b, plus sine a sine b.

**中文**

我们来看看这个公式是否合理。假设有两个 position embedding，一个位于位置 m，另一个位于位置 n。再假设你根据这个预先确定的公式计算所有值。如果你还记得三角函数公式，cosine(a − b) 等于 cosine(a) cosine(b) 加上 sine(a) sine(b)。

### [19:12](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=1152s) · b000036

**English**

Right? Well, turns out that if you express cosine of omega i, factor of m minus n, this is something that you obtain. It's just the identity that I mentioned. Well, it just turns out that this quantity is just one component that appears when you do the dot product of these two position embeddings.

**中文**

对吧？那么，如果你把 cosine(omega i × (m − n)) 展开，就会得到这个式子。它就是我刚才提到的恒等式。而这个量，恰好就是对这两个 position embedding 做点积时出现的一项。

### [19:43](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=1183s) · b000037

**English**

Right? Because basically here, when you do the dot product of position m and position n, what you do is you take the first position, you multiply them, then you plus the second position, you multiply them, et cetera, et cetera. And then you come here, it's sign of this times sine of this, plus cosine of this times cosine of this, which is just this quantity. So at the end of the day, what you realize is that when you perform a dot product of these embeddings, you end up with a sum of cosine that are a function of the relative distance between m and n.

**中文**

对吧？因为在这里，对位置 m 和位置 n 做点积时，你会取第一个位置，把它们相乘，再加上第二个位置相乘的结果，以此类推。然后到这里，就是这个量的 sign \[字幕疑误，可能指 sine\] 乘以这个量的 sine，再加上这个量的 cosine 乘以这个量的 cosine，也就是这个量。所以最终你会发现，对这些 embedding 做点积，得到的是一组 cosine 的和，它们都是 m 与 n 之间相对距离的函数。

### [20:32](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=1232s) · b000038

**English**

Yep.

**中文**

是的。

### [20:42](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=1242s) · b000039

**English**

What do you mean by pair, by the way?

**中文**

顺便问一下，你说的“一对”是什么意思？

### [21:01](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=1261s) · b000040

**English**

Exactly, yeah. So the question is, so the closer they are, the more similar they are. So that's the intuition, that basically this way of formulating the embeddings is trying to approximate or it's trying to mimic. So with that, you basically obtain a dot product that is just a function of m and n, the relative distance between them, actually. And just as a reminder, so why do I care about the dot product?

**中文**

完全正确，是的。问题是，它们越近，就越相似。这就是这种 embedding 表达方式想要近似或模拟的直觉。这样一来，你得到的点积就是 m 和 n 的函数，准确地说，是它们之间相对距离的函数。再提醒一下，我为什么关心点积？

### [21:31](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=1291s) · b000041

**English**

Because if you remember, in the embedding world when we try to quantify the similarity between two embeddings, what we do is typically something that is involving the dot product of these two. So you typically have the cosine similarity. The cosine similarity is just dot product over the norm of each embedding. So which is basically a dot product. Right? So that's why we care about the dot product. And here we see, great, it's a function of the relative distance between the two.

**中文**

因为如果你还记得，在 embedding 的世界里，当我们试图量化两个 embedding 的相似程度时，通常会用到它们的点积。一般会用余弦相似度（cosine similarity）。cosine similarity 就是点积除以各个 embedding 的范数（norm）。所以基本上还是点积，对吧？这就是我们关心点积的原因。在这里我们看到，很好，它是两者相对距离的函数。

### [22:06](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=1326s) · b000042

**English**

So in particular, again, if you remember your trigonometry class, cosine of 0 is 1. And the higher this number, the lower the value of cosine of this number. Of course, it's periodic, so what I'm saying is not necessarily true. Past pi, just goes the other way.

**中文**

具体来说，如果你还记得三角函数课，cosine(0) 等于 1。而这个数越大，它的 cosine 值就越小。当然，它是周期性的，所以我说的并不一定成立。超过 pi 之后，变化方向就反过来了。

### [22:38](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=1358s) · b000043

**English**

But I guess what I'm trying to say is for m equal to n, you have basically a sum of cosine of 0. And it is the value at which this quantity is maximum. So when m is equal to n, this quantity is maximum. Which means basically if you're looking at the position itself, it's the most similar. Basically, it matches our intuition.

**中文**

不过，我想表达的是，当 m 等于 n 时，基本上得到的是一组 cosine(0) 的和。此时这个量达到最大值。所以当 m 等于 n 时，这个量最大。这基本上意味着，如果你看这个位置本身，它与自身最相似。这符合我们的直觉。

### [23:10](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=1390s) · b000044

**English**

And so now when you plot the values of the embeddings, this is what you obtain. So here in this graph on the y-axis, I'm basically representing all the embeddings for each of the, let's say, 50 positions. And on the x-axis, it's basically values along a given vector across several dimensions of a vector. So if you take, let's say, the first row, you're looking at the first or number 0 position, depending on how you index your vector.

**中文**

现在把 embedding 的数值画出来，就会得到这幅图。这里图中的 y 轴，基本上表示每个位置的所有 embedding，比如说 50 个位置。而 x 轴基本上表示某个向量在多个维度上的取值。例如，如果你取第一行，看到的就是第一个位置，或者编号为 0 的位置，取决于你如何为向量编索引。

### [23:48](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=1428s) · b000045

**English**

And you're looking at all the values of the position 0 embedding. And so you see that for low dimensions, this value goes up and down very frequently. So it's more high frequency. And when the dimension is high, it basically takes a lot of time for the value to go up and down. So it's basically more low frequency.

**中文**

你看到的是位置 0 的 embedding 的所有数值。你会发现，在较低的维度上，这个值非常频繁地上下变化，也就是频率更高。而当维度较高时，这个值要过很久才会上下变化，也就是频率更低。

### [24:22](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=1462s) · b000046

**English**

So this relates to this omega i that I mentioned, this omega i. So omega i is very high for low values of i, which is the dimension. And it's very low for high values of i. So this basically just determines how quickly your cosine and sine basically vary.

**中文**

这就与我提到的 omega i 有关，就是这个 omega i。当 i 较小时，也就是维度较低时，omega i 非常大。当 i 较大时，它就非常小。所以它基本上决定了 cosine 和 sine 变化的快慢。

### [24:52](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=1492s) · b000047

**English**

Cool. So this is what the original authors have tried. And basically what they said, what they noted was that using these methods leads to comparable results compared to the learned one. But here we have a big advantage, because it can extend to any sequence length, not just a sequence length that you saw at training time. And this is one of the reasons why this may be something that is preferable.

**中文**

好。这就是原作者尝试的方法。他们表示，也就是他们观察到，使用这些方法与使用学习得到的 embedding 相比，结果相当。不过这里有一个很大的优势，因为它能够扩展到任意序列长度，而不只是训练时见过的序列长度。这也是这种方法可能更值得采用的原因之一。

### [25:26](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=1526s) · b000048

**English**

So yeah, this is the intuition and this is what the authors chose. Now, fast forward to 2025. I guess you may ask me, are we still using that? And the answer is kind of. So we're still using this idea of we want far--I guess, tokens to be less similar than closer tokens. But we're not injecting the embedding like they did. And we're going to see why.

**中文**

是的，这就是背后的直觉，也是作者的选择。现在快进到 2025 年。我想你可能会问，我们还在用这个吗？答案是，某种程度上是的。我们仍然沿用这个想法：希望远处的——我是说，token 比近处的 token 更不相似。不过我们不再像他们那样注入 embedding。接下来会解释为什么。

### [25:56](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=1556s) · b000049

**English**

Because if you remember, what you care about is determining how similar tokens are in the self-attention computation. And where does the self-attention computation happen? In the attention layer. But here, what did I say? I said, let's compute these embeddings and let's add them here. But actually what we want is to reflect this similarity in the attention layer.

**中文**

因为如果你还记得，我们关心的是，在 self-attention 计算中确定 token 之间的相似程度。self-attention 计算在哪里发生？在 attention 层。但这里我刚才说了什么？我说，计算这些 embedding，然后把它们加在这里。可实际上，我们希望在 attention 层中体现这种相似性。

### [26:35](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=1595s) · b000050

**English**

Do you have a question? Yeah.

**中文**

你有问题吗？嗯。

### [26:40](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=1600s) · b000051

**English**

So in this first method, yes. So the question is, is it added to the input feature. Yes.

**中文**

在这第一种方法里，是的。问题是，它是否加到了输入特征上？是的。

### [26:47](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=1607s) · b000052

**English**

Yes, just add. Yeah, yeah. But the problem is, we mostly want these, I guess, intuition to hold true in the multi-head attention layer. So this is one of the reasons why people have tried different variations, and in particular have these position embeddings intervene directly in the attention layer, as opposed to the input.

**中文**

对，直接相加。对，对。但问题是，我们主要希望这些直觉在 multi-head attention 层里成立。所以这也是人们尝试不同变体的原因之一，尤其是让这些 position embedding 直接作用于 attention 层，而不是输入。

### [27:22](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=1642s) · b000053

**English**

Because basically when you do it at the input--just here, fair, OK--it's going to be roughly something that is going to go into this attention layer, but it's kind of indirect. So what we want is to directly do something about the attention formula that would, I guess, reflect the fact that we want close tokens to be more similar, compared to further tokens.

**中文**

因为如果你在输入端做这件事——就在这里，可以，没问题——它大致上会进入这个 attention 层，但这个过程有点间接。所以我们希望直接调整 attention 公式，使它反映这样一个想法：我们希望近处的 token 比远处的 token 更相似。

### [27:52](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=1672s) · b000054

**English**

And the way we do that is, if you remember, the self-attention layer is basically the softmax of qk transpose over square root of d times v. So what we want is to add a little something inside that softmax, which is basically where you quantify how similar a token is to another token. You want to add a little something to reflect the fact that some tokens, they're supposed to be more similar compared to that token, compared to others.

**中文**

具体做法是，如果你还记得，self-attention 层基本上就是 softmax(qk 的转置 / √d) × v。所以我们想在这个 softmax 里面加一点东西，因为这里正是量化一个 token 与另一个 token 相似程度的地方。你想加一点东西，来反映这样一个事实：相对于其他 token，有些 token 应该与这个 token 更相似。

### [28:32](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=1712s) · b000055

**English**

So there's a few methods that have tried to have some variation of that. So for those of us who know the T5 paper, what we're going to see a little bit later, they have tried these relative position bias by learning the bias term, which is in the formula above.

**中文**

有几种方法尝试了这方面的变体。对于了解 T5 论文的同学，我们稍后会讲到它，他们尝试了相对位置偏置（relative position bias），通过学习上面公式中的偏置项（bias term）来实现。

### [29:04](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=1744s) · b000056

**English**

So what they did was, let's suppose you have a given distance between the positions m and n. So their idea was, let's learn that. Let's basically bucketize all m minus n into some buckets. And let's just have the model learn these quantities that are then going to be injected into softmax.

**中文**

他们的做法是，假设位置 m 和 n 之间有一个给定的距离。他们的想法是，那就学习它。基本上，把所有 m − n 分到一些桶里，也就是分桶（bucketize）。然后让模型学习这些量，再把它们注入 softmax。

### [29:34](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=1774s) · b000057

**English**

Yeah.

**中文**

嗯。

### [29:43](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=1783s) · b000058

**English**

So the question is, does that pose a problem that the bias is here with respect to the probability at the end? Because it has to sum to 1. Well, you can do whatever you want inside the softmax, because the softmax is going to normalize it anyways.

**中文**

问题是，相对于最终的概率，把 bias 放在这里是否会造成问题？因为概率之和必须等于 1。其实，你可以在 softmax 里面做任何事情，因为 softmax 最终都会将它归一化。

### [29:59](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=1799s) · b000059

**English**

So you can think of the bias as being something that is maybe more negative for things that are far apart, compared to things that are closer together. So T5 says, let's learn them. We have another message from, I guess, this "Train Short, Test Long" paper, which introduced this method called ALiBi. ALiBi stands for Attention with linear bias, I believe.

**中文**

所以你可以把 bias 理解为：对于距离较远的内容，它可能比距离较近的内容更加负。T5 说，那就学习这些 bias。另一个思路来自这篇《Train Short, Test Long》论文，它提出了一种叫 ALiBi 的方法。我记得 ALiBi 是带线性偏置的注意力（Attention with linear bias）的缩写。

### [30:30](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=1830s) · b000060

**English**

And what they did was, say instead of learning those biases, let's actually have a deterministic formula, which is as a function of the relative difference between those two positions. And they said that. So they had some results. So all these papers, they always compare based on one another to see which one is, I guess, more performant.

**中文**

他们的做法是，与其学习这些 bias，不如直接使用一个确定性的公式，把它写成两个位置相对差值的函数。他们就是这么说的。他们也有一些结果。所有这些论文总是相互比较，看看哪一种性能更好。

### [31:01](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=1861s) · b000061

**English**

But the reality is is that in today's models, most models actually use another kind of position embedding method. And we're going to see it now. So this method relies on rotating the query and the key vector by some angle. And I guess you can think of it as, you have your query, you have your key, let's suppose in a 2D space.

**中文**

但实际情况是，在当今模型中，大多数模型用的是另一种 position embedding 方法。我们现在就来看。这种方法依靠将 query 和 key 向量旋转某个角度。你可以这样理解：有一个 query，有一个 key，假设它们处于二维（2D）空间中。

### [31:37](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=1897s) · b000062

**English**

So what you're going to do is rotate your query by some angle that is a function of its position. And you're going to rotate the key vector by some angle that is a function of its position n. And I guess how do you do that, by the way? I wasn't supposed to show this thing. So let's suppose you have a vector, by the way. And you want to rotate that vector, because I had the answer on the slide.

**中文**

接下来，把 query 旋转某个角度，这个角度是它所在位置的函数。再把 key 向量旋转某个角度，这个角度是它所在位置 n 的函数。顺便问一下，这要怎么做呢？我本来不该把这个展示出来的。假设你有一个向量，想要旋转这个向量，因为我已经把答案放在幻灯片上了。

### [32:09](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=1929s) · b000063

**English**

But how would you go about this, I guess, for people who just want to talk about this with intuition?

**中文**

不过，如果只想从直觉角度讨论这件事，你会怎么做呢？

### [32:21](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=1941s) · b000064

**English**

So who here has done, I don't know, rotations in space? Yeah.

**中文**

在座有谁做过，我不知道，空间中的旋转？嗯。

### [32:33](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=1953s) · b000065

**English**

That's correct, yeah. Matrix multiplication. And you're going to use a quantity that's called rotation matrix. And the rotation matrix is expressed as follows. So it's basically a 2 by 2 matrix in the 2D plane that has cosine of this angle, minus sine of this angle, sine of this angle, cosine of this angle. I'm looking at the time. It's quite simple to just show that it works, but we may run out of time.

**中文**

对，没错。矩阵乘法。你会用到一个叫旋转矩阵（rotation matrix）的量。rotation matrix 的表达式如下。在 2D 平面里，它基本上是一个 2 × 2 矩阵，元素依次是这个角度的 cosine、负 sine、sine 和 cosine。我看一下时间。证明它确实有效其实很简单，但我们可能会没时间。

### [33:04](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=1984s) · b000066

**English**

Do you want me to quickly show you that it's indeed a way to rotate the vector? OK. So here as a reminder what we're trying to show is that we can use a matrix multiplication to rotate a vector in 2D space. So let's suppose we have the following vector. That is something that you can quantify with two dimensions, let's say x and y.

**中文**

你们想让我快速展示一下，它确实能旋转向量吗？好。提醒一下，这里我们想证明的是，可以用矩阵乘法旋转 2D 空间中的一个向量。假设有下面这个向量。它可以用两个维度来量化，比如 x 和 y。

### [33:42](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=2022s) · b000067

**English**

You can express your vector in 2D space with this. Right? But I guess this, if you note, are the norm of the vector, and phi, the angle with respect to the x-axis. You can also write v as R with vector cosine of phi and sine of phi.

**中文**

你可以用这个来表示 2D 空间中的向量，对吧？不过，如果你把向量的范数记作 R，把它与 x 轴的夹角记作 phi，也可以把 v 写成 R 乘以由 cosine(phi) 和 sine(phi) 组成的向量。

### [34:21](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=2061s) · b000068

**English**

Right? So if you multiply the rotation matrix with this phi, what you're going to obtain is some multiplication of cosine minus sine, sine and cosine of this and that. And I will leave this exercise for you. But you can show that rotation times this v can be expressed as R of cosine of theta plus phi, and sine of theta plus phi.

**中文**

对吧？所以，如果把 rotation matrix 与这个 phi 相乘 \[原文如此，此处可能指向量 v\]，得到的就是一些 cosine、负 sine、sine 和 cosine 之间的乘法。我把这道练习留给大家。不过可以证明，旋转矩阵乘以这个 v，可以表示为 R 乘以由 cosine(theta + phi) 和 sine(theta + phi) 组成的向量。

### [35:09](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=2109s) · b000069

**English**

So this is a quick proof. So I'll just leave you the multiplication of the rotation matrix and v. But you will obtain these trigonometric identities that will, I guess, lead you to this formula. This basically shows that if you multiply this matrix and this vector, you're basically rotating the vector by this angle. Yeah. So the question is, why do you want to do this?

**中文**

这就是一个简短的证明。我把 rotation matrix 与 v 的乘法留给你们做。你会得到这些三角恒等式，它们会导出这个公式。这基本上证明了，把这个矩阵与这个向量相乘，就相当于把向量旋转这个角度。嗯。问题是，为什么要这么做？

### [35:40](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=2140s) · b000070

**English**

It's a great question. It's my next slide. So this is just a little intro. So I guess here, just going back to this method, what we want to do is to quantify the similarity between tokens, and have close tokens be more similar compared to tokens that are more afar. So the problem that we had with the previous methods was--so in the first method, this learned embedding, you always had this overfitting issue.

**中文**

这是个很好的问题。下一页幻灯片就会讲。所以这里只是一个小引子。回到这个方法，我们想做的是量化 token 之间的相似度，并让近处的 token 比远处的 token 更相似。之前那些方法的问题是——第一种方法，也就是学习得到的 embedding，总会存在过拟合（overfitting）问题。

### [36:18](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=2178s) · b000071

**English**

Because basically when you learn these biases, it always depends on which training set you have. So maybe your data set is in a way that, let's say, tokens that are close are similar, but in a different way compared to what you see at inference time. And this ALiBi method, it didn't have that learnable component, but it was quite restrictive, because it's a very simple formula after all, just the relative difference between n and m.

**中文**

因为学习这些 bias 时，总会依赖你使用的训练集。也许你的数据集里，相邻 token 确实相似，但这种相似方式与推理时看到的情况不同。而 ALiBi 方法虽然没有可学习的部分，但它的限制很强，因为说到底，它的公式非常简单，就是 n 和 m 之间的相对差值。

### [36:49](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=2209s) · b000072

**English**

So I guess people have tried different ways of coming up with something that tells you that, I guess, an embedding that reflects the fact that you want further positions to be less similar than closer ones. So in this method, we're going back to the sine and cosine world from what the author had proposed. And think about similarity from the lens of cosine and sine functions.

**中文**

所以，人们尝试了不同方式，想构造出某种东西，也就是一个 embedding，来体现我们希望较远位置比较近位置更不相似这一点。在这个方法中，我们又回到作者所提出的 sine 和 cosine 的世界，从 cosine 和 sine 函数的角度来思考相似性。

### [37:24](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=2244s) · b000073

**English**

So this is a little intro. And their method is called RoPE. So I'm not sure if you've heard of it. So it stands for Rotary Position Embeddings. And we're going to see that this method-- so why do we care about this method? So this method has two great things. So the first one is that if you rotate the query and the key, you will end up with a quantity that will be a function of the relative distance between the two.

**中文**

这就是一个小引子。他们的方法叫 RoPE。不知道你们是否听说过。它代表旋转位置嵌入（Rotary Position Embeddings）。接下来我们会看到这个方法——我们为什么关心它呢？它有两个很好的特点。第一个是，如果旋转 query 和 key，最终得到的量会是两者相对距离的函数。

### [37:59](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=2279s) · b000074

**English**

That's going to be very nice, and that's why I wrote this thing on the blackboard. Not sure if you can see, by the way, but we won't have time to go into the mathematical detail. But if you want to just express these things at home, this is just the foundation.

**中文**

这会非常好，也正是我把这个写在黑板上的原因。顺便说一下，不知道你们能不能看清，但我们没有时间深入数学细节。如果你想回家把这些表达式写出来，这就是基础。

### [38:19](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=2299s) · b000075

**English**

And so in particular, if you remember your attention formula, so you have query times key transpose. So if you rotate the query by an angle m and the key by an angle n, what you're going to end up is a formula that has the rotation matrix of angle theta and, I guess, n minus m.

**中文**

具体来说，如果你还记得 attention 公式，里面有 query 乘以 key 的转置。如果把 query 旋转角度 m，把 key 旋转角度 n，最终得到的公式会包含一个 rotation matrix，其角度是 theta 和，我想是 n − m。

### [38:53](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=2333s) · b000076

**English**

And this is great because this is a function of the relative distance between these two positions.

**中文**

这很好，因为它是这两个位置相对距离的函数。

### [39:01](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=2341s) · b000077

**English**

OK, so why do I talk about this in detail? Well, it turns out that most models these days, they use RoPE, which is why it's important. And I would say another thing, it's maybe a little bit hard to get the intuition as to why that works. But hopefully, the explanation that I gave regarding the sine and cosine at the very beginning can help you just build that intuition. And speaking of that, it turns out that the upper bound of the attention weight given by the query and the key is such that we observe a long-term decay.

**中文**

好，那我为什么这么详细地讲这个？因为现在大多数模型都使用 RoPE，所以它很重要。另外一点是，要从直觉上理解它为什么有效，可能有点难。但希望我最开始关于 sine 和 cosine 的解释能帮助大家建立这种直觉。说到这里，由 query 和 key 给出的 attention weight 的上界，会呈现出一种长期衰减。

### [39:48](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=2388s) · b000078

**English**

Meaning that as n minus m is large, we do see the upper bound that gets smaller and smaller. Well, you see these little oscillations, it's not perfect either. But we do have some mathematical, I guess, results as to just the upper bounds decaying over the long-term.

**中文**

意思是，当 n − m 很大时，我们确实会看到这个上界越来越小。当然，你也能看到这些小幅振荡，它也不完美。不过，关于上界长期衰减这件事，我们确实有一些数学结果。

### [40:18](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=2418s) · b000079

**English**

Cool. Any questions on this? Yeah, yeah.

**中文**

好。关于这个有什么问题吗？嗯，嗯。

### [40:38](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=2438s) · b000080

**English**

Exactly, yeah. So the question is the relative distance is captured in the rotation matrix--and yes, yes.

**中文**

完全正确，是的。问题是，相对距离是不是体现在 rotation matrix 里——是的，是的。

### [40:49](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=2449s) · b000081

**English**

Oh, yeah.

**中文**

哦，是的。

### [40:53](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=2453s) · b000082

**English**

It's a great question. So the question is, what is theta? So theta is actually fixed. So do you remember this omega that I talked about here? Here. So it's basically some function of i and d. I actually pass it quite quickly. But what I showed you is in the 2D space. But here we're in a d-dimensional space, which is greater than 2. So I glossed it very quickly.

**中文**

这是个很好的问题。问题是，theta 是什么？theta 实际上是固定的。还记得我在这里讲过的 omega 吗？这里。它基本上是 i 和 d 的某个函数。我刚才讲得确实比较快。我展示的是 2D 空间中的情况，但这里我们处于 d 维空间，而且 d 大于 2。所以这一点我很快就带过去了。

### [41:25](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=2485s) · b000083

**English**

But the way you extend this method is by having these 2D space by block. But then the theta is a function of typically something that you fix, but a function of i, which is the dimension. It's basically between 1 and d over 2. It's a function of that, and it's a function of d as well. You will see this theta as being roughly equal to omega i, just this one, more or less, more or less.

**中文**

扩展这个方法的方式，就是把这些 2D 空间按块组织起来。theta 通常是某个固定设定的函数，但也是 i 的函数，这里的 i 是维度，基本上在 1 到 d / 2 之间。它是 i 的函数，同时也是 d 的函数。你会看到，这个 theta 大致等于 omega i，就是这一个，差不多，差不多。

### [42:04](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=2524s) · b000084

**English**

Sorry?

**中文**

什么？

### [42:07](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=2527s) · b000085

**English**

Oh, so the question is, so that it has the same dimension as the latent dimension? So, well, here you have a product of matrices. So you need to have the dimensions match. So I guess your answer-- yeah.

**中文**

哦，问题是，这样它就和潜在维度（latent dimension）的维数相同了？这里涉及矩阵乘法，所以维度必须匹配。所以我想，你的答案——对。

### [42:30](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=2550s) · b000086

**English**

Does that make sense?

**中文**

这样讲清楚了吗？

### [42:34](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=2554s) · b000087

**English**

I'll take that as a yes. So I spent a bunch of time on this, because I think this is actually quite important. A lot of models use this. And yeah, I guess the intuition is not super obvious. So I hope this was helpful. So this was position embeddings. Yeah. Oh, yeah. Yeah, so the question is about, how do you obtain this curve? So this is actually a curve that I believe is shown mathematically.

**中文**

那我就当作是清楚了。我在这上面花了不少时间，因为我觉得它确实很重要。很多模型都在用它。而且背后的直觉确实不是特别明显。希望这些讲解有所帮助。以上就是 position embedding。嗯。哦，是的。对，问题是，这条曲线怎么得到？我认为这实际上是一条通过数学推导得到的曲线。

### [43:09](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=2589s) · b000088

**English**

So it's kind of complicated. We're not going to write down the formula. But if you're interested, so in this paper, in the RoFormer paper, there's an appendix where they show mathematically that it is upper bounded by some quantity. And this is what this is showing. Yeah, great question.

**中文**

它有点复杂，我们就不把公式写出来了。如果你感兴趣，在这篇 RoFormer 论文里有一个附录，他们从数学上证明了它被某个量上界约束。这里展示的就是那个量。对，问得很好。

### [43:29](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=2609s) · b000089

**English**

Cool. So, position embeddings is one part of the transformer that has changed a little bit. And we've seen how that changed, and why. So now we're going to see another component of the transformer that has also a little bit changed. And that component is the layer normalization. So if you remember, the transformer architecture, which is composed, again, of encoder, decoder, and then you have the components inside.

**中文**

好。position embedding 是 transformer 中发生了一些变化的部分。我们看到了它如何变化，以及为什么变化。现在来看 transformer 中另一个也发生了一些变化的组件，也就是层归一化（layer normalization）。如果大家还记得，transformer 架构还是由 encoder、decoder，以及它们内部的组件组成的。

### [44:02](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=2642s) · b000090

**English**

So you have these boxes that say add and norm. So what do they mean? So basically, here, what we do is we take the input, as well as the output of this sublayer. We add them together, and then we normalize. So this is a little trick that the authors do. And it is shown in practice to improve convergence and just make the convergence be quicker.

**中文**

这里有一些方框写着 add 和 norm。它们是什么意思？基本上，我们取输入，以及这个子层（sublayer）的输出，把它们加起来，然后归一化。这是作者使用的一个小技巧。实践表明，它能够改善收敛（convergence），让收敛更快。

### [44:40](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=2680s) · b000091

**English**

So the idea is as follows--if you have a vector, sometimes the components of the vector can be super large, sometimes they can be super small. The idea here is to normalize the components of your vector within some range, some normalized range. So the way you're going to do that is you're going to take your vector, and then subtract it by the computed mean, which is basically the sum of its components, and normalize it by basically its standard deviation.

**中文**

思路如下：如果有一个向量，它的分量有时可能特别大，有时可能特别小。这里的想法是，把向量的分量归一化到某个范围，也就是某个归一化的范围。做法是，取这个向量，减去计算得到的均值，基本上就是它各分量的总和，然后基本上用它的标准差进行归一化。

### [45:20](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=2720s) · b000092

**English**

And what you're going to do is you're going to learn two quantities--one, gamma, which is going to be the rescaling factor, and then beta, which is another term as well that you learn. And you're going to let these two quantities be learned by your model. And so in practice, as I mentioned, so what this does is it helps with training stability and with convergence time.

**中文**

接下来，你要学习两个量：一个是 gamma，用作重新缩放的因子；另一个是 beta，也是需要学习的项。让模型学习这两个量。正如我所说，在实践中，这样做有助于训练稳定性，并缩短收敛时间。

### [45:53](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=2753s) · b000093

**English**

So this was a technique that was used in the original transformer paper. I just want to call out that there has been some changes since then. So we went from normalizing the input plus the output of the sublayer, to having a sum of the input and the sublayer of the normalized input. So in other words, what we've done is to change where the normalization is located.

**中文**

这是原始 transformer 论文使用的一种技术。我想指出，自那以后发生了一些变化。我们从对输入与子层输出之和进行归一化，变成了把输入与“归一化后的输入经过子层的结果”相加。换句话说，我们改变了归一化所在的位置。

### [46:28](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=2788s) · b000094

**English**

So here in the transformer paper, it was what we now call a post-norm version. And nowadays, we use a pre-norm version, which basically consists of having the LayerNorm right before the vector goes into the sublayer. And sublayer here can be either the attention layer or the FFN.

**中文**

在 transformer 论文中，使用的是现在称为后置归一化（post-norm）的版本。如今，我们使用前置归一化（pre-norm）版本，也就是把 LayerNorm 放在向量进入子层之前。这里的子层可以是 attention 层，也可以是前馈网络（FFN）。

### [46:56](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=2816s) · b000095

**English**

But not only that, there is also another change. So nowadays, people, they do not use LayerNorm. They use something else called RMSNorm--RMS, Root Mean Square, Normalization, which is basically a variation of what you've seen before. So instead of computing this, basically what people do is they just normalize x by the root mean square of the components of x, and they learn gamma, only gamma.

**中文**

不仅如此，还有另一个变化。如今人们不使用 LayerNorm，而使用另一种叫 RMSNorm 的方法——RMS，也就是均方根（Root Mean Square），Normalization，也就是归一化。它基本上是刚才那种方法的变体。不再计算这个，而是用 x 各分量的均方根对 x 进行归一化，并学习 gamma，只学习 gamma。

### [47:34](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=2854s) · b000096

**English**

So why do they do that? Basically, they show that the convergence properties, they're basically comparable. But here you have fewer parameters to learn. So it's basically quicker. Yeah.

**中文**

为什么这么做？基本上，他们证明了两者的收敛性质相当。但这里需要学习的参数更少，所以基本上会更快。嗯。

### [48:12](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=2892s) · b000097

**English**

Good question. So the question is, what is the intuition behind normalizing? So the intuition is that, if you look at your model, you have several layers. In some layers your vector--your activation, to be more precise--so do you know the vector that you see that goes from here to here is basically called activation. Sometimes the activation has extreme values in one part of its component, sometimes in another part. And the model is typically having trouble in learning the weights in each of these layers if these activations, they vary too much.

**中文**

好问题。问题是，归一化背后的直觉是什么？直觉是，如果看一下模型，它有好几层。在某些层里，你的向量——更准确地说是激活值（activation）——你知道，这个从这里传到这里的向量基本上就叫 activation。有时 activation 在一部分分量上出现极端值，有时在另一部分。如果这些 activation 变化太大，模型通常就难以学习各层中的权重。

### [48:54](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=2934s) · b000098

**English**

So the idea is to bring the values of the components of the activation to some range that is not too far off in some direction. So in case you're interested, there is this key word, internal covariate shift, which is basically the term that is given to the phenomenon that I'm describing here. So yeah, that's the intuition.

**中文**

所以思路是，把 activation 各分量的值带到某个范围内，使它们不会在某个方向偏得太远。如果你感兴趣，有一个关键词叫内部协变量偏移（internal covariate shift），基本上就是我刚才描述的这种现象的名称。是的，这就是直觉。

### [49:24](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=2964s) · b000099

**English**

Yeah.

**中文**

嗯。

### [49:27](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=2967s) · b000100

**English**

Oh, great, great question. So question is, what is the difference between this and batch normalization? So batch normalization is normalization across the other dimension, which is the dimension of the batch. So let's suppose you have a bunch of vectors. What you do is you normalize each component with respect to all the other components for the same dimension, but of the other vectors.

**中文**

哦，很好，非常好的问题。问题是，这与批归一化（batch normalization）有什么区别？batch normalization 是沿另一个维度归一化，也就是 batch 的维度。假设你有一组向量。你会针对每个分量，参照其他向量在相同维度上的所有分量进行归一化。

### [49:57](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=2997s) · b000101

**English**

So you can think of it as just another way of normalizing. But that being said, when it comes to these transformer-based models, typically people use LayerNorm, probably because empirically it works better. But also because BatchNorm, you're basically also dependent on the batch. And it can introduce, I guess, differences between training and then inference. So that's basically the reason why.

**中文**

所以你可以把它看成另一种归一化方式。不过，对于这些基于 transformer 的模型，人们通常使用 LayerNorm，可能是因为经验上它效果更好。同时也是因为 BatchNorm 还依赖 batch，这可能导致训练和推理之间存在差异。基本上就是这个原因。

### [50:30](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=3030s) · b000102

**English**

Cool, great. So we've seen position embeddings. We've seen layer normalization. So now we're going to see a third important component of the transformer, which is the attention. And in particular, I guess there is something I've not really emphasized. But when you do self-attention, you're basically letting every token interact with all other tokens. So when you look at, let's, say a matrix that shows all the interactions, so you have n, the sequence length.

**中文**

好，很好。我们已经看了 position embedding，也看了 layer normalization。现在来看 transformer 的第三个重要组件，也就是 attention。尤其是，有一件事我之前没有特别强调：做 self-attention 时，基本上是在让每个 token 与所有其他 token 交互。所以如果看一张展示所有交互的矩阵，这里有 n，也就是序列长度。

### [51:06](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=3066s) · b000103

**English**

And the sequence length, you basically have o of n squared complexity, which is a lot, especially as n grows longer. So people have tried to approximate this o of n squared into something that is a little bit more tractable, but does not lose the performance. So there is this paper in 2020 that came out, "LongFormer." So what it did was just try different versions of the attention by restricting the window at which it operates.

**中文**

对于这个序列长度，基本上有 O(n²) 的复杂度，这非常大，尤其当 n 变得更长时。所以，人们尝试用更容易处理的计算来近似这个 O(n²) 计算，同时不损失性能。2020 年发表了一篇论文《LongFormer》。它做的就是通过限制 attention 作用的窗口，尝试不同的 attention 版本。

### [51:42](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=3102s) · b000104

**English**

So here, instead of letting each token interact with everyone, each token only interacts with its neighborhood. Yeah.

**中文**

这里不再让每个 token 与所有 token 交互，而是让每个 token 只与它的邻域交互。嗯。

### [51:55](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=3115s) · b000105

**English**

Oh, again, a great question. So question is, do you do that after the attention matrix computation? You mean the softmax, right, softmax? So you raise a great point, which is, if you do the softmax of everything, why would you do this? So in practice there is a bunch of implementations that does a clever--so it's called tiling--a bunch of clever operations that do not involve this huge matrix operation that you see in the softmax.

**中文**

哦，又是个很好的问题。问题是，是在计算完 attention 矩阵之后再做这件事吗？你是指 softmax，对吧，softmax？你提出了一个很好的点：如果已经对所有内容算了 softmax，为什么还要这么做？实际上，有很多实现采用了一些巧妙的——它叫分块（tiling）——一些巧妙的操作，避免执行你在 softmax 中看到的那个巨大的矩阵运算。

### [52:30](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=3150s) · b000106

**English**

Again, I guess, like against the softmax of qk transpose over d. You're not going to compute the whole thing. You're going to have some cleverness in how you compute that, basically.

**中文**

再说一次，我想，就是对 qk 的转置除以 d 做 softmax。你不会把整个东西都算出来。基本上，你会采用一些巧妙的计算方式。

### [52:54](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=3174s) · b000107

**English**

Yeah, so the question is, can it be something that's comparable to convolutions? And we're going to see that in a second. But you have some similarities with the vision world. And we're going to see that in a second.

**中文**

是的，问题是，它是否可以类比卷积（convolutions）？我们马上就会讲到。它与视觉领域中的一些东西确实有相似之处。我们马上会看到。

### [53:11](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=3191s) · b000108

**English**

Cool. So nowadays when you have local attention like this, like this, people use the term sliding window attention. So when they use that term, they mean this, which is basically just restricting the attention to neighboring tokens. And nowadays what people do is in some layers they will have local attention. In some others, they will have global attention.

**中文**

好。如今，像这样的局部注意力（local attention），人们会使用滑动窗口注意力（sliding window attention）这个术语。他们使用这个术语时，指的就是这种方式，基本上把 attention 限制在相邻 token 上。如今的做法是，有些层采用 local attention，另一些层采用全局注意力（global attention）。

### [53:44](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=3224s) · b000109

**English**

And they interleave these layers. So depending on the model, they typically try different combinations. So there's not a set recipe. But it's typically something that is used nowadays. So the window here, I mean, for, illustrative, purposes, the window is super small in my illustration. But I guess nowadays with the sequence lengths that can be very big, you can think of this window as being, o of several, thousands.

**中文**

这些层会交错排列。根据模型的不同，人们通常会尝试不同的组合。没有一套固定的配方，但这是现在经常采用的做法。这里的窗口，我是说，为了便于说明，我画的窗口非常小。不过现在序列长度可能非常大，所以可以把这个窗口理解为几千的量级。

### [54:20](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=3260s) · b000110

**English**

And just to give you another example. So back to the convolution comparison that you mentioned. So you have some architectures. And here I'm going to take the example of a mistral that has these sliding window attention at every layer. But then when you think about it, the token here can attend up to the token here, but then the token here can attend up to the token here, et cetera, et cetera.

**中文**

再举一个例子。回到你提到的与卷积的比较。有一些架构，这里我用 mistral 举例，它每一层都使用 sliding window attention。不过仔细想想，这里的 token 可以关注到那里的 token，然后那里的 token 又可以关注到更远处的 token，以此类推。

### [54:53](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=3293s) · b000111

**English**

So I guess, if you think about it, it's similar to the idea of the receptive field in computer vision. So I'm not sure if you're familiar or from the computer vision world. But if you are, what this means is just taking one token and trying to think what other tokens has this token effectively interacted with, which is basically the question that people also sometimes ask.

**中文**

所以仔细想想，这类似于计算机视觉（computer vision）中的感受野（receptive field）概念。不知道你是否熟悉，或者是否来自 computer vision 领域。如果是，这里的意思就是，取一个 token，思考它实际上与哪些其他 token 发生过交互。这基本上也是人们有时会问的问题。

### [55:25](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=3325s) · b000112

**English**

When they do convolution, they're like, OK, so this value, what are the values did it actually see? So you can also think it this way. OK, so first variation is, instead of doing the full n by n attention, people sometimes do local attention. The second variation that is orthogonal to all of this is to not have one projection matrix per head, but to share projection matrices across heads.

**中文**

做卷积时，人们会问，好，这个值实际上看到了哪些值？所以你也可以这样理解。好，第一种变体是，不做完整的 n × n attention，而有时采用 local attention。第二种变体与这些都是正交的，也就是不再为每个 head 设置一个投影矩阵，而是跨 head 共享投影矩阵。

### [56:10](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=3370s) · b000113

**English**

So here the idea is you have, let's say, h heads. The idea is you're going to have some number of projection matrices for the query. But then what you're going to do is to group the projection matrices for the key and the value that you're going to share across several heads.

**中文**

这里的想法是，假设有 h 个 head。你会为 query 设置一定数量的投影矩阵。然后，把 key 和 value 的投影矩阵分组，让多个 head 共享它们。

### [56:34](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=3394s) · b000114

**English**

Now you may ask, why do you share projection matrices for the keys and the values, but not for the queries? Is this the question that you're wondering? Well here, I guess, people do things to just try out if something works or not. I guess here you can intuitively think that the query is basically wondering if something is similar to another thing. So I guess you can ask yourself this question in different ways.

**中文**

现在你可能会问，为什么共享 key 和 value 的投影矩阵，却不共享 query 的？这是你正在想的问题吗？这里，我想，人们做这些事情就是为了试试看是否有效。直观上，你可以把 query 理解为，它基本上在询问某个东西是否与另一个东西相似。而你可以用不同的方式问自己这个问题。

### [57:06](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=3426s) · b000115

**English**

So it may make sense to keep that diversity. But one of the core reasons why we choose to group projection matrices for the keys and the values and not the query is because, when you decode, you perform attention between the current word and all the words before. So in other words, every time you generate a new word, you're going to attend that word to all the words before.

**中文**

所以保留这种多样性可能有道理。不过，选择对 key 和 value 的投影矩阵进行分组，而不对 query 这么做的一个核心原因是，在解码时，你要在当前词与之前所有词之间计算 attention。换句话说，每次生成一个新词，都要让这个词关注之前所有的词。

### [57:43](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=3463s) · b000116

**English**

So the keys and the values, they're going to come up a lot. So every time you want to decode something, you need to attend to all other things, again and again. So we're going to see in, I think, next, lecture there's something called the KV cache, which basically saves the values of the keys and values. And one thing that we want is for that cache to not become too big.

**中文**

所以 key 和 value 会被反复用到。每次想要解码一些内容，都需要一遍又一遍地关注所有其他内容。我想下一讲会讲到一个叫键值缓存（KV cache）的东西，它基本上保存 key 和 value 的数值。而我们希望这个 cache 不要变得太大。

### [58:16](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=3496s) · b000117

**English**

So if you share projection matrices across heads, just allows you to save a little bit of space, a little bit of memory. That's the why. Does that roughly make sense?

**中文**

所以，跨 head 共享投影矩阵，就可以节省一点空间、一点内存。这就是原因。大致能理解吗？

### [58:33](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=3513s) · b000118

**English**

OK, cool. So speaking of that, there are some variations as to, I guess, just how many projection matrices to share. So you have the extreme example where all h heads, they all share the same projection matrices for v and k. And in that case, this method is called MQA, Multi-Query Attention.

**中文**

好，很好。说到这里，关于具体共享多少投影矩阵，也有一些变体。有一个极端情况，就是全部 h 个 head 都共享同一组 v 和 k 的投影矩阵。这种方法叫多查询注意力（Multi-Query Attention，MQA）。

### [59:04](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=3544s) · b000119

**English**

You have the in-between case where you share g, where g is the number of groups g projection matrices for v and k. And then you have groups of size, let's say, h over g. So this one is called Group Query Attention, GQA. And then you have the case that you are very familiar with from the transformer, which is every head has its own query projection, key projection, and value projection matrices.

**中文**

还有一种介于两者之间的情况，共享 g 组投影矩阵，g 是分组数量，也就是 v 和 k 分别有 g 个投影矩阵。每组的大小，比如说，是 h / g。这种叫分组查询注意力（Group Query Attention，GQA）\[字幕疑误，可能指 Grouped Query Attention\]。然后还有你在 transformer 中已经很熟悉的情况，就是每个 head 都有自己的 query 投影、key 投影和 value 投影矩阵。

### [59:45](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=3585s) · b000120

**English**

And this is the standard, multi-head attention.

**中文**

这就是标准的 multi-head attention。

### [59:53](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=3593s) · b000121

**English**

Cool. So I'm, going to just take a pause to see if what I mentioned makes sense. I'm going to soon transition it to Shervine. But before I do, I just want to make sure that what I discussed is making sense, roughly. Yeah.

**中文**

好。那么我先停一下，看看我刚才讲的是否清楚。我马上就要交给 Shervine。不过在这之前，我想确认一下，我讨论的内容大家大致能理解。对。

### [1:00:21](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=3621s) · b000122

**English**

So the question is, do we apply this to self-attention and cross-attention? I don't want to spoil the show. So I'm going to talk about something later on. But where is my trans? So if you take a look at the transformer architecture, we're going to see soon that what we care about most is what is in the decoder, because we actually forego of the encoder in nowadays' models. We have not seen this yet, but I'm just telling you.

**中文**

那么问题是，我们会把这个应用于自注意力（self-attention）和交叉注意力（cross-attention）吗？我不想提前剧透。所以我稍后会讲到一些内容。不过，我的 trans 在哪儿？\[字幕疑误，可能指 transformer\] 如果你看看 Transformer 架构，我们很快就会看到，我们最关心的是解码器（decoder）里的部分，因为如今的模型实际上舍弃了编码器（encoder）。我们还没有讲到这个，不过我先告诉大家。

### [1:00:52](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=3652s) · b000123

**English**

And so this typically comes into play for the masked self-attention in the decoder. But this technique can be applied in all attention layers. But I guess what I'm telling you is modern LLMs, their decoder only models which basically only have the decoder part of the transformer. We're going to see this in a second, which is the masked self-attention. So I'm not going to say too much because Shervine is going to cover that.

**中文**

所以，这通常会用在 decoder 中的掩码自注意力（masked self-attention）上。不过这项技术可以应用于所有注意力层。但我想说的是，现代的大语言模型（LLMs）是仅解码器（decoder-only）模型，基本上只有 Transformer 的 decoder 部分。我们马上就会看到，也就是 masked self-attention。所以我就不多说了，因为 Shervine 会讲这部分。

### [1:01:25](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=3685s) · b000124

**English**

But yeah, just a quick peek of what we're going to see. Cool, yeah.

**中文**

不过，对，这只是提前看一下我们接下来要讲的内容。好，对。

### [1:01:36](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=3696s) · b000125

**English**

Yeah.

**中文**

对。

### [1:01:41](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=3701s) · b000126

**English**

Great question. So the question is, when do you know which one you should use? I would say the choice is always driven by a few factors. One is how well it performs. Second is how much do you care about things like latency costs. And so it really depends how big is your model, how much you want to save on, let's say, compute, how is your input length, for instance if you have a shorter input length. So here what we want to do is to avoid having to do all these things for the whole o of n squared thing.

**中文**

好问题。那么问题是，你怎么知道应该用哪一种？我会说，选择始终由几个因素决定。一个是效果如何。第二个是，你有多在意延迟、成本之类的事情。所以，这确实取决于你的模型有多大，你想节省多少，比如计算量，以及你的输入长度是多少，比如输入长度比较短的情况。所以这里我们想做的，是避免为整个 O(n²) 的东西做所有这些事情。

### [1:02:15](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=3735s) · b000127

**English**

So I guess all of these come into play. So I would say it's not straightforward as to what the answer should be. But I would say a lot of recent models, they tend to share projection matrices. So typically, I would say GQA is what you would see. But it's not necessarily the case for all models.

**中文**

所以我想，这些因素都会起作用。因此我会说，答案并不直接。不过我会说，很多最近的模型倾向于共享投影矩阵（projection matrices）。所以通常来说，你会看到的是 GQA。但并非所有模型都是这样。

### [1:02:36](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=3756s) · b000128

**English**

Cool. We're running out of time. So I'm going to have Shervine here for the second part. Thank you. OK, great. Thank you, Afshine. So we're going to continue this lecture with some deeper dive into the kinds of models that we have in the transformer landscape. And then we're going to do a deep dive into one specific architecture that is very useful for classification settings. So first, we're going to come back to the architecture that we saw together last time, so this traditional encoder/decoder architecture where you have both components.

**中文**

好。时间快不够了。所以我请 Shervine 来讲第二部分。谢谢。好的，很好。谢谢你，Afshine。那么我们继续这节课，更深入地了解 Transformer 领域中的各种模型。接着，我们会深入研究一种对分类场景非常有用的特定架构。首先，我们回到上次一起看过的架构，也就是这种传统的 encoder/decoder 架构，其中两个组件都有。

### [1:03:19](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=3799s) · b000129

**English**

And so you have the original transformer paper from 2017 that had this architecture. But also later on, you see more architectures that built on top of it. So here we talk about the T5 family of models. So T5 is a paper that's an abbreviation of multiple Ts. So the first one is transfer, and then it's text-to-text, transformers.

**中文**

2017 年最初的 Transformer 论文采用的就是这个架构。不过后来，你也会看到更多在它的基础上构建的架构。这里我们要讲的是 T5 模型家族。T5 这篇论文的名字是多个 T 的缩写。第一个是 transfer，然后是 text-to-text、transformers。

### [1:03:49](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=3829s) · b000130

**English**

So this is where the T5 naming comes from. And then it's derived into multiple versions. So the T5 is like the vanilla paper. And then it had mT5. m stands for multilingual where there was some more work on the data it was trained on, as well as the vocabulary that it was computed over. And then you have ByT5, which is some of tokenizer-free method of all of this where you forego of the fact of tokenizing.

**中文**

这就是 T5 这个名字的来源。然后它又衍生出了多个版本。T5 就相当于最初的基础版论文。接着有了 mT5。m 代表多语言（multilingual），它对训练数据以及所用词表做了更多工作。然后还有 ByT5，它是这类方法中的一种免分词器（tokenizer-free）方法，舍弃了分词这一步。

### [1:04:26](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=3866s) · b000131

**English**

And instead of that, you basically operate at the byte level. So By is like byte. And basically, you have a vocabulary size that is much smaller. So instead of having an o of 30k, you have 2 to the power of 8. So a byte is 8 bits. And then you can represent every character into bytes. So that's what they do.

**中文**

取而代之的是，基本上直接在字节（byte）层面操作。所以 By 就像 byte。这样一来，词表大小就小得多。不是大约 O(30k)，而是 2 的 8 次方。一个字节是 8 位（bits）。然后你可以用字节表示每个字符。这就是他们的做法。

### [1:04:55](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=3895s) · b000132

**English**

OK, great. And then one thing I want to mention regarding the T5 family is that the objective function changes a bit with what the original transformer did. So the original transformer did next token prediction for the training task. But the T5 family, what they did is that they operated on the so-called span corruption task. So basically you would have your sentence as an input to the encoder.

**中文**

好的，很好。关于 T5 家族，我还想提一点，它的目标函数（objective function）与最初的 Transformer 有一些不同。最初的 Transformer 在训练任务中做的是下一个词元预测（next token prediction）。但 T5 家族采用的是所谓的片段破坏（span corruption）任务。基本上，你会把句子作为 encoder 的输入。

### [1:05:29](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=3929s) · b000133

**English**

And instead of putting everything to the encoder, you would leave blanks. And this is what we call span corruption. And then the span corruption could be one or multiple tokens missing. So if I want to give an example, so for example, my teddy bear is cute and reading. So you could have my teddy bear span corrupted, and is reading. So that could be one potential encoder input.

**中文**

但你不会把所有内容都放进 encoder，而是会留下一些空白。这就是我们所说的 span corruption。span corruption 可以是缺失一个或多个词元（tokens）。如果要举个例子，比如，我的泰迪熊很可爱，而且正在阅读。那么你可以有「我的泰迪熊」，接着一个被破坏的片段，再接「正在阅读」。这就是一种可能的 encoder 输入。

### [1:06:03](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=3963s) · b000134

**English**

And then you could have up to n--I mean, n is the parameterization of the number of spans that are corrupted. So you would have n such tokens here. And then the T5 families calls them sentinel tokens. So if you see sentinel tokens, they represent a span of corrupted tokens. So you have them here in the encoder. And then the decoder's work is to find each of these spans in series.

**中文**

然后你最多可以有 n 个——我是说，n 是被破坏片段数量的参数。所以这里会有 n 个这样的 token。T5 家族把它们称为哨兵词元（sentinel tokens）。因此，如果你看到 sentinel tokens，它们代表的是一段被破坏的 tokens。它们出现在 encoder 这里。而 decoder 的工作就是依次找出这些片段。

### [1:06:33](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=3993s) · b000135

**English**

So you start with a token that denotes the first corrupted span. And then you start the decoding process until it hits a prediction that predicts the next sentinel token up to the n plus 1, 1, where the tokens that are decoded between two consecutive sentinel tokens corresponds to the corrupted spans that are recovered. So these parentheses is basically a shift from the next token prediction objective function.

**中文**

所以，你从一个表示第一个被破坏片段的 token 开始。然后开始解码过程，直到它预测出下一个 sentinel token，一直到 n 加 1，1 \[字幕疑误，末尾的 1 可能重复\]。两个相邻 sentinel tokens 之间解码出来的 tokens，就对应于恢复出的被破坏片段。所以这段插话基本上是在说明，相对于 next token prediction 目标函数的一个变化。

### [1:07:08](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=4028s) · b000136

**English**

Yep.

**中文**

对。

### [1:07:27](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=4047s) · b000137

**English**

Yeah. So the question is, can you elaborate with the decoding process? So what you said regarding the reconstruction is exactly right. So you have sentinel tokens that denote some missing text. So what you want to decode is that missing text. So the decoder output will be exactly like each span reconstructed. And then if you want to know how training works, you do a teacher-forcing mechanism where you input everything in the decoder, and then try to reconstruct everything at once.

**中文**

对。那么问题是，能否详细解释一下解码过程？你关于重建所说的完全正确。sentinel tokens 表示一些缺失的文本。因此，你想解码出来的就是那些缺失文本。所以 decoder 的输出就是每个重建出来的片段。如果你想知道训练是如何进行的，会使用教师强制（teacher forcing）机制，把所有内容输入 decoder，然后尝试一次性重建全部内容。

### [1:08:00](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=4080s) · b000138

**English**

So any other questions?

**中文**

那么还有其他问题吗？

### [1:08:07](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=4087s) · b000139

**English**

Great.

**中文**

很好。

### [1:08:10](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=4090s) · b000140

**English**

And then now we're going to talk about another class of transformers where basically you have this encoder/decoder structure, where you just forget about the decoder and then just deal with the encoder. So you might tell me, OK, hey, you cannot do generation with this. And then I would respond to you, yes, that's exactly the point.

**中文**

现在我们要讲另一类 Transformer，基本上你有这种 encoder/decoder 结构，但把 decoder 舍弃，只处理 encoder。你可能会跟我说，好吧，嘿，这样没法做生成。而我会回答你，对，这正是它的用意。

### [1:08:37](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=4117s) · b000141

**English**

So it has encoder representations that can be used for tasks that might be more geared towards classification. So sentiment extraction, token classification, all of these things that used to be done with specific language models, they can be done with the encoder part of the transformer. And we're going to dive deeper a bit later into a three-key encoder only models. So BERT, which is like the central one, I would say in this landscape, and then two other architectures, DistilBERT and RoBERTa, that are investigating on axis of improvements.

**中文**

它提供 encoder 表示，可以用于更偏向分类的任务。比如情感提取（sentiment extraction）、词元分类（token classification），这些过去使用特定语言模型完成的任务，都可以用 Transformer 的 encoder 部分来做。稍后，我们会进一步深入了解三个关键的仅编码器（encoder-only）模型。BERT，我会说它是这个领域的核心模型；还有另外两种架构，DistilBERT 和 RoBERTa，它们探索了不同的改进方向。

### [1:09:20](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=4160s) · b000142

**English**

So it's going to be good to see. So OK, great. And then there is one last class. So as Afshine just mentioned, two days LLMs, they remove the encoder part altogether. And then when you have no encoder, you don't have your encoder embeddings at the end of your stacked encoders that could be fed to the cross-attention. So this module disappears altogether.

**中文**

所以看一看会很有帮助。好的，很好。还有最后一类。正如 Afshine 刚刚提到的，two days LLMs \[字幕疑误，可能指 today's LLMs，即如今的 LLMs\] 完全移除了 encoder 部分。没有 encoder，就不会有堆叠的 encoders 末端产生的编码器嵌入（encoder embeddings）可以输入 cross-attention。所以这个模块也完全消失了。

### [1:09:52](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=4192s) · b000143

**English**

So each decoder that is stacked just has masked self-attention and an FFN as part of it. And yeah, that's basically something that has caught up since then. Because when you look at the popularity of each of these models, so you used to have these transformer-like architecture that was popular towards the beginning, where the main hypothesis was that the encoder part is very useful for getting to the decoder's representation.

**中文**

因此，堆叠起来的每个 decoder 内部只有 masked self-attention 和一个前馈网络（FFN）。对，这基本上是后来流行起来的做法。因为如果看看这些模型各自的流行程度，早期流行的是这种类似 Transformer 的架构，当时的主要假设是，encoder 部分对于获得 decoder 的表示非常有用。

### [1:10:28](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=4228s) · b000144

**English**

But as time went, people realized that your compute budget could be best invested in the decoder only. And then there has been more investment into the kind of tasks that is, I would say, easiest to scale up and generalize-- next-word prediction--as opposed to the task I just mentioned for T5, which might be more bespoke. So you need to corrupt things.

**中文**

但随着时间推移，人们意识到，计算预算最好只投入 decoder。随后，更多投入转向了我认为最容易扩展和泛化的任务——下一个词预测（next-word prediction）——相较之下，我刚刚提到的 T5 任务可能更需要专门设计。你需要破坏一些内容。

### [1:10:59](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=4259s) · b000145

**English**

So it's more complex. Whereas next-word prediction is, I would say, the simplest thing you can do. And it proved to be wonders and well-aligned with the task of being a helpful kind of chatbot, which is like two days' applications mainly. And then the decoder-only architectures-- so I'm not going to talk about them today. But it's going to be the central part of the next lectures when we're going to talk about LLMs more and more.

**中文**

所以它更复杂。而 next-word prediction 可以说是你能做的最简单的事情。事实证明，它的效果非常出色，而且与充当有帮助的聊天机器人的任务很契合，而这基本上就是 two days 的应用 \[字幕疑误，可能指 today's applications，即如今的应用\]。至于 decoder-only 架构，我今天不会讲。不过，它会成为接下来几节课的核心内容，届时我们会越来越多地讨论 LLMs。

### [1:11:35](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=4295s) · b000146

**English**

OK, awesome. So now we can dive deep, as promised, into encoder-only architectures and with BERT. So first we're going to start by seeing what does BERT mean. So BERT, it's an acronym that denotes Bidirectional Encoder Representations from Transformers. And we're going to see together how does each section of this acronym, what does it correspond to?

**中文**

好的，太好了。现在我们可以按之前说的，深入了解 encoder-only 架构以及 BERT。首先，我们来看 BERT 是什么意思。BERT 是一个缩写，表示来自 Transformers 的双向编码器表示（Bidirectional Encoder Representations from Transformers）。我们会一起看看，这个缩写的各个部分分别对应什么。

### [1:12:08](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=4328s) · b000147

**English**

So let's just start with the encoder part, which is the easiest to grasp. So as we said, we just dropped the decoder. So this encoder from transformer is basically exactly what it means. Now on the other part, so why do we talk about bidirectionality? So it's a way, so the paper's result is remarkable, because we are able from a given input to get output representations that have attended to everything for each token.

**中文**

先从 encoder 部分开始，这最容易理解。正如我们所说，我们只是去掉了 decoder。因此，来自 Transformer 的这个 encoder，基本上就是字面意思。现在看另一部分，为什么我们会谈到双向性（bidirectionality）？这是因为，这篇论文的结果很出色：给定一个输入，我们能够得到输出表示，其中每个 token 都关注了所有内容。

### [1:12:51](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=4371s) · b000148

**English**

And this is the case. Because since we only have the encoder, we have this self-attention layer that truly attends to every other token. And this is in contrast with the masked self-attention that you have where we said that the mask is making the attention mechanism causal. So every token can attend to itself and to the tokens before it. And this is, by the way, something that the authors discuss a lot in the paper, saying that GPT came out, GPT they're not truly bidirectional.

**中文**

情况确实如此。因为我们只有 encoder，所以这个 self-attention 层确实会关注其他每一个 token。这与 masked self-attention 不同，我们说过，其中的掩码（mask）让注意力机制具有因果性（causal）。所以每个 token 可以关注自身以及它之前的 tokens。顺便说一下，这也是作者在论文中大量讨论的内容，他们说 GPT 出来了，但 GPT 并不是真正双向的。

### [1:13:30](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=4410s) · b000149

**English**

And then these encodings that can be used for classification tasks, they truly are. Any questions? Yep.

**中文**

而这些可以用于分类任务的编码，确实是双向的。有问题吗？对。

### [1:13:50](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=4430s) · b000150

**English**

Yep, that's right. So the question is, when you don't have the mask, each token can attend to each other. That's exactly right. And then the mask is exactly there to prevent links from tokens to those that come after them. Yeah. OK, great. So I just want to put this paper in context. And the field of NLP was booming back then. So you had another landmark paper that same year, which was called ELMo, so Embeddings from Language Models.

**中文**

对，没错。那么问题是，没有 mask 时，每个 token 都可以关注其他每个 token。完全正确。mask 的作用恰恰就是阻止 tokens 与它们之后的 tokens 建立连接。对。好的，很好。我想介绍一下这篇论文的背景。当时自然语言处理（NLP）领域正蓬勃发展。同一年还有另一篇里程碑式的论文，叫 ELMo，也就是来自语言模型的嵌入（Embeddings from Language Models）。

### [1:14:24](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=4464s) · b000151

**English**

And I would say that the timing of that paper was a bit unfortunate, because it truly had new insights of also building bidirectional representations. But it just turns out that it came the same year as the transformer, as the kind of transformer-based same line of work. So it got a bit masked by it. So ELMo, just to give the main lines, it was based on a bidirectional LSTM where you had multiple layers, each stacked on top of each other.

**中文**

我会说，那篇论文发表的时机有点不巧，因为它确实在构建双向表示方面提出了新的见解。但恰好它与 Transformer，与这类基于 Transformer 的同一研究路线，出现在同一年。所以它有点被掩盖了。简单介绍一下 ELMo 的主要思路，它基于双向长短期记忆网络（bidirectional LSTM），包含多个彼此堆叠的层。

### [1:15:01](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=4501s) · b000152

**English**

And basically you were able to build a bidirectional representation for each word, thanks to this architecture. And so why didn't it become as popular as BERT? It's because you had the same downsides as the previous models, where basically it's hard to scale because of this recurrence. And I think a lot of you, when you think about ELMo and BERT, you don't think about these papers at first, because they are characters in Sesame Street.

**中文**

基本上，借助这种架构，你可以为每个词构建双向表示。那么，为什么它没有像 BERT 那么流行呢？因为它有之前模型同样的缺点，基本上由于这种循环性（recurrence），很难扩展。我想，你们很多人在想到 ELMo 和 BERT 时，首先想到的不是这些论文，因为它们是《芝麻街》（Sesame Street）里的角色。

### [1:15:40](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=4540s) · b000153

**English**

And I grew up in a place where I did not know about Sesame Street. So for me, ELMo and BERT is like paper names. But it might be what represents to you at first. So I thought that was quite funny. And then researchers, they are generally quite playful. They try to fit their acronyms into themes. So if you look at paper names, you will get entertained.

**中文**

我长大的地方不认识《芝麻街》。所以对我而言，ELMo 和 BERT 就是论文的名字。但对你们来说，首先想到的可能是那些角色。所以我觉得这挺有趣。研究人员通常也挺爱玩。他们会尝试让缩写符合某个主题。所以如果你看看论文名字，会觉得挺有意思。

### [1:16:11](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=4571s) · b000154

**English**

OK, great. So to dive deeper into what I mentioned to be the goal of encoder-only models, so you have your set of tokens as input. And the goal here is to perform tasks that might be focused on projecting some representation somewhere, so typically classification tasks. And here, the way BERT works is very specific. So you have two kinds of tokens that you will see are structural here.

**中文**

好的，很好。为了深入了解我刚才提到的 encoder-only 模型的目标，你有一组 tokens 作为输入。这里的目标是执行一些任务，这些任务可能侧重于把某种表示投影到某个地方，通常就是分类任务。而 BERT 在这里的工作方式很具体。你会看到，这里有两类具有结构性作用的 tokens。

### [1:16:46](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=4606s) · b000155

**English**

So you have first the CLS token, which stands for classification. And it's basically a placeholder token that is put at the beginning of the sequence that will then, at the end of the whole attention and then projection and the whole encoder mechanism, be projected into an embedding that we can then use for classification. So CLS is just some kind of placeholder that will carry the bidirectional information of your whole input.

**中文**

首先是 CLS token，CLS 代表分类（classification）。它基本上是放在序列开头的占位 token，经过整个注意力、投影以及整个 encoder 机制之后，最终会被投影成一个可以用于分类的嵌入（embedding）。所以 CLS 就是某种占位符，用来承载整个输入的双向信息。

### [1:17:23](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=4643s) · b000156

**English**

And another token that might be useful to see is this SEP token. So it's like separator. And then you will see very soon we're going to see the objective functions that it operates on. It aims at separating two sentences. Yeah. So this is the very high level. And then so one thing that is very interesting to see with this model is that you have this concept of multi-stage training.

**中文**

另一个值得了解的 token 是这个 SEP token。它就像分隔符（separator）。我们很快就会看到它所对应的目标函数。它的目的是分隔两个句子。对。这就是非常概括的介绍。这个模型还有一点非常值得关注，就是它有多阶段训练（multi-stage training）这个概念。

### [1:17:56](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=4676s) · b000157

**English**

So you don't train the model in one shot. You do it in multiple stages. So the first stage is aimed at being aligned with the task of interest. And so this is what we call pre-training. And this pre-training, we will see in detail, is done with two objective functions that are respectively MLM and NSP. So MLM stands for Masked Language Model. And NSP is the Next Sentence Prediction.

**中文**

你不是一次性完成模型训练，而是分多个阶段进行。第一阶段的目的是与目标任务对齐。这就是我们所说的预训练（pre-training）。我们会详细看到，这种 pre-training 使用两个目标函数，分别是 MLM 和 NSP。MLM 代表掩码语言模型（Masked Language Model），NSP 则是下一句预测（Next Sentence Prediction）。

### [1:18:30](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=4710s) · b000158

**English**

So masked language model, it's a way for the model to learn the internal structure of the inputs. And then NSP, it might be seen as a way to see if the ordering of sentences makes sense. So we're going to go a bit deeper into each, but it's a combination of objective function that the authors assumed to be helpful for learning general embeddings of high quality.

**中文**

masked language model 是让模型学习输入内部结构的一种方式。而 NSP 可以看作一种判断句子顺序是否合理的方式。我们会分别深入了解一下，不过，这是作者假设有助于学习高质量通用 embeddings 的一组目标函数。

### [1:19:03](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=4743s) · b000159

**English**

OK. So the second thing that I want to mention is that, once you have all of this, you have a further stage where you keep the embeddings that you have learned. And then you attach to it some other network, like typically a linear projection, to then fine tune the embeddings that you have learned into some target task. So this is what we call fine tuning. Yep.

**中文**

好。我想提到的第二点是，当你完成这些之后，还会有进一步的阶段，保留已经学到的 embeddings。然后在它上面接入另一个网络，通常是线性投影（linear projection），把学到的 embeddings 针对某个目标任务进行微调（fine-tuning）。这就是我们所说的 fine-tuning。对。

### [1:19:46](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=4786s) · b000160

**English**

So yeah. So the question is, do we still have just an encoder here? Because a next-sentence prediction could be seen as a decoder task. So actually I'm going to go in detail. The next-sentence prediction task is actually us putting two sentences, one after the other, and predicting whether they are truly consecutive. So it's a classification task. Yeah, great point. And yeah, we're going to see that in detail very soon.

**中文**

对。那么问题是，这里依然只有一个 encoder 吗？因为 next-sentence prediction 看起来可能是 decoder 的任务。实际上，我马上会详细解释。next-sentence prediction 任务其实是把两个句子一前一后放在一起，预测它们是否真的连续。所以这是一个分类任务。对，这一点提得很好。我们很快就会详细看到。

### [1:20:17](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=4817s) · b000161

**English**

So before we see that in detail, I'm going to discuss the pros and cons that this method usually has. So regarding on the pro side, this pre-training mechanism can be done on fairly unlabeled data. So you still have this next-sentence prediction task. But this is something that you control, because you know which sentences follow each other. So it's something that you know it's self-supervised.

**中文**

在详细介绍之前，我会讨论一下这种方法通常具有的优点和缺点。优点方面，这种 pre-training 机制可以在基本没有标注的数据上完成。你仍然有这个 next-sentence prediction 任务。但这是你可以控制的，因为你知道哪些句子彼此相接。所以你知道，这是自监督的（self-supervised）。

### [1:20:51](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=4851s) · b000162

**English**

And the masked language model task, we're going to see how it consists. But it's also something that is unsupervised. So this is a very interesting way to learn interesting embeddings out of unlabeled data. And then in practice is that we see that these unlabeled data leads to helpful representations being learned. And then you need very little data to build on top of it. So at the fine tuning stage, you just start from these very nice embeddings that you have learned, and you just have a few weights to tune.

**中文**

至于 masked language model 任务，我们会看到它的具体内容。但它也是无监督的（unsupervised）。所以，这是一种从无标注数据中学习有意思的 embeddings 的非常有趣的方法。实际中，我们看到这些无标注数据能让模型学到有用的表示。然后，你只需要很少的数据就能在此基础上继续构建。因此，在 fine-tuning 阶段，你从已经学到的这些很好的 embeddings 出发，只需要调整少量权重。

### [1:21:30](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=4890s) · b000163

**English**

And then this usually leads to a performance that exceeds state of the art back then. And then regarding the downsides, we have of course all the text generation tasks that are out of reach because we don't have a decoder. And also, we can see these two stage process and the fact that we need to further tune embeddings as something that can be over hurdled. So it might be, when you compare this kind of methodology with respect to more traditional methods, that can be one shot.

**中文**

这通常能带来超越当时最先进水平（state of the art）的表现。至于缺点，当然，由于没有 decoder，所有文本生成任务都做不了。此外，这个两阶段过程，以及我们需要进一步调整 embeddings 这一点，也可以被看作一种 over hurdled \[字幕疑误，可能指额外障碍或负担\]。也就是说，与一些可以一次完成的更传统的方法相比，这种方法可能存在这样的问题。

### [1:22:08](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=4928s) · b000164

**English**

This could be seen as a downside. OK, great. And I have some names regarding variants here. We're going to dive deep into two of them a bit later on.

**中文**

这可以被看作一个缺点。好的，很好。这里我列了一些变体的名字。稍后我们会深入了解其中两个。

### [1:22:24](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=4944s) · b000165

**English**

OK. So I want us to focus on the original transformer. And we're going to go step by step into what happened to it, and then how we get the BERT architecture. So this is what we had in the original transformer paper that we saw last week. And what BERT did is extract the encoder part of it and attach basically these new objective functions that I just mentioned, alongside some new set of tricks when it comes to representing tokens.

**中文**

好。我想让大家关注最初的 Transformer。我们会一步一步看它发生了哪些变化，以及我们如何得到 BERT 架构。这就是上周我们在最初的 Transformer 论文中看到的内容。而 BERT 所做的，是提取其中的 encoder 部分，基本上接上我刚才提到的这些新目标函数，同时在表示 tokens 方面采用一些新的技巧。

### [1:23:00](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=4980s) · b000166

**English**

So I think we're going to go through them one by one. So first of all, one interesting note is that it uses a specific tokenizer called WordPiece. So you can see it as a tokenizer that learns on your training set, based on merge rules that maximize the likelihood. So basically, you have some huge training set, and you train a tokenizer that merges atomic tokens together to build your target vocabulary.

**中文**

我想我们会逐一讲解。首先，有趣的一点是，它使用一种名为 WordPiece 的特定分词器（tokenizer）。你可以把它看成一种在训练集上学习的 tokenizer，所依据的合并规则会使似然（likelihood）最大化。基本上，你有一个庞大的训练集，然后训练一个 tokenizer，把原子 tokens 合并起来，构建目标词表。

### [1:23:38](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=5018s) · b000167

**English**

And some order of magnitude, I mentioned o of 30k. So it's typically, I think this is the size that they chose in this paper. And in general, like vocabulary sizes in these sorts of paper are in the order of magnitude of 10 to the power of 4, 10 to the power of 5, except for our token-free method that we saw, like ByT5, which is like this very restricted set of tokens, like 2 to the power of 8, which is 256. Apart from this specific case, you always have this order of magnitude.

**中文**

关于数量级，我提到了 O(30k)。通常，我想这就是他们在这篇论文中选择的大小。一般来说，这类论文中的词表大小在 10 的 4 次方、10 的 5 次方这个数量级，除了我们看到的免 token 方法，比如 ByT5，它的 tokens 集合非常有限，比如 2 的 8 次方，也就是 256。除了这个特例，通常都是这个数量级。

### [1:24:18](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=5058s) · b000168

**English**

And basically, we are going to make use of the tokens that I mentioned. Like at the beginning, so you have the CLS token that is going to carry the bidirectional representation of all your sequence. And then you have SEP tokens to separate the two sentences towards the next-sentence prediction task. And there is something that I haven't talked about just yet. So I think maybe we can talk about it at the time of the deep dive.

**中文**

基本上，我们会使用我提到的那些 tokens。比如，在开头放 CLS token，它会承载整个序列的双向表示。然后，用 SEP tokens 分隔两个句子，以进行 next-sentence prediction 任务。还有一点我暂时没讲到。我想，也许可以在深入讲解时再讨论。

### [1:24:53](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=5093s) · b000169

**English**

So in order to have this masked language model task, so of course you need to mask some tokens. So we're going to see the technique that is basically applying these sorts of mask and where and at which frequency. And we're going to see with respect to the output what is going to be our task based on the resulting representation. So I'm just going to pass quickly on it here, but we're going to come back very soon.

**中文**

为了开展这个 masked language model 任务，当然需要遮蔽一些 tokens。所以，我们会看到这类 mask 的具体应用方法，放在哪里，以及以什么频率应用。我们也会从输出的角度来看，基于得到的表示，我们的任务是什么。这里我先快速略过，不过很快就会再回来讲。

### [1:25:24](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=5124s) · b000170

**English**

OK, great. So one big piece of news regarding your input embeddings--so what stays the same? So you still have these huge dictionary lookup of embeddings for each token that you're going to learn. And you're going to additively add the positional encoding that we saw at last lecture. And Afshine talked about earlier in this lecture, which can either be hard-coded or learned.

**中文**

好的，很好。关于输入 embeddings，有一个很大的新变化——那么哪些保持不变？你仍然有庞大的 embedding 字典查找，为每个 token 提供要学习的 embedding。然后，你会把我们上节课看到的、Afshine 在本节课前面也讲过的位置编码（positional encoding）加上去，它既可以是硬编码的，也可以是学习得到的。

### [1:25:56](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=5156s) · b000171

**English**

I think the authors here just used a hard-coded version here, but I'm not too sure. But it's roughly the same performance usually. But there is something new. There is the introduction of a new kind of encoding called segment encoding that is going to still be additively added to tokens, with the exception that we just have two possible encodings there.

**中文**

我想这里的作者用的是硬编码版本，但我不太确定。不过通常性能大致相同。但这里有个新东西。它引入了一种新的编码，叫分段编码（segment encoding），仍然会以相加的方式加到 tokens 上，区别在于这里只有两种可能的编码。

### [1:26:26](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=5186s) · b000172

**English**

So you have segment A that represents the first sentence, and then segment B that represents the second sentence. And it's supposed to help with the NSP task to represent what could be features that can helpfully represent a sentence that precedes another one. So at least that was the hypothesis admitted by the authors. We're going to see it has been challenged later on. But this is one of the key concepts that was introduced here.

**中文**

segment A 表示第一个句子，segment B 表示第二个句子。它的设想是帮助 NSP 任务，表示那些可能有助于刻画一个句子先于另一个句子的特征。至少这是作者采用的假设。我们会看到，后来这个假设受到了质疑。不过，这是这里引入的关键概念之一。

### [1:26:59](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=5219s) · b000173

**English**

Any questions so far? Yep.

**中文**

到目前为止有问题吗？对。

### [1:27:28](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=5248s) · b000174

**English**

Yep, so a great point. So the question is, what does segment encoding do at all? So it's basically something that is learned. So you have two indices, two basically embeddings that you can learn. You just additively add them, segment A for tokens in the first part of the sentence, and then segment B in the second part. And you just learn it with gradient descent. So you do nothing with it. I think there was another question here? Yeah.

**中文**

对，这一点很好。那么问题是，segment encoding 到底有什么作用？它基本上是学习出来的。你有两个索引，基本上就是两个可以学习的 embeddings。你只需把它们加上去，句子第一部分的 tokens 加 segment A，第二部分加 segment B。然后通过梯度下降（gradient descent）学习它。你不需要对它做什么。我想这边还有一个问题？对。

### [1:28:07](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=5287s) · b000175

**English**

That's right. So the question is, is every token in the same sentence going to have the same segment encoding? Yes, yeah. OK, awesome. So I'm seeing I might need to speed up a tiny bit. So yeah, the second thing that I want to highlight here is that we take the encoder part of the transformer. And nothing new here. It's just the same. We have self-attention, followed by these FFN.

**中文**

没错。那么问题是，同一句子中的每个 token 都会具有相同的 segment encoding 吗？是的，对。好的，太好了。我发现我可能需要稍微加快一点。第二点我想强调的是，我们采用了 Transformer 的 encoder 部分。这里没有新东西，完全一样。我们有 self-attention，后面接这些 FFN。

### [1:28:37](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=5317s) · b000176

**English**

So this is where you're going to get your bidirectional nature of your encodings. And then basically we're assuming that training both MLM and NSP on it is going to help us learn helpful projection matrices in this encoder that can be suited for any classification task.

**中文**

编码的双向性质就是从这里获得的。基本上，我们假设，同时使用 MLM 和 NSP 进行训练，会帮助我们在这个 encoder 中学到有用的 projection matrices，使其适用于任何分类任务。

### [1:29:01](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=5341s) · b000177

**English**

OK, great. And as promised, I talked about detailing more about what this MLM task was going to do. So when you look at the input, you're going to basically have your input sentence, and replace at random some tokens. So it will be replaced either with the token mask. So it's in 80% of the time. In 10% of the time, the tokens selected for this MLM objective function are not going to be replaced at all.

**中文**

好的，很好。按照之前说的，我要更详细地讲一下这个 MLM 任务会做什么。看输入时，你基本上会有一个输入句子，然后随机替换一些 tokens。可能会替换为 mask token，这种情况占 80%。有 10% 的情况下，为这个 MLM 目标函数选中的 tokens 完全不会被替换。

### [1:29:39](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=5379s) · b000178

**English**

So we're just saying, it's the same token, just predict the same token. And then 10% of the time, it's going to be changed to some random other word. So at the end of it, you have the subset of tokens you're going to perform your MLM task on. And then this is how it's composed. OK, great. And so basically the intuition here is that when you want to predict what a token is, you need to know about its context.

**中文**

我们相当于在说，它还是同一个 token，只要预测这个相同的 token。还有 10% 的情况下，它会被换成某个随机的其他词。最终，你会得到一个用于执行 MLM 任务的 token 子集。这就是它的组成方式。好的，很好。这里的直觉基本上是，要预测一个 token 是什么，你就需要了解它的上下文。

### [1:30:10](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=5410s) · b000179

**English**

So we're going to force the model to learn about what surrounds it, left and right. So this is the bidirectional property of this architecture put into action.

**中文**

所以，我们会迫使模型学习它左右两侧周围的内容。这就是这种架构的双向性质实际发挥作用的地方。

### [1:30:24](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=5424s) · b000180

**English**

OK, great. And now we're going to talk about the next-sentence prediction task where basically the process here is to select two sentences from a given corpus, and then present them side by side in order 50% of the time, and in some random order the other part of the time. And the goal is for some classification head on top of the CLS token to determine whether A and B are consecutive.

**中文**

好的，很好。现在我们要讲 next-sentence prediction 任务。基本过程是从给定语料库中选择两个句子，50% 的情况下把它们按顺序并列呈现，其余时候则以某种随机顺序呈现。目标是在 CLS token 之上使用一个分类头（classification head），判断 A 和 B 是否连续。

### [1:30:58](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=5458s) · b000181

**English**

So that's all it does. And so the assumption is that it also helps learn some useful embeddings.

**中文**

这就是它所做的全部事情。这里的假设是，它也有助于学到一些有用的 embeddings。

### [1:31:09](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=5469s) · b000182

**English**

OK, great. And here I'm going to present the notation that is used in the paper. So the paper is something I recommend reading. It's a very nice read, alongside the "Attention is All You Need." I would say it's a landmark paper. I think it has a 170k citations, something really impressive. And basically what we called n in the original transformer paper is now called L. H, that was called d model, is the dimension of our embeddings.

**中文**

好的，很好。这里我会介绍论文中使用的符号。我推荐大家阅读这篇论文。它非常值得读，《Attention is All You Need》也是。我会说，这是一篇里程碑式的论文。我想它有 170k 次引用，确实令人印象深刻。基本上，我们在最初的 Transformer 论文中称为 n 的量，现在称为 L。H，也就是之前称为 d model 的量，是 embeddings 的维度。

### [1:31:43](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=5503s) · b000183

**English**

And A is the number of attention heads, which was called the little h. So here I'm just showing these new notations for information, just to give you the mapping. But of course, together with Afshine, we're going to stay consistent with the original notations we had, so just like for information. And one interesting note is that you will see that the BERT model, when you look at some repository of models such as Hugging Face, so usually it's given in several versions.

**中文**

A 是注意力头（attention heads）的数量，之前称为小写 h。这里展示这些新符号只是供参考，给大家说明一下对应关系。当然，我和 Afshine 会继续沿用原来的符号，保持一致，所以这里只是提供信息。还有一点有趣的是，当你在 Hugging Face 这样的模型仓库中查看 BERT 模型时，通常会发现它有多个版本。

### [1:32:17](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=5537s) · b000184

**English**

So you will see sometimes like case, uncased. So this denotes what kind of preprocessing was done to the data, whether you only have lowercase words in there or whether casing matters. So based on your task of interest, it might be one thing you want to choose from. OK, great. And I give some orders of magnitude from the paper on what values were chosen for each of these.

**中文**

有时你会看到 case、uncased 这样的名称 \[字幕疑误，case 可能指 cased\]。这表示对数据进行了哪种预处理，是只包含小写词，还是会区分大小写。所以根据你关心的任务，这可能是一个需要选择的方面。好的，很好。我还给出了论文中为这些量选择的数值的大致数量级。

### [1:32:51](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=5571s) · b000185

**English**

So if I remember correctly, I think the original transformer had 12 stacked encoders and decoders. So I think some numbers here were taken from there.

**中文**

如果我没记错，我想最初的 Transformer 有 12 个堆叠的 encoders 和 decoders。所以我想，这里的一些数字就是取自那里。

### [1:33:08](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=5588s) · b000186

**English**

So yeah, order of magnitude is 100 million parameters.

**中文**

所以，对，数量级是 1 亿个参数。

### [1:33:16](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=5596s) · b000187

**English**

Any questions so far?

**中文**

到目前为止有问题吗？

### [1:33:21](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=5601s) · b000188

**English**

OK, great. And then now we're going to talk about the fine-tuning stage where the goal is to basically take whatever we have learned at pre-training stage, and then freeze those weights. And instead of training again on those same weights, you have some classification linear layer that is put on top of either the CLS token or on top of tokens of interest. And you're going to learn about the linear embeddings there.

**中文**

好的，很好。现在我们要讲 fine-tuning 阶段，目标基本上是拿来 pre-training 阶段学到的内容，然后冻结那些权重。不再重新训练同样的权重，而是在 CLS token 或你关心的 tokens 之上放一个用于分类的线性层。然后，你会学习那里的线性 embeddings。

### [1:33:54](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=5634s) · b000189

**English**

So you're going to have some classification task. So you could either freeze all these pre-trained weights and just train on these small weights. Or you can just retrain the whole thing. I think there is multiple classification schemes. And some of it will be influenced by your willingness to retrain a lot of the network and how different the classification task is with respect to the original pre-training task.

**中文**

你会有一个分类任务。你既可以冻结所有这些预训练权重，只训练这些少量权重，也可以重新训练整个模型。我想有多种分类方案。其中一些选择会受到这些因素的影响：你愿意重新训练多大一部分网络，以及分类任务与原始 pre-training 任务有多大不同。

### [1:34:23](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=5663s) · b000190

**English**

OK, great. And then just to give some examples of what could be fine-tuning tasks for tasks of interest, you can have a sentiment extraction where you build a classification layer on top of the CLS token. And we give some other example question answering where basically you are given some input. And the goal of the model is to detect beginning and end spans of the response. So it's basically some objective function that is at the token level.

**中文**

好的，很好。举几个目标任务的 fine-tuning 例子，可以做 sentiment extraction，在 CLS token 上面构建一个分类层。我们还给出了其他例子，比如问答（question answering），基本上给你某个输入，模型的目标是检测回答片段的起点和终点。所以它基本上是 token 级别的某种目标函数。

### [1:34:59](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=5699s) · b000191

**English**

OK, great. So now I propose that we do some deep dive into one specific example. Our favorite example, this teddy bear is so cute. Let's just see how BERT works in practice. So basically what you would do in an uncased setting is take the sentence, pre-process it, just put everything lowercase. Then you apply the WordPiece algorithm on whatever tokenization mechanism that your tokenizer has learned.

**中文**

好的，很好。现在我建议深入看一个具体例子。我们最喜欢的例子，这只泰迪熊太可爱了。来看看 BERT 实际上是如何工作的。基本上，在 uncased 设置下，你会取这个句子，进行预处理，把所有内容都转成小写。然后，基于 tokenizer 学到的分词机制，应用 WordPiece 算法。

### [1:35:38](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=5738s) · b000192

**English**

So for example here, apparently it had all these merge rules. So this is the tokens that appear in the vocabulary. And then as I promised, we add the CLS token at the beginning. And then we add the SEP token. And you also have this PAD tokens that are basically used to fill out the sequence until the end. Because when you train, you train by batch, and then batches are composed of matrices that have a fixed length.

**中文**

比如这里，显然它学到了所有这些合并规则。所以这些就是出现在词表中的 tokens。然后，正如我之前说的，在开头加上 CLS token。接着加上 SEP token。还有这些 PAD tokens，基本上用于把序列填充到末尾。因为训练时是按批次（batch）进行的，而批次由长度固定的矩阵组成。

### [1:36:13](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=5773s) · b000193

**English**

Yeah. So let's just have this deep dive a bit the same as what we had in the transformer deep dive last time. So you have the embeddings that are learned. So it's some huge lookup table between the index of each token and the learned representation. So you add to it the position embedding of the token. And something that's new here--the segment embedding. So exactly as we said, it's an embedding that is added to each token.

**中文**

对。我们就像上次深入讲解 Transformer 时一样，来深入看一看。这里有学习得到的 embeddings。它是一个庞大的查找表，把每个 token 的索引对应到学到的表示。你会加上 token 的位置嵌入（position embedding）。这里还有一个新东西——分段嵌入（segment embedding）。就像我们说的，它是一个加到每个 token 上的 embedding。

### [1:36:47](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=5807s) · b000194

**English**

And the same embedding is added to the same tokens. So all the tokens have the same segment A. Then some other embedding B is added to all the tokens of the segment B. OK, great. So now you have, similarly as the transformer, something that is position-aware and context-aware--so not context-aware just yet, but segment-aware here. OK, great. And basically it goes through this encoder architecture.

**中文**

相同的 embedding 会加到相同的 tokens 上。所以所有这些 tokens 都有相同的 segment A。然后，另一个 embedding B 会加到 segment B 的所有 tokens 上。好的，很好。现在，类似 Transformer，你得到了具有位置感知和上下文感知能力的东西——还没有上下文感知，不过这里已经有分段感知了。好的，很好。基本上，它会经过这个 encoder 架构。

### [1:37:22](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=5842s) · b000195

**English**

And then at the end of it, for the case of sentiment extraction, we do not care about the embeddings that are corresponding to each token that is not the CLS token. Because what we care about is the output embedding of the CLS token, where we plug a linear layer that will learn some classification task.

**中文**

然后，在最后，对于 sentiment extraction，我们不关心除 CLS token 以外的各个 token 对应的 embeddings。因为我们关心的是 CLS token 的输出 embedding，在它上面接一个线性层，用来学习某个分类任务。

### [1:37:50](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=5870s) · b000196

**English**

So any question here?

**中文**

这里有问题吗？

### [1:37:55](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=5875s) · b000197

**English**

So does the fact that we drop all the output embeddings, apart from the CLS token, make sense? Yeah, yep.

**中文**

所以，除了 CLS token 之外，我们舍弃所有输出 embeddings，这一点大家能理解吗？对，嗯。

### [1:38:21](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=5901s) · b000198

**English**

Yeah, so the question is, what does this FFN, is that right? What does this FFN correspond to? So basically you have a map between the dimension of the output embedding and your task of interest. So it might be classification of either positive or negative. So you have some hidden layer with some length. So you have typically two matrices to learn the projection from one to that hidden layer, and then the hidden layer to the output.

**中文**

对，那么问题是，这个 FFN 是什么，对吗？这个 FFN 对应什么？基本上，你有一个从输出 embedding 的维度到目标任务的映射。比如，它可以是正面或负面的分类。你有一个具有某种宽度的隐藏层（hidden layer）。通常会用两个矩阵，学习从输入到那个隐藏层，再从隐藏层到输出的投影。

### [1:38:51](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=5931s) · b000199

**English**

And then you learn these weights in order to do the classification task, based on the embeddings that it has learned here.

**中文**

然后，基于这里学到的 embeddings，学习这些权重，以完成分类任务。

### [1:38:59](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=5939s) · b000200

**English**

Yeah, great question. So that was the question I was waiting for. So the question is, why do we throw away all these other output embeddings? So we don't need them here. So we are in a classification task. We have put as convention to operate on top of some token, like the CLS token. And then the magic of this token is that all these self-attention mechanisms that are in the encoder has mixed the representation of each of the other tokens in that representation, such that the output embeddings, they are context-aware.

**中文**

对，好问题。这正是我在等的问题。那么问题是，为什么我们要丢弃其他所有输出 embeddings？这里不需要它们。我们正在做一个分类任务。我们约定在某个 token，比如 CLS token，之上进行操作。这个 token 的神奇之处在于，encoder 中的所有这些 self-attention 机制已经把其他各个 token 的表示混合到了这个表示中，因此输出 embeddings 具有上下文感知能力。

### [1:39:39](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=5979s) · b000201

**English**

So basically, it's an embedding that is geared towards classification. And this is what we say will be what we plug in to that linear layer. And so when I say we throw out all the other embeddings, it's actually something that we do for the case of classification. But if we do classification at the token level, then each of them may be used. So for example, when I say question answering, if you want to detect whether a given token is the beginning of an answer, beginning of end of an answer, you would typically have two FFNs that respectively predict the start and end of the answer.

**中文**

所以基本上，这是一个面向分类的 embedding。我们说的要接入那个线性层的，就是它。当我说丢弃其他所有 embeddings 时，实际上指的是分类这种情况。但如果是在 token 级别做分类，那么每一个都可能用到。比如我提到问答时，如果你想检测一个给定 token 是否是答案的开头、答案结尾的开头 \[字幕疑误，可能指答案的开头或结尾\]，通常会有两个 FFN，分别预测答案的起点和终点。

### [1:40:23](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=6023s) · b000202

**English**

And you would apply it on each of these embeddings.

**中文**

你会把它应用到每一个这样的 embedding 上。

### [1:40:29](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=6029s) · b000203

**English**

Any other questions? Yep.

**中文**

还有其他问题吗？对。

### [1:40:37](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=6037s) · b000204

**English**

So the question is, what is query, key, and value for CLS? So it's going to be the same process as all the other tokens. So you learn here a representation for the embedding, for the token CLS. It gets projected to query. It gets projected to key. It gets projected to value. It does all its attention computation. And at the end, you get this embedding that basically that has attended to all the other ones. So it's like the answer is, it's the same as for the other tokens.

**中文**

那么问题是，CLS 的查询（query）、键（key）和值（value）是什么？它的过程与其他所有 tokens 相同。这里，你为 CLS token 学习一个 embedding 表示。它会被投影成 query，投影成 key，投影成 value，完成所有注意力计算。最后，你得到这个基本上已经关注过其他所有 tokens 的 embedding。所以答案就是，它和其他 tokens 一样。

### [1:41:11](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=6071s) · b000205

**English**

So, yeah. So just treat it as one token, it could be any token, and it's the same. OK, awesome. So I see we have five more minutes. And I'm going to quickly go through the end of it. And one thing that was great with BERT, and it was also great with ELMo, is that you have embeddings that are contextual. And here you can see that it's very easy to learn any classification task that you want, based on these learn embeddings.

**中文**

对。把它当作一个 token 就行，它可以是任何 token，过程都一样。好的，太好了。我看到我们还剩五分钟。我会快速讲完剩下的内容。BERT 的一个优点，也是 ELMo 的优点，就是 embeddings 是具有上下文信息的。在这里你可以看到，基于这些学到的 embeddings，学习任何你想做的分类任务都很容易。

### [1:41:43](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=6103s) · b000206

**English**

So this is a flexibility that was greatly appreciated here. And it's widely used in the industry. So anything that comes with sentiment detection or other classification-related tasks, it's very common to use a BERT-like model nowadays. And I'm going to talk a bit about its limitations now. So as you see in the original paper, I think the context length was of size 512.

**中文**

这种灵活性很受欢迎。它在业界被广泛使用。如今，只要涉及情感检测（sentiment detection）或其他分类相关任务，使用类似 BERT 的模型就很常见。现在我来讲一下它的局限性。正如你在原始论文中看到的，我想上下文长度是 512。

### [1:42:16](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=6136s) · b000207

**English**

So it was typically limited in this early paper. Afshine has mentioned of techniques as to how we can further grow this context size without making the complexity go completely, basically like hike. And then you have some approximation methods where you compute local attention, and so on. And then the use of these tricks helps you grow the size of the context while staying within reasonable computation requirement bounds.

**中文**

因此，在这篇早期论文中，它通常是受限的。Afshine 提到了一些技术，说明如何进一步增大上下文大小，而不让复杂度基本上完全飙升。还有一些近似方法，比如计算局部注意力（local attention）等。使用这些技巧，可以在将计算需求保持在合理范围内的同时，增大上下文。

### [1:42:50](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=6170s) · b000208

**English**

And I'm going to talk about two other limitations that we're going to see what other models try to remedy. So there is one where the latency could be seen as high. You have a still 110 million parameters for a BERT base, so it's quite a lot. Is there a way to make this smaller and faster? And then the second one is basically you have these two objective functions of MLM and NSP. Are those two truly helpful?

**中文**

我还会讲另外两个局限性，我们将看看其他模型如何尝试解决它们。一个是延迟可能被认为较高。BERT base 仍然有 1.1 亿个参数，相当多。有没有办法让它更小、更快？第二个是，你有 MLM 和 NSP 这两个目标函数。它们真的都有用吗？

### [1:43:21](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=6201s) · b000209

**English**

Is there any way we can simplify the pre-training process? So we're going to see in a second how.

**中文**

有没有办法简化 pre-training 过程？我们马上会看到如何做。

### [1:43:30](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=6210s) · b000210

**English**

So first, regarding this second limitation that we had, this basically sensitivity to cost. So who here has heard of distillation?

**中文**

首先，关于我们提到的第二个局限性，基本上就是对成本的敏感性。这里有谁听说过蒸馏（distillation）？

### [1:43:49](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=6229s) · b000211

**English**

Good, few people. So I just want to flash this quote from Hinton, Vinyals, and Jeff Dean, which I think has been informative. And it's a good mindset to have to see that the distribution that is output by a given model is actually super helpful to know what it has learned. So the soft targets contain almost all the knowledge. So it's some lecture from them that contain this quote.

**中文**

很好，有几个人。我想快速展示一下 Hinton、Vinyals 和 Jeff Dean 的这段话，我觉得很有启发性。一个值得具备的思维方式是，认识到给定模型输出的分布，对于了解它学到了什么其实非常有帮助。所以，软目标（soft targets）包含了几乎全部知识。这句话出自他们的一次讲座。

### [1:44:23](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=6263s) · b000212

**English**

So basically they were at the origin of the concept of distillation later on. And you quickly see in practice that basically learning the distribution of a model is more helpful than directly learning the hard labels. So you have this concept of teacher and student models, where basically the goal in distillation is going to be to map this output distribution of a smaller model directly to your more complex model, rather than the hard labels.

**中文**

基本上，他们后来开创了 distillation 这个概念。你很快就会在实践中发现，学习一个模型的分布，比直接学习硬标签（hard labels）更有帮助。这里有教师模型（teacher model）和学生模型（student model）的概念。distillation 的目标基本上是让较小模型的输出分布直接对应更复杂的模型，而不是 hard labels。

### [1:45:00](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=6300s) · b000213

**English**

And the objective function that you use for this to minimize this is the KL divergence, which basically says in a world that is described by the teacher, the teacher T, how bad is it to model with the student S. So it basically tries to assess how close the student distribution is going to be to the world's T.

**中文**

为此使用的最小化目标函数是 KL 散度（KL divergence），它基本上是在说，在由教师，也就是教师 T，所描述的世界中，用学生 S 建模会有多糟。它基本上是在评估学生分布会有多接近 T 所描述的世界。

### [1:45:30](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=6330s) · b000214

**English**

And one interesting note that you will see here is that you find the cross-entropy loss if your yT distribution is just a hard label. So if you have just a 1 at one position and then 0 everywhere else, you have minus log of yS, which is very interesting. And then what the DistilBERT folks have done--so by the way, it's a very clean paper, it's like four pages, but super impactful.

**中文**

这里有趣的一点是，如果你的 yT 分布只是一个 hard label，就会得到交叉熵损失（cross-entropy loss）。也就是说，如果只有一个位置是 1，其他所有位置都是 0，那么就得到负的 log yS，这很有意思。然后，DistilBERT 的作者所做的是——顺便说一下，这篇论文非常简洁，大概只有四页，但影响非常大。

### [1:46:00](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=6360s) · b000215

**English**

So it says that if you reduce the number of layers by 2, you have a lot of gains and almost the same performance, which is very remarkable. And they basically used distillation as a way to retain that performance. So this has been like the key, alongside diminishing the number of layers. And last, I'm going to talk about RoBERTa. That studied the fact that removing the NSP objective function led to no decrease in performance almost.

**中文**

它说，如果把层数减少 2 \[原文表述有歧义，可能指减至一半\]，就能获得很大收益，同时性能几乎不变，这非常了不起。他们基本上用 distillation 来保留这种性能。因此，除了减少层数之外，distillation 就是关键。最后，我要讲 RoBERTa。它研究发现，移除 NSP 目标函数，几乎不会导致性能下降。

### [1:46:36](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=6396s) · b000216

**English**

So they just dropped it. And they added some tricks, such as dynamically doing the masking. So for example, for a given piece of text, at each epoch, so every time you see the same kind of text, you would change the masking. And they also had some data strategy where they saw that the model was vastly undertrained. So they increased the diversity and the size of the data lot. And they saw that benchmark performance increased quite a bit on the same benchmarks.

**中文**

所以他们就把它去掉了。还加入了一些技巧，比如动态进行遮蔽（masking）。例如，对于某段给定文本，在每个训练轮次（epoch），也就是每次看到相同文本时，都会改变 masking。他们还采用了一些数据策略，因为他们发现模型的训练远远不够。所以，他们大幅增加了数据的多样性和规模。结果发现，在相同基准测试（benchmarks）上的性能提高了不少。

### [1:47:10](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=6430s) · b000217

**English**

And that's it for today. Thank you, everyone. Have a great weekend.

**中文**

今天就到这里。谢谢大家。周末愉快。
