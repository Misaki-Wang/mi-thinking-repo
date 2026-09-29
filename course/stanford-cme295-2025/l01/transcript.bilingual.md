# Stanford CME295 Transformers &amp; LLMs \| Autumn 2025 \| Lecture 1 - Transformer

_Bilingual transcript · 双语讲稿_

- Channel: Stanford Online
- Source: [YouTube](https://www.youtube.com/watch?v=Ub3GoFaUcds)
- Duration: 1:41:59
- Caption source: manual
- Status: complete
- Chinese translation: 208/208
- Translation provider: codex
- Generated: 2026-09-29T15:38:06+00:00

## Transcript · 讲稿

### [00:05](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=5s) · b000001

**English**

Cool. Hello everyone, and welcome to CME 295--Transformers and Large Language Models. So my name is Afshine. And I will be teaching this class with Shervine, who's in the back. And before I start, I'm just going to introduce ourselves. So we're twin brothers, and we actually had a similar background. So we both went to a school in France called Centrale Paris, and then we each went our way.

**中文**

好。大家好，欢迎来到 CME 295——Transformers 与大语言模型（Large Language Models）。我叫 Afshine。我会和在后面的 Shervine 一起教授这门课。开始之前，先介绍一下我们自己。我们是双胞胎兄弟，背景也很相似。我们都就读于法国一所叫 Centrale Paris 的学校，之后各自走上了不同的道路。

### [00:37](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=37s) · b000002

**English**

So on my end, I went to MIT, and then Shervine went to Stanford to do the ICME Master's program. And after that, I guess our industry background is very similar as well. So I first went to Uber, and then Shervine came to Uber as well, and then Shervine left to Google, and I went to Google. And then very recently, I joined Netflix, and Shervine joined Netflix as well. And we've been working on Large Language Models.

**中文**

我这边去了 MIT，Shervine 则去了 Stanford，攻读 ICME 硕士项目。之后，我想我们的业界经历也很相似。我先去了 Uber，随后 Shervine 也来了 Uber，接着 Shervine 离开去了 Google，我也去了 Google。最近，我加入了 Netflix，Shervine 也加入了 Netflix。我们一直在从事大语言模型方面的工作。

### [01:07](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=67s) · b000003

**English**

So yeah, I guess we have technical backgrounds, and mostly oriented towards LLMs. OK, so why are we doing this class? So since 2020, Shervine and I have been specializing in NLP. And we've been giving this class in the format of a workshop that was done on a yearly basis. So in 2021, 2022, 2023, 2024, ChatGPT came in 2022, and suddenly there was a lot of interest for LLMs.

**中文**

所以，是的，我想我们都有技术背景，主要面向大语言模型（LLMs）。好，那我们为什么要开这门课呢？从 2020 年起，Shervine 和我一直专注于自然语言处理（Natural Language Processing，NLP）。我们一直以每年一次的工作坊形式讲授这门课。也就是 2021、2022、2023、2024 年。ChatGPT 在 2022 年出现，突然之间，大家对 LLMs 产生了很大的兴趣。

### [01:40](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=100s) · b000004

**English**

And so it's actually last spring that we started to offer this class as a Stanford course that is now called CME 295, and this is the second instance.

**中文**

所以，实际上是在去年春天，我们开始把这门课作为 Stanford 的正式课程开设，现在叫 CME 295，这是第二次开课。

### [01:55](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=115s) · b000005

**English**

Cool. So what can you expect from this class? So first of all, LLMs are basically everywhere now. And I guess our goal here is twofold. So the first one is to learn about the underlying mechanism that makes all this work. And we're going to see the transformer, which is the foundational architecture that makes all this work. And then the second thing is to know how these LLMs are trained and where they are applied.

**中文**

好。那你们可以期待从这门课中学到什么？首先，LLMs 现在基本上无处不在。我想我们这里有两个目标。第一个是了解让这一切运转起来的底层机制。我们会学习 Transformer，它是让这一切成为可能的基础架构。第二个是了解这些 LLMs 如何训练，以及应用在哪里。

### [02:31](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=151s) · b000006

**English**

So in case you're still wondering if this class is good for you, I would say that this class is great for people who just in general have an interest in this field, either because you wanted to make it your career goal, if you want to be a research scientist or an ML scientist, or if you want to develop a personal project that relies on LLMs to some extent, to just knowing the caveats, I guess what works, what doesn't, or just say if you're in a separate field and you just want to know how this whole AI, GenAI, LLMs thing works and how you can apply it to your domain.

**中文**

所以，如果你还在考虑这门课是否适合你，我会说，它很适合一般来说对这个领域感兴趣的人：无论是因为你想把它作为职业目标，想成为研究科学家或机器学习科学家（ML scientist）；还是想开发一个在某种程度上依赖 LLMs 的个人项目，想了解一些注意事项，我想，也就是哪些方法有效、哪些无效；又或者你来自其他领域，只想知道人工智能（AI）、生成式人工智能（GenAI）、LLMs 这一整套东西是如何运作的，以及如何把它应用到自己的领域。

### [03:14](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=194s) · b000007

**English**

So now in terms of prerequisites, I would say that at a very minimum you should have some foundations in ML, like basically know how a model is trained, what a neural network is, and also some basics in linear algebra, so basically how matrices are multiplied, for instance. But even if you have a developing, I guess, competency in this field, I guess it's fine, we're still be here to help you out.

**中文**

那么，关于先修要求，我会说，最起码你应该具备一些机器学习（ML）基础，比如基本了解模型如何训练、什么是神经网络（neural network），还有一些线性代数基础，比如矩阵是如何相乘的。不过，即使你在这个领域的能力还在培养中，我想也没关系，我们仍然会在这里帮助你。

### [03:48](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=228s) · b000008

**English**

But I guess this is like the ideal set of prerequisites.

**中文**

不过，我想这些就是比较理想的先修要求。

### [03:54](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=234s) · b000009

**English**

Cool. So still on the logistics, so this class will be held every Friday from 3:30 to 5:20, and it will be held here.

**中文**

好。继续说课程安排，这门课每周五 3:30 到 5:20 上课，地点就在这里。

### [04:08](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=248s) · b000010

**English**

So this class is two units. And you have the choice to either take it as a letter or a credit/non-credit. So as you could tell from the setup, we're basically recording this class. And if you cannot for some reason attend this time, this slot, we'll make sure with Shervine to make the recordings available, either tonight, like every Friday night, or on Saturday. So in terms of the grades, so what we're doing for this quarter is to have two exams.

**中文**

这门课是两个学分。你可以选择字母评分制（letter grade），或者学分／无学分制（credit/non-credit）。从这里的设备布置，你们也能看出来，我们正在录制这门课。如果你因为某种原因无法在这个时间段来上课，Shervine 和我会确保在今晚，也就是每周五晚上，或者周六提供录像。关于成绩，这个学季我们会安排两次考试。

### [04:47](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=287s) · b000011

**English**

So one is the midterm, which will be happening during our fifth instance, which is October 24. And then the second exam will be the final exam, which will be held in the week of December 8. So date is still TBD. So we'll let you know. Cool. So every time we have a lecture, we'll be posting the slides and the recordings on the website.

**中文**

一次是期中考试，会在第五次课时进行，也就是 10 月 24 日。第二次是期末考试，会在 12 月 8 日那一周举行。具体日期仍待定（TBD），之后会通知大家。好。每次讲课后，我们都会把幻灯片和录像发布到网站上。

### [05:21](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=321s) · b000012

**English**

And in case you're interested, we also have the syllabus in there, so you can know a little bit what are the topics that we'll be talking about. And the class textbook is this Super Study Guide--Transformer LLMs. So we have a copy here in case you want to take a look. So yeah, I guess a lot of the concepts that we have in this class will actually be in the book. So I guess it's a helpful way to follow this as well. And also, we did some very short, condensed version of this whole class that we called the VIP cheat sheet.

**中文**

如果你感兴趣，我们也把教学大纲放在那里了，这样你就能大致了解我们会讲哪些主题。课程教材是这本 Super Study Guide--Transformer LLMs。这里有一本，想看的话可以翻一翻。是的，我想这门课里的很多概念实际上都在书里。所以，我想它也是辅助跟上课程的一个好办法。另外，我们还为整门课制作了一个非常简短、浓缩的版本，叫 VIP cheat sheet。

### [05:58](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=358s) · b000013

**English**

So this one is available on GitHub in case you're interested. And yeah, we also translated it into a number of languages now. By the way, if your language is not there, let us know, and happy to work on that as well together. OK, cool. I think it's the last things on the logistics part. So in terms of announcements, we'll be posting things on Canvas. In case you have any questions, you can of course reach out to us. But there is also a tab on Canvas that's called Ed.

**中文**

如果你感兴趣，这份资料可以在 GitHub 上找到。而且，我们现在已经把它翻译成了多种语言。顺便说一下，如果里面没有你的语言，请告诉我们，我们也很乐意一起合作完成。好。我想课程安排部分就剩最后这些了。关于公告，我们会在 Canvas 上发布。如果有任何问题，当然可以联系我们。不过，Canvas 上还有一个叫 Ed 的标签页。

### [06:32](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=392s) · b000014

**English**

I'm sure you're familiar. So you just click on that, just post your question, and then Shervine and I will be responding. And I guess to reach out to us, you have this mailing list. Or we're just two, so just ding us. Cool. So on the logistics, do we have any questions so far? And one thing I forgot to mention is that, given that we're recording this class, I guess if you're asking a question, it may not be super clear for the viewer what your question was.

**中文**

相信你们都很熟悉。点击它，发布你的问题，然后 Shervine 和我会回复。要联系我们的话，这里有一个邮件列表。或者，我们就两个人，直接给我们发消息就行。好。关于课程安排，目前有什么问题吗？还有一件事忘了说，因为我们在录制这门课，如果你提问，观看录像的人可能不太能听清你的问题。

### [07:08](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=428s) · b000015

**English**

So I'm going to make an effort to just repeat your question. It will sound weird, but I'll try to not forget, but yeah. So any questions so far on the logistics? Yeah.

**中文**

所以，我会尽量重复一下你的问题。听起来可能有点奇怪，不过我会尽量记得这样做，就是这样。那么，目前关于课程安排有什么问题吗？请说。

### [07:29](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=449s) · b000016

**English**

So the question is whether there are coding parts in the exams. So the answer is no. So the exams will purely focus on concepts that we see in class. And actually, it's not meant to trap you. So I guess if you follow the class, if you see the slides and the concepts that we see, should be fine. Yeah.

**中文**

问题是考试中是否会有编程部分。答案是没有。考试只会关注我们在课堂上讲过的概念。实际上，考试不是为了为难大家。所以，我想只要你跟着课程学习，看过幻灯片和我们讲的概念，应该就没问题。请说。

### [07:53](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=473s) · b000017

**English**

Oh, yeah. Question is, if you're waitlisted, what do you do? I think, so by experience, a lot of people will finalize their schedule. Some people will drop, some won't. In case you're still waitlisted, come talk to us. But I'm pretty confident it's going to be OK, because I think the waitlist right now is six. So, I think it should be fine. Cool. Yeah.

**中文**

哦，是的。问题是，如果还在候补名单上，应该怎么办？我想，根据经验，很多人还会最终确定自己的课表。有些人会退课，有些不会。如果你仍在候补名单上，来找我们聊聊。不过，我很有信心这不会有问题，因为我想现在候补名单上有六个人。所以，我觉得应该没问题。好。请说。

### [08:19](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=499s) · b000018

**English**

They will be on the website, and we'll make sure to also post a link on Canvas. Yeah. So the question was, where are the slides. And they're on the website. Cool, yeah.

**中文**

它们会放在网站上，我们也会确保在 Canvas 上发布链接。是的，刚才的问题是幻灯片在哪里。它们在网站上。好，请说。

### [08:40](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=520s) · b000019

**English**

So question is on the weighting of the exams. So there is no homework. So 50% is midterm, 50% is final. And no grades--I mean, no weights are from that. And particular, I mean if this slot is conflicting with something, just keep in mind that we are recording this. So it's fine if you cannot attend this session. Yeah.

**中文**

问题是关于考试的权重。这门课没有作业。所以期中占 50%，期末占 50%。而且没有成绩——我是说，没有权重来自那个。另外，我是说，如果这个时段和其他事情冲突，请记住我们会录制课程。所以，如果你无法来现场上课，也没关系。请说。

### [09:06](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=546s) · b000020

**English**

Sorry?

**中文**

不好意思，你说什么？

### [09:11](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=551s) · b000021

**English**

Oh, is the question that the final is about just the second half of the class? We have not written the exam yet, but I think this is something we are thinking of. So the final is probably going to be about the second half of the topics.

**中文**

哦，你的问题是期末考试是否只涉及课程的后半部分吗？我们还没有出试卷，但我想这确实是我们正在考虑的安排。所以，期末考试大概会考后半部分的主题。

### [09:29](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=569s) · b000022

**English**

Cool. OK, long story short, 50% midterm, 50% final exam. And it's a fun class. Cool. So with that, I'm going to just slowly start the class. So another thing that I want to mention was every time we're talking about something, you will see that at the bottom of the slide there will be a source, and it's mostly for-- so first, to credits, whatever, we're quoting, but also for you to dig into those materials a bit more in case you're interested.

**中文**

好。总之，期中考试占 50%，期末考试占 50%。这是一门有趣的课。好，那接下来我就慢慢开始讲课了。还有一件事想提一下，每次我们讲某个内容时，你们都会看到幻灯片底部有一个来源。这主要是为了——首先，注明我们引用内容的出处；另外，如果你感兴趣，也方便你进一步深入阅读那些材料。

### [10:04](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=604s) · b000023

**English**

Because, of course, we have only two hours per week, and we only have nine or 10 weeks, so there's nowhere near enough time for us to cover everything. And the second disclaimer is you will see that the field is full of abbreviations. So I myself was completely scared of them when I started. But hopefully by the end of the class, you will have a mental mapping of what these abbreviations mean, respect to what they correspond to.

**中文**

因为，当然，我们每周只有两个小时，总共也只有九周或 10 周，所以时间远远不足以涵盖所有内容。第二点提醒是，你们会发现这个领域充满了缩写。我刚开始时，自己也完全被这些缩写吓到了。不过，希望到课程结束时，你们脑海里能建立起一套对应关系，知道这些缩写是什么意思、分别对应什么。

### [10:36](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=636s) · b000024

**English**

So yes, so if you have a mental mapping towards the end of the class, then we know e did a good job. So with that, let's start. And I guess we will start at a very high level, because I will just assume that I guess we're starting from scratch. And we're going to talk about NLP in general. So NLP is going to be our first abbreviation. So NLP stands for Natural Language Processing.

**中文**

所以，是的，如果到课程结束时，你们脑海里能建立起这样的对应关系，我们就知道自己做得不错了。那么，我们开始吧。我想先从非常宏观的层面讲起，因为我会假设大家是从零开始的。我们先来谈谈 NLP 的总体情况。NLP 是我们的第一个缩写。NLP 代表自然语言处理（Natural Language Processing）。

### [11:07](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=667s) · b000025

**English**

And it is a field that is around manipulating text, just computing things with text. And at a very high level, can basically classify NLP tasks into three buckets. So the first bucket is what we call classification. So we have an input text as an input. And then what we want is to predict something. So one example is you have a movie review and you want to predict whether the sentiment is positive, negative, or neutral.

**中文**

这是一个围绕文本操作展开的领域，也就是对文本进行计算。从非常宏观的层面，可以把 NLP 任务分为三类。第一类叫分类（classification）。我们以一段文本作为输入，然后想要预测某个东西。举个例子，你有一条电影评论，想预测它的情感是正面、负面还是中性。

### [11:44](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=704s) · b000026

**English**

So that's one example. You can also have intent detection, just knowing what, for instance, the person wants to do. So let's suppose you say, I want to create an alarm for tomorrow. So the intent here is create an alarm. So also to detect a language-- so for instance, if you write among French, you want to detect that text is in French, topic modeling. The second category is what we call multi-classification. So we still have a text as input, but this time we predict more than one thing.

**中文**

这是一个例子。还可以做意图检测（intent detection），也就是了解一个人想做什么。假设你说，我想为明天设置一个闹钟。那么这里的意图就是设置闹钟。还可以检测语言——例如，如果你写的是 among French \[字幕疑误，可能指用法语书写\]，你想检测出这段文本是法语，还有主题建模（topic modeling）。第二类叫多重分类（multi-classification）。输入仍然是一段文本，但这一次我们要预测不止一个东西。

### [12:21](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=741s) · b000027

**English**

So you have a number of tasks in that bucket as well. So one that is very popular is called Named Entity Recognition, a.k.a. NER. So what that task does is, given an input text, we want to basically label some specific words, like, for instance, identifying whether something is a location, or a time, and so on. And then you have some other tasks as well that are a little bit more on the linguistic side.

**中文**

这一类里也有不少任务。其中一个很常见的任务叫命名实体识别（Named Entity Recognition，NER）。这个任务是说，给定一段输入文本，我们想给一些特定的词加上标签，比如识别某个内容是否是地点、时间等等。还有一些其他任务，更偏向语言学。

### [12:53](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=773s) · b000028

**English**

I think they're less trendy now, but I guess 10 years ago it was something that people would study a lot. So part of speech tagging, which is about just figuring out which word is a noun, a verb, et cetera, or some parsing-related tasks, so dependency or constituency parsing. And then the last bucket, which is very popular these days is the generation bucket. So you have the text as input, and you also have text as output.

**中文**

我想它们现在没那么热门了，但大概 10 年前，很多人会研究这些任务。例如词性标注（part of speech tagging），也就是判断哪个词是名词、动词等等；或者一些与句法分析有关的任务，比如依存句法分析（dependency parsing）或成分句法分析（constituency parsing）。最后一类是如今很热门的生成（generation）类。输入是文本，输出也还是文本。

### [13:28](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=808s) · b000029

**English**

And here the length can be variable, meaning you don't know what the length of your output text will be beforehand. So here you have several tasks. So for instance, you have machine translation. So for instance, something in English and I wanted to let's say German. Question answering-- so typically the ChatGPT, Gemini that you're using, the assistant. So you ask a question and you have a response. And then you have other tasks as well, like summarization, you want to summarize an article, let's say, or just generate something.

**中文**

这里的长度可以变化，也就是说，你事先不知道输出文本会有多长。这一类也有几种任务。例如机器翻译（machine translation），比如有一段英语，我想把它变成德语。问答（question answering）——典型的就是你们在用的 ChatGPT、Gemini 这些助手。你提出一个问题，然后得到回答。还有其他任务，比如摘要生成（summarization），例如你想概括一篇文章，或者只是生成一些内容。

### [14:02](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=842s) · b000030

**English**

So something can be generate codes, generate a poem, can also be a lot of things.

**中文**

这些内容可以是生成代码、生成一首诗，也可以是很多其他东西。

### [14:11](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=851s) · b000031

**English**

Cool. So now what we will do is go through these tasks one by one to just illustrate what people typically handle with. So we're going to start with the first bucket, which is the classification bucket. And here we're going to illustrate this with the sentiment extraction task. So let's suppose we have a sentence, "this teddy bear is so cute." We want our model to predict this to be a positive sentiment.

**中文**

好。接下来我们会逐一看看这些任务，说明大家通常处理什么。先从第一类，也就是 classification 类开始。这里我们用情感提取（sentiment extraction）任务来说明。假设有这样一句话：“这只泰迪熊真可爱。”我们希望模型预测这表达的是正面情感。

### [14:43](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=883s) · b000032

**English**

So typically what you would use is sentiment extraction data sets. So I mentioned movie reviews, so this is IMDb critiques. But you also have reviews about products, so Amazon reviews or tweets. Now I guess it's called X, so X posts. And the way you would evaluate such outputs would be by typically using traditional classification metrics.

**中文**

通常，你会用情感提取数据集。我提到了电影评论，比如 IMDb 影评。但也有产品评论，比如 Amazon 评论，或者推文。现在我想它叫 X 了，所以是 X 帖子。评估这些输出时，通常会使用传统的分类指标（classification metrics）。

### [15:13](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=913s) · b000033

**English**

So you have accuracy, which is what is the percentage of the observations that you correctly predicted. But you also have two key metrics, which I'm just going to remind. I'm not sure if everyone knows about them. So one is precision, which is, out of all the positive predictions that you made, which ones were correct? And then the second one is recall. Out of all the true labels, how many of them did you correctly predict as being positive?

**中文**

其中有准确率（accuracy），也就是你正确预测的观测样本占多少百分比。另外还有两个关键指标，我简单提醒一下，不确定大家是否都知道。一个是精确率（precision），也就是在所有被你预测为正类的样本中，哪些预测是正确的？第二个是召回率（recall）。在所有真实标签中，有多少被你正确预测为正类？

### [15:47](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=947s) · b000034

**English**

And you have this metric called the F1 score, which basically takes the harmonic mean of precision and recall to just give you one number. So now you may wonder, why do you need all these metrics? So the short answer is that sometimes you have tasks and data sets where your classes are very imbalanced. So for instance, you can have 99% of your data set that is a positive label, and then only 1% of the data set which is negative.

**中文**

还有一个指标叫 F1 分数（F1 score），基本上就是取 precision 和 recall 的调和平均数，得到一个数字。现在你可能会问，为什么需要这些指标？简短的答案是，有些任务和数据集的类别非常不平衡。例如，数据集中 99% 都是正类标签，只有 1% 是负类。

### [16:20](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=980s) · b000035

**English**

And so here if you take a metric like accuracy, can be very misleading. Because if you have a model that would predict everything as the majority class, then you will have a great classifier, but that's not the case. So that's why precision and recall really play a role. So that's for the first one. So now let's move to the second category of NLP tasks. So this one is the multi-classification category.

**中文**

在这种情况下，如果使用 accuracy 这样的指标，就可能非常具有误导性。因为如果一个模型把所有内容都预测为多数类，你就会觉得这是一个很棒的分类器，但事实并非如此。所以 precision 和 recall 才真正发挥了作用。这是第一类。现在我们来看第二类 NLP 任务，也就是 multi-classification 类。

### [16:51](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=1011s) · b000036

**English**

So you have an input text and you predict multiple things. And we're illustrating this with the NER task, which as I mentioned is about identifying the category of given words. And so here, for instance, we want to identify a teddy bear as being an entity. I guess for that, you would use classification metrics, but not at the sentence level, but more either at the token level or at the entity-type level.

**中文**

输入一段文本，然后预测多个东西。我们用 NER 任务来说明，正如我提到的，它要识别给定词语的类别。例如这里，我们想把泰迪熊识别为一个实体。我想，对此你会使用分类指标，但不是在句子层面，而更多是在词元（token）层面或实体类型（entity type）层面。

### [17:26](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=1046s) · b000037

**English**

And by that I mean, let's suppose you have a category, let's say location. And you want to know how well you're predicting words in that category. So you would typically aggregate these metrics as a function of that. Cool.

**中文**

我的意思是，假设有一个类别，比如地点。你想知道自己对这一类词语的预测效果如何。通常，你会据此汇总这些指标。好。

### [17:47](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=1067s) · b000038

**English**

OK, let's go to the last category, which is, as I mentioned, the most popular one. So this one is text in, text out. So I'm illustrating this with the machine translation task, which is around translating a text from a source language to a target language. So here you have the example with English to French. So cute teddy bear is reading, un ours en peluche mignon lit. So for that, I guess it's harder to get data sets, because here you need to have pairs of texts.

**中文**

好，来看最后一类，正如我说过的，它也是最热门的一类。这里是文本输入、文本输出。我用机器翻译任务来说明，也就是把一段文本从源语言翻译成目标语言。这里的例子是从英语翻译成法语。所以，cute teddy bear is reading，un ours en peluche mignon lit，也就是可爱的泰迪熊正在阅读。我想，这类任务更难获取数据集，因为这里需要成对的文本。

### [18:23](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=1103s) · b000039

**English**

So you have a very popular data set that's called WMT, which stands for Workshop on Machine Translation. And that one contains a bunch of paired sequences in different languages. So for instance, you have the English-French, English-German, coming from the European Parliament data set, for instance. So to evaluate those, to evaluate the performance of your model, it's actually a lot more tricky.

**中文**

有一个很常见的数据集叫 WMT，全称是机器翻译研讨会（Workshop on Machine Translation）。里面包含大量不同语言的成对序列。例如英语—法语、英语—德语，可以来自 European Parliament 数据集等。评估这些结果，也就是评估模型的性能，实际上要棘手得多。

### [18:55](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=1135s) · b000040

**English**

Because, as you can imagine, you can have many different ways to translate something. I'm sure many of us in the room are bilingual, trilingual. So that's what is making it this hard. So in the past, people have used several rule-based metrics to do that. So one that you may have heard is BLEU. BLEU stands for Bilingual Evaluation Under Study.

**中文**

因为，你可以想象，同一个内容可以有很多不同的翻译方式。我相信在座很多人都会两种或三种语言。这就是它这么难的原因。过去，人们使用过几种基于规则的指标来评估。你们可能听过其中一个，叫 BLEU。BLEU 代表 Bilingual Evaluation Under Study \[字幕疑误，通常写作 Bilingual Evaluation Understudy\]，即双语评估替代指标。

### [19:27](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=1167s) · b000041

**English**

And it is a measure of how well your translation stands with respect to a reference text. Same story for ROUGE, which is actually a suite of metrics, but captures that in a different way. And you will see that the machine learning community is funny, because BLEU--I'm not sure if you know French-- means blue, but rouge means red. So I guess they tried to add some fun in this.

**中文**

它衡量的是，相对于参考文本，你的翻译表现如何。ROUGE 也是类似的，不过它实际上是一组指标，用不同的方式来衡量。你们会发现机器学习社区很有趣，因为 BLEU——不知道你们是否懂法语——意思是蓝色，而 rouge 意思是红色。所以，我想他们是想给这里增添一点乐趣。

### [20:00](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=1200s) · b000042

**English**

But the problem with these metrics is that you always need a reference text. So you basically need labels. And in practice, having labels is very cost expensive. It takes a lot of time, a lot of money to get labels. And we will see later in the class that with the progress that we have made in the LLM space, or that the community has made in the LLM space, we can actually forego of this reference-based metrics and go towards a more reference-free metrics.

**中文**

但这些指标的问题是，你总是需要参考文本。也就是说，你基本上需要标签（labels）。实际中，获取标签的成本非常高，需要花很多时间、很多钱。课程后面我们会看到，随着我们在 LLM 领域取得进展，或者说社区在 LLM 领域取得进展，我们实际上可以不用这些基于参考文本的指标（reference-based metrics），转向更多无需参考文本的指标（reference-free metrics）。

### [20:40](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=1240s) · b000043

**English**

And we will see that later on. And then the last metric that I will say that people sometimes use is called perplexity. And perplexity only looks at the probabilities that are output by the model. And it basically quantifies how surprised the model is by its output. So BLEU and ROUGE, the higher the better. Perplexity, the lower the better.

**中文**

我们后面会讲到这一点。最后一个我想提到的、人们有时会使用的指标，叫困惑度（perplexity）。Perplexity 只看模型输出的概率，基本上是在量化模型对其输出有多惊讶。所以 BLEU 和 ROUGE 越高越好，perplexity 越低越好。

### [21:10](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=1270s) · b000044

**English**

And I guess LLMs have been a hot topic since 2022. But actually, the field goes way back, way before that year. So in the '80s, we'll see it in a second, but there's a class of models that were actually thought of, even in the '80s. And the '90s, we had LSTMs that we'll see also in a second.

**中文**

我想，LLMs 从 2022 年起一直是热门话题。但实际上，这个领域的历史可以追溯到很久以前，远早于那一年。在 80 年代，有一类模型就已经被提出了，我们马上会看到。到了 90 年代，我们有了长短期记忆网络（Long Short-Term Memory，LSTMs），我们也很快会讲到。

### [21:41](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=1301s) · b000045

**English**

But the problem was, during that time, we didn't have the internet. We didn't have a lot of compute. And I guess this was one of the limiting factors which prevented the models from today from being trained. And then more recently, we've had several advances. So Word2vec was really one of the pioneering work in just computing meaningful embeddings. And we'll see it in a second.

**中文**

但问题在于，当时我们没有互联网，也没有很多算力。我想，这就是当时无法训练出今天这些模型的限制因素之一。再往近一些，我们取得了几项进展。Word2vec 确实是计算有意义的嵌入（embeddings）方面的先驱工作之一。我们马上会讲到它。

### [22:12](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=1332s) · b000046

**English**

And then, of course, we had the transformers, which were part of a paper that was published in 2017, which is basically at the foundation of all of the models that you see today. And then these models, they just were scaled up, both by compute, but also in terms of the data that was used to train them. And that's how LLMs were dubbed. And I guess these are more like the 2020s. But yeah, I guess we'll see those.

**中文**

接着，当然就是 Transformers，它们出自 2017 年发表的一篇论文，基本上奠定了你们今天看到的所有模型的基础。之后，这些模型的规模不断扩大，不仅算力增加了，用于训练的数据量也增加了。于是就有了 LLMs 这个称呼。我想，这更多是 2020 年代的事情。不过，是的，我们会讲到这些。

### [22:46](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=1366s) · b000047

**English**

Cool. Any questions on, I guess, the high level? Everyone good? Cool. So I guess the first question that I want to ask ourselves is, what we want to do is to have a model that handles text. But models, they understand numbers, they don't really understand text. So we need to somehow do something with that text to make it more quantifiable, something that a model can understand.

**中文**

好。关于这个宏观介绍，有什么问题吗？大家都没问题？好。那么，我想我们要问自己的第一个问题是：我们想要一个能处理文本的模型。但模型理解的是数字，它们并不真正理解文本。所以，我们需要对文本做一些处理，让它更可量化，变成模型能理解的东西。

### [23:23](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=1403s) · b000048

**English**

So if you look at a sentence, for instance, "a cute teddy bear is reading," you first need to ask yourself, how can you cut this sentence to pass it to a model? So this part is called tokenization. And what that entails is basically cutting the text with respect to some arbitrary unit of text. So there are several ways of doing this.

**中文**

例如，看这样一句话：“a cute teddy bear is reading”。首先你得问自己，怎样切分这个句子，才能把它传给模型？这个过程叫词元化（tokenization）。它基本上是按照某种任意选定的文本单位来切分文本。做这件事有几种方式。

### [23:54](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=1434s) · b000049

**English**

I guess the first way is doing it completely arbitrarily. So here, for instance, you would have "a." That would be one unit of text. "Cute" could be another unit of text. "Teddy bear" would be another one, and so on. And by the way, the unit of text is called a token, which is why the method is called tokenization.

**中文**

我想，第一种方式是完全任意地切分。例如这里，你可以有“a”，它是一个文本单位。“Cute”可以是另一个文本单位。“Teddy bear”又是一个，依此类推。顺便说一下，这种文本单位叫 token，所以这个方法才叫 tokenization。

### [24:19](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=1459s) · b000050

**English**

Another way would be to just separate by words.

**中文**

另一种方式就是按词切分。

### [24:25](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=1465s) · b000051

**English**

But I guess we would have always pros and cons. I guess one of the goals that we want to achieve is for us to then be able to represent these tokens in a meaningful way. So one con with doing this at the word level is you will end up with words that look similar, but that are actually considered as different tokens. And I guess the limitation here is you will need to compute embeddings for these similar yet different tokens and somehow make their embeddings similar.

**中文**

但我想，始终都会有优点和缺点。我们希望实现的一个目标，是之后能以有意义的方式表示这些 tokens。按词级别处理的一个缺点是，你会得到一些看起来很相似、但实际上被当作不同 tokens 的词。我想这里的局限在于，你需要为这些相似却不同的 tokens 计算 embeddings，并设法让它们的 embeddings 相似。

### [25:07](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=1507s) · b000052

**English**

So I'll give you an example. So let's suppose I have the word "bear." And then you have another word, plural form "bears." So these two words, they are very similar. Just one is singular, the other one is plural. If we go ahead with the word-level tokenization, then we will end up with just two different entities, which are basically just considered as different. Same with "run," and then "runs," variations of verbs.

**中文**

我举个例子。假设有一个词“bear”，然后还有另一个词，也就是复数形式“bears”。这两个词非常相似，只是一个是单数，另一个是复数。如果采用词级别的 tokenization，最终就会得到两个不同的实体，基本上它们只被看作是不同的。“run”和“runs”这样的动词变化也是一样。

### [25:42](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=1542s) · b000053

**English**

So for that reason, people have dug into a category of tokenizers that are called subword tokenizers, which is around leveraging roots of words in order to find what are the common roots that we can find in these words. So, for instance, for bear and bears, you would have the bear particle that would be shared.

**中文**

因此，人们深入研究了一类称为子词分词器（subword tokenizers）的工具，它们利用词根，寻找这些词里有哪些共同的词根。例如，对于 bear 和 bears，它们会共享 bear 这个部分。

### [26:12](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=1572s) · b000054

**English**

And so I guess the pro is that you get to leverage the root of the words. But then the con here is that your sequence would be longer. And we will see why this is a con. I guess later on, I guess I can give you a preview. So the complexity of these models is also a function of the sequence length. So the more tokens you have to process, the more time it will take for your model to run, because it needs to basically process all these tokens.

**中文**

所以，我想优点是你可以利用词根。但缺点是序列会变得更长。我们会看到为什么这是缺点。我想后面会讲，不过可以先透露一下。这些模型的复杂度也取决于序列长度。因此，需要处理的 tokens 越多，模型运行所需的时间就越长，因为它基本上要处理所有这些 tokens。

### [26:52](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=1612s) · b000055

**English**

So that's one con. So pro is it leverages the root of words. Con is it just makes your sequences longer.

**中文**

这是一个缺点。所以，优点是利用了词根，缺点是会使序列变长。

### [27:05](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=1625s) · b000056

**English**

You have a last category of ways of tokenizing things, which is just going at the character level, just like taking out characters. So here, I guess, you and I when we write a message, we typically have sometimes misspellings. And with the subword way of tokenizing things, you may not be able to recognize the word that has been misspelled.

**中文**

还有最后一类 tokenization 方式，就是按字符级别处理，把字符一个个拆出来。这里，我想，你我写消息时通常有时会拼错单词。而用 subword 方式进行 tokenization 时，可能无法识别这个拼错的词。

### [27:36](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=1656s) · b000057

**English**

And this is something that the character-level tokenizer can, I guess, take into consideration. But here the problem is you have a sequence length that's much, much longer, which will make your model, I guess, take much more time to process the sequence. So that's one con. And then the other con is, I guess, when you want to represent each of these tokens, I guess it's very hard to know that a representation of a letter really means.

**中文**

我想，字符级分词器（character-level tokenizer）可以考虑到这种情况。但这里的问题是，序列长度会长得多得多，使模型处理序列花费更多时间。这是一个缺点。另一个缺点是，当你想表示每一个 token 时，我想，很难知道一个字母的表示究竟意味着什么。

### [28:08](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=1688s) · b000058

**English**

Like, what does the representation of the letter U mean. It's very hard. OK, cool. So I have just a quick recap. So word-level is a super naive way, super simple way of, I guess, dividing your text into arbitrary units. But then the problem is, as we mentioned, we do not leverage the root of words. And I did not mention this, but there is a term.

**中文**

例如，字母 U 的表示意味着什么？这很难。好。这里快速回顾一下。词级别（word-level）是一种非常朴素、非常简单的方式，把文本划分成任意单位。但问题是，正如我们说过的，没有利用词根。另外，我之前没提到，还有一个术语。

### [28:41](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=1721s) · b000059

**English**

Whenever you cut something and then at inference time when you want to make a prediction, I guess, one prerequisite that you have is that you need to have the token that you saw at training time, you need to have it in your training sets. And the problem is, let's suppose at inference time you cut your text into words. And let's suppose you have not seen a word at training time.

**中文**

每当你切分文本，之后在推理时（inference time）想要做预测，我想有一个前提：这个 token 必须是在训练时见过的，你的训练集里必须有它。问题是，假设在 inference time，你把文本切成词，然后假设其中有一个词是训练时没见过的。

### [29:12](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=1752s) · b000060

**English**

You will need to mark it as unknown. And so this thing is called OOV, Out Of Vocabulary. So luckily, the subword-level tokenizer mitigates that problem. So you have a lower risk of OOV, but still you can have. And as we mentioned, in terms of the pro, you leverage the roots of the words.

**中文**

你就需要把它标记为未知。这种情况叫词表外（Out Of Vocabulary，OOV）。幸运的是，subword-level tokenizer 可以缓解这个问题。OOV 的风险会更低，但仍然可能出现。正如我们提到的，它的优点是利用了词根。

### [29:41](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=1781s) · b000061

**English**

And then character-level, it's robust to our misspellings and our casing errors. But the problem is it makes computations just much slower. And your sequences would be very, very long, which will also make your, I guess, inference time much higher. That sound good? I guess this is really the foundation, I guess, how to handle things with text. But yeah, does that make sense overall?

**中文**

然后是字符级别（character-level），它对拼写错误和大小写错误具有鲁棒性（robustness）。但问题是，它会让计算慢得多。序列会变得非常、非常长，这也会让推理耗时高很多。这样可以吗？我想，这确实是基础，也就是如何处理文本。不过，是的，总体上能理解吗？

### [30:13](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=1813s) · b000062

**English**

Cool. OK, so now what we did is we took an input text. What we did is we cut it into parts that are basically tokens. So in order for our model to understand these tokens, we need to find a representation for each of them. So here, we're going to take a look at this. So that's called a word representation. Or I guess, in a more correct way, it should be token representation.

**中文**

好。现在，我们取了一段输入文本，把它切分成了若干部分，也就是 tokens。为了让模型理解这些 tokens，我们需要为每一个 token 找到一种表示。接下来我们看看这个。这叫词表示（word representation）。或者，更准确地说，应该叫词元表示（token representation）。

### [30:45](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=1845s) · b000063

**English**

So we want to find a way to represent each of these tokens.

**中文**

所以，我们想找到一种方式来表示每一个 token。

### [30:52](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=1852s) · b000064

**English**

So the simple and naive way to do this would be to just assign the one hot vector for each word or for each token. So for instance, let's suppose we have a vocabulary of three tokens--book, soft, and teddy bears. We would have, let's say, soft. That is 1, 0, 0 vector. Teddy bear, that is, let's say a 0, 1, 0 vector. And book, that is, let's say, a 0, 0, 1 vector.

**中文**

一个简单、朴素的做法，是为每个词或每个 token 分配一个独热向量（one-hot vector）。例如，假设词表里有三个 tokens——book、soft 和 teddy bears。比如说，soft 对应向量 1, 0, 0；Teddy bear 对应向量 0, 1, 0；book 对应向量 0, 0, 1。

### [31:25](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=1885s) · b000065

**English**

So this is called a One-Hot Encoding, OHE. We'll typically see. So cool. This is a way to represent our tokens. But basically what people want to do is compare these tokens to basically see which ones are more similar to what other ones. So common similarity measure that people use is something called cosine similarity.

**中文**

这叫独热编码（One-Hot Encoding，OHE），我们经常会看到。好，这是一种表示 tokens 的方法。但人们基本上想做的是比较这些 tokens，看看哪些与哪些更相似。人们常用的一种相似度度量叫余弦相似度（cosine similarity）。

### [31:56](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=1916s) · b000066

**English**

I'm not sure if you have heard of it. So you can think of it as just seeing what angle these vectors make in the n dimensional space. And if, I guess, they are pointing in the same direction, then maybe they're similar. Maybe if they're orthogonal, maybe they're independent. And if they're completely opposite, then maybe they're opposite. That's basically the mental model we want to go into.

**中文**

不知道你们是否听说过。可以把它理解为看这些向量在 n 维空间里形成什么夹角。如果它们指向同一个方向，那么它们可能相似。如果它们正交，可能就彼此独立。如果它们完全相反，那么它们可能就是相反的。这基本上就是我们想采用的理解方式。

### [32:28](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=1948s) · b000067

**English**

So the problem is, if you represent your tokens in a one hot fashion, you will end up with all your vectors being orthogonal to one another. So that's the problem. So ideally, what we want is for tokens that mean the same or similar to basically have a high similarity. And for tokens that are not similar on about different thing, to be more orthogonal.

**中文**

问题在于，如果用 one-hot 的方式表示 tokens，最终所有向量都会彼此正交。这就是问题所在。理想情况下，我们希望含义相同或相似的 tokens 具有较高的相似度；而不相似、谈论不同事物的 tokens，则更接近正交。

### [33:03](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=1983s) · b000068

**English**

So here, just for illustrative purposes, teddy bears are soft. So you want teddy bear and soft to be, I guess, with a high similarity. And let's say teddy bear and book, which is independent, you want them to be closer to 0. So that's what you want. That's what you have with one-hot encoding, and that's what you want. Yeah.

**中文**

这里只是为了举例，泰迪熊是柔软的。所以，你希望 teddy bear 和 soft 有较高的相似度。假设 teddy bear 和 book 彼此独立，那么你希望它们的相似度更接近 0。这就是你想要的。这是使用 one-hot encoding 得到的结果，而这是你想要的结果。请说。

### [33:31](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=2011s) · b000069

**English**

Sorry?

**中文**

不好意思，你说什么？

### [33:38](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=2018s) · b000070

**English**

Oh, I see. The question is, why do you care about the norm? So I guess cosine similarity is actually normalized by norms. So it's dot products. Oh, you mean why did I just put dot product here instead of 2?

**中文**

哦，明白了。问题是，为什么要关心范数（norm）？我想，cosine similarity 实际上是用 norms 做了归一化的。所以它是点积（dot product）。哦，你是说，为什么我这里只写了 dot product，而不是 2？

### [34:01](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=2041s) · b000071

**English**

Oh, I see. And your question is, why do we not care about the norm? Cool, I guess the viewers know the question. I guess these measures, they are all measures. They are all ways to try to capture these similarity things. So I guess why do you not care about the norm?

**中文**

哦，明白了。你的问题是，为什么我们不关心 norm？好，我想观众现在知道问题了。我想，这些度量都是度量，都是试图刻画相似性的方式。所以，为什么不关心 norm 呢？

### [34:25](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=2065s) · b000072

**English**

I guess it's how people have tried to quantify that. I guess you will need to see how your vectors are trained and whether the norm would be indicative of something. I guess the best answer I can give you is, I guess, this is a measure. This is not the perfect measure. People may use also dot product as a measure, but yeah, I don't have a great answer for you. But as long as you capture, I guess, how these vectors they're pointing, I guess, typically what you care about is the angle between them.

**中文**

我想，这是人们尝试量化相似性的一种方式。你需要看向量是如何训练的，以及 norm 是否能反映什么信息。我想，我能给出的最好答案是，这是一种度量，并不是完美的度量。人们也可能把 dot product 用作度量。不过，是的，我没有一个特别好的答案。但只要能捕捉到这些向量指向什么方向，我想，通常你关心的就是它们之间的夹角。

### [35:03](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=2103s) · b000073

**English**

But typically, you don't really take into consideration the norm.

**中文**

不过，通常不会真正把 norm 考虑进去。

### [35:10](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=2110s) · b000074

**English**

Cool, any questions? Any other questions? Yeah, yeah, yeah, yeah.

**中文**

好，有什么问题吗？还有其他问题吗？请说，请说，请说，请说。

### [35:39](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=2139s) · b000075

**English**

It's a great question. So the question is around size of vocabulary and how that would inform the choice with respect to word, subword, and how that changes across languages. So great question. So I would say it really depends, first of all, on the tasks that you're trying to achieve. If your task is just about one language, you will just take that same language. You would typically go with a subword tokenizer just because of the reasons that we mentioned here. So I guess subwords is a nice trade-off between being able to identify words by their roots, like leveraging that, but also running less into the OOV risk.

**中文**

这是个很好的问题。问题是关于词表（vocabulary）的大小，以及它如何影响 word、subword 的选择，还有这种选择在不同语言中如何变化。好问题。我会说，首先这确实取决于你想完成的任务。如果任务只涉及一种语言，那就只用那种语言。通常会选择 subword tokenizer，原因就是我们刚才提到的那些。我想，subwords 是一种不错的折中：既能通过词根识别单词，利用这一点，又能减少遇到 OOV 的风险。

### [36:23](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=2183s) · b000076

**English**

So in terms of the size, I know that people have tried different things. I think typically for English, you would target something on the order of tens of thousands of vocabulary size. But nowadays, the models, they are multilingual, they are also about codes. So you will see that the vocabulary size now is sometimes on the order of hundreds of thousands. So with respect to Chinese, so I guess you have this difference in characters that you're using.

**中文**

关于大小，我知道人们尝试过不同方案。我想，一般对英语来说，目标词表大小是几万这个数量级。但如今的模型是多语言的，也涉及代码。所以你会看到，现在的词表大小有时是几十万这个数量级。说到中文，我想，你使用的字符会有所不同。

### [37:00](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=2220s) · b000077

**English**

So for Latin, I guess it's the alphabet we're all accustomed to. But of course for the other ones, you'd have something similar, but in I guess the target language character. So yeah, I would say order of magnitude, tens of thousands for one language, hundreds of thousands if it's multilingual. These are the order of magnitude that you want to target for.

**中文**

对于拉丁字母，我想，就是我们都熟悉的那套字母表。当然，其他语言也会有类似的东西，不过用的是目标语言的字符。所以，我会说，数量级上，一种语言是几万，多语言则是几十万。这些就是你要考虑的数量级。

### [37:28](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=2248s) · b000078

**English**

Cool, yeah.

**中文**

好，请说。

### [37:41](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=2261s) · b000079

**English**

Great question. So the question is, how do you get those embeddings? So it's actually the next slide. So I'm going to talk about this. Cool, great. So now that we know that the one-hot encoding is not a good way to represent tokens, what we want to do is to learn those embeddings from the data. So I mentioned that there was this paper that came out in the 2010s-- so I think it was 2013-- that was called Word2vec.

**中文**

好问题。问题是，如何得到这些 embeddings？实际上这就是下一张幻灯片的内容，我接下来会讲。好，很好。既然我们知道 one-hot encoding 不是表示 tokens 的好方法，那么我们想做的就是从数据中学习这些 embeddings。我之前提到，2010 年代有一篇论文——我想是 2013 年——叫 Word2vec。

### [38:15](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=2295s) · b000080

**English**

And the reason why it was so popular is because they showed a very intuitive and interpretable way of seeing these embeddings, because they were saying something like, OK, king is to queen, what this is to that, like Paris is to France what Berlin is to Germany. So there was basically a way to make sense of the embeddings. So now the question is, how did they do that? So they had two ways of computing these embeddings.

**中文**

它之所以这么受欢迎，是因为它们展示了一种非常直观、可解释的方式来理解这些 embeddings。他们会说，king 之于 queen，就像这个之于那个；比如 Paris 之于 France，就像 Berlin 之于 Germany。也就是说，有了一种能理解 embeddings 含义的方法。那么问题来了，他们是怎么做到的？他们有两种计算这些 embeddings 的方式。

### [38:47](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=2327s) · b000081

**English**

So one way was called continuous bag of words. The other one was called skip gram. But they all rely on the same idea, which is let's just leverage texts that we have, and then try to predict something that is part of the text, based on, let's say, the context. So for instance, continuous bag of words, the goal is you take into consideration the words that are around a given target words.

**中文**

一种叫连续词袋（continuous bag of words），另一种叫跳元模型（skip gram）。不过，它们都依赖同一个思路：利用现有文本，然后根据上下文之类的信息，预测文本中的某个部分。例如 continuous bag of words，它的目标是考虑给定目标词周围的词。

### [39:20](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=2360s) · b000082

**English**

And your goal is to predict that target word. And skip gram is the opposite. You go from a target word and you want to predict the words that are around it. So I guess this task is commonly called a proxy task. Because at the end of the day, in this exercise, what we care about is not necessarily to predict the next word, or at least not yet. Our goal is to learn a representation of these words that are meaningful.

**中文**

然后预测那个目标词。而 skip gram 正好相反，从一个目标词出发，预测它周围的词。我想，这种任务通常叫代理任务（proxy task）。因为归根结底，在这个练习中，我们关心的不一定是预测下一个词，至少暂时不是。我们的目标是学习这些词的有意义的表示。

### [39:56](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=2396s) · b000083

**English**

And so here the idea is, if you have a model that somehow knows how to predict, let's say, the next word, then it means that your model has some understanding of how language works, which is basically what you want. You basically want an embedding that is reflective of, I guess, what language is, which is king and queen, or similar, Paris and France, this is a capital.

**中文**

这里的想法是，如果一个模型以某种方式知道如何预测，比如下一个词，那么说明它对语言如何运作有一定理解，而这基本上就是我们想要的。我们想要一种能反映语言本身的 embedding，比如 king 和 queen，或者类似的，Paris 和 France，这是首都。

### [40:32](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=2432s) · b000084

**English**

You want to have these associations embedded in the representation.

**中文**

你希望这些关联被嵌入到表示当中。

### [40:39](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=2439s) · b000085

**English**

And let's go through a very simple example of what that looks like. So here in our example, let's suppose that our proxy task is about predicting the next word. So here what we take is a very vanilla neural network model, which basically receives a vector of size v, has multiplication and a bias term to get a hidden state, and then another set of multiplications to get our final vector.

**中文**

我们来看一个非常简单的例子，看看它是什么样的。在这个例子中，假设 proxy task 是预测下一个词。我们采用一个非常基础的神经网络模型（vanilla neural network model），它接收一个大小为 v 的向量，通过乘法和一个偏置项（bias term）得到隐藏状态（hidden state），然后再经过一组乘法，得到最终向量。

### [41:23](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=2483s) · b000086

**English**

So here it's basically a very simple neural network. So the input is of size v. The hidden layer is of size d, which is typically much smaller than the vocabulary. So vocabulary is typically like tens of thousands or hundreds of thousands. So d is typically hundred. Like, 768, for instance, is one example of dimension. So it's much, much smaller. So what we're trying to do is to learn the word representation through this proxy task.

**中文**

这里基本上是一个非常简单的神经网络。输入大小是 v，隐藏层（hidden layer）大小是 d，通常远小于词表大小。词表通常有几万或者几十万个词。而 d 通常是几百，比如 768 就是一个维度的例子。所以它要小得多得多。我们想做的就是通过这个 proxy task 来学习词表示。

### [41:59](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=2519s) · b000087

**English**

And what we're going to do is try to consider the words as inputs and predict the next word.

**中文**

我们会尝试把词作为输入，并预测下一个词。

### [42:12](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=2532s) · b000088

**English**

So let's go with the first word of the sequence. So by the way, I use token and words interchangeably. So let's suppose we have the word "a," and we want to predict the next word, which is the word "cute." So what we do is we take the word "a," we take the one-hot encoding representation, and we pass it through the network. So here, if you're familiar with neural networks, so here you have, I guess, a multiplication between a matrix and this vector.

**中文**

先看序列中的第一个词。顺便说一下，我会交替使用 token 和词这两个说法。假设有一个词“a”，我们想预测下一个词，也就是“cute”。做法是取出词“a”的 one-hot encoding 表示，然后把它传入网络。如果你熟悉神经网络，这里就是一个矩阵与这个向量相乘。

### [42:51](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=2571s) · b000089

**English**

So you have a hidden state representation, which is a vector of size d. So here, let's suppose it's 0.2 and 0.9, so D equal 2. And then you have, I guess, another pass here. And then you get, after softmax, a set of probabilities which are around seeing what is the next word. So in this example, we have a vocabulary of size 6.

**中文**

于是得到一个 hidden state 表示，它是大小为 d 的向量。这里假设它是 0.2 和 0.9，所以 D 等于 2。然后这里再进行一次传递。经过 softmax 后，你会得到一组概率，用来判断下一个词是什么。在这个例子中，词表大小是 6。

### [43:24](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=2604s) · b000090

**English**

So the first word is predicted with probability 0.2, second word, 0.4, and then the other words are all 0.1 in this example. So let's suppose that we want to somehow be able to maximize our prediction to be the second word of the vocabulary, which is the 0.4. So we basically compare the prediction with, I guess, 0, 1, 0, 0, 0, which is the representation of the second word of the vocabulary.

**中文**

第一个词的预测概率是 0.2，第二个词是 0.4，其他词在这个例子中都是 0.1。假设我们想设法最大化预测为词表中第二个词的概率，也就是那个 0.4。我们基本上会把预测结果与 0, 1, 0, 0, 0 进行比较，它就是词表中第二个词的表示。

### [44:01](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=2641s) · b000091

**English**

And then we do the back prop, we update the weights. I'm not sure if everyone is familiar with that part. But the idea here is, once you obtain a prediction, you compute the loss, so typically cross-entropy, which will determine how far off you are from the true answer. And based on that difference, you're going to update the weights in order to make your prediction closer to the truth.

**中文**

然后进行反向传播（back prop），更新权重（weights）。不知道大家是否都熟悉这部分。这里的思路是，得到预测后，计算损失（loss），通常使用交叉熵（cross-entropy），用来确定预测与真实答案相差多远。再根据这个差距更新 weights，使预测更接近真实值。

### [44:36](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=2676s) · b000092

**English**

So that's what you do. And then you repeat that process. Let's suppose you take the word "cute," which, as we said, is the second word in the vocabulary. So the one-hot encoding representation is 0, 1, 0, 0, 0. So you go through that network, you have a hidden state, like the vector is 0.8 and 0.4. You do that again. And what you want to do is to predict the next token, and here is teddy bear.

**中文**

这就是做法。然后重复这个过程。假设取词“cute”，正如我们说的，它是词表中的第二个词。所以它的 one-hot encoding 表示是 0, 1, 0, 0, 0。让它通过网络，得到一个 hidden state，比如向量是 0.8 和 0.4。再做一次。你想预测下一个 token，这里就是 teddy bear。

### [45:08](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=2708s) · b000093

**English**

And so you see now your model in this example is predicting the next word to be uniform, but you want to somehow maximize the probability for teddy bear. So you go about doing this again and again for all the words. And at the end of the day, you obtain a model that learns how to predict the next word, which is basically the proxy task. And what you're going to do is to take the representation that the model learns, which is the green units.

**中文**

你会看到，在这个例子中，模型目前对下一个词给出的是均匀概率，但你想设法最大化 teddy bear 的概率。于是，对所有词反复做这件事。最终，你得到一个学会了预测下一个词的模型，这基本上就是 proxy task。接下来，你要取出模型学到的表示，也就是绿色的那些单元。

### [45:43](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=2743s) · b000094

**English**

So what happens now is every time you have a word, you just represent that as a one-hot encoding representation. And you just multiply this with these weights, and then you obtain the green representation. And that is your word representation.

**中文**

这样一来，每当有一个词，你就把它表示成 one-hot encoding 形式，再与这些 weights 相乘，就能得到绿色的表示。那就是你的词表示。

### [46:09](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=2769s) · b000095

**English**

Does that make sense? Yeah, yeah.

**中文**

这样能理解吗？请说，请说。

### [46:33](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=2793s) · b000096

**English**

Yeah, great question, great question. So the question is about what does v correspond to and why there's only six. So yes, in this example we only have six possible words, which is basically the vocabulary size, just like a very toy example, because in practice there is many more. So I guess that's one of the challenges with language. So you can technically have many variations of words, which is why if you take a word-level way to divide your text into tokens, you can end up with the vocabulary that's very big, because you need to account for all the variations of given words.

**中文**

是的，好问题，好问题。问题是 v 对应什么，以及为什么这里只有六个。是的，在这个例子里只有六个可能的词，也就是词表大小。这只是一个非常简单的玩具示例，因为实际中会多得多。我想，这是语言的挑战之一。理论上，词可以有很多变化形式，所以如果按 word-level 的方式把文本划分成 tokens，词表可能会变得非常大，因为你需要考虑给定词的所有变化形式。

### [47:15](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=2835s) · b000097

**English**

And the other thing that I want to point out is, let's suppose you have a vocabulary size of 6, and it's the six words that you saw at training time. But what happens if at inference time you have a word that you have not seen at training time? And so the answer for that is typically what people do is they reserve a spot for what they call an unknown token or out-of-vocabulary token, which is basically you can think of it as a bucket for everything that we were not able to identify.

**中文**

我还想指出另一点。假设词表大小是 6，这六个词就是训练时见过的词。但如果在 inference time 出现了一个训练时没见过的词，会怎样？通常，人们的做法是预留一个位置，放所谓的未知词元（unknown token）或词表外词元（out-of-vocabulary token）。你基本上可以把它看成一个桶，用来收纳所有无法识别的东西。

### [47:55](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=2875s) · b000098

**English**

So if let's suppose at inference time you have a token that you were not able to identify, they will all take that representation, which is the unknown token representation. And this is, by the way, something that I guess the word-level tokenizer has trouble to do, because you will have a much bigger chance of having out-of-vocabulary tokens. Subword level will have a lower chance. And then character level, I guess, you don't have that problem.

**中文**

所以，假设在 inference time 有无法识别的 token，它们都会采用同一种表示，也就是 unknown token 的表示。顺便说一下，我想这也是 word-level tokenizer 的一个难点，因为它遇到 out-of-vocabulary tokens 的概率会大得多。Subword level 的概率更低。而 character level，我想就没有这个问题。

### [48:28](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=2908s) · b000099

**English**

Does that answer your question? Yeah. Cool, yeah.

**中文**

这回答你的问题了吗？是的。好，请说。

### [48:53](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=2933s) · b000100

**English**

Great, great question. So first question is, when you're done? So the thing with the proxy task is when you train your model, I guess your true objective is to not really learn--I mean, in this case--to learn how to predict the next word. Your objective is to have meaningful representations. But what you can do is to somehow track the loss function for the proxy task that you're pursuing, but then also taking into consideration that this is not necessarily your end goal.

**中文**

很好，很好的问题。第一个问题是，什么时候算完成？关于 proxy task，在训练模型时，真正的目标并不是学习——我是说，在这个例子里——如何预测下一个词。你的目标是得到有意义的表示。不过，你可以跟踪所做 proxy task 的损失函数（loss function），同时也要考虑到，这不一定是你的最终目标。

### [49:24](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=2964s) · b000101

**English**

So I guess one very reasonable way of going about doing this is just to wait until your model converges. So here, what you do is you track the loss as a function of--so there's this term "epoch," just how many times your model sees the training set. And so you compare these different curves. And when this converges, this is typically a good time to stop the training process and just see if that makes sense.

**中文**

我想，一个非常合理的做法就是等模型收敛（converge）。这里，你要跟踪 loss 随着——这里有个术语叫训练轮次（epoch），也就是模型看过训练集多少遍——的变化。然后比较这些不同的曲线。当它收敛时，通常就是停止训练过程、看看结果是否合理的一个好时机。

### [49:54](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=2994s) · b000102

**English**

Depends on your downstream task, of course. But that's one. So your second question-- sorry, can you repeat the second question? Yeah, yeah, oh, great question. So the question is, how do you know when the generation stops? I guess, otherwise it will never stop.

**中文**

当然，这取决于你的下游任务（downstream task）。这是第一个问题。那么你的第二个问题——不好意思，能重复一下第二个问题吗？是的，是的，哦，好问题。问题是，如何知道生成什么时候停止？否则，我想它就永远不会停。

### [50:26](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=3026s) · b000103

**English**

So yeah, exactly. So you have some special tokens. Typically, you have end of sequence, end of sequence. So typically when you have the end of sequence token generated, then it's when it stops.

**中文**

是的，没错。所以会有一些特殊词元（special tokens）。通常，有序列结束（end of sequence），序列结束。一般来说，当生成了 end of sequence token 时，就会停止。

### [50:40](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=3040s) · b000104

**English**

All right. So second question was what informs the size of the hidden layer? I would say it's a trade-off, because you want the embedding to be rich enough that it can be informative for your downstream task. So for instance, if you want to somehow get an embedding of, let's say, your sentence, and if you want to, let's say, do a very, very specialized task, like with a lot of different outcomes, maybe you want a vector that recaptures that, so maybe you want a bigger vector, but if you had a very simple task, maybe a smaller vector might make sense.

**中文**

好。那么第二个问题是，什么决定了 hidden layer 的大小？我会说，这是一个权衡，因为你希望 embedding 足够丰富，能够为 downstream task 提供有用信息。例如，假设你想得到句子的 embedding，并想做一个非常、非常专门的任务，可能会有很多不同的结果，那么你可能希望向量能体现这些信息，所以可能需要更大的向量。但如果任务非常简单，也许更小的向量就合理了。

### [51:22](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=3082s) · b000105

**English**

So I guess the size of your hidden dimension also impacts the complexity of whatever you're running after. Because of course, if you have longer vectors, you'll have more computation, so your inference will be probably more expensive, et cetera. So I guess there's a lot of factors. So I guess just to recap, one is how complicated your downstream task is. Second one is how sensitive are you with latency, cost, all these things.

**中文**

我想，隐藏维度（hidden dimension）的大小也会影响后续运行内容的复杂度。因为当然，向量越长，计算量就越大，推理（inference）的成本可能也会更高，等等。所以有很多因素。简单回顾一下：第一，下游任务有多复杂；第二，你对延迟（latency）、成本这些因素有多敏感。

### [51:52](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=3112s) · b000106

**English**

So it's really a trade-off. But out there you would typically see embeddings of a pool of hundreds or thousands. Of course, these models, they've been growing, so this number may change. But that's the order of magnitude that you're looking at.

**中文**

所以，这确实是一种权衡。不过，通常会看到几百或几千维的 embeddings。当然，这些模型一直在变大，所以这个数字可能会变化。但这就是你要考虑的数量级。

### [52:11](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=3131s) · b000107

**English**

Right. This is indeed empirical. Yeah, yeah. I guess you can also rely on what others found and just go from that. But 768, these numbers are things that people typically take.

**中文**

对，这确实是经验性的。是的，是的。我想，你也可以参考别人得出的结果，以此作为起点。不过，768 这样的数字是人们通常会选的。

### [52:27](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=3147s) · b000108

**English**

Cool, yeah.

**中文**

好，请说。

### [52:47](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=3167s) · b000109

**English**

Great question. So the question is, how can you distinguish words that are spelled the same but in different contexts? So you're way ahead of me. So this is basically the basics. And we're going to tackle methods that can tackle these problems of just contextualizing the word in the sentence. So yeah, so we'll see that in a bit.

**中文**

好问题。问题是，如何区分拼写相同但出现在不同上下文中的词？你已经想到我前面去了。这里讲的基本上还是基础。接下来，我们会介绍一些能够处理这些问题的方法，也就是在句子中根据上下文理解词语。是的，我们稍后会讲到。

### [53:14](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=3194s) · b000110

**English**

Cool.

**中文**

好。

### [53:17](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=3197s) · b000111

**English**

I'm not on time. So I'll try to get moving. So OK, so now what we did was see how we could learn representations of tokens. But I guess you may also want to get representations of sentences or pieces of text. So one very naive way to do that with what we saw before is to take something like the average of words, let's say, the word representations.

**中文**

我没跟上时间安排，所以接下来得加快一点。好，刚才我们看了如何学习 tokens 的表示。但你可能也想得到句子或一段文本的表示。利用我们刚才看到的内容，一个非常朴素的做法是对词，比如说词表示，取平均值。

### [53:53](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=3233s) · b000112

**English**

But the problem is you lose a lot of meaning, you lose the order, you lose--and I guess here, I think you pointed out very well, the representations that you learn are token-specific, regardless of where they're at. So that's why we have a class of models that aim at capturing the sequential nature of how text appears. So we're going to talk about RNNs, which stands for Recurrent Neural Network.

**中文**

但问题是，你会丢失很多含义，丢失顺序，丢失——而且，我想你刚才指出得很好，学到的表示是每个 token 固定对应的，不管它出现在什么位置。因此，有一类模型旨在捕捉文本呈现出来的序列特性。我们要讲循环神经网络（Recurrent Neural Network，RNNs）。

### [54:26](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=3266s) · b000113

**English**

So what RNNs do is, instead of processing words one at a time, what they do is they keep a hidden representation of the sentence so far, and they consider tokens one at a time. So as I mentioned before, this technique was actually introduced a fair amount of time ago, so in the '80s. And what this model does is it takes into consideration the order at which words appeared or tokens appeared.

**中文**

RNNs 的做法是，不再只是一次处理一个词，而是保留到目前为止句子的隐藏表示（hidden representation），并且一次考虑一个 token。正如前面提到的，这种技术其实很早就提出了，在 80 年代。这种模型会把词或 tokens 出现的顺序考虑进去。

### [55:05](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=3305s) · b000114

**English**

And so in this example, you start the, I guess, processing at the very beginning of the sentence. You have some dummy hidden states that is called A, typically denoted A or H. It's called the hidden state, activation, or even sometimes a context vector. And you have some kind of a module that takes into account the hidden state so far and the word at time step t, so here time step 1.

**中文**

在这个例子中，从句子的最开头开始处理。有一些占位的 hidden states，叫 A，通常记作 A 或 H。它被称为隐藏状态（hidden state）、激活（activation），有时也叫上下文向量（context vector）。然后，有一个模块会同时考虑到目前为止的 hidden state，以及时间步（time step）t 上的词，这里是 time step 1。

### [55:41](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=3341s) · b000115

**English**

So here what it does is it takes in the meaning of the sentence so far and takes into consideration the word that is happening now. And it produces an output vector that here can be used to try to predict the next word. So for instance here we have this hidden state and the representation of the word that then you have some matrix multiplications in this blue box.

**中文**

这里，它接收句子到目前为止的含义，并考虑当前出现的词。然后生成一个输出向量，在这里可以用来尝试预测下一个词。例如，这里有这个 hidden state 和词表示，然后在这个蓝色方框里进行一些矩阵乘法。

### [56:12](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=3372s) · b000116

**English**

And you have an output vector that you try to train on predicting the next words. And then you keep on doing that by keeping track of these hidden states. And so you repeat the process. And I guess the way you would interpret these hidden states is it's a representation of the sequence process so far.

**中文**

你会得到一个输出向量，并尝试通过预测后面的词来训练它。接着，持续跟踪这些 hidden states，继续这样做。于是不断重复这个过程。我想，可以把这些 hidden states 理解为对截至目前已处理序列的一种表示。

### [56:49](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=3409s) · b000117

**English**

So the good thing with RNNs is now the word order matters. And you're also able to encode the sentence in a more natural way.

**中文**

所以，RNNs 的好处在于，词序现在起作用了。而且你能以更自然的方式对句子进行编码。

### [57:04](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=3424s) · b000118

**English**

So let's see roughly how it works. So we have the same favorite example, so cute teddy bear is reading. So you would have the token A. You want one-hot encoding vector. You pass it through your network. You compute the hidden state. You try to predict cute. But then you keep track of the hidden state. And then you input that into another module. And then you also consider the next words.

**中文**

我们大致看看它如何运作。还是我们最喜欢的那个例子，cute teddy bear is reading。这里有 token A。你需要一个 one-hot encoding 向量，将它传入网络，计算 hidden state，尝试预测 cute。但接下来会保留 hidden state，再把它输入另一个模块。然后，还会考虑接下来的词。

### [57:37](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=3457s) · b000119

**English**

So you consider not only the word itself, but also the hidden state of this sentence so far. And you try to predict the next word again, and again and again.

**中文**

所以，你考虑的不仅是词本身，还有句子到目前为止的 hidden state。然后再次预测下一个词，一遍又一遍。

### [57:51](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=3471s) · b000120

**English**

So this is RNN.

**中文**

这就是 RNN。

### [57:54](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=3474s) · b000121

**English**

So RNNs were used for a bunch of tasks, and just like mapping that back to the categories that we saw before. For classification purposes, you can basically use the hidden state of the last word in your sentence. For instance, if you want to predict like the sentiment of a review, you would take basically the last vector here and try to project it into the space of the predictions or the labels that you want to predict on.

**中文**

所以，循环神经网络（RNNs）被用于很多任务，我们可以把它们对应到之前看到的那些类别。对于分类（classification），基本上可以使用句子中最后一个词的隐藏状态（hidden state）。例如，如果你想预测一条评论的情感，基本上就会取这里最后一个向量，尝试把它投影到你想预测的结果或标签所在的空间。

### [58:28](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=3508s) · b000122

**English**

So for instance, if you want positive or negative, you basically project that vector onto that space. You can do that here. For multi-classification, so you would basically have the representation of the token of interest, and you would project that. Or for generation, you would basically process the whole source text, and then have a context vector, a.k.a. activation vector, a.k.a. hidden state at the end of your processing, which will then be used to decode the output prediction.

**中文**

例如，如果你想判断正面还是负面，基本上就是把那个向量投影到那个空间。你可以在这里这样做。对于多分类（multi-classification），基本上就是取得你关注的词元（token）的表示，然后将它投影。或者，对于生成（generation），基本上会处理整个源文本，然后在处理结束时得到一个上下文向量（context vector），也叫激活向量（activation vector），也叫 hidden state，随后用它来解码输出预测。

### [59:09](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=3549s) · b000123

**English**

So this is how you would use an RNN for each of these tasks. So the reason why you have not really heard of RNNs these days is because they had some pros, but a lot of cons. So one of the cons is that the meaning of the sentence is basically solely encapsulated into this hidden state.

**中文**

这就是你在这些任务中使用 RNN 的方式。如今你不太听说 RNNs，是因为它们虽然有一些优点，但缺点很多。其中一个缺点是，句子的含义基本上完全封装在这个 hidden state 中。

### [59:39](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=3579s) · b000124

**English**

So you have this problem of long-range dependencies, which basically impacts your ability to quote, unquote, "remember" what the model saw in the past, which is why you have another class of models that try to build on RNNs. So this one is called LSTMs, Long Short-Term Memory. And the goal of that extension is to have the way to somehow keep track of the things that are quote, unquote, "important" to remember, on top of the hidden state that we talked about.

**中文**

所以就有了长距离依赖（long-range dependencies）的问题，它基本上会影响你用引号括起来的“记住”模型过去看到的内容的能力。因此，有另一类模型尝试在 RNNs 的基础上进行改进。这一类叫作 LSTMs，即长短期记忆（Long Short-Term Memory）。这种扩展的目标是，在我们刚才讨论的 hidden state 之外，设法持续记录那些用引号括起来的、值得记住的“重要”内容。

### [1:00:20](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=3620s) · b000125

**English**

So here you have a of t, which is your activation, basically the sequence so far encoded in there. And then you have another quantity that you track that is called the cell state. It's denoted c here. So this architecture aims at improving that piece, but I guess it was not perfect either. But yeah, so that was the main issue of RNN-based methods, which is that they have this issue of forgetting what was in the past.

**中文**

这里有 a of t，也就是你的激活（activation），基本上把截至目前的序列编码在其中。然后还有另一个需要跟踪的量，叫作细胞状态（cell state），这里用 c 表示。这种架构旨在改善这一部分，但我想它也并不完美。对，所以这就是基于 RNN 的方法的主要问题：它们会忘记过去的内容。

### [1:01:01](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=3661s) · b000126

**English**

So you will see in the literature that this phenomenon is called vanishing gradient. And the reason why it's called that way-- so I know we're running out of time, but I'm going to just explain that part. So in order for you to predict, let's say, the last words, you're basically dependent on every hidden state that came before that.

**中文**

你会在文献中看到，这种现象叫作梯度消失（vanishing gradient）。至于为什么这样命名——我知道时间快不够了，不过我还是解释一下这一部分。为了预测，比如说，最后几个词，你基本上依赖于它之前的每一个 hidden state。

### [1:01:30](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=3690s) · b000127

**English**

So far so good? And so whenever you want to update the weights of your model to match the prediction here with the actual prediction, when you do the back propagation, you somehow need to take into account that the value here is basically not only a matter of this computation, but also this computation or this computation that basically happened in a sequential manner.

**中文**

到这里都明白吗？所以，每当你想更新模型的权重，让这里的预测与实际预测相匹配时，在进行反向传播（back propagation）时，你就需要以某种方式考虑到，这里的值基本上不仅取决于这次计算，还取决于这次计算或这次计算，它们基本上都是按顺序发生的。

### [1:02:03](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=3723s) · b000128

**English**

So you have this phenomenon of trying to, I guess, back-propagate through time. But the problem is, in practice when you write that down-- so it's a very ugly formula. But when you write that down, it ends up being a product of a bunch of quantities that can-- so if it's greater than 1, then it's exploding. If it's less than 1, it's vanishing.

**中文**

所以就出现了这种，我想可以说是，尝试随时间进行反向传播的情况。但问题是，实际把它写出来时——这是一个很难看的公式。不过写出来之后，它最终会变成一连串量的乘积，这些量可能——如果它大于 1，就会爆炸；如果小于 1，就会消失。

### [1:02:34](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=3754s) · b000129

**English**

Because if you multiply a lot of things that are less than 1, it just goes to 0. So I guess if you have something that you're trying to update that goes to 0, basically you have trouble just doing your updates. So that's a high-level intuition. This is not the focus of this class, which is why I'm not going into the detail of this ugly formulas. But I hope you get the idea that for remembering things from the past, it's not doing a great job, because of this sequential, I guess, characteristic.

**中文**

因为如果你把很多小于 1 的东西相乘，结果就会趋近于 0。所以我想，如果你试图更新的某个东西趋近于 0，基本上就很难进行更新。这就是一个宏观上的直观解释。这不是这门课的重点，所以我不会详细讲解这些难看的公式。但我希望你们能理解，由于这种，我想可以说是，顺序性的特点，它并不擅长记住过去的内容。

### [1:03:10](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=3790s) · b000130

**English**

Does that make sense? OK, I hope the next thing will make a bit more sense. But before that, I'll just recap what we saw. So our goal is to represent text. So we first started with representing words or tokens, which was what we tried to do with Word2vec. And we saw that it was a good way to leverage proxy tasks to learn this representation. But we had a bunch of limitations.

**中文**

这样说能理解吗？好，希望接下来的内容会更容易理解一些。不过在那之前，我先回顾一下我们讲过的内容。我们的目标是表示文本。所以我们首先从表示单词或 token 开始，这就是我们尝试用 Word2vec 做的事情。我们看到，利用代理任务（proxy tasks）来学习这种表示是一个很好的方法。但它有很多局限。

### [1:03:42](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=3822s) · b000131

**English**

And one of them that you mentioned was that this was not aware of the context. And also the word order didn't count. And so you have this other class of methods that is able to take into consideration the words, but then they have some trouble keeping track of things when the sequence gets very long. And you have this problem of vanishing gradients or long-range dependencies.

**中文**

其中一个是你们提到的，它无法感知上下文。而且词序也不起作用。因此，就有了另一类能够把这些词考虑进去的方法，但当序列变得很长时，它们就不太能持续跟踪其中的内容。于是就出现了梯度消失或长距离依赖的问题。

### [1:04:12](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=3852s) · b000132

**English**

So whenever you see this term, it's basically referring to that. And also another thing that I have not mentioned, but the computations are very slow. So when you want to train these models, at training time, in order to predict this word, you basically need to compute all these hidden states before. So when your sequence gets very long, it just takes a very long time.

**中文**

所以，每当你看到这个术语时，基本上就是指这个。还有一点我没提到，就是计算非常慢。训练这些模型时，为了预测这个词，基本上需要先计算前面的所有 hidden states。所以，当序列变得很长时，就会花费很长时间。

### [1:04:46](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=3886s) · b000133

**English**

So for all of these reasons, for I guess what reason. So for the fact that the model has trouble remembering things from the past, people have tried having more direct connections between something and the thing from the past, and this is the idea behind attention. So what attention does is it tries to have a direct link between what we're trying to predict and something from the past.

**中文**

所以，出于所有这些原因，或者我想是出于什么原因。也就是，因为模型难以记住过去的内容，人们尝试在某个东西与过去的东西之间建立更直接的连接，这就是注意力（attention）背后的想法。attention 所做的，就是尝试在我们要预测的内容与过去的某个内容之间建立直接联系。

### [1:05:26](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=3926s) · b000134

**English**

So in this example, let's suppose I'm trying to translate an English sentence into a French one. So here I guess the input sentence is given. I'm computing the hidden state. I'm processing words one at a time. This is my traditional RNN. So "a cute teddy bear is reading." So here I have a hidden state that I'm then decoding. And you can imagine that when wanting to generate the next word of my translation, it would be great if I knew what word I'm trying to predict.

**中文**

在这个例子中，假设我想把一个英语句子翻译成法语句子。这里，我想输入句子已经给出了。我在计算 hidden state，一次处理一个词。这就是传统的 RNN。所以，“一只可爱的泰迪熊正在阅读”。这里我有一个 hidden state，然后对它进行解码。你可以想象，当我想生成译文中的下一个词时，如果我知道自己要预测哪个词，那就太好了。

### [1:06:07](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=3967s) · b000135

**English**

Or in other words, it would be great if I could take a peek at a certain area of the input text. So the idea behind attention is to have a direct link between what you're trying to predict and things before. This is the idea behind attention. And so it was introduced in 2014. And yeah, again, this is trying to solve for these long-range dependency issues.

**中文**

或者换句话说，如果我能看一眼输入文本的某个区域，那就太好了。所以 attention 背后的想法，是在你试图预测的内容与之前的内容之间建立直接联系。这就是 attention 背后的想法。它是在 2014 年提出的。对，再说一次，这是为了尝试解决这些长距离依赖问题。

### [1:06:42](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=4002s) · b000136

**English**

And so yeah, this example we want to do that. And this concept is going to actually be key for this class. Because we're going to see that the attention mechanism is the thing that is going to make everything--I mean, most of the things work. And this is actually the main principle that the transformer paper relies on. So the transformer, which is the core architecture that we will see in this class, has been introduced or was introduced in 2017 in this paper named Attention is All You Need.

**中文**

对，在这个例子中，我们就想这样做。而且，这个概念实际上会是这门课的关键。因为我们会看到，注意力机制（attention mechanism）会让一切——我是说，大多数东西——运作起来。这其实也是 transformer 论文所依赖的主要原理。transformer 是我们在这门课中将看到的核心架构，它是在 2017 年这篇名为 Attention is All You Need 的论文中提出的。

### [1:07:22](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=4042s) · b000137

**English**

So even from the title, you can see that the authors wanted to just rely on that part. So what the authors tried to do was to move away from this sequential way of processing the text, and instead let the model just have direct connections with all parts of the text at once. So that is called self-attention. So they tried that on translation tasks.

**中文**

所以，光从标题就能看出，作者希望只依靠这一部分。作者尝试摆脱这种按顺序处理文本的方式，转而让模型同时与文本的所有部分直接连接。这就叫作自注意力（self-attention）。他们在翻译任务上进行了尝试。

### [1:07:55](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=4075s) · b000138

**English**

And they just realized that it was giving great results. So back to the example that we're still using, a cute teddy bear is reading Here what we would say is that in order to compute the representation of the token teddy bear, we're going to look at all the other tokens in the sequence at once, and directly with direct links.

**中文**

他们发现效果很好。回到我们一直在用的例子，一只可爱的泰迪熊正在阅读。这里我们的说法是，为了计算 teddy bear 这个 token 的表示，我们会同时查看序列中的所有其他 token，并通过直接连接来直接查看它们。

### [1:08:27](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=4107s) · b000139

**English**

So I guess back to your question-- here, we would have a representation of teddy bear that would be unique to the context that it is part of. So back to your question about riverbank and robbing a bank, like here the bank would have different representations. So this is the idea. I guess, does the idea roughly make sense?

**中文**

我想，回到你的问题——这里 teddy bear 的表示，会是它所处上下文特有的表示。再回到你关于 riverbank（河岸）和 robbing a bank（抢银行）的问题，这里的 bank 就会有不同的表示。这就是这个想法。我想，这个大致思路能理解吗？

### [1:08:55](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=4135s) · b000140

**English**

And again, this is called the self-attention mechanism. Afshine, how am I doing on time? 8. I have 8? OK, cool. OK, so this is the idea. So now I'm going to just introduce another set of ideas which is more terminology but is going to be very important. So when you want to express something in terms of something else, we use the words "query," "key," and "value," Q, K and V.

**中文**

再说一次，这叫作 self-attention 机制。Afshine，我时间用得怎么样？8。我还有 8？好，太好了。好，这就是基本想法。现在我要介绍另一组概念，更多是术语，但会非常重要。当你想用其他东西来表示某个东西时，我们使用“查询（query）”“键（key）”和“值（value）”这几个词，也就是 Q、K 和 V。

### [1:09:30](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=4170s) · b000141

**English**

So in this example, our goal is to figure out what other tokens is the query teddy bear more similar to. So here the question is, OK, you have a query and you want to see what other tokens are most similar. And so what you're going to do is to look at all the other tokens which are basically composed of keys and values.

**中文**

在这个例子中，我们的目标是弄清楚 query teddy bear 与哪些其他 token 更相似。所以这里的问题是，好，你有一个 query，你想看看哪些其他 token 最相似。你要做的就是查看所有其他 token，它们基本上由 keys 和 values 组成。

### [1:10:03](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=4203s) · b000142

**English**

So we're going to compare the query to the key to quantify how similar your query is to a given key, and take the corresponding value. So we'll see that in this example, so let's suppose you want to express teddy bear in terms of everything else. What you're going to do is you're going to take the query teddy bear, and you're going to compare that query with all the other keys to see which element is most similar, and then weight the more similar ones and take their associated value.

**中文**

所以，我们会比较 query 和 key，量化 query 与某个给定 key 的相似程度，然后取对应的 value。我们会在这个例子中看到，假设你想用其他所有内容来表示 teddy bear。你要做的是取 query teddy bear，将这个 query 与所有其他 keys 比较，看看哪个元素最相似，然后为更相似的那些赋予权重，并取它们关联的 value。

### [1:10:41](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=4241s) · b000143

**English**

So that's a very high level idea of how these things are. Of course, we're going to see exactly how they work. But that's the general idea.

**中文**

这就是这些东西如何运作的一个非常宏观的想法。当然，我们会具体看它们如何工作。不过总体思路就是这样。

### [1:10:55](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=4255s) · b000144

**English**

OK, cool. And speaking of query and key and value, we will also see that one benefit of expressing things this way is that we can express doing this self-attention computation across the whole sequence in a matrix format. And GPUs love matrices. So it's really made for the hardware that we have. And I guess what I mentioned here can be expressed in a form of softmax of the query and the key, which is basically a way to get some kinds of weights of which values will be more important.

**中文**

好，太好了。说到 query、key 和 value，我们还会看到，用这种方式表达有一个好处，就是可以把整个序列上的 self-attention 计算表示成矩阵形式。而图形处理器（GPUs）很喜欢矩阵。所以它确实很适合我们现有的硬件。我想，我这里提到的内容可以表示为对 query 和 key 做 softmax 的形式，基本上就是获得某种权重，用来表示哪些 values 更重要。

### [1:11:40](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=4300s) · b000145

**English**

So for instance, if a value is more important, you have bigger weight. And another one will be less important, you'll have a smaller weight. And you basically multiply that by the value. So don't worry, we'll have a detailed example after. So if it still feels very high-level fuzzy, don't worry. We'll have a detailed walkthrough. And yes, so this is how it works. OK, cool.

**中文**

例如，如果某个 value 更重要，它就有更大的权重。另一个没那么重要，就会有较小的权重。然后基本上就是把它乘以 value。不用担心，我们后面会有详细的例子。如果现在仍然觉得很宏观、很模糊，不用担心。我们会详细走一遍。对，这就是它的工作方式。好，太好了。

### [1:12:11](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=4331s) · b000146

**English**

Any questions on what self-attention is? Yeah.

**中文**

关于什么是 self-attention，有什么问题吗？请说。

### [1:12:40](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=4360s) · b000147

**English**

Great, great question. So the question is, what is value, what is key? I guess, how to get those? What do they mean? So first of all, I just want to say that these quantities, they are learned. So you are not fixing them. But from an interpretation standpoint, you can interpret that the key is there for you to figure out which one is most similar to the query. And the value is the actual value that is associated with that element. So here, you will have something like you want to express this in terms of all the values.

**中文**

很好，很好的问题。问题是，什么是 value，什么是 key？我想，也就是如何得到它们？它们是什么意思？首先，我想说，这些量是学习出来的，不是固定设定的。不过从解释的角度，你可以把 key 理解为用来判断哪一个与 query 最相似的东西。而 value 是与那个元素关联的实际值。所以这里，你会有这样的情况：你想用所有 values 来表示这个东西。

### [1:13:18](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=4398s) · b000148

**English**

So the weights in your weighted average will be basically the dot product between--basically-- between the query and the key. And the value will be the actual vector that you will use. But again, these things are learned. And something I have not mentioned, but you mentioned it correctly, so we're going to actually do projections to obtain these quantities. And these projections are actually learned by the model.

**中文**

所以，加权平均（weighted average）中的权重，基本上就是——基本上就是——query 与 key 之间的点积（dot product）。而 value 则是你实际使用的向量。但再说一次，这些东西是学习出来的。还有一点我没有提到，但你说得对，我们实际上会通过投影（projections）来获得这些量。而这些投影实际上是由模型学习的。

### [1:13:48](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=4428s) · b000149

**English**

That's good? OK, cool. So with that, we have 15 minutes, right, to talk about the architecture. OK, so at a very high level, in order to make the self-attention mechanism happen, the authors propose an architecture that is composed of two parts, an encoder, which is on the left side, and a decoder, which is on the right side.

**中文**

这样可以吗？好，太好了。那么，我们还有 15 分钟来讨论架构，对吧？好，从非常宏观的角度来看，为了实现 self-attention 机制，作者提出了一种由两部分组成的架构：左边的编码器（encoder），以及右边的解码器（decoder）。

### [1:14:26](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=4466s) · b000150

**English**

So the application that they have is translation. So what will go through the encoder is the input text in your source language. And what is going to go through the decoder is the target language that you're predicting. So the high-level idea is you're going to compute meaningful embeddings from your input text by passing them through the encoder.

**中文**

他们的应用是翻译。通过 encoder 的，是源语言的输入文本。通过 decoder 的，是你正在预测的目标语言。总体思路是，把输入文本送入 encoder，计算出有意义的嵌入（embeddings）。

### [1:14:57](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=4497s) · b000151

**English**

And you want that self-attention mechanism to apply, meaning you want to compute representations of each token as a function of others. And you do that by using a layer called the attention layer. So multi-head attention layer, but multi-head is just doing this computation in different ways to just allow the model to learn different representations or different projections. But the idea here is you are going to input your input text, and all the tokens in your input text are going to attend to one another.

**中文**

你希望应用 self-attention 机制，也就是说，你希望把每个 token 的表示计算为其他 token 的函数。为此，你会使用一个叫作注意力层（attention layer）的层。具体来说，是多头注意力层（multi-head attention layer），不过 multi-head 只是以不同方式进行这种计算，让模型能够学习不同的表示或不同的投影。这里的思路是，你把输入文本输入进去，输入文本中的所有 token 都会相互关注。

### [1:15:40](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=4540s) · b000152

**English**

So for instance, a cute teddy bear is reading, you are going to compute the representation of all the tokens in this text basically as a function of others. And you're going to do that with the encoder, so here with the multi-head attention. And then you have a feedforward layer, which is just to let the model learn another kind of projection. And what you're going to obtain at the end of your encoding process is rich representations of the tokens from the input sentence.

**中文**

例如，一只可爱的泰迪熊正在阅读，你基本上会把这段文本中所有 token 的表示计算为其他 token 的函数。你会通过 encoder 来做这件事，也就是这里的 multi-head attention。然后还有一个前馈层（feedforward layer），只是为了让模型学习另一种投影。在编码过程结束时，你会得到输入句子中各个 token 的丰富表示。

### [1:16:19](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=4579s) · b000153

**English**

So far, so good? But now your goal is to actually translate the input sentence. So what you're going to do is to start your translation with, let's suppose, the beginning of sentence token, so your first token. And what you're going to do is use all the representations from your input sentence in order to figure out what to predict next.

**中文**

到这里都明白吗？但现在你的目标是实际翻译输入句子。因此，你要做的是从，比如说，句子起始 token 开始翻译，也就是你的第一个 token。然后，你会使用输入句子中的所有表示，来确定接下来预测什么。

### [1:16:50](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=4610s) · b000154

**English**

So this what I just said is the cross-attention layer, which is the one that is the second, so this one, which basically--I'm not sure if you see the arrows, but there are two arrows coming from the encoder, one arrow coming from the decoder. Can anyone tell me what the arrow from the decoder represents? Is decoder a query key or value?

**中文**

我刚才说的就是交叉注意力层（cross-attention layer），也就是第二个，这一个，它基本上——我不确定你们是否能看到箭头，不过有两个箭头来自 encoder，一个箭头来自 decoder。谁能告诉我，来自 decoder 的箭头表示什么？decoder 是 query、key 还是 value？

### [1:17:22](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=4642s) · b000155

**English**

I guess there is 1 over 3, 33% chance. Who wants to try? Is it key? OK.

**中文**

我想有 1 over 3，也就是 33% 的概率。谁想试试？是 key 吗？好。

### [1:17:35](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=4655s) · b000156

**English**

Query? OK. So the way to think about it is you're trying to ask yourself, what are the words from the input that matter. Right? So basically, you want know, given your query, what are the elements from the inputs that matter? So here, this arrow is indeed the query, because this is the thing that you want to figure out. And the keys and values are actually coming from the encoder, which are basically coming from the input sequence.

**中文**

query？好。你可以这样理解：你在问自己，输入中的哪些词是重要的，对吧？所以，基本上，你想知道，给定你的 query，输入中的哪些元素是重要的？这里这个箭头确实是 query，因为这就是你想弄清楚的东西。而 keys 和 values 实际上来自 encoder，基本上也就是来自输入序列。

### [1:18:14](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=4694s) · b000157

**English**

And then you have another attention layer, which is this one. And that one is trying to figure out what other tokens of the output sentence that you're decoding is going to be useful to predict the next token. So let's suppose you start decoding and you say, un ours en peluche, which is in French. To predict the next word, you want to basically figure out what are the tokens translated so far that are going to be useful to predict the next word.

**中文**

然后还有另一个 attention layer，也就是这个。这个层试图弄清楚，你正在解码的输出句子中，还有哪些 token 有助于预测下一个 token。假设你开始解码，得到 un ours en peluche，这是法语。为了预测下一个词，你基本上想弄清楚，到目前为止已经翻译出来的哪些 token 有助于预测下一个词。

### [1:18:51](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=4731s) · b000158

**English**

So this is what this attention layer is about. And it's called masked, because it only looks at the tokens that translated so far. It does not look at tokens that were not translated, because of course they were not translated. So there's no way, like on the right side of the token that you're trying to predict.

**中文**

这就是这个 attention layer 的作用。它被称为掩码的（masked），因为它只查看截至目前已经翻译出来的 token。它不会查看尚未翻译出来的 token，因为它们当然还没有被翻译出来。所以没有办法，比如说，去看你正在尝试预测的 token 右侧的内容。

### [1:19:15](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=4755s) · b000159

**English**

Cool. So at a very high level, you have this attention layer, which is present in the encoder, which is present in the decoder, but it has several, I guess, use cases. So the attention layer here aims at computing embeddings from the input sentence as a function of themselves. And then the ones from the decoder, so the first one, the masked self-attention layer, aims at expressing something as a function of everything that has been decoded so far.

**中文**

很好。所以，从非常宏观的角度来看，你有这种 attention layer，它既存在于 encoder 中，也存在于 decoder 中，但它有几种，我想可以说是，用途。这里的 attention layer 旨在根据输入句子本身来计算它的 embeddings。然后是 decoder 中的那些层，第一个是掩码自注意力层（masked self-attention layer），旨在将某个东西表示为截至目前已解码的所有内容的函数。

### [1:19:56](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=4796s) · b000160

**English**

And the second one, the cross-attention layer, tries to express things as a function of what has been seen in the input. So here, given that you are having direct links to different tokens, you don't have this sense of order. Because in the RNN, you are basically expressing things one at a time. So you had some sense of the word order, but here you don't have it, because it's like a direct link, which is why you have position encodings, which are there to inform on the position of the word in the sequence.

**中文**

第二个是 cross-attention layer，它尝试根据输入中已经看到的内容来表示这些东西。这里，因为你与不同 token 之间都有直接连接，所以并没有这种顺序感。在 RNN 中，你基本上是一次表示一个东西，因此会有某种词序信息。但这里没有，因为它就像直接连接。这就是为什么需要位置编码（position encodings），它们用来提供词在序列中的位置信息。

### [1:20:40](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=4840s) · b000161

**English**

So we're not going to dig into that today, but I just want to call that out. So at a very high level, and we're going to see this in the detailed example, what we do is in order to translate a sentence from source language to target language, we're first going to tokenize the text, so dividing into arbitrary units. We're going to learn an embedding for these tokens. So this is what the input embedding is about. Then we're going to add some encoding with respect to the position.

**中文**

今天我们不会深入讨论这一点，不过我想特别指出它。所以，从非常宏观的角度来看——我们会在详细示例中看到——为了把一个句子从源语言翻译成目标语言，我们首先会对文本进行词元化（tokenize），也就是把它划分为任意单位。我们会为这些 token 学习 embedding。这就是输入嵌入（input embedding）的作用。然后我们会添加一些与位置有关的编码。

### [1:21:14](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=4874s) · b000162

**English**

We're not going to talk about it today, but just good to note. And then we go through the encoder. So the encoder tries to figure out how to express things as a function of other things from the inputs. So it does that in the multi-head attention layer. And then it goes through a feedforward neural network, which is just a way to just project the vectors to just have some more degrees of freedom to learn things.

**中文**

今天不会讨论它，不过知道这一点就好。然后我们经过 encoder。encoder 尝试弄清楚，如何把某些东西表示为输入中其他东西的函数。它在 multi-head attention layer 中完成这件事。然后经过一个前馈神经网络（feedforward neural network），这只是一种投影向量的方法，让模型多一些学习的自由度。

### [1:21:48](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=4908s) · b000163

**English**

And then once you have these representations from the input, you're then going to start your translation. So you start with the BOS token. And what you're trying to do is figure out what the next word is. So you're going to see, OK, what are the words that were translated so far that are useful for translation. So this is what the masked multi-head attention layer does. And then you have another attention layer, which is about expressing things as a function of what was in the input, which is the cross-attention layer over there.

**中文**

一旦得到输入的这些表示，你就开始翻译。从句子起始词元（BOS token）开始。你要做的是弄清楚下一个词是什么。所以你会看，好，目前已经翻译出来的哪些词对翻译有帮助。这就是掩码多头注意力层（masked multi-head attention layer）所做的。然后还有另一个 attention layer，用来把这些东西表示为输入内容的函数，也就是那里的 cross-attention layer。

### [1:22:27](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=4947s) · b000164

**English**

And then you have a feedforward neural network to, again, give some more degrees of freedom. And at the end of the day, you have a vector that you then go through softmax. And it just is a way for you to guess what is the next word. So you have a vector of vocabulary size. And you're going to use these values to determine what is your next word.

**中文**

然后还有一个 feedforward neural network，同样是为了增加一些自由度。最终，你得到一个向量，再让它经过 softmax。这就是用来猜测下一个词的一种方式。你会得到一个大小等于词表大小的向量，然后利用这些值来确定下一个词。

### [1:22:58](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=4978s) · b000165

**English**

Easy, right? Any questions on this? Yeah.

**中文**

很简单，对吧？关于这个有什么问题吗？请说。

### [1:23:09](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=4989s) · b000166

**English**

All right, that's a great question. The question is, what does head mean? So I guess I went too fast. I ignored that part. But when you do the self-attention computation, you basically make queries interact with keys, and then take the corresponding value. But nothing prevents you from doing that several times. So the term "head" is given to the projection matrices that you use to obtain the query, key, and value.

**中文**

好，这是个很好的问题。问题是，头（head）是什么意思？我想我讲得太快了，略过了这一部分。不过，在进行 self-attention 计算时，基本上是让 queries 与 keys 交互，然后取对应的 value。但你完全可以重复做几次。所以，“head”这个术语指的是你用来获得 query、key 和 value 的那些投影矩阵。

### [1:23:46](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=5026s) · b000167

**English**

And when you have several heads, what you're doing is you're allowing your model to learn different projections. So it's basically an additional degree of freedom for your model to learn different associations between your vectors. So it's a great question. So typically it will be noted lowercase h, number of heads. And this is what this corresponds to. Does that answer your question?

**中文**

当你有多个 heads 时，你就是在允许模型学习不同的投影。所以，这基本上为模型提供了额外的自由度，让它学习向量之间不同的关联。这是个很好的问题。通常会用小写 h 表示 heads 的数量。这就是它所对应的含义。这样回答了你的问题吗？

### [1:24:16](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=5056s) · b000168

**English**

Cool, very cool.

**中文**

很好，非常好。

### [1:24:23](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=5063s) · b000169

**English**

OK, we have a lot to discuss, but here I had the slide actually for this. So this is the multi-heads that you were mentioning. So we're basically running the self-attention computation several times in parallel, again, with different projection matrices that the model learns. So in case you have a computer vision background, it is similar to having multiple filters in your convolution. So it's the same idea, but it's different here.

**中文**

好，我们还有很多内容要讨论，不过我这里其实有一张讲这个的幻灯片。这就是你提到的 multi-heads。我们基本上是在并行运行多次 self-attention 计算，同样，使用模型学习到的不同投影矩阵。如果你有计算机视觉（computer vision）背景，这类似于在卷积（convolution）中使用多个滤波器（filters）。所以是同样的想法，不过这里有所不同。

### [1:24:58](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=5098s) · b000170

**English**

Yeah, great question. So the question is, are the projections different? So we're typically not constraining things. We're just letting the model learn. But in practice, it just tends to learn different ways of saying the same thing. So yeah, typically there is no constraint. Of course, you have papers that dig into how about if you change this.

**中文**

对，很好的问题。问题是，这些投影不同吗？通常我们不会施加约束，只是让模型自己学习。但在实践中，它往往会学到表达同一件事的不同方式。所以对，通常没有约束。当然，也有论文深入研究，如果改变这一点会怎么样。

### [1:25:28](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=5128s) · b000171

**English**

But typically you don't have any constraint.

**中文**

但通常不会有任何约束。

### [1:25:34](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=5134s) · b000172

**English**

Cool, great. OK, I will just mention one trick, another trick that the transformer authors use. So it's called label smoothing. Who has heard of label smoothing? So one new thing here is in NLP when you want to predict what comes next, there's typically more than one way.

**中文**

很好，太好了。好，我再提一个技巧，transformer 作者使用的另一个技巧。它叫作标签平滑（label smoothing）。谁听说过 label smoothing？这里一个新的点是，在自然语言处理（NLP）中，当你想预测接下来是什么时，通常不止一种可能。

### [1:26:06](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=5166s) · b000173

**English**

When you say, what a great day, what a great lecture, what a great book, what a great--there's always multiple choices. There's more than one way of filling that gap. So label smoothing is a technique that tries to intuitively address that. And what it does is, instead of saying predict this word 100% is this one, there is no other words, what it does is it says, predict this word, but there's a chance it's not this word.

**中文**

当你说，多么美好的一天、多么精彩的一堂课、多么棒的一本书、多么棒的——总会有多种选择。填补这个空缺的方式不止一种。所以 label smoothing 是一种尝试从直觉上处理这个问题的技术。它的做法不是说，预测这个词，100% 就是这个词，没有其他词；而是说，预测这个词，但也有可能不是这个词。

### [1:26:40](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=5200s) · b000174

**English**

And in practice, what it does is it takes the one-hot encoding. And instead of saying it's a 1, 0, 0, 0, that you need to predict, it says it's actually 1 minus epsilon, and then epsilon over v minus 1, I guess, is you're trying to predict.

**中文**

在实践中，它会取独热编码（one-hot encoding）。它不会说你需要预测的是 1, 0, 0, 0，而是说，实际上你要预测的是 1 减 epsilon，然后是 epsilon 除以 v 减 1，我想是这样。

### [1:27:00](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=5220s) · b000175

**English**

So in practice, it's a method that tends to make your model be more unsure. Again, to be less sure about this prediction because you always tell it, OK, try to predict this, but actually it's possible it's not the correct value. But in practice, the authors see that it tends to improve metrics like BLEU, which is a proxy metric for translation tasks.

**中文**

所以在实践中，这种方法往往会让模型更不确定。再说一次，就是对这个预测没那么确定，因为你总是在告诉它，好，试着预测这个，但实际上它也可能不是正确的值。不过在实践中，作者发现它往往能改善 BLEU 之类的指标，BLEU 是翻译任务的一个代理指标。

### [1:27:31](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=5251s) · b000176

**English**

So yeah, I think this method is pretty general for NLP. So yeah, it's a good one to know. And with that, I think there's about 20-ish minutes left. So yeah, Shervine is going to walk you through an end-to-end example. And with that, you--yeah, Oh, u? So I guess here you can think of this as, I guess, some quantity.

**中文**

所以，对，我认为这个方法在 NLP 中相当通用。对，了解它很有用。讲到这里，我想大约还剩 20 来分钟。接下来，Shervine 会带你们完整看一个端到端（end-to-end）的例子。那么，你——对，哦，u？我想这里可以把它看成，我想是，某个量。

### [1:28:06](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=5286s) · b000177

**English**

It's not defined, so some quantity. And the delta is like one hot, if you want, something like this. It can also be a constant. Yeah, yeah.

**中文**

它没有定义，所以就是某个量。而 delta 类似于 one hot，如果你愿意，可以这样理解。它也可以是一个常数。对，对。

### [1:28:32](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=5312s) · b000178

**English**

So question is, is there a relation with explore and exploit? It's an interesting one.

**中文**

问题是，这与探索和利用（explore and exploit）有关系吗？这是个有意思的问题。

### [1:28:42](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=5322s) · b000179

**English**

So why would softmax give it for free, by the way?

**中文**

顺便问一下，为什么 softmax 会自带这个效果呢？

### [1:28:48](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=5328s) · b000180

**English**

Right, but I guess it would still--so I guess at the end of the day, what you're trying to do is to compare your prediction with respect to the label. So I guess the question here is, do you want to compare with 1, 0, 0, 0, or do you want to compare with something that is not 1, 0, 0, 0. So I guess softmax does not allow you to do that. Exactly, yes. So I'm not sure if this was super clear, but this is actually the label. So what you're trying to predict is not 1, 0, 0.

**中文**

对，但我想它仍然会——我想，归根结底，你要做的是将预测与标签进行比较。所以这里的问题是，你想和 1, 0, 0, 0 比较，还是想和不是 1, 0, 0, 0 的某个东西比较。我想 softmax 并不能让你做到这一点。没错，是的。我不确定刚才是否讲得特别清楚，但这实际上是标签。所以，你试图预测的并不是 1, 0, 0。

### [1:29:21](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=5361s) · b000181

**English**

But we change the label in a way that makes the model, I guess, predict something that is less sure, I guess. Cool, thanks. And with that, yeah, Shervine. OK, great. Thank you, Afshine. And yes, so we saw basically how the transformer worked. And now we're going to piece it all together with the one specific example. OK, great. So let's take our favorite example again. So a cute teddy bear is reading.

**中文**

而是我们改变标签，让模型，我想，预测出一个没那么确定的东西，我想是这样。很好，谢谢。那么，对，Shervine。好，太好了。谢谢你，Afshine。对，我们基本上已经看到了 transformer 如何工作。现在我们会通过一个具体的例子，把所有内容串起来。好，太好了。再来看看我们最喜欢的那个例子：一只可爱的泰迪熊正在阅读。

### [1:29:51](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=5391s) · b000182

**English**

And then we'll go all together through each step. So first we start with tokenization. So as we said, we can use any arbitrary decomposition to decompose this into tokens. And then as someone mentioned, you need to have some way to indicate the start and the end of a sequence. So typically, this is done with the BOS and EOS tokens. So you add them.

**中文**

然后我们一起走过每一个步骤。首先从词元化（tokenization）开始。正如我们所说，可以用任意划分方式把它拆成 tokens。然后，正如有人提到的，需要某种方式来标记序列的开始和结束。通常，这是通过 BOS 和句子结束词元（EOS tokens）完成的。所以把它们加上。

### [1:30:25](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=5425s) · b000183

**English**

So now let's focus on the composition of each token representation. So you have its embedding. That is learned. And as Afshine mentioned, in order to have an idea of what is the position of the words or the token, I should say as part of the sequence, you have some added information that is in the form of a position embedding. And here, the original paper uses the convention of some sines and cosines that it adds additively to the representation.

**中文**

现在来关注每个 token 表示的组成。它有自己的 embedding，这是学习出来的。正如 Afshine 提到的，为了知道单词，或者应该说 token，在序列中的位置，你会加入一些额外信息，形式是位置嵌入（position embedding）。这里，原始论文采用了一种使用正弦和余弦的约定，将它们以相加的方式加入表示中。

### [1:30:58](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=5458s) · b000184

**English**

So it's like an element-wise addition. OK, great. So now you have a position-aware embedding for your token. And you repeat that for each of your tokens. So now you can see all of these embeddings in the format of a matrix, which is of size d model, which is the size of your embeddings. And then the other dimension is the length of the sequence, so typically n.

**中文**

所以，这类似于逐元素相加（element-wise addition）。好，太好了。现在你的 token 就有了包含位置信息的 embedding。对每个 token 都重复这个过程。现在，可以把所有这些 embeddings 看成一个矩阵，其中一个维度是 d model，也就是 embeddings 的大小。另一个维度是序列长度，通常记作 n。

### [1:31:29](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=5489s) · b000185

**English**

So all make sense so far? Any questions on the inputs? OK, great. So now we will send this representation through the encoder. So as Afshine said, you have this concept of self-attention. And the way you perform self-attention is that you take this input and project it on three spaces. So you project it to the space Wq, you get queries.

**中文**

到这里都能理解吗？关于输入有什么问题吗？好，太好了。现在我们把这个表示送入 encoder。正如 Afshine 所说，这里有 self-attention 这个概念。进行 self-attention 的方式是，取这个输入，并将它投影到三个空间。把它投影到 Wq 空间，就得到 queries。

### [1:32:00](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=5520s) · b000186

**English**

You project the same embeddings in the space Wk, you get keys. And you do the same for values, you get your values. And then Wq, Wk, and Wv are learned by the model. They are basically projection matrices.

**中文**

把同样的 embeddings 投影到 Wk 空间，就得到 keys。对 values 也做同样的事情，就得到 values。Wq、Wk 和 Wv 都是模型学习出来的。它们基本上就是投影矩阵。

### [1:32:19](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=5539s) · b000187

**English**

So far, so good? So now with all of that in mind, you can apply the formula that Afshine mentioned, that is the self-attention formula, which is softmax of Qk transpose over square root of dk times v, which gives you another matrix out of all of this.

**中文**

到这里都明白吗？理解这些之后，就可以应用 Afshine 提到的公式，也就是 self-attention 公式：对 Qk 的转置除以 dk 的平方根做 softmax，再乘以 v \[字幕疑误，可能指 Q 与 k 的转置相乘后除以 dk 的平方根，再做 softmax 并乘以 v\]，这样就从这些计算中得到另一个矩阵。

### [1:32:42](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=5562s) · b000188

**English**

Now let's pause for a second and look at how this computation is done in practice and what every step means.

**中文**

现在我们暂停一下，看看这个计算在实践中是怎么做的，以及每一步都意味着什么。

### [1:32:52](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=5572s) · b000189

**English**

So let's look at Q. When you compute Q, basically you project your embeddings into that space. What do you obtain? You obtain a matrix where each row represents a given query. When you say k transpose, it's basically the same matrix, but transposed, where each column represents the key representation of each token. Now let's mix them together with the matrix multiplication.

**中文**

来看 Q。计算 Q 时，基本上就是把 embeddings 投影到那个空间。会得到什么？会得到一个矩阵，其中每一行代表一个给定的 query。说到 k 的转置，基本上是同样的矩阵，但进行了转置，其中每一列代表每个 token 的 key 表示。现在，通过矩阵乘法把它们组合起来。

### [1:33:25](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=5605s) · b000190

**English**

So when you multiply each of them, you see that each row represents the projection of the query over each key, such that when you take the matrix multiplication and get the softmax of all of this, you get a probability distribution of the projection of the query over keys for each query. Each line will have this. And I don't know if anyone asked the question regarding why do we scale by square root of dk?

**中文**

当你把它们相乘时，会看到每一行代表 query 在每个 key 上的投影。因此，当你进行矩阵乘法，再对所有这些结果取 softmax 时，就会为每个 query 得到它在各个 keys 上投影的概率分布。每一行都有这样的分布。我不知道之前是否有人问过，为什么要用 dk 的平方根进行缩放？

### [1:34:03](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=5643s) · b000191

**English**

So it could be dq as well because matrix multiplication, like the dot product here, enforces the fact that dq equals dk. And basically, what you see is that these dot products has the dimension of key and queries grows, it will tend to grow as well. So you want to normalize these dot products. And this is why you divide by square root of the dimension of keys. OK, great. And then now you have your softmax of all of these, and then you multiply it with the matrix v. And this is Afshine explained as having the query projected on the space of keys, and then multiplied by the corresponding value.

**中文**

它也可以是 dq，因为矩阵乘法，比如这里的 dot product，要求 dq 等于 dk。基本上你会看到，随着 key 和 queries 的维度增大，这些 dot products 往往也会增大。所以你想对这些 dot products 进行归一化（normalize）。这就是为什么要除以 keys 维度的平方根。好，太好了。现在，你得到了所有这些结果的 softmax，然后将它乘以矩阵 v。这就是 Afshine 解释的，把 query 投影到 keys 的空间，然后乘以对应的 value。

### [1:34:49](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=5689s) · b000192

**English**

So the value is the representation of the corresponding key that we project on. So you end up with a weighted sum of values for each query.

**中文**

所以，value 是我们所投影到的那个对应 key 的表示。因此，最终会为每个 query 得到 values 的加权和（weighted sum）。

### [1:35:03](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=5703s) · b000193

**English**

OK, great. Does that make sense so far?

**中文**

好，太好了。到这里能理解吗？

### [1:35:12](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=5712s) · b000194

**English**

OK, awesome. And someone asked, what is the multi-head stuff? So you're right, it's not just single one, one time that it's done. It's actually done each times. And what you obtain is, like, all of that is done in parallel. And at the end, you obtain h such matrices. And you concatenate them with respect to the columns. And at the end of this, you have another projection matrix that you call Wo that will project all of these back to the original dimension of embeddings.

**中文**

好，太棒了。有人问，multi-head 是什么？你说得对，它并不是只做单独的一次。实际上会做 each 次 \[字幕疑误，可能指 h 次\]。你得到的就是，所有这些都并行完成。最后，你会得到 h 个这样的矩阵。你按照列将它们拼接起来。最后，还有一个叫作 Wo 的投影矩阵，把所有这些投影回 embeddings 的原始维度。

### [1:35:49](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=5749s) · b000195

**English**

So it's a way for the network to basically have a dimension-invariant way--bless you-- to go from the original dimension back to the original one. Any questions? Yep.

**中文**

所以，这是一种让网络基本上以保持维度不变的方式——祝你健康——从原始维度再回到原始维度的方法。有什么问题吗？请说。

### [1:36:15](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=5775s) · b000196

**English**

So the question is regarding h. Is it possible to get the same result each time? And if so, concatenate the same thing, will it be helpful? Did I get the question right?

**中文**

问题是关于 h 的。每次是否可能得到相同的结果？如果是这样，把相同的东西拼接起来会有帮助吗？我理解对你的问题了吗？

### [1:36:28](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=5788s) · b000197

**English**

So what makes it different? So it's the magic of gradient descent. So the network has an objective function at the end. It has degrees of freedom. Its incentive is to build a representation that will be helpful to learn the next word. So it doesn't have an incentive to copy the same thing or do the same mechanism. And this is why in practice you see the model converge towards building different representations that it can then concatenate and then project into something useful. So what makes it such that you don't have the same thing?

**中文**

那么，是什么让它们不同呢？这就是梯度下降（gradient descent）的神奇之处。网络最终有一个目标函数（objective function），也有自由度。它的动力是构建一种有助于学习下一个词的表示。所以，它没有动力去复制同样的东西或采用同样的机制。这就是为什么在实践中，你会看到模型收敛到构建不同表示的方式，然后将它们拼接起来，再投影成某种有用的东西。那么，究竟是什么确保你不会得到相同的东西呢？

### [1:37:00](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=5820s) · b000198

**English**

Nothing. Like, you don't have any constraints. But the nature of the learning that you let the model have makes it do so in practice.

**中文**

没有。也就是说，你没有任何约束。但你让模型进行的这种学习，其本身的性质使它在实践中会这样做。

### [1:37:14](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=5834s) · b000199

**English**

Any other questions? And that is a great question. I mean, typically gradient descent does wonders. OK great. So now that we have gone through the self-attention layer, you have another component that is the FFN. And I think there was a question just here regarding how to choose the dimension of the hidden layer with respect to the input and outputs. So when Afshine mentioned Word2vec, typically you have a smaller dimension than the input and output.

**中文**

还有其他问题吗？这是个很好的问题。我的意思是，gradient descent 通常会创造奇迹。好，太好了。现在我们已经经过了 self-attention layer，还有另一个组件，就是前馈网络（FFN）。我想刚才这里有个问题，是关于如何相对于输入和输出来选择隐藏层的维度。Afshine 提到 Word2vec 时，通常隐藏层的维度小于输入和输出。

### [1:37:48](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=5868s) · b000200

**English**

But here, actually, the hidden layer is of a bigger dimension than input and output. And the rationale for that is that you want to have enough degrees of freedom for the model to learn useful representations. So it's a way to complexify the features that you learn. And, yeah \[INAUDIBLE\]. OK, great. And you don't have just one encoder module. You have actually n of them, big N in the original paper.

**中文**

但在这里，隐藏层的维度实际上比输入和输出更大。原因是，你希望模型有足够的自由度来学习有用的表示。所以，这是一种让所学特征变得更复杂的方法。然后，对，\[听不清\]。好，太好了。而且，你并不只有一个 encoder 模块，实际上有 n 个，在原始论文中用大写 N 表示。

### [1:38:19](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=5899s) · b000201

**English**

And at the end of all of this, you have an encoded context-aware set of embeddings. And then each of these setups encoded embeddings will be those that will be fed to the n decoders. So you have like a stacked succession of n encoders. You have a stacked succession of n decoders. And the last representation of the encoder is what you will feed to the cross-attention of each decoder.

**中文**

在这一切结束时，你会得到一组经过编码、能够感知上下文的 embeddings。然后，这些组中的每组已编码 embeddings 都会被送入 n 个 decoders。所以，你有 n 个依次堆叠的 encoders，也有 n 个依次堆叠的 decoders。而 encoder 的最后一个表示，就是你送入每个 decoder 的 cross-attention 的内容。

### [1:38:54](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=5934s) · b000202

**English**

So yeah, we're going to see that more in detail. So how do we even start the decoding process? So you start with the BOS token. Basically saying to the model, hey, we need to predict the next word, let's start. So what happens to the BOS token at the very beginning? So you feed it to the decoder. And then similarly as before for the encoder, you have a self-attention layer. And as Afshine mentioned, the self-attention layer is causal.

**中文**

对，我们会更详细地看这一点。那到底如何开始解码过程呢？从 BOS token 开始。基本上就是对模型说，嘿，我们需要预测下一个词，开始吧。那么，最开始 BOS token 会发生什么？你把它送入 decoder。然后，与之前 encoder 的情况类似，你有一个 self-attention layer。正如 Afshine 提到的，这个 self-attention layer 是因果的（causal）。

### [1:39:27](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=5967s) · b000203

**English**

So the attention will be done on the same token and the tokens that precede it. So on this first BOS token, you don't see a difference, because it will just attend to itself. But when you have other tokens that you want to decode, you will have this difference in where you attend with respect to decoder. OK, great, goes through the self-attention layer. And then you have what I mentioned to be the cross-attention that takes as keys and values these encoded embeddings as inputs.

**中文**

所以，attention 会作用于同一个 token 以及它之前的 tokens。对于这个最初的 BOS token，你看不出区别，因为它只会关注自身。但当你有其他想要解码的 tokens 时，在 decoder 中关注哪些位置就会体现出这种差别。好，太好了，经过 self-attention layer。然后是我提到的 cross-attention，它把这些已编码的 embeddings 作为输入，用作 keys 和 values。

### [1:40:04](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=6004s) · b000204

**English**

And then the queries are those that come out of the self-attention layer. OK, great. And then once you do this cross-attention, you have, just like in the encoder, an FFN component that makes the representation richer. Was there a question there? No.

**中文**

而 queries 则来自 self-attention layer 的输出。好，太好了。完成这个 cross-attention 之后，与 encoder 中一样，还有一个 FFN 组件，让表示更加丰富。那边有问题吗？没有。

### [1:40:28](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=6028s) · b000205

**English**

And then at the very end, so you do all of that n times. And at the very end of the decoding process, you have a linear projection and a softmax layer to turn the prediction of the next word into a probability distribution over the vocabulary. OK, great. So we saw how to do that for the next word here. And basically you do that again and again. So you have found your next token, which is like a one-hot basically encoding of what you want.

**中文**

然后在最后，你会把所有这些做 n 次。在解码过程的最末端，有一个线性投影（linear projection）和一个 softmax 层，把对下一个词的预测转换为词表上的概率分布。好，太好了。我们已经看到了如何为这里的下一个词完成这个过程。基本上，你会不断重复这样做。你已经找到了下一个 token，它基本上就是你想要的内容的 one-hot 编码。

### [1:41:03](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=6063s) · b000206

**English**

And then you take that embedding and then put it back in the decoder and continue this process. And when do you stop? It's a question for you all. When you hit the EOS token. Yeah, yeah exactly. OK, great. And with this process, it's basically how the authors of this original landmark paper did machine translation. So this is typically the use case that was presented.

**中文**

然后你取那个 embedding，再把它放回 decoder，继续这个过程。什么时候停止呢？这个问题问你们。当遇到 EOS token 时。对，对，完全正确。好，太好了。通过这个过程，原始的这篇里程碑式论文的作者基本上就是这样进行机器翻译（machine translation）的。所以，这就是当时展示的典型用例。

### [1:41:37](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=6097s) · b000207

**English**

Any questions?

**中文**

有什么问题吗？

### [1:41:45](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=6105s) · b000208

**English**

OK, awesome. And with that, thank you for your attention. \[APPLAUSE\]

**中文**

好，太棒了。那么，谢谢大家的聆听。\[掌声\]
