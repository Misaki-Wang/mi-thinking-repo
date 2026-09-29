# Stanford CME295 Transformers &amp; LLMs \| Autumn 2025 \| Lecture 5 - LLM tuning

_Bilingual transcript · 双语讲稿_

- Channel: Stanford Online
- Source: [YouTube](https://www.youtube.com/watch?v=PmW_TMQ3l0I)
- Duration: 1:47:41
- Caption source: manual
- Status: complete
- Chinese translation: 221/221
- Translation provider: codex
- Generated: 2026-09-29T16:05:19+00:00

## Transcript · 讲稿

### [00:05](https://www.youtube.com/watch?v=PmW_TMQ3l0I&t=5s) · b000001

**English**

Cool. Hello, everyone. And welcome to Lecture 5 of CME295. So first of all, thank you all for taking the time to take the midterm last week. So I hope it was reasonable for you. So for those of you who are auditing, in case you are interested in taking the exam, just know that the exam and the solutions are both posted on the website. And so now, you know a little bit how the exam looks like.

**中文**

好。大家好，欢迎来到 CME295 第 5 讲。首先，感谢大家抽出时间参加上周的期中考试。希望你们觉得考试还算合理。对于旁听的同学，如果你们也有兴趣做这份试卷，试卷和答案都已发布在网站上。这样，你们现在对考试是什么样子也有了一些了解。

### [00:39](https://www.youtube.com/watch?v=PmW_TMQ3l0I&t=39s) · b000002

**English**

So for the final, we'll have the same format, except that the content will be on lectures 5, so this one, up until 9. So all good on that point? Cool. Great. So with that, we're going to start the lecture. So today, we're going to talk about LLM tuning. So as usual, we're just going to recap what we saw last time. So last time was already two weeks ago.

**中文**

期末考试的形式会相同，不过内容将涵盖第 5 讲，也就是这一讲，一直到第 9 讲。这一点大家都没问题吧？好。很好。那么，我们开始上课。今天我们要讲大语言模型调优（LLM tuning）。和往常一样，我们先回顾一下上次讲的内容。上次课已经是两周前了。

### [01:11](https://www.youtube.com/watch?v=PmW_TMQ3l0I&t=71s) · b000003

**English**

But we talked about how to train an LLM. And in particular, we've looked at two important steps. So the first one was called pre-training, where you're basically taking a model that has been initialized, and you're trying to teach the model about language, about code. So you have this step that is very time consuming, expensive, compute heavy, that is happening on a lot of data.

**中文**

我们讲了如何训练一个 LLM。具体来说，我们看了两个重要步骤。第一步叫作预训练（pre-training），基本上就是拿一个已经初始化的模型，尝试教会它语言和代码。这一步非常耗时、昂贵，需要大量计算，并且要在大量数据上进行。

### [01:44](https://www.youtube.com/watch?v=PmW_TMQ3l0I&t=104s) · b000004

**English**

So we've seen training optimizations on how to make that happen. So we've seen techniques to parallelize that across GPUs. So we've seen data parallelism methods and, in particular, 0. So the variant 0, 1, 2, 3. And we've also seen very quickly what model parallelism was in this case. So at the end of this step, what you obtain is a model that knows about the structure of language, about codes--basically, all the texts that it has been fed.

**中文**

我们看了如何通过训练优化来实现这一步。我们看了在多个 GPU 上并行执行的技术，看了数据并行（data parallelism）方法，尤其是 0 \[字幕疑误，可能指 ZeRO\]，也就是变体 0、1、2、3。我们还非常简要地看了这里的模型并行（model parallelism）是什么。完成这一步后，得到的模型了解语言的结构、代码，也就是基本上了解它接收过的所有文本。

### [02:20](https://www.youtube.com/watch?v=PmW_TMQ3l0I&t=140s) · b000005

**English**

But what this model can do is only predict the next token. So it's a great autocompleter, but it's not a helpful model yet, which is why we have a second step. And we saw here, it's typically called finetuning or SFT for Supervised Fine Tuning. So here what we do is we take our pre-trained model, and we train it for specific tasks.

**中文**

但这个模型能做的只有预测下一个词元（token）。所以，它是一个很棒的自动补全器，但还不是一个有用的模型，因此我们需要第二步。我们看到，这一步通常叫作微调（finetuning），或者监督微调（Supervised Fine Tuning，SFT）。这里我们要做的，就是拿预训练模型来针对特定任务进行训练。

### [02:50](https://www.youtube.com/watch?v=PmW_TMQ3l0I&t=170s) · b000006

**English**

So nowadays, you have ChatGPT and all these chat assistants. So this can be one application. So transforming your model into an assistant. And so here, the goal is to teach the model how to behave. So the model already knows what language is, what code is, et cetera. And you're just trying to make it behave like the use case that you're trying to tune it for. So typically here, what you have is a data set that is much smaller in scale, but of much higher quality.

**中文**

如今有 ChatGPT 和各种聊天助手。这可以是其中一种应用，也就是把模型变成一个助手。这里的目标是教模型如何表现。模型已经知道什么是语言、什么是代码，等等。你只是想让它按照你要为其调优的使用场景来表现。因此，这里使用的数据集通常规模小得多，但质量高得多。

### [03:28](https://www.youtube.com/watch?v=PmW_TMQ3l0I&t=208s) · b000007

**English**

And you're basically taking your model, your pre-trained model, and teaching it exactly which tokens to predict with the next token prediction task. And we've seen, LoRA, which is a parameter efficient method, which does not tune all the weights, but in a clever way, introduces low rank matrices that are the ones that are being tuned.

**中文**

基本上，你拿着模型，也就是预训练模型，通过下一个 token 预测任务，明确教它应该预测哪些 token。我们还看了 LoRA，这是一种参数高效（parameter efficient）的方法，它不会调优所有权重，而是巧妙地引入低秩矩阵（low rank matrices），实际调优的是这些矩阵。

### [03:59](https://www.youtube.com/watch?v=PmW_TMQ3l0I&t=239s) · b000008

**English**

And we had stopped there. So what we're going to see today is how to align the model to align with, what we call, human preferences. And so here, we're taking our model that has been finetuned for a specific task. And trying to align our model to make it more something that a human would like or that some metric that we're defining would be more aligned with that.

**中文**

我们上次就讲到这里。今天要看的是如何对齐（align）模型，使其符合我们所说的人类偏好（human preferences）。这里，我们拿一个已经针对特定任务微调过的模型，尝试对齐它，使它更符合人类的喜好，或者更符合我们定义的某个指标。

### [04:29](https://www.youtube.com/watch?v=PmW_TMQ3l0I&t=269s) · b000009

**English**

So as an example, let's suppose if you have an assistant at the end step 2. So it's very much possible that your assistant is behaving the way you want, but not, let's say, at the tone that you want. So it's not, let's say, friendly or it's not safe. So you want to tune those aspects in that third step.

**中文**

举个例子，假设你在第 2 步结束后得到了一个助手。它很可能已经按你希望的方式表现，但比如说，语气还不是你想要的。比如，它不够友好，或者不够安全。你就希望在第三步中调优这些方面。

### [04:56](https://www.youtube.com/watch?v=PmW_TMQ3l0I&t=296s) · b000010

**English**

Cool. So this step is called preference tuning. And we're going to exactly see what that is. So here for context, let's suppose that we have an SFT model. And so by SFT model, I mean a model that has gone through the pre-trained stage and the finetuning stage. And so for instance, we may ask our model to suggest a new activity we could do with our teddy bear. And here the model, let's say, responds with, "I would suggest you to not spend much time with your teddy bear at all."

**中文**

好。这一步叫作偏好调优（preference tuning），我们将具体看看它是什么。这里先设定一下背景，假设我们有一个 SFT 模型。所谓 SFT 模型，我指的是经过预训练阶段和微调阶段的模型。比如，我们可以让模型推荐一种可以和泰迪熊一起做的新活动。假设模型回答：“我建议你根本不要花太多时间和你的泰迪熊待在一起。”

### [05:31](https://www.youtube.com/watch?v=PmW_TMQ3l0I&t=331s) · b000011

**English**

So this is the response of an assistant, but it's not necessarily aligned with what we want. So the idea here is to take these, quote unquote, "bad outputs" and find an output or rewrite an output that we would want to have instead. So this pair would be what we call a preference pair. So in other words, given this prompt, we have two responses--one that we want to see, which is this one.

**中文**

这是一个助手的回答，但它不一定符合我们的期望。这里的思路是，拿这些加引号的“糟糕输出”，找到一个我们想要的输出，或者把输出改写成我们想要的样子。这一对就叫作偏好对（preference pair）。换句话说，给定这个提示词（prompt），我们有两个回答，一个是我们希望看到的，也就是这个。

### [06:08](https://www.youtube.com/watch?v=PmW_TMQ3l0I&t=368s) · b000012

**English**

And I'm going to read it in a second. And then the other one that we do not want to see. So for instance, in this example, the answer we want to see is, "Of course, teddy bears not only make awesome companions for a delightful sleep, but can also be great buddies for fun activities," and just like suggest some activities. Does the setup sound good? Yeah? So long story short, we want to align our model with human preferences.

**中文**

我马上读一下。另一个则是我们不希望看到的。比如在这个例子中，我们想看到的回答是：“当然，泰迪熊不仅是陪你甜美入睡的绝佳伙伴，也可以是一起进行有趣活动的好朋友。”然后推荐一些活动。这个设定大家觉得没问题吧？是吗？总而言之，我们希望让模型与人类偏好对齐。

### [06:41](https://www.youtube.com/watch?v=PmW_TMQ3l0I&t=401s) · b000013

**English**

So you may ask, we have this finetuning step already. Why would we want to have a third step? Well, during the second step, which is the finetuning stage, if you remember, what we did was construct a very high quality data set of the kinds of prompts on which we want our model to behave in a certain way. So in order to compose such a data set, it's actually something that is very time consuming and very actually difficult, because the data set must be of very high quality.

**中文**

你可能会问，我们已经有微调这一步了，为什么还需要第三步？在第二步，也就是微调阶段，如果你还记得，我们构建了一个质量很高的数据集，其中包含我们希望模型以某种方式回应的各类 prompt。构建这样的数据集实际上非常耗时，而且确实非常困难，因为数据集必须具有很高的质量。

### [07:21](https://www.youtube.com/watch?v=PmW_TMQ3l0I&t=441s) · b000014

**English**

And in this case, what we're doing is not really teaching the model exactly what it should generate, but rather telling the model what kind of output it should prefer. So we're less in "please generate that" kind of thing and more a "I prefer this option" kind of thing. And so typically, if we asked you write a poem, write a great poem from scratch, it would typically be much more difficult to do rather than just showing you two poems, one bad poem and one great poem, and ask you to just say which one is better.

**中文**

而在这里，我们并不是明确教模型应该生成什么，而是告诉它应该偏好哪种输出。所以，这更少是“请生成那个”，更多是“我更喜欢这个选项”。通常，如果我们让你写一首诗，从零开始写一首好诗，这通常会比直接给你看两首诗，一首差的、一首好的，然后让你说哪首更好，要困难得多。

### [08:11](https://www.youtube.com/watch?v=PmW_TMQ3l0I&t=491s) · b000015

**English**

So in order to obtain the data sets, it's already much easier. The second reason is--so during the SFT stage, when we compose our data set of very high quality, there is one aspect that we really try to get right, which is the distribution of prompts. And what I mean by that is if we have too much of a given of prompt, our model will be more biased towards responding in that particular way.

**中文**

因此，获取数据集本身就容易得多。第二个原因是，在 SFT 阶段构建高质量数据集时，有一个方面我们会特别努力地做好，那就是 prompt 的分布。我的意思是，如果某一类 prompt 太多，模型就会更偏向于以那种特定方式回答。

### [08:46](https://www.youtube.com/watch?v=PmW_TMQ3l0I&t=526s) · b000016

**English**

So what people try to do is to be careful about the distribution of prompts that are in the SFT data. And so here, let's say if our model misbehaves, if we were thinking about just adding one example in the SFT data set, well, we would have to be very careful about which prompt we're adding and whether it's not going to bias the model like too much in that direction. So that's the second reason.

**中文**

所以，人们会留意 SFT 数据中 prompt 的分布。假设我们的模型表现不当，如果我们只想着往 SFT 数据集中加一个例子，就必须非常谨慎地考虑加入的是哪个 prompt，以及它是否会让模型过度偏向那个方向。这是第二个原因。

### [09:17](https://www.youtube.com/watch?v=PmW_TMQ3l0I&t=557s) · b000017

**English**

And then, the third reason is what I mentioned, which is the SFT data is typically very high quality. So if you're looking at all the missteps that your model is doing and trying to put that in the SFT data, you'll just have a hard time. It takes a lot of time. But one note here is if your SFT data is misbehaving a lot, it may also be due to the fact that your SFT data set has some problem.

**中文**

第三个原因就是我刚才提到的，SFT 数据通常质量很高。因此，如果你逐一查看模型犯的所有错误，并试图把这些放进 SFT 数据里，就会很吃力。这需要很多时间。不过这里要说明一点，如果你的 SFT 数据频繁表现不当 \[原文如此，可能指 SFT 模型\]，也可能是因为你的 SFT 数据集存在一些问题。

### [09:51](https://www.youtube.com/watch?v=PmW_TMQ3l0I&t=591s) · b000018

**English**

So preference tuning is not the answer to everything. Maybe it's better sometimes to just check your SFT data set for some issues. Does that sound good? Yeah. \[AUDIO OUT\]

**中文**

所以 preference tuning 不是万能的。有时候，检查一下 SFT 数据集是否存在问题，可能会更好。这样说大家能理解吗？好。\[音频缺失\]

### [10:20](https://www.youtube.com/watch?v=PmW_TMQ3l0I&t=620s) · b000019

**English**

Yeah, so to do that in the preference tuning stage? OK, so the question is, we saw LoRA for SFT, what is the equivalent for preference tuning? So we'll see that later in the lecture. But you can think of LoRA as being some way to, I guess, reduce the number of parameters that you need to tune. That is slightly different with the objective function that you're using to train your model. And here, preference tuning, you can think of it more as a different objective function, but it may very well be something that you also use LoRA for.

**中文**

是说在 preference tuning 阶段这样做吗？好，问题是，我们在 SFT 中看到了 LoRA，那么 preference tuning 中对应的是什么？我们会在这节课后面讲到。不过，你可以把 LoRA 理解成一种减少需要调优的参数数量的方法。这和训练模型时使用的目标函数（objective function）略有不同。这里的 preference tuning，你可以更多地把它理解为一种不同的目标函数，但你完全也可以对它使用 LoRA。

### [10:56](https://www.youtube.com/watch?v=PmW_TMQ3l0I&t=656s) · b000020

**English**

So the two are not incompatible. But it will become more clear later on. But yeah, great question. One last thing I will add here is another difference with the SFT stage is that preference tuning allows us to inject some negative signal. Because SFT is all about teaching the model about what it should predict, but it does not teach the model about what it should not predict.

**中文**

所以，两者并不冲突。后面会更清楚。这个问题很好。我在这里再补充最后一点，与 SFT 阶段的另一个区别是，preference tuning 允许我们引入一些负向信号（negative signal）。因为 SFT 完全是在教模型应该预测什么，却没有教模型不应该预测什么。

### [11:30](https://www.youtube.com/watch?v=PmW_TMQ3l0I&t=690s) · b000021

**English**

And we will see that preference tuning allows you to inject some negative signal.

**中文**

我们会看到，preference tuning 允许你引入一些负向信号。

### [11:36](https://www.youtube.com/watch?v=PmW_TMQ3l0I&t=696s) · b000022

**English**

Cool. So to start, of course, we need to have our preference pairs. And so we're going to look at this data collection step first. So here's the setup. You have a prompt. Let's say write a poem. And you have a given response, which is the poem that is being generated by the model. You have a few ways to construct your preference data.

**中文**

好。首先，我们当然需要偏好对。所以，我们先看数据收集这一步。设定是这样的：你有一个 prompt，比如“写一首诗”。你还有一个给定的回答，也就是模型生成的那首诗。构建偏好数据有几种方式。

### [12:08](https://www.youtube.com/watch?v=PmW_TMQ3l0I&t=728s) · b000023

**English**

So either you start with a pointwise mindset, where you score each proposed poem with some kind of pointwise score, and here pointwise score means a score just relative to one observation. You could very well do that, but I will say it's kind of hard. It's kind of tough as a human to say, OK, this one is, I don't know, a 0.9. This one is like a 0.2.

**中文**

你可以从逐点（pointwise）的思路出发，用某种逐点评分给每首候选诗打分。这里的逐点评分指的是只针对单个观测样本的分数。你完全可以这样做，但我会说这有点难。对于人来说，要判断“好，这首，我不知道，给 0.9；这首大概给 0.2”，是有些困难的。

### [12:38](https://www.youtube.com/watch?v=PmW_TMQ3l0I&t=758s) · b000024

**English**

It's not super clear exactly how you would scale that. The second idea is for you to get two observations at the time and for you to say which one is better. So this one is called pairwise preference data. And it's much easier. And then, the third one is listwise, which is get a list of, let's say, n poems, and then you just rank which one is best, which one is worst, et cetera, et cetera.

**中文**

究竟如何确定这个评分尺度，并不是特别清楚。第二种思路是，每次给你两个观测样本，让你说哪个更好。这叫作成对偏好数据（pairwise preference data），要容易得多。第三种是列表式（listwise），就是给你一个列表，比如 n 首诗，然后你把它们排个序，哪首最好、哪首最差，等等。

### [13:15](https://www.youtube.com/watch?v=PmW_TMQ3l0I&t=795s) · b000025

**English**

And I guess this one is easier than pointwise, because you don't have to specify, I guess, how much better it is, but I guess it's still a bit more complicated. And that's the reason why people typically use pairwise. So what they do is they collect pairwise preference data. Meaning for each prompt, they have two possible answers, and then they just specify which one is better.

**中文**

我想，这比 pointwise 容易，因为你不必明确指出它究竟好多少，但我想它还是稍微复杂一些。这就是人们通常使用 pairwise 的原因。他们会收集成对偏好数据，也就是说，每个 prompt 有两个可能的回答，然后只需指出哪个更好。

### [13:47](https://www.youtube.com/watch?v=PmW_TMQ3l0I&t=827s) · b000026

**English**

And so that's the one we'll continue this lecture with. OK, so now you may ask, OK, great, pairwise preference data. But how do you get it? Well, here is the recipe. So in order to generate a pair of responses--so first, you need a prompt. And we've seen-- previously, I think it's in lecture probably 3--that what you could do was to generate different answers if you have a temperature that's positive.

**中文**

因此，我们这节课接下来会采用这种方式。好，现在你可能会问，成对偏好数据很好，但如何获取呢？方法是这样的：为了生成一对回答，首先需要一个 prompt。我们之前看过，我想大概是在第 3 讲，如果温度（temperature）为正，就可以生成不同的回答。

### [14:23](https://www.youtube.com/watch?v=PmW_TMQ3l0I&t=863s) · b000027

**English**

So typically, what people do is they put this prompt, let's say, twice into the model with a positive temperature, and then they can get two different answers.

**中文**

通常，人们会把这个 prompt 在 temperature 为正的情况下输入模型，比如输入两次，然后就可以得到两个不同的回答。

### [14:37](https://www.youtube.com/watch?v=PmW_TMQ3l0I&t=877s) · b000028

**English**

The prompt is typically something where we wanted to follow the distribution of what the users typically ask. So the prompt x can be something that we obtain from the logs or from, let's say, a desired set of prompts. And then what we do is we have these two observations. So the first one is the prompt and the first response. The second one is the prompt and the second response.

**中文**

对于 prompt，我们通常希望它符合用户实际提问的分布。因此，prompt x 可以从日志中获取，也可以来自某个期望使用的 prompt 集合。然后，我们就有了这两个观测样本。第一个是 prompt 和第一个回答，第二个是 prompt 和第二个回答。

### [15:07](https://www.youtube.com/watch?v=PmW_TMQ3l0I&t=907s) · b000029

**English**

And what we do is we rate--we compare them. So we can compare them with, of course, human ratings. But we can also compare them with some other metrics. So I'll just list a few. So we have LLM as a judge, which you may have heard of, which we have not seen yet, which we will see in a few lectures that is also typically used to just compare, I guess, how much better one observation is compared to another.

**中文**

接下来我们评分，也就是比较它们。当然，可以通过人工评分来比较，但也可以使用其他一些指标。我列举几个。比如让 LLM 担任评判者（LLM as a judge），你们可能听说过。我们还没讲到，但会在之后几讲中讲到。这种方法通常也用于比较一个观测样本比另一个好多少。

### [15:46](https://www.youtube.com/watch?v=PmW_TMQ3l0I&t=946s) · b000030

**English**

We can also use some other metrics, rule-based one like BLEU, ROUGE, et cetera, although, it is not as used these days. And the simplest way to compare these two observations is to have a binary setting, where you say, OK, is response 1 better or worse than response 2? But you could also think of a more nuanced scale, meaning you can also say, OK, response 1 is much better, better, slightly better, slightly worse, worse, or much worse.

**中文**

我们还可以使用其他一些基于规则的指标，比如 BLEU、ROUGE 等，不过如今用得没有那么多了。比较这两个观测样本最简单的方式是采用二元设定，即判断回答 1 比回答 2 更好还是更差。但你也可以采用更细致的尺度，比如说回答 1 好得多、更好、稍好、稍差、更差，或者差得多。

### [16:24](https://www.youtube.com/watch?v=PmW_TMQ3l0I&t=984s) · b000031

**English**

So this is also something that you can do. But there are some challenges with that approach. Because for instance, if you, I don't know, consider human ratings, a lot of tasks are a little bit subjective. So in a lot of cases, actually, what people do is having a pairwise preference data set on the binary scale. So only is it better or worse.

**中文**

这也是一种可行的方式。不过，这种方法存在一些挑战。比如说，如果考虑人工评分，许多任务都有点主观。因此，很多情况下，人们实际上会采用二元尺度的成对偏好数据集，也就是只判断更好还是更差。

### [16:54](https://www.youtube.com/watch?v=PmW_TMQ3l0I&t=1014s) · b000032

**English**

Does that sound good? Yeah. OK, so another way to obtain that data is to have--to find in your logs a response that you did not like to take that response and to rewrite it, which is basically what we did here. So here, when we have the response here, what we did is take the response and rewrite a good one.

**中文**

这样可以吗？好。获取这类数据的另一种方式是，从日志中找到一个你不喜欢的回答，然后把它改写，这基本上就是我们刚才在这里做的。这里有这个回答，我们做的就是拿来改写成一个好的回答。

### [17:27](https://www.youtube.com/watch?v=PmW_TMQ3l0I&t=1047s) · b000033

**English**

So this is also what people do. But of course, it is a bit more involved, because you need to generate. And I told you that generation was kind of costly and tough, but this is also possible.

**中文**

人们也会这样做。不过，这当然稍微更费事，因为你需要生成内容。我之前说过，生成内容有些昂贵，也有些困难，但这也是一种可行的方式。

### [17:41](https://www.youtube.com/watch?v=PmW_TMQ3l0I&t=1061s) · b000034

**English**

Does the data collection make sense?

**中文**

数据收集这部分大家能理解吗？

### [17:46](https://www.youtube.com/watch?v=PmW_TMQ3l0I&t=1066s) · b000035

**English**

Yeah? Cool. OK, so now, we have our preference data. And what we want is to align our model to prefer responses that were preferred by the rating, and, I guess, down weight the responses that were not preferred. And so in order to do that, we will see a method that's called RLHF. RLHF. And I'll see-- we'll see that in more details in a second.

**中文**

能吗？好。现在我们有了偏好数据。我们想要对齐模型，使它更偏好评分中被偏好的回答，并且降低那些不被偏好的回答的权重。为此，我们将介绍一种叫作 RLHF 的方法。RLHF。我会看——我们马上会更详细地讲它。

### [18:22](https://www.youtube.com/watch?v=PmW_TMQ3l0I&t=1102s) · b000036

**English**

But as the name indicates, RLHF relies on RL. So I'm just going to start with some RL basics. So do we have any RL experts here?

**中文**

不过，顾名思义，RLHF 依赖于强化学习（RL）。所以，我先讲一些 RL 基础知识。这里有 RL 专家吗？

### [18:37](https://www.youtube.com/watch?v=PmW_TMQ3l0I&t=1117s) · b000037

**English**

Yeah? No? \[CHUCKLES\] So no need to be an RL expert. So don't worry. We'll go really slowly on that. So in the RL world, what people do is they have an agent--and here, I mean the agent in RL term--which interacts with an environment. So what does it do? It is at a given state, at, let's say, time t, it can take an action at time t.

**中文**

有吗？没有？\[轻笑\] 不需要是 RL 专家，别担心。这部分我们会讲得很慢。在 RL 的世界里，有一个智能体（agent），这里指的是 RL 意义上的 agent，它与环境（environment）交互。那么它会做什么？它处于一个给定的状态（state），比如在时刻 t，可以在时刻 t 采取一个动作（action）。

### [19:09](https://www.youtube.com/watch?v=PmW_TMQ3l0I&t=1149s) · b000038

**English**

And it takes that action according to some policy. The policy is typically denoted pi, pi of theta of the action given the state. So what that policy means is simply giving you the probability of you taking an action given a state. Easy, right? And so given that the agent takes some action, it also receives some rewards.

**中文**

它根据某个策略（policy）采取这个动作。策略通常记作 pi，也就是以状态为条件的动作的 pi of theta。这个策略的含义很简单，就是给出在某个状态下采取某个动作的概率。很简单，对吧？当 agent 采取某个动作后，它也会获得一些奖励（reward）。

### [19:46](https://www.youtube.com/watch?v=PmW_TMQ3l0I&t=1186s) · b000039

**English**

So sometimes, it's a good reward. Sometimes, it's bad rewards.

**中文**

有时是好的奖励，有时是差的奖励。

### [19:52](https://www.youtube.com/watch?v=PmW_TMQ3l0I&t=1192s) · b000040

**English**

So what we're going to do is to leverage that mindset for our preference tuning exercise. So let's see together how we can transpose these quantities in the LLM world. So what is the agent? The agent is the LLM. So in terms of the state that it is in, so it's simply the input that it has so far.

**中文**

我们接下来要把这种思路用于 preference tuning。一起看看如何把这些量对应到 LLM 的世界里。agent 是什么？agent 就是 LLM。至于它所处的状态，就是它到目前为止拥有的输入。

### [20:25](https://www.youtube.com/watch?v=PmW_TMQ3l0I&t=1225s) · b000041

**English**

So the action that it wants to do is to predict the next token. So it basically always wonders, OK, what is the next token given this input? And this action or this next token is among the set of tokens that are out there. So if you want--the environment can be the set of tokens of your vocabulary. And in order to decide which token should come next, the LLM determines that using the probability of next token, which is obtained by when you do your forward pass, and when you look at the probability distribution as an output, which is basically our policy.

**中文**

它想采取的动作是预测下一个 token。基本上，它一直在想：给定这个输入，下一个 token 是什么？这个动作，或者说下一个 token，来自所有可用 token 的集合。所以，如果你愿意这样理解，环境可以是词表中的 token 集合。为了决定下一个应该是哪个 token，LLM 会使用下一个 token 的概率，这个概率通过前向传播（forward pass）得到，也就是你看到的输出概率分布，它基本上就是我们的策略。

### [21:15](https://www.youtube.com/watch?v=PmW_TMQ3l0I&t=1275s) · b000042

**English**

So our policy here is simply equal to the output of the LLM given the input in order to determine the next token. So far, so good? And now, we're adding one additional thing. So I told you we're composing our preference data sets. And we want to know which output is better than the other output. And so we're going to use that for our reward.

**中文**

这里的策略就是 LLM 在给定输入时用于确定下一个 token 的输出。到这里都没问题吧？现在，我们再加一个东西。我说过，我们在构建偏好数据集，并且想知道哪个输出比另一个更好。我们会把这用于奖励。

### [21:47](https://www.youtube.com/watch?v=PmW_TMQ3l0I&t=1307s) · b000043

**English**

We're going to somehow use that for our reward. And we'll see how we will use that.

**中文**

我们会以某种方式把它用于奖励，接下来会看具体怎么用。

### [21:54](https://www.youtube.com/watch?v=PmW_TMQ3l0I&t=1314s) · b000044

**English**

So I'm going to just recap that part. So we have our LLM take some input, and then it wants to predict the next token. It wants to take this action. So in order to do that, it uses the probability distribution that it outputs.

**中文**

我来回顾一下这部分。LLM 接收一些输入，然后想预测下一个 token。它想采取这个动作。为此，它使用自己输出的概率分布。

### [22:13](https://www.youtube.com/watch?v=PmW_TMQ3l0I&t=1333s) · b000045

**English**

And then, the token that it predicts or the output that it generates then receives some reward that is going to feed back into tuning the agent. And here is the LLM. Yep. \[AUDIO OUT\]

**中文**

然后，它预测的 token 或生成的输出会获得某个奖励，这个奖励会反馈回来，用于调优 agent，而这里的 agent 就是 LLM。嗯。\[音频缺失\]

### [22:36](https://www.youtube.com/watch?v=PmW_TMQ3l0I&t=1356s) · b000046

**English**

So the question is, wouldn't that be expensive if we do this for all pairs? Why would that be expensive? \[AUDIO OUT\]

**中文**

问题是，如果对所有偏好对都这样做，难道不会很昂贵吗？为什么会很昂贵？\[音频缺失\]

### [22:53](https://www.youtube.com/watch?v=PmW_TMQ3l0I&t=1373s) · b000047

**English**

Mm-hmm. \[AUDIO OUT\] Yeah, so--\[AUDIO OUT\] Yeah, the question is, what do you do in terms of how expensive that is? So yeah, typically, people take batches, for instance. But I would not--so it is indeed expensive. But we're going to see a little bit some order of magnitude and how that works. But you can think of this as being kind of a training procedure that could be seen as expensive as some other training procedure. There's nothing that makes this more expensive, but we're going to see exactly.

**中文**

嗯。\[音频缺失\] 对，所以——\[音频缺失\] 对，问题是，面对这样的成本，你们会怎么做？通常，人们会采用批次（batches），比如说。不过我不会——它确实很昂贵，但我们会稍微看一下数量级，以及具体如何运作。你可以把它看成一种训练过程，成本可能和其他某种训练过程相当。这里没有什么使它更昂贵，不过我们会具体看。

### [23:27](https://www.youtube.com/watch?v=PmW_TMQ3l0I&t=1407s) · b000048

**English**

So I think there are some points that you're touching correctly. There are some parts that are added compared to the regular supervised-- let's say, supervised fine tuning setting. And we're going to see that in a second. \[AUDIO OUT\]

**中文**

我觉得你确实提到了一些关键点。与通常的监督——比如说监督微调设定相比，这里确实增加了一些部分。我们马上会看到。\[音频缺失\]

### [23:55](https://www.youtube.com/watch?v=PmW_TMQ3l0I&t=1435s) · b000049

**English**

So the question is, does the reward that you're getting from here, I guess, powerful enough for the LLM to change? Well, you will see some expressions on the internet just characterizing this training procedure as it's nearly not as many signals as what you would get for SFT, let's say. But because for SFT, you're literally always taking a partial input and making the LLM learn how to generate the next token.

**中文**

问题是，从这里获得的奖励是否足够有力，能让 LLM 发生变化？你会在网上看到一些说法，描述这种训练过程的信号远没有 SFT 那么多。因为在 SFT 中，你实际上总是在拿一段部分输入，让 LLM 学习如何生成下一个 token。

### [24:28](https://www.youtube.com/watch?v=PmW_TMQ3l0I&t=1468s) · b000050

**English**

But here, you're only getting roughly one signal per completion. So yeah, definitely it's more sparse. And that's why you will see that RLHF is seen as more an approach that has sparse signals.

**中文**

而在这里，每个完整生成结果（completion）大致只得到一个信号。所以，它肯定更稀疏。这就是为什么你会看到，RLHF 被认为是一种信号较稀疏的方法。

### [24:46](https://www.youtube.com/watch?v=PmW_TMQ3l0I&t=1486s) · b000051

**English**

Yeah, yep. \[AUDIO OUT\]

**中文**

对，嗯。\[音频缺失\]

### [24:53](https://www.youtube.com/watch?v=PmW_TMQ3l0I&t=1493s) · b000052

**English**

Great question. So the question is, do you apply a reward for each token or for the whole thing? We're going to see this in more detail, but it's for the whole thing. It's for the whole thing. But we'll see that in just a second. Yep. \[AUDIO OUT\] So the AD and--oh, right, so the question is, what is the AT and ST. So just as a reminder, ST is the state that you're in, and AT is the action you want to take.

**中文**

好问题。问题是，每个 token 都有奖励，还是对整个结果给奖励？我们会更详细地看，但答案是对整个结果。对整个结果。不过我们马上会讲到。嗯。\[音频缺失\] 所以 AD 和——哦，对，问题是 AT 和 ST 是什么。提醒一下，ST 是你所处的状态，AT 是你想采取的动作。

### [25:26](https://www.youtube.com/watch?v=PmW_TMQ3l0I&t=1526s) · b000053

**English**

So in the context of an LLM, the state that you're in for an LLM is the input that you have so far. And then the action is which token you want to generate given that input. Yep.

**中文**

在 LLM 的情境中，LLM 所处的状态就是它到目前为止拥有的输入。动作则是给定该输入后，你想生成哪个 token。嗯。

### [25:44](https://www.youtube.com/watch?v=PmW_TMQ3l0I&t=1544s) · b000054

**English**

Cool. Yeah, so far so good? OK, perfect. So now that we know a little bit what a mental model could be for, I guess, LLM-based RL, I just want to highlight once more that what we're trying to achieve is learn how to align this policy with rewards. So we want to learn theta, and theta is the parameters of our LLM, such that pi of theta aligns with preferences.

**中文**

好。目前都没问题吧？好，很好。现在我们对基于 LLM 的 RL 可以怎样理解有了一些认识，我想再次强调，我们要实现的是学习如何让这个策略与奖励对齐。我们希望学习 theta，theta 就是 LLM 的参数，使得 pi of theta 与偏好对齐。

### [26:25](https://www.youtube.com/watch?v=PmW_TMQ3l0I&t=1585s) · b000055

**English**

And that's where RLHF comes into play. So RLHF stands for Reinforcement Learning from Human Feedback. And it is typically composed of two stages. So the first stage is you figuring out how to distinguish good output from bad output. So here, all the preference pairs that you collected are actually used for you to learn what is good, what is bad.

**中文**

这就是 RLHF 发挥作用的地方。RLHF 代表基于人类反馈的强化学习（Reinforcement Learning from Human Feedback）。它通常包括两个阶段。第一个阶段是弄清楚如何区分好的输出和差的输出。这里，你收集的所有偏好对，实际上都用于学习什么是好、什么是差。

### [26:59](https://www.youtube.com/watch?v=PmW_TMQ3l0I&t=1619s) · b000056

**English**

So the input here is the concatenation of the prompt and the response. And the output is a score. So what you want to know given a prompt and the response, how good that is. And then the second step is the RL step, the Reinforcement Learning step. And this is where you use the rewards to align your model with the preferences. So here as input, you have the prompts. And what you somehow want to do is to be able to generate y hat that is more aligned with the rewards.

**中文**

这里的输入是 prompt 与回答的拼接，输出是一个分数。你想知道的是，给定一个 prompt 和回答，它有多好。第二步是 RL，也就是强化学习这一步。在这里，你使用奖励，让模型与偏好对齐。这里输入的是 prompt。你想做的是能够生成与奖励更对齐的 y hat。

### [27:38](https://www.youtube.com/watch?v=PmW_TMQ3l0I&t=1658s) · b000057

**English**

And by the way, I just want to call out one thing. So RLHF is Reinforcement Learning from Human Feedback. The Human Feedback part refers to the labels on which the reward model is trained. So if there are preference pairs are based on human ratings, then we're relying on human preferences, then we're in RLHF. Because you will see out there, there is also RL, let's say, AIF, a Reinforcement Learning from AI Feedback.

**中文**

顺便，我想特别指出一点。RLHF 是 Reinforcement Learning from Human Feedback。其中 Human Feedback 指的是训练奖励模型（reward model）所用的标签。如果偏好对基于人工评分，那么我们依赖的就是人类偏好，这就属于 RLHF。因为你们还会看到 RL，比如说 AIF，也就是基于 AI 反馈的强化学习（Reinforcement Learning from AI Feedback）。

### [28:13](https://www.youtube.com/watch?v=PmW_TMQ3l0I&t=1693s) · b000058

**English**

And that one is relying on non-human preferences. So yeah. Cool. OK, so now that we know what RLHF is and we know that there are two steps, we'll go through the first step naturally. So here the idea is we want to construct a model that knows which output is good, which output is bad. And of course, here, what we want is to not only consider the output, but also the input, because you need to somehow contextualize that answer.

**中文**

后者依赖的是非人类偏好。好。现在我们知道 RLHF 是什么，也知道它有两个步骤，自然先看第一步。这里的想法是构建一个模型，让它知道哪个输出好、哪个输出差。当然，我们不只要考虑输出，也要考虑输入，因为需要把回答放在某种上下文中理解。

### [28:53](https://www.youtube.com/watch?v=PmW_TMQ3l0I&t=1733s) · b000059

**English**

So let's go with our favorite example. So let's suppose you have the following prompt. Suggest a new activity I could do with my teddy bear. So what you want is to have a reward model that-- here, we note RM, --that tells you that the answer that we rewrote into the good answer is good. And we want to somehow have that model that tells us that the output that we constructed--or that we did not construct, the output that we saw was bad is bad.

**中文**

我们用最喜欢的那个例子。假设有以下 prompt：“推荐一种我可以和泰迪熊一起做的新活动。”你希望有一个奖励模型，这里记作 RM，告诉你我们改写成好回答的那个答案是好的。我们也希望这个模型告诉我们，我们构建的那个输出——或者说不是我们构建的，而是我们看到的那个差的输出——是差的。

### [29:30](https://www.youtube.com/watch?v=PmW_TMQ3l0I&t=1770s) · b000060

**English**

So we want to somehow have a model that takes in the prompts and the good response and say it's good. And we want to somehow have a model that takes the prompt and the bad response to say it's bad. So now the question is, how do you construct such a model? Well, in order to do that, we are using a formulation that's called the Bradley-Terry formulation. So that one is an important formula. So we'll just stay here for a little bit.

**中文**

我们希望有一个模型，接收 prompt 和好的回答，然后说它是好的。也希望有一个模型，接收 prompt 和差的回答，然后说它是差的。现在的问题是，如何构建这样的模型？为此，我们使用一种叫作 Bradley-Terry 表述（Bradley-Terry formulation）的形式。这是一个重要公式，我们会在这里多停留一会儿。

### [30:03](https://www.youtube.com/watch?v=PmW_TMQ3l0I&t=1803s) · b000061

**English**

So what it says is that the probability-- bless you--to have an output yi be better than an output yj is equal to an exponential of some score, which is a score with respect to i over the exponential of that score with respect to i plus the exponential of some score with respect to j.

**中文**

它说的是，输出 yi 优于输出 yj 的概率——保重——等于某个分数的指数，也就是与 i 对应的分数的指数，除以该 i 对应分数的指数与某个 j 对应分数的指数之和。

### [30:36](https://www.youtube.com/watch?v=PmW_TMQ3l0I&t=1836s) · b000062

**English**

So that is called the Bradley-Terry formulation. And this is the formulation we will use to build our model. So here, it's also equal to sigma of ri minus rj. So who knows what sigma is? \[INAUDIBLE\] Yes, exactly. So it's a sigmoid. So just as a reminder sigmoid is 1 over 1 plus exponential of minus x. So this is how the graph looks like.

**中文**

这就叫作 Bradley-Terry formulation。我们会用它来构建模型。这里，它也等于 sigma of ri minus rj。谁知道 sigma 是什么？\[听不清\] 对，完全正确，是 sigmoid。提醒一下，sigmoid 就是 1 除以 1 加上负 x 的指数。它的图像是这样的。

### [31:08](https://www.youtube.com/watch?v=PmW_TMQ3l0I&t=1868s) · b000063

**English**

So when it's minus infinity, it tends towards 0, and then towards plus infinity, it tends towards 1. So in other words, if i is better than j, what we want is for the input to sigma to be as high as possible, because you want the probability to be as close to 1. So you want to somehow have ri be high if the output i is good and somehow rj to be low, if the output is bad.

**中文**

当输入趋向负无穷时，它趋向 0；当输入趋向正无穷时，它趋向 1。换句话说，如果 i 比 j 好，我们就希望 sigma 的输入尽可能大，因为希望这个概率尽可能接近 1。因此，如果输出 i 好，就希望 ri 高；如果输出差，就希望 rj 低。

### [31:54](https://www.youtube.com/watch?v=PmW_TMQ3l0I&t=1914s) · b000064

**English**

So far so good? So here, what we want to do is to somehow train a model that is able to output scores ri and rj using this formulation. So this formulation involves two quantities, because we have a pairwise data set.

**中文**

到这里都没问题吧？这里我们想做的是，使用这个表述训练一个能够输出分数 ri 和 rj 的模型。这个表述涉及两个量，因为我们有一个成对数据集。

### [32:24](https://www.youtube.com/watch?v=PmW_TMQ3l0I&t=1944s) · b000065

**English**

So far so good? So it will become more clear in a second. So here for training, the idea here is you have some model that you initialize, and you input on the one hand your prompt x and your winning output. So I'm saying winning, so it's y hat w. You put it into the model. It produces score r of x and y hat w.

**中文**

到这里都没问题吧？马上就会更清楚。在训练时，思路是这样的：初始化某个模型，一方面输入 prompt x 和胜出的输出。我这里说的是胜出，所以记作 y hat w。把它放进模型，模型会产生分数 r of x and y hat w。

### [32:57](https://www.youtube.com/watch?v=PmW_TMQ3l0I&t=1977s) · b000066

**English**

And then, you have a second output, so x and yl, y hat l, which is the losing output. So you put it into the model, and it has a second score. And now, you somehow want to have a loss function that takes into account these two scores. So based on this formulation, do you have some suggestion as to which loss function to use?

**中文**

然后还有第二个输出，也就是 x 和 yl，y hat l，这是落败的输出。把它输入模型，就会得到第二个分数。现在，我们希望有一个损失函数（loss function），把这两个分数都考虑进去。根据这个表述，大家对应该使用什么损失函数有什么建议吗？

### [33:34](https://www.youtube.com/watch?v=PmW_TMQ3l0I&t=2014s) · b000067

**English**

So here, our loss function would be pairwise. Yep. Yeah. So the proposed answer is a binary cross entropy. So can you explicit that a bit more? \[AUDIO OUT\] Mm-hmm. \[AUDIO OUT\]

**中文**

这里的损失函数会是成对的。嗯，对。提出的答案是二元交叉熵（binary cross entropy）。你能再具体说明一下吗？\[音频缺失\] 嗯。\[音频缺失\]

### [33:59](https://www.youtube.com/watch?v=PmW_TMQ3l0I&t=2039s) · b000068

**English**

OK, so I guess, in that case, what would it be? \[AUDIO OUT\] Yep. \[AUDIO OUT\] Yep. \[AUDIO OUT\] Yeah, exactly. So I guess, the-- yes, great answer. So I guess, your answer is having some negative log likelihoods of this quantity, which is--so the cross-entropy can be seen as kind of a special case of this.

**中文**

好，那么在这种情况下，它具体会是什么？\[音频缺失\] 对。\[音频缺失\] 对。\[音频缺失\] 对，完全正确。我想——对，很好的答案。我想，你的答案是取这个量的负对数似然（negative log likelihood），也就是——交叉熵可以看作它的一种特殊情况。

### [34:30](https://www.youtube.com/watch?v=PmW_TMQ3l0I&t=2070s) · b000069

**English**

So that we make sure that we get this part--

**中文**

为了确保我们理解这一部分——

### [34:36](https://www.youtube.com/watch?v=PmW_TMQ3l0I&t=2076s) · b000070

**English**

so in order to just get that formulation, which you mentioned again, I guess, one idea that we can have is given our data and given this formulation that we saw, the Bradley-Terry one, to find parameters theta that maximize the probability of that data happening, which basically, leads to what you mentioned. So here, I'm just going to write what that means, so that just we can be all aligned.

**中文**

为了得到你刚才提到的这个表述，我想可以这样考虑：给定我们的数据，以及刚才看到的 Bradley-Terry formulation，寻找能使这些数据出现的概率最大的参数 theta，这基本上就会得到你说的内容。这里我写一下它是什么意思，确保大家理解一致。

### [35:12](https://www.youtube.com/watch?v=PmW_TMQ3l0I&t=2112s) · b000071

**English**

So here, it's-- so let's suppose you have a preference data sets of, let's say, winning example associated with losing example. So you have a bunch of pairs like this. So let's suppose that these pairs, they happened independently of one another. So what you want is to find parameters that somehow maximize the probability of you seeing those examples.

**中文**

这里是——假设你有一个偏好数据集，比如胜出样本与落败样本配对。你有一批这样的样本对。假设这些样本对彼此独立地出现。那么，你希望找到一些参数，使观测到这些样本的概率最大。

### [35:50](https://www.youtube.com/watch?v=PmW_TMQ3l0I&t=2150s) · b000072

**English**

So here, what that means is we want to somehow how maximize the products of, let's say, these n preference pairs, which is the probability of some output w being better than some output \[? l. ?\] And we saw that with the Bradley-Terry formulation, so we have this formulation, which is basically the product of \[? y1 ?\] to n of these sigma of this reward, which is basically a function of the input prompts and the output.

**中文**

这里的意思是，我们希望最大化这 n 个偏好对的概率乘积，也就是某个输出 w 优于某个输出 \[? l ?\] 的概率。根据刚才的 Bradley-Terry formulation，我们得到了这个表述，基本上就是从 \[? y1 ?\] \[字幕疑误，可能指 i=1\] 到 n，对这些奖励的 sigma 求乘积，而这个奖励基本上是输入 prompt 和输出的函数。

### [36:41](https://www.youtube.com/watch?v=PmW_TMQ3l0I&t=2201s) · b000073

**English**

Like this.

**中文**

像这样。

### [36:45](https://www.youtube.com/watch?v=PmW_TMQ3l0I&t=2205s) · b000074

**English**

So what I'm doing here is to just reconstruct the loss from first principles. So whenever you see a product of probabilities, the first thing you need to think about is--yes, log. Because this can become very small, so it can cause instabilities. So if you take the log, if you want to maximize the product, it's the same as maximizing the log of that. So if you take the log of that-- so let's suppose I'm taking, let's say, the log of that.

**中文**

我这里是在从基本原理重新推导损失。每当看到概率的乘积，你首先应该想到什么？对，取对数（log）。因为这个乘积可能变得非常小，从而造成不稳定。如果取 log，最大化这个乘积就等同于最大化它的 log。那么，对它取 log——假设我对它取 log。

### [37:17](https://www.youtube.com/watch?v=PmW_TMQ3l0I&t=2237s) · b000075

**English**

Let's say I'm taking the log of that. So it's basically equal to the sum of the log of sigma of r of the winning minus the one from the losing.

**中文**

假设我对它取 log。它基本上就等于对各项求和，每一项是胜出样本的 r 减去落败样本的 r，再取 sigma，然后取 log。

### [37:42](https://www.youtube.com/watch?v=PmW_TMQ3l0I&t=2262s) · b000076

**English**

So we want to maximize that. But people in ML, they like to minimize things. So we're going to take--like, have a negative in front, so maximizing plus the sum of the log is the same as minimizing minus the sum of the log. And so this will be our loss function.

**中文**

我们希望最大化它。但机器学习（ML）领域的人喜欢最小化一些东西。所以我们会在前面加一个负号，最大化 log 之和，就等同于最小化 log 之和的相反数。这就是我们的损失函数。

### [38:12](https://www.youtube.com/watch?v=PmW_TMQ3l0I&t=2292s) · b000077

**English**

Does that make sense? And this is exactly what you mentioned. And typically, we write the expectation. And this is our loss function. So our loss function is minus the expectation of log of sigma r and x and y, y hat w minus the reward of the losing.

**中文**

能理解吗？这正是你刚才提到的。通常，我们把它写成期望（expectation）的形式。这就是我们的损失函数。也就是取负的期望，期望里面是 log of sigma，sigma 里面是 r、x 和 y、y hat w，减去落败样本的奖励。

### [38:40](https://www.youtube.com/watch?v=PmW_TMQ3l0I&t=2320s) · b000078

**English**

Sounds good? So here, the loss function is pairwise. But the reward model, is it pairwise or is it pointwise? I guess, do you need a pair to make a prediction or do you need just one? Do you need a pair? Pair? Well, that's the beauty of things. You don't need a pair, so you're just training it pairwise, but it's actually pointwise.

**中文**

没问题吧？这里的损失函数是 pairwise 的。但奖励模型是 pairwise 还是 pointwise 的？我是说，做一次预测需要一对样本，还是只需要一个？需要一对吗？一对？这正是妙处所在。你不需要一对；你只是以 pairwise 的方式训练它，但它实际上是 pointwise 的。

### [39:06](https://www.youtube.com/watch?v=PmW_TMQ3l0I&t=2346s) · b000079

**English**

So I think that's one thing I realize. I look at this loss, and this is a \[INAUDIBLE\] So you're training in a pairwise way. But at the end of the day, you have a reward model that takes in one prompt and its output and just outputs one number. And we saw that it will try to output a high score for winning examples and then a low score for losing examples. So this is our reward model.

**中文**

我想，这是我意识到的一点。我看着这个损失，这是一个 \[听不清\]。你用 pairwise 的方式训练它，但最终得到的是一个奖励模型，接收一个 prompt 及其输出，只输出一个数字。我们看到，它会尝试为胜出样本输出高分，为落败样本输出低分。这就是我们的奖励模型。

### [39:38](https://www.youtube.com/watch?v=PmW_TMQ3l0I&t=2378s) · b000080

**English**

And I'm looking at the time, I'm actually not on time, so I'll just move on. So typically, here, what you would need is a set of data, which is typically in the tens of thousands or maybe even more. And here, the label would be the preference rating. The preference here should come from humans if we're talking about RLHF. And in terms of model, where you have a bunch of different choices. So as we now, models that are decoder only that predict the next token are very popular.

**中文**

我看了一下时间，实际上进度落后了，所以继续往下。通常，这里需要一组数据，规模一般是数万条，甚至更多。这里的标签是偏好评分。如果说的是 RLHF，那么偏好应该来自人类。至于模型，有很多不同的选择。我们知道，只包含解码器（decoder only）、用于预测下一个 token 的模型非常流行。

### [40:15](https://www.youtube.com/watch?v=PmW_TMQ3l0I&t=2415s) · b000081

**English**

So you could very well take such an LLM and just have some classification heads at the end of your sentence that you're taking into consideration and then use that to predict the reward. Or if you remember, we've also seen encoder only models in the beginning of the class. So for instance, BERTs. You could typically also project the embedding of the CLS token. It could very well be an option.

**中文**

你完全可以拿这样一个 LLM，在所考虑的句子末尾加一些分类头（classification heads），然后用来预测奖励。或者，如果你还记得，我们在课程开始时也看过只包含编码器（encoder only）的模型，比如 BERTs。你也可以对 CLS token 的嵌入（embedding）进行投影。这完全可以是一个选择。

### [40:47](https://www.youtube.com/watch?v=PmW_TMQ3l0I&t=2447s) · b000082

**English**

So typically, what people do nowadays is take the LLM route because everything is an LLM these days. So it's like decoder only. You just put a classification head. And so people have also come up with benchmarks to evaluate how good you're doing. So we just put a reference here RewardBench in case you're interested. It's a pretty popular one.

**中文**

如今，人们通常采用 LLM 这条路线，因为现在什么都是 LLM。也就是 decoder only，加一个分类头。人们还提出了一些基准（benchmarks），用于评估效果如何。这里放了一个参考，RewardBench，如果你们感兴趣可以看看。这是一个相当流行的基准。

### [41:16](https://www.youtube.com/watch?v=PmW_TMQ3l0I&t=2476s) · b000083

**English**

But yeah. So at the end of this, you get a reward model that takes in a prompt and a given response and gives you a score. Yep. \[AUDIO OUT\]

**中文**

总之，完成这一步后，你会得到一个奖励模型，输入一个 prompt 和给定回答，它就会给出一个分数。嗯。\[音频缺失\]

### [41:49](https://www.youtube.com/watch?v=PmW_TMQ3l0I&t=2509s) · b000084

**English**

Exactly. So the question is in some tasks, the human preference would be something, but another task, it may be something else. So typically, those rewards, they are with respect to a given dimension. So they can be, let's say, is the output useful or is the outputs are not friendly? Is the output safe? So all of that are different dimensions, so they can be different reward models. You can also have some holistic score as well.

**中文**

没错。问题是，在某些任务中，人类偏好是这样，但在另一个任务中，可能就不同了。通常，这些奖励针对某个给定的维度。比如，输出是否有用，或者输出是否不友好？输出是否安全？这些都是不同的维度，因此可以对应不同的奖励模型。你也可以使用某种综合分数。

### [42:21](https://www.youtube.com/watch?v=PmW_TMQ3l0I&t=2541s) · b000085

**English**

But yeah. So you need to define a dimension across which you're actually quantifying how good your response is. So the ones that I mentioned are the common ones that you'd find. Another thing that we say as well, while we're at it, so human ratings are very sensitive to the guidelines that you're also exposing. So we're not going to go into details here, but one important aspect of human preference data is to make sure that the guidelines you're telling your readers are as objective as it could get.

**中文**

所以，你需要定义一个维度，沿着这个维度量化回答有多好。我提到的那些是常见的维度。说到这里，还要补充一点，人工评分对你提供的指导说明也非常敏感。这里不展开讲，但人类偏好数据一个重要的方面是，要确保你给阅读者的指导说明尽可能客观。

### [43:02](https://www.youtube.com/watch?v=PmW_TMQ3l0I&t=2582s) · b000086

**English**

I mean, sometimes you cannot have them be super objective, but you have, I guess, the task of just making sure they're clear enough, so that your human preferences, they're not noisy, because they can be noisy, but that's also one challenge. Yeah. \[AUDIO OUT\] So the question is, is the reward here a regression or a classification? So let's look at the loss function and here.

**中文**

我的意思是，有时做不到特别客观，但我想，你有责任确保这些说明足够清楚，使人类偏好不带有噪声，因为它们可能有噪声，这也是一个挑战。嗯。\[音频缺失\] 问题是，这里的奖励属于回归（regression）还是分类（classification）？我们来看看损失函数，看这里。

### [43:39](https://www.youtube.com/watch?v=PmW_TMQ3l0I&t=2619s) · b000087

**English**

So well, it's hard, I guess, I will say because the reward can be something that can be interpreted as a score, but we have a probabilistic formulation. So I'll probably frame that as a classification task because you have preference data. Is it better or worse? So it's 1 or 0. But at the end, you use the rewards. So it's not, I guess, purely a classification task because at the end, you have this.

**中文**

我想，这有点难说，因为奖励可以解释为一个分数，但我们使用的是概率形式。所以我可能会把它表述为分类任务，因为你有偏好数据：更好还是更差？也就是 1 或 0。但最终你使用的是奖励。因此，我想它也不是一个纯粹的分类任务，因为最后你得到的是这个。

### [44:14](https://www.youtube.com/watch?v=PmW_TMQ3l0I&t=2654s) · b000088

**English**

But one thing to note is that the scale that these rewards are at is typically something that is scaled itself. So at inference time, you have some normalization procedure that normalizes that across your batch. But yeah, I would probably characterize the formulation more as a probabilistic one I would say. \[AUDIO OUT\] Yep. Yep.

**中文**

不过，要注意的是，这些奖励的尺度通常本身也会经过缩放。在推理（inference）时，会有某种归一化（normalization）过程，在整个批次内对它进行归一化。但我可能更倾向于将这种表述描述为概率形式。\[音频缺失\] 对，对。

### [44:44](https://www.youtube.com/watch?v=PmW_TMQ3l0I&t=2684s) · b000089

**English**

\[AUDIO OUT\] Yep. So the question is, do we normalize the score? So there are many different methods to, I guess, normalize things. We typically do. We typically do normalize. So I guess if you're in the regression setting, you're trying to predict some score on a given scale, which you're not doing here. So it's free form here. So yeah. So there is some rescaling that happens. Yeah. You had a question.

**中文**

\[音频缺失\] 对。问题是，我们会对分数进行归一化吗？有许多不同的归一化方法。通常会。我们通常确实会归一化。我想，如果是回归设定，你会尝试预测给定尺度上的某个分数，而这里不是这样。这里是自由形式的。所以，是的，这里会进行某种重新缩放。对，你有一个问题。

### [45:14](https://www.youtube.com/watch?v=PmW_TMQ3l0I&t=2714s) · b000090

**English**

\[AUDIO OUT\]

**中文**

\[音频缺失\]

### [45:26](https://www.youtube.com/watch?v=PmW_TMQ3l0I&t=2726s) · b000091

**English**

Yeah. The question is, can you tell us more about what the output of a reward model is? So we're going to see that a bit later, but you can think of goods outputs as being, let's say, 1, bad outputs as being minus 2, minus 3. So it's basically on the continuous scale if you want. We're going to see an example in a little bit. So hopefully, this can--do you have a question? Perfect. We're going to see an example. So hopefully, that will be clear.

**中文**

对。问题是，能否再多讲讲奖励模型的输出是什么？我们稍后会看到，但你可以把好的输出想成比如 1，差的输出想成负 2、负 3。也就是说，它基本上处于一个连续尺度上。稍后我们会看一个例子。希望这样可以——你有问题吗？很好。我们会看一个例子，希望到时就清楚了。

### [45:59](https://www.youtube.com/watch?v=PmW_TMQ3l0I&t=2759s) · b000092

**English**

Cool.

**中文**

好。

### [46:03](https://www.youtube.com/watch?v=PmW_TMQ3l0I&t=2763s) · b000093

**English**

So what we did is train a reward model. Now, the second step is to use that reward model to align our model, and by model, I mean the LLM. The LLM that went through the pre-training stage and the SFT stage is the model that we want to align with human preferences. We're going to do that using reinforcement learning. And we're going to do that using the reward model that we just constructed.

**中文**

我们刚才训练了一个奖励模型。现在，第二步是使用这个奖励模型来对齐我们的模型，这里的模型指 LLM。我们希望与人类偏好对齐的是那个经过预训练阶段和 SFT 阶段的 LLM。我们会通过强化学习来完成，并使用刚刚构建的奖励模型。

### [46:36](https://www.youtube.com/watch?v=PmW_TMQ3l0I&t=2796s) · b000094

**English**

So the reward model here is the model that we obtained in step one. And it allows us to distinguish good outputs and bad outputs. So here is a general recipe of how you would align your model. So first, you would take your prompt as input. Your LLM will generate a completion.

**中文**

这里的奖励模型就是我们在第一步得到的模型，它让我们能够区分好的输出和差的输出。下面是对齐模型的一般做法。首先，把 prompt 作为输入。LLM 会生成一个 completion。

### [47:07](https://www.youtube.com/watch?v=PmW_TMQ3l0I&t=2827s) · b000095

**English**

So here, a completion means a full response from the model. So by the way, completion, people use also the term roll-outs. So it generates a completion, a rollout, a full response. And that full response along with the prompt goes into the reward model. So as we saw, the reward model right now knows if it's good, if it's bad. Let's say, right now, it's bad. So in practice, it does not generate the thumbs down.

**中文**

这里，completion 指模型的一条完整回答。顺便说一下，人们也把 completion 称作 roll-outs。所以，它会生成一个 completion、一个 rollout、一条完整回答。然后，这条完整回答与 prompt 一起进入奖励模型。正如我们看到的，奖励模型现在知道它是好是差。假设现在它是差的。实际上，模型不会生成一个向下的大拇指。

### [47:39](https://www.youtube.com/watch?v=PmW_TMQ3l0I&t=2859s) · b000096

**English**

It generates some kind of score. So if you want minus 2 let's suppose. So we take that reward into consideration. And then what we do is we tune the LLM with this information. So it's more complicated than that. And we'll see how we go about doing this. But this is the general idea.

**中文**

它会生成某种分数。比如，假设是负 2。我们把这个奖励考虑进去，然后利用这个信息调优 LLM。实际情况比这复杂，我们会看具体如何做。但总体思路就是这样。

### [48:05](https://www.youtube.com/watch?v=PmW_TMQ3l0I&t=2885s) · b000097

**English**

So just as a reminder, the reward model is the model that we trained as step one. And it is a model that is frozen. We're not training the reward model. The reward model has been trained. The model that we're training is the LLM. So I think that's an important point to note. And our goal is to optimize for higher rewards but then without going too far from the initial model.

**中文**

提醒一下，奖励模型是在第一步训练的模型，而且它是冻结（frozen）的。我们不训练奖励模型。奖励模型已经训练好了。现在训练的是 LLM。我觉得这是需要注意的一个重要点。我们的目标是优化以获得更高的奖励，但又不偏离初始模型太远。

### [48:49](https://www.youtube.com/watch?v=PmW_TMQ3l0I&t=2929s) · b000098

**English**

So I think the optimizing for higher rewards, I think, everyone agrees with me. But I just said a second statement, which is but we don't want to go too far from the initial model. So why would that be? Why would we want to not deviate too much from the base model? \[AUDIO OUT\] So one suggested answer is it will catastrophically forget what it has learned.

**中文**

我想，优化以获得更高奖励这一点，大家都同意。但我刚才还说了第二点，就是不希望偏离初始模型太远。为什么呢？为什么我们不希望偏离基础模型（base model）太多？\[音频缺失\] 有一个回答是，它会灾难性地遗忘已经学到的东西。

### [49:20](https://www.youtube.com/watch?v=PmW_TMQ3l0I&t=2960s) · b000099

**English**

Why would that be a problem? \[AUDIO OUT\]

**中文**

为什么这会是个问题？\[音频缺失\]

### [49:35](https://www.youtube.com/watch?v=PmW_TMQ3l0I&t=2975s) · b000100

**English**

Great. Yeah. I think it's a great way to put it. So the suggested answer here is you have all this knowledge in your initial model, which is pre-trained and then instruction tuned or tuned and you don't want to move away too much. This is exactly it. So that's one reason. What could be another reason? So definitely one. It's very, very good reason. What could be another reason? Yeah. \[AUDIO OUT\] Yep.

**中文**

很好，对。我觉得这样说非常好。这里提出的答案是，初始模型中已经有了所有这些知识，它经过了预训练，之后又经过指令调优（instruction tuning）或调优，所以不希望偏离太多。正是如此。这是一个原因。还有什么其他原因？这肯定是一个，而且是非常非常好的原因。还有什么原因？嗯。\[音频缺失\] 对。

### [50:05](https://www.youtube.com/watch?v=PmW_TMQ3l0I&t=3005s) · b000101

**English**

So overfitting on that data. So can you tell me more? \[AUDIO OUT\] Yeah. Great point. So the second suggested answer is you can overfit on data that is not super clean. And I will go a bit more into detail on what that means. Yeah. You wanted to add? \[AUDIO OUT\] Yep. Yeah. Exactly. So I guess your two points are, I guess, along the same lines, which is the reward model can be noisy.

**中文**

对这些数据过拟合（overfitting）。能再具体讲讲吗？\[音频缺失\] 对，很好的观点。第二个答案是，你可能会对不太干净的数据过拟合。我会再详细讲一下这是什么意思。对，你想补充？\[音频缺失\] 嗯，对，没错。我想，你们两人的观点方向是相同的，就是奖励模型可能有噪声。

### [50:37](https://www.youtube.com/watch?v=PmW_TMQ3l0I&t=3037s) · b000102

**English**

So that's exactly it. So it's a phenomenon that's called reward hacking, where if you are trying to optimize too much for the rewards, you're basically assuming that the reward is exactly quantifying what you want. But it may not be the case, because the reward model itself is imperfect. So just to make sure that everyone gets the point, I'm going to illustrate that with an example.

**中文**

正是如此。这是一种叫作奖励投机（reward hacking）的现象。如果你过度追求奖励，基本上就等于假设奖励准确量化了你想要的东西。但事实未必如此，因为奖励模型本身并不完美。为了确保大家理解这一点，我举个例子。

### [51:12](https://www.youtube.com/watch?v=PmW_TMQ3l0I&t=3072s) · b000103

**English**

So let's suppose that I'm giving a lecture. And my objective is for the lecture to be as informative as possible.

**中文**

假设我正在讲课，我的目标是让课程尽可能提供丰富的信息。

### [51:25](https://www.youtube.com/watch?v=PmW_TMQ3l0I&t=3085s) · b000104

**English**

So I can take the choice to have something that I can quantify to know if what I'm saying is informative. So let's suppose if my reward is how loud the claps are at the end of the lecture, if the clapping is a lot or not. The problem is if I optimize too much for the volume of clapping at the end, it may be the case that if I found out that you all like jokes and I start making jokes and then you clap at the end, my reward is maximized.

**中文**

我可以选择某种可量化的东西，来判断我讲的内容是否有信息量。假设我的奖励是课后掌声有多响，也就是掌声多不多。问题是，如果我过度优化课后掌声的音量，可能会出现这样的情况：我发现大家都喜欢笑话，于是开始讲笑话，最后大家鼓掌，我的奖励就最大化了。

### [52:05](https://www.youtube.com/watch?v=PmW_TMQ3l0I&t=3125s) · b000105

**English**

But my objective is not fulfilled, which is make the lecture informative. So in practice, this reward hacking phenomenon is something that leads your model to optimize too much on a metric or a score that is imperfect. So it can very well maximize the rewards but not fulfill what you want. And this is exactly what the idea behind reward hacking is. So yeah. And another reason by the way.

**中文**

但我的目标没有实现，也就是让课程有信息量。实际上，reward hacking 现象会让模型过度优化某个并不完美的指标或分数。它完全可能最大化奖励，却没有实现你想要的结果。这正是 reward hacking 背后的意思。对。顺便说，还有另一个原因。

### [52:36](https://www.youtube.com/watch?v=PmW_TMQ3l0I&t=3156s) · b000106

**English**

So it's one reason is because your base model is already great. It knows a lot of things. Second one is because the reward model is imperfect. So you have this reward hacking phenomenon. The third reason is also because you can have some training instabilities. Anyways, we have a bunch of reasons why we don't want to deviate too much.

**中文**

一个原因是，基础模型已经很好了，它知道很多东西。第二个原因是，奖励模型并不完美，因此会出现 reward hacking。第三个原因是，还可能出现训练不稳定。总之，有很多原因让我们不希望偏离太多。

### [52:59](https://www.youtube.com/watch?v=PmW_TMQ3l0I&t=3179s) · b000107

**English**

And so in this setup, you typically have more observations than in the reward model case. So you have typically at least 100K observations. And the label that you get here is from the reward model. And so you start with the model that you obtained after SFT. So that's the one that you trained. And the loss function will be something that will try for you to maximize the rewards but also to not have you deviate too much from the base model.

**中文**

在这种设定下，通常需要比奖励模型场景更多的观测样本。一般至少有 100K 个观测样本。这里得到的标签来自奖励模型。你从 SFT 之后得到的模型开始，也就是你训练过的那个模型。损失函数会尝试让你最大化奖励，同时又不让你偏离基础模型太多。

### [53:39](https://www.youtube.com/watch?v=PmW_TMQ3l0I&t=3219s) · b000108

**English**

So we're going to see exactly how we can do that. But that's the idea of how our loss function will look like. It will have these two parts.

**中文**

我们会具体看看如何实现。但这就是损失函数的大致思路。它会包含这两个部分。

### [53:49](https://www.youtube.com/watch?v=PmW_TMQ3l0I&t=3229s) · b000109

**English**

Sounds good? And as we saw, so we don't want it to deviate too much because of reward hacking and instability and so on. So in order to do that, you may have heard a very popular RL algorithm that's called PPO. So PPO stands for proximal policy optimization. So the reason why it's named proximal is because we do not want our model to deviate too much from the base model.

**中文**

没问题吧？正如我们看到的，由于 reward hacking、训练不稳定等原因，我们不希望模型偏离太多。为此，你们可能听说过一种很流行的 RL 算法，叫作 PPO。PPO 代表近端策略优化（proximal policy optimization）。之所以叫近端，是因为我们不希望模型偏离基础模型太多。

### [54:24](https://www.youtube.com/watch?v=PmW_TMQ3l0I&t=3264s) · b000110

**English**

And we're going to see how we do that. So this is roughly how our loss function will look like. So we'll have a part that is a reward model that we want to maximize. And then some other part that is around measuring how far the distribution of the policy that we're training is to the reference model or the base model. So here, the reference model would be your SFT model.

**中文**

我们会看看如何做到。损失函数大致会是这样：有一部分是我们希望最大化的奖励模型，另一部分则用于衡量我们正在训练的策略分布，与参考模型（reference model）或基础模型之间有多大差异。这里的参考模型就是 SFT 模型。

### [55:00](https://www.youtube.com/watch?v=PmW_TMQ3l0I&t=3300s) · b000111

**English**

So you have these two parts. Does the formulation of the loss roughly make sense so far? That makes sense?

**中文**

因此有这两个部分。到目前为止，这个损失的大致形式大家能理解吗？能理解吗？

### [55:12](https://www.youtube.com/watch?v=PmW_TMQ3l0I&t=3312s) · b000112

**English**

Cool. OK. KL divergence. So I'm just talking about KL divergence, but I don't want to just assume you know what that is. So the KL divergence is some measure. I don't want to say distance because distance has a lot of connotations to it. It's not a distance, but it's some measure of how far two probability distributions are. So you take a probability distribution, let's say, P and another one probability distribution Q. And you compute this formula, which is the sum of p i log of p i over q i.

**中文**

好。KL 散度（KL divergence）。我刚才在讲 KL divergence，但不想直接假设大家都知道它是什么。KL divergence 是一种度量。我不想说它是距离，因为距离有很多特定含义。它不是距离，但它可以衡量两个概率分布相差多远。取一个概率分布，比如 P，再取另一个概率分布 Q，计算这个公式，也就是对 p i 乘以 p i 除以 q i 的 log 求和。

### [55:55](https://www.youtube.com/watch?v=PmW_TMQ3l0I&t=3355s) · b000113

**English**

Just gives you a number of how distant or how far these two probability distributions are. So you want to minimize the loss. So I guess you want to minimize how far they are.

**中文**

它会给你一个数，表示这两个概率分布相距多远，或者相差多少。你希望最小化损失，所以，我想，你希望最小化它们之间的差异。

### [56:19](https://www.youtube.com/watch?v=PmW_TMQ3l0I&t=3379s) · b000114

**English**

Does that make sense that we're using this? Yeah. OK. So just one little question. So OK. Is the KL divergence positive or negative or what can you tell me about the KL divergence?

**中文**

能理解我们为什么使用它吗？好。这里有个小问题。KL divergence 是正的还是负的？或者，你能告诉我关于 KL divergence 的什么性质？

### [56:40](https://www.youtube.com/watch?v=PmW_TMQ3l0I&t=3400s) · b000115

**English**

Have you seen the-- yeah. It's positive. Why is it positive? \[AUDIO OUT\]

**中文**

你们见过——对，它是正的。为什么是正的？\[音频缺失\]

### [56:54](https://www.youtube.com/watch?v=PmW_TMQ3l0I&t=3414s) · b000116

**English**

Yeah. But why?

**中文**

对，但为什么呢？

### [56:59](https://www.youtube.com/watch?v=PmW_TMQ3l0I&t=3419s) · b000117

**English**

So maybe we can come later but great, great. I think the result is here, but I guess I want to why. Yes. Exactly. So yeah, if you use Jensen's inequality--because when you look at this formula, I mean, luck can take positive and negative values, it's not super clear. But yeah, the way you prove that it's always positive or equal to 0 is with the Jensen's inequality. And so yes, this quantity is equal to 0 if and only if P and Q are equal.

**中文**

也许我们可以稍后再讲，但很好，很好。我想结果已经说出来了，但我想知道为什么。对，完全正确。如果使用 Jensen 不等式（Jensen's inequality）——因为看这个公式时，我的意思是，luck \[字幕疑误，可能指 log\] 可以取正值，也可以取负值，所以并不是特别明显。证明它始终大于或等于 0 的方法，就是使用 Jensen's inequality。对，这个量等于 0，当且仅当 P 和 Q 相等。

### [57:34](https://www.youtube.com/watch?v=PmW_TMQ3l0I&t=3454s) · b000118

**English**

Cool. So with that, we're going to go a little bit more in depth into the loss function. So I mentioned that the loss function tries to maximize for rewards but also make it so that the model does not deviate too much from the base model. Well, there is something that I've lied a little bit about too, which is we don't want to maximize rewards.

**中文**

好。接下来，我们更深入地看一下损失函数。我提到过，损失函数一方面试图最大化奖励，另一方面让模型不要偏离基础模型太多。不过，有一点我刚才稍微说了点谎，那就是我们并不是要最大化奖励。

### [58:09](https://www.youtube.com/watch?v=PmW_TMQ3l0I&t=3489s) · b000119

**English**

We actually want to maximize a quantity called advantage. So what is the advantage? So you can think of the advantage as being how much better is your output compared to what you would expect.

**中文**

实际上，我们希望最大化一个叫作优势（advantage）的量。什么是 advantage？你可以把它理解为，输出比你预期的好多少。

### [58:29](https://www.youtube.com/watch?v=PmW_TMQ3l0I&t=3509s) · b000120

**English**

So people typically use advantage to make the whole process be, I guess, more stable, the training more stable. And we estimate that advantage with a function called a value function, which we will see in a little bit. Did you have a question? No, no question. So we have two quantities. Right. We have the reward that we saw previously how to compute, which is given a prompt, given a completion, how good is this prompt and completion?

**中文**

人们通常使用 advantage，让整个过程更稳定一些，让训练更稳定。我们会用一个叫作价值函数（value function）的函数来估计 advantage，稍后会讲到。你有问题吗？没有，没有问题。所以我们有两个量，对吧。一个是奖励，我们前面看过如何计算，也就是给定一个 prompt 和一个 completion，这个 prompt 与 completion 有多好？

### [59:08](https://www.youtube.com/watch?v=PmW_TMQ3l0I&t=3548s) · b000121

**English**

And then the value function is another estimation, but this estimation is not at the completion level. It is actually at the token level. So what we're doing here is we're taking the prompt along with the partial generation as input. And we're trying to estimate what the reward would be if we were to continue to generate the output following the policy.

**中文**

然后，价值函数（value function）是另一种估计，但这种估计不是在完整生成结果（completion）层面进行的，而是在词元（token）层面进行的。所以，我们这里做的是把提示词（prompt）和部分生成内容一起作为输入，尝试估计：如果我们按照策略（policy）继续生成输出，奖励（reward）会是多少。

### [59:45](https://www.youtube.com/watch?v=PmW_TMQ3l0I&t=3585s) · b000122

**English**

So I'm just going to repeat this one more time because it's charged in meaning. The value function is a token level estimation of the reward that takes in a partial input and predicts the reward. So that predicts the reward if you were to follow the policy in your generation. So this value function is something you will see in papers as something that people have to train when they do PPO.

**中文**

我再重复一遍，因为这句话包含的意思很多。value function 是对奖励的 token 级估计，它接收部分输入并预测奖励。也就是预测如果你按照 policy 进行生成，会得到多少奖励。所以，你会在论文中看到，人们做 PPO 时需要训练这个 value function。

### [1:00:21](https://www.youtube.com/watch?v=PmW_TMQ3l0I&t=3621s) · b000123

**English**

And it's typically because people need to have this value function when they compute the advantage that I mentioned above. And this value function is typically trained jointly with the policy. So in other terms, you have your LLM, which is initialized as the SFT model, which generates the prediction. So what you typically do is also have some value head that also--so this time, it's not a classification problem.

**中文**

这通常是因为人们在计算我上面提到的优势（advantage）时，需要这个 value function。而这个 value function 通常与 policy 联合训练。换句话说，你有一个大语言模型（LLM），它初始化为监督微调（SFT）模型，用来生成预测。所以，通常你还会有一个价值头（value head），它也会——所以这一次，它不是一个分类问题。

### [1:01:05](https://www.youtube.com/watch?v=PmW_TMQ3l0I&t=3665s) · b000124

**English**

It's a regression problem. You try to estimate the final reward if you were to continue to generate according to policy. So this is typically something that you also need to train jointly with the policy. And I am intentionally not going too much into detail as to exactly how that advantage is formulated. It is just beyond the scope of this class. But in case you're interested, I would highly recommend reading this paper, which is mathematically involved about the generalized advantage estimation methods, which people typically use for this.

**中文**

它是一个回归问题。你尝试估计，如果继续按照 policy 生成，最终奖励会是多少。所以，这通常也是你需要与 policy 联合训练的东西。我有意不深入讲解这个 advantage 具体如何构造，因为这超出了本课的范围。但如果你感兴趣，我非常推荐阅读这篇论文，它涉及较多数学内容，讲的是广义优势估计（generalized advantage estimation）方法，人们通常用它来做这件事。

### [1:01:48](https://www.youtube.com/watch?v=PmW_TMQ3l0I&t=3708s) · b000125

**English**

So it's this high dimensional continuous control using generalized advantage estimation paper. So if you're interested, just feel free to take a look. But this is typically the method that people use to estimate these advantages. So now, we're going to see in a second where those advantages are used. But just as a high level, does that make sense to everyone what we're trying to achieve here? \[AUDIO OUT\] Yeah.

**中文**

就是这篇 high dimensional continuous control using generalized advantage estimation 论文。所以，如果你感兴趣，可以看一看。但这通常就是人们用来估计这些 advantage 的方法。稍后我们会看到这些 advantage 用在哪里。不过，先从总体上说，大家明白我们这里想实现什么了吗？\[音频缺失\] 对。

### [1:02:22](https://www.youtube.com/watch?v=PmW_TMQ3l0I&t=3742s) · b000126

**English**

So in other words, what we want is to maximize the rewards but not deviate too much from the base model. But what we want is to actually find a way to make the rewards a bit more relative as to what you would actually expect. So you want to compare the rewards that you're obtaining with an average response if you want.

**中文**

换句话说，我们希望最大化奖励，但不要偏离基础模型（base model）太远。不过，我们实际想找到一种方法，让奖励相对于你实际预期的结果更有相对性。所以，可以这么说，你想把得到的奖励与一个平均水平的回答进行比较。

### [1:02:53](https://www.youtube.com/watch?v=PmW_TMQ3l0I&t=3773s) · b000127

**English**

The idea is, OK, if you are having a great reward, what would be the reward in the average case? And you want to maximize that. And the reason why people use these reward minus baseline is because it reduces the variance of these estimates, and it just makes the training just go faster typically. So that's why people use that part. But in order to compute the advantage, what people use is a method called generalized advantage estimation, which you can think of it as a big formula with some hyper-parameters that is in the paper below.

**中文**

这个想法是，好，如果你得到了很高的奖励，那么平均情况下的奖励会是多少？你想最大化这个差值。人们使用这种奖励减去基线（baseline）的原因是，它能降低这些估计的方差，通常也能让训练更快。这就是使用这一部分的原因。但为了计算 advantage，人们使用一种叫 generalized advantage estimation 的方法，你可以把它看作下面这篇论文中一个带有若干超参数（hyper-parameters）的大公式。

### [1:03:40](https://www.youtube.com/watch?v=PmW_TMQ3l0I&t=3820s) · b000128

**English**

That's the general idea.

**中文**

大体思路就是这样。

### [1:03:44](https://www.youtube.com/watch?v=PmW_TMQ3l0I&t=3824s) · b000129

**English**

Cool. OK. Looking at the time, so we're going to look at two typical variants of the PPO loss. The first one is called PPO-Clip. So the idea here is to prevent the updates to our model from being too large from one iteration to the next. So what you have is this loss formulation, which is the minimum of the ratio, and we're going to see what that is, times the advantage and some clipping of that ratio between two bands, which we're going to see in a second, times that advantage.

**中文**

好。好的。看一下时间，我们接下来看看 PPO 损失（loss）的两种典型变体。第一种叫 PPO-Clip。这里的想法是防止模型从一次迭代到下一次迭代的更新幅度过大。所以，你会看到这个 loss 公式，它取两项的最小值：一项是比率（ratio）——我们会看看那是什么——乘以 advantage；另一项是把这个 ratio 裁剪（clipping）到两个界限之间——我们马上会看到——再乘以这个 advantage。

### [1:04:35](https://www.youtube.com/watch?v=PmW_TMQ3l0I&t=3875s) · b000130

**English**

So before we go into details, I just want to call out a few things that may seem like it's confusing because it was confusing to me. So first of all, that formula is expressed as L is equal to, but it's actually not something we want to minimize, something that we want to maximize. So what people typically mean by L is loss. So yeah, just know that we want to maximize that.

**中文**

在深入细节之前，我想先指出几件可能让人困惑的事，因为它们当时也让我困惑。首先，这个公式写作 L 等于，但实际上它不是我们想最小化的东西，而是我们想最大化的东西。人们通常用 L 表示 loss。所以，对，只要记住，我们想最大化它。

### [1:05:05](https://www.youtube.com/watch?v=PmW_TMQ3l0I&t=3905s) · b000131

**English**

We don't want to minimize. The second thing is we're introducing a term called R of theta. This is not the reward model. So typically, people use R to say the reward. But here, it's not the reward. It's actually the ratio in the probabilities between our policy and the policy from the previous step, which is denoted pi old, pi theta old.

**中文**

我们不想最小化它。第二点是，我们引入了一个叫 R of theta 的项。这不是奖励模型（reward model）。通常人们用 R 表示奖励，但这里它不是奖励。它实际上是我们的 policy 与上一步的 policy 之间的概率比率，后者记作 pi old，pi theta old。

### [1:05:38](https://www.youtube.com/watch?v=PmW_TMQ3l0I&t=3938s) · b000132

**English**

So it quantifies how different your policy at the current stage is to your old policy. So here, when we say, old, it's not the SFT model. It's not the SFT model. It's the model at the previous iteration during the oral stage, because here what we want is for the policy to not have updates that are too wide.

**中文**

所以，它量化了当前阶段的 policy 与旧 policy 有多大差别。这里我们说的 old 不是 SFT 模型，不是 SFT 模型，而是 oral 阶段 \[字幕疑误，可能指 RL 阶段\] 上一次迭代的模型，因为这里我们希望 policy 的更新幅度不要太大。

### [1:06:11](https://www.youtube.com/watch?v=PmW_TMQ3l0I&t=3971s) · b000133

**English**

So far, so good? Yeah. \[AUDIO OUT\] What is A? A is our advantage. So you can think of it as this complicated formula that's a function of the reward and the value function that just tells you how good your piece is basically. So this complicated formula, we're just going to see why it makes sense.

**中文**

到这里还好吗？对。\[音频缺失\] A 是什么？A 是我们的 advantage。你可以把它看作一个复杂公式，它是奖励和 value function 的函数，基本上就是告诉你，你生成的这一部分有多好。对于这个复杂公式，我们接下来只看看它为什么合理。

### [1:06:43](https://www.youtube.com/watch?v=PmW_TMQ3l0I&t=4003s) · b000134

**English**

So if the advantage is positive, it means that we somehow want to reinforce whatever was generated. And so here, our objective function will look like this. So if A is positive, then this L of CLIP will look some linear function as a function of R because it's R times A.

**中文**

如果 advantage 为正，就意味着我们想以某种方式强化刚才生成的内容。所以，这里的目标函数（objective function）会是这样的。如果 A 为正，那么这个 L of CLIP 作为 R 的函数，看起来会是一个线性函数，因为它是 R 乘以 A。

### [1:07:17](https://www.youtube.com/watch?v=PmW_TMQ3l0I&t=4037s) · b000135

**English**

So it's a linear function as a function of R. And then after 1 plus epsilon, it will just be flat. So why do we want such a shape for our graph? Well, we need to think again about what R means. So if A is positive, meaning it's something that we want to reinforce, we typically want the probability of whatever happened to be increased.

**中文**

所以，它是关于 R 的线性函数。然后，超过 1 加 epsilon 之后，它就会变平。那么，为什么我们想让图像呈现这样的形状？我们需要再次思考 R 的含义。如果 A 为正，意味着这是我们想强化的东西，那么我们通常希望刚才发生的事情的概率增加。

### [1:07:54](https://www.youtube.com/watch?v=PmW_TMQ3l0I&t=4074s) · b000136

**English**

So we want R to be higher, but we don't want it to be too high. So that's why we have this clipping mechanism.

**中文**

所以，我们希望 R 更高，但不希望它太高。这就是我们采用这种 clipping 机制的原因。

### [1:08:10](https://www.youtube.com/watch?v=PmW_TMQ3l0I&t=4090s) · b000137

**English**

So that's why we have this clipping here. We want to, I guess, maximize L. So we go towards increasing R, but we don't want to increase R too much. So that's the rationale for this. But when A is negative, it means that somehow what we've done is something that we don't want to do as much. So in order to maximize L, what we want is to actually decrease the probability of just generating what we generated.

**中文**

所以，这就是这里进行 clipping 的原因。我想，我们希望最大化 L。因此，我们朝着增大 R 的方向走，但不想让 R 增大太多。这就是背后的理由。但当 A 为负时，就意味着我们刚才做的事，是我们不想那么频繁去做的。所以，为了最大化 L，我们实际想降低再次生成刚才那些内容的概率。

### [1:08:50](https://www.youtube.com/watch?v=PmW_TMQ3l0I&t=4130s) · b000138

**English**

So we want R to be smaller because it also increases L, but we don't want it to be much smaller. We don't want too big of an update, which is why we have this clipping mechanism here. So in other words, this super complicated formula can be just intuitively explained with what I just mentioned, which is if you have positive advantages, you want to reinforce the fact of generating this output because this is something that the model likes.

**中文**

所以，我们希望 R 更小，因为这也会增大 L，但不希望它小太多。我们不想更新幅度太大，这就是这里采用 clipping 机制的原因。换句话说，这个超级复杂的公式可以用我刚才说的内容直观解释：如果 advantage 为正，你就想强化生成这个输出的行为，因为这是模型喜欢的东西。

### [1:09:29](https://www.youtube.com/watch?v=PmW_TMQ3l0I&t=4169s) · b000139

**English**

I mean, by model, I mean the reward model, but you don't want it to update it too much, which is why you have this clipping. And same when the advantage is less than 0. I guess you want to down weight the probability of this output from happening. So you want to have a smaller R, which is your ratio between the policy you're training with respect to the old one, but you don't want to be too small either, again, to not make too big of an update.

**中文**

我说的模型是指 reward model，但你不想让它更新太多，所以才有这个 clipping。advantage 小于 0 时也是一样。我想，你希望降低这个输出出现的概率。所以，你希望 R 更小，它是正在训练的 policy 相对于旧 policy 的比率，但也不希望它太小，同样是为了避免更新幅度过大。

### [1:10:04](https://www.youtube.com/watch?v=PmW_TMQ3l0I&t=4204s) · b000140

**English**

Does this make sense?

**中文**

这样说清楚吗？

### [1:10:09](https://www.youtube.com/watch?v=PmW_TMQ3l0I&t=4209s) · b000141

**English**

Does this roughly make sense? OK. Roughly makes sense. Cool. I will just recommend just rereading this formula, just remembering what I mentioned. And hopefully, it will make a bit more sense. But yeah, happy to answer any questions if there are any. Yeah. Oh, yeah. Yeah. \[AUDIO OUT\]

**中文**

大致明白了吗？好。大致明白。很好。我建议大家再读一遍这个公式，记住我刚才说的内容。希望这样会更容易理解一些。不过，对，如果有任何问题，我很乐意回答。对。哦，对。对。\[音频缺失\]

### [1:10:43](https://www.youtube.com/watch?v=PmW_TMQ3l0I&t=4243s) · b000142

**English**

So the question is, what happens where it's not--it's the same as ReLU. You will basically use the same methods. So yeah, it's the same thing. Yeah. \[AUDIO OUT\] So great question. The question is, why are you using from the previous iteration and not the base model? Because actually, we don't want just to not be too far from the base model. We also want our updates to be not too extreme from one iteration to another.

**中文**

问题是，在它不——的地方会发生什么？这和 ReLU 一样。你基本上会使用相同的方法。所以，对，是一样的。对。\[音频缺失\] 很好的问题。问题是，为什么使用上一次迭代的模型，而不是 base model？因为实际上，我们不仅希望不要偏离 base model 太远，还希望从一次迭代到下一次迭代的更新不要过于极端。

### [1:11:16](https://www.youtube.com/watch?v=PmW_TMQ3l0I&t=4276s) · b000143

**English**

And this is to improve with stability of training. So this is just like another additional constraint we want. \[AUDIO OUT\] Question is are we considering the base model? We will consider it. And I will tell you exactly. But in this formulation, we are not. In this formulation, we are not. But in the formulation we're using typically for LLM based RL, we are and we will see how.

**中文**

这是为了提高训练的稳定性。所以，这就像我们想要的另一个附加约束。\[音频缺失\] 问题是，我们有没有考虑 base model？我们会考虑它。我会具体告诉你。但在这个公式中，没有。在这个公式中，没有。但在我们通常用于基于 LLM 的强化学习（RL）的公式中，会考虑它，我们会看看是怎么做的。

### [1:11:46](https://www.youtube.com/watch?v=PmW_TMQ3l0I&t=4306s) · b000144

**English**

Yeah. \[AUDIO OUT\]

**中文**

对。\[音频缺失\]

### [1:12:04](https://www.youtube.com/watch?v=PmW_TMQ3l0I&t=4324s) · b000145

**English**

Yeah. So the question is, how do you quantify R? What is R? What does it mean? So it's typically the probability of a token happening with respect to the inputs. So you can think of the probability distribution that you get at the output of your LLM. So you would use that.

**中文**

对。问题是，如何量化 R？R 是什么？它意味着什么？通常就是给定输入时，一个 token 出现的概率。你可以想一下 LLM 输出端得到的概率分布。你会使用那个。

### [1:12:24](https://www.youtube.com/watch?v=PmW_TMQ3l0I&t=4344s) · b000146

**English**

Cool. So this is the first variant that the PPO paper mentions. So it's called PPO-Clip.

**中文**

好。这就是 PPO 论文提到的第一种变体，叫 PPO-Clip。

### [1:12:33](https://www.youtube.com/watch?v=PmW_TMQ3l0I&t=4353s) · b000147

**English**

So the second variant that we have is the one that uses KL divergence, which is called KL penalty. And this one is a function of the ratio times the advantage minus the KL divergence between the old policy, which is the previous iteration, and the current iteration. So you had a great point, which is why are we using the old?

**中文**

我们讲的第二种变体使用 KL 散度（KL divergence），叫 KL 惩罚（KL penalty）。它是一个由 ratio 乘以 advantage，再减去旧 policy——也就是上一次迭代——与当前迭代之间的 KL divergence 构成的函数。你刚才提出了一个很好的问题：为什么我们使用旧的？

### [1:13:03](https://www.youtube.com/watch?v=PmW_TMQ3l0I&t=4383s) · b000148

**English**

In fact, old means previous RL iteration. But nowadays, people use the reference. So it's just a change--because this paper has been published in 2017, where in 2025, LLMs, they came more into something that was popular in the 2020s. So yeah, there's just been this difference in what you put there. So yeah, it's indeed the reference that you would typically put in a KL divergence.

**中文**

事实上，old 指的是上一次 RL 迭代。但现在，人们使用参考模型（reference）。所以，这只是一个变化——因为这篇论文发表于 2017 年，而我们现在是 2025 年，LLM 是在 2020 年代变得流行起来的。所以，对，放在那里的东西有了这个区别。对，你通常放进 KL divergence 中的确实是 reference。

### [1:13:38](https://www.youtube.com/watch?v=PmW_TMQ3l0I&t=4418s) · b000149

**English**

The other thing that I will say is that nowadays, when someone wants to train a policy using PPO, they would typically use the KL divergence, and they would also maybe mix it with the clipping thing with the old iteration. They will basically mix the two. There are many different formulations of what the loss can be. So what I'm saying is not always true.

**中文**

我还想说一点，如今有人想用 PPO 训练 policy 时，通常会使用 KL divergence，也可能把它与相对于上一次迭代的 clipping 结合起来。基本上就是把这两种方法混合使用。loss 可以有很多不同的公式。所以，我说的并不总是成立。

### [1:14:09](https://www.youtube.com/watch?v=PmW_TMQ3l0I&t=4449s) · b000150

**English**

But this is what people sometimes do. They sometimes mix the two.

**中文**

但这是人们有时会做的事。他们有时会把两者结合起来。

### [1:14:15](https://www.youtube.com/watch?v=PmW_TMQ3l0I&t=4455s) · b000151

**English**

Cool. So I talked to you about PPO and how it allowed you to maximize rewards, maximize advantages by not making your model deviate too much from the base model and also from the previous iteration. But the problem is that for PPO, you need a lot of models. So you need your policy, you need your LLM that you're training. You also need the value function, which what I mentioned is used for the advantage estimation.

**中文**

好。我已经讲了 PPO，以及它如何在让模型不要过度偏离 base model 和上一次迭代模型的同时，最大化奖励、最大化 advantage。但问题是，PPO 需要很多模型。你需要 policy，需要正在训练的 LLM。你还需要 value function，我提到过，它用于 advantage 估计。

### [1:14:53](https://www.youtube.com/watch?v=PmW_TMQ3l0I&t=4493s) · b000152

**English**

You also need the reward model of course. And then you need the base model. So the base model is frozen, so just the SFT model just to be able to compare with the current policy. So it's a lot of models. So now, the question that you may ask is, do you really need to have all these models to perform well? And the answer is maybe not, maybe but maybe not.

**中文**

当然，你还需要 reward model。然后，你需要 base model。base model 是冻结的，就是那个 SFT 模型，用来与当前 policy 进行比较。所以，模型很多。现在，你可能会问：真的需要所有这些模型，才能表现好吗？答案是可能不需要，也许需要，但也许不需要。

### [1:15:24](https://www.youtube.com/watch?v=PmW_TMQ3l0I&t=4524s) · b000153

**English**

And nowadays, there is a bunch of other methods that are becoming more popular. So you may have heard in GRPO in the context of reasoning models. So we will look at GRPO in more detail next week for lecture 6. But just know that there are many variants. So PPO is just one algorithm that has been very popular. And even within PPO, there's been many variants.

**中文**

如今，还有许多其他方法正在变得更流行。你可能在推理模型的语境中听说过 GRPO。我们将在下周第 6 讲更详细地介绍 GRPO。但你只需要知道，存在很多变体。PPO 只是一个曾经非常流行的算法。即使在 PPO 内部，也有很多变体。

### [1:15:55](https://www.youtube.com/watch?v=PmW_TMQ3l0I&t=4555s) · b000154

**English**

And nowadays, there are many other RL algorithms that are being used. Yeah. And yeah, if you want to just anticipate next lecture, you can also take a look at this paper from the Deep Seek team. So Deep Seek Math limits of mathematical reasoning in open language models that introduces the GRPO algorithm. But if you don't, it's fine. We're going to talk about it next week.

**中文**

如今，还有许多其他 RL 算法正在被使用。对。如果你想提前了解下一讲，也可以看看 Deep Seek \[字幕疑误，可能指 DeepSeek\] 团队的这篇论文。就是 Deep Seek Math limits of mathematical reasoning in open language models \[字幕疑误，可能指 DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models\]，它提出了 GRPO 算法。但不看也没关系，我们下周会讲。

### [1:16:27](https://www.youtube.com/watch?v=PmW_TMQ3l0I&t=4587s) · b000155

**English**

So I also want to talk about some challenges when it comes to RL-based approaches. So the first one is you need to have this two-stage process. You need to first train your reward model, and then you need to use the reward model to train your policy. But the problem is you do step one, you do step two, and then you realize, oh, wait, step one has a problem. Then you need to redo everything.

**中文**

我还想谈谈基于 RL 的方法面临的一些挑战。第一点是，你需要这个两阶段过程。你必须先训练 reward model，然后用 reward model 训练 policy。但问题是，你做了第一步，又做了第二步，然后才意识到，哦，等等，第一步有问题。那么你就需要把一切重做一遍。

### [1:16:58](https://www.youtube.com/watch?v=PmW_TMQ3l0I&t=4618s) · b000156

**English**

So there is a bunch of dependencies that can really make your life harder. And just the training recipe is not the simplest. So that's one downside. The second downside is about the number of hyper-parameters that you need to tune. So we saw beta from the KL divergence formulation. So that's one. We have epsilon from the PPO-Clip version.

**中文**

所以，这里面有很多依赖关系，真的会让事情变得更难。而且，训练方案本身也不是最简单的。这是一个缺点。第二个缺点是需要调节的超参数数量。我们看到了 KL divergence 公式中的 beta，这是一个。PPO-Clip 版本中还有 epsilon。

### [1:17:28](https://www.youtube.com/watch?v=PmW_TMQ3l0I&t=4648s) · b000157

**English**

That's another one. The generalized advantage estimation, we have not seen the formula. But there's, I think, at least two hyper-parameters that I can think of. Anyways, you have a bunch of them. So of course, some hyper-parameters perform better than others. And if you need to retrain, then, well, you need to do everything again. Then you have some instability challenges. So you can constrain your iterations to not be too wide to control for that but sometimes, it's not sufficient.

**中文**

这是另一个。generalized advantage estimation 的公式我们还没看过，但我想，至少有两个超参数是我能想到的。总之，你有一大堆超参数。当然，有些超参数比另一些表现更好。如果需要重新训练，那么，你就得把所有事情再做一遍。然后还有不稳定性方面的挑战。你可以限制每次迭代的幅度不要太大，以此加以控制，但有时这还不够。

### [1:18:08](https://www.youtube.com/watch?v=PmW_TMQ3l0I&t=4688s) · b000158

**English**

So in terms of the metric that you can use to monitor the training, well, what is the metric you would use?

**中文**

那么，在用来监控训练的指标方面，你会使用什么指标？

### [1:18:19](https://www.youtube.com/watch?v=PmW_TMQ3l0I&t=4699s) · b000159

**English**

So we're trying to maximize rewards in some sense. So typically, the metric that you would use to monitor your training would be the average rewards. But this is not a great--I mean, this is a way to monitor your training, but this is not the best way necessarily. So at least when it came to pre-training and SFT, you had this cross entropy loss that you were monitoring that was really telling you how your model was able to just reproduce the behavior you were trying to make it outputs.

**中文**

从某种意义上说，我们在尝试最大化奖励。所以，通常你会使用平均奖励来监控训练。但这并不是一个很好的——我的意思是，这是一种监控训练的方法，但未必是最好的方法。至少在预训练（pre-training）和 SFT 中，你可以监控交叉熵损失（cross entropy loss），它确实能告诉你，模型在多大程度上能够复现你希望它输出的行为。

### [1:18:58](https://www.youtube.com/watch?v=PmW_TMQ3l0I&t=4738s) · b000160

**English**

But yeah, so this is another challenge. And then the other thing is in the RL world, in order for you to know which completion you should not do and which completion you should do more, you need to have some diversity whenever you generate. So if during the RL training loop, every time you have a prompt, you generate something, and then you retry, and you generate something else that's too close, well, it's not great because you're not exploring the set of possible completions.

**中文**

但对，这是另一个挑战。还有一点，在 RL 中，为了知道哪些 completion 不应该生成，哪些应该多生成，你每次生成时都需要有一定的多样性。如果在 RL 训练循环中，每次有一个 prompt，你生成一些内容，然后再试一次，生成的另一个内容又太相似，那就不太好，因为你没有探索可能的 completion 集合。

### [1:19:34](https://www.youtube.com/watch?v=PmW_TMQ3l0I&t=4774s) · b000161

**English**

So this is another challenge you need to have in mind, which is you need to force your model to do some exploration to see, I guess, what can be good. And then the last point is, I mean, a lot of you were not familiar with RL. I was not, and it's not super clear why we would necessarily need RL to do this stage.

**中文**

所以，这是另一个需要记住的挑战：你需要迫使模型做一些探索（exploration），看看，我想，哪些东西可能是好的。最后一点，我的意思是，你们中很多人不熟悉 RL。我以前也不熟悉，而且为什么一定需要用 RL 来完成这个阶段，也不是特别清楚。

### [1:20:03](https://www.youtube.com/watch?v=PmW_TMQ3l0I&t=4803s) · b000162

**English**

Also, I will say one thing. So this RL-based training, you will hear a lot the term on policy training. I just want to tell you what that means. So what is different between this and SFT is during SFT, we had some prompts and some response that we wanted our model to generate, to mimic. But here, what we're doing is at each iteration, we're asking our model to generate an output, and then we're using how good that output is to update our model.

**中文**

另外，我还想说一件事。在这种基于 RL 的训练中，你会经常听到同策略训练（on policy training）这个术语。我只想告诉你它是什么意思。它与 SFT 的区别是，在 SFT 中，我们有一些 prompt 和一些希望模型生成、模仿的回答。但这里，我们做的是在每次迭代时让模型生成一个输出，然后根据这个输出有多好来更新模型。

### [1:20:46](https://www.youtube.com/watch?v=PmW_TMQ3l0I&t=4846s) · b000163

**English**

So there is a core difference between the two, because in here, what we're doing is we're asking the model to generate something, whereas for SFT, we're just using some data that is not necessarily generated by our model. So on policy training refers to training that involves the model generating from its current policy and optimizing on that.

**中文**

所以，两者有一个核心区别，因为在这里，我们让模型生成一些内容；而对于 SFT，我们只是使用一些数据，这些数据未必由我们自己的模型生成。因此，on policy training 指的是让模型根据其当前 policy 生成内容，并基于这些内容进行优化的训练。

### [1:21:17](https://www.youtube.com/watch?v=PmW_TMQ3l0I&t=4877s) · b000164

**English**

And this is in contrast with off policy training, which is relying on generations that are not done by the model that you're training.

**中文**

这与异策略训练（off policy training）形成对照，后者依赖的生成内容并非由你正在训练的模型产生。

### [1:21:31](https://www.youtube.com/watch?v=PmW_TMQ3l0I&t=4891s) · b000165

**English**

Does this make sense? Yeah. So this is a term you will see a lot, which is why I'm telling you. And yeah, so PPO is an on policy algorithm. Yeah. \[AUDIO OUT\]

**中文**

这样清楚吗？对。这是一个你会经常看到的术语，所以我才告诉你。对，所以 PPO 是一种 on policy 算法。对。\[音频缺失\]

### [1:21:53](https://www.youtube.com/watch?v=PmW_TMQ3l0I&t=4913s) · b000166

**English**

So the question is, why don't we do SFT on this preference data? Well, SFT, you tell the model, you should generate this given this input, then you should generate this given this input. But you're not telling it about things you should not generate. Let's suppose you have something that you don't want to happen, unless you rewrite that into perfect sentence, there is no way for you in the traditional SFT framework to tell your model to not generate that.

**中文**

问题是，为什么不在这些偏好数据（preference data）上做 SFT？在 SFT 中，你告诉模型，给定这个输入，你应该生成这个；然后，给定这个输入，你应该生成这个。但你没有告诉它哪些东西不应该生成。假设有某些你不希望出现的内容，除非你把它改写成一个完美的句子，否则在传统 SFT 框架中，你没办法告诉模型不要生成它。

### [1:22:27](https://www.youtube.com/watch?v=PmW_TMQ3l0I&t=4947s) · b000167

**English**

But that being said, it's a great prompt because later on in, let's say, 10 minutes, we will see a supervised way of doing what we did with RL. But yeah, it will be in about 10 minutes. But apart from that, does that roughly make sense? Yeah. Perfect. So in the next few minutes, we will see a method that is actually used more often than not. And this is for people who have a reward model but that don't want to do RL.

**中文**

不过，这个问题提得很好，因为再过，比如说，10 分钟，我们会看到一种用监督学习（supervised learning）来完成刚才用 RL 所做事情的方法。对，大约 10 分钟后会讲。不过，除此之外，大致清楚了吗？对。很好。接下来的几分钟，我们会看一种实际上更常被使用的方法。它适用于那些有 reward model，但不想做 RL 的人。

### [1:23:03](https://www.youtube.com/watch?v=PmW_TMQ3l0I&t=4983s) · b000168

**English**

So why do you not want to do RL? Because it's expensive. You need a lot of models. So to your point, it's indeed expensive because you need all these models. And sometimes it's just too hard to tune that training. So you have these methods called best of N or BoN. And the idea here is to leverage the reward model that you obtained in order to choose the output that you will return to the user.

**中文**

为什么不想做 RL？因为它很昂贵。你需要很多模型。所以，回应你的观点，它确实很昂贵，因为你需要所有这些模型。有时，要把训练调好也实在太难。因此，有一类方法叫 best of N，或 BoN。这里的想法是利用已经得到的 reward model，来选择要返回给用户的输出。

### [1:23:36](https://www.youtube.com/watch?v=PmW_TMQ3l0I&t=5016s) · b000169

**English**

So the idea here is you have a prompt, and you tell your models, OK, you actually want to have several generations. So you generate, let's say, 4 times, 5 times. And what you do is you give a score to each prompt completion, and you just return the best one, the top rated one, which is why it's called best of N.

**中文**

这里的想法是，你有一个 prompt，然后告诉模型，好，你实际上希望进行多次生成。比如，生成 4 次、5 次。然后，你给每个 prompt 的 completion 打分，只返回最好的那个、评分最高的那个，这就是它叫 best of N 的原因。

### [1:24:07](https://www.youtube.com/watch?v=PmW_TMQ3l0I&t=5047s) · b000170

**English**

So you have N completions. You rate all of them, and you just return the best one. So you have your prompt. So our favorite example, suggest a new activity I could do with my teddy bear. You put it into your SFT model. So you're not training your SFT model. It's as is. And you're just generating, let's suppose, three completions. The first one is a great answer. The second one is no, don't spend time with the teddy bear, which is not a good answer.

**中文**

你有 N 个 completion。你给它们全部打分，然后只返回最好的那个。你有一个 prompt。还是我们最喜欢的例子：推荐一项我可以和泰迪熊一起做的新活动。你把它放进 SFT 模型。这里不训练 SFT 模型，直接按原样使用。然后，假设你生成三个 completion。第一个是很好的回答。第二个是，不要，别花时间陪泰迪熊，这不是一个好回答。

### [1:24:39](https://www.youtube.com/watch?v=PmW_TMQ3l0I&t=5079s) · b000171

**English**

And then the third one, I think, is also a good one, take your teddy bear to a picnic. You put all of these into your reward model. And this is where I wanted to respond to you, what is an output of the reward model? So it would be a score like this. So for instance, the first one would be a pretty good completion, so it's 0.8. The second one is not good at all. Let's say, minus 2. And the third one is, let's say, so-so, so in between. So the best of N method would select the top rated one, which is the first one, and this is the one that you would return.

**中文**

然后第三个，我觉得也是个好回答：带你的泰迪熊去野餐。你把所有这些内容放进 reward model。这就是我想回答你刚才那个问题的地方：reward model 的输出是什么？它会是这样的分数。比如，第一个是相当不错的 completion，所以是 0.8。第二个一点也不好，假设是负 2。第三个，假设一般般，所以分数在中间。因此，best of N 方法会选择评分最高的那个，也就是第一个，而这就是你会返回的内容。

### [1:25:22](https://www.youtube.com/watch?v=PmW_TMQ3l0I&t=5122s) · b000172

**English**

So what is one problem with this approach? \[AUDIO OUT\] So the answer is if the model is bad, then it's going to be bad. That's fair. But I guess if you make enough completions with, let's say, a high enough temperature, you will have some diversity. So it's a fair point, which can be a problem, but let's suppose it's indeed a problem. Let's suppose it's not a problem. What is another problem that you may have?

**中文**

那么，这种方法有什么问题？\[音频缺失\] 回答是，如果模型很差，那么结果就会很差。这话有道理。但我想，如果你生成足够多的 completion，并且，比如说，使用足够高的温度（temperature），就会有一定的多样性。这是一个合理的观点，也可能成为问题，但我们先假设它确实是个问题。我们先假设它不是问题。你还可能遇到什么问题？

### [1:25:57](https://www.youtube.com/watch?v=PmW_TMQ3l0I&t=5157s) · b000173

**English**

Yep. \[AUDIO OUT\] Yes. Yes So the answer is you query the model many times, which is indeed the problem. So you're at inference. What you want is to not spend a bunch of money and compute. But here, what you're doing is complete your prompt multiple times. And this is indeed the main challenge with this. So you indeed skip the RL training, but you're basically pushing all the work to your inference, to the inference stage.

**中文**

对。\[音频缺失\] 是的。是的。回答是，你要多次查询模型，这确实是问题所在。你现在处于推理（inference）阶段。你希望不要花费大量金钱和计算资源。但这里，你要对同一个 prompt 进行多次补全。这确实是这种方法的主要挑战。你确实跳过了 RL 训练，但基本上是把所有工作都推到了 inference，推到了推理阶段。

### [1:26:33](https://www.youtube.com/watch?v=PmW_TMQ3l0I&t=5193s) · b000174

**English**

And this is just making everything so super costly. So when can it be bad? So if, for instance, you're in a case where you need to serve your model to, let's say, a bunch of traffic, it may not make sense for you just from a cost standpoint. So I would say, before taking that route, it may be good to just assess what will be your inference traffic, what would be your training cost, and determine that from there.

**中文**

这会让一切变得非常昂贵。那么，它什么时候会不好？比如，如果你需要让模型服务于，比如说，大量请求，那么仅从成本角度来看，这种方法可能就不合理。所以我会说，在走这条路线之前，最好先评估推理请求量会有多大，训练成本会是多少，然后再据此决定。

### [1:27:08](https://www.youtube.com/watch?v=PmW_TMQ3l0I&t=5228s) · b000175

**English**

And yeah, I think that's pretty much it. Do we have any questions on that part? Oh, yeah. Yeah. \[AUDIO OUT\]

**中文**

对，我想差不多就是这些。这一部分有什么问题吗？哦，对。对。\[音频缺失\]

### [1:27:25](https://www.youtube.com/watch?v=PmW_TMQ3l0I&t=5245s) · b000176

**English**

That sigmoid would be softmax. Are you talking about this one?

**中文**

那个 sigmoid 会是 softmax。你说的是这个吗？

### [1:27:31](https://www.youtube.com/watch?v=PmW_TMQ3l0I&t=5251s) · b000177

**English**

So in that algorithm, you're assuming that your reward model is trained. So the best of N approach is you do this training. So I guess the sigma here is pairwise because you trained your model in a pairwise fashion.

**中文**

在那个算法中，你假设 reward model 已经训练好了。所以，best of N 方法是先进行这个训练。我想这里的 sigma 是成对（pairwise）的，因为你是以 pairwise 的方式训练模型的。

### [1:27:52](https://www.youtube.com/watch?v=PmW_TMQ3l0I&t=5272s) · b000178

**English**

But in the best of N case, what you do is you just use your reward model to score N times, and you just pick the highest one. Yeah. \[AUDIO OUT\]

**中文**

但在 best of N 的情况下，你只是用 reward model 打分 N 次，然后选择分数最高的那个。对。\[音频缺失\]

### [1:28:33](https://www.youtube.com/watch?v=PmW_TMQ3l0I&t=5313s) · b000179

**English**

Yeah. The question is, but what if all the responses are bad? This is definitely a fair concern. And this is indeed a concern. So your model needs to be at least a little bit good.

**中文**

对。问题是，如果所有回答都很差怎么办？这绝对是一个合理的担忧，也确实值得担忧。所以，你的模型至少得稍微好一点。

### [1:28:47](https://www.youtube.com/watch?v=PmW_TMQ3l0I&t=5327s) · b000180

**English**

Yeah. Exactly. Yeah. Yeah. Yeah. \[AUDIO OUT\]

**中文**

对。正是如此。对。对。对。\[音频缺失\]

### [1:29:02](https://www.youtube.com/watch?v=PmW_TMQ3l0I&t=5342s) · b000181

**English**

It's a great question. Do you have any constraint on the scale? Well, depending on how your scaling is done, you actually don't care about the scale as long as you take the best one, the highest one on. If you think about it, let's suppose if you scale it, let's say, with a normal score, the highest one will still stay the highest one. So in this case, you actually do not care about the scale. \[AUDIO OUT\] Yes. You also don't care about that. But typically, the scaling matters when it is coming into play in a loss function, which is the case for RL.

**中文**

这是个很好的问题。对分值尺度（scale）有什么约束吗？这取决于你如何进行缩放（scaling），只要取最好的、分数最高的那个，你实际上并不在乎 scale。想一下，假设你对它进行缩放，比如使用一个普通的分数，最高的那个仍然会是最高的。所以，在这种情况下，你实际上不在乎 scale。\[音频缺失\] 对。那个你也不在乎。但通常，当 scaling 参与 loss function 时，它就很重要，RL 就是这种情况。

### [1:29:41](https://www.youtube.com/watch?v=PmW_TMQ3l0I&t=5381s) · b000182

**English**

And so that's where people use some scaling mechanism. That's the part that matters.

**中文**

所以，人们会在那里使用某种 scaling 机制。那才是重要的部分。

### [1:29:50](https://www.youtube.com/watch?v=PmW_TMQ3l0I&t=5390s) · b000183

**English**

Cool. And with that, I'm going to give it to Shervin. Thank you, Afshin. So for this last part, we're going to talk about DPO. But I'm not going to tell you what DPO means just yet. We're just going to first listen to the complaints we had in the RL world and then see what we could do about it and then how have folks remedied it. So the first thing that I'm going to repeat from what Afshin covered is that in the RL formulation of PPO, you have to carry, during your loss optimization, a bunch of model weights.

**中文**

好。接下来交给 Shervin。谢谢你，Afshin。最后这一部分，我们来讲 DPO。但我暂时不告诉你 DPO 是什么意思。我们先听听对 RL 的那些抱怨，再看看能做些什么，以及人们是如何补救的。首先，我要重复 Afshin 讲过的一点：在 PPO 的 RL 公式中，优化 loss 时，你必须带着一大堆模型权重。

### [1:30:34](https://www.youtube.com/watch?v=PmW_TMQ3l0I&t=5434s) · b000184

**English**

So when you look at this loss function, you have, first, the policy of the current model you have to optimize for, the one of the old model or the reference model. And then you have your advantage which hides the reward model, as well as the value function that we discussed. So all this four, which is a lot. And the second thing is that, let's say, you go with the approach of best of N, you don't do RL, you just generate multiple times and then pick the best completion.

**中文**

当你看这个 loss function 时，首先有需要优化的当前模型的 policy，还有旧模型或 reference model 的 policy。然后是 advantage，其中包含了 reward model，以及我们讨论过的 value function。所以总共是这四个，很多。第二点是，假设你采用 best of N 方法，不做 RL，只是多次生成，然后挑选最好的 completion。

### [1:31:12](https://www.youtube.com/watch?v=PmW_TMQ3l0I&t=5472s) · b000185

**English**

As Afshin mentioned, so you have this latency and cost issues. And just for the sake of thoughts, for a thought experiment, let's suppose we had infinite money, would it be still fine? So let's suppose you generate all of these in parallel. So you would still need to wait for the maximum time of the generation of an answer to give you a resulting answer.

**中文**

正如 Afshin 所说，这样就有延迟（latency）和成本问题。单纯想一想，做个思想实验，假设我们有无限的钱，那就没问题了吗？假设你并行生成所有这些回答，你仍然需要等到生成答案所需的最长时间过去，才能得到最终答案。

### [1:31:43](https://www.youtube.com/watch?v=PmW_TMQ3l0I&t=5503s) · b000186

**English**

And then if you look at the distribution of latency, usually it's some shape that is not centered on a single point. And when you look at the probability distribution of the max of, let's say, N answers, it will tend to be shifted to the right. So let's suppose you have infinite money, infinite compute, you still have to wait more than you would have on a single pass.

**中文**

再看 latency 的分布，它通常呈某种形状，并不集中在一个点上。当你看，比如说，N 个回答中最大延迟的概率分布时，它往往会向右偏移。所以，即使你有无限的钱、无限的计算资源，你仍然需要比单次运行等待更长的时间。

### [1:32:12](https://www.youtube.com/watch?v=PmW_TMQ3l0I&t=5532s) · b000187

**English**

Do these concerns make sense?

**中文**

这些担忧大家理解吗？

### [1:32:16](https://www.youtube.com/watch?v=PmW_TMQ3l0I&t=5536s) · b000188

**English**

And OK. So there comes the question that someone was asking, why don't we do supervision all this time? And this is the route that DPO folks have explored. So DPO stands for direct preference optimization. So instead of doing these expensive two-step process of, first, finding some reward model and then iterating on the model's weights, it optimizes a single loss function that directly optimizes for the model's weight.

**中文**

好。于是就有了刚才有人提出的问题：为什么不一直用监督学习呢？这就是 DPO 的研究者探索的路线。DPO 代表直接偏好优化（direct preference optimization）。它不再采用那种昂贵的两步过程——先找到一个 reward model，再迭代更新模型权重——而是优化一个直接针对模型权重的单一 loss function。

### [1:32:50](https://www.youtube.com/watch?v=PmW_TMQ3l0I&t=5570s) · b000189

**English**

And as you can see, there is no reward involved anymore, so no R. And you have a way to formulate what you care about as a function of your preference pairs. So in that loss function, all you have is a bunch of variables and then the sigmoid functions. But within the parentheses, you have the probability of a given completion to happen. And you have this subtraction operation that compares the probability of the winning completion to happen versus the losing one.

**中文**

如你所见，这里不再涉及奖励，所以没有 R。你可以把关心的目标表述为偏好对（preference pairs）的函数。在这个 loss function 中，只有一些变量和 sigmoid 函数。但在括号内，有某个给定 completion 出现的概率。还有这个减法运算，用来比较胜出 completion 出现的概率与落败 completion 出现的概率。

### [1:33:31](https://www.youtube.com/watch?v=PmW_TMQ3l0I&t=5611s) · b000190

**English**

So as you can see, it's a direct expression with respect to these preference pairs, which is pretty nice. And if you look at it a bit closer, you will recognize what afshin just mentioned regarding Bradley-Terry formulation because you have these expected value of log of a sigmoid. And then within that sigmoid, you have a difference of terms, where you can recognize the equivalent of what you saw as a reward term.

**中文**

所以，如你所见，这是直接关于这些 preference pairs 的表达式，相当不错。如果再仔细看一点，你就会认出 afshin 刚才提到的 Bradley-Terry 公式，因为这里有 sigmoid 的对数的期望值。然后，在这个 sigmoid 内部，是两个项的差，你可以认出，它们等价于之前看到的奖励项。

### [1:34:10](https://www.youtube.com/watch?v=PmW_TMQ3l0I&t=5650s) · b000191

**English**

So I know it's a lot to see at once. The formula is not super pretty. Do you have any questions? And then we're going to discuss in a bit what that beta is and also how we obtain this formula in the first place.

**中文**

我知道，一下子看这么多内容有点多。这个公式不是特别漂亮。有什么问题吗？接下来我们会稍微讨论一下这个 beta 是什么，以及这个公式最初是怎么得到的。

### [1:34:29](https://www.youtube.com/watch?v=PmW_TMQ3l0I&t=5669s) · b000192

**English**

And one thing I will mention before going to that is that the paper is titled your language model is secretly a reward model. And the reason for that is that the reward placeholder that you could identify from this loss function is expressed as a function of your policy. So you don't have any r's in there. But when you express the equivalent of a reward, you find the expression of your model directly.

**中文**

在讲这个之前，我要提一点：这篇论文的标题是 your language model is secretly a reward model。原因是，你能从这个 loss function 中识别出的奖励占位项，被表示成了 policy 的函数。所以，里面没有任何 r。但当你把相当于奖励的东西表达出来时，会直接得到模型的表达式。

### [1:35:02](https://www.youtube.com/watch?v=PmW_TMQ3l0I&t=5702s) · b000193

**English**

So which is pretty interesting insights. OK. So but now, let's think together about how we got there in the first place. So you recall from a few slides ago the PPO objective that we had. So we wanted to maximize rewards and minimize the distance of the obtained policy with respect to the reference one, which is this trade-off between maximizing rewards and KL divergence term.

**中文**

这是相当有趣的见解。好。不过，现在让我们一起想想，最初是怎么走到这一步的。回忆一下前面几页幻灯片里的 PPO 目标：我们希望最大化奖励，同时最小化得到的 policy 与 reference policy 之间的距离，也就是在最大化奖励和 KL divergence 项之间做权衡。

### [1:35:39](https://www.youtube.com/watch?v=PmW_TMQ3l0I&t=5739s) · b000194

**English**

And then you have this beta coefficient that appears there that controls how much you want to penalize going further from the base model. And what this paper did is that it wrote down this formula and then solves what would be the optimal solution. So it expressed the optimal policy pi star. And when you derive this expression, so you get it as a function of R.

**中文**

那里还有一个 beta 系数，用来控制你想对偏离 base model 更远的行为施加多大惩罚。这篇论文做的，就是写下这个公式，然后求解最优解是什么。因此，它表达出了最优 policy，pi star。当你推导这个表达式时，会得到一个关于 R 的函数。

### [1:36:11](https://www.youtube.com/watch?v=PmW_TMQ3l0I&t=5771s) · b000195

**English**

So that's another term that was in the objective function. And so all these steps have no extra assumptions. It's just a bunch of derivations that was done. And what you can see here is this Z term that stands for a partition function and that just normalizes things. But it's not something that is new. It's a function of the terms that were already in there.

**中文**

那是 objective function 中的另一个项。所有这些步骤都没有额外假设，只是进行了一系列推导。你在这里看到的 Z 项代表配分函数（partition function），只是用来做归一化。但它不是什么新东西，而是原本就存在的那些项的函数。

### [1:36:44](https://www.youtube.com/watch?v=PmW_TMQ3l0I&t=5804s) · b000196

**English**

So when you rearrange these terms, you can equivalently express r as a function of this pi star. So it's just rearranging terms between these two expressions. Nothing too fancy. And then the key part of what this paper did is recognize this term as some reward and then express it as part of a Bradley-Terry formulation.

**中文**

当你重新整理这些项时，就可以等价地把 r 表达为这个 pi star 的函数。只是对这两个表达式中的项进行重新整理，没有什么特别复杂的。然后，这篇论文所做的关键一步，是把这一项识别为某种奖励，再将其作为 Bradley-Terry 公式的一部分表达出来。

### [1:37:20](https://www.youtube.com/watch?v=PmW_TMQ3l0I&t=5840s) · b000197

**English**

So you remember you had this probability of a completion, of a winning completion being bigger than a losing completion. And you had this sigmoid of the difference between the two r's. So basically, they took this formulation again, and they plugged in the expression they had obtained for the optimal reward, which we had seen was a function of the policy. So at the end of it, you plug in things.

**中文**

你还记得，有一个 completion，一个胜出 completion 大于一个落败 completion 的概率。然后，是这两个 r 之差的 sigmoid。基本上，他们再次使用了这个公式，并代入了之前得到的最优奖励表达式，我们已经看到它是 policy 的函数。所以，到最后，你把这些东西代进去。

### [1:37:50](https://www.youtube.com/watch?v=PmW_TMQ3l0I&t=5870s) · b000198

**English**

You have no more rewards, just a function of the other parameters. So you have this beta and only the policy in there. And the last step is the same one as Afshin was mentioning, once you have this probability that you want to maximize, you can turn it into a loss function. And this loss function is what this paper proposes to optimize in order to tune policy weights in order to align it with this preference data.

**中文**

就不再有奖励了，只剩下其他参数的函数。里面有这个 beta，还有 policy。最后一步和 Afshin 提到的一样，一旦有了想要最大化的概率，就可以把它转换成 loss function。这篇论文提出优化的就是这个 loss function，以调整 policy 的权重，使它与这些 preference data 对齐。

### [1:38:26](https://www.youtube.com/watch?v=PmW_TMQ3l0I&t=5906s) · b000199

**English**

So I simplified a lot the quite heavy steps of this paper into these few steps. Do they make sense?

**中文**

我把这篇论文中相当繁重的步骤大幅简化成了这几个步骤。大家理解吗？

### [1:38:42](https://www.youtube.com/watch?v=PmW_TMQ3l0I&t=5922s) · b000200

**English**

And the beta that we see here is the same beta as we had seen in the PPO formulation, so typically taken around 0.1 if you want some order of magnitude. So beta is a hyper-parameter, and all you want to optimize for is the policy. And then the preference pairs, you have them as inputs. Makes sense? OK. Great. So now, let's compare what this method gives with respect to RLHF.

**中文**

这里看到的 beta，就是之前在 PPO 公式中看到的同一个 beta。如果你想知道大概的数量级，通常取 0.1 左右。所以，beta 是一个超参数，你要优化的只有 policy。preference pairs 则作为输入给定。明白吗？好。很好。现在，我们来比较一下这个方法相对于基于人类反馈的强化学习（RLHF）能带来什么。

### [1:39:14](https://www.youtube.com/watch?v=PmW_TMQ3l0I&t=5954s) · b000201

**English**

So RLHF is this two-stage training process where you first fit a reward function and then use it in order to do the policy update steps. So Afshin was mentioning it, it's quite heavy. We were mentioning it just before, you need a lot of models in memory and then training stability is a concern. You don't have direct supervision. You rely on the policy of the current model to generate the next updates.

**中文**

RLHF 是一个两阶段训练过程：先拟合奖励函数，然后用它来进行 policy 更新。Afshin 提到过，它相当繁重。我们刚才也说了，你需要在内存中放很多模型，训练稳定性也是个问题。你没有直接监督，而是依靠当前模型的 policy 来生成后续更新所需的内容。

### [1:39:47](https://www.youtube.com/watch?v=PmW_TMQ3l0I&t=5987s) · b000202

**English**

So there is a lot of complexity in it. And as opposed to that, this DPO formulation gives a supervised way to think about preference tuning, where you just take this preference pairs, and you directly fit a loss function on them. And yeah. And instead of four models, you just need two because you had this pi of theta and then a pi ref, which was your base SFT model, and you don't need any other model copies.

**中文**

所以，它很复杂。相比之下，这个 DPO 公式提供了一种从监督学习角度理解偏好调优（preference tuning）的方式：你只需取这些 preference pairs，直接在它们上面拟合一个 loss function。对。而且，你只需要两个模型，而不是四个，因为有这个 pi of theta，还有一个 pi ref，也就是你的基础 SFT 模型，不需要任何其他模型副本。

### [1:40:21](https://www.youtube.com/watch?v=PmW_TMQ3l0I&t=6021s) · b000203

**English**

So now, you might want to ask if it's much easier, why is not everyone just simply using DPO? So it's not as easy. In practice, there are some pros and cons to each method, and the paper that is listed below gives a very interesting study of the bench-marking differences and the steps to get there. So just to get the main lines, overall, PPO performs better than DPO.

**中文**

现在，你可能想问，既然容易这么多，为什么不是所有人都直接用 DPO？事情没那么简单。在实践中，每种方法都有优缺点，下面列出的论文对基准测试（benchmarking）的差异以及达到这些结果的步骤进行了非常有意思的研究。只看主要结论的话，总体上，PPO 的表现优于 DPO。

### [1:40:58](https://www.youtube.com/watch?v=PmW_TMQ3l0I&t=6058s) · b000204

**English**

And one great thing about DPO, which is the supervision, the direct supervision, comes at the cost of sometimes fitting something that is not the exact distribution that the model has seen as training time. So this paper talks about it a bit. If you train via SFT on the preference related data, you could get better performance. But this shift in distribution is a challenge intrinsic to DPO, because one thing that the DPO method enables you to have is just to not worry about that reward modeling at all and just get some preference data set out there.

**中文**

DPO 的一个很大优点，也就是监督、直接监督，是有代价的：有时拟合的分布，并不完全是模型在训练时见过的分布。这篇论文对此有一些讨论。如果你在偏好相关数据上进行 SFT 训练，就可能获得更好的表现。但这种分布偏移（distribution shift）是 DPO 固有的挑战，因为 DPO 方法让你能够完全不必操心奖励建模（reward modeling），只要从外部找一个偏好数据集就行。

### [1:41:46](https://www.youtube.com/watch?v=PmW_TMQ3l0I&t=6106s) · b000205

**English**

But the issue with doing so is exactly that distribution shift. So you could either train SFT on it or donate it yourself and then rate it. But that is yet another cost that you would need to pay.

**中文**

但这么做的问题，恰恰就是这个 distribution shift。所以，你可以在这些数据上做 SFT，也可以自己 donate it \[字幕疑误，可能指 generate it，即生成这些数据\]，然后再评分。但这又是你需要付出的另一项成本。

### [1:42:05](https://www.youtube.com/watch?v=PmW_TMQ3l0I&t=6125s) · b000206

**English**

Great.

**中文**

很好。

### [1:42:08](https://www.youtube.com/watch?v=PmW_TMQ3l0I&t=6128s) · b000207

**English**

And yep. Any questions?

**中文**

对。有什么问题吗？

### [1:42:14](https://www.youtube.com/watch?v=PmW_TMQ3l0I&t=6134s) · b000208

**English**

Yep. \[AUDIO OUT\] So the question is you are optimizing the parameters with respect to the base model. So yes, but it's not the base model. It's the current one. You have a base model that will stay fixed in the iterations. And it occurs in the loss function. And you're indeed updating parameters. And that will be like the preference tuned one. Yeah. So you have two weights, two set of weights, one frozen, one that you update.

**中文**

对。\[音频缺失\] 问题是，你是在相对于 base model 优化参数。是的，但优化的不是 base model，而是当前模型。你有一个在迭代过程中保持固定的 base model，它出现在 loss function 中。你确实在更新参数，而更新后的那个就会是经过 preference tuning 的模型。对。所以，你有两套权重，两组权重，一组冻结，一组进行更新。

### [1:42:45](https://www.youtube.com/watch?v=PmW_TMQ3l0I&t=6165s) · b000209

**English**

Yeah. OK. Great. Any other questions? \[AUDIO OUT\]

**中文**

对。好。很好。还有其他问题吗？\[音频缺失\]

### [1:42:58](https://www.youtube.com/watch?v=PmW_TMQ3l0I&t=6178s) · b000210

**English**

Yes. So the question is instead of the reference model, could you use another model, another large model? So I think that's an interesting point. I guess that would be a different algorithm. And you might lose a bit the meaning of what you're trying to do because this preference tuning stage is trying to align your responses to what you prefer. And you want them to align with respect to what you had learned so far.

**中文**

是的。问题是，能不能不用 reference model，而用另一个模型，另一个大型模型？我觉得这是个有意思的想法。我想，那会是一种不同的算法。而且，你可能会稍微失去你想做这件事的意义，因为 preference tuning 阶段，是要让回答与你偏好的内容对齐。你也希望这种对齐是相对于目前已经学到的内容来进行的。

### [1:43:30](https://www.youtube.com/watch?v=PmW_TMQ3l0I&t=6210s) · b000211

**English**

So if you start from a different model, and then you preference tune a different probability distribution, you might be doing things that might not make as much sense from a loss standpoint. But I guess the direction--I mean, I cannot tell a blanket answer there. Maybe it could give interesting behavior, but my intuition would tell you that the point of all of this is to start from the last train checkpoint that you had and then further preference tune the distribution of your completions.

**中文**

所以，如果从另一个模型出发，再对另一个概率分布进行 preference tuning，从 loss 的角度来看，你做的事情可能不那么有意义。不过，我想这个方向——我的意思是，我没法给出一个一概而论的答案。也许它会产生有意思的行为，但我的直觉是，这一切的意义在于从最近一次训练的检查点（checkpoint）出发，进一步对 completion 的分布进行 preference tuning。

### [1:44:12](https://www.youtube.com/watch?v=PmW_TMQ3l0I&t=6252s) · b000212

**English**

So the suggestion was if you change the reference model, that could be seen as another SFT version of your model. Yeah. I guess so.

**中文**

所以，刚才的建议是，如果更换 reference model，可以把它看作模型的另一个 SFT 版本。对。我想是这样。

### [1:44:25](https://www.youtube.com/watch?v=PmW_TMQ3l0I&t=6265s) · b000213

**English**

Great. And now, my favorite part of today. So do you all remember the completions we had obtained on our favorite prompts? So can I put my teddy bear in the washer? So if you remember last episode, we had said after instruction tuning, the response was, no, it might get damaged. Try hand washing it instead. So does anyone have any complaints regarding this answer?

**中文**

很好。现在到了我今天最喜欢的部分。大家还记得我们在那些最喜欢的 prompt 上得到的 completion 吗？比如，我能把泰迪熊放进洗衣机吗？如果你还记得上一讲，我们说过，在指令微调（instruction tuning）之后，回答是：不行，它可能会损坏。试着改用手洗吧。那么，有人对这个回答有什么不满吗？

### [1:44:59](https://www.youtube.com/watch?v=PmW_TMQ3l0I&t=6299s) · b000214

**English**

So I can give a hint. Teddy bears, they indeed should be hand washed. So it's factually correct.

**中文**

我可以给个提示。泰迪熊确实应该手洗。所以，它在事实上是正确的。

### [1:45:07](https://www.youtube.com/watch?v=PmW_TMQ3l0I&t=6307s) · b000215

**English**

But let's suppose it's factually correct. What else do you not like? I mean, could you not like about this answer?

**中文**

但我们先假设它在事实上是正确的。你还不喜欢什么？我的意思是，这个回答还有什么可能让你不喜欢的地方？

### [1:45:21](https://www.youtube.com/watch?v=PmW_TMQ3l0I&t=6321s) · b000216

**English**

Yeah. So the suggestion was it's asking to try it instead. And I guess a broader point is it's a bit too rough. It doesn't sound super friendly. And then someone who asks this question might love teddy bears, so you might want to tell them about it in a gentle way. And this is exactly what preference tuning stage is about. We don't want to learn new facts. We want to focus on existing distribution of completions and align what the model should return with respect to what the human prefers.

**中文**

对。刚才的意见是，它让你试着改用另一种方式。我想，更广泛的一点是，它有些太生硬了，听起来不太友好。而问这个问题的人可能很喜欢泰迪熊，所以你可能希望用温和的方式告诉对方。这正是 preference tuning 阶段要做的事情。我们不是想学习新事实，而是想关注已有的 completion 分布，让模型应该返回的内容与人类偏好对齐。

### [1:45:58](https://www.youtube.com/watch?v=PmW_TMQ3l0I&t=6358s) · b000217

**English**

So on this intuition, the preference tunes answer could be a gentler one. It's better not to. Your teddy bear could get hurt. A gentle hand wash is safer, so it's conveying the same points but in a tone that sounds much better to the ears of the person who asks. Great. Any questions on the DPO part?

**中文**

基于这个直觉，经过 preference tuning 的回答可以更温柔一些：最好不要。你的泰迪熊可能会受伤。轻柔地手洗更安全。所以，它传达的是相同的要点，但语气在提问者听来要好得多。很好。关于 DPO 部分，有什么问题吗？

### [1:46:29](https://www.youtube.com/watch?v=PmW_TMQ3l0I&t=6389s) · b000218

**English**

Yeah. \[AUDIO OUT\]

**中文**

对。\[音频缺失\]

### [1:46:41](https://www.youtube.com/watch?v=PmW_TMQ3l0I&t=6401s) · b000219

**English**

The question is, what are the trade offs and then which one is used in practice? So I think it all depends on your compute budget, on how much you want to worry about performance versus babysitting your training process. PPO, like the RL part, is very hard to tune right. It will give the highest results, but you might get almost at that level with much less efforts. So I guess if you want to get a quick preference tuning that is shown to show good results, but maybe not the best results, then DPO is your friend.

**中文**

问题是，有哪些权衡，以及实践中使用哪一种？我认为，这完全取决于你的计算预算，以及你有多在意性能，又愿意花多少精力照看训练过程。PPO，也就是 RL 那部分，很难调好。它会给出最好的结果，但你可能花少得多的精力，就能接近那个水平。所以，我想，如果你希望快速做一次 preference tuning，已经证明能得到不错的结果，但未必是最好的结果，那么 DPO 就是你的好帮手。

### [1:47:19](https://www.youtube.com/watch?v=PmW_TMQ3l0I&t=6439s) · b000220

**English**

And if you're an expert at reinforcement learning, you know what you're doing and you want the every last bit of performance, then PPO might be a better way.

**中文**

如果你是强化学习专家，知道自己在做什么，而且想榨取每一分性能，那么 PPO 可能是更好的方法。

### [1:47:32](https://www.youtube.com/watch?v=PmW_TMQ3l0I&t=6452s) · b000221

**English**

Amazing. And with that, thank you very much.

**中文**

太好了。那么，非常感谢大家。
