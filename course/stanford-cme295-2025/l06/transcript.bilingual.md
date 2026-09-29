# Stanford CME295 Transformers &amp; LLMs \| Autumn 2025 \| Lecture 6 - LLM Reasoning

_Bilingual transcript · 双语讲稿_

- Channel: Stanford Online
- Source: [YouTube](https://www.youtube.com/watch?v=k5Fh-UgTuCo)
- Duration: 1:47:10
- Caption source: manual
- Status: complete
- Chinese translation: 184/184
- Translation provider: codex
- Generated: 2026-09-29T16:13:49+00:00

## Transcript · 讲稿

### [00:05](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=5s) · b000001

**English**

Hello, everyone. And again, welcome to lecture 6 of CME 295. So today is actually an exciting day because we're going to cover a topic that has been trending over the past year or so which is LLM reasoning. And it's actually a good segue compared to what we talked last time, which was preference tuning, because a lot of the methods that we used in lecture 5 are going to be the ones that we'll be using as the foundations for this lecture.

**中文**

大家好。再次欢迎来到 CME 295 第 6 讲。今天其实是令人兴奋的一天，因为我们要讨论一个过去一年左右一直很热门的话题，也就是大语言模型推理（LLM reasoning）。它也很好地承接了我们上次讨论的偏好调优（preference tuning），因为我们在第 5 讲中用到的许多方法，将成为本讲所使用的基础。

### [00:40](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=40s) · b000002

**English**

So before we start, as usual, we're going to just cover quickly what we saw in the last lecture. So if you remember, lecture 4 and lecture 5 were all about learning how we can train a model. So in lecture 4, we saw the first part, which was the pre-training part, which is the most compute-intensive step where we basically teach the model the structure of text, the structure of codes.

**中文**

开始之前，和往常一样，我们先快速回顾上一讲的内容。如果大家还记得，第 4 讲和第 5 讲都是在学习如何训练模型。在第 4 讲，我们讲了第一部分，也就是预训练（pre-training）。这是计算最密集的步骤，我们基本上是在教模型文本的结构、代码的结构。

### [01:16](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=76s) · b000003

**English**

And we do this very large, large scale training. So at the end of this first step, which is pre-training, we get a model that knows about code, that knows about language, but it only knows how to autocomplete a sequence. And so that's why we also saw the second step, which was the fine tuning step where we take our pre-trained model and we try to make it useful.

**中文**

我们进行这种非常大、大规模的训练。所以，在第一步，也就是预训练结束时，我们得到一个懂代码、懂语言的模型，但它只知道如何自动补全一个序列。因此，我们还讲了第二步，也就是微调（fine tuning）：拿到预训练模型，尝试让它变得有用。

### [01:46](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=106s) · b000004

**English**

So one use case that we saw was for instance, an assistant. So we tried to tune it in a way that it can respond to questions. And so here, we have this work of preparing the SFT data, which is what we call the SFT data, which is a high quality, curated data set that we can use to teach our model on how to behave. So at the end of this second step, we have our model that is tuned for a specific task, which can be responding to queries.

**中文**

例如，我们讲过的一种用例是助手。我们尝试对它进行调优，让它能够回答问题。这里就需要准备监督微调（supervised fine-tuning，SFT）数据，也就是我们所说的 SFT 数据。这是经过精心整理的高质量数据集，可以用来教模型如何表现。因此，在第二步结束时，我们得到的是针对某项特定任务调优过的模型，比如回答查询。

### [02:22](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=142s) · b000005

**English**

And then last lecture, we saw this third step, which was the preference tuning step. And here the goal is to align our model with human preferences. So we saw, in particular, RLHF, which was a common method to do that. And we saw that there was two steps to it. So there was the first part, learning to distinguish good from bad using human preference data, and then there was this second step, which was this RL stage, which is going to be useful today.

**中文**

然后在上一讲，我们讲了第三步，也就是 preference tuning。这里的目标是让模型与人类偏好对齐。具体来说，我们讲了基于人类反馈的强化学习（reinforcement learning from human feedback，RLHF），这是一种常用方法。我们看到它分为两步。第一部分是利用人类偏好数据学习区分好坏，然后第二步是强化学习（reinforcement learning，RL）阶段，这个阶段今天会派上用场。

### [03:05](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=185s) · b000006

**English**

So in particular, if you remember, we had drawn a comparison between the RL setup that you may be familiar with outside of this class, where we have an agent that is interacting with the environment and the way that it interacts with it, is that given a state that it is in, it can take an action following a policy, which is nothing else than just a probability distribution over actions.

**中文**

具体来说，如果大家还记得，我们做过一个对比，一边是大家可能在本课程之外熟悉的 RL 设置：有一个与环境交互的智能体（agent）。它的交互方式是，在所处的给定状态下，按照某个策略（policy）采取一个动作，而策略其实就是动作上的概率分布。

### [03:41](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=221s) · b000007

**English**

So given a state, our agent can take an action following this policy. And at the result of this, it receives some reward. And we saw last lecture that we have this nice comparison between the traditional RL setup and the LLM setup. And so here, our, quote unquote, agents is just simply the LLM. The environment that it interacts with is just a set of tokens that it can predict over.

**中文**

所以，在给定状态下，智能体可以按照这个策略采取动作，随后获得某种奖励（reward）。上一讲我们看到，传统 RL 设置与 LLM 设置之间可以做一个很好的对照。这里，我们所谓的“智能体”就是 LLM。它交互的环境，就是它可以在其上进行预测的一组词元（tokens）。

### [04:18](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=258s) · b000008

**English**

So given an input that it has received so far, it can predict what the next token could be, which is the action. And it does that using the probability distribution that is the result of, I guess, the LLM prediction. And we saw that we can obtain human preferences for each completion.

**中文**

因此，根据目前收到的输入，它可以预测下一个 token 可能是什么，这就是动作。它利用的概率分布，可以说就是 LLM 预测的结果。我们还看到，可以针对每个补全（completion）获得人类偏好。

### [04:49](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=289s) · b000009

**English**

So you have a prompt, you have a completion, and you get those human preferences. And this is the one that you then use in order to tune the LLM. Because here, this step is about aligning the model with human preferences. And here, the human preferences is encapsulated in the reward. And so we saw that the loss function during the RL stage is composed of two parts.

**中文**

也就是说，你有一个提示（prompt），有一个 completion，然后得到相应的人类偏好。接着，你就用这些偏好来调优 LLM。因为这里这一步的目的，就是让模型与人类偏好对齐。这里，人类偏好体现在奖励中。我们看到，RL 阶段的损失函数（loss function）由两部分组成。

### [05:21](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=321s) · b000010

**English**

So the first part is this advantage maximization. And we saw that that advantage was based on the rewards. And it has some baseline to just reduce the variance of the gradient. So we have that part. But we also saw another part, which was that we don't want our model to deviate too much from either the previous iteration--so we don't want the model to change too much from iteration to iteration--but we also don't want our model to change too much compared to our initial model, like our base model.

**中文**

第一部分是优势最大化（advantage maximization）。我们看到，这个优势（advantage）基于奖励，并带有一个基线（baseline），用于降低梯度的方差。这是一部分。但我们还讲了另一部分：我们不希望模型偏离上一次迭代太多，也就是说，不希望模型在相邻迭代之间变化太大；同时，我们也不希望模型相对于初始模型，比如基础模型（base model），变化太大。

### [06:06](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=366s) · b000011

**English**

And here, it's the SFT model. And the reason why we don't want to change too much is because our model has already learned a lot. It's already quite performant in what it does. And what we want is to just align it with human preferences, which is not something for which we want the model to change completely. And I think that was the part that I think was a little bit scary, which was the actual loss functions.

**中文**

在这里，它就是 SFT 模型。我们不希望变化太大的原因是，模型已经学到了很多东西，在它所做的事情上已经有相当不错的表现。我们只是想让它与人类偏好对齐，并不希望为此让模型发生彻底的改变。我想，那部分可能有一点吓人，也就是实际的损失函数。

### [06:37](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=397s) · b000012

**English**

So if you remember, the main algorithm that is typically used in the RLHF setting is PPO, which stands for proximal policy optimization. And there is this one variant that's called PPO CLIP, which is such that it clips the updates from one iteration to another. So here, if you remember, R is actually not the reward, it is the ratio.

**中文**

如果大家还记得，RLHF 设置中通常使用的主要算法是 PPO，全称是近端策略优化（proximal policy optimization）。它有一个变体叫 PPO CLIP，会对相邻迭代之间的更新进行裁剪（clip）。这里，如果大家还记得，R 实际上不是奖励，而是比值。

### [07:09](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=429s) · b000013

**English**

And it's a confusing notation. So it's the ratio between the current policy and the old policy. And the old policy here is the policy that is at the previous RL iteration. So what we do is that we have a clipping mechanism such that the ratio cannot go beyond some certain thresholds, such that we do not want to incentivize the model to make too big of an update.

**中文**

这个记号有些容易让人混淆。它是当前策略与旧策略之间的比值。这里的旧策略，就是上一次 RL 迭代时的策略。我们的做法是使用一种裁剪机制，使这个比值不能超出某些阈值，从而避免激励模型做出过大的更新。

### [07:44](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=464s) · b000014

**English**

And we saw another variant of PPO which is called PPO-KL penalty. And this variant uses the KL divergence to penalize the model from changing too much. So if you remember in the original PPO paper, we used the old, quote unquote, old version of the model, which is the one that the previous RL iteration.

**中文**

我们还讲了 PPO 的另一个变体，叫 PPO-KL penalty。这个变体使用 KL 散度（KL divergence）来惩罚模型过大的变化。如果大家还记得，在原始 PPO 论文中，我们使用的是所谓的“旧版”模型，也就是上一次 RL 迭代时的模型。

### [08:14](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=494s) · b000015

**English**

But in modern day RLHF training, this KL divergence is typically applied to the base model, which is the SFT model. So I guess long story short is we have these two PPO variants that were variants that were introduced in the original PPO paper. But in modern day RLHF training, we typically have some combination, some mix of these two loss functions.

**中文**

但在现在的 RLHF 训练中，这个 KL divergence 通常是相对于基础模型，也就是 SFT 模型来应用的。所以，简单来说，我们有这两个 PPO 变体，它们都是原始 PPO 论文中提出的。但在现在的 RLHF 训练中，我们通常会组合、混合使用这两个损失函数。

### [08:50](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=530s) · b000016

**English**

Cool? So up until now, we've seen what I want to call vanilla LLMs, which are LLMs that take something as an input, let's say a prompt, and just respond with some answer. And so those vanilla LLMs, they have a lot of strength that you can enjoy. So first of all, we had seen that those LLMs, they know a lot about structure, of the text, they know a lot about codes. So in particular, if you want to debug your code, I guess they are great to find where the error is.

**中文**

可以吗？到目前为止，我们看到的都是我想称为普通 LLM（vanilla LLMs）的模型：接收某个输入，比如一个 prompt，然后直接给出回答。这些 vanilla LLMs 有很多优点。首先，我们已经看到，这些 LLM 非常了解文本的结构，也非常了解代码。具体来说，如果你想调试代码，我想它们很擅长找出错误在哪里。

### [09:25](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=565s) · b000017

**English**

They are great to generate codes. They're also great to generate essays or poems. They're really, really good at that. But I do want to call out some weaknesses. So the first, I guess, weakness that I want to call out in this vanilla LLMs is that they have, quote unquote, limited reasoning. So typically, if you have some sophisticated, let's say, math problem, it will not really come up with, I guess, the solution because maybe it will get lost in the way because up until now, our model has been really trained to, I guess, given a prompt, respond to it using the next token prediction.

**中文**

它们很擅长生成代码，也很擅长生成文章或诗歌，在这些方面真的非常、非常出色。但我也想指出一些弱点。第一个我想指出的 vanilla LLMs 的弱点，是它们所谓的“推理能力有限”。通常，如果你给出一个复杂的，比如数学问题，它不一定能得出解答，因为它可能会在途中迷失。毕竟到目前为止，我们对模型的训练，主要是在给定 prompt 后，用下一词元预测（next token prediction）来回应。

### [10:18](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=618s) · b000018

**English**

So I guess here, there is not really a big reason why it would be able to solve complicated problems. So I guess that is one. So second weakness is that the LLM that we have has been pre-trained on a huge amount of data, which is static, meaning that the knowledge that the LLM has acquired is bound to the cutoff date, what we call the cutoff date, at which we cut and formed our pre-training data.

**中文**

所以，我想这里其实没有很充分的理由，能让它具备解决复杂问题的能力。这是一点。第二个弱点是，我们的 LLM 在大量数据上进行了预训练，而这些数据是静态的。这意味着，LLM 学到的知识受限于一个截止日期（cutoff date），也就是我们截取并形成预训练数据时的日期。

### [10:53](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=653s) · b000019

**English**

So I know a few days ago, we had an election. So if, let's say, we trained our LLM based on data before the election and let's say today, we ask it, who is the--I don't know-- elected official of let's say X, it will not be able to answer us because it does not have access to knowledge after that date. So a third weakness is so far, it's all talk, no action. So you just prompt your LLM.

**中文**

我知道几天前我们举行了一场选举。那么，假如我们的 LLM 是用选举之前的数据训练的，而今天我们问它，比如 X 的当选官员是谁，它就无法回答，因为它无法获取那个日期之后的知识。第三个弱点是，到目前为止，它只会说，不会做。你只是给 LLM 一个 prompt。

### [11:24](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=684s) · b000020

**English**

But I guess if you want to let's say, I don't know, place an order or don't do some action, you just kind of do it. And then I guess the last weakness, which by the way, is not an exhaustive list, is contrary to traditional NLP models LLMs, they generate free form texts. And it's hard to evaluate them in the framework that we--I mean, by we is the ML community has adopted up until a few years ago.

**中文**

但我想，如果你想，比如说，我不知道，下一个订单，或者不做某个动作，你就有点自己去做了。然后，最后一个弱点——顺便说一下，这并不是一份穷尽所有情况的列表——是，与传统的自然语言处理（natural language processing，NLP）模型相反，LLM 生成的是自由形式的文本。很难用我们——这里的“我们”指机器学习（machine learning，ML）社区——直到几年前一直采用的框架来评估它们。

### [11:59](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=719s) · b000021

**English**

So if you're familiar with it, let's suppose if you worked in the translation world, you would use rule-based metrics like BLEU or for summarization, ROUGE to evaluate your output. But then here, LLMs, they can really do more than just that. So it's very hard to evaluate them. So what I want to say is that this is, let's say, a subset of all the weaknesses that LLMs can have. And the last three are going to be topics that we'll cover in the next lecture and in the lecture 8.

**中文**

如果大家熟悉这方面，比如你做过翻译工作，就会使用 BLEU 这样的基于规则的指标；做摘要时，则用 ROUGE 来评估输出。但这里的 LLM 真正能做的远不止这些，因此很难评估。我想说的是，这只是 LLM 所有可能弱点中的一部分。最后三点，会是我们在下一讲和第 8 讲讨论的话题。

### [12:36](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=756s) · b000022

**English**

And as I mentioned before, the focus of today is reasoning. So we'll see how we can improve the way our LLM reasons. Cool. And again, this is a topic that's been very new. And by new, I mean roughly a year. So almost everything that we will see is either from 2024 or 2025. And I guess we're lucky because now we have enough hindsight to just know which piece is more important than other things.

**中文**

正如我之前提到的，今天的重点是推理。我们会看看如何改善 LLM 的推理方式。好。再强调一下，这是一个非常新的话题。我说的“新”，是指大约一年。因此，我们将看到的几乎所有内容，都来自 2024 年或 2025 年。我想我们很幸运，因为现在已经有足够的回顾视角，知道哪些部分比其他部分更重要。

### [13:13](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=793s) · b000023

**English**

And so the goal for today is going to be to know what reasoning models are. And the second big goal is to how they are trained. So hopefully, at the end of this lecture, if you have a good answer to these two questions, that means that we have done a good job. So let's start with reasoning models. What are they? Well, to answer this question, we first need to, I guess, define what reasoning is.

**中文**

今天的目标是了解什么是推理模型（reasoning models）。第二个主要目标，是了解它们如何训练。希望本讲结束时，如果你能很好地回答这两个问题，就说明我们做得不错。那就从推理模型开始。它们是什么？要回答这个问题，我们首先需要定义一下什么是推理。

### [13:47](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=827s) · b000024

**English**

And the bad news here is there's not a commonly agreed upon definition out there of what reasoning is. So I will try to define it, I guess, to the best of my ability. So here, we define reasoning as the ability to solve a problem. And here, by problem, we typically think more of math problems or, let's say, coding problems. But hopefully, these abilities can also spread to other fields as well.

**中文**

坏消息是，对于什么是推理，目前并没有一个普遍认可的定义。所以，我会尽我所能尝试定义它。这里，我们将推理定义为解决问题的能力。这里所说的问题，通常更多是指数学问题，或者编程问题。不过，希望这些能力也能扩展到其他领域。

### [14:24](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=864s) · b000025

**English**

And in order to solve this problem, we typically need a multi-step reasoning process, a little bit like when you take an exam, when you have a question that's not trivial, you typically break that down into several steps and then go through them, and then come to the final answer. So I guess the idea is problems that are reasoning problems, they would have some pattern of that.

**中文**

为了解决这个问题，我们通常需要一个多步骤的推理过程。这有点像考试时，遇到一个并不简单的问题，你通常会把它拆成几个步骤，逐步完成，最后得到答案。我想，所谓的推理问题，大致就会有这样的模式。

### [14:56](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=896s) · b000026

**English**

So to illustrate this, let's just make sure we're all kind of thinking the same. So a non-reasoning question would be something what is the course code of Stanford's transformers and LLM class. So this one, it's a knowledge thing. Everyone knows it's CME 295. But then as opposed to that, in contrast to that, a reasoning-based question would be maybe a math question. So for instance, let's suppose we have a bear that was born in 2020.

**中文**

为了说明这一点，我们先确保大家想的差不多。一个非推理问题可以是：Stanford 的 transformers 和 LLM 课程的课程代码是什么？这个问题属于知识问题。大家都知道是 CME 295。相对而言，一个基于推理的问题，可能是数学问题。例如，假设有一只熊出生于 2020 年。

### [15:27](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=927s) · b000027

**English**

How old is that bear now in 2025? So that would be the kind of question that we're looking at. Of course, this is super easy. You can think of something that's much harder than that, and this would qualify. Cool. So now that we a little bit what reasoning is, now we're going to look at how we can, I guess, obtain a model that can deal with these kinds of prompts.

**中文**

现在是 2025 年，这只熊多大了？这就是我们要研究的那类问题。当然，这个问题非常简单。你可以想一个比它难得多的问题，那也属于这一类。好。现在我们对什么是推理有了一点了解，接下来就看看如何获得一个能够处理这类 prompt 的模型。

### [15:59](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=959s) · b000028

**English**

So the core idea here is to leverage a concept we saw earlier in the class. So I'm not sure if you remember, but back in lecture maybe two or three, we saw a technique called chain of thought. So who remembers what chain of thought is? Yeah? Yes, do you want to say what that is?

**中文**

这里的核心想法，是利用我们在课程前面讲过的一个概念。不知道大家还记不记得，大概在第 2 讲或第 3 讲，我们讲过一种叫思维链（chain of thought）的技术。谁还记得 chain of thought 是什么？嗯？好，你愿意说说吗？

### [16:32](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=992s) · b000029

**English**

Yeah, exactly. So the answer is thinking in steps instead of just giving just a blanket answer. So great answer. So here, just to illustrate--yeah.

**中文**

对，完全正确。答案就是分步骤思考，而不是只给出一个笼统的答案。回答得很好。这里，为了说明一下——嗯。

### [16:58](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=1018s) · b000030

**English**

Oh, yeah. Great point. So the question is, for some questions, you need to have some element of context. So for instance, here, you need for your LLM to know that this year, I don't know, today is November 7, 2025. So yes great points. So there are two parts of that. For that specific question, so typically LLMs they have something that we call preamble. So something that tells you about some context.

**中文**

哦，对。很好的观点。问题是，有些问题需要一些上下文。例如在这里，你需要让 LLM 知道今年，我不知道，今天是 2025 年 11 月 7 日。对，说得很好。这涉及两部分。对于这个具体问题，LLM 通常有一种我们称为前导信息（preamble）的东西，用来提供一些上下文。

### [17:28](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=1048s) · b000031

**English**

And typically the date is something that we put in the preamble. So for this very specific case, the date would be information that would already be, I guess, available to the LLM. But for some other problems, you can very well have information or context that you do not have. And in lecture 7, we will see how we can fetch that. And it's definitely something that will be very useful. But for the sake of today, we will consider this more as being an extension of reasoning models as opposed to something that is foundational to how they work.

**中文**

日期通常就是我们放进 preamble 的信息。因此，在这个非常具体的例子里，日期是 LLM 已经可以获取的信息。但对于其他一些问题，确实可能存在你没有的信息或上下文。在第 7 讲，我们会看看如何获取这些信息。这肯定会非常有用。不过就今天而言，我们会更多地把它看作推理模型的一种扩展，而不是其工作原理的基础。

### [18:09](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=1089s) · b000032

**English**

But we'll respond to this part, I guess, next lecture. Cool. And so here, we are about to illustrate what a chain of thought looked like. And so here, instead of having, as you mentioned, just a blanket answer, what we want is to explain also the reasoning. So the way chain of thought did that was by having some in-context learning examples that explicitly the reasoning to encourage the model to also do that before providing the answer.

**中文**

这一部分，我们下一讲会回答。好。这里我们正要说明 chain of thought 是什么样的。正如你刚才提到的，我们不想只有一个笼统的答案，还想解释推理过程。chain of thought 的做法，是提供一些上下文学习（in-context learning）示例，在示例中明确呈现推理，以鼓励模型在给出答案之前也这样做。

### [18:49](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=1129s) · b000033

**English**

So that's the rough--it's not the rough idea. It's the idea behind chain of thought. And here, what we want to do is to do that, but at a much larger scale. So I just want to build an intuition as to why this may help us. So LLMs, they are basically trained with this next token prediction objective.

**中文**

这就是大致——不是大致想法，而是 chain of thought 背后的想法。这里，我们想做同样的事，但规模要大得多。我想先建立一个直觉，说明为什么这可能有帮助。LLM 基本上是以 next token prediction 为目标来训练的。

### [19:20](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=1160s) · b000034

**English**

And so the way they respond to questions that we ask is typically to sound plausible in a way to maximize or optimize for the probability of the tokens that you want to generate to happen. So if you have a very hard problem that you're presenting to the LLM, there are very few chances that that problem appeared in the training sets. And so here, the idea is to have the LLM decompose the problem into tractable ones, and then rely on the patterns that it has seen during training to solve all these more tractable problems.

**中文**

因此，它们回答我们提出的问题时，通常会让回答听起来合理，以最大化或优化所要生成的 tokens 出现的概率。如果你向 LLM 提出一个非常难的问题，这个问题出现在训练集中的可能性很小。所以，这里的想法是让 LLM 把问题拆解成可处理的问题，然后依靠训练期间见过的模式，解决所有这些更容易处理的问题。

### [20:06](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=1206s) · b000035

**English**

And it's a little bit like you or when we were students. When we give you a problem, you try to link it back to something that you know, that you have seen at training time, like during your studying, to solve them in order to find the answer. So I guess that's the intuition. I guess another reason that you can think of is when you let the LLM generate more tokens, you're just giving it more compute, if you think about it, because at each generation step, you have this whole forward pass.

**中文**

这有点像你们，或者我们当学生的时候。给你一个问题，你会尝试把它与自己知道的、在训练时见过的东西联系起来，比如学习时见过的内容，借此解决问题并找到答案。我想这就是直觉。另一个可以想到的原因是，仔细想想，当你让 LLM 生成更多 tokens 时，其实就是给它更多计算量，因为每一步生成都有一次完整的前向传播（forward pass）。

### [20:47](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=1247s) · b000036

**English**

And when you do that more, you just give it more compute. And we will see there is a term that is dubbed compute budgets, which is, I guess, the budget that you want your LLM to have to generate your response that we will see later on. But yeah, so that also plays a role. So is everyone clear on the overall idea of what a reasoning model is? Yeah?

**中文**

你让它多做几次，就是给它更多计算量。我们还会看到一个叫计算预算（compute budgets）的术语，我想它就是你希望 LLM 在生成回答时拥有的预算，后面会讲到。对，这也有作用。大家对推理模型的整体想法都清楚了吗？嗯？

### [21:19](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=1279s) · b000037

**English**

Perfect. So just to make sure, again, that we're all clear on this, so up until now we had, quote unquote, Vanilla LLMs that had some question as inputs, and they were responding with something as output. And in our case, what we want is given a question as input, we don't want to directly generate an answer. We first want to think.

**中文**

很好。再次确认一下，确保大家都理解：到目前为止，我们所谓的 Vanilla LLMs 以问题为输入，再给出某个输出。而在这里，我们想要的是，给定一个问题作为输入后，不要直接生成答案，而是先思考。

### [21:53](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=1313s) · b000038

**English**

And here, I guess we think by first outputting a reasoning chain. And then we provide the answer. So here, the LLM output is not just the answer. It's the reasoning plus the answer. And I guess here, I was saying that this topic has been very hot and trendy for the past year.

**中文**

这里，可以说我们是通过先输出一条推理链（reasoning chain）来思考，然后再给出答案。因此，LLM 的输出不只是答案，而是推理加答案。正如我刚才说的，这个话题在过去一年非常热门。

### [22:24](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=1344s) · b000039

**English**

So this is a little bit of a preview of the timeline of reasoning models. So reasoning itself is a topic that has been studied for more than a year, but reasoning models have started popping out starting from OpenAI's release of 01 preview. And this one was September of 2024. And then after that, you basically have everyone just wondering how OpenAI did it.

**中文**

这里简单预览一下推理模型的发展时间线。推理本身已经被研究了不止一年，但推理模型开始涌现，是从 OpenAI 发布 01 preview \[字幕疑误，可能指 o1-preview\] 开始的。那是在 2024 年 9 月。此后，基本上所有人都在琢磨 OpenAI 是怎么做到的。

### [22:56](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=1376s) · b000040

**English**

And so you had all of these AI labs trying to see what we can do to, I guess, increase the reasoning abilities of the model. So you would have everyone working on this. And then you had Google's Gemini 2.0 flash thinking that was, I think, released in December. And then starting in 2025, there was this DeepSeek R1 paper that was published in January, which made a lot of noise because what they were able to do was to match OpenAI's reasoning ability performance with a method that they were actually describing in their paper.

**中文**

于是，各家 AI 实验室都在尝试探索，能做些什么来提高模型的推理能力。大家都在研究这个。接着，Google 推出了 Gemini 2.0 flash thinking，我记得是在 12 月发布的。到了 2025 年，DeepSeek R1 论文在 1 月发表，引起了很大轰动，因为他们用一种在论文中实际描述出来的方法，达到了与 OpenAI 相当的推理能力表现。

### [23:44](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=1424s) · b000041

**English**

So that was a big moment, January 2025. And then after that, all of these other models also had reasoning abilities added. So you had some models from xAI, from Anthropic with Claudes, and then from other labs as well, also from Mistral. So this timeline is not exhaustive, but it's just to show you, I guess, how recent these models are. And I guess one thing to have in mind is it basically started at the end of 2024.

**中文**

所以，2025 年 1 月是一个重要时刻。此后，其他这些模型也都加入了推理能力。比如 xAI 的一些模型、Anthropic 的 Claudes，以及其他实验室的模型，也包括 Mistral。这条时间线并不完整，只是想让大家看看这些模型有多新。有一点要记住：它基本上始于 2024 年底。

### [24:22](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=1462s) · b000042

**English**

Cool. So I know a lot of you, if not all of you, are using LLMs every day as chat bots like, let's say, ChatGPT or Gemini. And so I want you to know, when the model that you're interacting with is a reasoning model--so I have a question for you. I was having a discussion with ChatGPT the other day. And I was wondering, is this using a reasoning model.

**中文**

好。我知道你们很多人，如果不是所有人，每天都在把 LLM 当聊天机器人使用，比如 ChatGPT 或 Gemini。我想让大家知道，什么时候与你交互的模型是推理模型。所以，我有个问题。前几天我在和 ChatGPT 聊天，我在想：这里用的是推理模型吗？

### [24:52](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=1492s) · b000043

**English**

So what do you think? If you stare at this screenshot. Yeah? Why? Right, exactly. So the key word here is thinking. Actually, they put it everywhere. But when these UIs show you the thinking process, so what they do is actually--so they don't show you actually the full reasoning process. And we're going to see why. But they tell you that they spend time thinking.

**中文**

大家怎么看？看着这张截图。嗯？为什么？对，完全正确。这里的关键词是“thinking”。事实上，他们到处都放了这个词。但当这些用户界面（user interfaces，UIs）向你展示思考过程时，他们实际上——并不会展示完整的推理过程。我们后面会讲为什么。不过，他们会告诉你，模型花了时间思考。

### [25:26](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=1526s) · b000044

**English**

And that time thinking is actually the time that is needed to produce the reasoning chain. That can be, I guess, more or less something that takes time. And so for instance, for ChatGPT, you have this thinking that you can also change from standard to extended, et cetera. And you have this for other models as well. And in particular, the, quote unquote, thought summary that you see is not the raw reasoning chain.

**中文**

这个思考时间，实际上就是生成推理链所需的时间。我想，这可能或多或少会花一些时间。比如在 ChatGPT 里，有这个 thinking 选项，还可以从 standard 改成 extended，等等。其他模型也有类似选项。特别要注意，你看到的所谓“思考摘要”（thought summary）并不是原始推理链。

### [25:59](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=1559s) · b000045

**English**

It's a summary of it. And the reason why they do that--I mean, I'm hypothesizing-- is one, because the raw chain may not be something that is fully intelligible from a human standpoint. Second is because maybe you as a user, you don't want to read the pages and pages. And then third, this is going to be what we see. But if you have the reasoning chains, you can maybe train a model that is trained on these chains so it can basically mimic those abilities as well.

**中文**

它是推理链的摘要。他们这样做的原因——我是说，这只是我的推测——第一，原始推理链从人类角度看，可能并不完全容易理解。第二，作为用户，你可能不想读一页又一页的内容。第三，这也是我们后面会讲的，如果你获得了这些推理链，或许就能用它们训练一个模型，让它也基本上模仿这些能力。

### [26:40](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=1600s) · b000046

**English**

So this may be the reasons why you would typically not see the raw chain. And when it comes to pricing, so we saw that the output of reasoning models are not only the answer, but also the reasoning itself. And so you will see in, I guess, all of these APIs that you're actually getting charged for it. So you're not necessarily getting all the reasoning chain. But if you look at the docs, there's always, I guess, a sentence or two, I guess, that specifies that you're actually being charged for output tokens.

**中文**

所以，这些可能就是通常不展示原始推理链的原因。说到定价，我们已经看到，推理模型的输出不仅是答案，还包括推理本身。因此，你会看到，所有这些应用程序编程接口（application programming interfaces，APIs）实际上也会对此收费。你不一定能拿到完整推理链，但如果查看文档，总会有一两句话说明，实际上会按输出 tokens 向你收费。

### [27:18](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=1638s) · b000047

**English**

And those output tokens, they also include reasoning tokens. So I think that's also a good thing to know. And I guess from a user standpoint, this also gives an incentive to have the maximum reasoning ability for a minimum amount of reasoning token because you don't want to pay a lot. So we're going to see later on how we can deal with that.

**中文**

这些输出 tokens 也包含推理词元（reasoning tokens）。我觉得这一点也值得了解。从用户的角度看，这也会促使我们希望用最少的 reasoning tokens 获得最强的推理能力，因为你不想花太多钱。后面我们会看看如何处理这个问题。

### [27:51](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=1671s) · b000048

**English**

But this is just one thing that's good to note. Cool. So we talked about what reasoning was, or at least a tentative definition. We saw, I guess, the core idea behind reasoning models. So now we're going to talk about some of the benchmarks that people use to quantify reasoning abilities. So the first one, as I previously mentioned, is about assessing the coding abilities. And so here, the goal is typically to solve a coding problem or to fix a bug.

**中文**

这只是一个值得注意的点。好。我们讨论了什么是推理，至少给出了一个尝试性的定义，也看到了推理模型背后的核心想法。现在，我们要讨论人们用来量化推理能力的一些基准（benchmarks）。正如我之前提到的，第一个方面是评估编程能力。这里的目标通常是解决编程问题，或者修复一个 bug。

### [28:27](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=1707s) · b000049

**English**

So you typically have the following setup. So given a problem, you want to produce a solution that is able to pass test cases. So if you have a solution that passes all test cases, then you have a solution that works. And this is our way of verifying that a response that was generated is actually a correct one.

**中文**

通常的设置如下：给定一个问题，你想生成一个能够通过测试用例（test cases）的解法。如果一个解法通过了所有测试用例，那么它就是一个能用的解法。这就是我们验证生成的回答是否正确的方式。

### [29:01](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=1741s) · b000050

**English**

So that's for coding. So just giving you an overview of the kinds of benchmarks that are out there. So we have HumanEval, which is the screenshot screenshots here, which I believe is a set of 100 something coding problems that were human written, which is why it's called the HumanEval. But you have then CodeForces, which is coming from a website of competitive programming that some of you may know. And there is also SWE-bench, which is, I believe, a set of problems that were derived from GitHub issues.

**中文**

这是编程方面。简单介绍一下有哪些基准。我们有 HumanEval，就是这里的截图、这些截图。我记得它包含 100 多道由人类编写的编程题，这也是它叫 HumanEval 的原因。还有 CodeForces，它来自一个竞技编程网站，你们有些人可能知道。另外还有 SWE-bench，我记得它是一组从 GitHub issues 中提取出来的问题。

### [29:38](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=1778s) · b000051

**English**

So these are real practical problems. So you will see that these reasoning models in the reports, they typically have results along these benchmarks. So this is for coding. Now for math, the goal is to solve a problem. And the way it works here is given a problem, you want the answer. And of course, you're letting your model, generate some reasoning.

**中文**

所以，这些都是真实的实际问题。你会看到，这些推理模型的报告中，通常会给出在这些基准上的结果。这是编程方面。对于数学，目标是解决一个问题。这里的做法是，给定问题，你想得到答案。当然，你会让模型生成一些推理。

### [30:12](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=1812s) · b000052

**English**

And so here, what you would do to verify that your solution works is by parsing the answer like so and then comparing it with some ground truth. So here, we can really know if the answer that your model is producing is true by comparing the two. So you will ask me OK, how do you parse that. So you can force your model-- and by force, I mean in the prompt--to output the answer in a way that can be parsable.

**中文**

这里，验证解法是否正确的方法，是像这样解析出答案，然后与某个标准答案（ground truth）比较。通过比较两者，我们确实可以知道模型给出的答案是否正确。你可能会问，好，那怎么解析呢？你可以强制模型——这里的“强制”是指在 prompt 中要求——以一种可解析的方式输出答案。

### [30:49](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=1849s) · b000053

**English**

Sometimes people, they just put it in some box in the box brackets. So there's a number of different ways to do that. And this is how the problems look like. So you have some problem. And then you can let your model generate some reasoning chain along with the answer. And then you have the answer here that you can compare to. So I just want to add that the kinds of benchmarks that are out there are based typically on problems that are actually not that trivial.

**中文**

有时，人们会把答案放在某个框里，放在方框括号中。有很多不同的做法。题目大致就是这样：你有一道题，然后可以让模型生成一条推理链和答案。这里还有一个答案，可供比较。我还想补充，现有这些基准中的题目，通常实际上并不那么简单。

### [31:25](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=1885s) · b000054

**English**

So a name that you will see a lot is aim. So I'm not sure if you're familiar with it. It's a math exam to qualify for the US math olympiads. So there is a bunch of models that I guess quantify their performance based on that. There's also GSM 8-K, which is a grade school kind of math problem. And I guess now your question maybe, OK, it's great we have all these benchmarks, but what is the metric that you will use to quantify that what you're doing is good or not.

**中文**

你会经常看到一个名字，aim \[字幕疑误，可能指 AIME\]。不知道大家是否熟悉，它是一项用于取得美国数学奥林匹克竞赛资格的数学考试。有不少模型会基于它来量化自身表现。还有 GSM 8-K \[字幕疑误，可能指 GSM8K\]，是一类小学水平的数学问题。我想你现在可能会问，好，我们有了这些基准，这很好，但要用什么指标量化我们做得好不好呢？

### [32:09](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=1929s) · b000055

**English**

And so there is one metric that you will see a lot. And we're going to see that right now because it's not that obvious. So that metric is called pass@k. So pass@k is, by definition, a metric that tries to estimate the probability that at least one of k attempts succeeds. So here, what we're saying is let's suppose we're, I don't know, having some coding problem.

**中文**

有一个指标你会经常看到，我们现在就来讲，因为它并不那么直观。这个指标叫 pass@k。按照定义，pass@k 试图估计 k 次尝试中至少一次成功的概率。也就是说，假设我们有一道编程题。

### [32:45](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=1965s) · b000056

**English**

We tell our model to generate k answers. And pass@k is the probability that at least one of these k answers passes the tests. Does that make sense? So by the way, why would you have pass@k? Why would that make sense? So it's not super trivial. So you may have used cases where you can afford to spend more time to generate more answers.

**中文**

我们让模型生成 k 个答案。pass@k 就是这 k 个答案中至少有一个通过测试的概率。这样讲明白吗？顺便问一下，为什么要有 pass@k？它为什么有意义？这并不是特别显而易见。你可能会遇到一些用例，能够接受花更多时间生成更多答案。

### [33:26](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=2006s) · b000057

**English**

If you know that you will get more chances to get it right, then you can spend more time to generate more answers so that you can have the right one. So in a problem like coding, the good thing is you can check whether your answer is correct or not. And so here, the idea is if you are in cases where you can afford to generate not just one answer, but multiple answers, then it may be worth it to just spend more time, spend more compute to generate more answers if it means that the probability of getting it right in one of them is going to be higher.

**中文**

如果你知道这样会增加答对的机会，就可以花更多时间生成更多答案，以得到正确答案。编程这类问题的好处是，你可以检查答案是否正确。因此，这里的想法是，如果某些场景允许你不只生成一个答案，而是生成多个答案，那么多花一点时间、多花一些计算量来生成更多答案，可能是值得的，只要这样能提高其中某个答案正确的概率。

### [34:06](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=2046s) · b000058

**English**

There is one technique that we saw last lecture that is kind of familiar with this. Best of n. Do you remember? Yeah, roughly. So best of n is this method that we saw last week, which was you generate n answers. And you use your reward model to score everything. And you take the best of all of them. So here, you can think of it as being the same, just that we do not have a reward model, we have a deterministic, verifiable way of checking whether something is correct.

**中文**

我们上一讲讲过一种与此有些相似的技术，Best of n。大家还记得吗？嗯，大概记得。Best of n 是我们上周讲的方法：生成 n 个答案，用奖励模型（reward model）给所有答案打分，然后选出最好的一个。这里可以把它看成同样的做法，只不过我们没有 reward model，而是有一种确定性的、可验证的方法来检查答案是否正确。

### [34:47](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=2087s) · b000059

**English**

So it's very similar to that. And so now we're going to spend just a few minutes just aligning our understanding on how we can estimate such a quantity. Yeah.

**中文**

所以，两者非常相似。接下来我们花几分钟，统一一下对如何估计这个量的理解。嗯。

### [35:07](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=2107s) · b000060

**English**

That's a great question. So the question is, do you choose a particular temperature. So I have a slide on that. So I'll just hold your question for a few slides. Cool. By the way, if there is any other questions, happy to--is there any other questions on this? Everyone is super clear? OK, cool. So what we want to do here is to estimate this probability. But you may tell me, just generate k attempts and just count the number of the attempts that are correct to estimate that.

**中文**

这是个很好的问题。问题是，要不要选择一个特定的温度（temperature）。我有一页幻灯片会讲这个，所以先把你的问题留到几页之后。好。顺便说，如果还有其他问题，我很乐意——关于这个还有其他问题吗？大家都非常清楚了吗？好。我们这里想做的是估计这个概率。但你可能会说，直接生成 k 次尝试，再数一数其中正确的尝试有多少，不就可以估计了吗？

### [35:47](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=2147s) · b000061

**English**

But the problem is if you only do this k times, your estimate can be very noisy because by pure chance, I don't know, you may have one instance that has 3 correct out of 5 and the other one 1. So you want to have an estimate that doesn't have that much variance. So what you do is you typically generate not k, but n answers. And out of these n answers you're going to have c of them that are going to be successful, and then n minus c that are not going to be successful.

**中文**

但问题是，如果只做 k 次，估计的噪声可能很大，因为纯粹出于偶然，可能一个实例中 5 次有 3 次正确，另一个只有 1 次。所以，你希望估计的方差不要那么大。通常的做法是，不生成 k 个，而是生成 n 个答案。这 n 个答案里，会有 c 个成功，n 减 c 个不成功。

### [36:29](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=2189s) · b000062

**English**

And the question here that you ask yourself is out of these n attempts, you want to quantify the probability of having at least one out of k attempts that is right. So the question here, if you have those n observations, if you were to select, let's say k, what is the probability of having at least one of those k passing?

**中文**

这里要问的问题是，在这 n 次尝试中，你想量化 k 次尝试中至少一次正确的概率。也就是说，如果你有这 n 个观测结果，从中选出，比如 k 个，这 k 个中至少有一个通过的概率是多少？

### [37:03](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=2223s) · b000063

**English**

That's the question. So we're short on time. I'm going to actually derive that right now. And the reason why I want to do that is because the answer is not necessarily trivial. And I don't want you to be too surprised of how it looks like without knowing where it comes from. So we're going to derive that. So we want to derive the probability that at least one attempt out of k that we select out of these n samples is correct.

**中文**

这就是问题。时间有点紧，我现在直接推导一下。我想这么做，是因为这个答案不一定显而易见。我不希望大家在不知道它从何而来的情况下，对它的形式感到太意外。所以我们来推导。我们想推导的是，从这 n 个样本中选出的 k 次尝试中，至少有一次正确的概率。

### [37:43](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=2263s) · b000064

**English**

So in order to do that, I'm just going to write that down. So pass that k. So we want the estimate for that. So it's going to be the probability that at least one attempts out of k is correct.

**中文**

为此，我先把它写下来。pass that k \[字幕疑误，可能指 pass@k\]。我们想求它的估计值。它就是 k 次尝试中至少有一次正确的概率。

### [38:14](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=2294s) · b000065

**English**

So if you've done some probability, there is a very common trick, which is if you have a probability of at least one, it's 1 minus the probability of having all of them being incorrect. Do you all know that trick? Because we're going to use that trick. So it's going to be 1 minus the probability of having all k attempts incorrect.

**中文**

如果你学过概率，有一个很常见的技巧：如果要求至少有一次的概率，可以用 1 减去全部不正确的概率。大家都知道这个技巧吗？我们会用到它。所以，就是 1 减去 k 次尝试全部不正确的概率。

### [38:53](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=2333s) · b000066

**English**

So far so good? Yeah? So now we're going to try to quantify this probability. So what is the probability of you finding an unsuccessful attempt among these n you have n minus C unsuccessful. You have n observations is going to be n minus C over n.

**中文**

到这里都没问题吧？嗯？现在我们来尝试量化这个概率。在这 n 次尝试中找到一次不成功的尝试，概率是多少？你有 n 减 C 次不成功的尝试，总共有 n 个观测结果，所以就是 n 减 C 除以 n。

### [39:29](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=2369s) · b000067

**English**

So it's your first it's your first unsuccessful attempt. So now what is the probability that you have another unsuccessful attempts knowing this one? So you have n minus c minus 1 other unsuccessful attempts over n minus 1 because you already took one.

**中文**

这是第一次，这是第一次不成功的尝试。那么，在已知这一次的情况下，再得到一次不成功尝试的概率是多少？还有 n 减 c 减 1 次不成功的尝试，除以 n 减 1，因为你已经取走了一次。

### [40:01](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=2401s) · b000068

**English**

And you continue that k times n minus c minus k plus 1 over n minus k plus 1. Does everyone agree with me? So here, we are quantifying the probability that if we take k samples randomly among this n, that all k1's are incorrect.

**中文**

继续这样做 k 次，n 减 c 减 k 加 1，除以 n 减 k 加 1。大家都同意吗？这里，我们量化的是：如果从这 n 个中随机取 k 个样本，所有 k1's \[字幕疑误，可能指 k 个样本\] 都不正确的概率。

### [40:36](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=2436s) · b000069

**English**

So here, we compute this by computing the probability that the first attempt is incorrect. And then the second one is incorrect, knowing that the first one was incorrect, and so on, which we have for which we have this formula. So if you saw that in probability class, it's basically the same as sampling without replacement.

**中文**

这里的计算方式，是先计算第一次尝试不正确的概率，再计算已知第一次不正确时第二次也不正确的概率，依此类推，于是就有了这个公式。如果你在概率课上见过，这基本上就是无放回抽样（sampling without replacement）。

### [41:06](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=2466s) · b000070

**English**

And now the nice thing with this is that you can express that with a nice mathematical notation So for people who know, so n choose k is equal to factorial n factorial k factorial n minus k. So this is by definition of what this quantity is about.

**中文**

现在，它的好处是可以用一个很简洁的数学记号表达。对于了解这个记号的人，n choose k 等于 n 的阶乘、k 的阶乘、n 减 k 的阶乘 \[字幕疑漏运算符\]。这是这个量的定义。

### [41:36](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=2496s) · b000071

**English**

So we're going to use that here. So here, we have a series of products. So here, we can express that as factorial over another factorial. So here, it's factorial n minus c over factorial n minus c minus k. And then this quantity, we can also express that with factorials.

**中文**

我们在这里就要用到它。这里有一连串乘积，可以表示成一个阶乘除以另一个阶乘。这里是 n 减 c 的阶乘，除以 n 减 c 减 k 的阶乘。然后这个量也可以用阶乘表示。

### [42:10](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=2530s) · b000072

**English**

So it's factorial n. And the numerator is factorial n minus k. Everyone agrees with the math here? I'll take that as a yes. And so here, we're going to somehow pop the expression above up. So it's going to be equal to 1 minus so n minus c factorial over n minus c minus k factorial.

**中文**

这里是 n 的阶乘，分子是 n 减 k 的阶乘。大家都认可这里的数学推导吗？我就当大家都认可了。接下来，我们要想办法把上面的表达式凑出来。所以，它等于 1 减去，n 减 c 的阶乘，除以 n 减 c 减 k 的阶乘。

### [42:49](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=2569s) · b000073

**English**

And then k factorial. And then here, we're going to say it's this one, k factorial k factorial over n factorial. So here, I did a trick. What I did was I basically multiplied the numerator and the denominator by k factorial. And so here, I have 1 minus--so this is n minus c over n.

**中文**

再加上 k 的阶乘。然后这里，我们说是这个，k 的阶乘、k 的阶乘除以 n 的阶乘 \[字幕疑误，口述公式可能存在重复或省略\]。这里我用了一个技巧：基本上就是把分子和分母同时乘以 k 的阶乘。于是这里有 1 减去——这是 n 减 c 除以 n。

### [43:28](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=2608s) · b000074

**English**

So n minus c choose--sorry, n minus c choose k over n choose k. So this is our estimates of path at k. Does everyone agree? Yeah?

**中文**

所以，是 n 减 c 选——抱歉，是 n 减 c 选 k，除以 n 选 k。这就是我们对 path at k \[字幕疑误，可能指 pass@k\] 的估计。大家都同意吗？嗯？

### [44:01](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=2641s) · b000075

**English**

So the reason why I derived it is because this formula can be a little bit daunting to look at. But it's actually quite natural because it's only using some sampling without replacement considerations. And so you will see in papers that people have this pass@k metric. So if you were to compute it, this would be the formula to use.

**中文**

我推导它的原因是，这个公式看起来可能有点吓人。但它其实很自然，因为只用到了无放回抽样的一些考虑。因此，你会在论文里看到人们使用 pass@k 指标。如果要计算它，这就是应当使用的公式。

### [44:33](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=2673s) · b000076

**English**

Cool. And special k of pass@k is pass@1. And pass@1 is defined as the probability of a single attempt succeeding. So this is something that you commonly know. So if suppose you have a model that produces an answer, what is the probability that it's correct? So if you replace k with 1, you will see that this formula will simplify a lot.

**中文**

好。pass@k 的一个特殊 k 情况是 pass@1。pass@1 定义为单次尝试成功的概率。这就是大家熟悉的东西。假设有一个模型生成了一个答案，它正确的概率是多少？如果把 k 替换为 1，你会发现这个公式大大简化。

### [45:07](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=2707s) · b000077

**English**

And it will be just a proportion of successful attempts, which also makes sense, just intuitively. Everyone clear with this? Yeah? Great. So now to your question. So what do you do with the temperature. And you're exactly right. When you generate these solutions multiple times, something that will influence your results is how diverse the solutions that you will generate will be.

**中文**

它就只是成功尝试所占的比例，直觉上也很合理。大家都清楚了吗？嗯？很好。现在回答你的问题：温度该怎么设？你说得完全对。当你多次生成这些解答时，一个会影响结果的因素，就是所生成解答的多样性。

### [45:40](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=2740s) · b000078

**English**

And this is something that you indeed use the temperature for. Now so what is the relationship between temperature and pass@k? Do we want low temperature, do we want a high temperature, or do we want something in between? Well, if you take a very low temperature, you know that your solutions will be good, but they will not be diverse.

**中文**

这确实就是 temperature 的用途。那么，temperature 与 pass@k 之间是什么关系？我们想要低温度、高温度，还是介于两者之间？如果采用非常低的温度，你知道生成的解答会比较好，但不会有多样性。

### [46:11](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=2771s) · b000079

**English**

So if you increase the number of samples that you generate, that quantity will not change, which is seen with this graph with the T equal to 0. It doesn't change. But then when you have T equal to 0.2, now it's increases because you have some diversity. But if you increase this temperature too much, then you will have the diversity that you want. But they will also harm the performance of your predictions, because maybe the tokens that were not that likely will become likely.

**中文**

因此，即使增加生成的样本数量，这个量也不会变化。图中 T 等于 0 的曲线就体现了这一点，它没有变化。但当 T 等于 0.2 时，它开始上升，因为有了一些多样性。不过，如果温度升得过高，虽然会得到想要的多样性，却也会损害预测性能，因为原本不太可能出现的 tokens，可能会变得更容易出现。

### [46:46](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=2806s) · b000080

**English**

And so here, on the opposite side, we have t equal 1.2 here, which is extreme in this example, which is not the best. So I guess to respond to you, typical temperature choice would be something that is not too large, not too small. And I believe in this example is t equal to 0.8 that I think produces the best results towards the bigger samples. But then here, I guess it's not clear. Maybe 0.4. So that's why you will see that in papers, people always specify the temperature that they chose to produce the benchmark results.

**中文**

另一端是这里 t 等于 1.2，在这个例子中属于极端情况，并不是最好的。因此，回答你的问题，通常会选择一个不太大也不太小的温度。我记得在这个例子里，t 等于 0.8 在样本数较大时，似乎产生了最好的结果。但这里我觉得不太清楚，也可能是 0.4。所以，你会看到论文中总会注明，为得到基准结果，他们选择了什么温度。

### [47:28](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=2848s) · b000081

**English**

So that's why it's good to have that in mind. So these are the main metrics that people use but not the only ones. There's another one that you may see, which is called consensus at k, which is the answer that is coming from the highest number of times that the answer appears among your generations. And you can think of the self-consistency technique as being very related to that.

**中文**

因此，记住这一点很有用。这些是人们使用的主要指标，但不是仅有的指标。你还可能看到另一个，叫 consensus at k，也就是选择你生成的结果中出现次数最多的答案。你可以认为，自一致性（self-consistency）技术与它非常相关。

### [48:02](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=2882s) · b000082

**English**

So you may see that. And then the other metrics that you will see in those benchmarks are typically the ones that you're familiar with like accuracy, exact match, and so on. I took a lot of time on this first part. I think I need to go a bit faster. But does that roughly make sense so far? Yeah? So right now, I hope you what a reasoning model is. So now we're going to go into the most interesting part of the lecture, which is how can we build such a reasoning model.

**中文**

所以，你可能会看到它。然后，这些基准里的其他指标，通常就是你熟悉的那些，比如准确率（accuracy）、精确匹配（exact match）等等。第一部分我花了很多时间，我想得加快一点了。不过，到目前为止，大致都明白吗？嗯？现在，希望大家已经了解什么是推理模型。接下来进入本讲最有意思的部分：如何构建这样一个推理模型。

### [48:39](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=2919s) · b000083

**English**

So we know we want our reasoning model to produce a reasoning chain. But right now, we don't really how to do that at scale. And this is going to be the main focus in this part. So here the idea is to somehow incentivize the model to produce a chain of thought or reasoning chain before answering. So the problem with that is that reasoning chains writing is a very tough task, especially for, I guess, long reasoning chains.

**中文**

我们知道，希望推理模型生成一条推理链。但目前，我们还不太知道如何大规模地做到这一点。这将是这一部分的重点。这里的想法是，通过某种方式激励模型在回答之前生成 chain of thought，也就是推理链。问题在于，编写推理链是一项非常艰巨的任务，尤其是很长的推理链。

### [49:22](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=2962s) · b000084

**English**

And for that, let's suppose if we were to go look into our toolbox of the techniques we have learned so far, maybe we can think, OK, we can use SFT to do that. But the problem with SFT is you need high quality data, and in particular, you would need to write all of these reasoning chains. Let's suppose you do not have this reasoning chains. So how do you do that? You would typically write them from scratch. But that is very hard. So that's one, I guess, one vote to not do SFT, if we don't have any reasoning chains.

**中文**

对于这一点，假如我们翻一翻目前学过的技术工具箱，可能会想，好，可以用 SFT。但 SFT 的问题在于，需要高质量数据，尤其需要把这些推理链全部写出来。假设你没有这些推理链，该怎么办？通常就得从头编写。但这很难。所以，如果我们没有任何推理链，这算是不采用 SFT 的一个理由。

### [50:00](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=3000s) · b000085

**English**

So the second reason here is, or the second fact, is that the way the model reasons may be different from the way we reason. And for that, maybe a human written reasoning may not be the best way to teach the model on how to reason. So that's the second fact, which is going against having some human written reasoning chains as SFT data.

**中文**

第二个原因，或者说第二个事实，是模型的推理方式可能与我们的推理方式不同。因此，人类编写的推理可能并不是教模型推理的最佳方式。这是第二个事实，也是不支持将人类编写的推理链用作 SFT 数据的一个理由。

### [50:34](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=3034s) · b000086

**English**

And then the third fact that I want to say is we just saw that these reasoning tasks, they have a very natural reward, which is actually verifiable. So for coding, you know if your thing works, if it passes some test cases, if it compiles, and for math, you know if it works if the answer is the same as your ground truth. So naturally, you do have a reward signal.

**中文**

第三个我想说的事实是，我们刚刚看到，这些推理任务有一种非常自然的奖励，而且实际上是可验证的。对于编程，你可以知道它是否能运行、是否通过某些测试用例、是否能够编译。对于数学，如果答案与 ground truth 相同，你就知道它是否正确。因此，你自然就拥有了奖励信号（reward signal）。

### [51:05](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=3065s) · b000087

**English**

So we saw there's a reward signal. SFT is not a great way to start from scratch. Well, what do you do? Well, let's try RL then. And the good thing is last week, we saw how RL works in the case of LLMs. So I guess that's a great timing. So how would we do that? So just as a reminder, we want to teach our model to solve these more complicated problems.

**中文**

我们看到有奖励信号，而 SFT 并不是从零开始的好方法。那么怎么办？试试 RL 吧。好在上周我们已经讲了 RL 在 LLM 场景下如何工作，我觉得时机正好。那么，具体怎么做？先提醒一下，我们想教模型解决这些更复杂的问题。

### [51:42](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=3102s) · b000088

**English**

And we also want to teach it to reason before. So in order to do that, we first want to have a reward that checks whether the reasoning chain is there. So here, you can do that by simply checking whether the model has produced a reasoning chain. And you can check that by checking the presence, let's say, of the think, start, and end token that you can instruct your model to use to insert its reasoning chain.

**中文**

我们还想教它在这之前先推理。为此，首先需要一个检查推理链是否存在的奖励。这里，只要检查模型是否生成了推理链即可。比如，可以检查 think 的起始和结束 token 是否存在；你可以指示模型使用这些 tokens 来插入推理链。

### [52:18](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=3138s) · b000089

**English**

And then the second reward that you want to have is to check that the solution that it produced actually works. And so here, as we mentioned, this is something that you can actually do for the benchmarks that we care about. So for codes, you would check that it works for all cases. For math, you would just verify with respect to the answer being the same as the ground truth. So we also have that. So in summary, we will run RL, and we will run RL using a reward that is a combination of checking whether the thing tokens are here and that the end result is correct.

**中文**

然后，第二个想要的奖励，是检查它生成的解法是否真的有效。正如我们提到的，对于我们关注的基准，这实际上是可以做到的。对于代码，要检查它是否在所有情况中都能运行。对于数学，只需验证答案是否与 ground truth 相同。这一点也具备了。总之，我们会运行 RL，使用的奖励会结合两项检查：thing tokens \[字幕疑误，可能指 think tokens\] 是否存在，以及最终结果是否正确。

### [53:08](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=3188s) · b000090

**English**

And we saw that both of them, we can do this easily. No need for a model. So let's suppose you do that. Let's suppose you do RL on search rewards. Well, the nice thing that you see is if you plot the performance of the model with respect to one of those benchmarks that I mentioned-- so here it's aim. So if you remember, it's the math benchmark--you see that as you perform your RL steps, the performance of the model on those benchmarks, they actually increase.

**中文**

我们已经看到，这两项都很容易做到，不需要模型。假设你这么做，假设你基于 search rewards \[字幕疑误，可能指 such rewards，即这样的奖励\] 进行 RL。那么，你会看到一个很好的现象：如果画出模型在我刚才提到的某个基准上的性能，这里是 aim \[字幕疑误，可能指 AIME\]，如果大家还记得，它是数学基准，你会发现，随着 RL 步骤推进，模型在这些基准上的性能确实会提高。

### [53:46](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=3226s) · b000091

**English**

And they actually increase quite significantly. So the graph here is actually coming from the training of DeepSeek R1--actually, R1-Zero here, which we will see a little bit more in detail with Shervine how it actually works. But you can see that if you incentivize the model to think and produce the right answer, it can actually learn quite meaningfully, only with these two verifiable rewards.

**中文**

而且提高得相当显著。这里的图实际上来自 DeepSeek R1 的训练——准确说，这里是 R1-Zero。我们会和 Shervine 一起更详细地看看它到底如何工作。但你可以看到，只要激励模型思考并给出正确答案，它就能仅凭这两个可验证奖励，学到相当有意义的东西。

### [54:19](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=3259s) · b000092

**English**

But now you may wonder, let's suppose I'm teaching my model to think, well, not all prompts are equal. There are some prompts that do not need the model to think too much as opposed to other prompts which would need a little bit of thinking. So there has been a lot of, I guess, work happening in the community as how to control the amount of thinking that the model does.

**中文**

但你可能会想，假设我在教模型思考，可并非所有 prompt 都一样。有些 prompt 不需要模型思考太多，而另一些则需要一些思考。所以，社区里已经有很多工作在研究如何控制模型的思考量。

### [54:51](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=3291s) · b000093

**English**

So you have things like dynamic budget that you will see out there, how can we make sure that the model does not overthink on questions that do not need too much thinking. So for this, you can have something like a quick classifier, let's say, that runs on the prompt and tells you whether it's something that is kind of a high thinking kind of problem or a low thinking one. But this is more of an open problem. But this can be one solution.

**中文**

你会看到动态预算（dynamic budget）之类的工作：如何确保模型在不需要太多思考的问题上不过度思考？为此，可以使用一个快速分类器（classifier），对 prompt 进行判断，告诉你它属于需要大量思考的问题，还是只需少量思考的问题。不过，这更多还是一个开放问题。但这可以是一种解决方案。

### [55:24](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=3324s) · b000094

**English**

So the second one is those LLMs, they have a limited context window. So when the LLM thinks, it needs to. Also be aware of how much context length is left. It cannot think too much also because of that limitation. So you need to also have that context awareness. So there has been some work to also force the model to either think more or stop.

**中文**

第二点是，这些 LLM 的上下文窗口（context window）是有限的。因此，LLM 思考时，还需要意识到剩余的上下文长度有多少。由于这个限制，它也不能思考太多。所以，还需要这种上下文感知能力。已经有一些工作尝试强制模型多思考一些，或者停止思考。

### [56:00](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=3360s) · b000095

**English**

So there is this term, budget forcing, that I think was introduced in this paper, S1. So the idea here is if you want your model to continue thinking, you're going to introduce some tokens mid-way to force it to think more. And such tokens are, for instance, weights. I think there is another solution. So actually, it's a slide that I have not really talked about. So if you look at this reasoning chain, sometimes the model will output something like, oh wait, wait, wait, I think I found something else.

**中文**

有一个术语叫预算强制（budget forcing），我记得是在 S1 这篇论文中提出的。这里的想法是，如果希望模型继续思考，就在中途插入一些 tokens，迫使它多想一会儿。例如，这样的 tokens 可以是 weights \[字幕疑误，可能指 wait\]。“我觉得还有另一种解法。”实际上，有一页幻灯片我还没有真正讲过。看看这条推理链，有时模型会输出类似这样的话：“哦，等等，等等，等等，我想我发现了别的东西。”

### [56:36](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=3396s) · b000096

**English**

And typically, the model would go again on another kind of reasoning path. And this can be one way to incentivize your model to think more. Or another term can be, OK, your time is up. Now my answer is, and it will force your model to respond. And then if you think about it, your model gives tokens in its reasoning chain, but models may think on some other space, maybe not in the language space.

**中文**

通常，模型就会再次沿着另一种推理路径走下去。这可以是激励模型多思考的一种方式。或者也可以用另一句话：“好，时间到了。现在我的答案是”，这样就会强制模型回答。另外，仔细想想，模型在推理链中给出 tokens，但模型也可能在其他空间里思考，未必是在语言空间里。

### [57:16](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=3436s) · b000097

**English**

So there is also a line of work around having some continuous thoughts. Basically having this thinking token actually not be tokens, but be hidden representations that can be more meaningful, but also more compressed. So you have a bunch of papers on this. So there's one that we linked, which is actually from 2024. But I think even a few days ago, I also saw another paper on that. So it's very much active area of research.

**中文**

因此，还有一条研究路线是连续思维（continuous thoughts）。基本上，就是让这些思考 token 实际上不再是 tokens，而是隐藏表示（hidden representations），它们可能更有意义，也更紧凑。相关论文有不少。我们链接了一篇，实际上来自 2024 年。但我想，就在几天前，我还看到另一篇相关论文。所以，这是一个非常活跃的研究领域。

### [57:49](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=3469s) · b000098

**English**

And I guess just like that, I guess we saw that the way that we want to scale our model is with RL. I guess is everyone convinced of that? Did I convince you well with those arguments, or does anyone have any questions on this? And I guess here, I want you to have a takeaway, which is we want to use RL to incentivize our model to think more if we start from scratch, meaning we don't have reasoning chains.

**中文**

就这样，我们看到，想要扩展模型能力，可以使用 RL。大家都被说服了吗？这些论点说服大家了吗，还是有人对此有问题？这里，我希望大家记住一点：如果从零开始，也就是没有推理链，我们希望用 RL 来激励模型更多地思考。

### [58:27](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=3507s) · b000099

**English**

So is everyone good with this? Yeah? Kind of, yeah. So I'll take this as a yes. So now we're going to see the algorithm that we use to perform that RL step. And you may have heard this acronym a lot. So this algorithm that we will see is called GRPO. And GRPO has been released in 2024.

**中文**

大家对此都没问题吗？嗯？算是吧，嗯。那我就当大家同意了。现在我们来看执行这个 RL 步骤所用的算法。你可能经常听到这个缩写。我们要讲的算法叫 GRPO。GRPO 于 2024 年发布。

### [58:58](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=3538s) · b000100

**English**

And it has been the go to RL algorithm for all these reasoning tasks, or for this reasoning training tasks. So what is GRPO? So GRPO stands for group relative policy optimization. And it is an RL algorithm which, very much like PPO, aims to do these two things we talked about.

**中文**

它已经成为所有这些推理任务，或者说推理训练任务的首选 RL 算法。那么，什么是 GRPO？GRPO 的全称是组相对策略优化（group relative policy optimization）。它是一种 RL 算法，与 PPO 很相似，目标是完成我们讨论过的两件事。

### [59:29](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=3569s) · b000101

**English**

So the first one is to maximize advantages. And if you remember, advantage is something that tells you whether what you're producing as an answer is better than what you would expect. So this is the first part. And then the second part is that you do not want to deviate too much from either the old model, which is the model at the previous iteration, or the base model, which is the model at SFT stage.

**中文**

第一件事是最大化 advantage。如果大家还记得，advantage 会告诉你，所生成的答案是否比预期更好。这是第一部分。第二部分是，你不希望偏离旧模型太多，也就是上一次迭代时的模型；也不希望偏离基础模型太多，也就是 SFT 阶段的模型。

### [1:00:10](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=3610s) · b000102

**English**

So GRPO is also doing the same thing as PPO in that sense. But then there is a key difference. And that difference lies in how it computes the advantage. So if you remember, PPO estimated the advantage by taking the rewards, which is at the completion level. So you know you have your prompts, and you have a response, a full response.

**中文**

因此，从这个意义上说，GRPO 与 PPO 做的是同样的事。但有一个关键差异，差异在于它如何计算 advantage。如果大家还记得，PPO 估计 advantage 时，会使用 completion 级别的奖励。也就是说，你有 prompt，然后有一个回答，一个完整的回答。

### [1:00:40](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=3640s) · b000103

**English**

And then based on those two elements, you have a reward. So what PPO did was take that into consideration along with something else that it was training jointly at training time, which was called the value function. And the value function objective was to try to predict what that reward was if we were to continue generating the tokens following the policy.

**中文**

接着，根据这两个元素，得到一个奖励。PPO 会考虑这个奖励，同时考虑另一个在训练时联合训练的东西，叫价值函数（value function）。value function 的目标，是尝试预测：如果继续按照策略生成 tokens，奖励会是多少。

### [1:01:14](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=3674s) · b000104

**English**

And if you remember, the advantage here is actually, in the case of PPO, was something that we obtained based on a very complex formula that we did not see, actually. But that's called a generalized advantage estimation. That is a method to estimate those advantage. And the big limitation with that was that you had to train a value function jointly with your policy. So this big bottleneck.

**中文**

如果大家还记得，在 PPO 中，advantage 实际上是根据一个非常复杂的公式得到的，我们其实没有讲那个公式。它叫广义优势估计（generalized advantage estimation），是一种估计这些 advantage 的方法。它的一个重大局限是，你必须把 value function 与策略一起训练。这是一个很大的瓶颈。

### [1:01:45](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=3705s) · b000105

**English**

And in contrast to that, GRPO says, well, we're not going to do that. We're going to take a completion. We're going to compute each reward. And we're going to compare it with the average of rewards of completions for that same prompt. So I'll give you an example. So let's suppose we have a math problem. So what we're saying here is we're going to generate multiple completions for that same prompt.

**中文**

相比之下，GRPO 说，我们不这么做。我们拿一个 completion，计算各自的奖励，再把它与同一个 prompt 下各个 completion 的平均奖励进行比较。我举个例子。假设有一道数学题。这里的做法是，为同一个 prompt 生成多个 completions。

### [1:02:25](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=3745s) · b000106

**English**

And for each prompt and completion--and the prompt is shared. So for each completion, we're going to measure, I guess, a relative measure of the reward for that completion and all the other rewards of the other completions. So this will give us an idea of how much better or how much worse is it from, I guess, the rest of the group.

**中文**

然后，对每组 prompt 和 completion——prompt 是共享的——也就是说，对每个 completion，我们要衡量其奖励相对于其他所有 completions 奖励的某种相对量。这就能让我们知道，它比组内其余结果好多少或差多少。

### [1:02:56](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=3776s) · b000107

**English**

And so this is going to be our advantage. So the big benefit here is that we do not use value functions. We do not use that. The only thing we do is we sample not just one, but multiple completions in order to compute the average of the rewards of the group. Does this make sense?

**中文**

这就会成为我们的 advantage。这里最大的好处是，不使用 value functions。我们不用它。我们唯一要做的，就是不只采样一个，而是采样多个 completions，以计算这一组奖励的平均值。这样讲明白吗？

### [1:03:29](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=3809s) · b000108

**English**

Oh, yeah. So what would you do instead? So the question is, why would you do that. Well, the traditional RL algorithms, just for reference, they have been developed before all these LLMs became a thing. So for instance, PPO was a method that I believe is from 2017.

**中文**

哦，对。那你会怎么做？问题是，为什么要这样做？供大家参考，传统 RL 算法是在这些 LLM 兴起之前开发出来的。比如，PPO 我记得是 2017 年的方法。

### [1:04:03](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=3843s) · b000109

**English**

So these quantities, they may make a lot of sense in some setups, but maybe not in the language world. And I guess here, the idea is let's try to think of something that tells you how good your completion is just in the relative sense. But here, I guess what the authors want to do is to not have to have this very expensive joint model that they have to train and think of another relative way of doing that.

**中文**

所以，这些量在某些设置中可能很有意义，但在语言领域未必如此。这里的想法是，尝试找一个量，仅从相对意义上告诉你 completion 有多好。我想，作者在这里希望避免训练一个代价非常高的联合模型，转而寻找另一种相对的做法。

### [1:04:36](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=3876s) · b000110

**English**

So I think that's the high level intuition. And I guess here, the idea is let's just sample multiple times and see how one response is comparing to the others, and then use that as some kind of baseline to put this reward into context. So for instance, you may have a math problem that's kind of easy. And if you have a high reward for that one, maybe it's because the problem was easy to start with.

**中文**

我认为，这就是高层次的直觉。这里的想法是，多次采样，看看一个回答与其他回答相比如何，然后把这用作某种 baseline，为奖励提供参照。例如，你可能有一道比较简单的数学题。如果它得到了很高的奖励，可能只是因为题目本来就简单。

### [1:05:11](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=3911s) · b000111

**English**

But if you have, let's say, very hard problem, if you have the correct answer, then you want to make sure you're incentivizing your model to upweight those tokens much more because if you find a good solution, it's a good solution to a hard problem. So you want to somehow bake that in into your advantage. So that's the intuition. So GRPO was developed a year ago. And a year ago, LLMs were everywhere.

**中文**

但如果是一道非常难的题，而你得到了正确答案，那么你就希望确保激励模型，更大幅度地提高这些 tokens 的权重，因为找到的是难题的一个好解法。所以，你希望把这一点以某种方式纳入 advantage。这就是直觉。GRPO 是一年前开发的，而一年前，LLM 已经无处不在了。

### [1:05:43](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=3943s) · b000112

**English**

So this is also taking into consideration, I guess, what LLMs are incentivized to do in some sense. So yeah, I would think it that way. Does that help? Cool, cool. Any other question on this? Well, don't worry if you have questions because we will have a walkthrough of exactly how it works. So here, we're going to go through the exact same thing, but illustrate it.

**中文**

因此，从某种意义上说，它也考虑了我们要激励 LLM 去做什么。对，我会这样理解。有帮助吗？好，好。对此还有其他问题吗？即使有问题也不用担心，因为我们会一步步讲解它具体如何工作。这里，我们会再次讲同样的过程，不过用图来说明。

### [1:06:15](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=3975s) · b000113

**English**

So in the GRPO case, we're taking a query, and we're passing that through our policy model, which is our LLM that we're trying to train. And here, what we said was we want to generate not one, but multiple completions. Let's suppose g completions. And each of these query completions--So you have g such pairs.

**中文**

在 GRPO 中，我们拿到一个查询（query），把它传给策略模型（policy model），也就是正在尝试训练的 LLM。我们刚才说过，要生成的不是一个，而是多个 completions。假设是 g 个 completions。每个查询与 completion——因此，你有 g 个这样的配对。

### [1:06:49](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=4009s) · b000114

**English**

You pass them through the reward model that gives you g rewards. And what you want is to compute the advantage which puts all these rewards into their context. So we saw it was basically the reward minus the average. But it's actually not exactly that. So it's reward minus the average over the standard deviation of those rewards is how they defined it. By the way, we will see that it may not be the best way to do it, but we'll see that in a second.

**中文**

把它们传给 reward model，就会得到 g 个奖励。你想计算 advantage，让这些奖励都有相对的参照。我们说过，基本上是奖励减去平均值，但实际上并不完全如此。他们的定义是，奖励减去平均值，再除以这些奖励的标准差（standard deviation）。顺便说，我们会看到，这可能不是最好的做法，不过稍后再讲。

### [1:07:22](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=4042s) · b000115

**English**

And we use those advantages to then tune our policy model. And while we do that, we, of course, don't want to deviate too much for from the reference model. So we have this KL divergence term as well over here. So that is GRPO. And we're going to see right now exactly how this worked with PPO. So with PPO, if you remember, you have your prompt.

**中文**

然后，我们用这些 advantage 来调优 policy model。在这个过程中，当然也不希望偏离参考模型（reference model）太多。因此，这里也有一个 KL divergence 项。这就是 GRPO。现在，我们来看看 PPO 中具体是怎么做的。对于 PPO，如果大家还记得，你有一个 prompt。

### [1:07:55](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=4075s) · b000116

**English**

You have your query. You pass that through your policy model. And you only have one completion. And you pass your prompt and your completion. So this pair, you pass it through the reward model, and this gives you a reward for that whole completion. Now, there's one thing we did not see last time, which is more of a implementation detail. But we also have a KL divergence term that is, comparing the probability of each token with the probability of the token for from the reference model.

**中文**

你有一个 query，把它传给 policy model，只得到一个 completion。然后把 prompt 和 completion，也就是这一对，传给 reward model，就会得到针对整个 completion 的奖励。这里有一点上次没讲，更偏向实现细节：我们还有一个 KL divergence 项，用来比较每个 token 的概率与 reference model 给出的该 token 概率。

### [1:08:39](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=4119s) · b000117

**English**

And from an implementation standpoint, we also typically incorporate that in the rewards. So we have something like a per token rewards where only the last token has the reward of the whole completion. But then everyone has also a KL divergence term. So that one is not super important here to have in mind. But it's just good to know that people implement it that way.

**中文**

从实现角度来说，我们通常也会把它纳入奖励。因此，会有一种逐词元奖励（per token rewards），其中只有最后一个 token 带有整个 completion 的奖励，但每个 token 也都有一个 KL divergence 项。这里不必特别记住这一点，不过知道大家是这样实现的也有好处。

### [1:09:10](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=4150s) · b000118

**English**

So once you have those rewards, you also have a value function that this one is per token. This one tries to quantify the rewards if you were to continue generating the rest of the sequence following the policy. And we saw there is this method that we're not going to see. That is called generalized advantage estimation that takes in those two quantities and computes the advantage.

**中文**

得到这些奖励之后，你还有一个 value function，它也是逐 token 的。它试图量化：如果继续按照策略生成序列的剩余部分，奖励会是多少。我们还提到过一种不会展开讲的方法，叫 generalized advantage estimation，它接收这两个量并计算 advantage。

### [1:09:45](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=4185s) · b000119

**English**

You can think of it as some complicated formula. And you have your advantage that you use to tune the policy. And that's it, which is a complicated compared to this one. So GRPO, you use advantages that are a result of this group computation. But then PPO, you have an advantage that is a result of rewards and the value function, which is per token.

**中文**

你可以把它看成某个复杂公式。得到 advantage 后，就用它来调优策略。就是这样，相比这个方法要复杂一些。因此，在 GRPO 中，使用的 advantage 来自这种组内计算；而在 PPO 中，advantage 来自奖励和 value function，是逐 token 的。

### [1:10:20](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=4220s) · b000120

**English**

Yeah? So what are the models at stake here? So here, we have some models that we use that are, quote unquote, frozen, that are not the ones that we train. So for GRPO, we have the reference model that we do the KL divergence on. And then we have the reward model, which we trained in the past. And the same is the case for PPO.

**中文**

嗯？那么，这里涉及哪些模型？我们用到的一些模型是所谓“冻结”（frozen）的，也就是不参与训练的模型。对于 GRPO，有一个用于计算 KL divergence 的 reference model，还有一个之前已经训练好的 reward model。PPO 也是如此。

### [1:10:52](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=4252s) · b000121

**English**

Now, one thing to note is that in the reasoning case, we are actually not training a reward model because we know how to tell whether a solution is correct or not. We actually have a verifiable reward. So in the reasoning case, we're actually not having any reward model at all. It's the same for both. Now what is different is the models that we train. So in the GRPO case, we only train the policy model, whereas in the PPO case, we train the policy model and the value function the value model.

**中文**

现在，有一点要注意，在推理（reasoning）的情况下，我们实际上不训练奖励模型（reward model），因为我们知道如何判断一个解答是否正确。我们实际上有可验证奖励（verifiable reward）。所以在推理的情况下，我们实际上完全没有奖励模型。两者在这一点上相同。不同的是我们训练的模型。在 GRPO 的情况下，我们只训练策略模型（policy model）；而在 PPO 的情况下，我们训练策略模型和价值函数（value function），也就是价值模型（value model）。

### [1:11:36](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=4296s) · b000122

**English**

And this is the key difference. So until now, we've seen only drawings and illustrations. So let's see some math. So you have the GRPO loss function at the top and the PPO loss function at the bottom. They look scary. But we're going to see together some similarities and some differences.

**中文**

这就是关键区别。到目前为止，我们看到的都只是图画和示意图。现在来看一些数学。上面是 GRPO 的损失函数（loss function），下面是 PPO 的损失函数。它们看起来很吓人。但我们会一起看看其中的一些相似之处和不同之处。

### [1:12:07](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=4327s) · b000123

**English**

So what is one similarity? Both of them, they operate on the ratio of the probability of the current policy and the probability of the old policy. So as the first point in common. The second point in common is that both of them, they try to keep the updates within some region, not too wide.

**中文**

那么，相似之处是什么？两者都作用于当前策略（current policy）的概率与旧策略（old policy）的概率之比。这是第一个共同点。第二个共同点是，两者都试图把更新限制在某个范围内，不要太宽。

### [1:12:40](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=4360s) · b000124

**English**

And they do that with the clipping mechanism that we saw last lecture. So I recommend that you just go through these charts that we saw together. When the advantage is positive, how the loss looks like. And when the advantage is negative. So this clipping function just allows you to not make updates that are too big, that are too wide. But now. What is different.

**中文**

它们通过我们上一讲看到的裁剪机制（clipping mechanism）来做到这一点。所以我建议你们再看看我们一起看过的这些图。当优势（advantage）为正时，损失是什么样子。以及当 advantage 为负时又是什么样子。这个裁剪函数就是让你不要做出太大、幅度太宽的更新。但现在，区别是什么？

### [1:13:11](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=4391s) · b000125

**English**

So in the JPO case, the KL divergence is actually something that is explicitly part of the objective function. Whereas for the PPO case, this KL divergence is typically part of the advantage. So this is more of a technical detail. But a few minutes ago I had mentioned that from an implementation standpoint, we typically incorporate the KL divergence within the rewards that are considered in the advantage computation.

**中文**

在 JPO \[字幕疑误，可能指 GRPO\] 的情况下，KL 散度（KL divergence）实际上是目标函数（objective function）的显式组成部分。而在 PPO 的情况下，KL divergence 通常是 advantage 的一部分。这更多是一个技术细节。但几分钟前我提到过，从实现角度来看，我们通常把 KL divergence 纳入计算 advantage 时所考虑的奖励中。

### [1:13:51](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=4431s) · b000126

**English**

So that's one difference. And then the second difference is the way we compute advantages. So we saw that GRPO, we typically compute rewards for each completions, and then we compare them with the other completions from the group. Whereas for PPO, we use the rewards and the value models. So far so good? I think I have some other things I want to talk about.

**中文**

这是一个区别。第二个区别是计算 advantage 的方式。我们看到，在 GRPO 中，我们通常为每个补全（completion）计算奖励，然后将它们与组内其他 completions 进行比较。而对于 PPO，我们使用奖励和价值模型。到目前为止都还好吗？我想我还有一些其他内容要讲。

### [1:14:23](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=4463s) · b000127

**English**

But before that, I just want to open the floor if anyone has any questions. This is very technical, by the way. Very technical, probably the hardest part of the whole class. So it's completely normal to, I guess, take some time to digest that. And if no one has any questions, I actually see this as more of an alarm for myself because this is maybe--I don't know. So let me if there's any questions on this.

**中文**

但在那之前，我想先让大家提问，看看有没有人有问题。顺便说一句，这部分技术性很强。非常强，可能是整门课最难的部分。所以，我想，花一些时间来消化是完全正常的。如果没有人有问题，我反而会觉得这对我来说更像是个警报，因为这可能——我不知道。所以让我……看看有没有关于这部分的问题。

### [1:14:54](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=4494s) · b000128

**English**

And yeah, absolutely no problem to have any kind of questions. Is everything super clear? Super clear? So just tell yourself that these algorithms, they're just there to tune your model in the RL stage. PPO is heavily used in the preference tuning framework, where you try to tune your model to align it with human preferences, and is commonly used for these reasoning based training.

**中文**

对，任何问题都完全可以提。一切都非常清楚了吗？非常清楚？你们只要告诉自己，这些算法就是用来在强化学习（reinforcement learning，RL）阶段调整模型的。PPO 在偏好调优（preference tuning）框架中被大量使用，在这个框架里，你会尝试调整模型，使它与人类偏好对齐，而且也常用于这些基于推理的训练。

### [1:15:36](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=4536s) · b000129

**English**

So I think if you tell yourself that is something. And then the second thing you need to tell yourself is GRPO differs from PPO in that GRPO does not need a value function. It actually computes its advantages by comparing the rewards with respect to other completions. And then the PPO, it takes in the reward, it takes in the value, and then compares the two to get the advantage.

**中文**

所以我觉得，如果你这样告诉自己，就算理解了一些东西。然后，你需要告诉自己的第二点是，GRPO 与 PPO 的区别在于 GRPO 不需要价值函数。它实际上通过将奖励与其他 completions 的奖励进行比较来计算 advantage。而 PPO 则接收奖励，接收价值，然后比较两者来得到 advantage。

### [1:16:08](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=4568s) · b000130

**English**

So if this is making sense, I think this is already a very good thing. So is this making sense? Yeah?

**中文**

如果这些能理解，我觉得就已经很好了。所以这些能理解吗？可以吗？

### [1:16:20](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=4580s) · b000131

**English**

I would also recommend to just rewatch the recording. So we're recording this. This is very heavy and can be technical. So just rewatching it a few times I think can help. So we have 11 minutes before giving it to Shervine. And what we're going to see now is some extensions of the GRPO work that was done last year that people have done in the past few months.

**中文**

我也建议大家回看录像。我们正在录制这节课。这部分内容很繁重，也可能很技术化。所以我觉得多回看几次会有帮助。我们还有 11 分钟，然后就交给 Shervine。现在我们要看的是，大家在过去几个月里对去年完成的 GRPO 工作做出的一些扩展。

### [1:16:50](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=4610s) · b000132

**English**

So this research is going back to early 2025, but it has gained enough traction for us to talk about it in this class. So if you remember what I mentioned in the beginning of the lecture, reasoning tokens are being charged to you as a user. So you don't want to pay a lot. You don't want to pay too much. So you want your model to do what you want, but you do not want it to generate too much so that you're getting charged for it.

**中文**

这项研究可以追溯到 2025 年初，不过它已经获得了足够多的关注，值得我们在这门课上讨论。如果你们还记得我在这节课开头说过的内容，作为用户，你们需要为推理词元（reasoning tokens）付费。所以你不想付很多钱。不想付太多。你希望模型做你想让它做的事情，但又不希望它生成太多内容，以至于你要为这些内容付费。

### [1:17:26](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=4646s) · b000133

**English**

And also from the provider side, I guess it's much better to be more efficient. So there is an incentive to see what we can optimize from the output length perspective. So if you see the training of these models, one thing that you notice is that as you train it in the RL stage, the output increases in length.

**中文**

而且从提供方的角度来看，我想，效率更高也好得多。所以大家有动力去看看，从输出长度的角度能优化什么。如果你观察这些模型的训练，你会注意到一点：随着 RL 阶段的训练进行，输出长度会增加。

### [1:17:56](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=4676s) · b000134

**English**

So here this graph shows as a function of the RL step the average length per response. So you see, from an empirical perspective, that the answer that the LLM is outputting is getting longer and longer. And this is mainly coming from the reasoning chain that is being more and more sophisticated. And when you compare this graph with respect to how the performance of the model improves, you see that this increase here in length is actually correlated with an increase in performance.

**中文**

这张图展示了每条回复的平均长度随 RL 步数的变化。所以从经验观察来看，大语言模型（large language model，LLM）输出的回答越来越长。这主要源于推理链（reasoning chain）变得越来越复杂。当你把这张图与模型性能的提升情况作比较时，会看到这里的长度增加实际上与性能提升相关。

### [1:18:40](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=4720s) · b000135

**English**

And you might say, OK, it's good. But then there comes a stage over here where the performance-- so it's on the left--the performance of your model tends to stabilize, but then your output length still continues increasing. And so a lot of people have looked at these charts and they're like, OK, there's something going on. So here, what we're going to do is to look at this phenomenon and see how people have tried to mitigate it.

**中文**

你可能会说，好啊，这很好。但接着会到达这里的某个阶段，性能——也就是左边的图——模型的性能趋于稳定，但输出长度仍在继续增加。因此，很多人看了这些图后会说，好，这里面有些情况。所以接下来，我们要看看这种现象，以及人们如何尝试缓解它。

### [1:19:19](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=4759s) · b000136

**English**

So little Warning-- this is also a little bit technical. So please bear with me. There is one formula that I will try to explain to the best that I can. But there is some amount of math. So in order to understand what's happening, we need to look at the GRPO loss. And the loss is the one that I just mentioned here. Seems like a very complicated formula, but it's not really a complicated one. I'm going to just explain in plain terms what this means.

**中文**

先小小提醒一下——这部分也有一点技术性。请大家耐心跟着我。有一个公式，我会尽我所能解释清楚。但这里确实会涉及一些数学。为了理解发生了什么，我们需要看看 GRPO 的损失。这个损失就是我刚才在这里提到的那个。它看起来像一个很复杂的公式，但其实并不复杂。我会用通俗的话解释它的意思。

### [1:19:53](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=4793s) · b000137

**English**

So J of GRPO--J means objective function. So the objective function of GRPO is to maximize this quantity, which is a function of how much your model changes with respect to the old one. So it's these ratios that you see in the slide. And you have this clipping mechanism that prevents your updates from being too wide. And then you have the KL divergence on the right, which prevents your model from being too far from the base model.

**中文**

GRPO 的 J——J 表示目标函数。GRPO 的目标函数就是最大化这个量，它取决于你的模型相对于旧模型改变了多少。也就是幻灯片上看到的这些比值。然后有这个 clipping 机制，防止更新幅度太大。右边还有 KL divergence，防止你的模型偏离基础模型（base model）太远。

### [1:20:32](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=4832s) · b000138

**English**

The reference model. And then you have these summations here and the summations here. They correspond to you going through that process for all completions in your group. Because remember if you have a prompt you sample several times have several completions, and then you do that for every token of your output. So here, the first summation is over the indices of your group.

**中文**

也就是参考模型（reference model）。然后这里和这里有这些求和。它们对应于对组内所有 completions 都执行这个过程。因为请记住，如果有一个提示（prompt），你会多次采样，得到多个 completions，然后对输出中的每个 token 都执行这个过程。所以这里，第一个求和遍历组内的索引。

### [1:21:05](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=4865s) · b000139

**English**

The second summation is over the indices that are with respect to the token number in your sequence. And so here, I guess let's just think for a second, if we were to swap--I'm not sure if you see what I did here. I just swapped the 1 over length of output number I. Just swapped it here. I'm going to explain why I did that. So if you look at this, this is a factor that is only a function of which output you're in.

**中文**

第二个求和遍历序列中 token 编号对应的索引。那么这里，我想我们先想一下，如果我们交换——我不确定你们有没有看清我刚才做了什么。我只是把 1 除以第 I 个输出的长度这一项移了一下。把它移到了这里。我会解释为什么这样做。如果你看这里，这个因子只取决于你处于哪个输出中。

### [1:21:45](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=4905s) · b000140

**English**

So if you're in a very long output, this will be 1 over a very long output. It will be a small number. If it's a short output, it's going to be 1 over a short number. It's going to be a big number.

**中文**

如果你处于一个很长的输出中，这就是 1 除以一个很长的输出长度。它会是一个很小的数。如果输出很短，就是 1 除以一个很小的数。它会是一个很大的数。

### [1:22:04](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=4924s) · b000141

**English**

And the term on the right of this is token specific. So in other words, the contribution of a token with respect to the objective function depends on the output that it is in. So if the token is in a short sentence, it's going to have a higher weight bigger weight than in a longer sentence.

**中文**

而它右边的这一项是特定于 token 的。换句话说，一个 token 对目标函数的贡献取决于它所在的输出。因此，如果这个 token 在一个短句中，它的权重就会比在一个长句中更高、更大。

### [1:22:36](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=4956s) · b000142

**English**

Until now, is everyone agreeing with me? Yeah? So with that being said, I'm just going to rephrase what I just said, if you are in a short sentence, your weight will be bigger than if you're in the bigger sentence. Now let's try to think about this in terms of the advantage.

**中文**

到目前为止，大家都同意我说的吗？是吗？那么，我再换个说法重复一下刚才的话：如果你在一个短句中，你的权重就会比在一个更长的句子中更大。现在我们试着从 advantage 的角度想一想。

### [1:23:08](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=4988s) · b000143

**English**

If you are in the case of a token being in an output that is of advantage, that is positive, that means that we would want to upweight the probability of this token happening again, much more for short sentences as opposed to longer ones. And at the same time, you want, when the advantage is negative--so it's not you want.

**中文**

如果一个 token 所在输出的 advantage 为正，这意味着我们希望提高这个 token 再次出现的概率，而且短句中的提高幅度要远大于长句。同时，你希望，在 advantage 为负时——其实不是说你希望。

### [1:23:40](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=5020s) · b000144

**English**

It's just that this formulation--makes tokens that are in short outputs be down weighted even more compared to when they're in a long output. And so this is the problem. This is a bad incentive because what you're telling your model is if you have a short bad sentence, it is worse than if you have a long bad sentence.

**中文**

只是这个公式会让短输出中的 tokens 相比于长输出中的 tokens 被更大幅度地下调权重。这就是问题所在。这是一种不好的激励，因为你实际上在告诉模型，一个短的糟糕句子比一个长的糟糕句子更糟。

### [1:24:16](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=5056s) · b000145

**English**

So that's the idea here. So I'm just going to just rephrase what we said until now. The fact of dividing by the length of the output is incentivizing your model to downweight even more tokens. If the tokens in a short output, it will be down weighted even more than if it's in a long output. So in other words, what you're going to do is to prefer longer bad outputs as opposed to shorter bad outputs.

**中文**

这就是这里的意思。我再换个说法重复一下我们到目前为止说的内容。除以输出长度这件事，会激励模型对 tokens 进行更大幅度的降权。如果 token 在一个短输出中，相比于它在一个长输出中，它会被更大幅度地降权。换句话说，你这样做会更偏好较长的糟糕输出，而不是较短的糟糕输出。

### [1:24:51](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=5091s) · b000146

**English**

And this is what people are hypothesizing that is making the output length bigger and bigger. And we're going to see that in a second. So what people did was do something about this. So this 1 over length of o, people wanted to do something about it. So there is one paper that came out in March, DAPO--quite a popular paper now--that actually equalizes this token level contributions.

**中文**

人们猜测，这正是让输出长度越来越长的原因。我们马上就会看到。所以人们采取了措施。对于这个 1 除以 o 的长度，人们想做点什么。3 月有一篇论文发表，叫 DAPO——现在相当热门的一篇论文——它实际上让这些 token 层面的贡献变得一致。

### [1:25:26](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=5126s) · b000147

**English**

And so here, this normalization factor is now common to all tokens. And there is another paper that's called--So I think it's GRPO done right. But it's Dr. GRPO So I'm not sure how you pronounce it. But that paper actually proposes to remove the factor altogether. And when you do that, if you compare the GRPO versus the one that equalizes the token level contributions, you see that if you plot reward as a function of output length, your model will stop increasing its length again and again.

**中文**

这里，这个归一化因子（normalization factor）现在对所有 tokens 都是相同的。还有另一篇论文，叫作——我记得是 GRPO done right。但它叫 Dr. GRPO，所以我不确定应该怎么念。那篇论文实际上提出把这个因子完全去掉。当你这样做时，如果比较 GRPO 和让 token 层面的贡献一致的方法，你会看到，如果把奖励画成输出长度的函数，模型就会停止不断增加输出长度。

### [1:26:14](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=5174s) · b000148

**English**

So if you actually look deeper, samples that are correct are actually having a length that is matching with the GRPO one. But for incorrect solutions, here, the corrected policy is having an average length that's much lower than the ones from GRPO. So that's the bottom right charts. And that is actually making-- so this adjustment is actually making the intended consequence.

**中文**

如果再深入看看，正确样本的长度实际上与 GRPO 的相当。但对于错误解答，这里经过修正的策略所产生的平均长度远低于 GRPO。也就是右下角的图。这实际上产生了——这个调整实际上产生了预期的效果。

### [1:26:51](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=5211s) · b000149

**English**

So that's one very important--I think very important-- one important modification that people typically apply. And I'm looking at the time. In one minute, I will just tell you about some other modifications that people do. So there is a modification with respect to the standard deviation that is within the advantage formula that's biases towards in terms of the difficulty of the problem.

**中文**

所以这是一个非常重要——我觉得非常重要——一个大家通常会采用的重要修改。我看一下时间。接下来一分钟里，我会简单讲讲大家做的其他一些修改。有一种修改针对 advantage 公式里的标准差（standard deviation），它会在题目难度方面产生偏差。

### [1:27:26](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=5246s) · b000150

**English**

Because if let's suppose you have a very hard problem, most of your completions will be, let's say, failures. And so your standard deviation will not be super large. So this can cause problems. And then there is another modification that people typically also consider, which is having different epsilons. And if you remember that epsilon influences how much you're able to change the policy from one iteration to another.

**中文**

因为假设你有一道很难的题，大多数 completions 可能都会失败。因此，标准差不会特别大。这可能造成问题。还有另一种人们通常也会考虑的修改，就是使用不同的 epsilon。如果你们还记得，epsilon 会影响从一次迭代到下一次迭代时，策略能够改变多少。

### [1:28:03](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=5283s) · b000151

**English**

And the idea here is that if the probability of your token is very low, it is kind of unfair to just give it a small epsilon to grow because this epsilon is multiplied. So I'm just going to write that down. And then it's going to be Shervine--where is this?

**中文**

这里的想法是，如果 token 的概率非常低，只给它一个很小的 epsilon 来增长，就有点不公平，因为这个 epsilon 是以乘法方式起作用的。我把它写下来。然后就交给 Shervine——这个在哪儿？

### [1:28:30](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=5310s) · b000152

**English**

So we actually want the ratio of pi over pi all to be roughly in between those bounds roughly. So in other words, it's 1 plus epsilon times pi of old. So if this one is very low, you cannot really change your value too much.

**中文**

我们实际上希望 pi 除以 pi all \[字幕疑误，可能指 pi old\] 的比值大致处于这些边界之间，大致如此。换句话说，就是 1 加 epsilon，再乘以旧的 pi。如果这一项很低，你就无法让数值改变太多。

### [1:29:02](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=5342s) · b000153

**English**

And you don't want to have an epsilon that's too high because you don't want big probabilities to suddenly go to 0. So you want to introduce an asymmetry between the lower and the upper bounds. So this was a lot. Any questions on this? We're running short on time. We're going to have some time after the lecture in case you have any questions. And with that, I'm going to give it to Shervine.

**中文**

而你又不希望 epsilon 太高，因为你不希望很大的概率突然变成 0。所以你要让下界和上界之间存在不对称。这部分内容很多。对此有什么问题吗？我们时间不多了。课后还会有一些时间，大家有问题可以问。那么，我把时间交给 Shervine。

### [1:29:40](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=5380s) · b000154

**English**

Thank you, Afshine, for covering all the hard parts. Now it's going to be a bit easier because we're going to see how all of this comes together. And in particular, we're going to focus at the DeepSeek papers and exactly how they used all these techniques that Afshine covered into building these reasoning models. So what we saw at previous lectures, what, quote unquote, traditional LLMs. So you started from a pre-trained base model where you did a next token prediction on a bunch of texts of the internet.

**中文**

谢谢 Afshine 讲完了所有难的部分。接下来会稍微容易一点，因为我们会看看所有这些内容如何结合起来。具体来说，我们会重点看 DeepSeek 的论文，以及他们究竟如何使用 Afshine 讲过的这些技术来构建推理模型。我们在前几讲中看到的，是所谓的“传统”LLMs。你从一个预训练的基础模型开始，在大量互联网文本上进行下一个 token 预测（next token prediction）。

### [1:30:17](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=5417s) · b000155

**English**

And then out of this, you proceeded to do your alignments, which was composed of SFT and then RL. So not the reasoning style RL, but the regular one. And then the SFT was instruction tuning. And we're going to see how these newer models are being trained. And I think the example of the DeepSeek R1 paper is a great one because they go into multiple stages. First, into showing how powerful can the RL stage be if you apply the verifiable rewards that Afshine mentioned.

**中文**

然后在此基础上，继续进行对齐（alignment），其中包括监督微调（supervised fine-tuning，SFT），再接着是 RL。这里不是推理式的 RL，而是常规的 RL。其中 SFT 就是指令微调（instruction tuning）。我们会看看这些较新的模型是如何训练的。我觉得 DeepSeek R1 论文是一个很好的例子，因为他们分了多个阶段。首先展示，如果应用 Afshine 提到的可验证奖励，RL 阶段可以有多强大。

### [1:30:57](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=5457s) · b000156

**English**

And then based on the observations of the performance that you get out of it, how to devise a full pipeline of getting a super powerful model that they call R1. So, respectively, a proof of concept and then a full reasoning model. Does that sound good? OK, great. So now let's start with the recipe that DeepSeek folks use for the R1-Zero model.

**中文**

然后，根据观察到的性能，设计一套完整的流水线（pipeline），得到一个他们称为 R1 的超级强大的模型。也就是分别做一个概念验证（proof of concept），再做一个完整的推理模型。这样可以吗？好，很好。现在就从 DeepSeek 团队用于 R1-Zero 模型的方案开始。

### [1:31:28](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=5488s) · b000157

**English**

So they first started with a pre-trained model, trained on next token prediction on the latest architectures with all the bells and whistles. So you recall from previous lectures, we talked about a mixture of experts. So they have this, and they reuse a trick called multi-latent attention, MLA, that they had introduced in DeepSeek V2. And we had talked about it as well.

**中文**

他们首先从一个预训练模型开始，这个模型采用最新的架构，配备各种功能，通过 next token prediction 进行训练。回想前几讲，我们讨论过混合专家（mixture of experts）。他们采用了这个架构，还复用了一个叫 multi-latent attention、MLA \[字幕疑误，可能指 Multi-head Latent Attention\] 的技巧，这是他们在 DeepSeek V2 中引入的。我们也讨论过它。

### [1:32:01](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=5521s) · b000158

**English**

You can see, in their architecture, they use a pre norm in their transformer blocks. So they have a typical Bayes LLM. So they perform next token prediction on it. And then this is where the fun starts. So instead of going ahead with an alignment strategy that consists of SFT, they just start with this pre-trained model just trained on next token prediction. And it hasn't seen any supervision so far.

**中文**

你们可以看到，在他们的架构中，Transformer 块使用了前置归一化（pre norm）。所以他们有一个典型的 Bayes LLM \[字幕疑误，可能指 base LLM\]。他们对它进行 next token prediction。然后，有趣的部分就开始了。他们没有继续采用包含 SFT 的对齐策略，而是直接从这个仅通过 next token prediction 训练的预训练模型开始。到这时，它还没有接受过任何监督。

### [1:32:32](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=5552s) · b000159

**English**

And they apply the technique that Afshine just mentioned on reasoning data. So they look at rewards. And all they incentivize the model to do is to increase the rewards based on the outputs, like input answer that the model gives, as well as formatting. So if you have your think tokens that Afshine mentioned, then the reward on the formatting side would be given.

**中文**

他们在推理数据上应用了 Afshine 刚才提到的技术。他们关注奖励。他们对模型的全部激励，就是根据输出，比如模型给出的输入答案，以及格式，来提高奖励。如果你有 Afshine 提到的 think tokens，那么就会获得格式方面的奖励。

### [1:33:09](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=5589s) · b000160

**English**

And the paper gives exactly the templates over which they trained the model. So it's a very simple one. You have the first sentences that set up the stage that say, hey, you're discussing with the user, you're an assistant. And then the reward that I mentioned regarding formatting is explained in plain text. So it says, whatever you want to think about, just do it, but put it into think boxes.

**中文**

论文给出了他们用于训练模型的确切模板。这个模板非常简单。开头几句话设定场景，说，嘿，你正在和用户讨论，你是一个助手。然后用普通文本解释我刚才提到的格式奖励。它说，你想思考什么就尽管思考，但要把它放进 think 框里。

### [1:33:42](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=5622s) · b000161

**English**

And then once you're ready to give your answer, you should wrap it under like an answer--basically your answer blocks. And what you see here in red is what you replace by the sample prompts. And then at the end, you give the opportunity to the model to respond. Does that make sense? OK, great.

**中文**

当你准备好给出答案时，应该把它包在类似 answer 的——基本上就是你的 answer 块里。这里红色的内容，就是要用示例 prompts 替换的部分。最后，给模型一个回应的机会。这样能理解吗？好，很好。

### [1:34:13](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=5653s) · b000162

**English**

And I'm going to show you, again, a graph that Afshine had shown. So it was done on R1-Zero where they said that without any prior supervision, just having these as a reward increases scores on reasoning based benchmarks. So this one I think is on AIM. This like math one. And you see that the accuracy improves over time. And you might think, all is solved, it's great, no SFT, and we already have the best performance possible.

**中文**

我会再给大家看一张 Afshine 展示过的图。这是在 R1-Zero 上做的实验，他们表示，不需要任何先前的监督，只用这些作为奖励，就能提高基于推理的基准测试（benchmarks）分数。我记得这个是在 AIM \[字幕疑误，可能指 AIME\] 上，是那个数学测试。你会看到准确率随时间提高。你可能会想，一切都解决了，太好了，不需要 SFT，我们就已经达到了可能的最佳性能。

### [1:34:48](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=5688s) · b000163

**English**

Well, not so easy, because the authors, when they looked at the reasoning chains, they saw some issues with it of two kinds. So first, when the model was thinking about--was emitting distinct tokens, sometimes it would mix languages. And you had also syntax issues. And you could hypothesize that this might be the case because you haven't really seen any strong supervision just before that.

**中文**

但事情没那么简单，因为作者查看推理链时，发现了两类问题。首先，当模型在思考——在输出 distinct tokens \[字幕疑误，可能指 think tokens\] 时，有时会混用语言。还存在语法问题。你可以猜测，这可能是因为在此之前，它没有真正接受过任何强监督。

### [1:35:20](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=5720s) · b000164

**English**

And you give the opportunity to the model to optimize anything it wants, but it doesn't really have, as a background, a strong supervision signal to anchor on. So this is one key challenge that we're going to see together, how they try to resolve it. Does the R1-Zero process make sense? Awesome.

**中文**

你给模型机会，让它优化任何它想优化的东西，但它实际上没有一个强监督信号作为背景依托。这是一个关键挑战，我们会一起看看他们如何尝试解决它。R1-Zero 的流程能理解吗？太好了。

### [1:35:51](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=5751s) · b000165

**English**

So now that we have seen what R1-Zero tried to prove, the fact that with RL only, you can get reasoning level performance, now we're going to see how to adjust the challenges that we have seen into a full pipeline. So that one, they call it R1. And they start from the same basis. So they start from a V3 base, which is the pre-trained model that's DeepSeek had trained during their V3 paper.

**中文**

现在我们已经看到了 R1-Zero 想证明什么，也就是仅用 RL 就能获得推理层面的性能，接下来看看如何针对我们看到的挑战进行调整，形成一套完整的 pipeline。他们把它叫作 R1。他们从同样的基础开始，也就是从 V3 base 开始，这是 DeepSeek 在 V3 论文工作期间训练的预训练模型。

### [1:36:22](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=5782s) · b000166

**English**

So it was the non-reasoning version of this model. So they start from it. And then instead of starting directly to doing the RL stage that we have discussed, they try to align it in a way that will nicely try to alleviate the issues we have seen. So it starts from what they called as cold start data. They generated CoTs.

**中文**

这是该模型的非推理版本。他们从它开始。然后，他们没有直接进入我们讨论过的 RL 阶段，而是尝试以一种能够较好缓解上述问题的方式对它进行对齐。首先使用他们所谓的冷启动数据（cold start data）。他们生成了思维链（chains of thought，CoTs）。

### [1:36:57](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=5817s) · b000167

**English**

during the R1-Zero stage. And these CoTs sometimes had issues. So they used humans to rewrite some of these so that all these CoTs are compliant when it comes to formatting language consistency. And then they used these pairs, prompts and then rewritten prompts, as data to train SFT on it. And I think there was no number given on the number of samples given to that stage.

**中文**

这些 CoTs 是在 R1-Zero 阶段生成的，而且有时存在问题。因此，他们让人工重写其中一些，使这些 CoTs 在格式和语言一致性方面都符合要求。然后，他们使用这些配对，也就是 prompts 和重写后的 prompts \[字幕疑误，可能指重写后的回答或 CoTs\]，作为数据来进行 SFT。我记得没有给出这一阶段所用样本的数量。

### [1:37:33](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=5853s) · b000168

**English**

But from the wording of the paper, it could have been several orders of magnitude less than some of the other stages that we have seen. So potentially in the \[INAUDIBLE\] case of input output pairs. So now that we have this stage ready, they continued with the RL stage that R1 0 would do. And then we're going to explore the reward function that they used.

**中文**

但从论文的措辞来看，它可能比我们看到的其他一些阶段少几个数量级。所以输入输出对的数量可能在 \[听不清\] 的情况。这个阶段准备好之后，他们继续执行 R1 0 所进行的 RL 阶段。接下来我们会探讨他们使用的奖励函数（reward function）。

### [1:38:04](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=5884s) · b000169

**English**

So not only we have these verifiable reward based on the response of the reasoning model output that we wanted to have, but also we have the formatting reward. And there is something new that they introduced as well to counter the effects of having poor readability in their thoughts. There was something called a language consistency reward where they use a very simple heuristic to assess whether the model indeed doesn't mix languages.

**中文**

我们不仅有基于推理模型输出的、我们所希望得到的回答的可验证奖励，还有格式奖励。他们还引入了一个新东西，用来应对思考内容可读性差的问题。它叫语言一致性奖励（language consistency reward），他们用一个非常简单的启发式方法（heuristic）来评估模型是否确实没有混用语言。

### [1:38:43](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=5923s) · b000170

**English**

So I believe it was the ratio of the tokens in the target language in the outputted chain. So they just put that in order to maximize the amount of correct language tokens.

**中文**

我记得它是输出思维链中目标语言 tokens 的比例。他们加入这一项，是为了最大化正确语言的 tokens 数量。

### [1:39:00](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=5940s) · b000171

**English**

Great. And after this first pass of RL, they continued on with SFT with a very interesting strategy. So they do it as a larger scale than the cold start one. And now they mix both reasoning and non-reasoning data in order to make the model useful to the span of cases that you as a user might solicitate the model for. And regarding non-reasoning data, they recycled some of the data that was used for their non-reasoning version of the model for V3.

**中文**

很好。在第一轮 RL 之后，他们用一个非常有意思的策略继续做 SFT。这次的规模比冷启动阶段更大。现在他们把推理数据和非推理数据混合起来，让模型能够处理用户可能请求它完成的各种场景。对于非推理数据，他们复用了一部分曾用于 V3 非推理版本模型的数据。

### [1:39:42](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=5982s) · b000172

**English**

So about 200k pairs. And it covers the domains that we have mentioned during the instruction tuning lecture. So like a broad array of topics. And then what they did is that they added to it a lot of pairs that are directed towards reasoning. So the ratio was 3 to 1. And then the reasoning ones were generating with a method called rejection sampling.

**中文**

大约有 200k 对数据。它覆盖了我们在 instruction tuning 那一讲中提到的领域，也就是很广泛的主题。然后，他们又加入了大量面向推理的数据对。比例是 3 比 1。其中，推理数据是用一种叫拒绝采样（rejection sampling）的方法生成的。

### [1:40:13](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=6013s) · b000173

**English**

So what they did is that they took some prompts covering these reasoning-based fields, and they used the model that had been trained so far to generate a response. And then based on the output and with some judge, they would keep some answers and reject others such that the resulting data sets would be of very high quality. So this is what they call by rejection sampling.

**中文**

他们选取了一些覆盖这些推理领域的 prompts，并使用训练到当前阶段的模型生成回复。然后，根据输出，并借助某种评判者（judge），保留一些答案，拒绝另一些答案，让最终得到的数据集质量非常高。这就是他们所说的 rejection sampling。

### [1:40:44](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=6044s) · b000174

**English**

It's just the fact of filtering out any answers that are not perfect. And the reason why I guess they did it automatically with some LLM judges and so on is given the scale of the data--and these were heuristics that worked pretty nice on that--you had a question? No? So once they were done with that, they went on to a last stage that was one that might make you think about the ones that occur in non-reasoning model training pipelines.

**中文**

也就是把所有不完美的答案过滤掉。我想，他们使用一些 LLM 评判者（LLM judges）等来自动完成这件事，是考虑到数据规模——而这些启发式方法在这方面效果相当不错——你有问题吗？没有？完成这些之后，他们进入最后一个阶段，这个阶段可能会让你想起非推理模型训练 pipeline 中的那些阶段。

### [1:41:30](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=6090s) · b000175

**English**

So they mix this time not only reasoning data, but also non-reasoning ones. So for the reasoning data, same kind of reward as we have seen. But on the non-reasoning one, you try to align the model on characteristics that make an LLM a helpful assistant and a harmless one. So you have this helpfulness and harmlessness components of that part of the reward.

**中文**

这次他们不仅混合了推理数据，也混合了非推理数据。对于推理数据，使用与我们见过的相同类型的奖励。但对于非推理数据，会尝试让模型对齐那些使 LLM 成为有帮助且无害的助手的特征。因此，这部分奖励包含有帮助性（helpfulness）和无害性（harmlessness）两个组成部分。

### [1:42:01](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=6121s) · b000176

**English**

And the harmlessness was a reward that was applied on the whole tokens that were outputted. So not just the output because you want the chain of thoughts in the think section of the answer to be harmless indeed. And then the helpfulness one was more focused on what you saw at the user level. OK, great. And just to give some idea of the results they got, so first, you notice that

**中文**

无害性奖励应用于所有输出的 tokens，而不只是输出答案，因为你确实希望答案中 think 部分的思维链也是无害的。而有帮助性奖励则更关注用户层面看到的内容。好，很好。为了让大家对他们得到的结果有个概念，首先，你会注意到，

### [1:42:40](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=6160s) · b000177

**English**

on reasoning-based benchmarks you have two clusters of results that appear. You have all these non reasoning based models that have some performance. And then the reasoning-based ones have unsurprisingly a performance that is much higher. And then the second thing that we observe out of these results is that R1 was pretty competitive with respect to closed source models that claim to be reasoning-based.

**中文**

在基于推理的 benchmarks 上，会出现两簇结果。所有这些非推理模型都有一定的性能。而推理模型的性能要高得多，这并不令人意外。我们从这些结果中观察到的第二点是，相比那些声称基于推理的闭源模型，R1 相当有竞争力。

### [1:43:10](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=6190s) · b000178

**English**

And it was a pretty interesting moments, as Afshine had mentioned, to reproduce such a level of performance. OK, great. So I want to finish this lecture on an interesting note of let's say you don't have a 600B MOE at your disposal. Let's say you have a smaller model, but you want to have the capabilities of these large reasoning model.

**中文**

正如 Afshine 提到的，能够复现这样一个性能水平，是一个相当有意思的时刻。好，很好。我想用一个有趣的话题结束这节课：假设你手头没有一个 600B MOE。假设你有一个较小的模型，但你想让它拥有这些大型推理模型的能力。

### [1:43:43](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=6223s) · b000179

**English**

How would you go about it? So I just want to give you a reminder of how we had dealt with this topic a few lectures ago when we talked about distillation. So at that time, we were just talking about pre-training and an instruction tuning where the data we were dealing with was fixed. So for example, for next token prediction, you know the text you want the model to fit on. For SFT, you have fixed pairs. You know exactly what you want to learn.

**中文**

你会怎么做？我想提醒大家，几讲之前讨论蒸馏（distillation）时，我们是如何处理这个问题的。那时我们只是在讨论预训练（pre-training）和 instruction tuning，我们处理的数据是固定的。比如，对于 next token prediction，你知道希望模型拟合哪些文本。对于 SFT，你有固定的数据对。你确切知道想要学习什么。

### [1:44:14](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=6254s) · b000180

**English**

And what you did was look for each next token prediction at the output probability distribution of a teacher model. And on your student model, instead of fitting a hard label of the next token, you fit it instead the whole probability distribution of the teacher model in order to distill the knowledge of that teacher model into the student model.

**中文**

当时的做法是，对于每一次 next token prediction，查看教师模型（teacher model）的输出概率分布。然后对于学生模型（student model），不是去拟合下一个 token 的硬标签（hard label），而是去拟合教师模型的整个概率分布，从而把教师模型的知识蒸馏到学生模型中。

### [1:44:44](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=6284s) · b000181

**English**

You all remember that? Yeah? So now how could you go ahead with this in this case? So here, as you have seen, we don't necessarily have SFT pairs based on reasoning out of the box. So if you want to distill the knowledge of a teacher model here, the authors have gone through an interesting route that is still called distillation, but it's another flavor of it. So we use the teacher model here, R1, to generate some sample responses including thinking tokens.

**中文**

大家都还记得吗？记得？那么，在这种情况下，该如何进行呢？正如你们看到的，我们不一定有现成的基于推理的 SFT 数据对。因此，如果想在这里蒸馏教师模型的知识，作者采取了一条很有意思的路线，它仍然叫 distillation，但属于另一种形式。这里使用教师模型 R1 生成一些包含思考 tokens 的示例回复。

### [1:45:25](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=6325s) · b000182

**English**

So this is something that is done offline. And then in a second stage, you run this SFT and fit a smaller model on your distilled model, which is typically much less weights than the teacher one. So instead of fitting a probability distribution over the next token, you just fit the entire sequence. You just try to predict the same sequence of tokens that the teacher has outputted.

**中文**

这一步是离线完成的。然后在第二阶段，你进行 SFT，在你的蒸馏模型上拟合一个较小的模型 \[原文表述不清\]，它的权重数量通常比教师模型少得多。因此，你不是去拟合下一个 token 的概率分布，而是拟合整个序列。你只是尝试预测教师模型输出的同一个 token 序列。

### [1:45:59](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=6359s) · b000183

**English**

Does this framing of distillation here make sense? Yeah? Awesome. And I'm going to conclude here by looking at the results. So you can see that the results, once again, are very competitive with closed source alternatives that claim to be a smaller version of a reasoning model. So for example, o1-mini, you can see that the numbers here are competitive with respect to that. And then you could also wonder, but why did you go through the trouble of just distilling when you could just do the same RL techniques.

**中文**

这里这种 distillation 的表述能理解吗？可以？太好了。最后，我们来看看结果。你们可以看到，这些结果同样非常有竞争力，可以媲美那些声称是较小版本推理模型的闭源替代方案。比如 o1-mini，你可以看到这里的数值与它相比很有竞争力。然后你也可能会想，既然可以直接采用同样的 RL 技术，为什么还要费劲去做 distillation 呢？

### [1:46:41](https://www.youtube.com/watch?v=k5Fh-UgTuCo&t=6401s) · b000184

**English**

Well, actually, the authors have seen that at a smaller size level, distilling the knowledge is more efficient in terms of performance than directly learning from scratch. All good? And with that, have a great weekend.

**中文**

实际上，作者发现，在较小的模型规模下，从性能角度来看，蒸馏知识比直接从头学习更有效。都理解了吗？那么，祝大家周末愉快。
