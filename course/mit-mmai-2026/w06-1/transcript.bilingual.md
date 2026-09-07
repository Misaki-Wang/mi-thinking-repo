# Lecture 7 – Multimodal Generation (MIT How to AI Almost Anything/Multimodal AI, Spring 2026)

_Bilingual transcript · 双语讲稿_

- Channel: Paul Liang
- Source: [YouTube](https://www.youtube.com/watch?v=KlHIR7lT-mo)
- Duration: 1:17:14
- Caption source: automatic
- Status: complete
- Chinese translation: 91/91
- Translation provider: codex
- Generated: 2026-09-07T08:04:13+00:00

## Transcript · 讲稿

### [00:01](https://www.youtube.com/watch?v=KlHIR7lT-mo&t=1s) · b000001

**English**

Uh a couple of quick announcements. Homework 3 was released uh last Thursday. It's going to be due next Tuesday. Okay. It's primarily about uh training vision language models on your data which might involve images but also might involve other modalities but uh for simplicity we're going to render them as images for now and see what kind of results you get fine-tuning models on that data. And then homework four will be going deeper into designing more custom encoders for your data instead of treating everything as images. So that's homework three that'll be due next Tuesday. Um we're also going to do uh during lecture a midterm review next Tuesday just to recap all the topics that we discussed in the first half of the course and also some extra slides on some things I wasn't able to cover in enough detail because of lack of time in some of the previous lectures. Uh and that will summarize everything that you

**中文**

呃，先快速通知几件事。作业 3 已经在上周四发布了，下周二截止。好。它主要是关于在你们的数据上训练视觉语言模型（vision language models），这些数据可能包含图像，也可能包含其他模态（modalities），不过为了简单起见，我们目前会把它们呈现为图像，看看在这些数据上微调（fine-tuning）模型能得到什么样的结果。然后作业四会进一步深入，为你们的数据设计更定制化的编码器（encoders），而不是把所有东西都当作图像。所以，作业三下周二截止。嗯，我们还会在下周二的课堂上进行期中复习，回顾课程前半部分讨论的所有主题，也会补充一些幻灯片，讲一些之前几次课因为时间不足而没能充分展开的内容。呃，这会总结你们所需的全部内容，

### [00:54](https://www.youtube.com/watch?v=KlHIR7lT-mo&t=54s) · b000002

**English**

need for the midterm exam next Thursday. Okay. Uh midterm exam will be in class. It will be won't take the whole hour. Probably will take you know 45 50 minutes. I know some people have accommodations which gives them uh one and a half times the duration. So we'll try to keep everything within the the 80 minutes of class. But for those of you without accommodation it be around 45 minutes. I think we haven't decided exact time yet. Yes. No practice exams. It's first time I'm teaching this course. Uh and yes, the midterm exams will be here in class. Um I wouldn't I wouldn't worry too much about it. This is not a course like your linear algebra or probability courses. There's a bunch of theorems that you got to memorize and and apply to your midterm exams. The midterm exams will be mostly conceptual. Um some of them will have right and wrong answers, some of them won't have right or wrong answers.

**中文**

用于下周四的期中考试。好。呃，期中考试会在课堂上进行。它会，不会占满一整小时。大概会用，你知道，45 到 50 分钟。我知道有些同学有特殊考试安排，可以获得 1.5 倍的考试时长。所以我们会尽量把所有安排都控制在这节课的 80 分钟内。不过没有特殊安排的同学，考试大概是 45 分钟。我想我们还没决定确切时间。是的。没有模拟试卷。这是我第一次教这门课。呃，是的，期中考试就在这里，在课堂上。嗯，我不会，我不会太担心。这门课不像你们的线性代数或概率论课程，有一堆定理需要背下来，再用到期中考试中。期中考试主要是概念性的。嗯，有些题会有对错之分，有些题则没有标准的对或错。

### [01:51](https://www.youtube.com/watch?v=KlHIR7lT-mo&t=111s) · b000003

**English**

to be conceptual partly semiructured mostly about using the concepts and applying them for various domains. So I wouldn't worry too much about equations or bringing a cheat sheet or memorizing too many things for the exam. Yeah,&gt;&gt; professor for one student we need to understand for one week because we have modification.&gt;&gt; Okay, maybe send me an email. We'll&gt;&gt; we'll make some other accommodations.&gt;&gt; Thank you. All stone students.&gt;&gt; Uh I think almost four you&gt;&gt; as well.&gt;&gt; Yeah. A few of us.&gt;&gt; You as well.&gt;&gt; All right. Yes.&gt;&gt; Our lab is having activity on the 19th and 20s. Is it possible to make the film also online?

**中文**

会是概念性的，部分是 semiructured \[字幕疑误，可能指 semi-structured，半结构化\]，主要是运用这些概念，并将它们应用到不同领域。所以我不会太担心公式、带一张考试速查表，或者为了考试背太多东西。是的，&gt;&gt; 教授，对于一个学生，我们需要理解一周，因为我们有调整。&gt;&gt; 好，也许给我发封邮件。我们会 &gt;&gt; 我们会做一些其他的特殊安排。&gt;&gt; 谢谢。所有 stone 学生 \[字幕疑误，可能指 Sloan 学生\]。&gt;&gt; 呃，我想差不多有四个，你 &gt;&gt; 也是。&gt;&gt; 是的。我们有几个。&gt;&gt; 你也是。&gt;&gt; 好。是的。&gt;&gt; 我们实验室在 19 号和 20s 有活动。有没有可能让 film \[字幕疑误，可能指考试\] 也在线上进行？

### [02:45](https://www.youtube.com/watch?v=KlHIR7lT-mo&t=165s) · b000004

**English**

&gt;&gt; Uh no. We'll arrange another time. But I mean this this shouldn't happen. We've already put the midterm dates early on you know at the beginning of the semester it was on the syllabus. I mean for Sloan if there's an official departmental program I can make it exceptions but uh otherwise people should be in class like they should be all lecturers. So if there's a really oneoff you know thing that cannot be moved uh let me know if otherwise please come here in person to take the exam. no online um we have a makeup duration for people who really have official departmental activities. Okay. And also um project mentors were released. There was a spreadsheet. Uh each project was assigned one letter either myself or the TAs or other instructors. Uh try to meet with them as much as you can. Um I'll be around today and this whole week. So try to meet with

**中文**

&gt;&gt; 呃，不行。我们会另找时间。不过，我的意思是，这，这不应该发生。我们很早就公布了期中考试日期，你知道，学期刚开始时教学大纲上就写了。我的意思是，对 Sloan 来说，如果是院系的正式项目，我可以破例，但呃，否则大家应该来课堂，就像所有 lecturers \[字幕疑误，可能指 lectures，课程\] 都应该来一样。所以，如果真的是一次性的、你知道、无法改期的事情，呃，请告诉我，否则请到这里现场参加考试。不在线上考，嗯，对于确实有院系正式活动的同学，我们会安排补考时段。好。另外，嗯，项目导师的分配也公布了。有一个电子表格。呃，每个项目都分配了一位 letter \[字幕疑误，可能指 mentor，导师\]，可能是我、助教（TAs），或者其他老师。呃，尽量多和他们见面。嗯，我今天和这整周都会在。所以尽量来见

### [03:41](https://www.youtube.com/watch?v=KlHIR7lT-mo&t=221s) · b000005

**English**

us. Uh just to recap on timeline for the projects as well. This week, next week will be the midterm uh and the midterm review and the midterm. The following week will be spring break and the week after that when you come back uh the midterm report will be due. So at the point of the midterm report of which instructions will be posted later this week. You should have at least finalized of course your team, your ideas, your data sets. You should have already started processing your data sets and running existing models. all the state-of-the-art that you're trying to compare with that you're claiming that your method would be better. All that should have already been implemented and analyzed by the midterm report. So once the midterm report is submitted, you're going to go full steam ahead on proposing your new ideas. Okay. So there's actually quite a bit of substantial work needed in data processing, you know, finding the literature and the right baselines,

**中文**

我们。呃，也再回顾一下项目的时间安排。这周，下周会有期中，呃，期中复习和期中考试。再下一周是春假，春假之后一周，你们回来时，呃，期中报告就要交了。所以，到期中报告时，具体说明会在本周晚些时候发布，你们至少应该已经确定了，当然，你们的团队、想法和数据集（datasets）。你们应该已经开始处理数据集，并运行现有模型。所有你们打算比较、声称自己的方法会优于它们的最先进方法（state-of-the-art），到期中报告时都应该已经实现并分析过了。所以，期中报告提交之后，你们就要全力推进，提出自己的新想法。好。所以，在数据处理、你知道、查找文献和合适的基线（baselines）方面，其实有相当多实质性的工作需要完成，

### [04:31](https://www.youtube.com/watch?v=KlHIR7lT-mo&t=271s) · b000006

**English**

running them, uh analyzing the results and and paving the way for your new proposed approach by a midterm report. All right. So, meet with us um the TAs and our project mentors this week if you need any help with reviewing for the midterm and also for brainstorming and positioning your your projects with respect to existing work.&gt;&gt; Any questions about assignments and logistics?

**中文**

运行它们，呃，分析结果，并在期中报告时为你们提出的新方法铺好路。好。所以，如果需要帮助复习期中考试，或者需要为项目集思广益、确定你们的项目相对于现有工作的定位，本周请来找我们、助教和项目导师。&gt;&gt; 关于作业和课程安排，有什么问题吗？

### [05:03](https://www.youtube.com/watch?v=KlHIR7lT-mo&t=303s) · b000007

**English**

&gt;&gt; Yes. Maybe this is like a sort of thing, but there's a lot of relevant data sets for us and it's kind of like a bit confusing choosing between them. Um, do you have any recommendations in the near term for like so we don't play with all of them? Yeah.&gt;&gt; Yeah, definitely don't play with more than um two at most two data sets for the purposes of the course project. Um, I would really try to find data sets in which you are confident that your proposed method will make a difference. which means that data set should not be overly saturated with too high performance. It should not be too low in which your proposed method is not the main bottleneck. So it wouldn't make a noticeable difference. It should kind of right be in that sweet spot where uh methods that already exist solve problems ABC. You're trying to tackle problem X and that is the exact delta that the next step on that data set should um should people should work on.

**中文**

&gt;&gt; 有。也许这属于那种事情，但有很多和我们相关的数据集，在它们之间做选择有点让人困惑。嗯，近期您有什么建议，好让我们不用把它们都试一遍？是的。&gt;&gt; 是的，为了课程项目，绝对不要尝试超过，嗯，两个，最多两个数据集。嗯，我会尽量找那些你有把握认为自己提出的方法能带来变化的数据集。这意味着，那个数据集不应该因为已有性能太高而过度饱和。性能也不应该太低，以至于你提出的方法针对的不是主要瓶颈，因此不会带来明显变化。它应该刚好处在那个合适的区间，呃，现有方法已经解决了问题 A、B、C。你想解决问题 X，而这恰好就是那个差距，是这个数据集上接下来应该，嗯，应该由大家去研究的方向。

### [06:01](https://www.youtube.com/watch?v=KlHIR7lT-mo&t=361s) · b000008

**English**

So that's not not too low, not too overly saturated and at the right timing where people have studied the problems and solved them and they're right you're not next in line to solve the problem for that data set. But we can talk more in office hours. Um but I would not suggest going more than two data sets. Um maybe one that you pick as a primary one and another secondary one in case the first one doesn't work or if you have extra time and you want to show show better results. Great. Okay, so jumping in today's lecture. Today's lecture will be about generative models. We're going to continue our discussion uh from last week where we started talking about these multimodal foundation models. And as you recall, we explained that the next generation of these models will be basically multimodal input, multimodal output models, right? In terms of the input, they should be able to flexibly handle

**中文**

所以，既不要太低，也不要过度饱和，还要处在合适的时机：人们已经研究并解决了一些问题，而且他们正好，你不是接下来要解决那个数据集问题的人。不过我们可以在答疑时间多聊聊。嗯，但我不建议超过两个数据集。嗯，也许选一个作为主要数据集，另一个作为次要数据集，以防第一个行不通，或者你有额外时间，想展示，展示更好的结果。很好。好，那么进入今天的课程。今天讲生成模型（generative models）。我们会接着上周的讨论，当时我们开始讲这些多模态基础模型（multimodal foundation models）。你们应该记得，我们解释过，下一代这类模型基本上会是多模态输入、多模态输出的模型，对吧？在输入方面，它们应该能够灵活处理

### [06:55](https://www.youtube.com/watch?v=KlHIR7lT-mo&t=415s) · b000009

**English**

sequences of text. So sequences of words uh sequences of images in a video audio and so on. And the first key was how to learn multimodal representations that was able to learn the alignment between elements. So which elements are semantically meaningful together and how these aligned connect elements lead you to learn better representations that are useful downstream tasks. And as a recap, what we saw was essentially this key approach which is widely used today called multimodal transformers. Uh which essentially allows you to take in a sequence of elements in one modality, for example, three words. A sequence of elements in some other modality, for example, four verbal expressions and learning this 3x4 alignment matrix. It's telling you how each one of the three words is aligning with each one of your four non-verbal expressions. And this can be learned using this weighted outer product. You can also think about it as

**中文**

文本序列。也就是词的序列，呃，视频中的图像序列、音频等等。第一个关键是如何学习多模态表征（multimodal representations），使其能够学习元素之间的对齐（alignment）。也就是哪些元素在语义上结合起来有意义，以及这些对齐的、连接起来的元素如何帮助你学习更好的表征，用于下游任务（downstream tasks）。回顾一下，我们看到的基本上就是如今广泛使用的这个关键方法，叫作多模态 transformers（multimodal transformers）。呃，它基本上允许你输入一种模态中的元素序列，例如三个词；再输入另一种模态中的元素序列，例如四个 verbal expressions \[字幕疑误，可能指 non-verbal expressions，非言语表达\]，并学习这个 3x4 对齐矩阵（alignment matrix）。它告诉你，这三个词中的每一个如何与四个非言语表达中的每一个对齐。这可以通过这个加权外积（weighted outer product）来学习。你也可以把它看作

### [07:53](https://www.youtube.com/watch?v=KlHIR7lT-mo&t=473s) · b000010

**English**

an attention matrix where with appropriate normalizations you can interpret each of these entries as a probability distribution over which elements in the other modality you are aligning to. Right? So maybe the word privilege sounds very positive but in the alignment of 7 with saying it very loudly that gives it some new meaning. in the context of 0.3 alignment with eye rolling afterwards that gives it another meaning which in this case might be sarcasm. So this was a key idea of learning the alignment between multiple elements across modalities which can then be used to learn better representations. Right? So this alignment basically told you if I want a new representation for this word privileged I should actually be contextualizing it 7 with the semantic embedding for vocal emphasis plus.3 of the semantic embedding for eye rolling and that gives you a new language representation that has been

**中文**

一个注意力矩阵（attention matrix），经过适当的归一化（normalization）之后，你可以把其中每一项解释为一个概率分布，表示你正在和另一种模态中的哪些元素对齐。对吧？所以，privilege 这个词听起来可能很积极，但它以 7 \[字幕疑误，可能指 0.7\] 的权重与非常大声地说出来对齐，就会赋予它某种新的含义。在随后翻白眼、对齐权重为 0.3 的语境中，它又有了另一种含义，在这个例子里可能就是讽刺。所以，这是学习跨模态多个元素之间对齐的一个关键想法，然后可以用来学习更好的表征。对吧？所以，这个对齐基本上告诉你，如果我想得到 privileged 这个词的新表征，我实际上应该把它进行上下文化（contextualization）：7 \[字幕疑误，可能指 0.7\] 乘以声音强调的语义嵌入（semantic embedding），加上 .3 乘以翻白眼的语义嵌入，这样就得到一个新的语言表征，它已经

### [08:50](https://www.youtube.com/watch?v=KlHIR7lT-mo&t=530s) · b000011

**English**

contextualized with vision which can then be used for downstream tasks. So most of the models nowadays if they're taking in multiple streams of input all of which are sequences of text of images or audio they're using some kind of cross attention like this to learn the alignment between those two sets of modality sequences that's the alignment matrix and then using that to learn better representations just a recap from uh last last Thursday last Tuesday.

**中文**

利用视觉进行了上下文化，然后可以用于下游任务。所以，如今大多数模型，如果接收多路输入流，而这些输入都是文本、图像或音频的序列，就会使用某种像这样的交叉注意力（cross-attention）来学习这两组模态序列之间的对齐，也就是这个对齐矩阵，然后利用它学习更好的表征。这只是回顾一下，呃，上，上周四，上周二的内容。

### [09:22](https://www.youtube.com/watch?v=KlHIR7lT-mo&t=562s) · b000012

**English**

So that was about taking in multimodal sequential data and learning representations. We also discussed how we can use these representations as input to a often pre-trained large language model. Right? And that is very important because now you can basically ask expect answer of any question using this large language model and you can get this interactive dialogue and multi-turn interaction capabilities on top of your multimodal data. Yes. the um attention you see for both and is that usually something that we know that these are like the features of the I guess here audio but well sometimes also just some meaning of audio that we don't necessar

**中文**

所以，刚才讲的是接收多模态序列数据并学习表征。我们还讨论了如何把这些表征作为输入，送入一个通常经过预训练的大语言模型（large language model，LLM）。对吧？这很重要，因为现在你基本上可以提问、期待利用这个大语言模型回答任何问题，并且可以在你的多模态数据之上获得这种交互式对话和多轮交互能力。是的。那个，嗯，你看到的针对两者的注意力，这通常是我们已知的东西吗，也就是说，这些是，我想这里是音频的特征，但，有时也只是音频的某种含义，而我们不一定

### [10:19](https://www.youtube.com/watch?v=KlHIR7lT-mo&t=619s) · b000013

**English**

&gt;&gt; yeah great question. So I've seen both being done, right? Cross attention can operate directly on raw data. So maybe raw token embeddings and raw uh image patch embeddings uh in which case it might be raw features not directly into credible or not high level and semantic. I've also seen people uh extract for example you could use pre-extracted uh speech features and pre-extracted facial features. So you can get some of these semantically meaningful non-verbal tokens that represent emphasis and eye rolling. And of course these these pre-enccoders could also be learned jointly with the model. Right? So you could think of having a CNN or a vision transformer that first goes over the image to get some of these visual only features which are then input to this to this cross attention. So

**中文**

&gt;&gt; 是的，好问题。所以，这两种做法我都见过，对吧？Cross-attention 可以直接作用于原始数据。比如原始的 token 嵌入（token embeddings）和原始的，呃，图像块嵌入（image patch embeddings），在这种情况下，它们可能是原始特征，不能直接 into credible \[字幕疑误，可能指 interpretable，可解释\]，或者不是高层次的语义特征。我也见过有人提取，例如，你可以使用预先提取的语音特征和预先提取的面部特征。这样你就能得到一些在语义上有意义的非言语 token，表示强调和翻白眼。当然，这些，这些前置编码器也可以与模型联合学习。对吧？所以，你可以设想有一个卷积神经网络（CNN）或 vision transformer，先处理图像，得到一些仅包含视觉信息的特征，再把它们输入这个，这个 cross-attention。所以

### [11:16](https://www.youtube.com/watch?v=KlHIR7lT-mo&t=676s) · b000014

**English**

even though it's not so \[clears throat\]&gt;&gt; I mean it's hard to say it's the it's like the difference between early fusion and late fusion right if you're doing uh this cross tension on top of the raw features that's basically the early fusion style where the dimension of your cross tension might be larger uh more parameters but it's more flexible in what the model can learn if you start extracting pre- extracting some of these features beforehand. Uh depending on how good that pre-extraction is, you might be very well offering only on the most important features and having a smaller cross tension. So you got efficiency and the right features. The issue of course is if this pre-extraction, right, the unimodal encoding or pre-extraction of unimodal features is not good. If that is not good and you're doing a lot of pre-processing before that, then maybe downstream it's losing information. Um so it's all various trade-offs. say the same trade-off as whether you do early

**中文**

即使它不是那么 \[清嗓子\] &gt;&gt; 我的意思是，这很难说，它就像早期融合（early fusion）和晚期融合（late fusion）的区别，对吧？如果你在原始特征之上做这个 cross tension \[字幕疑误，可能指 cross-attention\]，那基本上就是 early fusion 的风格，你的 cross tension 维度可能更大，呃，参数更多，但模型能学习什么也更灵活。如果你开始提取，事先预先提取一些这样的特征，呃，取决于这种预提取做得有多好，你可能很好地只在最重要的特征上 offering \[字幕疑误，可能指 operating，运算\]，并使用更小的 cross tension。所以，你既获得了效率，也获得了合适的特征。当然，问题在于，如果这个预提取，对吧，单模态编码（unimodal encoding）或单模态特征的预提取做得不好。如果做得不好，而你在此前又进行了大量预处理，那下游可能就会丢失信息。嗯，所以这里涉及各种权衡。也就是同样的权衡：你是做早期

### [12:12](https://www.youtube.com/watch?v=KlHIR7lT-mo&t=732s) · b000015

**English**

fusion with a bigger model and letting the model figure out which features to extract and fuse or late fusion where you're extracting features first maybe using some domain knowledge assuming that's good then you have a smaller cross attention fusion on top of features that you know are good

**中文**

融合，使用更大的模型，让模型自己弄清楚该提取和融合哪些特征；还是做 late fusion，先提取特征，也许用一些领域知识，假设这些特征是好的，然后在你知道是好的特征之上使用一个更小的 cross-attention 融合模块。

### [12:36](https://www.youtube.com/watch?v=KlHIR7lT-mo&t=756s) · b000016

**English**

nowadays the trend of course for for for vision and for audio is to directly do this on the raw data because you know you have good pre-trained embeddings. Um but the trend for other modalities like you know time series or or sensors for example people are still extracting for example variability feature but signal processing features because we don't really have yet very good models that directly operate on the raw data. All right, any other questions about the recap of um these aligned representations using transformers?

**中文**

如今，当然，对于，对于，对于视觉和音频，趋势是在原始数据上直接做这个，因为，你知道，你有很好的预训练嵌入。嗯，但对于其他模态，比如，你知道，时间序列（time series）或传感器（sensors），人们仍然会提取，例如变异性特征，不过信号处理特征，因为我们实际上还没有非常好的、能够直接作用于原始数据的模型。好，关于用 transformers 获得这些对齐表征的回顾，还有其他问题吗？

### [13:19](https://www.youtube.com/watch?v=KlHIR7lT-mo&t=799s) · b000017

**English**

So as we saw the other second key part was to how to adapt these multimodal representations into language models often pre-trained language models right so you can ask and answer any question with respect to these other modalities and again a key to to recap last week is that we introduced this idea of adapters what adapters are is that you have these really powerful language models large pre-trained powerful language models, keep them frozen. Don't update them too much. If you have good unimodal encoders in image, for example, good pre-trained vision encoders, again, keep them frozen. Don't update them too much. Just try to learn the small adapter layers that take in these other modalities features and projects them into the input token of the large language model. Right? So that's this orange block over here. It can be as simple as a linear

**中文**

所以，正如我们看到的，另一个，第二个关键部分是如何把这些多模态表征适配到语言模型中，通常是预训练语言模型，对吧？这样，你就可以针对这些其他模态提出并回答任何问题。再回顾一下上周的一个关键点，我们介绍了适配器（adapters）这个想法。Adapters 是什么呢，就是你有这些非常强大的语言模型，大型、预训练的、强大的语言模型，把它们冻结。不要过多更新它们。如果你在图像方面有很好的单模态编码器，比如很好的预训练视觉编码器，同样，把它们冻结。不要过多更新它们。只尝试学习那些小型 adapter 层，它们接收这些其他模态的特征，并把它们投影到大语言模型的输入 token 中。对吧？所以，就是这里这个橙色模块。它可以简单到只是一个线性

### [14:15](https://www.youtube.com/watch?v=KlHIR7lT-mo&t=855s) · b000018

**English**

transformation that maps it from whatever dimensional visual feature into the input dimension of language model tokens. Now even though it's very simple, it works surprisingly well. Surprisingly well that just a simple linear transformation is able to align two very very very different models, different architectures trained on very different amounts of data. Now usually you know we saw that these are trained in two stages. The first stage is the alignment stage or you can think about it as image captioning. So you have the image coming in and you're going to collect some data about uh semantically meaningful description of that image. So that will allow you to train this linear layer to essentially take in these visual features and express them in natural language and predict the caption. Right? That's called alignment. You can get all sorts of these image captioning datas from Wikipedia, Instagram, uh, MSCO, huge

**中文**

变换（linear transformation），把任意维度的视觉特征映射到语言模型 token 的输入维度。虽然它很简单，但效果出奇地好。好得令人惊讶，仅仅一个简单的线性变换，就能对齐两个非常、非常、非常不同的模型，不同的架构，用非常不同数量的数据训练出来的模型。通常，你知道，我们看到这些模型分两个阶段训练。第一阶段是对齐阶段，或者你可以把它理解为图像描述（image captioning）。也就是输入图像，然后收集一些数据，是关于那张图像的、呃，在语义上有意义的描述。这使你能够训练这个线性层，基本上接收这些视觉特征，用自然语言表达它们，并预测图像描述。对吧？这就叫对齐。你可以从 Wikipedia、Instagram、呃，MSCO \[字幕疑误，可能指 MSCOCO\] 获取各种这类图像描述数据，大规模的

### [15:12](https://www.youtube.com/watch?v=KlHIR7lT-mo&t=912s) · b000019

**English**

databases of images and captions, but that in itself isn't useful for downstream tasks because we don't want to train this model and have it just do captioning all the time. We sometimes want it to be useful in answering questions or giving advice or solving other tasks on these images. So that's stage two, right? Stage two is what we call instruction tuning where you curate given what you expect users to use this model downstream for. You're going to curate triplets of the image of instructions people might ask or questions people might ask and answers that they might expect to see. uh so using image and text instructions and example completions that uh human experts give and then you can then start training a model to take in the image to take in the the instruction also as input to the language model and to decode the right completion. So you call that instruction tuning, right? So

**中文**

图像与描述数据库，但这本身对下游任务还不够有用，因为我们不想训练这个模型之后，让它一直只做图像描述。我们有时希望它能用于回答问题、给出建议，或者解决与这些图像相关的其他任务。所以，这就是第二阶段，对吧？第二阶段就是我们所说的指令微调（instruction tuning），根据你预期用户在下游如何使用这个模型来整理数据。你要整理三元组，包括图像、人们可能提出的指令或问题，以及他们可能期待看到的答案。呃，所以，使用图像、文本指令以及人类专家给出的示例补全（completions），然后你就可以开始训练模型：接收图像，同时把指令作为语言模型的输入，并解码出正确的补全。所以，这就叫 instruction tuning，对吧？所以

### [16:08](https://www.youtube.com/watch?v=KlHIR7lT-mo&t=968s) · b000020

**English**

pretty much follows the the pre-training on loss of text paradigm and instruction tuning on text but to the multimodal setting. Any questions about this recap part two on adapting large language models with other modalities? Do you think it's uh because the linear layer works so well there's there's like more evidence for kind of modalities having similarities overall model.&gt;&gt; Yeah. Whether it gives more uh credence to the platonic representations right where these models train completely separately lots of different data they somehow are very close that a linear layer is sufficient to map them together with each other. Yes and no. Right. So this this works really well in settings where first of all images that can be described really well in captions and user instructions that can be expressed

**中文**

基本上沿用了在 loss of text \[字幕疑误，可能指 lots of text，大量文本\] 上预训练、在文本上进行 instruction tuning 的范式，只是扩展到了多模态场景。对于回顾的第二部分，也就是用其他模态适配大语言模型，有什么问题吗？您觉得，是不是因为线性层效果这么好，所以这更能证明各种模态在整个模型中具有相似性？&gt;&gt; 是的。是不是给柏拉图式表征（platonic representations）这个观点增加了可信度，对吧？这些模型完全分开训练，使用大量不同的数据，却不知怎么就非常接近，以至于一个线性层就足以把它们相互映射起来。是，也不是。对吧？这种方法在一些场景下非常有效，首先，图像能用描述很好地表达，而用户指令也能被表达得

### [17:05](https://www.youtube.com/watch?v=KlHIR7lT-mo&t=1025s) · b000021

**English**

really well in text. Once you start applying some of these models and even we start applying some of the state-ofthe-art Gemini GPT5s type of models to visual settings where it's not easily describable in natural language. So you're asking about the texture of a material or the depth of of the robot arm behind a certain object or the lighting condition, right? Uh and then you go to things like touch, right? You know, how do you feel something? How do you touch something when it's not expressable in natural language? Uh we have not really yet seen these methods working. Of course, there's two hypothesis. One hypothesis is that for all these domains we don't have paired modality text data to train these models because it's just not possible to get it right. The other possibility is that you know there is some inherent bottleneck in these kind of approaches so that even if you have somehow able to curate you know textual descriptions of of texture and touch you may not be able to train

**中文**

非常好，用文本表达。一旦你开始把其中一些模型，甚至我们开始把一些最先进的 Gemini、GPT5s 这类模型，应用到不容易用自然语言描述的视觉场景中。比如你问的是一种材料的纹理，或某个物体后面机械臂的深度，或光照条件，对吧？呃，然后再到触觉之类的东西，对吧？你知道，你如何感受某个东西？当它无法用自然语言表达时，你如何触摸某个东西？呃，我们实际上还没有看到这些方法有效。当然，有两种假设。一种假设是，对于所有这些领域，我们没有用于训练这些模型的模态与文本配对数据，因为根本不可能得到，对吧。另一种可能是，你知道，这类方法存在某种内在瓶颈，所以，即使你不知怎么能够整理出，你知道，关于纹理和触觉的文字描述，你也可能无法训练

### [18:02](https://www.youtube.com/watch?v=KlHIR7lT-mo&t=1082s) · b000022

**English**

this model. Do you think it just like falls into like what would you call like in&gt;&gt; the modalities like won't work for certain&gt;&gt; I mean that's the main argument people people make for why we need to go beyond language models um more ofx paradox is the other one that people like talking about which some of you might have heard that it's a paradox between because things that people find really difficult like passing a bar exam or doing SAT or solving IMO questions are surprisingly easily tackled by today's AI models. Whereas things that people find trivial like clicking this clicker or going through your pocket and picking up your keys without looking at it are still not able to be done by any state-of-the-art robot or robot hand. That's a paradox. And the possible explanation is that you know things that we find really difficult like passing a bar exam or

**中文**

这个模型。您觉得它只是属于那种，您会怎么称呼，就是在 &gt;&gt; 某些模态上不起作用 &gt;&gt; 我的意思是，这就是人们主张我们需要超越语言模型的主要理由，嗯，more ofx paradox \[字幕疑误，可能指 Moravec's paradox，莫拉维克悖论\] 是大家喜欢谈的另一个，有些人可能听过。这个悖论是说，因为人们觉得非常困难的事情，比如通过律师资格考试、参加 SAT，或者解决 IMO 题目，今天的 AI 模型却能出奇地轻松应对。反过来，人们觉得很简单的事情，比如按一下这个翻页器，或者不看就从口袋里摸出钥匙，任何最先进的机器人或机械手却仍然做不到。这是一个悖论。可能的解释是，你知道，我们觉得非常困难的事情，比如通过律师资格考试，或者

### [18:59](https://www.youtube.com/watch?v=KlHIR7lT-mo&t=1139s) · b000023

**English**

taking SATs. We've curated so much of human knowledge into well-defined wellcrafted textbooks and practice questions that is easy to train AI models on. But things that we find trivial like picking up a cup or pressing a clicker, we don't even go about thinking about curating data for that. So it's innate, it's evolutionary. So that's not easy way to train AI models.&gt;&gt; Yeah.&gt;&gt; Isn't it also because you cannot understand as you mentioned like depth and perception of the world like it's it's easy to train a model with linear data. I want to call it the like text is just non tree dimension&gt;&gt; while understanding where to put your hand and not to squeeze that much. You need multiple type of senses. You need perception, you need touch, you need sight, you need probably hearing. Wouldn't that be solved if you unite

**中文**

参加 SAT，我们已经把大量人类知识整理成定义明确、编写精良的教科书和练习题，很容易拿来训练 AI 模型。但是，我们觉得很简单的事情，比如拿起杯子或按一下翻页器，我们甚至不会去想为此整理数据。所以，这是天生的，是进化而来的。所以，没有简单的方法来训练 AI 模型。&gt;&gt; 是的。&gt;&gt; 这是不是也因为你无法理解，正如您提到的，深度以及对世界的感知？就是，用线性数据训练模型很容易。我想把它叫作，文本只是 non tree dimension \[字幕疑误，可能指 non-three-dimensional，非三维的\] &gt;&gt; 而理解手该放在哪里，以及不要捏得那么用力，你需要多种感官。你需要感知，需要触觉，需要视觉，可能还需要听觉。如果把它们结合起来，这不就能解决了吗，

### [19:54](https://www.youtube.com/watch?v=KlHIR7lT-mo&t=1194s) · b000024

**English**

multiple senses as professor Demetrius said the other day? Um yes and no. Um I would say one counterargument to that is that you know some of these really hard hard problems that AI is solving they're also very multimodal in nature right be able to extract lots of information from clinical data it's highly multimodal requires uniting all these senses we make great progress in that right now some of these IMO or scientific discovery also requires understanding chemical molecules and chemical textbooks and lots of text data and protein structure sequences. I don't think it's a lack of progress in this multiensory integration which there's lots of progress right as Dimmitri said as as we're saying all here um but of course I think it comes to the point that some of these physical AI tasks we don't yet have the right sensors touch sensors step sensors you know to actually capture rich amounts of data whereas you know for for multimedia digital modalities we have the right

**中文**

结合多种感官，像 Demetrius 教授前几天说的那样？嗯，是，也不是。嗯，我想，一个反驳是，你知道，AI 正在解决的一些非常、非常困难的问题，本质上也是高度多模态的，对吧？能够从临床数据中提取大量信息，这就是高度多模态的，需要把所有这些感官结合起来，我们在这方面取得了很大进展，对吧？现在，一些 IMO 问题或科学发现也需要理解化学分子、化学教科书、大量文本数据，以及蛋白质结构序列。我不认为是这种多感官整合（multisensory integration）缺乏进展，这方面有很多进展，对吧，正如 Dimmitri 说的，也正如我们在这里一直说的，嗯，但当然，我觉得关键在于，对于一些具身物理 AI（physical AI）任务，我们还没有合适的传感器，触觉传感器、step sensors \[字幕疑误，可能指 depth sensors，深度传感器\]，你知道，来真正采集丰富的数据；而对于，你知道，对于多媒体数字模态，我们有合适的

### [20:48](https://www.youtube.com/watch?v=KlHIR7lT-mo&t=1248s) · b000025

**English**

sensors and the right amount of data. Yeah. navigating

**中文**

传感器和足量的数据。是的。在世界中导航

### [20:59](https://www.youtube.com/watch?v=KlHIR7lT-mo&t=1259s) · b000026

**English**

the world by using our home example like that is something that's very easy for us because of um so you think that a robot would um never possibly like be as efficient as students carrying these usicient

**中文**

用我们家的例子来说，那对我们是很容易的，因为，嗯，所以您觉得机器人会，嗯，永远不可能像学生携带这些 usicient \[字幕不清\] 那样高效

### [21:24](https://www.youtube.com/watch?v=KlHIR7lT-mo&t=1284s) · b000027

**English**

about species.&gt;&gt; Yeah, I think you know of course humans have billions of years of evolution not just human species but prehistoric you know animals single cellular organisms who could already move and have have tactile perception and reinforcement learning interacting with the world. So I think humans we have much I don't really buy the argument where a baby only sees this trillion number of tokens in their lifetime because there's years evolution from humans and also prehuman organisms. Um, that being said, nowadays there's this very exciting field of research called self- evvolving AI, which is basically, you know, all of this, we're still yet at this stage where we are crafting images and captions and train the AI model to replicate that and hope that it generalizes and hope that it generalizes to the same sort of instructions that we

**中文**

关于物种。&gt;&gt; 是的，我想，你知道，当然，人类经历了数十亿年的进化，不只是人类这个物种，还有史前的，你知道，动物、单细胞生物，它们已经能够移动，并且具有触觉感知，以及与世界交互的强化学习（reinforcement learning）。所以，我认为人类，我们有很多，我不太认同那种说法，说一个婴儿一生只看到了这么多万亿个 token，因为背后有人类以及前人类生物经历的多年进化。嗯，话虽如此，如今有一个非常令人兴奋的研究领域，叫作自我演化 AI（self-evolving AI），它基本上，你知道，所有这些，我们还处在这样的阶段：我们编制图像和描述，训练 AI 模型去复现这些，希望它能泛化，也希望它能泛化到与我们

### [22:20](https://www.youtube.com/watch?v=KlHIR7lT-mo&t=1340s) · b000028

**English**

set users to put in. But this new era of self-evolving AI, it's basically about designing these foundation models who can design their own tasks and design their own objectives for themselves, right? Not just once, but if you do it once successfully, you can do it multiple times, right? So hopefully it can self- evvolve and mimic evolution. Something that our group is actively working on that the community is actively working on. Um, we have a couple of open spots towards the end of the semester. So maybe we'll have that as a as a special topic lecture that we can put together if people are interested.

**中文**

设定用户会输入的同类指令上。但这个 self-evolving AI 的新时代，基本上是要设计能够为自己设计任务、为自己设计目标的基础模型，对吧？不只是一次，如果你成功做了一次，就可以做很多次，对吧？所以，希望它能够自我演化，模拟进化。这是我们研究组正在积极研究的，也是整个社区正在积极研究的。嗯，学期末我们还有几个空着的课时。所以，如果大家感兴趣，也许我们可以把这个安排成一节专题课。

### [22:58](https://www.youtube.com/watch?v=KlHIR7lT-mo&t=1378s) · b000029

**English**

All right, great. So that was part two on adapting these LLMs. And finally going to part three which is where we stopped last week was to kind of close the loop so that we can have models that are able to do multimodal perception get representations adapt LLM so that you can have text output through QA and text output but now also closing the loop to do multimodal generation. So you can also generate images, video, audio at the same time in the output space uh in a synchronized way that is still dependent on these multimodal inputs and generated text. Uh once you have this then you basically have this this whole loop of you know agents that can interact with multimodal perception and multimodal generation input and output. So I'll cover at a high level two ways of doing this. One way of doing it is to do text to image retrieval and the other

**中文**

好，很好。刚才是第二部分，关于适配这些 LLMs。最后进入第三部分，也就是我们上周停下来的地方，要把这个闭环补上，让模型能够进行多模态感知（multimodal perception），得到表征，适配 LLM，从而通过问答（QA）和文本输出得到文本输出；现在还要闭合这个环，实现多模态生成（multimodal generation）。这样，你也可以在输出空间中同时生成图像、视频、音频，呃，以同步的方式，并且仍然依赖这些多模态输入和生成的文本。呃，一旦做到这一点，你基本上就有了这个，这个完整的闭环，你知道，智能体（agents）能够通过多模态感知和多模态生成进行输入与输出交互。所以，我会从高层次介绍两种做法。一种是文本到图像检索（text-to-image retrieval），另一种

### [23:55](https://www.youtube.com/watch?v=KlHIR7lT-mo&t=1435s) · b000030

**English**

one is to do text to image generation to complete this last pipeline on the output space. Right? Main difference is whether you're completing these outputs by retrieving across a large set of images. You're guaranteed the accuracy and realism of these images. So you're fixed by the set of images that you began with or going towards open-ended generation where you're generating these you know other modalities pixel wise. So now you are not limited to a finite set of images. You can go much more beyond that infinitely possible space of images. But then you get all the potential concerns with hallucinations and maybe not the best quality images.

**中文**

是文本到图像生成（text-to-image generation），来补全输出空间中的最后这段流程。对吧？主要区别在于，你是否通过在大量图像中检索来完成这些输出。这样能保证这些图像的准确性和真实感。所以，你受到起初那组图像的限制；或者走向开放式生成（open-ended generation），逐像素生成这些，你知道，其他模态。这样，你就不再局限于有限的图像集合。你可以远远超出它，进入无限可能的图像空间。但随后也会出现所有潜在的幻觉（hallucinations）问题，图像质量也可能不够好。

### [24:38](https://www.youtube.com/watch?v=KlHIR7lT-mo&t=1478s) · b000031

**English**

So we'll see both starting with text to image retrieval. So if you think of text image retrieval, we've already seen very powerful model or a model clip and more broadly a class of models on these align representations, right? Especially discrete alignment, right? Where if you recall you had these these models where you could take in a input caption, you could take in an input image. These are positive pairs. You learn embeddings for them, right? text will go through LLM, images will go through a visual encoder, and you learn embedding such that you're maximizing the similarity of positive pairs. So they're close together, which makes them very suitable for retrieval through nearest neighbors, and then you're pushing apart the distance for negative pairs. So you've seen that that's clip, right? So in fact, one easy way to complete the loop between multimodal input and output is to

**中文**

所以，两种方式我们都会看，先从 text-to-image retrieval 开始。如果你考虑文本图像检索，我们已经见过一个非常强大的模型，或者一个叫 clip \[字幕疑误，可能指 CLIP\] 的模型，以及更广义上的一类基于这些对齐表征的模型，对吧？尤其是离散对齐（discrete alignment），对吧？你们应该记得，这些模型可以接收一条输入描述，也可以接收一张输入图像。这些是正样本对（positive pairs）。你为它们学习嵌入，对吧？文本经过 LLM，图像经过视觉编码器，然后学习嵌入，使正样本对的相似度最大化。所以它们会靠近彼此，这使它们非常适合通过最近邻（nearest neighbors）进行检索；同时，你会拉大负样本对（negative pairs）之间的距离。所以，你们已经见过，那就是 clip，对吧？因此，实际上，补全多模态输入与输出闭环的一个简单方法，就是

### [25:34](https://www.youtube.com/watch?v=KlHIR7lT-mo&t=1534s) · b000032

**English**

essentially attach clip as a image retriever on the output side. So this is what these folks did. Uh you first start by feeding in u pairs of images and captions. So an image and the corresponding caption is a silhouette of a plane against a sunset. You have the next image. You have the caption a QC cat getting sitting on a scooter. Right? So this is inputting into the model multiple sequences of image and text. And again you see here the images you pass it to a visual encoder and you have this green vox which is basically your adapter right that is a small adapter that is trained to take in the visual encoders representation and input that into your language model. So be series of interled image representations adapted into the LLM, a text tokenized caption and then a next image and then the next text tokenized caption and all this series of interle images and captions are input into the language

**中文**

基本上在输出端接一个 clip，作为图像检索器（image retriever）。这些人做的就是这个。呃，首先输入，呃，成对的图像和描述。一张图像及其对应描述是：夕阳映衬下的一架飞机的剪影。然后有下一张图像。描述是：一只 QC cat \[字幕疑误，可能指 cute cat，可爱的猫\] 正在，坐在一辆踏板车上。对吧？所以，这就是把多个图像和文本序列输入模型。同样，你在这里看到，图像被送入视觉编码器，而这个绿色的 vox \[字幕疑误，可能指 box，方框\]，基本上就是你的 adapter，对吧？它是一个小型 adapter，经过训练，接收视觉编码器的表征，并把它输入语言模型。所以，会是一系列 interled \[字幕疑误，可能指 interleaved，交错的\] 图像表征，适配到 LLM 中，再加上一段 token 化的文本描述，然后是下一张图像，再下一段 token 化的文本描述，这一整串 interle \[字幕疑误，可能指 interleaved\] 图像和描述都输入语言

### [26:32](https://www.youtube.com/watch?v=KlHIR7lT-mo&t=1592s) · b000033

**English**

model. And then the goal for the language model is to generate basically a completion, right? He sees that there's a silhouette of a of a plane. There's a cat on a scooter. And maybe it predicts that what's going to happen next is that there's going to be some uh some some you know I don't think it's here but maybe it's going to predict next for example a person walking around on a motorcycle afterwards. So after it generates the completed text it will just basically use clip to retrieve the nearest image describing that completed caption. So that's how it generates both the caption and also the aligned retrieved image at the same time. Here are some examples. So you can start having a dialogue with these agents. You say, "I'm thinking of an animal. It is brown and furry and has a tail. What is it?" The model guesses a squirrel. The model says, "No, the animal I'm thinking of lives in a river." And the model says, "Oh, it's a

**中文**

模型。然后，语言模型的目标基本上就是生成一个补全，对吧？它看到有一架，一架飞机的剪影。有一只猫在踏板车上。也许它预测接下来会发生的是，有一些，呃，一些，一些，你知道，我想这里没有展示，但也许它接下来会预测，例如，之后有一个人骑着摩托车四处走动。所以，在生成补全的文本之后，它基本上就会使用 clip 检索最贴近这段补全描述的图像。所以，它就是这样同时生成描述，以及对齐的检索图像的。这里有一些例子。你可以开始与这些智能体对话。你说：“我在想一种动物。它是棕色的，毛茸茸的，还有一条尾巴。它是什么？”模型猜是松鼠。模型说：“不，我想的那种动物住在河里。”然后模型说：“哦，是一只

### [27:29](https://www.youtube.com/watch?v=KlHIR7lT-mo&t=1649s) · b000034

**English**

beaver." And you ask, "What do beavers look like? Show me an illustration of a beaver." So it's going to retrieve that image using clip from a particular database uh illustration of a beaver. You can also go beyond and say what about a pencil drawing of one and a model is also able to retrieve using clip a pencil drawing of of a beaver. Uh here's another cool example. So you might be going around, you're shopping for a house, you take a photo of a house and you ask what is it? The model says it is a house with unique design. You ask for the shape and you ask to show me more houses like this and the model can also maybe retrieve other houses uh that are semantically similar in the image space. Uh here's one last example. Here's can be very useful in building this assistant for cooking. So let's say you're you're searching how to make a

**中文**

河狸。”然后你问：“河狸长什么样？给我看一张河狸的插画。”于是，它会用 clip 从某个特定数据库中检索那张图像，呃，一张河狸的插画。你还可以进一步问，那铅笔画呢？模型也能够用 clip 检索一张河狸的铅笔画。呃，这里还有一个很酷的例子。你可能在到处看房，准备买房，拍了一张房子的照片，然后问这是什么？模型说，这是一栋设计独特的房子。你询问它的形状，并要求给我看更多像这样的房子，模型也可能检索出其他房子，呃，在图像空间中语义相近的房子。呃，最后一个例子。这个可以很有助于构建烹饪助手。假设你正在搜索如何做一道

### [28:25](https://www.youtube.com/watch?v=KlHIR7lT-mo&t=1705s) · b000035

**English**

particular dish like like macaroons. They explain what it is. They retrieve the recipe. All this is still text interaction. And then maybe at some point you're confused. You know, you're supposed to beat it until the egg whites have stiff peaks. Uh, and you don't know what it looks like. So you say, "Please show me a photo of what egg whites with stiff peaks looks like." So he's able to retrieve the right image using that context embedding and retrieving using clips image retrieval capabilities. Okay. So very powerful if you have systems where textual interaction and also visual illustrations are very helpful for assisting users. Yeah.&gt;&gt; Not missing the limitation just like the green rectangular box I understood it as being trained using images. Is that right?

**中文**

特定的菜，比如，比如 macaroons（蛋白杏仁饼）。它们解释这是什么。它们检索食谱。这些仍然都是文本交互。然后，也许某一步让你困惑了。你知道，你应该把蛋白打发到硬性发泡（stiff peaks）。呃，但你不知道那是什么样子。所以你说：“请给我看一张蛋白打发到 stiff peaks 时的照片。”这样，它就能够利用那个上下文嵌入（context embedding），并使用 clips \[字幕疑误，可能指 CLIP 的\] 图像检索能力，检索出正确的图像。好。所以，如果你有一个系统，文本交互和视觉示例对帮助用户都很有用，那这就非常强大。是的。&gt;&gt; 不是漏掉这个局限，只是那个绿色长方框，我理解它是用图像训练的。是这样吗？

### [29:19](https://www.youtube.com/watch?v=KlHIR7lT-mo&t=1759s) · b000036

**English**

&gt;&gt; Yes. So in this case, if we assume that that green rectangular box is actually mapping our visual output embedding fairly well to the caption, what is the benefit of stillting the image and the caption still if one is interchangeable for the other?&gt;&gt; Uh that's a good question. So basically you're asking alo so so for context some of these data sets are called visual storytelling data sets. So it comes as a sequence of image with the caption, image of the caption, image of the caption and this whole sequence kind of tells the story, right? So this is basically training it with, you know, maybe the first five pairs of images and captions in the sequence and it's trying to predict the future pairs of images and captions, right? And the green is training basically the adapter with the frozen language model and perhaps some fine-tuning of the language

**中文**

&gt;&gt; 是的。所以，在这种情况下，如果我们假设那个绿色长方框实际上已经能够把视觉输出嵌入相当好地映射到描述，那么，如果二者可以互换，仍然 stillting \[字幕不清\] 图像和描述的好处是什么？&gt;&gt; 呃，好问题。所以，基本上你是在问，alo \[字幕不清\]，所以，所以补充一下背景，这些数据集中的一些叫作视觉叙事数据集（visual storytelling datasets）。它们是由图像和描述、图像和描述、图像和描述组成的序列，而整个序列讲述了一个故事，对吧？所以，这基本上是在训练它，比如用序列中前五对图像和描述，让它尝试预测后续的图像和描述对，对吧？绿色部分基本上是在冻结语言模型的情况下训练 adapter，也可能对语言

### [30:15](https://www.youtube.com/watch?v=KlHIR7lT-mo&t=1815s) · b000037

**English**

model. So the benefits of keeping in both and keeping this redundancy is as we've shown here you know there are you could say stiff peaks eight y to stiff peaks right as the caption of what the the next baking stage should be but then obviously I I'm not a baker I don't know what that looks like right so you want the model to also have in the in the um in the context window the visual embedding of egg whites with stiff peaks so that clip as a decoder could decode and retrieve the nearest image that actually shows me um illustration of the image. Right? So in this case all of this is if you think about it it's in the van diagram the caption and the image are basically overlapping perfectly in the information. Right? But still sometimes it's useful because even though the text description of stiff peaks is here I don't visually know what that looks like and I need to visually know what it looks like to complete my

**中文**

模型做一些微调。所以，同时保留两者、保留这种冗余的好处，就像这里展示的，你知道，有，你可以说 stiff peaks，eight y to stiff peaks \[字幕不清\]，对吧，作为下一步烘焙阶段的描述，但显然，我，我不是烘焙师，我不知道那是什么样子，对吧？所以，你希望模型在，在，嗯，上下文窗口（context window）中，也拥有蛋白硬性发泡的视觉嵌入，这样，clip 作为解码器（decoder）就能解码并检索出最近的图像，真正向我展示，嗯，这个图像的示例。对吧？所以，在这种情况下，如果你想一下，在 van diagram \[字幕疑误，可能指 Venn diagram，维恩图\] 中，描述和图像所包含的信息基本上完全重叠。对吧？但有时这仍然很有用，因为尽管这里有 stiff peaks 的文字描述，我在视觉上却不知道它长什么样，而我需要在视觉上知道它长什么样，才能更好地完成我的

### [31:12](https://www.youtube.com/watch?v=KlHIR7lT-mo&t=1872s) · b000038

**English**

baking tasks better. So that's why you have this um redundancy going on in the model.&gt;&gt; Yeah.

**中文**

烘焙任务。所以，这就是模型中存在这种，嗯，冗余的原因。&gt;&gt; 是的。

### [31:25](https://www.youtube.com/watch?v=KlHIR7lT-mo&t=1885s) · b000039

**English**

&gt;&gt; Uh then it would not work. Yes. So so in this case, yes, it's retrieving from a large set of images. Um and it's specifically doing this like nearest neighbor, right? It's is taking in the the the context that LLM has seen so far that context embedding and is doing nearest neighbors over the image embeddings in the h database and retrieving the nearest one. Um but nowadays these databases are huge. So if you play with click you can you can actually generate and retrieve a lot of a lot of images. It can't be extremely out of distribution. Uh but you'd be surprised you know you have a million or trillion size image database. um you know the the extent and diversity of images there are there. We'll talk about gener generation after this. So you're not limited to to retrieval. I saw another hand somewhere.&gt;&gt; Yeah. Yeah.&gt;&gt; Is there a reason why direct image

**中文**

&gt;&gt; 呃，那就不行了。是的。所以，所以在这个例子中，是的，它是从大量图像中检索。嗯，而且具体做的是这种最近邻检索，对吧？它接收 LLM 到目前为止看到的上下文，也就是那个上下文嵌入，然后在 h database \[字幕不清\] 中的图像嵌入上进行最近邻搜索，检索最近的一个。嗯，但如今这些数据库很大。所以，如果你试试 click \[字幕疑误，可能指 CLIP\]，你实际上可以生成和检索很多、很多图像。它不能是极端分布外（out of distribution）的。呃，但你会惊讶的，你知道，当你有一个百万或万亿规模的图像数据库，嗯，你知道，里面图像的覆盖范围和多样性有多大。之后我们会讲生，生成。所以，你并不局限于检索。我刚才看到还有人举手。&gt;&gt; 是的。是的。&gt;&gt; 不存在直接图像

### [32:20](https://www.youtube.com/watch?v=KlHIR7lT-mo&t=1940s) · b000040

**English**

retrieval doesn't exist is because like stolen data?&gt;&gt; What do you mean by direct image retrieval? So like if I ask Chap uh you know wants a picture of a cat or something like that, it'll either generate one or do a search&gt;&gt; and give credit that way. But it definitely has put image embedding that paired with that context.&gt;&gt; So why is this not standard in uh chat fun? That's a good question. I'm not sure I have the exact answer. I think it might be um copyright attribution issue. Um but even then when when when models generate these images, there's a there's a potential issue of how much copyright is being infringed if you're if you're memorizing and

**中文**

检索，是不是因为，比如，数据是偷来的？&gt;&gt; 你说的直接图像检索是什么意思？就是，如果我问 Chap \[字幕疑误，可能指 ChatGPT\]，呃，你知道，想要一张猫的图片之类的，它要么生成一张，要么进行搜索 &gt;&gt; 然后以这种方式注明出处。但它肯定已经放入了与那个上下文配对的图像嵌入。&gt;&gt; 所以，为什么这不是 chat fun \[字幕疑误，可能指 ChatGPT\] 的标准功能？这是个好问题。我不确定自己有确切答案。我觉得可能是，嗯，版权归属标注的问题。嗯，但即便如此，当模型生成这些图像时，也有一个潜在问题：如果你在记忆并且

### [33:15](https://www.youtube.com/watch?v=KlHIR7lT-mo&t=1995s) · b000041

**English**

regenerating something. Um so some of these huge image caption databases I talk about one of them is called Lion 5B 5 billion pairs of text and images. It was used quite a bit over the past couple of years to train open source multimodal LLMs and to do retrieval. I think some of these models might even be have been trained on it. But then um they had to partially retract a big portion of the data set because it happened to have a lot of uh um sensitive images um some illegal images some some copyrighted images. So yeah there some some concerns with um large scale image text databases and retrieval.

**中文**

重新生成某些东西，究竟侵犯了多少版权。嗯，我讲到的一些大型图像描述数据库，其中一个叫 Lion 5B \[字幕疑误，可能指 LAION-5B\]，有 50 亿对文本和图像。过去几年，它被大量用于训练开源多模态 LLMs，也用于检索。我想，这些模型里有一些甚至可能用它训练过。但是，嗯，后来他们不得不部分撤回数据集中的很大一部分，因为里面碰巧有很多，呃，嗯，敏感图像，一些非法图像，还有一些受版权保护的图像。所以，是的，大规模图像文本数据库和检索确实存在一些问题。

### [34:01](https://www.youtube.com/watch?v=KlHIR7lT-mo&t=2041s) · b000042

**English**

Right now there's also some exciting work. I'll talk about generation next using like diffusion models but there's some exciting work in having a model generate an image which is obviously is new right that never existed before but also attributing the nearest five nearest neighbors that it has seen in the training data while um I was using while generating that image. So now you're able to do some form of um loosely copyright attribution. Okay. So that's by plugging in clip as an image retriever as the output. Uh naturally you can also plug in as I've motivated text to image generation methods. So again you have you have some uh some caption and some image. Maybe you just bake some cookies. Uh you took a photo of six of them and your caption is how should I display these at a farmers market? Right? So these are the

**中文**

现在也有一些令人兴奋的工作。接下来我会讲使用扩散模型（diffusion models）之类的方法进行生成，但也有一些很有意思的研究，让模型生成一张图像，显然它是新的，对吧，以前从未存在过，同时还标注出它在训练数据中见过的、最接近的五个最近邻，嗯，在我使用，在生成那张图像时。所以，现在你能够做某种，嗯，宽泛意义上的版权归属标注。好。所以，这就是把 clip 作为输出端的图像检索器接入。呃，很自然地，你也可以接入我刚才引出的 text-to-image generation 方法。所以，同样，你有一些，呃，一些描述和一张图像。也许你刚烤好一些饼干。呃，你拍了其中六块的照片，描述是：我应该如何在农夫市集上展示这些饼干？对吧？所以，这些就是

### [34:56](https://www.youtube.com/watch?v=KlHIR7lT-mo&t=2096s) · b000043

**English**

two inputs going into the model. LLM gives you some context and this context the model would first start thinking and outputting some context and obviously you want to visually see it right. So two options. One option is to get the image embeddings that the model generates and retrieve over a set of images like as you just saw using clip right given some image candidates score the image embeddings compute a similarity and find the nearest retrieved one. Another possibility is to take these uh the text or image embeddings and input that into a SD image decoder. SD in this case stands for state diffusion which I'll talk about more in a detail in detail. Uh but primarily what this model does is that it takes in textual descriptions and actually generates an image literally pixel by pixel for you corresponding to

**中文**

进入模型的两个输入。LLM 给你一些上下文，而这些上下文，模型会先开始思考，并输出一些上下文，显然你希望能直观地看到它，对吧？所以有两种选择。一种是获取模型生成的图像嵌入，然后在一组图像上进行检索，就像刚才看到的那样，使用 clip，对吧，给定一些候选图像，对图像嵌入评分、计算相似度，并找到检索结果中最近的那个。另一种可能是把这些，呃，文本或图像嵌入输入一个 SD 图像解码器。这里 SD 代表 state diffusion \[字幕疑误，可能指 Stable Diffusion\]，我会更详细地，详细地介绍。呃，不过，这个模型主要做的事情就是接收文本描述，并且真的逐像素为你生成一张图像，对应于

### [35:52](https://www.youtube.com/watch?v=KlHIR7lT-mo&t=2152s) · b000044

**English**

that input text. So this is might what the model might generate. So one form is the cookie stacked up and with a string wrapped around them and another one is the cookies kind of equally equally spaced out. And maybe the the person would then say, "Okay, I would prefer prefer the one where they're on a tray, a little bit of space between them, just prefer the generated image." So again, tons of cool examples. Um, you can look through some of these, but okay, so if you're looking for a tattoo, for example, I'm looking for some ideas for a good tattoo. What do you think looks good for for me? And the model might generate something. And you might say, I'm thinking about a sunflower that is on this part of the body and the model generates something else. And you can ask them more questions and it would then generate more. Right? So this is clearly an example where it's unlikely to uh have these images in the database given the amount of specificity and

**中文**

那个输入文本。所以，这可能就是模型会生成的内容。一种形式是把饼干叠起来，用绳子绑住；另一种则是把饼干均匀地，均匀地摆开。也许这个人接着会说：“好，我更喜欢，更喜欢放在托盘上、彼此之间留一点空隙的那个，就是更喜欢那张生成的图像。”所以，同样，有很多很酷的例子。嗯，你们可以看看其中一些，不过，好，比如你在找纹身，想找一些好看的纹身创意。你觉得什么适合我？模型可能会生成一些东西。然后你可能会说，我想要一朵向日葵，纹在身体的这个部位，模型就会生成另一个东西。你可以再问它更多问题，它就会生成更多。对吧？所以，这显然是一个数据库中不太可能存在这些图像的例子，因为这些提示词（prompts）输入了如此具体的

### [36:49](https://www.youtube.com/watch?v=KlHIR7lT-mo&t=2209s) · b000045

**English**

requirements that these prompts are are inputting. So uh generation can be very helpful. Uh here are some examples of you know like these design applications where you're trying to look for uh ideas to generate a custom birthday cake. So you have custom names and ages and designs. So the gener generative model can actually help you iterate through and come up with a good design. All right. Any questions about closing a loop? Now, we've seen models that are basically very flexible at multimodal interaction. You can talk to it, you can give it photos, you can uh have it reply back in text, have it reply back by retrieving and generating images. And most of these ideas are again the backbones of most of these state-of-the-art frontier models now, right? You have these multimodal representations, sequential representations of your contextual

**中文**

要求。所以，呃，生成会非常有帮助。呃，这里有一些例子，你知道，这类设计应用，你正在寻找，呃，定制生日蛋糕的创意。你有定制的姓名、年龄和设计。所以，生，生成模型实际上可以帮助你反复迭代，想出一个好的设计。好。关于闭合这个环，有什么问题吗？现在，我们已经看到一些模型，基本上可以非常灵活地进行多模态交互。你可以和它说话，可以给它照片，可以，呃，让它用文本回复，让它通过检索和生成图像来回复。而且，这些想法大多也正是如今最先进的前沿模型（frontier models）的骨干，对吧？你有这些多模态表征，对上下文

### [37:47](https://www.youtube.com/watch?v=KlHIR7lT-mo&t=2267s) · b000046

**English**

inputs. There's some adapting of language only models using the visual features and finally at the output side usually some text to image retrieval or generation model is being stapled and and further fine-tuned for image generation.

**中文**

输入的序列表征。使用视觉特征对纯语言模型进行一些适配，最后在输出端，通常会接上某种文本到图像检索或生成模型，并为图像生成进一步微调。

### [38:08](https://www.youtube.com/watch?v=KlHIR7lT-mo&t=2288s) · b000047

**English**

Okay. So now let's go into detail about how some of these generative models actually work. Right? seconds staying at a pretty high abstract level for these text to image generation models. Um so let's see how they actually exactly work. So nowadays they're very powerful. You can give it arbitrary captions different objects composed in different ways in various stylistic attributes and these models are generating very accurate images. Um this is a classic example an armchair in the shape of an avocado. went to IKEA the other day and they've actually started manufacturing chairs in the shapes of avocados perhaps inspired by these image generation models and nowadays of course you've seen um sort of the extensions from text to image to text to audio video

**中文**

好。现在我们来详细看看这些生成模型到底如何工作。对吧？seconds \[字幕不清\]，对于这些 text-to-image generation 模型，我们一直停留在相当高的抽象层次。嗯，所以来看看它们究竟具体如何工作。如今它们非常强大。你可以给出任意描述，不同物体以不同方式组合，带有各种风格属性，这些模型就能生成非常准确的图像。嗯，这是一个经典例子，一把牛油果形状的扶手椅。前几天去了 IKEA，他们居然已经开始制造牛油果形状的椅子了，也许就是受这些图像生成模型启发。如今，当然，你们也见过，嗯，从文本到图像扩展到文本到音频、视频

### [39:02](https://www.youtube.com/watch?v=KlHIR7lT-mo&t=2342s) · b000048

**English**

and more modalities right so at its core how do some of these approaches work so at a high level this is a rough schematic right there's usually three stages right you have the image uh text data that you're starting with, you know, as your large pre-training data is often a way of extracting features from these images. And often times, clip is used as a really good encoder, right? Because as we've seen, clip is already pre-trained to take in images and to take in captions and to bring them very close by embedding space. So these image features are not just image alone, but usually image aligned with text. So clip encoders usually are a really good powerful choice for encoders to learn these embeddings for images because they're already quite close to text. And that's important because in step two what you're going to do is you're going to take captions and you know pass these captions to some text encoder like a

**中文**

以及更多模态，对吧？那么，这些方法的核心是如何工作的？从高层次看，这是一个粗略示意图，对吧？通常有三个阶段，对吧？你首先有图像，呃，文本数据，你知道，作为大规模预训练数据，通常会有一种从这些图像中提取特征的方式。很多时候，clip 会被用作一个非常好的编码器，对吧？因为正如我们看到的，clip 已经预训练过，可以接收图像，也可以接收描述，并在嵌入空间（embedding space）中把它们拉得很近。所以，这些图像特征不只是图像本身，通常还是与文本对齐的图像。因此，clip 编码器通常是一个非常优秀、强大的选择，用来学习图像嵌入，因为这些嵌入已经和文本相当接近。这很重要，因为在第二步，你要做的是接收描述，然后，你知道，把这些描述传给某个文本编码器，比如一个

### [39:59](https://www.youtube.com/watch?v=KlHIR7lT-mo&t=2399s) · b000049

**English**

auto reggressive or language model get those features and map them into the corresponding image space right image embeddings right so this mapping is of course easier if these image embeddings were already quite close to the text embeddings that you started with so that's the mapping uh usually it's some auto reggressive model that does is mapping and finally you need to close the loop and generate new images. So you need a decoder decoder that takes in some of these embeddings and actually outputs pixel wise the entire image and it raw pixels. So those are the three main steps in in these text to image models. So what are each of these individual steps? So firstly we'll talk some about this like clip encoder u there's several approaches some of them start with clip some of them start with VAE like I think I've seen clip being the more more

**中文**

自回归（autoregressive）模型或语言模型，得到这些特征，并把它们映射到相应的图像空间，对吧，图像嵌入，对吧？所以，如果这些图像嵌入本来就和你起初的文本嵌入很接近，这个映射当然会更容易。这就是映射，呃，通常是某个 autoregressive 模型完成这个映射。最后，你需要闭合这个环，生成新的图像。所以，你需要一个解码器，解码器接收这些嵌入中的一些，并真正逐像素输出整张图像，以及它的原始像素。这就是这些 text-to-image 模型中的三个主要步骤。那么，每个具体步骤是什么？首先，我们会讲一些像 clip 编码器这样的东西，呃，有几种方法，有些从 clip 开始，有些从变分自编码器（VAE）开始，我觉得我见到 clip 用得更，更

### [40:56](https://www.youtube.com/watch?v=KlHIR7lT-mo&t=2456s) · b000050

**English**

dominant used once but one key difference even if they do use clip is that they want to do what we call this discretization of the image embedding space right so you often take in these images pass them through clip and you have a decoder instead of having these as continuous features usually some quantization some clustering is done so that you convert them into discrete tokens right things like 98 3990 uh you might have seen VQ VIE uh same quantization approaches are applied to clip embeddings as well right this is often very useful because as you'll see later if you want to map text into this space it's often much easier to map text into these discrete tokens, then map them into highdimensional continuous tokens. There are 700 dimensional for example, it's very hard to predict highdimensional continuous

**中文**

普遍，但一个关键区别是，即使它们使用 clip，也希望进行我们所说的图像嵌入空间离散化（discretization），对吧？所以，你通常接收这些图像，把它们传过 clip，并且有一个解码器，不是把它们保留为连续特征，而是通常会做一些量化（quantization）、一些聚类（clustering），把它们转成离散 token（discrete tokens），对吧？像 98、3990 这样的东西。呃，你可能见过 VQ VIE \[字幕疑误，可能指 VQ-VAE\]，同样的量化方法也会用到 clip 嵌入上，对吧？这通常很有用，因为你稍后会看到，如果你想把文本映射到这个空间，把文本映射成这些离散 token，通常比把它们映射成高维连续 token 容易得多。比如，它们是 700 维的，很难预测高维连续

### [41:53](https://www.youtube.com/watch?v=KlHIR7lT-mo&t=2513s) · b000051

**English**

tokens. Whereas for discrete tokens, all you got to do is define a a cross entropy loss or classification loss to classify which of those discrete tokens they belong to. So some tokenization is going to go on. Uh you can think about it. Usually these token embedding sizes are 8,000 8192 power of two. Each digit can be thought of as a visual token and then a multiple of these visual tokens. So if that is a set of visual tokens for this cat image, uh another another house image might be a different set of visual tokens, right? Then these models are trained to take in learn these embeddings with a quantization set and then decode uh the image. And of course, a decoded version might be a a blurriier version of the original image because no reconstruction is going to be perfect. Yeah.

**中文**

token。而对于离散 token，你只需要定义一个交叉熵损失（cross entropy loss）或分类损失（classification loss），来判断它们属于哪个离散 token。所以，这里会进行某种 token 化（tokenization）。呃，你可以这样理解。通常这些 token 嵌入的规模是 8,000、8192，2 的幂。每个数字都可以看作一个视觉 token（visual token），然后由多个这样的视觉 token 组成。所以，如果这是一张猫图像对应的一组视觉 token，呃，另一张，另一张房子的图像可能对应另一组视觉 token，对吧？然后，这些模型经过训练，接收、学习这些带量化集合的嵌入，再解码，呃，图像。当然，解码后的版本可能比原始图像更模糊一些，因为没有任何重建会是完美的。是的。

### [42:47](https://www.youtube.com/watch?v=KlHIR7lT-mo&t=2567s) · b000052

**English**

A visual token is just any like a text token is basically a number between zero and 70,000, right? Because it's 70,000 vocap size. In this case, a visual token has a 8,000 vocap size. The visual token is just one of one discrete number within that set. token as a one to one app.&gt;&gt; No. So um in more detail there's some clustering going on. So in fact there's been many continuous embeddings that when they're clustered they belong to one visual token which is you can think of it as a cluster center. And of course you need to hope that it generalizes to a new embedding. Right? The new embedding gets gets clustered within there that same cluster. It should be mapped to the same cluster center.

**中文**

视觉 token 就是任意一个，像文本 token 基本上就是零到 70,000 之间的一个数字，对吧？因为词表（vocabulary）大小是 70,000。在这个例子里，视觉 token 的词表大小是 8,000。视觉 token 就是那个集合里的一个离散数字。token 是一对一的 app \[字幕疑误，可能指 mapping，映射\]。&gt;&gt; 不是。所以，嗯，更详细地说，这里会进行一些聚类。事实上，有许多连续嵌入，在聚类之后会归属于同一个视觉 token，你可以把它看作一个聚类中心（cluster center）。当然，你需要希望它能够泛化到一个新的嵌入。对吧？新的嵌入被，被聚到那里，那个相同的簇中。它应该映射到同一个聚类中心。

### [43:35](https://www.youtube.com/watch?v=KlHIR7lT-mo&t=2615s) · b000053

**English**

So these visual embeddings are often often clustered. So you have these discrete tokens which makes step two much easier. And as you recall step two what's happening is that you're basically taking in text for example armchair in the shape of an avocado uh through some text embedding and predicting the visual tokens corresponding to that input caption. Right? This is from paired data. Right? you're going to and these have some amount of paired data that has this text. It has this image and it's predicting what the visual tokens are for that image. And this is posed as an auto reggressive problem. So it comes in you predict the first visual token which is 56 and then you take in 56 you put next visual token which is 73 next visual token and so on. So this is the part that maps text inputs into I mean basically you can do with LLM nowadays you can just predict

**中文**

所以，这些视觉嵌入经常，经常会被聚类。这样，你就有了这些离散 token，使第二步容易得多。你们应该记得，第二步基本上是在接收文本，比如“牛油果形状的扶手椅”，呃，经过某种文本嵌入，并预测与这个输入描述对应的视觉 token。对吧？这来自配对数据（paired data）。对吧？你要，这些有一定数量的配对数据，其中有这段文本，也有这张图像，模型要预测这张图像的视觉 token 是什么。而这被设定为一个自回归问题。所以，输入进来，你预测第一个视觉 token，是 56，然后接收 56，给出下一个视觉 token，是 73，再下一个视觉 token，依此类推。所以，这部分把文本输入映射到，我的意思是，现在基本上可以用 LLM 来做，你可以直接预测

### [44:31](https://www.youtube.com/watch?v=KlHIR7lT-mo&t=2671s) · b000054

**English**

and finetun a model to predict each of these visual tokens one by one. So we've seen encoder of image into this set of discrete visual tokens. We've seen mapping text to these visual tokens. And finally the third stage is a decoder. So taking in these visual tokens and then actually decoding the image. So that basically completes the story, right? You have the clip encoder maps images into visual tokens. You have the model that takes in text and predicts the corresponding visual tokens. And finally you have something that takes in the visual tokens and decodes the image. And that basically means for a new caption that you put in, it's going to go through the text encoder, try to predict what the visual tokens will be for that new caption, and decode what

**中文**

并微调一个模型，让它逐个预测这些视觉 token。所以，我们看到了把图像编码为这组离散视觉 token 的编码器。我们看到了把文本映射到这些视觉 token。最后，第三阶段是一个解码器。也就是接收这些视觉 token，然后真正解码出图像。所以，这基本上就把整个过程补全了，对吧？clip 编码器把图像映射成视觉 token。有一个模型接收文本，并预测相应的视觉 token。最后，有一个东西接收视觉 token，并解码图像。这基本上意味着，对于你输入的一条新描述，它会经过文本编码器，尝试预测这条新描述对应的视觉 token，然后解码出

### [45:26](https://www.youtube.com/watch?v=KlHIR7lT-mo&t=2726s) · b000055

**English**

the image will be for those predicted visual tokens. Yeah,

**中文**

这些预测出的视觉 token 对应的图像会是什么样子。是的，

### [45:42](https://www.youtube.com/watch?v=KlHIR7lT-mo&t=2742s) · b000056

**English**

&gt;&gt; actually most of these are what a clip encoder you will pre-train it often. Uh diffusion model you often also pre-train it and some of these types encoder elements are also pre-trained. So ideally you just use a limited amount of data that has uh and all of these can be trained using well cliff encoder will be pre-trained using image and text data. The text encoder will be pre-trained using text only data. Diffusion models as we'll see later can be also trained using image only data. So afterwards you just want some hair amount of text and images. So you can fine-tune this mapping from the text encoder into the visual tokens. So, it's really leveraging the best use of um of of the best pre-trained models. And honestly, that's been the story. You know, when these textto image models first came out, there was a VAE here. So, VAE encoder decoder. I'll talk about VA in a second.

**中文**

&gt;&gt; 实际上，大多数这些是，一个 clip 编码器，你通常会预训练它。呃，diffusion model 通常也会预训练，一些这样的编码器组件也经过预训练。所以，理想情况下，你只需要使用有限数量的数据，其中有，呃，而且这些都可以用，好，cliff encoder \[字幕疑误，可能指 CLIP encoder\] 会用图像和文本数据预训练。文本编码器会用纯文本数据预训练。Diffusion models，正如稍后会看到的，也可以只用图像数据训练。所以，之后你只需要一些 hair amount \[字幕疑误，可能指 paired amount，配对数量\] 的文本和图像。这样，就可以微调从文本编码器到视觉 token 的这个映射。所以，这实际上是在尽量充分利用，嗯，最好的预训练模型。坦率地说，发展过程就是这样。你知道，这些 text-to-image 模型刚出来时，这里是一个 VAE。所以，是 VAE 编码器和解码器。我一会儿会讲 VA \[字幕疑误，可能指 VAE\]。

### [46:40](https://www.youtube.com/watch?v=KlHIR7lT-mo&t=2800s) · b000057

**English**

More specifically, was a vector quantized VAE. And this is another model. And everything was trained together, which made it very complex. Uh took a lot of time and results weren't super good, right? Right? And then one by one each of these encoder decoders became replaced by pre-trained models. Now you first replaced the VAE encoder with a clip encoder and pre-train. You then replace the VA decoder with a pre-trained diffusion model and that was pre-trained and then as these LLMs get upgraded you can also start upgrading these uh text encoders. So that that's a lot of the tricks that took it from stable diffusion one to two to three.&gt;&gt; Yeah. You should just repeat that&gt;&gt; for the first place and if you were to change size of that would improve our resolution.&gt;&gt; Yeah. So the intuition is that okay so now you have to map basically text into the image embedding. You want to find a

**中文**

更具体地说，是一个向量量化 VAE（vector quantized VAE）。而这是另一个模型。所有东西都一起训练，因此非常复杂。呃，花了很多时间，结果也不是特别好，对吧？对吧？后来，这些编码器和解码器一个接一个地被预训练模型替代。首先，你用 clip 编码器替换 VAE 编码器，并进行预训练。然后，用预训练的 diffusion model 替换 VA \[字幕疑误，可能指 VAE\] 解码器，而那个也经过预训练；再然后，随着这些 LLMs 升级，你也可以开始升级这些，呃，文本编码器。所以，这就是从 stable diffusion 一到二再到三过程中用到的许多技巧。&gt;&gt; 是的。您能重复一下 &gt;&gt; 第一个地方，如果改变它的大小，会提高我们的分辨率吗？&gt;&gt; 是的。所以，直觉是，好，现在你基本上需要把文本映射到图像嵌入。你想找到一个

### [47:38](https://www.youtube.com/watch?v=KlHIR7lT-mo&t=2858s) · b000058

**English**

corresponding image embedding representing that text. Often times if you want to predict an embedding if that embedding is high dimensional and continuous say it's like you know a standard 700 dimensional vector continuous these embeddings are very hard to predict right you'll try you can try using like MSE loss or MAE loss to predict it but often times the issue with MSAE is that they often just learn the average of all the dimensions instead of actually learning the uh the exact numbers themselves. So continuous highdimensional embeddings are super hard to predict, right? So whenever you see any any model that tries to generate or predict images or audio or embeddings, they all quantize the continuous embeddings into a set of discrete clusters first, say 8,000, right? So that can be done using K means clustering with a cluster of size of 8,000 and then instead of predicting the continuous embedding, you just predict

**中文**

表示那段文本的对应图像嵌入。通常，如果你想预测一个嵌入，而这个嵌入是高维且连续的，比如，你知道，一个标准的 700 维连续向量，那么这些嵌入就很难预测，对吧？你会尝试，可以尝试使用均方误差损失（MSE loss）或平均绝对误差损失（MAE loss）来预测，但 MSAE \[字幕疑误，可能指 MSE/MAE\] 的问题往往是，它们通常只学到所有维度的平均值，而不是实际学到，呃，具体数值本身。所以，连续的高维嵌入特别难预测，对吧？因此，每当你看到任何，任何尝试生成或预测图像、音频或嵌入的模型，它们都会先把连续嵌入量化成一组离散的簇，比如 8,000 个，对吧？这可以用 K means clustering（K 均值聚类）来完成，簇的数量为 8,000；然后，你不再预测连续嵌入，而只预测

### [48:36](https://www.youtube.com/watch?v=KlHIR7lT-mo&t=2916s) · b000059

**English**

the cluster ID corresponding to that embedding. So it becomes a 8,000way classification with a 8,000 dimensional softmax instead of regressing 700 dimensional continuous outputs. Um, we talked about this a little bit last week with the vector quantized uh models. Um, so I have some slides from it last week on it. I think it was during the the uh the multimodal language models part.

**中文**

与那个嵌入对应的簇 ID（cluster ID）。所以，它变成了一个使用 8,000 维 softmax 的 8,000 类分类问题，而不是回归 700 维的连续输出。嗯，上周讲向量量化模型时，我们稍微讨论过这个。嗯，所以，上周有一些关于它的幻灯片。我想是在，呃，多模态语言模型那一部分。

### [49:12](https://www.youtube.com/watch?v=KlHIR7lT-mo&t=2952s) · b000060

**English**

Okay. Any further questions? Great. All right. So, so that again that stayed at a pretty high level. So that gave you the kind of general schematic of these text to image models. I want to spend some time \[clears throat\] going into some technical detail of some of these modern generative models. Um I I'll see what I can cover today. It's again not the main point of the course. The main point of the course is kind of knowing about these multimodal models and of course be good at some technical detail about how for example VAEs and diffusion models actually operate if you don't have already. Um but again not meant to go into all the detail if it's interesting to you there are entire courses tutorials seminars on this okay but at a high level at a crash course uh when we say generative model what we

**中文**

好。还有其他问题吗？很好。好。所以，所以刚才仍然是相当高层次的介绍。它给了你们这些 text-to-image 模型的大致整体示意。我想花些时间 \[清嗓子\]，深入讲一些现代生成模型的技术细节。嗯，我，我看看今天能讲多少。这仍然不是这门课的重点。这门课的重点是了解这些多模态模型，当然，如果你还不了解，掌握一些技术细节也很好，比如 VAEs 和 diffusion models 究竟如何工作。嗯，但再次说明，这里不打算讲所有细节。如果你感兴趣，有完整的课程、教程和研讨课专门讲这些，好吧。不过，从高层次、以速成介绍的方式来说，当我们说生成模型时，我们

### [50:08](https://www.youtube.com/watch?v=KlHIR7lT-mo&t=3008s) · b000061

**English**

usually mean is that we want to model P of X right where X is the data that you're trying to generate X could be text images video multimodal data going to model P of X so everything that was classification was about P of Y given X right a label given given uh some input data. But now I want to model P of X. Uh often times the most important thing we have to choose is how do I give a parametric form to P of X, right? Is it a as simple as a Gaussian? Is it uh is there some independence or some factorization or is there some model that I can use to like a neuronet network to output P of X? So usually the model to parameterize P of X is very important. Once you define that a general strategy is to maximize likelihood which basically says if I have real data X like a real image can I maximize P of that image right when I put that X into the model that should

**中文**

通常指的是，我们想对 P of X 建模，对吧？其中 X 是你想生成的数据，X 可以是文本、图像、视频、多模态数据。要对 P of X 建模。所以，之前所有分类任务都是关于 P of Y given X，对吧？给定，给定，呃，一些输入数据时，某个标签的概率。但现在我想对 P of X 建模。呃，很多时候，最重要的选择是，我如何为 P of X 指定一个参数化形式（parametric form），对吧？它可以简单到只是一个高斯分布（Gaussian）吗？它是否，呃，存在某种独立性（independence）或某种因子分解（factorization），或者有没有某个模型可以使用，比如神经网络（neural network），来输出 P of X？所以，通常用于参数化 P of X 的模型非常重要。定义好之后，一个通用策略是最大化似然（maximize likelihood），基本上就是说，如果我有真实数据 X，比如一张真实图像，能不能最大化这张图像的 P，对吧？当我把那个 X 放入模型时，它应该

### [51:04](https://www.youtube.com/watch?v=KlHIR7lT-mo&t=3064s) · b000062

**English**

score very high on P of X and if I put a fake image or random noise it should score very low on P of X so roughly this P of X should correspond to your space your distribution of data right you have to define what that shape is that's the model you have for P of X and then you're basically maximizing likelihood by taking in points X and scoring them and maximizing the corresponding P of X for those real valued data. And of course if you have that you also may want to evaluate. So given a new X can I evaluate what P of X is? It should be high for real realistic looking data and low for fake looking data. And of course you might want to sample new P of X, right? So this P of X should be easy to sample from, right? Gaussians are easy to sample from. Mixtures of Gaussians are easy to sample from. When you start using neural networks to define P of X, there might be some difficulties to sample from it. Right? So you want to sample new X again according to regions of high likelihood.

**中文**

在 P of X 上得到很高的分数；而如果我放入一张假图像或随机噪声，它在 P of X 上的分数就应该很低。所以，大致来说，这个 P of X 应该对应你的空间、你的数据分布，对吧？你必须定义它的形状是什么，这就是你为 P of X 建立的模型。然后，你基本上通过接收数据点 X、为它们评分，并最大化这些实值数据对应的 P of X 来最大化似然。当然，如果有了这个，你可能还想进行评估。那么，给定一个新的 X，我能否评估 P of X 是多少？对于真实、看起来逼真的数据，它应该很高；对于看起来假的数据，它应该很低。当然，你可能还想采样新的 P of X，对吧？所以，这个 P of X 应该容易从中采样，对吧？高斯分布很容易采样。高斯混合（mixtures of Gaussians）也很容易采样。当你开始用神经网络定义 P of X 时，从中采样可能会有一些困难。对吧？所以，你希望再次根据高似然区域来采样新的 X。

### [52:01](https://www.youtube.com/watch?v=KlHIR7lT-mo&t=3121s) · b000063

**English**

Right? So that means sampling realistic images and not sampling unrealistic images that look like noise. Often times generation is not just useful for making pretty images. Usually when you start learning P of X, it can also be thought of as a form of unsupervised representation learning, right? Usually ideally this P of X should model the variations in your data, model the clusters in your data, model the hierarchy in your data so that you can actually use it to learn and fine-tune it for downstream tasks. That's why nowadays we've really seen these like generative models that learn P of X and fine-tune discrimin discrimination models, classification models really converging, right? So you can start learning P of X using generative models then fine-tune it for downstream representations.

**中文**

对吧？这意味着采样出逼真的图像，而不是采样出看起来像噪声的不真实图像。很多时候，生成不只是用来制作漂亮的图像。通常，当你开始学习 P of X 时，也可以把它看作一种无监督表征学习（unsupervised representation learning），对吧？通常，理想情况下，这个 P of X 应该对数据中的变化建模，对数据中的簇建模，对数据中的层级结构建模，这样你实际上就能用它进行学习，并针对下游任务微调它。这就是为什么如今我们确实看到，这些学习 P of X 的生成模型，以及微调判，判别模型（discriminative models）、分类模型，正在真正融合，对吧？所以，你可以先用生成模型学习 P of X，再针对下游表征进行微调。

### [52:55](https://www.youtube.com/watch?v=KlHIR7lT-mo&t=3175s) · b000064

**English**

Of course nowadays we also care about not just P of X but often P of X given C. That means conditional generation. So if I want to condition it on a caption, I want P of images given a particular caption. I don't want just P of red any random image. Um so C can be a category, it can be uh text, it can be another modality and more. And sometimes you also care about style transfer. So I might want to care about modeling T of X2 given X1 and C. So X1 might be an image that I already gave you and C might be a instruction to change the background or to change the artistic style and I want to see a new image sampled according to that change.

**中文**

当然，如今我们关心的不只是 P of X，往往还包括 P of X given C。这意味着条件生成（conditional generation）。所以，如果我想以一条描述为条件，我想要的是给定某个特定描述时图像的 P。我不想只是 P of red \[字幕不清\]，任意一张随机图像。嗯，所以，C 可以是一个类别，可以是，呃，文本，可以是另一种模态，等等。有时你还关心风格迁移（style transfer）。所以，我可能关心对 T of X2 given X1 and C \[字幕疑误，T 可能指 P\] 建模。X1 可能是我已经给你的一张图像，C 可能是一条更改背景或更改艺术风格的指令，而我想看到按照那个变化采样出的一张新图像。

### [53:41](https://www.youtube.com/watch?v=KlHIR7lT-mo&t=3221s) · b000065

**English**

Okay. So starting with uh several very popular generative models. Most of these generative models when we think about X which is the raw data we also usually think about these latent variables which we call Z right so the key intuition behind these latent variables is that X the space of data is so large and you think about these human faces the space is so large there's actually several key variables that you want to independently separately capture right one might be the color of the hair one might be uh the age of the person one might be wearing the person is wearing glasses or not. Right? So these cannot be seen as latent variable Z. Right? So ideally you want to learn P of X but also implicitly learn all these different combinations of Z and how they affect your generation of images X. Right? Uh of course a big challenge is that Z is often latent which means that you don't usually

**中文**

好。先从，呃，几种非常流行的生成模型讲起。对于大多数生成模型，当我们考虑 X，也就是原始数据时，通常也会考虑这些潜变量（latent variables），我们称之为 Z，对吧？这些潜变量背后的关键直觉是，X，也就是数据空间，非常庞大。想想这些人脸，空间非常庞大，但实际上有几个关键变量，你希望独立地、分别地捕捉，对吧？一个可能是头发颜色，一个可能是，呃，这个人的年龄，一个可能是戴着，这个人有没有戴眼镜。对吧？所以，这些不能被看作潜变量 Z。对吧？因此，理想情况下，你想学习 P of X，同时隐式地学习 Z 的所有这些不同组合，以及它们如何影响你生成图像 X。对吧？呃，当然，一个很大的挑战是，Z 通常是潜在的，意味着你通常不会

### [54:37](https://www.youtube.com/watch?v=KlHIR7lT-mo&t=3277s) · b000066

**English**

observe it. If you have all these images it's very hard to go in and label. They're wearing glasses. They're not they have dark hair. They have short hair long hair. very hard to annotate all the Z. That's why we often call them latent variables. And the goal is to kind of discover them through the generative model instead of having labels for them. So some of you might have started seeing these latent variable models. So Z2X where Z could be no different color of the eye of the hair of the pose and then together each of these Z variables uh allow you to generate your image X. Right? So in graphical model form, this is basically what we call a directed as cyclic graph. And you can see that there might be also be multiple levels to this graph that essentially tells how these latent variables are are organized.

**中文**

观察到它。如果你有所有这些图像，要逐一标注非常困难。他们戴着眼镜。他们没有，他们有深色头发。他们有短发、长发。很难标注所有的 Z。这就是为什么我们通常称它们为潜变量。目标是通过生成模型发现它们，而不是为它们提供标签。所以，你们有些人可能已经开始接触这些潜变量模型（latent variable models）。也就是 Z2X，其中 Z 可以是，不同的眼睛颜色、头发颜色、姿态，然后这些 Z 变量共同，呃，让你生成图像 X。对吧？用图模型（graphical model）的形式表示，这基本上就是我们所说的 directed as cyclic graph \[字幕疑误，可能指 directed acyclic graph，有向无环图\]。你可以看到，这个图也可能有多个层级，基本上说明这些潜变量是如何组织的。

### [55:32](https://www.youtube.com/watch?v=KlHIR7lT-mo&t=3332s) · b000067

**English**

So using this intuition, I mean the most simple generative model but still of course very relevant today is a mixture of Gaussians where Z might just be K variables, right? K latent variables and at each location of these latent variables um X P of X given Z is just some Gaussian distribution. So that's why in this case K is three, right? There may be K different options for long hair, short hair, no hair, right? That might be what K Z represents. There's three possibilities for type of hair. And then the data distribution of X given each of these is just one Gaussian which is basically that circle different mean and variance which can be different for each of your Z's, right? So that can be a very simple generative model, right? So how do you how do you learn this? Well, ideally you want have

**中文**

所以，利用这个直觉，我的意思是，最简单、但今天当然仍然很相关的生成模型，就是高斯混合，其中 Z 可能只是 K 个变量，对吧？K 个潜变量，而在这些潜变量的每个位置上，嗯，X，P of X given Z 就是某个高斯分布。所以，在这个例子里 K 是三，对吧？可能有 K 种不同选项：长发、短发、没有头发，对吧？这可能就是 K，Z 所表示的内容。头发类型有三种可能。然后，给定其中每一种时，X 的数据分布就是一个高斯分布，基本上就是那个圆，具有不同的均值（mean）和方差（variance），每个 Z 的均值和方差都可以不同，对吧？所以，这可以是一个非常简单的生成模型，对吧？那么，你如何，如何学习它？理想情况下，你希望有

### [56:29](https://www.youtube.com/watch?v=KlHIR7lT-mo&t=3389s) · b000068

**English**

data like this and you want to first identify that you know there are actually three uh settings for your latent variables as there three kind of clusters in your data and then sorry for each of these clusters you want to figure out that there is a particular mean and a particular variance. So if I want to generate new data I can always just pick one setting of Z. You can just specify I want to generate the person with long hair, short hair or no hair and then go into that Gaussian corresponding to one, two or three and then sample from that Gaussian. Very easy to sample from Gaussian distributions. Yeah.

**中文**

像这样的数据，首先识别出，你知道，你的潜变量实际上有三种，呃，取值，因为数据中有三类簇。然后，抱歉，对于每个簇，你都想确定它有一个特定的均值和特定的方差。所以，如果我想生成新数据，就可以随时选择 Z 的一个取值。你可以直接指定，我想生成一个长发、短发或者没有头发的人，然后进入对应一、二或三的那个高斯分布，再从那个高斯分布中采样。从高斯分布中采样非常容易。是的。

### [57:11](https://www.youtube.com/watch?v=KlHIR7lT-mo&t=3431s) · b000069

**English**

&gt;&gt; And you could base you also base by color.&gt;&gt; Yeah. As many as you want. as many as you want. Um, basically this becomes a hyperparameter in machine learning, right? Just like how many layers in your model, how many Z's, how the Zs are structured, that's going to be a hyperparameter. Often helps to in this case do PCA visualize your data, understand how many clusters might be there as a way of choosing choosing how many Z's and the dimensionality of each Z. Another way of course is to do your classic cross validation. So in this case the metric is P of X, right? So how well is my data being fit by this mixture of Gaussians? Is my P of X high or low? That's kind of the accuracy metric. So I can train on a training set evaluate on a test set how high the P of X is. And does it actually assign high P

**中文**

&gt;&gt; 而且你也可以根据，也可以根据颜色。&gt;&gt; 是的。想要多少就多少。想要多少就多少。嗯，基本上，这就成了机器学习中的一个超参数（hyperparameter），对吧？就像模型里有多少层、有多少个 Z、这些 Z 如何组织，这些都会是超参数。在这个例子里，做主成分分析（PCA）来可视化数据，了解可能有多少个簇，通常会有帮助，可以据此选择，选择有多少个 Z，以及每个 Z 的维度。另一种方法，当然，是经典的交叉验证（cross validation）。这里的指标是 P of X，对吧？我的数据被这个高斯混合拟合得有多好？我的 P of X 是高还是低？这有点像准确率指标。所以，我可以在训练集上训练，再在测试集上评估 P of X 有多高。它是否真的会给我看到的新数据点分配高的 P

### [58:07](https://www.youtube.com/watch?v=KlHIR7lT-mo&t=3487s) · b000070

**English**

of X to new data points that I see? That should be really high, right? Does it assign low P of X to noise which are unreal images? So you still have these, you know, you can still have these notions of training and testing and cross validation to tune your hyperparameters.&gt;&gt; Yeah, I think that's on like the type of distribution like you mentioned Gaussian. Is there any things that should like be careful of um like not assuming Gaussian?&gt;&gt; Very nice question. Um yes, images continuous data very well suited for Gausians. In fact, as we'll see later, if you start, you know, approximating and encoding with neuronet networks first to get features, almost most features are ging distributed in their continuence. Big change happens when you start applying generative models to text, right? Uh text tokens doesn't mean anything to add a Gaussian to to a

**中文**

of X？那应该非常高，对吧？它是否给噪声，也就是不真实的图像，分配低的 P of X？所以，你仍然有这些，你知道，仍然可以用训练、测试和交叉验证这些概念来调整超参数。&gt;&gt; 是的，我想问的是分布的类型，比如您提到高斯分布。有没有什么需要小心的地方，嗯，比如不要假设它是高斯分布？&gt;&gt; 非常好的问题。嗯，是的，图像、连续数据非常适合高斯分布。事实上，正如后面会看到的，如果你开始，你知道，先用神经网络近似和编码来获取特征，几乎大多数特征在它们的 continuence \[字幕不清\] 中都是 ging distributed \[字幕疑误，可能指 Gaussian distributed，呈高斯分布\] 的。大的变化发生在你开始把生成模型应用到文本时，对吧？呃，对于文本 token，给一个字符或一个 token 嵌入加上高斯分布并没有什么意义。

### [59:03](https://www.youtube.com/watch?v=KlHIR7lT-mo&t=3543s) · b000071

**English**

character or to a token embedding. Uh then you have to start going to discrete uh distributions. So in this case you also see the two types of distributions right Z know representing your latent variables was categorical right because in this case there's long short no hair of course you could have also changed that to to a Gaussian right length of hair right you could have a Gaussian that's centered at 10 and had mean variance or you could have uniform distribution over over hair length depending on what you assume to be the the state of the world so z can change right but if if both are g if z is Gaussian and then each of the X given Z is also Gaussian. It's still quite easy to solve. If Z is something else and then X given Z is a different distribution, there might be some computational issues in solving them.

**中文**

呃，然后你就得开始转向离散分布（discrete distributions）。所以，在这个例子里，你也能看到两类分布，对吧？表示潜变量的 Z，你知道，是类别型的（categorical），对吧？因为这里有长发、短发、没有头发。当然，你也可以把它改成高斯分布，对吧？头发长度，对吧？你可以有一个以 10 为中心、带有均值方差的高斯分布，也可以在头发长度上使用均匀分布（uniform distribution），这取决于你对世界状态的假设。所以，z 可以变，对吧？但是，如果两者都是 g，如果 z 是高斯分布，而每一个 X given Z 也是高斯分布，求解仍然相当容易。如果 Z 是其他分布，而 X given Z 又是另一种分布，求解时可能就会有一些计算问题。

### [59:56](https://www.youtube.com/watch?v=KlHIR7lT-mo&t=3596s) · b000072

**English**

So that's mixture of Gaussians. Um mixture of gaussians are fairly easy to solve. There are classic algorithms for this. Expectation maximization is one of them. You might have seen it in clustering in machine learning classes, but essentially you alternate between two steps, right? First, you're going to use the mean and variance of each of your three Gaussians that you have learned to basically assign each point to the nearest Gaussian. Right? If I know the mean and variance, so that basically means I know where the three circles are. It's basically just placing each data point into those Gaussians. So that tells you P of Z, right? the distribution of each point within those Gaussians. And then once I have done that clustering step, which is to assign each point to one of those three Gaussians, then I can readjust the mean and variance of those Gaussians based on the points that were assigned to it. Right? That is just a mean estimation by taking an average of the points in the

**中文**

所以，这就是高斯混合。嗯，高斯混合相当容易求解。有一些经典算法。期望最大化（Expectation maximization，EM）就是其中之一。你可能在机器学习课的聚类部分见过，但基本上，你是在两个步骤之间交替，对吧？首先，使用已经学到的三个高斯分布各自的均值和方差，基本上把每个数据点分配到最近的高斯分布。对吧？如果我知道均值和方差，基本上就意味着我知道那三个圆在哪里。这基本上就是把每个数据点放入那些高斯分布。因此，这会告诉你 P of Z，对吧？每个点在这些高斯分布中的分布情况。然后，一旦完成这个聚类步骤，也就是把每个点分配到三个高斯分布中的一个，我就可以根据分配给它们的数据点，重新调整那些高斯分布的均值和方差。对吧？均值估计就是取那个高斯分布中数据点的平均值，

### [1:00:53](https://www.youtube.com/watch?v=KlHIR7lT-mo&t=3653s) · b000073

**English**

Gaussian and the variance estimation by taking the variance of the points assigned to that Gaussian. Right? So you're essentially alternating by making all your data points, assigning it to the current three Gaussians based on what the means and variances are. You've done that assignment. That's the expectation step. Then you update the means and variances according to the points assigned to those Gaussians. And you do this until you've converged. Then your data is well clustered. They're assigned to the right Gaussian. And each Gaussian has also learned the right parameters, the right mean and variances. Yes.

**中文**

方差估计则是计算分配给那个高斯分布的数据点的方差。对吧？所以，你基本上是在交替进行：根据当前的均值和方差，把所有数据点分配到目前的三个高斯分布中。你完成了这个分配。这就是期望步骤（expectation step）。然后，根据分配给这些高斯分布的数据点，更新均值和方差。一直这样做，直到收敛。然后，你的数据就被很好地聚类了。它们被分配到了正确的高斯分布。每个高斯分布也学到了正确的参数、正确的均值和方差。是的。

### [1:01:30](https://www.youtube.com/watch?v=KlHIR7lT-mo&t=3690s) · b000074

**English**

every four everyone be in that gion. So why are you choosing which g?&gt;&gt; Uh so in this case so the example we gave was Z was like length of hair right long hair short hair no hair. So no hair there was a Gaussian short hair there was a Gaussian long hair there was a Gaussian right? So of course there could also be points that fell into multiple clusters, right? Or they had the boundary between between clusters. That's also also possible. And technically because of these Gaussians, there going to be a density of each point for all three Gaussians, right? Because Gaussian densities are non zero. So they have a likelihood in each of the Gaussians just which one is higher or lower. Any other questions?

**中文**

每四个，每个人都在那个 gion \[字幕疑误，可能指 Gaussian\] 中。所以，为什么要选择哪个 g？&gt;&gt; 呃，在这个例子里，我们举的例子是，Z 类似于头发长度，对吧，长发、短发、没有头发。所以，没有头发对应一个高斯分布，短发对应一个高斯分布，长发对应一个高斯分布，对吧？当然，也可能有数据点落入多个簇，对吧？或者位于簇与簇之间的边界上。这也，也是可能的。而且，从技术上说，由于这些是高斯分布，每个点在所有三个高斯分布下都会有一个密度，对吧？因为高斯密度非零。所以，它们在每个高斯分布下都有一个似然，只是哪一个高一些、哪一个低一些。还有其他问题吗？

### [1:02:26](https://www.youtube.com/watch?v=KlHIR7lT-mo&t=3746s) · b000075

**English**

Okay, so that was Gaussian mixture models in couple minutes. Uh again, we're going to go through at a high level so you can see the evolution of the field. Each of the specific algorithms itself is you know hours of lectures that you all can look at if there's more interest. So then naturally gaussium mixture models can be extended to very autoenccoders right and the key insight is that as we saw previously so z might still be a very simple distribution in a latent space categorical gaussian whatever we're not going to play with z too much but previously in some of these um these uh these gaussian mixture models the x given z so once I know which cluster it belong to the data distribution given that Z was a very simple distribution. It was simply a

**中文**

好，刚才用几分钟讲了高斯混合模型（Gaussian mixture models）。呃，再次说明，我们会从高层次介绍，让你们看到这个领域的演进。每个具体算法本身，你知道，都可以讲上几个小时，如果更感兴趣，你们都可以去看。然后，很自然地，高斯混合模型可以扩展到 very autoenccoders \[字幕疑误，可能指 variational autoencoders，变分自编码器\]，对吧？关键见解是，正如之前看到的，z 仍然可能是潜在空间（latent space）中一个非常简单的分布，类别分布、高斯分布，什么都行，我们不会对 z 做太多变化。但之前，在一些，嗯，这些，呃，这些高斯混合模型中，x given z，也就是一旦知道它属于哪个簇，给定那个 Z 时的数据分布，就是一个非常简单的分布。它只是一个

### [1:03:22](https://www.youtube.com/watch?v=KlHIR7lT-mo&t=3802s) · b000076

**English**

Gaussian with a fixed mean and variance right fixed mu K and sigma K for your three Gaussians. So that's actually a very simple distributions. You just end up learning basically as you see there right three Gaussians. Now VA extend this idea where your X given Z is potentially much more complicated. X given Z is much more complicated is going to be a Gaussian where the mean and variance are all learned by neuronet networks. Right? So that gives you two important benefits. is not just a a single number that is just predefined and learned by your EM algorithm. Uh it's learned by a much more expressive neuronet network. So you can learn all your nonlinear transformations. And more importantly, the mean and variance can also start changing with respect to Z, right? With respect to your input data, right? That is truly

**中文**

具有固定均值和方差的高斯分布，对吧？三个高斯分布各自有固定的 mu K 和 sigma K。所以，这其实是非常简单的分布。你最终学到的基本上就是，正如那里看到的，三个高斯分布。现在，VA \[字幕疑误，可能指 VAE\] 扩展了这个想法，你的 X given Z 可能复杂得多。X given Z 复杂得多，它会是一个高斯分布，但均值和方差都由神经网络学习。对吧？这带来两个重要好处。它不再只是一个预先定义、由 EM 算法学到的单一数值。呃，而是由表达能力强得多的神经网络学习。所以，你可以学习所有非线性变换（nonlinear transformations）。更重要的是，均值和方差也可以开始随 Z 而变化，对吧？随你的输入数据而变化，对吧？这才真正是

### [1:04:21](https://www.youtube.com/watch?v=KlHIR7lT-mo&t=3861s) · b000077

**English**

what makes it more expressive. not just one mean and one variance for the entire distribution but means and variances of these Gaussians which change with your batches of data. So it's almost like infinite number of small Gaussians that fit each batch of data differently. Um so again you can go into more detail from the original paper but you can think of VAEEs as just Gausian mixture models but elevated to a much more expressive level by replacing some of the parameters in Gausian mixture models with neuronet networks. Right? So now you get this dependence on uh your latent variable Z what the means and variances of the Gaussians are.

**中文**

让它更有表达能力的原因。不再是整个分布只有一个均值和一个方差，而是这些高斯分布的均值和方差会随着数据批次（batches）而变化。所以，这几乎就像有无限多个小的高斯分布，以不同方式拟合每一批数据。嗯，再次说明，你可以从原论文了解更多细节，但你可以把 VAEEs \[字幕疑误，可能指 VAEs\] 理解为高斯混合模型，只不过把高斯混合模型中的一些参数替换成神经网络，从而把表达能力提升到了更高的层次。对吧？所以，现在，高斯分布的均值和方差就依赖于，呃，你的潜变量 Z。

### [1:05:08](https://www.youtube.com/watch?v=KlHIR7lT-mo&t=3908s) · b000078

**English**

So you get all these other benefits as well. Uh ideally afterwards Z and now Z can also be higher dimensional right in practice Z can also be much higher dimensional. The hope is that Z could correspond to different changes in your data. for example, all your different hair color, eye color, glasses or not. And you can basically extract features by taking X and inferring what the Z's are. Z's can be thought of as features which are useful for unsupervised learning, right? Because sometimes capturing hair color, eye color is useful for, for example, identifying a person or reidentifying a person. And given a new Z, you can first sample what Z is from a distribution and then you can put it through X given Z so you can figure out what X is.

**中文**

因此，你也得到了所有这些其他好处。呃，理想情况下，之后 Z，而且现在 Z 也可以是更高维的，对吧？实际中 Z 的维度也可以高得多。我们希望 Z 能够对应数据中的不同变化。例如，各种不同的头发颜色、眼睛颜色、是否戴眼镜。你基本上可以通过接收 X 并推断 Z 是什么来提取特征。Z 可以看作对无监督学习（unsupervised learning）有用的特征，对吧？因为有时捕捉头发颜色、眼睛颜色，对于，比如，识别一个人或者重新识别一个人很有用。给定一个新的 Z，你可以先从一个分布中采样得到 Z，再把它送入 X given Z，这样就能确定 X 是什么。

### [1:06:03](https://www.youtube.com/watch?v=KlHIR7lT-mo&t=3963s) · b000079

**English**

How are VAEs learned? Then um I'm going to start drawing these figures. So often times when you look at these generative models, there's always a X to Z path and a Z2X path. As you recall, X is your data and Z are your latent variables, right? X is a raw data. Z is some lower dimensional latent variables. Can also be thought of as features that capture all your variations which tell you how to generate your data. And there's always two functions, right? One function is the generation function. So given a latent variable Z, can I take that in and output X, right? So that's P of X given Z, right? Z is the input, X is the output. And there's often some parameters data because some neuronet networks are involved. So that's a generation process. You can also think about it as a decoder that decodes your latent variables to data

**中文**

VAEs 是如何学习的？那么，嗯，我开始画这些图。通常，当你看这些生成模型时，总会有一条 X 到 Z 的路径，以及一条 Z2X 的路径。你们应该记得，X 是数据，Z 是潜变量，对吧？X 是原始数据。Z 是一些较低维的潜变量。它们也可以看作捕捉所有变化的特征，告诉你如何生成数据。而且，总会有两个函数，对吧？一个函数是生成函数（generation function）。也就是，给定一个潜变量 Z，我能不能把它接收进来并输出 X，对吧？这就是 P of X given Z，对吧？Z 是输入，X 是输出。通常还会有一些参数 data \[字幕疑误，可能指 theta\]，因为其中涉及一些神经网络。所以，这就是生成过程。你也可以把它看作一个解码器，把潜变量解码成数据。

### [1:06:58](https://www.youtube.com/watch?v=KlHIR7lT-mo&t=4018s) · b000080

**English**

symmetrically. There is also a inference model that takes in your data X and predicts what your latent features Z are. Right? So that can be think thought of as Q a different function from P. Now Q Z given X right so X is taken in and you're outputting a distribution over Z and again there might be several other parameters involved right say five right so this can be thought of as the encoder because you're encoding my data X into my feature Z and then I'm decoding my feature Z into my data X usually there's a P function a Q function different parameters one is a generator one is the inference uh you can also think about it as encoders and decoders. I'm sure all of you have seen maybe not the math but at least how vaes work using these encoders and decoders right

**中文**

对称地，还有一个推断模型（inference model），接收数据 X，并预测潜在特征 Z 是什么。对吧？这可以看作 Q，一个不同于 P 的函数。现在是 Q Z given X，对吧？输入 X，输出 Z 上的一个分布，同样，这里可能涉及几个其他参数，对吧，比如 five \[字幕疑误，可能指 phi\]，对吧？所以，这可以看作编码器，因为你把我的数据 X 编码成我的特征 Z，然后我再把特征 Z 解码成数据 X。通常有一个 P 函数、一个 Q 函数，不同的参数，一个是生成器（generator），一个是推断，呃，你也可以把它们看作编码器和解码器。我相信你们都见过，也许没见过数学推导，但至少知道 vaes 是如何利用这些编码器和解码器工作的，对吧？

### [1:07:53](https://www.youtube.com/watch?v=KlHIR7lT-mo&t=4073s) · b000081

**English**

there's a x that comes in it's encoded by the encoder that outputs z. But specifically how it outputs Z is that because I want the Z to be Gaussian, it doesn't just output the variable itself, but it outputs the mean and variance parameters for what that Gaussian distribution is. Right? This is what makes it expressive because if I change my input data X, I'm going to learn a different mean and variance. So whenever I input a different X, I'm going to learn a new mean and variance and get a new set of latent variable Z that best represent my data. compared to Gausian mixture models that was looking at mean and variance for the whole distribution not one per sample.

**中文**

有一个 x 输入进来，由编码器编码并输出 z。但具体来说，它是如何输出 Z 的呢？因为我希望 Z 是高斯分布，所以它不会只输出变量本身，而是输出那个高斯分布的均值和方差参数。对吧？这正是它具有表达能力的原因，因为如果我改变输入数据 X，就会学到不同的均值和方差。所以，每当我输入不同的 X，就会学到新的均值和方差，并得到一组最能表示我的数据的新潜变量 Z。相比之下，高斯混合模型关注的是整个分布的均值和方差，而不是每个样本各有一组。

### [1:08:38](https://www.youtube.com/watch?v=KlHIR7lT-mo&t=4118s) · b000082

**English**

So that gives you Z. Uh specifically, you know, if you have a mean and variance, you can first sample noise from 01 Gaussian, multiply it by the variance to get sigma epsilon and add the mean to get a random variable Z that actually follows a distribution from that Gaussian and then Z can be decoded back to X and you're reconstructing how the reconstructed X matches the input X. Right? So that's the main reconstruction objective in these VAEEs. X goes in, you learn an encoder to learn what the Gaussian variables are for your latent variables. That gives you Z, which is then decoded back to X. And that should try to be as close to the original image as possible as measured by either cross entropy or mean square error. There's also a subtle point where you have to also, you know, if you go through the math, there's a term that

**中文**

这样就得到了 Z。呃，具体来说，你知道，如果有了均值和方差，就可以先从 01 高斯分布中采样噪声，乘以方差，得到 sigma epsilon，再加上均值，得到一个随机变量 Z，它确实服从那个高斯分布；然后，Z 可以再被解码回 X，你要重建，看看重建的 X 与输入的 X 有多匹配。对吧？所以，这就是这些 VAEEs \[字幕疑误，可能指 VAEs\] 中的主要重建目标（reconstruction objective）。X 输入进来，你学习一个编码器，学习潜变量对应的高斯变量是什么。这样得到 Z，再把它解码回 X。它应该尽可能接近原始图像，用交叉熵或均方误差来衡量。还有一个微妙的地方，你还必须，你知道，如果推一遍数学公式，会出现一项，

### [1:09:34](https://www.youtube.com/watch?v=KlHIR7lT-mo&t=4174s) · b000083

**English**

comes out where each of these Z's, you want to make sure these are actually close to a Gaussian distribution because that is uh where you assume the latent variables to follow a distribution from. I'm almost out of time, so I'll pause here for any questions about VAEEs and Gaussian mixture models as an introduction to some of these generative models. Um, as a spoiler, we're going to start extending VAEEs to diffusion models on Thursday and then we'll extend diffusion models to flow matching models. All of which again follow a natural progression and is the evolution of generative models. They're all very related to each other. Um, so it' be a nice story. But any questions about VAES and Gaussian mixture models or anything else we presented earlier in class today? Yes.

**中文**

要求这些 Z 中的每一个，你都要确保它们确实接近高斯分布，因为，呃，那就是你假设潜变量所服从的分布。我快没时间了，所以先在这里停一下，看看大家对于 VAEEs \[字幕疑误，可能指 VAEs\] 和高斯混合模型有没有问题，它们是我们介绍这些生成模型的起点。嗯，先剧透一下，我们周四会开始把 VAEEs 扩展到 diffusion models，再把 diffusion models 扩展到流匹配（flow matching）模型。所有这些再次沿着自然的推进过程，也是生成模型的演进。它们彼此都非常相关。嗯，所以，这会是一条很好的脉络。不过，关于 VAES 和高斯混合模型，或者今天课堂前面介绍的其他任何内容，有什么问题吗？是的。

### [1:10:35](https://www.youtube.com/watch?v=KlHIR7lT-mo&t=4235s) · b000084

**English**

Yes. Um, so we want Z to follow we want these latent variables to essentially follow a Gaussian distribution with some particular mean and some particular variance. So one way of doing that is to first sample noise from a standard Gaussian. So with mean zero and variance one, I'm going to multiply that noise by your sigma. So now that will be a Gaussian for mean zero and variance sigma or sigma squar. Um and then I'm going to add uh mu and that gives you a vector that is sampled from gaussian with mean mu and varian sigma square. So that's just a way of of sampling from a distribution with a particular mean and variance. Uh to go into more technical detail, if you look at how these models are trained, the data comes in at X is going

**中文**

是的。嗯，我们希望 Z 服从，我们希望这些潜变量基本上服从一个具有某个特定均值和某个特定方差的高斯分布。实现它的一种方法，是先从标准高斯分布（standard Gaussian）中采样噪声。所以，均值为零、方差为一，我会把那个噪声乘以你的 sigma。这样，就会得到一个均值为零、方差为 sigma 或 sigma squar 的高斯分布。嗯，然后再加上，呃，mu，这就给出一个向量，它是从均值为 mu、方差为 sigma square 的高斯分布中采样得到的。所以，这只是一种从具有特定均值和方差的分布中采样的方法。呃，如果再深入一些技术细节，看看这些模型是如何训练的，数据从 X 输入，会

### [1:11:31](https://www.youtube.com/watch?v=KlHIR7lT-mo&t=4291s) · b000085

**English**

to predict the mean and variance to get Z using this mathematical addition. And Z is then encoded to get the final output Xhat, right? The reconstructed X. And I'm going to compute a loss between X hat and X say the mean square error right that mean squareed error has to be back propagated to update the decoder and to update the encoder which has your new network parameters right updating a decoder is easy right you define a loss like a mean square error between xhat and x updating a decoder is easy with gradient descent right if I didn't pull out sampling from this noise first then I would have to back propagate through a noise function. If I fully sample from this del with this mean and variance then I was to back propagate through a noise function which is actually not feasible uh with

**中文**

预测均值和方差，通过这个数学加法得到 Z。然后对 Z 进行编码，得到最终输出 Xhat，对吧？也就是重建的 X。接着，我会计算 X hat 与 X 之间的损失，比如均方误差，对吧？这个均方误差必须进行反向传播（back propagation），以更新解码器，也更新编码器，编码器包含你的新网络参数，对吧？更新解码器很容易，对吧？定义一个损失，比如 xhat 和 x 之间的均方误差，用梯度下降（gradient descent）更新解码器很容易，对吧？如果我没有先把这个噪声采样步骤单独拿出来，那就必须通过一个噪声函数进行反向传播。如果我直接从这个具有这组均值和方差的 del \[字幕不清\] 中完整采样，就得通过一个噪声函数反向传播，而这实际上无法用

### [1:12:24](https://www.youtube.com/watch?v=KlHIR7lT-mo&t=4344s) · b000086

**English**

gradient descent. So you have to pull out this noise function sample noise and then do the linear transformation with the mean and variance so that the back propagation can actually reach the mean and variance and then reach the encoder. There's more mathematical explanations and you can come to office hours if you want to go through the math. Um but that's the intuitive argument. Yeah.

**中文**

梯度下降来完成。所以，你必须把这个噪声函数单独拿出来，先采样噪声，再用均值和方差进行线性变换，这样反向传播才能真正到达均值和方差，进而到达编码器。有更详细的数学解释，如果你想推一遍数学过程，可以来答疑时间。嗯，不过，这就是直观的解释。是的。

### [1:13:07](https://www.youtube.com/watch?v=KlHIR7lT-mo&t=4387s) · b000087

**English**

&gt;&gt; Oh, so in this case, so it's predicting the mean and variance, right? Uh in Gaussian mixture models, these mean and variances were literally computed. So the mean is computed by if I have five points in my Gaussian. I take the average and that's the mean of that Gaussian, right? the sample mean from statistics. So in this case you're using a power of neural networks. We're given an input data X. You use an encoder to output basically two dimens two let's say this is five dimension. So this would be a five dimensional vector and this is a five dimensional vector. So it's outputting a fivedimensional vector that will be the mean of the Gaussian. And then for the variance it's also outputting a fivedimensional vector that represents the variance of the Gaussian. So he's using neuronet networks to output vectors that are the parameters of the gaussian.&gt;&gt; Yeah,&gt;&gt; but that's only calculated with one data point or is there already

**中文**

&gt;&gt; 哦，在这种情况下，它是在预测均值和方差，对吧？呃，在高斯混合模型中，这些均值和方差确实是直接计算出来的。比如，均值的计算方式是，如果我的高斯分布里有五个点，我取它们的平均值，这就是那个高斯分布的均值，对吧？统计学中的样本均值（sample mean）。而在这里，你使用的是神经网络的能力。给定输入数据 X，你用一个编码器，基本上输出两个维，两个，假设这里是五维。那么，这会是一个五维向量，这也是一个五维向量。所以，它输出一个五维向量，作为高斯分布的均值。然后，对于方差，它也输出一个五维向量，表示高斯分布的方差。所以，它是在用神经网络输出作为高斯分布参数的向量。&gt;&gt; 是的，&gt;&gt; 但那只是用一个数据点计算的吗，还是已经

### [1:14:04](https://www.youtube.com/watch?v=KlHIR7lT-mo&t=4444s) · b000088

**English**

&gt;&gt; this per data point? So that's the power of the right. The mean and variance is not a five dimensional mean that is the same for all data points in the data set, but every data point, every x will learn a different mean and different variance. So you can think about every data point as learning some local Gaussians, right? Some data points will be very close together, a bunch of local Gaussians with very similar means and variances, but some data points can be very different and learn a very different mean and variance for their Gaussian.

**中文**

&gt;&gt; 这是针对每个数据点的。所以，这就是它的能力，对吧。均值和方差不是一个对数据集中所有数据点都相同的五维均值，而是每个数据点、每个 x 都会学到不同的均值和不同的方差。所以，你可以把每个数据点理解为在学习某个局部高斯分布（local Gaussian），对吧？有些数据点会非常接近，形成一组均值和方差非常相似的局部高斯分布；但有些数据点可能非常不同，并为各自的高斯分布学到非常不同的均值和方差。

### [1:14:39](https://www.youtube.com/watch?v=KlHIR7lT-mo&t=4479s) · b000089

**English**

I'm curious who has seen VAEs before. So half half the class. Did y'all see it in some class here or in in research or where?&gt;&gt; Where did you see it?&gt;&gt; Both places.&gt;&gt; Huh?&gt;&gt; Both places.&gt;&gt; Both places. Okay. Well, given that people come from different backgrounds, um I think it's good to cover some things. Maybe it's it's repetitive for people who have seen it and for people who are just seeing it for the first time can can stay after the class for the office hours um to go into more detail. Any any final questions about this,

**中文**

我很好奇，谁以前见过 VAEs？所以，一半，一半同学。你们是在这里的某门课上见过，还是在研究中，或者在哪里？&gt;&gt; 你们在哪里见过？&gt;&gt; 两种地方都有。&gt;&gt; 嗯？&gt;&gt; 两种地方都有。&gt;&gt; 两种地方都有。好。考虑到大家来自不同背景，嗯，我觉得讲一些内容是有好处的。也许对见过的人来说有点重复，而第一次接触的人可以，可以在课后留下来，利用答疑时间了解更多细节。关于这个，还有，还有最后的问题吗，

### [1:15:27](https://www.youtube.com/watch?v=KlHIR7lT-mo&t=4527s) · b000090

**English**

but the key ideas are the same, right? It's all about again the purpose of some of these um these generative models I just again give a high level recap is to just find a really good way of modeling P of X where X is your data right you want ideally P of X to be expressive as possible so you're capturing all the highdimensional variations in various data sets at the same time you want to be able to you know explicitly sample from P of X or to maximize P of X given observed data which is your training objective. Um these mixtures of Gaussians basically say Z is just a categorical right three options for Z and my X given Z is just a Gaussian where the only variables are mu mu1 sigma 1 mu2 sigma 2 mu3 sigma 3 right just three gaussians for my whole

**中文**

不过，关键想法是一样的，对吧？归根结底，再说一次，这些，嗯，这些生成模型的目的，我再做一个高层次的回顾，就是找到一种非常好的方式来建模 P of X，其中 X 是你的数据，对吧？理想情况下，你希望 P of X 尽可能有表达能力，以捕捉各种数据集中的所有高维变化；同时，你希望能够，你知道，显式地从 P of X 中采样，或者根据观测数据最大化 P of X，这就是你的训练目标。嗯，这些高斯混合基本上就是说，Z 只是一个类别型变量，对吧，Z 有三个选项，而我的 X given Z 只是一个高斯分布，其中唯一的变量是 mu，mu1、sigma 1、mu2、sigma 2、mu3、sigma 3，对吧？整个

### [1:16:21](https://www.youtube.com/watch?v=KlHIR7lT-mo&t=4581s) · b000091

**English**

data set and the biggest difference that we went to VAE is that now your Z is higher dimensional right it can be entire vector and your X given Z are also neuronet network outputs. Whereas a Gaussian where the mean is some neonet that takes in Z and outputs some mean and your variance is some neuronet network that takes in Z and outputs some variance. So each data point could have a different mean and variance distribution for the Gaussian that I learned for it instead of having just one Gaussian for the whole data is the biggest difference.&gt;&gt; All right folks we're at time so um you all can go keep working on homework three and check in with me with any questions about the homeworks about the lecture or about um the projects. Thanks everyone.

**中文**

数据集只有三个高斯分布。而转向 VAE 后，最大的区别是，现在 Z 是更高维的，对吧，它可以是一个完整向量，而且 X given Z 也是神经网络的输出。也就是一个高斯分布，它的均值由某个神经网络接收 Z 并输出某个均值，方差则由某个神经网络接收 Z 并输出某个方差。所以，对于我为每个数据点学到的高斯分布，每个数据点都可以有不同的均值和方差分布，而不是整个数据只有一个高斯分布，这就是最大的区别。&gt;&gt; 好，各位，时间到了，所以，嗯，你们可以继续做作业三，如果对作业、课程内容或者，嗯，项目有任何问题，就来找我。谢谢大家。
