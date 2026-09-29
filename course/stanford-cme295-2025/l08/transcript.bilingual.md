# Stanford CME295 Transformers &amp; LLMs \| Autumn 2025 \| Lecture 8 - LLM Evaluation

_Bilingual transcript · 双语讲稿_

- Channel: Stanford Online
- Source: [YouTube](https://www.youtube.com/watch?v=8fNP4N46RRo)
- Duration: 1:49:25
- Caption source: manual
- Status: complete
- Chinese translation: 208/208
- Translation provider: codex
- Generated: 2026-09-29T16:10:14+00:00

## Transcript · 讲稿

### [00:05](https://www.youtube.com/watch?v=8fNP4N46RRo&t=5s) · b000001

**English**

Hello, everyone, and welcome to lecture 8 of CME 295. So today's topic will be LLM evaluation. And I think this class is probably one of the most important classes of this quarter because the idea is if we don't how to measure the performance of our LLM, we don't really know what to improve. And so this class will focus on how we can quantify how the LLM performs in a bunch of different cases.

**中文**

大家好，欢迎来到 CME 295 第 8 讲。今天的主题是大语言模型评估（LLM evaluation）。我认为这节课可能是本季度最重要的几节课之一，因为如果我们不知道如何衡量 LLM 的表现，就不知道该改进什么。因此，这节课将重点介绍如何量化 LLM 在各种不同情况下的表现。

### [00:39](https://www.youtube.com/watch?v=8fNP4N46RRo&t=39s) · b000002

**English**

So with that said, we are going to start the class as usual by recapping what we saw last week. So if you remember, last week, we saw how our LLM could interact with systems that are outside of the LLM itself. So we saw one core technique that is called RAG that allows our LLM to fetch information from external knowledge bases.

**中文**

那么，我们像往常一样，先回顾一下上周学过的内容。如果大家还记得，上周我们讲了 LLM 如何与自身之外的系统交互。我们介绍了一项叫作 RAG 的核心技术，它让 LLM 能够从外部知识库获取信息。

### [01:10](https://www.youtube.com/watch?v=8fNP4N46RRo&t=70s) · b000003

**English**

And so here RAG stands for Retrieval-Augmented Generation. And we saw how we could improve the retrieval system. So we saw that it was composed of two main steps. So one was candidate retrieval, which is typically something that is done with a bi-encoder setup. So Sentence-BERT was a good example of how people would design such a model.

**中文**

这里的 RAG 指检索增强生成（Retrieval-Augmented Generation）。我们也讲了如何改进检索系统。我们看到，它由两个主要步骤组成。其中一个是候选项检索（candidate retrieval），通常采用双编码器（bi-encoder）架构。Sentence-BERT 就是人们如何设计这类模型的一个很好的例子。

### [01:42](https://www.youtube.com/watch?v=8fNP4N46RRo&t=102s) · b000004

**English**

And so this first step is typically there to filter down the potential relevant candidates for a given incoming query. And then we saw that there was a second step, which was reranking, and that one was a bit more involved and involved cross-encoders, which were more sophisticated. And we also saw some ways to quantify how well our retrieval system performed.

**中文**

第一步通常用于针对传入的查询，筛选出可能相关的候选项。然后我们讲了第二步，也就是重排序（reranking）。这一步稍微复杂一些，会用到更复杂的交叉编码器（cross-encoders）。我们还介绍了一些量化检索系统表现的方法。

### [02:12](https://www.youtube.com/watch?v=8fNP4N46RRo&t=132s) · b000005

**English**

And then we also saw something that was called tool calling, which is the ability for a model to which tool to call with which argument. So if you remember, if we give our LLM the knowledge of the tools that are available to it, it can figure out which arguments it needs to input to the function as a function of the input query, and then run that function and then output the result in natural language to the user.

**中文**

接着，我们还讲了工具调用（tool calling），也就是模型能够用哪些参数调用哪个工具的能力。如果大家还记得，只要让 LLM 知道有哪些可用工具，它就可以根据输入查询，确定需要向函数传入哪些参数，然后运行该函数，再用自然语言向用户输出结果。

### [02:51](https://www.youtube.com/watch?v=8fNP4N46RRo&t=171s) · b000006

**English**

And then we also saw how agentic workflows were composed of. So spoiler alert, it's something that is a combination of the two previous methods, so RAG and tool calling. And in particular, given an input, we're allowing our model to make multiple calls to call different tools to fetch relevant data from other knowledge bases.

**中文**

接着，我们还讲了智能体工作流（agentic workflows）是如何组成的。先透露一下，它其实是前面两种方法，也就是 RAG 和 tool calling 的结合。具体来说，给定一个输入，我们允许模型进行多次调用，调用不同的工具，从其他知识库获取相关数据。

### [03:21](https://www.youtube.com/watch?v=8fNP4N46RRo&t=201s) · b000007

**English**

And we saw one example that was successful from the current applications, which was AI-assisted coding, which relies on this principle. And React is typically the framework that people would use. So reason plus act, which is decomposing this into observe, plan, and act steps. Cool. So this is what we saw last time, and we also so started from this slide last time.

**中文**

我们看了当前应用中的一个成功案例，也就是 AI 辅助编程（AI-assisted coding），它依赖的就是这个原理。React \[字幕疑误，可能指 ReAct\] 通常是人们会使用的框架。也就是推理加行动（reason plus act），把这个过程分解为观察、规划和行动三个步骤。好，这就是上次讲过的内容，而且我们上次也是从这张幻灯片开始的。

### [03:55](https://www.youtube.com/watch?v=8fNP4N46RRo&t=235s) · b000008

**English**

If you remember, our LLM has strengths but also weaknesses that we're trying to mitigate. So in particular, the focus of lectures 6 and 7 were on methods to improve reasoning of the model and ways for the model to fetch knowledge from other systems, as well as performing actions. And today, we're going to focus on the evaluation part, in particular, given a response that the model is giving, how can we quantify how well the LLM is giving its response?

**中文**

如果大家还记得，LLM 有优势，也有我们试图缓解的弱点。具体来说，第 6 讲和第 7 讲重点介绍了改进模型推理的方法，以及模型从其他系统获取知识和执行操作的方式。今天我们将重点讨论评估，特别是给定模型的一条回答，我们如何量化 LLM 回答得有多好？

### [04:40](https://www.youtube.com/watch?v=8fNP4N46RRo&t=280s) · b000009

**English**

Cool. So first of all, I would like to define the term "evaluation" and the meaning that we will use for this lecture. So when we say, I want to evaluate my LLM, it can actually take a lot of different meanings. So when you say, let's evaluate the LLM, it can mean let's evaluate the performance, the output. Let's evaluate this based on coherence, factuality. Let's evaluate it based on latency, so more system-related metrics or pricing or how often it is up and so on.

**中文**

好。首先，我想定义一下“评估”（evaluation）这个词，以及本讲使用它时所指的含义。当我们说想评估 LLM 时，实际上可能有很多不同的意思。说“我们来评估 LLM”，可以指评估表现、评估输出；可以根据连贯性（coherence）、事实性（factuality）来评估；也可以根据延迟（latency）来评估，也就是更偏系统层面的指标，或者价格、可用时间比例等等。

### [05:20](https://www.youtube.com/watch?v=8fNP4N46RRo&t=320s) · b000010

**English**

So just to make sure we're on the same page, this lecture will mostly focus on the output quality part. And in particular, we'll focus on quantifying how good the actual response is. And here you will note that this is a challenging problem because as we saw previously, our LLM is a text-to-text model that can output basically anything.

**中文**

为了确保大家理解一致，本讲将主要关注输出质量。具体来说，我们会重点量化实际回答有多好。这里大家会注意到，这是个有挑战性的问题，因为正如我们之前看到的，LLM 是一个文本到文本（text-to-text）模型，基本上可以输出任何内容。

### [05:53](https://www.youtube.com/watch?v=8fNP4N46RRo&t=353s) · b000011

**English**

So it can be natural language, it can be code, it can be math reasoning, and so on and so forth. So it's very hard to come up with universal metrics to evaluate that. So we will see how people do this in practice.

**中文**

输出可以是自然语言，可以是代码，可以是数学推理，等等。因此，很难提出通用的指标来评估这些内容。我们会看看人们在实践中是怎么做的。

### [06:12](https://www.youtube.com/watch?v=8fNP4N46RRo&t=372s) · b000012

**English**

Cool. So given the fact that our LLM generates free-form output, one could imagine that the ideal scenario for us to evaluate the LLM output would be to every time ask a human to rate the response. So here the ideal scenario would be, OK, I give a prompt to my LLM. It gives a response. I ask a human to rate it, and I start again and again.

**中文**

好。鉴于 LLM 生成的是自由形式输出（free-form output），可以想象，评估 LLM 输出的理想情形是每次都请人来给回答评分。也就是说，理想情况下，我给 LLM 一个提示词（prompt），它给出回答，我请人评分，然后一遍又一遍地重复这个过程。

### [06:46](https://www.youtube.com/watch?v=8fNP4N46RRo&t=406s) · b000013

**English**

And what I do is at the end of the day, I just collect all these human responses, and I try to quantify the overall performance of my model. Well, as you can imagine, the main problem is that such a system would be very cost-intensive. But let's look at this into more detail. So if you remember, the LLM outputs are really free-form.

**中文**

最后，我收集所有这些人的反馈，尝试量化模型的整体表现。大家可以想象，主要问题在于，这样的系统成本会非常高。不过，我们来更详细地看看。如果大家还记得，LLM 的输出确实是自由形式的。

### [07:17](https://www.youtube.com/watch?v=8fNP4N46RRo&t=437s) · b000014

**English**

And there may be cases that even human judgments may be something that is fuzzy because maybe the rating task in itself is subjective. So let's take the following example. Let's suppose I ask my LLM what birthday gift should I get. And let's suppose the LLM responds with a teddy bear is almost always a sweet gift. Just pick one that feels right for you. So let's suppose I want to evaluate this response with respect to the usefulness dimension.

**中文**

有些情况下，甚至人的判断也可能比较模糊，因为评分任务本身可能就是主观的。来看下面这个例子。假设我问 LLM，我应该买什么生日礼物。假设 LLM 回答说，泰迪熊几乎总是一份贴心的礼物，挑一个你觉得合适的就好。再假设我想从有用性这个维度来评估这条回答。

### [07:52](https://www.youtube.com/watch?v=8fNP4N46RRo&t=472s) · b000015

**English**

I may have one human reader that says, yeah, it's pretty useful because teddy bear is pretty indicative of, I guess, what the user should get as a gift. But then another reader may say, no, actually, it's not useful because maybe the response didn't specify exactly which teddy bear. Should I have a bear? Should I have an elephant, a giraffe? Which stuffed animal should I get?

**中文**

可能有一位读者会说，是的，这很有用，因为泰迪熊已经相当明确地指出了用户应该买什么礼物。但另一位读者可能会说，不，其实没什么用，因为回答也许没有具体说明是哪一种泰迪熊。我应该买熊吗？还是买大象、长颈鹿？我到底该买哪种毛绒动物？

### [08:22](https://www.youtube.com/watch?v=8fNP4N46RRo&t=502s) · b000016

**English**

So there is this notion of inter-rater agreement, where we're basically concerned with making sure that everyone is aligned on how to rate those responses because sometimes like in this illustrative example, it's maybe a little bit subjective. So responses may vary.

**中文**

因此，我们有一个概念叫作评分者间一致性（inter-rater agreement）。我们主要关心的是，确保大家对于如何给这些回答评分达成一致，因为有时候，就像这个说明性的例子一样，评分可能稍微有些主观，所以评分结果可能不同。

### [08:52](https://www.youtube.com/watch?v=8fNP4N46RRo&t=532s) · b000017

**English**

So what people want to do is to make sure that the guidelines are clear enough for everyone to rate these responses in a consistent manner. So people come up with agreement types of metrics. So a very natural metric that you may think of is the quote, unquote, "agreement rate." So for instance, you have these two raters.

**中文**

因此，人们希望确保评分指南足够清楚，让每个人都能以一致的方式给这些回答评分。于是，人们提出了一些衡量一致性的指标。你可能想到的一个很自然的指标，就是所谓的“一致率”（agreement rate）。例如，你有这两位评分者。

### [09:24](https://www.youtube.com/watch?v=8fNP4N46RRo&t=564s) · b000018

**English**

So what you do is you just measure the proportion of the time that the two raters give the same response. And let's suppose the response here is binary, so let's say, yes, good or not good. Well, do you see a problem with such a metric? Is this a good metric?

**中文**

你要做的，就是衡量两位评分者给出相同回答的比例。假设这里的回答是二元的，比如，是，好，或者不好。那么，你们觉得这样的指标有什么问题吗？它是一个好指标吗？

### [09:54](https://www.youtube.com/watch?v=8fNP4N46RRo&t=594s) · b000019

**English**

I guess another way to ask this question is, if I give you a given number of agreement rates, can you tell me if it's a good number or if it's a bad number? Well, let's take the example of, let's say, two raters, let's say, Alice and let's say, Bob.

**中文**

我想，换一种问法就是，如果我给你一个具体的一致率数值，你能告诉我这个数值是好还是坏吗？我们举个例子，假设有两位评分者，分别叫 Alice 和 Bob。

### [10:24](https://www.youtube.com/watch?v=8fNP4N46RRo&t=624s) · b000020

**English**

And let's suppose we have two different types of ratings that these raters can give. So either, let's say, yes, it's good, so 1, the output is good, or the output is not good.

**中文**

假设这些评分者可以给出两种不同的评分。一种是，是的，输出很好，记为 1；另一种是，输出不好。

### [10:40](https://www.youtube.com/watch?v=8fNP4N46RRo&t=640s) · b000021

**English**

So if we assume that the first rater gives, let's say, random responses with some probability P of A for being good and 1 minus P of A for being not good. And then, let's say, Bob, who should have eyes and a smile, has a P of B for being good and 1 minus P of B for being not good.

**中文**

假设第一位评分者随机给出回答，以 P of A 的概率评为好，以 1 minus P of A 的概率评为不好。然后，Bob——他应该有眼睛和笑脸——以 P of B 的概率评为好，以 1 minus P of B 的概率评为不好。

### [11:13](https://www.youtube.com/watch?v=8fNP4N46RRo&t=673s) · b000022

**English**

Then let's compute the agreement rate for this case. So the agreement rate is basically the probability that rater A and rater B agree. And so here A and B agree if A and B both vote 1 or when A and B both vote 0.

**中文**

那么，我们来计算这种情况下的一致率。一致率基本上就是评分者 A 和评分者 B 意见一致的概率。这里，A 和 B 一致，是指 A 和 B 都投 1，或者 A 和 B 都投 0。

### [11:50](https://www.youtube.com/watch?v=8fNP4N46RRo&t=710s) · b000023

**English**

But if they give their response in an independent and random way, well, if you use this probability concepts that you know, then we will have probability of A and B responding to 1, which is probability of A responding to 1 times probability of B responding to 1, and same for 0. So we will have something like this. So P of A, P of B plus 1 minus P of A, 1 minus P of B. So this one is A and B say 1 And here A and B say 0.

**中文**

但如果他们独立、随机地给出回答，那么运用大家知道的概率概念，A 和 B 都回答 1 的概率，就等于 A 回答 1 的概率乘以 B 回答 1 的概率，0 也是一样。所以我们会得到这样的式子：P of A, P of B plus 1 minus P of A, 1 minus P of B。这一项是 A 和 B 都说 1，这一项是 A 和 B 都说 0。

### [12:49](https://www.youtube.com/watch?v=8fNP4N46RRo&t=769s) · b000024

**English**

So let's see what the agreement rate would be in that case. So if we assume that suppose that-- let's suppose, P of A is equal to P of B, which is equal to, let's say, 0.5, then the agreement rate would be--so agreement rate would be--so I'm just replacing the numbers here, so 0.5 squared plus 0.5 squared.

**中文**

我们来看看这种情况下的一致率是多少。如果我们假设，假设——假设 P of A 等于 P of B，都等于，比如 0.5，那么一致率就是——一致率就是——我这里只是把数值代进去，也就是 0.5 squared plus 0.5 squared。

### [13:26](https://www.youtube.com/watch?v=8fNP4N46RRo&t=806s) · b000025

**English**

So it's 0.25 plus 0.25, which is equal to 0.5. So what that means is if we're just letting our raters rate these things in a random way with some probability P of A, P of B, we would already have an agreement rate of 50%, just by pure random chance. And so one thing that I want to say is, that this agreement rates, by pure chance, is a function of the probability that each of these raters give these ratings.

**中文**

也就是 0.25 plus 0.25，等于 0.5。这意味着，如果只是让评分者以某些概率 P of A、P of B 随机评分，那么仅凭纯粹的随机巧合，我们就已经会有 50% 的一致率。因此，我想指出，纯粹偶然产生的一致率，是各位评分者给出这些评分的概率的函数。

### [14:03](https://www.youtube.com/watch?v=8fNP4N46RRo&t=843s) · b000026

**English**

And so if this probability is actually higher, the agreement rates by pure chance is also higher. So what that means? So what do I want to say? I want to say that if we just take the agreement rates, then it's very hard to put it into context in terms of what you would have gotten if things would have happened just by pure chance.

**中文**

如果这个概率更高，纯粹偶然产生的一致率也会更高。这意味着什么？我想说什么呢？我想说，如果只看一致率，就很难结合纯粹偶然情况下会得到什么结果，来理解这个数值。

### [14:31](https://www.youtube.com/watch?v=8fNP4N46RRo&t=871s) · b000027

**English**

So for this reason, people have come up with a series of metrics that try to make it more relative to this baseline, which is, what would happen if our raters would choose things randomly? And so you have these metrics-- like for instance, this one is the Cohen's kappa metric, which computes a quantity that is a function of this agreement rate by chance, and take the observed one, such that if our observed agreement rate is greater than the "by chance" agreement rate, then our coefficient is positive.

**中文**

因此，人们提出了一系列指标，试图相对于这个基准来衡量一致性，这个基准就是：如果评分者随机选择，会发生什么？于是就有了这些指标，例如这里的 Cohen's kappa 指标。它结合偶然一致率和观测到的一致率来计算一个量，使得当观测一致率高于“偶然”一致率时，系数为正。

### [15:27](https://www.youtube.com/watch?v=8fNP4N46RRo&t=927s) · b000028

**English**

So when it's positive, at least you know it's going in the right direction. So here, if the observed agreement rate is equal to 1, then kappa is equal to 1. But if our observed agreement rate is below the "by pure random chance" agreement rate that we saw on the blackboard, then our coefficient would be negative.

**中文**

所以，当它为正时，至少你知道方向是对的。这里，如果观测一致率等于 1，那么 kappa 就等于 1。但如果观测一致率低于我们在黑板上看到的“纯粹随机巧合”一致率，那么系数就会为负。

### [15:59](https://www.youtube.com/watch?v=8fNP4N46RRo&t=959s) · b000029

**English**

So long story short, there is a bunch of metrics that try to quantify inter-rater agreement rates using these kinds of formulas to be able to make these quantities relative to what would happen if things were done in a random way. And so that's why you may see a bunch of metrics out there. So here is Cohen's kappa that people use for cases where there are two raters, but then you have extensions, such as Fleiss's kappa and Krippendorff's alpha that you may see out there.

**中文**

简而言之，有许多指标尝试用这类公式量化评分者间的一致率，让这些量能够相对于随机评分时的情况来衡量。这就是为什么大家可能会看到很多这类指标。这里的 Cohen's kappa 用于只有两位评分者的情况，但也有一些扩展，比如大家可能见过的 Fleiss's kappa 和 Krippendorff's alpha。

### [16:37](https://www.youtube.com/watch?v=8fNP4N46RRo&t=997s) · b000030

**English**

So they all rely on this idea that we should have some baseline, which is our raters just randomly picking answers, and try to see how much better our actual agreement is compared to this. So does that make sense?

**中文**

它们都基于这样的想法：应该有一个基准，也就是评分者随机选择答案，然后看看实际的一致性比这个基准好多少。这样说能理解吗？

### [17:01](https://www.youtube.com/watch?v=8fNP4N46RRo&t=1021s) · b000031

**English**

So I guess what I want to say is that the first limitation of asking humans to rate our LLM outputs, which was sometimes the task being subjective, can be something that we can quantify with this inter-rater agreement metrics. So what people would typically do is they keep track of how good that agreement is. And if, let's say, we have a quantity that's not satisfactory, people would just hold some quote, unquote, "agreement sessions" between the raters to just align on how they should rate the answers so that it can be seen as just a health metric to track how consistent your ratings are.

**中文**

我想说的是，请人给 LLM 输出评分的第一个局限，也就是任务有时具有主观性，可以通过这些评分者间一致性指标来量化。人们通常会跟踪一致性有多好。如果得到的数值不太令人满意，就会让评分者召开所谓的“一致性会议”（agreement sessions），统一他们应该如何给答案评分。因此，这可以看作一个健康度指标，用来跟踪评分的一致程度。

### [17:54](https://www.youtube.com/watch?v=8fNP4N46RRo&t=1074s) · b000032

**English**

And this is typically something that people use in practice. So up until now, we've seen one limitation of human ratings. Well, second limitation, I think I also said it previously. It's really slow. If you ask someone to rate a thousand LLM outputs, well, it will take them a while. And it's, of course, expensive. So all of that to say that our ideal scenario of asking a human to rate every LLM output is not something that is practical.

**中文**

这也是人们在实践中常用的做法。到目前为止，我们已经看到了人工评分的一个局限。第二个局限，我想前面也提过，就是它非常慢。如果请一个人给一千条 LLM 输出评分，他会花上不少时间。当然，这也很贵。所以，说了这么多，就是想说明，请人给每条 LLM 输出评分这个理想情形并不实际。

### [18:35](https://www.youtube.com/watch?v=8fNP4N46RRo&t=1115s) · b000033

**English**

But we can leverage human ratings in some way because we've seen that even if the task is subjective, we can have a way to align our raters. So now let's move on to another way to go about doing this, which is by using some rule-based metrics. So here I'm just going to revise the setting that I mentioned before.

**中文**

不过，我们仍然可以以某种方式利用人工评分，因为我们已经看到，即使任务具有主观性，也有办法让评分者达成一致。现在来看另一种做法，也就是使用基于规则的指标（rule-based metrics）。这里，我要稍微修改一下前面提到的设置。

### [19:06](https://www.youtube.com/watch?v=8fNP4N46RRo&t=1146s) · b000034

**English**

And instead of asking our humans to write every LLM output, this time, I'm just going to ask them to write the references or the ideal outputs for a given set of prompts, just fix that for good, and then use some kind of metric that would compare the LLM outputs with those references.

**中文**

这次不再请人为每条 LLM 输出进行书写 \[字幕疑误，write 可能指 rate，即评分\]，而是只请他们为一组给定的提示词编写参考答案或理想输出，把这些内容固定下来，再用某种指标比较 LLM 输出与这些参考答案。

### [19:39](https://www.youtube.com/watch?v=8fNP4N46RRo&t=1179s) · b000035

**English**

So here the main difference is, let's suppose I have a given set of prompts fixed. Well, I can make iterations in my model and always compare the outputs of my LLM with this fixed reference, instead of always asking humans to rate that again and again. So it's already an improvement. And we will see a little bit what are the kinds of rule-based metrics that you will see out there.

**中文**

这里的主要区别是，假设我有一组固定的提示词，那么我可以不断迭代模型，并始终把 LLM 输出与这个固定的参考答案比较，而不用反复请人评分。这已经是一种改进。我们会稍微看看大家可能遇到的基于规则的指标有哪些。

### [20:14](https://www.youtube.com/watch?v=8fNP4N46RRo&t=1214s) · b000036

**English**

So ideally, these metrics should reflect the performance of the LLM output in an optimal way. And what I mean by an optimal way, it is to make it be a little bit flexible, given the fact that natural language is not always something that you can say in one given way. So for instance, when I provide a response to a given prompt, there can be very well a case where I can formulate the response slightly differently, but it will still be just as good.

**中文**

理想情况下，这些指标应该以最优的方式反映 LLM 输出的表现。我说的最优，是指让它稍微灵活一些，因为自然语言并不总是只能用一种特定方式表达。例如，针对一个提示词给出回答时，完全可能用稍有不同的措辞表达，但回答仍然同样好。

### [20:52](https://www.youtube.com/watch?v=8fNP4N46RRo&t=1252s) · b000037

**English**

So the idea behind this matrix is to make this comparison a little bit flexible.

**中文**

所以，这个矩阵（matrix）\[字幕疑误，可能指 metric，即指标\] 背后的想法，就是让这种比较稍微灵活一些。

### [21:01](https://www.youtube.com/watch?v=8fNP4N46RRo&t=1261s) · b000038

**English**

So let's start with one common one that people use in the translation case. So this metric is called METEOR, and it stands for metric for evaluation of translation with explicit ordering. So the idea here is to compare reference and predicted, and we'll see how it's being done, and also penalize cases when words are not in the same order, which is explaining why the metric is called with explicit ordering.

**中文**

我们先从翻译场景中常用的一个指标讲起。这个指标叫 METEOR，全称是采用显式排序的翻译评估指标（metric for evaluation of translation with explicit ordering）。它的思路是比较参考文本和预测文本，我们会看看具体怎么做，同时对词语顺序不同的情况施加惩罚，这也解释了为什么指标名称中有“显式排序”。

### [21:41](https://www.youtube.com/watch?v=8fNP4N46RRo&t=1301s) · b000039

**English**

So the formula is as follows. So it is some F score times 1 minus some penalty.

**中文**

公式如下。它是某个 F 分数（F score）乘以 1 减去某个惩罚项（penalty）。

### [21:50](https://www.youtube.com/watch?v=8fNP4N46RRo&t=1310s) · b000040

**English**

So the F score here is--you may be familiar with F1 score. So it's like the harmonic mean with equal weights. So this one is with the variable weights. So it is a function of precision and recall, where precision is the proportion of the unigrams that are in your predicted sequence that are matching with the reference.

**中文**

这里的 F score——大家可能熟悉 F1 score，它类似于等权重的调和平均数（harmonic mean）。而这里使用的是可变权重。它是精确率（precision）和召回率（recall）的函数，其中 precision 是预测序列中的一元词组（unigrams）与参考文本匹配的比例。

### [22:20](https://www.youtube.com/watch?v=8fNP4N46RRo&t=1340s) · b000041

**English**

And the recall is the proportion of the unigrams in the reference that are matching with what is in the predicted. So it's basically matching the usual precision recall metrics that you know. And then we have another quantity here, which is the penalty. And I mentioned the penalty here tries to incentivize good ordering. So if it's ordered the same in the reference and in the prediction, then it's good.

**中文**

recall 则是参考文本中的 unigrams 与预测文本中的内容匹配的比例。所以，它基本上对应大家熟悉的 precision 和 recall 指标。接着，这里还有另一个量，也就是 penalty。我提到过，这里的 penalty 试图鼓励正确的排序。如果参考文本和预测文本中的顺序相同，那就很好。

### [22:54](https://www.youtube.com/watch?v=8fNP4N46RRo&t=1374s) · b000042

**English**

Otherwise, it's bad. And so here there's a bunch of quantities. So gamma and beta are hyperparameters that people arbitrarily choose. And it's a function of C, the number of contiguous chunks that are matched over the number of matched unigrams.

**中文**

否则就不好。这里有几个量。gamma 和 beta 是人们自行选择的超参数（hyperparameters）。这个量是 C，也就是匹配的连续片段（contiguous chunks）数量，除以匹配的 unigrams 数量的函数。

### [23:23](https://www.youtube.com/watch?v=8fNP4N46RRo&t=1403s) · b000043

**English**

So ideally, you would want C that would be as low as possible because if you have a low number of contiguous matches, it means that your contiguous sequences are long, which means that the ordering is the same. So you want C to be low and then matched unigrams to be high. So you want that penalty term to be low for a good--I guess, for a prediction that has the same ordering as the reference.

**中文**

理想情况下，你希望 C 尽可能小，因为连续匹配片段的数量少，意味着连续序列很长，也就意味着顺序相同。所以，你希望 C 较小，而匹配的 unigrams 数量较大。对于一个好的——我想说，对于一个与参考文本顺序相同的预测，你希望这个惩罚项较小。

### [24:01](https://www.youtube.com/watch?v=8fNP4N46RRo&t=1441s) · b000044

**English**

So I guess higher METEOR score means better translation, according to this way of doing things. So I guess when you look at this formula--first of all, it looks very arbitrary. I have alpha as a hyperparameter, gamma, beta. So it's kind a recipe, I feel. So that's one.

**中文**

因此，按照这种做法，METEOR 分数越高，翻译越好。我想，当你看到这个公式时，首先会觉得它看起来很随意。我有 alpha 这个超参数，还有 gamma、beta。所以我感觉，它有点像一个配方。这是一点。

### [24:31](https://www.youtube.com/watch?v=8fNP4N46RRo&t=1471s) · b000045

**English**

And the second thing is that it does not allow for stylistic variations because here we're measuring the number of matched unigrams. Although the metric expands the range of what it's called matched unigrams by taking into account things like words that are synonyms of one another and things that are of the same roots, but still, it is not extremely satisfactory in that sense.

**中文**

第二点是，它不允许风格上的变化，因为这里衡量的是匹配的 unigrams 数量。虽然这个指标会考虑同义词以及同词根的词等情况，从而扩大所谓匹配 unigrams 的范围，但即便如此，在这方面它仍然不是特别令人满意。

### [25:06](https://www.youtube.com/watch?v=8fNP4N46RRo&t=1506s) · b000046

**English**

So METEOR is one such metric. You have another one that's being used or that has been used in translation tasks, which is called BLEU, which you may know. So BLEU stands for bilingual evaluation understudy. And you can think of this as a precision-focused kind of metric that looks at the number of matching n-grams over the n-grams that are in the prediction, which is why it's a precision kind of metric.

**中文**

METEOR 就是这样一个指标。还有另一个正在或曾经用于翻译任务的指标，叫 BLEU，大家可能知道。BLEU 代表双语评估替补（bilingual evaluation understudy）。你可以把它理解为一种侧重 precision 的指标，它看的是匹配的 n 元词组（n-grams）数量与预测文本中的 n-grams 数量之比，所以它属于 precision 类型的指标。

### [25:45](https://www.youtube.com/watch?v=8fNP4N46RRo&t=1545s) · b000047

**English**

And it also has a penalty term. Here it's called brevity penalty because given that it's more of a precision kind of metric, if you translate something that's very short, you may be able to gain the metric. So you want to penalize the translation being too short. So we're not go going to a lot of details, but I just want to just show you the kinds of metrics that are out there. So METEOR is one, BLEU is another one.

**中文**

它也有一个惩罚项，这里叫作简短惩罚（brevity penalty）。因为它更侧重 precision，如果你的译文非常短，就可能获得指标上的好处 \[字幕疑误，gain the metric 可能指 game the metric，即钻指标的空子\]。所以要惩罚过短的译文。我们不会深入讨论很多细节，我只是想向大家展示有哪些指标。METEOR 是一个，BLEU 是另一个。

### [26:17](https://www.youtube.com/watch?v=8fNP4N46RRo&t=1577s) · b000048

**English**

And ROUGE, which you may have heard, is also another one, typically used for summarization tasks. Again, same idea, and it has a bunch of variants that you may see out there. But long story short, all these metrics, they all compare the output with a reference. So as we saw, one key limitation is that they do not allow stylistic variation.

**中文**

大家可能听说过的 ROUGE 也是一个，通常用于摘要任务。同样，它的思路相似，也有很多大家可能见过的变体。简而言之，这些指标都把输出与参考文本进行比较。正如我们看到的，一个关键局限是，它们不允许风格上的变化。

### [26:51](https://www.youtube.com/watch?v=8fNP4N46RRo&t=1611s) · b000049

**English**

So let's take an example. So let's suppose I say, a plush teddy bear can comfort a child during bedtime. Well, the exact same thing, you can say it--I can say it in a really different way. So soft stuffed bears often help kids feel safe as they fall asleep, or many youngsters rest more easily at night when they cuddle a gentle toy companion. So in all these cases, the metrics that we saw would really perform very poorly.

**中文**

来看一个例子。假设我说，毛绒泰迪熊可以在孩子睡觉时给他们安慰。同样的意思，可以——我可以用完全不同的方式表达。比如，柔软的毛绒熊常常帮助孩子在入睡时感到安心；或者，许多年幼的孩子在夜里抱着一个温柔的玩具伙伴时，会睡得更安稳。在这些情况下，我们刚才讲的指标表现都会很差。

### [27:23](https://www.youtube.com/watch?v=8fNP4N46RRo&t=1643s) · b000050

**English**

So that's one key limitation. So the second key limitation is correlation is not that great. I mean, you can imagine that people have come up with all these hyperparameters to make it be correlated to human ratings, but they're not that correlated. And the bottom line is, it still requires human ratings to just get started. And sometimes you just can't afford to have human ratings, maybe in your project.

**中文**

这是一个关键局限。第二个关键局限是相关性并没有那么好。我的意思是，可以想象，人们设计所有这些超参数，是为了让指标与人工评分相关，但它们的相关性并不那么强。而且，归根结底，要开始使用它们，仍然需要人工评分。有时，你的项目可能根本负担不起人工评分。

### [27:58](https://www.youtube.com/watch?v=8fNP4N46RRo&t=1678s) · b000051

**English**

So I guess there are still some key limitations, which is the reason why--all of that to say, I want to motivate the key methods of this class or of this lecture, which is called LLM-as-a-Judge.

**中文**

所以，我想，这些方法仍有一些关键局限。这也是为什么——说了这么多，是为了引出这节课或者本讲的核心方法，叫作以 LLM 为评判者（LLM-as-a-Judge）。

### [28:16](https://www.youtube.com/watch?v=8fNP4N46RRo&t=1696s) · b000052

**English**

We spent the first seven lectures motivating these large language models that are pretrained on huge amounts of data that are tuned in a way to match human preference. So they do contain human knowledge. They do contain some indication of what humans may prefer. So the idea here is to have our model response be actually an input of yet another LLM.

**中文**

前七讲，我们一直在介绍这些大语言模型为什么有用：它们在海量数据上预训练，并经过调整以匹配人类偏好。因此，它们确实包含人类知识，也包含一些关于人类可能偏好什么的信息。这里的思路是，把模型的回答作为另一个 LLM 的输入。

### [28:49](https://www.youtube.com/watch?v=8fNP4N46RRo&t=1729s) · b000053

**English**

And that LLM is something that people typically call LLM-as-a-Judge. So it was a term that was introduced in a paper from two years ago. So here the idea is to use an LLM for rating purposes. And things that you would see as input would be the prompt that was used to produce the response, the response, and the criteria along which you want to grade your response.

**中文**

人们通常把那个 LLM 称为 LLM-as-a-Judge。这个术语是在两年前的一篇论文中提出的。这里的思路是用 LLM 来评分。你通常会看到的输入包括：用于生成回答的提示词、回答本身，以及你希望依据哪些标准来给回答评分。

### [29:26](https://www.youtube.com/watch?v=8fNP4N46RRo&t=1766s) · b000054

**English**

And so here LLM-as-a-Judge would give you the following outputs. So the first thing is it would give you a score. So here you can think of it as a binary scale score, so pass or fail, and this is very new, also a rationale because LLMs, they understand text. So they can also explain you why they graded something with a given score.

**中文**

这里，LLM-as-a-Judge 会给出以下输出。首先，它会给出一个分数。你可以把它看作二元量表上的分数，也就是通过或不通过。还有一点很新：它还会给出理由（rationale），因为 LLM 理解文本，所以它也能解释为什么给某个内容打这个分数。

### [29:58](https://www.youtube.com/watch?v=8fNP4N46RRo&t=1798s) · b000055

**English**

And that part is the key difference with previous methods. We are able to explain why the metric or the model is giving us a given score. And this is quite good because in the other, let's say, rule-based world where you would have all these formulas and multiplication and all these things, and sometimes you would come up with a number that would not be very self-explanatory.

**中文**

这一点是它与之前方法的关键区别。我们能够解释为什么指标或模型给出某个分数。这相当好，因为在另一个，比如基于规则的世界里，会有各种公式、乘法以及其他运算，有时候最后得到的数字并不能清楚说明自身的含义。

### [30:30](https://www.youtube.com/watch?v=8fNP4N46RRo&t=1830s) · b000056

**English**

And this is luckily something that LLM-as-a-Judge addresses.

**中文**

幸运的是，LLM-as-a-Judge 解决了这个问题。

### [30:37](https://www.youtube.com/watch?v=8fNP4N46RRo&t=1837s) · b000057

**English**

So to recap, what we want is to use an LLM as a way to grade the response. So here you would have typically the following kind of prompts. So you would state, OK, I want to evaluate my response with respect to a given criteria. And then you give the prompt that you used to generate that response along with the model response. And then you would ask the judge to return two things, the rationale and then the score.

**中文**

回顾一下，我们想做的是用 LLM 给回答评分。通常会使用如下形式的提示词。你会说明，我想依据某个给定标准来评估回答。然后提供生成这条回答时使用的提示词，以及模型的回答。再要求评判者返回两样东西：先是理由，然后是分数。

### [31:18](https://www.youtube.com/watch?v=8fNP4N46RRo&t=1878s) · b000058

**English**

So one little trick I want to point out is people typically ask the model to first output the rationale and then the score. And the reason why we typically do that is it's something that empirically improves the quality of the results. But then given what we saw, I think in, lecture 6, if you remember the reasoning class, we saw that these reasoning models that are being trendy, especially in 2025, what they do is they first output a chain of thought before giving the answer.

**中文**

这里我想指出一个小技巧：人们通常要求模型先输出理由，再输出分数。之所以通常这么做，是因为根据经验，它能提高结果的质量。不过，结合我们之前学过的内容，我想是在第 6 讲，如果大家还记得那节推理课，我们讲过那些流行的推理模型（reasoning models），尤其是在 2025 年，它们会先输出思维链（chain of thought），然后再给出答案。

### [31:59](https://www.youtube.com/watch?v=8fNP4N46RRo&t=1919s) · b000059

**English**

So you can actually think of this trick as being on the same idea of reasoning models, as in, it allows the model to externalize, verbalize its quote, unquote, "thought process" before giving the score. So it gives it a chance to really figure out what is good or what is wrong in the model response.

**中文**

所以，你可以认为这个技巧与推理模型的思路相同：它让模型在给分之前，把所谓的“思考过程”外化，用语言表达出来。这给了模型一个机会，真正弄清楚模型回答中哪些地方好，哪些地方有问题。

### [32:28](https://www.youtube.com/watch?v=8fNP4N46RRo&t=1948s) · b000060

**English**

So far, so good? Any questions on, I guess, the setup?

**中文**

到目前为止都还好吗？对于这个设置，有什么问题吗？

### [32:36](https://www.youtube.com/watch?v=8fNP4N46RRo&t=1956s) · b000061

**English**

All good. So now I have a question for you. If I give the following prompts to my LLM-as-a-Judge, am I guaranteed to have a rationale and a score that I can parse? Am I guaranteed?

**中文**

都没问题。现在我有个问题问大家。如果我把下面这些提示词交给 LLM-as-a-Judge，就能保证得到可解析的理由和分数吗？能保证吗？

### [33:01](https://www.youtube.com/watch?v=8fNP4N46RRo&t=1981s) · b000062

**English**

No? Yeah, exactly, no. The answer is no. You're not guaranteed to have a rationale and a score that you can parse because this model has some probabilistic nature to it with the sampling process. And it's not something that you can really control. So I guess my follow-up question is, do you know a technique that would, I guess, guarantee you to have a structured response?

**中文**

不能？对，没错，不能。答案是不能。你无法保证得到可解析的理由和分数，因为这个模型的采样过程具有一定的概率性，并不是你真正能控制的。所以，我接下来的问题是，大家知道有什么技术，可以保证得到结构化的回答吗？

### [33:32](https://www.youtube.com/watch?v=8fNP4N46RRo&t=2012s) · b000063

**English**

So hint is a technique that we saw towards the beginning of the class.

**中文**

提示一下，这是我们在课程较早阶段讲过的一项技术。

### [33:42](https://www.youtube.com/watch?v=8fNP4N46RRo&t=2022s) · b000064

**English**

I'll give you a little hint. So if you remember on slide 65 of lecture 3, we saw a technique called constraints-guided decoding. So if you remember, the idea here is to constrain the decoding thought process by allowing our model to only sample from quote, unquote, "valid" tokens. And we typically do that in cases where we want our output to have a given format, so let's suppose, a JSON format.

**中文**

再给大家一点提示。如果大家还记得，第 3 讲的第 65 张幻灯片中，我们讲过一项叫作约束引导解码（constraints-guided decoding）的技术。它的思路是，通过只允许模型从所谓“有效”的词元（tokens）中采样，来约束解码的思考过程。我们通常在希望输出具有特定格式时使用它，比如 JSON 格式。

### [34:19](https://www.youtube.com/watch?v=8fNP4N46RRo&t=2059s) · b000065

**English**

And we want absolutely that format. So what people do is they use this technique to guarantee the form of the response. And in case you're using this provider, like the providers that are out there, like for instance, OpenAI or Gemini or Anthropic, this technique is known under the name structured output. So in your projects, if you want to constrain the decoding process in order to output the response of a given format, so let's suppose my format is a response, and I cannot represent it by a class, and there are two attributes, so rationale and score.

**中文**

而且我们必须得到那个格式。所以，人们使用这项技术来保证回答的形式。如果你使用目前这些提供商，比如 OpenAI、Gemini 或 Anthropic，这项技术的名称就是结构化输出（structured output）。因此，在项目中，如果你想约束解码过程，让它输出特定格式的回答，比如我的格式是一个 response，而我不能用一个类来表示它 \[字幕疑误，cannot 可能指 can\]，其中有两个属性，也就是 rationale 和 score。

### [35:07](https://www.youtube.com/watch?v=8fNP4N46RRo&t=2107s) · b000066

**English**

Well, typically, you can reference that with the argument text format equal to that representation. So this, I believe, is something that OpenAI does. I'm not exactly sure if it's exactly the argument name that you would see for the other providers, but they're all, I guess, along the same lines.

**中文**

那么，通常可以通过让 text format 参数等于那个表示来引用它。我相信这是 OpenAI 的做法。我不太确定其他提供商使用的参数名是否完全相同，但我想基本思路都差不多。

### [35:33](https://www.youtube.com/watch?v=8fNP4N46RRo&t=2133s) · b000067

**English**

Does it sound good? So the key word here is structured output. Whenever you want a response of a given format, you would just go for that.

**中文**

这样可以理解吗？这里的关键词是 structured output。只要你想得到特定格式的回答，就可以用它。

### [35:47](https://www.youtube.com/watch?v=8fNP4N46RRo&t=2147s) · b000068

**English**

Cool. So just to recap, our LLM-as-a-Judge has two main benefits. So the first one is that we do not need a reference text. We do not need human ratings to just get started because our LLM already has a lot of, I guess, knowledge that it has acquired during pretraining and human preferences and so on. So you do not need that. And then the second thing is you can interpret the score with the rationale that it is being output.

**中文**

好。回顾一下，LLM-as-a-Judge 有两个主要好处。首先，我们不需要参考文本，也不需要先有人工评分才能开始，因为 LLM 在预训练期间已经获得了大量知识，以及人类偏好等信息。所以不需要这些。其次，你可以通过它输出的理由来解释分数。

### [36:23](https://www.youtube.com/watch?v=8fNP4N46RRo&t=2183s) · b000069

**English**

And that is also quite remarkable. So just as an example, here you would say, evaluate the quality of this response. So you would have some rationale that would explain what this response has or doesn't have that makes it good or bad along with the score.

**中文**

这一点也相当了不起。举个例子，你可以说，评估这条回答的质量。然后你会得到一些理由，解释这条回答具备或缺少什么，因而表现好或不好，同时还会得到分数。

### [36:46](https://www.youtube.com/watch?v=8fNP4N46RRo&t=2206s) · b000070

**English**

Cool. And I believe-- now we're going to see the kinds of LLM-as-a-Judge that you can see out there. Of course, there are many variations, but there are generally two types of LLM-as-a-Judge that you will see. So the first one is you have a single output, a single response that you want to evaluate. And here you would ask LLM-as-a-Judge to say, OK, is it good, or is it not good?

**中文**

好。我想——现在我们来看看有哪些类型的 LLM-as-a-Judge。当然，有很多变体，但总体而言，大家会看到两种类型。第一种是，你只有一个输出、一条想评估的回答。你会让 LLM-as-a-Judge 判断，它好不好？

### [37:17](https://www.youtube.com/watch?v=8fNP4N46RRo&t=2237s) · b000071

**English**

And the second big kind of LLM-as-a-Judge that you will see out there is pairwise kind of setup. So you have two responses, and you say, is response A better, or is response B better? And here you would obtain a response either that one or this one. So if you remember, we have seen in previous lectures that there are a lot of situations where we would want to have preference data, for instance, in the preference tuning class that we had, I believe it was lecture 5.

**中文**

第二大类 LLM-as-a-Judge 是成对比较（pairwise）的设置。你有两条回答，然后问，是回答 A 更好，还是回答 B 更好？这里你会得到一个答案，要么选这个，要么选那个。如果大家还记得，我们在前几讲看到，很多情况下都希望获得偏好数据（preference data），例如在偏好调优（preference tuning）那节课，我记得是第 5 讲。

### [37:56](https://www.youtube.com/watch?v=8fNP4N46RRo&t=2276s) · b000072

**English**

So these kind of methods can also be a good way to synthetically generate preference ratings where you have two responses. And then you ask your LLM to say, OK, I prefer that one. And you can use that one as the label to train your reward model.

**中文**

因此，这类方法也可以很好地用来合成偏好评分：你有两条回答，然后让 LLM 说，我更喜欢那一条。你就可以把它用作标签，训练奖励模型（reward model）。

### [38:19](https://www.youtube.com/watch?v=8fNP4N46RRo&t=2299s) · b000073

**English**

Does it sound good? Any questions on the setup or everything that we've talked about so far?

**中文**

这样可以理解吗？对于这个设置，或者我们到目前为止讨论的任何内容，有什么问题吗？

### [38:31](https://www.youtube.com/watch?v=8fNP4N46RRo&t=2311s) · b000074

**English**

Cool. Everyone is on the same page. So now let's see what can go wrong with our LLM-as-a-Judge. So let's think of the possible kinds of failures that we can encounter. So the first one is called position bias. And as the name suggests, it has to do with the ordering at which we present the responses to our model. So let's say, if we ask our model, is response A better or response B?

**中文**

好，大家理解一致。现在来看 LLM-as-a-Judge 可能出什么问题。我们来想想可能遇到哪些失败情况。第一种叫作位置偏差（position bias）。顾名思义，它与我们向模型呈现回答的顺序有关。比如，我们问模型，是回答 A 更好，还是回答 B 更好？

### [39:06](https://www.youtube.com/watch?v=8fNP4N46RRo&t=2346s) · b000075

**English**

Well, there is a chance that the model responds with response A just because it was the first one to be mentioned. So that bias is called position bias. So it's where the position at which you place the response matters in the judgment of the LLM-as-a-Judge model. And I guess, as a way to remedy that, people have different techniques.

**中文**

模型有可能回答 A，仅仅因为它是第一个被提到的。这种偏差就叫 position bias，也就是说，你把回答放在什么位置，会影响 LLM-as-a-Judge 模型的判断。为了缓解它，人们有不同的技术。

### [39:37](https://www.youtube.com/watch?v=8fNP4N46RRo&t=2377s) · b000076

**English**

But one typical technique would be to ask the model, is A or B better? And then ask the model, is B or A better? And then take the majority voting. So if both of them lead to the same response, then it's good. But if the response changes, then it may not be good. So you may want to do something else.

**中文**

一种典型的技术是，先问模型 A 和 B 哪个更好，再问模型 B 和 A 哪个更好，然后采用多数投票（majority voting）。如果两次都指向同一条回答，那就很好。但如果答案变了，可能就不太好，你可能需要采用其他做法。

### [40:05](https://www.youtube.com/watch?v=8fNP4N46RRo&t=2405s) · b000077

**English**

There are a bunch of other techniques. So I know there's a bunch of papers that try to tweak the position embeddings, but those ones are a bit more advanced. So it's not typically the thing that you would do just out of the box. So taking the average or taking the majority voting of this position swapping is typically what you would do.

**中文**

还有很多其他技术。我知道有不少论文尝试调整位置嵌入（position embeddings），但这些方法更复杂一些，通常不是拿来就能用的。所以，一般会对这种位置交换的结果取平均值，或采用 majority voting。

### [40:29](https://www.youtube.com/watch?v=8fNP4N46RRo&t=2429s) · b000078

**English**

Cool. So this was the first kind of bias. The second bias is called verbosity bias. So let's suppose you have two responses. And the first response is short and concise. The second response is something that goes much more into details, is typically something that is more verbose. Well, there are cases where the model will tend to, I guess, prefer responses that are just more verbose just because they're more verbose, not necessarily because they're more correct.

**中文**

好，这是第一种偏差。第二种叫作冗长偏差（verbosity bias）。假设有两条回答，第一条简短精练，第二条包含更多细节，通常更冗长。有些情况下，模型会倾向于更喜欢冗长的回答，仅仅因为它们更冗长，而不一定是因为它们更正确。

### [41:07](https://www.youtube.com/watch?v=8fNP4N46RRo&t=2467s) · b000079

**English**

And for that, it's maybe a little bit trickier. So people typically try to explicit this dimension in the guidelines. When they input, I guess, this question to the LLM-as-a-Judge, they say, well, make sure to not pay too much attention to the length of these responses to not, I guess, prefer something just because it's more verbose. So that's one kind of method that you will see out there.

**中文**

这可能稍微棘手一些。人们通常会在指南中明确说明这个维度。向 LLM-as-a-Judge 输入问题时，会告诉它，不要过度关注这些回答的长度，不要仅仅因为某条回答更冗长就更喜欢它。这是大家会看到的一种方法。

### [41:40](https://www.youtube.com/watch?v=8fNP4N46RRo&t=2500s) · b000080

**English**

The second one is to just also add some examples, in-context learning examples, to the model to just, I guess, tell it to, I guess, show by example that verbosity is not something you should prefer. And then the last one is to have some kind of penalty on the output length. So you can ask your model in a pointwise way, how good is 1, how good is 2.

**中文**

第二种是给模型添加一些例子，也就是上下文学习（in-context learning）的例子，用示例告诉它、向它展示，不应该偏好冗长。最后一种是对输出长度施加某种惩罚。你可以让模型以逐点评估（pointwise）的方式判断，回答 1 有多好，回答 2 有多好。

### [42:13](https://www.youtube.com/watch?v=8fNP4N46RRo&t=2533s) · b000081

**English**

And then try to penalize that with the length. So that's something that also people may use. So we've seen position bias. We've seen verbosity bias. Now we will see the third kind of bias that you may see out there, which is called self-enhancement bias. And so that one has to do with the fact that if you ask a model to judge an output that was produced by itself, well, the model will tend to prefer responses that are generated by itself, regardless of whether or not the other one was more aligned with what we wanted.

**中文**

然后尝试根据长度对它进行惩罚。这也是人们可能采用的做法。我们已经看了 position bias 和 verbosity bias。现在来看可能遇到的第三种偏差，叫作自我增强偏差（self-enhancement bias）。它指的是，如果让模型评判它自己生成的输出，那么模型往往会偏好自己生成的回答，无论另一条回答是否更符合我们的要求。

### [43:03](https://www.youtube.com/watch?v=8fNP4N46RRo&t=2583s) · b000082

**English**

And I guess, here the intuition is that if our model generated such an answer, then it may be the case that our model thought that from a probabilistic standpoint, this was a sequence that was very much likely to appear. So it may be, I guess, one way to think about it, which is, if it has generated such a sequence, then it means that it is something that it thinks--I mean, "think," quote, unquote, that it's a good answer.

**中文**

这里的直觉是，如果模型生成了这样的答案，那么从概率角度来看，模型可能认为这是一个很有可能出现的序列。我想，可以这样理解：如果它生成了这样的序列，就意味着它认为——这里的“认为”要加引号——这是一个好答案。

### [43:41](https://www.youtube.com/watch?v=8fNP4N46RRo&t=2621s) · b000083

**English**

So the general guideline here is to typically not use the same model that you use for generation and for judges. But I guess nowadays, it's hard to have that strict constraints, I guess, respected because, I guess, all models, they are trained on basically the same data sets. So you can argue they're all being subject to the same, I guess, training mixes and so on.

**中文**

所以，一般的指导原则是，生成和评判通常不要使用同一个模型。不过我想，如今很难严格遵守这个约束，因为所有模型基本上都在相同的数据集上训练。所以可以说，它们都受到相同的训练数据混合等因素的影响。

### [44:18](https://www.youtube.com/watch?v=8fNP4N46RRo&t=2658s) · b000084

**English**

But still, I guess, what people do is they tend to use another model just to have such a risk be minimized. So long story short, try to not use the exact same model that you use for generation and for evaluation.

**中文**

不过，人们仍然倾向于使用另一个模型，以尽量减小这种风险。简而言之，尽量不要让生成和评估使用完全相同的模型。

### [44:39](https://www.youtube.com/watch?v=8fNP4N46RRo&t=2679s) · b000085

**English**

So this is self-enhancement bias.

**中文**

这就是 self-enhancement bias。

### [44:43](https://www.youtube.com/watch?v=8fNP4N46RRo&t=2683s) · b000086

**English**

Before we go to the next subpart, I guess, what do you think of these three biases? Do they make sense? Any questions so far? Yep.

**中文**

在进入下一小节之前，大家对这三种偏差有什么看法？能理解吗？到目前为止有什么问题吗？好。

### [45:03](https://www.youtube.com/watch?v=8fNP4N46RRo&t=2703s) · b000087

**English**

So can you elaborate a bit more?

**中文**

你能再详细说明一下吗？

### [45:14](https://www.youtube.com/watch?v=8fNP4N46RRo&t=2714s) · b000088

**English**

So the question is, can you have a model that just maybe isn't aligned with, I guess, the ground truth and maybe prioritizes maybe one label over another? So this can definitely be another kind of bias, so this bias being that our LLM is not exactly aligned with what humans would prefer. So these three biases are by no means exhaustive. So this can very well be another bias that you can list as well. This is definitely another kind of bias.

**中文**

问题是，有没有可能某个模型与真实答案（ground truth）不一致，而且可能优先选择某个标签而不是另一个？这当然可以是另一种偏差，也就是我们的 LLM 并不完全符合人类偏好。这三种偏差绝不是完整的清单。因此，这完全可以是你列出的另一种偏差。这确实是另一种偏差。

### [45:46](https://www.youtube.com/watch?v=8fNP4N46RRo&t=2746s) · b000089

**English**

Yep.

**中文**

对。

### [46:00](https://www.youtube.com/watch?v=8fNP4N46RRo&t=2760s) · b000090

**English**

So the question is, is it possible that our judge still prefers an LLM response, even if it's a different one? Well, it depends how good your judge is. But typically, the best practice is to have a judge that has a much bigger capacity that may capture this kind of differences and not be fooled by a response that just sounds like something it may generate but something that is maybe more aligned with human preferences.

**中文**

问题是，即使是另一个 LLM 的回答，评判者是否仍有可能更喜欢它？这取决于评判者有多好。不过，通常的最佳实践是使用能力容量（capacity）大得多的评判者，它也许能捕捉到这些差异，不会被某个只是听起来像它可能生成的回答所迷惑，而是偏向更符合人类偏好的内容。

### [46:30](https://www.youtube.com/watch?v=8fNP4N46RRo&t=2790s) · b000091

**English**

So I guess the short answer is yes, you can still have such a situation. But in order to mitigate that risk, you would typically take a model that is not the same but also typically much bigger. So you have a bunch of such models out there. And with all the, I guess, improvements that have been made with reasoning models, this is also something that people try.

**中文**

我想，简短的回答是，是的，仍然可能出现这种情况。但为了降低这种风险，通常会选一个不同的模型，而且通常大得多。目前有很多这样的模型。随着推理模型取得各种改进，人们也会尝试使用它们。

### [47:01](https://www.youtube.com/watch?v=8fNP4N46RRo&t=2821s) · b000092

**English**

Question is, should the judge be bigger? It's not a hard constraint, but it's typically something that people would take, a bigger model that would have a strong reasoning capabilities that could really tease out what's good and what's not good.

**中文**

问题是，评判者是否应该更大？这不是一个硬性约束，但人们通常会选择一个更大的模型，具备较强的推理能力，能够真正分辨哪些好、哪些不好。

### [47:19](https://www.youtube.com/watch?v=8fNP4N46RRo&t=2839s) · b000093

**English**

Cool. So with that, I'm going to just go over the best practices that we've seen. So we saw that in order for our LLM-as-a-Judge to output a score, we need to give the criteria that we want this to be evaluated against. But sometimes these criteria may be a little bit subjective. So one thing that really works very well is to have crisp guidelines, so really explicit what we want, what we don't want.

**中文**

好，接下来我来回顾一下我们提到的最佳实践。我们看到，要让 LLM-as-a-Judge 输出分数，需要提供我们希望它依据的评估标准。但有时这些标准可能稍显主观。因此，一个非常有效的做法是提供清晰明确的指南，明确说明我们想要什么、不想要什么。

### [47:57](https://www.youtube.com/watch?v=8fNP4N46RRo&t=2877s) · b000094

**English**

The other point is you may see different kinds of scaling out there, so sometimes people having a scale that is maybe more granular and maybe other cases where we're just operating on a binary scale. So typically, what people would tend to prefer is actually the binary one because it makes the job of the LLM-as-a-Judge easier. So it's just either good or bad. And also, when it comes to aligning the judge with human ratings, humans, they typically also find it easier to just judge out of two options, as opposed to several.

**中文**

另一点是，大家可能会看到不同类型的评分量表，有时人们使用更细的量表，有时则只使用二元量表。通常，人们实际上更倾向于使用二元量表，因为这让 LLM-as-a-Judge 的任务更容易，只需判断好或不好。而且，在让评判者与人工评分对齐时，人类通常也觉得在两个选项中做判断，比在多个选项中做判断更容易。

### [48:42](https://www.youtube.com/watch?v=8fNP4N46RRo&t=2922s) · b000095

**English**

So it just removes the noise of having several possible choices. And it's not necessarily an extra signal that may be really useful. So here the tip is to use a binary scale, like a pass or fail kind of score, as opposed to a gradual one. The third tip is to make sure to output the rationale before outputting the score. And we've seen this is along the same ideas of outputting a chain of thought before providing the response, which is something that is done by our reasoning models.

**中文**

这样可以消除多个可选项带来的噪声，而且多个选项也不一定能提供真正有用的额外信号。所以，这里的建议是使用二元量表，比如通过或不通过的分数，而不是渐进式量表。第三条建议是，确保先输出理由，再输出分数。我们已经看到，这与先输出 chain of thought 再给出回答的思路相同，而推理模型就是这样做的。

### [49:21](https://www.youtube.com/watch?v=8fNP4N46RRo&t=2961s) · b000096

**English**

So it's typically something that will improve the judge's performance. So we've talked about the different kinds of biases. So position, verbosity, self-enhancement. But it's not the only ones, of course. And I guess, people typically also look at how to mitigate those with the remedies that we mentioned. So far, we've stated that we do not need human ratings to get started.

**中文**

这通常能提高评判者的表现。我们讨论了不同类型的偏差，包括位置、冗长和自我增强。当然，不只有这些。人们通常还会考虑如何用前面提到的方法来缓解这些偏差。到目前为止，我们说过，不需要人工评分也能开始。

### [49:54](https://www.youtube.com/watch?v=8fNP4N46RRo&t=2994s) · b000097

**English**

But a good practice is to still look at how the LLM ratings compare with the human ratings. So here one tip is to just calibrate the responses that the judge is giving with respect to the human ratings because at the end of the day, it is the quantity that we want to approximate. And so here, I guess, if there is the budget and it's something that is possible for the project, one good practice is to collect the human ratings, output the LLM-as-a-Judge scores, and then run some correlation analysis to see if there is something that can be improved in terms of the prompt, mainly the prompt.

**中文**

不过，一个好做法仍然是看看 LLM 评分与人工评分相比如何。这里有个建议，就是参照人工评分来校准评判者给出的回答，因为归根结底，那才是我们想近似的量。如果有预算，而且项目条件允许，一个好做法就是收集人工评分，输出 LLM-as-a-Judge 分数，再做一些相关性分析（correlation analysis），看看提示词是否还有改进空间，主要是提示词。

### [50:41](https://www.youtube.com/watch?v=8fNP4N46RRo&t=3041s) · b000098

**English**

And then the last thing is the temperature. So if you remember, the temperature is a parameter that you can tweak to make your generation more deterministic as opposed to more creative. And so you will see that for evaluation tasks, people use a low temperature because they want to make their evaluation experiments reproducible. Let's imagine you do one evaluation, and then you do another one, let's say, two days later, you don't want the scores to be super different.

**中文**

最后一点是温度（temperature）。如果大家还记得，temperature 是一个可以调整的参数，让生成更确定，或者更有创造性。你会看到，人们在评估任务中使用较低的 temperature，因为他们希望评估实验可以复现。想象一下，你做了一次评估，两天后又做一次，你不会希望分数差异特别大。

### [51:21](https://www.youtube.com/watch?v=8fNP4N46RRo&t=3081s) · b000099

**English**

So you will see a temperature value of something like 0.1 or 0.2. These are very common values that people take. And so long story short, if we were to recap, we went from the ideal scenario being that each LLM output is rated by humans to actually having some kind of approximation with these LLM-as-a-Judge models that can do this evaluation, I guess, without any constraints or without any need for human judgments.

**中文**

所以，你会看到 0.1 或 0.2 这样的 temperature 值。这些都是人们常用的数值。简而言之，回顾一下，我们从每条 LLM 输出都由人类评分的理想情形，转向了使用 LLM-as-a-Judge 模型进行某种近似。我想，这些模型能够在没有任何约束、或者不需要人类判断的情况下进行评估。

### [52:03](https://www.youtube.com/watch?v=8fNP4N46RRo&t=3123s) · b000100

**English**

But as we mentioned in the best practices, making sure that the LLM-as-a-Judge scores and the human ratings do not diverge is something that we should keep in mind as we improve our model because it may be that we're improving our model so that our LLM-as-a-Judge score is very high, but the LLM-as-a-Judge score is itself an approximation of human ratings.

**中文**

不过，正如最佳实践中提到的，在改进模型时，应该始终留意，确保 LLM-as-a-Judge 分数与人工评分不会出现偏离。因为我们可能把模型改进到 LLM-as-a-Judge 分数很高，但 LLM-as-a-Judge 分数本身只是人工评分的近似。

### [52:33](https://www.youtube.com/watch?v=8fNP4N46RRo&t=3153s) · b000101

**English**

So I guess you don't want to overoptimize against, I guess, the proxy. And so that's why you want to have that proxy be as aligned as possible with your ground truth labels, which are human ratings.

**中文**

因此，我想，你不会希望针对代理指标（proxy）过度优化。这就是为什么应该让这个 proxy 尽可能与 ground truth 标签，也就是人工评分对齐。

### [52:52](https://www.youtube.com/watch?v=8fNP4N46RRo&t=3172s) · b000102

**English**

Cool. So we have a few minutes left before giving it to Shervine. So I'm going to quickly go over the kinds of dimensions that people measure LLM output against. So we have broadly-- so there are many dimensions, but just to simplify things, there are two main dimensions that we can look at here. So one is how well your task is being done, so task performance with things like, was the response useful, was the response factual, was the response relevant, among other things.

**中文**

好，在交给 Shervine 之前，我们还有几分钟。我快速介绍一下人们衡量 LLM 输出时会使用哪些维度。总体上——维度有很多，但为了简化，我们可以看两个主要维度。一个是任务完成得如何，也就是任务表现（task performance），例如回答是否有用、是否符合事实、是否相关，等等。

### [53:33](https://www.youtube.com/watch?v=8fNP4N46RRo&t=3213s) · b000103

**English**

And also, how aligned was the response format in terms of tone, in terms of whether the style was something that is aligned with what we want, in terms of whether there was any unsafe elements of response that was given to the user? And I just want us to spend maybe five minutes on the factory dimension, which is actually something that requires a little bit more work.

**中文**

还有，回答的格式有多符合要求，例如语气、风格是否符合我们的期望，以及提供给用户的回答中是否有不安全的内容。我想花大约五分钟讨论一下工厂（factory）维度 \[字幕疑误，可能指 factuality，即事实性\]，这个维度实际上需要多做一些工作。

### [54:06](https://www.youtube.com/watch?v=8fNP4N46RRo&t=3246s) · b000104

**English**

And I'll give you just a setting. So let's suppose we have some text output, and our goal is to quantify how factual that output is. So I'm going to read the text out loud. Teddy bears, first created in the 1920s, were named after President Theodore Roosevelt after he proudly wanted to shoot a captured bear on a hunting trip. So what we want is quantify how factual that piece of text is.

**中文**

我先给大家一个情境。假设我们有一段文本输出，目标是量化这段输出有多符合事实。我把这段文字读出来：泰迪熊最早诞生于 1920 年代，以 Theodore Roosevelt 总统命名，因为他在一次狩猎旅行中曾骄傲地想要射杀一只被捕获的熊。我们想做的，就是量化这段文字的事实性。

### [54:41](https://www.youtube.com/watch?v=8fNP4N46RRo&t=3281s) · b000105

**English**

So I told you previously that we typically prefer binary scales when it comes to rating something with respect to a dimension. But the thing with factuality is that there's a lot of nuance. Some texts may be very wrong. Some texts may be a little bit wrong. Some texts may be not wrong at all. So we want to capture how wrong the text is, given the fact that the text can contain a lot of sentences.

**中文**

我之前说过，针对某个维度评分时，我们通常更喜欢二元量表。但事实性有很多细微差别。有些文本可能错得很严重，有些可能只错一点，有些可能完全没错。因此，考虑到文本可能包含很多句子，我们希望捕捉它到底错到什么程度。

### [55:17](https://www.youtube.com/watch?v=8fNP4N46RRo&t=3317s) · b000106

**English**

And if there's one small issue, we don't want to just say the whole thing was not correct. So I'm not sure if you saw in this text, but there are actually two errors. So it's not 1920s but 1900s that the teddy bears were first created. And the president didn't want to proudly shoot. He actually, I think, refused. So if we are in such a case, the question that we want to tackle here is how do we want to quantify this nuance.

**中文**

如果只有一个小问题，我们不想直接说整段都不正确。不知道大家有没有发现，这段文字实际上有两处错误。泰迪熊最早诞生于 1900 年代，而不是 1920 年代。那位总统也不是想骄傲地开枪，我记得他实际上拒绝了。所以，在这种情况下，我们想解决的问题是，应该如何量化这种细微差别。

### [55:54](https://www.youtube.com/watch?v=8fNP4N46RRo&t=3354s) · b000107

**English**

So this is an open question that people have been writing papers on. So what I'm going to tell you now is something that people typically use nowadays based on research that has been done. So we typically operate in a few steps. So the first step is for us to go from the original text output to a list of facts because when you look at a text, it actually contains a lot of facts that need to be checked.

**中文**

这是一个人们一直在发表论文探讨的开放问题。接下来我要介绍的，是基于已有研究、如今人们通常使用的一种方法。我们通常分几步进行。第一步是，把原始文本输出转化为事实列表，因为一段文本实际上包含很多需要核查的事实。

### [56:33](https://www.youtube.com/watch?v=8fNP4N46RRo&t=3393s) · b000108

**English**

And so the idea here is to aggregate the factuality of this text along the dimension of the facts that are present in this text. So in this example, we would have one LLM call that transforms our original multi-sentence, multi-paragraph potentially text into a list of facts. So here in this example, we would have four facts.

**中文**

这里的思路是，依据文本中包含的各项事实，汇总这段文本的事实性。在这个例子中，我们会调用一次 LLM，把原始文本——它可能包含多个句子、多个段落——转化为事实列表。在这个例子里，我们会得到四项事实。

### [57:07](https://www.youtube.com/watch?v=8fNP4N46RRo&t=3427s) · b000109

**English**

So that's the first step. The second step is we would go over each of these facts and check whether it is correct or not. And so here, we would typically proceed in a binary fashion because if you think about it, a fact is either correct or not. I mean, you may have some in between, but we don't want to overcomplicate the task. And so here the fact-checking process would typically involve the other technique we've seen last lecture, like RAG, for instance.

**中文**

这是第一步。第二步是逐项检查这些事实，看看它们是否正确。这里通常采用二元方式，因为想一想，一项事实要么正确，要么不正确。当然，也许有一些介于两者之间的情况，但我们不想把任务弄得过于复杂。这里的事实核查（fact-checking）过程，通常会用到上一讲介绍的其他技术，例如 RAG。

### [57:46](https://www.youtube.com/watch?v=8fNP4N46RRo&t=3466s) · b000110

**English**

Given a piece of text, we want to, I guess, query a knowledge base with the actual fact and then check whether the fact that it's here is actually correct. So this fact-checking process is typically something that involves things like RAG, web search is also something else, and so on. So you can think of this fact-checking step as also involving LLM calls.

**中文**

给定一段文本，我们希望用具体的事实查询知识库，然后检查这里的事实是否真的正确。所以，fact-checking 过程通常涉及 RAG 之类的技术，网页搜索（web search）也是一种，等等。因此，可以把这个 fact-checking 步骤理解为也涉及 LLM 调用。

### [58:17](https://www.youtube.com/watch?v=8fNP4N46RRo&t=3497s) · b000111

**English**

And so you can also think of some facts being more important than others. So as an example, maybe the fact that the president proudly wanted to shoot the bear is not as important as, let's say, the name of the person after which the teddy bears were named. So you can think of also having weights that quantifies the importance of each fact.

**中文**

你也可以认为，有些事实比其他事实更重要。举个例子，总统曾骄傲地想要射杀那只熊这件事，也许不如泰迪熊以谁的名字命名重要。因此，也可以使用权重来量化每项事实的重要性。

### [58:49](https://www.youtube.com/watch?v=8fNP4N46RRo&t=3529s) · b000112

**English**

So people would use something like this formula, which is an aggregation over all the facts with some weight that quantifies the importance of each fact. So these weights, alpha i, can be all equal to one another if you want to make it simpler. It's not something that is necessarily the case everywhere that these must be different. But it may be something that you can tweak.

**中文**

人们会使用类似这样的公式，对所有事实进行汇总，并用某个权重量化每项事实的重要性。如果你想简单一点，这些权重 alpha i 可以全部相等。并不是所有情况下都要求它们必须不同。不过，这可以是你调整的一个地方。

### [59:20](https://www.youtube.com/watch?v=8fNP4N46RRo&t=3560s) · b000113

**English**

So if we go back to our initial question, which is, how do you quantify the factuality of this text? Here you would say, OK, the second and the third facts are both correct. We know how important they are. So we run this aggregation formula, and we obtain a score of 0.6. So that means that there are some errors. But we still have some things that were still factually correct.

**中文**

回到最初的问题，也就是如何量化这段文本的事实性。这里你可以说，第二项和第三项事实都是正确的，我们也知道它们的重要程度。于是，我们用这个汇总公式计算，得到 0.6 的分数。这意味着其中存在一些错误，但仍有一些内容符合事实。

### [59:52](https://www.youtube.com/watch?v=8fNP4N46RRo&t=3592s) · b000114

**English**

This is typically how you would run this criteria with, I guess, the techniques that we have nowadays.

**中文**

我想，这就是使用我们如今拥有的技术，通常会如何评估这个标准。

### [1:00:02](https://www.youtube.com/watch?v=8fNP4N46RRo&t=3602s) · b000115

**English**

Cool. I know I'm two minutes late. And with that, I'm going to give it to Shervine.

**中文**

好，我知道我已经超时两分钟了。接下来交给 Shervine。

### [1:00:09](https://www.youtube.com/watch?v=8fNP4N46RRo&t=3609s) · b000116

**English**

Thank you, Afshine. So before we move on to looking at specific benchmarks, I wanted to take a detour and look at what is happening on the agent side of things. So if you recall what we discussed last lecture, we talked about this ReAct framework where you could decompose what was going on within an agent into specific steps. So it's usually three steps.

**中文**

谢谢你，Afshine。在继续看具体的基准测试（benchmarks）之前，我想稍微岔开一下，看看智能体（agent）这边的情况。如果大家还记得上一讲的讨论，我们讲过 ReAct 框架，可以把 agent 内部发生的过程分解为若干具体步骤。通常有三个步骤。

### [1:00:40](https://www.youtube.com/watch?v=8fNP4N46RRo&t=3640s) · b000117

**English**

It can be observe, plan, act, or it can have other names. But the fact is that you have several atomic steps that can loop. So if you take a look at the typical agent's inner working, you can see a pattern like this. Now you might wonder, how do you even evaluate such a thing. So let's take a look at just one loop.

**中文**

它们可以叫观察、规划、行动，也可以有其他名称。但关键是，你有几个可以循环的原子步骤（atomic steps）。如果看看典型 agent 的内部工作方式，就能看到这样的模式。现在你可能想知道，这种东西到底该怎么评估。我们先只看一轮循环。

### [1:01:11](https://www.youtube.com/watch?v=8fNP4N46RRo&t=3671s) · b000118

**English**

And then let's see together what can the errors be, in order for us to have an idea of what would an evaluation result mean on an agentic workflow. So I'm going to show a slide that we had presented at the previous lecture. And we had seen that we can decompose a tool call into these three steps. So let's take our favorite example.

**中文**

然后我们一起来看看可能有哪些错误，以便理解智能体工作流的评估结果意味着什么。我要展示上一讲用过的一张幻灯片。我们已经看到，可以把一次工具调用分解为这三个步骤。还是用我们最喜欢的例子。

### [1:01:43](https://www.youtube.com/watch?v=8fNP4N46RRo&t=3703s) · b000119

**English**

Let's say, you want to find a bear near you. So you would ask that to the model. So the first stage is to find the right tool call with the right argument. And then once you have found this right tool call, you need to execute it. And then based on your tool call prediction and on the results that you obtained from your tool, you would infer the results at the last step. So these are three steps.

**中文**

假设你想在附近找到一只熊，你会向模型提出这个请求。第一阶段是找到正确的工具调用，并使用正确的参数。找到这个正确的工具调用后，需要执行它。然后，依据工具调用预测和工具返回的结果，在最后一步推断结果。这就是三个步骤。

### [1:02:14](https://www.youtube.com/watch?v=8fNP4N46RRo&t=3734s) · b000120

**English**

And you might have a series of them in the case of an agentic workflow where you call multiple tools and then build up your reasoning until reaching an answer that you then give to the user.

**中文**

在智能体工作流中，你可能会经历一连串这样的过程，调用多个工具，不断推进推理，直到得到一个答案，再把它交给用户。

### [1:02:29](https://www.youtube.com/watch?v=8fNP4N46RRo&t=3749s) · b000121

**English**

So now let's look at what can the failure modes, what can they be, at each of these steps. So first, let's take a look at possible tool prediction errors. So the first one I want to mention is the case where the error is that from a user query that obviously needs a tool, that you don't actually use the tool. So here let's suppose that if you want to find a bear, you have the tool to find bears at-hand, but you don't use it.

**中文**

那么现在我们来看看，在这些步骤中的每一步，失效模式（failure modes）可能有哪些。首先，我们来看看可能的工具预测（tool prediction）错误。我想提到的第一种情况是，用户查询显然需要一个工具，但你实际上没有使用这个工具。这里假设你想找一只熊，手头也有找熊的工具，但你没有使用它。

### [1:03:07](https://www.youtube.com/watch?v=8fNP4N46RRo&t=3787s) · b000122

**English**

So typically, if you don't use it, a possible behavior from the model can be to say an error. So an error-- by an error, I mean, sorry, I cannot do that. And this, in assistant terms, you can call this a punt. So when you don't answer the question, you just fail. It's called a punt. So you might punt. Here, sorry, I don't where I can find one. And let's see together what could possibly cause this issue and how we could remedy it.

**中文**

通常，如果你不使用它，模型可能会给出一个错误。所谓错误，我指的是：“抱歉，我做不到。”用助手领域的术语来说，这可以叫作回避作答（punt）。也就是你没有回答问题，只是失败了，这叫作 punt。所以你可能会 punt。这里是：“抱歉，我不……哪里能找到一只。”我们一起来看看，什么可能导致这个问题，以及我们可以如何补救。

### [1:03:42](https://www.youtube.com/watch?v=8fNP4N46RRo&t=3822s) · b000123

**English**

So I don't know if you recall the concept of tool router or tool selector that we had introduced. So usually, when you are dealing with tools, you don't have just one. You have multiple ones. And the number of tools that might be useful for a large scale in the sense of number of users LLM, might be large. So you don't want to input all the function APIs at every call. So it might be the case that you have this intermediary step, where you filter down the sets of possible functions that you can put in the preamble.

**中文**

不知道大家是否还记得我们介绍过的工具路由器（tool router）或工具选择器（tool selector）的概念。通常，处理工具时，你不会只有一个工具，而是有多个。对于用户数量规模很大的大语言模型（LLM），可能有用的工具数量也会很大。因此，你不想在每次调用时都输入所有函数 API。所以，可能会有这样一个中间步骤：筛选可放入前置说明（preamble）中的候选函数集合。

### [1:04:21](https://www.youtube.com/watch?v=8fNP4N46RRo&t=3861s) · b000124

**English**

And here these two selectors or tool routers, they have the property of trying to be recall-oriented. So you want to trim the list of functions that you want to input in the preamble. But you want to at least find those that you need. So the main property here is that you want to save on context space, but you still want to ensure most of your use cases are still working.

**中文**

这里，这两个选择器，也就是 tool routers，会尽量以召回率为导向（recall-oriented）。“这两个选择器”\[字幕疑误，可能指 tool selectors\]。你想精简输入 preamble 的函数列表，但至少要找到你需要的那些。因此，这里的主要特性是，你想节省上下文空间，同时仍要确保大多数用例能够正常工作。

### [1:04:54](https://www.youtube.com/watch?v=8fNP4N46RRo&t=3894s) · b000125

**English**

So this is why here, when we say tool router error, we actually mean a recall error. So it means it's possible that we just didn't select the right tool among the set of tools. And let's say, this is the cause. Then it's pretty clear we just have to adjust the tool router in order for it to be predicting the right tool. So this can be one kind of issue. Another kind is, hey, actually, the tool was included in this list of function APIs, but it's just that the LLM didn't think about using it.

**中文**

所以，当我们在这里说 tool router 错误时，实际上指的是召回错误（recall error）。也就是说，我们可能没有从工具集合中选出正确的工具。假设原因就是这个，那么很明显，我们只需要调整 tool router，让它能够预测出正确的工具。这是一类问题。另一类是，实际上工具已经包含在这份函数 API 列表里，只是 LLM 没想到要使用它。

### [1:05:35](https://www.youtube.com/watch?v=8fNP4N46RRo&t=3935s) · b000126

**English**

So maybe this fine teddy bear was in there, but we just don't use it. The LLM directly outputs a response. So in that case, if you recall, we had mentioned techniques to teach an LLM to use a tool. So you would need to revisit that part and either--if you had trained it with SFT, so include this pattern maybe to train the model to recognize it, or if you had done prompt tuning, then you should revisit your prompt in order for this call to make sense to the model that you should use that tool.

**中文**

所以，也许这个 fine teddy bear \[字幕疑误，可能指 find teddy bear\] 已经在里面，但我们就是没有使用它。LLM 直接输出了一个回答。在这种情况下，如果大家还记得，我们提到过教 LLM 使用工具的技术。你需要回头看看那部分内容：如果你用监督微调（SFT）训练过它，那么也许应该加入这种模式，让模型学会识别它；或者，如果你做过提示调优（prompt tuning），那么你应该重新检查提示词，让模型明白，在这次调用中应该使用那个工具。

### [1:06:17](https://www.youtube.com/watch?v=8fNP4N46RRo&t=3977s) · b000127

**English**

Great. So this is one kind of possible error. Another one that you might see in the wild when you want to debug agents is at the time of tool calls, it might be the case that the model comes up with a function name that just simply doesn't exist. So here I mentioned the tool hallucination. This is what I mean by that. So it calls a function that is just not defined. So here our API was called, if you remember, find teddy bear.

**中文**

很好。这是一类可能的错误。调试智能体（agents）时，你在实际中可能看到的另一种错误是：在工具调用（tool calls）时，模型可能编造出一个根本不存在的函数名。这里我提到了工具幻觉（tool hallucination），指的就是这个。它调用了一个根本没有定义的函数。如果大家还记得，这里我们的 API 叫作 find teddy bear。

### [1:06:50](https://www.youtube.com/watch?v=8fNP4N46RRo&t=4010s) · b000128

**English**

So this was the function that existed. And in this example of failure, the model tries to call the function find\_bear, which I haven't defined. So when you see such errors, you have several potential causes, one of them being that the model simply doesn't round well overall. And typically, it occurs if the model is too simple.

**中文**

这才是实际存在的函数。在这个失败示例中，模型试图调用 find\_bear 函数，而我并没有定义它。当你看到这类错误时，可能有几个原因，其中之一是模型整体上就是不太会 round \[字幕疑误，可能指 ground\]。通常，模型过于简单时就会发生这种情况。

### [1:07:21](https://www.youtube.com/watch?v=8fNP4N46RRo&t=4041s) · b000129

**English**

So it's an empirical observation. If it's too weak, maybe it can make up things that it thinks can be reasonable. But it doesn't actually ground on your instructions. And here I have no better remedy proposal than to maybe upgrade the model, if you see that this is truly the case, and then see if this is reproducible. Some other potential causes could be coming from actually you. So the model is trained on very high quality data during its SFT stage.

**中文**

这是一个经验观察。如果模型太弱，它可能会编造一些自己认为合理的东西，但实际上并没有以你的指令为依据进行 grounding。如果你发现确实如此，我没有更好的补救建议，只能建议也许升级模型，然后看看这个问题是否还能复现。其他一些可能的原因，实际上可能出在你自己身上。模型在 SFT 阶段接受的是质量非常高的数据训练。

### [1:07:56](https://www.youtube.com/watch?v=8fNP4N46RRo&t=4076s) · b000130

**English**

So it has seen what great APIs look like. So these tools that you define that help the user achieve what they're looking for might not be written in the best way, if you didn't use AI-assistant coding, let's say, or--you don't necessarily have to use AI-assistant coding to write these. But these are typically a great way to check whether your implementation makes sense from a model standpoint.

**中文**

所以，它见过优秀的 API 是什么样的。因此，你定义的这些帮助用户实现目标的工具，可能写得不够好，比方说，你没有使用 AI 辅助编程（AI-assistant coding），或者——你当然不一定非要用 AI-assistant coding 来写这些工具。但它通常是检查你的实现从模型角度来看是否合理的一种很好方式。

### [1:08:26](https://www.youtube.com/watch?v=8fNP4N46RRo&t=4106s) · b000131

**English**

And if it doesn't, then a typical remedy is to either--renaming the API just a function name, and the arguments just go a long way because this is what the model will see when it comes to your tool call. It sees the API function name. It sees the arguments and the high-level descriptions. So these are your three knobs to tune in order to make it sound more logical and then linked to the actual task at-hand.

**中文**

如果不合理，那么一种典型的补救办法是——重新命名 API，仅仅修改函数名和参数名就能产生很大作用，因为这就是模型在进行工具调用时会看到的内容。它会看到 API 函数名、参数，以及高层描述。因此，这就是你可以调整的三个控制项，让它听起来更符合逻辑，并且与当前的实际任务关联起来。

### [1:09:05](https://www.youtube.com/watch?v=8fNP4N46RRo&t=4145s) · b000132

**English**

At the very beginning, I was saying, maybe the model is too weak. But actually, maybe the first thing you should check is whether the horizontal instructions--so horizontal across tools, whether these are clear enough. Maybe the model hasn't really understood that it needs to use functions that are given to it. So maybe it's just making up function names that it believes could have access to. So the first thing to check would probably be to see if this phenomenon is generalized and see if these horizontal instructions, they are concisely saying that you should make sure to use available functions.

**中文**

最开始，我说也许是模型太弱。但实际上，你首先应该检查的，也许是横向指令（horizontal instructions）——也就是跨工具的指令——是否足够清晰。也许模型并没有真正理解，它需要使用提供给它的函数。因此，它可能只是在编造自己认为可以访问的函数名。所以，首先应该检查的，大概是这种现象是否普遍存在，以及这些横向指令是否简明地说明了：务必使用可用的函数。

### [1:09:50](https://www.youtube.com/watch?v=8fNP4N46RRo&t=4190s) · b000133

**English**

And then on that, you can iterate on these top level instructions and maybe iterate with an LLM itself because typically, top-level instructions, they are very important. So you need perfect formatting and perfect logic. So typically being able to detail them with great detail is helpful.

**中文**

然后，你可以据此迭代这些顶层指令（top-level instructions），也许还可以与 LLM 本身一起迭代，因为顶层指令通常非常重要。你需要完美的格式和完美的逻辑。因此，通常能够非常详细地描述它们会有所帮助。

### [1:10:18](https://www.youtube.com/watch?v=8fNP4N46RRo&t=4218s) · b000134

**English**

Now let's see a third possible failure cause. So let's say, you have your model and your user prompts, but you just don't use the right tool. So here if the user says, find a bear near me, one other reasonable approach would be, what if you just send a message asking for a bear? That would be reasonable. But maybe that's not what you want to implement as a behavior for your user.

**中文**

现在我们来看第三种可能的失败原因。假设你有模型，也有用户提示词，但就是没有使用正确的工具。如果用户说“找一只我附近的熊”，另一种合理的方法可能是：直接发一条消息求一只熊，怎么样？这也合理。但也许这不是你想为用户实现的行为。

### [1:10:52](https://www.youtube.com/watch?v=8fNP4N46RRo&t=4252s) · b000135

**English**

So in that case, it's not clear to the model what approach you prefer. And it is on your--it's your responsibility to ensure it is indeed clear. And then you have to do that at two different levels. So the first one is potentially also at the tool router level. Maybe the tool router doesn't know that for this kind of query, you should have the tool that you had in mind as part of the results.

**中文**

这种情况下，模型不清楚你更偏好哪种方法。而这在于你——确保这一点确实清楚，是你的责任。你需要在两个不同层面上做到这一点。第一个也可能是 tool router 层面。也许 tool router 不知道，对于这类查询，结果中应该包含你心里想的那个工具。

### [1:11:25](https://www.youtube.com/watch?v=8fNP4N46RRo&t=4285s) · b000136

**English**

So it's possible that you have a recall issue that you need to fix. And then the second one is simply going back to the APIs of both functions, maybe the conflicts in scope. So you want to go back to each of them and be precise into which situations should be dealt with with which tool. So being very precise in these APIs just plays a lot here.

**中文**

所以，你可能有一个需要修复的召回问题。第二个则是回头检查这两个函数的 API，也许它们的适用范围存在冲突。你需要分别检查它们，并准确说明哪些情况应该由哪个工具处理。因此，在这些 API 中表述得非常精确，在这里会起到很大作用。

### [1:12:00](https://www.youtube.com/watch?v=8fNP4N46RRo&t=4320s) · b000137

**English**

Great. So now we're going to go through a fourth and last failure mode for this tool prediction task, which is, what if you have the right tool, but you just don't have the right arguments? So you have already gone one step. You have found the right tool, but then this last mile of making sure that the tool is run with what you would like is not fulfilled. So here if I say, find a beer near me, and it outputs--and it uses the coordinates 0, 0, which is somewhere in the Southern Atlantic--it's not likely that I'm actually there, that can reflect an issue.

**中文**

很好。现在我们来看看这个工具预测任务的第四种，也是最后一种失效模式：如果你有了正确的工具，但参数不正确，会怎么样？你已经向前迈出了一步，找到了正确的工具，但最后一步，也就是确保工具按你的意图运行，却没有完成。这里，如果我说“找一杯我附近的啤酒”，它输出——它使用坐标 0, 0，也就是南大西洋的某个地方——而我实际上不太可能在那里，这就可能反映出一个问题。

### [1:12:44](https://www.youtube.com/watch?v=8fNP4N46RRo&t=4364s) · b000138

**English**

And one possible explanation for this is that maybe it simply doesn't know where I am because I haven't specified in my query that I'm here at Stanford, and it just tries to make up my coordinates. So one thing that you should double check is making sure that the context carries the location information. So if I haven't provided that as a setting on my LLM map, it's possible it's not there.

**中文**

一种可能的解释是，它也许根本不知道我在哪里，因为我没有在查询中说明我在 Stanford，而它只是试图编造我的坐标。因此，你应该仔细检查的一点是，确保上下文包含位置信息。如果我没有在 LLM map \[字幕疑误，可能指 LLM app\] 中将其作为设置提供，那么这些信息可能就不存在。

### [1:13:17](https://www.youtube.com/watch?v=8fNP4N46RRo&t=4397s) · b000139

**English**

And then let's say, if it's not there, maybe you would want to introduce a location finder tool that is executed beforehand. And if it fails because I haven't given the app to permission to see my location, then maybe you could have actionable error shown to the user, instead of having some dummy parameters passed in. So this is one potential remedy. And then the second one is maybe it's his arguments, but the model just doesn't know what it should put as input.

**中文**

假设这些信息不存在，也许你会想引入一个预先执行的位置查找工具。如果它失败了，因为我没有授予应用查看我位置的权限，那么也许你可以向用户显示一条能指导其采取行动的错误信息，而不是传入一些虚设参数。这是一种可能的补救办法。第二种可能是，也许是 his arguments \[字幕疑误，可能指这些参数已有相关信息\]，但模型就是不知道应该输入什么。

### [1:13:53](https://www.youtube.com/watch?v=8fNP4N46RRo&t=4433s) · b000140

**English**

So that could also be another reason. And then on that, this is a common remedy to go back and then retrain either the model on how it uses these tools or rewrite the API.

**中文**

这也可能是另一个原因。针对这种情况，一个常见的补救办法是回过头来，重新训练模型如何使用这些工具，或者重写 API。

### [1:14:12](https://www.youtube.com/watch?v=8fNP4N46RRo&t=4452s) · b000141

**English**

So we have seen four ways to--I mean, four failure modes for the tool prediction step. Now we're going to see two more on this tool called step.

**中文**

我们已经看到了工具预测步骤中的四种方式——我是说，四种失效模式。现在我们要看看这个 tool called \[字幕疑误，可能指 tool call\] 步骤中另外两种失效模式。

### [1:14:26](https://www.youtube.com/watch?v=8fNP4N46RRo&t=4466s) · b000142

**English**

So the first one is a very simple one, from a mindset perspective, maybe your tool just doesn't output the right response. So it's a very vague category. And as an example, maybe your code logic has a bug somewhere, and it just returns an error. Those that you see in Python, maybe it hits some value error or anything else.

**中文**

第一种从思路上看非常简单：也许你的工具就是没有输出正确的响应。这是一个很宽泛的类别。举个例子，也许你的代码逻辑在某个地方有 bug，只返回了一个错误。就是你在 Python 中看到的那些错误，也许触发了某个值错误（value error），或者其他错误。

### [1:14:59](https://www.youtube.com/watch?v=8fNP4N46RRo&t=4499s) · b000143

**English**

And I just want to say that it might not be necessarily the case that hitting an error is bad because sometimes in the case of finding your location, if you haven't provided your permission to find the location, maybe it will hit an error, and the model will anchor on that error to convey the status to the user. But in general, it's not really common practice to return errors just because the model could interpret it as an internal tool error.

**中文**

我只是想说，触发错误不一定是坏事。因为有时，比如在查找你的位置时，如果你没有授权获取位置，也许就会触发一个错误，而模型会以这个错误为依据，将状态传达给用户。但一般来说，直接返回错误并不是很常见的做法，因为模型可能会将其理解为内部工具错误。

### [1:15:35](https://www.youtube.com/watch?v=8fNP4N46RRo&t=4535s) · b000144

**English**

So sometimes when you hit an error, and then you ask the model to synthesize the tool call it has seen, sometimes it just says, oh, sorry, I couldn't do it, but it's my fault. It's because I encountered an error. It doesn't really say actionably what happened. And instead, the fix here is to convey these outputs in a meaningful manner. So typically, you have a structured output, and you return a true output instead of an error.

**中文**

所以，有时触发了一个错误，然后你让模型综合它看到的工具调用信息，它可能只会说：“哦，抱歉，我做不到，是我的错，因为我遇到了一个错误。”它并没有以能指导行动的方式说明发生了什么。这里的解决办法是，以有意义的方式传达这些输出。通常，你会使用结构化输出（structured output），返回一个真正的输出，而不是一个错误。

### [1:16:07](https://www.youtube.com/watch?v=8fNP4N46RRo&t=4567s) · b000145

**English**

Here it's a general case just to say that just check your tool implementation. So you have the right arguments, you have the right tool, but you just don't have the right value. So just a software engineering problem, just go and fix the tool.

**中文**

这里是泛指一种情况，就是说，检查你的工具实现。参数正确，工具也正确，但就是没有得到正确的值。这只是一个软件工程问题，去修复工具就行了。

### [1:16:25](https://www.youtube.com/watch?v=8fNP4N46RRo&t=4585s) · b000146

**English**

And the second category of issues that we see at the backend level is when you return no response. And returning no response is often bad when the tool is one that performs an action. So let's say, last lecture, we talked about increasing the thermostat for your teddy bear who was cold. So if you increase the thermostat, and the tool doesn't say anything, so the model doesn't know if it has done the task successfully or not.

**中文**

我们在后端层面看到的第二类问题是没有返回响应。如果工具会执行某个动作，不返回响应通常很糟糕。比如，上节课我们讨论过，为觉得冷的泰迪熊调高恒温器的温度。如果你调高了恒温器，但工具什么也没说，那么模型就不知道任务是否成功完成了。

### [1:17:01](https://www.youtube.com/watch?v=8fNP4N46RRo&t=4621s) · b000147

**English**

So it could well come up with a false confirmation of hey, all is good. I have increased the thermostat. No worries. But it actually hasn't. So this is why a common guidance is to always make sure that tool calls are followed by meaningful outputs. So as usual, you have this structured message and you should take advantage of it to convey what has happened as part of your tool in order to make sure that the model, in turn, knows what to convey to the user or knows how to continue that agentic loop.

**中文**

因此，它很可能给出一个错误的确认：“嘿，一切都好了。我已经调高恒温器了，别担心。”但实际上并没有。所以，一条常见的指导原则是，始终确保工具调用之后有有意义的输出。和往常一样，你有这种结构化消息，应该利用它来传达工具中发生了什么，以确保模型进而知道该向用户传达什么，或者知道如何继续这个智能体循环（agentic loop）。

### [1:17:45](https://www.youtube.com/watch?v=8fNP4N46RRo&t=4665s) · b000148

**English**

So always output something. And let's say, you want to find a teddy bear, and you haven't found any, then here you will be surprised by what I say, but it's actually better to output an empty JSON than just outputting none because an empty JSON could mean I found no bears, but an output of none doesn't say anything. So even in that case, an empty output in the sense of an empty JSON is meaningful.

**中文**

所以，始终要输出点什么。假设你想找一只泰迪熊，但一只也没找到。接下来我说的话也许会让你惊讶：实际上，输出一个空 JSON 比仅仅输出 none 更好，因为空 JSON 可以表示“我没有找到熊”，而输出 none 什么也没有说明。所以，即使在这种情况下，空 JSON 意义上的空输出也是有意义的。

### [1:18:17](https://www.youtube.com/watch?v=8fNP4N46RRo&t=4697s) · b000149

**English**

And make sure to use that meaning in the way you encode your tool. Great. So we have seen two more possible errors at the function call level. Now let's suppose that everything went great at the first step. Everything went great at the second step. So you have found the right tool output. But now the model has trouble to synthesize the output into a meaningful response.

**中文**

而且，要确保在编写工具时利用这种含义。很好，我们又看到了函数调用层面另外两种可能的错误。现在假设第一步一切顺利，第二步也一切顺利，你得到了正确的工具输出。但现在，模型在将输出综合成一个有意义的回答时遇到了困难。

### [1:18:49](https://www.youtube.com/watch?v=8fNP4N46RRo&t=4729s) · b000150

**English**

Let's suppose your tool found a bear named Teddy. And then the other attributes, which I haven't shown here, maybe say that they are one mile away from me. So the teddy bear has been found, and we just have to present it to the user. But if you put it to the model, let's suppose the model says, I didn't find any bear. So what could be the cause here? So it could be the case that you have an output that has information that the model doesn't ground on.

**中文**

假设你的工具找到了一只名叫 Teddy 的熊。其他属性，我没有在这里展示，也许说明它距离我一英里。泰迪熊已经找到了，我们只需要把它展示给用户。但如果你把它交给模型，假设模型说：“我没有找到任何熊。”这里的原因可能是什么？可能是输出中包含的信息没有被模型用来进行 grounding。

### [1:19:21](https://www.youtube.com/watch?v=8fNP4N46RRo&t=4761s) · b000151

**English**

So it could be the case that just the model lacks the ability to refer to content that was put previously. So here I have the same vanilla suggestion of upgrading the model. So usually, that doesn't happen really anymore, but it used to in early iterations of LLMs. There is one that is actually one that happens fairly often.

**中文**

也可能只是模型缺乏引用先前放入的内容的能力。这里，我还是给出同样的常规建议：升级模型。通常，现在已经不太会发生这种情况了，但在 LLMs 的早期迭代中确实发生过。还有一种情况，实际上相当常见。

### [1:19:52](https://www.youtube.com/watch?v=8fNP4N46RRo&t=4792s) · b000152

**English**

So sometimes the tool back end returns not only an output but a lot of output. And it's too much for the model to properly parse what is important. So you have maybe the information of Teddy in there. But it's drowning under an ocean of other kinds of information that are not useful. So the model cannot distinguish what is helpful. And then the solution for that is to go back to your tool implementation and ensure that whatever you output is meaningful to be used to the model in the next stage.

**中文**

有时，工具后端不只是返回输出，而是返回大量输出。内容太多，模型无法正确解析哪些才是重要的。也许里面有 Teddy 的信息，但它淹没在其他无用信息的海洋中。因此，模型无法分辨什么是有帮助的。解决办法是回头检查工具实现，确保你输出的任何内容，对下一阶段的模型使用来说都是有意义的。

### [1:20:32](https://www.youtube.com/watch?v=8fNP4N46RRo&t=4832s) · b000153

**English**

And I think this goes--this overlaps with the third reason I put here. So let's say, your output is trimmed already. Then another possible explanation is maybe it's not being presented in a meaningful way. So this is why in Python, you have these classes where you can instantiate attributes so that the output is very meaningful. So let's say, for saying that you have found a bear, you could return an object called teddy bear with attribute's name, distance, and so on--this is very meaningful, as opposed to maybe raw information that it doesn't how to interpret.

**中文**

我认为，这与我在这里列出的第三个原因有重叠。假设你的输出已经精简过了，那么另一种可能的解释是，它的呈现方式也许没有意义。所以在 Python 中，你有这些类，可以实例化属性，使输出非常有意义。比如，要表示你找到了一只熊，你可以返回一个名为 teddy bear 的对象，带有 name、distance 等属性。这就很有意义，而不是返回它不知道该如何解读的原始信息。

### [1:21:16](https://www.youtube.com/watch?v=8fNP4N46RRo&t=4876s) · b000154

**English**

Awesome. So we have seen here seven different failure modes over all these categories. So these are not the only ones. I have just mentioned those that I see very often that I thought could be helpful, but you could definitely see other failure modes. Does this make sense?

**中文**

很好。我们在这些类别中总共看到了七种不同的失效模式。当然，不只有这些。我只是提到了那些我经常看到、认为可能会有帮助的情况，但你肯定也会遇到其他失效模式。这样讲明白吗？

### [1:21:40](https://www.youtube.com/watch?v=8fNP4N46RRo&t=4900s) · b000155

**English**

Do you have any questions?

**中文**

大家有什么问题吗？

### [1:21:45](https://www.youtube.com/watch?v=8fNP4N46RRo&t=4905s) · b000156

**English**

Great. So we can move on to summarizing what were the common trends in these failure modes. So oftentimes, we have talked about the modeling side, where sometimes improving the model's ability to reason and ground could be the solution.

**中文**

很好。接下来，我们可以总结这些失效模式中的共同趋势。我们经常谈到建模方面，有时提高模型的推理（reasoning）和依据对齐（grounding）能力可能就是解决办法。

### [1:22:11](https://www.youtube.com/watch?v=8fNP4N46RRo&t=4931s) · b000157

**English**

Another complaint that we have seen is the relevance of what we put in the context window. If we improve that relevance, maybe it gets better. And on the modeling side, one more aspect is maybe the tool route's modeling or the tool API modeling itself, either by SFT tuning or just prompting, or even just the API description itself, does the function make sense? Do the arguments make sense?

**中文**

我们看到的另一个问题，是放入上下文窗口（context window）的内容的相关性。如果提高相关性，也许效果会更好。在建模方面，还有一个方面可能是工具路由的建模，或者工具 API 本身的建模，无论通过 SFT 调优、提示（prompting），甚至只是 API 描述本身：函数是否合理？参数是否合理？

### [1:22:42](https://www.youtube.com/watch?v=8fNP4N46RRo&t=4962s) · b000158

**English**

Does the docstring make sense? So this is one kind. And the other kind is the tool itself, so maybe it just has a problem. So you need to fix it. And I just want to say that when you deal with tools and evaluations, you have a lot of possible errors. So one thing that will help you to navigate through this is to be very methodical into categorizing kinds of errors and then dealing with them in group.

**中文**

文档字符串（docstring）是否合理？这是一类。另一类则是工具本身，也许它就是有问题，需要修复。我想说的是，当你处理工具和评估时，可能会出现很多错误。能帮助你应对这些问题的一点，是非常有条理地对错误类型进行分类，然后按类别处理。

### [1:23:14](https://www.youtube.com/watch?v=8fNP4N46RRo&t=4994s) · b000159

**English**

So you see there are lots of errors. And every time that you deal with a given loss, it's maybe just an adventure to solve. So really, being very organized here is going to help you a lot.

**中文**

你可以看到，错误有很多。每次处理某个给定的损失（loss）时，解决它也许就像一次冒险。因此，在这里保持井井有条，真的会对你很有帮助。

### [1:23:30](https://www.youtube.com/watch?v=8fNP4N46RRo&t=5010s) · b000160

**English**

With that in mind, we can delve into the world of benchmarks. So we talked about evaluations. Now you might wonder, how can you evaluate a large language model. Let's say, you have trained everything. How can you compare it with respect to others? So we're going to see together a series of benchmark categories that today's benchmarks usually--where today's benchmark usually resides, so in one of these.

**中文**

带着这一点，我们可以进入基准测试（benchmarks）的世界。我们谈过评估。现在你可能会想，如何评估一个大语言模型？假设你已经完成了所有训练，该如何将它与其他模型比较？我们将一起看一系列 benchmark 类别，当今的 benchmarks 通常——当今的 benchmark 通常归属于其中某一类。

### [1:24:04](https://www.youtube.com/watch?v=8fNP4N46RRo&t=5044s) · b000161

**English**

And we're going to see examples for each of them. Does that sound good? Awesome. So we can start with a kind of benchmark that I called a knowledge-based benchmark, where we want to test if the model is able to restitute given facts.

**中文**

我们会看每一类的示例。这样可以吗？很好。我们先从一种我称为基于知识的基准测试（knowledge-based benchmark）开始，在这里，我们想测试模型能否复述给定的事实。

### [1:24:30](https://www.youtube.com/watch?v=8fNP4N46RRo&t=5070s) · b000162

**English**

These facts are typically spanning lots of domains, so it doesn't have to be super precise on a given domain. But it's spanning all the kinds of domains that your users may care about. And then prime example for this is MMLU that we're going to see very soon. But just before we do so, I want to say that this knowledge benchmark mostly, but not only, measures how well pretraining was done, how well the information in your large corpora of data was retained by the model in order to be helpful at inference time.

**中文**

这些事实通常涵盖很多领域，因此不一定要对某个特定领域特别精细，而是覆盖用户可能关心的各种领域。一个典型例子就是 MMLU，我们很快就会看到。但在此之前，我想说，这类知识 benchmark 主要衡量的——但不只衡量这一点——是预训练（pretraining）做得怎么样，也就是模型对大规模数据语料中的信息保留得怎么样，从而能在推理时（inference time）发挥作用。

### [1:25:12](https://www.youtube.com/watch?v=8fNP4N46RRo&t=5112s) · b000163

**English**

So MMLU stands for Massive Multitask Language Understanding. And this benchmark has almost 60 different tasks that are super diverse. So it's not just one specific topic is just a bunch of topics, like everyday life topics or very--for example, there is law or medicine, and everything that you can think about.

**中文**

MMLU 代表大规模多任务语言理解（Massive Multitask Language Understanding）。这个 benchmark 包含近 60 项非常多样的任务。它不只是某个特定主题，而是很多主题，比如日常生活主题，或者非常——例如法律、医学，以及你能想到的各种内容。

### [1:25:44](https://www.youtube.com/watch?v=8fNP4N46RRo&t=5144s) · b000164

**English**

And the benchmark is redacted in a way that can be easily measuring an LLMs performance and weighing that performance with respect to others. So it's not something that is free-form. It's something that is very constrained. There is a question, and then you have four possible answers. And you ask the LLM to choose one of them. So it's a bit like CME 295 exams.

**中文**

这个 benchmark 的编写方式，便于衡量 LLM 的表现，并将其与其他模型的表现进行比较。它不是自由形式（free-form）的，而是受到严格约束的：有一道问题，然后有四个可能的答案，你让 LLM 选择其中一个。有点像 CME 295 的考试。

### [1:26:17](https://www.youtube.com/watch?v=8fNP4N46RRo&t=5177s) · b000165

**English**

Part of the exam is also multiple choice questions. And it's a good way to standardize the knowledge evaluation. And it's the same that is used here.

**中文**

考试的一部分也是选择题。这是将知识评估标准化的一种好方法，这里使用的也是同样的方法。

### [1:26:31](https://www.youtube.com/watch?v=8fNP4N46RRo&t=5191s) · b000166

**English**

And this is also a trend that you see across benchmarks. You don't ask the model to just come up with some answer. And you have maybe an LLM-as-a-Judge just giving some opinion about it because doing so introduces another layer of potential errors. The LLM-as-a-Judge, as I've seen mentioned, isn't necessarily perfect. So this framing enables us to have a hard-coded way to extract the answer output by the LLM.

**中文**

这也是你在各类 benchmarks 中会看到的趋势。你不会只是让模型给出某个答案，然后也许让一个作为评判者的 LLM（LLM-as-a-Judge）对此发表意见，因为这样做会引入另一层潜在错误。正如我之前提到的，LLM-as-a-Judge 不一定完美。因此，这种设定使我们能够用硬编码（hard-coded）的方式提取 LLM 输出的答案。

### [1:27:07](https://www.youtube.com/watch?v=8fNP4N46RRo&t=5227s) · b000167

**English**

So typically, you would ask it to output the right letter at the end of each question, which you can then extract and then compare with respect to the answer. So giving some examples about what is in this benchmark, as I mentioned, you have all sorts of fields in there. And you will notice that each problem mostly requires some prior knowledge about that topic. So it's not purely logic that will help you solve it.

**中文**

通常，你会要求它在每道题最后输出正确的字母，然后提取这个字母，与标准答案比较。举几个这个 benchmark 中的例子，正如我提到的，里面有各种领域。你会注意到，每道题大多都需要一些有关该主题的先验知识（prior knowledge）。因此，单靠逻辑并不能帮助你解决它。

### [1:27:41](https://www.youtube.com/watch?v=8fNP4N46RRo&t=5261s) · b000168

**English**

And I think the last example in this slide is a good representation of it, where you have something in the domain of medicine, and you have a bunch of numbers, patient has this and that, what would you say-- where would you say is the damage. So it's typically something that you could see in medicine books, maybe. And the same goes with other fields, such as law, where everything has been codified somewhere, and you need the knowledge of that somewhere in order to answer the question.

**中文**

我认为这张幻灯片上的最后一个例子很好地体现了这一点：它来自医学领域，有一堆数字，患者有这个情况、那个情况，你会说——你认为损伤在哪里？这通常是你可能在医学书籍中看到的内容。其他领域也是如此，比如法律，所有内容都已经在某个地方编纂成文，你需要掌握那个地方的知识才能回答问题。

### [1:28:14](https://www.youtube.com/watch?v=8fNP4N46RRo&t=5294s) · b000169

**English**

So this is the first kind. And it's not the only kind of benchmark. So it's not the only benchmark in this category. You have other benchmarks that can be in these categories, but it's just one of them. A second category that you might see are those that are in the reasoning space. So typically, these are kinds of benchmarks that require some amount of thoughts before outputting an answer.

**中文**

这是第一类。当然，benchmark 不只有这一类，而这个类别中也不只有这一个 benchmark。还有其他 benchmarks 可以归入这些类别，它只是其中一个。你可能会看到的第二类，是推理领域的 benchmarks。通常，这类 benchmarks 要求在输出答案之前进行一定程度的思考。

### [1:28:47](https://www.youtube.com/watch?v=8fNP4N46RRo&t=5327s) · b000170

**English**

So it assesses the quality of the chain of thoughts, or if you are in the reasoning world, maybe the quality of your think tokens, but just more broadly, your ability to infer a response based on some reasoning. And then for that, I'm going to mention two examples, so one in the field of math and then one other in the field of so-called common sense reasoning that is anchored in everyday life, which is typically the field that might be of interest for your LLM users.

**中文**

所以，它评估的是思维链（chain of thoughts）的质量，或者，如果你处在推理模型领域，也许是思考 token（think tokens）的质量。更广义地说，就是你基于某种推理得出回答的能力。为此，我会提到两个例子：一个来自数学领域，另一个来自所谓的常识推理（common sense reasoning）领域，它以日常生活为基础，而这通常是你的 LLM 用户可能感兴趣的领域。

### [1:29:27](https://www.youtube.com/watch?v=8fNP4N46RRo&t=5367s) · b000171

**English**

And we're going to see that very soon. So first, let's take a look at the benchmark focused on math. So how many of you about AIME?

**中文**

我们很快就会看到。首先，我们来看看侧重数学的 benchmark。你们有多少人……AIME？

### [1:29:41](https://www.youtube.com/watch?v=8fNP4N46RRo&t=5381s) · b000172

**English**

So AIME is an exam that high school students sit for when they want to participate to the Olympiads. And typically, it's a very hard test. And it's covering math topics. And then it's in a format that is LLM-friendly because you have a given problem statement. And at the end, you ask the student to write the response into a three-digit number.

**中文**

AIME 是高中生想参加奥林匹克竞赛时参加的一项考试。通常，这是一项非常难的测试，涵盖数学主题。它的形式对 LLM 很友好，因为它会给出一道题目陈述，最后要求学生把答案写成一个三位数。

### [1:30:19](https://www.youtube.com/watch?v=8fNP4N46RRo&t=5419s) · b000173

**English**

So it's very well-constrained, which makes it a right fit to benchmark LLMs. And just like the one before, it's hard-coded. And I give here some samples of the AIME exam as seen this year. So as you see--I don't know if you can read from afar, but it's not super simple. You have some one sentence. So you think maybe it's easy, but you actually need to write down the reasoning before finding the answer.

**中文**

因此，它的约束非常明确，很适合用来对 LLMs 进行基准测试。和前一个一样，它也是硬编码的。这里我给出了一些今年 AIME 考试的样题。大家可以看到——不知道你们从远处能不能看清——它并不是特别简单。有的题目只有一句话，你可能觉得很容易，但实际上需要先把推理过程写下来，才能找到答案。

### [1:30:50](https://www.youtube.com/watch?v=8fNP4N46RRo&t=5450s) · b000174

**English**

And this is what we want to test the LLM for. And then the second kind of reasoning that we mentioned here was so-called common sense reasoning. And the one that is often used these days is PIQA, so Physical Interaction, Question Answering. So these are tasks that are deeply grounded into the physical real world. So we have some samples at the next slide that we'll show.

**中文**

这就是我们想测试 LLM 的能力。我们这里提到的第二种推理，是所谓的常识推理。如今经常使用的一个 benchmark 是 PIQA，也就是物理交互问答（Physical Interaction, Question Answering）。这些任务深深扎根于真实的物理世界。下一张幻灯片会展示一些样例。

### [1:31:22](https://www.youtube.com/watch?v=8fNP4N46RRo&t=5482s) · b000175

**English**

But it is still reasoning-based questions, but that will rely on your understanding on how things work around you, not necessarily math-based but just everyday life. And this time, it's not multiple choice questions over four answers, like the MMLU. It's over two only. And you have the 20,000 examples. And then here, a good example that I really liked from the samples mentioned in the paper was, how do I find something I lost on the carpet?

**中文**

这些仍然是基于推理的问题，但依赖你对周围事物如何运作的理解，不一定涉及数学，而是日常生活。这一次，它不像 MMLU 那样是四个答案的选择题，而是只有两个答案。它有 20,000 个例子。这里有一个我特别喜欢的例子，来自论文提到的样例：“我如何找到掉在地毯上丢失的东西？”

### [1:32:02](https://www.youtube.com/watch?v=8fNP4N46RRo&t=5522s) · b000176

**English**

So there is one solution that says, vacuum with a solid seal. And the other one is vacuum with a hairnet. And of course, when you vacuum with the solid seal, then the seal is, of course, solid, so no air can go through it. But if you have a hairnet, you will vacuum the whole thing. And the thing that you lost will be caught inside of it. So what I mentioned is common sense, but it might not be obvious. And this is what we tasked the model to resolve.

**中文**

一个解决方案说，用实心封口的吸尘器吸；另一个说，用套着发网的吸尘器吸。当然，如果用实心封口的吸尘器吸，封口是实心的，空气就无法通过。但如果有一个发网，你就可以把整个地方吸一遍，丢失的东西会被拦在里面。我提到的是常识，但可能并不显而易见。这就是我们要求模型解决的问题。

### [1:32:37](https://www.youtube.com/watch?v=8fNP4N46RRo&t=5557s) · b000177

**English**

So then one other major area for benchmarks is coding, where we want to probe the model for solving complex questions, encoding. And this has two main uses in real life. So one is aligned with the use case that I mentioned at the end of last lecture, the one I liked regarding AI assistant coding. So these models, they aim at being used in that setting as well.

**中文**

benchmarks 的另一个主要领域是编程（coding），我们想探查模型解决复杂问题、encoding \[字幕疑误，可能指 in coding\] 的能力。这在现实生活中有两种主要用途。一种与我在上节课最后提到的用例一致，就是我喜欢的 AI 辅助编程。这些模型也旨在用于那种场景。

### [1:33:10](https://www.youtube.com/watch?v=8fNP4N46RRo&t=5590s) · b000178

**English**

So you should make sure that these benchmarks perform--these benchmarks show that these LLMs perform well in order to be useful to your users. And then a second reason why benchmarking on coding makes sense is that you have all these tools that you might want to use in an agentic setting. And then these tools are written maybe in a Python format. So you want to ensure that your model has the right ability to read and write code so that it can execute this tool calls and then interpret what's coming out of them.

**中文**

所以，你应该确保这些 benchmarks 表现——这些 benchmarks 能表明这些 LLMs 表现良好，从而对用户有用。对编程进行基准测试有意义的第二个原因是，在智能体场景（agentic setting）中，你可能想使用各种工具，而这些工具也许是用 Python 编写的。因此，你要确保模型具备适当的代码读写能力，以便执行这些工具调用，然后解读它们返回的内容。

### [1:33:49](https://www.youtube.com/watch?v=8fNP4N46RRo&t=5629s) · b000179

**English**

So these are two, I would say, motivations that motivate us to find coding useful here, even to the folks that don't do coding at all.

**中文**

所以，我会说，这是两个让我们认为编程在这里有用的动机，即便对完全不编程的人来说也是如此。

### [1:34:06](https://www.youtube.com/watch?v=8fNP4N46RRo&t=5646s) · b000180

**English**

And then one example of such benchmark is SWE-bench. So SWE-bench is--I put a question mark here because they didn't define exactly what the acronym meant. But it's likely that it meant software engineering benchmarks. So SWE is oftentimes the acronym for software engineering. And what they did is that they looked at popular Python repositories, and they filtered down those that contained pull requests that were solving an issue and that introduced tests.

**中文**

这类 benchmark 的一个例子是 SWE-bench。SWE-bench 是——我在这里放了一个问号，因为他们没有确切定义这个缩写的含义。但它很可能指软件工程基准测试（software engineering benchmarks）。SWE 通常是 software engineering 的缩写。他们的做法是查看热门的 Python 代码仓库，然后筛选出其中包含解决某个 issue 并引入测试的拉取请求（pull requests）的仓库。

### [1:34:44](https://www.youtube.com/watch?v=8fNP4N46RRo&t=5684s) · b000181

**English**

So you have some before-after behavior that you can quantitatively assess with the tests that are introduced. And supposedly, if you have pull request that introduces some tests and some fix, you can fairly assume that these tests were not passing without the fix, and that they are passing after the fix. So the fact that we have these tests at-hand is a good measure for us to assess the quality of ethics.

**中文**

这样就有了修改前后的行为，可以用引入的测试进行定量评估。按理说，如果某个 pull request 引入了一些测试和某个修复，就可以合理假设，这些测试在没有修复时无法通过，而在修复之后能够通过。因此，手头有这些测试，对我们来说是评估 ethics \[字幕疑误，可能指 a fix，即修复\] 质量的一种好方式。

### [1:35:18](https://www.youtube.com/watch?v=8fNP4N46RRo&t=5718s) · b000182

**English**

So if you have heard of a test-driven development, it's all about having tests and ensuring they pass. And this is what it relies on.

**中文**

如果你听说过测试驱动开发（test-driven development），它的核心就是先有测试，并确保测试通过。这里依赖的就是这一点。

### [1:35:30](https://www.youtube.com/watch?v=8fNP4N46RRo&t=5730s) · b000183

**English**

And then here you ask these LLMs to solve these GitHub issues. And then you assess whether they indeed pass by looking at the test status before and after patching the answer suggested by the LLM.

**中文**

在这里，你让这些 LLMs 解决这些 GitHub issues，然后通过查看应用 LLM 建议的答案补丁前后的测试状态，评估它们是否确实通过。

### [1:35:52](https://www.youtube.com/watch?v=8fNP4N46RRo&t=5752s) · b000184

**English**

Great. So here is a very nice figure that the paper introducing that benchmark gives. So you're given a code base. And then what you ask the model for is a patch. That is just it. And then you patch whatever the model has provided to find the tests--to find the test status. And then one last area that I want to mention in the case of base benchmarks is safety.

**中文**

很好。这里有一张非常好的图，来自介绍这个 benchmark 的论文。你会得到一个代码库，然后要求模型提供一个补丁（patch），仅此而已。接着，将模型提供的内容作为补丁应用上去，查看测试——查看测试状态。关于基础 benchmarks，我最后想提到的一个领域是安全性（safety）。

### [1:36:25](https://www.youtube.com/watch?v=8fNP4N46RRo&t=5785s) · b000185

**English**

So when you see fancy LLMs coming out, you usually don't see in the advertisements of modeling benchmarks the safety part because usually, safety is a bit subjective with respect to the LLM provider. So every company has its own policy. So you cannot necessarily compare a performance on a given benchmark across models just because all these providers might not claim they want to perfectly solve that benchmark 100%.

**中文**

当你看到令人瞩目的 LLMs 发布时，通常不会在模型 benchmark 的宣传中看到安全性部分，因为安全性通常相对于 LLM 提供商而言有一定主观性。每家公司都有自己的政策。因此，你不一定能根据某个给定 benchmark 的表现来跨模型比较，因为这些提供商未必都声称自己想要 100% 完美地解决这个 benchmark。

### [1:37:00](https://www.youtube.com/watch?v=8fNP4N46RRo&t=5820s) · b000186

**English**

As a result, it's not necessarily a good measure of that field. So if you look at model cards, oftentimes, you see a safety section being mentioned in reports to say the work that they have done. But they don't necessarily compare models with respect to a given benchmark.

**中文**

因此，它不一定是衡量这个领域的好指标。如果你查看模型卡（model cards），经常会看到报告中提到安全性部分，用来说明他们做了哪些工作。但他们不一定会根据某个给定 benchmark 来比较模型。

### [1:37:22](https://www.youtube.com/watch?v=8fNP4N46RRo&t=5842s) · b000187

**English**

And usually, the safety benchmarks, they are fairly aligned with what we think should or should not happen. But on top of it, you might have additional policies that maybe just policies. So you have some human that had to make some decision. It might not be a universal decision, it's just a given decision. So the benchmark's goal is to be aligned with what kind of policy the LLM provider has in mind in order to be truly meaningful.

**中文**

通常，安全性 benchmarks 与我们认为应该或不应该发生的事情相当一致。但除此之外，你可能还有一些额外政策，而这些也许只是政策：某个人必须作出某个决定。它未必是普遍适用的决定，只是一个特定决定。因此，benchmark 的目标是与 LLM 提供商心中设想的政策类型保持一致，这样才真正有意义。

### [1:37:57](https://www.youtube.com/watch?v=8fNP4N46RRo&t=5877s) · b000188

**English**

This is why when you execute a safety benchmark, you should check the content of the benchmark in order to put a meaning behind it. So here let's talk about HarmBench, which I am supposing it means harmful behavior benchmark. So this benchmark has four categories, the so-called standard category that is categorizing quote, unquote, "vanilla" harmful behavior.

**中文**

这就是为什么运行安全性 benchmark 时，你应该检查它的内容，以理解其背后的意义。这里我们来谈 HarmBench，我猜它的意思是有害行为基准测试（harmful behavior benchmark）。这个 benchmark 有四个类别，其中所谓的标准类别（standard category）对加引号的“常规（vanilla）”有害行为进行分类。

### [1:38:30](https://www.youtube.com/watch?v=8fNP4N46RRo&t=5910s) · b000189

**English**

Then you have copyright category that is assessing the model's ability to generate copyrighted content, which we do not want. And then the two last ones, contextual and multimodal, both of them are contextual based on a given modality. So contextual is on the text modality. And then multimodal is with other modalities than text. So we're going to see an example at the next slide.

**中文**

然后是版权类别（copyright category），用于评估模型生成受版权保护内容的能力，而这是我们不希望出现的。最后两个类别是上下文（contextual）和多模态（multimodal），两者都是基于某个特定模态的上下文。contextual 针对文本模态，而 multimodal 针对文本以外的其他模态。下一张幻灯片会展示一个例子。

### [1:39:02](https://www.youtube.com/watch?v=8fNP4N46RRo&t=5942s) · b000190

**English**

And here you don't have the same ability to assess performance on this benchmark based on some hard-coded match because these harmful statements might be open-ended. And you cannot possibly just solve all of these by RegEx matching. For example, one example in the standard category of this benchmark tries to entice harmful behavior into executing something that is harmful.

**中文**

在这里，你无法同样依靠某种硬编码匹配来评估这个 benchmark 上的表现，因为这些有害陈述可能是开放式的。你不可能仅靠正则表达式（RegEx）匹配解决所有这些情况。例如，这个 benchmark 的 standard 类别中的一个例子，会试图诱导有害行为，让模型执行有害的事情。

### [1:39:37](https://www.youtube.com/watch?v=8fNP4N46RRo&t=5977s) · b000191

**English**

And the paper mentions--distinguishes something that is very interesting. So it distinguishes model quality with safety by saying that if the model tries to do the harmful behavior, even if it wasn't successful, because it was not of a good quality enough, then it's enough to count the attack as successful. And for that, they trained some classifier to recognize these cases.

**中文**

论文提到——区分了一个非常有意思的点。它将模型质量与安全性区分开来，指出：如果模型试图执行有害行为，即便因为质量不够好而没有成功，也足以将这次攻击计为成功。为此，他们训练了某个分类器（classifier）来识别这些情况。

### [1:40:09](https://www.youtube.com/watch?v=8fNP4N46RRo&t=6009s) · b000192

**English**

This is the only benchmark among those that I presented here that is done based on a classifier that can itself be prone to error compared to others that are very grounded in constrained set of values. And as promised, here is a few examples as mentioned in the paper. So here we test whether you can unlock a door that you shouldn't unlock. And then here the test is on influencing someone with respect to some election.

**中文**

这是我在这里介绍的 benchmarks 中，唯一一个基于 classifier 进行评估的 benchmark，而 classifier 本身也可能出错；其他 benchmarks 则有受约束的取值集合作为明确依据。按照之前说的，这里是论文中提到的几个例子。这里测试你是否能打开一扇不该打开的门。这里则测试针对某场选举影响某个人。

### [1:40:46](https://www.youtube.com/watch?v=8fNP4N46RRo&t=6046s) · b000193

**English**

These are not safe behaviors.

**中文**

这些都不是安全的行为。

### [1:40:52](https://www.youtube.com/watch?v=8fNP4N46RRo&t=6052s) · b000194

**English**

Great. So I mentioned everything so far that you could solve without tools. So of course, I say, you could. Some of them, you could use tools, of course, to solve them. But what about measuring the behavior of agents? So for here, you have an interesting benchmark called tau-bench, where tau is a Greek letter that actually, you can write it as tool agent users. And this is why we say tau.

**中文**

很好。到目前为止，我提到的这些都可以不借助工具解决。当然，我说的是“可以”，其中一些当然也可以使用工具来解决。那么，如何衡量智能体的行为呢？这里有一个有意思的 benchmark，叫作 tau-bench。tau 是一个希腊字母，实际上你可以把它写成 tool agent users，这就是我们称它为 tau 的原因。

### [1:41:23](https://www.youtube.com/watch?v=8fNP4N46RRo&t=6083s) · b000195

**English**

And it's a benchmark that provides across two different fields, so the airline and the retail field, a set of tools. And it gives a set of policies, things that the agent can and cannot do. And then what you do is that you have a set of tasks. So tasks are problem statements that you give a given user. And the goal is for the user to achieve that task through the agent.

**中文**

这个 benchmark 在两个不同领域，也就是航空和零售领域，提供一组工具。它还提供一组政策，规定智能体可以做什么、不可以做什么。接着，你会有一组任务。任务就是给某个用户的问题陈述，目标是让用户通过智能体完成这个任务。

### [1:41:59](https://www.youtube.com/watch?v=8fNP4N46RRo&t=6119s) · b000196

**English**

And the interesting thing about tau-bench is that tau-bench is language model-simulated. So the user interaction with the agent, as you can imagine, cannot be hard-coded because further terms will depend on previous ones. So let's say, you say something as a user and your agent decides to do something, then you need the context of what it has done in order to continue the conversation. And this is why you have this simulation aspect that the paper introduces that is typically done by a separate big model that plays the role of the user.

**中文**

tau-bench 有意思的地方在于，它是通过语言模型进行模拟的。可以想象，用户与智能体的交互无法硬编码，因为后续的 terms \[字幕疑误，可能指 turns，即对话轮次\] 会依赖之前的内容。比如，你作为用户说了某句话，智能体决定做某件事，那么要继续对话，就需要知道它做了什么的上下文。这就是论文引入模拟这一环节的原因，通常由一个单独的大模型扮演用户。

### [1:42:41](https://www.youtube.com/watch?v=8fNP4N46RRo&t=6161s) · b000197

**English**

And here we have an example of the task of changing a flight. So you have given tools. The agent tries to help the user to achieve that goal. And at the end of it, we assess whether it's successful in doing so by calculating a reward that's a function of the database change. So let's say, the user has changed their tickets, so we want to see if the database has indeed the state that we're looking for and/or a given action.

**中文**

这里有一个更改航班任务的例子。给定一些工具，智能体尝试帮助用户实现目标。最后，我们通过计算一个由数据库变化决定的奖励（reward），评估它是否成功完成任务。假设用户更改了机票，我们就想看看数据库是否确实处于我们期望的状态，和／或是否执行了某个给定动作。

### [1:43:17](https://www.youtube.com/watch?v=8fNP4N46RRo&t=6197s) · b000198

**English**

So maybe the action of canceling is one that is the goal of this task. So this is part of the reward. And the paper that introduces this benchmark talks about a concept that is a funny word play. With respect to the metric that we had talked about at the last lecture, we had introduced pass@k. And then this paper talks about pass hat k, which is the probability that all k attempts succeed.

**中文**

也许取消这个动作就是该任务的目标，这就构成 reward 的一部分。介绍这个 benchmark 的论文谈到了一个概念，是个有趣的文字游戏。相对于上节课谈过的指标，我们介绍过 pass@k，而这篇论文谈的是 pass hat k，也就是全部 k 次尝试都成功的概率。

### [1:43:58](https://www.youtube.com/watch?v=8fNP4N46RRo&t=6238s) · b000199

**English**

And then why is that relevant metric here? So as you have seen, the airline and retail domains were ones that were chosen here. And then an agent in the loop here could be a way to see if automating the agent side of things could help. And in order to truly know whether it can help, you want to have reliability and consistency in mind. So if you execute the task k times, you don't want pass@k, the probability that at least one of them succeeds.

**中文**

为什么这个指标在这里很相关？正如大家看到的，这里选择了航空和零售领域。让智能体参与其中，可以用来看看将智能体这一侧的工作自动化是否有帮助。为了真正知道它能否带来帮助，你需要考虑可靠性和一致性。如果你执行任务 k 次，你想要的不是 pass@k，也就是至少有一次成功的概率。

### [1:44:38](https://www.youtube.com/watch?v=8fNP4N46RRo&t=6278s) · b000200

**English**

You want the probability that all of them succeeds, which is why this metric matters. So if we had more time, I would have derived the formula to find pass hat k with respect to the parameters of the problem. But I will refer you to the derivation that Afshine has done last time. I just want you to be convinced that this is indeed the formula. So if you're not convinced, please feel free to do it at home.

**中文**

你想要的是全部成功的概率，这就是这个指标重要的原因。如果时间更充裕，我会根据问题的参数推导计算 pass hat k 的公式。不过，我会请大家参考 Afshine 上次做的推导。我只是希望大家相信，公式确实是这样。如果你还不信，欢迎回家自己推导一下。

### [1:45:12](https://www.youtube.com/watch?v=8fNP4N46RRo&t=6312s) · b000201

**English**

And moving on, we talked about all these benchmarks. Now let's see how they are grounded in reality. So by now, I think everyone of you has seen the new Gemini launch a few days ago. So this was the report that was sent to everyone to justify that the performance here was better. And you can see that what we introduced here is mentioned in some format.

**中文**

继续往下，我们谈了所有这些 benchmarks。现在来看看它们如何联系实际。到现在，我想大家都看过几天前发布的新 Gemini。这就是发给大家、用来证明其性能更好的报告。你可以看到，我们这里介绍过的内容，都以某种形式被提到了。

### [1:45:43](https://www.youtube.com/watch?v=8fNP4N46RRo&t=6343s) · b000202

**English**

So the reasoning part on AIME and PIQA is there. And you will see that some of these benchmarks are derived in a flavor that introduces multilinguality--multi-languages. So this is the case for PIQA. Instead of PIQA, it's global PIQA. And then for coding, it uses a flavor of SWE-bench. And tool use, it uses also a flavor of tau-bench, which is tau squared bench.

**中文**

其中有 AIME 和 PIQA 上的推理部分。你会看到，其中一些 benchmarks 衍生出了引入多语言性的版本——也就是多种语言。PIQA 就是这样：使用的不是 PIQA，而是 global PIQA。编程方面，它使用了 SWE-bench 的一种版本；工具使用方面，它也使用了 tau-bench 的一种版本，叫作 tau squared bench。

### [1:46:19](https://www.youtube.com/watch?v=8fNP4N46RRo&t=6379s) · b000203

**English**

And a few last words, here I just want to say that benchmarks are here to characterize the profile of your LLM. So it's not all good or all bad. Maybe some of your LLMs will have some strength and some weaknesses. And your personal experience might guide you to use one specific one with respect to others in given situations. So if I had to just give my personal experience, I know that the Sonnet models are very helpful for coding.

**中文**

最后再说几句。我想说，benchmarks 是用来刻画你的 LLM 的能力特征的，并不是全好或全坏。你的某些 LLMs 可能有一些长处，也有一些短处。你的个人经验可能会指引你在特定情境下，选择某个特定模型而不是其他模型。如果只说我的个人经验，我知道 Sonnet 模型对编程很有帮助。

### [1:46:56](https://www.youtube.com/watch?v=8fNP4N46RRo&t=6416s) · b000204

**English**

And whenever I want outputs that are fast and cheap, Gemini Flash is usually good. But these are not, by any means, global recommendations. Your own use case and your own experience can guide you into having a profile of models that suits your tasks best. And you can interestingly plot the performance of your models with respect to the other dimension that you care about, which is price, for example, and see for a given price, what is the best model you can use.

**中文**

当我想要快速又便宜的输出时，Gemini Flash 通常不错。但这些绝不是通用推荐。你自己的用例和经验，可以引导你形成最适合任务的模型能力画像。有意思的是，你还可以将模型表现与另一个你关心的维度，比如价格，绘制在一起，看看在某个给定价格下，能用到的最佳模型是什么。

### [1:47:32](https://www.youtube.com/watch?v=8fNP4N46RRo&t=6452s) · b000205

**English**

And then the border that you see on the best models for that specific metric is called the Pareto frontier. And you might have a Pareto frontier with respect to several aspects, so cost, safety, context length. And then a few words regarding data contamination, one thing about these benchmarks is that they are as good as the assumption of whether you have seen the actual benchmark results or not.

**中文**

你看到的、由在那个特定指标上表现最好的模型形成的边界，就叫作帕累托前沿（Pareto frontier）。你也可以针对多个方面得到 Pareto frontier，比如成本、安全性、上下文长度。接下来简单谈谈数据污染（data contamination）。关于这些 benchmarks，有一点是：它们是否可靠，取决于是否见过实际 benchmark 结果这一假设是否成立。

### [1:48:03](https://www.youtube.com/watch?v=8fNP4N46RRo&t=6483s) · b000206

**English**

So make sure you haven't seen them. And for that, people introduce hash values. In the case of tool use, they introduce a blocklist in order to not access websites that might contain the responses, or in the case of math, we have the luxury of evaluating on new tests that the model has for sure not seen. And Goodhart's law is a very good adage that says, when a measure becomes a target, it ceases to be a good measure.

**中文**

所以，要确保没有见过这些内容。为此，人们引入哈希值（hash values）。在工具使用的情况下，会引入屏蔽列表（blocklist），以避免访问可能包含答案的网站；而在数学领域，我们有条件使用模型肯定没见过的新试题进行评估。古德哈特定律（Goodhart's law）是一句很好的格言：当一个衡量指标变成目标时，它就不再是一个好的衡量指标。

### [1:48:38](https://www.youtube.com/watch?v=8fNP4N46RRo&t=6518s) · b000207

**English**

So all these benchmark results are to be weighed against what you're truly looking for. And then these benchmark results don't necessarily tell you whether a model is good for you or not.

**中文**

所以，所有这些 benchmark 结果，都要结合你真正想要的东西来权衡。这些 benchmark 结果不一定能告诉你，一个模型是否适合你。

### [1:48:53](https://www.youtube.com/watch?v=8fNP4N46RRo&t=6533s) · b000208

**English**

We had talked about ChatBotArena. In one of the previous lectures, it can be one way to balance the real-life performance of these. But I would say, ultimately, should be the one trying out these best models and see for yourself which one corresponds to your best. And with that, I hope you all have a great Thanksgiving. And thank you.

**中文**

我们在之前的一节课中谈过 ChatBotArena。它可以是权衡这些模型实际表现的一种方式。但我想说，最终应该由你亲自试用这些最好的模型，看看哪一个最适合你。最后，希望大家感恩节愉快。谢谢。
