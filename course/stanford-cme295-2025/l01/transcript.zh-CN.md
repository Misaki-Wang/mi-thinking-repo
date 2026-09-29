# Stanford CME295 Transformers &amp; LLMs \| Autumn 2025 \| Lecture 1 - Transformer

_中文讲稿_

- Channel: Stanford Online
- Source: [YouTube](https://www.youtube.com/watch?v=Ub3GoFaUcds)
- Duration: 1:41:59
- Caption source: manual
- Status: complete
- Chinese translation: 208/208
- Translation provider: codex
- Generated: 2026-09-29T15:38:06+00:00

## 讲稿

### [00:05](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=5s) · b000001

好。大家好，欢迎来到 CME 295——Transformers 与大语言模型（Large Language Models）。我叫 Afshine。我会和在后面的 Shervine 一起教授这门课。开始之前，先介绍一下我们自己。我们是双胞胎兄弟，背景也很相似。我们都就读于法国一所叫 Centrale Paris 的学校，之后各自走上了不同的道路。

### [00:37](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=37s) · b000002

我这边去了 MIT，Shervine 则去了 Stanford，攻读 ICME 硕士项目。之后，我想我们的业界经历也很相似。我先去了 Uber，随后 Shervine 也来了 Uber，接着 Shervine 离开去了 Google，我也去了 Google。最近，我加入了 Netflix，Shervine 也加入了 Netflix。我们一直在从事大语言模型方面的工作。

### [01:07](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=67s) · b000003

所以，是的，我想我们都有技术背景，主要面向大语言模型（LLMs）。好，那我们为什么要开这门课呢？从 2020 年起，Shervine 和我一直专注于自然语言处理（Natural Language Processing，NLP）。我们一直以每年一次的工作坊形式讲授这门课。也就是 2021、2022、2023、2024 年。ChatGPT 在 2022 年出现，突然之间，大家对 LLMs 产生了很大的兴趣。

### [01:40](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=100s) · b000004

所以，实际上是在去年春天，我们开始把这门课作为 Stanford 的正式课程开设，现在叫 CME 295，这是第二次开课。

### [01:55](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=115s) · b000005

好。那你们可以期待从这门课中学到什么？首先，LLMs 现在基本上无处不在。我想我们这里有两个目标。第一个是了解让这一切运转起来的底层机制。我们会学习 Transformer，它是让这一切成为可能的基础架构。第二个是了解这些 LLMs 如何训练，以及应用在哪里。

### [02:31](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=151s) · b000006

所以，如果你还在考虑这门课是否适合你，我会说，它很适合一般来说对这个领域感兴趣的人：无论是因为你想把它作为职业目标，想成为研究科学家或机器学习科学家（ML scientist）；还是想开发一个在某种程度上依赖 LLMs 的个人项目，想了解一些注意事项，我想，也就是哪些方法有效、哪些无效；又或者你来自其他领域，只想知道人工智能（AI）、生成式人工智能（GenAI）、LLMs 这一整套东西是如何运作的，以及如何把它应用到自己的领域。

### [03:14](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=194s) · b000007

那么，关于先修要求，我会说，最起码你应该具备一些机器学习（ML）基础，比如基本了解模型如何训练、什么是神经网络（neural network），还有一些线性代数基础，比如矩阵是如何相乘的。不过，即使你在这个领域的能力还在培养中，我想也没关系，我们仍然会在这里帮助你。

### [03:48](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=228s) · b000008

不过，我想这些就是比较理想的先修要求。

### [03:54](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=234s) · b000009

好。继续说课程安排，这门课每周五 3:30 到 5:20 上课，地点就在这里。

### [04:08](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=248s) · b000010

这门课是两个学分。你可以选择字母评分制（letter grade），或者学分／无学分制（credit/non-credit）。从这里的设备布置，你们也能看出来，我们正在录制这门课。如果你因为某种原因无法在这个时间段来上课，Shervine 和我会确保在今晚，也就是每周五晚上，或者周六提供录像。关于成绩，这个学季我们会安排两次考试。

### [04:47](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=287s) · b000011

一次是期中考试，会在第五次课时进行，也就是 10 月 24 日。第二次是期末考试，会在 12 月 8 日那一周举行。具体日期仍待定（TBD），之后会通知大家。好。每次讲课后，我们都会把幻灯片和录像发布到网站上。

### [05:21](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=321s) · b000012

如果你感兴趣，我们也把教学大纲放在那里了，这样你就能大致了解我们会讲哪些主题。课程教材是这本 Super Study Guide--Transformer LLMs。这里有一本，想看的话可以翻一翻。是的，我想这门课里的很多概念实际上都在书里。所以，我想它也是辅助跟上课程的一个好办法。另外，我们还为整门课制作了一个非常简短、浓缩的版本，叫 VIP cheat sheet。

### [05:58](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=358s) · b000013

如果你感兴趣，这份资料可以在 GitHub 上找到。而且，我们现在已经把它翻译成了多种语言。顺便说一下，如果里面没有你的语言，请告诉我们，我们也很乐意一起合作完成。好。我想课程安排部分就剩最后这些了。关于公告，我们会在 Canvas 上发布。如果有任何问题，当然可以联系我们。不过，Canvas 上还有一个叫 Ed 的标签页。

### [06:32](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=392s) · b000014

相信你们都很熟悉。点击它，发布你的问题，然后 Shervine 和我会回复。要联系我们的话，这里有一个邮件列表。或者，我们就两个人，直接给我们发消息就行。好。关于课程安排，目前有什么问题吗？还有一件事忘了说，因为我们在录制这门课，如果你提问，观看录像的人可能不太能听清你的问题。

### [07:08](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=428s) · b000015

所以，我会尽量重复一下你的问题。听起来可能有点奇怪，不过我会尽量记得这样做，就是这样。那么，目前关于课程安排有什么问题吗？请说。

### [07:29](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=449s) · b000016

问题是考试中是否会有编程部分。答案是没有。考试只会关注我们在课堂上讲过的概念。实际上，考试不是为了为难大家。所以，我想只要你跟着课程学习，看过幻灯片和我们讲的概念，应该就没问题。请说。

### [07:53](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=473s) · b000017

哦，是的。问题是，如果还在候补名单上，应该怎么办？我想，根据经验，很多人还会最终确定自己的课表。有些人会退课，有些不会。如果你仍在候补名单上，来找我们聊聊。不过，我很有信心这不会有问题，因为我想现在候补名单上有六个人。所以，我觉得应该没问题。好。请说。

### [08:19](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=499s) · b000018

它们会放在网站上，我们也会确保在 Canvas 上发布链接。是的，刚才的问题是幻灯片在哪里。它们在网站上。好，请说。

### [08:40](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=520s) · b000019

问题是关于考试的权重。这门课没有作业。所以期中占 50%，期末占 50%。而且没有成绩——我是说，没有权重来自那个。另外，我是说，如果这个时段和其他事情冲突，请记住我们会录制课程。所以，如果你无法来现场上课，也没关系。请说。

### [09:06](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=546s) · b000020

不好意思，你说什么？

### [09:11](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=551s) · b000021

哦，你的问题是期末考试是否只涉及课程的后半部分吗？我们还没有出试卷，但我想这确实是我们正在考虑的安排。所以，期末考试大概会考后半部分的主题。

### [09:29](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=569s) · b000022

好。总之，期中考试占 50%，期末考试占 50%。这是一门有趣的课。好，那接下来我就慢慢开始讲课了。还有一件事想提一下，每次我们讲某个内容时，你们都会看到幻灯片底部有一个来源。这主要是为了——首先，注明我们引用内容的出处；另外，如果你感兴趣，也方便你进一步深入阅读那些材料。

### [10:04](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=604s) · b000023

因为，当然，我们每周只有两个小时，总共也只有九周或 10 周，所以时间远远不足以涵盖所有内容。第二点提醒是，你们会发现这个领域充满了缩写。我刚开始时，自己也完全被这些缩写吓到了。不过，希望到课程结束时，你们脑海里能建立起一套对应关系，知道这些缩写是什么意思、分别对应什么。

### [10:36](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=636s) · b000024

所以，是的，如果到课程结束时，你们脑海里能建立起这样的对应关系，我们就知道自己做得不错了。那么，我们开始吧。我想先从非常宏观的层面讲起，因为我会假设大家是从零开始的。我们先来谈谈 NLP 的总体情况。NLP 是我们的第一个缩写。NLP 代表自然语言处理（Natural Language Processing）。

### [11:07](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=667s) · b000025

这是一个围绕文本操作展开的领域，也就是对文本进行计算。从非常宏观的层面，可以把 NLP 任务分为三类。第一类叫分类（classification）。我们以一段文本作为输入，然后想要预测某个东西。举个例子，你有一条电影评论，想预测它的情感是正面、负面还是中性。

### [11:44](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=704s) · b000026

这是一个例子。还可以做意图检测（intent detection），也就是了解一个人想做什么。假设你说，我想为明天设置一个闹钟。那么这里的意图就是设置闹钟。还可以检测语言——例如，如果你写的是 among French \[字幕疑误，可能指用法语书写\]，你想检测出这段文本是法语，还有主题建模（topic modeling）。第二类叫多重分类（multi-classification）。输入仍然是一段文本，但这一次我们要预测不止一个东西。

### [12:21](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=741s) · b000027

这一类里也有不少任务。其中一个很常见的任务叫命名实体识别（Named Entity Recognition，NER）。这个任务是说，给定一段输入文本，我们想给一些特定的词加上标签，比如识别某个内容是否是地点、时间等等。还有一些其他任务，更偏向语言学。

### [12:53](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=773s) · b000028

我想它们现在没那么热门了，但大概 10 年前，很多人会研究这些任务。例如词性标注（part of speech tagging），也就是判断哪个词是名词、动词等等；或者一些与句法分析有关的任务，比如依存句法分析（dependency parsing）或成分句法分析（constituency parsing）。最后一类是如今很热门的生成（generation）类。输入是文本，输出也还是文本。

### [13:28](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=808s) · b000029

这里的长度可以变化，也就是说，你事先不知道输出文本会有多长。这一类也有几种任务。例如机器翻译（machine translation），比如有一段英语，我想把它变成德语。问答（question answering）——典型的就是你们在用的 ChatGPT、Gemini 这些助手。你提出一个问题，然后得到回答。还有其他任务，比如摘要生成（summarization），例如你想概括一篇文章，或者只是生成一些内容。

### [14:02](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=842s) · b000030

这些内容可以是生成代码、生成一首诗，也可以是很多其他东西。

### [14:11](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=851s) · b000031

好。接下来我们会逐一看看这些任务，说明大家通常处理什么。先从第一类，也就是 classification 类开始。这里我们用情感提取（sentiment extraction）任务来说明。假设有这样一句话：“这只泰迪熊真可爱。”我们希望模型预测这表达的是正面情感。

### [14:43](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=883s) · b000032

通常，你会用情感提取数据集。我提到了电影评论，比如 IMDb 影评。但也有产品评论，比如 Amazon 评论，或者推文。现在我想它叫 X 了，所以是 X 帖子。评估这些输出时，通常会使用传统的分类指标（classification metrics）。

### [15:13](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=913s) · b000033

其中有准确率（accuracy），也就是你正确预测的观测样本占多少百分比。另外还有两个关键指标，我简单提醒一下，不确定大家是否都知道。一个是精确率（precision），也就是在所有被你预测为正类的样本中，哪些预测是正确的？第二个是召回率（recall）。在所有真实标签中，有多少被你正确预测为正类？

### [15:47](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=947s) · b000034

还有一个指标叫 F1 分数（F1 score），基本上就是取 precision 和 recall 的调和平均数，得到一个数字。现在你可能会问，为什么需要这些指标？简短的答案是，有些任务和数据集的类别非常不平衡。例如，数据集中 99% 都是正类标签，只有 1% 是负类。

### [16:20](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=980s) · b000035

在这种情况下，如果使用 accuracy 这样的指标，就可能非常具有误导性。因为如果一个模型把所有内容都预测为多数类，你就会觉得这是一个很棒的分类器，但事实并非如此。所以 precision 和 recall 才真正发挥了作用。这是第一类。现在我们来看第二类 NLP 任务，也就是 multi-classification 类。

### [16:51](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=1011s) · b000036

输入一段文本，然后预测多个东西。我们用 NER 任务来说明，正如我提到的，它要识别给定词语的类别。例如这里，我们想把泰迪熊识别为一个实体。我想，对此你会使用分类指标，但不是在句子层面，而更多是在词元（token）层面或实体类型（entity type）层面。

### [17:26](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=1046s) · b000037

我的意思是，假设有一个类别，比如地点。你想知道自己对这一类词语的预测效果如何。通常，你会据此汇总这些指标。好。

### [17:47](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=1067s) · b000038

好，来看最后一类，正如我说过的，它也是最热门的一类。这里是文本输入、文本输出。我用机器翻译任务来说明，也就是把一段文本从源语言翻译成目标语言。这里的例子是从英语翻译成法语。所以，cute teddy bear is reading，un ours en peluche mignon lit，也就是可爱的泰迪熊正在阅读。我想，这类任务更难获取数据集，因为这里需要成对的文本。

### [18:23](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=1103s) · b000039

有一个很常见的数据集叫 WMT，全称是机器翻译研讨会（Workshop on Machine Translation）。里面包含大量不同语言的成对序列。例如英语—法语、英语—德语，可以来自 European Parliament 数据集等。评估这些结果，也就是评估模型的性能，实际上要棘手得多。

### [18:55](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=1135s) · b000040

因为，你可以想象，同一个内容可以有很多不同的翻译方式。我相信在座很多人都会两种或三种语言。这就是它这么难的原因。过去，人们使用过几种基于规则的指标来评估。你们可能听过其中一个，叫 BLEU。BLEU 代表 Bilingual Evaluation Under Study \[字幕疑误，通常写作 Bilingual Evaluation Understudy\]，即双语评估替代指标。

### [19:27](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=1167s) · b000041

它衡量的是，相对于参考文本，你的翻译表现如何。ROUGE 也是类似的，不过它实际上是一组指标，用不同的方式来衡量。你们会发现机器学习社区很有趣，因为 BLEU——不知道你们是否懂法语——意思是蓝色，而 rouge 意思是红色。所以，我想他们是想给这里增添一点乐趣。

### [20:00](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=1200s) · b000042

但这些指标的问题是，你总是需要参考文本。也就是说，你基本上需要标签（labels）。实际中，获取标签的成本非常高，需要花很多时间、很多钱。课程后面我们会看到，随着我们在 LLM 领域取得进展，或者说社区在 LLM 领域取得进展，我们实际上可以不用这些基于参考文本的指标（reference-based metrics），转向更多无需参考文本的指标（reference-free metrics）。

### [20:40](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=1240s) · b000043

我们后面会讲到这一点。最后一个我想提到的、人们有时会使用的指标，叫困惑度（perplexity）。Perplexity 只看模型输出的概率，基本上是在量化模型对其输出有多惊讶。所以 BLEU 和 ROUGE 越高越好，perplexity 越低越好。

### [21:10](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=1270s) · b000044

我想，LLMs 从 2022 年起一直是热门话题。但实际上，这个领域的历史可以追溯到很久以前，远早于那一年。在 80 年代，有一类模型就已经被提出了，我们马上会看到。到了 90 年代，我们有了长短期记忆网络（Long Short-Term Memory，LSTMs），我们也很快会讲到。

### [21:41](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=1301s) · b000045

但问题在于，当时我们没有互联网，也没有很多算力。我想，这就是当时无法训练出今天这些模型的限制因素之一。再往近一些，我们取得了几项进展。Word2vec 确实是计算有意义的嵌入（embeddings）方面的先驱工作之一。我们马上会讲到它。

### [22:12](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=1332s) · b000046

接着，当然就是 Transformers，它们出自 2017 年发表的一篇论文，基本上奠定了你们今天看到的所有模型的基础。之后，这些模型的规模不断扩大，不仅算力增加了，用于训练的数据量也增加了。于是就有了 LLMs 这个称呼。我想，这更多是 2020 年代的事情。不过，是的，我们会讲到这些。

### [22:46](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=1366s) · b000047

好。关于这个宏观介绍，有什么问题吗？大家都没问题？好。那么，我想我们要问自己的第一个问题是：我们想要一个能处理文本的模型。但模型理解的是数字，它们并不真正理解文本。所以，我们需要对文本做一些处理，让它更可量化，变成模型能理解的东西。

### [23:23](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=1403s) · b000048

例如，看这样一句话：“a cute teddy bear is reading”。首先你得问自己，怎样切分这个句子，才能把它传给模型？这个过程叫词元化（tokenization）。它基本上是按照某种任意选定的文本单位来切分文本。做这件事有几种方式。

### [23:54](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=1434s) · b000049

我想，第一种方式是完全任意地切分。例如这里，你可以有“a”，它是一个文本单位。“Cute”可以是另一个文本单位。“Teddy bear”又是一个，依此类推。顺便说一下，这种文本单位叫 token，所以这个方法才叫 tokenization。

### [24:19](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=1459s) · b000050

另一种方式就是按词切分。

### [24:25](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=1465s) · b000051

但我想，始终都会有优点和缺点。我们希望实现的一个目标，是之后能以有意义的方式表示这些 tokens。按词级别处理的一个缺点是，你会得到一些看起来很相似、但实际上被当作不同 tokens 的词。我想这里的局限在于，你需要为这些相似却不同的 tokens 计算 embeddings，并设法让它们的 embeddings 相似。

### [25:07](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=1507s) · b000052

我举个例子。假设有一个词“bear”，然后还有另一个词，也就是复数形式“bears”。这两个词非常相似，只是一个是单数，另一个是复数。如果采用词级别的 tokenization，最终就会得到两个不同的实体，基本上它们只被看作是不同的。“run”和“runs”这样的动词变化也是一样。

### [25:42](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=1542s) · b000053

因此，人们深入研究了一类称为子词分词器（subword tokenizers）的工具，它们利用词根，寻找这些词里有哪些共同的词根。例如，对于 bear 和 bears，它们会共享 bear 这个部分。

### [26:12](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=1572s) · b000054

所以，我想优点是你可以利用词根。但缺点是序列会变得更长。我们会看到为什么这是缺点。我想后面会讲，不过可以先透露一下。这些模型的复杂度也取决于序列长度。因此，需要处理的 tokens 越多，模型运行所需的时间就越长，因为它基本上要处理所有这些 tokens。

### [26:52](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=1612s) · b000055

这是一个缺点。所以，优点是利用了词根，缺点是会使序列变长。

### [27:05](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=1625s) · b000056

还有最后一类 tokenization 方式，就是按字符级别处理，把字符一个个拆出来。这里，我想，你我写消息时通常有时会拼错单词。而用 subword 方式进行 tokenization 时，可能无法识别这个拼错的词。

### [27:36](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=1656s) · b000057

我想，字符级分词器（character-level tokenizer）可以考虑到这种情况。但这里的问题是，序列长度会长得多得多，使模型处理序列花费更多时间。这是一个缺点。另一个缺点是，当你想表示每一个 token 时，我想，很难知道一个字母的表示究竟意味着什么。

### [28:08](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=1688s) · b000058

例如，字母 U 的表示意味着什么？这很难。好。这里快速回顾一下。词级别（word-level）是一种非常朴素、非常简单的方式，把文本划分成任意单位。但问题是，正如我们说过的，没有利用词根。另外，我之前没提到，还有一个术语。

### [28:41](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=1721s) · b000059

每当你切分文本，之后在推理时（inference time）想要做预测，我想有一个前提：这个 token 必须是在训练时见过的，你的训练集里必须有它。问题是，假设在 inference time，你把文本切成词，然后假设其中有一个词是训练时没见过的。

### [29:12](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=1752s) · b000060

你就需要把它标记为未知。这种情况叫词表外（Out Of Vocabulary，OOV）。幸运的是，subword-level tokenizer 可以缓解这个问题。OOV 的风险会更低，但仍然可能出现。正如我们提到的，它的优点是利用了词根。

### [29:41](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=1781s) · b000061

然后是字符级别（character-level），它对拼写错误和大小写错误具有鲁棒性（robustness）。但问题是，它会让计算慢得多。序列会变得非常、非常长，这也会让推理耗时高很多。这样可以吗？我想，这确实是基础，也就是如何处理文本。不过，是的，总体上能理解吗？

### [30:13](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=1813s) · b000062

好。现在，我们取了一段输入文本，把它切分成了若干部分，也就是 tokens。为了让模型理解这些 tokens，我们需要为每一个 token 找到一种表示。接下来我们看看这个。这叫词表示（word representation）。或者，更准确地说，应该叫词元表示（token representation）。

### [30:45](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=1845s) · b000063

所以，我们想找到一种方式来表示每一个 token。

### [30:52](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=1852s) · b000064

一个简单、朴素的做法，是为每个词或每个 token 分配一个独热向量（one-hot vector）。例如，假设词表里有三个 tokens——book、soft 和 teddy bears。比如说，soft 对应向量 1, 0, 0；Teddy bear 对应向量 0, 1, 0；book 对应向量 0, 0, 1。

### [31:25](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=1885s) · b000065

这叫独热编码（One-Hot Encoding，OHE），我们经常会看到。好，这是一种表示 tokens 的方法。但人们基本上想做的是比较这些 tokens，看看哪些与哪些更相似。人们常用的一种相似度度量叫余弦相似度（cosine similarity）。

### [31:56](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=1916s) · b000066

不知道你们是否听说过。可以把它理解为看这些向量在 n 维空间里形成什么夹角。如果它们指向同一个方向，那么它们可能相似。如果它们正交，可能就彼此独立。如果它们完全相反，那么它们可能就是相反的。这基本上就是我们想采用的理解方式。

### [32:28](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=1948s) · b000067

问题在于，如果用 one-hot 的方式表示 tokens，最终所有向量都会彼此正交。这就是问题所在。理想情况下，我们希望含义相同或相似的 tokens 具有较高的相似度；而不相似、谈论不同事物的 tokens，则更接近正交。

### [33:03](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=1983s) · b000068

这里只是为了举例，泰迪熊是柔软的。所以，你希望 teddy bear 和 soft 有较高的相似度。假设 teddy bear 和 book 彼此独立，那么你希望它们的相似度更接近 0。这就是你想要的。这是使用 one-hot encoding 得到的结果，而这是你想要的结果。请说。

### [33:31](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=2011s) · b000069

不好意思，你说什么？

### [33:38](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=2018s) · b000070

哦，明白了。问题是，为什么要关心范数（norm）？我想，cosine similarity 实际上是用 norms 做了归一化的。所以它是点积（dot product）。哦，你是说，为什么我这里只写了 dot product，而不是 2？

### [34:01](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=2041s) · b000071

哦，明白了。你的问题是，为什么我们不关心 norm？好，我想观众现在知道问题了。我想，这些度量都是度量，都是试图刻画相似性的方式。所以，为什么不关心 norm 呢？

### [34:25](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=2065s) · b000072

我想，这是人们尝试量化相似性的一种方式。你需要看向量是如何训练的，以及 norm 是否能反映什么信息。我想，我能给出的最好答案是，这是一种度量，并不是完美的度量。人们也可能把 dot product 用作度量。不过，是的，我没有一个特别好的答案。但只要能捕捉到这些向量指向什么方向，我想，通常你关心的就是它们之间的夹角。

### [35:03](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=2103s) · b000073

不过，通常不会真正把 norm 考虑进去。

### [35:10](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=2110s) · b000074

好，有什么问题吗？还有其他问题吗？请说，请说，请说，请说。

### [35:39](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=2139s) · b000075

这是个很好的问题。问题是关于词表（vocabulary）的大小，以及它如何影响 word、subword 的选择，还有这种选择在不同语言中如何变化。好问题。我会说，首先这确实取决于你想完成的任务。如果任务只涉及一种语言，那就只用那种语言。通常会选择 subword tokenizer，原因就是我们刚才提到的那些。我想，subwords 是一种不错的折中：既能通过词根识别单词，利用这一点，又能减少遇到 OOV 的风险。

### [36:23](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=2183s) · b000076

关于大小，我知道人们尝试过不同方案。我想，一般对英语来说，目标词表大小是几万这个数量级。但如今的模型是多语言的，也涉及代码。所以你会看到，现在的词表大小有时是几十万这个数量级。说到中文，我想，你使用的字符会有所不同。

### [37:00](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=2220s) · b000077

对于拉丁字母，我想，就是我们都熟悉的那套字母表。当然，其他语言也会有类似的东西，不过用的是目标语言的字符。所以，我会说，数量级上，一种语言是几万，多语言则是几十万。这些就是你要考虑的数量级。

### [37:28](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=2248s) · b000078

好，请说。

### [37:41](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=2261s) · b000079

好问题。问题是，如何得到这些 embeddings？实际上这就是下一张幻灯片的内容，我接下来会讲。好，很好。既然我们知道 one-hot encoding 不是表示 tokens 的好方法，那么我们想做的就是从数据中学习这些 embeddings。我之前提到，2010 年代有一篇论文——我想是 2013 年——叫 Word2vec。

### [38:15](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=2295s) · b000080

它之所以这么受欢迎，是因为它们展示了一种非常直观、可解释的方式来理解这些 embeddings。他们会说，king 之于 queen，就像这个之于那个；比如 Paris 之于 France，就像 Berlin 之于 Germany。也就是说，有了一种能理解 embeddings 含义的方法。那么问题来了，他们是怎么做到的？他们有两种计算这些 embeddings 的方式。

### [38:47](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=2327s) · b000081

一种叫连续词袋（continuous bag of words），另一种叫跳元模型（skip gram）。不过，它们都依赖同一个思路：利用现有文本，然后根据上下文之类的信息，预测文本中的某个部分。例如 continuous bag of words，它的目标是考虑给定目标词周围的词。

### [39:20](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=2360s) · b000082

然后预测那个目标词。而 skip gram 正好相反，从一个目标词出发，预测它周围的词。我想，这种任务通常叫代理任务（proxy task）。因为归根结底，在这个练习中，我们关心的不一定是预测下一个词，至少暂时不是。我们的目标是学习这些词的有意义的表示。

### [39:56](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=2396s) · b000083

这里的想法是，如果一个模型以某种方式知道如何预测，比如下一个词，那么说明它对语言如何运作有一定理解，而这基本上就是我们想要的。我们想要一种能反映语言本身的 embedding，比如 king 和 queen，或者类似的，Paris 和 France，这是首都。

### [40:32](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=2432s) · b000084

你希望这些关联被嵌入到表示当中。

### [40:39](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=2439s) · b000085

我们来看一个非常简单的例子，看看它是什么样的。在这个例子中，假设 proxy task 是预测下一个词。我们采用一个非常基础的神经网络模型（vanilla neural network model），它接收一个大小为 v 的向量，通过乘法和一个偏置项（bias term）得到隐藏状态（hidden state），然后再经过一组乘法，得到最终向量。

### [41:23](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=2483s) · b000086

这里基本上是一个非常简单的神经网络。输入大小是 v，隐藏层（hidden layer）大小是 d，通常远小于词表大小。词表通常有几万或者几十万个词。而 d 通常是几百，比如 768 就是一个维度的例子。所以它要小得多得多。我们想做的就是通过这个 proxy task 来学习词表示。

### [41:59](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=2519s) · b000087

我们会尝试把词作为输入，并预测下一个词。

### [42:12](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=2532s) · b000088

先看序列中的第一个词。顺便说一下，我会交替使用 token 和词这两个说法。假设有一个词“a”，我们想预测下一个词，也就是“cute”。做法是取出词“a”的 one-hot encoding 表示，然后把它传入网络。如果你熟悉神经网络，这里就是一个矩阵与这个向量相乘。

### [42:51](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=2571s) · b000089

于是得到一个 hidden state 表示，它是大小为 d 的向量。这里假设它是 0.2 和 0.9，所以 D 等于 2。然后这里再进行一次传递。经过 softmax 后，你会得到一组概率，用来判断下一个词是什么。在这个例子中，词表大小是 6。

### [43:24](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=2604s) · b000090

第一个词的预测概率是 0.2，第二个词是 0.4，其他词在这个例子中都是 0.1。假设我们想设法最大化预测为词表中第二个词的概率，也就是那个 0.4。我们基本上会把预测结果与 0, 1, 0, 0, 0 进行比较，它就是词表中第二个词的表示。

### [44:01](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=2641s) · b000091

然后进行反向传播（back prop），更新权重（weights）。不知道大家是否都熟悉这部分。这里的思路是，得到预测后，计算损失（loss），通常使用交叉熵（cross-entropy），用来确定预测与真实答案相差多远。再根据这个差距更新 weights，使预测更接近真实值。

### [44:36](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=2676s) · b000092

这就是做法。然后重复这个过程。假设取词“cute”，正如我们说的，它是词表中的第二个词。所以它的 one-hot encoding 表示是 0, 1, 0, 0, 0。让它通过网络，得到一个 hidden state，比如向量是 0.8 和 0.4。再做一次。你想预测下一个 token，这里就是 teddy bear。

### [45:08](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=2708s) · b000093

你会看到，在这个例子中，模型目前对下一个词给出的是均匀概率，但你想设法最大化 teddy bear 的概率。于是，对所有词反复做这件事。最终，你得到一个学会了预测下一个词的模型，这基本上就是 proxy task。接下来，你要取出模型学到的表示，也就是绿色的那些单元。

### [45:43](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=2743s) · b000094

这样一来，每当有一个词，你就把它表示成 one-hot encoding 形式，再与这些 weights 相乘，就能得到绿色的表示。那就是你的词表示。

### [46:09](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=2769s) · b000095

这样能理解吗？请说，请说。

### [46:33](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=2793s) · b000096

是的，好问题，好问题。问题是 v 对应什么，以及为什么这里只有六个。是的，在这个例子里只有六个可能的词，也就是词表大小。这只是一个非常简单的玩具示例，因为实际中会多得多。我想，这是语言的挑战之一。理论上，词可以有很多变化形式，所以如果按 word-level 的方式把文本划分成 tokens，词表可能会变得非常大，因为你需要考虑给定词的所有变化形式。

### [47:15](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=2835s) · b000097

我还想指出另一点。假设词表大小是 6，这六个词就是训练时见过的词。但如果在 inference time 出现了一个训练时没见过的词，会怎样？通常，人们的做法是预留一个位置，放所谓的未知词元（unknown token）或词表外词元（out-of-vocabulary token）。你基本上可以把它看成一个桶，用来收纳所有无法识别的东西。

### [47:55](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=2875s) · b000098

所以，假设在 inference time 有无法识别的 token，它们都会采用同一种表示，也就是 unknown token 的表示。顺便说一下，我想这也是 word-level tokenizer 的一个难点，因为它遇到 out-of-vocabulary tokens 的概率会大得多。Subword level 的概率更低。而 character level，我想就没有这个问题。

### [48:28](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=2908s) · b000099

这回答你的问题了吗？是的。好，请说。

### [48:53](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=2933s) · b000100

很好，很好的问题。第一个问题是，什么时候算完成？关于 proxy task，在训练模型时，真正的目标并不是学习——我是说，在这个例子里——如何预测下一个词。你的目标是得到有意义的表示。不过，你可以跟踪所做 proxy task 的损失函数（loss function），同时也要考虑到，这不一定是你的最终目标。

### [49:24](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=2964s) · b000101

我想，一个非常合理的做法就是等模型收敛（converge）。这里，你要跟踪 loss 随着——这里有个术语叫训练轮次（epoch），也就是模型看过训练集多少遍——的变化。然后比较这些不同的曲线。当它收敛时，通常就是停止训练过程、看看结果是否合理的一个好时机。

### [49:54](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=2994s) · b000102

当然，这取决于你的下游任务（downstream task）。这是第一个问题。那么你的第二个问题——不好意思，能重复一下第二个问题吗？是的，是的，哦，好问题。问题是，如何知道生成什么时候停止？否则，我想它就永远不会停。

### [50:26](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=3026s) · b000103

是的，没错。所以会有一些特殊词元（special tokens）。通常，有序列结束（end of sequence），序列结束。一般来说，当生成了 end of sequence token 时，就会停止。

### [50:40](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=3040s) · b000104

好。那么第二个问题是，什么决定了 hidden layer 的大小？我会说，这是一个权衡，因为你希望 embedding 足够丰富，能够为 downstream task 提供有用信息。例如，假设你想得到句子的 embedding，并想做一个非常、非常专门的任务，可能会有很多不同的结果，那么你可能希望向量能体现这些信息，所以可能需要更大的向量。但如果任务非常简单，也许更小的向量就合理了。

### [51:22](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=3082s) · b000105

我想，隐藏维度（hidden dimension）的大小也会影响后续运行内容的复杂度。因为当然，向量越长，计算量就越大，推理（inference）的成本可能也会更高，等等。所以有很多因素。简单回顾一下：第一，下游任务有多复杂；第二，你对延迟（latency）、成本这些因素有多敏感。

### [51:52](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=3112s) · b000106

所以，这确实是一种权衡。不过，通常会看到几百或几千维的 embeddings。当然，这些模型一直在变大，所以这个数字可能会变化。但这就是你要考虑的数量级。

### [52:11](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=3131s) · b000107

对，这确实是经验性的。是的，是的。我想，你也可以参考别人得出的结果，以此作为起点。不过，768 这样的数字是人们通常会选的。

### [52:27](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=3147s) · b000108

好，请说。

### [52:47](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=3167s) · b000109

好问题。问题是，如何区分拼写相同但出现在不同上下文中的词？你已经想到我前面去了。这里讲的基本上还是基础。接下来，我们会介绍一些能够处理这些问题的方法，也就是在句子中根据上下文理解词语。是的，我们稍后会讲到。

### [53:14](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=3194s) · b000110

好。

### [53:17](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=3197s) · b000111

我没跟上时间安排，所以接下来得加快一点。好，刚才我们看了如何学习 tokens 的表示。但你可能也想得到句子或一段文本的表示。利用我们刚才看到的内容，一个非常朴素的做法是对词，比如说词表示，取平均值。

### [53:53](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=3233s) · b000112

但问题是，你会丢失很多含义，丢失顺序，丢失——而且，我想你刚才指出得很好，学到的表示是每个 token 固定对应的，不管它出现在什么位置。因此，有一类模型旨在捕捉文本呈现出来的序列特性。我们要讲循环神经网络（Recurrent Neural Network，RNNs）。

### [54:26](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=3266s) · b000113

RNNs 的做法是，不再只是一次处理一个词，而是保留到目前为止句子的隐藏表示（hidden representation），并且一次考虑一个 token。正如前面提到的，这种技术其实很早就提出了，在 80 年代。这种模型会把词或 tokens 出现的顺序考虑进去。

### [55:05](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=3305s) · b000114

在这个例子中，从句子的最开头开始处理。有一些占位的 hidden states，叫 A，通常记作 A 或 H。它被称为隐藏状态（hidden state）、激活（activation），有时也叫上下文向量（context vector）。然后，有一个模块会同时考虑到目前为止的 hidden state，以及时间步（time step）t 上的词，这里是 time step 1。

### [55:41](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=3341s) · b000115

这里，它接收句子到目前为止的含义，并考虑当前出现的词。然后生成一个输出向量，在这里可以用来尝试预测下一个词。例如，这里有这个 hidden state 和词表示，然后在这个蓝色方框里进行一些矩阵乘法。

### [56:12](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=3372s) · b000116

你会得到一个输出向量，并尝试通过预测后面的词来训练它。接着，持续跟踪这些 hidden states，继续这样做。于是不断重复这个过程。我想，可以把这些 hidden states 理解为对截至目前已处理序列的一种表示。

### [56:49](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=3409s) · b000117

所以，RNNs 的好处在于，词序现在起作用了。而且你能以更自然的方式对句子进行编码。

### [57:04](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=3424s) · b000118

我们大致看看它如何运作。还是我们最喜欢的那个例子，cute teddy bear is reading。这里有 token A。你需要一个 one-hot encoding 向量，将它传入网络，计算 hidden state，尝试预测 cute。但接下来会保留 hidden state，再把它输入另一个模块。然后，还会考虑接下来的词。

### [57:37](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=3457s) · b000119

所以，你考虑的不仅是词本身，还有句子到目前为止的 hidden state。然后再次预测下一个词，一遍又一遍。

### [57:51](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=3471s) · b000120

这就是 RNN。

### [57:54](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=3474s) · b000121

所以，循环神经网络（RNNs）被用于很多任务，我们可以把它们对应到之前看到的那些类别。对于分类（classification），基本上可以使用句子中最后一个词的隐藏状态（hidden state）。例如，如果你想预测一条评论的情感，基本上就会取这里最后一个向量，尝试把它投影到你想预测的结果或标签所在的空间。

### [58:28](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=3508s) · b000122

例如，如果你想判断正面还是负面，基本上就是把那个向量投影到那个空间。你可以在这里这样做。对于多分类（multi-classification），基本上就是取得你关注的词元（token）的表示，然后将它投影。或者，对于生成（generation），基本上会处理整个源文本，然后在处理结束时得到一个上下文向量（context vector），也叫激活向量（activation vector），也叫 hidden state，随后用它来解码输出预测。

### [59:09](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=3549s) · b000123

这就是你在这些任务中使用 RNN 的方式。如今你不太听说 RNNs，是因为它们虽然有一些优点，但缺点很多。其中一个缺点是，句子的含义基本上完全封装在这个 hidden state 中。

### [59:39](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=3579s) · b000124

所以就有了长距离依赖（long-range dependencies）的问题，它基本上会影响你用引号括起来的“记住”模型过去看到的内容的能力。因此，有另一类模型尝试在 RNNs 的基础上进行改进。这一类叫作 LSTMs，即长短期记忆（Long Short-Term Memory）。这种扩展的目标是，在我们刚才讨论的 hidden state 之外，设法持续记录那些用引号括起来的、值得记住的“重要”内容。

### [1:00:20](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=3620s) · b000125

这里有 a of t，也就是你的激活（activation），基本上把截至目前的序列编码在其中。然后还有另一个需要跟踪的量，叫作细胞状态（cell state），这里用 c 表示。这种架构旨在改善这一部分，但我想它也并不完美。对，所以这就是基于 RNN 的方法的主要问题：它们会忘记过去的内容。

### [1:01:01](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=3661s) · b000126

你会在文献中看到，这种现象叫作梯度消失（vanishing gradient）。至于为什么这样命名——我知道时间快不够了，不过我还是解释一下这一部分。为了预测，比如说，最后几个词，你基本上依赖于它之前的每一个 hidden state。

### [1:01:30](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=3690s) · b000127

到这里都明白吗？所以，每当你想更新模型的权重，让这里的预测与实际预测相匹配时，在进行反向传播（back propagation）时，你就需要以某种方式考虑到，这里的值基本上不仅取决于这次计算，还取决于这次计算或这次计算，它们基本上都是按顺序发生的。

### [1:02:03](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=3723s) · b000128

所以就出现了这种，我想可以说是，尝试随时间进行反向传播的情况。但问题是，实际把它写出来时——这是一个很难看的公式。不过写出来之后，它最终会变成一连串量的乘积，这些量可能——如果它大于 1，就会爆炸；如果小于 1，就会消失。

### [1:02:34](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=3754s) · b000129

因为如果你把很多小于 1 的东西相乘，结果就会趋近于 0。所以我想，如果你试图更新的某个东西趋近于 0，基本上就很难进行更新。这就是一个宏观上的直观解释。这不是这门课的重点，所以我不会详细讲解这些难看的公式。但我希望你们能理解，由于这种，我想可以说是，顺序性的特点，它并不擅长记住过去的内容。

### [1:03:10](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=3790s) · b000130

这样说能理解吗？好，希望接下来的内容会更容易理解一些。不过在那之前，我先回顾一下我们讲过的内容。我们的目标是表示文本。所以我们首先从表示单词或 token 开始，这就是我们尝试用 Word2vec 做的事情。我们看到，利用代理任务（proxy tasks）来学习这种表示是一个很好的方法。但它有很多局限。

### [1:03:42](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=3822s) · b000131

其中一个是你们提到的，它无法感知上下文。而且词序也不起作用。因此，就有了另一类能够把这些词考虑进去的方法，但当序列变得很长时，它们就不太能持续跟踪其中的内容。于是就出现了梯度消失或长距离依赖的问题。

### [1:04:12](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=3852s) · b000132

所以，每当你看到这个术语时，基本上就是指这个。还有一点我没提到，就是计算非常慢。训练这些模型时，为了预测这个词，基本上需要先计算前面的所有 hidden states。所以，当序列变得很长时，就会花费很长时间。

### [1:04:46](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=3886s) · b000133

所以，出于所有这些原因，或者我想是出于什么原因。也就是，因为模型难以记住过去的内容，人们尝试在某个东西与过去的东西之间建立更直接的连接，这就是注意力（attention）背后的想法。attention 所做的，就是尝试在我们要预测的内容与过去的某个内容之间建立直接联系。

### [1:05:26](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=3926s) · b000134

在这个例子中，假设我想把一个英语句子翻译成法语句子。这里，我想输入句子已经给出了。我在计算 hidden state，一次处理一个词。这就是传统的 RNN。所以，“一只可爱的泰迪熊正在阅读”。这里我有一个 hidden state，然后对它进行解码。你可以想象，当我想生成译文中的下一个词时，如果我知道自己要预测哪个词，那就太好了。

### [1:06:07](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=3967s) · b000135

或者换句话说，如果我能看一眼输入文本的某个区域，那就太好了。所以 attention 背后的想法，是在你试图预测的内容与之前的内容之间建立直接联系。这就是 attention 背后的想法。它是在 2014 年提出的。对，再说一次，这是为了尝试解决这些长距离依赖问题。

### [1:06:42](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=4002s) · b000136

对，在这个例子中，我们就想这样做。而且，这个概念实际上会是这门课的关键。因为我们会看到，注意力机制（attention mechanism）会让一切——我是说，大多数东西——运作起来。这其实也是 transformer 论文所依赖的主要原理。transformer 是我们在这门课中将看到的核心架构，它是在 2017 年这篇名为 Attention is All You Need 的论文中提出的。

### [1:07:22](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=4042s) · b000137

所以，光从标题就能看出，作者希望只依靠这一部分。作者尝试摆脱这种按顺序处理文本的方式，转而让模型同时与文本的所有部分直接连接。这就叫作自注意力（self-attention）。他们在翻译任务上进行了尝试。

### [1:07:55](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=4075s) · b000138

他们发现效果很好。回到我们一直在用的例子，一只可爱的泰迪熊正在阅读。这里我们的说法是，为了计算 teddy bear 这个 token 的表示，我们会同时查看序列中的所有其他 token，并通过直接连接来直接查看它们。

### [1:08:27](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=4107s) · b000139

我想，回到你的问题——这里 teddy bear 的表示，会是它所处上下文特有的表示。再回到你关于 riverbank（河岸）和 robbing a bank（抢银行）的问题，这里的 bank 就会有不同的表示。这就是这个想法。我想，这个大致思路能理解吗？

### [1:08:55](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=4135s) · b000140

再说一次，这叫作 self-attention 机制。Afshine，我时间用得怎么样？8。我还有 8？好，太好了。好，这就是基本想法。现在我要介绍另一组概念，更多是术语，但会非常重要。当你想用其他东西来表示某个东西时，我们使用“查询（query）”“键（key）”和“值（value）”这几个词，也就是 Q、K 和 V。

### [1:09:30](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=4170s) · b000141

在这个例子中，我们的目标是弄清楚 query teddy bear 与哪些其他 token 更相似。所以这里的问题是，好，你有一个 query，你想看看哪些其他 token 最相似。你要做的就是查看所有其他 token，它们基本上由 keys 和 values 组成。

### [1:10:03](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=4203s) · b000142

所以，我们会比较 query 和 key，量化 query 与某个给定 key 的相似程度，然后取对应的 value。我们会在这个例子中看到，假设你想用其他所有内容来表示 teddy bear。你要做的是取 query teddy bear，将这个 query 与所有其他 keys 比较，看看哪个元素最相似，然后为更相似的那些赋予权重，并取它们关联的 value。

### [1:10:41](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=4241s) · b000143

这就是这些东西如何运作的一个非常宏观的想法。当然，我们会具体看它们如何工作。不过总体思路就是这样。

### [1:10:55](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=4255s) · b000144

好，太好了。说到 query、key 和 value，我们还会看到，用这种方式表达有一个好处，就是可以把整个序列上的 self-attention 计算表示成矩阵形式。而图形处理器（GPUs）很喜欢矩阵。所以它确实很适合我们现有的硬件。我想，我这里提到的内容可以表示为对 query 和 key 做 softmax 的形式，基本上就是获得某种权重，用来表示哪些 values 更重要。

### [1:11:40](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=4300s) · b000145

例如，如果某个 value 更重要，它就有更大的权重。另一个没那么重要，就会有较小的权重。然后基本上就是把它乘以 value。不用担心，我们后面会有详细的例子。如果现在仍然觉得很宏观、很模糊，不用担心。我们会详细走一遍。对，这就是它的工作方式。好，太好了。

### [1:12:11](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=4331s) · b000146

关于什么是 self-attention，有什么问题吗？请说。

### [1:12:40](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=4360s) · b000147

很好，很好的问题。问题是，什么是 value，什么是 key？我想，也就是如何得到它们？它们是什么意思？首先，我想说，这些量是学习出来的，不是固定设定的。不过从解释的角度，你可以把 key 理解为用来判断哪一个与 query 最相似的东西。而 value 是与那个元素关联的实际值。所以这里，你会有这样的情况：你想用所有 values 来表示这个东西。

### [1:13:18](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=4398s) · b000148

所以，加权平均（weighted average）中的权重，基本上就是——基本上就是——query 与 key 之间的点积（dot product）。而 value 则是你实际使用的向量。但再说一次，这些东西是学习出来的。还有一点我没有提到，但你说得对，我们实际上会通过投影（projections）来获得这些量。而这些投影实际上是由模型学习的。

### [1:13:48](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=4428s) · b000149

这样可以吗？好，太好了。那么，我们还有 15 分钟来讨论架构，对吧？好，从非常宏观的角度来看，为了实现 self-attention 机制，作者提出了一种由两部分组成的架构：左边的编码器（encoder），以及右边的解码器（decoder）。

### [1:14:26](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=4466s) · b000150

他们的应用是翻译。通过 encoder 的，是源语言的输入文本。通过 decoder 的，是你正在预测的目标语言。总体思路是，把输入文本送入 encoder，计算出有意义的嵌入（embeddings）。

### [1:14:57](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=4497s) · b000151

你希望应用 self-attention 机制，也就是说，你希望把每个 token 的表示计算为其他 token 的函数。为此，你会使用一个叫作注意力层（attention layer）的层。具体来说，是多头注意力层（multi-head attention layer），不过 multi-head 只是以不同方式进行这种计算，让模型能够学习不同的表示或不同的投影。这里的思路是，你把输入文本输入进去，输入文本中的所有 token 都会相互关注。

### [1:15:40](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=4540s) · b000152

例如，一只可爱的泰迪熊正在阅读，你基本上会把这段文本中所有 token 的表示计算为其他 token 的函数。你会通过 encoder 来做这件事，也就是这里的 multi-head attention。然后还有一个前馈层（feedforward layer），只是为了让模型学习另一种投影。在编码过程结束时，你会得到输入句子中各个 token 的丰富表示。

### [1:16:19](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=4579s) · b000153

到这里都明白吗？但现在你的目标是实际翻译输入句子。因此，你要做的是从，比如说，句子起始 token 开始翻译，也就是你的第一个 token。然后，你会使用输入句子中的所有表示，来确定接下来预测什么。

### [1:16:50](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=4610s) · b000154

我刚才说的就是交叉注意力层（cross-attention layer），也就是第二个，这一个，它基本上——我不确定你们是否能看到箭头，不过有两个箭头来自 encoder，一个箭头来自 decoder。谁能告诉我，来自 decoder 的箭头表示什么？decoder 是 query、key 还是 value？

### [1:17:22](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=4642s) · b000155

我想有 1 over 3，也就是 33% 的概率。谁想试试？是 key 吗？好。

### [1:17:35](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=4655s) · b000156

query？好。你可以这样理解：你在问自己，输入中的哪些词是重要的，对吧？所以，基本上，你想知道，给定你的 query，输入中的哪些元素是重要的？这里这个箭头确实是 query，因为这就是你想弄清楚的东西。而 keys 和 values 实际上来自 encoder，基本上也就是来自输入序列。

### [1:18:14](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=4694s) · b000157

然后还有另一个 attention layer，也就是这个。这个层试图弄清楚，你正在解码的输出句子中，还有哪些 token 有助于预测下一个 token。假设你开始解码，得到 un ours en peluche，这是法语。为了预测下一个词，你基本上想弄清楚，到目前为止已经翻译出来的哪些 token 有助于预测下一个词。

### [1:18:51](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=4731s) · b000158

这就是这个 attention layer 的作用。它被称为掩码的（masked），因为它只查看截至目前已经翻译出来的 token。它不会查看尚未翻译出来的 token，因为它们当然还没有被翻译出来。所以没有办法，比如说，去看你正在尝试预测的 token 右侧的内容。

### [1:19:15](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=4755s) · b000159

很好。所以，从非常宏观的角度来看，你有这种 attention layer，它既存在于 encoder 中，也存在于 decoder 中，但它有几种，我想可以说是，用途。这里的 attention layer 旨在根据输入句子本身来计算它的 embeddings。然后是 decoder 中的那些层，第一个是掩码自注意力层（masked self-attention layer），旨在将某个东西表示为截至目前已解码的所有内容的函数。

### [1:19:56](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=4796s) · b000160

第二个是 cross-attention layer，它尝试根据输入中已经看到的内容来表示这些东西。这里，因为你与不同 token 之间都有直接连接，所以并没有这种顺序感。在 RNN 中，你基本上是一次表示一个东西，因此会有某种词序信息。但这里没有，因为它就像直接连接。这就是为什么需要位置编码（position encodings），它们用来提供词在序列中的位置信息。

### [1:20:40](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=4840s) · b000161

今天我们不会深入讨论这一点，不过我想特别指出它。所以，从非常宏观的角度来看——我们会在详细示例中看到——为了把一个句子从源语言翻译成目标语言，我们首先会对文本进行词元化（tokenize），也就是把它划分为任意单位。我们会为这些 token 学习 embedding。这就是输入嵌入（input embedding）的作用。然后我们会添加一些与位置有关的编码。

### [1:21:14](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=4874s) · b000162

今天不会讨论它，不过知道这一点就好。然后我们经过 encoder。encoder 尝试弄清楚，如何把某些东西表示为输入中其他东西的函数。它在 multi-head attention layer 中完成这件事。然后经过一个前馈神经网络（feedforward neural network），这只是一种投影向量的方法，让模型多一些学习的自由度。

### [1:21:48](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=4908s) · b000163

一旦得到输入的这些表示，你就开始翻译。从句子起始词元（BOS token）开始。你要做的是弄清楚下一个词是什么。所以你会看，好，目前已经翻译出来的哪些词对翻译有帮助。这就是掩码多头注意力层（masked multi-head attention layer）所做的。然后还有另一个 attention layer，用来把这些东西表示为输入内容的函数，也就是那里的 cross-attention layer。

### [1:22:27](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=4947s) · b000164

然后还有一个 feedforward neural network，同样是为了增加一些自由度。最终，你得到一个向量，再让它经过 softmax。这就是用来猜测下一个词的一种方式。你会得到一个大小等于词表大小的向量，然后利用这些值来确定下一个词。

### [1:22:58](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=4978s) · b000165

很简单，对吧？关于这个有什么问题吗？请说。

### [1:23:09](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=4989s) · b000166

好，这是个很好的问题。问题是，头（head）是什么意思？我想我讲得太快了，略过了这一部分。不过，在进行 self-attention 计算时，基本上是让 queries 与 keys 交互，然后取对应的 value。但你完全可以重复做几次。所以，“head”这个术语指的是你用来获得 query、key 和 value 的那些投影矩阵。

### [1:23:46](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=5026s) · b000167

当你有多个 heads 时，你就是在允许模型学习不同的投影。所以，这基本上为模型提供了额外的自由度，让它学习向量之间不同的关联。这是个很好的问题。通常会用小写 h 表示 heads 的数量。这就是它所对应的含义。这样回答了你的问题吗？

### [1:24:16](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=5056s) · b000168

很好，非常好。

### [1:24:23](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=5063s) · b000169

好，我们还有很多内容要讨论，不过我这里其实有一张讲这个的幻灯片。这就是你提到的 multi-heads。我们基本上是在并行运行多次 self-attention 计算，同样，使用模型学习到的不同投影矩阵。如果你有计算机视觉（computer vision）背景，这类似于在卷积（convolution）中使用多个滤波器（filters）。所以是同样的想法，不过这里有所不同。

### [1:24:58](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=5098s) · b000170

对，很好的问题。问题是，这些投影不同吗？通常我们不会施加约束，只是让模型自己学习。但在实践中，它往往会学到表达同一件事的不同方式。所以对，通常没有约束。当然，也有论文深入研究，如果改变这一点会怎么样。

### [1:25:28](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=5128s) · b000171

但通常不会有任何约束。

### [1:25:34](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=5134s) · b000172

很好，太好了。好，我再提一个技巧，transformer 作者使用的另一个技巧。它叫作标签平滑（label smoothing）。谁听说过 label smoothing？这里一个新的点是，在自然语言处理（NLP）中，当你想预测接下来是什么时，通常不止一种可能。

### [1:26:06](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=5166s) · b000173

当你说，多么美好的一天、多么精彩的一堂课、多么棒的一本书、多么棒的——总会有多种选择。填补这个空缺的方式不止一种。所以 label smoothing 是一种尝试从直觉上处理这个问题的技术。它的做法不是说，预测这个词，100% 就是这个词，没有其他词；而是说，预测这个词，但也有可能不是这个词。

### [1:26:40](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=5200s) · b000174

在实践中，它会取独热编码（one-hot encoding）。它不会说你需要预测的是 1, 0, 0, 0，而是说，实际上你要预测的是 1 减 epsilon，然后是 epsilon 除以 v 减 1，我想是这样。

### [1:27:00](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=5220s) · b000175

所以在实践中，这种方法往往会让模型更不确定。再说一次，就是对这个预测没那么确定，因为你总是在告诉它，好，试着预测这个，但实际上它也可能不是正确的值。不过在实践中，作者发现它往往能改善 BLEU 之类的指标，BLEU 是翻译任务的一个代理指标。

### [1:27:31](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=5251s) · b000176

所以，对，我认为这个方法在 NLP 中相当通用。对，了解它很有用。讲到这里，我想大约还剩 20 来分钟。接下来，Shervine 会带你们完整看一个端到端（end-to-end）的例子。那么，你——对，哦，u？我想这里可以把它看成，我想是，某个量。

### [1:28:06](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=5286s) · b000177

它没有定义，所以就是某个量。而 delta 类似于 one hot，如果你愿意，可以这样理解。它也可以是一个常数。对，对。

### [1:28:32](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=5312s) · b000178

问题是，这与探索和利用（explore and exploit）有关系吗？这是个有意思的问题。

### [1:28:42](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=5322s) · b000179

顺便问一下，为什么 softmax 会自带这个效果呢？

### [1:28:48](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=5328s) · b000180

对，但我想它仍然会——我想，归根结底，你要做的是将预测与标签进行比较。所以这里的问题是，你想和 1, 0, 0, 0 比较，还是想和不是 1, 0, 0, 0 的某个东西比较。我想 softmax 并不能让你做到这一点。没错，是的。我不确定刚才是否讲得特别清楚，但这实际上是标签。所以，你试图预测的并不是 1, 0, 0。

### [1:29:21](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=5361s) · b000181

而是我们改变标签，让模型，我想，预测出一个没那么确定的东西，我想是这样。很好，谢谢。那么，对，Shervine。好，太好了。谢谢你，Afshine。对，我们基本上已经看到了 transformer 如何工作。现在我们会通过一个具体的例子，把所有内容串起来。好，太好了。再来看看我们最喜欢的那个例子：一只可爱的泰迪熊正在阅读。

### [1:29:51](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=5391s) · b000182

然后我们一起走过每一个步骤。首先从词元化（tokenization）开始。正如我们所说，可以用任意划分方式把它拆成 tokens。然后，正如有人提到的，需要某种方式来标记序列的开始和结束。通常，这是通过 BOS 和句子结束词元（EOS tokens）完成的。所以把它们加上。

### [1:30:25](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=5425s) · b000183

现在来关注每个 token 表示的组成。它有自己的 embedding，这是学习出来的。正如 Afshine 提到的，为了知道单词，或者应该说 token，在序列中的位置，你会加入一些额外信息，形式是位置嵌入（position embedding）。这里，原始论文采用了一种使用正弦和余弦的约定，将它们以相加的方式加入表示中。

### [1:30:58](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=5458s) · b000184

所以，这类似于逐元素相加（element-wise addition）。好，太好了。现在你的 token 就有了包含位置信息的 embedding。对每个 token 都重复这个过程。现在，可以把所有这些 embeddings 看成一个矩阵，其中一个维度是 d model，也就是 embeddings 的大小。另一个维度是序列长度，通常记作 n。

### [1:31:29](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=5489s) · b000185

到这里都能理解吗？关于输入有什么问题吗？好，太好了。现在我们把这个表示送入 encoder。正如 Afshine 所说，这里有 self-attention 这个概念。进行 self-attention 的方式是，取这个输入，并将它投影到三个空间。把它投影到 Wq 空间，就得到 queries。

### [1:32:00](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=5520s) · b000186

把同样的 embeddings 投影到 Wk 空间，就得到 keys。对 values 也做同样的事情，就得到 values。Wq、Wk 和 Wv 都是模型学习出来的。它们基本上就是投影矩阵。

### [1:32:19](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=5539s) · b000187

到这里都明白吗？理解这些之后，就可以应用 Afshine 提到的公式，也就是 self-attention 公式：对 Qk 的转置除以 dk 的平方根做 softmax，再乘以 v \[字幕疑误，可能指 Q 与 k 的转置相乘后除以 dk 的平方根，再做 softmax 并乘以 v\]，这样就从这些计算中得到另一个矩阵。

### [1:32:42](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=5562s) · b000188

现在我们暂停一下，看看这个计算在实践中是怎么做的，以及每一步都意味着什么。

### [1:32:52](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=5572s) · b000189

来看 Q。计算 Q 时，基本上就是把 embeddings 投影到那个空间。会得到什么？会得到一个矩阵，其中每一行代表一个给定的 query。说到 k 的转置，基本上是同样的矩阵，但进行了转置，其中每一列代表每个 token 的 key 表示。现在，通过矩阵乘法把它们组合起来。

### [1:33:25](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=5605s) · b000190

当你把它们相乘时，会看到每一行代表 query 在每个 key 上的投影。因此，当你进行矩阵乘法，再对所有这些结果取 softmax 时，就会为每个 query 得到它在各个 keys 上投影的概率分布。每一行都有这样的分布。我不知道之前是否有人问过，为什么要用 dk 的平方根进行缩放？

### [1:34:03](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=5643s) · b000191

它也可以是 dq，因为矩阵乘法，比如这里的 dot product，要求 dq 等于 dk。基本上你会看到，随着 key 和 queries 的维度增大，这些 dot products 往往也会增大。所以你想对这些 dot products 进行归一化（normalize）。这就是为什么要除以 keys 维度的平方根。好，太好了。现在，你得到了所有这些结果的 softmax，然后将它乘以矩阵 v。这就是 Afshine 解释的，把 query 投影到 keys 的空间，然后乘以对应的 value。

### [1:34:49](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=5689s) · b000192

所以，value 是我们所投影到的那个对应 key 的表示。因此，最终会为每个 query 得到 values 的加权和（weighted sum）。

### [1:35:03](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=5703s) · b000193

好，太好了。到这里能理解吗？

### [1:35:12](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=5712s) · b000194

好，太棒了。有人问，multi-head 是什么？你说得对，它并不是只做单独的一次。实际上会做 each 次 \[字幕疑误，可能指 h 次\]。你得到的就是，所有这些都并行完成。最后，你会得到 h 个这样的矩阵。你按照列将它们拼接起来。最后，还有一个叫作 Wo 的投影矩阵，把所有这些投影回 embeddings 的原始维度。

### [1:35:49](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=5749s) · b000195

所以，这是一种让网络基本上以保持维度不变的方式——祝你健康——从原始维度再回到原始维度的方法。有什么问题吗？请说。

### [1:36:15](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=5775s) · b000196

问题是关于 h 的。每次是否可能得到相同的结果？如果是这样，把相同的东西拼接起来会有帮助吗？我理解对你的问题了吗？

### [1:36:28](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=5788s) · b000197

那么，是什么让它们不同呢？这就是梯度下降（gradient descent）的神奇之处。网络最终有一个目标函数（objective function），也有自由度。它的动力是构建一种有助于学习下一个词的表示。所以，它没有动力去复制同样的东西或采用同样的机制。这就是为什么在实践中，你会看到模型收敛到构建不同表示的方式，然后将它们拼接起来，再投影成某种有用的东西。那么，究竟是什么确保你不会得到相同的东西呢？

### [1:37:00](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=5820s) · b000198

没有。也就是说，你没有任何约束。但你让模型进行的这种学习，其本身的性质使它在实践中会这样做。

### [1:37:14](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=5834s) · b000199

还有其他问题吗？这是个很好的问题。我的意思是，gradient descent 通常会创造奇迹。好，太好了。现在我们已经经过了 self-attention layer，还有另一个组件，就是前馈网络（FFN）。我想刚才这里有个问题，是关于如何相对于输入和输出来选择隐藏层的维度。Afshine 提到 Word2vec 时，通常隐藏层的维度小于输入和输出。

### [1:37:48](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=5868s) · b000200

但在这里，隐藏层的维度实际上比输入和输出更大。原因是，你希望模型有足够的自由度来学习有用的表示。所以，这是一种让所学特征变得更复杂的方法。然后，对，\[听不清\]。好，太好了。而且，你并不只有一个 encoder 模块，实际上有 n 个，在原始论文中用大写 N 表示。

### [1:38:19](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=5899s) · b000201

在这一切结束时，你会得到一组经过编码、能够感知上下文的 embeddings。然后，这些组中的每组已编码 embeddings 都会被送入 n 个 decoders。所以，你有 n 个依次堆叠的 encoders，也有 n 个依次堆叠的 decoders。而 encoder 的最后一个表示，就是你送入每个 decoder 的 cross-attention 的内容。

### [1:38:54](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=5934s) · b000202

对，我们会更详细地看这一点。那到底如何开始解码过程呢？从 BOS token 开始。基本上就是对模型说，嘿，我们需要预测下一个词，开始吧。那么，最开始 BOS token 会发生什么？你把它送入 decoder。然后，与之前 encoder 的情况类似，你有一个 self-attention layer。正如 Afshine 提到的，这个 self-attention layer 是因果的（causal）。

### [1:39:27](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=5967s) · b000203

所以，attention 会作用于同一个 token 以及它之前的 tokens。对于这个最初的 BOS token，你看不出区别，因为它只会关注自身。但当你有其他想要解码的 tokens 时，在 decoder 中关注哪些位置就会体现出这种差别。好，太好了，经过 self-attention layer。然后是我提到的 cross-attention，它把这些已编码的 embeddings 作为输入，用作 keys 和 values。

### [1:40:04](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=6004s) · b000204

而 queries 则来自 self-attention layer 的输出。好，太好了。完成这个 cross-attention 之后，与 encoder 中一样，还有一个 FFN 组件，让表示更加丰富。那边有问题吗？没有。

### [1:40:28](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=6028s) · b000205

然后在最后，你会把所有这些做 n 次。在解码过程的最末端，有一个线性投影（linear projection）和一个 softmax 层，把对下一个词的预测转换为词表上的概率分布。好，太好了。我们已经看到了如何为这里的下一个词完成这个过程。基本上，你会不断重复这样做。你已经找到了下一个 token，它基本上就是你想要的内容的 one-hot 编码。

### [1:41:03](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=6063s) · b000206

然后你取那个 embedding，再把它放回 decoder，继续这个过程。什么时候停止呢？这个问题问你们。当遇到 EOS token 时。对，对，完全正确。好，太好了。通过这个过程，原始的这篇里程碑式论文的作者基本上就是这样进行机器翻译（machine translation）的。所以，这就是当时展示的典型用例。

### [1:41:37](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=6097s) · b000207

有什么问题吗？

### [1:41:45](https://www.youtube.com/watch?v=Ub3GoFaUcds&t=6105s) · b000208

好，太棒了。那么，谢谢大家的聆听。\[掌声\]
