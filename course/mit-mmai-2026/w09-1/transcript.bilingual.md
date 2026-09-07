# Lecture 9 – Multimodal Reasoning (MIT How to AI Almost Anything/Multimodal AI, Spring 2026)

_Bilingual transcript · 双语讲稿_

- Channel: Paul Liang
- Source: [YouTube](https://www.youtube.com/watch?v=Vhe_bX8mV2s)
- Duration: 1:17:35
- Caption source: automatic
- Status: complete
- Chinese translation: 94/94
- Translation provider: codex
- Generated: 2026-09-07T07:49:34+00:00

## Transcript · 讲稿

### [00:00](https://www.youtube.com/watch?v=Vhe_bX8mV2s&t=0s) · b000001

**English**

All right, folks. Welcome back. Hope you had a great spring break. So, uh, one more assignment was released. It is the project midterm report. Uh, the requirements for the project midterm reports are that you should have finalized your idea. You should have uh finalized your data sets and baseline models and ideally already started you know processing your data sets and running baselines. Baselines meaning methods that are prior state-of-the-art methods that's already exist that are precursor to the methods that you are proposing they're hoping to improve upon. You should be running those on your data sets uh before the midterm. You should be colleating those results, numerical results, and also analyzing what works and what doesn't. So doing some error analysis and use that as a way to inform

**中文**

好了，各位，欢迎回来。希望你们春假过得愉快。那么，呃，又发布了一项作业，就是项目期中报告。呃，项目期中报告的要求是，你们应该已经确定了自己的想法。你们应该已经，呃，确定了数据集（data sets）和基线模型（baseline models），而且最好已经开始，你知道，处理数据集、运行基线。基线指的是已经存在的、此前最先进的（state-of-the-art）方法，它们是你们正在提出、希望加以改进的方法的前身。你们应该在期中之前，在自己的数据集上运行这些方法。你们应该汇集这些结果、数值结果，还要分析哪些有效、哪些无效。所以，要做一些错误分析（error analysis），并以此来指导

### [00:57](https://www.youtube.com/watch?v=Vhe_bX8mV2s&t=57s) · b000002

**English**

what you're going to do next for your project. Okay, so those are the main requirements for for the midterm report. Um to also clarify what I mean by baselines, I'm sure a lot of you are working on some new data set, some new task, right? A baseline doesn't mean a prior model that was developed for that data set. You can find any data set that no one has trained LLM on LLM training on that data set will not be a new contribution. That would be a baseline. So even if the model itself had never been applied through that data set, it is your job to find what is the most suitable model and apply it to that data set and see how it works and outline it errors and then for the final project to propose something new on top of that existing baseline. Okay. So just because u a method has not been applied to that data set, it doesn't mean it's not a baseline doesn't mean that's new contribution. that has

**中文**

你们的项目接下来要做什么。好，这些就是期中报告的主要要求。嗯，再澄清一下我说的基线是什么意思。我相信你们很多人都在研究某个新数据集、某个新任务，对吧？基线并不意味着此前专门为那个数据集开发的模型。你可以找到任何一个没有人训练过大语言模型（Large Language Model, LLM）的数据集，但在那个数据集上训练 LLM，并不是一项新的贡献。那会是一个基线。所以，即使模型本身从未应用到那个数据集，你的任务也是找出最适合的模型，把它应用到那个数据集上，看看效果如何，概述它的错误，然后在最终项目中，在现有基线之上提出新的东西。好。所以，仅仅因为某种方法没有应用到那个数据集上，并不意味着它不是基线，也不意味着那就是新的贡献。那是

### [01:54](https://www.youtube.com/watch?v=Vhe_bX8mV2s&t=114s) · b000003

**English**

to be something that you kind of get working um for this midterm report. Uh specific logistics and the detailed write up for the assignment has been posted on canvas. I think it was a six-page report. So four pages for the proposal. Now it's six pages. So it's two extra pages for you to detail your results from running these approaches. what early results you're getting and any error analysis and why these existing methods are are not working well. Sounds good. Any questions about the midterm report?

**中文**

你们在这次期中报告中需要基本跑通的东西。呃，具体安排和作业的详细书面说明已经发布在 canvas 上了。我记得是六页的报告。提案是四页，现在是六页。所以多了两页，让你们详细说明运行这些方法得到的结果：你们得到了哪些初步结果，有哪些错误分析，以及为什么这些现有方法效果不好。这样可以吗？关于期中报告，有什么问题吗？

### [02:32](https://www.youtube.com/watch?v=Vhe_bX8mV2s&t=152s) · b000004

**English**

&gt;&gt; There's still like each group submit one. Yes, each group submits one on Canvas and I think there's an option to tag your tag your teammates or you can just submit it by yourself and you can share with your teammates the the score and the the feedback. Uh speaking of which, we just released the scores and the feedback for the proposal. Everyone did really well. Everyone got most most people got above 90 or 91. Uh so if you don't see a score on your canvas and if you weren't the one who submitted just ask uh your teammate who submitted for the score and for the feedback.

**中文**

&gt;&gt; 还是每个小组提交一份，对吧？是的，每个小组在 Canvas 上提交一份，我想那里有一个选项，可以标记你们的、标记你们的组员；或者你也可以自己提交，再把分数和反馈分享给组员。呃，说到这个，我们刚刚发布了提案的分数和反馈。大家都做得很好。每个人都拿到了，大多数、大多数人都在 90 或 91 分以上。呃，所以如果你在自己的 canvas 上看不到分数，而且你不是提交的人，就去问提交的那位组员，要一下分数和反馈。

### [03:10](https://www.youtube.com/watch?v=Vhe_bX8mV2s&t=190s) · b000005

**English**

Great. Uh continue meeting with myself and TAs who are in charge of your projects. We're still going to be holding office hours every Tuesday and Thursday to um hear about your progress. Yes.&gt;&gt; Oh yeah. Just another small question about the the term report like if we had some like small like small different ideas from our proposal is that going to be okay like if we like search for more data then we found that like a better data set instead of the original one that we proposed for like the pipeline their core architecture like we kind of modified it.&gt;&gt; Yeah.&gt;&gt; Absolutely.&gt;&gt; Okay. Yeah. Thank you.&gt;&gt; Yeah. If there's any um new ideas, new data sets, new baselines, new topics, it's all okay. I mean, team members might also be slightly different. I don't know who's recently added or dropped the class. So, team members might also change. So, that's all good.&gt;&gt; Thank you so much.&gt;&gt; All right. Um but yeah, I looked through everyone's

**中文**

很好。呃，请继续和我以及负责你们项目的助教（Teaching Assistants, TAs）见面。我们仍然会在每周二和周四安排答疑时间，了解你们的进展。请说。&gt;&gt; 哦，对。还有一个关于学期报告的小问题：如果我们有一些和提案稍微、稍微不同的想法，这可以吗？比如我们又找了一些数据，发现了比原先提议的更好的数据集，或者流程（pipeline）的核心架构，我们做了一些修改。&gt;&gt; 可以。&gt;&gt; 完全可以。&gt;&gt; 好的，谢谢。&gt;&gt; 对。如果有任何新想法、新数据集、新基线、新主题，都没问题。我是说，组员也可能稍微有些变化。我不知道最近有谁加选或退选了这门课，所以组员也可能会变。这些都没问题。&gt;&gt; 非常感谢。&gt;&gt; 好的。嗯，不过，我看过了大家的

### [04:07](https://www.youtube.com/watch?v=Vhe_bX8mV2s&t=247s) · b000006

**English**

project proposals. Yeah, all the ideas were great. All very fascinating. uh the only issue as I mentioned was you know most of you are working on some new data set some new tasks and direct application of you know method A to your task B uh that should be the expectation for the midterm report right applying LLM or applying a genic AI or applying multimodal fusion these are baseline they already exist so that should be part of the midterm report um you know apply them see how they work most likely they won't work super well first time off the shelf and that gives you a bottomup way of uh analyzing its errors and identifying what next to do to improve that. We'll come up with something new. Great. Let me also recap the schedule we've seen for the first half. The first half of the class was mostly the foundations. We really covered the basics of multimodal AI, specifically fusion,

**中文**

项目提案。对，所有想法都很好，都很有意思。呃，正如我提到的，唯一的问题是，你们大多数人在研究新数据集、新任务，而把方法 A 直接应用到你的任务 B 上，呃，这应该是期中报告中预期要完成的内容，对吧？应用 LLM，或者应用 a genic AI \[字幕疑误，可能指 agentic AI\]，或者应用多模态融合（multimodal fusion），这些都是基线，它们已经存在了，所以应该是期中报告的一部分。嗯，你知道，把它们应用起来，看看效果如何。很可能第一次直接用现成的方法，效果不会特别好，这就给了你一种自下而上（bottom-up）的方法，来分析它的错误，确定下一步做什么来改进它。我们会提出一些新东西。很好。我也回顾一下前半学期的安排。课程前半部分主要是基础。我们确实讲了多模态 AI 的基础，具体来说包括融合（fusion）、

### [05:02](https://www.youtube.com/watch?v=Vhe_bX8mV2s&t=302s) · b000007

**English**

alignment, representation learning, transformers, generative models. I I really view these as all uh the basic foundations. So, congrats on getting through all of that. Uh, commentator in the midterm, which again, we're not going to release the grades yet because people are doing a makeup midterm this week. Needless to say, don't discuss the midterm with those who haven't done it yet. But from what I've seen, you know, everyone did really well. So, average scores are already high. Um, no thanks to the 10 bonus points, but average score really good. So, congrats. So, that was the first half of the semester, more on these foundations. As a precursor to this second half of the semester, it will mostly be about advanced topics and applications. So starting today and next week, we're going to cover reasoning. So reasoning goes beyond single step prediction or just outputs to methods that can rethink across multiple steps, synthesize information, and build up more complex

**中文**

对齐（alignment）、表征学习（representation learning）、transformers、生成模型（generative models）。我、我确实把这些都看作基本基础。所以，祝贺大家学完了这些内容。呃，期中考试的 commentator \[字幕疑误，可能指 culminating\]，再次说明，我们还不会公布成绩，因为这周还有人在参加期中补考。不用说，不要和还没考的人讨论期中考试。不过就我看到的情况而言，大家都做得很好。所以平均分已经很高了。嗯，这可不归功于那 10 分加分，不过平均分确实很好。所以，恭喜大家。这就是前半学期，更多是在讲这些基础。作为后半学期的铺垫，后半学期主要会讲进阶主题和应用。所以从今天和下周开始，我们会讲推理（reasoning）。推理超越了单步预测或仅仅给出输出，转向能够跨多个步骤重新思考、综合信息，并构建更复杂的

### [05:59](https://www.youtube.com/watch?v=Vhe_bX8mV2s&t=359s) · b000008

**English**

logical arguments. and and you've seen the great applications of reasoning nowadays for things like math and coding and solving long complicated tasks that is the new frontier of AI. So the next two weeks will be about reasoning. I'll cover some work in RL and the basics of you know using RL to train train the sequence models like language models and this multimodal extensions and then Dimmitri will be covering some work in explainable reasoning and prescriptive reasoning. So prescriptive reasoning not just outputting something but you know outputting actions then actionable goal for people to use alongside confidence intervals and uncertainty predictions so people really know when to trust the model and when not to trust the model. So those next two topics will really be about explanability and trust in reasoning and using that to make real world life decisions. And then after reasoning, I'll cover uh interactive agents. Right? Another huge application

**中文**

逻辑论证的方法。你们也看到了如今推理在数学、编程，以及解决漫长复杂任务方面的出色应用，这就是 AI 的新前沿。所以，接下来两周会讲推理。我会介绍一些强化学习（reinforcement learning, RL）方面的工作，以及用 RL 训练语言模型这类序列模型（sequence models）及其多模态扩展的基础知识。然后 Dimmitri 会讲一些可解释推理（explainable reasoning）和处方性推理（prescriptive reasoning）方面的工作。处方性推理不只是输出某种东西，而是输出行动，然后是可供人们使用的可执行目标，同时给出置信区间（confidence intervals）和不确定性预测（uncertainty predictions），让人们真正知道什么时候该信任模型，什么时候不该信任模型。所以，接下来这两个主题主要会围绕推理的可解释性（explainability）和信任，以及如何利用它来做现实生活中的决策。推理之后，我会讲交互式智能体（interactive agents）。对吧？推理的另一个巨大应用

### [06:55](https://www.youtube.com/watch?v=Vhe_bX8mV2s&t=415s) · b000009

**English**

of reasoning is to be able to use these models to output multiple sequences of sets uh not just on your computer but can actually be executed, right? Executed like taking actions on the web or taking real robot actions in the real world or to control some physical system like in manufacturing or even in your nuclear nuclear plants. Uh so that will bring the discussion to interaction and agents right a lot of which are are built on top of multimodal systems. We'll cover some of that in week 11 and 12. And then we have an exciting two weeks of these um applicationoriented lectures where where Sunuk will be discussing uh applications of these interactive agents in manufacturing. Right? That's a domain where lots of multimodal data lots of closed loop systems where it makes sense to use agents to automate and improve the optimization or improve the throughput or to reduce uh reduce dangers for example. So in manufacturing and design

**中文**

是能够用这些模型输出多个 sets 的序列 \[字幕疑误，可能指 steps\]，呃，不只是停留在电脑上，而是能够真正执行，对吧？执行，比如在网上采取行动，或者在现实世界里执行真正的机器人动作，或者控制某种物理系统，比如制造业中的系统，甚至是核电厂中的系统。呃，所以这会把讨论带到交互（interaction）和智能体（agents），其中很多都是建立在多模态系统之上的。我们会在第 11 和第 12 周介绍其中一些内容。接着有两周很令人期待的、面向应用的课程，Sunuk 会讨论这些交互式智能体在制造业中的应用。对吧？这个领域有大量多模态数据、大量闭环系统（closed-loop systems），使用智能体来实现自动化、改善优化效果、提高吞吐量（throughput），或者比如说减少危险，是很合理的。所以，在制造和设计领域

### [07:53](https://www.youtube.com/watch?v=Vhe_bX8mV2s&t=473s) · b000010

**English**

and Tininoa will discuss some of these applications in more open-ended settings in cities and transportation again an area where there's all sorts of multimodal data from vision to graphs to sensor data to tabular data uh and also all sorts of applications and how do you analyze \[clears throat\] analyze data from a city how do you you know optimize certain throughput measures for a city and so on and finally week 14 I'll come back and discuss some more advanced topics, advanced topics like cross modal transfer, right? Why is it that nowadays you can train a language model and it can directly work well for robotics without ever having seen a robot? How can you take a language model and use it to release smell, analyze smell data and really smell? That's some of the stuff that we're doing. So all this falls into this exciting area called cross model transfer where you can train on one modality and somehow the model magically is able to transfer to some other

**中文**

以及 Tininoa 会讨论其中一些在城市和交通等更开放场景中的应用。这同样是一个拥有各种多模态数据的领域，从视觉、图（graphs）、传感器数据到表格数据（tabular data），呃，也有各种各样的应用。你如何分析 \[清嗓子\] 分析一个城市的数据，如何优化城市的某些吞吐量指标，等等。最后，第 14 周我会回来讨论一些更进阶的主题，比如跨模态迁移（cross modal transfer），对吧？为什么现在你可以训练一个语言模型，而它即使从未见过机器人，也能直接很好地用于机器人领域？如何拿一个语言模型，让它释放气味、分析气味数据，并真正闻到气味？这是我们正在做的一些工作。所以，这些都属于一个令人兴奋的领域，叫作 cross model transfer \[字幕疑误，可能指 cross modal transfer\]，你可以在一种模态上训练，然后模型不知怎么就神奇地能够迁移到另一种

### [08:49](https://www.youtube.com/watch?v=Vhe_bX8mV2s&t=529s) · b000011

**English**

modality even without training on it. And finally, uh, self-evolving agents. I talked a little bit about this, I think, right before spring break, and a lot of people showed excitement, right? The next frontier of these, uh, reasoning models and agentic models are those that go beyond how humans supervise and how humans design rewards agents that can supervise themselves, propose new tasks for themselves, design reward functions for themselves, and recursively improve over time. And finally, week 15, 12th of May would be your project presentations. Uh, so by then you should have finished your projects. We're going to do a little bit of a poster session in the third floor atrium. uh every team will prepare a poster and it'll be open to obviously everybody else in the class but also general uh members of the MIT community who are interested to see what amazing work all

**中文**

模态，即使从未在那种模态上训练过。最后，呃，自我演化智能体（self-evolving agents）。我想就在春假之前，我稍微讲过一点，很多人都表现得很兴奋，对吧？这些推理模型和智能体模型（agentic models）的下一个前沿，是超越人类如何监督、如何设计奖励的模型：能够自我监督、为自己提出新任务、为自己设计奖励函数（reward functions），并随着时间递归改进的智能体。最后，第 15 周，5 月 12 日，是你们的项目展示。呃，到那时你们应该已经完成了项目。我们会在三楼中庭办一个小型海报展示。每个小组准备一张海报，显然它会向班上其他所有人开放，也会向 MIT 社区里有兴趣了解你们大家正在做的出色工作的人

### [09:46](https://www.youtube.com/watch?v=Vhe_bX8mV2s&t=586s) · b000012

**English**

of you are doing. So that will be 12th of May also last day of class and then the midterm reports will be due about a week after that. I have to check when is the last date for assignments. Okay. Uh so no more final just the project midterm report. due I think next week and then the final presentation and report due last week of class and two homeworks homework four and five um these will be one will be a really short homework and one will be a standard homework just to make sure you all have time for the final projects uh we haven't decided which is which one of the homeworks will be about reinforcement learning and reasoning the other homework will be about interactive agents One of them will be much shorter \[clears throat\] than usual maybe one week and the other one will be a standard homework of about two weeks.

**中文**

开放。所以，时间是 5 月 12 日，也是最后一天上课，然后期中报告将在那之后大约一周截止。我得查一下作业最晚可以安排在哪一天。好。呃，所以没有期末考试了，只有项目期中报告，我想是下周截止，然后是最后一周上课时截止的最终展示和报告，以及两次作业，作业四和作业五。嗯，其中一次会很短，另一次会是标准长度的作业，只是为了确保大家有时间做最终项目。呃，我们还没决定哪次是哪种。其中一次会是关于强化学习和推理，另一次会是关于交互式智能体。其中一次会比平常短很多 \[清嗓子\]，可能是一周，另一次则是标准的、大约两周的作业。

### [10:42](https://www.youtube.com/watch?v=Vhe_bX8mV2s&t=642s) · b000013

**English**

Great. Any questions about the schedule and topics for the second half of the semester? Some of these are of course inspired by the topics that um people have filled in in the midterm on topics they wanted to see. uh most likely week 14 you'll be you know not a full lecture on one topic but you'll break down like 20 minutes 20 minutes for for different subtopics that are that are of interest to people. Okay. Okay. Jumping into today's lecture. So today's lecture will be about reasoning and reinforcement learning as a way of incentivizing and enabling reasoning in these frontier models. So I'll cover first of all obviously what is reasoning and how reasoning differentiates is different from singlestep prediction and supervised learning and then I'll cover some basics of reinforcement learning culminating in everyone at least having a high level idea of how these modern PO

**中文**

很好。关于后半学期的安排和主题，有什么问题吗？其中一些当然受到了大家在期中考试中填写的、希望看到的主题的启发。呃，第 14 周很可能不会用整堂课讲一个主题，而是分成比如 20 分钟、20 分钟，讲大家感兴趣的不同子主题。好。好，进入今天的课程。今天会讲推理，以及把强化学习作为激励和实现这些前沿模型推理能力的方法。我首先当然会讲什么是推理，以及推理如何区别、如何不同于单步预测和监督学习（supervised learning）；然后介绍强化学习的一些基础，最终让大家至少在高层次上了解这些现代的 PO

### [11:38](https://www.youtube.com/watch?v=Vhe_bX8mV2s&t=698s) · b000014

**English**

and GRPO methods work for incentivizing LLMs to reason and then we'll extend it to how we can do uh reasoning over different modalities and I'll give some very specific case study from some of our research on building multimodal models that can reason over over multimodal medical data. So first of all uh intuitive definition for reasoning it is to combine knowledge usually through multiple inferential steps that exploits in some way the structure of your problem right so several key words over here uh first of all the idea of combin combining knowledge right across multiple steps right you do a do a math problem for example it's often many different lemas each lema to be combined sequentially or in parallel until you can actually get more informative statements and you finally get to your food, right? If you're doing some of these long or any task that you do, for example, cooking something, you got to follow a sequence

**中文**

和 GRPO 方法如何激励 LLMs 进行推理。然后我们会扩展到如何在不同模态上进行推理，我会从我们构建能够对多模态医疗数据进行推理的多模态模型的研究中，给出一个非常具体的案例。首先，呃，推理的直观定义是：通常通过多个推断步骤来组合知识，并以某种方式利用问题的结构，对吧？这里有几个关键词。首先是组、组合知识的想法，对吧？跨越多个步骤。比如做一道数学题，通常有许多不同的引理（lemmas），每个引理都要按顺序或并行组合，直到你真正得到信息更丰富的陈述，最后得到你的 food \[字幕疑误，可能指 proof\]，对吧？如果你在做某些很长的任务，或者任何任务，比如做饭，你都必须按顺序遵循一系列

### [12:33](https://www.youtube.com/watch?v=Vhe_bX8mV2s&t=753s) · b000015

**English**

of steps in line in order until you finally complete that task. So, reasoning usually involves a series of actions, a series of steps, each perhaps getting more and more complicated and accumulating information from from previous steps. And of course most of the times when you think about reasoning there is some uh structure of the problem that we are exploiting right whether it's a symbolic structure in mathematics whether it is um some other structure in real world robotics tasks there often some sequential or treebased or graphical structure of the problem that we are leveraging. So visually and also how this ties in with the first half of the semester. So we've seen how to represent different modalities, different elements across your modalities. You can fuse them, you can coordinate them using a line representations and so on. Uh we saw how

**中文**

步骤，直到最终完成任务。所以，推理通常涉及一系列行动、一系列步骤，每一步可能越来越复杂，并不断积累前面步骤的信息。当然，大多数时候，当你想到推理时，我们都在利用问题的某种结构，对吧？无论是数学中的符号结构（symbolic structure），还是现实世界机器人任务中的其他结构，问题通常都有某种顺序结构、树结构或图结构，是我们正在利用的。所以，从视觉上看，以及它如何与前半学期联系起来。我们已经看过如何表示不同模态、各个模态中的不同元素。你可以融合它们，可以用 a line representations \[字幕疑误，可能指 aligned representations，对齐表征\] 来协调它们，等等。呃，我们看过如何

### [13:29](https://www.youtube.com/watch?v=Vhe_bX8mV2s&t=809s) · b000016

**English**

to extend it from one element to a sequence. So we saw all these sort of a line representations. So it could be multiple word that you're typing in context, multiple images that you have as input. And so you have all these local sources of information coming in through time. And reasoning is really all about you know having multiple inferential steps on different aspects of the problem and then combining it systematically in some way to lead to higher order inferences to solve these more difficult tasks.

**中文**

从一个元素扩展到一个序列。所以我们看过所有这些 a line representations \[字幕疑误，可能指 aligned representations\]。它可能是你在上下文中输入的多个词，也可能是作为输入的多张图像。于是，你会有这些随时间传入的局部信息来源。而推理实际上就是对问题的不同方面进行多个推断步骤，然后以某种方式系统地把它们组合起来，得到更高阶的推断，以解决这些更困难的任务。

### [14:02](https://www.youtube.com/watch?v=Vhe_bX8mV2s&t=842s) · b000017

**English**

So we think about uh reasoning we often also think about this challenge of compositionality. Compositionality is very similarly defined, right? It's really about how to represent individual elements and how do you combine these elements so that you can lead to more semantically meaningful information in a combination. So uh I think I've shown you some of these examples where you can create these compositional uh compositional data sets where one way of combining data so uh plants surrounding a light bulb is very natural, right? You see this all the time when you look at photos. So in uh these visual language models can recognize this and generate this image very easily. But then you take the same objects and you just combine them in a different way. Right? So a light bulb surrounding some plants. So you have these, you know, these plants inside of a light bulb. This is something that is almost never seen in the real world.

**中文**

所以，当我们思考推理时，也经常想到组合性（compositionality）这一挑战。Compositionality 的定义也非常相似，对吧？它实际上关心的是如何表示单个元素，以及如何组合这些元素，让组合产生在语义上更有意义的信息。嗯，我想我给你们看过一些例子，可以创建这类组合性数据集。其中一种数据组合方式，比如植物围绕着一个灯泡，这很自然，对吧？你看照片时经常见到。所以，这些视觉语言模型（vision language models）很容易识别它，也很容易生成这张图像。但是，如果拿同样的物体，只是换一种方式组合，对吧？比如一个灯泡围绕着一些植物。于是，这些植物就在一个灯泡里面。这种东西在现实世界中几乎从未出现过。

### [14:58](https://www.youtube.com/watch?v=Vhe_bX8mV2s&t=898s) · b000018

**English**

Never seen in the real world. And therefore all these DLMs you know if they're trying to do question answering or trying to generate this image uh they fail really terribly. So clip vision language transformers all these multimodal bird models pre-train models they all get close to zero chance zero random chance when trying to to classify these images. So this is a reasoning problem right there's a reasoning problem. It is a problem of how do you get these models to really combine information in the right way where one way of combining it is is super common and is really seen in the world a lot and the other way of combining is super rare and not often seen.

**中文**

在现实世界中从未出现过。因此，这些 DLMs \[字幕疑误，可能指 VLMs\]，如果尝试回答问题或者生成这种图像，呃，都会失败得非常惨。所以，clip、vision language transformers、所有这些多模态 bird models \[字幕疑误，可能指 BERT models\]、预训练模型（pre-trained models），在尝试分类这些图像时，都接近零概率、零随机概率。所以这是一个推理问题，对吧？这是一个推理问题。问题在于，你如何让这些模型真正以正确的方式组合信息，其中一种组合方式非常常见，在世界中经常能看到，而另一种组合方式非常罕见，不太能看到。

### [15:42](https://www.youtube.com/watch?v=Vhe_bX8mV2s&t=942s) · b000019

**English**

&gt;&gt; Uh people have obviously shown this for other examples. If you have a uh astronaut riding a horse, that's kind of rare, but still models can generate it. If you switch it to a horse riding an astronaut, then uh at least in 2022, 2023, these models will not be able to generate that image. So that's a challenge with the model's reasoning capabilities, right? It is not able to combine these two individual logical evidences \[clears throat\] in the right way. Whereas you know for us people this is almost trivial right and of course there's all sorts of examples right pre like 2023 2024 almost every other paper written on LLMs was uh the inability to read them they could not count how many Rs was in the word strawberry they sometimes would struggle with very simple uh mathematical equations like 2 plus 3 if you started

**中文**

&gt;&gt; 显然，人们也用其他例子展示过这一点。如果是一个宇航员骑着马，这有点少见，但模型仍然能生成。如果把它换成一匹马骑着一个宇航员，那么至少在 2022、2023 年，这些模型还无法生成这张图像。所以，这是模型推理能力面临的挑战，对吧？它不能以正确的方式组合这两条独立的逻辑证据 \[清嗓子\]。而对我们人来说，这几乎是轻而易举的，对吧？当然，还有各种各样的例子。比如在 2023、2024 年之前，几乎每隔一篇关于 LLMs 的论文都在讲它们无法 read them \[字幕疑误，可能指 reason\]；它们数不清 strawberry 这个词里有多少个 R；有时它们甚至会在非常简单的数学等式上遇到困难，比如 2 加 3，如果你开始

### [16:39](https://www.youtube.com/watch?v=Vhe_bX8mV2s&t=999s) · b000020

**English**

prompting it in Chinese instead of English all these really brutal cases of uh models not being able to reason. Uh but then of course came a came a turning point uh with several key works. Um of course unless you've been living under a rock, you probably know and heard of what train of thought prompting is. So that's an example of reasoning, right? You give the model maybe a question and in this case it's a mathematical question requires some reasonable amount of these logical inferences, right? They got to add two numbers together. They got to solve some equations. And they at least got to do a couple of steps of algebra to solve the problem. So if you just do standard prompting, the model gets it wrong. But if you just uh add for example, let's think step by step, then the model start getting it correct, right? With train of thought prompters, right? The model not

**中文**

用中文而不是英文给它提示，所有这些都是模型无法推理的非常严重的例子。呃，但随后当然出现了转折点，伴随着几项关键工作。嗯，当然，除非你一直与世隔绝，否则你大概知道，也听说过 train of thought prompting \[字幕疑误，可能指思维链提示（chain-of-thought prompting）\]。这就是推理的一个例子，对吧？你可能给模型一个问题，这里是一个数学问题，需要相当程度的逻辑推断，对吧？它需要把两个数相加，需要解一些方程，至少得做几步代数运算才能解决问题。所以，如果只用标准提示，模型会答错。但如果你只是加上，比如说，“让我们一步一步思考”，模型就开始答对了，对吧？通过 train of thought prompters \[字幕疑误，可能指 chain-of-thought prompting\]，对吧？模型不

### [17:33](https://www.youtube.com/watch?v=Vhe_bX8mV2s&t=1053s) · b000021

**English**

only gets it correct, but the model is actually able to explicitly verbalize each step of their thinking, each step of, you know, they have 23 apples, they use 20, so 23 - 20 goes to three, and they bought six more. 3 + 6 equals to 9. So the model is prompted to explicitly verbalize each step of his reasoning which essentially follows this chain sequential structure and that helps the model answer the question correctly.

**中文**

仅答对了，而且实际上能够明确地用语言表达每一步思考，每一步，比如，他们有 23 个苹果，用掉 20 个，所以 23 - 20 得到三，然后他们又买了六个。3 + 6 等于 9。所以，提示会让模型明确地用语言表达每一步推理，这本质上遵循一种链式顺序结构，而这帮助模型正确回答问题。

### [18:10](https://www.youtube.com/watch?v=Vhe_bX8mV2s&t=1090s) · b000022

**English**

People have extended train of thought to all sorts of acts of thought. So chain of thought. So consistency chain of thought, tree of thoughts, graph of thoughts and this is really where uh the structure as I mentioned the structure of the problem comes in right certain types of problems it lends itself very well to sequential reasoning. So in math for example we saw previously you know 23 apples minus 20 equals to three that's the first step and then the next step is to add six apples equals to 9. So it's a very linear chain, right? Some problems naturally are are tree based, right? How you reason and how you solve the problem is very tree based, which basically means at some current state, you explore over several states, you start recursing and maybe you reach a dead end, you backtrack, you do all sorts of breath or deferred search. Uh so you do this kind of search, right? So one example is maybe you're playing

**中文**

人们把 train of thought \[字幕疑误，可能指 chain of thought\] 扩展成了各种各样的 acts of thought。所以，思维链（chain of thought）。一致性思维链（consistency chain of thought）、思维树（tree of thoughts）、思维图（graph of thoughts）。而这正是我提到的问题结构发挥作用的地方，对吧？某些类型的问题非常适合顺序推理。比如数学中，我们之前看到，23 个苹果减去 20 等于三，这是第一步；下一步再加六个苹果，等于 9。所以，这是一个非常线性的链，对吧？有些问题天然是树形的，对吧？你如何推理、如何解决问题，本身就非常具有树形结构，这基本上意味着，在某个当前状态，你探索几个状态，开始递归，也许走到死路，于是回溯，做各种 breath or deferred search \[字幕疑误，可能指 breadth-first or depth-first search，广度优先或深度优先搜索\]。呃，所以你会做这种搜索，对吧？比如，你可能在玩

### [19:06](https://www.youtube.com/watch?v=Vhe_bX8mV2s&t=1146s) · b000023

**English**

Sudoku. uh maybe you're trying to do some crossword all sorts of things whereas some path you have to diverge try different things and have the model numerate and also backtrack and it gets stuck until it finally finds some answer. So that's a another very common type of reasoning. So people have embedded that into language models as well. So tree of thoughts is also a prompting based approach. Right now it's just prompting the model to basically generate the search tree, try out different paths in the search tree when it's stuck, backtrack and recurse on the ones where it's not stuck. So also a simple way of you know embedding reasoning into these models.

**中文**

数独（Sudoku）。呃，也可能是在做填字游戏，各种这样的事情：在某条路径上你必须分叉，尝试不同的东西，让模型枚举，也让它回溯，在卡住时这样做，直到最终找到某个答案。所以，这是另一种很常见的推理类型。人们也把它嵌入到语言模型中。所以，tree of thoughts 也是一种基于提示的方法。现在它只是提示模型基本上生成搜索树，尝试搜索树中的不同路径，卡住时回溯，并在没有卡住的路径上递归。所以，这也是一种把推理嵌入这些模型的简单方法。

### [19:53](https://www.youtube.com/watch?v=Vhe_bX8mV2s&t=1193s) · b000024

**English**

These have been extended to to multimodal settings. Uh so this is a paper that I like very much. is called socratic models composing zerosot multimodal reasoning with language and what this model basically does is that it takes all sorts of models right the llm which has some unique reasoning ability it has a vision language model which is able to convert the image into language it has a audio language model which can convert um audio and sounds and caption that in language and it has some you know vision language action model which can take language and outputs actions. So language is the medium right this multimodal setting language is a medium the bottleneck over which reasoning happens and with language as a reasoning medium you can do all sorts of tasks across different modalities for example here's an image captioning example

**中文**

这些方法已经被扩展到多模态场景。呃，这是一篇我非常喜欢的论文，叫作 socratic models composing zerosot multimodal reasoning with language \[字幕疑误，zerosot 可能指 zero-shot\]。这个模型基本上做的是，把各种模型拿过来，对吧？有具备某种独特推理能力的 llm；有能把图像转换成语言的视觉语言模型；有能把音频和声音转换成语言描述的音频语言模型（audio language model）；还有某种视觉语言动作模型（vision language action model），能够接收语言并输出动作。所以，语言是媒介，对吧？在这个多模态场景中，语言是媒介，是推理发生所经过的瓶颈。有了语言作为推理媒介，你就可以跨不同模态完成各种任务。比如，这里是一个图像描述（image captioning）的例子

### [21:02](https://www.youtube.com/watch?v=Vhe_bX8mV2s&t=1262s) · b000025

**English**

So you prompted by saying your intelligent bot. You give it some templates. Some of these templates give also include in context examples, right? So you can start applying it to do all sorts of image captioning, identifying people, identifying objects, having open-ended dialogue with this image. Nothing you haven't really seen from from the vision language models we saw in the first half of the semester. But going beyond that, it can also do robotic perception and planning. So now you start getting more into having a model out of multiple sets and taking the executing those steps. So I show this video. So maybe the task is to move move all the blocks to different corners counterclockwise. That's a pretty accurate task. So another generate plan would first break it down into move the green block where move the yellow block where and then move the blue block where

**中文**

所以，你通过说“你的智能机器人”来给它提示。你给它一些模板。其中一些模板还包含上下文示例（in-context examples），对吧？于是，你可以开始用它做各种图像描述、识别人、识别物体、围绕这张图像进行开放式对话。这些其实都不是你们没见过的，我们在前半学期的视觉语言模型里已经看过。不过，除此之外，它还能进行机器人感知和规划（robotic perception and planning）。现在，你就更进一步，让模型 out of multiple sets \[字幕疑误，可能指 output multiple steps，输出多个步骤\]，并去执行这些步骤。我来放这个视频。任务可能是把所有积木按逆时针方向移到不同角落。这是一个相当准确的任务。于是，另一个生成的计划会先把它分解成：把绿色积木移到哪里，把黄色积木移到哪里，然后把蓝色积木移到哪里

### [21:59](https://www.youtube.com/watch?v=Vhe_bX8mV2s&t=1319s) · b000026

**English**

and then it will actually execute each of these steps in sequence. Another example stack of blocks on top of each other. You see other lamb is planning out individual steps to first put the yellow block and then put the blue block on top of it and then put the green block further on top of it and then executing those actions.

**中文**

然后它就会真正依次执行每一步。另一个例子，把积木一块叠在另一块上。你看到 other lamb \[字幕疑误，可能指 the LLM\] 正在规划各个步骤：先放黄色积木，再把蓝色积木放在它上面，然后再把绿色积木放到更上面，接着执行这些动作。

### [22:38](https://www.youtube.com/watch?v=Vhe_bX8mV2s&t=1358s) · b000027

**English**

and and more, right? So, it's using okay again none of this is really of amps. It's using just the innate ability of your language model to take in that task. For example, you know, a range order of blocks counterclockwise. It takes in the current image and this model is prompted to plan out each of the individual steps that it has to take, right? how we should move the green block, how we should move the yellow block, how we should move the blue block. Right? So that's all your steps over there. And then that is sent to an action model which then outputs in this case is connected to the robot simulator is going to adjust the degrees of freedom on the robot hand uh to actually execute each of those actions in sequence. So that's an example of reasoning. And finally, here's a another example. So now it's going to video video reasoning. So uh I'm going to show you some examples. But at the high level,

**中文**

还有、还有更多，对吧？所以，它使用的是，好，再说一次，这些其实都不是 of amps \[字幕疑误，原意不明\]。它只是使用语言模型本身已有的能力来接收任务。例如，你知道，按逆时针方向安排积木的顺序。它接收当前图像，然后通过提示让模型规划它必须执行的每一个步骤，对吧？应该如何移动绿色积木，如何移动黄色积木，如何移动蓝色积木。对吧？那边就是所有步骤。然后，这些会被发送给一个动作模型（action model），它接着输出，在这个例子中，它连接着机器人模拟器，会调整机械手的自由度（degrees of freedom），以真正依次执行这些动作。所以，这是一个推理的例子。最后，这里还有另一个例子。现在进入视频、视频推理（video reasoning）。呃，我会展示一些例子。但从高层次来看，

### [23:34](https://www.youtube.com/watch?v=Vhe_bX8mV2s&t=1414s) · b000028

**English**

what this is going to do is that it's going to parse this scene and it's going to keep track of all the objects in that scene, right? You know that you're watching a TV that you have a remote in your hand. And after a while, you put the remote down. It's going to keep track of a of a state, a memory state of all of the objects and actions. And then maybe after a couple of minutes, you ask the model, where did I put the remote? can find it. It should be able to retrieve that you have put it uh at some particular location from its world state history. So here's the example.

**中文**

它要做的是解析这个场景，并持续跟踪场景中的所有物体，对吧？你知道，你正在看电视，手里拿着遥控器。过了一会儿，你把遥控器放下。它会持续记录所有物体和动作的一个状态、一个记忆状态。然后，也许几分钟之后，你问模型：“我把遥控器放在哪儿了？”能找到它。它应该能够从世界状态历史（world state history）中检索到，你把它放在了某个特定位置。这里就是例子。

### [24:18](https://www.youtube.com/watch?v=Vhe_bX8mV2s&t=1458s) · b000029

**English**

So it's storing at each time the location, the action, the objects, and this can basically be a log of your whole day. Imagine you're wearing a glasses. You can log visually everything that you're doing. And obviously storing vision is very expensive. Storing video is very expensive. So you want to just summarize it into a compact summary. And then you can go back and ask questions like, how much time did I spend doing this and that? Uh where did I put my keys? I might have forgotten them. And you can then start asking questions. So, why did I go to the front porch?

**中文**

所以，它在每个时刻存储位置、动作和物体，这基本上可以成为你一整天的日志。想象你戴着一副眼镜，就可以从视觉上记录你做的所有事情。显然，存储视觉信息非常昂贵，存储视频也非常昂贵。所以，你希望把它概括成一个紧凑的摘要。然后，你可以回头提问，比如：“我在这件事和那件事上分别花了多少时间？”呃，“我把钥匙放在哪儿了？我可能忘了。”然后你就可以开始提问。所以，“我为什么去了前廊？”

### [24:59](https://www.youtube.com/watch?v=Vhe_bX8mV2s&t=1499s) · b000030

**English**

Where did I leave my mouth? Is it going to extract my brain?

**中文**

“我把嘴落在哪儿了？”“它会提取我的大脑吗？”

### [25:10](https://www.youtube.com/watch?v=Vhe_bX8mV2s&t=1510s) · b000031

**English**

\[clears throat\]

**中文**

\[清嗓子\]

### [25:22](https://www.youtube.com/watch?v=Vhe_bX8mV2s&t=1522s) · b000032

**English**

So temporal reasoning when did something last happened. You get the idea. It's able to to answer all sorts of questions about about this long context and it's able to do so. Uh sometimes these question are easier just by identifying something. Sometimes they require for example chaining together a sequence of events that are stored in this in this history. So there are many debates surrounding reasoning. Um it is kind of seen as a holy grail of AI, right? Being able to reason, be able to think, being able to do math, being able to take actions over a long sequence like people cans. Really been the holy grail of AI. And uh it's really you know people approaching it from different spectrums right there are some people who believe that reasoning will emerge just from data. You give the model all sorts of examples of theorems being proved and give the model all sorts of examples of

**中文**

所以，时间推理（temporal reasoning），某件事上次是什么时候发生的。你们明白这个意思了。它能够回答关于这段长上下文（long context）的各种问题，而且能够做到。呃，有时候这些问题比较简单，只需识别某个东西。有时候则需要，比如，把存储在这段历史中的一系列事件串联起来。所以，围绕推理有很多争论。它被看作 AI 的某种圣杯，对吧？能够推理，能够思考，能够做数学，能够像人一样在一个很长的序列中采取行动。这确实一直是 AI 的圣杯。呃，人们从不同的立场来研究它，对吧？有些人相信，推理只会从数据中涌现。你给模型各种定理证明的例子，给模型各种

### [26:19](https://www.youtube.com/watch?v=Vhe_bX8mV2s&t=1579s) · b000033

**English**

robots moving around and videos of you know robots cleaning or people cleaning the house that all this reasoning would somehow be merged and learned by the model. And then you have people who are uh staunch believers that reasoning has to be top down. It has to be injected into the model. There has to be some symbolic structure. There has to be you know theorem provers. There has to be you know you know world models inside the model so that it can plan within it. So this is the one that goes with more symbolic structure and planning for reasoning. And the other side is more bottom up datadriven. Um I mean obviously most most progress nowadays is here right even though you might think that most progress is here datadriven LMS but in fact we are injecting a lot of structure into these language models it's not pure language model zero shot reasoning nowadays it's

**中文**

机器人四处移动的例子，以及机器人清洁或人们打扫房屋的视频，所有这些推理就会以某种方式被整合，并被模型学会。然后也有一些人坚定地相信，推理必须是自上而下（top-down）的，必须被注入模型。必须有某种符号结构，必须有定理证明器（theorem provers），必须在模型内部有世界模型（world models），使它能够在其中规划。所以，这一边更强调符号结构以及用于推理的规划，另一边则更强调自下而上、数据驱动（data-driven）。嗯，我是说，显然如今大多数进展都在这里，对吧？尽管你可能认为大多数进展在这里，也就是数据驱动的 LMS \[字幕疑误，可能指 LLMs\]，但事实上，我们正在给这些语言模型注入大量结构。如今并不是纯粹的语言模型零样本推理（zero-shot reasoning），而是

### [27:14](https://www.youtube.com/watch?v=Vhe_bX8mV2s&t=1634s) · b000034

**English**

a lot of hybrid symbolic approaches that are slowly making their way into these models right I gave the example of train of thought right chain of thought is an example of injecting some sequential structure in how the language model outputs users dependencies from previous outputs. Right? When chain of thought doesn't work really well, tree of thoughts is a way of embedding search and a classic symbolic AI algorithm search into the output of language models. So it seems data driven but you know on the output side of the models and on the training side you will see that there's a lot of ways where whereby structure is injected to enable reasoning. Of course, I'm also not saying it has to be fully structured. Obviously, no one does this anymore, but you're still going to use, you know, MLMs and multimodal models as key components in today's reasoning systems. So, what are some of the main decisions

**中文**

大量混合符号方法（hybrid symbolic approaches）正在逐步进入这些模型，对吧？我举了 train of thought \[字幕疑误，可能指 chain of thought\] 的例子。Chain of thought 就是一个例子：在语言模型如何输出、如何使用此前输出的依赖关系方面，注入某种顺序结构。对吧？当 chain of thought 效果不太好时，tree of thoughts 是一种将搜索、这种经典符号 AI 算法，嵌入语言模型输出的方法。所以它看起来是数据驱动的，但你会看到，在模型的输出端和训练端，有很多注入结构以实现推理的方法。当然，我也不是说它必须完全结构化。显然，现在已经没有人这么做了，但你仍然会把 MLMs \[字幕疑误，可能指 LLMs\] 和多模态模型作为当今推理系统的关键组成部分。那么，为了让 AI 能够推理，我们需要做出的主要决策

### [28:11](https://www.youtube.com/watch?v=Vhe_bX8mV2s&t=1691s) · b000035

**English**

that we have to make in order to enable AI to reason? Well, one big thing is uh differentiability, right? You're going to see this a lot when you look at paper says that AI reason, right? By definition, reasoning is symbolic. It's discrete, right? is a discrete number of steps. Each step is a discrete number of actions. If I want to search over all these possible steps and actions, this by nature is very discreet, right? Uh that makes it not super compatible sometimes with your AI models because in AI models, sorry, in deep learning, you often need differentiability, right? You need differentiable forward passes so that you can back propagate and update gradients. So that will be a big point of contention. You read a lot of stuff that start with some reasoning structure that is partly symbolic not differentiable and to make some relaxations to make it differentiable so it's compatible with deep learning. Another uh key thing which follows a

**中文**

有哪些？其中一个重要方面是可微性（differentiability），对吧？你看那些声称 AI 能推理的论文时，会经常看到这一点。按照定义，推理是符号性的，是离散的，对吧？它有离散数量的步骤，每一步有离散数量的动作。如果我想搜索所有这些可能的步骤和动作，这本质上是非常离散的，对吧？呃，这有时会让它和 AI 模型不太兼容，因为在 AI 模型中，抱歉，在深度学习（deep learning）中，你通常需要可微性，对吧？你需要可微的前向传播（forward passes），才能反向传播（backpropagate）并更新梯度。所以，这会是一个很大的争论点。你会读到很多工作，从某种部分符号化、不可微的推理结构出发，再做一些松弛（relaxations），让它变得可微，从而兼容 deep learning。另一个关键点，和第一个有点

### [29:08](https://www.youtube.com/watch?v=Vhe_bX8mV2s&t=1748s) · b000036

**English**

little bit on the first one is in the concepts right the concepts that you use to reason over are they discrete or continuous right discrete gives interpretability it gives a small set of possibilities but it's not differentiable often times there is a need for continuous relaxations and finally what is the best m mix of knowledge and data which part should be learned by the model and which part should be injected by human expert knowledge

**中文**

关联，是概念（concepts），对吧？你用来推理的概念，是离散的还是连续的？离散概念提供可解释性（interpretability），提供一小组可能性，但它不可微。因此，很多时候需要连续松弛（continuous relaxations）。最后，知识与数据的最佳混合方式是什么？哪些部分应该由模型学习，哪些部分应该由人类专家知识注入？

### [29:39](https://www.youtube.com/watch?v=Vhe_bX8mV2s&t=1779s) · b000037

**English**

And there's many implications, right? There's many implications based on all these decisions on the model that you end up training. How intercredible it is, how robust is it, how efficient it is, how many samples it needs to achieve performance. So that's a precursor example. So now let's jump deep into reasoning and specifically the sub challenges of reasoning. So I like to think of any problem as kind of having these perpendicular dimensions right perpendicular dimensions that break down the problem to into each of these sub problems. So one very important sub problem as I motivated in reasoning is the structure of the problem. Is it a single step identification? So most people maybe refer to this as perception. Is there a person perceiving something? And then you have things like you know temporal or sequential like your train of thought style you have

**中文**

而这有很多影响，对吧？这些决策会对你最终训练出的模型产生很多影响。它有多 intercredible \[字幕疑误，可能指 interpretable，可解释\]，多鲁棒（robust），多高效，需要多少样本才能达到性能要求。所以，这是一个铺垫性的例子。现在，让我们深入推理，具体看看推理中的子挑战。我喜欢把任何问题看成具有这些相互垂直的维度，对吧？这些相互垂直的维度把问题拆成各个子问题。正如我在引出推理时提到的，一个非常重要的子问题是问题的结构。它是单步识别吗？大多数人可能会把这称为感知（perception）。是不是有人正在感知某个东西？接着，还有时间性或顺序性的东西，比如你的 train of thought 风格 \[字幕疑误，可能指 chain of thought\]；还有

### [30:35](https://www.youtube.com/watch?v=Vhe_bX8mV2s&t=1835s) · b000038

**English**

hierarchical you have these trees or tree of thought search and you also have interactive problems where it's not just enough to to search and then finish by searching maybe changes the state taking action changes the state and you have to repeat multiple times in that environment. So that's what we we termed as interactive concepts. Concepts are you know we break down reasoning into individual steps right each step how do you parameterize the information right are these in words so nowadays when you do LLM reasoning most of the reasoning is done with word as a concept each word is a is a concept that you're reasoning over when you do reasoning over other modalities it may or may not be words it could be latent representations it can be attention maps it can be bounding boxes other basic concepts in reasoning.

**中文**

层次结构（hierarchical），还有这些树或 tree of thought 搜索，也有交互式问题：并不是搜索然后结束就足够了，也许搜索会改变状态，采取行动会改变状态，你必须在那个环境中重复多次。所以，这就是我们所说的交互式。概念。概念是，你知道，我们把推理拆成单独的步骤，对吧？每一步如何参数化（parameterize）信息？这些信息是词语吗？如今做 LLM 推理时，大多数推理都把词语作为概念，每个词都是一个你所围绕着推理的概念。当你对其他模态进行推理时，它可能是词语，也可能不是；它可以是潜在表征（latent representations），可以是注意力图（attention maps），可以是边界框（bounding boxes），或者推理中的其他基本概念。

### [31:32](https://www.youtube.com/watch?v=Vhe_bX8mV2s&t=1892s) · b000039

**English**

Inference tells you how to combine concepts, right? So a lot of these uh can be the if then relationships. If A happens then b. So that if then is a relation, right? Uh and and ors are also possible relations when you're trying to combine information. So when proving something lema one is true and lema two is true or lema one is true or lema two is true. So these are ways of combining concepts and finally a big sub challenge is how to inject the knowledge right what kind of knowledge there usually has to be some human expert who is um defining all of these so not going to cover everything we have the survey paper which covers everything but we're not going to cover everything in class we're going to focus more on really what is I guess state-of-the-art today which is to mostly use language as a medium for reasoning, right? Using the

**中文**

推断（inference）告诉你如何组合概念，对吧？其中很多可以是 if-then 关系。如果 A 发生，那么 b。所以这个 if-then 就是一种关系，对吧？呃，当你尝试组合信息时，and 和 or 也是可能的关系。例如，证明某件事时，引理一为真并且引理二为真，或者引理一为真或者引理二为真。所以，这些都是组合概念的方式。最后，一个重要的子挑战是如何注入知识，对吧？什么样的知识？通常必须有某个人类专家来定义所有这些内容。我们不会把所有东西都讲完，我们有一篇综述论文覆盖了全部内容，但课堂上不会全讲。我们会更多聚焦于，我想，如今真正最先进的方法，也就是主要使用语言作为推理媒介，对吧？利用

### [32:28](https://www.youtube.com/watch?v=Vhe_bX8mV2s&t=1948s) · b000040

**English**

power of pre-training LLMs. But then the question becomes, how do you incentivize and train these multimodal LLMs to reason uh in an accurate and robust manner?

**中文**

预训练 LLMs 的能力。但接下来的问题是，如何激励并训练这些多模态 LLMs，让它们以准确且鲁棒的方式进行推理？

### [32:44](https://www.youtube.com/watch?v=Vhe_bX8mV2s&t=1964s) · b000041

**English**

So the setup usually looks like this. Input can be uh you know text prompt perhaps also with images, videos, any other modalities and this input obviously would also include the question which um necessitates necessitates reasoning right so it's a maybe a hard question and reasoning usually as you've seen is across all of these step one two three uh step one two and three and so on right multiple steps and after the model has reasoned sufficiently over uh number of steps it is happy with it will stop reasoning and it will output some final answer. So this uh can be thought of as a general schematic. What is important could be just a final output. For example, we have lots of calculations in math and just one final answer. But sometimes we also want to score the quality of the intermediate reasoning as well.

**中文**

通常的设置是这样的。输入可以是文本提示（text prompt），也可能包含图像、视频或任何其他模态，而且输入显然还会包含一个需要、需要推理的问题，对吧？它可能是一个难题，而推理通常正如你们看到的，会经过这些步骤一、二、三，呃，步骤一、二、三，等等，对吧？多个步骤。当模型经过它认为足够数量的步骤，充分推理之后，它就会停止推理，输出某个最终答案。所以，这可以看作一个通用示意框架。重要的可能只是最终输出。例如，我们在数学中做大量计算，最后只得到一个答案。但有时候，我们也希望对中间推理的质量进行评分。

### [33:38](https://www.youtube.com/watch?v=Vhe_bX8mV2s&t=2018s) · b000042

**English**

Method one as we've seen is just direct right? If you will just give us the input things like think step by step or think methodically or you give us part of the input some in context examples of the model doing this uh step-by-step reasoning then you don't really have to change the model. You don't have to change its parameters. You don't have to train it any further and the model will still do reasonably well. Right? So this is all your stuff like various prompting based chain or any thought based prompting approaches. Method two is what we call supervised fine tuning. Supervised fine-tuning basically assumes that you're going to collect some data set that has not just input output examples without the reasoning but data examples of input reasoning steps output right. So you get full supervision when data set with full supervision over what reasoning. So in

**中文**

方法一，正如我们看到的，就是直接进行，对吧？如果你只在输入中给出“一步一步思考”或“有条理地思考”这样的内容，或者把模型进行逐步推理的一些上下文示例作为输入的一部分，那么实际上不必改变模型。不必改变参数，不必进一步训练它，模型仍然会做得相当不错，对吧？这就是各种基于提示的链式方法，或者任何基于 thought 的提示方法。方法二是我们所说的监督微调（supervised fine-tuning）。监督微调基本上假设，你会收集某个数据集，其中不只是没有推理的输入—输出示例，而是输入—推理步骤—输出的示例，对吧？这样，你就获得了完整监督，一个对推理有完整监督的数据集。所以，在

### [34:33](https://www.youtube.com/watch?v=Vhe_bX8mV2s&t=2073s) · b000043

**English**

the case of math maybe you will just get you know examples of of well annotated workings of how each step should reason in the case of robotics would maybe have the prompt where you're moving the blocks counterclockwise and you would have real annotations of where each block should be placed as the reasoning steps. \[snorts\] So if you're able to curate such a data data set uh basically meaning assuming you have these reasoning traces then you can do a supervised fine-tuning which basically means you're training your model to auto regressively predict given the input not just the output but also each step in the reasoning right so fairly straightforward uh there's a trade-off of course depending on how large this data set you collect with the reasoning traces if it's zero zero then you're just doing direct prompting. If it's small like five or 10 then you would do kind of in context learning where you just give examples as the inputs and if it's

**中文**

数学情况下，你也许会得到一些标注完善的解题过程示例，说明每一步应该如何推理；在机器人情况下，也许会有一个提示，让你把积木按逆时针方向移动，并且会有真实标注，说明每块积木应该放在哪里，作为推理步骤。\[吸鼻声\] 所以，如果你能够整理出这样的数据集，呃，基本上意味着，假设你有这些推理轨迹（reasoning traces），那么就可以做监督微调，也就是训练模型在给定输入时，以自回归（autoregressive）方式，不仅预测输出，还预测推理中的每一步，对吧？所以，相当直接。当然有一个权衡，取决于你收集的、带推理轨迹的数据集有多大。如果是零、零，那么你就是直接提示。如果很小，比如五个或 10 个，那么就做一种上下文学习（in-context learning），直接把示例作为输入；如果它

### [35:30](https://www.youtube.com/watch?v=Vhe_bX8mV2s&t=2130s) · b000044

**English**

larger then you'll probably update the model using Laura and do supervised functioning right the classic uh training of LLMs just treating the reasoning as the target of course the interesting thing happens when you don't have such a data set or where it's very expensive to get all of these reading traits need so you only have inut output pairs very difficult to get the reasoning traces. How do you still get the model to get better at doing this intermediate reasoning before giving the output? So that's where reinforcement learning comes in and that will be today's focus. Right? Reinforcement learning is a way of training these models even without these intermediate reasoning sets given only perhaps the output or as you see what we mean a reward function scoring the quality of the reasoning and the outputs using that as a signal to train

**中文**

更大，那么你可能会用 Laura \[字幕疑误，可能指 LoRA\] 来更新模型，做 supervised functioning \[字幕疑误，可能指 supervised fine-tuning\]，对吧？也就是经典的 LLMs 训练，只是把推理当作目标。当然，有意思的情况是，你没有这样的数据集，或者要获得所有这些 reading traits \[字幕疑误，可能指 reasoning traces\] 的成本很高。所以你只有输入—输出对，很难得到推理轨迹。你如何仍然让模型更擅长在给出输出之前完成这些中间推理？这就是强化学习发挥作用的地方，也是今天的重点，对吧？强化学习是一种训练这些模型的方法，即使没有这些中间推理 sets \[字幕疑误，可能指 steps\]，可能只给输出，或者正如你们将看到的，我们所说的奖励函数，用来给推理和输出的质量评分，并把它作为信号来训练

### [36:26](https://www.youtube.com/watch?v=Vhe_bX8mV2s&t=2186s) · b000045

**English**

a model to automatically infer what these reasoning steps are. Right? Often times just having the output is easy. A reward function is often also easy. Right? reward function could be uh does the does a theorem type check right or does a theorem pass a theorem verifier that is much easier to evaluate rather than actually writing out the theorem uh in code it could be does the model does the code that you write pass the test cases so what percentage of the test cases does it pass really easy to evaluate and therefore define a reward for all sorts of code that a model may have written but it is very difficult to write the code itself often times this reward function or as we call it verifier is much more accessible than actual uh actual ground truth reasoning. Okay, any questions about uh this setup before we dive into the details?

**中文**

模型，让它自动推断这些推理步骤是什么。对吧？很多时候，只得到输出很容易。奖励函数往往也很容易，对吧？奖励函数可以是，呃，这个定理能否通过类型检查（type check），或者能否通过定理验证器（theorem verifier）。这比实际写出定理容易评估得多。在代码中，它可以是模型、你写的代码是否通过测试用例，通过了多大比例的测试用例。这很容易评估，因此也很容易为模型可能写出的各种代码定义奖励，但编写代码本身却非常困难。很多时候，这个奖励函数，或者我们称之为验证器（verifier）的东西，比真正的、真实的标准答案推理（ground truth reasoning）更容易获得。好，在深入细节之前，关于这个设置有什么问题吗？

### [37:27](https://www.youtube.com/watch?v=Vhe_bX8mV2s&t=2247s) · b000046

**English**

\[clears throat\]

**中文**

\[清嗓子\]

### [37:35](https://www.youtube.com/watch?v=Vhe_bX8mV2s&t=2255s) · b000047

**English**

All right, great. So, we'll discuss reinforcement learning. Uh, a topic which is which always been useful, right? You know, key area of AI, key area of computer science, uh, but really blown up in popularity over, you know, 2025 and 2026 because of its implications and use in training language models. So in reinforcement learning uh the basic setup is this right? We think about it as an agent in some environment right agent can be thought of as taking a bunch of possible states in the environment. Uh sorry let me go to here. So uh agent can be thought of as you know being in a potential number of states in the environment right usually we think of these environments as some of these like grid world environments where the agent is maybe some character

**中文**

好，很好。接下来我们讨论强化学习。呃，这是一个一直都很有用的主题，对吧？你知道，AI 的关键领域，计算机科学的关键领域，不过在 2025 和 2026 年，由于它对语言模型训练的影响和应用，热度确实大幅上升。强化学习中的基本设置是这样的，对吧？我们把它看作某个环境（environment）中的一个智能体，对吧？智能体可以被看作在环境中采取一组可能的状态（states）。呃，抱歉，让我切到这里。智能体可以被看作处于环境中若干可能状态之一，对吧？我们通常把这些环境想象成网格世界（grid world）环境，其中智能体也许是某个角色

### [38:31](https://www.youtube.com/watch?v=Vhe_bX8mV2s&t=2311s) · b000048

**English**

that's moving up down left right so the states will just be different locations in that environment right one one two two one two2 different locations actions are just different things that the agent could do it could move up down left right and so on transition functions basically Say if the model is in some state and it takes some action what next state would it go into right most of the times that's deterministic if it's going forward go forward one step but sometimes there might be some randomness involved in the transition so that's a transition function the reward function is very important basically says you know when the uh agent is in some state takes some action and goes to some next state what reward would it get you think about it as some some parts in this math have a negative reward because they fall into a hole and some parts of the map have positive reward because they get some diamond. Right? So that's a reward

**中文**

在上下左右移动。所以，状态就是环境中的不同位置，对吧？一一、二二、一二二，不同位置。动作（actions）就是智能体能做的不同事情，它可以向上、向下、向左、向右移动，等等。转移函数（transition functions）基本上是在说，如果模型处于某个状态，并采取某个动作，那么下一步会进入哪个状态，对吧？大多数时候这是确定性的（deterministic），如果向前，就向前走一步。但有时转移过程可能涉及某种随机性，这就是转移函数。奖励函数非常重要，基本上是说，当智能体处于某个状态、采取某个动作并进入下一个状态时，会得到什么奖励。你可以把它想象成，这个 math \[字幕疑误，可能指 map\] 中的某些部分有负奖励，因为它们会掉进洞里，而地图的某些部分有正奖励，因为它们会获得某颗钻石。对吧？这就是奖励

### [39:29](https://www.youtube.com/watch?v=Vhe_bX8mV2s&t=2369s) · b000049

**English**

function and there's some state which a model starts in and some discount factor and horizon. These are not super important but you can think about this as basically constraints on how long the agent would interact with the environment total. So it wouldn't really go on forever. So we sometimes draw it as this, right? agent takes some action in the environment and it goes to some new state and it gets some reward as a result of taking that action and this happens across multiple steps. There are some important things that we care about in reinforcement learning, right? The most important thing is what we call this reward or return. A return basically means, you know, when I'm taking an action right now, what is the immediate reward that I get, right? That's R and T plus one, right? At the next time step, but more importantly, what are also future rewards I might get? Is it the long-term rewards that I really care about? Sometimes you might

**中文**

函数。还有模型开始时的某个状态，以及某个折扣因子（discount factor）和时域（horizon）。这些不是特别重要，但你可以把它们基本上看作对智能体与环境总共交互多长时间的约束，所以它不会真的永远持续下去。有时我们把它画成这样，对吧？智能体在环境中采取某个动作，进入一个新状态，并因采取该动作得到某个奖励，这个过程发生在多个步骤中。在强化学习中，我们关心一些重要的东西，对吧？最重要的是我们所说的奖励（reward）或回报（return）。回报基本上意味着，当我现在采取一个动作时，我得到的即时奖励（immediate reward）是什么，对吧？那就是 R 和 T 加一，对吧？在下一个时间步。但更重要的是，我还可能得到哪些未来奖励？我真正关心的是长期奖励吗？有时候，你可能

### [40:26](https://www.youtube.com/watch?v=Vhe_bX8mV2s&t=2426s) · b000050

**English**

have to sacrifice some reward in the short term to get more rewards in the long term. Sometimes you don't care about it. Sometimes you want big amounts of reward in the short term and you don't care about the long term. There's various trade-offs, various trade-offs and whether you want short-term rewards or long-term reward. We want to have some definition of you know maximizing long-term rewards, right? And then a policy is another very key aspect. Policy basically tells the agent how to act. How to act is basically a distribution where given any state what action I should take right so it's a distribution over next states a next actions given particular states we usually refer to the policy as time and your goal is to find the policy which basically maximizes your return overall different ways of acting over all different actions that you could take which is the one that would lead to not just immediate reward maximize in

**中文**

必须牺牲一些短期奖励，才能获得更多长期奖励。有时候你不关心这个。有时候你想在短期内获得大量奖励，而不关心长期。有各种权衡，关于你想要短期奖励还是长期奖励的各种权衡。我们希望有某种最大化长期奖励的定义，对吧？然后，策略（policy）是另一个非常关键的方面。策略基本上告诉智能体如何行动。如何行动基本上是一个分布：给定任意状态，我应该采取什么动作，对吧？所以，它是在给定特定状态时，关于下一状态、下一动作的分布。我们通常把策略称为 time \[字幕疑误，可能指 pi\]，你的目标是找到使回报最大化的策略。在所有不同的行动方式、所有你能够采取的不同动作中，哪一种能够不仅让即时奖励在

### [41:23](https://www.youtube.com/watch?v=Vhe_bX8mV2s&t=2483s) · b000051

**English**

the short term term but long term the reward also being mass. You can think of the analogy to your language models, right? In this case, the states are basically words, right? Context, things that the model has interacted with you so far. That's your current state. Actions are basically different tokens that you can generate, right? Policy is basically the response, right? Over all the actions, all the words that a model could generate, what is the right sequence of words that it should generate? And the return is ideally long-term not just to make you happy to pursue you in the one response but to actually lead to some meaningful interaction and lead to some meaningful outcome in the long term. So you can think about this as a context of LLMs and almost any any problem can be thought of using this setup.

**中文**

短期内最大化，而且让长期奖励也被 mass \[字幕疑误，可能指 maximized\]。你可以把它类比到语言模型，对吧？在这种情况下，状态基本上就是词语，对吧？上下文，模型到目前为止与你交互过的内容。这就是当前状态。动作基本上就是你可以生成的不同词元（tokens），对吧？策略基本上就是回复，对吧？在模型可能生成的所有动作、所有词语中，它应该生成的正确词语序列是什么？而回报理想情况下是长期的，不只是为了让你开心，在一次回复中 pursue you \[字幕疑误，可能指 persuade you\]，而是要真正带来有意义的交互，并在长期带来某种有意义的结果。所以，你可以把它放到 LLMs 的语境中思考，几乎任何问题都可以用这个设置来考虑。

### [42:17](https://www.youtube.com/watch?v=Vhe_bX8mV2s&t=2537s) · b000052

**English**

Of course uh there's some distinction between RL and supervised learning. I think it's quite obvious, right? RL cares about uh making decisions over a sequence not just focusing on the immediate reward uh one prediction but over multiple predictions but multiple words multiple responses that the model has to generate. Uh thereby you care about maximizing some cumulative reward. Uh sometimes the rewards are very sparse. Sometimes the model interacts with the user over multiple turns before the user is asked to rate whether they liked or disliked the conversation. So the rewards can be very fast and as you'll see that's a big challenge with RL and there's several challenges. Uh one quick thing is that there's actually a intersection between RL and supervised learning which is called imitation learning. So that's you can think about that as the first RL algorithm imitation learning and that's also used to train a lot of models

**中文**

当然，RL 和监督学习之间有一些区别。我想这很明显，对吧？RL 关心的是在一个序列中做决策，不只是关注即时奖励、一次预测，而是多个预测、多个词语、模型必须生成的多次回复。因此，你关心的是最大化某种累积奖励（cumulative reward）。呃，有时奖励非常稀疏（sparse）。有时模型与用户交互多轮后，才会要求用户评价他们是否喜欢这段对话。所以，奖励可能非常 fast \[字幕疑误，可能指 sparse\]，你们会看到，这是 RL 的一个重大挑战，而且还有几个挑战。呃，简单提一点，RL 和监督学习实际上存在一个交集，叫作模仿学习（imitation learning）。你可以把它看作第一个 RL 算法，imitation learning，它也被用来训练如今的许多模型

### [43:15](https://www.youtube.com/watch?v=Vhe_bX8mV2s&t=2595s) · b000053

**English**

today. What application learning basically mean as let's say I care about learning some policy right which means uh given some state what actions to take in fact I'm going to make it more concrete so I use the example of a self-driving car that's also an example of reinforcement learning so the state could be whatever the car sees in the image actions could be like how to turn the wheel whether to accelerate or decelerate and so on so what's a easy way of training this right well but One way is to just get human drivers to give you data, right? Put a dash cam and all the drivers assume they're driving well. So you can basically see, you know, the sequence of uh driving scenarios that real human experts go through and you can also log where they turn their wheel, how much they accelerated, decelerated. So you get a sequence of state action trajectories from the expert, right? for every state as zero

**中文**

。Application learning \[字幕疑误，可能指 imitation learning\] 基本上是什么意思呢？假设我关心学习某个策略，对吧？也就是给定某个状态，要采取什么动作。其实，我把它说得更具体一点，用自动驾驶汽车的例子，这也是强化学习的一个例子。所以，状态可以是汽车在图像中看到的东西，动作可以是如何转动方向盘、是否加速或减速，等等。那么，有什么简单的方法来训练它呢？一种方法就是让人类司机提供数据，对吧？装上行车记录仪，假设所有司机都开得很好。这样，你基本上就能看到真正的人类专家所经历的一系列驾驶场景，也可以记录他们在哪儿转了方向盘、加速和减速了多少。所以，你就从专家那里获得了一系列状态—动作轨迹（state-action trajectories），对吧？对于每个状态 s zero

### [44:11](https://www.youtube.com/watch?v=Vhe_bX8mV2s&t=2651s) · b000054

**English**

what action they took next state next action next state next action as well. Uh and then you can basically train this assuming this is a data set just train it as supervised learning which basically means pair it up into data sets as zero. The first action is a ground truth. Right? Here's what the human driver did when they saw this. Here's what the human driver did when they saw this. Put this data set and train a model. Right? If you do this, you're most likely going to train a pretty good model. You be able to train a pretty good model that imitates how human drivers run. But the big danger is when you start straying away from the sequence of demonstrations that the human experts see. If you just even go a little bit, maybe you veer a little bit towards the sidewalk. If you've never seen how human drivers recover from going onto the sidewalk and coming back, then you're basically in this setting where your

**中文**

，他们采取了什么动作，下一个状态、下一个动作，下一个状态、下一个动作，依此类推。呃，然后基本上就可以训练它：把它当作一个数据集，用监督学习来训练，也就是把它们配对成数据集，s zero，第一个动作就是真值（ground truth）。对吧？这是人类司机看到这个情况时所做的事，这是人类司机看到这个情况时所做的事。把这个数据集拿来训练一个模型，对吧？如果这样做，你很可能会训练出一个相当不错的模型，能够模仿人类司机如何驾驶。但最大的危险是，你开始偏离人类专家所见的示范序列。即使你只偏离一点点，也许稍微向人行道偏了一点。如果你从没见过人类司机如何从开上人行道的情况中恢复、再回到路上，那么你基本上就进入了这样一种情境：你的

### [45:08](https://www.youtube.com/watch?v=Vhe_bX8mV2s&t=2708s) · b000055

**English**

model has never seen how, you know, what distribution it is and it could do all sorts of very dangerous actions, right? they could further keep driving on the sidewalk or you could start driving to people's houses. It was never seen examples of how human experts recover. So imitation learning basically is good uh if you're confident the model will stay in the exact same distributions as the expert trajectories, but once it starts veering off course, you have no guarantees of how you'll recover. So never really works in safety critical situations fully but often very useful to initialize your model. I mean you see this analogy with language models today right which is that pre-training can be thought of well pre-training would be just training of internet data instruction tuning right the second stage instruction tuning instruction fine-tuning can be thought of as imitation learning right where you get humans to annotate what questions

**中文**

模型从未见过这种情况，不知道它处于什么分布中，于是可能采取各种非常危险的动作，对吧？它可能继续在人行道上开，或者开始开进别人家里。它从未见过人类专家如何恢复的例子。所以，imitation learning 基本上在你确信模型会始终处于与专家轨迹完全相同的分布时很有效，但一旦开始偏离路线，就无法保证它如何恢复。因此，它在安全关键（safety-critical）场景中从来不能完全奏效，但通常非常适合用来初始化模型。我是说，你也能在今天的语言模型中看到这种类比，对吧？预训练（pre-training）可以看作，好，预训练只是用互联网数据训练；指令调优（instruction tuning），对吧？第二阶段，instruction tuning、指令微调（instruction fine-tuning），可以看作 imitation learning，对吧？你让人类标注他们希望模型回答什么问题

### [46:05](https://www.youtube.com/watch?v=Vhe_bX8mV2s&t=2765s) · b000056

**English**

they expect the model to answer and how they would answer the question so that's your states and actions and then you just imitate right you train a model on these human annotated instructions and expert completions. So that was the second stage of training. And then as we'll see, we now have a third stage which is to use reinforcement learning to further fine-tune the model and steer the model towards settings where it may not have seen uh in instruction tuning or imitation learning. So you must think of it as a third stage.

**中文**

，以及他们会如何回答问题，这就是你的状态和动作。然后你只是模仿，对吧？你用这些人工标注的指令和专家补全（expert completions）来训练模型。所以，那是训练的第二阶段。接下来，正如我们将看到的，现在还有第三阶段，就是用强化学习进一步微调模型，把模型引导到它在 instruction tuning 或 imitation learning 中可能没见过的情境中。所以，你必须把它看作第三阶段。

### [46:41](https://www.youtube.com/watch?v=Vhe_bX8mV2s&t=2801s) · b000057

**English**

Any questions so far about the differences between supervised learning, reinforcement learning, and this imitation learning, which is kind of a mix of

**中文**

到目前为止，关于监督学习、强化学习，以及这种有点像两者混合的模仿学习之间的区别，有什么问题吗

### [47:11](https://www.youtube.com/watch?v=Vhe_bX8mV2s&t=2831s) · b000058

**English**

Okay. So I'm going to just explain one arrow algorithm uh the simplest one. The simplest one also turns out to be what is enough for for you know training LLMs. And I'm going to explain it using this example uh this pong example just to give you more examples of you know RL settings. So in this case the states are you know there's this game board which is visible and the model is controlling one of these paddles right maybe the human is controlling the other one. So the actions are very simple. Just move up and down. Move up and down. And the reward is one if you are able to successfully shoot the ball over your opponent's paddle and negative one if the opponent uh shoots their ball over across your paddle. Right? So states, actions, rewards, you know, that's first thing you want to think about when you want to frame something as a as a

**中文**

？好。接下来我只讲一个 arrow algorithm \[字幕疑误，可能指 RL algorithm\]，最简单的那个。这个最简单的算法，也恰好足以用于训练 LLMs。我会用这个例子，这个 pong 的例子来解释，也是为了给你们更多 RL 场景的例子。在这里，状态就是，可见的游戏画面，模型控制其中一个球拍，对吧？也许人类控制另一个。动作非常简单，只是上下移动，上下移动。奖励是：如果你成功把球打过对手的球拍，就是一；如果对手把球打过你的球拍，就是负一。对吧？所以，状态、动作、奖励，这就是当你想把某个问题表述为

### [48:09](https://www.youtube.com/watch?v=Vhe_bX8mV2s&t=2889s) · b000059

**English**

reinforcement learning problem. Most of the time it's quite straightforward. So let's say you want to train a train a model for this. So ideally maybe you would just start by defining some neuronet right it takes in a state which is this this vision this this image of the of the game board right 32 by 32 that goes some input layer maybe a CNN whatever and it outputs something. What should it output? Well, because we want to train this AI model to play the game and so it should output the actions, right? So you can think about this neuronet network as the policy model pi that takes in states and outputs actions. In this case, action is just up or down. Binary classification, which also means that you can just have one neuron that outputs some probability of up down is just one minus that. Okay. Um, and the network as we mentioned the

**中文**

强化学习问题时，首先要考虑的内容。大多数时候，这相当直接。假设你想为此训练一个模型。理想情况下，也许首先定义一个神经网络（neural network），对吧？它接收一个状态，也就是这个视觉画面、这张游戏画面图像，对吧？32 乘 32，进入某个输入层，也许是卷积神经网络（Convolutional Neural Network, CNN），什么都可以，然后输出某个东西。它应该输出什么？因为我们想训练这个 AI 模型来玩游戏，所以它应该输出动作，对吧？你可以把这个神经网络看作策略模型 pi，它接收状态并输出动作。在这里，动作只有向上或向下。这是二分类（binary classification），也意味着你只需要一个神经元，输出向上的概率，向下的概率就是一减去它。好。嗯，而这个网络，正如我们提到的，

### [49:06](https://www.youtube.com/watch?v=Vhe_bX8mV2s&t=2946s) · b000060

**English**

reward is that it sees a plus one if it scored a point against the opponent and minus one if the opponent scored a point against you. So how do we train a model? So again go back to the idea of imitation learning. Let's say you had for example an expert that told you at every state the annotated for you whether they move up or down. Right? This is probably very hard to get. it will never cover all states because it's all possible configurations of where is where paddles are. So it's going to be pretty hard. But if you had such a model, you would just do binary classification, right? Given the states in those expert trajectories, can you output what the action is? And that basically means maximize the log probabilities of predicting that particular uh label yi action yi given x i. So that's basically your your uh maximizing your lock likelihood binary cross entropy.

**中文**

奖励是：如果它从对手那里赢得一分，就看到加一；如果对手从你这里赢得一分，就是减一。那么，我们如何训练模型？再次回到 imitation learning 的想法。假设你有一位专家，在每个状态下告诉你，为你标注他们是向上还是向下移动，对吧？这大概很难获得，也永远无法覆盖所有状态，因为它包含球拍位置的所有可能配置。所以会相当困难。但如果有这样的模型，你只需做二分类，对吧？给定专家轨迹中的状态，能否输出对应动作？基本上就是最大化给定 x i 时，预测特定标签 yi、动作 yi 的对数概率（log probabilities）。所以，这基本上是在最大化 lock likelihood \[字幕疑误，可能指 log likelihood，对数似然\]，二元交叉熵（binary cross entropy）。

### [50:03](https://www.youtube.com/watch?v=Vhe_bX8mV2s&t=3003s) · b000061

**English**

So but however we don't have uh these actual trajectories right so what do we do so in RL a key aspect is what we call exploration exploration basically means you know if I don't know what the expert should do right there's no trained signal what I can do is I can just do trial and error I can just try out various things in the environment and just hope for the best sometimes I might be lucky I get some positive rewards Sometimes I may be unlucky, I get negative rewards, but I'm going to just try different things, hope for the best, and see what it gives me and maybe use that to learn. So I might just run according to the current policy. It's a random policy at the beginning. So it's basically just random actions. Sometimes you are lucky and you win and sometimes over a sequence of actions you are unlucky and you lose, right? I purposely annotate, you know, four actions before

**中文**

不过，我们没有这些真实轨迹，对吧？那怎么办？在 RL 中，一个关键方面是我们所说的探索（exploration）。探索基本上意味着，如果我不知道专家应该做什么，对吧？没有训练信号，那我可以做的就是试错（trial and error）。我可以在环境中尝试各种事情，寄希望于好的结果。有时我可能很幸运，得到一些正奖励；有时可能不幸，得到负奖励。但我会尝试不同的事情，期待好结果，看看它会给我什么，也许用这些来学习。所以，我可能就按照当前策略运行。一开始它是一个随机策略，基本上就是随机动作。有时候你很幸运，赢了；有时候经过一系列动作，你不走运，输了，对吧？我特意标出了在

### [51:00](https://www.youtube.com/watch?v=Vhe_bX8mV2s&t=3060s) · b000062

**English**

you win and lose because as you've seen from most of these these problems, you're going to take a bunch of actions before you observe a reward. You have this sparse reward problem. In this case, you might have to move the paddle a couple of times until you either see the ball go over and you get a plus one and you have the ball come over to your side and you get a negative one. So, some sequences you win, some sequences you lose. So then a very straightforward thing to do is that I'm just going to assume all the actions that I did in the sequence of actions leading to me winning were good, right? I mean after all I won, right? I I won at the end. So I'm just going to assume all of those actions were good. So I'm going to maximize the log prop of all the actions in that sequence, all four actions in that sequence because I wanted them. And I'm going to assume for all the other sequences where I lost

**中文**

获胜和失败之前的四个动作，因为正如你们从这些问题中看到的，大多数时候，在观察到奖励之前，你要采取一系列动作。你会遇到稀疏奖励问题（sparse reward problem）。在这里，你也许必须移动几次球拍，直到看到球越过对方，于是得到加一，或者球来到你这边，于是得到负一。所以，有些序列你赢了，有些序列你输了。接下来，一个非常直接的做法就是：我假设，在导致我获胜的动作序列中，我采取的所有动作都是好的，对吧？毕竟我赢了，对吧？我最后赢了。所以，我就假设所有这些动作都是好的。于是，我会最大化那个序列中所有动作的 log prop \[字幕疑误，可能指 log prob，对数概率\]，也就是那四个动作，因为我想要它们。而对于所有其他我输了的序列，我会假设

### [51:58](https://www.youtube.com/watch?v=Vhe_bX8mV2s&t=3118s) · b000063

**English**

all of the actions in those sequence were bad. Right? So I'll minimize the log prob or otherwise maximize negative one times the lock prob for the actions of those actions in those. And this is a big assumption. It's a big assumption because in the end you know this might be a very long sequence of actions right? You don't actually know which action here contributed to you winning or losing. So assigning the equal credit equal either winning credits or equal losing credit to each of those actions is a very strong but we'll see actually works in practice. So in a general case you can think about it as you know you take a bunch of actions you start by exploring your environments some sequence of actions are good and you win some are bad and you lose and regardless of what you do you're maximizing your lock probability scaled by the reward r right uh reward r

**中文**

那些序列中的所有动作都是坏的，对吧？所以，我会最小化这些动作的 log prob，或者换一种说法，最大化负一乘以 lock prob \[字幕疑误，可能指 log prob\]。这是一个很大的假设。之所以是很大的假设，是因为最终这可能是一个非常长的动作序列，对吧？你实际上不知道这里哪个动作促成了获胜或失败。所以，给每个动作分配相同的功劳，无论是相同的获胜功劳还是相同的失败责任，是一个很强的假设，但我们会看到，它在实践中确实有效。一般情况下，你可以这样理解：你采取一系列动作，从探索环境开始，有些动作序列是好的，你赢了；有些是坏的，你输了。而无论做什么，你都在最大化由奖励 r 缩放的 lock probability \[字幕疑误，可能指 log probability\]，对吧？呃，奖励 r

### [52:54](https://www.youtube.com/watch?v=Vhe_bX8mV2s&t=3174s) · b000064

**English**

so in the winning case the reward is plus one and the losing case the reward was negative one here's a general general way of optimizing this model and in fact that is a classic reinforcement learning algorithm. It is called the reinforce algorithm and this is basically the algorithm but I kind of gave you the intuition behind it which is that you have some policy model pi in this case it was a neuron net some states output some actions uh and then you just keep iterating right you just generate a random episode which basically means you know that sequence of up down actions and you wait until you get a reward R and you're basically updating your model with the gradient of the log probabilities scaled by the reward. In this case, the reward

**中文**

，在获胜情况下是加一，在失败情况下是负一。这就是优化这个模型的一种通用方法。事实上，这就是一个经典的强化学习算法，叫作 reinforce 算法。这基本上就是算法本身，不过我给了你们它背后的直觉：你有一个策略模型 pi，在这里它是一个神经网络，接收某些状态，输出某些动作。然后你只需不断迭代，对吧？生成一个随机回合（episode），基本上就是那一串向上、向下的动作，然后等待得到奖励 R，接着用经奖励缩放的对数概率梯度来更新模型。在这里，奖励

### [53:50](https://www.youtube.com/watch?v=Vhe_bX8mV2s&t=3230s) · b000065

**English**

notation was G. So the exact same argument is possibly 4,000. One thing I want to highlight here before kind of giving intuition for why it works is this idea, right? So how do you decide what actions to take? I said at the beginning that you know when you don't know what to do when uh the experts aren't given to you you just want the model to explore right you just randomly take all sorts of actions and hope for the best some sequence of actions lead you to high reward and you'll increase the lock props of those actions some sequence of actions lead to low reward and you minimize the lock probability of those actions right so to start you're going to explore but after as you're training a model the model gets better and better right the model gets better and better which basically means your your your pie your policy model is going to increasingly decide to take good actions that have high rewards instead of bad actions. So you don't

**中文**

的记号是 G。所以，完全相同的论述可能是 4,000。在给出它为何有效的直觉之前，我想强调这一点，对吧？你如何决定采取什么动作？我一开始说过，当你不知道该做什么、没有给你专家示范时，你只是想让模型探索，对吧？随机采取各种动作，期待好的结果。有些动作序列会带来高奖励，你就提高这些动作的 lock props \[字幕疑误，可能指 log probs\]；有些动作序列会带来低奖励，你就最小化这些动作的 lock probability \[字幕疑误，可能指 log probability\]，对吧？所以，一开始你会探索。但随着训练，模型越来越好，对吧？模型越来越好，基本上意味着你的 pie \[字幕疑误，可能指 pi\]，也就是策略模型，会越来越倾向于选择奖励高的好动作，而不是坏动作。所以，你就不

### [54:47](https://www.youtube.com/watch?v=Vhe_bX8mV2s&t=3287s) · b000066

**English**

want to explore too much anymore and then you want to instead follow what your model is outputting as actions for each of the states. Right? So that's a very key concept in reinforcement learning. It is this exploration and exploitation trade-off. Right? When your model isn't good, you want to incentivize the model to explore. so that it sees all different cases and hope for the best and some positive reward will come. When you get increasingly confident that your model becomes better, you want to exploit exploit what the model is giving you as the actions instead of exploring too much. Uh so this is formalizing this epsilon greedy thing which basically means that you start with a higher exploration factor with probability one right you start exploring and then eventually you go down with probability epsilon you start exploring and you instead follow your model.

**中文**

再想进行太多探索，而是想遵循模型为每个状态输出的动作，对吧？这是强化学习中一个非常关键的概念：探索与利用的权衡（exploration–exploitation trade-off），对吧？当模型不好时，你希望激励它探索，让它看到各种不同情况，并期待好结果，希望出现一些正奖励。当你越来越确信模型变好了，就希望利用、利用模型给你的动作，而不是探索太多。呃，这被形式化为 epsilon greedy 这个方法，基本上意味着，开始时有较高的探索因子，以概率一开始探索，然后最终降下来，以概率 epsilon 开始探索，而改为遵循模型。

### [55:42](https://www.youtube.com/watch?v=Vhe_bX8mV2s&t=3342s) · b000067

**English**

So the intuition behind these policy gradients is again this equation. um if the reward is high, I'm going to increase the probability of the actions that I see. And if the reward is low or the reward is negative, I'm going to decrease the probability of the actions that I took. Right? The intuition is that even though there's a very very long sequence of actions that may have happened before you see the reward in expectation the average reward for each of those actions is basically just the final reward divided by um by the length of the sequence. So in expectation it is going to just incentivize you know the good actions and it would penalize the poor actions.

**中文**

所以，这些策略梯度（policy gradients）背后的直觉还是这个公式。嗯，如果奖励高，我就提高我看到的那些动作的概率；如果奖励低，或者奖励为负，我就降低所采取动作的概率，对吧？直觉是，尽管在你看到奖励之前，可能已经发生了一段非常、非常长的动作序列，但在期望意义上，每个动作的平均奖励基本上就是最终奖励除以序列长度。所以，从期望来看，它会激励好的动作，并惩罚差的动作。

### [56:33](https://www.youtube.com/watch?v=Vhe_bX8mV2s&t=3393s) · b000068

**English**

Uh any questions? Okay. So, one downside of these policy gradients uh is this idea that a raw rewards may not be super meaningful, right? Sometimes the rewards may all be positive because your game by definition just always give positive rewards. Sometimes your rewards are all negative because by definition your game just always give negative rewards. So the raw rewards are not super important. Uh what is important is how the rewards change relative to some baseline over time. So people find that one very critical thing to get these methods to work is to wait not just by the reward but the reward minus some baseline reward. You think about the baseline as some rolling average or exponential moving average of the rewards that you have seen so far,

**中文**

呃，有问题吗？好。这些 policy gradients 的一个缺点是，原始奖励（raw rewards）可能并不是特别有意义，对吧？有时奖励可能全是正的，因为游戏按定义就总是给正奖励。有时奖励全是负的，因为游戏按定义就总是给负奖励。所以，原始奖励并不是特别重要。重要的是，奖励随时间相对于某个基线如何变化。因此，人们发现，要让这些方法有效，一个非常关键的做法是，不只是按奖励加权，而是按奖励减去某个基线奖励来加权。你可以把这个基线看作截至目前见过的奖励的某种滚动平均（rolling average）或指数移动平均（exponential moving average），

### [57:30](https://www.youtube.com/watch?v=Vhe_bX8mV2s&t=3450s) · b000069

**English**

right? And then this difference is just whether compared to this baseline, my current reward is better or the current reward is worse. So now this basically helps you scale all your rewards to something that is on average zero and it's just slightly positive and slightly negative.

**中文**

对吧？这个差值表示的就是，相比这个基线，我当前的奖励更好，还是更差。因此，这基本上帮助你把所有奖励缩放到平均为零的水平，只是略微为正或略微为负。

### [57:57](https://www.youtube.com/watch?v=Vhe_bX8mV2s&t=3477s) · b000070

**English**

Okay, we're almost there. So this is essentially what is being done in a lot of these LLMs. Uh so to see how this applies \[clears throat\] to LLM. So again step zero you will pre-train your LLM using using you know just unsupervised data and then in step two you would sorry you will first pre-train LLM with all sorts of unlabelled data and then you will do supervised fine tuning using instruction data and then you will have this stage three right this we're talking I'm talking about this stage three which is this post training some people call it post training which is that you would um give the model some prompts and then ask the LLM to basically generate using its current policy different sequence of words. So maybe the first thing I was doing is this up down in the palm but you can think about it as words in some response and then it might be another set of words in some response another

**中文**

好，我们快讲到了。这本质上就是许多 LLMs 正在做的事情。呃，看看它如何应用到 \[清嗓子\] LLM。再次，步骤零，你会用无监督数据（unsupervised data）预训练 LLM，然后在步骤二，抱歉，你首先用各种无标签数据预训练 LLM，然后用指令数据进行监督微调，接着进入第三阶段，对吧？我们正在讲、我正在讲的就是这个第三阶段，也就是后训练（post-training），有些人叫它 post-training。你会给模型一些提示，然后要求 LLM 基于当前策略生成不同的词语序列。也许我前面做的是 palm 里的上下移动 \[字幕疑误，palm 可能指 pong\]，但你可以把它想象成某个回复中的词语，然后也许是另一个回复中的另一组词语，另一个

### [58:55](https://www.youtube.com/watch?v=Vhe_bX8mV2s&t=3535s) · b000071

**English**

sequence of words in a third response right so you're basically sampling multiple responses from your model uh humans would rank this by some quality right so it gives some reward to these sometimes it's you know just reward for each response sometimes it's a pair-wise ranking but with pair wise ranking you can basically recover the rewards for each sequence. Um that gives you a limited number of rewards which means that sometimes it's useful to train a reward model which basically means if a person has annotated these 10 responses to these 10 rewards just train a model that maps these 10 responses to those 10 results. Right? is just a classification problem which means that this reward model can then be applied to future responses and predict the risk rewards for those future responses. That's the intuitive idea behind a reward model. And then once you have the reward model, you can just use RL which

**中文**

第三个回复中的词语序列，对吧？所以，你基本上是在从模型中采样多个回复。人类会根据某种质量标准给它们排序，对吧？从而给它们一些奖励。有时是给每个回复一个奖励，有时是成对排序（pair-wise ranking），但通过成对排序，基本上也能恢复每个序列的奖励。嗯，这给了你数量有限的奖励，因此有时候训练一个奖励模型（reward model）会很有用。基本上就是，如果一个人把这 10 个回复标注为这 10 个奖励，那就训练一个模型，把这 10 个回复映射到那 10 个结果，对吧？这只是一个分类问题，意味着这个奖励模型随后可以应用于未来的回复，预测这些未来回复的 risk rewards \[字幕疑误，可能指 rewards\]。这就是奖励模型背后的直观想法。一旦有了奖励模型，就可以使用 RL，也就是

### [59:52](https://www.youtube.com/watch?v=Vhe_bX8mV2s&t=3592s) · b000072

**English**

is the policy gradient method that I showed which is to basically update the model increase the lock probabilities scaled by positive rewards or decrease the lock probabilities of the actions scale by negative rewards. Right? That would be used to do this stage three post-training of the model or some people call it reinforcement learning fine tuning of the model to maximize these rewards. Any questions about this quiet group today?

**中文**

我展示的 policy gradient 方法，基本上就是更新模型：按正奖励缩放，提高 lock probabilities \[字幕疑误，可能指 log probabilities\]，或者按负奖励缩放，降低动作的 lock probabilities。对吧？这会用于模型的第三阶段后训练，或者有些人称之为模型的强化学习微调（reinforcement learning fine-tuning），以最大化这些奖励。关于这个，有问题吗？今天大家很安静。

### [1:00:31](https://www.youtube.com/watch?v=Vhe_bX8mV2s&t=3631s) · b000073

**English**

Are people confused or lost? Too easy? Too hard? Okay. Uh several several key things that are good to know, right? Um this is the part where I was showing the reward model, which is that you have a bunch of prompts and then the human might score the rewards for some of them, right? Maybe humans would say this response is really good or this way of answering a question is bad and so on. Uh but that is not generalizable and that data set is often small. The reward model is basically it's a another neuronet network that takes in the the text and tries to predict what the human annotated rewards were. Right? So this reward model can then be used to label the rewards or other prompts and other responses that you get. So this makes it more generalizable. And of course you can also see how this is more generalizable than your supervised earning, right? Because in

**中文**

大家是困惑了，还是跟不上？太简单？太难？好。呃，有几个、几个值得了解的关键点，对吧？嗯，这里是我展示奖励模型的部分，也就是你有一批提示，然后人类可能为其中一些打奖励分，对吧？比如人类会说，这个回复非常好，或者这种回答问题的方式很差，等等。但这无法泛化（generalize），而且数据集通常很小。奖励模型基本上是另一个神经网络，它接收文本，并尝试预测人类标注的奖励是什么，对吧？所以，这个奖励模型随后可以用于为其他提示和得到的其他回复标注奖励。这使它更具泛化能力。当然，你也可以看出，这比监督学习更具泛化能力，对吧？因为在

### [1:01:27](https://www.youtube.com/watch?v=Vhe_bX8mV2s&t=3687s) · b000074

**English**

supervised learning all you get is the person annotating a couple of completions. Now you can get the model to reward not just that completion that the person wrote but any possible combination of uh of completions that anybody or any model generated. So this is why people sometimes say that uh instruction fine-tuning causes the model to sometimes memorize memorize how people conceive it the us but in reinforcement learning the model can truly generalize. It can assign rewards to other ways of solving the task which makes the model more adept at maybe finding other solutions that may also have high rewards or solutions that uh people didn't provide to the model which are also alternative solutions.

**中文**

监督学习中，你得到的只是一个人标注的几个补全。现在，你可以让模型不仅奖励那个人写下的补全，还奖励任何人或任何模型生成的、任何可能组合的补全。所以，人们有时会说，instruction fine-tuning 会让模型有时记住、记住人们如何 conceive it the us \[字幕疑误，原意不明\]，但在强化学习中，模型能够真正泛化。它可以给解决任务的其他方式分配奖励，这让模型更擅长找到也可能具有高奖励的其他解决方案，或者人们没有提供给模型、但同样可行的替代解决方案。

### [1:02:20](https://www.youtube.com/watch?v=Vhe_bX8mV2s&t=3740s) · b000075

**English**

Uh this part I mentioned as well. Sometimes it's much easier to have people compare whether one response is better than the other than to give objective numbers as the reward to each model. Right? This eight versus 1.2 is hard to assign, but it's clear that that is better than this. Uh you can take ranking data as a reward and convert it into the raw rewards.

**中文**

呃，这部分我也提到了。有时，让人比较一个回复是否优于另一个，比给每个模型一个客观数值作为奖励要容易得多，对吧？这个八和 1.2 很难分配，但那一个比这一个好是很明显的。呃，你可以把排序数据当作奖励，并将其转换成原始奖励。

### [1:02:52](https://www.youtube.com/watch?v=Vhe_bX8mV2s&t=3772s) · b000076

**English**

Okay. And I won't go into uh too much detail about this but that is basically the idea behind relevant things GPPO GRPO approaches which are state-of-the-art all of them are just based on the idea of this policy optimization right you have your Q which is your prompt your policy model is your language model you're going to sample a bunch of responses from the language model a group of responses that's the group hyperparameter in gpo for each of the uh responses the model is going to go through a reward model to predict what are the rewards R1 through RG let's say G rewards this reference model I'll say a little bit about it it is where the uh P in pol stands for proximal policy optimization policy optimization is the algorithm

**中文**

好。我不会深入太多细节，但这基本上就是相关的 GPPO \[字幕疑误，可能指 PPO\]、GRPO 方法背后的想法，它们是最先进的方法。所有这些都基于策略优化（policy optimization）的想法，对吧？你有 Q，也就是提示；策略模型是语言模型；你会从语言模型中采样一批回复，一组回复，这就是 gpo \[字幕疑误，可能指 GRPO\] 中的 group 超参数（hyperparameter）。对于每个回复，模型会经过一个奖励模型，预测奖励 R1 到 RG，假设有 G 个奖励。这个参考模型（reference model），我会稍微讲一点，它对应的是 pol 中的 P \[字幕疑误，pol 可能指 PPO\]，代表近端策略优化（proximal policy optimization）。Policy optimization 就是

### [1:03:47](https://www.youtube.com/watch?v=Vhe_bX8mV2s&t=3827s) · b000077

**English**

that we discussed the proximal term is basically you think of the reference model as a copy of the model's parameters in the previous step. And this KL basically means I don't want the new update to the model to be too different from the weights of the previous model. So I'm going to add a KL term between the new model and a frozen copy of the model from the previous step. So it doesn't change too much, right? We've already pre-trained a very good model. These things should only just be fine-tuning the model a little bit instead of changing the model too much. So that's a reference model and a KL. So a bunch of rewards. The bunch of rewards are used to estimate these A's. These A's are what we call advantages which I covered over here. Um as I emphasize sometimes the raw rewards aren't very useful right because the raw rewards themselves can

**中文**

我们讨论过的算法，而 proximal 这一项，基本上可以把参考模型理解为模型在上一步的参数副本。这个 KL 基本上意味着，我不希望模型的新更新与前一个模型的权重差异太大。所以，我会在新模型和上一步模型的冻结副本之间，加一个 KL 项，让它不要变化太大，对吧？我们已经预训练了一个非常好的模型，这些操作应该只是稍微微调模型，而不是让模型变化太多。这就是参考模型和 KL。然后有一组奖励，这组奖励用来估计这些 A。这些 A 就是我们所说的优势（advantages），我在这里讲过。嗯，正如我强调的，有时原始奖励并不是很有用，对吧？因为原始奖励本身可能

### [1:04:43](https://www.youtube.com/watch?v=Vhe_bX8mV2s&t=3883s) · b000078

**English**

always be positive or can always be negative. So it always makes sense to subtract a baseline which is the exponential moving average of the rewards that you have seen over time. It's basically standardizing them to be zero mean and kind of variance variance around zero. So some people use the advantage to refer to the reward minus the exponential moving average tracking of the baseline reward.

**中文**

总是为正，也可能总是为负。所以，减去一个基线总是有道理的，这个基线就是随着时间看到的奖励的指数移动平均。这基本上是在将它们标准化为零均值，让方差、方差围绕零。因此，有些人用 advantage 来指奖励减去用指数移动平均跟踪的基线奖励。

### [1:05:14](https://www.youtube.com/watch?v=Vhe_bX8mV2s&t=3914s) · b000079

**English**

So there are those advantages and then the advantages are used to scale the log likelihoods and to update the policy model. Okay. So that's the uh that's GRP algorithm. Any question about this?

**中文**

所以，这些就是 advantages，然后用 advantages 来缩放对数似然，并更新策略模型。好。这就是 GRP 算法 \[字幕疑误，可能指 GRPO\]。关于这个有什么问题吗？

### [1:05:47](https://www.youtube.com/watch?v=Vhe_bX8mV2s&t=3947s) · b000080

**English**

uh just want to end with some some interesting quotes. Obviously when when when IB R1 came out everyone was losing their minds but uh people who have been doing RL for a long time came out and said yeah you know the reason why no one has tried GRPO before is uh we have in reinforce which is the algorithm the most simple version of the algorithm we derived right in reinforce you update the policy by subtracting a baseline right reward minus baseline which is typically the average reward from several trajectories to reduce the variance. Now in fact theory shows us that the ideal baseline is the total expected future reward from a state often called the value. I didn't get into this but you can read into it. Using a value function as the baseline is known as actor critic. PO is a stable version of that. So PO as we discussed P

**中文**

呃，最后想用几段有意思的引语来结束。显然，当 IB R1 \[字幕疑误，可能指 DeepSeek-R1\] 出来时，所有人都激动得不行，但长期从事 RL 的人站出来说，对，你知道，为什么以前没人尝试 GRPO？其实我们在 reinforce 中已经做过了。Reinforce 就是我们推导的那个算法的最简单版本，对吧？在 reinforce 中，你通过减去一个基线来更新策略，也就是奖励减去基线，基线通常是若干条轨迹的平均奖励，以降低方差（variance）。事实上，理论告诉我们，理想的基线是从某个状态出发的未来总期望奖励，通常称为价值（value）。我没有深入讲这个，但你们可以去读。使用价值函数（value function）作为基线，被称为 actor critic。PO \[字幕疑误，可能指 PPO\] 是它的一个稳定版本。所以，正如我们讨论的，PO，P

### [1:06:43](https://www.youtube.com/watch?v=Vhe_bX8mV2s&t=4003s) · b000081

**English**

proximal policy optimization proximal is the one that has the KL term. So the model update doesn't differ too much from the previous frozen copy of the model weights. So in traditional reinforce the baseline can be any function of the current state and traditionally it's just a reward for the trajectories in a single batch. Right? So that's the baseline rewards across your batch. In GRPO this baseline is computed over thousand samples generated for each prompt which is novel. So a lot of it is um these kind of age-old ideas that have been around in in reinforcement learning that uh nowadays apply to language models which is nice, right? Which means that you know all of these thousands and thousands of papers uh building upon these RL reasoning or usually minor modifications from the traditional RL literature. um which is kind of one way

**中文**

，proximal policy optimization，proximal 就是带有 KL 项的那部分，让模型更新后与前一个冻结的模型权重副本不会相差太多。所以，在传统 reinforce 中，基线可以是当前状态的任意函数，而传统上它只是单个批次（batch）中轨迹的奖励，对吧？也就是整个 batch 的基线奖励。在 GRPO 中，这个基线是基于为每个提示生成的一千个样本计算的，这是新颖之处。所以，其中很大一部分，是强化学习中已经存在很久的老想法，如今被应用到了语言模型上，这很好，对吧？这意味着，那些成千上万篇基于 RL 推理的论文，通常只是对传统 RL 文献的小幅修改。嗯，这算是某种

### [1:07:41](https://www.youtube.com/watch?v=Vhe_bX8mV2s&t=4061s) · b000082

**English**

of cable climbing the research.

**中文**

对研究进行 cable climbing 的方式 \[字幕疑误，原意不明\]。

### [1:07:53](https://www.youtube.com/watch?v=Vhe_bX8mV2s&t=4073s) · b000083

**English**

Okay, let me go into some application. Um there was a feedback there was some feedback of maybe a lectur at some points being a bit too algorithmic and wanting to see more applications. So show you one example of how we have been recently applying this um you know GRPO and using RL to train multimodal LLMs to train a clinical reasoning foundation model. So ideally what we wanted you know we started out to do this project what we wanted the model to do was to synthesize all of this medical data. So as uh we remember Dimmitri pointed out right there's you know sensors like ECG medical sensors there's all sorts of images all sorts of text historical patient and doctor conversations and clinical records and nowadays with the

**中文**

好，让我讲一些应用。嗯，有一些反馈说，课程在某些地方可能有点过于偏重算法，希望看到更多应用。所以，给你们看一个例子：我们最近如何应用 GRPO，以及如何用 RL 训练多模态 LLMs，来训练一个临床推理基础模型（clinical reasoning foundation model）。理想情况下，当我们开始做这个项目时，希望模型做到的是综合所有这些医疗数据。正如我们记得 Dimmitri 指出的那样，对吧？有心电图（electrocardiogram, ECG）这样的传感器、医疗传感器，有各种图像、各种文本、历史上的患者与医生对话，以及临床记录。如今，凭借这些

### [1:08:49](https://www.youtube.com/watch?v=Vhe_bX8mV2s&t=4129s) · b000084

**English**

power of these uh these models you can not just make a prediction about the disease but you can also do things like have the model explain right in reasoning why it is this disease and rule out disability diseases and to uh explain that here are some ways of you know treating or diagnosing the patient. You can also have the model highlight regions. So now it's reasoning not just in text but also reasoning in vision. So for example highlighting some part of the X-ray or highlighting some part of the pathology, right? With small bounding boxes showing the tumor, right? This can help doctors verify the presence of maybe a a tumor. Um and it can also help you know converse with the doctor and patient to do diagnosis. So that's what we wanted the model to do. The base model nothing really special. Text can go through directly into the tokenizer. Vision can be encoded using a vision encoder and then

**中文**

模型的能力，你不仅可以预测疾病，还可以做诸如让模型解释的事情，对吧？通过推理说明为什么是这种疾病，排除 disability diseases \[字幕疑误，可能指其他候选疾病\]，并解释这里有哪些治疗或诊断患者的方法。你也可以让模型高亮某些区域。现在，它不仅在文本中推理，也在视觉中推理。例如，高亮 X-ray 的某一部分，或者病理图像的某一部分，对吧？用小边界框展示肿瘤，对吧？这可以帮助医生核实是否存在某个肿瘤。嗯，它还可以帮助与医生和患者对话，进行诊断。这就是我们希望模型做的事情。基础模型没什么特别的，文本可以直接进入分词器（tokenizer），视觉可以用视觉编码器（vision encoder）编码，然后

### [1:09:45](https://www.youtube.com/watch?v=Vhe_bX8mV2s&t=4185s) · b000085

**English**

adapted using a projection layer into the model. And likewise for any of your time series and sensing data that can go through some encoder and then get projected using an adapter into your uh LLM. Right? So the this multimodal LLM is the backbone. So several things first of all where we get the data and how do we use RL to train this multimodal model. uh data wise my my student David did a lot of hard work in curating some extremely large data sets I think I covered this in the first second week of class as we're going through data sets but this is a huge multimodal clinical data set covering all the modalities that I showed previously uh in all sorts of uh conditions clinical conditions uh but one important key note is that it has the input modalities right sensing

**中文**

通过一个投影层（projection layer）适配到模型中。同样，你的任何时间序列（time series）和传感数据，都可以通过某个编码器，再使用适配器（adapter）投影到 LLM 中，对吧？所以，这个多模态 LLM 是骨干（backbone）。有几件事，首先我们从哪里获取数据，以及如何用 RL 训练这个多模态模型。呃，数据方面，我的学生 David 做了大量辛苦工作，整理了一些规模极大的数据集。我想在课程第一、第二周讲数据集时已经介绍过。但这是一个巨大的多模态临床数据集，覆盖了我之前展示的所有模态，以及各种临床状况。不过，一个重要的注意点是，它有输入模态，对吧？传感

### [1:10:42](https://www.youtube.com/watch?v=Vhe_bX8mV2s&t=4242s) · b000086

**English**

steps and imaging and it has the final diagnosis. So whether the person has COVID or pneumonia or cancer uh but it doesn't have a reason doesn't have the step-by-step reasoning. So that's why you want to train a model to output. So how we train a model? First part was you know some stuff you had to do which was the multimodal training. In this case time series was causing us some problems. So we had to fine-tune these time series encoders to get them to be better and then inject them into the other lens using some adapter. And then the second part which is the key that I'll focus on was how we train this model for reasoning. So as we discussed in reasoning the big step is to define the rewards define both reward functions because you only have the input and the output. you don't have these

**中文**

steps \[字幕疑误，可能指数据\] 和影像，也有最终诊断，比如这个人是否患有 COVID、肺炎或癌症，但它没有理由，没有逐步推理。因此，这就是你希望训练模型输出的东西。那么我们如何训练模型？第一部分是一些必须做的工作，也就是多模态训练。在这里，时间序列给我们带来了一些问题，所以我们必须微调这些时间序列编码器，让它们变得更好，然后用某个 adapter 把它们注入 other lens \[字幕疑误，可能指 LLMs\]。第二部分，也是我将重点讲的关键部分，是我们如何训练这个模型进行推理。正如我们讨论的，在推理中，重要的一步是定义奖励，定义两个奖励函数，因为你只有输入和输出，没有这些

### [1:11:38](https://www.youtube.com/watch?v=Vhe_bX8mV2s&t=4298s) · b000087

**English**

intermediate reasoning places. How you end up incentivizing a model to get the reasoning out is to you find good reward functions. So the reward function should be high for good reasoning examples and the reward function should be low for bad reasoning examples. Right? Then when you start using RL, the model would maximize the reward and ideally give out good reasoning examples corresponding to high reward. So there were some rewards that we're building upon and some uh new rewards that we um we also developed. One reward that is very common is the accuracy of the alpha. Right? So the model is going to reason and then upput the answer. You have the label for the answer. Right? In this case the answer is like tumor or no tumor. So obviously the model should get the answer correct. The model get the answer wrong. It's probably reasoning was wrong. So the accuracy reward is just one if the final answer was correct and zero if the model got the answer

**中文**

中间推理 places \[字幕疑误，可能指 traces\]。你最终如何激励模型给出推理？就是找到好的奖励函数。奖励函数应该对好的推理示例给高分，对差的推理示例给低分，对吧？然后，当你开始使用 RL 时，模型会最大化奖励，理想情况下会给出与高奖励对应的良好推理示例。所以，我们沿用了一些奖励，也开发了一些新的奖励。一种很常见的奖励是 alpha 的准确性 \[字幕疑误，alpha 可能指 output\]。对吧？模型会先推理，再输出答案。你有答案的标签，对吧？在这里，答案比如是有肿瘤或没有肿瘤。所以，显然模型应该答对。如果模型答错了，它的推理很可能也错了。因此，准确性奖励（accuracy reward）很简单：最终答案正确就是一，如果模型答

### [1:12:34](https://www.youtube.com/watch?v=Vhe_bX8mV2s&t=4354s) · b000088

**English**

wrong. Pretty simple. Uh because we are working in the multimodal setting, we also define a semantic alignment reward. So the model will be outputting some text description of the reasoning and also sporadically pointing to the image via some bounding box. So you want a semantic alignment between the reasoning in text and the visual bounding box that the model was highlighting. Right? So this can be measured as the um uh IOU intersection over union between the ground truth uh segmented part of the image and where the model predicted the bounding box to be uh inside the image. So you can think about this as a as a visual reward incentivized visual reason. And then another reward that we had was length. So sometimes you want these models to uh to actually say something like pretty at a length that was useful. So we gave the reward of up to one of

**中文**

错了就是零。很简单。呃，因为我们在多模态场景下工作，所以还定义了语义对齐奖励（semantic alignment reward）。模型会输出一些描述推理的文本，也会不时通过某个边界框指向图像。因此，你希望文本推理与模型高亮的视觉边界框之间存在语义对齐，对吧？这可以用 IOU，也就是交并比（intersection over union）来衡量：图像中真值分割区域，与模型在图像中预测的边界框位置之间的 IOU。你可以把它看作一种视觉奖励，用来激励视觉推理。我们还有另一个奖励，就是长度（length）。有时你希望这些模型确实说一些内容，达到有用的长度。所以，我们给予最高为一的奖励，如果

### [1:13:32](https://www.youtube.com/watch?v=Vhe_bX8mV2s&t=4412s) · b000089

**English**

the models reasoning is at least 100 tokens uh but no more if it's longer, right? So you don't want the model to um give too long reasoning as well. And a bunch of people really play around with this. A lot of people study how do you incentivize the model to reason at the right number of steps and not too long or not too short. Bunch of work gone into designing those rewards. And finally we scaled each of these 0.6 for the accuracy reward 2 for the visual uh bounding box reward and 2 for the length reward.

**中文**

模型的推理至少有 100 个 tokens；但如果更长，就不再增加奖励，对吧？你也不希望模型给出太长的推理。很多人确实会反复尝试这一点，研究如何激励模型用恰当数量的步骤推理，不太长，也不太短。大量工作都在设计这些奖励。最后，我们对每项进行缩放：准确性奖励乘以 0.6，视觉边界框奖励乘以 2，长度奖励乘以 2。

### [1:14:14](https://www.youtube.com/watch?v=Vhe_bX8mV2s&t=4454s) · b000090

**English**

&gt;&gt; \[clears throat\]&gt;&gt; So yes, so then we trained it and there's some other minor details in the paper which I don't get into but you can see what the model is able to output. So it's able to take an image and so only this and the answer like you know past tumor is given to the model for training right all of this is automatically inferred as reasoning by the model. So the model is able to say well first the model is able to draw the bounding box around the tumor and then also explain that the tumor appears as a round or well circumscribed lesion. Tumors are often characterized as having these these boundaries which are distinct from the surrounding brain tissue. So the model is able to do all this explanation and also highlight the part of the X-ray which is very suspicious. So that's good. Here's another example. Uh now the model is taking in both X-ray and I think

**中文**

&gt;&gt; \[清嗓子\] &gt;&gt; 所以，对，然后我们训练了它，论文里还有一些其他小细节，我就不讲了，但你们可以看到模型能够输出什么。它能够接收一张图像，训练时给模型的只有这个和答案，比如 past tumor \[字幕疑误，可能指 has tumor\]，对吧？所有这些都是模型自动推断出来的推理。所以，模型能够说，好，首先它能在肿瘤周围画出边界框，然后解释肿瘤表现为圆形或边界清晰的病灶。肿瘤的特征通常是具有这些、这些与周围脑组织明确区分的边界。所以，模型能够做所有这些解释，也能高亮 X-ray 中非常可疑的部分。这很好。这里还有一个例子。呃，现在模型同时接收 X-ray 和，我想，

### [1:15:11](https://www.youtube.com/watch?v=Vhe_bX8mV2s&t=4511s) · b000091

**English**

these are some of these ICU sensing readings and a model is able to identify that the patient has been on mechanical ventilation for 96 hours. It's able to infer that from from some of the time series readings very surprising uh which is a quite long condition indicating a complex respiratory condition. The ECG and other lab results do not show any immediate critical issue. So now it's reasoning over the ECG data but the patient's hemot hemotric and hemoglobin levels are low which could be a sign of anemia or other underlying conditions requiring treatment and so on. So and then finally the model gets the right answer which is that the patient has to stay in the ICU for more than 12 days. So all of this reasoning over for example some of the medical history and some of these ECG and lab

**中文**

这些是一些重症监护病房（Intensive Care Unit, ICU）的传感读数，模型能够识别出患者已经接受机械通气（mechanical ventilation）96 小时。它能从某些时间序列读数中推断出这一点，非常令人惊讶。这个时间相当长，表明存在复杂的呼吸系统状况。ECG 和其他实验室检查结果没有显示任何需要立即处理的危急问题。所以，它现在正在对 ECG 数据进行推理。不过，患者的 hemot hemotric \[字幕疑误，可能指 hematocrit，血细胞比容\] 和血红蛋白（hemoglobin）水平较低，这可能是贫血或其他需要治疗的潜在病症的征兆，等等。最后，模型得到了正确答案：患者必须在 ICU 住超过 12 天。所以，所有这些针对例如某些病史、这些 ECG 和实验室

### [1:16:05](https://www.youtube.com/watch?v=Vhe_bX8mV2s&t=4565s) · b000092

**English**

values and also highlighting the the the X-ray was done by the model.

**中文**

数值的推理，以及对 X-ray 的高亮标注，都是由模型完成的。

### [1:16:15](https://www.youtube.com/watch?v=Vhe_bX8mV2s&t=4575s) · b000093

**English**

All right we are out of time. Uh but yes summary is you know we started looking at reasoning we looked at different dimensions of reasoning you know about this multi-step problem each with intermediate levels of evidence how you combine it over multiple steps solve harder problems probably the biggest frontier in AI nowadays so very important to know about um and then we started you know obviously we we said this prompt based approaches to reasoning which don't involve any training if you have the reasoning example You can do supervised fine-tuning, but often times you only have the input and the answer and you don't have all this reasoning. So reinforcement learning is a way of incentivizing the model to output all this reason. And the biggest things to do with practice are to define reward functions. Maybe some examples, right? Maybe getting the answer correct, you know, having some keywords correct. Uh

**中文**

好，我们时间到了。呃，不过，做个总结：我们开始研究推理，考察了推理的不同维度，也就是这个多步骤问题，每一步都有中间层次的证据，以及如何跨多个步骤把它们组合起来，解决更难的问题。这大概是当今 AI 最大的前沿，所以非常值得了解。然后，我们开始，显然我们说过这些基于提示的推理方法，它们不涉及任何训练。如果你有推理示例，就可以做监督微调。但很多时候你只有输入和答案，并没有这些推理。所以，强化学习是一种激励模型输出所有这些推理的方法。而实践中最重要的事情，是定义奖励函数。也许举几个例子，对吧？比如答案正确，或者某些关键词正确。呃，

### [1:17:13](https://www.youtube.com/watch?v=Vhe_bX8mV2s&t=4633s) · b000094

**English**

people really like to play with the length of these models. So defining reward functions and then you can just plug into some of these existing RL algorithms um which we covered. They're all called policy. The PO and all of these XXPO algorithms are called policy optimization algorithms. Right.

**中文**

人们确实喜欢调整这些模型的长度。所以，定义奖励函数，然后就可以接入我们讲过的一些现有 RL 算法。它们都叫 policy。PO 和所有这些 XXPO 算法，都叫策略优化算法（policy optimization algorithms）。对。
