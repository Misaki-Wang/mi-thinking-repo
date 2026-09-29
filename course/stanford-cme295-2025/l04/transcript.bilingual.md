# Stanford CME295 Transformers &amp; LLMs \| Autumn 2025 \| Lecture 4 - LLM Training

_Bilingual transcript · 双语讲稿_

- Channel: Stanford Online
- Source: [YouTube](https://www.youtube.com/watch?v=VlA_jt_3Qc4)
- Duration: 1:47:27
- Caption source: manual
- Status: complete
- Chinese translation: 209/209
- Translation provider: codex
- Generated: 2026-09-29T15:56:39+00:00

## Transcript · 讲稿

### [00:05](https://www.youtube.com/watch?v=VlA_jt_3Qc4&t=5s) · b000001

**English**

Cool. Hello, everyone, and welcome to lecture 4 of CME 295. So today is Friday, October, the 17, which means that the midterm is one week away. So before we start, I'm just going to go over some logistics to make sure we're all aligned on what to expect. So the midterm will take place next week same time.

**中文**

好。大家好，欢迎来到 CME 295 第 4 讲。今天是 10 月 17 日，星期五，这意味着距离期中考试还有一周。在开始之前，我先讲一下具体安排，确保大家对考试的预期一致。期中考试将在下周同一时间举行。

### [00:36](https://www.youtube.com/watch?v=VlA_jt_3Qc4&t=36s) · b000002

**English**

Instead of an hour and 15 minutes, it will be an hour and 30 minutes. So it's 3:30 to 5:00 in this classroom. Just like business as usual. In terms of topics, the midterm will be about lectures 1, 2, and 3, which we had, and this one, which is lecture 4. So just to give you an overview of what you can expect in the midterm, there's going to be some multi-choice questions along with some free form questions, but they're mainly going to be about the things that we've seen in class.

**中文**

考试时长不是 1 小时 15 分钟，而是 1 小时 30 分钟。所以是 3:30 到 5:00，就在这间教室。和往常一样。关于考试内容，期中考试会涵盖我们已经上过的第 1、2、3 讲，以及今天的第 4 讲。先给大家介绍一下期中考试大概会是什么样：会有一些选择题和自由作答题，但主要都是关于我们课堂上讲过的内容。

### [01:17](https://www.youtube.com/watch?v=VlA_jt_3Qc4&t=77s) · b000003

**English**

So if you watch the recordings, or attend the lectures, and just go through the slides, and know the important formulas, I think you'll be fine. So I know that you may have questions until next week, so that's why after this lecture with Shervin, we will be holding office hours. So feel free to come to us and ask us any questions. And of course, we'll be fully available between now and next week.

**中文**

所以，如果你看了录像，或者来听课，再把幻灯片过一遍，掌握重要公式，我想就没问题。我知道直到下周大家可能还会有问题，所以今天这节课之后，我和 Shervin 会安排答疑时间。欢迎来找我们，问任何问题。当然，从现在到下周，我们都会随时为大家答疑。

### [01:47](https://www.youtube.com/watch?v=VlA_jt_3Qc4&t=107s) · b000004

**English**

So in case you have any questions, feel free to ping us on Ed. And yeah, we'll make sure to respond.

**中文**

所以，如果有任何问题，随时在 Ed 上联系我们。我们一定会回复。

### [01:57](https://www.youtube.com/watch?v=VlA_jt_3Qc4&t=117s) · b000005

**English**

Cool. I also know that a number of you are auditing this class. So in case you're still interested to take the midterm for some reason, maybe because you have an upcoming interview, just tell us, so that we can just expect the number of copies to print. So we'll be printing this on Monday. So just let us over the weekend in case you're interested. Cool. So that's for the midterm. And then the second piece of news is the final.

**中文**

好。我也知道有一些同学在旁听这门课。如果你出于某种原因仍然想参加期中考试，比如近期有面试，只需要告诉我们，这样我们就能估计要打印多少份试卷。我们会在星期一打印。所以，如果你感兴趣，周末告诉我们就好。好，期中考试就说到这里。第二个消息是关于期末考试。

### [02:29](https://www.youtube.com/watch?v=VlA_jt_3Qc4&t=149s) · b000006

**English**

So we said that we were working on the dates. So we finally finalized the dates which did not change. So it's Wednesday, December the 10. OK. So a little bit late, 7:00 PM to 8:30 PM. So it's a slot that we have. The location is different from this one. So it's in this room.

**中文**

我们之前说过还在确定日期。现在终于定下来了，日期没有变，就是 12 月 10 日，星期三。好，时间稍微晚一点，是晚上 7:00 到 8:30。这是分配给我们的时段。地点和这里不同，在这间教室。

### [02:51](https://www.youtube.com/watch?v=VlA_jt_3Qc4&t=171s) · b000007

**English**

And the final will only cover the second part of the class, which is basically lectures 5 to 9. Any questions on this? Yeah. Oh, yeah. Good question. So is it closed notes? Yes. Yeah. Yes.

**中文**

期末考试只涵盖课程的第二部分，基本上就是第 5 到第 9 讲。对此有什么问题吗？嗯。哦，对，好问题。问题是不能看笔记吗？是的。对，是的。

### [03:14](https://www.youtube.com/watch?v=VlA_jt_3Qc4&t=194s) · b000008

**English**

So the question is, what is the format of the multiple choice? So you'll have-- so we did not finish writing the exam, but it's going to be something like you have a question and let's say, you have three, four possible answers and then you just choose the one that. That's correct. Something like this. And you'll also have some free form, like you'll have to just answer in your own words. Yeah.

**中文**

问题是，选择题是什么形式？你会有——我们还没出完试卷，不过大概是给你一道题，比如有三四个备选答案，然后你选择那个。正确的那个。大概就是这样。也会有一些自由作答题，比如需要你用自己的话回答。嗯。

### [03:41](https://www.youtube.com/watch?v=VlA_jt_3Qc4&t=221s) · b000009

**English**

Thanks. So the question is, are we allowed to take anything? So it's closed book. So no. Yeah. Nothing. Just a pen. Yeah. Question is no calculator. You will not need a calculator. But speaking of the cheat sheets, so I'm not sure if we mentioned, I think we did, so there is a cheat sheet for this one, which we cannot bring to the exam but you can use just for your studying that's on the website.

**中文**

谢谢。问题是，我们可以带什么东西吗？这是闭卷考试，所以不可以。对，什么都不能带，只带一支笔。对。问题是不能带计算器吗？你不需要计算器。不过说到速查表（cheat sheet），我不确定我们有没有提过，我想应该提过：这门课有一份 cheat sheet，不能带进考场，但可以用来复习，就在网站上。

### [04:14](https://www.youtube.com/watch?v=VlA_jt_3Qc4&t=254s) · b000010

**English**

Class website. So Jess recommends looking at it. Cool. So super clear for everyone? Very cool. Well, OK. As always, we'll be starting the class just recapping what we saw in the previous lecture. So if you remember, we basically studied a new kind of architecture, which was called the mixture of experts, which is such that if you have an input, what you want is to not necessarily activate all the parameters.

**中文**

课程网站上。所以 Jess 建议大家看看。好，大家都很清楚了吗？非常好。好吧，和往常一样，我们先回顾上一讲的内容。如果大家还记得，我们主要学习了一种新的架构，叫混合专家（mixture of experts）。这种架构的特点是，给定一个输入，你不一定想激活所有参数。

### [04:54](https://www.youtube.com/watch?v=VlA_jt_3Qc4&t=294s) · b000011

**English**

And so you are in a setting where you have multiple experts, and in the forward pass, you only activate some of them. So that's a sparse MOE. You also have the dense MOE, which basically weights the outputs as a function of the output of the gate. So we saw that this architecture was used in LLMs, and it was mainly used to be able to scale this LLMs without incurring an expensive cost at inference time, because you don't want to activate all the parameters.

**中文**

所以，在这种设置下，你有多个专家，而在前向传播（forward pass）时，只激活其中一部分。这就是稀疏 MOE（sparse MOE）。还有稠密 MOE（dense MOE），它基本上是根据门控（gate）的输出来对各个输出加权。我们看到，这种架构被用于大语言模型（LLMs），主要是为了扩大这些 LLMs 的规模，同时避免在推理（inference）时产生高昂的成本，因为你不想激活所有参数。

### [05:29](https://www.youtube.com/watch?v=VlA_jt_3Qc4&t=329s) · b000012

**English**

The second thing that we saw was just defining what an LLM was and in particular, how you could decide on what the next token prediction is. So we saw three methods. First one was we called greedy decoding, which was always taking the highest probable token. The second method we saw was beam search, where we kept track of the K most probable sequences.

**中文**

我们讲的第二件事是定义什么是 LLM，尤其是如何决定下一个词元（token）的预测结果。我们看了三种方法。第一种叫贪心解码（greedy decoding），就是始终选择概率最高的 token。第二种是束搜索（beam search），我们会跟踪概率最高的 K 个序列。

### [06:00](https://www.youtube.com/watch?v=VlA_jt_3Qc4&t=360s) · b000013

**English**

And then the third one was sampling. So we're not doing the most probable. We're not keeping track of the highest probable sequences. What we do is we sample the next token with respect to the distribution that we get as outputs. And then we saw there's this hyperparameter that's called temperature that allows you to tweak how spiky you want your distribution to like versus not. And we also saw some inference optimization techniques, which are used in practice to avoid having a big cost at decoding time.

**中文**

第三种是采样（sampling）。我们不选择概率最高的，也不跟踪概率最高的那些序列，而是根据输出的分布来采样下一个 token。然后，我们看到了一个叫温度（temperature）的超参数（hyperparameter），它可以调节你希望分布有多尖锐，或者不那么尖锐。我们还看了一些推理优化（inference optimization）技术，在实际中用来避免解码（decoding）时产生很大的成本。

### [06:41](https://www.youtube.com/watch?v=VlA_jt_3Qc4&t=401s) · b000014

**English**

So I'm not going to just mention everything, but I would say KV cache, for instance, is an important method. So yeah, just recommend just knowing what it is along with the other ones. And with that, we're going to start lecture 4. And actually, I was really looking forward to today because lecture 1, we saw what self-attention was, what a transformer was. Second lecture, we saw some of the tricks that people use today and some of the variations from the transformer.

**中文**

我不会把所有方法都再说一遍，不过我会说，比如 KV 缓存（KV cache）就是一种重要的方法。所以，建议大家了解它是什么，也了解其他那些方法。接下来我们开始第 4 讲。其实我非常期待今天，因为第 1 讲我们讲了什么是自注意力（self-attention），什么是 transformer。第 2 讲，我们讲了现在人们使用的一些技巧，以及 transformer 的一些变体。

### [07:15](https://www.youtube.com/watch?v=VlA_jt_3Qc4&t=435s) · b000015

**English**

We introduced what an LLM was last lecture. And this lecture, we're finally going to see how these LLMs are trained. So today, we're going to focus on LLM training.

**中文**

上一讲我们介绍了什么是 LLM。这一讲，我们终于要看看这些 LLMs 是如何训练的。所以，今天我们重点讲 LLM 训练。

### [07:31](https://www.youtube.com/watch?v=VlA_jt_3Qc4&t=451s) · b000016

**English**

And the first thing that I'm going to say is if you've been in the ML field for, let's say, more than a few years now, you may have noticed that traditionally, if you had a task, what you would do is train a model specifically for that task. So let's suppose 10 years ago, let's suppose we had a task which was around detecting spam. You would train a model specifically to detect spams.

**中文**

首先我想说，如果你在机器学习（ML）领域已经待了，比如好几年，你可能注意到，传统上，如果你有一个任务，你会专门为这个任务训练一个模型。假设是 10 年前，假设我们有一个检测垃圾邮件的任务，你就会专门训练一个检测垃圾邮件的模型。

### [08:04](https://www.youtube.com/watch?v=VlA_jt_3Qc4&t=484s) · b000017

**English**

So you would train on the training set, eval on the validation set, and then test on the test set. If you had another use case, let's suppose sentiment extraction, you would train a model specifically for that and so on and so forth. But one could argue that these tasks, they are not completely disjoint. They're all involving just understanding the text.

**中文**

你会在训练集（training set）上训练，在验证集（validation set）上评估，然后在测试集（test set）上测试。如果你有另一个应用场景，比如情感提取（sentiment extraction），你会专门为它训练一个模型，以此类推。但可以说，这些任务并不是完全没有交集，它们都涉及理解文本。

### [08:35](https://www.youtube.com/watch?v=VlA_jt_3Qc4&t=515s) · b000018

**English**

So one could argue we could find a way to somehow leverage the knowledge that we acquired during training for, let's say, one task and reuse that for another task. So this method has a name. It's been around for some time, and it's called transfer learning. So the goal of transfer learning is to not always start from scratch if you have a new task. It's to start with some pre-trained model, and we're going to see what pre-trained is, and then tune it for your task instead of starting from scratch.

**中文**

所以可以说，我们可以找到一种方法，以某种方式利用在一个任务的训练过程中获得的知识，再将它用于另一个任务。这种方法有一个名字，已经存在一段时间了，叫迁移学习（transfer learning）。transfer learning 的目标是，有新任务时不必总是从零开始，而是从一个预训练模型（pre-trained model）开始——我们会讲什么叫预训练——然后针对你的任务进行调优，而不是从零开始。

### [09:16](https://www.youtube.com/watch?v=VlA_jt_3Qc4&t=556s) · b000019

**English**

Well, it's basically the paradigm on which LLMs are trained. So the idea here is that all these tasks, they involve understanding language. So what we're going to do is have what we call a pre-training stage, which involves training your LLM on vast amounts of data to just understand what language, what code is and then have a second stage of, quote unquote, "tuning."

**中文**

这基本上就是训练 LLMs 所采用的范式。这里的想法是，所有这些任务都涉及理解语言。因此，我们会先进行一个所谓的预训练阶段（pre-training stage），用海量数据训练 LLM，让它理解什么是语言、什么是代码，然后进入第二个阶段，也就是加引号的“调优（tuning）”。

### [09:52](https://www.youtube.com/watch?v=VlA_jt_3Qc4&t=592s) · b000020

**English**

And we're going to see a little bit what that tuning is. But in that second stage, we're going to take our pre-trained model and somehow find a way to tune the weights to adapt to a specific task. So as an example, here, we would pre-train a huge model and then suppose for spam detection. We would somehow tune it for that sentiment extraction, same. We would tune it for that and so on. So this is just to take the example from before.

**中文**

我们会稍微介绍一下这种 tuning 是什么。在第二个阶段，我们会拿到预训练模型，然后以某种方式调整权重（weights），使它适应特定任务。比如在这里，我们会预训练一个巨大的模型，然后假设要做垃圾邮件检测，就以某种方式针对这个任务调优。情感提取也一样，针对它进行调优，以此类推。这只是沿用前面的例子。

### [10:25](https://www.youtube.com/watch?v=VlA_jt_3Qc4&t=625s) · b000021

**English**

And the idea here is in order to obtain these models, we're not going to start from scratch.

**中文**

这里的想法是，为了得到这些模型，我们不会从零开始。

### [10:34](https://www.youtube.com/watch?v=VlA_jt_3Qc4&t=634s) · b000022

**English**

Cool. So now, we're going to see what pre-training is. So pre-training is by far the most expensive both in terms of compute, cost, everything part of the training. So what it does is taking a huge amount of data and training your LLM to just predict the next token. And here, by data, what I mean is basically everything you can find.

**中文**

好。现在我们来看看什么是预训练（pre-training）。无论从计算量、成本还是其他各方面来说，pre-training 都是训练过程中最昂贵的部分，而且远远超过其他部分。它做的事情就是使用海量数据，训练 LLM 去预测下一个 token。这里所说的数据，基本上是指你能找到的一切。

### [11:06](https://www.youtube.com/watch?v=VlA_jt_3Qc4&t=666s) · b000023

**English**

So it can be text in English. It can be text in other languages. It can be even code, can be code in different languages, can be basically the whole internet. We're going to see some of the data sets that people use for that, but you can think of this as just training your model to try to predict anything that's written. And as I mentioned, the objective here is to predict the next token.

**中文**

可以是英文文本，也可以是其他语言的文本，甚至可以是代码，可以是不同语言的代码，基本上可以是整个互联网。我们会看一些人们为此使用的数据集，但你可以把它理解为训练模型去尝试预测任何写下来的内容。正如我刚才提到的，这里的目标是预测下一个 token。

### [11:40](https://www.youtube.com/watch?v=VlA_jt_3Qc4&t=700s) · b000024

**English**

So if you remember, our LLM is a text-to-text model and most likely a decoder only model in more than 90% of the cases. So what it does is it takes some input text, and it tries to always predict the next token in an iterative basis. So in terms of the data sets that are used, you will see the term Common Crawl a lot on papers. It's basically a data set composed of anything you can find on the internet.

**中文**

如果你还记得，我们的 LLM 是一个文本到文本（text-to-text）模型，而且在超过 90% 的情况下，很可能是仅解码器（decoder only）模型。它接收一些输入文本，然后通过迭代，始终尝试预测下一个 token。至于所使用的数据集，你会在论文中经常看到 Common Crawl 这个词。它基本上是由互联网上能找到的各种内容组成的数据集。

### [12:13](https://www.youtube.com/watch?v=VlA_jt_3Qc4&t=733s) · b000025

**English**

So I think they have something like three billion pages per month. So if you go on their website, they have a huge archive. So there's a bunch of other websites as well that you can find in there. So for instance, Wikipedia articles, any social media as well, like Reddit. And there are a lot of Reddit conversations in those data sets. You have a lot of codes, and of course, you have a bunch of places for that. You have GitHub, you have Stack Overflow, all these forums that talk about codes. So all of this is meant for your model to just understand the structure of the language and code.

**中文**

我记得它们每个月大概有 30 亿个网页。如果你去它们的网站，可以看到一个巨大的存档。里面也能找到很多其他网站的内容。比如 Wikipedia 文章，还有各种社交媒体，比如 Reddit。这些数据集中有很多 Reddit 对话，也有很多代码，当然，代码有很多来源，比如 GitHub、Stack Overflow，以及所有这些讨论代码的论坛。所有这些都是为了让模型理解语言和代码的结构。

### [12:51](https://www.youtube.com/watch?v=VlA_jt_3Qc4&t=771s) · b000026

**English**

And in terms of size, so it's measured in terms of tokens, number of tokens. And one order of magnitude that I want you to remember is on the order of hundreds of billions or even trillions or even tens of trillions of tokens. So I'll give you an example. So GPT-3 was trained on 300 billion tokens. And for instance, Llama 3, which was I believe published last year, was trained on 15 trillion tokens.

**中文**

至于规模，是用 token 来衡量的，也就是 token 数量。我希望大家记住的一个数量级是，数千亿，甚至数万亿，甚至数十万亿个 token。我举个例子，GPT-3 使用了 3000 亿个 token 进行训练。而比如 Llama 3，我记得是去年发布的，使用了 15 万亿个 token 进行训练。

### [13:23](https://www.youtube.com/watch?v=VlA_jt_3Qc4&t=803s) · b000027

**English**

So these are huge data sets.

**中文**

所以，这些数据集非常庞大。

### [13:27](https://www.youtube.com/watch?v=VlA_jt_3Qc4&t=807s) · b000028

**English**

So before we go further, I want to introduce two notations. And I think one of them I introduced it last lecture. The reason why I want to talk to you about these notations is they're used everywhere to talk about how much compute some model needs. So the first notation is FLOPs, which stands for floating operations. And what it is it's a unit of compute.

**中文**

在继续之前，我想介绍两个记号。其中一个我想上一讲已经介绍过。我之所以想讲这些记号，是因为在讨论一个模型需要多少计算量时，到处都会用到它们。第一个是 FLOPs，代表 floating operations \[字幕疑误，可能指 floating point operations，即浮点运算\]。它是计算量的单位。

### [14:01](https://www.youtube.com/watch?v=VlA_jt_3Qc4&t=841s) · b000029

**English**

So the higher the FLOPs, the more operations are involved. Because by definition, FLOPs is the number of operations that involve floating point numbers. So floating point numbers, you can think of them as just numbers with decimal points. So in terms of order of magnitudes, training an LLM is on the order of 10 to the power of 25 FLOPs. And the way you obtain FLOPs, so usually, it's a complicated formula.

**中文**

FLOPs 越高，涉及的运算就越多。因为按照定义，FLOPs 是涉及浮点数（floating point numbers）的运算次数。你可以把浮点数理解为带小数点的数。从数量级上看，训练一个 LLM 需要大约 10 的 25 次方 FLOPs。至于如何计算 FLOPs，通常会有一个复杂的公式。

### [14:35](https://www.youtube.com/watch?v=VlA_jt_3Qc4&t=875s) · b000030

**English**

But in your mind, you can think of it as something that is a function of the size of your data, so the number of tokens that you train it on, and the number of parameters of your model. So there's not an universal formula because it also is a function of the architecture. So you can think, for instance, MOE based LLMs as requiring, let's say, less compute because only some parts are activated compared to, let's say, dense LLMs.

**中文**

不过，在脑海中，你可以把它理解为数据规模，也就是训练所用的 token 数量，以及模型参数数量的函数。并不存在一个通用公式，因为它也是架构的函数。比如，你可以认为，相比 dense LLMs，基于 MOE 的 LLMs 所需的计算量更少，因为只有一部分被激活。

### [15:08](https://www.youtube.com/watch?v=VlA_jt_3Qc4&t=908s) · b000031

**English**

But you can just think of it as it's a function of the number of tokens and parameters. It's like O of the product between the two, more or less. And then there's a second notation that I want to introduce, which is also FLOPS, but it's different. So here, FLOPS stands for floating point operations per second. So it's a measure of compute speeds. So it's basically how fast can your hardware execute these operations.

**中文**

但你可以把它理解为 token 数量和参数数量的函数，大致就是两者乘积的 O。然后，我想介绍第二个记号，也是 FLOPS，但含义不同。这里 FLOPS 代表每秒浮点运算次数（floating point operations per second）。它衡量的是计算速度，基本上就是硬件执行这些运算有多快。

### [15:46](https://www.youtube.com/watch?v=VlA_jt_3Qc4&t=946s) · b000032

**English**

And so you also have some order of magnitudes here. But if you're into, let's say GPUs, you will see that in the description of GPUs, they always indicate FLOPS. And we will see that in a second. But I just want to call out that FLOPS here is usually all caps, although you may see some papers that use one for the other, which is confusing.

**中文**

这里也有一些数量级。不过，如果你关注图形处理器（GPUs），就会发现 GPU 的说明里总会标明 FLOPS。我们马上会看到。我只是想指出，这里的 FLOPS 通常全部大写，不过你可能会看到一些论文把这两个记号混着用，这会让人困惑。

### [16:16](https://www.youtube.com/watch?v=VlA_jt_3Qc4&t=976s) · b000033

**English**

So I'll just recommend just contextualizing this notation with respect to the sentence that it is in because sometimes people actually switch the two. But this is the common notation. So far, so good? Cool. So now, we know that we have a pre-training step. We know it involves a lot of compute. We know it involves a lot of data. We know our model is large.

**中文**

所以，我建议结合它所在的句子来理解这个记号，因为有时人们确实会把两者互换。不过，这就是常见的记法。到这里都没问题吧？好。现在，我们知道有一个 pre-training 步骤，知道它需要大量计算，需要大量数据，也知道我们的模型很大。

### [16:47](https://www.youtube.com/watch?v=VlA_jt_3Qc4&t=1007s) · b000034

**English**

So what people did was trying to see how the performance evolves as a function of model size and training size. And there is this one paper called Scaling Loss for Neural Language Models that was published in 2020 that performed a bunch of experiments by varying these parameters. And what they found was the more compute you have, the better your model learns about predicting the next token.

**中文**

于是，人们尝试研究性能如何随着模型规模和训练规模变化。有一篇 2020 年发表的论文，叫 Scaling Loss for Neural Language Models \[字幕疑误，可能指 Scaling Laws for Neural Language Models\]，通过改变这些参数做了大量实验。他们发现，计算量越多，模型就越能学会预测下一个 token。

### [17:20](https://www.youtube.com/watch?v=VlA_jt_3Qc4&t=1040s) · b000035

**English**

Same for data set size. So the bigger your training set, the better it is, and the bigger your model, the better it is. So for some time, I think, between 2019 and 2024, you were seeing models that were larger and larger, just people just building things that were bigger and bigger because according to these experiments, the performance was just getting better.

**中文**

数据集规模也是一样。训练集越大越好，模型越大越好。所以有一段时间，我想大概在 2019 年到 2024 年之间，你会看到模型越来越大，人们不断构建越来越大的东西，因为按照这些实验，性能一直在变好。

### [17:53](https://www.youtube.com/watch?v=VlA_jt_3Qc4&t=1073s) · b000036

**English**

So something else that they noticed was bigger models tend to be more what they call sample efficient. So what that means is for an equal amount of tokens that is processed, you will have a better performance with a bigger model compared to a smaller one.

**中文**

他们还注意到，较大的模型往往具有更高的所谓样本效率（sample efficient）。也就是说，在处理相同数量 token 的情况下，大模型会比小模型表现更好。

### [18:19](https://www.youtube.com/watch?v=VlA_jt_3Qc4&t=1099s) · b000037

**English**

But then you can wonder, we don't have unlimited compute. Compute is expensive. It has a lot of drawbacks. So you have a fixed compute, and people also try to answer the question given a certain amount of compute, how can you fix your training set size and your model size in a way that's more optimal?

**中文**

但接下来你可能会想，我们的计算资源并不是无限的。计算很贵，也有很多不利之处。因此，当计算量固定时，人们也尝试回答这样一个问题：给定一定的计算量，如何更优地确定训练集规模和模型规模？

### [18:50](https://www.youtube.com/watch?v=VlA_jt_3Qc4&t=1130s) · b000038

**English**

Because here, you need to decide how big is your model. So what they did is they fixed a unit of compute, which is the color of these curves. And they tried training models of different sizes with different training set size. And what they saw was that there was always a sweet spot here, which followed some kind of relationship, and in particular, this is a table that summarizes, quote unquote, "the optimal set of number of parameters and training set size," which is sometimes called the Chinchilla law.

**中文**

因为在这里，你需要决定模型要有多大。他们的做法是固定一个计算量，这些曲线的颜色就代表它。然后，他们尝试用不同大小的训练集训练不同规模的模型。他们发现，这里总有一个最佳点，而且它遵循某种关系。具体来说，这张表总结了加引号的“最优参数数量和训练集规模组合”，有时称为 Chinchilla 定律（Chinchilla law）。

### [19:33](https://www.youtube.com/watch?v=VlA_jt_3Qc4&t=1173s) · b000039

**English**

And what they realized was if you have an amount of training set size that's about 20 times the model size, then you're spending your compute in a, quote unquote, "an optimal way." And in particular, GPT-3, for instance, I think it was like 175 billion parameters, if I remember correctly, but it's only trained on 300 billion tokens.

**中文**

他们发现，如果训练集规模大约是模型规模的 20 倍，那么你就是在以加引号的“最优方式”使用计算资源。具体来说，比如 GPT-3，如果我没记错，它大概有 1750 亿个参数，但只用了 3000 亿个 token 进行训练。

### [20:06](https://www.youtube.com/watch?v=VlA_jt_3Qc4&t=1206s) · b000040

**English**

So this one, for instance, is, according to this, "really undertrained," quote unquote. I think there was a question. Yeah. \[AUDIO OUT\]

**中文**

因此，比如这个模型，按照这个说法，就是加引号的“训练严重不足”。我想有一个问题。嗯。\[音频缺失\]

### [20:26](https://www.youtube.com/watch?v=VlA_jt_3Qc4&t=1226s) · b000041

**English**

So yeah. The question is, do they fit the neural architecture? So I think by now, everyone agrees that LLMs are transformer-based decoder only models. So everyone uses the same model. So you can assume that when I say LLM here, it basically means decoder only transformer-based models. \[AUDIO OUT\] Yeah. Question is architecture change does not play a big role. So that's what they say actually in their paper.

**中文**

是的。问题是，他们会拟合神经网络架构吗？所以，我想现在大家都认同，LLMs 是基于 transformer 的 decoder only 模型。大家都使用同一种模型。因此，你可以假定，我这里说 LLM，基本上就是指基于 transformer 的 decoder only 模型。\[音频缺失\] 对。问题是，架构变化不会起很大作用吗？这其实就是他们在论文里说的。

### [20:57](https://www.youtube.com/watch?v=VlA_jt_3Qc4&t=1257s) · b000042

**English**

They say the thing that changes the most is the amount of tokens on which you train and the size of your model.

**中文**

他们说，影响变化最大的，是训练使用的 token 数量和模型规模。

### [21:05](https://www.youtube.com/watch?v=VlA_jt_3Qc4&t=1265s) · b000043

**English**

Cool. Any other questions? Yeah. \[AUDIO OUT\]

**中文**

好。还有其他问题吗？嗯。\[音频缺失\]

### [21:23](https://www.youtube.com/watch?v=VlA_jt_3Qc4&t=1283s) · b000044

**English**

Oh, yeah. Good question. So question is, is there some kind of transfer learning between different versions of models? So for a lot of these models, they're actually closed source. So they don't exactly reveal these things. But I guess it's an interesting question, one that I cannot answer in a general way. So maybe I think it's the best answer I can give you. But in any case, when you look at some of these papers, they always state how much it costs to train this.

**中文**

哦，对，好问题。问题是，不同版本的模型之间是否存在某种 transfer learning？这些模型中有很多实际上是闭源的，所以它们并不会确切披露这些事情。不过，我觉得这是个有意思的问题，我无法给出一个普遍适用的答案。所以，也许我想这就是我能给你的最好回答。不过无论如何，你看这些论文时，它们总会说明训练模型花了多少钱。

### [21:53](https://www.youtube.com/watch?v=VlA_jt_3Qc4&t=1313s) · b000045

**English**

And it's always in the order of millions. It's always an expensive step regardless. Cool. Just speaking of that, so pre-training has a lot of challenges. One of them is cost. So when I say, millions of dollars, it's minimum. I think it can even cost tens of millions of dollars or sometimes hundreds of millions of dollars. It takes a lot of time, and people have been mindful of the impact on the environment.

**中文**

而且总是数百万的量级。无论如何，这一步总是很昂贵。好。说到这里，pre-training 有很多挑战，其中之一就是成本。我说数百万美元，那还是最低的。我想它甚至可能花费数千万美元，有时会达到数亿美元。它需要很长时间，而且人们也一直在关注对环境的影响。

### [22:26](https://www.youtube.com/watch?v=VlA_jt_3Qc4&t=1346s) · b000046

**English**

So they've also been including the ecological costs. So the other challenge is that the pre-training step is on data that is up to the time at which you pre-train your model on. So what that means is that the knowledge that you acquire from training on this data set can only go up until the date at which you cut your data set.

**中文**

因此，他们也开始把生态成本纳入考虑。另一个挑战是，pre-training 使用的数据，只能截至你对模型进行预训练的那个时候。这意味着，通过在这个数据集上训练获得的知识，只能截至你截断数据集的日期。

### [23:00](https://www.youtube.com/watch?v=VlA_jt_3Qc4&t=1380s) · b000047

**English**

So this date is called the knowledge cutoff date. And so what that means is your base model, your pre-trained base model has no way to know by itself knowledge that occurred after this date. And speaking of that, a lot of papers, they have tried to edit knowledge, inject knowledge. It's always tricky because there's not a clean way to change the weights in a way that does not penalize some parts.

**中文**

这个日期叫知识截止日期（knowledge cutoff date）。这意味着，你的基础模型（base model），也就是预训练的 base model，本身没有办法知道这个日期之后出现的知识。说到这里，很多论文尝试过编辑知识、注入知识。这始终很棘手，因为没有一种干净利落的办法，能在修改权重的同时不损害某些部分。

### [23:34](https://www.youtube.com/watch?v=VlA_jt_3Qc4&t=1414s) · b000048

**English**

So I guess what people want to do is inject knowledge but not regress in some other domains. And this is a very hard problem. And of course, these models, they try to predict the next token. And there's this question of what if it just generates something that it has seen at training time? So what we call plagiarism. So there's always a risk. So these are all the challenges I just want to illustrate when I said knowledge cutoff date. So if you go on, let's say, the OpenAI website or Google website to look at the model cards, you will always see--so I'm not sure as you can see from here, but there is always a line on knowledge cutoff date, which tells you on when the pre-training of this model was done.

**中文**

所以，我想人们希望做到的是注入知识，同时不让其他领域的表现退步。这是一个非常困难的问题。当然，这些模型在尝试预测下一个 token，于是就有这样一个问题：如果它生成了训练时见过的内容怎么办？这就是我们所说的抄袭。所以，总会有风险。这些就是所有这些挑战。我只是想说明一下刚才说的 knowledge cutoff date。如果你去，比如 OpenAI 网站或 Google 网站查看模型卡（model cards），你总会看到——我不确定大家从这里能否看清——总会有一行 knowledge cutoff date，告诉你这个模型是在什么时候完成预训练的。

### [24:24](https://www.youtube.com/watch?v=VlA_jt_3Qc4&t=1464s) · b000049

**English**

So here, for instance, GPT-5 was released a few weeks ago, and here, it says, the knowledge cutoff date is September 30. So you can guess that they've done their pre-training around that stage.

**中文**

比如这里，GPT-5 是几周前发布的，这里写着 knowledge cutoff date 是 9 月 30 日。所以你可以推测，它们是在那个时间附近进行 pre-training 的。

### [24:39](https://www.youtube.com/watch?v=VlA_jt_3Qc4&t=1479s) · b000050

**English**

Cool. Any questions on the first part? All good? Perfect. So in this first part, we've seen that pre-training was a crucial step of the LLM training process. And we've seen all these big numbers. And one could wonder, well, how can you train such a big model on such a big amount of data?

**中文**

好。关于第一部分，有什么问题吗？都没问题？很好。在第一部分，我们看到 pre-training 是 LLM 训练流程中至关重要的一步，也看到了这些巨大的数字。于是你可能会想，如何用如此海量的数据训练这么大的模型？

### [25:09](https://www.youtube.com/watch?v=VlA_jt_3Qc4&t=1509s) · b000051

**English**

How do people do that? So this is what we're going to see here. So this is what I mentioned. So LLMs, you can think of them as decoder only transformer-based models. So in order to train your model, you need that. You need a lot of data, but then if you look at your architecture, you see that a lot of the operations involve matrix multiplications.

**中文**

人们是怎么做到的？这就是我们接下来要看的内容。这是我之前提到的，你可以把 LLMs 理解为基于 transformer 的 decoder only 模型。为了训练模型，你需要这个，需要大量数据。但再看一下架构，你会发现，很多运算都涉及矩阵乘法（matrix multiplications）。

### [25:44](https://www.youtube.com/watch?v=VlA_jt_3Qc4&t=1544s) · b000052

**English**

And I guess I have a question for you. What is the kind of hardware that loves matrix multiplications? GPUs. Yes. So you also need GPUs. Actually more than one. Yeah. You had a question. \[AUDIO OUT\]

**中文**

我想问大家一个问题：哪种硬件特别喜欢矩阵乘法？GPUs。对。所以你也需要 GPUs，实际上不止一块。嗯，你有个问题。\[音频缺失\]

### [26:03](https://www.youtube.com/watch?v=VlA_jt_3Qc4&t=1563s) · b000053

**English**

Oh. Question is GPT for inference. So this one, we're going to focus on training, but requirements for GPUs, they differ a little bit between training and inference, but in this part, we're solely focused on training. And speaking of GPUs, I guess, it's not GPUs everywhere because, for instance, Google, they've developed their own hardware that's called TPUs, but any non Google-based models, they've most likely been trained on GPUs.

**中文**

哦，问题是用于推理的 GPT \[字幕疑误，可能指 GPU\]。这里我们重点讲训练。训练和推理对 GPU 的要求略有不同，但在这一部分，我们只关注训练。说到 GPUs，我想也不是所有地方都用 GPUs，比如 Google 就开发了自己的硬件，叫张量处理器（TPUs）。不过，任何非 Google 的模型，很可能都是在 GPUs 上训练的。

### [26:33](https://www.youtube.com/watch?v=VlA_jt_3Qc4&t=1593s) · b000054

**English**

Cool. So in order to train your model, what do you do? So first of all, you have your LLM which is now-- so it is this model, but now, we're representing with a box just for simplicity. You initialize it. It's a lot of parameters. So you can think of the scale as being somewhere around billions to hundreds of billions of parameters, so huge model. And what are the steps involved to train a model? Well, what you're trying to do is to tune the weights, so that the model can learn how to generate the next token.

**中文**

好。为了训练模型，你要做什么？首先，你有一个 LLM，现在它——就是这个模型，不过为了简单起见，现在我们用一个方框表示它。你对它进行初始化。它有很多参数，你可以认为规模大约在数十亿到数千亿个参数之间，所以是一个巨大的模型。那么训练模型涉及哪些步骤？你要做的是调整权重，让模型学会如何生成下一个 token。

### [27:14](https://www.youtube.com/watch?v=VlA_jt_3Qc4&t=1634s) · b000055

**English**

So you have one step called the forward pass, where you have a bunch of data that you're trying to pass through the network. And while we do that, I just want to call out things that are important to note that we need to somehow save in memory. So when you do this forward pass, you have something that's called activations, which are basically the values at each layer that are needed in order to compute the loss.

**中文**

其中有一步叫 forward pass，就是把一批数据送入网络。在这个过程中，我想指出一些重要的东西，它们需要以某种方式保存在内存中。进行 forward pass 时，会产生所谓的激活值（activations），基本上就是各层中用于计算损失（loss）的数值。

### [27:46](https://www.youtube.com/watch?v=VlA_jt_3Qc4&t=1666s) · b000056

**English**

So the loss tells you how off you are compared to the label that you want to train this on. And so the amount of memory that you will use here is dependent on a lot of things. It's dependent on the model size, which impacts the number of activations. It's dependent on how big your batch of data is for training. And it's dependent on how large your context length is, because if you remember, here we have O of N squared complexity because of this self-attention operation, where N is the sequence length.

**中文**

loss 告诉你，相比训练所针对的标签（label），你的结果偏离了多少。这里使用的内存大小取决于很多因素。它取决于模型规模，因为这会影响 activations 的数量；也取决于训练数据的批次（batch）有多大；还取决于上下文长度（context length）有多长。因为如果你还记得，由于 self-attention 运算，这里有 O(N²) 的复杂度，其中 N 是序列长度。

### [28:21](https://www.youtube.com/watch?v=VlA_jt_3Qc4&t=1701s) · b000057

**English**

So you have all these parameters that come into play. So once you do the forward pass, let's suppose you compute the loss. You know how off you are compared to your label. Now, the next step is to somehow tweak the weights in a way that minimizes the loss. So how do you do that? There is this another pass called backwards pass. So what this pass does is quantify the direction where the loss is going to be minimized.

**中文**

所以，这些参数都会起作用。完成 forward pass 后，假设你计算了 loss，就知道结果相对于 label 偏离了多少。下一步，就是以某种方式调整权重，使 loss 最小化。那么怎么做呢？还有另一个过程，叫反向传播（backwards pass）。这个过程所做的，就是量化 loss 将被最小化的方向。

### [28:58](https://www.youtube.com/watch?v=VlA_jt_3Qc4&t=1738s) · b000058

**English**

It's called the gradient. You take the gradient of the loss with respect to each parameter. Well, gradients, they also need to be saved somewhere in memory. And then you have finally the weights update, which is where you know where the direction at which your loss is going to be minimized. So you apply that update to your weights. And you typically use optimizers out there. Have you heard of Adam optimizer?

**中文**

这叫梯度（gradient）。你对每个参数求 loss 的梯度。gradients 也需要保存在内存中的某个地方。最后是权重更新（weights update），这时你已经知道使 loss 最小化的方向，就把这个更新应用到权重上。通常会使用已有的优化器（optimizers）。大家听说过 Adam 优化器（Adam optimizer）吗？

### [29:29](https://www.youtube.com/watch?v=VlA_jt_3Qc4&t=1769s) · b000059

**English**

Yeah. So Adam optimizer is just a fancy version that has some additional quantities, which keep track of--which are basically a function of the gradients. So you have the first moment and the second moment, which is basically the moving average of the gradient and the squared gradients. And all these quantities, so the first moment, the second moment, you also need to somehow save them somewhere in memory.

**中文**

嗯。Adam optimizer 就是一种更复杂的版本，它有一些额外的量，用来跟踪——这些量基本上是 gradients 的函数。其中有一阶矩（first moment）和二阶矩（second moment），基本上就是梯度和梯度平方的移动平均（moving average）。这些量，也就是 first moment 和 second moment，也需要以某种方式保存在内存里的某个地方。

### [30:00](https://www.youtube.com/watch?v=VlA_jt_3Qc4&t=1800s) · b000060

**English**

So it's a lot of things to save. Well, OK. Breaking news, memory is not unlimited. Memory is limited. And so here, what we have in front of us is the description of a GPU. I think. Yeah. H100, which is a very good GPU. And you will see in that description, there's a line on GPU memory. So GPU memory is your amount of memory per GPU. It's 80 gig for this one.

**中文**

所以，要保存的东西很多。好吧，告诉大家一个突发新闻：内存不是无限的，内存是有限的。我们眼前这张是一个 GPU 的规格说明。我想。对，是 H100，它是一款很好的 GPU。你会看到说明里有一行 GPU 内存（GPU memory）。GPU memory 就是每块 GPU 的内存容量。这款是 80 GB。

### [30:32](https://www.youtube.com/watch?v=VlA_jt_3Qc4&t=1832s) · b000061

**English**

It's quite large. So it's in on the order of tens of gigabytes. So you need to store all these things in 80 gigabytes, which is not a lot. So what are we doing? What will you be doing? So I guess the idea is to leverage not one but several GPUs in order to somehow distribute the load across CPUs. And in order to do that, you have several methods, which we will see in a second.

**中文**

这相当大了，是几十 GB 的数量级。不过，你需要把所有这些东西存进 80 GB，这又不算多。那么我们怎么办？你会怎么做？我想，办法是利用多块 GPU，而不是一块，以某种方式把负载分散到 CPUs \[字幕疑误，可能指 GPUs\] 上。为此，有几种方法，我们马上会看到。

### [31:08](https://www.youtube.com/watch?v=VlA_jt_3Qc4&t=1868s) · b000062

**English**

So the first set of methods is called data parallelism, also known as DP. So what this set of methods does is it distributes data across GPUs, so that this forward pass and backward pass, they can all be done independently. And so the idea here is to divide the batch of data across devices, and then in order to do that, of course, you need to have a copy of the model per device.

**中文**

第一类方法叫数据并行（data parallelism），也称 DP。这类方法会把数据分配到多个 GPUs 上，使 forward pass 和反向传播（backward pass）都能独立完成。这里的想法是，把一个 batch 的数据分到不同设备上。当然，为了做到这一点，每个设备都需要有一份模型副本。

### [31:47](https://www.youtube.com/watch?v=VlA_jt_3Qc4&t=1907s) · b000063

**English**

Because of course, you need to compute the activations. You need to compute all these things. But when you do that, you're are able to reduce the memory that is linked to the batch size. So that's called data parallelism. Yes.

**中文**

因为你当然需要计算 activations，需要计算所有这些东西。不过这样做，就能减少与 batch size 有关的内存占用。这就叫 data parallelism。嗯。

### [32:07](https://www.youtube.com/watch?v=VlA_jt_3Qc4&t=1927s) · b000064

**English**

Question is how about the gradient update? Well, it's a great question. So what do you do when you have independent computations here and there? Well, the gradient is just the average of the gradients for this thing. So you have some communication in between the GPUs that basically aggregates the gradient for the updates. So I have a question for you. Is this the answer to everything? If we just scale up like this for, I don't know, a lot of GPUs, is it great, always great or do we have cons?

**中文**

问题是，那梯度更新怎么办？好，这是个很好的问题。当各个地方都独立计算时，该怎么做？这里的梯度就是这些梯度的平均值。因此，GPUs 之间会进行一些通信，基本上就是聚合用于更新的梯度。我有个问题问大家：这能解决所有问题吗？如果我们就这样扩展到，不知道，很多块 GPUs，这样好吗？总是很好，还是也有缺点？

### [32:48](https://www.youtube.com/watch?v=VlA_jt_3Qc4&t=1968s) · b000065

**English**

Oh, yeah. Great point. So yeah, you have to fit one model. So yeah, this is a great point. So the second point that I will add is you have an additional cost, which is called communication cost, because you need to somehow communicate between your GPUs in order to aggregate some quantities. So your training is going to be slower. It's good. You can scale up the memory. Of course, you need to fit a model on a device, and we will see how we to do that.

**中文**

哦，对，很好的观点。是的，你得装得下一个模型。对，这一点很好。我再补充第二点：会有一项额外成本，叫通信成本（communication cost），因为你需要以某种方式在 GPUs 之间通信，来聚合一些量。所以训练会变慢。它有好处，可以扩大可用内存。当然，你需要在一个设备上装下一个模型，我们会看看怎么做。

### [33:18](https://www.youtube.com/watch?v=VlA_jt_3Qc4&t=1998s) · b000066

**English**

But you will be incurring those communication costs, so it's not all great. So speaking of the memory and the fact that we want to, I guess, be able to at least store a model per device. So people have realized that there's actually a lot of duplication. And there has been a paper on wanting to deduplicate this duplicate information and this method is called ZeRO, ZeRO redundancy optimization.

**中文**

但你会产生这些 communication costs，所以也不全是好处。说到内存，以及我们希望至少能在每个设备上存储一个模型这件事，人们发现其实存在很多重复信息。有一篇论文研究如何消除这些重复信息，这个方法叫 ZeRO，也就是零冗余优化（ZeRO redundancy optimization）。

### [34:01](https://www.youtube.com/watch?v=VlA_jt_3Qc4&t=2041s) · b000067

**English**

And the idea is that on each GPU, you store the same parameters, you store the same gradients, you store the same optimizer states. So the idea here is how about we shard, we partition those quantities across GPUs? So the first variation is around sharing the optimizer state.

**中文**

它的思路是，每块 GPU 上都存储相同的参数、相同的梯度、相同的优化器状态（optimizer states）。那么，能不能把这些量分片（shard）、分区到不同 GPUs 上呢？第一个变体是共享优化器状态（sharing the optimizer state）\[字幕疑误，可能指 sharding，即分片\]。

### [34:31](https://www.youtube.com/watch?v=VlA_jt_3Qc4&t=2071s) · b000068

**English**

So meaning, we partition those states across the GPUs. So this reduces the memory by a lot. We can also partition the gradients, and we can also partition the parameters. So here, we have no redundant information. Things are just partitioned. Well, the problem is you're going to have even more communication costs, but at least it allows for us to decrease the memory load on each GPU.

**中文**

也就是说，我们把这些状态分区到不同 GPUs 上，这能大幅减少内存占用。我们还可以对 gradients 分区，也可以对 parameters 分区。这样就没有冗余信息了，所有东西都只是被分区保存。问题是，通信成本会更高，但至少这样能降低每块 GPU 的内存负担。

### [35:07](https://www.youtube.com/watch?v=VlA_jt_3Qc4&t=2107s) · b000069

**English**

So this is ZeRO, so there's ZeRO 1, ZeRO 2, ZeRO 3. And I guess the variation that you will choose will be a function of how sensitive you are to, I guess, training time and how big is your model and whether this will be an actual problem, or are you just fine with just storing everything? So that's one set of methods. So this set of methods is, again, data parallelism.

**中文**

这就是 ZeRO，有 ZeRO 1、ZeRO 2、ZeRO 3。我想你会选择哪个变体，取决于你对训练时间有多敏感、模型有多大，以及这是否真的会成为问题，还是把所有东西都存下来对你而言就没问题。这是一类方法。再说一次，这类方法是 data parallelism。

### [35:39](https://www.youtube.com/watch?v=VlA_jt_3Qc4&t=2139s) · b000070

**English**

So it's basically you having independent sets of data that are handled by different GPUs. Well, you have another set of methods that's called model parallelism. So model parallelism tries to parallelize the operation even within one batch. So there's a bunch of methods. I don't want to sound too like a catalog. So we're not going through them all but one by one.

**中文**

基本上就是让不同 GPUs 处理相互独立的数据集合。还有另一类方法，叫模型并行（model parallelism）。model parallelism 尝试把运算并行化，甚至是在同一个 batch 内部。这里有很多方法。我不想讲得太像罗列目录，所以我们不会把它们全部都讲一遍，而是一个一个讲。

### [36:12](https://www.youtube.com/watch?v=VlA_jt_3Qc4&t=2172s) · b000071

**English**

But I will just call out a few that are worth noting. So if you remember last lecture, we talked about MOE-based LLMs and how sequences were being sent to different experts. Well, there is a way to distribute that across GPUs via this expert parallelism techniques, which is having, let's say, one expert on a device, another one on another device.

**中文**

不过，我会指出几个值得注意的方法。如果你还记得，上一讲我们讨论了基于 MOE 的 LLMs，以及序列如何被发送到不同专家。通过专家并行（expert parallelism）技术，可以把这些分配到不同 GPUs 上，比如在一个设备上放一个专家，在另一个设备上放另一个专家。

### [36:42](https://www.youtube.com/watch?v=VlA_jt_3Qc4&t=2202s) · b000072

**English**

So that's one thing worth noting. Another one, I will say, so a tensor parallelism is when you have big matrix multiplications to somehow cut that in a way that decreases the memory required for that. And maybe the last one I will say is pipeline parallelism. It's when you consider a forward pass as involving several layers. So you're going to say that one GPU is going to only be responsible for, let's say, layers 1 to 3 and then another one layer 3--sorry, 4 to 5, 4, 5, 6, and so on and so forth.

**中文**

这是一个值得注意的方法。另一个，我会说，张量并行（tensor parallelism）就是在遇到大型矩阵乘法时，以某种方式把它切分，从而降低所需内存。最后我想说的是流水线并行（pipeline parallelism）。也就是把一次 forward pass 看作涉及多个层，然后规定一块 GPU 只负责，比如第 1 到第 3 层，另一块负责第 3——抱歉，第 4 到第 5 层，第 4、5、6 层，以此类推。

### [37:25](https://www.youtube.com/watch?v=VlA_jt_3Qc4&t=2245s) · b000073

**English**

So you also have that kind of parallelism. But anyways, there's a bunch of techniques. And the ones that I mentioned they fall in the bucket of model parallelism.

**中文**

所以，也有这种并行方式。总之，有很多技术，而我提到的这些都属于 model parallelism。

### [37:38](https://www.youtube.com/watch?v=VlA_jt_3Qc4&t=2258s) · b000074

**English**

Make sense? No need to know the details on there. But I think just knowing that there are several methods and just a rough idea, I think, is a good thing to have in mind. Cool. So what did we do? So we realized that during the training process, we had to save a lot of things in memory. So what we saw was techniques that reduce the burden of having memory per GPU, so we are trying to distribute that across GPUs.

**中文**

能理解吗？不需要了解其中的细节。不过，我想知道有几种方法，并且有一个大致概念，是值得记住的。好。我们做了什么？我们发现，在训练过程中，需要把很多东西保存在内存中。于是，我们看到了一些减轻每块 GPU 内存负担的技术，尝试把这些分散到多个 GPUs 上。

### [38:13](https://www.youtube.com/watch?v=VlA_jt_3Qc4&t=2293s) · b000075

**English**

So we saw data parallelism and then the ZeRO method that has some extra optimizations. And we saw model parallelism as well. So now, we're going to see another technique that leverages the structure of the GPU. And you may have heard of this technique. It's called flash attention. It was actually developed here at Stanford in 2022.

**中文**

我们看了 data parallelism，以及带有一些额外优化的 ZeRO 方法，也看了 model parallelism。现在，我们要看另一种利用 GPU 结构的技术。你可能听说过，叫 flash attention（闪存注意力）。它实际上是 2022 年在这里，Stanford 开发的。

### [38:44](https://www.youtube.com/watch?v=VlA_jt_3Qc4&t=2324s) · b000076

**English**

And in order for me to talk to you about this technique, I want to tell you more about what the GPU is composed of. So if you look under the hood--well, GPU is very complicated and I'm for sure not--I don't know everything either. But what I know is that we have two kinds of memories in GPU. So you have one kind of memory that's big but relatively slow. That's in the HBM.

**中文**

为了介绍这项技术，我想进一步讲一下 GPU 的组成。如果看看它的内部——GPU 很复杂，我肯定也不是——我也不是什么都懂。但我知道，GPU 里有两种内存。一种容量大，但相对较慢，也就是高带宽内存（HBM）。

### [39:17](https://www.youtube.com/watch?v=VlA_jt_3Qc4&t=2357s) · b000077

**English**

And then another kind of memory that is fast but much, much smaller, which is on chip next to where the compute happens. That's called the SRAM. So you have HBM and SRAM. HBM has something around tens of gigabytes. So it's like the GPU memory that you saw in the description. SRAM is much smaller. It's like something around several tens of megabytes let's say.

**中文**

另一种内存速度很快，但容量小得多，位于芯片上，靠近进行计算的地方，叫静态随机存取存储器（SRAM）。所以，有 HBM 和 SRAM。HBM 的容量大约是几十 GB，就像你在规格说明里看到的 GPU memory。SRAM 小得多，大概是几十 MB。

### [39:49](https://www.youtube.com/watch?v=VlA_jt_3Qc4&t=2389s) · b000078

**English**

So it's much smaller, but then it is 10 times faster. So this one is a few terabytes per second let's say. And the SRAM is tens of terabytes per second. So it's a noticeable difference in speed. So what we want is to somehow leverage the strength of these kinds of memories in order to speed up the attention computation in an exact way.

**中文**

所以，它小得多，但速度快 10 倍。这个大概是每秒几 TB，而 SRAM 是每秒几十 TB。速度差异很明显。因此，我们希望以某种方式利用这两种内存的优势，以精确的方式加速注意力（attention）计算。

### [40:22](https://www.youtube.com/watch?v=VlA_jt_3Qc4&t=2422s) · b000079

**English**

So what do I mean by exact way? So what I mean is we're not making any approximations to the computation. What we're doing is we're just leveraging the strength of these components and sending the computation in a clever way. So if you remember, the self-attention computation is done with this very important formula. So it's softmax of queries and keys over some scaling factor times V.

**中文**

我说的精确方式是什么意思？就是说，我们不会对计算做任何近似。我们只是利用这些组件的优势，以巧妙的方式安排计算。如果你还记得，self-attention 计算使用的是这个非常重要的公式，也就是对查询（queries）和键（keys）除以某个缩放因子（scaling factor）后取 softmax，再乘以 V。

### [41:00](https://www.youtube.com/watch?v=VlA_jt_3Qc4&t=2460s) · b000080

**English**

So this allows queries to interact with everyone else. So in matrix form, you can think of queries as having the number of rows equal to the sequence length. And then columns to being the dimension of the query. And then same for key and value. So you have this big matrix multiplications. So if you do it--if you do this computation, the standards the vanilla way, what you would do is store them in the big but slow memory component of the GPU.

**中文**

这让 queries 能够与其他所有对象交互。用矩阵形式来看，queries 的行数等于序列长度，列数是 query 的维度。键（key）和值（value）也一样。因此，你有这些大型矩阵乘法。如果按照标准的、最普通的方式计算，你会把它们存储在 GPU 中容量大但速度慢的内存组件里。

### [41:43](https://www.youtube.com/watch?v=VlA_jt_3Qc4&t=2503s) · b000081

**English**

So you would store it in the HBM. So here is what you would do if you were to not do any optimization. So you would take those matrices from the big but slow HBM, perform the computation, and then write it back to the HBM. And then you would read that result again from the HBM, compute the softmax, and then write it back to the HBM.

**中文**

也就是存储在 HBM 中。如果不做任何优化，你会这样操作：从容量大但速度慢的 HBM 中取出这些矩阵，执行计算，再写回 HBM。然后，再从 HBM 读取结果，计算 softmax，再写回 HBM。

### [42:16](https://www.youtube.com/watch?v=VlA_jt_3Qc4&t=2536s) · b000082

**English**

And then you would again load this plus the value matrix, multiply them, and then write them to the HBM. See, there's a lot read and write to the HBM. So it's a lot of data transfer, which actually becomes the bottleneck. So a GPU is very, very fast, but then you spend a lot of time just loading your matrices from the memory. The reason why you do that is because of this softmax operation.

**中文**

然后，你会再次加载这个结果和 value 矩阵，将它们相乘，再写入 HBM。你看，这里有大量对 HBM 的读写。因此，数据传输很多，实际上会成为瓶颈。GPU 非常非常快，但你却花了很多时间从内存中加载矩阵。之所以这样做，是因为这个 softmax 运算。

### [42:51](https://www.youtube.com/watch?v=VlA_jt_3Qc4&t=2571s) · b000083

**English**

So do you remember what a softmax does? So it normalizes the quantities, so that they sum to 1. But it's row dependent meaning that each row needs to sum up to 1. So in a sense, you need that computation to happen first before you do your softmax. If you just look at it like that, you would think, yeah, you need to do the whole thing first.

**中文**

大家还记得 softmax 做什么吗？它会对这些量进行归一化（normalization），让它们的和为 1。不过，它是按行处理的，也就是说，每一行的和都需要为 1。所以从某种意义上说，你需要先完成那个计算，才能做 softmax。如果只是这样看，你会觉得，是的，必须先把整个计算都做完。

### [43:22](https://www.youtube.com/watch?v=VlA_jt_3Qc4&t=2602s) · b000084

**English**

Well, it turns out that you don't need to do everything at once. And this is the core idea behind flash attention. So what flash attention does is it tries to minimize the amount of read and write from and to the HBM and instead takes small blocks--and it's called tiling, the method is called tiling. It takes small blocks that it sends to the SRAM, so that it gets computed from end to end before being sent back to the HBM.

**中文**

但事实证明，不需要一次把所有东西都算完。这就是 flash attention 的核心思想。flash attention 尝试尽量减少对 HBM 的读写量，而是取出小块——这个方法叫分块（tiling）。它把小块送到 SRAM，让它们完成端到端计算，然后再送回 HBM。

### [44:05](https://www.youtube.com/watch?v=VlA_jt_3Qc4&t=2645s) · b000085

**English**

Does that make sense? So the idea is let's send small matrices into the SRAM, so that it does the whole full end-to-end computation and just send it back to the HBM, because we want to minimize the amount read and write from the HBM. So here is how you would do it. So you remember, the softmax computation with the query and the key and then the value. Well, what you would do is to cut your matrices and then proceed step by step.

**中文**

能理解吗？想法就是，把小矩阵送进 SRAM，在那里完成整个端到端计算，然后再送回 HBM，因为我们希望尽量减少对 HBM 的读写量。具体可以这样做。还记得吗，先对 query 和 key 做 softmax 相关的计算，然后再用 value。你要做的，就是切分矩阵，然后一步一步进行。

### [44:46](https://www.youtube.com/watch?v=VlA_jt_3Qc4&t=2686s) · b000086

**English**

But then there's a cool trick that I want to talk to you about, which is that you don't need to compute the whole matrix inside a softmax in order to achieve the whole softmax computation. Because if you think about it, let's suppose you have a whole matrix, and then you have different, let's say, columns or submatrices, S1 to SN, well, softmax of this huge matrix is equal to this matrix, where the softmax is taken with respect to each of these submatrices up to some scaling factor.

**中文**

不过，我想介绍一个很巧妙的技巧：你不需要把 softmax 里面的整个矩阵都计算出来，才能完成整个 softmax 计算。因为想一想，假设你有一个完整矩阵，然后把它分成不同的列或者子矩阵，比如 S1 到 SN，那么对这个大矩阵做 softmax，等于这个矩阵，其中分别对各个子矩阵做 softmax，再加上某个缩放因子的调整。

### [45:26](https://www.youtube.com/watch?v=VlA_jt_3Qc4&t=2726s) · b000087

**English**

So this is the core trick. And if you want to be convinced of it, just look at the softmax formula, it's exponential of something over some quantity, which is shared across the row. So this scaling factor will just fix this with respect to that. So with this in mind, what we will do is take each respective slices of this matrices, do the whole computation, and then populate the corresponding entry in the output matrix.

**中文**

这就是核心技巧。如果你想确信这一点，只要看一下 softmax 公式：分子是某个值的指数，分母是同一行共享的某个量。因此，这个 scaling factor 就能对此进行修正。有了这个想法，我们会取出这些矩阵各自的切片，完成整个计算，然后填入输出矩阵中的对应项。

### [46:07](https://www.youtube.com/watch?v=VlA_jt_3Qc4&t=2767s) · b000088

**English**

So we will do that between, let's say, the first slice of the query and the first slice of the keys and the values. And then we will repeat for the other slice until the end. And then we will repeat for the other queries as well until the end. So what the paper explains is how this scaling factor is being computed. So this one is some formula that I did not put on the slide, so it's not necessary for you to memorize the formula.

**中文**

比如，我们会对 query 的第一个切片，以及 keys 和 values 的第一个切片进行这个操作。然后对其他切片重复，一直到最后。接着，对其他 queries 也重复这个过程，一直到最后。论文解释的就是如何计算这个 scaling factor。它有一个公式，我没有放在幻灯片上，所以大家不需要记住这个公式。

### [46:40](https://www.youtube.com/watch?v=VlA_jt_3Qc4&t=2800s) · b000089

**English**

It's just the idea. And the idea is exactly this trick.

**中文**

只需要理解这个想法，而这个想法恰恰就是这个技巧。

### [46:47](https://www.youtube.com/watch?v=VlA_jt_3Qc4&t=2807s) · b000090

**English**

So once you do that, you basically end up with only one read from the HPM. And these \[INAUDIBLE\] quantities are stored in the SRAM. And then they're read from the SRAM, which is very fast, and then computed, and then back to the SRAM. And then at the end, in order to accumulate the results, they're being sent back to the HBM.

**中文**

这样做之后，基本上就只需要从 HPM \[字幕疑误，可能指 HBM\] 读取一次。这些\[听不清\]量存储在 SRAM 中，然后从速度很快的 SRAM 中读取，进行计算，再放回 SRAM。最后，为了累积结果，再把它们送回 HBM。

### [47:18](https://www.youtube.com/watch?v=VlA_jt_3Qc4&t=2838s) · b000091

**English**

So just to make sure we're clear. So in green, it's basically when it's read from SRAM, and then in blue, it's from the HBM. You have a question? Yeah. \[AUDIO OUT\]

**中文**

再确认一下大家都理解了：绿色基本上表示从 SRAM 读取，蓝色表示从 HBM 读取。你有问题吗？嗯。\[音频缺失\]

### [47:41](https://www.youtube.com/watch?v=VlA_jt_3Qc4&t=2861s) · b000092

**English**

The question is, do you take the whole row or a portion of it? So you can take a portion of it. But just for illustrative purposes, here we take the exclusive. This is just for illustrative purposes. You can think of your matrix as being completely a grid. And then you just multiply accordingly. But yeah, this is just for illustrative purposes. Yeah.

**中文**

问题是，你取的是整行，还是其中一部分？可以取其中一部分。不过，这里只是为了说明，我们取 exclusive \[字幕疑误，含义不明\]。这只是为了说明。你可以把矩阵想成一个完整的网格，然后按对应关系做乘法。不过，这里只是为了说明。嗯。

### [48:12](https://www.youtube.com/watch?v=VlA_jt_3Qc4&t=2892s) · b000093

**English**

Yeah. So the question is, are you computing alpha and all these quantities on the fly or do you have some estimation? So all of this is exact, and they're computed in an iterative basis. So the way it works is when you populate the output, you will keep on having some extra quantity that will adjust for that. Think of it as just some formula that works. So yeah, I highly recommend looking at the paper. They actually explicit that quite a lot.

**中文**

对。问题是，alpha 和所有这些量是即时计算的，还是有某种估计？所有这些都是精确的，而且是迭代计算出来的。具体来说，在填充输出时，你会持续保留一些额外的量，用于进行调整。你可以把它理解为一个有效的公式。所以，我非常推荐大家看看论文。他们实际上对此解释得相当详细。

### [48:44](https://www.youtube.com/watch?v=VlA_jt_3Qc4&t=2924s) · b000094

**English**

So the paper is Flash Attention, fast and memory efficient exact attention with IO awareness. All of the links are in the slides. But yeah, I highly recommend just looking at the exact formula in case you want to be convinced. Cool. But the idea makes sense overall?

**中文**

这篇论文是 Flash Attention, fast and memory efficient exact attention with IO awareness \[字幕疑误，可能指 FlashAttention: Fast and Memory-Efficient Exact Attention with IO-Awareness\]。所有链接都在幻灯片里。如果你想确信这一点，我非常推荐去看一下确切的公式。好。不过，总体上能理解这个想法吗？

### [49:02](https://www.youtube.com/watch?v=VlA_jt_3Qc4&t=2942s) · b000095

**English**

Any questions on this?

**中文**

对此有什么问题吗？

### [49:06](https://www.youtube.com/watch?v=VlA_jt_3Qc4&t=2946s) · b000096

**English**

Cool. Well, this was flash attention, but there's actually another idea from the paper. So this was only the first idea, which was around making the attention computation faster. The second idea is given that the attention computation is faster, now let's try to be smarter about the backwards pass, because when you compute in the backwards pass, when you compute the gradient of the loss with respect to a parameter, the chain rule will surface some activations that you need to have in memory.

**中文**

好。这就是 flash attention，不过论文里其实还有另一个想法。刚才只是第一个想法，也就是让 attention 计算更快。第二个想法是，既然 attention 计算更快了，那我们就尝试更聪明地处理 backwards pass。因为在 backwards pass 中计算 loss 对某个参数的梯度时，链式法则（chain rule）会涉及一些需要保存在内存中的 activations。

### [49:52](https://www.youtube.com/watch?v=VlA_jt_3Qc4&t=2992s) · b000097

**English**

Well, here, given that computing these activations is very fast, one idea is to just not store activations from the forward pass or at least not store everything, but instead in the backwards pass, compute these activations again.

**中文**

这里，既然计算这些 activations 非常快，一个想法就是不保存 forward pass 中的 activations，或者至少不全部保存，而是在 backwards pass 中重新计算这些 activations。

### [50:15](https://www.youtube.com/watch?v=VlA_jt_3Qc4&t=3015s) · b000098

**English**

So it's called the recomputation. So when you do the forward pass, you compute an activation to be able to compute the loss, but then instead of saving it to reuse it during the gradient update, you will just discard it and then recompute the activation during the backwards pass with this very fast technique. And when you do that, it's actually quite remarkable. So you do more operations.

**中文**

这叫重计算（recomputation）。进行 forward pass 时，你计算一个 activation，以便计算 loss，但之后不会把它保存下来供梯度更新时复用，而是把它丢弃，再在 backwards pass 中用这种非常快的技术重新计算。这样做的效果其实相当惊人。你执行的运算会更多。

### [50:48](https://www.youtube.com/watch?v=VlA_jt_3Qc4&t=3048s) · b000099

**English**

So gigaFLOPs is just a derivative of FLOPs. So it's the number of operations you're doing. So with flash attention, you're doing more operations because you're actually recomputing things. But then so you also see fewer read and writes from the HBM. So here, for instance, it was 40.3 in the standard way and then 4 point-- so it's like almost a 10x reduction. But then you see that the runtime is also smaller. So this is very remarkable because usually, when you recompute things, you are saving memory but at the expense of runtime.

**中文**

gigaFLOPs 只是 FLOPs 的一个衍生单位，表示执行的运算次数。使用 flash attention 时，运算次数会更多，因为你确实在重新计算一些东西。不过，你也会看到，对 HBM 的读写更少了。比如这里，标准方式是 40.3，然后是 4 点——所以几乎减少到十分之一。而且，你会看到运行时间（runtime）也更短了。这非常惊人，因为通常 recomputation 是通过增加 runtime 来节省内存的。

### [51:30](https://www.youtube.com/watch?v=VlA_jt_3Qc4&t=3090s) · b000100

**English**

You're just taking longer. But here, you're not only taking less amount of time, you're also saving memory. So you're basically having everything. It's the best of all worlds. So this is what flash attention mentioned. So you will see that there are some other, I guess, variants of flash attention. So flash attention 2, flash attention 3. And I would say that these are more adaptation of these methods to the current infra, because each new GPU comes with new pros and cons, so strengths and weaknesses.

**中文**

也就是花更长时间。但在这里，你不仅用时更少，还节省了内存。所以，基本上你什么好处都得到了，各方面都占优。这就是 flash attention 提到的内容。你会看到 flash attention 还有一些其他变体，比如 flash attention 2、flash attention 3。我会说，这些更多是在让这些方法适应当前的基础设施，因为每一代新 GPU 都有新的优缺点，也就是长处和短处。

### [52:06](https://www.youtube.com/watch?v=VlA_jt_3Qc4&t=3126s) · b000101

**English**

And I guess there's always a way to make these optimizations better. But yeah, I would say flash attention is quite a common trick, and I think it's a very good thing to. So does that make sense?

**中文**

我想，总有办法把这些优化做得更好。不过，我会说 flash attention 是一种相当常见的技巧，而且我觉得这是一个非常好的东西，值得去。这样能理解吗？

### [52:25](https://www.youtube.com/watch?v=VlA_jt_3Qc4&t=3145s) · b000102

**English**

Cool. I'll take that as a yes. OK. Cool. OK, so last thing--no, we have a few things that I want to talk to you about. So you have your LLM with a bunch of weights. These weights are all floating points. So you can think of them as just being numbers with a bunch of numbers after the decimal. One natural question you can ask yourself is, do you really need to know that much precision after the decimal point to be able to do a good job?

**中文**

好，我就当大家都理解了。好。好。最后一件事——不，还有几件事我想讲。你的 LLM 有很多权重，这些权重都是浮点数。你可以把它们理解为小数点后有很多位数字的数。一个很自然的问题是：为了达到好的效果，真的需要知道小数点后那么高的精度吗？

### [53:01](https://www.youtube.com/watch?v=VlA_jt_3Qc4&t=3181s) · b000103

**English**

I guess put another way, can you just cut your precision in some way to save on memory but then keep the same performance? So this is the idea behind quantization. So quantization is the process of converting the precision of a number from, let's say, one setting to another. In order to better understand that, I think it's important to know how floating points--sorry, floating point numbers, how they are encoded.

**中文**

换个说法，能不能以某种方式降低精度，节省内存，同时保持相同的性能？这就是量化（quantization）背后的想法。quantization 是将一个数的精度从某种设置转换到另一种设置的过程。为了更好地理解这一点，我想有必要了解浮点——抱歉，浮点数是如何编码的。

### [53:40](https://www.youtube.com/watch?v=VlA_jt_3Qc4&t=3220s) · b000104

**English**

So in practice, they're just a bunch of bits. And here, you have some bits that are responsible for, let's say, the exponent, some that are responsible for the mantissa, which is basically how granular your number is. And then one that is about the sign. So you have a bunch of representations of floats. So the most common ones are in this table. So you have so single point precision, half precision, floating point 64, brain float 16 that are each having different granularities for the three dimensions.

**中文**

实际中，它们就是一组比特（bits）。其中有些 bits 负责指数（exponent），有些负责尾数（mantissa），后者基本上决定数值的精细程度，还有一个负责符号（sign）。浮点数有多种表示形式，最常见的几种列在这张表里，包括单点精度（single point precision）\[字幕疑误，可能指 single precision，即单精度\]、半精度（half precision）、floating point 64、brain float 16，它们在这三个方面各有不同的精细程度。

### [54:23](https://www.youtube.com/watch?v=VlA_jt_3Qc4&t=3263s) · b000105

**English**

So if we take the first two rows, which are the two most common representations that you will see out there, floating point 16 is only represented on 16 bits compared to 32. So it takes basically half the memory if you want to think about it this way. But then it's less precise, meaning it's less granular. So I guess one idea that we could have is to somehow decrease the granularity of these weights and these numbers, hoping that it will not impact performance too much.

**中文**

如果看前两行，也就是最常见的两种表示形式，floating point 16 只用 16 bits 来表示，相比之下另一种是 32 bits。所以你可以认为，它基本上只占用一半内存。但它的精度更低，也就是不那么精细。因此，一个想法是，以某种方式降低这些权重和数值的精细程度，希望不会对性能产生太大影响。

### [55:03](https://www.youtube.com/watch?v=VlA_jt_3Qc4&t=3303s) · b000106

**English**

So another thing that I want to mention is back to that GPU description. You see that there is also a bunch of information around the compute speed. So I'm not sure if you can see very well on there. Can you see very well on the slide? So I'll read it. The compute speed as a function of which representation you're using. So here, if you're using FP64, which is this super granular way of representing numbers, you only have 34 teraFLOPs of compute speed.

**中文**

我还想提一点，再看一下 GPU 的规格说明。你会看到，还有很多关于计算速度的信息。我不确定大家能不能看清。幻灯片上看得清吗？我来读一下：计算速度取决于你使用哪种表示形式。这里，如果使用 FP64，也就是这种非常精细的数值表示方式，计算速度只有 34 teraFLOPs。

### [55:38](https://www.youtube.com/watch?v=VlA_jt_3Qc4&t=3338s) · b000107

**English**

But then if you're using a, let's say, FP32, which is half of it, you can double your compute speed and so on. You have all these other numbers as well. So the idea is you can save on memory. You can also go faster.

**中文**

但如果使用，比如 FP32，它只有一半，那么计算速度就可以翻倍，以此类推。这里还有其他这些数字。所以，想法就是，你既能节省内存，也能提高速度。

### [55:59](https://www.youtube.com/watch?v=VlA_jt_3Qc4&t=3359s) · b000108

**English**

So with this in mind, I just want to touch on one last technique before giving it to Shervin, which is mixed precision training. So the idea behind mixed precision training is to leverage different granularities of float representations such that it will not hurt the performance too much but allow you to save on memory and do things faster.

**中文**

有了这个认识，在把时间交给 Shervin 之前，我想简要介绍最后一项技术：混合精度训练（mixed precision training）。mixed precision training 的想法是，利用不同精细程度的浮点表示形式，在不太损害性能的情况下，节省内存并加快计算。

### [56:31](https://www.youtube.com/watch?v=VlA_jt_3Qc4&t=3391s) · b000109

**English**

So the idea behind mixed precision training is you have your models or you have your model, you keep your weights in high precision, so FP32, and all the operations that you do in the forward and backward pass, you're going to do it in a lower precision. So in this case, FP16. But then the weight updates will be done still in FP32.

**中文**

mixed precision training 的想法是，你有一些模型，或者说一个模型，把权重保留为高精度，也就是 FP32，而 forward pass 和 backward pass 中的所有运算都用较低精度进行。在这个例子中，就是 FP16。但权重更新仍然用 FP32 进行。

### [57:04](https://www.youtube.com/watch?v=VlA_jt_3Qc4&t=3424s) · b000110

**English**

So the authors of the paper, when they did that, basically what they realized was the performance was not degraded too much. But then you had a lot of savings on memory and then it was running faster. So now you may wonder, well, why are you keeping the weights at a high precision but not the activations and so on? So I can offer you just a bit of intuition. So whenever you perform a forward pass, you're performing that on a set of data.

**中文**

论文作者这样做之后，基本上发现，性能没有下降太多，但节省了大量内存，而且运行得更快。现在你可能会想，为什么权重保持高精度，而 activations 等不需要？我可以提供一点直观理解。每次进行 forward pass 时，你都是在一组数据上计算。

### [57:39](https://www.youtube.com/watch?v=VlA_jt_3Qc4&t=3459s) · b000111

**English**

But that set of data can be noisy in itself. So maybe all the decimal points after--so all the numbers after the decimal point may not be as useful. So you can think of this update as being more in which direction should the weights go to a more optimal state. So it doesn't require them to be super precise, but then it's much more important to keep your weights, so the weights of the model in high precision in order to not accumulate errors due to quantization.

**中文**

但这组数据本身可能就有噪声。所以，小数点后的所有——也就是小数点后的那些数字，可能没那么有用。你可以把这种更新理解为，更多是在判断权重应该向哪个方向移动，才能达到更优的状态。因此，它们不需要特别精确。但把权重，也就是模型的权重，保持为高精度要重要得多，这样才能避免因 quantization 而累积误差。

### [58:18](https://www.youtube.com/watch?v=VlA_jt_3Qc4&t=3498s) · b000112

**English**

That's one way just think about it. But the long story short is if you reduce the granularity of some numbers, then you will have a lot of benefits and not a lot of disadvantages in terms of the performance.

**中文**

这是一种理解方式。长话短说，如果降低某些数值的精细程度，就能获得很多好处，而在性能方面没有太多不利影响。

### [58:36](https://www.youtube.com/watch?v=VlA_jt_3Qc4&t=3516s) · b000113

**English**

Cool. Yeah.

**中文**

好。嗯。

### [58:52](https://www.youtube.com/watch?v=VlA_jt_3Qc4&t=3532s) · b000114

**English**

That's a great question. So the question is, do you apply this technique to all weights of all layers or just to some of them? So there has been a lot of papers on that. And the answer is there are some variations to it. And so the answer is not necessarily. So I do have some pointers. Happy to share them with you. But some parts may be more important than others. So this strategy is a little bit a high level idea, but there are always some variations from setup to setup.

**中文**

这是个很好的问题。问题是，这项技术会应用到所有层的所有权重，还是只应用到其中一部分？关于这个问题已经有很多论文。答案是，它有一些变体，所以答案是不一定。我确实有一些参考资料，很乐意分享给你。不过，有些部分可能比其他部分更重要。所以，这个策略是一个比较高层次的想法，但不同设置总会有一些变化。

### [59:30](https://www.youtube.com/watch?v=VlA_jt_3Qc4&t=3570s) · b000115

**English**

Yeah.

**中文**

嗯。

### [59:35](https://www.youtube.com/watch?v=VlA_jt_3Qc4&t=3575s) · b000116

**English**

So is your question that people rely on the relationship between compute--and sorry, not compute, parameters and token from the Chinchilla paper, but it may be different from their setup which may introduce something-- this is basically your question?

**中文**

所以，你的问题是，人们依赖 Chinchilla 论文中计算量之间的关系——抱歉，不是计算量，是参数和 token 之间的关系，但它可能与他们自己的设置不同，从而可能引入一些——基本上是这个问题吗？

### [1:00:01](https://www.youtube.com/watch?v=VlA_jt_3Qc4&t=3601s) · b000117

**English**

So the question is, is there also an optimal precision to use? So I would say, people use different things. There's not like a set way where everyone does something. But I would say that these scaling, like this Chinchilla law, is actually something that some authors, they try to reproduce for their own model. So actually, for instance, the Llama 3 paper, there's a whole part around trying to have some relationship between given a fixed amount of compute, what is the optimal number of tokens and then a number of parameters that is unique to their setup.

**中文**

问题是，是否也存在一个最优的使用精度？我会说，人们采用不同的做法，并没有一种大家都遵循的固定方式。不过，我会说，这些缩放关系（scaling），比如 Chinchilla law，确实是一些作者会尝试针对自己模型复现的东西。比如 Llama 3 论文，有一整部分是在尝试建立一种关系：给定固定计算量，对他们独有的设置而言，最优 token 数量和参数数量是多少。

### [1:00:46](https://www.youtube.com/watch?v=VlA_jt_3Qc4&t=3646s) · b000118

**English**

So what people do is they do this thing themselves on a small amount of training set and on smaller models, so that it doesn't cost them too much. They try to see what the relationship is for their setup, and then they extrapolate. And I believe that's how Llama 3--so I think there's a model that--so Llama 3, 405 billion parameters. I think they had the whole section just justifying that they came up to this number with some experiments that they run. So to your question, I think it highly depends on the kind of model that someone is training.

**中文**

人们会先用少量训练数据和较小的模型，自己做这些实验，这样成本不会太高。他们尝试找出适用于自己设置的关系，然后进行外推（extrapolate）。我相信 Llama 3 就是这样——我想有一个模型——Llama 3，4050 亿个参数。我记得他们用了一整节来说明，是通过运行一些实验才得出这个数字的。所以，针对你的问题，我认为这在很大程度上取决于训练的模型类型。

### [1:01:20](https://www.youtube.com/watch?v=VlA_jt_3Qc4&t=3680s) · b000119

**English**

And they'll probably have this analysis, I guess, with respect to their own setup. Does that answer your question? Cool. Cool. OK. Great. Yeah.

**中文**

我想，他们可能会针对自己的设置做这种分析。这回答了你的问题吗？好。好。好的。很好。嗯。

### [1:01:49](https://www.youtube.com/watch?v=VlA_jt_3Qc4&t=3709s) · b000120

**English**

The question is, is there something you can do about the range? So there are several types of quantization. We're not going into details here, but I can give you a ZeRO point quantization and absmax quantization, which are different techniques that play with these ranges. There's also quantization technique that Shervin will cover that also talks about that. So yeah, stay tuned for this. But I think ZeRO point quantization and absmax are ones that maybe you can look into for this.

**中文**

问题是，对于数值范围（range），有没有什么办法？quantization 有几种类型。这里不展开细节，不过我可以给你举出 ZeRO point quantization \[字幕疑误，可能指 zero-point quantization，即零点量化\] 和绝对最大值量化（absmax quantization），它们是处理这些范围的不同技术。Shervin 还会介绍一种 quantization 技术，也涉及这个问题。所以，敬请期待。不过，我想 ZeRO point quantization 和 absmax 可能是你可以针对这个问题了解的方法。

### [1:02:19](https://www.youtube.com/watch?v=VlA_jt_3Qc4&t=3739s) · b000121

**English**

Cool. So with that, I'm going to give it to Shervin.

**中文**

好。那么接下来，我把时间交给 Shervin。

### [1:02:27](https://www.youtube.com/watch?v=VlA_jt_3Qc4&t=3747s) · b000122

**English**

Thank you, Afshin. So now, we have seen how a pre-training worked. We're going to see together the next stages of training. So as we saw with Afshin, pre-training was a way to build the intuition to the model about how language was constructed and about the main characteristics of what is contained in the training data. That is general enough. So this is why we had corpuses that spans huge corpora of texts that are typically of the size of what you find on the internet.

**中文**

谢谢你，Afshin。现在，我们已经了解了预训练（pre-training）是如何进行的。接下来，我们一起看看训练的后续阶段。正如我们刚才跟着 Afshin 看到的，pre-training 是一种让模型建立直觉的方法，让它了解语言是如何构成的，以及训练数据中所包含内容的主要特征。这些都足够通用。所以，我们使用的语料涵盖了庞大的文本语料库，其规模通常相当于你在互联网上能找到的文本规模。

### [1:03:02](https://www.youtube.com/watch?v=VlA_jt_3Qc4&t=3782s) · b000123

**English**

So typically, very large and raw and conveying aspects of language. So now, you might want to ask yourself, how can we make such knowledge actually helpful? So this is something that we're going to discuss just in a second. But before we discuss about what could motivate further training, I want to come back to some very simple example that will surface what could be such a need.

**中文**

所以通常，它们规模非常大、未经处理，并且传达了语言的各个方面。现在，你可能想问自己，怎样才能让这些知识真正有用？这就是我们马上要讨论的内容。不过，在讨论进一步训练的动机之前，我想回到一个非常简单的例子，它会展示这种需求可能是什么。

### [1:03:36](https://www.youtube.com/watch?v=VlA_jt_3Qc4&t=3816s) · b000124

**English**

So let's take our favorite example about our teddy bear. And let's say, we have a very practical use case. So we have thoroughly loved our teddy bear. But now, it has become a bit dirty, so we need to wash it. And you might want to ask your favorite LLM if you can put it in the washer. So with the description that Afshin mentioned of LLM pre-training, I wanted to ask you all what was your opinion about what could the output to this be.

**中文**

我们来看看最喜欢的泰迪熊例子。假设我们有一个非常实际的使用场景。我们一直非常喜爱这只泰迪熊，但现在它变得有点脏了，所以需要洗一洗。你可能想问问你最喜欢的大语言模型（large language model，LLM），能不能把它放进洗衣机。根据 Afshin 对 LLM pre-training 的描述，我想问问大家，你们觉得它可能会输出什么？

### [1:04:11](https://www.youtube.com/watch?v=VlA_jt_3Qc4&t=3851s) · b000125

**English**

So any guesses?

**中文**

有人猜猜吗？

### [1:04:15](https://www.youtube.com/watch?v=VlA_jt_3Qc4&t=3855s) · b000126

**English**

Yep.

**中文**

对。

### [1:04:21](https://www.youtube.com/watch?v=VlA_jt_3Qc4&t=3861s) · b000127

**English**

Yeah. Yeah. Excellent. Yeah. So the answer, the guess was maybe another question. So I think that is a great guess that could definitely be it. So here, in the example, we put some other sentence that could be likely, but the gist is the same. It has been trained on next token prediction, not being an assistant or someone that is helpful to you. So this is why it will try to mimic what could be the pattern here and what could be potential likely next words.

**中文**

对，对，非常好。对。刚才的回答，或者说猜测是，可能会再给出一个问题。我觉得这是个很好的猜测，完全有可能。在这里的例子中，我们放了另一个可能出现的句子，但核心意思是一样的。它接受的训练是预测下一个词元（next token prediction），而不是成为助手或对你有帮助的对象。所以，它会尝试模仿这里可能存在的模式，以及接下来可能出现哪些词。

### [1:04:53](https://www.youtube.com/watch?v=VlA_jt_3Qc4&t=3893s) · b000128

**English**

So for example, the example we put here is something that relates to how the teddy bear is composed of. And because it's in the same domain as teddy bear and then when you talk about washer, then maybe it has been trained on data that includes materials of teddy bears. So that could be it. And I have a question with you all. Are you happy with it?

**中文**

例如，我们这里放的例子涉及泰迪熊是由什么构成的。因为它与泰迪熊属于同一个领域，而且当你谈到洗衣机时，它可能恰好在包含泰迪熊材料信息的数据上训练过。所以，它可能会这样回答。我想问大家一个问题：你们对此满意吗？

### [1:05:25](https://www.youtube.com/watch?v=VlA_jt_3Qc4&t=3925s) · b000129

**English**

No. Yeah. Exactly. So this is why we're going to see what we can do with the model to make it helpful to you. And this stage is called fine tuning. So we're going to see that it enables us to, in the general case of LLMs, make the LLM a helpful assistance, but also, if you have a specific use case, you can also use this technique to tune the general representation of the language towards your task of interest.

**中文**

不满意。对，没错。所以，我们接下来要看看，可以对模型做些什么，让它对你有帮助。这个阶段叫作微调（fine tuning）。我们会看到，对于一般的 LLM，它能让 LLM 成为有用的助手；而如果你有特定的使用场景，也可以利用这种技术，把通用的语言表示调整到你所关注的任务上。

### [1:06:02](https://www.youtube.com/watch?v=VlA_jt_3Qc4&t=3962s) · b000130

**English**

But we're going to focus first on what is done for LLMs in general. So first, I want to define some terms. So model fine tuning is commonly known as SFT. SFT is short for supervised fine tuning. So the supervised part suggests that we need some labels. And it's actually the case. So it's pairs of inputs and outputs that we provide the model to be trained on.

**中文**

不过，我们先重点看看 LLM 通常会做些什么。首先，我想定义几个术语。模型 fine tuning 通常被称为 SFT。SFT 是监督微调（supervised fine tuning）的缩写。其中的“监督”意味着我们需要一些标签，实际也确实如此。我们向模型提供成对的输入和输出，供它训练。

### [1:06:34](https://www.youtube.com/watch?v=VlA_jt_3Qc4&t=3994s) · b000131

**English**

And this is why it's called supervised. And then fine tuning is the term that refers to refining the weights that have been already trained. So you start from the pre-trained weights, and you further train the model on additional data to get a fine tuned model. And then one interesting note that I will tell you all is that the objective function, even though it's the same, will differ a bit from the pre-training task.

**中文**

这就是它被称为“监督”的原因。而 fine tuning 指的是对已经训练过的权重进行进一步调整。所以，你从预训练权重出发，用额外的数据继续训练模型，得到一个经过 fine tuning 的模型。接下来，我想告诉大家一个有趣的点：目标函数（objective function）虽然相同，但与 pre-training 任务相比，还是会有一点区别。

### [1:07:09](https://www.youtube.com/watch?v=VlA_jt_3Qc4&t=4029s) · b000132

**English**

So in the pre-training task, you start with the BOS token, beginning of sentence, and you fit all your corpora of data trying to predict the next token. But here, since we have this supervised fine tuning setup, where you want the model to do something useful in cases of interest, so let's say, when I ask the model about washing my teddy bear, so washing my teddy bear is actually an input that I give to the model.

**中文**

在 pre-training 任务中，你从 BOS token，也就是句首（beginning of sentence）词元开始，用全部语料数据进行拟合，尝试预测下一个 token。但在这里，我们采用的是 supervised fine tuning 设置，希望模型在关注的场景中做一些有用的事。比如，当我向模型询问清洗泰迪熊的问题时，清洗泰迪熊这件事实际上就是我给模型的输入。

### [1:07:39](https://www.youtube.com/watch?v=VlA_jt_3Qc4&t=4059s) · b000133

**English**

It's fixed. I don't want the model to parrot what I say. I want the model to be a helpful assistance to what I conditioned it on. So in this setup, the input is not a location where you would predict the next token. You would not do teacher forcing on it but rather start from this input and then predict the next token onwards. And then you're going to tune what the optimal distribution of next token can be based on this input.

**中文**

它是固定的。我不希望模型鹦鹉学舌般重复我的话。我希望模型能针对我给它的条件提供有用的帮助。所以，在这种设置中，输入部分不是你要预测下一个 token 的位置。你不会在输入部分做教师强制（teacher forcing），而是从这个输入出发，接着预测后面的 token。然后，你会根据这个输入，调整下一个 token 的最优分布。

### [1:08:13](https://www.youtube.com/watch?v=VlA_jt_3Qc4&t=4093s) · b000134

**English**

So any questions on the overall idea of SFT before we dive in a bit deeper? Yep.

**中文**

在我们进一步深入之前，大家对 SFT 的总体思路有什么问题吗？请说。

### [1:08:24](https://www.youtube.com/watch?v=VlA_jt_3Qc4&t=4104s) · b000135

**English**

So the question is we don't put a loss over the input. That's right. So you start from the input, and you start predicting the next token. And then the loss calculation starts from there.

**中文**

问题是，我们不在输入上计算损失（loss）。没错。你从输入出发，开始预测下一个 token，然后从那里开始计算 loss。

### [1:08:38](https://www.youtube.com/watch?v=VlA_jt_3Qc4&t=4118s) · b000136

**English**

Everything good? OK. So what I was just telling you is that SFT can be done to tune your own task of interest, but also, it's something that is being done at one of the main stages of training LLMs as you use it every day. And then this transition from the model being a good representation of language to a useful assistance is a subcategory of SFT called instruction tuning.

**中文**

都没问题吗？好。我刚才说的是，SFT 可以用来针对你自己关注的任务进行调整，同时，它也是你每天使用的 LLM 的主要训练阶段之一。模型从良好的语言表示转变为有用助手的这个过程，是 SFT 的一个子类别，叫作指令微调（instruction tuning）。

### [1:09:13](https://www.youtube.com/watch?v=VlA_jt_3Qc4&t=4153s) · b000137

**English**

So instruction tuning comes from the fact that we want the model to answer instructions. So now, I'm going to show with the graph what I was just mentioning regarding predicting the next word. So actually, just in a bit. First, we're going to look at the data. So with Afshin, we saw that the composition of the data for pre-training was basically the whole internet where you had sources that were carrying knowledge such as Wikipedia.

**中文**

instruction tuning 这个名字来自我们希望模型响应指令这一点。现在，我要用图来展示刚才提到的预测下一个词的过程。其实，稍后再展示。我们先看数据。刚才跟着 Afshin，我们看到 pre-training 的数据基本上来自整个互联网，其中包括 Wikipedia 这样承载知识的信息源。

### [1:09:46](https://www.youtube.com/watch?v=VlA_jt_3Qc4&t=4186s) · b000138

**English**

And in general, masses of text of English that tells the model about how English and other languages work, as well as coding. And here, it's slightly different. For instruction tuning, we're going to look at data that's presents to the model how it can most helpfully respond to instructions. So you can divide this in several categories. So here, we present some categories that could be helpful to users of LLMs.

**中文**

总体来说，大量英文文本会告诉模型英语及其他语言是如何运作的，也包括编程。而这里稍有不同。对于 instruction tuning，我们要看的是向模型展示如何最有帮助地响应指令的数据。你可以把这些数据分为几个类别。这里，我们列出了一些可能对 LLM 用户有帮助的类别。

### [1:10:20](https://www.youtube.com/watch?v=VlA_jt_3Qc4&t=4220s) · b000139

**English**

For example, story writing. You're interested in writing a story. You give it a set of instructions, and then you have a ground truth that is attached to it. Other examples include a poem creation, list generation, explanation, and many more that are part of the data mixture of SFT. So basically, you run all these supervised fine tuning training with the inputs that is given, and then you train the model on predicting the output.

**中文**

例如，故事写作。你想写一个故事，就给它一组指令，并配有相应的标准答案（ground truth）。其他例子包括诗歌创作、列表生成、解释，还有许多其他内容，它们都是 SFT 数据混合（data mixture）的一部分。基本上，你用给定的输入进行所有这些 supervised fine tuning 训练，然后训练模型预测输出。

### [1:11:03](https://www.youtube.com/watch?v=VlA_jt_3Qc4&t=4263s) · b000140

**English**

And I'm going now to show what it looks like. So let's say your instruction is here. So you ask your model to do something. So it could be formulated in a different way but just to keep it short, I just said, do X. And then the yellow part is where you start fitting your objective function on.

**中文**

现在，我来展示一下它是什么样的。假设你的指令在这里。你要求模型做某件事。它可以用不同的方式表述，不过为了简短，我只写了“做 X”。黄色部分就是你开始用目标函数进行拟合的地方。

### [1:11:28](https://www.youtube.com/watch?v=VlA_jt_3Qc4&t=4288s) · b000141

**English**

Does this make sense?

**中文**

这样能理解吗？

### [1:11:32](https://www.youtube.com/watch?v=VlA_jt_3Qc4&t=4292s) · b000142

**English**

Great. So as I was mentioning, the data mixture includes instruction geared data. So for example, you had all of these kinds of tasks that users might ask for at inference time. So it's what I put under the category assistant dialogues. And these days, since you have all these large models that already exist out there, and let's say you want to generate a new one, you don't necessarily have to start from scratch.

**中文**

很好。正如我刚才提到的，data mixture 包括面向指令的数据。例如，刚才那些任务都是用户在推理时（inference time）可能提出的要求。我把它们归在“助手对话”这个类别下。如今，已经存在这么多大型模型，假设你想生成一个新模型，也不一定非要从零开始。

### [1:12:11](https://www.youtube.com/watch?v=VlA_jt_3Qc4&t=4331s) · b000143

**English**

So all of these that I mentioned were originally human written. So you had all these instructions that people gathered, and you had expert linguists that had set of instructions on how to write the best answer that was fluent, helpful, and everything that was geared towards maximizing your happiness as a user. But these days, you can use these already trained LLMs to generate such data.

**中文**

我刚才提到的这些数据，最初都是由人类编写的。人们收集了各种指令，语言学专家则有一套指导要求，告诉他们如何写出最佳回答：要流畅、有帮助，各个方面都以最大限度提高用户满意度为目标。不过，如今你可以使用这些已经训练好的 LLM 来生成此类数据。

### [1:12:43](https://www.youtube.com/watch?v=VlA_jt_3Qc4&t=4363s) · b000144

**English**

So typically, when you have a large model that is very performant, you can feed it such instructions, sample some generated outputs, and then have a human or some other LLM review the quality. So it's something that speeds up a bit the curation of such data sets. So I just wanted to emphasize on the fact that it's not only human generated these days, but you can have some assistance. And besides all of the categories that you care about, so typically, math or how you write a proof, how things follow each other, or codes, high quality code bases, you also have other aspects that are very important which when you release a product like this to the wider population that come under the umbrella of safety.

**中文**

通常，当你有一个表现非常好的大型模型时，可以把这些指令输入给它，对生成的输出进行采样，再让人类或另一个 LLM 审查质量。这能稍微加快此类数据集的整理过程。我只是想强调，如今这些数据并非全部由人类生成，你可以借助一些帮助。除了你关注的各类内容，例如数学、如何写证明、事物之间如何衔接，或者代码、高质量代码库之外，当你把这样的产品发布给更广泛的人群时，还有其他非常重要的方面，它们都属于安全性（safety）的范畴。

### [1:13:40](https://www.youtube.com/watch?v=VlA_jt_3Qc4&t=4420s) · b000145

**English**

So you want your model to be helpful but also harmless. So you also have in the data mixture oftentimes a subset that enforces the model's behavior not to repeat some of the harmful content it might have seen on its pre-training corpus. So it will include techniques that might reject some user prompts. So you might have tested on your own the limits of an LLM today.

**中文**

你希望模型有帮助，同时也无害。因此，data mixture 中通常还会有一个子集，用来约束模型的行为，让它不要重复在 pre-training 语料中可能见过的某些有害内容。其中会包含可能拒绝某些用户提示词（prompts）的技术。你可能已经亲自试探过如今 LLM 的边界。

### [1:14:14](https://www.youtube.com/watch?v=VlA_jt_3Qc4&t=4454s) · b000146

**English**

If you submit queries that might lead to something that is considered bad, it would just say, OK, sorry, I cannot answer this. And this sorry, I cannot answer could be done via regex but very rarely because it's not scalable. And people actually embed this property as part of the model. So you have techniques that rejects user queries that are seen as harmful. Or there is some other phenomenon such as hedging that nuance the output of the model in order to not make blanket statement as well.

**中文**

如果你提交的查询可能导致某种被认为不好的结果，它就会说：“好吧，抱歉，我无法回答这个问题。”这种“抱歉，我无法回答”可以通过正则表达式（regex）实现，但这种做法非常少见，因为它不具备可扩展性。人们实际上会把这种特性嵌入模型本身。因此，有一些技术会拒绝被视为有害的用户查询。还有其他现象，例如保留性表达（hedging），它会让模型的输出带有限定，避免作出一概而论的陈述。

### [1:14:58](https://www.youtube.com/watch?v=VlA_jt_3Qc4&t=4498s) · b000147

**English**

So you might have data sets that includes such flavors. And you can have many more depending on the task of interest that you're dealing with. But what I'm listing here is what usually the LLMs out there that aim at being general assistance gather. They tend to be like general tasks that are being trained on. Any questions on the data? Yep.

**中文**

所以，你可能会有包含这些风格的数据集。根据你正在处理的任务，还可以有更多类型。不过，我这里列出的，是目前那些旨在成为通用助手的 LLM 通常会收集的内容。它们往往是在通用任务上进行训练。关于数据有什么问题吗？请说。

### [1:15:44](https://www.youtube.com/watch?v=VlA_jt_3Qc4&t=4544s) · b000148

**English**

Yep. So the question is the story writing example doesn't precise what kind of poetry the story should be about. So it might be ambiguous. How can it generalize? So that is a great point. So we rely on the model's knowledge that it has accumulated at pre-training time to be able to generalize beyond the examples that it has been fed. So let's say, now, you have a story about poetry, and from pre-training, it knows about all kinds of poetry that exist out there.

**中文**

对。问题是，故事写作的例子没有明确说明故事应该围绕哪种诗歌展开，因此可能存在歧义。它如何泛化（generalize）？这是个很好的问题。我们依靠模型在 pre-training 时积累的知识，让它能够泛化到所提供示例之外的情况。假设现在你有一个关于诗歌的故事，而通过 pre-training，它已经知道各种各样的诗歌。

### [1:16:18](https://www.youtube.com/watch?v=VlA_jt_3Qc4&t=4578s) · b000149

**English**

So you could imagine, after fitting such an example at supervised fine tuning time, that you could give more details to this prompt. And then the model has the ability to generalize the generation of the story with respect to those other attributes. So you can have--I think, the example that you mentioned is a great example of the magical ability of LLMs to adapt to natural language. And all of that has to do with the kind of distribution it has seen in the past and what we teach it.

**中文**

所以，你可以想象，在 supervised fine tuning 时拟合了这样的例子之后，你可以给这个 prompt 补充更多细节。模型就有能力根据那些其他属性，对故事生成进行泛化。因此，你可以有——我觉得你刚才提到的例子，很好地体现了 LLM 适应自然语言的神奇能力。而这一切都与它过去见过的分布，以及我们教给它的内容有关。

### [1:16:54](https://www.youtube.com/watch?v=VlA_jt_3Qc4&t=4614s) · b000150

**English**

So I think the concept itself of writing stories is the key learning to the model that it can then generalize. Does that make sense? Yeah. OK. Great. I think there was another question here.

**中文**

所以我觉得，写故事这个概念本身，才是模型学到并随后能够泛化的关键。这样能理解吗？对。好，很好。我记得这边还有一个问题。

### [1:17:19](https://www.youtube.com/watch?v=VlA_jt_3Qc4&t=4639s) · b000151

**English**

Yeah. So the question is about the term of alignment. Is this post training what is called as being aligned? So you are ahead of me. In a few slides, we're going to talk about it. Great questions. Any other question?

**中文**

对。问题是关于对齐（alignment）这个术语的。这里的后训练（post training），就是所谓的对齐吗？你已经走在我前面了。再过几页幻灯片，我们就会讲到它。问题很好。还有其他问题吗？

### [1:17:36](https://www.youtube.com/watch?v=VlA_jt_3Qc4&t=4656s) · b000152

**English**

Awesome. So and then just like Afshin did it for the pre-training part, I'm going to give some orders of magnitude. So the same GPT-3 and Llama 3 papers that Afshin referred some numbers from don't actually give their statistics in terms of token numbers for the instruction tuning side but actually in number of examples. So you see you have about 13 K used GPT-3 and 10 million for Llama 3.

**中文**

很好。接下来，就像 Afshin 在 pre-training 部分做的那样，我会给出一些数量级。Afshin 引用过一些数字的那两篇 GPT-3 和 Llama 3 论文，实际上并没有用 token 数来给出 instruction tuning 部分的统计，而是用样本数量。所以你可以看到，GPT-3 使用了大约 13 K 个样本，Llama 3 则是 1000 万个。

### [1:18:10](https://www.youtube.com/watch?v=VlA_jt_3Qc4&t=4690s) · b000153

**English**

And OK. So let's do some quick estimation. Let's say each example is about 1,000 tokens. When you multiply that with the number of examples, you see that the size of the data sets used for SFT is several orders of magnitude lower than the one used for pre-training. So the mental model that you need to have here is that pre-training is a lot of data you want to learn about general characteristics, about language.

**中文**

好，我们来做个快速估算。假设每个样本大约有 1,000 个 token。把它乘以样本数量，就能看到，SFT 使用的数据集规模比 pre-training 使用的数据集低了好几个数量级。所以，你在这里需要建立的认识是：pre-training 使用大量数据，是为了学习语言的一般特征。

### [1:18:43](https://www.youtube.com/watch?v=VlA_jt_3Qc4&t=4723s) · b000154

**English**

And then SFT is more exactly what--so someone was mentioning just now regarding alignments-- was aligning the goal of the model to being suited for your tasks. So typically, very high quality data sets and much more concise and precise in terms of number. So less order of magnitude.

**中文**

而 SFT 更确切地说是——刚才有人提到 alignment——把模型的目标对齐到适合你的任务上。因此，通常使用的是质量非常高的数据集，在数量上也精简得多、精确得多。所以，数量级更低。

### [1:19:10](https://www.youtube.com/watch?v=VlA_jt_3Qc4&t=4750s) · b000155

**English**

OK. Great. So now, let's try this exercise again. What do you think could be the answer to our instruction tuned now model to the same question?

**中文**

好，很好。现在，我们再做一次这个练习。对于同一个问题，你们觉得现在经过 instruction tuning 的模型会给出什么回答？

### [1:19:23](https://www.youtube.com/watch?v=VlA_jt_3Qc4&t=4763s) · b000156

**English**

Anyone wants to take a guess?

**中文**

有人想猜猜吗？

### [1:19:29](https://www.youtube.com/watch?v=VlA_jt_3Qc4&t=4769s) · b000157

**English**

You want to try again.

**中文**

你想再试一次。

### [1:19:35](https://www.youtube.com/watch?v=VlA_jt_3Qc4&t=4775s) · b000158

**English**

Yeah. So the answer was yes. You can put in the teddy bear in the washer, except that you shouldn't put your teddy bear in the washer. You should handwash it. So it will give you the answer that is helpful to the user. And indeed, this time respond to the query. So which is pretty nice. So now, we talked about all the things that are great about supervised fine tuning. Now, I'm going to detail a bit more about what could make it hard or challenging and then motivate the optimization part that we're going to see afterwards.

**中文**

对，刚才的回答是“可以”。你可以把泰迪熊放进洗衣机，只不过其实你不应该把泰迪熊放进洗衣机，而应该手洗。所以，它会给出对用户有帮助的回答，而且这一次确实回应了查询。这相当不错。现在，我们已经讨论了 supervised fine tuning 的各种优点。接下来，我会更详细地讲讲它可能有哪些困难或挑战，然后引出我们之后要看的优化部分。

### [1:20:14](https://www.youtube.com/watch?v=VlA_jt_3Qc4&t=4814s) · b000159

**English**

So first, we talked about it a bit. When we have these data sets, these data mixtures for SFT training, we need high quality data. And when you say high quality data, means oftentimes human involved in the loop, you need to make sure it abides with all the rules and all the characteristics that the user will care about. So typically, it's highly involved. So originally, these first models, they were almost all human.

**中文**

首先，我们已经稍微谈过这一点。当我们有这些用于 SFT 训练的数据集、这些 data mixture 时，我们需要高质量数据。而说到高质量数据，往往意味着有人参与其中，你需要确保数据符合所有规则，以及用户在意的所有特征。所以，通常需要投入大量精力。最初的那些模型，几乎全都依靠人工。

### [1:20:47](https://www.youtube.com/watch?v=VlA_jt_3Qc4&t=4847s) · b000160

**English**

But now, you might have some mixture of human and generation. But one good thing about these things is that the data sets they are trained on are reused. So it's a work that you do once, and you can complement with respect to time. But it's still very expensive in time and resources. So the second point I want to mention comes back to a point that someone just made regarding the distribution of your SFT data sets and how it would align with actual inference distribution.

**中文**

但现在，可能会混合人工数据和生成数据。不过，这些做法有一个好处：模型训练所用的数据集可以重复使用。因此，这是一项做一次、之后可以随时间补充的工作。但它在时间和资源方面仍然非常昂贵。我要提到的第二点，又回到了刚才有人提出的问题：SFT 数据集的分布，以及它如何与实际推理时的分布对齐。

### [1:21:27](https://www.youtube.com/watch?v=VlA_jt_3Qc4&t=4887s) · b000161

**English**

So in the case of the story regarding a specific kind of poetry, the distribution of prompts, that precise the kind of poetry seems close enough for generalization to be made. But you could think about examples that widely differ. So let's say you ask for a story that is in some movie plots, and it differs from the stories that you might see in textbooks. So this could be slightly out of distribution, and it could have trouble generalizing to that.

**中文**

在关于某种特定诗歌的故事这个例子中，那些明确指定诗歌类型的 prompt，其分布似乎足够接近，因此能够泛化。但你也可以想到差异很大的例子。假设你要求一个涉及某些电影情节的故事，而它不同于你可能在教科书中看到的故事。那么，这就可能稍微偏离分布（out of distribution），模型可能难以泛化到这种情况。

### [1:22:03](https://www.youtube.com/watch?v=VlA_jt_3Qc4&t=4923s) · b000162

**English**

So prompt distribution is very important. And aligning that prompt distribution with respect to the target task is of interest. Yep.

**中文**

所以，prompt 的分布非常重要。让 prompt 分布与目标任务对齐，是值得关注的。请说。

### [1:22:22](https://www.youtube.com/watch?v=VlA_jt_3Qc4&t=4942s) · b000163

**English**

Yeah. Great point. So the question is about, let's say, you have SFT tuned your model, and now, you put a training input back to the model. Will you get the same story? So it has to do with the phenomenon that Afshin was mentioning regarding memorization. So in practice, you will not see the same story most likely because the sampling that you're doing is with a non ZeRO temperature. It will maybe have the same flavor but not word for word.

**中文**

对，很好的问题。问题是，假设你已经对模型做了 SFT，现在把一个训练输入重新交给模型，会得到同一个故事吗？这与 Afshin 刚才提到的记忆（memorization）现象有关。实际中，你很可能不会看到同一个故事，因为你采样时使用的是非 ZeRO 温度 \[字幕疑误，可能指 non-zero temperature，即非零温度\]。它可能会有相同的风格，但不会逐字一致。

### [1:22:58](https://www.youtube.com/watch?v=VlA_jt_3Qc4&t=4978s) · b000164

**English**

Then the flavor of that story, if you have the exact same prompts, might be the same. It depends on what it has seen at pre-training time. But yeah, so the answer is that if I had to give a guess on that precise example, it might be the same flavor but definitely not the same wording. Yeah. So and it might be a different story if the sampling goes through some other region of the space. Stories are highly creative and pre-training corpora of data mixture had all kinds of stories in there.

**中文**

那么，如果你使用完全相同的 prompt，故事的风格可能会相同。这取决于它在 pre-training 时见过什么。对，所以，如果让我针对这个具体例子猜一下，答案是它可能风格相同，但措辞肯定不会一样。对。如果采样进入了空间中的其他区域，也可能得到一个不同的故事。故事具有很强的创造性，而 pre-training 语料的 data mixture 中包含了各种故事。

### [1:23:36](https://www.youtube.com/watch?v=VlA_jt_3Qc4&t=5016s) · b000165

**English**

So the specific example of story is likely to generate different outcomes.

**中文**

因此，故事这个具体例子很可能会产生不同的结果。

### [1:23:54](https://www.youtube.com/watch?v=VlA_jt_3Qc4&t=5034s) · b000166

**English**

Yep. So the question is, will how much the model wanders around depend on the temperature parameter? And yes. So typically, when you have a higher temperature, you also--so it's also called more creative. And it's for that reason. It might also generate things that are less likely in its output distribution with respect to what it has learned. And this is exactly a case of something that we learn. So the answer is yes.

**中文**

对。问题是，模型游走的程度是否取决于温度参数（temperature parameter）？是的。通常，当温度更高时，你也会——这也被称为更有创造性，原因就在这里。相对于它所学到的内容，它也可能生成输出分布中概率较低的东西。这恰好就是我们学到的一个例子。所以答案是肯定的。

### [1:24:27](https://www.youtube.com/watch?v=VlA_jt_3Qc4&t=5067s) · b000167

**English**

So the question is, is there any way to tune that? So when you tune the temperature, you exactly do that. Or were you thinking about something else?

**中文**

问题是，有没有什么办法可以调整它？你调整 temperature 时，做的正是这件事。还是说，你想到的是别的东西？

### [1:24:49](https://www.youtube.com/watch?v=VlA_jt_3Qc4&t=5089s) · b000168

**English**

Yeah. So the question is, is there something else you could do to have variations in the response? So for that, I have a simple but hard solution. You will need more data in that category that will ground the model into seeing what kind of distribution we target with such queries. And I think that will be one way for the model to generalize more. So I think it will be working on the data part. Was there another question?

**中文**

对。问题是，还有没有其他方法能让回答产生变化？对此，我有一个简单但很难实现的解决办法。你需要更多这一类别的数据，让模型据此建立基础（ground），看到我们希望这类查询对应什么样的分布。我觉得这会是让模型更好地泛化的一种方法。所以，我认为需要在数据部分下功夫。还有其他问题吗？

### [1:25:22](https://www.youtube.com/watch?v=VlA_jt_3Qc4&t=5122s) · b000169

**English**

All good. So yeah. So this is a very relevant question because it touches on the topic of generalization. So yeah. So data mixture matters a lot. And having points that are sparse enough in the distribution space to give the gist to the model of what it needs to learn, rather than repeating the same story again and again, will have a lot to do with generalization powers. And then this is something we are going to see in a second, how do you evaluate such models?

**中文**

都没问题了。对，这是个非常相关的问题，因为它涉及泛化。所以，data mixture 非常重要。在分布空间中提供足够分散的数据点，让模型领会它需要学什么，而不是一遍又一遍重复同一个故事，这与泛化能力有很大关系。接下来，我们马上要看另一个问题：如何评估这样的模型？

### [1:25:57](https://www.youtube.com/watch?v=VlA_jt_3Qc4&t=5157s) · b000170

**English**

The feeling that you get as a user on how helpful a model tends to be subjective. So how can you put some number on it is going to be a key topic of interest. And then also very soon, we're going to see how to make the computations not that expensive. So Afshin talked about training optimization techniques. But now, when we're at the fine tuning stage, maybe we can go one step further and see what simplification assumption we could make.

**中文**

作为用户，你对模型有多大帮助的感受往往是主观的。那么，如何用一个数字来衡量它，将是一个关键话题。另外，很快我们也会看到，如何让计算不那么昂贵。Afshin 讲过训练优化技术。但现在，当我们处于 fine tuning 阶段时，也许可以更进一步，看看我们能作出哪些简化假设。

### [1:26:30](https://www.youtube.com/watch?v=VlA_jt_3Qc4&t=5190s) · b000171

**English**

OK. Awesome. Now, let's dive into one of these challenges, which was the evaluation part. So people have decomposed what they care about in categories. So I'm listing here some dimensions that are evaluated against and that gives some quantitative number. So you have a general language where this benchmark that is popular is generally one score that people reports. It's a MMLU, which massive multitask language understanding.

**中文**

好，很好。现在，我们深入看看其中一个挑战，也就是评估部分。人们把关注的内容拆分成了不同类别。我在这里列出了一些评估维度，它们会给出一些定量数字。首先是通用语言能力，这里有一个很流行的基准（benchmark），人们通常会报告它的分数。它叫 MMLU，也就是大规模多任务语言理解（massive multitask language understanding）\[字幕疑误，MMLU 全称可能指 Massive Multitask Language Understanding，原句缺少连接词\]。

### [1:27:07](https://www.youtube.com/watch?v=VlA_jt_3Qc4&t=5227s) · b000172

**English**

So it has, I think, 50 or so tasks in there where the model is being evaluated against, and you have some score that you can compare with. You have benchmarks on reasoning, on math reasoning, as well as code generation. So here, you have all sorts of acronyms, and there is even way more. So basically, the setting up benchmark has been one area of research.

**中文**

我记得它包含大约 50 个任务，用来评估模型，并给出可供比较的分数。还有评估推理、数学推理以及代码生成的 benchmark。这里有各种各样的缩写，而且实际上还有更多。基本上，建立 benchmark 本身已经成为一个研究领域。

### [1:27:38](https://www.youtube.com/watch?v=VlA_jt_3Qc4&t=5258s) · b000173

**English**

So you always see more and more benchmark coming in because people tend to optimize for those that exist. And then there are some gaps that might be filled by further ones. And the GSM 8K stands for grad school--so yeah, grad school math. 8K stands for the number of examples. Yeah, I think so. Or maybe G stands for something else, but it's high school topics basically.

**中文**

所以，你总会看到越来越多的 benchmark 出现，因为人们往往会针对已有的 benchmark 进行优化。而后来出现的 benchmark 可能会填补一些空白。GSM 8K 代表 grad school——对，研究生院数学（grad school math）\[原文如此，可能指 grade school math，即小学数学\]。8K 代表样本数量。对，我想是这样。也可能 G 代表别的意思，但基本上是高中内容。

### [1:28:12](https://www.youtube.com/watch?v=VlA_jt_3Qc4&t=5292s) · b000174

**English**

And one very interesting pattern that people have seen as these models came out and as they were evaluated against these benchmarks is that sometimes for the same kind of model, you see all of a sudden a spike in numbers with respect to some of these benchmarks without a clear explanation behind it. And there is this paper that I highly recommend taking a look, which explores the phenomenon of training on the test task, not the test set.

**中文**

随着这些模型问世，并在这些 benchmark 上接受评估，人们观察到一个非常有意思的模式：有时，对于同一种模型，你会看到它在某些 benchmark 上的分数突然大幅上升，却没有明确的解释。我非常推荐大家看看这篇论文，它研究的是在测试任务（test task）上训练的现象，而不是在测试集（test set）上训练。

### [1:28:49](https://www.youtube.com/watch?v=VlA_jt_3Qc4&t=5329s) · b000175

**English**

The test task. So when you have benchmarks regarding math reasoning, let's say, it matters a lot if the model has been trained on a data that relates to that kind of reasoning versus not. And this is why when you type in those kinds of benchmarks, you will see that there are sets of so-called auxiliary training that can be used for the model to be trained on the same domain.

**中文**

是测试任务。比如，当你有数学推理方面的 benchmark 时，模型是否在与这类推理相关的数据上训练过，影响非常大。因此，当你搜索这类 benchmark 时，会看到一些所谓的辅助训练（auxiliary training）数据集，可以用来让模型在同一领域进行训练。

### [1:29:21](https://www.youtube.com/watch?v=VlA_jt_3Qc4&t=5361s) · b000176

**English**

And in that way, it enables the fact of comparing models with respect to that specific capability. So what the paper tries to convey here is that if you want to compare models between each other, you need to compare the training mixture it has been trained on and then ensure parity in terms of training on the test task. So you need to make sure that, for example, the two have been trained on the test task or not.

**中文**

这样一来，就可以针对这种特定能力比较模型。因此，这篇论文想传达的是，如果你想比较不同模型，就需要比较它们训练时使用的 data mixture，并确保在测试任务上的训练情况相当。比如，你需要确保两个模型都在测试任务上训练过，或者都没有训练过。

### [1:29:55](https://www.youtube.com/watch?v=VlA_jt_3Qc4&t=5395s) · b000177

**English**

And if it's one and the other not, then it might not be a good thing to compare them. It doesn't give you the intrinsic value of the model. So yeah, that's an interesting phenomenon here. Any questions?

**中文**

如果一个训练过，另一个没有，那么比较它们可能就不太合适。这无法体现模型本身的价值。对，这是一个有趣的现象。有什么问题吗？

### [1:30:15](https://www.youtube.com/watch?v=VlA_jt_3Qc4&t=5415s) · b000178

**English**

OK. Great. So we can move on. So one thing that I was mentioning here is that it's very hard to get a sense of how good a model is, even with respect to benchmark scores, because oftentimes what happens is that as they come out, people design data on the training site that resembles more what we try to solve on the benchmark side. So sometimes you end up with models that score great everywhere, but you as a user don't necessarily see added value to it.

**中文**

好，很好。我们可以继续了。我刚才提到的一点是，即便参考 benchmark 分数，也很难判断一个模型到底有多好，因为常常会发生这样的情况：随着 benchmark 出现，人们会在训练端设计数据，让它更像我们在 benchmark 端试图解决的问题。因此，有时你最终得到的模型在各项指标上都得分很高，但作为用户，你不一定能看到它带来的额外价值。

### [1:30:50](https://www.youtube.com/watch?v=VlA_jt_3Qc4&t=5450s) · b000179

**English**

And it's not the fault of models. It's not the fault of the benchmarks. It's just that it's very hard to give a number that conveys the value to you of the model. So this is why people have come up with other techniques to put a number on model evaluation. And you might have heard of Chatbots Arena. Have any folks heard of it here? Yeah. So it's a website where models can be submitted, and users come in, and they ask their questions, and they're presented responses from two models.

**中文**

这不是模型的错，也不是 benchmark 的错。只是，要用一个数字表达模型对你的价值，确实非常困难。因此，人们想出了其他方法，给模型评估赋予一个数值。你可能听说过 Chatbots Arena。这里有人听说过吗？有。它是一个可以提交模型的网站，用户进入网站，提出问题，然后会看到两个模型给出的回答。

### [1:31:33](https://www.youtube.com/watch?v=VlA_jt_3Qc4&t=5493s) · b000180

**English**

And they're being asked to judge which one is better. And then with some pairwise computations done on the website side, they come up with some ranking in the end that ranks model with respect to, quote unquote, "user preference." So it's a number that is being put on the vibes seen by the user. And is it all perfect? Actually, no.

**中文**

用户需要判断哪个回答更好。然后，网站端会做一些成对比较（pairwise）的计算，最后得出一个排名，按照所谓的“用户偏好（user preference）”给模型排序。也就是说，它给用户感受到的感觉赋予了一个数字。那么，它完美无缺吗？实际上并不是。

### [1:32:04](https://www.youtube.com/watch?v=VlA_jt_3Qc4&t=5524s) · b000181

**English**

So it suffers from several issues that are--another set of issues that are hard to deal with. So among them, when you have a new model that comes in, you have some noise at the beginning with respect to which other model it's being compared against. And these first few steps actually influence quite a bit the actual ranking, which makes it a brittle property. And there is a paper that actually shows that it's easily possible to rig such a leaderboard.

**中文**

它也存在几个问题——另一组很难处理的问题。其中一个是，当一个新模型加入时，最初会有一些噪声，取决于它被拿来与哪个其他模型比较。而最初几步实际上会对最终排名产生相当大的影响，这让排名变得不稳健。还有一篇论文确实表明，这样的排行榜很容易被操纵。

### [1:32:43](https://www.youtube.com/watch?v=VlA_jt_3Qc4&t=5563s) · b000182

**English**

So I'm not sure if there is any evidence that it has been done in the past. But you can use any model, if you ask the question, who are you, it's just going to say who it is. If you ask ChatGPT, who are you. It's going to say, hey, I'm ChatGPT, I'm a helpful assistant. And this paper observed on this very simple property that it was able to detect what model was being evaluated against. And let's say, you have an adversarial player, it could rig the ranking just by selecting the right model.

**中文**

我不确定是否有证据表明过去已经发生过这种事。不过，你可以使用任何模型，问它“你是谁”，它就会告诉你自己是谁。如果你问 ChatGPT“你是谁”，它会说：“你好，我是 ChatGPT，我是一个有用的助手。”这篇论文利用这个非常简单的特性，发现可以识别出正在被评估的模型。假设有一个恶意参与者，他只需选择相应的模型，就能操纵排名。

### [1:33:16](https://www.youtube.com/watch?v=VlA_jt_3Qc4&t=5596s) · b000183

**English**

So it's not foolproof. And then on other aspects, so some of the benchmarks that evaluate these models, they're actually curated by experts that know very well about the target distribution of what a given prompt should give. So it has a set of guidelines that says clearly, OK, this is factual. This is non-factual. So they're able to determine what is good versus bad.

**中文**

所以，这并非万无一失。再看其他方面，有些评估这些模型的 benchmark，实际上是由专家整理的，他们非常清楚给定 prompt 应当产生什么样的目标分布。它有一套指导标准，明确指出：好，这是符合事实的，这是不符合事实的。因此，他们能够判断什么是好、什么是坏。

### [1:33:47](https://www.youtube.com/watch?v=VlA_jt_3Qc4&t=5627s) · b000184

**English**

And you as a user, you might not know about it. Because let's just take the example of the teddy bear that you wanted to put in the washer, if I don't know that I need to hand wash my teddy bear, and if I have a detailed response regarding you need to wash it with a machine wash cold, and I could, as a user, find these pieces of advice helpful because they are actionable to me. But actually, are they factual? That is a whole other set of issues that you as a user wouldn't be able to tell on a lot of queries.

**中文**

而作为用户，你可能并不了解这些。就拿你想放进洗衣机的泰迪熊来说，如果我不知道泰迪熊需要手洗，而我得到了一份详细回答，告诉我应该用冷水机洗，那么作为用户，我可能会觉得这些建议很有帮助，因为它们可以直接执行。但实际上，它们符合事实吗？这是另一整组问题，对于许多查询，作为用户的你都无法作出判断。

### [1:34:22](https://www.youtube.com/watch?v=VlA_jt_3Qc4&t=5662s) · b000185

**English**

And another challenge that we have here is a user preference. So who here likes it when there are emojis in LLM responses? Yes? No? Yeah. Personally, I do. And I think there are strong opinions. And some people don't like it at all. So they will down rank such responses. But actually, it's something that the user should be able to tell and choose.

**中文**

我们这里面临的另一个挑战是 user preference。在座有谁喜欢 LLM 的回答里带表情符号（emojis）？喜欢？不喜欢？对，我个人是喜欢的。我觉得大家对此的意见很强烈，有些人完全不喜欢。所以，他们会给这样的回答较低的排名。但实际上，这应该是用户能够表达并作出选择的事情。

### [1:34:52](https://www.youtube.com/watch?v=VlA_jt_3Qc4&t=5692s) · b000186

**English**

And then the distribution of people who choose the best model with respect to the distribution of the wider population that is going to use these models is going to be different oftentimes. And I think the emoji case is a good example, because I think generally, emojis are popular in the wider population. But I think domain experts might not like it as much. So I think that mismatch is one that you would see here. And then the last one I will mention here is the safety side.

**中文**

而选择最佳模型的人群分布，与将来使用这些模型的更广泛人群的分布，往往会有所不同。我觉得 emojis 是个很好的例子，因为总体来说，emojis 在大众中很受欢迎。但领域专家可能没那么喜欢。所以，我认为你会在这里看到这种不匹配。最后，我要提到的是 safety 方面。

### [1:35:25](https://www.youtube.com/watch?v=VlA_jt_3Qc4&t=5725s) · b000187

**English**

So you as a user, you don't really like it when a model rejects your prompts. When you ask about something, and it says, OK, hey, sorry, I cannot answer it. So there will be a bias towards responses that actually respond to your query, rather than respect some safety principle that might be eventually the intended product decision. So there is also this kind of bias that pops up here. And as I was mentioning, evaluation is a hard problem.

**中文**

作为用户，你并不喜欢模型拒绝你的 prompt。你问了某件事，它却说：“好吧，抱歉，我无法回答。”所以，人们会偏向于真正回答查询的响应，而不是遵守某些安全原则的响应，尽管这些原则最终可能是产品有意作出的决策。因此，这里也会出现这种偏差。正如我刚才提到的，评估是个难题。

### [1:35:57](https://www.youtube.com/watch?v=VlA_jt_3Qc4&t=5757s) · b000188

**English**

So you have all these angles that you can explore. And it's not one number that's going to tell you what you care about. It's the combination of all of these. And in the end, it's tailored to what you actually need. So you would need to see the strengths and weaknesses of a given model and to determine which one corresponds to your use case. So I'm going to come back to one question about alignment here.

**中文**

你可以从所有这些角度去探索。不会有一个数字就能告诉你所关心的一切，而是需要把这些方面结合起来。最终，还要根据你的实际需求来定制。因此，你需要了解给定模型的优点和缺点，判断哪一个适合你的使用场景。现在，我要回到刚才关于 alignment 的那个问题。

### [1:36:29](https://www.youtube.com/watch?v=VlA_jt_3Qc4&t=5789s) · b000189

**English**

So we're going to see at the next lecture a further step into aligning the model to do what you want to do in a step called preference tuning. And then the combination of fine tuning and preference tuning, which comes after pre-training, is what we call alignment of the model. So these two steps are called alignments. And I want to call out one other thing. There is one step we didn't mention here that is called mid training that has been emerging very recently, which consists in a step just after pre-training in aligning the kind of data that the model is being trained on to the tasks that you really care about.

**中文**

下一讲，我们会看到让模型进一步对齐、去做你希望它做的事情的一个步骤，叫作偏好微调（preference tuning）。在 pre-training 之后进行的 fine tuning 和 preference tuning，两者结合起来，就是我们所说的模型 alignment。所以，这两个步骤被称为对齐。我还想指出另一件事。这里有一个我们没有提到的步骤，叫作中期训练（mid training），它是最近才出现的，位于 pre-training 之后，目的是让模型训练所用的数据类型与你真正关心的任务对齐。

### [1:37:15](https://www.youtube.com/watch?v=VlA_jt_3Qc4&t=5835s) · b000190

**English**

So it's the same pre-training objective but aligning the kind of tasks and the kind of data sets to something that you care about. And yeah, so it's an emerging trend. I have not mentioned it, but just so that you know, mid training is something that you would have between pre-training and fine tuning. All good?

**中文**

它使用相同的 pre-training 目标，但会把任务类型和数据集类型调整到你关心的内容上。对，这是一个新兴趋势。我之前没有提到，不过让大家了解一下，mid training 是位于 pre-training 和 fine tuning 之间的一个阶段。都没问题吗？

### [1:37:39](https://www.youtube.com/watch?v=VlA_jt_3Qc4&t=5859s) · b000191

**English**

OK. Great. So now, we're going to tackle one aspect of the challenges that we had mentioned regarding fine tuning, which is computational expense--the fact of being computationally expensive. And we're going to look at it with one well-known technique called LoRA, which is a technique to fine tune your weights at the fine tuning stage in an efficient manner. So it's widely used. And it saves a lot of compute.

**中文**

好，很好。现在，我们来解决之前提到的 fine tuning 挑战中的一个方面，也就是计算开销——计算成本高昂这一点。我们会通过一种广为人知的技术 LoRA 来看看这个问题。LoRA 是一种在 fine tuning 阶段高效微调权重的技术。它被广泛使用，而且能节省大量计算。

### [1:38:12](https://www.youtube.com/watch?v=VlA_jt_3Qc4&t=5892s) · b000192

**English**

So when you look at your weight matrices, instead of directly fine tuning the whole weight matrix, the LoRA technique decomposes the fine tuning between the weights of the pre-trained model and additional weights that it decomposes into a low rank multiplication. So in this formulation, the pre-trained weights that you have is frozen.

**中文**

当你看这些权重矩阵时，LoRA 并不是直接微调整个权重矩阵，而是把 fine tuning 分解为预训练模型的权重和额外的权重，并把额外权重分解为一个低秩乘积（low rank multiplication）。在这种形式下，已有的预训练权重是冻结的。

### [1:38:45](https://www.youtube.com/watch?v=VlA_jt_3Qc4&t=5925s) · b000193

**English**

So this W0 is frozen. And then B and A are the matrices that you need to tune. So B and A are typically--so they have dimensions that will match the number of rows and number of columns respectively for the number of rows of B and number of columns of A. But then the dimension of the columns of B and then rows of A is R, which is the rank of these matrices, which is typically taken very small.

**中文**

所以，W0 是冻结的。然后，B 和 A 是你需要调整的矩阵。B 和 A 通常——它们的维度会分别匹配原矩阵的行数和列数，也就是 B 的行数和 A 的列数。但 B 的列维度以及 A 的行维度是 R，这是这些矩阵的秩（rank），通常取一个非常小的值。

### [1:39:16](https://www.youtube.com/watch?v=VlA_jt_3Qc4&t=5956s) · b000194

**English**

So the dimensions of W is typically hundreds or thousands, and the dimension of R is typically up to 10 or O of 10. So as you can imagine, it results in much less weights to train.

**中文**

W 的维度通常是几百或几千，而 R 的维度通常最多是 10，或者是 O of 10 \[原文表述不明确，可能指 10 的数量级\]。所以，你可以想象，这会让需要训练的权重少得多。

### [1:39:37](https://www.youtube.com/watch?v=VlA_jt_3Qc4&t=5977s) · b000195

**English**

And then I will mention just other techniques to improve efficiency and then ease the fine tuning, some methods called a prefix tuning and adapters. So they're explained in the class textbook. But we're not going to dive deep into them because they're less commonly used. But just so that you know. So let's walk through in detail how does LoRA work. So when you want to fine tune your model, so you have all these ways for which you have already learned a distribution at pre-training time.

**中文**

接下来，我还想提一下其他一些提高效率、让 fine tuning 更容易的技术，比如前缀微调（prefix tuning）和适配器（adapters）。课程教材中解释了这些方法。不过，我们不会深入讨论，因为它们没那么常用。只是让大家知道有这些方法。现在，我们详细看看 LoRA 是如何工作的。当你想对模型进行 fine tuning 时，你已经有了所有这些方式（ways）\[字幕疑误，可能指 weights，即权重\]，在 pre-training 时已经为它们学到了一个分布。

### [1:40:15](https://www.youtube.com/watch?v=VlA_jt_3Qc4&t=6015s) · b000196

**English**

So one naive way of operating fine tuning would be to directly iterate on these weights. But what we're doing here, as we said, is to decompose these into the weights that we have already pre-trained on and this product of matrices. And what LoRA says is that you can do a forward pass on both these terms and then adds these quantities in the end. And A and B is going to be a characterization of your task of interest.

**中文**

一种朴素的 fine tuning 方法，是直接迭代更新这些权重。但正如我们说过的，这里要做的是，把它们分解为已经预训练好的权重，以及这个矩阵乘积。LoRA 的思路是，你可以分别对这两项进行前向传播（forward pass），最后再把这些量相加。而 A 和 B 会表征你关注的任务。

### [1:40:52](https://www.youtube.com/watch?v=VlA_jt_3Qc4&t=6052s) · b000197

**English**

So let's say you have a model that--so Afshin was mentioning the kinds of tasks that you can maybe specialize your model on, for example, spam detection. So you would take your pre-trained model, instantiate this B and A in weights, in the weights of your model, fine tune on them. And then what you will have is that B and A are going to be specific to this task of spam detection, similarly for sentiment extraction and so on.

**中文**

假设你有一个模型——Afshin 刚才提到过一些可以让模型专门处理的任务，例如垃圾邮件检测（spam detection）。你会拿来预训练模型，在模型的权重中实例化 B 和 A，再对它们进行 fine tuning。随后得到的 B 和 A，就会专门对应 spam detection 这个任务。情感提取（sentiment extraction）等任务也是类似的。

### [1:41:23](https://www.youtube.com/watch?v=VlA_jt_3Qc4&t=6083s) · b000198

**English**

So it's a very nice property that you can start from a base model, further tune your weights, and then have your A's and B's that are task specific.

**中文**

所以，这是一个非常好的特性：你可以从一个基础模型（base model）出发，进一步调整权重，然后得到针对特定任务的 A 和 B。

### [1:41:37](https://www.youtube.com/watch?v=VlA_jt_3Qc4&t=6097s) · b000199

**English**

So I want to comment now on where were these matrices being learned. So in the original paper of LoRA, it mentioned training only on the attention matrices. But later on, people realized that it might not be the place where it has the most positive impact on performance. And then there is a blog that came out a few weeks ago that studies this into detail, and then they realized that the feed-forward blocks are actually those where putting LoRA is most beneficial.

**中文**

现在，我想说说这些矩阵是在哪里学习的。LoRA 的原始论文提到，只在注意力矩阵（attention matrices）上训练。但后来，人们意识到，这可能并不是对性能产生最大正面影响的位置。几周前有一篇博客详细研究了这个问题，他们发现，前馈模块（feed-forward blocks）实际上才是应用 LoRA 最有益的地方。

### [1:42:22](https://www.youtube.com/watch?v=VlA_jt_3Qc4&t=6142s) · b000200

**English**

So today, typically, both these components carry LoRA matrices, but the bulk of the performance improvements is actually contained in the feed-forward block.

**中文**

因此，如今通常这两个组件都会带有 LoRA 矩阵，但性能提升的主要部分实际上来自 feed-forward block。

### [1:42:38](https://www.youtube.com/watch?v=VlA_jt_3Qc4&t=6158s) · b000201

**English**

And then I want to mention two interesting properties about LoRA. So when you fine tune with LoRA weights, you want to use a higher learning rate. So typically, 10 times more is the guidance. And then one interesting fact is that it doesn't perform as well when you train it with larger batch size. So I don't have a good theoretical explanation to give you for each of them.

**中文**

接下来，我想提一下 LoRA 的两个有趣特性。使用 LoRA 权重进行 fine tuning 时，你需要使用更高的学习率（learning rate）。通常的建议是提高到 10 倍。另外，一个有趣的事实是，使用更大的批大小（batch size）训练时，它的表现并没有那么好。对于这两点，我都没有很好的理论解释可以提供给大家。

### [1:43:08](https://www.youtube.com/watch?v=VlA_jt_3Qc4&t=6188s) · b000202

**English**

It's more empirical observations that have been emitted. But to give the main lines behind the mindset shared from people who study this phenomenon, the first one might be guided by the rank of the LoRA matrices that might be small. And as a result, given the regions of space that it needs to explore, you need a higher learning rate. And then the second one, the hypothesis here is that the training dynamic of products of matrices is different than a full matrix.

**中文**

这些更多是人们报告的经验观察。不过，我可以概括一下研究这种现象的人所分享的思路。第一点可能与 LoRA 矩阵的 rank 较小有关。因此，考虑到它需要探索的空间区域，你需要更高的 learning rate。第二点的假设是，矩阵乘积的训练动态与完整矩阵不同。

### [1:43:47](https://www.youtube.com/watch?v=VlA_jt_3Qc4&t=6227s) · b000203

**English**

And this is where the increasing batch size phenomenon occurs. So it's basically the explanations, tentative explanations given there. So now, we're going to explore an optimization of this. But before I dive deep into that part, does anyone have any questions on the LoRA part? Yep.

**中文**

而增大 batch size 时的现象就发生在这里。这基本上就是他们给出的解释，或者说尝试性的解释。现在，我们要探索它的一种优化。不过，在深入那部分之前，大家对 LoRA 部分有什么问题吗？请说。

### [1:44:23](https://www.youtube.com/watch?v=VlA_jt_3Qc4&t=6263s) · b000204

**English**

Yep. Great point. So the question is, do you do grid search on the rank? So you could. So it's a design choice to rank R. Typically, people would have done it before you. So you have an idea of what rank could be well suited for your use case. So you could definitely do grid search, or you could just pick a popular value. I think a 4 is used commonly. You can just go with one of them. Yeah. And we are going to see that the reduction in number of parameters is so huge already that reducing even more maybe doesn't matter that much.

**中文**

对，很好的问题。问题是，要对 rank 做网格搜索（grid search）吗？可以。这是一个设计选择，也就是选择 rank R。通常，别人已经在你之前做过了，所以你会对哪种 rank 适合你的使用场景有一定了解。你当然可以做 grid search，也可以直接选一个常用值。我记得 4 很常用。你可以直接选择其中一个。对。接下来我们会看到，参数数量的减少已经非常巨大，因此再进一步减少，可能就没那么重要了。

### [1:45:02](https://www.youtube.com/watch?v=VlA_jt_3Qc4&t=6302s) · b000205

**English**

That initial reduction by orders of magnitude goes a long way, and that is just a hyperparameter tuning. And you can see a given rank in a given setup as being a design choice. So we have two minutes, and we're going to quickly cover quantized LoRA. So the techniques that Afshin mentioned just now regarding quantizing weights and so reducing the memory footprint is something that we're going to see just here.

**中文**

最初几个数量级的减少已经能带来很大帮助，而这只是一个超参数调优（hyperparameter tuning）问题。你可以把特定设置下的某个 rank 看作一个设计选择。我们还剩两分钟，要快速介绍一下量化 LoRA（quantized LoRA）。Afshin 刚才提到的权重量化（quantization）以及由此减少内存占用的技术，就是我们接下来要看的内容。

### [1:45:37](https://www.youtube.com/watch?v=VlA_jt_3Qc4&t=6337s) · b000206

**English**

So when you look at these matrices W0 and A and B, what people have done in this paper is to quantize the weights of W0 into a format that is very smart and then compute and iterate on these matrices that are being learned, A and B in full precision, which is in that case BF16.

**中文**

当你看这些矩阵 W0、A 和 B 时，这篇论文的做法是，把 W0 的权重量化成一种非常巧妙的格式，然后以全精度（full precision）对正在学习的矩阵 A 和 B 进行计算和迭代，在这里就是 BF16。

### [1:46:02](https://www.youtube.com/watch?v=VlA_jt_3Qc4&t=6362s) · b000207

**English**

And then the quantization of these frozen weights is super smart. It's in a format called NF4, which assumes that the weights are distributed normally. And it splits the space into quantiles rather than buckets of fixed size, which puts about the same amount of number of values into each. So it optimizes the bits that you use for encoding.

**中文**

这些冻结权重的量化非常巧妙。它使用一种叫作 NF4 的格式，假设权重服从正态分布（normal distribution）。它按照分位数（quantiles）划分空间，而不是划分成固定大小的桶（buckets），这样每个部分包含的数值数量大致相同。因此，它优化了编码所使用的位（bits）。

### [1:46:33](https://www.youtube.com/watch?v=VlA_jt_3Qc4&t=6393s) · b000208

**English**

And what it does is that it does a double quantization process. So it quantizes the weights. And then in a second step, it quantizes the quantization constants that we didn't see at length here. But basically, when you want to convert your full weights in and out of quantized states, you have constants that are generated. And they propose to quantize these constants as well.

**中文**

它还会执行一个双重量化（double quantization）过程。首先量化权重，然后在第二步中量化那些我们在这里没有详细讨论的量化常数（quantization constants）。基本上，当你要在完整精度权重与量化状态之间转换时，会产生一些常数。他们提出，也对这些常数进行量化。

### [1:47:03](https://www.youtube.com/watch?v=VlA_jt_3Qc4&t=6423s) · b000209

**English**

So this method generated minus 16X VRAM savings, and then the double quantization methods gave some extra savings but not that much. But it's interesting to know. And then we are exactly on time. Thank you for your time.

**中文**

所以，这种方法带来了 minus 16X 的显存（VRAM）节省 \[字幕疑误，minus 16X 的含义不明确，可能指显存占用减少至约 1/16\]，而 double quantization 方法又带来了一些额外节省，但没有那么多。不过，了解这一点很有意思。我们也刚好讲完。感谢大家的时间。
