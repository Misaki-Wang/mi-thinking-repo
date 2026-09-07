# Lecture 2 – Multimodal Research Tasks (MIT How to AI Almost Anything/Multimodal AI, Spring 2026)

_Bilingual transcript · 双语讲稿_

- Channel: Paul Liang
- Source: [YouTube](https://www.youtube.com/watch?v=zlTCAER4z9A)
- Duration: 1:16:36
- Caption source: automatic
- Status: complete
- Chinese translation: 87/87
- Translation provider: codex
- Generated: 2026-09-07T07:36:33+00:00

## Transcript · 讲稿

### [00:00](https://www.youtube.com/watch?v=zlTCAER4z9A&t=0s) · b000001

**English**

All right, folks. Let's get started.

**中文**

好了，各位。我们开始吧。

### [00:12](https://www.youtube.com/watch?v=zlTCAER4z9A&t=12s) · b000002

**English**

Okay, so welcome back. This is lecture 1.2 and today we'll be discussing important research tasks and data sets in multimodal AI. Uh the goal of this lecture is to do several things. uh most of this is meant to prepare you for the course project and the homeworks and the course projects are the main components for this class. So we'll start by discussing in my opinion the main components of AI research. How is good research done? How is it evaluated and how can we learn to become better AI researchers. I'll then give concrete examples of multimodal tasks and data sets that are really common today. probably you'll pick something for your course project and from your homeworks from one of the list of the multimodal tasks and data sets that we present today but you also not limited to the ones that we present right you just want to get the idea and you can find other data sets of similar nature I'll then

**中文**

好，欢迎回来。这是第 1.2 讲，今天我们将讨论多模态人工智能（multimodal AI）中的重要研究任务和数据集（data sets）。呃，这节课有几个目标。呃，这些内容大多是为了帮助大家准备课程项目和作业，课程项目是这门课的主要组成部分。所以，我们首先会讨论我认为 AI 研究的主要组成部分。好的研究是如何开展的？如何评价研究？我们又如何学习成为更好的 AI 研究者？然后，我会给出当今非常常见的多模态任务和数据集的具体例子。你们可能会从我们今天介绍的多模态任务和数据集列表中，为课程项目和作业选择一些内容，但也不限于我们介绍的这些，对吧？主要是让大家了解思路，你们可以寻找其他性质类似的数据集。然后我会

### [01:08](https://www.youtube.com/watch?v=zlTCAER4z9A&t=68s) · b000003

**English**

give some advice on research projects as you start thinking about what you want to do during the semester and finally we'll save some time at the end where you mingle with other people in the class and try to find teammates of common interests I also make uh two quick announcements. First of all, Canvas should be set up and published pretty soon. There was some uh logistical confusions because there's two versions of the course. One with MAS numbers and one with core six numbers. So half the students are in one canvas and half the students are in some other canvas. So we're trying to get that uh figured out and once Canvas is published, we are going to release all the lecture slides uh and lecture recorded lecture videos. I'm recording some of these on Zoom uh for people who miss the class. Uh but that doesn't mean you shouldn't come to class. Uh hoping everyone still come to class and learn live instead of staying home and watching lecture videos. Uh there will

**中文**

在大家开始思考这学期想做什么时，提供一些关于研究项目的建议。最后，我们会在结尾留出一些时间，让大家和班里的其他同学交流，尝试寻找兴趣相投的队友。我还要简单宣布两件事。首先，Canvas 应该很快就会设置好并发布。因为这门课有两个版本，一个使用 MAS 课程编号，另一个使用 core six 课程编号 \[字幕疑误，可能指 Course 6\]，所以在事务安排上出现了一些混乱。于是，一半学生在一个 Canvas 里，另一半学生在另一个 Canvas 里。我们正在设法解决，等 Canvas 发布后，就会放出所有讲义幻灯片和课堂录制视频。我正在用 Zoom 录制其中一些课程，供缺课的人观看。但这并不意味着你们就不该来上课。希望大家仍然来课堂现场学习，而不是待在家里看课程视频。呃，会有

### [01:57](https://www.youtube.com/watch?v=zlTCAER4z9A&t=117s) · b000004

**English**

be uh questions in which students can get bonus points if people come to class and answer these questions correctly. So that's the first announcement. Uh second announcement is that uh we'll also be putting up these project preferences form later this week. There'll be a form where people can sign up, tell us about who you are, your department, uh your background, what data sets you're most interested in, and that could be used to uh that'll be then shared with everybody in your class so you can find people with common interests to group together and do projects. Okay, so first up, just some basic introduction to AI research. Uh I like to think about AI research as any other research in science following the scientific process. Usually you start with some initial observations and ideas about the world. Given these initial observations and ideas and intuitions, a big step is doing literature review. Right? Then the project proposal is meant to really

**中文**

一些问题，如果同学们来上课并且回答正确，就能获得加分。这是第一件事。第二件事是，我们也会在本周晚些时候发布项目意向表。大家可以填写表格，告诉我们你是谁、所在院系、背景，以及最感兴趣的数据集。这些信息可以用来，呃，之后会分享给班里的所有人，方便大家找到兴趣相同的人组队做项目。好，首先简单介绍一下 AI 研究。我倾向于把 AI 研究看作与其他科学研究一样，遵循科学过程。通常，你会从对世界的一些初步观察和想法开始。有了这些初步观察、想法和直觉，一个重要步骤就是文献综述（literature review），对吧？项目提案的目的，就是切实

### [02:52](https://www.youtube.com/watch?v=zlTCAER4z9A&t=172s) · b000005

**English**

guide you towards forming these initial ideas and doing a comprehensive literature review. That constitutes learning about what is state-of-the-art in that field and what are the limitations in current state-of-the-art. Given that given your initial ideas and your lid review, usually you'll come up with several research questions, a hypothesis. Research questions are questions that you like to answer and hypotheses are potential answers to those questions. And we'll give some examples of different research questions and hypothesis later in the lecture. So given these questions and your intuitions and what the answers to those questions might be, the majority of the work is testing out with experiments the answers to those research questions. So that might involve usually implementing models, running these models on data sets, analyzing the results of propuse by the model and repeating that multiple times. Right? So testing with the experiments, analyzing your data. Once

**中文**

引导你们形成这些初步想法，并开展全面的文献综述。这包括了解该领域当前最先进的水平（state-of-the-art），以及当前 state-of-the-art 的局限。基于这些，基于你最初的想法和 lid review \[字幕疑误，可能指 literature review\]，通常你会提出几个研究问题（research questions），一个假设（hypothesis）。研究问题是你想回答的问题，假设则是这些问题的潜在答案。我们会在这节课后面给出不同研究问题和假设的例子。有了这些问题、你的直觉，以及对这些问题可能答案的想法，大部分工作就是通过实验检验这些研究问题的答案。这通常涉及实现模型、在数据集上运行这些模型、分析模型的 propuse 结果 \[字幕疑误，可能指模型产生的结果\]，并反复进行多次，对吧？所以，通过实验进行检验，分析你的数据。一旦

### [03:48](https://www.youtube.com/watch?v=zlTCAER4z9A&t=228s) · b000006

**English**

you've done that enough, you're satisfied with the results that you obtain either confirming or invalidating your research questions, uh then you report your conclusions and write up a paper. So that's a general uh general sequence of the scientific method. So as I mentioned, initial observations and ideas and literature review is what we're going to encourage everyone to do during the proposal. Forming research questions, hypothesis, and doing initial experiments with current models is what you're going to be tasked to do for the midterm report. and coming up with new methods, new experiments, and pushing beyond the state-of-the-art and reporting your conclusions is what you're supposed to do for the final report. So, we're going to guide you through this uh this whole process. So, perhaps the biggest question in research is how to come up with good research ideas, right? And I think there's two general ways of doing that.

**中文**

你做得足够多，对得到的结果感到满意，无论结果是证实还是否定了你的研究问题，接着就报告结论，写成论文。这就是科学方法的一般顺序。正如我提到的，初步观察、想法和文献综述，是我们鼓励大家在提案阶段做的事情。形成研究问题、假设，并用现有模型开展初步实验，是期中报告要求你们做的事情。提出新方法、新实验，超越 state-of-the-art，并报告结论，则是期末报告要求你们做的事情。我们会引导大家走完整个过程。那么，研究中最大的问题，可能就是如何想出好的研究点子，对吧？我认为大体有两种方式。

### [04:43](https://www.youtube.com/watch?v=zlTCAER4z9A&t=283s) · b000007

**English**

The first way is what we call bottomup discovery. Bottom-up discovery means you take a look at what is currently being done in the field. Figure out what models are good at doing and what models are bad at doing and try to fix model shortcomings on a specific data set or application that you care about. This is called bottom up, right? You start with data, you start with observations that other people have made and you're slowly building up and trying to improve the state-of-the-art. This is perhaps a safer approach, right? It's always very clear what current model limitations are. There's always a lack of application to some new domain or new application that you care about. So this a more safe approach and you're always kind of at least guaranteed with enough effort to push for the state-of-the-art. Uh but sometimes it can tend to be more incremental. Can be incremental because it only pushes the state-of-the-art uh slightly by addressing one small limitation or by

**中文**

第一种方式是我们所说的自下而上的发现（bottom-up discovery）。Bottom-up discovery 意味着，你先看看这个领域目前正在做什么，弄清楚模型擅长什么、不擅长什么，然后尝试在你关心的某个数据集或应用上修复模型的不足。这就叫自下而上，对吧？从数据出发，从其他人已经做出的观察出发，逐步积累，尝试提升 state-of-the-art。这可能是一种更稳妥的方法，对吧？当前模型的局限总是很明确。总有某个你关心的新领域或新应用，还缺少相应的应用研究。因此，这是一种更稳妥的方法，只要投入足够努力，至少总能在某种程度上保证推进 state-of-the-art。但有时候，它可能更偏向渐进式改进。之所以说是渐进式，是因为它只是通过解决一个小局限，或者通过

### [05:36](https://www.youtube.com/watch?v=zlTCAER4z9A&t=336s) · b000008

**English**

applying it to some new domain. This sometimes could pre preclude larger leaps in research. Uh but it's more safe. On the other hand, in a on contrast to bottom up discovery is this idea of top-down research where you start with perhaps bigger ideas, bigger hypotheses, bigger visions of where the field might be moving towards without really looking too much at what people are doing today and what the limitations are. So looking at bigger visions for the field and using that as a top- down identification of research progress towards that vision. This naturally favors bigger ideas, right? You start with a bigger vision and then you break it down into achievable manageable steps. Favors bigger ideas. Uh but sometimes it can be disconnected from reality. If people don't care about your vision, then they won't care about the individual steps that you use to achieve that vision. And of course it can be more risky, right? It's not often clear that the biggest

**中文**

将其应用到某个新领域，略微推进 state-of-the-art。这有时可能妨碍研究取得更大的飞跃。但它更稳妥。另一方面，与 bottom-up discovery 相对的是自上而下的研究（top-down research）：你可能从更大的想法、更大的假设、更宏大的领域发展愿景出发，而不太关注人们今天正在做什么，以及现有局限是什么。也就是着眼于领域的更大愿景，以此自上而下地确定朝着这个愿景推进的研究方向。这自然更有利于产生宏大的想法，对吧？你从一个更大的愿景出发，再将它拆解为可以实现、可以管理的步骤。有利于更大的想法。但有时候，它可能脱离现实。如果人们不在意你的愿景，他们也就不会在意你为实现愿景采取的各个步骤。当然，它也可能更有风险，对吧？通常并不清楚，最大的

### [06:33](https://www.youtube.com/watch?v=zlTCAER4z9A&t=393s) · b000009

**English**

visions are the ones that would fan out in in the in the process. So, we're going to do both in a class, right? Firstly, we're going to encourage and enable you to do bottomup discovery uh usually through several means. First of all, in your proposal report, your goal is to identify existing methods that are currently state-of-the-art. And from that literature review, you should have identified key limitations in a state-of-the-art. So that's really the first step towards bottomup discovery. Secondly, the homeworks and the midterm assignment will further enable this bottomup study because as we discussed in the in the last lecture, the homeworks is all about implementing in a pretty guided fashion with you know structured code prepared by us implementing the current state of the art. For example, just implementing whatever is a state-of-the-art supervised learning method or implementing language models on your data or implementing, you know, existing

**中文**

愿景是否就是那些会在过程中 fan out 的愿景 \[字幕疑误，可能指 pan out，即最终取得成功\]。所以，我们会在课上同时做这两种，对吧？首先，我们会鼓励并帮助你们开展 bottom-up discovery，通常通过几种方式。第一，在提案报告中，你的目标是识别当前处于 state-of-the-art 的现有方法。通过文献综述，你应该已经识别出现有 state-of-the-art 的关键局限。这就是迈向 bottom-up discovery 的第一步。第二，作业和期中任务会进一步支持这种自下而上的研究。因为正如上节课讨论的，作业主要是在相当明确的指导下，使用我们准备好的结构化代码，实现当前的 state-of-the-art。例如，直接实现当前最先进的监督学习（supervised learning）方法，或者在你的数据上实现语言模型（language models），或者实现，你知道，现有的

### [07:27](https://www.youtube.com/watch?v=zlTCAER4z9A&t=447s) · b000010

**English**

reasoning LLM reasoning or a Gent models on your data. All of this is basically about implementing the current state-of-the-art. And likewise for your midterm assignment, you'll be also be implementing some other state-of-the-art that is more specialized for your research project beyond the generic five homework assignments that we present. So all of this is experimenting with state-of-the-art models meant to get you familiar and based on running these models also to get you a good understanding of where these current methods fail on your data set and application. Right? So once you start analyzing the successes and failures of these models, you are more prepared to identify ways in which you could improve upon them. Okay? And given that done in homeworks and your midterm, your final report should naturally propose ideas that do better. And these will evolve over the semester as you try out existing methods. Of course, we're not only going to do bottom-up discovery in the class. We're

**中文**

推理，大语言模型（LLM）推理，或者在你的数据上实现 a Gent 模型 \[字幕疑误，可能指 agent models\]。所有这些基本上都是在实现当前的 state-of-the-art。同样，期中任务也会让你实现一些其他的 state-of-the-art 方法，它们针对你的研究项目更为专门，超出我们提供的五次通用作业的范围。因此，所有这些都是用 state-of-the-art 模型开展实验，目的是让你熟悉它们，同时通过运行这些模型，充分了解当前方法在你的数据集和应用中会在哪些地方失败，对吧？所以，一旦开始分析这些模型的成功和失败，你就更有准备去找出改进它们的方法，好吗？完成作业和期中任务中的这些工作后，期末报告自然应该提出效果更好的想法。这些想法会随着你在整个学期里尝试现有方法而不断发展。当然，我们在课上不仅会做 bottom-up discovery。我们

### [08:20](https://www.youtube.com/watch?v=zlTCAER4z9A&t=500s) · b000011

**English**

also going to incentivize top- down brainstorming and top down visions. Uh these would usually come in a form of brainstorming. So, uh the TAs and I will have office hours that will that will publish on the course website and on Canvas. So we encourage you to meet with us this week and next week as you start brainstorming about maybe broader visions that you might have for your research uh in the literature review as well as you are scoping out specific ideas and specific methods that have been implemented uh you should also be encouraged to think about broader visions and trends of where the field is going and of course most of the stuff that I present in lectures are also a synthesis not just of individual papers but a synthesis of broader trends in this multimodal AI space. Okay, so that's a quick introduction of how to come up with research ideas through both bottom-up discovery and top down design or top down visions.

**中文**

也会鼓励自上而下的头脑风暴（top-down brainstorming）和自上而下的愿景。这些通常会以头脑风暴的形式出现。我和助教（TAs）会安排答疑时间，公布在课程网站和 Canvas 上。因此，我们鼓励大家这周和下周来找我们交流，开始围绕你们研究中可能拥有的更宏观愿景进行头脑风暴。在文献综述中，当你们界定具体想法、梳理已经实现的具体方法时，也应该思考更宏观的愿景和领域的发展趋势。当然，我在课上介绍的大部分内容，也不只是单篇论文的综合，而是对多模态 AI 领域更广泛趋势的综合。好，这就是对如何通过 bottom-up discovery 和自上而下的设计或愿景来产生研究想法的简要介绍。

### [09:18](https://www.youtube.com/watch?v=zlTCAER4z9A&t=558s) · b000012

**English**

I also want to explain a bit about research questions and hypothesis for these research questions. So research questions in general are one or several explicit questions regarding something that you want to find out. Uh usually these hypothesis uh research questions are easier to draft with yes no questions, right? Does X affect Y or is X an indicator of Y? These yes no questions are typically easier to answer, right? You can have a more direct answer with these questions. Your hypothesis is what you think the answer to the question will be a priority before you start running experiments. And again, these hypotheses should be falsifiable. There should be sufficient experiments. So at some point you can say yes this hypothesis is true and other experiments that you could run which you know at some point you'll be saying no this hypothesis is false. So research questions are usually well posed if they're yes no questions and again hypotheses are also well well

**中文**

我还想解释一下研究问题，以及针对这些研究问题的假设。一般来说，研究问题是围绕你想弄清楚的事情提出的一个或几个明确问题。通常，这些假设，呃，研究问题，更容易写成是非问题，对吧？X 是否影响 Y？或者 X 是否是 Y 的指标？这些是非问题通常更容易回答，对吧？你可以给出更直接的答案。你的假设，就是在开始运行实验之前，你 a priority 认为问题的答案会是什么 \[字幕疑误，可能指 a priori，即事先\]。再次强调，这些假设应该是可证伪的（falsifiable）。应该有足够的实验，使你在某个时候可以说，是的，这个假设成立；也应该有其他可以运行的实验，使你在某个时候会说，不，这个假设不成立。所以，如果研究问题是是非问题，通常就定义得比较清楚。同样，如果假设也

### [10:14](https://www.youtube.com/watch?v=zlTCAER4z9A&t=614s) · b000013

**English**

posed if they are either yes or no answers to these research questions. I want to give you some examples of both uh good and not so good research questions uh all from recent papers that I've written. So good papers and I think also critiques of research questions that I think ended up going into some of these papers. So here's one example. You can read this paragraph. I'll go briefly explain. In this case, we are looking at um this phenomena of aligning representations across data modalities. Right? So you might have some text or caption. You might some have some images that represent the same content uh in the text or caption. And traditionally people looked at explicitly aligning these together using things like similarity measures. So you bring the text embedding close to the image embedding. And some other people actually had this really surprising finding that even without explicitly forcing these embeddings to come together uh with sufficiently large

**中文**

是对这些研究问题给出肯定或否定的回答，它们通常也就定义得比较清楚。我想给大家举一些好的和不太好的研究问题，全部来自我最近写的论文。所以，有好的论文，也有我认为最终写进其中一些论文的研究问题值得批评之处。这里有一个例子。你们可以读一下这段话，我简单解释一下。在这个例子中，我们研究的是跨数据模态的表征对齐（representation alignment）现象，对吧？你可能有一些文本或图像描述（caption），也可能有一些图像，表达与文本或 caption 相同的内容。传统上，人们会使用相似度度量（similarity measures）等方法，显式地将它们对齐。也就是让文本嵌入（text embedding）靠近图像嵌入（image embedding）。另一些人实际上有一个非常令人惊讶的发现：即便不显式地强迫这些 embeddings 聚到一起，只要

### [11:11](https://www.youtube.com/watch?v=zlTCAER4z9A&t=671s) · b000014

**English**

models, the embeddings become automatically closer and closer together. So that's this distinction we're making here between explicitly aligning these representations using some similarity function versus how these models can become implicitly aligned as they get bigger in size and better in performance. That's a little bit of a context. I want to highlight uh specifically the research questions that we summarize here in the paper. Right? First we asked when and why does alignment emerge implicitly? Right? Okay, so that's an example of a research question and of course you might have some hypothesis when and why alignment emerges. Of course, when is a more precise research question because you can say it emerges perhaps when your model performance reaches a certain target or when your models become certain size and parameters or when there is some feature in the data that's when alignment emerges. So this when question is a better question that's more well posed with more clear

**中文**

模型足够大，这些 embeddings 就会自动越来越接近。因此，我们在这里区分的是：使用某种相似度函数显式对齐这些 representations，与模型随着规模增大、性能提升而产生隐式对齐（implicit alignment）。这是一点背景。我特别想强调我们在论文中总结的研究问题，对吧？首先，我们问，对齐何时以及为何会隐式出现？对吧？好，这就是一个研究问题的例子，当然，你可能会对 alignment 何时以及为何出现提出某些假设。当然，“何时”是一个更精确的研究问题，因为你可以说，它可能在模型性能达到某个目标时出现，或者在模型达到某种规模和参数量时出现，或者当数据中存在某种特征时，alignment 就会出现。因此，这个“何时”的问题更好，定义更清楚，也有更明确的

### [12:07](https://www.youtube.com/watch?v=zlTCAER4z9A&t=727s) · b000015

**English**

hypothesis. Why is perhaps not the best research question because it's much more open-ended and it's not really clear how to come up with a hypothesis that would validate or invalidate that question. The second question is perhaps even more precise. Is alignment a reliable indicator of performance? In this case, you can come up with hypothesis that would either confirm that yes, alignment directly correlates with better performance or no that alignment sometimes does not correlate or lead to worse performance. And you can directly run experiments to verify this, right? Having models with better alignment and seeing how these models perform and seeing the correlation between them. So these are perhaps good qu good examples of research questions with a very clear positioning and a very clear answer for them. Here are some examples of perhaps uh not so good research questions. And again, this is from a paper that our group

**中文**

假设。“为何”可能不是最好的研究问题，因为它更加开放，也不太清楚应该如何提出一个假设，来验证或否定这个问题。第二个问题可能更加精确：alignment 是否是性能的可靠指标？在这种情况下，你可以提出假设，证实是的，alignment 与更好的性能直接相关；或者不是，alignment 有时并不相关，或者会导致更差的性能。你也可以直接运行实验来验证，对吧？找 alignment 更好的模型，看看这些模型表现如何，再看两者的相关性。因此，这些可能是研究问题的好例子，定位非常明确，也有非常明确的答案。下面是一些可能不太好的研究问题。再次说明，这来自我们团队

### [13:03](https://www.youtube.com/watch?v=zlTCAER4z9A&t=783s) · b000016

**English**

recently put out. So, I can criticize my own work. Um, in this case, we're proposing a new method. It's called DRPO. Some of you might have heard of GRPO, which is a method that is state-of-the-art uh using reinforcement learning to train language models to reason. And we came up with this uh DRPO approach, which we hypothesized would be better in applying GRPO to multimodal data because multimodal data often has data from various different distributions. We found that GRPO overfits to one distribution and doesn't handle the others. The goal of this DRPO was to have a more balanced training across various different distributions. Uh so look at these questions. RQ1, how does DRPO compare with other critic free RL methods and models? So this is an okay research question, but it's perhaps not the best well posed, right? because there's a almost infinite possible answers and infinite possible hypothesis

**中文**

最近发表的一篇论文。所以，我可以批评自己的工作。在这个例子中，我们提出一种新方法，叫作 DRPO。你们有些人可能听说过 GRPO，这是一种使用强化学习（reinforcement learning）训练语言模型进行推理的 state-of-the-art 方法。我们提出了 DRPO 方法，假设它在将 GRPO 应用于多模态数据时效果会更好，因为多模态数据往往来自各种不同的分布。我们发现，GRPO 会过拟合（overfit）其中一个分布，无法处理其他分布。DRPO 的目标是在不同分布之间实现更均衡的训练。看看这些问题。RQ1：DRPO 与其他不使用 critic 的强化学习（critic free RL）方法和模型相比如何？这是一个还可以的研究问题，但可能不是定义得最清楚的，对吧？因为这个研究问题有近乎无穷多种可能的答案，以及无穷多种可能的假设

### [14:01](https://www.youtube.com/watch?v=zlTCAER4z9A&t=841s) · b000017

**English**

for this research question. It's not really posed as a yes no question which makes it easy to verify yes or no. Uh likewise for RQ2 how well does the rpo handle mixed multimodal inputs? It's again there's a infinite number of answers or infinite number of hypotheses for that question. It's not really clear how to answer it and it's not clear whether we can verify that we are successful at answering that question. So if I were to maybe rephrase RQ1, I would probably say something like you know is it true that DRPO performs or is it true that DRPO outperforms this other method when applied to you know heterogeneous data across different modalities. In this case, you could have a very specific context for the research question and also a very specific question you're trying to answer. Does it outperform or no?

**中文**

。它并没有被表述成一个易于验证是或否的是非问题。同样，RQ2：rpo \[字幕疑误，可能指 DRPO\] 处理混合多模态输入的效果如何？这个问题同样有无穷多个答案，或者无穷多个假设。并不清楚应该如何回答，也不清楚能否验证我们已经成功回答了它。所以，如果让我重新表述 RQ1，我可能会说，例如，DRPO 的表现是否，或者说，DRPO 在应用于跨不同模态的异构数据（heterogeneous data）时，是否优于另一种方法？这样，你就可以为研究问题提供非常具体的背景，也有一个非常具体的问题需要回答：它是否优于其他方法？

### [14:55](https://www.youtube.com/watch?v=zlTCAER4z9A&t=895s) · b000018

**English**

Great. So, anyways, uh we'll iterate with you through different research questions. It's time to start thinking about what they might be as you work on um identifying your data sets and identifying what you want to do for the project. Okay. So let me jump into the main content for today's lecture which is to give an overview of different multimodal data sets and tasks and the main research questions and challenges and the goal is to give you all this context so that you can eventually zoom into one or a few of them uh for the semester given the complimentarity to your own backgrounds. If you recall I showed this trend this historical perspectives of multimodal AI on Tuesday. We started with the behavioral studies of you know a effect and how people expressed uh emotions through audio and visual expressions. Uh so that was one key task in multimodal AI. Soon after with the birth of the internet we saw a huge boom of

**中文**

很好。总之，我们会和你们一起反复打磨不同的研究问题。当你们开始确定数据集，以及项目想做什么时，现在就该开始思考研究问题可能是什么。好，让我进入今天这节课的主要内容：概述不同的多模态数据集和任务，以及主要的研究问题与挑战。目标是提供这些背景，让你们最终能根据这些内容与你们自身背景的互补性，在这学期聚焦其中一个或几个。如果还记得，我周二展示过这个趋势，这个多模态 AI 的历史视角。我们从关于 a effect 的行为研究 \[字幕疑误，可能指 affect，即情感\]，以及人们如何通过声音和视觉表达情绪开始。这是多模态 AI 中的一项关键任务。随后，随着互联网诞生，我们看到了

### [15:52](https://www.youtube.com/watch?v=zlTCAER4z9A&t=952s) · b000019

**English**

multimedia data sets like text, videos, audio and naturally tasks to retrieve the right uh right video audio give it some query. And nowadays with deep learning starting the 2010s we've seen so many data sets on captioning images captioning videos nowadays going to even generating images and videos given text prompts. So we've already seen a good historical perspective of multimodal AI. I want to summarize uh the main data sets and tasks that I think are especially relevant today and especially relevant for for all of you groups of students into these key categories. Right? First one being new modalities and applications especially those beyond image and text because a lot of you here have some domain expertise and you're interested in playing with modalities beyond image and text. A second broad category is uh perhaps more core research. core research on designing

**中文**

文本、视频、音频等多媒体数据集的大幅增长，自然也产生了给定查询后检索正确视频、音频的任务。而从 2010 年代深度学习（deep learning）兴起至今，我们已经看到大量用于图像描述、视频描述的数据集，现在甚至发展到了根据文本提示（text prompts）生成图像和视频。所以，我们已经对多模态 AI 的历史有了一个较好的认识。我想将我认为在今天尤其相关、也尤其适合你们这些学生群体的主要数据集和任务，总结为这几个关键类别，对吧？第一个是新模态和新应用，尤其是图像与文本之外的模态，因为在座很多人有某些领域的专业知识，希望探索图像和文本之外的模态。第二大类可能是更核心的研究，关于设计

### [16:49](https://www.youtube.com/watch?v=zlTCAER4z9A&t=1009s) · b000020

**English**

better fusion alignment and foundation models for multimodal data. This because it's more core research is not going to be focused on a specific application but you then need to show performance on several data sets. Uh reasoning is another one. How do you go beyond just perceiving and identifying something in a modality but systems that can reason over multiple steps to solve harder questions? uh interactive agents is something that people are definitely excited about. AI systems that don't just make a prediction or answer a question, but can actually take actions in some closed loop autonomous environment. Socially intelligent AI is something that I'm especially interested in. Building systems that don't just understand the physical world, but really understand people, what people are thinking, feeling, and how to improve human lives and experiences. embody AI extending interactive agents to the real physical world. So things like robotics and finally it's also of

**中文**

更好的多模态数据融合（fusion）、对齐（alignment）和基础模型（foundation models）的核心研究。因为它更偏核心研究，所以不会聚焦某个具体应用，而是需要在多个数据集上展示性能。推理（reasoning）是另一类。如何超越仅仅感知和识别某个模态中的事物，构建能够通过多步推理解决更困难问题的系统？交互式智能体（interactive agents）无疑也是大家非常兴奋的方向。AI 系统不仅作出预测或回答问题，还能在某种闭环自主环境（closed loop autonomous environment）中实际采取行动。具有社会智能的 AI（socially intelligent AI）是我特别感兴趣的方向。构建不仅理解物理世界，而且真正理解人、理解人们的想法和感受，以及如何改善人类生活与体验的系统。embody AI \[字幕疑误，可能指 embodied AI，即具身 AI\] 则将 interactive agents 扩展到真实物理世界，比如机器人。最后，当然也

### [17:46](https://www.youtube.com/watch?v=zlTCAER4z9A&t=1066s) · b000021

**English**

course critical to do research projects in looking at not just building better AI systems but how they improve people's lives while maintaining ethics and safety. So here's a a broad grouping of the main data sets and tasks that I'll introduce today. At a high level, when I talk about these different data sets, I still want you to think about the key schematic, which is that these are in the end just different data modalities that can be seen as a combination of different elements. Right? Language is a sequence of words that a person is saying. Um vision is a sequence of you know objects or sequence of frames in a video. Sensor readings are just you know sensing uh time series basically sensor readings across time. So today these are just modalities that are very different in nature each of them segmented into different elements the main building blocks and the goal is to design AI systems that can learn

**中文**

至关重要的是，研究项目不仅要关注构建更好的 AI 系统，也要关注它们如何在维护伦理与安全的同时改善人们的生活。所以，这里是我今天将介绍的主要数据集和任务的大致分类。从宏观上看，当我讨论这些不同数据集时，仍然希望大家想着这个关键示意图：它们归根结底只是不同的数据模态，都可以看作不同元素的组合，对吧？语言是一个人说出的一串词。视觉是一系列物体，或者视频中的一系列帧。传感器读数基本上就是随时间变化的感测时间序列（time series），也就是跨时间的传感器读数。因此，今天这些模态在本质上非常不同，每一种都被分割成不同元素，也就是基本构建块，目标是设计能够学习

### [18:45](https://www.youtube.com/watch?v=zlTCAER4z9A&t=1125s) · b000022

**English**

representations combining the information with different modalities while accounting for their inherent heterogeneity and differences. After which these representations could be used to make some prediction. It could be used to generate more data. It could be used to take actions or it could be used to transfer from high resource to low resource settings. So I want you to again keep this schematic in mind as a common denomination across different multimodal data sets and tasks that we will present.

**中文**

结合不同模态信息的 representations，同时考虑其固有异质性（heterogeneity）和差异的 AI 系统。之后，这些 representations 可以用于作出某种预测，可以用于生成更多数据，可以用于采取行动，也可以用于从高资源场景迁移到低资源场景。因此，我希望大家再次记住这个示意图，把它看作我们将介绍的不同多模态数据集和任务的共同之处。

### [19:17](https://www.youtube.com/watch?v=zlTCAER4z9A&t=1157s) · b000023

**English**

Okay. So first up first theme that I think many people might be interested in would be research projects on new modalities. new modalities going beyond the common vision, language, audio, uh where we have tons of data that we already have really good foundation models and that's commonly available on the internet. Of course, the main motivation for going beyond these traditional so-called traditional digital modalities is that there's many ways of sensing the world, many ways of sensing the world, each with very complimentarity, very complimentary information, different privacy concerns, different invasiveness, and different efficiency trade-offs. So uh in terms of understanding people uh not only is it important to just use vision but sometimes people design physiological sensors like the rings the watches uh EEG sensors different ways of sensing physiological signals from people to understand the cities and environments around us oftent times is not just

**中文**

好，首先，我认为很多人可能感兴趣的第一个主题，是关于新模态的研究项目。新模态，也就是超越常见的视觉、语言、音频。在这些常见模态中，我们拥有海量数据，已经有非常好的 foundation models，而且数据在互联网上很常见。当然，超越这些传统的、所谓传统数字模态的主要动机是，感知世界有很多种方式，感知世界有很多种方式，各自带来非常互补、非常互补的信息，也有不同的隐私问题、不同的侵入性，以及不同的效率权衡。例如，在理解人方面，不仅仅使用视觉很重要，有时人们还会设计生理传感器，比如戒指、手表、脑电图（EEG）传感器，通过不同方式感测人的生理信号。要理解我们周围的城市和环境，往往仅仅

### [20:14](https://www.youtube.com/watch?v=zlTCAER4z9A&t=1214s) · b000024

**English**

enough to use vision but there's other types of sensing for example sensing of LAR and temperature and depth and efficiency and different other operations in the environment. So there's a ton of applications to things like cities, climate, environment and engineering. Um going beyond going beyond uh touch beyond our language to also other human senses for example looking at smell, looking at taste. People who are interested in creative domains have to look at art, music, tangible forms, other modalities. And often times this introduces one very key challenge which is that you're never going to have a lot of data in these new modalities as you would for internet scale modalities. So oftent times you might not have a lot of unimodal data in that domain and worse yet you probably won't have a lot of multimodal data right it's hard to find the pairings between this new domain with other modalities. So here are just some

**中文**

使用视觉还不够，还需要其他类型的感测，例如 LAR 感测 \[字幕疑误，可能指 LiDAR\]，以及温度、深度、效率和环境中其他各种运行情况的感测。因此，在城市、气候、环境和工程等方面有大量应用。嗯，超越，超越触觉，超越我们的语言，还可以涉及其他人类感官，比如嗅觉、味觉。对创意领域感兴趣的人，需要关注艺术、音乐、有形形式和其他模态。而这往往带来一个非常关键的挑战：这些新模态的数据量，永远不会像互联网规模的模态那么多。因此，你往往在这个领域没有很多单模态数据（unimodal data），更糟的是，你可能也没有很多多模态数据，对吧？很难找到这个新领域与其他模态之间的配对。所以，下面是一些

### [21:11](https://www.youtube.com/watch?v=zlTCAER4z9A&t=1271s) · b000025

**English**

examples of um good resources. People have been creating increasingly larger EEG data sets for people who are interested in brain sensing. Uh increasingly larger data sets for speech and face and gestures. Uh for those who are interested in understanding people and their expressions. Uh our group is doing some interesting work in touch. Touch is a modality especially important for building robots that can feel and interact in the physical environment. And nowadays of course people are building language models that go beyond language and can even understand things like wearable sensor and physiological sensors in the world. Let me highlight some data sets in this space that people might be interested in. So our group has been curating lots of these multimodal clinical data sets. Right? Health is a big domain where multimodal is super important. doctors all diagnose patients by by talking to them by uh prescribing them different

**中文**

优质资源的例子。对于对脑感测感兴趣的人，人们一直在构建规模越来越大的 EEG 数据集。对于对理解人及其表达方式感兴趣的人，也有越来越大的语音、人脸和手势数据集。我们团队正在触觉方面做一些有趣的工作。触觉是一种特别重要的模态，有助于构建能够感受物理环境并与之交互的机器人。当然，如今人们正在构建超越语言的语言模型，甚至能够理解世界中的可穿戴传感器和生理传感器之类的东西。让我重点介绍这个方向中一些大家可能感兴趣的数据集。我们团队一直在整理大量多模态临床数据集，对吧？医疗健康是多模态极其重要的一个大领域。医生诊断患者时，会与他们交谈，会为他们开具不同的

### [22:08](https://www.youtube.com/watch?v=zlTCAER4z9A&t=1328s) · b000026

**English**

tests that they have to undergo can be imaging can be um other sensing it can be other you know vital signs all of this constitutes a ton of modalities that are important for understanding a person's health and well-being so climb is a resource we put up uh open source and publicly available the links available over there which curates a ton of these open-source data sets in the healthare domain. This includes uh 1D data. So that's things like sensing, EEG sensing, physiological sensing, ICU sensing. So onedimensional data across time. It includes uh 2D data. So those are your static images. Two dimensions, height and width, things like X-ray, hisystologology, so under the microscope, pathology, other forms of imaging. Contains 3D data. So that's 2D images with a time dimension. So basically videos uh things like CT scans

**中文**

检查，这些检查可能是影像检查，可能是其他感测，也可能是其他生命体征。所有这些构成了大量模态，对于理解一个人的健康与福祉非常重要。因此，climb \[字幕疑误，可能指 CLIMB\] 是我们发布的一个开源、公开可用的资源，链接在那边。它整理了医疗健康领域大量的开源数据集。这包括 1D 数据，比如感测、EEG 感测、生理感测、重症监护室（ICU）感测，也就是随时间变化的一维数据。它也包括 2D 数据，也就是静态图像，两个维度，高和宽，比如 X-ray、hisystologology \[字幕疑误，可能指 histology，即组织学\]，也就是显微镜下的图像、病理图像，以及其他形式的影像。还包含 3D 数据，也就是带时间维度的 2D 图像，基本上是视频，比如计算机断层扫描（CT）

### [23:04](https://www.youtube.com/watch?v=zlTCAER4z9A&t=1384s) · b000027

**English**

and ultrasounds are 2D images across time and even graph data some some areas of health look at different proteins and genomes and you know brain networks all of this is graph structure data and finally for certain data sets we also have multimodal data. So for example pairings between text doctor reports and imaging that's collected from the patients. So it contains all of this multimodal data. It covers a lot of tasks for people who are interested in health. It probably contains all the tasks that you might be interested in things like COVID, pneumonia, cancer, um, uh, and more. It also more importantly comes from different regions. So, not everything is from the US area, but also from under reppresented areas, uh, from different hospitals, uh, from regions with very different diseases than the ones that we we see on a day-to-day basis. And so all of this is nicely packaged and you can load any of these data sets in a couple

**中文**

和超声，都是随时间变化的 2D 图像，甚至还有图数据（graph data）。某些医疗健康领域会研究不同的蛋白质、基因组，以及脑网络，这些都是图结构数据。最后，对于某些数据集，我们还有多模态数据。例如，医生文本报告与从患者处采集的影像之间的配对。因此，它包含所有这些多模态数据。对医疗健康感兴趣的人来说，它涵盖很多任务。它可能包含你感兴趣的所有任务，比如 COVID、肺炎、癌症，嗯，呃，以及更多。更重要的是，这些数据来自不同地区。所以，并非所有数据都来自美国，也来自代表性不足的地区，来自不同医院，来自疾病类型与我们日常见到的非常不同的地区。所有这些都经过很好的封装，你只需几

### [24:02](https://www.youtube.com/watch?v=zlTCAER4z9A&t=1442s) · b000028

**English**

of lines of code and already start playing and training multimodal models on them. So climb is an example of a data sets that people in AI and health might be interested in for their course projects and for their homeworks. Uh this mimic data set is one of the data sets included in climb. I want to give special recognition to this because it is one of the very few multimodal data sets for healthcare out there and it's extremely comprehensive. It contains notes for like radiology reports, discharge summaries, all that is in text. It includes uh various hospital information like lab tests and medications. Uh most of this is in a form of tabular data and also includes uh other ICU sensing information. Most of this comes in a form of time series data. for example, IV prescriptions, different observations on heart rate and blood pressure over time. All that comes in a form of time series data mostly text tabular and time series and some of

**中文**

行代码，就能加载其中任意一个数据集，开始探索，并在上面训练多模态模型。因此，climb 是 AI 和医疗健康领域的人可能会在课程项目和作业中感兴趣的一个数据集资源。这个 mimic 数据集 \[字幕疑误，可能指 MIMIC\] 是 climb 收录的数据集之一。我想特别介绍它，因为它是目前为数不多的医疗多模态数据集之一，而且极其全面。它包含放射学报告、出院小结等记录，这些都是文本。还包括化验和用药等各种医院信息，其中大部分以表格数据（tabular data）的形式存在，也包括其他 ICU 感测信息。其中大部分以 time series 数据的形式存在，例如静脉输注（IV）医嘱，以及心率、血压随时间变化的不同观测记录。所有这些都以 time series 数据形式出现，主要是文本、表格和 time series，其中一些

### [24:59](https://www.youtube.com/watch?v=zlTCAER4z9A&t=1499s) · b000029

**English**

it also includes things like imaging like check X-rays. So all this can come together and it's nicely annotated for uh diseases that a patient was diagnosed with and also length of stay and mortality rate in these patients. I'm quite excited about smell. Again, some shameless plug from our group. We created new data sets uh digitizing how various foods and substances smell in the world. Uh so these are these are sensing these are small sensing chips that essentially capture volatile gases. Uh things like your carbon monoxide, alcohol, ethanol, uh volatile gases that are released by different foods and beverages as you put them out in the environment. So these look like uh sensor readings over time and we have multiple of them right multiple gas sensor readings and also sensor readings like temperature, humidity and pressure and you can start playing with some of these data and see if you can train

**中文**

还包括影像，比如 check X-rays \[字幕疑误，可能指 chest X-rays，即胸部 X 光片\]。所有这些信息可以整合在一起，并且对患者确诊的疾病、住院时长和死亡率都有很好的标注。我对嗅觉非常兴奋。再次不害臊地宣传一下我们团队的工作。我们创建了新的数据集，将世界上各种食物和物质的气味数字化。这些是感测，这些是小型感测芯片，本质上捕获的是挥发性气体，例如一氧化碳、酒精、乙醇，以及将不同食物和饮料放到环境中时释放的挥发性气体。因此，这些看起来就是随时间变化的传感器读数，而且我们有多个，对吧？多个气体传感器读数，以及温度、湿度和压力等传感器读数。你们可以开始探索其中一些数据，看看能否训练

### [25:56](https://www.youtube.com/watch?v=zlTCAER4z9A&t=1556s) · b000030

**English**

these multimodal models to combine these sensor readings to make a prediction on the substance. Uh so this there's about 50 substances over here including different types of nuts, spices, herbs, fruits and vegetables. each has a sensor reading log multiple times so that you get multiple independent readings of those substances. So that can be really cool. You can start by detecting substances. You can also try to push the limits to detect mixtures of substances. You can also try to detect peanuts in different trace amounts and that can be useful for people who might be allergic to peanuts. Question

**中文**

这些多模态模型，结合这些传感器读数，对物质作出预测。这里大约有 50 种物质，包括不同种类的坚果、香料、香草、水果和蔬菜。每一种都有多次记录的传感器读数日志，因此你能获得这些物质的多个独立读数。这会很有意思。你可以从检测物质开始，也可以尝试挑战极限，检测物质混合物。你还可以尝试检测不同微量含量的花生，这对可能对花生过敏的人很有用。问题。

### [26:35](https://www.youtube.com/watch?v=zlTCAER4z9A&t=1595s) · b000031

**English**

modality and having different modalities. For instance, this to me looks a lot like red and blue sensors.&gt;&gt; Uh fant fantastic question. So let me repeat it for people might not have heard. What basically what constitutes a modality right? Is one time series reading a modality or should I look at different time series readings and just multiple dimensions within the same modality? I get asked this question a lot. I think there is no one answer to that question. Rather, it really goes back to the three principles of multimodal data that we discussed on Tuesday, right? The extent to which data is heterogeneous, the extent to which they show connections, so overlap and shared information and different ways that they interact with each other. You can view these as basically the same modality, multiple channels or different modalities. At the end of the day, they're going to be much more homogeneous, right? They're all time

**中文**

模态，以及拥有不同模态。例如，在我看来，这很像红色和蓝色传感器。&gt;&gt; 呃，非常、非常好的问题。让我为可能没听清的人重复一下。基本上，究竟什么构成一个模态，对吧？一个 time series 读数算一个模态，还是应该将不同的 time series 读数看作同一模态内的多个维度？我经常被问到这个问题。我认为这个问题没有唯一答案。它实际上回到了我们周二讨论的多模态数据的三个原则，对吧？数据在多大程度上具有异质性，它们在多大程度上体现出联系，也就是重叠与共享信息，以及它们相互交互的不同方式。你可以把这些看作基本相同的模态、多个通道，也可以看作不同模态。归根结底，它们会更加同质，对吧？它们都是 time

### [27:31](https://www.youtube.com/watch?v=zlTCAER4z9A&t=1651s) · b000032

**English**

series readings, so they're more homogeneous. uh they might show uh very large connected information so very much overlap between temperature and humidity and yet they might interact in very different ways. So often times just helpful to think about along these three dimensions where your modalities sit.&gt;&gt; Great. Okay. So that's smell looking at a sense of smell as a new modality. Yeah. any signaling or any pre-work after your TV series or doing any for transformations?&gt;&gt; We have not done anything because we just collected a data but you are free to explore any of these approaches if you're interested in this data set. I think of course for your transforms time series analysis signal processing would all would all make sense. Looking at how that uh perhaps synergizes with you know deep learning and all your modern transformer sequence models would be exciting directions. uh but to our

**中文**

series 读数，所以更加同质。它们可能体现出非常多相互关联的信息，比如温度和湿度之间有很多重叠，但它们又可能以非常不同的方式交互。因此，通常沿着这三个维度思考你的模态处在什么位置，会很有帮助。&gt;&gt; 很好。好，这就是嗅觉，把嗅觉作为一种新模态。请说。有没有在 TV series 之后做任何信号处理或前期工作，或者做任何 for transformations？\[字幕疑误，TV series 可能指 time series，for transformations 可能指 Fourier transforms\] &gt;&gt; 我们还没做任何处理，因为我们只是采集了数据，但如果你对这个数据集感兴趣，可以自由探索这些方法。我认为，当然，你的 transforms、time series 分析、信号处理都很合理。研究这些方法如何与 deep learning，以及各种现代 transformer 序列模型协同，会是令人兴奋的方向。但据我们

### [28:29](https://www.youtube.com/watch?v=zlTCAER4z9A&t=1709s) · b000033

**English**

knowledge is kind of like first first of its kind data sets for for smell. So lots of possibilities. Yeah.&gt;&gt; So these are smell sensing chips that basically record volatile organic compounds. Uh here I give an example of carbon monoxide and that's an actual sensor reading. Um basically combinations of CH and O ethanol, alcohol um yeah and those kind of organic gases. Uh and then some of these things over here uh these other chips at the back over here they capture temperature, humidity and pressure. Uh funny thing so we put up smellet and then a few months later um another group also put up a fantastic data set called New York smells. Um so they basically apply some of these sensors and I think it's a group out of Colombia. Uh, so they went around New York into the subway where it smells bad, into Central

**中文**

所知，这算是首个、首个此类嗅觉数据集。所以有很多可能性。请说。&gt;&gt; 这些嗅觉感测芯片基本上记录的是挥发性有机化合物（volatile organic compounds）。这里我给出一氧化碳的例子，这是真实的传感器读数。基本上是 CH 和 O 的组合、乙醇、酒精，嗯，对，还有那类有机气体。然后，这边的一些东西，后面的其他芯片，捕获的是温度、湿度和压力。有件有趣的事，我们发布了 smellet \[字幕疑误，可能指 SmellNet\]，几个月后，另一个团队也发布了一个很棒的数据集，叫 New York smells。他们基本上使用了其中一些传感器，我想是一个来自 Colombia 的团队 \[字幕疑误，可能指 Columbia University\]。他们在纽约各处走动，去了气味不好的地铁，去了气味更好的 Central

### [29:25](https://www.youtube.com/watch?v=zlTCAER4z9A&t=1765s) · b000034

**English**

Park where it smells better, different areas of New York. Uh, recording how it smells and also taking photos. Uh, so that gives you a good paired data set with both a image and smells. So we'll put we'll put some of these links. Um, oh yeah, by the way, so I'm going to introduce all these data sets. Slides will be online and we're also going to release a spreadsheet as we accumulate these data sets. All of you are also free to add to these spreadsheets and then we'll share it with the class. So we get a nice collated list of of modern multimodal data sets categorized by these areas.

**中文**

Park，去了纽约不同的地方，记录气味，同时拍照。因此，这提供了一个很好的配对数据集，同时包含图像和气味。我们会放出其中一些链接。哦，对了，我会介绍所有这些数据集。幻灯片会上线，我们也会随着数据集的积累发布一个电子表格。大家也可以自由向这些电子表格添加内容，然后我们会与全班分享。这样，我们就能得到一份整理好的现代多模态数据集清单，按这些领域分类。

### [30:06](https://www.youtube.com/watch?v=zlTCAER4z9A&t=1806s) · b000035

**English**

All right. So that's smell. Touch is another data set uh that our group and also the broader research community has been making several inroads. uh we recently released this data set called open touch. It is a very large data set with paired data between vision and touch. So vision comes from asking these participants to wear glasses which can basically capture what they're seeing and touch comes from if you see this over here uh they're wearing these gloves on their hand. So these gloves on their hand are high resolution tactile sensors. They can basically measure how strong or how light and in what configuration you're gripping or interacting with different objects. And over here you'll see the tactile readings light up um in purple where pressure is being applied. And over here this is a 3D hand model. Another part of the glove actually allows you to capture based on various IMU sensors the position of all your fingers and your

**中文**

好，这就是嗅觉。触觉是我们团队以及更广泛研究社区正在取得一些进展的另一个数据集方向。我们最近发布了一个名叫 open touch 的数据集。这是一个非常大的数据集，包含视觉和触觉之间的配对数据。视觉数据来自让参与者佩戴眼镜，基本上可以捕获他们所看到的东西；触觉数据来自，你看这里，他们手上戴着这些手套。这些手套是高分辨率触觉传感器（tactile sensors），基本上能够测量你以多大或多轻的力度、以什么构型抓握不同物体或与它们交互。在这里，你会看到受到压力的位置，触觉读数会以紫色亮起。而这里是一个 3D 手部模型。手套的另一个部分实际上可以基于各种惯性测量单元（IMU）传感器，捕获你所有手指以及

### [31:03](https://www.youtube.com/watch?v=zlTCAER4z9A&t=1863s) · b000036

**English**

hand. So that gives you a 3D model of your hand. So basically a large scale data set with touch 3D hand pose and uh egocentric first-person vision. So here is just some samples from the data set. You know as you're gripping this this bath you see the tactile readings light up and your 3D handles changes. And again this is repeated across multiple environments with lots of different objects um inside control settings also outdoors and with different people. So this is a really large data set. Um we also site uh in our in our work you know all the other data sets that people have also released in the space of touch. So you're excited about touch and tactile sensing. Um here are some data sets to start with. This can be used for many things. It can be useful to you know if you have really good models for touch you can use that to train better robots that interact and feel the world like people can. uh people who are interested in world

**中文**

手的位置，从而得到手部的 3D 模型。所以，这基本上是一个包含触觉、3D 手部姿态（hand pose）以及自我中心第一人称视觉（egocentric first-person vision）的大规模数据集。这里是数据集中的一些样本。当你抓握这个 bath \[字幕疑误，所指物体不明\] 时，会看到触觉读数亮起，你的 3D handles 也会变化 \[字幕疑误，可能指 3D hand pose\]。再次说明，这在多个环境、许多不同物体上重复进行，既有受控环境，也有户外，还有不同的人。所以，这是一个非常大的数据集。我们也在工作中引用了其他人在触觉领域发布的所有其他数据集。如果你对触觉和触觉感测感兴趣，这里有一些可以入手的数据集。它们可以用于很多事情。比如，如果你有非常好的触觉模型，就可以用来训练更好的机器人，使它们能够像人一样与世界交互并感受世界。对于对世界

### [32:01](https://www.youtube.com/watch?v=zlTCAER4z9A&t=1921s) · b000037

**English**

models nowadays a big question in world models is to generate vision based on physical interacting information right so condition on touch can you generate images or videos and finally touch is the sensing component if I have good recordings of how I am touching and grasping different objects you can also build gloves which are called haptics gloves so that somebody else somewhere else can feel the force I was applying because a lot of folks uh well some folks here are in the engineering domain. I also want to highlight uh several multimodal data sets that we have access to in the manufacturing space. Um so here this is a typical manufacturing system where there's different stations each with different tasks that being completed in this whole process and you have lots of multimodal data that's being used to record the

**中文**

模型（world models）感兴趣的人，如今 world models 中一个重要问题，是根据物理交互信息生成视觉内容，对吧？也就是以触觉为条件，能否生成图像或视频？最后，触觉是感测部分。如果我有很好的记录，知道自己如何触摸和抓握不同物体，你也可以构建一种叫作触觉反馈手套（haptics gloves）的手套，让身处其他地方的另一个人感受到我施加的力。因为很多人，嗯，在座有一些人属于工程领域，我也想重点介绍几个我们能够获取的制造业多模态数据集。这里是一个典型的制造系统，其中有不同工位，每个工位在整个流程中完成不同任务，并且有大量多模态数据用来记录这些

### [32:57](https://www.youtube.com/watch?v=zlTCAER4z9A&t=1977s) · b000038

**English**

status of these manufacturing systems. You naturally have vision so camera recordings of different steps in the manufacturing process. You often have things like temperature sensing, pressure sensing, smell is a big component as well, right? Whether something smells good or smells bad is actually a big indicator of whether things are running smoothly in manufacturing. So there's lots of multimodal data coming in and there's many tasks where AI will be very helpful in predicting predicting the state of a system predicting the current events that are happening in the system predicting whether machines are breaking down and if maintenance is required and if so can you automatically predict how to repair who should be assigned to repair it and of course in the future perhaps even um automatically using agents to repair these systems. So there are some data sets over here. It's called Intel Minifab. Um people who are interested in the manufacturing space

**中文**

制造系统的状态。自然会有视觉，也就是制造过程不同步骤的摄像记录。通常还会有温度感测、压力感测，气味也是一个重要部分，对吧？某样东西闻起来好不好，实际上是制造流程是否顺畅运行的重要指标。因此，有大量多模态数据不断输入，也有很多任务可以从 AI 中受益，比如预测系统状态，预测系统当前发生的事件，预测机器是否发生故障、是否需要维护；如果需要，能否自动预测如何修理，以及应该安排谁来修理。当然，未来甚至可能自动使用 agents 修复这些系统。这里有一些数据集，叫作 Intel Minifab。对制造业领域感兴趣的人

### [33:51](https://www.youtube.com/watch?v=zlTCAER4z9A&t=2031s) · b000039

**English**

let me know. Uh we have instructors and TAs who are able to serve as mentors uh in this specific domain. Here I'm just showing more examples um of different manufacturing processes where vision is of course very important to look at the state of the system. But most of this these systems are also fitted with multiple types of sensors. uh and given uh vision sensor sometimes also acoustic signals sometimes force measurements accelerometer data microphone data dynamometer data how do you better assess the state of the system and build agentic systems that can uh identify faults and automatically fix these faults. Okay, so that wraps up the first general theme on new multimodal sensing and new multimodal data sets. Any questions before I go on to the next one?

**中文**

请告诉我。我们有能够在这个具体领域担任导师的教师和助教。这里我只是展示更多不同制造流程的例子，视觉当然对观察系统状态非常重要。但这些系统中的大部分也安装了多种类型的传感器。给定视觉传感器，有时还有声学信号，有时有力测量、加速度计数据、麦克风数据、测力计（dynamometer）数据，如何更好地评估系统状态，并构建能够识别故障、自动修复这些故障的智能体系统（agentic systems）？好，这就结束了关于新型多模态感测和新型多模态数据集的第一个大主题。在进入下一个主题之前，大家有什么问题吗？

### [34:53](https://www.youtube.com/watch?v=zlTCAER4z9A&t=2093s) · b000040

**English**

Okay, so the first theme was much more application centric, right? We looked specifically at different data sets, specifically at different application domains. It's much more application ccentric. Um as a guideline usually for these application related projects what I like to think about is if you apply existing methods in this case for example say vision and audio is very important to understand these manufacturing systems often times a key research question is we have all these existing audio and video multimodal systems they have been applied to things like YouTube videos they've never been applied to the manufacturing domain so the key research question is Where do these methods fail when you start applying them to manufacturing domains? Is it because there's very limited data? Is it because the audio is super high frequency so that it doesn't resemble typical music or speech? Right? Those are the kind of questions you want to think about because these methods have typically

**中文**

好，第一个主题更以应用为中心，对吧？我们具体考察了不同数据集，具体考察了不同应用领域，明显更以应用为中心。作为一般指导，对于这些应用相关项目，我通常会这样思考：如果应用现有方法，例如，在这个例子中，视觉和音频对理解这些制造系统非常重要，那么一个关键研究问题往往是，我们已经有所有这些音频和视频多模态系统，它们被应用于 YouTube 视频等场景，却从未应用于制造业。因此，关键研究问题是：当你开始把这些方法应用于制造业时，它们会在哪些地方失败？是因为数据非常有限吗？是因为音频频率特别高，与典型的音乐或语音不同吗？对吧？这些就是你应该思考的问题，因为这些方法通常

### [35:49](https://www.youtube.com/watch?v=zlTCAER4z9A&t=2149s) · b000041

**English**

been applied in other domains but never been applied to this new application domain. So the second theme is going to be more fundamental. I'm hoping some students can uh be interested in building more fundamental approaches to better integrate and connect heterogeneous data. Uh perhaps bridging spatial and temporal data, bridging discrete and continuous data. I think these are the next frontiers for multimodal AI. So what are some examples? We've seen deep learning work really well for things like vision and language, right? Language is nicely tokenized and segmented into words. Vision despite pixels being continuous nowadays are mostly segmented into individual object regions that are semantically meaningful. So we've mostly see multimodal AI applied to vision and language in these more discrete domains. That's why transformers work. That's why tokenization works. That's why your self-supervised masking and next token

**中文**

已经应用于其他领域，却从未应用于这个新的应用领域。因此，第二个主题会更加基础。我希望有些同学能对构建更基础的方法感兴趣，以更好地整合和连接异构数据。比如，连接空间数据与时间数据，连接离散数据（discrete data）与连续数据（continuous data）。我认为这些是多模态 AI 的下一个前沿。那么，有哪些例子？我们已经看到 deep learning 在视觉和语言等领域表现很好，对吧？语言可以很好地进行词元化（tokenization），分割成词。视觉虽然像素是连续的，如今也大多被分割成语义有意义的单个物体区域。因此，我们看到的多模态 AI，主要应用于视觉和语言这些更离散的领域。这就是 transformers 能起作用的原因。这就是 tokenization 能起作用的原因。这就是自监督掩码（self-supervised masking）和下一词元

### [36:46](https://www.youtube.com/watch?v=zlTCAER4z9A&t=2206s) · b000042

**English**

prediction uh typically works. Many data sets and many real world modalities are inherently very continuous, inherently very high frequency, inherently very temporal in nature. So how do you build systems that bridge multimodal deep learning with time series models? How do you bridge it with also tabular models in which case it's much more unstructured? There isn't really a clear relationship between your tokens. How do you build methods that can fuse discrete and continuous data? Um how do you well two perspectives if you have continuous and high frequency data how do you better discretize and tokenize it in a way that is semantically meaningful to be aligned with other modalities that's one extreme the other extreme can you also do multimodal fusion and alignment natively in continuous space without inherently tokenizing your data so these are questions I think that are really at the

**中文**

预测（next token prediction）通常能起作用的原因。很多数据集、很多现实世界模态，本质上非常连续、频率非常高，而且具有很强的时间性。那么，如何构建将多模态 deep learning 与 time series 模型连接起来的系统？如何也将它与表格模型（tabular models）连接起来？在那种情况下，数据要更加无结构，tokens 之间没有真正明确的关系。如何构建能够融合离散与连续数据的方法？嗯，如何，从两个角度来看：如果你拥有连续且高频的数据，如何更好地将它离散化并 tokenize，使其在语义上有意义，能够与其他模态对齐？这是一个极端。另一个极端是，能否直接在连续空间中原生进行多模态 fusion 和 alignment，而不必从根本上将数据 tokenize？我认为，这些问题确实处于

### [37:41](https://www.youtube.com/watch?v=zlTCAER4z9A&t=2261s) · b000043

**English**

frontier for AI today nowadays also this uh this shift towards not multimodal but omnimodal and the key difference is that in multimodal often times it is still orchestration of different modalities. You have a vision encoder, you have a language model, you have something that fuses them, you have something that does reasoning can be seen as a much more modular uh decomposed into different modules. Omnimodel is this recent trend of building models that are exactly the same same architecture, the same parameters and somehow it works for language, vision, audio and more. And that would be great because if you had such a model well you wouldn't need to tune any other models. You can just use that model it will be able to flexibly handle any combinations of modalities. You can give it language and it uses the model. You use language and vision you just use the same model as well. So it's going to be much more flexible. So omnimodal models is a big trend. Um and

**中文**

当今 AI 的前沿。如今还有一个转变，从多模态（multimodal）走向全模态（omnimodal）。关键区别在于，多模态往往仍然是不同模态的编排。你有一个视觉编码器（vision encoder），有一个语言模型，有一个负责融合它们的部分，还有一个负责推理的部分，可以看作更加模块化，拆分成不同模块。Omnimodel \[字幕疑误，可能指 omnimodal\] 是最近的一个趋势：构建具有完全相同架构、相同参数的模型，却能以某种方式处理语言、视觉、音频以及更多内容。这会很棒，因为如果有这样的模型，你就不需要调优任何其他模型。只用这一个模型，就能灵活处理任意模态组合。给它语言，就用这个模型；使用语言和视觉，也还是用同一个模型。所以，它会灵活得多。Omnimodal 模型是一个大趋势。嗯，而且

### [38:37](https://www.youtube.com/watch?v=zlTCAER4z9A&t=2317s) · b000044

**English**

we'll dive deeper into you know fusion alignment and these omnimodal models in the main content of the course. But right now let me highlight some data sets that you can start probing as if you're interested in these more fundamental questions. Uh because these questions are more fundamental. It's important to apply them to data sets uh well first of all apply them to multiple data sets uh not just one and also data sets across multiple domains. This allows you to essentially come up with conclusions that generalize across different domains and not just having a method that works on one application and not something else. So one example is multi-bench. Um this is a a series of works people have released on large scale and yet very generalizable multimodal data sets. So over here you see that the domains include things like effective computing. So understanding people's emotions in healthcare in robotics. So that would be vision and touch. Uh in finance which is you know

**中文**

我们会在课程的主要内容中更深入地讨论 fusion、alignment 和这些 omnimodal 模型。但现在，让我重点介绍一些数据集，如果你对这些更基础的问题感兴趣，可以开始探索。因为这些问题更加基础，所以将它们应用到数据集上很重要，首先，要应用到多个数据集，而不只是一个，而且要跨多个领域。这样，你基本上就能得出可以泛化（generalize）到不同领域的结论，而不只是得到一种在某个应用上有效、在其他应用上无效的方法。一个例子是 multi-bench。这是一系列关于大规模、同时又具有很强泛化性的多模态数据集的工作。在这里，你会看到涵盖的领域包括 effective computing \[字幕疑误，可能指 affective computing，即情感计算\]，也就是理解人的情绪，还有医疗健康、机器人，也就是视觉和触觉，还有金融，也就是

### [39:35](https://www.youtube.com/watch?v=zlTCAER4z9A&t=2375s) · b000045

**English**

lots of high frequency time series multimedia which is your language vision and audio. They've packaged all of these different data modalities together spanning all these and with a unified platform so that you could basically train models on all of these data sets and come up with all the results very quickly. That allows you to basically test these omnimodal models. Right? you claim that your model is general that can encode all of these modalities, you need a generalizable data set to quickly test the performance on all of them. Right? So that's the benefit of some of these more general modality agnostic and application agnostic benchmarks. Uh multi-bench+ was further built on and released. This had a even a larger collection of data sets, even more modalities and also various fusion paradigms. So back then when people created this, it allowed

**中文**

大量高频 time series，还有多媒体，也就是语言、视觉和音频。他们将横跨这些领域的不同数据模态打包到一起，并提供统一平台，让你基本上可以在所有这些数据集上训练模型，并很快得到全部结果。这样，你就能测试这些 omnimodal 模型，对吧？你声称模型具有通用性，能够编码所有这些模态，就需要一个可泛化的数据集，快速测试它在所有模态上的性能，对吧？这就是一些更通用、与模态无关（modality agnostic）、与应用无关（application agnostic）的基准（benchmarks）的好处。后来，在此基础上进一步构建并发布了 multi-bench+。它收集了更多数据集、更多模态，以及各种 fusion 范式。当时，人们创建这些资源，使得

### [40:31](https://www.youtube.com/watch?v=zlTCAER4z9A&t=2431s) · b000046

**English**

people to study you know very concrete research questions. Was method A for fusing better than method B for fusing? Right? That's a very concrete and well specified research question. And by using these very generalized data sets, they could quickly run comparative analysis, controlled experiments, comparing fusion method A with fusion method B and looking at the results to answer that research question. Okay. Uh third set of projects involve reasoning. So whereas the tasks that I showed previously was mostly about perception. So given the reading what given the smell reading what the substance is or uh given for example you know uh video information what is the state of the manufacturing system these are mostly perception tasks just identifying something and associating with

**中文**

大家能够研究非常具体的研究问题。融合方法 A 是否优于融合方法 B？对吧？这是一个非常具体、定义明确的研究问题。使用这些非常通用的数据集，他们能够快速开展对比分析和受控实验（controlled experiments），比较 fusion 方法 A 与 fusion 方法 B，并根据结果回答研究问题。好。第三类项目涉及 reasoning。前面展示的任务主要与感知（perception）有关，比如给定读数，给定嗅觉读数，判断是什么物质；或者给定视频信息，判断制造系统处于什么状态。这些主要是 perception 任务，只是识别某个事物，并将其关联到

### [41:27](https://www.youtube.com/watch?v=zlTCAER4z9A&t=2487s) · b000047

**English**

associating it with some label. So reasoning tasks are usually more complicated. They usually require synthesizing information across multiple steps involving multiple modalities before reaching an answer. And nowadays perhaps the rage in 2025 in AI was about LLM reasoning. Right? We saw huge progress in building systems that could solve very complicated math problems by breaking it down and solving each step and then uh synthesizing all your answers to come up with the answer to these very complicated IMO questions for complicated coding problems and more. So naturally people have also extended this to multimodal domains where you have to reason across difficult language tasks and also about complicated images and other modalities. Uh there's several challenges here. Reasoning is often very fine grain. You have to break things down into individual steps. It's often compositional. You have to combine

**中文**

某个标签。因此，reasoning 任务通常更复杂。它们通常需要在得出答案之前，跨多个步骤、涉及多种模态，综合信息。2025 年 AI 领域最热门的话题，可能就是 LLM reasoning，对吧？我们看到，在构建能够解决非常复杂数学问题的系统方面取得了巨大进展：把问题拆解，逐步求解，然后综合所有答案，得到这些极其复杂的国际数学奥林匹克竞赛（IMO）题目、复杂编程问题以及更多问题的答案。因此，人们自然也把它扩展到多模态领域，需要对困难的语言任务进行推理，也需要对复杂图像和其他模态进行推理。这里有几个挑战。Reasoning 往往是细粒度的（fine-grained），必须将事情拆解成单独步骤。它通常具有组合性（compositional），需要

### [42:23](https://www.youtube.com/watch?v=zlTCAER4z9A&t=2543s) · b000048

**English**

information procedurally across multiple steps. Um and there's always this debate whether reasoning needs to be uh built in through neuro symbolic methods right which is the case of AI in the several decades ago or does reasoning automatically emerge if you scale up these uh data sets and models to sufficiently large size. So I highlight several data sets uh in terms of reasoning starting with things like media description. So if you have, you know, have these images, can you come up with really good captions that are very well descriptive of these images? This is kind of straddling the line between perception and you start slowly seeing some amount of reasoning because it's not just enough to identify something, but you now need to think and come up with a coherent summary of what's happening in the image. Um, and there's a lot of data sets. MS Coco is perhaps the most famous one. uh it's called uh Microsoft common objects and

**中文**

按照程序跨多个步骤组合信息。而且，始终存在这样一个争论：reasoning 是否需要通过神经符号方法（neuro symbolic methods）内置进去，就像几十年前的 AI 那样；还是只要把这些数据集和模型扩展到足够大的规模，reasoning 就会自动涌现？我在 reasoning 方面重点介绍几个数据集，先从媒体描述（media description）等任务开始。如果你有这些图像，能否给出非常好的 captions，准确而充分地描述它们？这有点处在 perception 的边界上，你开始逐渐看到一定程度的 reasoning，因为仅仅识别某个东西已经不够，现在还需要思考，并对图像中发生的事情给出连贯的概述。有很多数据集。MS Coco 可能是最著名的一个，它叫作 Microsoft common objects and

### [43:20](https://www.youtube.com/watch?v=zlTCAER4z9A&t=2600s) · b000049

**English**

context where it's a ton of images and they got annotators to write descriptions for each of these images. Uh since this was released of course people have also extended it to other forms of captioning. Captioning videos, captioning time series data, captioning audio and also captioning at different levels. Not just descriptive captioning but also explaining what the intentions for example of the people are uh in these in these images. Uh after captioning was released, people found that captioning was very difficult to evaluate because you had a reference caption written by a person and you had a caption that was generated by your AI model. Uh but there's many ways of captioning an image, right? Many of which can be correct uh and many of which are at different degrees of correctness. So it became quite hard to evaluate. They had to rely on human evaluation. Nowadays, of course, you can use language models to evaluate how good

**中文**

context \[字幕疑误，可能指 Microsoft Common Objects in Context\]，包含大量图像，并让标注人员为每张图像撰写描述。当然，发布之后，人们也将其扩展到了其他形式的 captioning：视频 captioning、time series 数据 captioning、音频 captioning，以及不同层次的 captioning。不只是描述性的 captioning，还包括解释，比如这些图像中人物的意图是什么。Captioning 推出后，人们发现它很难评估，因为你有人工撰写的参考 caption，也有 AI 模型生成的 caption。但是，描述一张图像有很多种方式，对吧？其中很多都可能正确，也有很多在不同程度上正确。因此，它变得很难评估，不得不依赖人工评估。当然，如今你可以使用语言模型来评价

### [44:15](https://www.youtube.com/watch?v=zlTCAER4z9A&t=2655s) · b000050

**English**

a caption is with responses to to the real caption. Uh, but these series of question answering data sets then became popular and replace captioning because instead of captioning entire image, these QA data sets ask very specifically a targeted question about the image. So, VQA is perhaps the very first one that came up in the series. Actually, pretty interesting. Uh, this image and the question is what is the mustache? uh made of and the answer is bananas. So some which are easy uh questions to answer but some are also quite counterintuitive. Uh so this is a very classic data set. Of course performance now on VQA has been pretty much saturated with all your vision language models. Uh and naturally from images people looked at building QA data sets that require more deeper reasoning and understanding of videos. So TV QA and movie QA these are you know several data

**中文**

一个 caption 相对于真实 caption 有多好。但随后，这一系列问答（question answering，QA）数据集开始流行，并取代 captioning，因为这些 QA 数据集不是描述整张图像，而是针对图像提出非常具体的问题。视觉问答（VQA）可能是这一系列中最早出现的一个。其实很有趣，这张图像对应的问题是：胡子是用什么做的？答案是香蕉。有些问题很容易回答，但有些也相当反直觉。所以，这是一个非常经典的数据集。当然，现在各种视觉语言模型（vision language models）在 VQA 上的性能已经基本饱和。人们自然又从图像出发，研究构建需要对视频进行更深入推理和理解的 QA 数据集。TV QA 和 movie QA 就是这一代中出现的几个数据

### [45:12](https://www.youtube.com/watch?v=zlTCAER4z9A&t=2712s) · b000051

**English**

sets that came up in this generation. Uh they essentially got these long movies or even longer TV shows uh that were that were annotated with questions throughout the TV show. So you can see some of these questions are are perceptive you know what is happening or what is the object but some of these questions also require some pretty long-term understanding of the video uh TV. In this case, it's a the friends TV show. You got to understand the context of who these characters are and what their relationships are from from previous episodes. But some of them require a much longer compositional and temporal reasoning about these characters.

**中文**

集。他们基本上拿来这些长电影，甚至更长的电视剧，在整部电视剧中标注问题。你可以看到，其中一些问题是感知性的，比如正在发生什么，或者这是什么物体；但有些问题也要求对视频、电视剧有相当长期的理解。在这个例子中，是 friends 这部电视剧。你得从之前的剧集中理解这些角色是谁，以及他们之间是什么关系。有些问题需要围绕这些角色进行更长跨度的组合推理（compositional reasoning）和时序推理（temporal reasoning）。

### [45:55](https://www.youtube.com/watch?v=zlTCAER4z9A&t=2755s) · b000052

**English**

There was also a generation of data sets uh that are procedurally generated. So when I say procedurally generated, they look more artificial. Uh but don't let them looking artificial fool you. Some of these data sets are actually very very difficult. So you can procedurally generate for example in this case blocks or shapes of different color, different sizes, different positions and then you can start asking pretty non-trivial questions uh about this combination of objects. For example, there is or is there at least one tower with four blocks with a yellow block at the base and a blue block beneath the top block. Right? This uh this is a pretty non-trivial question. It requires the model to understand color, understand how to count, understand relative positions, what is above, what is below. Um some of these also require understanding relative sizes, whether

**中文**

还有一代数据集是程序化生成的（procedurally generated）。我说程序化生成，是指它们看起来更加人工化。但不要被这种人工化的外观骗了，有些数据集实际上非常、非常难。例如，你可以通过程序生成不同颜色、不同大小、不同位置的积木或形状，然后就可以围绕这些物体的组合提出相当不简单的问题。例如，存在，或者说，是否至少有一座由四块积木组成的塔，底部是一块黄色积木，最上方积木的下方是一块蓝色积木？对吧？这是一个相当不简单的问题。它要求模型理解颜色、理解如何计数、理解相对位置，什么在上面、什么在下面。其中一些还要求理解相对大小，判断

### [46:51](https://www.youtube.com/watch?v=zlTCAER4z9A&t=2811s) · b000053

**English**

one is bigger or smaller than the other. And because these data sets are procedurally generated, you can essentially have infinite complexity, right? And people basically find that if there's like two objects, you can identify, yes, there's one red and one blue, that's pretty easy for these models. But if you scale up the number of objects and the number of relationships between these objects, these models very quickly fail. So that was perhaps the first initial tests of reasoning and compositionality in these models. So that's called Cornell NLVR standing for natural language visual reasoning and subsequently they extended it to NLVR2 which uh which followed the same principles uh but now with natural images that were partially synthetically generated right you could get some of these images and you could uh back then use Photoshop nowadays use Genai to place different objects and people and things at different locations

**中文**

一个是否比另一个更大或更小。因为这些数据集是程序化生成的，所以基本上可以具有无限复杂度，对吧？人们发现，如果只有两个物体，你可以识别，是的，有一个红色的、一个蓝色的，这对这些模型相当容易。但如果增加物体数量，以及物体之间的关系数量，这些模型很快就会失败。这可能是最早对这些模型的 reasoning 和组合性（compositionality）进行的初步测试。因此，它叫 Cornell NLVR，意思是自然语言视觉推理（natural language visual reasoning）。后来，他们将其扩展成 NLVR2，沿用了相同原则，但现在使用部分合成的自然图像，对吧？你可以拿来一些图像，当时可以用 Photoshop，如今可以用 Genai，将不同的物体、人物和东西放到不同位置

### [47:47](https://www.youtube.com/watch?v=zlTCAER4z9A&t=2867s) · b000054

**English**

procedurally and generate arbitrarily complex questions or captions for that. So in this case uh well the answer is whether it's true or false whether a left image contains twice the number of dogs as the right image and at least two dogs in total are standing. Let's see. So that's actually pretty challenging for today's AI models. Requires quite a bit of reasoning. Window ground is a is a data set I really love. Uh the idea is very simple, right? You have an image and a caption. Let's just swap the order of certain words in the caption. So some plants surrounding a light bulb. That's something you often see on a day-to-day basis, right? A light bulb over here. You have some plants surrounding it. What if you swap it into a caption that says a light bulb surrounding some plants? So you have the light bulb on the outside and plants on

**中文**

，通过程序为它们生成任意复杂的问题或 captions。在这个例子中，答案是判断真假：左图中的狗的数量是否是右图的两倍，而且总共至少有两只狗站着。看看。所以，这对今天的 AI 模型其实相当有挑战，需要不少 reasoning。Window ground \[字幕疑误，可能指 Winoground\] 是一个我非常喜欢的数据集。思路很简单，对吧？你有一张图像和一个 caption。我们只需交换 caption 中某些词的顺序。“一些植物围绕着一个灯泡。”这是日常生活中经常见到的，对吧？这里有一个灯泡，周围有一些植物。如果把 caption 改成“一个灯泡围绕着一些植物”呢？也就是灯泡在外面，植物在

### [48:45](https://www.youtube.com/watch?v=zlTCAER4z9A&t=2925s) · b000055

**English**

the inside. something that you almost have never seen before, right? So something that's commonly seen and a swap of the of the objects into something you never see before. Turns out models get confused at this very easily. They are confused. They associate the common image with the common caption, but they really struggle identifying this uncommon image with the uncommon caption. uh so winter ground was released in in I think 20 late 2023 but still remains a challenge for today's today's AI models. I'm sure all of you have also seen um you know whenever a new uh image generation model is released they test it with you know an astronaut riding a horse that used to be challenging and now you swap it to a horse riding an astronaut can a model still generate the image and probably nowadays they're getting better and better at doing that but that's a question of compositionality. Yes. for this one. Some thoughts

**中文**

里面。这是你几乎从未见过的，对吧？所以，一个是常见情景，另一个通过交换物体变成你从未见过的情景。结果发现，模型非常容易对此感到困惑。它们会混淆。它们会把常见图像与常见 caption 联系起来，但在将这个不常见的图像与不常见的 caption 对应起来时非常吃力。winter ground \[字幕疑误，可能指 Winoground\] 是在，我想是 20，2023 年末发布的，但直到今天仍然对 AI 模型构成挑战。我相信大家都见过，每次有新的图像生成模型发布，人们就会用“一个宇航员骑着一匹马”来测试，以前这很有挑战；现在把它交换成“一匹马骑着一个宇航员”，模型还能生成图像吗？如今它们可能越来越擅长做这件事，但这是一个 compositionality 问题。请说。对于这个，有一些想法

### [49:45](https://www.youtube.com/watch?v=zlTCAER4z9A&t=2985s) · b000056

**English**

&gt;&gt; um can we have it would be great if there were that would be a good topic for a research project. To my knowledge there there aren't yet you know perfect solutions to this right we are getting&gt;&gt; uh what do you mean by guardrails? Then you might not be certain that it's the answer, but just unlike&gt;&gt; yeah I mean intuitively you could have guard rails but the thing is how would you enforce them right for example detecting the plants and the light bulb here using object detection is easy you can draw bounding boxes over the light bulb and the plants but over here you can't even draw like a bounding box around the light bulb or the bounding box around the plants. Uh so that's one challenge if you wanted to build an explicit system that that checked for you know a surrounding b and then surrounding is quite ambiguous. It means different things in different

**中文**

&gt;&gt; 嗯，我们能不能有，如果有就太好了，这会是一个很好的研究项目题目。据我所知，目前还没有完美的解决方案，对吧？我们正在得到 &gt;&gt; 呃，你说的防护机制（guardrails）是什么意思？那么你可能不确定这就是答案，但只是不同于 &gt;&gt; 是的，我的意思是，直觉上你可以设置 guardrails，但问题是如何实施它们，对吧？例如，在这里使用目标检测（object detection）检测植物和灯泡很容易，你可以给灯泡和植物画边界框（bounding boxes）。但在这里，你甚至没法给灯泡或植物画出一个 bounding box。所以，如果你想构建一个显式系统，检查 A 围绕 B，这就是一个挑战。而且，“围绕”相当模糊，在不同

### [50:43](https://www.youtube.com/watch?v=zlTCAER4z9A&t=3043s) · b000057

**English**

contexts. And this is just one example, right? You could have a guardrail for this if you overfit a system to this, but then you know there's an infinite number of, you know, AB objects and relationships between them.&gt;&gt; Yeah.&gt;&gt; Yes. Yes. So a lot of these are only meaningful if they're generalizable. Uh that's one issue with a lot of these reasoning benchmarks. Um, some of you might have seen like ARC AGI which people claim is like a good test for AGI and it also falls under this broad category of compositional reasoning benchmarks that are procedurally generated and they get harder and harder and of course people are building solutions that really overfit to that domain with maybe some guard rails or with neuro symbolic uh but it doesn't really inform us about how other domains or other tasks will get better. Um so yeah I think it's always a debate whether you know we build data sets just

**中文**

上下文中意思不同。这只是一个例子，对吧？如果让系统过拟合这个例子，你可以为它设置一个 guardrail，但 A、B 物体及其相互关系有无穷多种。&gt;&gt; 是的。&gt;&gt; 对，对。所以，其中很多只有能够泛化时才有意义。这是很多 reasoning benchmarks 的一个问题。你们有些人可能见过 ARC AGI，人们声称它是一个很好的通用人工智能（AGI）测试，它也属于程序化生成的 compositional reasoning benchmarks 这一大类，而且越来越难。当然，人们正在构建真正过拟合那个领域的解决方案，也许使用某些 guardrails，或者使用 neuro symbolic 方法，但这并不能告诉我们其他领域或其他任务会如何变得更好。所以，是的，我认为这始终存在争论：我们构建数据集，究竟只是

### [51:38](https://www.youtube.com/watch?v=zlTCAER4z9A&t=3098s) · b000058

**English**

to test whether we over fit to it or is it actually a reflection of overall trends but I mean this I mean there's good ideas for guard rails that be a good idea for a research project yes like train the always a process or one For example, this number

**中文**

为了测试我们是否会过拟合它，还是它确实反映了整体趋势？不过，我的意思是，这里关于 guardrails 有不错的想法，会是一个很好的研究项目点子。请说。比如训练这个总是一个过程或者一个，例如，这个数字 \[字幕疑误，语句不完整\]

### [52:17](https://www.youtube.com/watch?v=zlTCAER4z9A&t=3137s) · b000059

**English**

um we'll dive into more details about how these modern models are trained but I I would say they are procedural in a sense that they are pre-trained instruction fine-tuned or supervised fine tune. and then they're doing test time reasoning and people think in 2026 there'll be a stage four which is kind of like test time discovery or test time learning. Uh so in that sense they are kind of trained in different stages and when you start doing reasoning for example the goal is to for the model to break the problem down into individual steps um and solve each step and then combine the steps. So I mean the hope is that yes there will be this procedurally improvements but but sometimes you don't see that happening.

**中文**

嗯，我们会更详细地讨论这些现代模型是如何训练的，但我会说，从某种意义上，它们是按过程进行的：先进行预训练（pre-training）、指令微调（instruction fine-tuning）或监督微调（supervised fine-tuning），然后进行测试时推理（test time reasoning）。人们认为，到 2026 年会出现第四阶段，有点像测试时发现（test time discovery）或测试时学习（test time learning）。所以，从这个意义上说，它们是在不同阶段训练的。当你开始做 reasoning 时，例如，目标是让模型把问题拆解为单独步骤，逐步解决，再把这些步骤组合起来。所以，我的意思是，我们希望，是的，会出现这种按过程逐步发生的改进，但有时你看不到它发生。

### [53:03](https://www.youtube.com/watch?v=zlTCAER4z9A&t=3183s) · b000060

**English**

One domain that I've heard there's a lot of critique on is physics,&gt;&gt; right?&gt;&gt; And I wonder if there's any data set there and&gt;&gt; definitely. Yeah. I I didn't uh put them here. I mean again disclaimer, these are not the data sets that you have to work with. I'm just presenting examples and how I kind of go about dissecting and analyzing the challenges. Please take this as inspiration. use them if they're they're interesting to you. Find more data sets that you're interested in but fit in similar flavor but intuitive physics yes although I feel that for intuitive physics um models are getting quickly quite good at it. Uh but it'd be good to see for some people must have proposed a lot of intuitive physics tasks for these world models today looking at whether they are physically consistent and follow geometry. Um so that'll be a good set of data sets to start with.

**中文**

我听说有很多批评的一个领域是物理，&gt;&gt; 对吧？&gt;&gt; 我想知道那里有没有什么数据集，而且 &gt;&gt; 当然有，是的。我没有把它们放在这里。我的意思是，再说明一下，这些不是你们必须使用的数据集。我只是提供例子，以及我如何拆解和分析这些挑战。请把它们当作启发。如果感兴趣，就使用它们。再找一些你感兴趣、但性质相似的数据集。至于直觉物理（intuitive physics），是的，不过我觉得模型在 intuitive physics 方面正在迅速变得相当擅长。但值得看看，有些人一定已经针对今天这些 world models 提出了很多 intuitive physics 任务，考察它们在物理上是否一致，是否遵循几何规律。所以，那会是一组很好的入门数据集。

### [54:09](https://www.youtube.com/watch?v=zlTCAER4z9A&t=3249s) · b000061

**English**

All right. Um, we put up a data recent data set on puzzles. I mean, this is MIT. Who here likes doing puzzle hunts? Yes, quite a few people. Uh, so we recently put up a data set called Puzzle World, which is basically a data set of, uh, introductory puzzle hunts. Uh for those of you who are not familiar, the puzzle hunts uh is basically I think it's ultimate test for reasoning. It requires you to um use clues. In this case, the only clue that you have is top down processing. So there isn't even an explicit instruction like you know mathematics or coding. You have some explicit instruction here. you just have clues and hints and you got to use a mix of your intuition and your your cultural knowledge and sometimes you know esoteric knowledge from TV shows and and and uh recent culturally popular phenomena to try to solve this problem. In this case this top down processing

**中文**

好。我们最近发布了一个关于谜题的数据集。我的意思是，这里可是 MIT。在座有谁喜欢玩解谜寻宝（puzzle hunts）？是的，还挺多人。我们最近发布了一个叫 Puzzle World 的数据集，基本上是入门级 puzzle hunts 数据集。对于不熟悉的人，puzzle hunts 基本上，我认为是 reasoning 的终极测试。它要求你利用线索。在这个例子中，你唯一的线索是“自上而下的处理（top down processing）”。所以，它甚至没有数学或编程那样明确的指令。在那些任务中，你有明确的指令；这里，你只有线索和提示，必须结合直觉、文化知识，有时还需要来自电视剧和近期文化流行现象的冷门知识，尝试解决这个问题。在这个例子中，这个 top down processing

### [55:06](https://www.youtube.com/watch?v=zlTCAER4z9A&t=3306s) · b000062

**English**

basically hints that these models should process this set of overlapping images in a top- down manner. And because these are flags, the models should identify that uh these are images of flags and they can identify the countries that these flags are representing. Barbados, Oman, Tajakhstan, Seells and so on. And often times it's important to extract the first letter or some letter from this sequence of words and that actually spells out Botswana which is another country. Right? So this is probably one of the easiest puzzles uh in this benchmark. GBT01 actually guesses correct. Um and in general it does require a good amount of visual reasoning recognizing what's happening in the image some amount of external knowledge especially domain expert knowledge from solving these puzzles and text reasoning in this case actually manipulating different symbols and characters uh to actually solve solve the puzzle. So we released a benchmark called puzzle world. Uh again people

**中文**

基本上暗示模型应该以自上而下的方式处理这一组重叠的图像。因为这些是国旗，模型应该识别出这些是国旗图像，并识别它们代表的国家。Barbados、Oman、Tajakhstan \[字幕疑误，可能指 Tajikistan\]、Seells \[字幕疑误，可能指 Seychelles\]，等等。通常，从这一串词中提取首字母或某个字母很重要，而它实际上拼出了 Botswana，也就是另一个国家，对吧？所以，这可能是这个 benchmark 中最简单的谜题之一。GBT01 \[字幕疑误，可能指 GPT o1\] 实际上猜对了。总体而言，它确实需要相当程度的视觉推理（visual reasoning），识别图像中发生的事情；需要一定的外部知识，尤其是解这些谜题的领域专业知识；也需要文本推理（text reasoning），在这个例子中，实际操作不同符号和字符来解开谜题。因此，我们发布了一个叫 puzzle world 的 benchmark。再次说明，

### [56:04](https://www.youtube.com/watch?v=zlTCAER4z9A&t=3364s) · b000063

**English**

interested in puzzle hunts they can do this for their course project that requires a good amount of multimodal understanding reasoning across different strategies and extensive exploration. Right? A lot of this is about trying and failing and trying and failing um and until you succeed. So that's puzzle world. U has 500 puzzles and also good thing is that it's annotated for human reasoning. Bless you. It's a annotative for human reasoning. So how human experts will solve this. So that actually gives you good data to start you know fine-tuning or training these models with a intermediate human supervision. And finally last one in reasoning science QA uh science is a natural domain where you have you know very complicated reasoning questions and you often have visuals. For example, uh in this case, you know, looking at the baby trying to pull or push uh a cabinet and the force that might be required to do

**中文**

对 puzzle hunts 感兴趣的人，可以用它做课程项目。它要求相当程度的多模态理解、跨不同策略的 reasoning，以及广泛探索，对吧？这里面有很多尝试、失败、再尝试、再失败，直到成功。所以，这就是 puzzle world。嗯，它有 500 个谜题，还有一个优点，是它标注了人类推理过程。祝你健康。它有人类推理标注，也就是人类专家会如何解决这些问题。因此，这实际上提供了很好的数据，让你开始通过中间的人类监督（intermediate human supervision）来 fine-tune 或训练这些模型。最后，reasoning 部分的最后一个是 science QA。科学是一个很自然的领域，其中有非常复杂的 reasoning 问题，而且常常有视觉内容。例如，这个例子里，一个婴儿试图拉动或推动柜子，以及完成这个动作可能需要的力

### [57:00](https://www.youtube.com/watch?v=zlTCAER4z9A&t=3420s) · b000064

**English**

that. So often as visuals, uh this data also includes things like math where there's geometry questions which has diagrams and questions includes like calculus and others and u looking at whether these models can basically understand and answer these questions. So that's science QA. Okay, any final questions about reasoning?

**中文**

。因此，经常有视觉内容。这个数据还包括数学，比如带图示的几何问题，也包括微积分等问题，考察这些模型是否基本能够理解并回答这些问题。这就是 science QA。好，关于 reasoning，还有最后的问题吗？

### [57:31](https://www.youtube.com/watch?v=zlTCAER4z9A&t=3451s) · b000065

**English**

All right, agents. Everything we've seen so far, the goal is still to maybe come up with the right answer, make the right prediction, or do the right analysis, right? agents looks at how these models can be used to automatically take actions in some environment either one action or a sequence of actions to maximize some long-term reward or long-term objective. Uh this is becoming increasingly popular. We've seen AI models, AI agents that can operate on the web, on your computer, on other closed environments um that can help you solve tasks, right? for example, emails and um calendars and uh purchasing things and spreadsheets and powerpoints. So there's a lot of challenges here, a lot of interest, but also a lot of challenges. This requires the instructions and language, but also visual and other modalities grounded in things like images in different tools

**中文**

好，智能体（agents）。到目前为止，我们看到的一切，目标仍然可能是给出正确答案、作出正确预测，或者进行正确分析，对吧？Agents 研究的是如何使用这些模型，在某种环境中自动采取行动，可以是一个动作，也可以是一串动作，以最大化某种长期奖励（long-term reward）或长期目标。这正在变得越来越流行。我们已经看到能够在网页、你的电脑以及其他封闭环境中操作的 AI 模型、AI agents，帮助你完成任务，对吧？例如，电子邮件、日历、购买物品、电子表格和 powerpoints。所以，这里有很多挑战，很多关注，但也有很多挑战。这要求指令和语言，也要求视觉和其他模态，与不同工具中的图像等内容建立落地关联（grounding）

### [58:26](https://www.youtube.com/watch?v=zlTCAER4z9A&t=3506s) · b000066

**English**

and different APIs. It requires usually a lot of actions to be taken before they actually solve the task. uh and the longer the action sequence is, the harder the model uh the harder it is for the model. Uh most of these benchmarks also show potential risks, right? There's a lot of benchmarks looking at whether if a agent has access to a computer, can someone adversarily attack the agent to leak your passwords or to send malicious emails. So I'll cover some interesting data sets. So a lot of this work started with web QA. So again looking at those QA data sets but now extending it to websites websites news articles can you answer questions correctly. After web QA came web arena. So these are environments where given only language can you you know use an AI model to understand the instruction execute tasks on these websites. So example task could be purchasing some earphones with certain stars and rating

**中文**

，以及不同的应用程序接口（APIs）。通常，它们需要采取很多动作才能真正完成任务。而且，动作序列越长，模型就越难，模型完成任务就越困难。这些 benchmarks 中的大多数也显示出潜在风险，对吧？有很多 benchmarks 研究：如果一个 agent 可以访问电脑，是否有人能够对它发动对抗性攻击，让它泄露你的密码或发送恶意电子邮件。我会介绍一些有趣的数据集。很多工作是从 web QA 开始的，也就是再次考察这些 QA 数据集，但现在扩展到网站和新闻文章，能否正确回答问题。Web QA 之后出现了 web arena。这些是一些环境，给定的只有语言，你能否使用 AI 模型理解指令，在这些网站上执行任务？例如，一个任务可能是在网站上购买具有特定星级和评分的耳机

### [59:23](https://www.youtube.com/watch?v=zlTCAER4z9A&t=3563s) · b000067

**English**

the website. I'm showing this as a visual but the first version of web arena they only gave this in the form of HTML to the AI model only HTML so only text uh and then ideally the model should be able to you know search for your earphones filter by number of stars add it to your checkout and then give you the order confirmation uh so include a lot of a lot of really nice environments uh one-stop shop which is basically this uh clone of Amazon because if you use real Amazon you'll get you know rate limited uh edit. It also included things like GitLab which is um you know GitHub uh but also solving solving issues and writing code on GitHub and these tasks were very easy for people but very difficult at that time for LLM agents. It was 40 14% now it's hovering about 50ish%. uh but tasks were initially designed to use only text and HTML source code. But of course text and HTML source code is

**中文**

。我在这里以视觉形式展示，但 web arena 的第一个版本只向 AI 模型提供 HTML 形式的内容，只有 HTML，也就是只有文本。理想情况下，模型应该能够搜索耳机，按星级数量筛选，将其加入结账，然后给你订单确认。它包含很多很不错的环境，比如 one-stop shop，基本上是一个 Amazon 的克隆，因为如果使用真正的 Amazon，就会受到速率限制，呃，edit \[字幕疑误，可能指 Reddit\]。它还包括 GitLab，嗯，就是类似 GitHub，也包括在 GitHub 上解决 issues 和编写代码。这些任务对人来说很容易，但在当时对 LLM agents 非常困难。当时是 40，14%，现在大约在 50% 左右。但这些任务最初设计为只使用文本和 HTML 源代码。当然，文本和 HTML 源代码是一种

### [1:00:20](https://www.youtube.com/watch?v=zlTCAER4z9A&t=3620s) · b000068

**English**

such an unintuitive medium for these models, right? They usually take up uh I mean they take up thousands of lines or tens of thousands of lines of context for a single web page which basically means even just stepping through five or six web pages you're already almost at 100,000 tokens for your models which then the model will start forgetting. Whereas if you had a visual representation, you could just process that using a visual encoder. And naturally visual representations is also much more spatial. You can see for example categories with objects underneath them. You can look at the color. You can look at actual images that are embedded in the website which HTML doesn't give you. So after web arena came visual web arena which is a natural progression of of data sets that also included you know visual representations of these websites to train multimodal web agents. So again included similar tasks uh Reddit

**中文**

对这些模型而言非常不直观的媒介，对吧？通常一个网页就会占用几千行甚至几万行上下文，基本意味着，即便只浏览五六个网页，模型就已经接近 100,000 tokens，然后模型就会开始遗忘。而如果有视觉表示（visual representation），就可以直接用视觉编码器处理。自然，视觉表示也更具有空间性。例如，你可以看到类别及其下方的物体，可以看颜色，可以看网站中实际嵌入的图像，而 HTML 不会给你这些。因此，web arena 之后出现了 visual web arena，这是数据集的自然演进，也纳入了这些网站的视觉表示，用于训练多模态网页 agents。它同样包括类似任务，Reddit

### [1:01:16](https://www.youtube.com/watch?v=zlTCAER4z9A&t=3676s) · b000069

**English**

shopping uh it provided these models with the visual representation of the website also HTML also these uh textlike things which are called accessibility trees which are a more clean version of HTML stripping out of all the redundancy um and these models have to basically perform tasks on these websites. So visual web arena is a is a pretty good environment for that. Um I'll show you one example. So extending web arena now you can start giving it tasks that also involve vision. For example, you take a photo and you want to pass the model to buy the cheapest color photo printer and send it to Emily's place where the address is shown in the image because that requires some OCR to figure out the address. requires going on the websites to look for printers, finding color printers that are the cheapest, uh

**中文**

、购物。它向这些模型提供网站的视觉表示，也提供 HTML，还提供这些类似文本的东西，叫作无障碍树（accessibility trees），这是更干净的 HTML 版本，去掉了所有冗余。模型基本上必须在这些网站上执行任务。所以，visual web arena 是一个很不错的环境。我给你们看一个例子。在 web arena 的基础上扩展后，现在可以开始给它涉及视觉的任务。例如，你拍了一张照片，希望把它交给模型，让它购买最便宜的彩色照片打印机，并寄到 Emily 家，地址显示在图像里。因为这需要光学字符识别（OCR）来确定地址，需要上网站寻找打印机，找到最便宜的彩色打印机，

### [1:02:13](https://www.youtube.com/watch?v=zlTCAER4z9A&t=3733s) · b000070

**English**

purchasing that printer, and then adding to the destination address the address from the photo. So, these are these are reasonably complicated.

**中文**

购买这台打印机，然后把照片中的地址填入收货地址。所以，这些任务相当复杂。

### [1:02:32](https://www.youtube.com/watch?v=zlTCAER4z9A&t=3752s) · b000071

**English**

So after these web tasks came a bunch of environments that further extended it to multiple operating systems. So web, desktop, mobile, Linux, Windows, Mac OS. Um and of course this became the foundation for a lot of these more you know open-ended agentic models that are now able to operate on different environments in the computer. So OS Atlas is an environment um that that is open source that also includes all of these different visual information from different domains allowing you to benchmark and train these more generalist multimodal agents.

**中文**

这些网页任务之后，又出现了一批环境，进一步扩展到多种操作系统。包括网页、桌面、移动端、Linux、Windows、Mac OS。当然，这成为很多更加开放的 agentic 模型的基础，它们现在能够在电脑上的不同环境中操作。OS Atlas 是一个开源环境，也包含来自不同领域的所有这些不同视觉信息，让你能够评测并训练这些更通用的多模态 agents。

### [1:03:11](https://www.youtube.com/watch?v=zlTCAER4z9A&t=3791s) · b000072

**English**

Okay, I'm running out of time so I'll skip some slides. Uh social intelligence is something that I'm particularly interested in. So building AI systems that don't just work on a computer and don't just work in the physical world but also work in the social world that understand and interact with people. I mean that's the main premise. Um several key things here. How do people how do models understand first perceive? So understand people what they're thinking what their emotions are what they're feeling what they're saying. How do they interact with people? So in the right times say the right things in the right emotions. And also have social common sense. uh you know the unspoken rules of what to do and what not to do in social interactions. Um theory of mind is also a particularly interesting topic right theory of mind is you know what I think you are thinking and you can even go multiple layers what I think you think I am thinking and a lot of this goes along

**中文**

好，我快没时间了，所以会跳过一些幻灯片。社会智能（social intelligence）是我特别感兴趣的方向。也就是构建不仅在电脑上工作、不仅在物理世界中工作，而且在社会世界中工作，能够理解人并与人交互的 AI 系统。这就是主要前提。这里有几个关键点。人如何，模型如何理解，首先是感知？也就是理解人，理解他们在想什么、情绪是什么、感受是什么、在说什么。它们如何与人交互？也就是在合适的时间，以合适的情绪，说合适的话。还要具有社会常识（social common sense），也就是社交互动中哪些事该做、哪些事不该做的未言明规则。心智理论（theory of mind）也是一个特别有趣的话题，对吧？Theory of mind 就是，我认为你在想什么，而且甚至可以递进多层：我认为你认为我在想什么。其中很多都沿着

### [1:04:06](https://www.youtube.com/watch?v=zlTCAER4z9A&t=3846s) · b000073

**English**

this idea of common sense where a lot of what is socially uh interactive and socially acceptable is is not really said and spoken explicitly. So lots of data sets in this space starting from perception. There's been a lots of series of data sets on recognizing a effect and emotions right from a variety of modalities from spoken language from visual expressions and video from tone of voice and vocal expressions um also from other forms of physological sensing. When you wear these smartwatches and wristbands you can look at skin conductance which is how much you're sweating. You can look at heart rate. Um, and all of these are very useful indicators of mood and emotion and a effect. So, a bunch of affect recognition data sets. Sentiment as well. So, how positive or negative a person feels about a particular topic. Lots of interest in sentiment analysis. A lot of these data sets were curated when people were reviewing a movie or reviewing a TV show

**中文**

这种常识的思路展开，也就是很多具有社交互动性、在社会上可接受的事情，并不会真正明确地说出来。所以，这个领域有很多数据集，从 perception 开始。已经出现了很多系列的数据集，用于从各种模态识别 a effect \[字幕疑误，可能指 affect\] 和情绪，包括口语、视觉表情和视频、语调和声音表达，也包括其他形式的生理感测。当你戴着这些智能手表和手环时，可以查看皮肤电导（skin conductance），也就是你出了多少汗。可以查看心率。这些都是情绪状态、情绪和 a effect \[字幕疑误，可能指 affect\] 的非常有用的指标。因此，有一批情感识别（affect recognition）数据集。还有情感倾向（sentiment），也就是一个人对某个话题有多正面或负面。大家对情感分析（sentiment analysis）很感兴趣。其中很多数据集是在人们面对摄像头评论电影或电视剧

### [1:05:04](https://www.youtube.com/watch?v=zlTCAER4z9A&t=3904s) · b000074

**English**

in front of a camera and expressing their opinions about that movie or TV show. Naturally, you can correlate that with the ratings, how much they liked or disliked that TV show. These are all single person expressions of affect and sentiment. You also have extensions to multi-party. So in dialogue between people, again, a lot of these use TV shows like Friends and Big Bang Theory because the actors are particularly expressive in these TV shows. So in these dialogues at different moments what a person is feeling know what a person is feeling about the other person and this back and forth. So Mel is a data set for multi-party emotion recognition these are still only recognizing a small set either positive or negative or a small set of five or six basic emotions. uh naturally they extended this to question answer but more open-ended question answering about different people's emotions and attitudes and

**中文**

，表达对那部电影或电视剧的看法时整理出来的。自然，你可以将这些表达与评分联系起来，看他们有多喜欢或不喜欢那部电视剧。这些都是单个人的 affect 和 sentiment 表达。也有扩展到多方的情况，也就是人与人之间的对话。同样，其中很多使用 Friends 和 Big Bang Theory 这样的电视剧，因为这些剧中的演员表现力特别丰富。因此，在这些对话的不同时间点，一个人是什么感受，一个人对另一个人是什么感受，以及这种来回互动。所以，Mel \[字幕疑误，可能指 MELD\] 是一个用于多方情绪识别的数据集。这些仍然只识别一个很小的类别集合，要么正面或负面，要么五六种基本情绪。人们自然将其扩展到 question answering，而且是更开放的问答，涉及不同人的情绪、态度、

### [1:06:02](https://www.youtube.com/watch?v=zlTCAER4z9A&t=3962s) · b000075

**English**

judgments and relationships. So this is called social IQ. So in this case yeah what how is the discussion between the woman and the man in the white shirt they are either having a romantic conversation or it's an argument or they're blaming person A is blaming B or B is blaming A. So it can be quite rich beyond just simple classification of sentiment and emotions. Recently we've been quite interested in mimes. MS is an example where uh well the motivation for doing this was that when you look at how people express emotions and a effect. If they're saying something positive or negative as they do 90% of the time, it's actually quite easy to detect whether they're happy or sad. Um so it doesn't become very challenging. So he wanted to look at the long tale of how people express themselves explicitly when they're not speaking. So MS is a good example of this, right? MS these actors are trying

**中文**

判断和关系。这叫 social IQ。例如，在这个例子中，这名女子和穿白衬衫的男子之间的讨论是什么样的？他们是在进行浪漫对话，还是在争吵，或者在责怪，A 在责怪 B，还是 B 在责怪 A？因此，它可以非常丰富，超越简单的 sentiment 和情绪分类。最近，我们对哑剧（mimes）很感兴趣。MS \[字幕疑误，可能指 mimes\] 是一个例子，开展这项工作的动机是，当你观察人们如何表达情绪和 a effect \[字幕疑误，可能指 affect\] 时，如果他们像 90% 的时候那样，说一些正面或负面的话，实际上很容易检测出他们是高兴还是难过。因此，这就不那么有挑战了。所以，他想研究人们表达自己的长尾（long tail）情况，特别是在不说话时如何表达。MS \[字幕疑误，可能指 mimes\] 就是一个很好的例子，对吧？MS 中的这些演员正尝试

### [1:06:57](https://www.youtube.com/watch?v=zlTCAER4z9A&t=4017s) · b000076

**English**

to show their emotions and showcase the story without speaking and using only very subtle expressions and gestures. So I just show some examples over here. Uh in this case we got all these mind videos and we annotated questions and what the answers might be.

**中文**

在不说话的情况下，仅使用非常细微的表情和手势，展示自己的情绪并呈现故事。我在这里展示一些例子。在这个例子中，我们收集了所有这些 mind 视频 \[字幕疑误，可能指 mime videos，即哑剧视频\]，并标注了问题及其可能的答案。

### [1:07:22](https://www.youtube.com/watch?v=zlTCAER4z9A&t=4042s) · b000077

**English**

What do people think the person in the black shirt is holding? Any thoughts? Any guesses? Louder. I heard something. Yeah, something heavy. Probably a stone, right? Round heavy object. He's struggling to lift it. Um so this requires you to kind of do object recognition when the object is not present. We call this grounding the imaginary. Uh that's be a good challenge for computer vision experts. Uh so this is the next video in the sequence. So question is what caused a person reading a book to trip?

**中文**

大家觉得穿黑衬衫的人拿着什么？有什么想法？有什么猜测？大声一点。我听到了一点。对，一个很重的东西。可能是一块石头，对吧？圆的、很重的物体。他正费力地把它举起来。所以，这要求你在物体并不存在时进行某种目标识别（object recognition）。我们称之为“想象内容的落地关联（grounding the imaginary）”。这对计算机视觉（computer vision）专家会是一个很好的挑战。这是序列中的下一个视频。问题是，是什么使读书的人绊倒了？

### [1:08:03](https://www.youtube.com/watch?v=zlTCAER4z9A&t=4083s) · b000078

**English**

Any takers? Yeah. Yes. You got identify that it comes in a sequence, right? is the well first I know that they're acting out a different person uh and that they they tripped over the stone left earlier and this is the third video. How did the person's actions demonstrate his personality?

**中文**

有人想回答吗？对。是的。你必须识别出它属于一个连续序列，对吧？首先，我知道他们正在扮演另一个人，而那个人被之前留下的石头绊倒了。这是第三个视频。这个人的行为如何体现了他的性格？

### [1:08:30](https://www.youtube.com/watch?v=zlTCAER4z9A&t=4110s) · b000079

**English**

Anybody?&gt;&gt; Yes. Mischievous Jolly. Now he's uh reenacting and mocking the other person reading the book and tripping. Uh so here's a fun data set uh again publicly available if you're interested in working on on this. Okay. Embodied and tangible AI. So naturally this extends interactive agents. So agents that can you know process different data take actions. We previously discussed it in the simulated environments like websites and the computers. Uh this brings it to the real world. How do you build systems that can actually take actions, perceive and take actions to complete tasks in the real world? This is the holy grail for for robotics, right? Lots of challenges here. Perception, when you start looking at real world perception, super noisy, super challenging. Uh how do you connect what the model perceives to the actions

**中文**

有人吗？&gt;&gt; 对。调皮，欢乐。现在他正在重演并模仿嘲弄另一个人读书、绊倒的样子。所以，这是一个有趣的数据集，如果你有兴趣研究，它同样是公开可用的。好，具身与有形 AI（embodied and tangible AI）。这自然是 interactive agents 的延伸，也就是能够处理不同数据并采取行动的 agents。我们之前讨论的是网站和电脑这样的模拟环境。这里则将它带到真实世界。如何构建真正能够在现实世界中感知并采取行动、完成任务的系统？这是机器人学的终极目标，对吧？这里有很多挑战。Perception，一旦考察真实世界的 perception，噪声就非常大，也非常困难。如何将模型感知到的东西与需要采取的

### [1:09:26](https://www.youtube.com/watch?v=zlTCAER4z9A&t=4166s) · b000080

**English**

to take? Um there's also an element of making models efficient so they can run on real world hardware. And often times because safety is absolutely critical, you can kind of make a mistake in a on a computer, you know, you might buy something accidentally, but if you bump into somebody or you hurt somebody in the real world as a robot, that's extremely dangerous. So for robustness, these models have to understand and predict how the actions make influence the world. So several cool data sets here. A lot of these data sets which were the precursors to the world models you see today and probably the world models you see today were trained on some of these data sets. I included tasks like navigating through homes. Um so a lot of like these real estate companies actually do these you know these videos where you can step through different houses. So they took some of these videos and the task was to head upstairs, walk past the piano, turn

**中文**

行动联系起来？还有一个方面是提升模型效率，使它们能够运行在现实世界的硬件上。而且，安全通常绝对关键。你可以在电脑上犯个错误，比如不小心买了东西；但如果机器人在现实世界中撞到或伤害了某个人，那就极其危险。因此，为了稳健性（robustness），这些模型必须理解并预测行动如何影响世界。这里有几个很棒的数据集。很多数据集是你们今天看到的 world models 的前身，今天的 world models 很可能也使用过其中一些数据集进行训练。我列出的任务包括在住宅中导航。很多房地产公司会拍摄这类视频，让你能够逐步浏览不同房屋。因此，研究者拿来其中一些视频，任务是：上楼，走过钢琴，在走廊尽头向

### [1:10:22](https://www.youtube.com/watch?v=zlTCAER4z9A&t=4222s) · b000081

**English**

right where the hallway ends. That's the instruction. Can the AI model execute this sequence of actions in this simulated house environment? So that's called uh roomto room. Um it was extended to room across room. Uh much larger multilingual multiple paths seeing whether robots could navigate perceive and navigate through these houses. Uh for some reason people are really excited about whether robots can cook for us. So naturally law of data sets of people cooking so that you can train robot that can cook. Epic kitchens is one example. Large scale data sets of firstperson egocentric vision seeing what they cook or cleaning with audio and with also descriptions of what actions people are taking. Epic kitchens. This is um an example of a subset of these larger data sets that were created called ego 40. Ego standing

**中文**

右转。这就是指令。AI 模型能否在这个模拟住宅环境中执行这一系列动作？这叫 roomto room \[字幕疑误，可能指 Room-to-Room\]。后来它被扩展为 room across room \[字幕疑误，可能指 Room-Across-Room\]，规模更大、多语言、多路径，考察机器人能否在这些住宅中感知并导航。不知道为什么，人们特别期待机器人能不能为我们做饭。所以，自然就有大量人们做饭的数据集，以便训练会做饭的机器人。Epic kitchens 就是一个例子。大规模第一人称 egocentric vision 数据集，观察人们做什么菜，或者打扫卫生，包含音频，也包含对人们所采取行动的描述。Epic kitchens。这是更大规模数据集的一个子集示例，那个更大的数据集叫 ego 40 \[字幕疑误，可能指 Ego4D\]。Ego 代表

### [1:11:17](https://www.youtube.com/watch?v=zlTCAER4z9A&t=4277s) · b000082

**English**

for egocentric. egocentric vision. So in the past couple of years there's been a huge interest in getting participants to wear glasses and to digitize various activities that they do in the world. Um so you see uh this includes interacting with other people playing games including some strategy games. Uh so that's an interesting intersection of social and physical uh and of course lots of environments in the house doing laundry, baking, doing sports and so on. So this could be very interesting data sets for people who are interested in video audio processing while at the same time uh training models that can take actions in these environments with demonstrations of what people actions are.

**中文**

egocentric，自我中心视觉。因此，在过去几年中，大家非常关注让参与者戴上眼镜，将他们在世界中进行的各种活动数字化。你可以看到，这包括与其他人互动、玩游戏，其中也有一些策略游戏。这是社会与物理层面一个有趣的交叉。当然，还有很多家居环境中的活动，比如洗衣、烘焙、运动等等。所以，对视频和音频处理感兴趣，同时也想借助人类行动示范来训练能够在这些环境中采取行动的模型的人来说，这些数据集会很有意思。

### [1:12:08](https://www.youtube.com/watch?v=zlTCAER4z9A&t=4328s) · b000083

**English**

Okay. Uh, one last data set, um, open VLA, open source vision language action models and these RTX projects nowadays for people who are interested in robotics. A lot of data sets that have been released on how these robotic arms um are are manipulating and working with different objects includes vision, audio, propriioception. So that's the internal state and position of the robot arm and some of these have touch information as well. So pressure and force sensing and the final action that the robot took. So a lot of interest in building these large scale open source uh vision language and action models for robots. Right. Uh finally I'll just run through these. I don't have specific data sets for these because these are much more open-ended much more humanentric tasks. So if you're doing projects in this space, uh leave some time to actually

**中文**

好，最后一个数据集，open VLA，开源视觉语言动作模型（vision language action models），以及如今这些 RTX 项目，面向对机器人感兴趣的人。已经发布了很多数据集，记录这些机械臂如何操作和处理不同物体，包括视觉、音频、本体感觉（proprioception），也就是机械臂的内部状态和位置，其中一些还有触觉信息。因此，包括压力和力感测，以及机器人最终采取的动作。所以，大家很关注为机器人构建这些大规模开源 vision language action models。好。最后，我快速过一下这些内容。我没有为这些提供具体数据集，因为这些任务更加开放，也更加以人为中心。因此，如果你在这个方向做项目，请留出一些时间来实际

### [1:13:04](https://www.youtube.com/watch?v=zlTCAER4z9A&t=4384s) · b000084

**English**

you know run user studies in some sense. Give your models to people and see how people use them. So a lot of things we've been discussing so far are mostly about building better AI systems. How do these AI systems also enable better collaboration and synergy with people? What tasks do they help people in? What tasks shouldn't they help people in? what is the right uh sequence of robot and human uh actions so that they together solve the task much faster. I put some references over here and finally ethics and safety. Multimodal is great because you have access to a lot more rich data but biases especially societal biases and unfair generalizations can also manifest in any modality. Right? In text, we have examples of biases that language models generate. For vision, once you're looking at people, you can start detecting race and gender and that comes with different biases. How to train models that leverage the benefits of multimodal while at the same time still

**中文**

开展某种用户研究（user studies）。把模型交给人们，看看人们如何使用。到目前为止，我们讨论的很多事情主要是构建更好的 AI 系统。这些 AI 系统如何也能促进与人的更好协作和协同？它们在哪些任务上帮助人？哪些任务上不应该帮助人？机器人与人的行动应该以怎样的正确顺序进行，才能一起更快地完成任务？我在这里放了一些参考文献。最后是伦理与安全。多模态很棒，因为你能够获取更加丰富的数据，但偏见，尤其是社会偏见和不公平的泛化，也可能在任何模态中出现，对吧？在文本中，我们有语言模型生成偏见的例子。对于视觉，一旦开始观察人，就可以检测种族和性别，而这会带来不同偏见。如何训练模型，发挥多模态优势，同时仍然

### [1:14:02](https://www.youtube.com/watch?v=zlTCAER4z9A&t=4442s) · b000085

**English**

mitigating potential biases from compounding. All right, I will wrap up. Um we will we'll be distributing credits for for your course projects. Uh some of these are API credits. Um so be on the lookout and some advice is you know start um start looking at which of these topics are the most interesting. Uh Canvas should be up and merge between the two groups of students today. So we'll put lecture from Tuesday there. we'll put today's lecture and we're also preparing this you know huge collated spreadsheet starting with the data sets that I've shown here and some other ones and we'll make that um available as a resource to everybody in your class and you're free to also add data sets that you think are are are relevant. Uh main assignments is

**中文**

减轻潜在偏见的叠加？好，我要结束了。我们会为你们的课程项目发放额度，其中一些是 API 额度，请留意。给大家一些建议：开始看看这些主题中哪些最有意思。Canvas 应该今天就会上线，并将两组学生合并。因此，我们会把周二的课程放上去，也会放今天的课程。我们还在准备一个庞大的汇总电子表格，从我在这里展示的数据集和其他一些数据集开始，将其作为资源提供给全班所有人。你们也可以自由添加自己认为相关的数据集。主要的任务是

### [1:15:00](https://www.youtube.com/watch?v=zlTCAER4z9A&t=4500s) · b000086

**English**

that we will put out a project preference form that we release on canvas. So be on a lookout. It will include some basic questions like uh what you know data sets and tasks you're most interested in and if you have any teammates already um and that will will collect all the responses. We again send all of those out to people so you can look at people who have the similar interests and form groups. We'll also release homework one uh early next week. This would be a data set where ideally you have found and started processing and visualizing and labeling some unique multimodal data set of your interest. Right? It can be something that we shown today. It can also be something from your own field of research, something that you're interested in. Um, but we'll have some guiding instructions on general formatting, processing, visualizing, and labeling that data set so that it's ready for subsequent model

**中文**

我们会在 Canvas 上发布一份项目意向表，请留意。它会包含一些基本问题，例如你最感兴趣的数据集和任务是什么，以及是否已经有队友。我们会收集所有回复，再把它们发送给大家，方便你们寻找兴趣相似的人组队。我们也会在下周初发布作业一。这会涉及一个数据集，理想情况下，你已经找到一个自己感兴趣的独特多模态数据集，并开始处理、可视化和标注它，对吧？可以是我们今天展示过的，也可以来自你自己的研究领域，是你感兴趣的东西。我们会提供关于该数据集一般格式、处理、可视化和标注的指导说明，让它为后续模型

### [1:15:56](https://www.youtube.com/watch?v=zlTCAER4z9A&t=4556s) · b000087

**English**

training and analysis. And finally, next Tuesday, it will be a tutorial led by uh the TAs on various methods for processing, visualizing and labeling data and also a gentle introduction to to PyTorch and running ML experiments. Uh that will give you good preparation for homework one which will be done throughout next week and the following week. All right, there's still um five minutes before the class officially ends, but please mingle around, meet people, and that can be useful for finding students with common interests for the projects. Thanks everyone.

**中文**

训练和分析做好准备。最后，下周二将由助教带领一节教程课，介绍处理、可视化和标注数据的各种方法，也会循序渐进地介绍 PyTorch 和如何运行机器学习（ML）实验。这将帮助你们为作业一做好准备，作业一会在下周和再下一周完成。好，距离正式下课还有五分钟，请大家四处交流，认识其他人，这会帮助你们找到对项目有共同兴趣的同学。谢谢大家。
