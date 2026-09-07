# Lecture 1 – Course Introduction (MIT How to AI Almost Anything/Multimodal AI, Spring 2026)

_Bilingual transcript · 双语讲稿_

- Channel: Paul Liang
- Source: [YouTube](https://www.youtube.com/watch?v=Xm2crsD5ngA)
- Duration: 1:11:09
- Caption source: automatic
- Status: complete
- Chinese translation: 83/83
- Translation provider: codex
- Generated: 2026-09-07T07:35:54+00:00

## Transcript · 讲稿

### [00:01](https://www.youtube.com/watch?v=Xm2crsD5ngA&t=1s) · b000001

**English**

All right, folks. It's 2:35. Let's get started. Uh so, welcome. Welcome to multimodal AI. This is a new course that's being offered between the Media Lab, EECS, and the Schwarzman Common Ground. My name is Paul. Really excited to be a lead instructor for this course. So, multimodality will be the next frontier for AI systems. All right, you've seen great progress in AI starting with language, language models that can understand your spoken or typed text. But, understanding people goes beyond text alone, right? It requires understanding our voice, our facial expressions, and our body language to really understand a person. Likewise, you've seen great progress in AI for health, starting with great progress in AI for X-ray images. But, a doctor would diagnose a patient using not only X-rays, but also histology, so microscopic images of cells that are suspected to be cancerous, using various medical sensors, and more data. And that's just the tip of the iceberg.

**中文**

好了，各位。现在是 2:35。我们开始吧。呃，欢迎。欢迎来到多模态 AI（multimodal AI）课程。这是 Media Lab、EECS 和 Schwarzman Common Ground 联合开设的一门新课。我叫 Paul。非常高兴能担任这门课的主讲教师。那么，多模态将成为 AI 系统的下一个前沿。大家已经看到，AI 从语言入手取得了巨大进展，语言模型（language models）能够理解你说出或键入的文本。但是，理解人不仅仅是理解文本，对吧？要真正理解一个人，还需要理解我们的声音、面部表情和肢体语言。同样，大家也看到了医疗 AI 的巨大进展，最初是 AI 在 X 光图像方面取得的巨大进展。但是，医生诊断患者时不仅会使用 X 光，还会使用组织学（histology），也就是疑似癌变细胞的显微图像，还会使用各种医疗传感器以及更多数据。而这还只是冰山一角。

### [00:58](https://www.youtube.com/watch?v=Xm2crsD5ngA&t=58s) · b000002

**English**

I've seen so many examples of data being collected about people, about our environments, and the world around us, that naturally we need multimodal AI systems to process and make predictions on all of this data. Let me give you a few examples of that. Uh there's a big focus in AI for physical sensing. Building AI systems that can understand the physical world, such as robots, understanding manufacturing systems. And this fundamentally requires systems that can see and hear and touch and feel the world. Right? So, those are the examples of robotic systems that are much more adept because they have cameras attached to them, while at the same time being able to feel surroundings, right? To understand the material and objects and properties of the environment. Our group is also extending into smell sensing. So, smelling gases can be a huge indicator of various foods and beverages in the world to understand allergies. So, over here we built a sensor that can detect whether or not a

**中文**

我见过很多收集有关人、环境以及周围世界的数据的例子，因此，我们自然需要多模态 AI 系统来处理所有这些数据并据此进行预测。让我举几个例子。呃，AI 有一个重要方向是物理感知（physical sensing）。构建能够理解物理世界的 AI 系统，例如机器人，以及理解制造系统。而这从根本上要求系统能够看见、听见、触摸并感受世界，对吧？这些机器人系统之所以能力更强，是因为它们配有摄像头，同时还能感受周围环境，对吧？从而理解环境中的材料、物体和属性。我们小组也在拓展到嗅觉感知（smell sensing）。因此，闻出气体可以成为了解世界上各种食品和饮料、理解过敏问题的重要指标。所以，在这里，我们构建了一个传感器，它能检测某种

### [01:54](https://www.youtube.com/watch?v=Xm2crsD5ngA&t=114s) · b000003

**English**

peanut is present in some substance, and that can be used to detect whether somebody might be allergic to these peanuts. So, there's examples of vision, touch, and smell modalities. In the generative AI space today, we're starting to see lots of examples of data modalities being generated. From language systems that can generate videos, from given a video, can you pair it up with the right music? And from images, can you animate entire videos based on the starting image? But, the future of this multimodal generative AI is going to be, you know, being able to flexibly take in any modality and generate any other modality for content creation. For folks who are looking at AI for health, as I've motivated, health is multifaceted. Right? You want to understand a patient's physical health, at the same time understand their emotional well-being, and how they flourish in social interactions. On the side of physical health, you have examples where you're trying to

**中文**

物质中是否存在花生，这可以用来检测某个人是否可能对这些花生过敏。这些就是视觉、触觉和嗅觉模态（modalities）的例子。在如今的生成式 AI（generative AI）领域，我们开始看到很多生成各种数据模态的例子。从能够生成视频的语言系统，到给定一个视频，你能否为它配上合适的音乐？再到从图像出发，能否基于起始图像制作出整段视频动画？但是，这种多模态生成式 AI 的未来，将是能够灵活地接收任意模态并生成任意其他模态，用于内容创作。对于关注医疗 AI 的同学，正如我之前说明的，健康是多方面的，对吧？你既要了解患者的身体健康，也要了解他们的情绪健康，以及他们在社交互动中如何良好发展。在身体健康方面，有一些例子是尝试

### [02:43](https://www.youtube.com/watch?v=Xm2crsD5ngA&t=163s) · b000004

**English**

understand patients in the ICU based on sensor readings, based on imaging data, based on other medical sensors. On the side of emotional well-being, it's about understanding people and how they're reacting, and their moods and emotional states. And for understanding social bonus, you have to understand how people are conversing and talking and showing attention, and flourishing in social interactions. And finally, there's also this huge interest in building agentic systems. Agentic systems that are grounded in some world and are able to take actions. For example, agents on the internet that can take in instructions, like purchasing a set of earphones with certain stars and rating. And these systems have to go on to these websites, actually understand visual information, execute actions, and complete the sequence of actions to solve the task. And we're going to see more and more of these agentic systems. Agents that are able to understand human instructions,

**中文**

根据传感器读数、成像数据以及其他医疗传感器来了解重症监护室（ICU）中的患者。在情绪健康方面，要理解人们及其反应，以及他们的心情和情绪状态。而要理解社交加成（social bonus）\[字幕疑误，可能指 social well-being\]，你必须了解人们如何交谈、说话、表现出关注，以及在社交互动中良好发展。最后，人们也非常关注构建智能体系统（agentic systems）。这些智能体系统以某个世界为依托（grounded），并能够采取行动。例如，互联网上的智能体（agents）可以接收指令，比如购买一副具有特定星级和评分的耳机。这些系统必须进入这些网站，真正理解视觉信息，执行操作，并完成一系列操作来解决任务。我们将会看到越来越多这样的智能体系统。这些智能体能够理解人类指令，

### [03:34](https://www.youtube.com/watch?v=Xm2crsD5ngA&t=214s) · b000005

**English**

and yet are grounded in web pages, in other computer tasks like PowerPoints and spreadsheets, in the embodied world like robotics, that are able to see and hear and interact in robotic worlds, and for various other engineering applications such as manufacturing. Those are about really understanding various sensors in the world and being able to take actions to optimize some system. So, a lot of these progress in interactive agents also need to be grounded in different data modalities. So, that leads us to this course, right? A course on the foundations and recent trends in multimodal AI, meant to give everybody introduction to various, you know, key principles in learning from different data sources, how to fuse and how to combine and how to align these different data sources, and build foundation models with the capabilities of multimodal learning beyond just language alone. Really excited to introduce your teaching team for this semester. Uh my name is Paul. I'm a faculty in the

**中文**

同时又以网页、PowerPoints 和电子表格等其他计算机任务，以及机器人等具身世界（embodied world）为依托，能够在机器人世界中看、听并互动，还能用于制造等其他各种工程应用。这些应用涉及真正理解世界中的各种传感器，并能够采取行动优化某个系统。因此，交互式智能体（interactive agents）的许多这些进展，也需要以不同的数据模态为依托。这就引出了这门课，对吧？这是一门关于多模态 AI 基础与近期趋势的课程，旨在向大家介绍从不同数据源学习的各种关键原理，如何融合（fuse）、组合以及对齐（align）这些不同的数据源，并构建具有超越单纯语言的多模态学习（multimodal learning）能力的基础模型（foundation models）。非常高兴向大家介绍本学期的教学团队。呃，我叫 Paul。我是

### [04:28](https://www.youtube.com/watch?v=Xm2crsD5ngA&t=268s) · b000006

**English**

Media Lab and EECS, where I've been working on multimodal AI, and I'm joined by three other instructors, right? Dimitri Bertsimas is a faculty in Sloan, also working on multimodal AI, especially in healthcare and operations research. Si Quia is a faculty in DUSP, looking at how multimodal modeling of cities gives us a better perspective on how to better operate and improve the standard of living in cities. As Sanga Kim is an instructor in Mechanical Engineering, looking at how multimodal AI can be used in various engineering processes, looking at how visual data and sensory information can be used to better understand and optimize these manufacturing pipelines. And they'll be each giving several lectures on the foundations and real-world applications of multimodal AI. I'm also joined by several amazing teaching assistants, Edgar, Valdemar, and David, who'll be helping out with uh the projects and the homeworks and mentoring students in the course.

**中文**

Media Lab 和 EECS 的教师，一直从事多模态 AI 研究，还有另外三位教师与我共同授课，对吧？Dimitri Bertsimas 是 Sloan 的教师，也研究多模态 AI，尤其是医疗和运筹学（operations research）方面。Si Quia 是 DUSP 的教师，研究城市的多模态建模如何为我们提供更好的视角，以更好地运营城市并提高城市生活水平。As Sanga Kim 是 Mechanical Engineering 的教师，研究多模态 AI 如何用于各种工程流程，以及如何利用视觉数据和传感信息来更好地理解和优化这些制造流水线。他们每个人都会讲授几节有关多模态 AI 基础和实际应用的课程。此外，还有几位出色的助教与我一起授课，Edgar、Valdemar 和 David，他们会协助处理项目、作业，并指导这门课的学生。

### [05:25](https://www.youtube.com/watch?v=Xm2crsD5ngA&t=325s) · b000007

**English**

So, that's a warm welcome to this class from your teaching team. So, I also want to hear from all of you, uh just briefly, in maybe one or two sentences, so not taking more than 30 seconds, your name, department, and program, uh any favorite modalities you've been involved in processing or that you want to learn from this course, and why you're most interested in taking this course. Why don't we start over here and just maybe briefly go for 2 seconds, a short introduction.&gt;&gt; Hi, my name is Ruby. I'm a student from Harvard and I'm currently doing the design engineering. And um my favorite modality is visual, uh especially the images. And my previous research experiences I'm currently working on um um building benchmark for this AI system. And I'm interested in this course because I'm interested in how to um combine the current modality across this um system.

**中文**

那么，教学团队热烈欢迎大家来上这门课。我也想听听大家的情况，呃，简单说一两句话，不超过 30 秒，介绍你的姓名、院系和项目，你最喜欢哪些已经参与处理过的模态，或者希望通过这门课学习哪些模态，以及你为什么对这门课最感兴趣。我们从这边开始吧，简单讲个 2 秒，做个简短介绍。&gt;&gt; 大家好，我叫 Ruby。我是 Harvard 的学生，目前在读设计工程。嗯，我最喜欢的模态是视觉，呃，尤其是图像。我以前的研究经历，我目前正在做的是，嗯，嗯，为这个 AI 系统构建基准（benchmark）。我对这门课感兴趣，是因为我想了解如何，嗯，在这个系统中结合当前的模态。

### [06:22](https://www.youtube.com/watch?v=Xm2crsD5ngA&t=382s) · b000008

**English**

&gt;&gt; My name is Jeremy. I'm in the MEng program. So, that's affiliated with their Sloan and the ORC. My favorite modality is probably just text. And um I've done some research in uh in related to assessing implicit um bias in dialogues. I am interested in this course because it gives me a like a intro- brief introduction to um how to combine some modalities.&gt;&gt; Um my name is Manav Gupta. I'm also MEng and um his method uh is text and images. Uh previously I've worked uh in robotics, specifically multi-agent path planning problem. And uh while I'm in uh design, I want to explore more like how to integrate different modalities and then to uh do a better job in that. Um

**中文**

 &gt;&gt; 我叫 Jeremy。我在 MEng 项目。所以，它隶属于他们的 Sloan 和 ORC。我最喜欢的模态可能就是文本。嗯，我做过一些与评估对话中的隐性偏见有关的研究。我对这门课感兴趣，因为它能让我对如何结合一些模态有一个入门——简短的介绍。&gt;&gt; 嗯，我叫 Manav Gupta。我也在 MEng，嗯，他的方法，呃，是文本和图像。呃，我以前做过机器人方面的工作，具体来说是多智能体路径规划问题（multi-agent path planning problem）。呃，而我在，呃，设计方面，我想进一步探索如何整合不同模态，然后把这方面做得更好。嗯，

### [07:17](https://www.youtube.com/watch?v=Xm2crsD5ngA&t=437s) · b000009

**English**

I guess like for even tasks like this.&gt;&gt; Hi, this is Sijia. I'm currently a student at the GSD. Um actually my favorite modality is moving images. Maybe not the focus of this course, but I just also wanted to explore other aspects of AI. And my previous research experience in AI academy I worked with uh neural networks to get the accuracy of the the neural hardware and that's it.&gt;&gt; Great. My name is Solomon part of the Media Lab. My favorite modality would be language. Biggest research in AI healthcare and also in on serious foundation models. Um I'm just in Yeah, all the reasons above.&gt;&gt; I'm Nesty and I'm also part of the Media Lab. My favorite modality is probably language.&gt;&gt; Education, memory and things like that. And real life experience mostly on that

**中文**

我想，即使是像这样的任务。&gt;&gt; 大家好，我是 Sijia。我目前是 GSD 的学生。嗯，其实我最喜欢的模态是动态图像。也许这不是这门课的重点，但我也想探索 AI 的其他方面。我之前在 AI academy 的研究经历中，用过神经网络（neural networks）来获得神经硬件（neural hardware）的准确率，就是这些。&gt;&gt; 很好。我叫 Solomon，来自 Media Lab。我最喜欢的模态是语言。最大的研究是在 AI 医疗，以及 serious foundation models \[字幕疑误，可能指 time series foundation models\] 方面。嗯，我就是，是的，上面提到的所有原因。&gt;&gt; 我叫 Nesty，也来自 Media Lab。我最喜欢的模态可能是语言。&gt;&gt; 教育、记忆之类的东西。而实际生活经验主要在那

### [08:15](https://www.youtube.com/watch?v=Xm2crsD5ngA&t=495s) · b000010

**English**

side. Yeah, I believe in mixed terms and this is what we combine more than one modality I mean a lot of reasons to be good. That's the scope of that.&gt;&gt; Yeah. I I'm really I'm also part of the Media Lab. I think my favorite modality is audio, touch, video, medicine, music, speech and text. So, my first research experience I did like multi-agent video game. I don't honestly know what they're also like a video game multi-agent game. I like tasks and I try to combine this task and the video together. Now, I think that's one kind of interesting task to combine all of the elements together.&gt;&gt; I'm Edward. I'm also part of the Media Lab program. My favorite modality is vision and also sound is pretty interesting. And I previously worked on work and researching generating proteins with important designs. And for this course I'm pretty

**中文**

一方面。是的，我相信混合的术语，而这就是我们组合不止一种模态的内容，我的意思是，有很多理由说明它会很好。这就是它的范围。&gt;&gt; 是的。我，我真的，我也来自 Media Lab。我想我最喜欢的模态是音频、触觉、视频、医学、音乐、语音和文本。所以，我第一次研究经历做的是类似多智能体电子游戏。我老实说不知道它们是什么，也像是电子游戏，多智能体游戏。我喜欢任务，我尝试把这个任务和视频结合起来。现在，我觉得把所有这些元素结合起来，是一种有趣的任务。&gt;&gt; 我叫 Edward。我也在 Media Lab 项目。我最喜欢的模态是视觉，声音也很有意思。我以前做过一些工作，研究通过重要的设计生成蛋白质。对于这门课，我非常

### [09:11](https://www.youtube.com/watch?v=Xm2crsD5ngA&t=551s) · b000011

**English**

interested in integrating different modalities and yeah, both of them are modeling.&gt;&gt; Okay, well, clearly we're not going to have time to go through everybody. Mine is for when the course is still 20-30 people. But even within a small sampling we see in examples of of course language, vision, molecular structure, touch, very interesting data modalities. So, maybe a random sampling of maybe 10 more people want to share interesting answers where your favorite modalities aren't the ones that have been mentioned above and then we can move on. You get uh some bonus points if you start sharing. Yes.

**中文**

感兴趣的是整合不同模态，而且，是的，它们两者都是建模。&gt;&gt; 好吧，显然我们没有时间让每个人都介绍一遍。我这个安排是针对课程还只有 20–30 人时的情况。但即使只听了这么一小部分，我们也看到了语言、视觉、分子结构、触觉等非常有意思的数据模态的例子。那么，也许再随机请 10 个人分享一些有意思的答案，你最喜欢的模态是上面还没提到过的，然后我们就继续。主动分享的话，你会得到一些加分。好的。

### [09:58](https://www.youtube.com/watch?v=Xm2crsD5ngA&t=598s) · b000012

**English**

&gt;&gt; And for this course I'm interested in learning sort of principles behind learning modalities so that we can build foundation models for biology but look at different like scales of biology since there's no one modality that captures it.&gt;&gt; Right. Yes.&gt;&gt; Uh hi everyone. My name is Steve. I'm a dual degree Sloan MBA and ECS masters. I think my favorite modality would be discrete event driven data. I used to work in robotics when you go about people following explaining robots to market. They've been playing blocks in Boston right here. But getting my actual physical data was a lot of fun getting those numbers you can see and confirm they're there. But there are many other modalities which is why I take this course.&gt;&gt; I was just going to add so it's not necessarily my favorite modality but I'm really interested in the integration of EEG and EDA data into these models and

**中文**

 &gt;&gt; 对于这门课，我有兴趣学习模态学习背后的一些原理，这样我们就能为生物学构建基础模型，同时关注生物学的不同尺度，因为没有一种模态能涵盖全部。&gt;&gt; 对。好的。&gt;&gt; 呃，大家好。我叫 Steve。我在读 Sloan MBA 和 ECS 硕士双学位。我觉得我最喜欢的模态是离散事件驱动数据（discrete event driven data）。我以前做过机器人，当你围绕跟随人的事情，把机器人解释给市场。他们一直在就在这里的 Boston 玩积木。但是，获取我实际的物理数据很有意思，获得那些你能看到并确认存在的数字。不过，还有很多其他模态，这也是我选这门课的原因。&gt;&gt; 我只是想补充一下，这不一定是我最喜欢的模态，但我非常感兴趣的是将脑电图（EEG）和皮肤电活动（EDA）数据整合到这些模型中，以及

### [10:55](https://www.youtube.com/watch?v=Xm2crsD5ngA&t=655s) · b000013

**English**

how they relate to my use of these models.&gt;&gt; Anybody else? We Yes.&gt;&gt; or No. Um Um pardon me if I get this wrong. My favorite modality I wouldn't say I have one but I'm working a lot with tabular data. I think it's also very interesting one. Um I'm also working mostly on like inter-pixels machine learning. So it's tabular data. You're still there? Um there are obviously many other ways to but turn Boston Model Leader into Tableau of features in I think that would be an interesting aspect.&gt;&gt; Great. Anybody else? Go, yeah.&gt;&gt; I am using Python. Big point of relevance probably is symbolic to me. I guess that's not

**中文**

它们如何与我使用这些模型相关。&gt;&gt; 还有其他人吗？我们，好的。&gt;&gt; 或者没有。嗯，嗯，如果我说错了，请见谅。我最喜欢的模态，我不会说自己有某一种，但我目前大量使用表格数据（tabular data）。我觉得这也是一种非常有趣的模态。嗯，我也主要在做类似 inter-pixels machine learning \[字幕疑误，术语不明\] 的工作。所以是表格数据。你还在吗？嗯，显然还有很多其他方法可以，但是把 Boston Model Leader \[字幕疑误，术语不明\] 转换成特征的 Tableau，我觉得那会是一个有趣的方面。&gt;&gt; 很好。还有谁？来吧，好的。&gt;&gt; 我在用 Python。对我来说，一个很大的相关点可能是符号。我想这不是

### [11:52](https://www.youtube.com/watch?v=Xm2crsD5ngA&t=712s) · b000014

**English**

something quite common I find. That is in the journal of previous research papers. Briefing like who knows also like this.&gt;&gt; Awesome. Um great great sampling of of data modalities people are interested in and various reasons for why they want to take the course and of course also a good representation across different departments at MIT. Um as you'll soon realize, this course won't overfit necessarily to any single modality. So, no worries if you feel a certain modality isn't explained in definite course, but rather the purpose of the course is to really introduce the building blocks. How What are the general principles of applying AI to new data modalities? Right? How do you generally think about the principles within that data modality? How do you think about the principles of how you should design AI systems to model that modality? And how do you, you know, reliably evaluate and deploy systems for that data modality? So, ideally the

**中文**

我所见到的很常见的东西。那是在以前研究论文的期刊里。简报，就像谁知道也像这样。&gt;&gt; 太好了。嗯，很好，很好地展示了大家感兴趣的数据模态，以及大家想选这门课的各种原因，当然，也很好地代表了 MIT 的不同院系。嗯，大家很快就会发现，这门课不会一定过拟合（overfit）到任何单一模态。因此，如果你觉得某种模态没有在明确的课程中得到讲解，也不用担心，因为这门课的目的是介绍基本构件。如何——将 AI 应用于新数据模态的一般原理是什么？对吧？你通常如何思考某种数据模态内部的原理？你如何思考应该怎样设计 AI 系统来对该模态建模的原理？以及你如何可靠地评估和部署面向该数据模态的系统？因此，理想情况下，

### [12:50](https://www.youtube.com/watch?v=Xm2crsD5ngA&t=770s) · b000015

**English**

principles taught in this course is going to generalize to any data modality of interest. Uh that's also why, if you look at the course website, it's called Modeling with Multimodal AI, but also aka How to AI Almost Anything, which is the name of the course uh last year when it was much smaller because the goal is truly to teach the principles of AI so that you can apply it to almost any data modality. So, that's the first key goal of the course. And actually the second key goal of the course, in addition to applying AI to unique and specific data modalities, is to also teach the principles of multimodal AI. How do you connect multiple different data sources? Right, they might involve connecting language and gestures or connecting sensing and proprioception. Again, not about specifically connecting a particular pair, but what are the general principles in terms of the data you got to collect or in terms of the models that you're going to design so that you can pair up

**中文**

这门课教授的原理将能够泛化到任何感兴趣的数据模态。呃，这也是为什么，如果你查看课程网站，会看到它叫作 Modeling with Multimodal AI，也称为 How to AI Almost Anything。这是去年课程规模小得多时的名称，因为我们的目标确实是教授 AI 的原理，让你能将其应用于几乎任何数据模态。所以，这是课程的第一个关键目标。实际上，这门课的第二个关键目标，除了将 AI 应用于独特且具体的数据模态之外，还包括教授多模态 AI 的原理。如何连接多个不同的数据源？对吧，这可能涉及连接语言与手势，或者连接感知与本体感觉（proprioception）。同样，重点不在于具体连接某一对模态，而在于，就你需要收集的数据，或你将设计的模型而言，有哪些一般原理，使你能够配对

### [13:44](https://www.youtube.com/watch?v=Xm2crsD5ngA&t=824s) · b000016

**English**

and learn features and representations from different pairs of data modalities. So, here are the learning objectives, right? The goal of the course is to study recent technical achievements in AI research. We will use reading of papers and a significant course project to improve critical and creative thinking skills, particularly when it comes to AI. We're going to use that to also understand future research challenges in AI. It's not just going to be about implementing things in the past, but very much reading the most recent papers at the frontier of AI research and doing a course project that would significantly improve the capabilities of today's AI systems. And to do that AI research project, you got to explore and implement several new ideas that are at the frontier. I'm hoping that everybody here has satisfied some prerequisites, either at the MIT course Introduction to Machine Learning level or equivalent, and that involves some knowledge of programming, ideally in Python,

**中文**

并从不同的数据模态配对中学习特征与表示（representations）。那么，这些就是学习目标，对吧？课程的目标是研究 AI 研究中近期的技术成果。我们会通过阅读论文和一个重要的课程项目，提高批判性与创造性思维能力，尤其是在 AI 方面。我们也会借此了解 AI 未来的研究挑战。课程不只是实现过去的东西，而是会大量阅读 AI 研究前沿的最新论文，并开展一个能够显著提升当今 AI 系统能力的课程项目。要完成这个 AI 研究项目，你必须探索并实现几个处于前沿的新想法。我希望在座每个人都满足一些先修要求，达到 MIT 的 Introduction to Machine Learning 课程或同等水平，这包括一定的编程知识，最好是 Python，

### [14:41](https://www.youtube.com/watch?v=Xm2crsD5ngA&t=881s) · b000017

**English**

uh some basic understanding of today's AI systems, and also be curious, right? Bringing some non-AI expertise from your domain into the course, sharing it with your students and with us with us. So, in terms of logistics, uh this course meets every Tuesday and Thursday for 1 and 1/2 hours, from 2:30 to 4:00 p.m. You'll be in this lecture hall. Outside of these two meetings, there's going to be several homeworks and reading assignments. They're going to be each two weeks in duration for a total of five homeworks and reading assignments, which I'll go into detail. Uh there'll be an in-class midterm exam, which will be short, mostly short answers, and some longer answer questions, but it's not going to be very complicated. No amount of proofs or no significant implementations. And there's going to be a significant research project outside of course, right? That will be uh a significant research project to be done in groups with several checkpoints, a proposal, a midterm reports, and a

**中文**

呃，对当今 AI 系统有一些基本理解，同时保持好奇心，对吧？把你所在领域的一些非 AI 专业知识带到课堂上，与自己的学生以及我们、我们分享。那么，关于课程安排，这门课每周二和周四上课，每次 1 又 1/2 小时，下午 2:30 到 4:00。就在这个报告厅。除了每周这两次课，还会有几次作业和阅读任务。每次的完成周期为两周，总共五次作业和阅读任务，后面我会详细介绍。呃，会有一次随堂期中考试，时间较短，主要是简答题，也有一些回答较长的问题，但不会非常复杂。没有证明题，也没有大量的实现任务。此外，还会有一个重要的课外研究项目，对吧？这是一个需要分组完成的重要研究项目，有几个检查节点，包括提案、期中报告和

### [15:37](https://www.youtube.com/watch?v=Xm2crsD5ngA&t=937s) · b000018

**English**

final presentation. In terms of topics, this course will be divided into three broad sections. The first 1/3 of the course would cover the foundations of multimodal AI. So, starting this week, we'll introduce what is multimodal AI, various important research tasks and data sets in this space. We'll then cover what are the principles for designing AI for unimodal data. So, if I have a new modality, for example, molecular structures, how can I reason about the principles of that data modality and design the most suitable AI model to learn from that data modality. So, that'll be week two. In week three, we'll be discussing multimodal fusion. How do you build systems that can combine information from different data modalities? And week four, we're going to discuss multimodal representations, of which fusion is one special case, but what other ways of learning multimodal representations are, and how to evaluate the success of these representations.

**中文**

最终展示。在主题方面，这门课会分成三个大部分。课程的前 1/3 将涵盖多模态 AI 的基础。因此，从本周开始，我们会介绍什么是多模态 AI，以及这个领域的重要研究任务和数据集（datasets）。然后，我们会介绍为单模态数据（unimodal data）设计 AI 的原理。比如，如果我有一种新模态，例如分子结构，我应该如何思考这种数据模态的原理，并设计最适合从这种数据模态学习的 AI 模型。这是第二周的内容。第三周，我们将讨论多模态融合（multimodal fusion）。如何构建能够组合不同数据模态信息的系统？第四周，我们将讨论多模态表示（multimodal representations），融合是其中一种特殊情况，但还有哪些学习多模态表示的方法，以及如何评估这些表示是否成功。

### [16:34](https://www.youtube.com/watch?v=Xm2crsD5ngA&t=994s) · b000019

**English**

Starting week five, we'll cover the second module in the course, which will be multimodal foundation models. So, this is very much at the frontier of what all today's AI research and frontier labs are working on. How do you build these foundation models that have the same capabilities of large language models, but are also increasingly grounded in different data modalities? So, we'll start by discussing multimodal foundation models in week five, including multimodal transformers and how they are trained, both pre-training and fine-tuning. In week six, we'll talk about how we can transfer data from really powerful multimodal pre-trained models to downstream tasks. In week seven, we'll go beyond simply predictive models to systems that can generate things like text-to-image models or text to video models. We'll cover multimodal generation. Week eight will be spring break, and we'll come back in week nine with a deeper dive into multimodal reasoning.

**中文**

从第五周开始，我们将进入课程的第二个模块，即多模态基础模型（multimodal foundation models）。这正处于如今整个 AI 研究界和前沿实验室所研究的最前沿。如何构建这些基础模型，使它们具有大型语言模型（large language models）的同等能力，同时又越来越多地与不同数据模态建立 grounding？因此，第五周我们会首先讨论多模态基础模型，包括多模态 transformers 及其训练方式，既包括预训练（pre-training），也包括微调（fine-tuning）。第六周，我们将讨论如何将非常强大的多模态预训练模型中的数据迁移到下游任务（downstream tasks）。第七周，我们将超越单纯的预测模型，讨论能够生成内容的系统，例如文本到图像模型（text-to-image models）或文本到视频模型（text-to-video models）。我们会介绍多模态生成（multimodal generation）。第八周是春假，第九周回来后，我们会深入探讨多模态推理（multimodal reasoning）。

### [17:26](https://www.youtube.com/watch?v=Xm2crsD5ngA&t=1046s) · b000020

**English**

I'm sure all of you have seen that LLMs are really powerful at reasoning over complicated problems involving multiple steps of language reasoning. How do you extend these reasoning capabilities to multimodal problems? And finally, week 10, we'll wrap up the discussion of multimodal foundation models with um introduction to multimodal interactive agents. And finally, module three will cover application domains. So, starting with week 11, uh Sang Uk and Tsinghua will cover various ways in which multimodal models have been applied in their field of expertise, in design, in manufacturing, in cities and transportation. We'll wrap up week 14 with several new research topics. I'm sure there's going to be some significant new innovations in AI space between now and week 14. And we'll finally wrap up the course with uh project final presentations by all of you students.

**中文**

我相信大家都看到过，大型语言模型（LLMs）非常擅长推理涉及多个语言推理步骤的复杂问题。如何把这些推理能力拓展到多模态问题？最后，第 10 周，我们将通过介绍多模态交互式智能体，结束对多模态基础模型的讨论。最后，第三个模块将涵盖应用领域。因此，从第 11 周开始，呃，Sang Uk 和 Tsinghua 将介绍多模态模型在他们的专业领域中的各种应用方式，包括设计、制造、城市和交通。第 14 周，我们将以几个新的研究主题收尾。我相信，从现在到第 14 周，AI 领域一定会出现一些重要的新创新。最后，我们将通过大家的项目最终展示结束这门课。

### [18:21](https://www.youtube.com/watch?v=Xm2crsD5ngA&t=1101s) · b000021

**English**

Great. Let me dive into grading. Um 35% of the course will be graded via homework assignments. There will be five homework assignments, roughly two weeks for each. These homework assignments will include several short answer, conceptual, and primarily implementation questions. And as you'll see when we dive into the homeworks, these implementation questions are meant to guide you to understand what we taught in course in in in the lectures, and also to guide you towards building new methods for your final course project. Uh so, 35% for homework assignments. There's going to be 15% for reading assignments. These reading assignments, also five of them, they're going to introduce several state-of-the-art papers in multimodal AI. Uh these are usually released within uh the past couple of months, and they're going to be released together with the homework in roughly 2 weeks for each reading assignment.

**中文**

很好。让我详细介绍评分。嗯，课程成绩的 35% 来自作业。总共有五次作业，每次大约两周。这些作业会包含若干简答题、概念题，以及主要的实现题。等我们具体介绍作业时，你们会看到，这些实现题旨在引导大家理解课堂上、在、在、在讲课时所教授的内容，同时引导大家为最终课程项目构建新方法。呃，所以，作业占 35%。阅读任务占 15%。这些阅读任务也有五次，会介绍几篇多模态 AI 的最新先进水平（state-of-the-art）论文。呃，这些论文通常在过去几个月内发表，而阅读任务会与作业一起发布，每次阅读任务大约有 2 周时间。

### [19:18](https://www.youtube.com/watch?v=Xm2crsD5ngA&t=1158s) · b000022

**English**

There's going to be 15% for your in-class midterm exam, and 35% for your research project. That'll be broken down into 5% for your proposal, primarily a lit review with some proposal ideas, 10% for a midterm progress, and 20% for your final report and presentation. Okay? So, firstly, five homework assignments. In the first homework assignment, you will be tasked with deciding on a multimodal data set that you would operate on for the remaining semester. There can be changes to this multimodal data set if you think, you know, you spent the first homework processing it and you didn't like it, you can still change it afterwards. But, the goal is to find, process, visualize, and label some multimodal data set that you would use for the semester. Uh, this ideally would overlap with your field of interest, whether it's the healthcare space or design or biology space. Ideally, be

**中文**

随堂期中考试占 15%，研究项目占 35%。项目部分将细分为提案占 5%，主要是文献综述（literature review）加上一些提案想法；期中进展占 10%；最终报告和展示占 20%。好吗？首先，五次作业。第一次作业中，你需要选定一个多模态数据集，在本学期剩余时间里使用。如果你觉得，你知道，第一次作业处理了这个数据集以后不喜欢它，之后还是可以更换。但目标是寻找、处理、可视化并标注一个本学期会使用的多模态数据集。呃，理想情况下，它应该与你感兴趣的领域有所重合，无论是医疗、设计还是生物学。理想情况下，它应该是

### [20:15](https://www.youtube.com/watch?v=Xm2crsD5ngA&t=1215s) · b000023

**English**

something of interest uh, to your own background. And when I say multimodal, it doesn't necessarily mean that the data set itself must have multimodalities. It should introduce some new data modality that is not commonly touched upon. And technically, language is also a modality. So, you're building a system that is asking questions about molecular structures, your two modalities will be molecular structures and the language they're using to ask and answer questions about that data modality. So, that'll be homework one. And we'll guide you through how you could find and process and visualize, and more importantly, label your data set in preparation for the remaining homeworks. In homework two, once a data set is prepared, uh, it's going to be a homework on designing simple multimodal fusion and supervised learning approaches. So, you're going to be training models from scratch. You're going to be designing models and playing around with various architectures that work really well at

**中文**

与你自己的背景相关、让你感兴趣的东西。这里我说多模态，并不一定意味着数据集本身必须包含多种模态。它应该引入某种不常涉及的新数据模态。而且从技术上讲，语言也是一种模态。因此，如果你要构建一个围绕分子结构提问的系统，你的两种模态就是分子结构，以及用于对这种数据模态进行提问和回答的语言。这就是第一次作业。我们会指导你如何寻找、处理、可视化，以及更重要的，标注数据集，为后续作业做准备。第二次作业中，一旦数据集准备好，呃，就要设计简单的多模态融合和监督学习（supervised learning）方法。你将从头训练模型。你将设计模型，并尝试各种非常擅长

### [21:10](https://www.youtube.com/watch?v=Xm2crsD5ngA&t=1270s) · b000024

**English**

processing that data set, leveraging the principles that you have learned in class, and leveraging what you know about that data modality. So, that'll be homework two. In homework three, we're going to start to adapt multimodal language models, right? Starting with a base LLM, how do you adapt it so that the LLM can basically understand that new data modality you're bringing to it. And when I say understand, it's often evaluated by asking questions to the model and being able to answer questions correctly on that data modality. For example, asking questions about an image, or asking questions about a medical report, or asking questions about some sensing data. In homework four, we're going to extend simple QA, one-step question answering and perception, to multi-step reasoning. How do you build systems that are able to answer more complicated multi-step questions about that data modality? And this will be trained using reinforcement learning that we're introducing in class.

**中文**

处理该数据集的架构，运用你在课堂上学到的原理，以及你对该数据模态的了解。这就是第二次作业。第三次作业中，我们将开始适配多模态语言模型，对吧？从一个基础 LLM 出发，如何对它进行适配，让 LLM 基本上能够理解你引入的那种新数据模态。而我说的理解，通常是通过向模型提问，并看它能否正确回答关于该数据模态的问题来评估的。例如，询问有关图像的问题，或有关医疗报告的问题，或有关某些传感数据的问题。第四次作业中，我们会将简单的问答（QA）、单步问答和感知，扩展到多步推理（multi-step reasoning）。如何构建能够回答关于该数据模态的、更复杂的多步问题的系统？我们将使用课堂上介绍的强化学习（reinforcement learning）来训练它。

### [22:04](https://www.youtube.com/watch?v=Xm2crsD5ngA&t=1324s) · b000025

**English**

This will now allow you to elevate these systems to answer harder questions that involve thinking through multiple steps and not simply perceiving something. And finally, in homework five, we're going to turn these QA systems into agents. Systems that can basically automatically take actions in some environment grounded in your data modality. For example, if you're looking at a manufacturing domain, three and four we're just asking and answering questions about sensors so you can understand the state of the system. In homework five, you're actually going to develop a system that can take actions to optimize the quality of the manufacturing process. So, that'll be homework five. And again, all of these homeworks, they're going to build upon each other, right? You're starting with some data, you're training simple classification models to learn representations, you're going to simple LLMs to more advanced reasoning, and finally agentic systems. And all of this is again also help uh

**中文**

这样，你就能提升这些系统，让它们回答更难的问题，这些问题需要多步思考，而不仅仅是感知某样东西。最后，第五次作业中，我们会把这些 QA 系统变成智能体。也就是能够在以你的数据模态为依托的某个环境中，基本上自动采取行动的系统。例如，如果你关注制造领域，第三和第四次作业只是围绕传感器提问和回答，让你了解系统的状态。第五次作业中，你将真正开发一个能够采取行动、优化制造过程质量的系统。这就是第五次作业。同样，所有这些作业都会相互衔接，对吧？你从一些数据开始，训练简单的分类模型（classification models）来学习表示，然后从简单的 LLMs 走向更高级的推理，最后是智能体系统。而所有这些也都是帮助，呃，

### [22:59](https://www.youtube.com/watch?v=Xm2crsD5ngA&t=1379s) · b000026

**English**

meant to help your course project because these are basically baselines, so things that already exist. You're basically implementing them and trying out how they perform. Throughout the process, you realize that maybe LLMs don't work on your system or agentic models don't work for your system. And then that gives you ideas for developing new methods for your course project. There are some seats over here if you want to sit down. Okay. So those are the five homework assignments. Roughly 2 weeks each, 35% of your grade. And also all of this will be very guided. We're going to give, you know, Colab notebooks. We're going to ask you all to fill out different portions of the code. We're also going to give skeletons in the form of Colab notebooks so that you're guided in not doing everything from scratch. We're also going to be providing some amount of compute so you can run these systems on your data.

**中文**

旨在帮助你的课程项目，因为这些基本上都是基线（baselines），也就是已经存在的东西。你基本上是在实现它们，并尝试它们的表现。在这个过程中，你可能会发现 LLMs 不适用于你的系统，或者智能体模型不适用于你的系统。这就能为你开发课程项目的新方法提供思路。如果想坐下，这边还有一些座位。好。所以，这就是五次作业。每次大约 2 周，占总成绩的 35%。而且，所有这些都会有非常具体的指导。我们会提供 Colab notebooks。我们会要求大家填写代码的不同部分。我们还会以 Colab notebooks 的形式提供骨架，让你有指导，不必从头完成所有东西。我们也会提供一定的计算资源，让你能在自己的数据上运行这些系统。

### [23:51](https://www.youtube.com/watch?v=Xm2crsD5ngA&t=1431s) · b000027

**English**

So, second grading objective, second evaluation of the course is through reading assignments. There's going to be five reading assignments, released at the same time as the five homeworks. Each of these will involve two required papers and some suggested but optional papers alongside five to six discussion prompts. These papers are usually going to cover some state-of-the-art concept in multimodal AI. And the goal of these reading assignments is to first read the papers and summarize your notes from these readings, to also scout for additional papers that are related to the ones that we gave, but also broadening your view by scouting for additional papers and they might come from different perspectives. And finally to use both the assigned papers and the papers that you have found to holistically answer the discussion prompts. So reflecting upon and synthesizing your answers to these discussion prompts. And these discussion prompts will usually be

**中文**

那么，第二个评分目标，课程的第二种考核方式，是阅读任务。一共有五次阅读任务，与五次作业同时发布。每次包括两篇必读论文和一些推荐但可选的论文，以及五到六个讨论问题。这些论文通常会涵盖多模态 AI 的某个 state-of-the-art 概念。这些阅读任务的目标是，首先阅读论文并总结阅读笔记，同时寻找与我们提供的论文相关的其他论文，也通过寻找其他论文来拓宽视野，它们可能来自不同的视角。最后，使用指定论文和你自己找到的论文，全面回答讨论问题。也就是对这些讨论问题进行反思，并综合形成你的答案。这些讨论问题通常会

### [24:45](https://www.youtube.com/watch?v=Xm2crsD5ngA&t=1485s) · b000028

**English**

pretty open-ended. There's not going to be a single right answer. There's usually going to be some trade-offs between different perspectives. And the goal is to really understand both perspectives and to come up with your own assessment of the problem. All right, no no single right answer. So, reading assignments will be 15%. Uh midterm will be 15%. That'll be towards the middle of the semester. And the final 35% will be the course project. So, the course project is to meant to introduce students to the research process. And that entails being able to learn how to read literature in some space, being able to become familiar with your application domain, trying various state-of-the-art models. And again, the homework is meant to prove you to try state-of-the-art models. From state-of-the-art classification models to language models to reasoning models to agentic models. These are all just trying state-of-the-art models on your data. Uh based on these state-of-the-art models,

**中文**

相当开放。不会只有一个正确答案。不同观点之间通常会存在一些取舍。目标是真正理解双方的观点，并形成你自己对问题的判断。好的，没有，没有唯一的正确答案。所以，阅读任务占 15%。呃，期中考试占 15%，会安排在学期中间附近。最后的 35% 是课程项目。课程项目旨在让学生了解研究过程。这包括学会如何阅读某个领域的文献，熟悉自己的应用领域，并尝试各种 state-of-the-art 模型。同样，作业旨在推动你尝试 state-of-the-art 模型。从 state-of-the-art 分类模型，到语言模型、推理模型，再到智能体模型。这些都是在你的数据上尝试 state-of-the-art 模型。呃，基于这些 state-of-the-art 模型，

### [25:42](https://www.youtube.com/watch?v=Xm2crsD5ngA&t=1542s) · b000029

**English**

what differentiates from just implementing baselines to research is to understand the limitations of these current models. So, where they fail, performing error analysis, and then developing and iterating on these new methods to come up with new approaches to overcome some significant limitation. All right, so that turns it from just implementing state-of-the-art baselines on your data to actually coming up with something new. And the goal of course project is to incentivize this last part. Uh this will be done in groups of two to three students. Ideally, those who share some common interests and some common domain knowledge about the problems at hand. Each group will also be assigned a mentor, either myself, one of the other co-instructors, or one of the TAs. So, these folks will give you pretty hands-on guidance on your research projects. And these course projects are meant to be equal contribution among teammates, uh tracked via updates with the mentors,

**中文**

从仅仅实现基线到开展研究，区别在于理解这些现有模型的局限。也就是它们在哪里失败，进行错误分析（error analysis），然后开发并迭代这些新方法，提出新的方案，克服某个重要的局限。这样，就从仅仅在你的数据上实现 state-of-the-art 基线，变成了真正提出新东西。课程项目的目标就是鼓励最后这一部分。呃，项目由两到三名学生组成小组完成。理想情况下，组员对所研究的问题有共同的兴趣和领域知识。每个小组还会分配一位导师，可能是我、其他联合授课教师之一，或者一位助教。这些导师会非常具体地指导你们的研究项目。而且，这些课程项目要求组员贡献相当，呃，我们会通过与导师的进度更新、

### [26:32](https://www.youtube.com/watch?v=Xm2crsD5ngA&t=1592s) · b000030

**English**

presentations, and also any code or writing reports that are due. So, a timeline for the course projects. This is week one. I'm going to hope that everybody decides whether they want to take or drop the course this week. And in week two, we're going to ask people to fill in a project preferences form. This should outline what you're most interested in and uh uh whether there's any teammates that you've already identified or whether you need help from us assigning teammates to your group. So, that'll be week two, a project purposes form. In week four, a project proposal will be due. This will be a short one-to-two-page report that outlines a literature review for your field of interest and several research ideas that you might want to pursue during the semester. Between week four and week nine, so roughly week six, you're you're meant to maybe start processing your data set, running different baselines, getting a getting a handle of what works and what

**中文**

展示，以及到期需提交的任何代码或书面报告来跟踪。因此，课程项目的时间安排如下。现在是第一周。我希望大家在本周决定是否选修或退选这门课。第二周，我们会请大家填写项目偏好表。这份表应该说明你最感兴趣的内容，以及，呃，呃，你是否已经确定了队友，或者是否需要我们帮助为你的小组分配队友。所以，第二周是项目目的表。第四周，需要提交项目提案。这是一份简短的一到两页报告，概述你感兴趣领域的文献综述，以及本学期可能想探索的几个研究想法。在第四周和第九周之间，也就是大约第六周，你，你应该开始处理数据集，运行不同的基线，了解哪些有效，哪些

### [27:27](https://www.youtube.com/watch?v=Xm2crsD5ngA&t=1647s) · b000031

**English**

doesn't. So, that by week nine, your midterm report, you would have several baselines implemented for your data, done some basic error analysis of whether these baselines work or not, and use that to update what your research ideas will be for the second half of the semester. Um between week 11 and 13, you will start implementing a research idea together with doing error analysis and ablations on your approach, seeing what works and seeing what doesn't, iterate a couple of times so that by week 15, for final presentations, you will describe the research ideas that you've explored with analysis, results, and discussion of what worked and what didn't. And finally, week 16, uh the week after your final presentations with feedback from your your classmates and from the instructors, you will submit a final report detailing your findings. So, this course project um

**中文**

无效。这样，到第九周提交期中报告时，你应该已经为自己的数据实现了几个基线，进行了一些基本的错误分析，判断这些基线是否有效，并据此更新学期后半段的研究想法。嗯，在第 11 到 13 周之间，你们会开始实现一个研究想法，同时对自己的方法进行错误分析和消融实验（ablations），看看哪些有效、哪些无效，迭代几次。这样，到第 15 周最终展示时，你们就能介绍探索过的研究想法，给出分析、结果，并讨论哪些有效、哪些无效。最后，第 16 周，呃，也就是最终展示后的一周，你们根据同学和教师的反馈，提交一份详细说明研究发现的最终报告。所以，这个课程项目，嗯，

### [28:21](https://www.youtube.com/watch?v=Xm2crsD5ngA&t=1701s) · b000032

**English**

5% for the proposal report, 10% for the midterm report, and 20% total for the final report and presentations, right? Constituting 35% of your grade.

**中文**

提案报告占 5%，期中报告占 10%，最终报告和展示合计占 20%，对吧？总共占成绩的 35%。

### [28:38](https://www.youtube.com/watch?v=Xm2crsD5ngA&t=1718s) · b000033

**English**

All right, any questions about the main deliverables for the course and grading scheme?

**中文**

好了，关于这门课的主要提交内容和评分方案，大家有什么问题吗？

### [28:52](https://www.youtube.com/watch?v=Xm2crsD5ngA&t=1732s) · b000034

**English**

&gt;&gt; Uh lectures are going to be recorded, but primarily to release on my YouTube. Uh but students should attend live the lectures wherever possible. Please let us know if you plan to miss, you know, more than a few lectures during the semester so that we can plan ahead. Uh there's going to be some some wild cards or late days for the assignments. For homeworks and reading assignments, there'll be two late days per student. This Each late day allows you to extend the the due date by 24 hours, uh but a maximum of one per assignment can be used. And for project wild cards, there's going to be two per team, which again extends either of the deadlines by 24 hours. Um it gives you a 24-hour extension and can be used together, so extended by 2 days. It can be used for either a proposal report, midterm report, or final report, uh but it cannot be used for the final presentation because that all has to be

**中文**

 &gt;&gt; 呃，课程会录制，但主要是发布到我的 YouTube 上。不过，学生应尽可能到现场听课。如果你计划在学期内缺席不止几节课，请告知我们，以便我们提前安排。呃，作业会有一些通用延期额度（wild cards）或延期天数（late days）。对于作业和阅读任务，每位学生有两天延期额度。这，每一天延期额度都允许你将截止时间延长 24 小时，但每次作业最多只能使用一天。对于项目的 wild cards，每组有两次，同样可以将某个截止时间延长 24 小时。嗯，每次提供 24 小时延期，而且可以合并使用，也就是延长 2 天。它可以用于提案报告、期中报告或最终报告，但不能用于最终展示，因为所有展示都必须

### [29:50](https://www.youtube.com/watch?v=Xm2crsD5ngA&t=1790s) · b000035

**English**

done on the same day. It's either going to be slide presentations or maybe a poster presentation in the space outside. We have a course website at that link. Uh so it's mostly meant to be a public-facing version where I release all the the slides and lecture videos sporadically. Uh we're also going to set up Canvas uh enroll everybody in Canvas after we figure out um everyone who's taking our course, and that'll be used to track homework and project submissions.

**中文**

在同一天完成。可能是幻灯片展示，也可能是在外面的区域进行海报展示。课程网站就在那个链接。呃，它主要是面向公众的版本，我会不定期发布所有幻灯片和课程视频。呃，我们还会设置 Canvas，在确定所有选课学生之后，将大家加入 Canvas，用来跟踪作业和项目的提交情况。

### [30:25](https://www.youtube.com/watch?v=Xm2crsD5ngA&t=1825s) · b000036

**English**

Let me turn your attention to the syllabus. So if you go to the website, there's a tab on syllabus, and if you click on it, you're going to be led to a Google Doc with a syllabus. So this is will detail all the content for Tuesday lectures and Thursday lectures, alongside uh when we expect the homeworks to be out Uh for each of the homeworks. I just want to highlight one quick thing. So, you can see here that today 3rd February, that's course introduction. And then I'll be giving a lecture on multimodal data sets on this Thursday. And next Tuesday is going to be a data sets tutorial. So, essentially we're going to have five tutorials spread out according throughout the semester. Each of the tutorials are meant to introduce to you what is delivered and what is expected to be delivered in that homework. So, homework one is going to be about, you know, processing your data sets and understanding and visualizing them. We're going to give a short tutorial

**中文**

请大家看一下教学大纲。如果你打开网站，会看到一个 syllabus 标签，点击后会进入一个包含教学大纲的 Google Doc。这里会详细列出周二和周四课程的所有内容，以及我们预计每次作业发布的时间。我只想快速强调一点。你可以看到，今天是 2 月 3 日，内容是课程介绍。本周四我会讲多模态数据集。下周二则是数据集辅导课。因此，我们基本上会在整个学期分散安排五次辅导课。每次辅导课旨在向大家介绍该次作业提供什么，以及预期提交什么。第一次作业是处理、理解并可视化你的数据集。我们会给出一个简短的辅导，

### [31:21](https://www.youtube.com/watch?v=Xm2crsD5ngA&t=1881s) · b000037

**English**

about how people typically process and visualize data sets and best practices. And in the first tutorial we're also going to cover, you know, introduction to Python, PyTorch, and basic, you know, tensors and modeling in PyTorch. In preparation for homework two, which will be about multimodal fusion and supervised learning, we're going to have a tutorial on multimodal fusion. So, that's going to be running through code of how different fusion architectures are implemented in PyTorch, you know, recapping what was taught in course during the lectures, but not providing new material, but rather implementations and code and stepping through the code for that material. Hopefully that will be that will be useful for preparing for the homeworks. That will be led by the the TAs. The third tutorial will be on multimodal LLMs. So, that will again be stepping through actual code implementations of pre-training and fine-tuning these multimodal LLMs, which will be in preparation for homework three.

**中文**

介绍人们通常如何处理和可视化数据集，以及最佳实践。在第一次辅导课中，我们还会介绍 Python、PyTorch，以及基本的张量（tensors）和 PyTorch 建模。为准备第二次关于多模态融合和监督学习的作业，我们会安排一次多模态融合辅导课。我们会逐步讲解不同融合架构如何在 PyTorch 中实现的代码，回顾课堂上讲授的内容，但不提供新材料，而是提供这些内容的实现与代码，并逐步讲解代码。希望这对准备作业有所帮助。这部分将由助教负责。第三次辅导课将讲多模态 LLMs。同样，我们会逐步讲解这些多模态 LLMs 的预训练和微调的实际代码实现，为第三次作业做准备。

### [32:17](https://www.youtube.com/watch?v=Xm2crsD5ngA&t=1937s) · b000038

**English**

We can do some of that for your data. Tutorial four will be on multimodal reasoning and tutorial five will be on multimodal agents in preparation for the last two homeworks.

**中文**

我们可以针对你的数据做其中一些内容。第四次辅导课将讲多模态推理，第五次辅导课将讲多模态智能体，为最后两次作业做准备。

### [32:33](https://www.youtube.com/watch?v=Xm2crsD5ngA&t=1953s) · b000039

**English**

All right. Any final questions about logistics? Grading, lectures, course websites, course projects?

**中文**

好了。关于课程安排还有最后的问题吗？评分、讲课、课程网站、课程项目？

### [32:50](https://www.youtube.com/watch?v=Xm2crsD5ngA&t=1970s) · b000040

**English**

Okay. If there's no questions, let me jump into introduction to multimodal AI. Let me start this introduction by first giving a historical perspective. Right? Uh I think multimodal AI started sometime in the 1970s and '80s. And the first phase of multimodal AI was the behavioral phase, where you know, back then AI wasn't super advanced. Uh people didn't have access to computers or deep learning. And the first phase of multimodal AI was really about understanding how people communicated, how people used language and gestures and other modalities to communicate with other people. At this point, there was a very seminal work by the psychologist at the University of Chicago called David McNeill, who studied the interaction between language and gestures. So, for McNeill, gestures were central to how we communicated our expressions and emotions. Whereas at

**中文**

好。如果没有问题，我就进入多模态 AI 的介绍。首先，我想从历史角度开始。对吧？呃，我认为多模态 AI 大约起源于 1970 年代和 1980 年代。多模态 AI 的第一个阶段是行为阶段（behavioral phase），那时 AI 还不是很先进。呃，人们无法使用计算机或深度学习（deep learning）。多模态 AI 的第一阶段，主要是理解人们如何交流，如何使用语言、手势和其他模态与别人交流。当时，University of Chicago 的一位心理学家 David McNeill 开展了一项非常具有开创性的研究，研究语言与手势之间的互动。对 McNeill 来说，手势是我们传达表达与情绪的核心。而在

### [33:47](https://www.youtube.com/watch?v=Xm2crsD5ngA&t=2027s) · b000041

**English**

that time, you most other people just thought language was a primary medium for communication and gestures were basically an afterthought. So, David McNeill pointed to this effect, it's called the McGurk effect. I'm going to play two videos illustrating the McGurk effect, and I want you to look at the similarities and differences between these two videos. Here's the first video.&gt;&gt; Ba. Ba. Ba. Ba. Ba. Ba.&gt;&gt; Okay. And here's the second video.&gt;&gt; Ba. Ba. Ba. Ba. Ba. Ba.&gt;&gt; Who can tell me what's interesting about the similarities and differences between these two videos? Yes.&gt;&gt; It seems like the same audio with a different video. Same password but

**中文**

那个时候，其他大多数人只是认为语言是交流的主要媒介，手势基本上是附带的。因此，David McNeill 指出了这种效应，叫作 McGurk effect。我将播放两个展示 McGurk effect 的视频，希望大家观察这两个视频的相同点与不同点。这是第一个视频。&gt;&gt; Ba。Ba。Ba。Ba。Ba。Ba。&gt;&gt; 好。这是第二个视频。&gt;&gt; Ba。Ba。Ba。Ba。Ba。Ba。&gt;&gt; 谁能告诉我，这两个视频的相同点和不同点有什么有趣之处？好的。&gt;&gt; 感觉是同样的音频配上不同的视频。同样的密码，但是

### [34:44](https://www.youtube.com/watch?v=Xm2crsD5ngA&t=2084s) · b000042

**English**

&gt;&gt; Have you seen this before?&gt;&gt; Um seen before.&gt;&gt; Okay. Well, spoilers. Um So, whenever I talk about this, I mean, in class most people some people will be on their laptops and they wouldn't even realize that we had moved on from the first video to the second, right? Because the audio is exactly the same. The audio is exactly the same and the only difference is the movement of the mouth that the speaker was making, whether they were making a ba with a B, ba, or a fa with an F. And this is a really cool experiment because previously people just thought that, you know, sound basically all you needed to hear was what the person was speaking and that was important for recognizing speech. But through this experiment you then started realizing that it's actually really important to contextualize the audio together with the visuals and how the person's lips were moving to perceive speech from the person.

**中文**

 &gt;&gt; 你以前看过这个吗？&gt;&gt; 嗯，以前看过。&gt;&gt; 好吧，剧透了。嗯，每次我讲这个时，我是说，课堂上大多数人，有些人会在用笔记本电脑，他们甚至意识不到我们已经从第一个视频切换到了第二个，对吧？因为音频完全一样。音频完全一样，唯一的区别是说话者的嘴部动作，是在发带 B 的 ba，ba，还是带 F 的 fa。这是一个非常有意思的实验，因为以前人们认为，声音基本上，你需要听到的只是那个人说的话，这对于识别语音很重要。但通过这个实验，人们开始意识到，要感知对方的语音，将音频与视觉信息，以及对方嘴唇的运动结合起来理解，实际上非常重要。

### [35:42](https://www.youtube.com/watch?v=Xm2crsD5ngA&t=2142s) · b000043

**English**

So, that kind of started this behavioral era where people looked at analyzing uh how people communicate using both audio and visual and how people perceived how people communicate from both audio and visual channels. That was research from 1970s, 1980s. Naturally, after studies of human communication, people wanted to build computational models, right? Models that could basically perceive speech and interact with people just like how people can. So, that led to this computational era of multimodal AI. Then came the interaction era where you started building computational models for a single person perceiving and yeah, and generating speech. Now, can you start building systems that are interactive in nature, right? Between a person and a robot or a person, multiple people and multiple robots interacting with each other using speech and gestures. And finally, in the 2010s, we started seeing this deep learning era, where massive amounts of compute, massive

**中文**

所以，这在某种程度上开启了行为时代（behavioral era），人们开始分析人们如何同时使用音频和视觉进行交流，以及人们如何通过音频和视觉两个通道感知他人的交流。这是 1970 年代、1980 年代的研究。自然，在研究人类交流之后，人们希望构建计算模型（computational models），对吧？这些模型基本上能够像人一样感知语音并与人互动。这就引出了多模态 AI 的计算时代（computational era）。之后进入互动时代（interaction era），你开始为单个人构建用于感知、是的，以及生成语音的计算模型。现在，能否开始构建本质上具有交互性的系统，对吧？让人与机器人，或者一个人、多个人和多个机器人，使用语音与手势相互互动。最后，在 2010 年代，我们开始看到深度学习时代，大量的计算资源、大量的

### [36:37](https://www.youtube.com/watch?v=Xm2crsD5ngA&t=2197s) · b000044

**English**

GPUs, and very powerful large-scale models enabled us to achieve multimodal capabilities that we previously were not able to. And primarily, in the 2010 in the 2020s, we started seeing this foundation model era, where we further scaled up the amount of data and compute and models that we're able to train. So, just some really cool examples of various eras. In the computational era, we had really cool examples of building multimodal interfaces, where people could, you know, speak and point to a certain location, and AI systems that could basically understand both speech and gestures from people. We had examples of systems that could understand randomly understand various aspects of the human body, looking at gestures first, and then started to look at body tracking and post tracking. Here's an example of a system that could understand pose and gestures of different people.

**中文**

GPUs，以及非常强大的大规模模型，让我们实现了以前无法达到的多模态能力。而主要是在 2010，在 2020 年代，我们开始看到基础模型时代（foundation model era），我们进一步扩大了数据量、计算量，以及能够训练的模型的规模。这里举几个不同时代非常有意思的例子。在计算时代，我们有构建多模态界面（multimodal interfaces）的有趣例子，人们可以一边说话，一边指向某个位置，而 AI 系统基本上能够同时理解人们的语音与手势。我们也有一些系统的例子，能够理解，随机地理解人体的各个方面，先研究手势，然后开始研究身体跟踪（body tracking）和 post tracking \[字幕疑误，可能指 pose tracking\]。这里是一个能够理解不同人的姿态与手势的系统示例。

### [37:31](https://www.youtube.com/watch?v=Xm2crsD5ngA&t=2251s) · b000045

**English**

And around that same time, we also saw systems that were much better at digitizing various forms of multimedia information. Systems that could essentially take in text and retrieve books, retrieve videos, retrieve images, all your precursors to today's YouTube and large-scale search engines. In the interaction era, we saw projects that were precursors to Zoom, right? Projects that looked at lots of people discussing different topics with audio and visual, transcribing all their text, and trying to see what kind of discussions emerged that led to creative ideas. So, precursors to studies of social science and precursors to to tools like Zoom. And in the interaction era, we also saw lots of interest in building systems that could better recognize emotions of different people. Recognizing not just what people were saying, but how they

**中文**

大约同一时期，我们也看到了更擅长将各种多媒体信息数字化的系统。这些系统基本上可以接收文本，然后检索书籍、检索视频、检索图像，它们都是如今 YouTube 和大规模搜索引擎的前身。在互动时代，我们看到了 Zoom 的前身项目，对吧？这些项目通过音频和视觉观察许多人讨论不同话题，转录他们说的所有文字，并尝试了解什么样的讨论会产生创造性的想法。因此，它们是社会科学研究的前身，也是 Zoom 等工具的前身。在互动时代，我们还看到人们非常关注构建能够更好识别不同人情绪的系统。不仅识别人们说了什么，还识别他们说这些话时

### [38:26](https://www.youtube.com/watch?v=Xm2crsD5ngA&t=2306s) · b000046

**English**

felt and what they were thinking when they were saying them. And of course, most of us are here in this course because we're interested in deep learning era. Right? In the early 2010s, we saw huge amount of investment in compute and GPU resources that enabled us to train much more powerful models than previously available. Some of these uh early models involved um Some of these early models involved, for example, captioning. Given an image, can you generate a pretty realistic caption for that image? And that saw the connection of CNNs that processed the image with LSTMs that could decode a caption given the representations extracted from the image.

**中文**

的感受和想法。当然，我们大多数人来上这门课，是因为对深度学习时代感兴趣，对吧？在 2010 年代初期，我们看到了对计算和 GPU 资源的巨额投入，这使我们能够训练出比以前强大得多的模型。其中一些，呃，早期模型涉及，嗯，其中一些早期模型涉及，例如，描述生成（captioning）。给定一张图像，你能否为它生成一段相当符合实际的描述？这促成了处理图像的卷积神经网络（CNNs）与长短期记忆网络（LSTMs）的连接，后者能够根据从图像提取的表示，解码生成一段描述。

### [39:08](https://www.youtube.com/watch?v=Xm2crsD5ngA&t=2348s) · b000047

**English**

And here's also what I think is a really good timeline to chart out the different multimodal tasks that people were interested in. We had the behavioral era where people started looking at how people communicate. And naturally, the first task that people designed multimodal AI systems to do was audio-visual speech recognition. Looking at both the audio, the sounds, and the visual information from people to recognize what they were saying. Right? That intersected between what was interesting to the computational people with what was interesting to the behavioral people, audio-visual speech recognition. After audio-visual speech recognition and the um the computational era, we saw lots of interest in video retrieval. So, given a large multimedia corpus, can you input language and retrieve the right video corresponding to that input query? We saw examples of recognizing affect and emotions of video from people.

**中文**

这里还有一条我认为非常好的时间线，展示人们感兴趣的不同多模态任务。在行为时代，人们开始研究人如何交流。自然，人们最先设计多模态 AI 系统去完成的任务，是视听语音识别（audio-visual speech recognition）。同时观察人们的音频、声音，以及视觉信息，识别他们说了什么，对吧？视听语音识别正是计算研究者与行为研究者兴趣的交叉点。在视听语音识别以及计算时代之后，我们看到了人们对视频检索（video retrieval）的浓厚兴趣。因此，给定一个大型多媒体语料库（multimedia corpus），能否输入语言，检索与该输入查询对应的正确视频？我们也看到了从人的视频中识别情感与情绪的例子。

### [40:05](https://www.youtube.com/watch?v=Xm2crsD5ngA&t=2405s) · b000048

**English**

In the interaction era, we also saw lots of interest in recognizing events in videos, what people were doing, and what they felt when they were doing it. Perhaps the one of the key drivers in the deep learning era was image captioning. So, how do you take an image and generate a very realistic caption for that image? And that was really surprising at the time because whereas previous models were only able to just make a prediction, like a classification of what sentiment or a classification of what video was happening, image captioning enabled us to generate much more open-ended captions. And that was enabled by, you know, powerful progress in CNNs for image processing and LSTMs for text captioning. And this is perhaps the birth of language and vision research. That allowed people to really build systems that could understand vision and generate captions.

**中文**

在互动时代，人们也非常关注识别视频中的事件、人们在做什么，以及他们做这些事时的感受。深度学习时代的关键驱动力之一，可能是图像描述生成（image captioning）。如何输入一张图像，并为它生成非常符合实际的描述？这在当时非常令人惊讶，因为此前的模型只能做预测，比如判断情感类别，或者对视频中发生的事情进行分类，而 image captioning 使我们能够生成开放程度高得多的描述。这得益于用于图像处理的 CNNs 和用于文本描述生成的 LSTMs 的重大进展。这可能就是语言与视觉研究的诞生。它让人们能够真正构建既理解视觉又生成描述的系统。

### [40:58](https://www.youtube.com/watch?v=Xm2crsD5ngA&t=2458s) · b000049

**English**

And since 2014, we've seen so much progress, right? From image captioning to video captioning. People found that image captioning and video captioning are really hard to evaluate. So, people started developing QA systems. Instead of open-ended generation of a caption from an image, then I ask a very specific a question about the image and assess whether the AI system gave me the right answer. So, this started visual question answering models and subsequently video question answering models. From then on, we saw examples of multimodal dialogue. Extending language-based dialogue between a human AI systems to dialogue that was grounded in either image or video that a user could give. We saw examples of large-scale video retrieval uh catalyzed with large YouTube datasets. How do you build systems that can take in a video and recognize events in a video? Or how can you find a uh semantically similar video to some other query video that you're given?

**中文**

自 2014 年以来，我们看到了很多进展，对吧？从图像描述生成到视频描述生成（video captioning）。人们发现，图像描述生成和视频描述生成很难评估。所以，人们开始开发 QA 系统。不再从图像开放式生成描述，而是针对图像提出一个非常具体的问题，再评估 AI 系统是否给出了正确答案。于是出现了视觉问答（visual question answering）模型，随后是视频问答（video question answering）模型。之后，我们看到了多模态对话（multimodal dialogue）的例子。将人与 AI 系统之间基于语言的对话，扩展成以用户提供的图像或视频为依托的对话。我们看到了大型 YouTube 数据集推动大规模视频检索的例子。如何构建能够接收视频并识别视频中事件的系统？或者，如何找到一个与给定查询视频在语义上相似的视频？

### [41:57](https://www.youtube.com/watch?v=Xm2crsD5ngA&t=2517s) · b000050

**English**

Soon after, this coincided with the era where people were looking at reinforcement learning. So, it came an era where we built systems that could take in vision and language and navigate. Right? Robots that could take in a language instruction, for example, go to the fridge and could actually navigate through your house and go towards the fridge. And after 2022, we saw lots of cool progress in generative models. So, that kick-started a wave of text-to-image generation research, text-to-video generation research, and nowadays agentic AI, multimodal agents that could basically do a lot of tasks, right? Answer questions, but also take actions uh grounded in different environments.

**中文**

不久之后，这与人们开始研究强化学习的时期重合。于是，我们进入了构建能够接收视觉和语言并进行导航的系统的时代，对吧？机器人可以接收语言指令，例如“去冰箱那里”，然后真的穿过你的房子，走向冰箱。2022 年之后，我们看到了生成模型（generative models）的许多有趣进展。这开启了一波文本到图像生成（text-to-image generation）研究、文本到视频生成（text-to-video generation）研究，以及如今的智能体 AI（agentic AI）。这些多模态智能体基本上能够完成很多任务，对吧？回答问题，也能以不同环境为依托采取行动。

### [42:42](https://www.youtube.com/watch?v=Xm2crsD5ngA&t=2562s) · b000051

**English**

And just in 2025, right? I think some of the most interesting examples of multimodal AI being successful include video generation and world models. All of this is actually just generated by AI systems that takes in a text prompt and generates super super realistic video, sometimes with audio at the same time, and at the same time being able to condition on various actions, right? So, you can see some of this um things in the bottom left being highlighted. You can press up, down, left, right keys, and you can change the position and direction that a person in the video generation is going. We have seen progress in virtual agents that are super realistic and super human-like. And people are starting to use these virtual agents for uh for health, for well-being, for therapy, for um conversing with people, especially old people so they don't feel lonely. And of course, that comes lots of opportunities, but also different risks of using such models for real

**中文**

仅在 2025 年，对吧？我认为，多模态 AI 成功的一些最有趣的例子，包括视频生成和世界模型（world models）。这些实际上都是 AI 系统生成的，它们接收文本提示（text prompt），生成极其、极其逼真的视频，有时还会同时生成音频，同时又能以各种动作作为条件（condition on），对吧？你可以看到左下角有一些东西被高亮标出。你可以按上、下、左、右键，改变生成视频中的人物所处的位置和行进方向。我们也看到了非常逼真、非常像人的虚拟智能体（virtual agents）的进展。人们开始把这些虚拟智能体用于健康、福祉、治疗，以及与人交谈，尤其是老年人，让他们不感到孤独。当然，这带来了许多机会，但将这些模型用于真实的

### [43:40](https://www.youtube.com/watch?v=Xm2crsD5ngA&t=2620s) · b000052

**English**

human interaction. And nowadays, we're also starting to go beyond multimedia domains in language, vision, and audio to other data modalities like touch, to smell, to taste, to real-world sensing, to biology, to health, and more. So, clearly it's a great time to be studying multimodal AI. Okay. So, enough examples. I'm going to cover in the last 30 minutes of the course of this lecture, I'm going to cover some basics of multimodal AI. And this is meant to prepare you for uh the semester that's going to come up ahead. So, a lot of this is based on the survey paper that we wrote called Foundations and Recent Trends of Multimodal Machine Learning. It covers several key definitions of multimodal AI, several principles of multimodal data, and

**中文**

人际互动，也会带来不同的风险。如今，我们也开始超越语言、视觉和音频这些多媒体领域，拓展到触觉、嗅觉、味觉、现实世界感知、生物学、健康等其他数据模态。因此，显然现在是学习多模态 AI 的好时机。好，例子就讲到这里。在这门课，这节课的最后 30 分钟，我会介绍一些多模态 AI 的基础知识。这是为了帮助大家为接下来的学期做好准备。其中很多内容基于我们撰写的综述论文 Foundations and Recent Trends of Multimodal Machine Learning。它涵盖了多模态 AI 的几个关键定义、多模态数据的几条原理，以及

### [44:36](https://www.youtube.com/watch?v=Xm2crsD5ngA&t=2676s) · b000053

**English**

several key research challenges. So, firstly, what is a modality? Right? I tend to think of a modality as some way in which a physical phenomena is expressed or perceived in the world. And when we think of a multimodal AI, you usually have to think of a sensor. Right? A sensor is often used to collect real-world information and convert them into some digital space, digital representation that we can then start processing using computational AI methods. So, given these sensors, it's helpful to think of a spectrum of of modalities from raw modalities that are closer to a sensor to abstract modalities that are further away from a sensor. Raw modalities could be things like a speech signal that's being picked up by a microphone or an image that's being captured by a camera. After more processing, you can start to extract language from speech signals or

**中文**

几个关键研究挑战。首先，什么是模态？对吧？我倾向于将模态理解为物理现象在世界中被表达或被感知的某种方式。而当我们思考多模态 AI 时，通常必须想到传感器，对吧？传感器通常用于收集现实世界的信息，将其转换到某种数字空间，转换为数字表示，随后我们就能使用计算性的 AI 方法开始处理。因此，考虑这些传感器时，可以把模态看成一个谱系，从更接近传感器的原始模态（raw modalities），到距离传感器更远的抽象模态（abstract modalities）。原始模态可以是麦克风拾取的语音信号，或摄像头捕获的图像。经过更多处理后，你可以开始从语音信号中提取语言，或者

### [45:32](https://www.youtube.com/watch?v=Xm2crsD5ngA&t=2732s) · b000054

**English**

extract different objects from images. And after further and further processing, you can then start getting things like sentiment intensity or object categories from those two modalities. So, you can start seeing a spectrum of modalities from more raw, which are closer to a sensor, to more abstract, that are further away and undergo more processing from the sensor. Given these data modalities, multimodal refers to problems that involve different modalities and particularly introduces three core challenges. The first core challenge is that of heterogeneity, the fact that different data modalities are often very different in their representations, in their input data, in the information that they contain, and therefore have to be processed differently. The second and third challenges are what we call connections and interactions. Connected referring to the fact that these data modalities often share some information, which is very important to

**中文**

从图像中提取不同物体。经过进一步、再进一步的处理，你就可以从这两种模态中得到情感强度（sentiment intensity）或物体类别等信息。因此，你可以看到一个模态谱系，从更原始、更接近传感器的模态，到更抽象、距离传感器更远、经过更多处理的模态。对于这些数据模态，多模态指的是涉及不同模态的问题，尤其会带来三个核心挑战。第一个核心挑战是异质性（heterogeneity），也就是不同数据模态在表示、输入数据以及所包含的信息上，往往非常不同，因此必须采用不同的方式处理。第二和第三个挑战，我们称为联系（connections）与交互（interactions）。联系指的是这些数据模态通常共享一些信息，而让你的

### [46:29](https://www.youtube.com/watch?v=Xm2crsD5ngA&t=2789s) · b000055

**English**

exploit by your AI model, and interactions meaning that these data modalities often combine in different ways for some downstream task that you care about. So, let me give you some more details. So, as I've explained, heterogeneity is the phenomenon that information in different modalities often show different qualities, different structures, and different representations. And again, you want to think about heterogeneity as a spectrum. A spectrum from more homogeneous modalities with more similar qualities to heterogeneous modalities with more different qualities. So, as an example, images from two different cameras are more homogeneous, but yet still different, right? You have a camera that's coming in here, and a camera view that's coming in here. They're both visual modalities, so they carry very similar visual structure and spatial information, but because they're coming in from different angles, they still contain different information about the

**中文**

AI 模型利用这些信息非常重要；交互则意味着，对于你关心的某个下游任务，这些数据模态往往以不同的方式组合。让我进一步说明。正如我解释过的，异质性是指不同模态的信息往往呈现不同的性质、结构和表示。同样，你应该把异质性看成一个谱系。从性质更相似、更加同质（homogeneous）的模态，到性质更不同、更加异质（heterogeneous）的模态。例如，来自两个不同摄像头的图像更加同质，但仍然不同，对吧？有一个摄像头从这里拍摄，另一个摄像头视角从这里拍摄。它们都是视觉模态，因此具有非常相似的视觉结构和空间信息，但由于拍摄角度不同，它们仍然包含关于你正在拍摄的

### [47:26](https://www.youtube.com/watch?v=Xm2crsD5ngA&t=2846s) · b000056

**English**

object that you're trying to take a photo off. You can start seeing modalities that are more different. For example, text from two different languages. Let's say you have English and French. These two languages have very different grammar, very different vocabulary, very different structures, but at the same time, they're still primarily quite similar because you can translate from one to the other without too much effort. Language and vision now starts becoming even more different. Language has a sequential spatial a sequential structure, whereas vision has a more spatial structure. And sometimes you can go from language to vision, but often times you also lose information that's in one modality that's not in the other. And finally, you have language and sensors. These are perhaps even more different because sometimes not even clear whether language can can fully capture information in some sensor. So, you see a spectrum, right? From more homogeneous modalities with more similar

**中文**

物体的不同信息。接着可以看到差异更大的模态。例如，两种不同语言的文本。假设是英语和法语。这两种语言的语法、词汇和结构都非常不同，但与此同时，它们总体上仍然相当相似，因为你无需太多努力就能将一种翻译成另一种。语言和视觉之间的差异则开始变得更大。语言具有序列性的空间，序列结构，而视觉则具有更强的空间结构。有时你可以从语言转到视觉，但往往也会丢失一种模态中存在、而另一种模态中不存在的信息。最后，是语言和传感器。它们之间的差异可能更大，因为有时甚至不清楚语言能否完整表达某个传感器中的信息。因此，你看到的是一个谱系，对吧？从性质更相似、更同质的

### [48:23](https://www.youtube.com/watch?v=Xm2crsD5ngA&t=2903s) · b000057

**English**

qualities to more heterogeneous modalities with more different qualities. So, that's the first principle. The idea that modalities show heterogeneity, and it is this heterogeneity that makes these models uh these modalities very difficult to model together. A second principle is that of connections, right? Connections refers to the shared information that relates modalities. If I draw these modalities as two Venn diagrams, the shared information is in position to unique information, which is in one modality but not in the other. And again, you can think about it as a spectrum, right? There's cases of modalities which are stronger and show more connections to those that are weaker and perhaps one that is not even connected without showing any overlap in information at all. If I just give you any example any any example from image and language, you might have image over here and you might

**中文**

模态，到性质差异更大、更异质的模态。这就是第一个原理。模态呈现异质性，正是这种异质性，使这些模型，呃，这些模态非常难以放在一起建模。第二个原理是联系，对吧？联系指的是把模态关联起来的共享信息（shared information）。如果我把这些模态画成两个维恩图（Venn diagrams），共享信息与独有信息（unique information）相对，后者存在于一种模态中，却不存在于另一种模态中。同样，你可以把它看成一个谱系，对吧？有些模态联系更强、更多，有些联系较弱，还有一些甚至没有联系，信息完全没有重叠。如果我随便举一个图像与语言的例子，你这边可能有一张图像，而你可能

### [49:19](https://www.youtube.com/watch?v=Xm2crsD5ngA&t=2959s) · b000058

**English**

have a caption that says a teacup on the right of a laptop in a clean room. You see some examples of connections, right? It refers to the teacup, refers to the right of a laptop, in a clean room, but at same time, there's still a lot of information that is in the image that cannot be described fully in language. For example, the fact that there's a sofa, the shape, the size, the geometry of the sofa, the shape and size and geometry of a table. So, these are examples of parts that are connected, but at same time, information that is one in the visual modality but not in the language.

**中文**

有一段描述，说的是“在一个干净的房间里，笔记本电脑右边有一只茶杯”。你能看到一些联系的例子，对吧？它提到了茶杯，提到了笔记本电脑的右边，提到了干净的房间，但与此同时，图像中仍有很多信息无法用语言完整描述。例如，有一张沙发，以及沙发的形状、大小、几何结构，还有桌子的形状、大小和几何结构。因此，这些例子展示了部分内容之间存在联系，但同时也有一些信息存在于视觉模态中，却不在语言中。

### [49:57](https://www.youtube.com/watch?v=Xm2crsD5ngA&t=2997s) · b000059

**English**

So, principle two describes the fact that modalities are often connected with each other. And the third key principle is that modalities often interact when you're trying to combine them for some task. So, interactions refers to how these modalities combine, how the information is combined for this task. So, again, starting with modalities one and two as Venn diagrams with some connected information between them and also some unique information in one and not the other, you can think of a task as a third circle Y. So, there are several types of interactions that are super interesting. One interaction is that of redundancy. So, this is a phenomena where both modalities gives you the same information about the task, and it is that same information that you must exploit to make a prediction on the task. So, one example is someone saying this movie is great with a huge smile on their face. Like, both of those are examples of

**中文**

所以，第二个原理描述的是，模态通常彼此存在联系。第三个关键原理是，当你尝试为某个任务组合这些模态时，它们通常会发生交互。因此，交互指的是这些模态如何组合，信息如何为这个任务组合。同样，先把模态一和模态二画成维恩图，它们之间有一些相联系的信息，也有一些仅存在于一种模态、而不在另一种模态中的独有信息。你可以把任务看成第三个圆 Y。有几种非常有意思的交互类型。一种交互是冗余（redundancy）。这是一种现象，即两种模态都为你提供关于任务的相同信息，而你必须利用这些相同信息来预测这个任务。一个例子是，有人说“这部电影太棒了”，同时脸上露出灿烂的笑容。这两者都是

### [50:53](https://www.youtube.com/watch?v=Xm2crsD5ngA&t=3053s) · b000060

**English**

positive information being conveyed, and together you are very confident that a person really enjoyed the movie. So, that's an example of redundancy. You're exploiting similar information that is present in both modalities important for the task. So, that's in contrast to unique information. Unique information refers to the presence of information in one that is important to the task, but is not there in the other. So, for example, the person might say, "This movie does a good job developing the characters," which is pretty positive, but with mostly neutral facial expressions. And out of these, it is the first modality that has the positive information that is important for the task.

**中文**

传达正面信息的例子，把它们结合起来，你就很确定这个人真的很喜欢这部电影。这就是冗余的例子。你在利用两种模态中都存在的、对任务很重要的相似信息。这与独有信息相对。独有信息指的是，某种模态中存在对任务很重要、但另一种模态中没有的信息。例如，这个人可能会说：“这部电影在塑造人物方面做得很好。”这相当正面，但面部表情大体是中性的。在这两者之中，是第一种模态包含了对任务很重要的正面信息。

### [51:39](https://www.youtube.com/watch?v=Xm2crsD5ngA&t=3099s) · b000061

**English**

And the third type of interaction is that of synergy, where there is some emerging information that was neither in both modalities or neither in one of the modalities, that only emerges when you start combining these two modalities together. So, one example is when the person say something positive like, "Wow." but with anger or frustration on their face. And then you can start realizing that it's a disagreement, the conflict between these two modalities that indicates a person is actually being sarcastic about that topic. So, that's an example where sarcasm wasn't directly evident uh in both of them, or in one and not the other, but you have to combine them and the sarcasm emerges from these two modalities. So, that's an example of an interaction that is synergistic.

**中文**

第三种交互是协同（synergy），也就是出现了一些新涌现的信息，这些信息既不在两种模态共有的信息中，也不在其中某一种模态中，而是只有在开始将这两种模态结合起来时才会出现。例如，一个人说了像“哇”这样正面的话，但脸上却带着愤怒或沮丧。这时，你就能开始意识到，正是两种模态之间的不一致与冲突，表明这个人实际上在讽刺这个话题。因此，在这个例子中，讽刺并不是在两种模态中都直接可见，也不是存在于一种而不在另一种中，而是必须将它们结合起来，讽刺才会从这两种模态中显现。这就是协同性交互的例子。

### [52:30](https://www.youtube.com/watch?v=Xm2crsD5ngA&t=3150s) · b000062

**English**

So, to summarize, multimodal is the study of problems in which a data modality show heterogeneity, and they are interconnected. Right? And these are the three key principles of multimodal problems. Heterogeneity because data modalities are very different, and their differences cause us problems and challenges in modeling these data modalities together. And at the same time, there are very rich connections, overlapping information between data modalities, and very rich interactions, new ways these modalities combine to provide more information, which makes us want to process them together to learn these connections and interactions. So, to summary, multimodal is a scientific study of heterogeneous and interconnected, which means connections plus interacting data.

**中文**

因此，总结一下，多模态研究的是数据模态呈现异质性，并且彼此相互联系的问题，对吧？这就是多模态问题的三个关键原理。异质性是因为数据模态非常不同，这些差异使我们在将它们一起建模时遇到问题和挑战。同时，数据模态之间又存在非常丰富的联系，也就是重叠信息，以及非常丰富的交互，也就是这些模态以新的方式组合，提供更多信息。这让我们希望把它们一起处理，以学习这些联系与交互。因此，总结来说，多模态是对异质且相互关联的数据的科学研究，这里的相互关联意味着存在联系以及交互。

### [53:23](https://www.youtube.com/watch?v=Xm2crsD5ngA&t=3203s) · b000063

**English**

So, given these key principles of what makes multimodal data unique, why is it difficult? Why is it challenging to model them? So, these challenge can be manifested across six key challenges. What the first key challenge is that of representations. It is often very difficult to learn multimodal representations that capture the fact that these modalities are interacting in certain ways while also dealing with the inherent heterogeneity across the modalities. There's this fundamental conflict between the differences and heterogeneity between them and the commonalities between data modalities. So, this is a core building block and you're deciding what representations to learn is a core building block for almost any multimodal problem. It's often step one in dealing with these multimodal problems. So, schematically, I'm going to represent different modalities like this. So, data A might be a bunch of triangles and modality B

**中文**

那么，了解了这些使多模态数据具有独特性的关键原理之后，为什么它很难？为什么对它们建模具有挑战？这些挑战可以体现为六个关键挑战。第一个关键挑战是表示。学习多模态表示往往很难，既要捕捉这些模态以特定方式交互这一事实，又要处理模态间固有的异质性。模态之间的差异与异质性，以及数据模态之间的共性，存在一种根本冲突。因此，这是一个核心构件，而决定要学习什么表示，是几乎所有多模态问题的核心构件。它通常是处理这些多模态问题的第一步。在示意图中，我会这样表示不同模态。数据 A 可能是一组三角形，模态 B

### [54:20](https://www.youtube.com/watch?v=Xm2crsD5ngA&t=3260s) · b000064

**English**

might be a bunch of circles. Oftentimes, you can think about each triangle as a most basic element in one modality. So, it might be a single word or a single facial expression or a single sense sensor reading or a single chemical. But, most data modalities often come not just as one token but as a sequence of multiple tokens. For example, multiple words that a person is saying or multiple expressions that a person is making across time or multiple chemical molecules they're trying to model together. So, in the case of representation, we're going to first just look at a single element in each modality. So, ignore the rest. We're going to deal with the rest in the other challenges. We're just going to look at a single individual element, the most basic element in each modality. And there's three general ways of learning representations. Both of all three of which are are useful in different settings.

**中文**

可能是一组圆形。通常，你可以把每个三角形看作一种模态中最基本的元素。它可能是一个词、一个面部表情、一个感知，传感器读数，或者一种化学物质。但是，大多数数据模态通常不是只以一个词元（token）的形式出现，而是以多个 tokens 组成的序列出现。例如，一个人说出的多个词，或一个人随时间做出的多个表情，或他们试图一起建模的多个化学分子。因此，在表示这个问题中，我们先只看每种模态中的一个元素。忽略其他元素。我们会在其他挑战中处理剩余部分。现在只看一个单独的元素，即每种模态中最基本的元素。学习表示有三种一般方法。这三种方法在不同的场景中都有用。

### [55:16](https://www.youtube.com/watch?v=Xm2crsD5ngA&t=3316s) · b000065

**English**

Uh we call these three different ways fusion, coordination, and fission. In fusion, it's all about taking these two elements and combining them into one single representation that best combines the information. So, you start from two modality elements and end up with one representation. In coordination, you start with these two elements and you learn a representation for each one. These two representations aren't independent, but you try to coordinate them with some coordination function. Right? So, with two modality elements, you learn two representations while coordinating them. This coordination can be something like cosine similarity or some other similarity function. These can be very useful when you're trying to do retrieval. Right? So, you're taking, for example, an image, learn a really good image representation, but this image representation should be coordinated with a caption so you can retrieve the closest caption given that image

**中文**

呃，我们把这三种方法称为融合（fusion）、协调（coordination）和裂分（fission）。在 fusion 中，重点是将这两个元素组合成一个单一表示，让信息得到最佳结合。因此，你从两个模态元素出发，最终得到一个表示。在 coordination 中，你从这两个元素出发，分别为每个元素学习一个表示。这两个表示不是独立的，而是尝试通过某种协调函数将它们协调起来，对吧？因此，对于两个模态元素，你学习两个表示，同时协调它们。这种协调可以采用余弦相似度（cosine similarity）或其他相似度函数。当你尝试做检索时，这些方法会非常有用，对吧？例如，你输入一张图像，学习一个非常好的图像表示，但这个图像表示应当与一段描述相协调，这样就能根据该图像

### [56:14](https://www.youtube.com/watch?v=Xm2crsD5ngA&t=3374s) · b000066

**English**

representation. Whereas for fusion, you wouldn't be able to do this kind of retrieval. And finally, the third type of learning representation is what we call fusion. So, you start with two elements and you learn this factorized, this disentangled representation space that captures different portions of information. Some portion might be the fact that these two modalities share some common information, and some other portions of the representation capture more unique information in one and not the other. So, we call this fusion. Fusion is obviously less common than fusion and coordination, but when done right, it can also have significant benefits. And nowadays, we're also seeing a rise in these fusion-based architectures with your mixture of experts and your multimodal elements. But, we'll get into those in more detail in future lectures.

**中文**

表示检索最接近的描述。而对于 fusion，你无法进行这种检索。最后，第三种表示学习方法，我们称为 fusion \[字幕疑误，结合前文可能指 fission\]。你从两个元素出发，学习一个因子化（factorized）、解耦（disentangled）的表示空间，用于捕捉不同部分的信息。某些部分可能表示这两种模态共享一些共同信息，而表示的其他部分则捕捉仅存在于一种模态、而不在另一种模态中的更独有的信息。因此，我们称之为 fusion \[字幕疑误，可能指 fission\]。Fusion \[字幕疑误，可能指 fission\] 显然没有 fusion 和 coordination 那么常见，但如果做得好，也能带来显著好处。如今，我们也看到这些基于 fusion \[字幕疑误，可能指 fission\] 的架构随着混合专家（mixture of experts）和多模态元素而兴起。但我们会在之后的课程中更详细地讨论它们。

### [57:08](https://www.youtube.com/watch?v=Xm2crsD5ngA&t=3428s) · b000067

**English**

So, that's challenge one, how to learn representations. And challenge two, the goal is to start aligning data modalities, uh elements from data modalities. So, if you recall, in representation, we looked at just one element from each modality. In alignment, we're going to look at all of these elements. Right? In this case, the goal is to align similarly connected elements from one modality with those in the other. There are three main challenges in learning alignment. The first challenge is what we call discrete alignment. Where the goal just is to learn which element from one modality is matching the element some other modality. For example, which part of the image matches which part of the caption? Right, if I reference a laptop in the image, I reference a laptop here in the caption. This is what we call discrete alignment or discrete connections.

**中文**

这就是挑战一，如何学习表示。挑战二的目标是开始对齐数据模态，呃，来自数据模态的元素。如果你还记得，在表示中，我们只看了每种模态的一个元素。在对齐（alignment）中，我们将观察所有这些元素，对吧？在这里，目标是将一种模态中具有相似联系的元素，与另一种模态中的元素对齐。学习对齐主要有三个挑战。第一个挑战叫作离散对齐（discrete alignment）。目标只是学习一种模态的哪个元素，与另一种模态的元素相匹配。例如，图像的哪一部分对应描述的哪一部分？对吧，如果我指的是图像中的笔记本电脑，这里的描述也提到了笔记本电脑。这就是我们所说的离散对齐，或离散联系（discrete connections）。

### [58:05](https://www.youtube.com/watch?v=Xm2crsD5ngA&t=3485s) · b000068

**English**

It's making several simplifying assumptions here, which is that each modality can be well segmented into discrete bounding boxes. For example, language into discrete tokens or image into discrete object regions. And once you segment into discrete regions, the goal is just learn the matching between your discrete elements. This problem becomes more complicated when it's not so clear how to segment your modality into discrete elements. If I have a high-frequency sensor, for example, it's not super clear how to segment it into discrete boundaries, in which case you have to deal with this continuous alignment problem if you want to align it with something else. So, you have to figure out the granularity and segmentation and discretization of these continuous uh signals. And finally, whereas these two, the goal is to just match the alignment from one modality to the other, a third sub-challenge is what we call contextualized representations.

**中文**

这里做了几个简化假设，即每种模态都能很好地划分为离散的边界框（bounding boxes）。例如，将语言划分为离散 tokens，或将图像划分为离散物体区域。一旦划分成离散区域，目标就只是学习离散元素之间的匹配。当不太清楚如何把模态划分为离散元素时，这个问题就会变得更复杂。例如，如果我有一个高频传感器，就不太清楚如何把它划分为离散边界。在这种情况下，如果想把它与其他东西对齐，就必须处理连续对齐（continuous alignment）问题。因此，你必须确定这些连续信号的粒度、分割方式和离散化方式。最后，前两种挑战的目标只是让一种模态与另一种模态匹配对齐，而第三个子挑战是我们所说的上下文化表示（contextualized representations）。

### [59:03](https://www.youtube.com/watch?v=Xm2crsD5ngA&t=3543s) · b000069

**English**

The goal here is to use the fact that certain modalities are aligned with other modalities in order to learn better representations that can be used for downstream tasks. This is really common in language models and vision language models. In language models, it's all about leveraging the part, you know, leveraging which parts of your context align to which other parts of your context using your attention matrix to learn a better representation that enables next token prediction. How can we extend this to multimodal settings where figuring out which elements should be contextualized with other elements to learn better representations for downstream tasks?

**中文**

这里的目标是，利用某些模态与其他模态已经对齐这一事实，学习可用于下游任务的更好表示。这在语言模型和视觉语言模型（vision language models）中非常常见。在语言模型中，核心是利用部分，你知道，利用上下文中的哪些部分与其他哪些部分对齐，通过注意力矩阵（attention matrix）学习更好的表示，从而实现下一个 token 预测（next token prediction）。我们如何把这扩展到多模态场景，弄清哪些元素应结合其他元素进行上下文化，从而为下游任务学习更好的表示？

### [59:42](https://www.youtube.com/watch?v=Xm2crsD5ngA&t=3582s) · b000070

**English**

Challenge three is reasoning. In reasoning, the goal is to combine knowledge, usually through multiple steps, and exploiting some knowledge about the problem to solve harder tasks than simply perception. So, when we used to think about reasoning, we used to think about multiple layers of neural networks, where each layer learns increasingly abstract and powerful representations that were not learned in previous layers. And that's still a valid way of doing reasoning, but of course, nowadays, we see reasoning being emerged from large language models, from tree structures, from tree search. We can now start doing reasoning in a much more principled and interpretable way. So, several sub-challenges in reasoning. How do you parameterize the individual concepts in the reasoning process? Whether reasoning should be done using language like chain of thought, where each step is just a different language thought or different language step, or should the reasoning be done in some

**中文**

挑战三是推理（reasoning）。推理的目标是组合知识，通常通过多个步骤，并利用关于问题的一些知识，解决比单纯感知更困难的任务。过去我们想到推理时，会想到多层神经网络，每一层都学习越来越抽象、越来越强大的表示，这些表示是前面各层没有学到的。这仍然是一种有效的推理方式，但如今，我们当然看到推理从大型语言模型、树结构和树搜索（tree search）中涌现。现在，我们可以开始以更有原则、更可解释的方式进行推理。因此，推理有几个子挑战。如何参数化（parameterize）推理过程中的各个概念？推理是否应该使用语言来进行，例如思维链（chain of thought），其中每一步都是一个不同的语言想法或语言步骤，还是应该在某种

### [1:00:39](https://www.youtube.com/watch?v=Xm2crsD5ngA&t=3639s) · b000071

**English**

other medium like using attention heat maps for image? What is the structure of a reasoning? Is it a chain of thought or a tree of thought or other symbolic structures? And finally, for reasoning to be possible, you often need some external knowledge about how humans reason or how humans think about the problem. So, what is the right way of injecting external knowledge from domain experts into the reasoning process? Challenge four is generation. Right, in generation, the goal is to learn a generative process that is able to generate new raw modalities, while at the same time maintaining some semblance of structure and coherence and alignment with other modalities. Several sub-challenges here. One sub-challenge is to summarize. If I have long videos or long documents, how do I summarize the most salient features? Another sub-challenge is to translate.

**中文**

其他媒介中推理，例如使用图像的注意力热图（attention heat maps）？推理的结构是什么？是 chain of thought、思维树（tree of thought），还是其他符号结构？最后，要使推理成为可能，往往需要一些关于人类如何推理或如何思考该问题的外部知识。那么，将领域专家的外部知识注入推理过程的合适方式是什么？挑战四是生成（generation），对吧？在生成中，目标是学习一个能够生成新的原始模态的生成过程，同时保持一定的结构、连贯性，以及与其他模态的对齐。这里有几个子挑战。一个子挑战是摘要（summarize）。如果我有很长的视频或文档，如何概括其中最显著的特征？另一个子挑战是转换（translate）。

### [1:01:37](https://www.youtube.com/watch?v=Xm2crsD5ngA&t=3697s) · b000072

**English**

This is where all your text-to-image or text-to-video models fall in. Given one modality, can you generate the same content in some other modality? And finally, creation. Can you start with less data and generate more data? Can you generate videos given only the first frame in the video? Or can I generate video, audio, and text synchronized in a manner given only some initial prompt?

**中文**

所有 text-to-image 或 text-to-video 模型都属于这一类。给定一种模态，能否以另一种模态生成相同的内容？最后是创造（creation）。你能否从较少的数据开始，生成更多的数据？能否只给定视频的第一帧就生成视频？或者，能否只给定某个初始提示，就以同步的方式生成视频、音频和文本？

### [1:02:08](https://www.youtube.com/watch?v=Xm2crsD5ngA&t=3728s) · b000073

**English**

Challenge five is transfer. Oftentimes, we have lots of multimodal data, but there's imbalance in which modality has more data or more labels. So, in transference, there's often some modality B which has a lot more data, and the goal is to help do prediction in modality A that you care about. For example, if I want to do modeling of health data, I'm often not going to have too much health data because of privacy concerns and because of um yeah, because of privacy concerns, but can I use larger resources, for example, large language models or medical textbooks or open-source medical data to help me make predictions in a limited data setting that I care about. So, we call this transference. Several sub-challenges here. One is the problem of transfer, especially transfer between different data modalities. Nowadays, you've seen that large language models as a large,

**中文**

挑战五是迁移（transfer）。我们通常有很多多模态数据，但不同模态的数据量或标签数量并不均衡。因此，在迁移（transference）中，通常有某种模态 B 拥有多得多的数据，目标是帮助在你关心的模态 A 中进行预测。例如，如果我想对健康数据建模，通常不会有太多健康数据，因为隐私方面的顾虑，而且因为，嗯，是的，因为隐私方面的顾虑。但是，我能否利用更大的资源，例如大型语言模型、医学教材或开源医疗数据，帮助我在关心的有限数据场景中进行预测？我们将其称为 transference。这里有几个子挑战。一个是 transfer 问题，尤其是不同数据模态之间的迁移。如今，你已经看到，大型语言模型作为一种大型的、

### [1:03:04](https://www.youtube.com/watch?v=Xm2crsD5ngA&t=3784s) · b000074

**English**

resource-rich knowledge data can help not just in language tasks, but also help in many other tasks like robotics or sensing or medical. How do you enable this sort of transfer, especially across modalities. How do you do co-learning? Co-learning refers to this phenomena where you're adding some additional modality either as the input or as a prediction target during training, but is then subsequently removed during testing because during testing you don't have access to this secondary modality. And finally, model induction. How do you do all this using only access to black box APIs and exchanging information either at the prompt or at the output level without modifying the model internals.

**中文**

资源丰富的知识数据，不仅能帮助语言任务，也能帮助机器人、感知或医疗等许多其他任务。如何实现这种迁移，尤其是跨模态迁移？如何进行协同学习（co-learning）？Co-learning 指的是这样一种现象：在训练时，将某种额外模态作为输入或预测目标加入，但之后在测试时移除，因为测试时你无法获取这种第二模态。最后是模型归纳（model induction）。如何仅通过访问黑盒 API（black box APIs），并在提示或输出层面交换信息，而不修改模型内部结构，来完成所有这些事情？

### [1:03:51](https://www.youtube.com/watch?v=Xm2crsD5ngA&t=3831s) · b000075

**English**

And finally, challenge six is quantification. Whereas challenges one to five were all about building better models, challenge six on quantification aims to better understand the models that we develop. Right, our goal is to provide a better empirical and theoretical study to understand various modalities and how they're heterogeneous, how they interact, and how the whole multimodal learning process goes. So, several sub-challenges. Better understanding heterogeneity, better understanding interactions between different modalities, and better improving the learning process of multimodal data so that you are learning at a stable and appropriate rate.

**中文**

最后，挑战六是量化（quantification）。挑战一到五都是为了构建更好的模型，而量化这个第六个挑战，旨在更好地理解我们开发的模型，对吧？我们的目标是提供更好的实证与理论研究，理解各种模态，它们如何具有异质性、如何交互，以及整个多模态学习过程如何进行。因此，有几个子挑战。更好地理解异质性，更好地理解不同模态之间的交互，以及更好地改进多模态数据的学习过程，使学习能够以稳定且合适的速度进行。

### [1:04:34](https://www.youtube.com/watch?v=Xm2crsD5ngA&t=3874s) · b000076

**English**

So, to summarize, six core multimodal challenges. Firstly, how do you represent your data? Right, if I have very complicated data, let me just look at the most simple case. You have one element in language, one element in images. How do I decide whether to learn a fused representation where you're combining information into one representation, whether you're going to coordinate, so learning two separate representations that are coordinated through some similarity function, or doing fusion, learning more representations than you started with to exploit the fact that different representations capture different information. So, that's the challenge of representation. While representation just looked at one element from each modality, alignment starts to model multiple elements across your two modalities. So, several sub-challenges here. Can you link the fact that this is a visual representation to the fact that this is

**中文**

因此，总结一下，六个核心多模态挑战。首先，如何表示你的数据？对吧，如果我有非常复杂的数据，先看最简单的情况。语言中有一个元素，图像中有一个元素。如何决定是学习融合表示（fused representation），将信息组合成一个表示；还是进行协调，学习两个通过某种相似度函数协调的独立表示；或者进行 fusion \[字幕疑误，结合前文可能指 fission\]，学习比起始数量更多的表示，以利用不同表示捕捉不同信息这一事实。这就是表示的挑战。表示只看每种模态中的一个元素，而对齐开始对两种模态中的多个元素建模。因此，这里有几个子挑战。你能否把这是一个视觉表示这一事实，与这是一个

### [1:05:31](https://www.youtube.com/watch?v=Xm2crsD5ngA&t=3931s) · b000077

**English**

a language token that references this visual representation? Finding out the links between elements in different modalities. This is, of course, simplest when your elements are discrete in nature. Uh but, it becomes much more challenging when your modalities and elements are continuous. So, in almost any problem, you have to deal with the problems or the challenges of representation and alignment. After that, reasoning is the challenge of combining data, often through multiple inferential steps, over multiple steps to solve harder problems. And reasoning can be done using multiple layers of neural networks, but nowadays with language models and neurosymbolic methods, we have an opportunity to do reasoning over complex problems while retaining some amount of interpretability to human domain experts. Uh several sub-challenges include designing the structure of reasoning, whether it's a chain or a tree,

**中文**

指向该视觉表示的语言 token 这一事实联系起来？找出不同模态中元素之间的联系。当然，当元素本身是离散的时，这是最简单的。呃，但当模态和元素是连续的时，挑战就大得多。因此，几乎在任何问题中，你都必须处理表示与对齐的问题或挑战。之后，推理是组合数据的挑战，通常要通过多个推断步骤，经过多个步骤来解决更难的问题。推理可以通过多层神经网络进行，但如今，借助语言模型和神经符号方法（neurosymbolic methods），我们有机会对复杂问题进行推理，同时为人类领域专家保留一定的可解释性。呃，几个子挑战包括设计推理结构，是链还是树，

### [1:06:28](https://www.youtube.com/watch?v=Xm2crsD5ngA&t=3988s) · b000078

**English**

designing the intermediate features for reasoning, and finding out the best way to integrate human domain knowledge into reasoning. That can be used to make a prediction on a label if you care about, you know, predictive tasks. But, sometimes we also care about generative tasks. How do you take in lots of data and summarize it into salient features? How do you translate from one modality to the other? For example, given a caption, generate the right image or video, preserving the same information. And finally, how can you create more information? Start with this image or latent representation and generate entire video and audio and dialogue. That's a problem of creation. Transference refers to the problem where you might care about predicting in some modality, but there's often very limited data, noisy data, or limited labels because of privacy or concerns where

**中文**

设计推理的中间特征，以及找出将人类领域知识融入推理的最佳方式。如果你关心预测任务，就可以用它来预测标签。但有时，我们也关心生成任务。如何接收大量数据，并将其概括为显著特征？如何从一种模态转换到另一种模态？例如，给定一段描述，生成正确的图像或视频，同时保留相同的信息。最后，如何创造更多信息？从这张图像或潜在表示（latent representation）出发，生成完整的视频、音频和对话。这是创造的问题。Transference 指的是这样一种问题：你可能关心在某种模态中进行预测，但由于隐私或其他顾虑，通常只有非常有限的数据、有噪声的数据，或有限的标签，导致

### [1:07:24](https://www.youtube.com/watch?v=Xm2crsD5ngA&t=4044s) · b000079

**English**

it's hard to get data. How do you use another resource-rich modality to help and transfer information to the modality that you care about? And finally, whereas these first five challenges all care about building better methods, the sixth sub-challenge of quantification is the magnifying glass. It's all about understanding in a deeper way why these methods work, when they don't work, and trying to improve the learning process to be more principled.

**中文**

数据难以获取。如何利用另一种资源丰富的模态来提供帮助，并将信息迁移到你关心的模态？最后，前五个挑战都关注构建更好的方法，而量化这个第六个子挑战就像放大镜。它关注的是更深入地理解这些方法为什么有效、何时无效，并尝试改进学习过程，使其更有原则依据。

### [1:07:56](https://www.youtube.com/watch?v=Xm2crsD5ngA&t=4076s) · b000080

**English**

To summarize, at a very high level, what is multimodal? Multimodal is the scientific study of heterogeneous, connected, and interacting data. Data modalities are often heterogeneous, which makes it very challenging to model together. At the same time, instead of giving up on modeling them together, there are often benefits, tangible benefits because these modalities are connected and share information, and they often interact in very rich ways to create new information that is important for downstream tasks. These are the three key principles that define multimodal problems. At the same time, it is very challenging to model them because of these these key principles, right? They are hard to represent. They have often show challenges in aligning one data modality with the other. You have to deal with how to reason over multimodal data. It's hard to generate. You have to transfer from high resource to low resource. And of course, it's difficult to quantify

**中文**

总结一下，从非常宏观的层面看，什么是多模态？多模态是对异质、相互联系且相互交互的数据的科学研究。数据模态通常具有异质性，这使得将它们共同建模极具挑战。同时，尽管如此，我们没有放弃共同建模，因为这样做往往有好处，有切实的好处：这些模态彼此联系并共享信息，而且通常以非常丰富的方式交互，产生对下游任务很重要的新信息。这就是定义多模态问题的三个关键原理。与此同时，正因为这些关键原理，对它们建模非常具有挑战，对吧？它们难以表示。将一种数据模态与另一种对齐也常常面临挑战。你必须处理如何对多模态数据进行推理。生成也很难。你必须从高资源迁移到低资源。当然，对学习过程进行量化

### [1:08:51](https://www.youtube.com/watch?v=Xm2crsD5ngA&t=4131s) · b000081

**English**

and have a deep understanding of the learning process. So, this is why it's multimodal is difficult. And personally, where I feel multimodal is next, and which will also be focuses of this course, will be how to design and train these multimodal large language models which have the open-ended QA capability of LLMs, but at same time are grounded in different data modalities beyond language. So, they're actually useful for real-world tasks. How do you improve generative AI systems so that they can generate many modalities in synchronization and while remaining efficient? How do you build these systems for various aspects of physical sensing? How do you apply them in health? And how do you build agents that are increasingly grounded in multimodal digital and embodied environments? So, this course will cover all of these from the principles to the core challenges, the latest methods, and new methods in these

**中文**

并深入理解也很困难。这就是为什么多模态很难。就我个人而言，我认为多模态的下一步，也将是这门课的重点，是如何设计并训练这些多模态大型语言模型：它们具有 LLMs 的开放式 QA 能力，同时又与语言之外的不同数据模态建立 grounding。因此，它们对现实世界任务真正有用。如何改进生成式 AI 系统，使其能够同步生成多种模态，同时保持高效？如何为物理感知的各个方面构建这些系统？如何将它们应用于健康领域？以及如何构建越来越深地扎根于多模态数字环境和具身环境（embodied environments）的智能体？这门课会涵盖所有这些内容，从原理到核心挑战、最新方法，以及针对这些

### [1:09:47](https://www.youtube.com/watch?v=Xm2crsD5ngA&t=4187s) · b000082

**English**

challenges, and touching upon what is next both in terms of the foundational aspects and real-world application domains. All right. So, that's the end of the content today. This Thursday, we're going to meet back here for a lecture on multimodal data sets and tasks. We're going to cover several important tasks in the multimodal space. We're going to dive deep into several data sets. And the purpose of this lecture is to help you decide on the data sets and tasks that you want to focus on in your course projects. Uh that is the most pressing deadline. We're hoping to have people decide if they want to stay in the course and hopefully, you know, form teams of two to three students for course projects uh because we want to nail that in uh by ideally week two or week three so that you can start getting uh get getting get go start working on these project proposals and literature

**中文**

挑战的新方法，并涉及基础层面和现实应用领域的下一步方向。好了，今天的内容就到这里。本周四，我们会回到这里，讲多模态数据集与任务。我们会介绍多模态领域的几个重要任务，深入研究几个数据集。这节课的目的是帮助你们决定课程项目中想重点关注的数据集和任务。呃，这是最迫近的截止事项。我们希望大家决定是否继续选修这门课，并希望能够为课程项目组成两到三人的小组，因为我们希望最好能在第二周或第三周确定下来，让你们能够开始，开始，开始着手这些项目提案和文献

### [1:10:44](https://www.youtube.com/watch?v=Xm2crsD5ngA&t=4244s) · b000083

**English**

reviews. We're going to uh release a more formal project preference form this week. Uh so, try to start thinking about what domains you're interested in and whether you already know people in the course that you might be interested in teaming up with for your projects. All All right, we're going to end a little bit early today. Try to mingle with classmates if you don't know anybody so that you can form teams and start thinking about what projects you want to work on. Thanks, everyone.

**中文**

综述。我们会在本周发布一份更正式的项目偏好表。因此，请开始思考自己对哪些领域感兴趣，以及是否已经认识课程中可以一起组队做项目的人。好，好，今天我们会稍微提前结束。如果你还不认识其他同学，试着和大家交流一下，这样就能组队，并开始思考想做什么项目。谢谢大家。
