# Stanford CME295 Transformers &amp; LLMs \| Autumn 2025 \| Lecture 7 - Agentic LLMs

_Bilingual transcript · 双语讲稿_

- Channel: Stanford Online
- Source: [YouTube](https://www.youtube.com/watch?v=h-7S6HNq0Vg)
- Duration: 1:49:22
- Caption source: manual
- Status: complete
- Chinese translation: 218/218
- Translation provider: codex
- Generated: 2026-09-29T16:03:01+00:00

## Transcript · 讲稿

### [00:05](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=5s) · b000001

**English**

Hello, everyone. And welcome to lecture 7 of CME 295. So today, we're going to focus on practical techniques to let our LLM interact with the outside world with other systems. Because up until now, our LLM was purely on its own. We've trained it. We've seen how it can reason on problem math, coding math, coding problems.

**中文**

大家好，欢迎来到 CME 295 第 7 讲。今天，我们将重点讨论一些实用技术，让我们的大语言模型（LLM）能够与外部世界、与其他系统交互。因为到目前为止，我们的 LLM 都是独立运行的。我们训练了它，也看到了它如何对问题、数学、编程数学、编程问题进行推理。

### [00:38](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=38s) · b000002

**English**

And now, what we want to do is to use our LLM in the context of other systems. So today's class, we'll focus on RAG, that you may have heard, tool calling, and agents. But before we start, as usual, I'm going to recap what we did last time. So if you remember, last time, we focused on reasoning models. And we saw the differences between reasoning model and what we call the vanilla LLM.

**中文**

现在，我们想要把 LLM 放到其他系统的环境中使用。因此，今天的课程将重点介绍你们可能听说过的 RAG、工具调用（tool calling）和智能体（agents）。不过，在开始之前，和往常一样，我先回顾一下上次的内容。如果你们还记得，上次我们重点讲了推理模型（reasoning models），也看到了推理模型与我们所说的普通 LLM（vanilla LLM）之间的区别。

### [01:14](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=74s) · b000003

**English**

And in particular, up until the lecture before last lecture, what we saw was we fed a prompt to the LLM, and it gave us directly a response. But what we saw last time was that if we let the LLM reason before outputting the response, then we can gain some performance when it comes to reasoning tasks, such as math and coding. And so, in particular, reasoning models, what they do is they take a prompt as input, and then what they output is both a reasoning chain, which is typically hidden from the user, and then a response.

**中文**

具体来说，直到上上讲，我们看到的都是向 LLM 输入一个提示词（prompt），它就直接给出回答。但上次我们看到，如果让 LLM 在输出回答之前先进行推理，那么在数学和编程等推理任务上，就能获得一些性能提升。具体来说，推理模型接收一个 prompt 作为输入，然后既输出一条通常对用户隐藏的推理链（reasoning chain），又输出一个回答。

### [02:02](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=122s) · b000004

**English**

So with that, we saw how we could train a model to be more of a reasoning model. And in particular, we saw a core RL algorithm called GRPO, which stands for Group Relative Policy Optimization. And we saw that this algorithm had some differences compared to the ones that we saw previously. And in particular, one notable aspect is that it does not have--it does not train a value function.

**中文**

由此，我们看了如何训练模型，让它更像一个推理模型。具体来说，我们介绍了一种核心的强化学习（RL）算法，叫作 GRPO，全称是组相对策略优化（Group Relative Policy Optimization）。我们看到，这个算法与之前介绍的那些算法有一些区别。其中一个值得注意的方面是，它没有——它不训练价值函数（value function）。

### [02:37](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=157s) · b000005

**English**

So here, this illustration shows a little bit how GRPO is trained. So it takes a query as input. And then it computes an advantage for each output by computing the rewards for different completions of a same prompt. And then computing a quantity, which is the advantage, that is relative to the other rewards of that group of completions.

**中文**

这里的示意图大致展示了 GRPO 是如何训练的。它接收一个查询（query）作为输入，然后计算同一个 prompt 的不同补全结果（completions）的奖励，并据此计算每个输出的优势（advantage）。接着计算的这个量，也就是 advantage，是相对于这一组补全结果中其他奖励而言的。

### [03:09](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=189s) · b000006

**English**

And then we saw that if we applied GRPO with carefully chosen rewards, which is one, rewarding the model for outputting a reasoning chain, and then second, rewarding the model for producing a good response. What we saw is that as the RL training progresses, we have an improvement of the model on these reasoning tasks.

**中文**

然后我们看到，如果应用 GRPO，并仔细选择奖励：第一，奖励模型输出推理链；第二，奖励模型生成好的回答。我们看到，随着 RL 训练推进，模型在这些推理任务上的表现有所提高。

### [03:40](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=220s) · b000007

**English**

And so we saw one of the tasks being math problems. So here on the left graph, you see the evolution of the performance of the model on the aim data set, which is a challenging math problem. And we saw that, but we also saw that the model kept on outputting responses that were longer and longer.

**中文**

我们看到，其中一项任务是数学题。在左边的图中，你们可以看到模型在 aim \[字幕疑误，可能指 AIME\] 数据集上的性能变化，这是一个有挑战性的数学问题。我们看到了这一点，同时也看到模型不断输出越来越长的回答。

### [04:10](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=250s) · b000008

**English**

And in particular, we saw that even though towards the end of the graph above, that the performance was plateauing. We saw that the output length was still increasing. So then what we did was go back to the loss formulation that is used by GRPO and realize that there is a term that makes the contribution of a token different, if it is in a short response or a long response.

**中文**

具体来说，我们看到，尽管上方图表接近末尾时性能已经趋于平稳，输出长度仍然在增加。于是，我们回头查看了 GRPO 使用的损失函数表达式（loss formulation），发现其中有一项会让一个 token 的贡献因它处于短回答还是长回答中而有所不同。

### [04:49](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=289s) · b000009

**English**

So this is a phenomenon called length bias. And we saw some mitigation strategies that were explored by some papers that came out in the past few months. So one was DAPO, which had a normalization factor that was not dependent on where the token was located and which sentence it was located. And the other one was this paper called "GRPO Done Right," which actually just removed the normalization term.

**中文**

这种现象叫作长度偏差（length bias）。我们看了过去几个月发表的一些论文所探索的缓解策略。一种是 DAPO，它使用的归一化因子（normalization factor）不依赖于 token 所在的位置，也不依赖于它位于哪个句子中。另一种是名为“GRPO Done Right”的论文，它实际上直接去掉了归一化项。

### [05:27](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=327s) · b000010

**English**

All good on that? Cool. So this was last time. And last time, what we said right before starting the reasoning class was to enumerate the strengths and the weaknesses of vanilla LLMs. So last lecture was all about focusing on how we can improve the limited reasoning capabilities of vanilla LLMs. And in this lecture, what we will do is two things.

**中文**

这些都明白了吗？好。这就是上次的内容。上次，在开始讲推理之前，我们先列举了 vanilla LLMs 的优点和缺点。因此，上一讲主要聚焦于如何改善 vanilla LLMs 有限的推理能力。而在这一讲中，我们将做两件事。

### [06:01](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=361s) · b000011

**English**

So the first one is see how we can connect our LLM to the ever evolving knowledge base, and, in particular, see how we can have access to the latest information. And then the second one is how our LLM can help us perform actions. And we will see this with Shervine with things like tool calling and agentic workflows.

**中文**

第一，看看如何将 LLM 连接到不断演变的知识库（knowledge base），具体来说，就是如何获取最新信息。第二，看看 LLM 如何帮助我们执行操作。我们将和 Shervine 一起，通过 tool calling 和智能体工作流（agentic workflows）等内容来了解这一点。

### [06:33](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=393s) · b000012

**English**

Cool. So with that, let's start with the first one. And let's start with this method called RAG, that you may have heard. So let's suppose you have a model that you have trained. But the problem is that the pre-training data on which you have trained your model is, let's say, a month ago, let's suppose.

**中文**

好，那我们先从第一件事开始。先介绍一下你们可能听说过的 RAG 方法。假设你已经训练好了一个模型。但问题在于，训练这个模型所用的预训练数据（pre-training data），假设是一个月前的数据。

### [07:04](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=424s) · b000013

**English**

Now, let's suppose you want to prompt your model about the winner of the elections that happened a couple of weeks ago. Well, your model will not be able to respond to you, or it will output the incorrect answer because up until now, our LLM does not have any link to outside sources. It only relies on the knowledge that it has acquired during training. So the response that it will give us will only be based on the data that has been trained up until the cutoff, which is a month ago in this example.

**中文**

现在，假设你想向模型询问几周前举行的选举中谁获胜了。那么，模型将无法回答，或者会输出错误答案，因为到目前为止，我们的 LLM 与外部来源没有任何连接。它只依赖在训练过程中获得的知识。因此，它给出的回答只会基于截止日期之前用于训练的数据，在这个例子中就是一个月前。

### [07:45](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=465s) · b000014

**English**

And so we have this big limitation, which is our LLM only knows about things that it has been trained on. And you will see that all the models out there. So here, I have an example with OpenAI GPT-5 So if you look at their model cards, they always have these knowledge cutoff dates that is written somewhere. And in the case, for instance of GPT-5, the knowledge cutoff date is September 30, 2024, which means that if you ask it in a very naive way, anything that happened after that, the base model will not be able to answer you as is.

**中文**

所以我们有一个很大的限制，就是 LLM 只知道它训练过的内容。你会看到，市面上所有模型都是这样。这里我用 OpenAI GPT-5 举例。如果你查看它们的模型卡（model cards），总会在某处看到写明的知识截止日期（knowledge cutoff dates）。例如，GPT-5 的知识截止日期是 2024 年 9 月 30 日，这意味着，如果你以非常朴素的方式询问那之后发生的任何事情，基础模型（base model）本身将无法直接回答。

### [08:30](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=510s) · b000015

**English**

Well, you may tell me why not just continue training your model on data that happened after that? Well, the problem with that-- actually, there are several problems with this. So the first problem is that it's very tricky to change the knowledge of an LLM without causing regression on other things. So this is typically a task that people, they try to avoid doing.

**中文**

你可能会说，为什么不直接用那之后的数据继续训练模型呢？问题在于——其实，这里有几个问题。第一个问题是，要改变 LLM 的知识，同时不导致其他方面的能力退化，是非常棘手的。因此，这通常是人们会尽量避免做的一项任务。

### [09:01](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=541s) · b000016

**English**

And the second thing is it's not very practical, because you may very well have use cases that require you to fine tune this model. So let's suppose you have a use case one, you fine tune from this model. And then somehow you want to update the weights of your model to inject some knowledge. Well, you somehow will have to do that for all the use cases that you are doing, which basically adds a lot of overhead for you and just adds a lot of maintenance.

**中文**

第二，这不太实用，因为你的应用场景很可能要求你对这个模型进行微调（fine tune）。假设你有应用场景一，你基于这个模型进行微调。然后，你又想更新模型权重来注入一些知识。那么，你就得以某种方式对所有正在使用的应用场景都做这件事，这基本上会增加大量额外开销，也会增加大量维护工作。

### [09:37](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=577s) · b000017

**English**

So people, they typically prefer to not do additional training to inject knowledge. So one idea can be to somehow take your prompt and just add anything that happens after the cutoff date as a way for your model to just know what happened. Well, the problem with that naive approach is that as you know context length is limited.

**中文**

因此，人们通常更倾向于不通过额外训练来注入知识。一个想法是，拿到 prompt 后，把截止日期之后发生的所有事情都加进去，让模型知道发生了什么。但这种朴素方法的问题在于，正如你们所知，上下文长度（context length）是有限的。

### [10:12](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=612s) · b000018

**English**

And so typically, models have on the order of magnitude of hundreds of thousands of tokens in context length. Do you know what that is roughly--what it is roughly equal to?

**中文**

通常，模型的 context length 在数十万 token 这个数量级。你们知道这大致——大致相当于多少内容吗？

### [10:34](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=634s) · b000019

**English**

Yes. So one token is equal to four characters. So using this rough approximation, hundreds of thousands of tokens is roughly like hundreds of pages, something like a very big book.

**中文**

对，一个 token 相当于四个字符。因此，按照这个粗略估算，数十万 token 大致相当于几百页，也就是一本很厚的书。

### [10:50](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=650s) · b000020

**English**

It's big, but it's not enough for us to go in that very naive route. So again, going back to GPT-5, so if you go to the model card, you have the knowledge cutoff date, which is September 2024. You also have the context window. And in this case, it's 400,000 tokens. So let's suppose actually, context is not a problem. It's actually unlimited.

**中文**

这很大，但还不足以让我们采取那种非常朴素的做法。还是回到 GPT-5，如果你查看模型卡，会看到知识截止日期是 2024 年 9 月。还有上下文窗口（context window），这里是 400,000 token。现在，假设上下文其实不是问题，它实际上是无限的。

### [11:21](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=681s) · b000021

**English**

Let's imagine we actually put everything in the context. Well, the problem then is that people noticed that if you feed a lot of irrelevant information to your LLM, the performance of the LLM will actually degrade. Meaning, that if for instance, you ask it about, I guess, who was the winner of the last elections? And then you feed it a bunch of information that are not relevant, your LLM will tend to be confused.

**中文**

设想我们真的把所有东西都放进上下文里。那么，问题在于，人们注意到，如果向 LLM 输入大量无关信息，LLM 的性能反而会下降。也就是说，例如，你问它，我想，比如上次选举谁获胜了？然后给它输入一大堆不相关的信息，LLM 就容易感到困惑。

### [11:58](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=718s) · b000022

**English**

And so people have run these tests. That's called the needle in a haystack test, where the idea is you give a big prompt to your LLM, which is your haystack, and you place a fact in the prompt. And you ask your model what that fact was. So the idea is for your LLM to know, I guess, among that huge prompt, where is the relevant information, which is the needle.

**中文**

人们做过这样的测试，叫作大海捞针测试（needle in a haystack test）。其思路是，给 LLM 一个很长的 prompt，也就是你的“干草堆”，然后在 prompt 中放入一个事实，再问模型那个事实是什么。因此，其目的就是让 LLM 找出，我想，在那个巨大的 prompt 中，相关信息在哪里，也就是那根“针”在哪里。

### [12:37](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=757s) · b000023

**English**

And so when people have tried doing this for several length of prompts and tried different positions of where to put the facts, they have seen that the length of the prompt and the position at which you put the facts are both important. So here on the slide, we have a heat map that was performed for GPT-4, which was I guess one or two years ago.

**中文**

当人们尝试不同长度的 prompt，并把事实放在不同位置时，他们发现，prompt 的长度和事实放置的位置都很重要。这张幻灯片上是针对 GPT-4 测试得到的一张热力图（heat map），我想大概是一两年前的。

### [13:10](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=790s) · b000024

**English**

And what the person did was placed the fact at different places in the document. So this is document depth, and the x-axis is the length of your prompt. And what we saw was that for prompts that exceeded a certain amount of tokens, the LLM actually had trouble retrieving the correct piece of information. And in particular, it had trouble doing so when the fact was somewhere in the first half of the prompt.

**中文**

测试者把这个事实放在文档中的不同位置。因此，这里是文档深度（document depth），而 x 轴是 prompt 的长度。我们看到，当 prompt 超过一定数量的 token 时，LLM 实际上很难检索到正确的信息。尤其是当事实位于 prompt 前半部分的某个位置时，它很难做到这一点。

### [13:44](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=824s) · b000025

**English**

So this just tells us that, even if, let's say, our context length was unlimited, we would still have a problem by just going through that naive approach. So that's another reason. So now, let's suppose, context length is unlimited. Let's suppose the problem that I mentioned is not a problem. Well, the other problem is that you pay. So in particular, these calls, these LLM calls, they are per token.

**中文**

这说明，即使假设 context length 是无限的，直接采用这种朴素方法仍然会有问题。这是另一个原因。现在，假设 context length 是无限的，也假设我刚才提到的问题不存在。那么，另一个问题就是你要付费。具体来说，这些调用，这些 LLM 调用，是按 token 收费的。

### [14:20](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=860s) · b000026

**English**

So the bigger your input prompt, the more you will pay. So you have an incentive to not put too much in your prompt just from that standpoint. And so for instance, again, going back to GPT-5, order of magnitude is somewhere around $1 per million token. So I guess it's not that expensive, but it can add up, if you do that for all your prompts.

**中文**

所以，输入的 prompt 越大，你付的钱就越多。仅从这个角度出发，你就有理由不要往 prompt 里放太多内容。例如，还是回到 GPT-5，费用的数量级大约是每百万 token 1 美元。我想，这不算很贵，但如果所有 prompt 都这样做，费用就会累积起来。

### [14:50](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=890s) · b000027

**English**

So for all these reasons, I hope I convinced you that we need a more clever approach, where instead of putting all the new information all at once in the prompt, what we do is we only somehow find the relevant information and put that in the prompt. So that is the idea behind RAG. RAG stands for Retrieval Augmented Generation.

**中文**

出于所有这些原因，希望我已经说服你们，我们需要一种更聪明的方法：不是一次性把所有新信息都放进 prompt，而是设法只找到相关信息，再把它放进 prompt。这就是 RAG 背后的想法。RAG 的全称是检索增强生成（Retrieval Augmented Generation）。

### [15:22](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=922s) · b000028

**English**

And the idea here is to augment the prompt with relevant information. And here, I put relevant in bold. And this is the, I guess, the core part of this technique is how can we get only the relevant part in the prompt? So we'll see that in a second. So just at a very high level, so you have, let's say, a question as input. So in this case, who was the winner of, let's say, the local election?

**中文**

这里的思路是用相关信息来增强 prompt。我在这里把“相关”加粗了。我想，这项技术的核心就是：如何只把相关部分放进 prompt？我们马上会看到。从很高层次来看，假设你输入一个问题。在这个例子中，问题是，比如，地方选举的获胜者是谁？

### [15:56](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=956s) · b000029

**English**

The idea here is to somehow fetch the correct or the relevant piece of information and then augment that here in order to output your answer.

**中文**

这里的思路是设法获取正确或相关的信息，然后在这里用它进行增强，从而输出答案。

### [16:11](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=971s) · b000030

**English**

So that's the rough idea. So does this method make sense so far? Yeah. OK. Cool. So that is the idea behind RAG. And now, we're going to go into more details. So what I mentioned is the rough idea. And here, I just want to emphasize on the three main steps of RAG. So first one is you have your prompt, and you somehow want to retrieve a relevant piece of information that will help you in answering your prompt.

**中文**

这就是大致思路。到目前为止，这个方法能理解吗？能。好，很好。这就是 RAG 背后的想法。现在我们要进一步讨论细节。刚才讲的是大致思路，这里我想强调 RAG 的三个主要步骤。首先，你有一个 prompt，然后你想设法检索到一条相关信息，帮助你回答这个 prompt。

### [16:48](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=1008s) · b000031

**English**

So here, the first step is to retrieve relevant documents. And so you can think of your prompt as being one entity. And then you can have some other space, which maybe, I don't know, knowledge base, where all your documents live. And so the idea is to somehow fetch the relevant documents. So this is the retrieve step. The second step is once you have fetched the relevant information, you augment your prompt.

**中文**

这里，第一步是检索相关文档。你可以把 prompt 看作一个实体，然后还可以有另一个空间，比如，我不知道，一个存放所有文档的知识库。因此，思路就是设法获取相关文档。这就是检索（retrieve）步骤。第二步是在获取相关信息后，增强（augment）你的 prompt。

### [17:21](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=1041s) · b000032

**English**

So you take that retrieved info. You just put it in your prompt, and then ask the question. So in the local election example, it's as if I was saying, who is the winner of this election? And then I retrieve the relevant piece of information. And now, the prompt becomes, who is the winner of this election? And by the way, this election was held, blah, blah, blah. And this was the winner. And this is what we're feeding to our LLM.

**中文**

你拿到检索出的信息，把它放进 prompt，然后提出问题。以地方选举为例，就好像我在问：这次选举的获胜者是谁？然后，我检索到相关信息。现在，prompt 就变成了：这次选举的获胜者是谁？顺便说一下，这次选举举行于，诸如此类。这就是获胜者。这就是我们输入给 LLM 的内容。

### [17:53](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=1073s) · b000033

**English**

So in other words, we're giving the answer in the prompt. And the third step is to feed that prompt to the LLM to generate the response. Yeah?

**中文**

换句话说，我们在 prompt 中给出了答案。第三步是把这个 prompt 输入给 LLM，让它生成（generate）回答。嗯？

### [18:20](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=1100s) · b000034

**English**

Exactly. So the question is, you may very well somehow do a bad job at retrieval stage, so yes. So this is why the retrieval stage is so important. And we're going to focus on what we can do to make sure that one part does well.

**中文**

完全正确。问题是，你在检索阶段很可能做得不好，是的。因此，检索阶段才如此重要。我们将重点讨论如何确保这一部分做得好。

### [18:41](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=1121s) · b000035

**English**

We'll see how we can evaluate, I guess, our setup and different methods. But when we talk about RAG, we're mainly focusing on making the retrieval parts as good as it can. Cool. And I just want to emphasize once again on why it's called RAG. So you have retrieve, augment, generate--RAG.

**中文**

我们会看看如何评估我们的配置和不同方法。不过，谈到 RAG 时，我们主要关注的是尽可能把检索部分做好。好。我还想再强调一次，为什么它叫 RAG：检索、增强、生成——retrieve、augment、generate，RAG。

### [19:13](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=1153s) · b000036

**English**

Cool. And as you pointed out, the first step, which is the retrieval step is very important, which is why we'll spend a little bit of time over there. So I guess the first step is for us to somehow clean the set of documents that we may need. So I said, we may want to look into outside information, but we need to somehow sort that order that put that somewhere.

**中文**

好。正如你指出的，第一步，也就是检索步骤，非常重要，所以我们会在这里花一些时间。我想，第一步是设法清理我们可能需要的文档集合。我说过，我们可能想查看外部信息，但需要对这些信息进行某种整理、排序，再把它们放在某个地方。

### [19:48](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=1188s) · b000037

**English**

And this whole thing is usually called a knowledge base. So in order to form our knowledge base, what we do is typically collect the set of documents that are or may be useful. And once we do that, what we do is we divide them into, what we call, chunks. So a chunk is you can think of it as a subset of the document which has a given maximum length, which is are measured in number of tokens, which is typically on the order of hundreds of tokens.

**中文**

这一整套东西通常叫作知识库。为了构建知识库，我们通常会收集一组有用或可能有用的文档。完成后，我们会把它们划分成所谓的文本块（chunks）。你可以把一个 chunk 理解为文档的一个子集，它有给定的最大长度，以 token 数量衡量，通常在几百个 token 的数量级。

### [20:29](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=1229s) · b000038

**English**

And the idea here is whenever you hear retrieval, you should think about embeddings. And here, what we do is we compute embeddings corresponding to each of these chunks. Now, when you create your knowledge base, there are a few hyperparameters that you need to tweak. So the first one, obviously, is the size of the embedding. So typically, you would want a bigger size, if, let's say, your documents are maybe more nuanced, more complex.

**中文**

这里的思路是，每当听到检索，你就应该想到嵌入（embeddings）。在这里，我们会为每一个 chunk 计算对应的 embedding。创建知识库时，有几个超参数（hyperparameters）需要调整。第一个显然是 embedding 的维度。通常，如果你的文档可能更加细腻、更加复杂，你会希望维度更大。

### [21:07](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=1267s) · b000039

**English**

But then if you have a higher size, maybe it will take more space. Maybe you'll have more computation at inference time. So I guess it's a trade-off. You don't necessarily want too big of an embedding size. So here, typically, embedding sizes are on the order of thousands. So for instance, like 1,500 something like this. So then you have the chunk size. Chunk size is how big your little pieces here are.

**中文**

但如果维度更高，可能就会占用更多空间，在推理时也可能需要更多计算。所以我想，这是一个权衡。你不一定希望 embedding 的维度过大。这里，embedding 的维度通常在几千这个数量级，比如 1,500 左右。然后是 chunk 大小，也就是这里这些小片段有多大。

### [21:39](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=1299s) · b000040

**English**

So you don't want them to be too small, because, otherwise, the text may be out of context. You don't want it to be too large, because maybe the embedding will not represent, in a meaningful way, what is inside. So again, it's a trade-off. But typically, people they choose chunk size of around 500 tokens, like, on the order of hundreds of tokens. And then you also have a-- oh yeah. You have a question. Yeah?

**中文**

你不希望它们太小，否则文本可能会脱离上下文。你也不希望它们太大，因为 embedding 可能无法有意义地表示其中的内容。所以，这同样是一个权衡。不过，人们通常会选择大约 500 token 的 chunk 大小，也就是几百 token 这个数量级。然后还有一个——哦，对，你有问题。请说？

### [22:10](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=1330s) · b000041

**English**

So the question is, do you train an embedding model for this. So you have two choices, either you can use a pre-trained embedding model, which people typically do, or you can train your own. We will see that in a bit more detail in a few slides.

**中文**

问题是，你会为此训练一个 embedding 模型吗？你有两个选择：可以使用预训练的 embedding 模型，这也是人们通常的做法；也可以训练自己的模型。再过几张幻灯片，我们会稍微详细地介绍。

### [22:34](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=1354s) · b000042

**English**

So the question is, what is the purpose of the embedding model? So we will see this in a second. But long story short, it tries to represent chunks, such that it achieves your end goal, which is to fetch relevant documents. So we will see a little bit how they're trained. But this is the general idea.

**中文**

问题是，embedding 模型的作用是什么？我们马上会看到。简单来说，它试图表示这些 chunks，以实现你的最终目标，也就是获取相关文档。我们会稍微了解一下它们是如何训练的。这就是总体思路。

### [22:58](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=1378s) · b000043

**English**

Cool. So that's this. And then we have a third hyperparameter, which is how much overlap you want to have in between your chunks. So here, when you do the division, in a very naive way, you have everything be independent, no overlap in between. But typically, you have some part that is from the previous chunk that is relevant to understand the current chunk, which is why we want to have some overlap, which is why people, they typically also have that.

**中文**

好，这部分就是这样。然后还有第三个超参数，即你希望 chunks 之间有多少重叠。如果采用非常朴素的划分方式，所有片段都是相互独立的，彼此之间没有重叠。但通常，前一个 chunk 中的某些内容与理解当前 chunk 有关，所以我们希望有一些重叠，这也是人们通常会设置重叠的原因。

### [23:35](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=1415s) · b000044

**English**

So it's typically in the low hundreds of tokens.

**中文**

它通常是一百多个到几百个 token，处于几百这个数量级的较低范围。

### [23:41](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=1421s) · b000045

**English**

Cool. So let's suppose you have your knowledge base. Now, the question is, given a prompt, how can you retrieve relevant documents? And the answer to that is we typically proceed in two steps. So I'm not sure if any of you has a background in recommendation systems or search. Does any? Yeah. So the methods we're seeing here are very similar to that space.

**中文**

好。假设你已经有了知识库。现在的问题是，给定一个 prompt，如何检索相关文档？答案是，我们通常分两步进行。不知道你们有没有人有推荐系统（recommendation systems）或搜索方面的背景？有吗？有。这里介绍的方法与那个领域非常相似。

### [24:12](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=1452s) · b000046

**English**

So I guess people in the LLM community. They have borrowed ideas and just leveraged some techniques that we have over there. And this is typically, a setting that will also have for recommendation problems. So we have two stages. So the first stage is typically called candidate retrieval. And the goal here is to go from a set of many, many, many chunks, and filter it down to a much smaller set of potentially relevant candidates.

**中文**

我想，LLM 社区的人借鉴了一些想法，并利用了那个领域中的一些技术。这也是推荐问题中通常会出现的一种设置。我们有两个阶段。第一阶段通常叫作候选检索（candidate retrieval）。这里的目标是从非常、非常、非常多的 chunks 中，筛选出一个小得多、可能相关的候选集合。

### [24:49](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=1489s) · b000047

**English**

So during that stage, what we're trying to do is to somehow maximize recall, just do a rough operation, so that we get as many potentially relevant candidates as possible. And then we have a second stage, which is sometimes optional. But this stage is to really make sure we have the top documents being really the relevant ones. And this one is called ranking.

**中文**

在这个阶段，我们试图尽可能提高召回率（recall），只是进行一个粗略操作，以便获得尽可能多的潜在相关候选。然后是第二阶段，这一步有时是可选的。但这个阶段是为了真正确保排在最前面的文档确实是相关的。这个阶段叫作排序（ranking）。

### [25:21](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=1521s) · b000048

**English**

So the idea here is based on the list of potentially relevant documents, to really rank them in a way that really the relevant ones come at the top and so on. And typically, during that stage, we're going to use a model, a method that's going to be a bit more compute intensive because we have a much smaller set of candidates to rank compared to the first one.

**中文**

这里的思路是，根据可能相关的文档列表，对它们进行排序，让真正相关的文档排在最前面，依此类推。通常，在这个阶段，我们会使用一个计算量稍大的模型或方法，因为与第一阶段相比，需要排序的候选集合小得多。

### [25:52](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=1552s) · b000049

**English**

So going back to your question on how do we want our embeddings to be? So here, it will really impact the first stage. And we will see that in a second. But the second stage is also quite important.

**中文**

回到你刚才的问题，我们希望 embeddings 是什么样的？它主要影响第一阶段，我们马上会看到。不过，第二阶段也非常重要。

### [26:08](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=1568s) · b000050

**English**

Cool. So far so good? Is everyone clear with the two-stage approach? Yeah.

**中文**

好，到目前为止都明白吗？大家都清楚这个两阶段方法了吗？嗯。

### [26:27](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=1587s) · b000051

**English**

Very good question. So the question is, do we chunk things in a naive way, as in we just go with the number of tokens regardless of what happens? So it's a great question. And the answer is that we will see some extensions that will mitigate the problem of when you chunk it in a way that does not make sense in a naive way, you want to somehow put that into context. And we will see a method that does that. So in a few slides, we will see that.

**中文**

非常好的问题。问题是，我们是否以朴素的方式划分 chunks，也就是说，不管内容如何，只按 token 数量划分？这是个很好的问题。答案是，我们会介绍一些扩展方法，来缓解朴素划分导致片段不合理的问题，你希望设法为它补上上下文。我们会介绍一种能做到这一点的方法。再过几张幻灯片就会讲到。

### [26:57](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=1617s) · b000052

**English**

But I think your question is also a great question, because depending on the kind of document that we have, for instance, if we have, I don't know, like a JSON file or a markdown or depending on the file that you need to chunk, you also need to be aware of the structure that is within those files. So there is also some nuance there that we will not go into details, but I just want to call that out. But, yeah, great question. Any other questions?

**中文**

不过，我觉得你的问题也很好，因为这取决于文档类型。比如，如果我们有，我不知道，比如一个 JSON 文件或者 markdown，或者取决于你需要切分的文件，你还需要注意这些文件内部的结构。所以这里还有一些细微之处，我们不会详细展开，但我想特别指出这一点。是的，很好的问题。还有其他问题吗？

### [27:29](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=1649s) · b000053

**English**

OK. Cool. So now that we're clear on the two main stages of retrieval, we're going to focus on each one of these steps. So as I mentioned, the first step is candidate retrieval. So here, what we want is among that potentially huge knowledge base to somehow filter it down to, let's say, over 100 potentially relevant candidates.

**中文**

好，很好。现在我们已经清楚了检索的两个主要阶段，接下来分别讨论每一步。正如我提到的，第一步是 candidate retrieval。我们想从这个可能非常庞大的知识库中，设法筛选出，比如，100 多个可能相关的候选。

### [28:02](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=1682s) · b000054

**English**

So here, what we do is well, we will leverage the embeddings that I guess computed during the knowledge base initialization. And we will try to fetch potentially relevant candidates by doing a semantic similarity search. So do you recall how we compare embeddings?

**中文**

在这里，我们会利用知识库初始化时计算出的 embeddings，并通过语义相似度搜索（semantic similarity search）来获取可能相关的候选。你们还记得如何比较 embeddings 吗？

### [28:31](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=1711s) · b000055

**English**

Yes. So cosine similarity is typically one way one good way to compare embeddings. So the idea here is to represent our query with an embedding. We already have embeddings of all our chunks. So the idea here is to somehow find the most relevant chunks by doing this similarity search and filtering out the ones that come at the top.

**中文**

对，余弦相似度（cosine similarity）通常是一种比较 embeddings 的好方法。这里的思路是用一个 embedding 表示查询。我们已经拥有所有 chunks 的 embeddings，因此可以通过相似度搜索找到最相关的 chunks，并筛选出排在最前面的那些。

### [29:03](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=1743s) · b000056

**English**

So the idea here is you have your query, you have your chunk. both of them, you find an embedding. And then you perform a similarity operation, which is most of the time cosine similarity. And you obtain a similarity score. So the idea here is you just keep top, I don't 100, and you go with that. So I just want to call out that there is some complexity in that stage, because your knowledge base can potentially be huge.

**中文**

这里的思路是，你有查询，也有 chunk，为两者分别得到一个 embedding。然后进行相似度运算，大多数情况下是 cosine similarity，得到一个相似度分数。然后只保留前面，比如，我不知道，100 个，再继续处理。我想指出，这个阶段有一定的复杂性，因为你的知识库可能非常庞大。

### [29:40](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=1780s) · b000057

**English**

So what people do is typically use what we call approximate nearest neighbor methods. So you may have heard of some libraries that do that. So typically, this is something that will be relevant here. We're not going to go into details, but I just want to call that out. So here, the idea here is that when you build your knowledge base, you somehow partition the embeddings in a way that will avoid-- like make you avoid doing like just a naive linear search.

**中文**

人们通常会使用所谓的近似最近邻（approximate nearest neighbor）方法。你们可能听说过一些实现这类方法的库。这些通常会在这里派上用场。我们不会深入细节，但我想指出这一点。这里的思路是，在构建知识库时，以某种方式对 embeddings 进行分区，从而避免——就是让你避免直接进行朴素的线性搜索。

### [30:18](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=1818s) · b000058

**English**

So that's the idea. But you may see some techniques like ANN techniques, approximate nearest neighbor techniques. And these are typically happening here. So another thing that I want to point out is the name of the architecture that we typically use here that you may also hear. And for that, we need to recall that these embeddings, they're actually obtained by passing them through a model.

**中文**

这就是思路。你可能会看到一些技术，比如 ANN 技术，也就是 approximate nearest neighbor 技术。这些技术通常就在这里使用。我还想指出另一点，就是这里通常使用的架构名称，你们也可能听说过。为此，我们需要回忆一下，这些 embeddings 实际上是通过模型处理得到的。

### [30:50](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=1850s) · b000059

**English**

So typically encoder only. So you may hear the term BI encoder. And this one refers to the fact that we are passing the query through an encoder and then passing the chunk through an encoder. So both of them are independent. And we're comparing the embeddings.

**中文**

通常是仅编码器（encoder only）模型。你们可能会听到双编码器（BI encoder）这个术语。它指的是，我们把查询输入一个 encoder，再把 chunk 输入一个 encoder。两者相互独立，然后比较 embeddings。

### [31:16](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=1876s) · b000060

**English**

So this is another question I wanted to ask you. But I guess I didn't get the chance to. If you remember, I think lecture two or three, we had seen the BERT model. And so typically, you would have something like a BERT-like model that you would use to encode these documents. So going back to your question, how do you compute these embeddings? So there is a paper that I highly recommend reading.

**中文**

这也是我想问你们的另一个问题，但我想我还没来得及问。如果你们还记得，我想是在第二讲或第三讲，我们介绍过 BERT 模型。通常，你会使用类似 BERT 的模型来编码这些文档。回到你的问题，如何计算这些 embeddings？有一篇论文，我非常推荐阅读。

### [31:47](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=1907s) · b000061

**English**

Actually, that's called Sentence BERT. And so that paper explains--so it's, first of all, it's an extension of BERT, as the name suggests. And it's an extension that allows you to compute an embedding per, let's say, sequence for your query, for your document, that is tailored to be used for similarity search purposes.

**中文**

它叫作 Sentence BERT。这篇论文解释了——首先，正如名字所示，它是 BERT 的扩展。这个扩展让你能够为查询、为文档中的每个，比如，序列计算一个 embedding，并专门使它适用于相似度搜索。

### [32:17](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=1937s) · b000062

**English**

So the idea here is to have a loss function that will incentivize having a high cosine similarity for relevant entities and low cosine similarity for entities that are not relevant. So yeah, so feel free to check that paper out, if you know BERT, which I know right now, you do, it's quite easy to read. So highly recommend. So far so good? Yeah?

**中文**

这里的思路是，使用一个损失函数（loss function），鼓励相关实体之间具有较高的 cosine similarity，而不相关实体之间具有较低的 cosine similarity。对，欢迎看看这篇论文。如果你了解 BERT，我知道你们现在已经了解了，那么这篇论文读起来相当容易。非常推荐。到目前为止都明白吗？嗯？

### [32:48](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=1968s) · b000063

**English**

Yeah?

**中文**

嗯？

### [32:54](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=1974s) · b000064

**English**

So the question is, what is the default way to compute the similarity? So yes, it's cosine similarity. But again, you will see in different implementations that people can use other distances. And I would encourage you to think about how they relate to one another. So you will see, for instance, the L2 distance. But then if everything has a norm of 1, there's a lot of simplifications that can happen. So you may see some variants, but I would say they're all more or less cosine similarities.

**中文**

问题是，默认用什么方式计算相似度？对，就是 cosine similarity。不过，你会在不同实现中看到，人们也会使用其他距离。我鼓励你们思考这些距离之间的关系。比如，你会看到 L2 距离。但如果所有向量的范数都是 1，就会出现很多可以简化的地方。因此，你可能会看到一些变体，但我会说，它们或多或少都相当于 cosine similarity。

### [33:29](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=2009s) · b000065

**English**

Yeah, great question. Cool. So we're still at the candidate retrieval stage. And what we saw was one way of retrieving documents from a similarity--sorry from a semantic similarity standpoint. So by the way, what does semantic similarity mean? It means is finding documents or finding entities that have the same meaning or that are relevant, but in the way that we compute these embeddings, we're not enforcing any kind of keyword match, like when we retrieve documents in this way, it can very well be that the documents that are matched, they do not have any word in common, but they mean the same.

**中文**

对，很好的问题。好，我们仍然在 candidate retrieval 阶段。刚才看到的是从相似度——抱歉，从语义相似度的角度检索文档的一种方法。顺便问一下，语义相似度是什么意思？它意味着找到含义相同或相关的文档或实体。但我们计算这些 embeddings 时，并没有强制要求任何关键词匹配。用这种方式检索文档时，匹配到的文档完全可能没有任何共同的词，但表达的意思相同。

### [34:26](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=2066s) · b000066

**English**

Well, sometimes you want to ensure that what you're looking for, what you're searching for, is exactly containing the keywords that is in your prompt. And in that case, you would want to have a second way of doing things. So you may have seen BM25 out there. So BM25 is a relevant score that is actually a heuristic score. It is based on some function of the overlap between what is in your query and what is in your document.

**中文**

有时，你希望确保查找、搜索到的内容确实包含 prompt 中的关键词。这种情况下，你就会希望有第二种处理方式。你可能在其他地方看到过 BM25。BM25 是一种相关性分数，实际上是启发式分数（heuristic score）。它基于查询内容与文档内容之间重叠部分的某种函数。

### [35:09](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=2109s) · b000067

**English**

And so that one is actually quite handy for cases, where you have a query where you absolutely want to have documents that contain keywords of this query. So here, I have an example that I actually passed super briefly for the previous one. And we will come back to it. But let's suppose we have let's say two teddy bears. One is named Cuddly and the other one is named Huggy.

**中文**

在某些情况下，它非常方便，比如你有一个查询，并且一定要找到包含该查询关键词的文档。这里有一个例子，前面讲上一种方法时，我实际上非常简略地带过了，稍后还会回来讨论。假设我们有两只泰迪熊，一只叫 Cuddly，另一只叫 Huggy。

### [35:40](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=2140s) · b000068

**English**

So what you want is to figure out where is Cuddly. So this is your query. So if you use BM25, well, the answers that you are going to get are by definition going to contain some overlap of words that were in your query. And so here, you will have, let's say documents that contain, let's say where cuddly is. But if let's say you only used these semantic similarity search, you would not have that guarantee.

**中文**

你想弄清楚 Cuddly 在哪里。这就是你的查询。如果使用 BM25，那么按照定义，你得到的答案会包含与你查询中某些词的重叠。因此，这里你会得到，比如，包含 cuddly 在哪里这类内容的文档。但如果只使用 semantic similarity search，就没有这种保证。

### [36:20](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=2180s) · b000069

**English**

You would only have documents that are semantically similar. And those they are not guaranteed to contain keywords of your prompts. And so just to illustrate that. So here, Huggy and Cuddly, they can be thought of semantically similar. So you will probably not have cuddly--you will not necessarily have cuddly in there. Just to illustrate that.

**中文**

你只会得到语义相似的文档，而这些文档不保证包含 prompt 中的关键词。举个例子，Huggy 和 Cuddly 可以被认为在语义上是相似的。因此，里面可能不会有 cuddly——不一定会有 cuddly。只是用这个来说明一下。

### [36:51](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=2211s) · b000070

**English**

And that is the reason why nowadays, what people do is to look at the use cases that they have and think about whether having some heuristic, as well in the relevance score is useful for their use case. So some people, they go with the hybrid combination of this embedding-based search and the heuristic-based search. So some combination of embeddings and BM25 in which case you may have.

**中文**

这就是为什么现在人们会根据自己的应用场景，考虑在相关性分数中也加入一些启发式因素，是否对这个应用场景有用。有些人会把基于 embedding 的搜索和基于启发式的搜索混合起来。也就是以某种方式结合 embeddings 和 BM25，在这种情况下，你可能会得到。

### [37:26](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=2246s) · b000071

**English**

Even more relevant documents, depending on your use case.

**中文**

更加相关的文档，具体取决于你的应用场景。

### [37:32](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=2252s) · b000072

**English**

Does that make sense? Yeah. So now I'll come back to what you mentioned about whether cutting chunks in a naive way will necessarily lead you to things that are coherent. Well, you're completely right. Sometimes you will not. But before we answer this question, we actually are going to address another concern, which is that typically, when people want to ask about something in their LLM, the query that they input is of a different nature compared to what is in the knowledge base.

**中文**

这样能理解吗？嗯。现在我回到你刚才提到的问题：朴素地切分 chunks 是否一定能得到连贯的内容？你说得完全正确，有时候不能。但在回答这个问题之前，我们先讨论另一个问题：通常，当人们想向 LLM 询问某件事时，输入的查询与知识库中的内容在性质上有所不同。

### [38:17](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=2297s) · b000073

**English**

So your query is typically going to be maybe something short, maybe a question. But what is in your documents is typically going to be longer. These are like sentences and sentences. So if you really think about it, if you use the same encoder to embed your query and to embed your documents, well, these two embeddings, they're not super comparable, because one is for a question and the other one is for a document.

**中文**

查询通常可能比较短，也可能是一个问题。但文档中的内容通常更长，是一句接一句的文本。因此，仔细想想，如果用同一个 encoder 来嵌入查询和文档，那么这两个 embeddings 并不是特别具有可比性，因为一个对应问题，另一个对应文档。

### [38:50](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=2330s) · b000074

**English**

So there's one extension that tries to mitigate that issue. And I link the paper down there. So it's called the height. So what it does is instead of computing the embedding related to the prompt, it will first generate a fake document. So it's just an LLM call, a fake document based on that prompt. And then embeds that fake document to find relevant chunks.

**中文**

有一种扩展方法试图缓解这个问题，我在下面放了论文链接。它叫作 height \[字幕疑误，可能指 HyDE\]。它不是直接计算 prompt 对应的 embedding，而是先生成一篇虚构文档。也就是调用一次 LLM，根据这个 prompt 生成一篇虚构文档，再对这篇虚构文档进行嵌入，以寻找相关 chunks。

### [39:27](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=2367s) · b000075

**English**

So it may or may not work. It's not used all the time by everyone. So I would say just something that is good to try to see if that works. But this is one way of mitigating this, another way could be to simply have encoders that are specifically trained to encode the query on one side and encode the documents on the other side. In other words, to not use the same encoder. People typically don't do that, just because of maintenance purposes.

**中文**

它可能有效，也可能无效，并不是所有人都会一直使用。我会说，它是一种值得尝试、看看是否有效的方法。这是缓解问题的一种方式。另一种方式是，分别使用专门训练的 encoders，一个编码查询，另一个编码文档。换句话说，不使用同一个 encoder。人们通常不会这样做，主要是出于维护方面的考虑。

### [40:00](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=2400s) · b000076

**English**

But this could also be another solution.

**中文**

不过，这也可以是另一种解决方案。

### [40:04](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=2404s) · b000077

**English**

So now, finally going to your question regarding how we can make sense of these chunks. If they are taken out of context, they may not make sense. And so here, the idea here is to prepend some piece of text that just sums up what you need to in order to understand that chunk. So here, the idea is that you have all your documents.

**中文**

现在，终于回到你关于如何让这些 chunks 有意义的问题。如果脱离上下文，它们可能就没有意义。因此，这里的思路是在前面加上一段文本，简要概括理解这个 chunk 所需的内容。这里，假设你拥有所有文档。

### [40:34](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=2434s) · b000078

**English**

Let's say you have one document, that you divide it into n chunks. The idea here is instead of considering these chunks separately, you're going to compute some kind of context that is relevant to each chunk, and that is based on the whole document.

**中文**

假设你有一篇文档，把它划分成 n 个 chunks。这里的思路是，不再孤立地看待这些 chunks，而是基于整篇文档，为每个 chunk 计算一些与它相关的上下文。

### [40:59](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=2459s) · b000079

**English**

So how are you going to do that? Again, the LLM call. So what you do is typically, have, let's say, the whole document. And then you have the chunk that you want to contextualize. And you ask your model, well, please give me a short succinct context to just make sense of that chunk. And now you may tell me, well, that's a lot of LLM calls. You have potentially a lot of chunks. And that's just going to be very pricey.

**中文**

那要怎么做呢？还是调用 LLM。通常，你会提供，比如，整篇文档，再提供你想补充上下文的 chunk。然后问模型：请给我一段简短、精炼的上下文，让这个 chunk 能够被理解。现在你可能会说，这需要很多次 LLM 调用，你可能有大量 chunks，这会非常昂贵。

### [41:31](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=2491s) · b000080

**English**

Well, there's one strategy to make this less expensive, and I'm not sure if you've heard that option. It's called prompt caching. So now that you very well how LLMs work, you know, typically, these are decoder only and so on. So you know that if you use the same prefix for all your prompts, well, it's going to be the same computations that you just do again and again and again.

**中文**

有一种策略可以降低费用，不知道你们是否听说过这个选项。它叫作提示词缓存（prompt caching）。既然你们现在已经很了解 LLM 的工作原理，知道它们通常是仅解码器（decoder only）模型等等，那么你们就知道，如果所有 prompt 都使用相同的前缀，就会一遍又一遍地执行相同的计算。

### [42:10](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=2530s) · b000081

**English**

So the idea here is you just do it once. And you save all the relevant activations. And instead of computing them again, you're just going to look them up, just do a lookup, and then decode the rest.

**中文**

这里的思路是，只计算一次，保存所有相关的激活值（activations）。之后不再重新计算，而是直接查找，只做一次查找，再解码剩余部分。

### [42:30](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=2550s) · b000082

**English**

Does that make sense? Yeah. The question is activation from a language model. Yes, because when you feed a prompt to your model and you ask it to generate a response, what the model needs to do is well, to take all of this input and then compute the activations of all the layers, and then have for the generation process to have this attention across all these other components. Well, given that it's decoder only meaning, it's only left to right.

**中文**

能理解吗？嗯。问题是，来自语言模型的 activation 吗？对，因为当你向模型输入一个 prompt，并要求它生成回答时，模型需要处理全部输入，计算所有层的 activations，然后在生成过程中，对所有这些其他组成部分进行注意力（attention）计算。既然它是 decoder only，也就是说，它只从左向右处理。

### [43:07](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=2587s) · b000083

**English**

The thing that you input, if it's the same, then it will lead to the same activations. Yeah.

**中文**

如果输入的内容相同，就会产生相同的 activations。对。

### [43:20](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=2600s) · b000084

**English**

The question is, what if you have a closed model where prompt caching, and I'm going to just talk about this in just one slide, is an option that is closed models or providers offer? And what they tell you is, well, this is the same prefix for all your prompts. So what we're going to do is we're just going to make it cheaper for you. So if you look at the model pricing page, you will see that there is a price for regular inputs.

**中文**

问题是，如果你用的是一个封闭模型怎么办？prompt caching——我马上会用一张幻灯片讲到——是封闭模型或提供商提供的一个选项。他们会告诉你：你的所有 prompt 都有相同的前缀，因此，我们会为你降低费用。如果你查看模型定价页面，就会看到常规输入的价格。

### [43:56](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=2636s) · b000085

**English**

So inputs that are not cached. And then you have the price per cached input token. And here, you see for the let's say, OpenAI model, it's 110th of the price. So I guess, what do I want to tell you by this? Well, just try to be smart with the prompts and try to gather all the things that are likely to be repeated across prompts in the beginning. So that you can leverage this nice percentage off.

**中文**

也就是未缓存输入的价格。然后还有每个已缓存输入 token 的价格。这里你可以看到，比如 OpenAI 模型，价格是原来的 110th \[字幕疑误，可能指 1/10\]。那么，我想借此告诉你们什么呢？就是尽量聪明地组织 prompts，把那些可能在不同 prompts 中重复出现的内容集中放在开头，这样就能利用这个不错的折扣。

### [44:32](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=2672s) · b000086

**English**

Does that make sense? OK. Cool. Great. So up until now, we have seen how we can go from potentially thousands or even, let's say, millions of chunks up to, or down to, let's say, hundreds of potentially relevant chunks. Now, what we want to do is to sort them in a more meaningful way. And the second part is more optional, because maybe sometimes this first cut that we've done may be good enough, but I guess this second step is about being more intentional in how we give the final score to be able to really select the final, let's say, top k chunks.

**中文**

能理解吗？好，很好。到目前为止，我们已经看到了如何从可能有数千、甚至数百万个 chunks，增加到——或者说减少到——数百个可能相关的 chunks。现在，我们希望以更有意义的方式对它们排序。第二部分更偏向可选，因为有时第一轮筛选可能已经足够好了。不过，我想，第二步是更有针对性地给出最终分数，以便真正选出最终的，比如，前 k 个 chunks。

### [45:24](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=2724s) · b000087

**English**

So the second stage is called ranking or even re-ranking. Re-ranking because, I guess, with the first step, you already have some ranking. So we're re-ranking. And what we're doing is instead of using this very quick operation, similarity operation between embeddings that we've computed, we're going to use something that is maybe a bit more sophisticated. So instead of considering the query and the chunk separately, what we're going to do is to actually put them both in the encoder, both of them, and have a relevance score out of that.

**中文**

第二阶段叫作 ranking，或者重排序（re-ranking）。叫 re-ranking，是因为第一步已经有了某种排序，所以我们是在重新排序。我们不再使用已计算好的 embeddings 之间那种非常快速的相似度运算，而是使用一种可能稍微复杂一点的方法。我们不再分别考虑查询和 chunk，而是把它们两个一起输入 encoder，并由此得到相关性分数。

### [46:11](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=2771s) · b000088

**English**

So the reason why it may be a little bit more meaningful to do it this way is that you have a model that takes a look at both your query and your chunk at the same time and gives you a score. Whereas in the first step, you had one embedding for the query and one embedding for the chunk, which didn't have that interaction that a model could capture. And you will also see out there that this setup is called cross-encoder setup because you have both your inputs fed to your encoder.

**中文**

这样做可能更有意义，是因为模型会同时查看查询和 chunk，再给出一个分数。而在第一步中，查询有一个 embedding，chunk 有另一个 embedding，缺少模型能够捕捉到的那种交互。你也会看到，这种设置被称为交叉编码器（cross-encoder）设置，因为两个输入都会一起送入 encoder。

### [46:52](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=2812s) · b000089

**English**

So there's some cross interactions. So if you remember the first approach is a bi-encoder setup. And this one is a cross-encoder.

**中文**

因此，两者之间会有一些交叉交互。如果你还记得，第一种方法是 bi-encoder 设置，而这一种是 cross-encoder。

### [47:09](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=2829s) · b000090

**English**

Yeah. The question is, you will actually compute the attention between the two. Yes, absolutely. And here, sentence there they have a lot of good documents. So I highly recommend just reading their docs. They're at the bottom of the slide. Cool. Well, you do that on all your potentially relevant chunks. So you have this score that is computed for each of these chunks with the prompts.

**中文**

对。问题是，实际上会计算两者之间的 attention 吗？对，完全正确。这里，sentence there \[字幕疑误，可能指 Sentence Transformers\] 有很多不错的文档。我非常推荐阅读它们的文档，链接就在幻灯片底部。好。你会对所有可能相关的 chunks 进行这一操作，因此，每个 chunk 都会结合 prompt 计算出一个分数。

### [47:42](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=2862s) · b000091

**English**

And then you finally obtain the ranking. And now the question is, are you happy with the ranking? And in order to answer that question, you need a way to quantify your performance. And that's where we're going to see in the next five minutes. What are the metrics that we typically use to do that? So again, this is very similar to if you do search or recommendation. So in case you have a background there, you will see some commonalities.

**中文**

然后，你最终得到排序。现在的问题是，你对这个排序满意吗？为了回答这个问题，你需要一种量化性能的方法。接下来五分钟，我们就来看看，通常用哪些指标来做这件事。还是那句话，这与搜索或推荐非常相似。如果你有这方面的背景，就会看到一些共同之处。

### [48:18](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=2898s) · b000092

**English**

So here's the setup. You have a bunch of chunks. You do this first and second step. And at the end of the day, you will have k chunks that will come at the top, that you will qualify as being relevant. And you want to compare that with respect to actually relevant chunks. So you can think of it as you have label like, same as in binary classification.

**中文**

具体设置是这样：你有一批 chunks，执行第一步和第二步。最终，会有 k 个 chunks 排在最前面，你会把它们判定为相关。然后，你想把这些结果与真正相关的 chunks 进行比较。可以把它理解为，你有标签，就和二分类（binary classification）一样。

### [48:49](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=2929s) · b000093

**English**

So you have relevant and not relevant, and you predict some that are relevant and you want to know well you're doing. So this is the setup. Well, when it comes to ranking, you need to somehow incorporate this information of how high in the ranking you've put stuff. So here, let's suppose that you have ranked this n chunks from most important to least important.

**中文**

有相关和不相关两种标签，你预测其中一些是相关的，并想知道自己做得怎么样。这就是设置。对于排序来说，你还需要以某种方式纳入“把内容排在多靠前的位置”这一信息。这里，假设你已经把这 n 个 chunks 按照从最重要到最不重要的顺序排好了。

### [49:21](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=2961s) · b000094

**English**

So let's suppose you have first, second, third, and so on, and so forth. And you only care about the first k, because in the rack setting, you typically retrieve the top k that are relevant. And you put all these top k in your prompt. Well, the first metric that you will likely use is called NDCG.

**中文**

假设有第一、第二、第三，依此类推。你只关心前 k 个，因为在 rack \[字幕疑误，可能指 RAG\] 设置中，你通常会检索相关的前 k 个，并把这前 k 个都放进 prompt。那么，你很可能会使用的第一个指标叫作 NDCG。

### [49:49](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=2989s) · b000095

**English**

It's a lot of letters. I'm going to just explain what that means. So NDCG tries to quantify how good your ranking is by taking into consideration where you ranked relevant documents. So you have this formula that may seem scary, but it's actually quite simple what it's trying to do. So it's trying to incentivize the score to be higher.

**中文**

字母有点多，我来解释它的含义。NDCG 会考虑你把相关文档排在什么位置，试图以此量化排序的好坏。这里有个公式，看起来可能有些吓人，但它要做的事其实很简单。它希望在这种情况下让分数更高。

### [50:23](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=3023s) · b000096

**English**

If your ranking the relevant documents closer to the first position. So what it does, is it is the sum over the first k positions that you're ranked. And it is looking at whether what you've ranked for each of these positions is relevant or not. So for instance, it checks the first position. First position is irrelevant or not. So relevance-- if it's relevant, it's one.

**中文**

就是当你把相关文档排得更接近第一名时。它会对排序中的前 k 个位置求和，并查看每个位置上的内容是否相关。例如，它检查第一个位置，看第一个位置的内容是否不相关。那么相关性——如果相关，就是 1。

### [50:55](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=3055s) · b000097

**English**

So it's one over some quantity that is a function of the rank. And it does that for all the ranks. So the score will be higher if you rank relevant documents high. So that's basically the goal of this metric. So this part is the discounted cumulative gain. So it's cumulative gain because you're looking at basically, if you had relevant documents in your first k positions, which is cumulative part, it's discounted because it's better for you to have a relevant document in position one, let's say, than position k.

**中文**

于是就是 1 除以某个与排名有关的量。它会对所有排名都这样计算。因此，如果你把相关文档排得靠前，分数就会更高。这基本上就是这个指标的目标。这部分叫作折损累计增益（discounted cumulative gain，DCG）。之所以是累计增益，是因为你基本上在查看前 k 个位置中是否有相关文档，这是累计的部分。之所以是折损，是因为对你来说，把相关文档放在第 1 位，比放在第 k 位更好。

### [51:42](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=3102s) · b000098

**English**

And you can see that in the denominator. Now, why do we say NDCG? What is the normalization part? Well, this metric can take a lot of different values, depending on how many relevant documents there are. So what people do is they compute the quote, unquote, "ideal or optimal or upper bound" DCG that you can get for a given query, and they call that ideal DCG, and they just normalized DCG over IDCG.

**中文**

这一点可以从分母中看出来。那么，为什么叫 NDCG？归一化的部分是什么？这个指标可能取很多不同的值，取决于有多少相关文档。因此，人们会针对给定查询，计算你能够获得的所谓“理想、最优或者上界”DCG，称为理想 DCG（ideal DCG，IDCG），再用 DCG 除以 IDCG 进行归一化。

### [52:23](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=3143s) · b000099

**English**

So the reason why they do that is they want you to score a score of one, if you are matching the optimal ranking. They basically want to make the score meaningful.

**中文**

这样做的原因是，他们希望当你的排序与最优排序一致时，你能得到 1 分。他们基本上是想让这个分数具有意义。

### [52:39](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=3159s) · b000100

**English**

So does this make sense? Yeah?

**中文**

这样能理解吗？嗯？

### [52:52](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=3172s) · b000101

**English**

So the question is, how do they compute the relevance score? So you can think step one and step two as being a two-step process for you to say which documents you are saying are relevant. So at the end of this two-step stage, the ones that you say are relevant are here. Now, you typically have a score for each retrieved chunk. So you're going to sort these chunks.

**中文**

问题是，相关性分数是如何计算的？你可以把第一步和第二步看作一个两步流程，用来决定你认为哪些文档相关。完成这两个阶段后，你认为相关的文档就在这里。通常，每个检索出的 chunk 都会有一个分数，然后你会对这些 chunks 排序。

### [53:25](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=3205s) · b000102

**English**

You're going to sort them by the score in a descending order. And the relevance here that you're going to use is the actual label. So is the chunk actually relevant or not? So you're going to look at your k retrieved chunks, and you're going to ask yourself, OK, is the first chunk actually relevant? So you have a label. You know which ones are relevant, which ones are not. And these ones are going to be the ones you will use in the formula.

**中文**

你会按分数从高到低排序。而这里要使用的相关性，是实际标签。也就是说，这个 chunk 到底是否相关？你要查看检索出的 k 个 chunks，然后问自己：好，第一个 chunk 实际上相关吗？你有标签，知道哪些相关，哪些不相关。公式中使用的就是这些标签。

### [53:58](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=3238s) · b000103

**English**

Yes, that's the ground truth. Exactly. Yeah.

**中文**

对，那就是真实标签（ground truth）。完全正确。对。

### [54:04](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=3244s) · b000104

**English**

Cool. Does that make sense? Yeah. OK. Great. So you have a bunch of other metrics. You have another one that's called the reciprocal rank. So this one is much simpler. It takes the inverse of the highest rank of all the relevant documents. So if let's suppose in your top k documents, let's suppose the first relevant document, let's say, comes at rank number two.

**中文**

好。能理解吗？嗯，好，很好。还有其他一些指标。另一个叫作倒数排名（reciprocal rank）。这个简单得多，它取所有相关文档中最靠前名次的倒数。例如，假设在前 k 个文档中，第一个相关文档排在第 2 位。

### [54:40](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=3280s) · b000105

**English**

Then rank will be equal to two. So it basically does not care about any relevant documents that are past that first relevant document. So this is just like a simpler metric that typically correlates well. So that's why people use it. And then, of course, you're familiar with the classic classification metrics--recall and precision. So if you remember, if you have two classes, you have the positive class, you have the negative class.

**中文**

那么 rank 就等于 2。它基本上不关心第一个相关文档之后的任何相关文档。这是一个更简单的指标，通常有很好的相关性，所以人们会使用它。当然，你们也熟悉经典的分类指标——recall 和精确率（precision）。如果你们还记得，当有两个类别时，有正类，也有负类。

### [55:14](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=3314s) · b000106

**English**

So recall, what it does is it takes a look at all the actually positive observations, and it tries to ask itself among all these actually positive samples, which are the ones that you actually predicted positive? That's the recall that you all know. And there is, I guess, a ranking equivalent, which is out of all the documents that are relevant, actually relevant, so this is like your positive class, which are the ones that you actually predicted as being relevant?

**中文**

recall 会查看所有实际上为正的观测，并问：在所有实际正样本中，哪些是你确实预测为正的？这就是你们熟悉的 recall。我想，排序中也有一个对应版本：在所有相关、实际相关的文档中，也就是相当于正类，哪些被你预测为相关？

### [55:55](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=3355s) · b000107

**English**

So this is basically which ones are in the top k? And similarly, you also have the precision equivalent. So if you remember, precision is out of all the ones that you have predicted to be positives, how many of them are actually positive? So this is the equivalent here. So which are the ones that you've predicted to be positive? So which are the ones that you have selected in your top k?

**中文**

这基本上就是问，哪些位于前 k 个中？同样，也有 precision 的对应版本。如果你还记得，precision 是在所有预测为正的样本中，有多少实际上为正？这里也是一样。哪些是你预测为正的？也就是，你选入前 k 个的是哪些？

### [56:26](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=3386s) · b000108

**English**

And among those ones, which ones are actually positive? So which ones are actually relevant?

**中文**

在这些里面，哪些实际上为正？也就是，哪些实际相关？

### [56:35](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=3395s) · b000109

**English**

Does that make sense? So I guess these four metrics--NDCG, MRR, precision at k, recall at k, we see this in a bunch of papers. So I just highly recommend you just get familiar with their ideas and maybe with the formula. And these would be the ones that you would use to quantify, whether your retriever is doing a good job or not. So you have a bunch of benchmarks out there. So there is one that is actually quite popular.

**中文**

能理解吗？我想，这四个指标——NDCG、MRR、precision at k、recall at k——在很多论文中都会出现。因此，我非常建议你们熟悉它们的思路，或许也熟悉一下公式。你会使用这些指标，量化检索器（retriever）做得好不好。现在有很多基准测试（benchmarks），其中有一个相当流行。

### [57:05](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=3425s) · b000110

**English**

It's is called massive text embedding benchmark. So if you want to test your retriever, if it performs well or not would typically take it, and then just evaluate it on that benchmark, and then have all these metrics computed. And then if you have different solutions, you would typically compare this metric.

**中文**

它叫作 massive text embedding benchmark。如果想测试 retriever 的表现好不好，通常会把它拿来，在这个 benchmark 上进行评估，然后计算所有这些指标。如果你有不同的解决方案，通常就会比较这个指标。

### [57:29](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=3449s) · b000111

**English**

And with that, we, I guess, hopefully, have a better sense of how to build a RAG system and specifically how to have a good retriever. So we have just maybe one more minute. Is there any questions on that first part? Yeah?

**中文**

讲到这里，希望我们对如何构建 RAG 系统，尤其是如何拥有一个好的 retriever，有了更清楚的认识。我们大概还剩一分钟。关于第一部分，有什么问题吗？嗯？

### [57:58](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=3478s) · b000112

**English**

So the question is, so for the re-ranking, we're using an encoder that will output a relevance score. So we will typically train a model that does that. So there are typically--I believe there are some pre-trained ones, but out there, you can very well have your custom one. So that model will typically be a bit more sophisticated compared to the first step. Because here, you can afford to spend more time to produce that score because you're operating out of, let's say, over 100 possible candidates, as opposed to let's say, much more millions or hundreds of thousands.

**中文**

问题是，对于 re-ranking，我们使用一个输出相关性分数的 encoder。通常，我们会训练一个能完成这件事的模型。一般来说——我相信已经有一些预训练模型，但你完全也可以使用自己的定制模型。相比第一步，这个模型通常会稍微复杂一些。因为这里你可以花更多时间来生成这个分数，毕竟处理的是，比如，100 多个可能的候选，而不是多得多的数百万或数十万个候选。

### [58:38](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=3518s) · b000113

**English**

So that's the idea. Yeah?

**中文**

这就是思路。嗯？

### [58:46](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=3526s) · b000114

**English**

So the question is, how about training with contrastive loss? This is a detail, we not I guess, cover here. But in order to train these models, you'll have a bunch of different types of loss function. So I highly recommend you read the S-BERT paper, because in that paper, there are several loss functions that the paper tries to compare. And this is one of them. So that's a great question. I highly recommend reading the S-BERT paper for that.

**中文**

问题是，用对比损失（contrastive loss）进行训练怎么样？这是一个我们在这里，我想，不会展开的细节。不过，为了训练这些模型，你可以使用很多不同类型的 loss function。我非常推荐阅读 S-BERT 论文，因为那篇论文尝试比较了几种 loss function，而这就是其中之一。所以，这是个很好的问题。我非常推荐为此阅读 S-BERT 论文。

### [59:17](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=3557s) · b000115

**English**

Cool. With that, I'll give it to Shervine. Thank you, Afshine. So thanks a lot for covering the RAG methodology. So now, we arrive at my favorite part of the lecture. We're going to see tool calling and the agentic world. And we're going to see how much more powerful your LLMs are going to become just in a second. So what Afshine just mentioned is how you would deal with incorporating data that is not structured as part of your prompts to the LLM.

**中文**

好，接下来交给 Shervine。谢谢你，Afshine。非常感谢你介绍 RAG 方法。现在，来到这节课中我最喜欢的部分。我们将了解 tool calling 和智能体的世界，很快就会看到你的 LLMs 将变得多么强大。Afshine 刚才介绍的是，如何把非结构化数据作为 prompt 的一部分输入 LLM。

### [59:53](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=3593s) · b000116

**English**

And now, we're going to see what we could do more. In the case, the data that we want to inject is structured. So in the case of RAG, you have documents with words and words and words. And you just want to fetch the relevant documents to answer your prompts. But here, let's suppose that you have some structure that determines input/outputs in your data. So typically, you could represent it maybe as a table.

**中文**

现在，我们要看看还能做些什么，针对的是我们想注入的数据具有结构的情况。在 RAG 中，你有一些满是文字、文字、文字的文档，只想获取相关文档来回答 prompt。但在这里，假设你的数据中存在某种结构，决定了输入与输出。通常，你也许可以把它表示为一张表。

### [1:00:23](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=3623s) · b000117

**English**

So you have separate columns. And then depending on the value of given columns, you have a given output. So we could probably reframe that setup into a function, a setup. So we mentioned tool calling. And then this rephrasing is called the function calling. So let's suppose that you get this relationship between input and output through a function for the rest of this part.

**中文**

表中有不同的列，根据某些列的值，会有一个给定的输出。因此，我们大概可以把这种设置重新表述为一个函数、一种设置。我们提到了 tool calling，而这种重新表述叫作函数调用（function calling）。在这一部分接下来的内容中，假设你通过一个函数获得这种输入和输出之间的关系。

### [1:00:55](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=3655s) · b000118

**English**

And then here, if I had to transpose what the result of a given ID and field and other arguments would look like, you could interpret it as a function with these as arguments. And the output would be simply what you have as an output to the function.

**中文**

这里，如果我要把给定 ID、字段和其他参数所对应的结果换一种形式表示，你可以把它理解为一个以这些内容为参数的函数。输出就是这个函数所给出的输出。

### [1:01:16](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=3676s) · b000119

**English**

In the world of tool calling and function calling, very oftentimes, you're going to see that LLMs tend to use Python as a language, just because it's so simple to read. So this is what we are going to use as an example as well. But there is nothing that ties us to Python necessarily. So you could well have a tool calling in other languages.

**中文**

在 tool calling 和 function calling 的领域中，你经常会看到 LLMs 倾向于使用 Python 作为语言，因为它读起来非常简单。因此，我们也将使用 Python 作为示例。不过，没有任何东西要求我们一定使用 Python。你完全可以使用其他语言进行 tool calling。

### [1:01:42](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=3702s) · b000120

**English**

Just as a note. Any questions on the setup? OK. Awesome. So there is nothing controversial about tool calling, but I'm going to still state a full definition to make sure that we are on the same page. So I was browsing here and there, and I tried to find an authoritative source. And this website like on IBM, there is an article that defines--that tries to define what tool calling is.

**中文**

只是补充说明一下。关于这个设置有什么问题吗？好，很棒。tool calling 本身没有什么有争议的地方，不过我还是会给出一个完整定义，确保大家的理解一致。我到处浏览了一下，试图找到一个权威来源。在 IBM 这个网站上，有一篇文章定义了——试图定义什么是 tool calling。

### [1:02:12](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=3732s) · b000121

**English**

So I'm going to anchor on their definition from now on. So I'm going to read out loud. So tool calling allows autonomous systems to complete complex tasks by dynamically accessing and may act upon external resources. So the things that I want you to get from that are two things. So first, you have the notion of completing some task. So given an input and you have to complete some task and then the reliance potentially on external resources.

**中文**

所以从现在起，我会以他们的定义为依据。我来大声读一下。工具调用（tool calling）使自主系统能够通过动态访问外部资源，并可能对这些资源采取行动，来完成复杂任务。我希望大家从中理解两点。首先，是完成某个任务这个概念。也就是，给定一个输入，你必须完成某个任务，然后是可能会依赖外部资源。

### [1:02:49](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=3769s) · b000122

**English**

So it doesn't have to be external. You don't have to rely on external resources. But this is one potential property that can help you fill the gap that Afshine was mentioning at the beginning of the lecture, regarding filling the knowledge gap that your pre-trained LLM has. So we're going to see examples in a few minutes, regarding what that could mean. But yeah, this is one magical part of it.

**中文**

所以，它不一定非得是外部的。你不一定要依赖外部资源。但这是一个潜在的特性，可以帮助你弥补 Afshine 在讲座开头提到的差距，也就是弥补预训练的大语言模型（LLM）所存在的知识缺口。几分钟后，我们会看一些例子，说明这可能意味着什么。不过，是的，这是其中一个神奇之处。

### [1:03:22](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=3802s) · b000123

**English**

OK. Great. And just to make these statements very grounded in real-life applications, let's just walk through what would a tool call give us in the case of a very specific example? So let's suppose you love teddy bears. You're currently here at Stanford, and you want a teddy bear near you. What if you pull your phone out, and you just ask, find a teddy bear near me.

**中文**

好。很好。为了让这些说法切实对应现实应用，我们来看看，在一个非常具体的例子中，一次工具调用（tool call）能给我们带来什么。假设你很喜欢泰迪熊。你现在就在 Stanford，想在附近找一只泰迪熊。如果你拿出手机，直接问：找一只我附近的泰迪熊，会怎么样？

### [1:03:55](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=3835s) · b000124

**English**

Well, your current LLM, without any tools, would not know some real-life or like real-time update of availability of teddy bears near you. So it would probably answer you something in the flavor of, I don't know or not sure. And I just want to say that with the use of tools, let's see how we could get to a stage where we can inject the information that is necessary for the LLM to know how to respond to your query.

**中文**

那么，你现在的 LLM 如果没有任何工具，就不会知道你附近哪里有泰迪熊的现实情况，或者实时更新的信息。所以，它很可能会回答类似于“我不知道”或“不确定”的内容。我想说的是，借助工具，我们来看看如何做到注入必要的信息，让 LLM 知道该如何回应你的查询。

### [1:04:31](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=3871s) · b000125

**English**

And the goal of the next few minutes is going to be for us to figure out, both what we could do what-- what we could inject in the preamble of the LLM? And what would be the steps that we could go through in order to complete such a request?

**中文**

接下来几分钟的目标，就是弄清楚两件事：我们能做什么——能在 LLM 的前置说明（preamble）里注入什么？以及，为了完成这样的请求，我们可以经历哪些步骤？

### [1:04:52](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=3892s) · b000126

**English**

Does that make sense so far? Yeah?

**中文**

到目前为止都明白吗？嗯？

### [1:05:02](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=3902s) · b000127

**English**

So the question is, are those function APIs pre-computed? So that's a great question. So yes, you define them beforehand. You have some API. And we're going to see that in a second. They're not LLM generated on the fly.

**中文**

问题是，这些函数 API 是预先计算好的吗？这是个很好的问题。是的，你要事先定义它们。你有一些 API。我们马上就会看到。它们不是由 LLM 即时生成的。

### [1:05:19](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=3919s) · b000128

**English**

OK. Great. Any other questions on the setup? So I know it will be a lot to take in.

**中文**

好。很好。关于这个设定，还有其他问题吗？我知道需要消化的内容会很多。

### [1:05:28](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=3928s) · b000129

**English**

OK. Great. So in order to be grounded in real life, let's take a full example of what a function definition could be. So in the case of finding a teddy bear, you could imagine a function definition that is called find teddy bear. And depending on your location, calls some API and retrieves potential candidates.

**中文**

好。很好。为了对应现实情况，我们来看一个完整的例子，看看函数定义（function definition）可以是什么样。在寻找泰迪熊这个例子里，你可以设想一个名为 find teddy bear 的函数定义。它会根据你的位置调用某个 API，并检索出可能的候选对象。

### [1:05:58](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=3958s) · b000130

**English**

So I'm going to go through the main characteristics of what a function call contains and link it to the definition. So first of all, when we want to display such an API to the model, you need to document it, its input and output, in order for the model to what this function is for. So typically, the description that you have in the example of Python under a given function would be crucial for the model to know what it is about.

**中文**

我会介绍函数调用（function call）所包含的主要特征，并把它们与定义联系起来。首先，当我们想把这样的 API 展示给模型时，需要为它以及它的输入和输出编写文档，让模型知道这个函数是做什么的。所以，通常在 Python 示例中，某个函数下面的描述，对于模型理解它的用途至关重要。

### [1:06:34](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=3994s) · b000131

**English**

And then we saw in the definition of tool call that we just gave, that we have the ability to make backend calls. And this is exactly what we would need to do in the case of finding teddy bears around you. You would need to query some API to retrieve available teddy bears. And based on your location, return the nearest ones. So this is exactly what this function implementation is doing.

**中文**

然后，我们在刚才给出的 tool call 定义中看到，我们能够发起后端调用（backend calls）。这正是寻找你周围的泰迪熊时需要做的事情。你需要查询某个 API，获取可获得的泰迪熊。然后根据你的位置，返回最近的那些。这正是这个函数实现所做的事。

### [1:07:08](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=4028s) · b000132

**English**

It returns something that is well structured. So you see maybe it's small from where you are, but you have some class definition that puts some structure into the output and makes it interpretable. And we're going to see very soon that this output is going to be what the model will anchor on in order to give its final response.

**中文**

它会返回结构清晰的内容。你们可以看到，也许从你们的位置看有点小，不过这里有一个类定义（class definition），为输出赋予某种结构，让它可以被解释。我们很快就会看到，模型将以这个输出为依据，给出最终回答。

### [1:07:36](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=4056s) · b000133

**English**

OK. Great. And one other thing I will say is all of these that we see here is what you have implemented. You will not see all of these--if you are an LLM, you will not see all of this. All you care about as an LLM is the function API, the input and output, as well as the main lines of documentations. So all these implementation details, you're going to have it on your code base.

**中文**

好。很好。我还想说一点，我们在这里看到的这些，都是你实现的内容。你不会看到所有这些——如果你是一个 LLM，你不会看到全部内容。作为 LLM，你只关心函数 API、输入和输出，以及文档的主要内容。所以，这些实现细节都会放在你的代码库（code base）里。

### [1:08:07](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=4087s) · b000134

**English**

But the LLM is not going to see it. OK. Great. So now, let's go step-by-step into how we could make this work. So the first stage is as you ask a question that is related to your function, you would insert at the beginning of your preamble the function API. And as I mentioned without its implementation. So you just have the function itself, and then a full documentation.

**中文**

但 LLM 不会看到它们。好。很好。现在，我们一步一步来看，怎样让它运行起来。第一个阶段是，当你提出一个与函数有关的问题时，你会在 preamble 的开头插入函数 API。正如我提到的，不包含它的实现。所以只有函数本身，以及完整的文档。

### [1:08:43](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=4123s) · b000135

**English**

So here, you would want the LLM based on your user query to feed the right arguments to your function. s to your point, the goal of the LLM here is not going to be to infer any of the functions implementations, rather only what arguments we should put to it. Yeah?

**中文**

在这里，你希望 LLM 根据用户查询，把正确的参数（arguments）传给函数。对应你刚才说的，这里 LLM 的目标不是推断任何函数的实现，而只是确定应该传入哪些参数。嗯？

### [1:09:19](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=4159s) · b000136

**English**

So the question is, how do you even train this? So we're going to see that in just a few slides. Great point. That's the next question we need to ask ourselves.

**中文**

问题是，这到底要怎么训练？再过几张幻灯片，我们就会看到。问得很好。这正是接下来需要问自己的问题。

### [1:09:33](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=4173s) · b000137

**English**

So we're going to see how we train these. But here, let's say it has been trained. The LLM would have, from its context, probably our localization, because let's say you have activated your location permissions and your LLM knows where you are. So it knows you are at Stanford. And these would be the coordinates being fed to your LLM. And then the second stage is to actually do that function call.

**中文**

我们会看到如何训练这些能力。不过在这里，先假设它已经训练好了。LLM 从上下文（context）中可能已经知道我们的位置，因为假设你开启了位置权限，LLM 知道你在哪里。所以，它知道你在 Stanford。这些就是提供给 LLM 的坐标。然后，第二个阶段就是真正执行那次 function call。

### [1:10:04](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=4204s) · b000138

**English**

So it has nothing to do with LLMs. You just take your function, your argument, and you execute that and you get some answer. And the answer, as we mentioned, is structured in a way that's understandable. So in that function implementation, you return some object that informs characteristics about the return teddy bear. So for example, you have its name, maybe location, and so on.

**中文**

这与 LLM 无关。你只需要拿到函数和参数，执行它，然后得到某个答案。正如我们提到的，这个答案以一种可以理解的方式组织起来。所以，在那个函数实现中，你会返回一个对象，说明返回的泰迪熊有哪些特征。例如，它的名字，也许还有位置，等等。

### [1:10:34](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=4234s) · b000139

**English**

And you feed that response back to the LLM in order to get a final response. So when you ask to do LLM a given question, you don't want to have this JSON-like response, but rather a response in natural language. And this exactly is the motivation for that last stage. So I'm going to pause here for a second and check that this three-stage mechanism makes sense to everyone.

**中文**

然后，你把这个响应反馈给 LLM，以得到最终回答。当你向 LLM 提出某个问题时，你不想得到这种类似 JSON 的响应，而是想要自然语言的回答。这正是最后这个阶段的目的。我在这里暂停一下，确认大家都理解这个三阶段机制。

### [1:11:09](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=4269s) · b000140

**English**

OK. Great. And exactly what you were mentioning here is going to be the next focus. How do you even train that? So let me ask you this question. If you were to train an LLM to use this tool, what steps would you need to focus on?

**中文**

好。很好。你刚才提到的，正是我们接下来要关注的重点。这究竟怎么训练？让我问大家一个问题。如果你要训练一个 LLM 来使用这个工具，需要重点关注哪些步骤？

### [1:11:36](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=4296s) · b000141

**English**

So the answer is you're going to feed the API implementation. Yes. So you would need the first LLM call to be somehow recognizing the pattern of the function implementation and the query, and link it to the arguments that you would put in your function. So yeah. Great. So tool prediction. And do you need a second set of SFT pairs?

**中文**

所以，回答是你会输入 API 的实现。是的。你需要让第一次 LLM 调用以某种方式识别函数实现与查询的模式，并将其与要传入函数的参数联系起来。是的。很好。所以，就是工具预测（tool prediction）。那你还需要第二组监督微调（supervised fine-tuning，SFT）样本对吗？

### [1:12:11](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=4331s) · b000142

**English**

So you have this last stage that is still LLM-driven, where you have your tool answer, and you need to output a final response.

**中文**

最后这个阶段仍然由 LLM 驱动：你拿到工具的回答，需要输出最终响应。

### [1:12:22](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=4342s) · b000143

**English**

You might say, OK, hey, the LLM has seen a bunch of structured data and knows how to put into words, things that it sees, which is a fair point. But usually, you might want your responses to be formatted a given way. So you might want to also have SFT pairs that do this mapping the way you want it to. So this is why you typically have these two SFT pairs. And if I have to be a bit more precise, the second pair isn't just mapping the JSON response to the final response, it's actually linking all the conversation history so far, so that it knows that the initial query was someone in search of a teddy bear.

**中文**

你可能会说，好吧，LLM 已经见过很多结构化数据，也知道怎样把看到的内容用语言表达出来，这个说法有道理。但通常，你可能希望回答采用特定的格式。所以，你可能也希望有一些 SFT 样本对，按你想要的方式完成这种映射。这就是为什么通常会有这两种 SFT 样本对。如果说得更准确一点，第二种样本对并不只是把 JSON 响应映射成最终回答，而是实际关联截至目前的全部对话历史，让它知道最初的查询是有人想找一只泰迪熊。

### [1:13:06](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=4386s) · b000144

**English**

It knows there has been a tool call, and it knows that the results correspond to that tool call. So it would be a slightly longer input in this SFT pair. Does that make sense? OK. Great. Yeah?

**中文**

它知道已经发生了一次 tool call，也知道这些结果对应那次 tool call。所以，这个 SFT 样本对的输入会稍微长一点。这样说清楚吗？好。很好。嗯？

### [1:13:29](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=4409s) · b000145

**English**

Yeah. So great point. So the question is, what if we have more tools, do we need some tool selection or more examples? So this is a great topic. We're going to see it like in a few slides. Yeah. So it's slightly more complex way of doing things. But if you want a very quick answer, if you go the SFT way, you could show multi-tool inputs. So you could include all of that in your SFT data sets. But we're going to see the topic of tool selection very soon.

**中文**

是的。说得很好。问题是，如果我们有更多工具，是不是需要某种工具选择（tool selection），或者更多例子？这是个很好的话题。再过几张幻灯片就会讲到。是的。这种做法会稍微复杂一些。不过，如果你想要一个非常简短的回答：如果采用 SFT 的方式，可以展示包含多个工具的输入。也就是说，你可以把这些都放进 SFT 数据集里。但我们很快就会讲 tool selection。

### [1:14:03](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=4443s) · b000146

**English**

Great. Any other questions?

**中文**

很好。还有其他问题吗？

### [1:14:08](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=4448s) · b000147

**English**

OK. Awesome. This is what I just mentioned. Yeah, the conversation history so far is always what you get as part of the input. And then the output is what you would want the LLM to predict at that given stage. And since you're doing SFT here, you don't have just one, but multiple such examples. And you would want your examples to be varied and representing the typical user distribution. So I was asking, find a bear near me.

**中文**

好。太好了。这就是我刚才提到的。是的，截至目前的对话历史始终是输入的一部分。然后，输出就是你希望 LLM 在那个阶段预测的内容。而且，由于你这里做的是 SFT，所以不会只有一个，而是会有多个这样的例子。你希望这些例子具有多样性，并能代表典型的用户分布。比如，我刚才问的是：找一只我附近的熊。

### [1:14:40](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=4480s) · b000148

**English**

And this example showed to the model how you could ground the information of location based on the user's location, even though you didn't give it. And in this other examples, you could give the model other kinds of instructions, directly saying, I want a bear at that location to teach the model to look at--like to ground the argument at different places. And you could expand these sets by also varying the kind of input, so it doesn't have to be worried that way.

**中文**

这个例子向模型展示了，即使用户没有给出位置，也可以根据用户所在的位置，让位置信息获得依据（grounding）。在其他例子中，你可以给模型其他类型的指令，直接说：我想要那个位置的一只熊。以此教模型去查看——也就是从不同地方为参数寻找依据。你还可以通过改变输入的类型来扩充这些集合，所以不必按那种方式来 worried \[字幕疑误，可能指 worded，即措辞\]。

### [1:15:13](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=4513s) · b000149

**English**

You could do it multi-turn maybe in the middle of a conversation, you ask for a bear and so on. OK. Great. But this is not the only way of training a model to do so. So these days, LLMs become more and more powerful in their reasoning. And the kind of data they are trained at pre-training and initial instruction tuning is typically these kinds of code data.

**中文**

你可以采用多轮对话（multi-turn），比如在对话中间提出想要一只熊，等等。好。很好。但这并不是训练模型做到这一点的唯一方式。如今，LLM 的推理（reasoning）能力越来越强。而它们在预训练（pre-training）和初始指令微调（instruction tuning）阶段使用的数据，通常就包含这类代码数据。

### [1:15:44](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=4544s) · b000150

**English**

So at the end of it, they how to manipulate Python codes very well. So you might ask yourself, is it really needed for me to teach the model how to map a query to a function call? And that is a very interesting observation. And you see these days that you can forego of specific SFT training and try to get around it with only training.

**中文**

所以，完成这些之后，它们就很擅长操作 Python 代码了。你可能会问自己：我真的有必要教模型如何把查询映射成 function call 吗？这是一个很有意思的观察。如今你会看到，可以省去专门的 SFT 训练，尝试仅通过训练（training）\[字幕疑误，结合下文可能指 prompting\] 来解决这个问题。

### [1:16:15](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=4575s) · b000151

**English**

So here, instead of writing SFT and then retraining the model, we're going to see that you could actually replace it with only an explanation. And does anyone have an idea of how we could even come up with such an explanation?

**中文**

所以，在这里，我们会看到，你实际上可以只用一段说明来代替编写 SFT 内容、然后重新训练模型这件事。有人知道，我们可以怎样得到这样一段说明吗？

### [1:16:38](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=4598s) · b000152

**English**

So let's say I have a new tool. I have the API. I want my model to use it. How would you go around it?

**中文**

假设我有一个新工具。我有 API。我想让模型使用它。你会怎么做？

### [1:16:52](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=4612s) · b000153

**English**

Yeah, that's a great point. So one method could be few shot learning. You just show in the context window samples of input/output. This is a great point. You could definitely do that. And this is typically one accepted practice. But if I told you that few shot learning has challenges when it comes to generalization, because you would need to give specific points as input/output. So it might fit to some cases and not necessarily unnecessarily generalized to the whole span of human language.

**中文**

是的，这个想法很好。一种方法是少样本学习（few shot learning）。你只需要在上下文窗口（context window）中展示输入／输出样例。这个想法很好。你完全可以这么做，而且这通常是一种被接受的做法。不过，如果我告诉你，few shot learning 在泛化（generalization）方面存在挑战，因为你需要提供具体的输入／输出样例。所以，它可能适用于某些情况，却未必能泛化到人类语言的整个范围。

### [1:17:29](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=4649s) · b000154

**English**

Is there another way you could go around it?

**中文**

还有其他方法可以解决这个问题吗？

### [1:17:39](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=4659s) · b000155

**English**

Yeah. So the answer is ask it to do reasoning. Great point. And writing a prompt that does the reasoning in a way that makes sense is very hard. So in practice, you wouldn't write it yourself. You would take these SFT pairs. So these are the behavior that you want to enforce. And you could use it as some evaluation set. So you could say, OK, hey, if I ask this question, I want that stool call.

**中文**

是的。回答是，让它进行 reasoning。这个想法很好。而要写出一段能让它以合理方式推理的提示词（prompt），非常困难。所以在实践中，你不会自己写。你会拿这些 SFT 样本对，也就是你想要强化的行为，把它们用作某种评估集（evaluation set）。你可以说，好，如果我问这个问题，我希望得到那个 stool call \[字幕疑误，可能指 tool call\]。

### [1:18:13](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=4693s) · b000156

**English**

And you have a set of pairs. And you could run whatever you have so far in terms of explanation. You evaluate these prompts against the evaluation set. So you have some wins and losses. Maybe find a bear in Paris. Doesn't work well. Some other prompts do. So you have a list of each sample with a score. And you could feed it back to a reasoning model, typically, to do the explanation writing for you.

**中文**

你有一组这样的样本对。然后，你可以运行目前已有的说明，用评估集来评估这些 prompt。这样你会得到一些成功和失败的结果。比如，在 Paris 找一只熊，效果不好。其他一些 prompt 则有效。于是，你得到了一份列表，每个样本都有一个分数。然后，通常可以把这些反馈给一个推理模型（reasoning model），让它替你编写说明。

### [1:18:49](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=4729s) · b000157

**English**

So this is a trick to help you avoid doing that hard work. Basically, showing the model, hey, with the current prompts, here's what we get. What would you have changed in order to make the evaluation results better? So you get with that process an iteration on the detailed explanation. And if you have to see results in practice, you would be surprised at how well it does the explanation for you.

**中文**

这是一个帮你省去这项困难工作的技巧。基本上，就是向模型展示：看，使用当前的 prompt，我们得到了这些结果。为了改善评估结果，你会做哪些修改？通过这个过程，你就能迭代那份详细说明。如果你看看实际结果，会惊讶于它替你编写说明的效果有多好。

### [1:19:19](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=4759s) · b000158

**English**

So the takeaway here is I do not recommend you write it end-to-end. Maybe just a draft and you let some very powerful model with excellent knowledge of logic do it for you. Yeah?

**中文**

所以，这里要记住的是，我不建议你从头到尾自己写。也许只写个草稿，然后让某个拥有出色逻辑知识、能力很强的模型替你完成。嗯？

### [1:19:51](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=4791s) · b000159

**English**

Yeah. So the question is, what you just mentioned, is it training or inference? So it's training. So you do it at the very beginning. You want a fixed prompt that explains to the LLM how to use it, how to use that function. So you would typically do that offline. Offline you iterate on the explanation that says exactly how you use the prompt, how you use the function. And then at inference time, you would put that fixed explanation alongside the function API, such that for any query, it knows what to do.

**中文**

是的。问题是，你刚才提到的属于训练（training），还是推理执行（inference）？它属于训练。也就是你在最开始做这件事。你想要一段固定的 prompt，向 LLM 解释如何使用它，如何使用那个函数。所以，通常你会离线（offline）完成这件事。你离线迭代那段说明，明确说明如何使用 prompt、如何使用函数。然后，在 inference 时，把那段固定说明和函数 API 放在一起，让它对于任何查询都知道该做什么。

### [1:20:24](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=4824s) · b000160

**English**

Does that make sense? OK. Great. Any other questions here?

**中文**

这样说清楚吗？好。很好。这里还有其他问题吗？

### [1:20:35](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=4835s) · b000161

**English**

OK. Amazing.

**中文**

好。太好了。

### [1:20:38](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=4838s) · b000162

**English**

I just mentioned an example with teddy bears that would be in the category of maybe informational.

**中文**

我刚才举了一个泰迪熊的例子，它大概属于信息类（informational）。

### [1:20:48](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=4848s) · b000163

**English**

So you have a question and you want to ask some external API to retrieve that. And you have in reality a lot more use cases that you might see. So one actually mentioned, you have some cutoff dates. And let's say you ask your LLM about news of the day. So you typically wouldn't have anything that comes from the model itself. You would have an API that fetches it from a tool called maybe Search. But you have also other kinds of tools available in the information category.

**中文**

也就是，你有一个问题，想请求某个外部 API 来获取相关信息。实际上，你还会看到更多使用场景。刚才有人提到过，模型有知识截止日期（cutoff dates）。假设你向 LLM 询问当天的新闻，通常模型本身无法提供这些内容。你会有一个 API，通过一个也许叫 Search 的工具来获取它。不过，在信息类中，还有其他类型的工具可用。

### [1:21:20](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=4880s) · b000164

**English**

So for example, whether stocks and, let's see, but you also have other categories. For example, if you want to ask the model to do some calculation for you. You could let the model figure it out with some reasoning chain. But one way to get around it is to transform the query into code, execute that code, and then read out the answer.

**中文**

例如，whether \[字幕疑误，可能指 weather，即天气\]、股票，还有，让我看看，不过你也有其他类别。例如，如果你想让模型替你做一些计算，可以让模型通过某种推理链（reasoning chain）来算出来。但另一种解决方法是把查询转换成代码，执行代码，然后读出答案。

### [1:21:51](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=4911s) · b000165

**English**

So this is why tool call has a whole span of applications in the computation area. So you have calculations. And you have another category that we can cite here. So you can take actions on behalf of the user. So let's say you have a tool that sends emails. You could ask the model to send an email for you, and it could put the right things into the header and the message body, and even hit Send for you because you have that component that interacts with the external world as part of the tool API.

**中文**

这就是为什么 tool call 在计算领域有着广泛的应用。你可以做计算。这里还有另一类可以举出来，就是代表用户采取行动。假设你有一个发送电子邮件的工具，你可以让模型替你发送一封邮件，它能把正确的内容填入邮件头和正文，甚至替你点击 Send，因为 tool API 中包含了与外部世界交互的组件。

### [1:22:33](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=4953s) · b000166

**English**

Yeah. So these are just a few examples, but I just want to say that the field of tool calling is so powerful. You can do anything you want. And in practice, exactly as you mentioned, you wouldn't have just a single tool API as part of the context. You would have several ones because your LLM is not just an LLM for finding bears. You might want to do other things with your LLM. Maybe you want to hug a teddy bear or check a teddy bear's moods, send teddy bear's a gift and other things.

**中文**

是的。这些只是几个例子，但我想说的是，tool calling 这个领域非常强大。你可以做任何想做的事。实际上，正如你刚才提到的，上下文中不会只有一个 tool API，而是会有多个，因为你的 LLM 并不只是一个用来找熊的 LLM。你可能还想让它做其他事情。也许你想拥抱一只泰迪熊，或者查看泰迪熊的心情，给泰迪熊送礼物，以及其他事情。

### [1:23:11](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=4991s) · b000167

**English**

So you have a lot more functions that might be relevant to be added as a preamble. Just because you don't know what function would need to be used, you just need to put all of that just in case.

**中文**

所以，还有很多可能相关的函数可以加入 preamble。只是因为你不知道会需要哪个函数，所以只能把这些全都放进去，以备不时之需。

### [1:23:28](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=5008s) · b000168

**English**

The setup is exactly the one that you mentioned where you don't have just one API but multiple ones.

**中文**

这个设定正是你提到的那种：你拥有的不只是一个 API，而是多个。

### [1:23:36](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=5016s) · b000169

**English**

Does anyone see any issues with doing so?

**中文**

有人看出这样做有什么问题吗？

### [1:23:43](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=5023s) · b000170

**English**

So the suggestion is that, that's a lot of tools. And then you're right. So typically, if you have too many tools, you have the problem that Afshine mentioned at the beginning of a needle in a haystack, where maybe some tool API will get lost in the context and you don't really what to use. You have a lot of conflicting APIs, maybe, and we're going to see very soon how to overcome that issue. OK. Great. So I want to take a pause here and summarize how far we've come and some of the drawbacks that we have and see together what we could do to remedy these drawbacks.

**中文**

刚才的意见是，工具太多了。你说得对。通常，如果工具太多，就会出现 Afshine 开头提到的大海捞针（needle in a haystack）问题：某个 tool API 可能会淹没在上下文中，你不太清楚应该使用什么。也许会有很多相互冲突的 API，我们很快就会看到如何克服这个问题。好。很好。我想在这里暂停一下，总结目前讲到的内容，以及存在的一些缺点，一起看看可以怎样弥补这些缺点。

### [1:24:27](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=5067s) · b000171

**English**

So first, we saw that we came from an LLM that just responded back at you with a normal words. To an LLM that can actually interact with the outside world, fetch real-time information, or even extends computing capabilities. And exactly like overcomes the issue that Afshine was mentioning the knowledge cutoff one in a different way that than what RAG would do.

**中文**

首先，我们看到，LLM 从只能用普通文字回复你，发展到能够真正与外部世界交互、获取实时信息，甚至扩展计算能力。而且，它以不同于检索增强生成（retrieval-augmented generation，RAG）的方式，克服了 Afshine 提到的知识截止问题。

### [1:24:58](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=5098s) · b000172

**English**

So you could see these two methods as being complementary. And yeah, both try to do the same thing in some sense. But exactly as someone mentioned here, if you have more tools, then your context window might have things that it doesn't need. And then if you try to support so many cases, you might end up being mediocre at all of them. So this is an issue.

**中文**

所以，你可以把这两种方法看作互补的。是的，从某种意义上说，它们都在尝试做同一件事。但正如这里有人提到的，如果工具更多，上下文窗口中可能就会包含不需要的内容。而且，如果你试图支持太多场景，最终可能在所有场景中的表现都很平庸。这是一个问题。

### [1:25:30](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=5130s) · b000173

**English**

And even if that wasn't an issue, you still have the context window that is finite. So let's say you have hundreds of millions of users that use your LLM and that want to use to do a lot of things. You cannot support everyone's use cases at once, just because you couldn't possibly fit all of such tools in your context.

**中文**

即使这不是问题，上下文窗口仍然是有限的。假设有数亿用户使用你的 LLM，想用它做很多事情。你无法同时支持所有人的使用场景，因为你根本不可能把所有这些工具都放进上下文里。

### [1:25:55](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=5155s) · b000174

**English**

And then last, when I mentioned these tools, these are things I hand wrote. And maybe each LLM has their own way of defining and using tools. We're going to see if there is a way to standardize, maybe the way we define and use tools later on. So do these drawbacks make sense. Yeah. OK. Great. So let's move on to tool selection.

**中文**

最后，我提到的这些工具，都是我手写的。每个 LLM 可能都有自己定义和使用工具的方式。稍后我们会看看，是否有办法把工具的定义和使用方式标准化。这些缺点都能理解吗？是的。好。很好。接下来讲 tool selection。

### [1:26:26](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=5186s) · b000175

**English**

So let's see what we could do in order to make a tool use more scalable. So I'm going to cite here a technical paper from Google DeepMind, which uses a tool selector system. So it functions in two steps. So first you have your query and you have a list of tools that can be as big as you want. And a list of tools only contains the API name and, maybe one or two words about what it does.

**中文**

我们来看看，可以怎样让工具使用（tool use）更具可扩展性。这里我要引用 Google DeepMind 的一篇技术论文，其中使用了一个工具选择器（tool selector）系统。它分两步运行。首先，你有查询，以及一个工具列表，这个列表可以任意大。工具列表只包含 API 名称，也许再加上一两个词说明它的作用。

### [1:27:03](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=5223s) · b000176

**English**

So you have this prompt and the list of tools. And we ask the LLM to pick the tools that might be relevant. So this is why the technical paper calls this system tool selector. You could even see the term router being pronounced in the literature. So tool selection, routing are similar concepts. And the goal here is to restrict the number of tools to only those that might be useful.

**中文**

你有这个 prompt 和工具列表，然后让 LLM 选择可能相关的工具。这就是为什么那篇技术论文把这个系统称为 tool selector。你甚至可能在文献中看到路由器（router）这个术语。tool selection 和路由（routing）是相似的概念。这里的目标，就是把工具数量限制为那些可能有用的工具。

### [1:27:38](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=5258s) · b000177

**English**

And in the second stage, you take all the selected tool APIs and feed only those to the context alongside your query. And this is one way you could take to overcome this issue of having too many tools at once.

**中文**

第二个阶段，你把所有选中的 tool API 与查询一起放入上下文，只提供这些 API。这是一种可以用来克服同时存在过多工具这一问题的方法。

### [1:28:01](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=5281s) · b000178

**English**

Is everyone convinced that tool selection could be a good way to fix the problem here?

**中文**

大家都认同 tool selection 可能是解决这里这个问题的好方法吗？

### [1:28:14](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=5294s) · b000179

**English**

So the question is that basically RAG? You could do it with RAG. That's a great point. But it doesn't necessarily have to. So you could have an LLM that does this job, just picking the right tools. And you ask some instructions to the LLM to output the right answer. You could definitely do it with RAG. That is just a great point. Yeah.

**中文**

问题是，这基本上不就是 RAG 吗？你可以用 RAG 来做。这个观点很好。但不一定非得用它。你可以让一个 LLM 来完成这项工作，只负责选择正确的工具。你给 LLM 一些指令，让它输出正确答案。你当然可以用 RAG 来做。这确实是个很好的观点。是的。

### [1:28:40](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=5320s) · b000180

**English**

So does it make sense to everyone? OK. Great. And I see time is flying. So we're going to go very quickly on the standardization issue. So as I mentioned, every tools implementation, like the way you specify a tool implementation can be bespoke to a given LLM. And you wouldn't want that. Because for every LLM, you might need to implement always these tools over and over again.

**中文**

大家都理解吗？好。很好。我发现时间过得很快，所以我们会快速讲一下标准化问题。正如我提到的，每个工具的实现，比如你指定工具实现的方式，都可能是针对某个 LLM 定制的。你不会希望这样，因为对于每个 LLM，你可能都得一遍又一遍地重新实现这些工具。

### [1:29:14](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=5354s) · b000181

**English**

And duplication is not what you want. This is why there is a standard called MCP, that I know a lot of people talk about it. So it's something from the Anthropic team that standardizes the way tools are exposed to models. So it's a protocol. It's called a model context protocol. And it defines a standard way of presenting these tools. So I'm going just to say the very big lines of it, so you have this kind of vocabulary as part of MCP.

**中文**

重复工作并不是你想要的。这就是为什么有一个叫 MCP 的标准，我知道很多人都在谈论它。这是 Anthropic 团队推出的东西，用来标准化向模型开放工具的方式。它是一种协议，叫作模型上下文协议（model context protocol，MCP）。它定义了展示这些工具的标准方式。我只会介绍它的大致内容，让大家了解 MCP 中的这类术语。

### [1:29:53](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=5393s) · b000182

**English**

So you have an MCP server, which is the instance that serves tools. And then tools are implementations of the functions that you want people to use. Prompts are templates that could show the user how to use these tools. And then all of these can anchor on resources, which are external databases that you can use to complete the task.

**中文**

你有一个 MCP 服务器（MCP server），它是提供工具的实例。工具（tools）则是你希望人们使用的函数的实现。提示词（prompts）是一些模板，可以向用户展示如何使用这些工具。然后，所有这些都可以依托资源（resources），也就是可用于完成任务的外部数据库。

### [1:30:25](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=5425s) · b000183

**English**

And then an MCP server, when you use it, has a one-to-one connection with a piece of infrastructure in your LLM host that is called MCP clients. But these are maybe infrastructure details. And I just want to ground what I just mentioned in reality. So we know our teddy bear loves to read poetry. So in the case of recommending a poetry book to our teddy bear, you could think of a MCP server that provides tools that are linked to books.

**中文**

当你使用 MCP server 时，它与你的 LLM 宿主（LLM host）中一块称为 MCP 客户端（MCP clients）的基础设施建立一对一连接。不过，这些可能属于基础设施细节。我想把刚才提到的内容对应到现实例子。我们知道，我们的泰迪熊喜欢读诗。那么，在向泰迪熊推荐诗集这个场景中，你可以设想一个 MCP server，它提供与图书有关的工具。

### [1:30:59](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=5459s) · b000184

**English**

So your LLM hosts here--so let's just take the example of Claude since MCP is from Anthropic. So Claude would be your LLM host. Your MCP server would be probably implemented by your book provider. Because typically, they are the most experts as at serving such content. And we could assume that the book provider, MCP server has tools regarding finding books or recommending them. And then the prompts here could be a ways to show you how to find a given title, or maybe recommend it with respect to some flavor, maybe with respect to the user's test taste.

**中文**

这里的 LLM host——既然 MCP 来自 Anthropic，我们就以 Claude 为例。Claude 就是你的 LLM host。你的 MCP server 可能由图书提供方来实现，因为通常他们最擅长提供这类内容。我们可以假设，图书提供方的 MCP server 有查找或推荐图书的工具。这里的 prompts 则可以展示如何查找某个书名，或者根据某种风格，也许根据用户的 test taste \[字幕疑误，可能指 taste，即喜好\] 来推荐它。

### [1:31:42](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=5502s) · b000185

**English**

And some examples of resources here could be the teddy bear's personal collection, or maybe top books that people buy, just as an example. OK. Awesome. So now, I'm going to come to potentially the most exciting part of today's lecture, which is agents. So we saw how much more powerful LLMs could become with tools. Agents could be seen as one layer up from it.

**中文**

这里的 resources 可以是泰迪熊的个人藏书，也可以是大家购买最多的图书，只是举个例子。好。太好了。现在，我要讲今天这堂课中可能最令人兴奋的部分，也就是智能体（agents）。我们看到了，工具可以让 LLM 变得强大得多。agents 可以看作是在此基础上更高的一层。

### [1:32:16](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=5536s) · b000186

**English**

So I'm going to give first a definition, just so that we agree of what agent means here. So it's a system that autonomously pursues goal and completes tasks on a user's behalf. So compared to tools, you not only can perform tasks, but you have also some reasoning involved in it. So you could have multiple loops of iterations.

**中文**

我会先给出一个定义，让我们对这里 agent 的含义达成一致。它是一个代表用户自主追求目标并完成任务的系统。所以，与工具相比，你不仅能执行任务，其中还涉及一些 reasoning。因此，你可以有多轮迭代循环。

### [1:32:47](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=5567s) · b000187

**English**

And this is what differentiates an agent from a tool in plain terms. When usually people talk about agents, it has that recurrence or higher level of reasoning baked into it. And so I'm going to contrast like the agentic world with respect to the world we have seen, where you may have multiple calls to tools. And these new agentic framework is not necessarily disjoint from the ones that we presented before.

**中文**

简单来说，这就是 agent 与工具的区别。通常，人们谈到 agents 时，指的就是其中内置了这种循环，或者更高层次的 reasoning。接下来，我会把智能体式（agentic）的世界，与我们已经看到的、可能会多次调用工具的世界作比较。这些新的 agentic 框架与此前介绍的那些并不一定互不相交。

### [1:33:25](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=5605s) · b000188

**English**

You could well have reasoning chains inside of it. So it's like a potentially overlapping. But the structure consists of tool calls and iterations. OK. Great. And now, I'm going to talk about a hallmark paper called ReAct, to reason plus acts, which decomposes possible loops into different stages.

**中文**

其中完全可以包含 reasoning chains。所以，它们可能存在重叠。但其结构由 tool calls 和迭代组成。好。很好。现在我要介绍一篇标志性的论文，叫 ReAct，也就是推理加行动（reason plus acts），它把可能的循环拆分成不同阶段。

### [1:33:58](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=5638s) · b000189

**English**

So very oftentimes, when you have a query and you want to pursue a goal, you cannot do it one shot. You need somehow to decompose the goal into actionable substeps, perform each of these steps, and then come up with the answer. And this is exactly what ReAct is about. It's about decomposing complex tasks into loops of things that can be done atomically.

**中文**

很多时候，当你有一个查询，想要达成一个目标时，无法一次完成。你需要以某种方式把目标拆解成可执行的子步骤，逐一执行这些步骤，然后得出答案。这正是 ReAct 的核心：把复杂任务拆解成由可作为原子操作执行的事项构成的循环。

### [1:34:31](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=5671s) · b000190

**English**

So here, I just want to say one thing. We decompose these steps into observe, plan, and act. But it doesn't necessarily have to be called that way or be in that order. For example, the ReAct paper, I think, introduces terms think, observe, act. You might see the language changing a bit from paper to paper to paper. But the high-level intuition remains.

**中文**

这里我想说明一点。我们把这些步骤分为观察（observe）、规划（plan）和行动（act）。但它们不一定非得这样命名，也不一定按这个顺序。例如，我记得 ReAct 论文引入的术语是思考（think）、observe、act。不同论文中的用语可能会有些变化，但高层次的直觉是一致的。

### [1:35:02](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=5702s) · b000191

**English**

So let's just ground on a very specific example. So to be in the theme of these days weather, it starts becoming a bit cold. And our teddy bear might be cold in its home. So let's just have that as an input. My teddy bear is cold. Please, do something. And let's see what an agentic workflow could do about it. So first, you have this observe stage, which translates the user query into an actionable formulation.

**中文**

我们来看一个非常具体的例子。为了贴合这几天的天气，天气开始变得有点冷，我们的泰迪熊在家里可能会觉得冷。就把这个作为输入：我的泰迪熊很冷。请做点什么。我们来看看，agentic 工作流（agentic workflow）能对此做些什么。首先，是 observe 阶段，把用户查询转换成一种可执行的表述。

### [1:35:38](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=5738s) · b000192

**English**

So when you say that your teddy bear is cold and you ask it to do something like here, in this observe stage, you would link it back to the notion of temperature. The user's teddy bear is cold, which may be due to the current temperature of the room, which is currently unknown. So right off the bat, you now know that you need to do something with temperatures. So this brings us to the next step called Plan, where that something is unknown, and you need to find it.

**中文**

当你说泰迪熊很冷，并像这里这样要求它做点什么时，在 observe 阶段，你会把这件事关联到温度这个概念。用户的泰迪熊很冷，可能是因为房间当前的温度，而这个温度目前未知。所以，一开始你就知道，需要针对温度做些什么。这把我们带到下一步，叫 Plan：某件事尚不明确，而你需要把它弄清楚。

### [1:36:12](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=5772s) · b000193

**English**

Plan will spell that out for you. So here, you want to determine the temperature of the room. And luckily, among your tools, you might have something that does something in these lines. And this is where you use it. So the Act stage is using all these APIs that might be in the context. So for example here, if you have get current room temperature, this is the way to use it. And as I mentioned, these tools are useful to the LLM when you output information back to it that it can interpret.

**中文**

Plan 会把它明确表达出来。这里，你想确定房间的温度。幸运的是，在你的工具中，可能有某个工具能完成类似的事情。这就是使用它的时候。所以，Act 阶段就是使用上下文中可能存在的这些 API。例如这里，如果你有 get current room temperature，这就是使用它的方式。正如我提到的，当这些工具把 LLM 能够解释的信息输出回给它时，它们才对 LLM 有用。

### [1:36:47](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=5807s) · b000194

**English**

So this tool returns the temperature. And you need now to interpret what the temperature means. So this is why you go back to the observed stage.

**中文**

这个工具会返回温度。现在，你需要解释这个温度意味着什么。这就是为什么要回到 observed 阶段 \[字幕疑误，可能指 observe 阶段\]。

### [1:37:02](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=5822s) · b000195

**English**

You describe what the world looks like and what you should do about it. So here, you can read that the temperature of the room is cold. It's 65 Fahrenheit, and the observed stage might indicate that it's colder than expected. So this is why you need to plan something. And then at the Plan stage, you're like this, this was colder than expected. So I need to increase the temperature. And then you go back to the Act stage.

**中文**

你描述世界现在是什么样，以及应该对此做什么。这里，你可以读到房间温度偏冷，是 65 华氏度，observed 阶段 \[字幕疑误，可能指 observe 阶段\] 可能会指出，这比预期更冷。所以，你需要规划一些事情。然后，在 Plan 阶段，你会想：这，这比预期更冷，所以我需要提高温度。接着，你又回到 Act 阶段。

### [1:37:32](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=5852s) · b000196

**English**

Luckily, how to increase the temperature. And it has a function that can have the temperature increase arguments and put it to it, so you can adjust the temperature. And then once it's done, the observed stage concludes that the temperature is not set to the correct temperature. And this is the time where you can exit the loop and return the response to the user.

**中文**

幸运的是，如何提高温度。它有一个函数，可以接收温度增量参数，把参数传进去，就能调节温度。完成之后，observed 阶段 \[字幕疑误，可能指 observe 阶段\] 得出结论：温度尚未设为正确温度 \[字幕疑误，原文为 not，结合下文可能指 now，即现在已设为正确温度\]。这时，就可以退出循环，把响应返回给用户。

### [1:38:06](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=5886s) · b000197

**English**

So here, we have increased the temperature by 5 degrees. And then the output reads that back to the user in the hope that it has fulfilled the user's query. So what I described within the loop is what makes a workflow an agentic one. So you have some initial query. You have some actions that you can perform. And then at each stage, the LLM tries to see if it has reached the goal yet.

**中文**

这里，我们把温度提高了 5 度。然后，输出会向用户说明这件事，希望已经满足用户的查询。我在循环中描述的这些，就是让一个工作流成为 agentic 工作流的原因。你有一个初始查询，有一些可以执行的动作。然后，在每个阶段，LLM 都会尝试判断自己是否已经达成目标。

### [1:38:39](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=5919s) · b000198

**English**

And then if it has, then it will go to the output stage. Otherwise, it may have more reasoning loops, where it does more work. So does the definition of agent that I propose here make sense?

**中文**

如果达成了，就会进入输出阶段。否则，它可能还会经历更多 reasoning 循环，继续做更多工作。我在这里提出的 agent 定义，大家能理解吗？

### [1:39:00](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=5940s) · b000199

**English**

OK. Great. So now taking this a bit further, you could think of way more than one agent. You could have an agent for setting the thermostat. But maybe in your home, you want to manage how energy is distributed, or air quality, if you have some settings to tune. So you can have different agents. And one interesting use case is to have the user say something to an agent, and potentially have all of them communicate together.

**中文**

好。很好。再往前一步，你可以设想不止一个 agent。你可以有一个负责设置恒温器的 agent。但在家里，你也许还想管理能源如何分配，或者空气质量，如果有一些设置可以调节的话。所以，你可以有不同的 agents。一个有意思的使用场景是，让用户对一个 agent 说些什么，然后可能让所有 agents 相互交流。

### [1:39:33](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=5973s) · b000200

**English**

So these prompts potential needs for also a standardization of communications between agents, similarly to what we have seen between LLM hosts and tools. And this is what prompted Google to release the Agent2Agent protocol earlier this year. So yeah, highly recommend taking a look at their document specification. But just to give the main lines around it, you have some standardization of what an agent can expose.

**中文**

这就带来了对 agents 之间通信进行标准化的潜在需求，类似于我们看到的 LLM hosts 与工具之间的标准化。这也促使 Google 在今年早些时候发布了 Agent2Agent 协议。是的，非常推荐大家去看看它的规范文档。不过，简单介绍一下，它对 agent 可以开放哪些内容做了一些标准化。

### [1:40:12](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=6012s) · b000201

**English**

So it typically exposes a set of skills. So it can do things. And then it gives examples about it so that other agents are aware of it. And what you need to do as a developer would be to define these skills. And also, another key thing is to define how the agent executes a given request. So for example, when you execute a given query, what is the status that you emit to other agents?

**中文**

通常，它会开放一组技能（skills），也就是它能做哪些事情。然后，它会给出相关示例，让其他 agents 了解这些能力。作为开发者，你需要做的就是定义这些 skills。另外一个关键点，是定义 agent 如何执行给定的请求。例如，当你执行某个查询时，会向其他 agents 发出什么状态？

### [1:40:44](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=6044s) · b000202

**English**

Or there is a cancel method, as well, where let's say an agent says, stop what you're doing. What is the process to cancel an action? So these are some of the main functions like the Agent2Agent protocol asks people to fill out. Yeah?

**中文**

此外，还有一个 cancel 方法。假设某个 agent 说：停止你正在做的事。那么，取消某个动作的流程是什么？这些就是 Agent2Agent 协议要求人们填写的一些主要函数。嗯？

### [1:41:14](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=6074s) · b000203

**English**

So the question is, is each agent an LLM with some context to do some tasks? So you could definitely imagine it be the case. Typically, in the example that I mentioned here, yes. And the agents operate independently. So they have their own reasoning loops. And all the other agency is the input and output.

**中文**

问题是，每个 agent 是否都是带有一些上下文、用于完成某些任务的 LLM？你完全可以这样设想。通常，在我这里举的例子中，是这样的。而且，这些 agents 独立运行，各自有自己的 reasoning 循环。而其他 agency \[字幕疑误，可能指 agents see，即其他 agents 所看到的\] 就是输入和输出。

### [1:41:51](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=6111s) · b000204

**English**

Yeah. So the remark here is maybe your token budget can go all over the place. So you can have some budget restrictions put in place. This is a good point. But each of these agents, they would not eat on each other's budgets. It might eat on your money budget, but this is indeed a concern. So I'm going to move on to the topic of safety, which I have not mentioned so far.

**中文**

是的。这里的意见是，你的 token 预算可能会变得难以控制。你可以设置一些预算限制。这个观点很好。但这些 agents 不会消耗彼此的预算。它们可能会消耗你的金钱预算，但这确实是一个需要关注的问题。接下来我要转向安全（safety）这个话题，目前还没有提到过。

### [1:42:23](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=6143s) · b000205

**English**

But that is very important because with these new capabilities comes a whole string of new potential issues. And you have seen these models. They have now the ability to execute actions for you. So you could think of some harmful actor doing things that you wouldn't want for you. And I give one example here that could be a concern--data exfiltration. So let's say you have access to a tool that can write in a public visible way data.

**中文**

但这非常重要，因为这些新能力会带来一整串新的潜在问题。你们已经看到，这些模型现在能够替你执行动作。所以，你可以想象，某个恶意行为者可能会做一些你不希望发生的事。这里我举一个可能令人担忧的例子：数据外传（data exfiltration）。假设你可以使用一个工具，它能以公开可见的方式写入数据。

### [1:43:00](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=6180s) · b000206

**English**

So let's say you have, I don't know some email agent. So if you have a prompt that, for example, says, write my password, which potentially the tool could have access to to an email to that address, you could exfiltrate data that belongs to the user out of it. So this is typically one risk that you might have. You can have other safety risks. And I link the paper here that goes through some of them. So tool sort.

**中文**

假设你有一个，比如说，电子邮件 agent。如果有一个 prompt，例如说，把我的密码——工具可能能够访问它——写入一封发往那个地址的电子邮件，那么就可能把属于用户的数据外传出去。这通常是你可能面临的一种风险。还可能有其他安全风险。我在这里链接了一篇论文，介绍了其中一些风险。就是 tool sort \[字幕疑误，可能指 ToolSword\]。

### [1:43:32](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=6212s) · b000207

**English**

So I recommend a read.

**中文**

所以，我推荐读一下。

### [1:43:36](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=6216s) · b000208

**English**

Now, you might ask, what could you do to get around it? So you have typically two classes of remediations. One that might come at the training stage where, if you recall the training process of R1 or even other models, you have these harmlessness components. So you typically have data as part of the data mixtures that you train during SFT and reinforcement learning that could cover safety.

**中文**

现在，你可能会问，可以怎样解决这个问题？通常有两类缓解措施（remediations）。一类可以在训练阶段实施。如果你还记得 R1 或其他模型的训练过程，其中包含无害性（harmlessness）部分。所以，在 SFT 和强化学习（reinforcement learning）的训练数据混合中，通常会有一些涵盖安全问题的数据。

### [1:44:11](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=6251s) · b000209

**English**

So this is where you could remedy these issues. You have another option. Let's say, you have a query that has gone through your lines of defenses, your training lines of defenses. You can also have inference safeguards. For example, safety classifier that looks at the conversation so far, and that judges whether the output of the LLM is going to be safe or not. So you have even that as a safeguard.

**中文**

你可以在这里缓解这些问题。还有另一种选择。假设某个查询已经突破了你的防线，也就是训练阶段的防线，你还可以设置推理阶段防护措施（inference safeguards）。例如，安全分类器（safety classifier）会查看截至目前的对话，判断 LLM 的输出是否安全。所以，这也可以作为一道防护。

### [1:44:42](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=6282s) · b000210

**English**

And just as a pointer, I'm going to talk about that agent safety bench, which summarizes the span of possible safety hazards and offers a benchmark, a full suite for it. So people can refer to these benchmarks to know whether their LLM is safe.

**中文**

另外，提供一个参考方向，我想提一下 agent safety bench \[字幕疑误，可能指 AgentSafetyBench\]，它总结了各种可能的安全隐患，并提供了一个基准测试（benchmark），一整套测试。人们可以参考这些 benchmarks，了解自己的 LLM 是否安全。

### [1:45:08](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=6308s) · b000211

**English**

And it's a very important topic. And just yesterday, Anthropic revealed that there were the victims of a large scale cyber attack launched from Claude. So this is an issue that is--so it was also using tools and agentic capabilities, and they published super detailed report, saying exactly what the attackers did and went step-by-step through possible lines of remediations.

**中文**

这是一个非常重要的话题。就在昨天，Anthropic 披露，他们遭受了一场通过 Claude 发起的大规模网络攻击。所以，这是一个问题——那次攻击也使用了工具和 agentic 能力。他们发布了一份非常详细的报告，明确说明攻击者做了什么，并逐步介绍可能采取的缓解措施。

### [1:45:40](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=6340s) · b000212

**English**

And this is just to emphasize how important safety is in this more capable world. And both attackers and the line of defense can be more and more sophisticated. So it's not a lost battle, it's just that the tools we have for defending against like tool-based attacks need to be--so we need to have such measures in place. And with these measures, maybe it's going to be fine.

**中文**

这只是为了强调，在能力更强的这个世界里，安全有多重要。攻击者和防御手段都可能变得越来越复杂。所以，这并不是一场已经输掉的战斗，只是我们用来防御基于工具的攻击的工具需要——也就是说，我们需要落实这类措施。有了这些措施，也许情况就会没问题。

### [1:46:11](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=6371s) · b000213

**English**

So I think that was the overall mindset of that article, which I strongly recommend to read.

**中文**

我想，这就是那篇文章的整体思路，我强烈推荐大家阅读。

### [1:46:21](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=6381s) · b000214

**English**

I'm going to say a last few words. So when you talk about agents, you have this risk that at every step of your thought process, you might diverge to something that just doesn't work. So that is a huge problem. Let's say if the model doesn't grounds to the output properly, or maybe does a mistake into the argument prediction of a tool call, so this is one big issue, which is the reason why you don't see large scale agents ruling the world right now, because it's really like, we are limited by these consequences.

**中文**

最后再说几句。当你谈论 agents 时，会存在这样一种风险：在思考过程的每一步，都可能偏离到某条行不通的路径上。这是一个大问题。比如，模型没有正确以输出为依据（grounding），或者在预测某次 tool call 的参数时出错，这都是严重问题。这也是为什么我们现在还没有看到大规模 agents 统治世界，因为我们确实受到了这些后果的限制。

### [1:47:01](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=6421s) · b000215

**English**

And then I'm going to talk about the developing capabilities of models that enable you to have this agentic capabilities. So this is something that you can fix with SFT. But ideally, you wouldn't want to use SFT to fix reasoning gaps and use the model itself. And we're going to see next week what the evaluation landscape looks like. So I'm going to reserve it to next week. And just a few words of advice regarding building tools or building agents, always start small on a very simple case.

**中文**

然后，我要谈谈模型不断发展的能力，这些能力让 agentic 能力成为可能。这是可以用 SFT 修复的事情。但理想情况下，你不会希望用 SFT 来弥补 reasoning 上的缺口，而是希望利用模型本身。下周我们会看看评估领域的情况，所以我把这个留到下周。再给大家几句关于构建工具或 agents 的建议：始终从一个非常简单的小场景开始。

### [1:47:41](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=6461s) · b000216

**English**

For example, find the nearest bear. Try to see if your current implementation and prompts just works and then start from there. So start small and then start smart. So take the most capable model first so that you know the headroom of where you can go with the current models, and then try to gain on latency capabilities and so on. Start correct, start small, and then you can optimize later.

**中文**

例如，找到最近的熊。先看看你当前的实现和 prompt 是否有效，然后再从那里出发。所以，先从小处着手，再聪明地起步。先使用能力最强的模型，让你知道当前模型能达到的上限，然后再尝试改善延迟等方面。先做正确，从小处开始，之后再优化。

### [1:48:15](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=6495s) · b000217

**English**

And when it comes to debuggability, these LLMs they output chains of reasoning. So it's always good to look at them, to see what is going wrong. And I will close this lecture on a note. My favorite use case of using agents right now is as an AI assistant coding. So this is something I strongly recommend in case you have a project that requires you to do complex piping of things. You can free your mental load by delegating some of these tasks.

**中文**

说到可调试性（debuggability），这些 LLM 会输出 reasoning 链。所以，查看这些内容、看看哪里出了问题，总是有帮助的。最后，我想用一点感想结束这堂课。目前，我最喜欢的 agents 使用场景是作为 AI 编程助手。如果你的项目需要做复杂的衔接工作，我非常推荐这种方式。把其中一些任务委派出去，可以减轻你的脑力负担。

### [1:48:49](https://www.youtube.com/watch?v=h-7S6HNq0Vg&t=6529s) · b000218

**English**

And this is something that is you're going to see in the real world, very much used now, but with the caveat that, please make sure to learn the foundations of codes, know how to code right, because your taste is going to matter most from now on. Generating code is cheap, but judging whether a code is correct, and does the right thing, this is the hard part. And with that, thank you. \[APPLAUSE\]

**中文**

你会在现实世界中看到，这种方式现在已经得到广泛使用。但要提醒一点：请务必学习代码的基础，知道如何正确编程，因为从现在起，你的判断品味会最重要。生成代码很便宜，但判断代码是否正确、是否做了该做的事，才是困难的部分。就到这里，谢谢大家。\[掌声\]
