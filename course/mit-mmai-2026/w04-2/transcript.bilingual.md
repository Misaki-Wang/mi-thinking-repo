# Lecture 5 – Multimodal Alignment (MIT How to AI Almost Anything/Multimodal AI, Spring 2026)

_Bilingual transcript · 双语讲稿_

- Channel: Paul Liang
- Source: [YouTube](https://www.youtube.com/watch?v=u-H43tRgYJg)
- Duration: 1:23:04
- Caption source: automatic
- Status: complete
- Chinese translation: 103/103
- Translation provider: codex
- Generated: 2026-09-07T07:53:12+00:00

## Transcript · 讲稿

### [00:00](https://www.youtube.com/watch?v=u-H43tRgYJg&t=0s) · b000001

**English**

Welcome back. Let's get started. So, several announcements uh before we begin. So, thank you all for submitting your project proposals. Uh we are taking all the project proposals. We're making a spreadsheet and we'll assign several mentors for every project. Uh either myself or the TAs and the hope is that uh we can meet with you all at least once a week to track progress on the projects. Uh so those project mentors will be announced to all the teams uh this week. Uh hopefully you can meet with us every week to help you all in fact progress. Uh just also for planning purposes as I mentioned we have some credits. Um you can try to use some of these KI models. They claim to be quite state-of-the-art multimodal models. So we have 40 teams about $50 of credits for for Kimi and then 40 teams with $40 of credits for anything else that you

**中文**

欢迎回来。我们开始吧。那么，开始之前先通知几件事，呃。谢谢大家提交项目提案。呃，我们正在整理所有项目提案，制作一个电子表格，并会为每个项目分配几位导师。呃，要么是我，要么是助教（TAs），希望我们每周至少能和大家见一次面，跟踪项目进度。呃，这些项目导师会在本周通知各个小组。呃，希望大家每周都能和我们见面，帮助大家实际推进项目。呃，另外也是为了方便规划，正如我提过的，我们有一些额度。嗯，你们可以试着使用其中一些 KI 模型 \[字幕疑误，可能指 Kimi\]。他们声称这些是相当先进的多模态模型（multimodal models）。我们有 40 个小组，每组大约有 $50 的 Kimi 使用额度，另外还有 40 个小组，每组有 $40 的额度，可以用于你们

### [00:56](https://www.youtube.com/watch?v=u-H43tRgYJg&t=56s) · b000002

**English**

need for the course including compute GPUs or other API calls. Okay? And make sure to keep working through homework 2. Uh that'll be due next Wednesday. Um and then we'll have homework three out after that. All right. Any questions about these announcements? Yes,&gt;&gt; the credits are uh delegated only for the projects, right? Or is it should it be approximately?&gt;&gt; Uh you can you can use them if you want to use for the homeworks, but I think this will be the the maximum that we can give the credits. All right. So, let me just quickly recap a little bit of multimodal fusion. Um I think it went fairly quickly on Tuesday. Let me just recap in a couple of slides before I move on to this next topic that we'll be talking about which is on alignment. But as you recall, fusion is all about taking in different data

**中文**

课程所需的其他任何东西，包括计算用的 GPU 或其他 API 调用。好吗？另外，记得继续完成作业 2。呃，截止时间是下周三。嗯，之后我们会发布作业三。好。大家对这些通知有什么问题吗？请说。&gt;&gt; 这些额度，呃，只分配给项目使用，对吧？还是说应该大致……？&gt;&gt; 呃，如果你们想用在作业上，也可以用，但我想这就是我们能提供的最高额度了。好。那么，我快速回顾一下多模态融合（multimodal fusion）。嗯，我觉得周二讲得有点快。在进入下一个要讨论的话题，也就是对齐（alignment）之前，我先用几张幻灯片回顾一下。不过大家应该记得，融合（fusion）就是接收不同的数据

### [01:52](https://www.youtube.com/watch?v=u-H43tRgYJg&t=112s) · b000003

**English**

modalities and learning some joint representation. And ideally, this joint representation summarizes the ways that these different data modalities interact with each other. And we saw a spectrum where first you can take it for example really good encoders for your modality for passing it through a vision encoder for images passing it through a text encoder for your text to get features right these features summarize some semantic content so they're already quite homogeneous then the fusion can do less heavy lifting the fusion can be more lightweight we learn disjoint representation we call that fusion with abstract modalities at the same time another paradigm is to directly do fusion with raw modalities where instead of defining encoders for each you start with your raw data for your modalities which are more heterogeneous and both representation learning and fusion between the modalities are done together. So now the fusion does more heavy lifting. Uh these are can also be

**中文**

模态（modalities），并学习某种联合表示（joint representation）。理想情况下，这种 joint representation 概括了这些不同数据模态彼此交互的方式。我们看到了一个连续谱：首先，你可以采用适合某个模态的非常好的编码器（encoders），例如把图像送入视觉编码器（vision encoder），把文本送入文本编码器（text encoder），来得到特征，对吧？这些特征概括了一些语义内容，所以已经相当同质了。那么 fusion 需要承担的工作就更少，可以更加轻量。我们学习不相交的表示（disjoint representation）\[字幕疑误，可能指 joint representation\]，我们称之为抽象模态融合（fusion with abstract modalities）。与此同时，另一种范式是直接对原始模态进行融合（fusion with raw modalities）：不再为每个模态定义编码器，而是从模态的原始数据开始，这些数据更具异质性，表示学习（representation learning）和模态间的 fusion 一起完成。因此，这时 fusion 承担了更多工作。呃，这些也可以

### [02:50](https://www.youtube.com/watch?v=u-H43tRgYJg&t=170s) · b000004

**English**

called kind of more late fusion where you first extract features and fusion is done later in the model or early fusion in which fusion happens early on in the model more close to the data and there's more space for how the fusion operates. Uh several pros and cons for each. Late fusion typically means the fusion is more lightweight can be more interpretable uh but it cannot be that expressive. Early fusion gives the opportunity for the fusion to be more expressive, but usually the fusion is larger and more complex and less understandable. And then as a quick recap, we also saw several basic concepts for fusing different representations. Uh we saw the basic concept where focusing simply on the univariat case we saw uh linear fusion and linear fusion typically involves a constant with some error term additive terms which are just weighted functions of modality one plus weighted

**中文**

称为比较偏后期融合（late fusion）的方式，也就是先提取特征，再在模型较后的位置做 fusion；或者称为早期融合（early fusion），也就是 fusion 发生在模型较早、离数据更近的位置，fusion 如何运作也有更多空间。呃，两者各有一些优缺点。late fusion 通常意味着 fusion 更轻量，也可能更具可解释性，呃，但表达能力没那么强。early fusion 让 fusion 有机会具备更强的表达能力，但通常 fusion 更大、更复杂，也更难理解。再快速回顾一下，我们还看到了融合不同表示的几个基本概念。呃，我们看了基本概念，先只关注单变量（univariate）的情况，我们看了线性融合（linear fusion）。linear fusion 通常包含一个常数、某个误差项，以及加性项，也就是模态一的加权函数，加上模态

### [03:47](https://www.youtube.com/watch?v=u-H43tRgYJg&t=227s) · b000005

**English**

functions of modality 2. That's a simple way of doing fusion and it's at the same time still very powerful because you have different weights that are assigned to different modalities. Multiplicative fusion further generalizes this where now you start considering multiplicative interactions between A and B. Right? And we saw the example where this can be seen as the weight for B is W3 \* X A. So the weight which modality B takes in the fusion actually depends on X A and vice versa the weight of X A is W3 \* X of B. The weight for A depends on B. So now you get these nonlinear relationships in multiplicative fusion and usually it's a good guideline to have both lower order terms so just additive functions uh and multiplicative terms. So these are the higher order interactions between your modalities. We saw the case when you go to higher dimensions uh this can become more

**中文**

2 的加权函数。这是一种简单的 fusion 方式，同时仍然很强大，因为不同模态会被赋予不同权重。乘法融合（multiplicative fusion）进一步推广了这一点，现在开始考虑 A 和 B 之间的乘性交互，对吧？我们看了一个例子，可以把它看作 B 的权重是 W3 \* X A。因此，模态 B 在 fusion 中占有的权重实际上取决于 X A；反过来，X A 的权重是 W3 \* X of B。A 的权重取决于 B。因此，在 multiplicative fusion 中就得到了这些非线性关系。通常，一个不错的指导原则是既保留低阶项，也就是加性函数，呃，也保留乘法项。这些就是模态之间的高阶交互（higher order interactions）。我们看了扩展到更高维的情况，呃，这样可以变得更有

### [04:43](https://www.youtube.com/watch?v=u-H43tRgYJg&t=283s) · b000006

**English**

expressive but also more complex. So you saw this trick of adding a one behind your modalities doing this outer product which is basically your your vector transpose times a vector. So 5x 1 \* 1x 5 gives you this 5x5 matrix of which 4x4 are your pair-wise uh biodal interactions. You have two 4x1's which are your two unimodal interactions and you have the one by one which is the bias. Right? So adding this one uh as a constant to your vector and then doing this outer product is a trick to get both a higher order and lower order interactions in your data. And in the three modality case, we have this uh quite beautiful tensor that you can build where there's a cube of these 4x4x4 trrimodal interactions and you have your faces which are 4x4 pair-wise

**中文**

表达能力，但也更复杂。你们看到了这个技巧：在模态向量末尾添加一个 1，然后做外积（outer product），基本上就是向量转置乘以一个向量。所以 5x 1 \* 1x 5 得到这个 5x5 矩阵，其中 4x4 是成对的，呃，biodal \[字幕疑误，可能指 bimodal，双模态\] 交互。有两个 4x1，分别是两个单模态（unimodal）交互，还有一个 1x1，是偏置（bias）。对吧？所以，把这个 1 作为常数加入向量，然后做 outer product，是一种同时获取数据中高阶和低阶交互的技巧。而在三个模态的情况下，我们可以构建这个，呃，相当漂亮的张量（tensor），其中有一个由 4x4x4 的 trrimodal \[字幕疑误，可能指 trimodal，三模态\] 交互组成的立方体，还有各个面，它们是 4x4 的成对

### [05:38](https://www.youtube.com/watch?v=u-H43tRgYJg&t=338s) · b000007

**English**

biodal between AB, AC, and BC. You have your three unit modal vectors and you have the the one uh vector hidden at the back. Right? So this is great but sometimes this can also get very large and very expensive. So these are you know five dimensional vectors this becomes 5x 5x 51 125 right. So this tensor itself can be large and the more multiplicative interactions you do among your data the obviously the more dimension uh the higher the dimension the resulting factor would be and that's where we saw this idea of essentially doing low rank fusion. This idea that you want to do these multiplicative interactions and form these higher order tensors but you don't have to keep all the dimensions. You can do low rank approximations. uh so you can approximately represent

**中文**

biodal \[字幕疑误，可能指 bimodal，双模态\]，分别位于 AB、AC 和 BC 之间。有三个 unit modal \[字幕疑误，可能指 unimodal，单模态\] 向量，还有那个，呃，藏在后面的 1 向量。对吧？这很好，但有时它也会变得很大、计算代价很高。所以，这些是五维向量，这就变成了 5x 5x 51 125 \[字幕疑误，可能指 5x5x5，125\]，对吧？所以这个 tensor 本身可能很大，而且在数据之间做的乘性交互越多，显然维度就越……呃，得到的因子的维度就越高。这就是我们看到的低秩融合（low rank fusion）这一思路的由来。其想法是，你希望进行这些乘性交互并形成这些高阶 tensor，但不必保留全部维度。可以做低秩近似（low rank approximations）。呃，因此你可以近似表示

### [06:33](https://www.youtube.com/watch?v=u-H43tRgYJg&t=393s) · b000008

**English**

these higher order interactions but still stay quite efficient and we saw this animation where let's say you have two modalities you are doing this outer product with the one that's your Z representation and not only is Z big the other big bottleneck is the weight matrix W on top of Z that brings it to the next dimension H right so if Z is 5 by 5 that's 25 If this H is three, then this W is 5 by 5 by 3, right? So even larger. And we saw how we could use low rank approximations instead of learning this entire W, rather view W as a summation of these little vectors that have taken out of product with each other. So each of these will be 5 by3 outer product with 5 by3 that gives you 5 by 5 by 3, right?

**中文**

这些高阶交互，同时仍然保持相当高的效率。我们看了这个动画：假设有两个模态，加入那个 1 后做 outer product，得到你的 Z 表示。不仅 Z 很大，另一个大的瓶颈是 Z 上方的权重矩阵 W，它把 Z 映射到下一个维度 H，对吧？所以，如果 Z 是 5x5，就是 25。如果这个 H 是三，那么 W 就是 5x5x3，对吧？所以更大。我们看了如何使用 low rank approximations：不学习整个 W，而是把 W 看成这些小向量彼此进行 out of product \[字幕疑误，可能指 outer product，外积\] 后的求和。所以，其中每一个都是 5x3 与 5x3 做 outer product，得到 5x5x3，对吧？

### [07:29](https://www.youtube.com/watch?v=u-H43tRgYJg&t=449s) · b000009

**English**

And how many of these little vectors that you add up essentially is the rank of that tensor. Right? Two of them means you're only considering these these tensors or rank two. Three of them is you're considering only tensors or rank three. Uh and essentially in most of machine learning even though your your matrices are very high in dimension in practice when you optimize these matrices and these parameters they end up with pretty low rank solutions. So that's a easy way of reducing the dimensionality and becoming more efficient while still maintaining good amount of precision and that's what we can get with low rank fusion where you can essentially use these lower rank factors multiply them with your data. You can read these papers to show that uh this computation is equivalent. So you get all the benefits of these higher order interactions while only approximating

**中文**

你把多少个这样的小向量加起来，基本上就是那个 tensor 的秩（rank）。对吧？两个意味着你只考虑这些 tensor，或者说秩为二。三个意味着你只考虑秩为三的 tensor。呃，基本上在机器学习的大多数情况下，尽管矩阵的维度非常高，但在实践中优化这些矩阵和参数时，最终得到的解往往秩很低。因此，这是一种降低维度、提升效率，同时仍然保持相当不错精度的简单方法。这就是 low rank fusion 能带来的：基本上可以用这些低秩因子乘以数据。你们可以阅读这些论文，里面说明，呃，这种计算是等价的。因此，你获得了这些高阶交互的所有好处，同时只用这些

### [08:23](https://www.youtube.com/watch?v=u-H43tRgYJg&t=503s) · b000010

**English**

them with these uh low rank factors. Okay. And you'll get some practice in your homework. Um this can be implemented in a differentiable manner in PyTorch. You can optimize what that rank is. Right? These this rank goes to the full dimension of the matrix. you recover all possible weight matrices but in practice usually low rank is sufficient. Any questions about these higher order interactions fusion and these low rank approximations.

**中文**

呃，低秩因子来近似它们。好。你们会在作业中做一些练习。嗯，这可以在 PyTorch 中以可微（differentiable）的方式实现。你可以优化这个 rank。对吧？这个 rank 达到矩阵的完整维度时，就恢复了所有可能的权重矩阵，但在实践中，通常低秩就足够了。大家对这些高阶交互的 fusion，以及这些 low rank approximations，有什么问题吗？

### [09:04](https://www.youtube.com/watch?v=u-H43tRgYJg&t=544s) · b000011

**English**

Okay. And then we saw um you know so far in these in these methods each of these weights right that we learned that weight how much a modality contributes to the fusion is static and what that means is that it is the same weight w1 always applied to x plus the same weight w2 always applied to xb right so we then saw uh these weights extended to become more dynamic so we call this ga fusion where perhaps the weight for XA should depend itself on what XA is and the weight for XB should depend itself on what W XB is right and it could also depend on the other modality as well. So this gives you a formulation where you're doing fusion in the additive setting. Your output Z is still a weighted function times X A except it's

**中文**

好。然后我们看到，嗯，到目前为止，这些方法中学到的每个权重，也就是决定一个模态对 fusion 贡献多少的权重，都是静态的（static）。这意味着，始终把同一个权重 w1 应用于 x，再把同一个权重 w2 应用于 xb，对吧？所以接下来我们看到，把这些权重扩展得更加动态（dynamic），我们称之为 ga fusion \[字幕疑误，可能指 gated fusion，门控融合\]。也许 XA 的权重本身应该取决于 XA 是什么，而 XB 的权重本身应该取决于 W XB 是什么，对吧？它也可以取决于另一个模态。因此，这给出了一种在加性设定下进行 fusion 的形式。输出 Z 仍然是某个权重函数乘以 X A，只不过它

### [09:59](https://www.youtube.com/watch?v=u-H43tRgYJg&t=599s) · b000012

**English**

not a static weight W1 that is the same for all XA but rather a function that depends on the current X A and XB. Right? So this function can be learned depending on what X A and XB is. That output could be different. Uh likewise the weight for XB could depend on another function that is learned G of B that depends on what the current A and B is. So the intuition here is that depending on what it is sometimes A is more important sometimes B is more important we should not give global weights to each one of them but you want to have weights that depend on the current importance as scored by these uh GA and GB models. So these A and G and GB can be seen as attention functions and the gating instead of being a single weight now depends per data point that you give to the model.

**中文**

不再是对所有 XA 都相同的静态权重 W1，而是一个取决于当前 X A 和 XB 的函数。对吧？因此可以学习这个函数，根据 X A 和 XB 是什么，其输出可能不同。呃，同样，XB 的权重也可以取决于另一个学到的函数 G of B，这个函数取决于当前 A 和 B 是什么。所以这里的直觉是，视具体情况而定，有时 A 更重要，有时 B 更重要。我们不应该给它们各自分配全局权重，而是希望权重取决于这些，呃，GA 和 GB 模型评出的当前重要性。因此，这些 A 和 G 和 GB 可以看作注意力函数（attention functions），而门控（gating）不再是单一权重，现在会随着输入模型的每一个数据点而变化。

### [10:56](https://www.youtube.com/watch?v=u-H43tRgYJg&t=656s) · b000013

**English**

By the way, somebody asked a question. So um all of these slides are on Canvas and uh they're they're kind of uploaded before class. So this is on Canvas. And a quick note about the the website. The website is meant to be public facing uh so it's not going to be updated as sporadically and I have to edit all the videos before I can put them for the public. So all these slides and recordings and syllabus and homeworks are all on canvas. That will be our primary medium uh where everything is centralized.

**中文**

顺便说一下，有人问了个问题。嗯，所有这些幻灯片都在 Canvas 上，呃，基本上课前就会上传。所以这些在 Canvas 上。另外简单说明一下网站。网站是面向公众的，呃，所以不会那么零散地更新，而且我必须先编辑所有视频，才能公开发布。因此，所有幻灯片、录像、教学大纲和作业都在 canvas 上。那会是我们的主要媒介，呃，所有内容都集中在那里。

### [11:29](https://www.youtube.com/watch?v=u-H43tRgYJg&t=689s) · b000014

**English**

Great. Any questions about dynamic fusion? Yes. when you learn these. So this uh establishing like GB is that involves some domain knowledge like for example someone that that person that presented the other day about uh like ocean dynamics and things like that. Would that involve having some like coming in with some knowledge about that function do or is it very much just like attention determining kind of with no yeah like adop knowledge?&gt;&gt; Yeah, I mean it could be both. It could be both um purely data driven. So this recovers as you've already pointed out some of these attention functions that we see today. It could also depend um on some domain knowledge. Uh on Tuesday, I'm just recapping here. But on Tuesday, we also further gave this example where this GA and GB need not be symmetric, right? So you could have a primary modality A. Nowadays, language is very

**中文**

很好。大家对动态融合（dynamic fusion）有什么问题吗？请说。学习这些时，这个，呃，建立像 GB 这样的东西，会涉及领域知识（domain knowledge）吗？比如前几天做报告的那个人，讲了，呃，海洋动力学之类的内容。这是否需要事先对那个函数的作用有些了解，还是基本上就像 attention 那样决定，不需要，嗯，像 adop knowledge \[字幕疑误，含义不明\]？&gt;&gt; 是的，我想两者都可以。两者都可以，嗯，完全由数据驱动。所以，正如你已经指出的，这可以涵盖我们今天看到的一些 attention functions。它也可以依赖，嗯，一些 domain knowledge。呃，周二，我这里只是在回顾，但周二我们还进一步举过例子，GA 和 GB 不必是对称的，对吧？你可以有一个主要模态 A。如今，语言非常

### [12:25](https://www.youtube.com/watch?v=u-H43tRgYJg&t=745s) · b000015

**English**

dominant. You have very good language models and language representations. So I'm not going to modify language too much but I'm going to only modify and learn this GA and GB for my audio and video modalities right so that is some sort of domain knowledge based on the fact that language is very dominant for communication and I just want to learn these gates for the non-verbal audio and video yeah so it need not be symmetric need not be fully data driven absolutely there's space for for some domain knowledge in this

**中文**

占主导。我们有非常好的语言模型（language models）和语言表示（language representations）。所以我不会过多修改语言，而只针对音频和视频模态修改并学习 GA 和 GB，对吧？这就是某种 domain knowledge，基于语言在交流中非常占主导这一事实，我只想为非语言的音频和视频学习这些门控。是的，所以它不必对称，也不必完全由数据驱动。这里绝对有融入一些 domain knowledge 的空间。

### [12:58](https://www.youtube.com/watch?v=u-H43tRgYJg&t=778s) · b000016

**English**

Okay, so these are all examples of um of of you know how we can inject and how we can design these fusion methods very carefully and of course um we also saw the other extreme being this early fusion. We contaminate your data or your features very early on and you let the fusion and your prediction model do most of the heavy lifting and try to design uh models that you hope are able to capture that fusion. uh also a very straightforward approach easy to implement should probably try out for any application that you're working on. Uh so concatenate at the data level or feature level and and just design what is treat them as basically one single modality from then on afterwards and design the best model that is fusing and predicting them. A big question of course then becomes what is this model learning right? We're hoping that your model will learn something interesting and something

**中文**

好，这些都是，嗯，关于我们如何注入、如何仔细设计这些 fusion 方法的例子。当然，嗯，我们也看到了另一个极端，也就是 early fusion。很早就把数据或特征混杂起来，让 fusion 和预测模型承担大部分工作，并尝试设计一些你希望能捕获这种 fusion 的模型。呃，这也是一种非常直接、容易实现的方法，你们做任何应用时大概都应该尝试一下。呃，所以在数据层面或特征层面做拼接（concatenate），然后设计……基本上从此把它们当作一个单一模态，设计能融合并预测它们的最佳模型。当然，接下来一个大问题就是：这个模型到底学到了什么，对吧？我们希望模型能学到一些有意思的东西，以及一些

### [13:56](https://www.youtube.com/watch?v=u-H43tRgYJg&t=836s) · b000017

**English**

nonlinear about the how the modalities interact. Uh but how can we measure whether the model is actually successful at doing that? So I want to highlight a paper that I like very much it falls under this bucket of not just developing new methods but really trying to probe and understand how existing methods perform. So it is a paper that's called you know how to measure what non-additive interactions are learned by your model. So it assumes that you have some function f which is your fusion function that you've already learned on top of a and b and this function f predicts your label. Right? The goal to analyze how much non-additive complex interactions this model learns is to simply project this model in to the simplest and closest additive function.

**中文**

关于模态如何交互的非线性内容。呃，但我们如何衡量模型是否真的成功做到了这一点？所以，我想重点介绍一篇我非常喜欢的论文，它属于这样一类工作：不仅开发新方法，而是真正尝试探查和理解现有方法的表现。这篇论文讲的是，如何衡量模型学到了哪些非加性交互（non-additive interactions）。它假设你有某个函数 f，也就是已经在 a 和 b 上学到的 fusion 函数，函数 f 用来预测标签，对吧？要分析这个模型学到了多少非加性的复杂交互，目标就是把这个模型投影到最简单、最接近的加性函数（additive function）上。

### [15:02](https://www.youtube.com/watch?v=u-H43tRgYJg&t=902s) · b000018

**English**

dance party going on over there. So how do you project this function f arbitrary? It can be anything that you learned neuronet networks, transformers, huge foundation models. How can we find the nearest approximation of this function that is simply an additive combination f of a on x a plus f of b on xb? Right? If I can find this closest additive function and measure the difference to that function, then I can summarize how much of my function was just purely additive, which is this f of a plus f of b and how much of it was non-additive that was actually learning any of these complex tensors or dynamic fusions between your modalities. So it turns out from statistics there is actually a very simple way of finding this closest additive function and this is what it looks like. So the closest additive function is the summation of two terms of course because it's

**中文**

那边在开舞会。所以，如何投影这个任意函数 f？它可以是你学到的任何东西：neuronet networks \[字幕疑误，可能指 neural networks，神经网络\]、transformers、巨大的基础模型（foundation models）。我们如何找到这个函数最接近的近似，而且只是一个加性组合，即作用于 x a 的 f of a，加上作用于 xb 的 f of b？对吧？如果我能找到这个最近的加性函数，并测量与该函数的差异，就能概括我的函数有多少只是纯加性的，也就是这个 f of a 加 f of b，又有多少是非加性的，真正学习了模态之间的这些复杂 tensor 或 dynamic fusions。结果是，在统计学中，实际上有一种非常简单的方法来寻找这个最近的加性函数，它看起来就是这样。最近的加性函数当然是两项之和，因为它是

### [15:58](https://www.youtube.com/watch?v=u-H43tRgYJg&t=958s) · b000019

**English**

additive and the first term is you take your fusion f of x a plus xb uh sorry f of xa and xb and take an expectation over xb expectation basically means feed all possible xbs that you have in your data set into this model and take an average over all your xbs right by definition taking expectation over xb marginalizes xb B out and that gives you a function over f of a and x of a. Uh likewise for the other term I'm going to take an expectation of the fusion over all x of a right feed in all possible x a see what the output is and take an average over all xas again by definition that marginalizes x a away from the function and that gives you a function f of b only over modality b right so you can actually show that this is the nearest uh additive function

**中文**

加性的。第一项是，取 fusion f of x a plus xb，呃，抱歉，是 f of xa and xb，然后对 xb 取期望（expectation）。expectation 基本上就是把数据集中所有可能的 xb 输入这个模型，再对所有 xb 的结果取平均，对吧？根据定义，对 xb 取 expectation 会把 xb B 边缘化掉（marginalize），这样就得到一个关于 f of a 和 x of a 的函数。呃，同样，对于另一项，我会对 fusion 关于所有 x of a 取 expectation，对吧？输入所有可能的 x a，看看输出是什么，然后对所有 xa 的结果取平均。再说一次，根据定义，这会从函数中边缘化掉 x a，从而得到只关于模态 b 的函数 f of b。对吧？所以实际上可以证明，这是最近的，呃，加性函数

### [16:54](https://www.youtube.com/watch?v=u-H43tRgYJg&t=1014s) · b000020

**English**

that works for any particular input function f that you And visually it looks something like this right it can take uh all these sort of complex functions like neuron nets uh pre-trained models like your multimodal vert pre-trained models or language models it can even take you know svms and other kernel functions essentially projecting them into the space of functions that are purely additive functions f of a plus f of b uh so they call this emap or empirically multimodal additive projection Yes.

**中文**

它适用于你所……的任何输入函数 f。直观上，它看起来像这样，对吧？它可以接收各种复杂函数，比如 neuron nets \[字幕疑误，可能指 neural networks，神经网络\]、预训练模型（pre-trained models），比如多模态 vert \[字幕疑误，可能指 BERT\] 预训练模型或语言模型，甚至也可以接收 svms 和其他核函数（kernel functions），本质上把它们投影到纯加性函数 f of a 加 f of b 所构成的函数空间。所以他们把这个叫作 emap，或者 empirically multimodal additive projection \[字幕疑误，可能指 empirical multimodal additive projection，经验多模态加性投影\]。请说。

### [17:29](https://www.youtube.com/watch?v=u-H43tRgYJg&t=1049s) · b000021

**English**

What you comput?&gt;&gt; Um it depends on distance function but you can think about as nearest and in the square distance between the yhat produced by the function f with the yhat produced by this space of um additive functions. So it's the claim that across all distance functions this map gives you the&gt;&gt; yeah I mean I didn't I don't know whether it's across all distance functions but the paper includes uh some proof of this right for some distance functions.

**中文**

&gt;&gt; 你计算什么……？&gt;&gt; 嗯，这取决于距离函数（distance function），但你可以把它理解为最近，也就是函数 f 产生的 yhat 与这个加性函数空间产生的 yhat 之间的平方距离。&gt;&gt; 所以这个论断是说，对所有距离函数，这个映射都会给出……&gt;&gt; 是的，我的意思是，我没有……我不知道是不是适用于所有距离函数，但论文包含了一些证明，对吧，针对某些距离函数。

### [18:00](https://www.youtube.com/watch?v=u-H43tRgYJg&t=1080s) · b000022

**English**

So that means in practice we can take some fancy fusion function that you've learned or claim to be good and you can do this EMAP projection into your f of a plus f of b where each of them are expectations over the other modality and of course there'll be some difference there'll be some difference mu which is the difference in the predictions that you did not capture using this additive projections another question is how much of these models are captured using an additive function and how How much of it is not? So how much is new? So they took a bunch of models uh some of these are very complex models and they find that surprisingly you can capture quite a bit using just the additive approximation. So that's measured by the difference in performance between the original fusion model and the additive projection which is this line over here called EMAP. So

**中文**

所以这意味着，在实践中，我们可以拿一个你学到的、很花哨或者声称很好的 fusion 函数，对它进行 EMAP 投影，得到 f of a 加 f of b，其中每一项都是对另一个模态取 expectation。当然会有一些差异，会有某个差异 mu，也就是这种加性投影没有捕获到的预测差异。另一个问题是，这些模型有多少能被加性函数捕获，又有多少不能？也就是有多少是新的？于是他们拿了一批模型，呃，其中一些非常复杂，结果发现，令人惊讶的是，只用加性近似就能捕获相当多的内容。衡量方法是原始 fusion 模型与加性投影之间的性能差异，这里的这一行叫作 EMAP。所以

### [18:56](https://www.youtube.com/watch?v=u-H43tRgYJg&t=1136s) · b000023

**English**

sometimes you see 91.3 drop to 91.1. Sometimes you see 74.4 drop to 74.2. You see uh 53.4 drop to 51.0. So you're seeing some performance drop when you start doing this additive approximation. But surprisingly sometimes it is not too much. Right? So this is um this is a hard truth. Right? Sometimes you try to design really complexion. You think you're successful. You think you have this beautiful fusion algorithm. Well, it's always good to do a check to see how much of it is simply learning good additive models of your data and how much of it is actually going beyond additive and learning these complex interactions. Right? I mean there's two reasons why it's not successful at learning these complex interactions. One possibility is that these complex interactions are just not present in your data to begin with

**中文**

有时你会看到 91.3 降到 91.1。有时会看到 74.4 降到 74.2。还有，呃，53.4 降到 51.0。因此，开始做这种加性近似时，确实会看到一些性能下降。但令人惊讶的是，有时下降并不大。对吧？所以这是，嗯，一个残酷的事实，对吧？有时你尝试设计真的很 complexion \[字幕疑误，可能指 complex，复杂的东西\]。你觉得自己成功了，觉得有了一个漂亮的 fusion 算法。不过，最好始终检查一下，它有多少只是在学习数据中良好的加性模型，又有多少真正超越了加性，学到了这些复杂交互。对吧？我的意思是，它没能成功学到这些复杂交互，有两个原因。一种可能是，数据中本来就不存在这些复杂交互

### [19:52](https://www.youtube.com/watch?v=u-H43tRgYJg&t=1192s) · b000024

**English**

and your data set to predict a label can be pretty much solved using adequate combinations. That's one hypothesis. The data itself is not complex enough. Second hypothesis is that the data is complex enough but the way that you are designing or training the model means the model is not successful at capturing those complex interactions. uh you can get some intuition also on uh what the performance numbers look like right if in this case I think um I don't know why this INT data set I don't remember what it was but in this case the performance is already 91.3 it dropped to 91.1 that means probably this data set doesn't have complex interactions so both your multimodal models and your additive models are already very good more than 90%. this other data set for example TV vis um the best additive model is 51 the best multimodal model is 53.4 more probably

**中文**

而在你的数据集上预测标签，基本上用 adequate combinations \[字幕疑误，可能指 additive combinations，加性组合\] 就能解决。这是一种假设：数据本身不够复杂。第二种假设是，数据足够复杂，但你设计或训练模型的方式，使得模型没能成功捕获那些复杂交互。呃，从性能数字中也能得到一些直觉，对吧？在这个例子里，我想，嗯，我不知道为什么这个 INT 数据集，我不记得它是什么了，但这里性能已经是 91.3，降到了 91.1，这意味着这个数据集可能没有复杂交互，因此多模态模型和加性模型都已经非常好，超过 90%。另一个数据集，比如 TV vis，嗯，最好的加性模型是 51，最好的多模态模型是 53.4，更可能

### [20:48](https://www.youtube.com/watch?v=u-H43tRgYJg&t=1248s) · b000025

**English**

means that this data set contains complex interactions but uh these folks are not successful at training a model that capture these interactions otherwise you'd be getting 80 90% instead of 53% performance.

**中文**

意味着这个数据集包含复杂交互，但，呃，这些人没能成功训练出捕获这些交互的模型，否则性能应该达到 80、90%，而不是 53%。

### [21:07](https://www.youtube.com/watch?v=u-H43tRgYJg&t=1267s) · b000026

**English**

Okay. So these kind of um these kind of sanity checks uh these kind of diagnostic tools are always very useful uh because we don't want to just train models but we also want to really understand what these models are learning. Any questions about this?

**中文**

好。因此，这类，嗯，这类合理性检查（sanity checks）、诊断工具（diagnostic tools）总是很有用，呃，因为我们不仅想训练模型，还想真正理解这些模型在学习什么。大家对此有什么问题吗？

### [21:30](https://www.youtube.com/watch?v=u-H43tRgYJg&t=1290s) · b000027

**English**

Yeah.

**中文**

请说。

### [21:36](https://www.youtube.com/watch?v=u-H43tRgYJg&t=1296s) · b000028

**English**

Well, additive fusions themselves can also be very powerful, right? They they give these kind of late fusion approaches where you just, you know, put A through a classifier, B through a classifier, add them up. If they work well, like for example, in these cases, they're at 91% performance. Yes, we should definitely use them. They're efficient, they're interpretable. Um, they of course don't work well in some settings. So, that's one story, right? Sometimes they don't work well. But I think a bigger more important story here is that uh one should not just design models that seem complex and and seem to work well on the surface without really understanding what they're learning deep inside. And therefore I like these kind of works which are challenge the assumptions and go back and quantify exactly what these models are learning and in this case challenging the hypothesis that you need all these complex interactions when in fact they don't seem to be very prominent in practice. Yes.

**中文**

嗯，加性融合（additive fusions）本身也可以很强大，对吧？它们提供了这种 late fusion 方法：把 A 输入一个分类器（classifier），把 B 输入一个 classifier，然后相加。如果效果很好，比如这些例子里性能达到 91%，那么是的，我们当然应该使用它们。它们高效、可解释。嗯，当然，在某些场景中它们效果不好。所以这是一方面，对吧？有时它们不好用。但我认为这里更大、更重要的一点是，我们不应该只设计表面上看起来复杂、效果不错的模型，却不真正理解它们内部到底在学什么。因此，我喜欢这类挑战假设、回过头精确量化模型究竟学到了什么的工作。在这个例子中，它挑战了你需要所有这些复杂交互的假设，因为实际上，这些交互在实践中似乎并不很突出。请说。

### [22:30](https://www.youtube.com/watch?v=u-H43tRgYJg&t=1350s) · b000029

**English**

&gt;&gt; Does that suggest we just start with this or let's start with like an additive fusion before you go to&gt;&gt; Yes, always a good baseline. Things like early fusion, late fusion, additive fusion, just concatenating is always a good baseline. That's why we we push you all to do it for for homework too. And then likewise for the midterm where people have to run you all have to run like strong baselines and then you start uh going complex.

**中文**

&gt;&gt; 这是否意味着我们应该先从这个开始，或者先从 additive fusion 开始，然后再……&gt;&gt; 是的，它始终是一个很好的基线（baseline）。early fusion、late fusion、additive fusion，或者只是拼接，始终都是很好的 baseline。这也是我们督促大家在作业中也做这些的原因。同样，期中项目中大家必须运行，你们所有人都必须运行强 baseline，然后再开始，呃，增加复杂度。

### [23:01](https://www.youtube.com/watch?v=u-H43tRgYJg&t=1381s) · b000030

**English**

Yes.

**中文**

请说。

### [23:15](https://www.youtube.com/watch?v=u-H43tRgYJg&t=1395s) · b000031

**English**

&gt;&gt; These are accuracies. These are accuracies. Um so the point being that um I mean ideally they should have ran all this with you know confidence intervals and and cross validation but the point being that sometimes it's not too much of a difference between a a proper you know complex model versus the the model that's just doing linear combinations. Um I mean of course sometimes maybe this 2% can make a difference. Uh but that's up to up to you and up to the domain.

**中文**

&gt;&gt; 这些是准确率（accuracies）。这些是 accuracies。嗯，要点在于，理想情况下，他们应该在所有这些实验中报告置信区间（confidence intervals），并做交叉验证（cross validation），但要点是，有时一个正规的复杂模型与一个只做线性组合的模型之间，差异并没有那么大。嗯，当然，有时候这 2% 可能会产生影响。呃，但这取决于你，也取决于具体领域。

### [23:54](https://www.youtube.com/watch?v=u-H43tRgYJg&t=1434s) · b000032

**English**

So one extension from this to really force to really force the model to um you know start learning these interactions is also not to do all this fusion at the same time but to do this fusion stage wise right fusion can also be done in a stage-wise manner. uh to see what that means. You know, one approach you could do that's in follow-ups to this work as well is that you have your you know two or three modalities. You first start by pushing the model to learn as much unimodal information as possible. Right? So basically you train unimodal classifiers uh where XA is taken to predict label, XB is taken to predict a label, XC is taken to predict a label all separately and then you add them up. Right? So that gives you the uh the best unimodal models and when you start adding them up the best additive models

**中文**

因此，由此延伸出的一种方法，是为了真正迫使模型，嗯，开始学习这些交互，不是同时完成所有 fusion，而是分阶段进行 fusion，对吧？fusion 也可以按阶段进行。呃，看看这是什么意思。你可以采用的一种方法，在这项工作的后续研究中也有，就是你有两个或三个模态，首先推动模型尽可能学习单模态信息。对吧？基本上就是训练 unimodal classifiers，分别用 XA 预测标签，用 XB 预测标签，用 XC 预测标签，然后把它们加起来。对吧？这样就得到最好的单模态模型，而把它们加起来时，就得到最好的加性模型

### [24:51](https://www.youtube.com/watch?v=u-H43tRgYJg&t=1491s) · b000033

**English**

right you first train that that's stage one once you've trained that you then train stage two which is then you start looking at B and C combinations B uh A and C B and C A and B combinations and start adding these biodal and then you start combining all three of them and you learn this triangle and how you learn it through these three stages is that you would first take the label Y and you would measure the difference between your target label and what the best additive function learns, right? So try to push the additive function to be as good as a label as possible. And then you compute the difference, the difference that is not captured by the additive models. You call that the residual and you use the residual and try to learn that residual using a biodal ver. Right? So the residual is y minus y unimodal. You compute a difference between that residual and y

**中文**

对吧？先训练这个，这是第一阶段。训练完后，再训练第二阶段，开始考虑 B 和 C 的组合，B，呃，A 和 C、B 和 C、A 和 B 的组合，并开始添加这些 biodal \[字幕疑误，可能指 bimodal，双模态\]。然后开始把三者全都组合起来，学习这个三角形。这三个阶段的学习方式是，先取标签 Y，测量目标标签与最好的加性函数学到的结果之间的差异，对吧？所以尽量推动加性函数逼近标签。然后计算差异，也就是加性模型没有捕获到的差异。把它称为残差（residual），用这个 residual，并尝试用 biodal ver \[字幕疑误，可能指 bimodal 部分\] 来学习它。对吧？所以 residual 是 y 减 y unimodal。再计算这个 residual 与 y

### [25:47](https://www.youtube.com/watch?v=u-H43tRgYJg&t=1547s) · b000034

**English**

biodal. So the output predicted using pairs of modalities. And then you see there's again some error. Uh you treat that as a residual again which is y minus unimodal minus biodal. And then you fit that residual using the the three modality terms. So you can treat this fusion also stage wise. Uh this is really good because now you're guaranteed for each stage you get better and better because you're only fitting the residual using the next modality. So you either get better and the residual decreases or if nothing is learned the error is the same. So you're guaranteed to either get better not worse. That's good. And you can also stop wherever you want. Right? If you think this residual at the start is 10, that's too large. I'm going to fit it to biodal. If I fit bodal the residual becomes two uh that's good enough. Uh then you don't have to do this. So you can basically do this

**中文**

biodal \[字幕疑误，可能指 bimodal，双模态\] 之间的差异，也就是使用成对模态预测的输出。然后你看到又有一些误差。呃，再把它作为 residual，也就是 y 减 unimodal 减 biodal。然后使用三个模态的项来拟合这个 residual。所以，也可以把 fusion 分阶段处理。呃，这非常好，因为现在你保证每个阶段都会越来越好，因为你只用下一个模态去拟合 residual。因此，要么变得更好，residual 减小；要么什么都没学到，误差保持不变。所以保证只会变好，不会变差。这很好。而且，你可以在任何想停的地方停下。对吧？如果你觉得一开始 residual 是 10，太大了，那我就用 biodal 去拟合。如果我拟合 bodal \[字幕疑误，可能指 bimodal\] 后，residual 变成二，呃，这就够好了，那么就不必再做这一步。所以你基本上可以做这种

### [26:44](https://www.youtube.com/watch?v=u-H43tRgYJg&t=1604s) · b000035

**English**

stage wise fusion and decide wherever you want to stop and find the right balance between what you use and what the error is.

**中文**

分阶段融合（stage wise fusion），自行决定在哪里停下，并在所使用的内容和误差之间找到合适的平衡。

### [26:57](https://www.youtube.com/watch?v=u-H43tRgYJg&t=1617s) · b000036

**English**

All right. So that's that's stage wise fusion. Uh good way of dealing with with problems in which data is very complex. You want to do fusion stage wise, you want to determine when to stop and you don't want fusion to uh to make things worse because sometimes fusion does make things worse. Sometimes uh you have these like three modality fusions, they take up a lot of parameters and these parameters are hard to optimize. Sometimes you see adding more modalities can also make things worse.

**中文**

好。这就是 stage wise fusion。呃，这是处理数据非常复杂的问题的一种好方法。你希望分阶段做 fusion，希望决定何时停止，也不希望 fusion 让事情变得更糟，因为有时 fusion 确实会让事情变糟。有时，呃，三模态 fusion 会占用大量参数，而这些参数很难优化。有时会看到，增加更多模态也会让效果变差。

### [27:31](https://www.youtube.com/watch?v=u-H43tRgYJg&t=1651s) · b000037

**English**

Okay, so to summarize uh both recapping Tuesday and also adding a little bit more content that I wasn't able to cover on Tuesday, multimodal fusion, the purpose is to learn this joint representation that models how two different modalities interact, right? And the goal is really to try to model all the interactions that are necessary in the data but nothing more, nothing less, still remaining reasonably compact, efficient and understandable to downstream users. We saw two spectrums. One where you first start extracting features from your modalities, right? Using good unimodal encoders and features that are more semantically meaningful and more likely to be homogeneous in nature. And on the other extreme there's also a paradigm where you have raw data you're doing fusion earlier when the data is more heterogeneous but this gives you benefits because now the fusion and representation learning can be learned

**中文**

好，总结一下，呃，既回顾了周二的内容，也补充了一点周二没来得及讲的内容。multimodal fusion 的目的是学习一个 joint representation，用来建模两个不同模态如何交互，对吧？目标其实是尽量建模数据中所有必要的交互，不多也不少，同时仍然保持合理的紧凑性、效率，以及对下游用户而言的可理解性。我们看了两个连续谱。一端是先从模态中提取特征，对吧？使用良好的 unimodal encoders，以及语义上更有意义、本质上更可能同质的特征。而在另一个极端，也有一种范式：你有原始数据，在数据更异质时更早地做 fusion。不过这样也有好处，因为现在 fusion 和 representation learning 可以

### [28:27](https://www.youtube.com/watch?v=u-H43tRgYJg&t=1707s) · b000038

**English**

end to end together. And we saw different methods along this spectrum extreme being late fusion when you're already predicting a label and then you're you're combining the labels in some way. We saw additive fusion um going beyond additive first order you saw multiplicative three modalities was tensor and it can go to even higher order polomials between modalities. Uh some of this can be very expensive. So we saw low rank approximations of them and all of these still maintain the same weights for your modalities right same W1 for X A W2 for XB. So we then saw settings in which your weights are dynamically changing given your current A and B. So those are gated fusion or dynamic and modality shifting fusion.

**中文**

一起端到端（end to end）学习。我们看了这个连续谱上的不同方法，一个极端是 late fusion：已经在预测标签，然后以某种方式组合这些标签。我们看了 additive fusion，嗯，超越加性的一阶交互后，看了 multiplicative，三个模态时是 tensor，还可以进一步扩展到模态之间更高阶的 polomials \[字幕疑误，可能指 polynomials，多项式\]。呃，其中一些计算可能非常昂贵。所以我们看了它们的 low rank approximations。所有这些仍然对各个模态使用相同的权重，对吧？对 X A 使用同一个 W1，对 XB 使用同一个 W2。然后我们看了权重根据当前 A 和 B 动态变化的设定。这些就是门控融合（gated fusion）、动态融合（dynamic fusion）以及模态转移融合（modality shifting fusion）。

### [29:24](https://www.youtube.com/watch?v=u-H43tRgYJg&t=1764s) · b000039

**English**

And then we'll see some of these um which are more early fusion methods later on in the semester when we talk about how these transformers and multimodal transformers can be used to do much earlier fusion. Right? Any last questions about fusion? Yes.

**中文**

之后，本学期后面还会看一些更偏 early fusion 的方法，届时我们会讨论如何使用 transformers 和多模态 transformers 来更早地进行 fusion。对吧？关于 fusion，还有最后的问题吗？请说。

### [29:54](https://www.youtube.com/watch?v=u-H43tRgYJg&t=1794s) · b000040

**English**

So for example problem here would be the classification your classes might be like the cat&gt;&gt; it can be cross entropy difference in cross entropy error um great you can any mean square error cross entropy error and any other any loss function that you use um can be done with Yes. Great. Yes.&gt;&gt; Question about this slide. So, yeah. No, the one the one that you have.&gt;&gt; Okay.&gt;&gt; Um, so you you talk briefly about compute for those different approaches. Um so do we have a good understanding like what is the difference between those approaches magnitude as we progress more towards

**中文**

所以，比如这里的问题是分类，类别可能像猫……&gt;&gt; 可以用交叉熵（cross entropy），cross entropy 误差的差异。嗯，很好，你可以用任何均方误差（mean square error）、cross entropy 误差，以及你使用的任何其他损失函数（loss function），都可以用来做。请说。很好。请说。&gt;&gt; 关于这张幻灯片的问题。是的，不是，是你现在这张。&gt;&gt; 好。&gt;&gt; 嗯，你简要谈到了这些不同方法的计算量。嗯，我们是否很好地理解，当逐渐走向更

### [30:50](https://www.youtube.com/watch?v=u-H43tRgYJg&t=1850s) · b000041

**English**

heterogeneous modalities.&gt;&gt; Uh do we have a good understanding? Uh if you mean do we have a good theoretical understanding and guarantees? No, because these things are hard to come by in in deep learning or anything where you know neuronets \[snorts\] and non-convex optimization is evolved. Do we have good intuitions? Um I think it comes with practice, right? Comes with I mean that's the purpose of this course where you're going to try a bunch of different fusion methods for homework two maybe for your project if you're focusing on fusion. Um and then you'll start seeing for example you plot compute right a lot of these as you go from this to this roughly speaking you'll need more and more compute uh because the fusion the the the fusion parameters is larger and then you can see for yourself whether performance gets better or worse right so not necessarily always performance gets better but also sometimes those

**中文**

异质的模态时，这些方法之间计算量的数量级差异？&gt;&gt; 呃，我们是否有很好的理解？如果你指的是是否有很好的理论理解和保证，答案是没有，因为在深度学习（deep learning）或者任何涉及 neuronets \[字幕疑误，可能指 neural networks，神经网络\]\[吸鼻声\] 和非凸优化（non-convex optimization）的领域中，这些都很难获得。我们是否有不错的直觉？嗯，我想这来自实践，对吧？来自……我的意思是，这就是这门课的目的，你们会在作业二中尝试很多不同的 fusion 方法，如果项目侧重 fusion，也可能在项目中尝试。嗯，然后你就会开始看到，比如把计算量画出来，对吧？大致来说，很多方法从这里到这里时，会需要越来越多的计算量，呃，因为 fusion 的参数更多。然后你可以自己观察性能是变好还是变差，对吧？所以性能不一定总是变好，但有时这些

### [31:45](https://www.youtube.com/watch?v=u-H43tRgYJg&t=1905s) · b000042

**English**

don't work at all and you have to start doing early fusion using huge models right Um I mean there's general guidelines right general guidelines is that simple baselines are always very helpful simple early fusion late fusion baselines um you know simple baselines based on pre-trained models are always very helpful and then comes these task specific requirements which is how much compute or how much are you willing to use a black box which is something that really tells you here are the fusions that's happening at this stage and here is the interaction. So there's a lot of considerations there as well.

**中文**

根本不起作用，你就必须开始用大型模型做 early fusion，对吧？嗯，我的意思是，有一些一般性的指导原则：简单 baseline 总是很有帮助，简单的 early fusion、late fusion baseline，嗯，基于 pre-trained models 的简单 baseline 总是很有帮助。然后还有具体任务的要求，比如需要多少计算量，或者你愿意在多大程度上使用黑箱（black box），就是某种真正告诉你这一阶段发生了哪些 fusion、这里有哪些交互的东西。所以也有很多需要考虑的因素。

### [32:29](https://www.youtube.com/watch?v=u-H43tRgYJg&t=1949s) · b000043

**English**

We are trying to build up um I mean a key a key vision uh that some of the work we're doing is is to kind of build up a more formal understanding of these. So you can search up some of the papers that we have. Um and what story we can essentially tell is that if you have some data right X1, X2 and Y you have some samples you can first quantify some statistics from your data and these statistics might say there is this amount of synergy between your modalities for these certain elements right we are we are on our path towards developing such a framework and we already have some early evidence to show that this exists and then based on that knowledge for example there's this much of bits of synergy that has to be fused we can then approximately prescribe which fusion method is the most useful right so sometimes you find that uh you quantify and most of the

**中文**

我们正在尝试建立，嗯，我的意思是，我们所做的一些工作中，一个关键愿景就是建立对这些问题更形式化的理解。所以你们可以搜索我们的一些论文。嗯，我们基本上能够说明的是，如果你有一些数据，对吧，X1、X2 和 Y，有一些样本，就可以先量化数据中的一些统计量。这些统计量可能会告诉你，在某些元素上，模态之间有这么多协同信息（synergy），对吧？我们正在朝着建立这样一个框架的方向前进，而且已经有一些早期证据表明它存在。然后根据这些知识，例如有这么多 bit 的 synergy 需要融合，就可以大致给出哪一种 fusion 方法最有用的建议，对吧？所以有时你会发现，呃，量化之后，大部分

### [33:25](https://www.youtube.com/watch?v=u-H43tRgYJg&t=2005s) · b000044

**English**

information is very unique in X1 in which case you don't need all these fancy methods right just use X1 unimodal and then sometimes you quantify and find there's lots of synergy between A and B uh between one and two uh then you have to use maybe some more complex fusion method it's not a perfect mapping but uh it helps give you some intuition uh and more work needs to be done in this. So if you want to do a project in this space that's also highly encouraged. So more more rigorous more more more foundational principles.

**中文**

信息是 X1 独有的，这种情况下就不需要所有这些花哨方法，对吧？只使用 X1 这个单模态即可。有时你量化后发现 A 和 B 之间，呃，一和二之间有很多 synergy，那么可能就必须使用更复杂的 fusion 方法。这不是一个完美的映射，但，呃，可以帮助你形成一些直觉，而这方面还需要更多工作。所以，如果你想在这个方向做项目，也非常鼓励。也就是更加严谨、更加、更加基础性的原则。

### [34:01](https://www.youtube.com/watch?v=u-H43tRgYJg&t=2041s) · b000045

**English**

All right. Any final questions about fusion? Okay. Very good. So now we'll move on to what this today's lecture was actually planned for which is to discuss alignment. Uh fusion and alignment are perhaps the two biggest core concepts right uh in multimodal. So we'll cover basics of multimodal alignment. We'll cover contrastive learning as a common approach of explicitly enforcing alignment uh in a discrete setting. We'll cover a little bit continuous alignment and then we'll cover this very new theme of what we call implicit alignment, right? Where alignment emerges from training models without explicitly enforcing it using your objective functions like contrastive learning. So what is alignment? So alignment aims to identify and model all different ways in which different elements in your

**中文**

好。关于 fusion，还有最后的问题吗？好。很好。现在进入今天这节课原本计划的内容，也就是讨论 alignment。呃，fusion 和 alignment 可能是多模态中两个最大的核心概念，对吧？我们会介绍多模态对齐（multimodal alignment）的基础。我们会介绍对比学习（contrastive learning），作为在离散设定中显式强制 alignment 的一种常见方法。我们会稍微介绍连续对齐（continuous alignment），然后介绍一个很新的主题，也就是所谓的隐式对齐（implicit alignment），对吧？alignment 会在训练模型时涌现，而不需要通过 contrastive learning 这样的目标函数显式强制实现。那么，什么是 alignment？alignment 的目标是识别并建模不同

### [34:57](https://www.youtube.com/watch?v=u-H43tRgYJg&t=2097s) · b000046

**English**

modalities are connected with each other. And we'll give a more formal version of what connected means. But you can intuitively think of it as you know overlapping information or representing some underlying similar concept. There's three sub challenges for alignment. The first case being the most simple where you can segment your modalities into discrete elements. Right? So words that a person is speaking, objects that are in the image that are being referenced, uh facial expressions that a person is making across something. So once you can uh explicitly separate your modalities into elements, then you can think of alignment as basically this this matching problem. For example, which word in the caption references this chair in the image and then which other word references this other part of the image. often times alignment is this this matching problem between semantically similar elements across

**中文**

模态中的不同元素彼此连接的各种方式。我们会给出“连接”更形式化的定义，但直观上可以把它理解为重叠信息，或者表示某种底层的相似概念。alignment 有三个子挑战。第一种情况最简单，你可以把模态分割成离散元素（discrete elements）。对吧？比如一个人说的话语、图像中被指代的物体，呃，以及一个人在某种过程中做出的面部表情。所以，一旦能显式地把模态分成元素，就可以把 alignment 基本上视为一个匹配问题（matching problem）。例如，描述中的哪个词指代图像中的这把椅子，另一个词又指代图像的另一个部分。很多时候，alignment 就是两个

### [35:54](https://www.youtube.com/watch?v=u-H43tRgYJg&t=2154s) · b000047

**English**

your two modalities. So discrete alignment or learning these discrete connections is the easiest case. This problem becomes more challenging when your elements are more continuous whereas higher resolution continuous it is not clear what the granularity is. Right? So for example, aligning video to text or aligning sensor data to text is more difficult because it's not really clear what the semantic boundaries are in video and sensors. It is not as clear as you know here's a word that I'm saying in my sentence. So we cover both of these today. Uh I also want to complete the story and note that in this two settings alignment is the end goal where the goal is to find out which word references this part of the image or which word references which part of the video. Alignment is the end goal. There is a third sub challenge where alignment is used as an

**中文**

模态之间语义相似元素的 matching problem。因此，离散对齐（discrete alignment），或者学习这些离散连接，是最简单的情况。当元素更加连续、分辨率更高且连续时，这个问题就更具挑战性，因为粒度（granularity）并不明确。对吧？例如，把视频与文本对齐，或者把传感器数据与文本对齐，就更困难，因为视频和传感器数据中的语义边界并不十分明确。它不像“这是我在句子里说的一个词”那样清楚。所以今天我们会介绍这两种情况。呃，我还想把整个脉络补充完整，指出在这两种设定中，alignment 是最终目标，目的是找出哪个词指代图像的哪一部分，或者哪个词指代视频的哪一部分。alignment 是最终目标。还有第三个子挑战，alignment 被用作

### [36:51](https://www.youtube.com/watch?v=u-H43tRgYJg&t=2211s) · b000048

**English**

intermediate step to learn better downstream representations and we call that contextualized or line representations. So over here I draw you know most of these alignments are in gray. How do you use the alignment to learn better representations? For example, as you all seen language models today, we have these words and we know how they align and are contextualized with other words in the context. This is critical to learn more powerful sentence representations. Right? In multimodal LLMs, we have all these words and questions that are contextualized with previous words and also contextualized with parts of the image depending on how the alignment happens. It is this alignment and contextualization that allows you to train better multimodal LLMs. So this is where alignment is used implicitly as an intermediate step to learn better representations. We'll cover a lot more of this in the next two weeks where we'll cover you know these

**中文**

中间步骤，以学习更好的下游表示，我们称之为上下文化表示（contextualized representations）或 line representations \[字幕疑误，可能指 aligned representations，对齐表示\]。这里我画的这些 alignment 大多是灰色的。如何使用 alignment 来学习更好的表示？例如，大家都见过今天的语言模型，我们有这些词，并且知道它们如何与上下文中的其他词对齐、如何在上下文中得到表示。这对学习更强大的句子表示至关重要，对吧？在多模态大语言模型（multimodal LLMs）中，所有这些词和问题都会结合前面的词，也会根据 alignment 的情况结合图像的部分内容进行上下文化。正是这种 alignment 和上下文化，让你能训练出更好的 multimodal LLMs。所以，这里 alignment 被隐式地用作中间步骤，以学习更好的表示。接下来两周会更详细地介绍这些内容，届时会讲这些

### [37:46](https://www.youtube.com/watch?v=u-H43tRgYJg&t=2266s) · b000049

**English**

multimodal transformers and foundation models. Today we'll stick with um just where alignment is a goal of learning discrete and continuous alignment between modalities. Any questions about this this road map?

**中文**

multimodal transformers 和 foundation models。今天我们只讨论，嗯，把 alignment 作为目标，学习模态之间离散和连续 alignment 的情况。大家对这个路线图有什么问题吗？

### [38:08](https://www.youtube.com/watch?v=u-H43tRgYJg&t=2288s) · b000050

**English**

Okay. So starting with discrete alignment. So the goal here is to identify and model these connections between discrete elements across modalities, right? And you want to think about these connections as some amount of information that is shared with a similar semantic meaning between them. Again, I'll use these uh these these you know triangles and circles A and B. And you want to think of these connections as capturing what is shared and basically ignoring what is unique, right? Anything that is unique will basically be discarded once you start doing alignment. Yes.&gt;&gt; Um would it be possible for you to get practical examples with um each challenge? So I guess like in this case modality a could be laby pictures. So um modality like each unique um feature would be like one CT image for example.

**中文**

好。从 discrete alignment 开始。这里的目标是识别并建模模态之间离散元素的连接，对吧？可以把这些连接理解为它们之间共享的一定量信息，具有相似的语义含义。我还是用这些，呃，这些三角形和圆形 A 和 B。你应该把这些连接理解为捕获共享的东西，同时基本上忽略独有的东西，对吧？一旦开始做 alignment，任何独有的信息基本上都会被丢弃。请说。&gt;&gt; 嗯，能否为每个挑战提供一些实际例子？比如，我想在这个例子里，模态 a 可以是 laby pictures \[字幕疑误，含义不明\]。所以，嗯，模态，比如每一个独有的特征，可以是一张 CT 图像。

### [39:05](https://www.youtube.com/watch?v=u-H43tRgYJg&t=2345s) · b000051

**English**

&gt;&gt; Well we'll get to that next slide. um which is one example is I mean the easier example is basically vision and text uh image and text. So this is a image and your caption could be a woman reading newspaper right image is segmented into bounding boxes of different objects woman newspaper the caption is segmented into tokens um and woman text corresponds to that part of the image newspaper text corresponds to that part of the image. Uh it's interesting to note what was the alignment between the word reading and the MHV anybody? Yes.&gt;&gt; Probably eyes or the hands or the combination of them&gt;&gt; perhaps? Any other takers? What would the word reading map to? Yeah,&gt;&gt; you like the head tilted down&gt;&gt; maybe. But even head tilted down, eyes, if you don't see what is the newspaper,

**中文**

&gt;&gt; 下一张幻灯片就会讲到。嗯，一个例子，我的意思是，比较简单的例子就是视觉和文本，呃，图像和文本。这是一张图像，描述可以是“一个女人在读报纸”，对吧？图像被分割成不同物体的边界框（bounding boxes），女人、报纸；描述被分割成词元（tokens）。嗯，woman 这个文本对应图像的那一部分，newspaper 这个文本对应图像的那一部分。呃，有意思的是，reading 这个词与 MHV \[字幕疑误，可能指 image，图像\] 之间是什么 alignment？有人知道吗？请说。&gt;&gt; 可能是眼睛、手，或者二者的组合？&gt;&gt; 也许？还有其他人吗？reading 这个词会映射到什么？请说。&gt;&gt; 比如头向下倾斜。&gt;&gt; 也许。但即使头向下倾斜、有眼睛，如果看不到报纸是什么，

### [40:02](https://www.youtube.com/watch?v=u-H43tRgYJg&t=2402s) · b000052

**English**

the target, you don't know whether the person is reading or just like staring at something or falling asleep, right?&gt;&gt; Color of what pixels?&gt;&gt; Oh, the news. So if red was a phone, it would probably be dark. If it was a newspaper, it's probably lighter.&gt;&gt; Uhhuh.&gt;&gt; Interesting. Well, I mean the short answer is that it's ambiguous. Uh this is not a onetoone mapping. probably it will be the reading should align to a function of of course the the woman's face and gaze direction at the same time also uh the newspaper and maybe the color newspaper has to be there to know that there's some target that there is reading so alignment is often not just one to one in the case of women newspaper it's one to one sometimes it is one to many this word maps to many things and it can also be the relationship between different things the relationship in this case between the

**中文**

也就是目标，你也不知道这个人是在阅读，还是只是在盯着某样东西，或者快睡着了，对吧？&gt;&gt; 什么像素的颜色？&gt;&gt; 哦，报纸。所以如果 red \[字幕疑误，可能指所读的对象\] 是手机，可能会比较暗。如果是报纸，可能更亮。&gt;&gt; 嗯哼。&gt;&gt; 有意思。嗯，简单说，它是有歧义的。呃，这不是一对一映射（one-to-one mapping）。reading 大概应该对齐到某个函数，它当然涉及女人的脸和视线方向，同时也涉及报纸，也许还有颜色。报纸必须在那里，才能知道有一个被阅读的目标。所以 alignment 往往不只是一对一。在女人、报纸的例子中是一对一；有时是一对多，一个词映射到许多东西，也可能是不同东西之间的关系。在这个例子中，就是

### [40:57](https://www.youtube.com/watch?v=u-H43tRgYJg&t=2457s) · b000053

**English**

and a newspaper right but that's uh an example that I was going to give uh and here I also want to highlight several intuitions of why this alignment why these connections exist right and how we can discover them right one is through from a more statistical perspective right based on association if I always see you know the word newspaper in these captions with various newspapers in different you know images where newspapers exist this then with enough data you can identify this association that the common word in all of these captions newspaper maps to the common object in all of these images which is the photo of a newspaper. Uh so that's from a correlation perspective a co-occurrence perspective how we can discover the alignment. uh but also that gives some semantic meaning which is that you know this newspaper the word newspaper actually

**中文**

与报纸之间的关系，对吧？不过，这就是我本来打算给的一个例子。这里我还想强调几个直觉：为什么这些 alignment、这些连接存在，以及我们如何发现它们。一个是从更偏统计学的角度，通过关联（association）来理解。如果我总是在这些描述中看到 newspaper 这个词，同时在不同的、存在报纸的图像中看到各种报纸，那么有了足够多的数据，就能识别这种 association：所有描述中共同的词 newspaper，映射到所有这些图像中共同的物体，也就是报纸的照片。呃，这就是从相关性（correlation）和共现（co-occurrence）的角度，理解如何发现 alignment。呃，同时这也赋予了某种语义含义，也就是说，这个 newspaper，newspaper 这个词实际上

### [41:53](https://www.youtube.com/watch?v=u-H43tRgYJg&t=2513s) · b000054

**English**

means something and the image of the newspaper actually means something. So this identifies the correspondence which has the same meaning between those two terms that just so happen to be expressed one in text one in image. Uh beyond these uh I you know singular co- occurrences like we saw the onetoone mapping between women and newspaper we also have other you know pairwise or higher order interactions between higher order connections between one modality and another. So we saw the example of reading right this idea of reading in text uh really maps to this dependency where there's this eyes and this directed mapping to the newspaper right and likewise from a semantic perspective there's some relationship between the eyes and the newspaper that indicates you know the function of the eyes which is which is to read so there's different levels in which these connections exist

**中文**

有某种意义，而报纸的图像实际上也有某种意义。因此，这识别出了两者之间含义相同的对应关系，只不过一个用文本表达，一个用图像表达。呃，除了这些单独的 co-occurrences，比如我们看到的女人和报纸的一对一映射，还有其他成对或高阶交互，也就是一个模态与另一个模态之间的高阶连接。所以我们看到了 reading 的例子，对吧？文本中的 reading 这个概念，实际上映射到这样的依赖关系：有眼睛，还有指向报纸的定向映射。对吧？同样，从语义角度看，眼睛与报纸之间存在某种关系，表明眼睛的功能，也就是阅读。所以，这些连接存在于不同的层次

### [42:48](https://www.youtube.com/watch?v=u-H43tRgYJg&t=2568s) · b000055

**English**

onetoone associations is the easiest and most clear but at the same time there are higher order pair-wise functionality that needs to be captured uh during alignment. Okay, but how exactly do we capture this? Uh a general way of capturing this is through what we call um paired data, right? If you have lots of paired data, in this case, paired data between images and text. So pairing basically mean that image corresponds to this caption. Image two corresponds to this other caption. I can then start learning these representations where A and B are each encoded by F of A and F of B. This encodes them into representations Z A and ZB. And the goal is to define a similarity function G

**中文**

一对一关联最简单、最明确，但与此同时，还有一些高阶的、成对的功能关系，需要在 alignment 过程中捕获。好，但究竟如何捕获呢？呃，一种通用方法是使用所谓的配对数据（paired data），对吧？如果你有大量 paired data，在这里就是图像与文本之间的 paired data。配对基本上意味着，这张图像对应这段描述，图像二对应另一段描述。然后我就可以开始学习这些表示，其中 A 和 B 分别由 F of A 和 F of B 编码。这会把它们编码为表示 Z A 和 ZB。目标是定义一个相似度函数（similarity function）G

### [43:43](https://www.youtube.com/watch?v=u-H43tRgYJg&t=2623s) · b000056

**English**

that captures the fact that ZA and ZB are connected with each other and perhaps other ZA and ZB are not connected with each other. So that's a general way of capturing alignment, right? A and B come in one encoder for each F of A F of B. This gives you features Z of A, Z of B and there is some similarity function G scoring whether they are aligned or not or the extent to which they are aligned. Okay. Uh you'll see that now this is different from fusion right in fusion you have A and B and you're bringing them together into one joint representation Z. Uh but now in alignment you have A and B. You're learning two separate representations Z of A and Z of B and you are computing some alignment or some similarity function between them. Yeah.&gt;&gt; Would attention kind of piggyback on these statistical um co occurrences

**中文**

来捕获 ZA 和 ZB 彼此连接，而其他 ZA 和 ZB 可能没有连接这一事实。所以，这就是捕获 alignment 的通用方式，对吧？输入 A 和 B，各自对应一个编码器 F of A、F of B，得到特征 Z of A、Z of B，再由某个 similarity function G 评估它们是否对齐，或者对齐程度有多高。好。呃，你会发现，这与 fusion 不同，对吧？在 fusion 中，你有 A 和 B，把它们合成一个 joint representation Z。而在 alignment 中，你有 A 和 B，学习两个独立的表示 Z of A 和 Z of B，再计算它们之间的某种 alignment 或 similarity function。请说。&gt;&gt; attention 是否会利用这些统计上的 co-occurrences，

### [44:39](https://www.youtube.com/watch?v=u-H43tRgYJg&t=2679s) · b000057

**English**

like between reading for example and data.&gt;&gt; Uh yes yes alignment would would capture some of this. So that's how we'll talk about um you know how this alignment can be learned using attention uh but using that how you also learn these downstream representations later when we talk about this uh next week. Yeah. But yes attention and is one way of learning that. Okay. So any question about this this paradigm and how it differs from fusion. Right now we're not learning one joint representation that fuse us but we're learning and keeping separate representations Z of A Z and B and you are uh keeping them consistent using this this similarity function.

**中文**

比如 reading 与数据之间的共现？&gt;&gt; 呃，是的，是的，alignment 会捕获其中一些内容。所以，下周讨论这个话题时，我们会讲如何用 attention 学习这种 alignment，以及如何利用它进一步学习这些下游表示。是的。不过，是的，attention 是学习它的一种方式。好。关于这个范式，以及它和 fusion 的区别，有什么问题吗？现在我们不是在学习一个融合我们的 joint representation，而是在学习并保留独立的表示 Z of A、Z and B，再通过这个 similarity function 让它们保持一致。

### [45:28](https://www.youtube.com/watch?v=u-H43tRgYJg&t=2728s) · b000058

**English**

All right. So you can think of these encoders as or you can define them however you want. These encoders are designed to capture you know the heterogeneity. It's it's you know it's adapted to the different data modalities and their individual structures. But once Z of A Z of B are learned then this uh coordination function G essentially captures the the connections uh between them. And a general way of of learning this learning this alignment function is to define a loss function. uh loss function is going to be first put f of a um on madata da and then you put f of b on madata db that gives you representations and then you score them with g right g is the function that scores the the similarity between them what are the trainable parameters you' be trainable parameters

**中文**

好。你可以把这些编码器理解为，或者按你想要的方式定义它们。这些编码器旨在捕获异质性（heterogeneity）。它们适配不同的数据模态及其各自的结构。但一旦学到了 Z of A、Z of B，这个，呃，协调函数（coordination function）G 基本上就捕获了它们之间的连接。学习这个 alignment 函数的一种通用方式，是定义一个 loss function。呃，这个 loss function 首先把 f of a，嗯，应用于 madata da \[字幕疑误，可能指模态数据 da\]，然后把 f of b 应用于 madata db \[字幕疑误，可能指模态数据 db\]，得到表示，再用 g 给它们打分，对吧？g 就是衡量它们之间相似度的函数。有哪些可训练参数呢？可训练参数

### [46:23](https://www.youtube.com/watch?v=u-H43tRgYJg&t=2783s) · b000059

**English**

data inside this g function so in fact that similarity function could also have trainable parameters okay uh and Then you will of course have the trainable parameters data for f of a your encoder for a and f of b your encoder for b. Right? So those are the trainable parameters and you would optimize them uh to in this case maximize this g if g is similarity or minimize it if g is some some distance function.

**中文**

是这个 g 函数里的 data \[字幕疑误，可能指 theta\]，因此 similarity function 本身实际上也可以有可训练参数。好，呃，然后当然还有 f of a，也就是 A 的编码器，以及 f of b，也就是 B 的编码器中的可训练参数 data \[字幕疑误，可能指 theta\]。对吧？这些就是可训练参数，你会优化它们，呃，在这里，如果 g 是相似度，就最大化 g；如果 g 是某个 distance function，就最小化它。

### [46:55](https://www.youtube.com/watch?v=u-H43tRgYJg&t=2815s) · b000060

**English**

So what are some examples of g? um G can be cosine similarity, right? So G takes in Z and ZB can be cosine similarity that essentially takes a dotproduct between A and B uh perhaps normalized by their by their magnitudes. Right? So that keeps it nice and intuitive between between uh negative 1 positive one uh normalized by the magnitudes that captures a linear notion of similarity. So whether these two vectors point in the same direction in representation space we can also extend it to kernel similarities. Folks have taken machine learning have seen kernels. Kernels are any function that scores uh given these two vectors score some distance between them. Right? These kernels can be linear in which you recover the dotproduct between these two vectors. So where they

**中文**

那么 g 有哪些例子？嗯，G 可以是余弦相似度（cosine similarity），对吧？G 接收 Z 和 ZB，可以采用 cosine similarity，基本上是对 A 和 B 做点积（dot product），呃，也许再用它们的模长归一化。对吧？这样就很好理解，范围在负 1 到正一之间，呃，通过模长归一化，捕获一种线性的相似性概念。也就是这两个向量在表示空间（representation space）中是否指向同一方向。还可以扩展到核相似度（kernel similarities）。学过机器学习的同学见过核（kernels）。kernels 是给定这两个向量、对它们之间某种距离进行评分的函数，对吧？这些 kernels 可以是线性的，此时就恢复为这两个向量之间的 dot product，也就是它们是否

### [47:51](https://www.youtube.com/watch?v=u-H43tRgYJg&t=2871s) · b000061

**English**

point in the same direction but they can also be polomial exponential RBF the only differences between these other kernel functions is the space in which you're computing these similarities in you first transform them to some polinomial space and then compute these similarities or do you keep them in the original space and compute those similarities in the original space. uh there are benefits of transforming them into different representation spaces and basically thought of as learning similarity in some nonlinear function of the vectors instead of in the original space that they came in. So any of the kernel functions can be used for similarity correlation can also be used. So in this case, I may not care about just whether these two points themselves, right? Whether these two points are close by or they're pointing in the same direction, but I care about the whole distribution, right? I care about this whole

**中文**

指向同一个方向，但也可以是 polomial \[字幕疑误，可能指 polynomial，多项式\]、指数型（exponential）、RBF。这些其他 kernel functions 的区别仅在于计算相似度所处的空间：你是先把它们变换到某个 polinomial \[字幕疑误，可能指 polynomial，多项式\] 空间再计算相似度，还是保留在原始空间中，在原始空间里计算相似度。呃，把它们变换到不同的 representation spaces 有一些好处，基本上可以理解为在向量的某种非线性函数中学习相似性，而不是在它们最初所在的空间中。因此，任何 kernel function 都可以用来衡量相似度，correlation 也可以。在这种情况下，我可能不只是关心这两个点本身，对吧？这两个点是否接近，或者是否指向同一方向；我关心的是整个分布（distribution），对吧？我关心这个完整的

### [48:48](https://www.youtube.com/watch?v=u-H43tRgYJg&t=2928s) · b000062

**English**

distribution of points in my first modality and the distribution in the second and whether they're correlated with each other, right? So that could be a notion of similarity. Similarly, I might care about Yes.

**中文**

第一模态中的点分布，以及第二模态中的分布，还有它们是否彼此相关，对吧？这可以是一种相似性概念。同样，我也可能关心……请说。

### [49:09](https://www.youtube.com/watch?v=u-H43tRgYJg&t=2949s) · b000063

**English**

Yeah, I'll give some examples. But uh let me talk about this first before we go to distribution. Let me talk about the pair wise case first. Um sometimes I don't care about whether let's say I'm apple orange and apple orange, right? Apple orange in text, apple orange in en invision. I may not care that the word embedding for apple is close to the image embedding of apple. Doesn't really matter where they are. But what I might care about is that the relationship between the word embeddings of apple and oranges are consistent with the relationship between the image embeddings of apples and oranges. Right? Specifically that this transformation represents keeping the shape by changing the color. Right? Right? So I may not care about the individual locations of points themselves, but I care about the the order or the pair wise relationships distances between for example apple orange in text and apple orange in um in

**中文**

是的，我会给一些例子。不过，呃，在讲 distribution 之前，先说这个。先讲成对（pairwise）的情况。嗯，有时我不关心，比如我是苹果、橙子，以及苹果、橙子，对吧？文本中的苹果、橙子，和视觉中的苹果、橙子。我可能不关心苹果的词嵌入（word embedding）是否接近苹果的图像嵌入（image embedding）。它们在哪里并不重要。我可能关心的是，苹果与橙子的 word embeddings 之间的关系，是否与苹果和橙子的 image embeddings 之间的关系一致。对吧？具体来说，这个变换表示保持形状、改变颜色。对吧？对吧？所以我可能不关心各个点自身的位置，但关心它们的顺序，或者成对关系、距离，比如文本中的苹果、橙子与，嗯，

### [50:04](https://www.youtube.com/watch?v=u-H43tRgYJg&t=3004s) · b000064

**English**

images. Uh if we send it to the three threepoint case I might care that apple orange are nearby but very far away from table in word embeddings and likewise apple orange are nearby but very far away from table in the visual embeddings. Right? So now you start seeing it is sometimes these pair-wise and three-way relationships between the points more important than the specific location of the individual points themselves. Make sense? Yeah.

**中文**

图像中的苹果、橙子。呃，如果扩展到三个点的情况，我可能关心，在 word embeddings 中，苹果和橙子彼此接近，但与桌子相距很远；同样，在视觉嵌入（visual embeddings）中，苹果和橙子彼此接近，但与桌子相距很远。对吧？现在你就开始看到，有时候，点之间这些成对和三元关系，比各个点本身的具体位置更重要。明白吗？请说。

### [50:55](https://www.youtube.com/watch?v=u-H43tRgYJg&t=3055s) · b000065

**English**

it can still be trained. Um I mean this paradigm would still work, right? You will put a uh text through a text model, you get text embeddings. You put B images through a image model, you get image embeddings. And now I have a bunch of text embeddings representing apple, orange, and table. I get my image embeddings representing apple, orange, and table. And all I'm doing is computing this differentiable function which is the pair wise distances between apple orange and table for text and the pair wise distances between apple orange and table for images and I'm trying to structure them in some coherent way right and that is your function jeep right um in fact one slide in the back for this um I mean this is what uh it looks like right so my care that my image embeddings apple orange and elephant are structured in this way. Apple orange close together elephant far away and

**中文**

仍然可以训练。嗯，我的意思是，这个范式仍然适用，对吧？把文本输入文本模型，得到 text embeddings。把 B 图像输入图像模型，得到 image embeddings。现在我有一组表示苹果、橙子和桌子的 text embeddings，也有表示苹果、橙子和桌子的 image embeddings。我要做的只是计算这个可微函数，也就是文本中苹果、橙子和桌子之间的 pairwise distances，以及图像中苹果、橙子和桌子之间的 pairwise distances，并尝试以某种一致的方式组织它们，对吧？这就是你的函数 jeep \[字幕疑误，可能指 G\]。嗯，实际上后面有一张幻灯片讲这个。我的意思是，它看起来就是这样，对吧？我可能关心苹果、橙子和大象的 image embeddings 按这种方式组织：苹果和橙子靠近，大象离得远，而且

### [51:52](https://www.youtube.com/watch?v=u-H43tRgYJg&t=3112s) · b000066

**English**

likewise for text embedding apple orange close together elephant far away. How do you do that? Um I won't get into details but you can define kernels for each right so this function basically says I'm going to look at all pairwise distances between all the image embeddings that I have. This will say I'm going to look at all pair wise distances between the word embeddings that I have. Those two give you some summary as some kernel and my similarity is how these two kernels which basically means a pair wise graph of distances how similar they are right you can maximize that to ensure similarity.

**中文**

text embedding 中也一样，苹果和橙子接近，大象离得远。怎么做到呢？嗯，我不展开细节，但可以分别定义 kernels，对吧？这个函数基本上是说，我要查看所有 image embeddings 两两之间的距离。这个则是说，我要查看所有 word embeddings 两两之间的距离。两者各自以某种 kernel 的形式给出一个概括，而我的相似度就是看这两个 kernels 有多相似，它们基本上就是成对距离的图，对吧？你可以最大化这一点来保证相似性。

### [52:33](https://www.youtube.com/watch?v=u-H43tRgYJg&t=3153s) · b000067

**English**

I saw. Yes.&gt;&gt; The ground truth label is somehow implicit. I think in the that function it's just using the embeddings of the two modities but we don't actually like is it not also in the last but

**中文**

我看到了。请说。&gt;&gt; 真值标签（ground truth label）在某种程度上是隐式的。我觉得那个函数只是在使用两个模态的 embeddings，但我们实际上没有……它难道不也在最后……但是

### [53:07](https://www.youtube.com/watch?v=u-H43tRgYJg&t=3187s) · b000068

**English**

uh so I think asking two questions here one question is uh the loss is has to be defined right so in this case the loss has to be defined beforehand it is not going to automatically learn that sometimes you care about pair-wise losses sometimes you care about correlation sometimes you care about cosine similarity you have to specify what the loss is so you have to specify what G Um but G can be anything any of these that we just discussed.&gt;&gt; Yes.&gt;&gt; There is a different that actually when are they

**中文**

呃，我想这里问了两个问题。一个问题是，loss 必须定义，对吧？在这里，loss 必须事先定义。它不会自动学到，有时你关心 pairwise losses，有时关心 correlation，有时关心 cosine similarity。你必须指定 loss 是什么，也就是必须指定 G 是什么。嗯，但 G 可以是任何东西，可以是我们刚才讨论的任何一种。&gt;&gt; 是的。&gt;&gt; 还有一个不同之处，实际上，当它们

### [53:49](https://www.youtube.com/watch?v=u-H43tRgYJg&t=3229s) · b000069

**English**

in a supervised manner image and Apple text they should be a positive.&gt;&gt; Yeah. Yeah. So, so we started by saying that um you have paired data, right? So, apple image, apple text, orange image, orange text. So, so you need to have paired data at least in this current setting, you have supervision based on a pair data. Uh but note that the the requirements for what it need to be paired depends on the similarity function. If a similarity function is scoring that you know apple have to be similar and orange have to be similar then your pairing has to come at these individual objects. If for example I only care that uh the whole structure is the same for example if I care about these three pair wise distances being the same then I don't need actually paired data between uh I just need my three embeddings of apple orange

**中文**

以监督方式时，图像与 Apple 文本应该是一个正样本。&gt;&gt; 是的，是的。我们一开始就说，你有 paired data，对吧？苹果图像、苹果文本，橙子图像、橙子文本。所以至少在当前设定中，你需要 paired data，监督来自 paired data。呃，但注意，哪些东西需要配对，取决于 similarity function。如果 similarity function 要求苹果必须相似、橙子必须相似，那么配对就必须落实到这些单独的物体上。比如，如果我只关心整体结构相同，例如这三个 pairwise distances 相同，那么实际上我不需要……之间的 paired data，我只需要一侧有苹果、橙子、

### [54:46](https://www.youtube.com/watch?v=u-H43tRgYJg&t=3286s) · b000070

**English**

elephant on one side and I can have three embeddings of orange apple elephant on the other side I don't need the pairing between the three if I'm doing a a triplet wise similarity function like this but if I carry that apple and apple must be nearby. Then I need Yes, this is apple. This is orange. This is elephant. Then I need that.

**中文**

大象的三个 embeddings，另一侧可以有橙子、苹果、大象的三个 embeddings。如果用这种三元相似度函数（triplet wise similarity function），就不需要这三者之间的配对。但如果我关心苹果和苹果必须靠近，那么我就需要：是的，这是苹果，这是橙子，这是大象。那就需要这些。

### [55:18](https://www.youtube.com/watch?v=u-H43tRgYJg&t=3318s) · b000071

**English**

Okay. Any other questions? Great. Uh so we see yeah several things um lots of different choices for the similarity function. lots of uh different functions may been proposed throughout your really just depends on the setting whether you care about individual points being aligned whether you care about the um the global structure right the other case is the more global structure being aligned you care about pairwise relationships being aligned um all that can change what your what your similarity function is and it also changes your requirements for your supervised data right you basically need supervised data at the resolution at which you want the pairing to be achieved in a similarity function. And also want to emphasize all this again learn to end right. So your loss function which you're trying to optimize

**中文**

好。还有其他问题吗？很好。呃，我们看到了几个方面，similarity function 有很多不同选择。很多不同函数已经在……中被提出，实际上取决于具体设定：你是关心各个点对齐，还是关心全局结构，对吧？另一种情况是更全局的结构对齐，或者关心成对关系对齐。这些都会改变 similarity function，也会改变对监督数据的要求，对吧？基本上，你需要的监督数据分辨率，要与希望 similarity function 实现配对的分辨率一致。另外还想再次强调，所有这些都是端到端学习（end to end learning）的。你试图优化的 loss function

### [56:14](https://www.youtube.com/watch?v=u-H43tRgYJg&t=3374s) · b000072

**English**

is the function similarity function G on top of your two embeddings ZA and ZB but each of those two embeddings are also functions of your unit model encoders F of A modala TA F of B or Madala TB. So all this can be back propagated and trained end to end. Of course, if you see benefits of pre-training f of a and f of b uh that also works. So using that let's let's give the concrete algorithm which is you know nowadays people call it contrastive learning. Uh but again there's much more general similarity functions than just contrastive learning which is that you start with some paired data for example images and text. uh in the standard version of contrastive learning they care about having each image and text representation being very close to each other. So for that to happen you need

**中文**

是作用在两个 embeddings ZA 和 ZB 上的 similarity function G，但这两个 embeddings 本身也分别是 unit model encoders \[字幕疑误，可能指 unimodal encoders，单模态编码器\] 的函数，F of A modala TA、F of B or Madala TB \[字幕疑误，可能指带参数的模态编码器\]。所以，这一切都可以反向传播（backpropagate）并端到端训练。当然，如果预训练 f of a 和 f of b 有好处，也可以这么做。基于这一点，我们来给出具体算法，也就是现在大家所说的 contrastive learning。呃，不过还是那句话，similarity functions 比 contrastive learning 所用的要广泛得多。做法是先从一些 paired data 开始，比如图像和文本。呃，在标准版 contrastive learning 中，要求每对图像与文本表示彼此非常接近。要做到这一点，就需要

### [57:08](https://www.youtube.com/watch?v=u-H43tRgYJg&t=3428s) · b000073

**English**

paired data for each image and text right. So as an example here you would have image of that and you say text caption in blue car image and that's yellow bus image and airplane and this image that says bowl of cats. Um so using this paired data you would define each of the correspondences as positive pairs. Uh so there's four positive pairs here and anything that is not a positive pair which is a random permutation will be negative pair. Okay. So there's um 12 negative pairs here. So positive pairs in green, negative pairs in red. And then in contrasted learning, the idea is to again score this alignment between modalities by bringing positive pairs which are connected close together and pushing together negative pairs

**中文**

每张图像及其文本的 paired data，对吧？这里举个例子，有这样一张图像，文本描述是蓝色汽车；还有黄色公交车的图像、飞机，以及这张描述为“一碗猫”的图像。嗯，使用这些 paired data，你会把每个对应关系定义为正样本对（positive pairs）。呃，这里有四个 positive pairs，而任何不是 positive pair 的组合，也就是随机排列产生的组合，都是负样本对（negative pair）。好。所以这里有，嗯，12 个 negative pairs。positive pairs 用绿色表示，negative pairs 用红色表示。然后在 contrasted learning \[字幕疑误，可能指 contrastive learning\] 中，思路还是对模态之间的 alignment 打分，让有连接的 positive pairs 靠近，并把相距较远的 negative pairs 推到一起 \[原字幕如此，可能指推开\]

### [58:04](https://www.youtube.com/watch?v=u-H43tRgYJg&t=3484s) · b000074

**English**

which are far apart. Okay. And what that might look like is uh using this kind of hinge loss formulation is to maximize this function where G your similarity is scored on ZA and ZB plus which are your positive pairs. Uh that's going to be a positive dependence. So you're going to maximize the similarity and it's going to maximize a negative. So in other words, minimize the similarity of G uh between ZA and ZB minus which are your negative pairs. So four terms go into adding up the similarity between positive pairs that's maximized and 12 terms go into adding up to these um similarity functions for negative pairs which are minimized.

**中文**

好。它可能看起来像这样，使用这种合页损失（hinge loss）的形式来最大化这个函数。其中 G，也就是 similarity，作用于 ZA 和 ZB plus，也就是 positive pairs。呃，这会是一个正向依赖关系。因此你要最大化相似度，同时最大化一个负值。换句话说，就是最小化 ZA 与 ZB minus 之间的 G 相似度，它们是 negative pairs。所以四个项相加，得到 positive pairs 的相似度之和，并最大化它；12 个项相加，得到 negative pairs 的这些 similarity functions，并最小化它们。

### [58:52](https://www.youtube.com/watch?v=u-H43tRgYJg&t=3532s) · b000075

**English**

And in the um in contrastive learning, these coordination functions are are cosign similarity. And while you know contrasted learning became popular with clip nowadays, but even even back in like 20 2010s, people people were doing this albeit at a smaller scale. And once you start aligning your data like this, you actually see very interesting observations, right? So you could essentially do retrieval. Uh one really powerful thing about these alignment methods is that you can you know score a feature or your image and retrieve what is nearest in text. Uh you can do this crossodal retrieval. So you can also do this crossodal arithmetic. Uh so what's happening here is that you take a image of a blue car, you embed it into your feature space, you subtract the feature embedding of blue text and then you add the feature embedding of uh red the word

**中文**

而在，嗯，contrastive learning 中，这些 coordination functions 是 cosign similarity \[字幕疑误，可能指 cosine similarity，余弦相似度\]。虽然如今 contrasted learning \[字幕疑误，可能指 contrastive learning\] 随着 clip 流行起来，但早在大约 20、2010 年代，人们就在做这个，只是规模更小。一旦开始这样对齐数据，就会观察到一些很有意思的现象，对吧？基本上可以做检索（retrieval）。呃，这些 alignment 方法很强大的一点是，你可以对一个特征或图像打分，然后检索文本中最接近的内容。呃，可以做这种 crossodal retrieval \[字幕疑误，可能指 cross-modal retrieval，跨模态检索\]。还可以做 crossodal arithmetic \[字幕疑误，可能指 cross-modal arithmetic，跨模态算术\]。这里发生的是，取一张蓝色汽车的图像，把它嵌入特征空间，减去 blue 文本的 feature embedding，再加上，呃，red 这个词

### [59:49](https://www.youtube.com/watch?v=u-H43tRgYJg&t=3589s) · b000076

**English**

red, right? And that gives you a new feature and you can score the nearest similarities and you can retrieve uh nearest images of red cars, right? And this is only possible this kind of arithmetic minus saying some concept adding some concept is only possible when these two representation spaces are well aligned. Right? So blue text actually means something in the context of your images and the red word actually means something in the context of your images. You can take a blue image minus the word blue plus the word yellow to get yellow cars. You can do this from yellow buses to red buses. Uh you can do things like airplane photo of a plane minus the word flying plus sailing and you treat images of sailboats and even this cute bowl of cats minus the word bowl plus the word box to get a box of cats.

**中文**

red 的 feature embedding，对吧？这样就得到一个新特征，可以计算最近的相似度，检索最接近的红色汽车图像，对吧？只有当这两个表示空间很好地对齐时，这种算术，也就是减去某个概念、加上某个概念，才有可能实现。对吧？因此，blue 文本在图像的语境中确实有意义，red 这个词在图像的语境中也确实有意义。你可以用一张蓝色图像减去 blue 这个词，再加上 yellow 这个词，得到黄色汽车。也可以从黄色公交车变成红色公交车。呃，还可以拿飞机照片减去 flying 这个词，再加上 sailing，检索到帆船图像，甚至用这张可爱的“一碗猫”减去 bowl 这个词，再加上 box 这个词，得到“一箱猫”。

### [1:00:48](https://www.youtube.com/watch?v=u-H43tRgYJg&t=3648s) · b000077

**English**

So you know early signs of contrastive learning of course this was just done with small low resolution images and just one word or or one word or you know one adjective and one one uh one object for for your text. And nowadays people have really scaled this up using clip and other forms of of free training where you can get a huge bank of images and get a huge bank of their captions, right? You can get this from Wikipedia. You can get it from Instagram, Flickr and other image retrieval data sets. You have a huge bank. You put them in a batch. Everything that is in the diagonal are basically positive pairs, right? Those are examples where the image actually corresponds to the caption and everything off diagonal are basically negative pairs. Right? In this uh big batch by batch uh matrix and each of these entries in the batch obviously

**中文**

所以，这是 contrastive learning 的早期迹象。当然，当时只用小型低分辨率图像，文本也只是一个词，或者一个词，或者一个形容词加一个物体。现在，人们通过 clip 和其他形式的 free training \[字幕疑误，可能指 pre-training，预训练\]，真正把它扩展到了大规模，可以获取海量图像，以及海量对应描述，对吧？可以从 Wikipedia 获取，也可以从 Instagram、Flickr 和其他图像检索数据集获取。有了一个庞大的库，把它们放进一个批次（batch）。对角线上的所有内容基本上都是 positive pairs，对吧？也就是图像确实对应描述的例子；非对角线上的内容基本上都是 negative pairs。对吧？在这个大的 batch 乘 batch 矩阵中，每个条目显然

### [1:01:44](https://www.youtube.com/watch?v=u-H43tRgYJg&t=3704s) · b000078

**English**

passing your images to your imaging encoders you get n image embeddings. Uh you put your caption through a text encoder you get n of those text embeddings. And each of these entries are the cosine similarity between uh image embedding I with text embedding J. Right? And everything in a diagonal those cosine similarities represent positive pairs. Everything off diagonal represents negative pairs. And the contrastive learning loss would essentially be uh no longer this this uh hinge loss but rather this ratio where on the top which you are maximizing because it's a loss with a negative. So you're actually maximizing that term the similarity of positive pairs and on the bottom you're minimizing the similarity uh technically you should only minimize it over negative pairs but for implementation efficiency reasons you minimize the sum of similarities across

**中文**

都是把图像输入图像编码器，得到 n 个 image embeddings。呃，把描述输入 text encoder，得到 n 个 text embeddings。每个条目都是 image embedding I 与 text embedding J 之间的 cosine similarity。对吧？对角线上的所有 cosine similarities 表示 positive pairs；非对角线上的所有条目表示 negative pairs。contrastive learning loss 基本上不再是这个 hinge loss，而是这个比值：分子是你要最大化的，因为 loss 前面有负号，所以实际上你是在最大化这一项，也就是 positive pairs 的相似度；分母则是你要最小化的相似度。呃，严格来说，只应该对 negative pairs 最小化，但出于实现效率的原因，会最小化

### [1:02:39](https://www.youtube.com/watch?v=u-H43tRgYJg&t=3759s) · b000079

**English**

all negative pairs and that one positive pair. It's much easier to implement efficient on GPU kernels and even adding one positive pair the denominator doesn't really make a difference in practice. is still going to be dominated by about a negative pair losses. Okay. And the similarity function is still cosine similarity. So each of these are just I uh I embedding for image dotproduct embedding for text.

**中文**

所有 negative pairs 加上那一个 positive pair 的相似度之和。在 GPU kernels 上，这样更容易高效实现，而且即使在分母中增加一个 positive pair，实践中也不会造成什么差别。它仍然会主要由 negative pair losses 主导。好。而 similarity function 仍然是 cosine similarity。所以每一项都只是图像的 I，呃，I embedding 与文本 embedding 的 dot product。

### [1:03:12](https://www.youtube.com/watch?v=u-H43tRgYJg&t=3792s) · b000080

**English**

Okay. So people find that uh once you train the model in this way your encoders which are what you're being what you're training uh your encoder for language and coding for vision they're really good encoders for downstream tasks and again the key idea is that you have these embeddings that are aligned but are separate right it's not fusion but you're keeping them separate but aligned with each other and of course nowadays you can do much better crossal retrieval with these larger models. So, you could give it um give it an image. For example, this image is look like a television studio. You can give it a bunch of possible captions, right? A photo of a television studio, a photo of a podium, a photo of a conference room, lecture room, and so on. And you embed the image, get a feature. You embed each of these possible captions. You get a

**中文**

好。人们发现，一旦以这种方式训练模型，所训练的编码器，也就是语言编码器和视觉编码器，会成为非常适合下游任务（downstream tasks）的编码器。再说一次，关键思想是，这些 embeddings 已对齐，但保持独立，对吧？这不是 fusion，而是让它们保持独立、同时彼此对齐。当然，现在使用这些更大的模型，可以做效果更好的 crossal retrieval \[字幕疑误，可能指 cross-modal retrieval，跨模态检索\]。比如，给它一张图像，这张图像看起来像一个电视演播室。再给它一组可能的描述，对吧？“电视演播室的照片”“讲台的照片”“会议室的照片”“教室的照片”等等。把图像嵌入，得到一个特征；再分别嵌入这些可能的描述，得到一个

### [1:04:09](https://www.youtube.com/watch?v=u-H43tRgYJg&t=3849s) · b000081

**English**

feature and you basically score for each one what the cosign similarity is. Use that as a way to rank what is the most likely caption. So it does say a photo of a television studio. Uh here you can even find the closest caption which is a photo of a Siberian husky even though it doesn't look like a real world husky. Uh but I think it sometimes still makes mistakes. Right? In this case when clip was first released you gave it a images of these different shapes and sizes. Uh it was still not very good at counting. So it gave for example photo of three objects as the most likely instead of four objects. Uh but now these models are again much better at counting. So you can essentially learn these align representations and use them to get really good features useful for downstream tasks. You can do retrieval by scoring a similarity based on the alignment function scoring a similarity across the modalities. And not only can

**中文**

特征，然后基本上逐一计算 cosign similarity \[字幕疑误，可能指 cosine similarity，余弦相似度\]。用这个来排序，判断哪个描述最有可能。所以它确实给出了“电视演播室的照片”。呃，这里甚至可以找到最接近的描述，即“西伯利亚哈士奇的照片”，尽管它看起来不像现实中的哈士奇。呃，不过我想它有时仍会犯错，对吧？这里，在 clip 刚发布时，给它这些不同形状和大小物体的图像，它还不太擅长计数。所以，比如它认为“三个物体的照片”最有可能，而不是四个物体。呃，但现在这些模型的计数能力又强了很多。所以，基本上可以学习这些对齐表示，得到对 downstream tasks 很有用的优质特征。可以通过 alignment function 对跨模态相似度打分来做 retrieval。而且不仅

### [1:05:05](https://www.youtube.com/watch?v=u-H43tRgYJg&t=3905s) · b000082

**English**

you do retrieval, you can also kind of do this classification where uh you can give it a bunch of possible categories and let it classify by choosing which one has the highest ranked similarity with the image. That's why some people might have seen that when clip first came out, it was a big win for what we call open set or open domain classification, right? Traditionally, if you want to classify an image into different categories, you had to prespecify what the categories were, right? 10 types of digits or 50 types of of cats and dogs. You had to prespecify what these categories were. uh which either means it was either too big, a lot of them are not used, you're wasting parameters or sometimes too small and you don't are not able to classify new categories. So one of the power of these models is that you could basically give it an image, give it any number of categories, just write a caption for each category, any number any category that you want and you can

**中文**

可以做 retrieval，还可以做这种分类：给它一组可能的类别，让它选择与图像相似度排名最高的类别来分类。这也是为什么一些人可能见过，clip 刚出现时，在所谓开放集分类（open set classification）或开放域分类（open domain classification）方面取得了很大成功，对吧？传统上，如果想把图像分到不同类别，必须预先指定类别是什么，对吧？10 种数字，或者 50 种猫和狗。必须预先指定这些类别。呃，这意味着类别集合可能太大，很多类别用不到，浪费参数；有时又太小，无法对新类别进行分类。所以这些模型的一个强大之处是，基本上可以给它一张图像、任意数量的类别，只要为每个类别写一段描述，数量任意、类别任意，仍然可以

### [1:06:02](https://www.youtube.com/watch?v=u-H43tRgYJg&t=3962s) · b000083

**English**

still score the similarity and do classification over that set of categories. Any questions about clip and contrastive learning?&gt;&gt; Is there scoring with like similar classification scoring using very similarity functions? Oh, is that just&gt;&gt; um you can yeah any any similarity function you can score right take a image get the embedding right now it's cosign similarity it can be it can be um it can be kernel similarity right all of that is also super fast to compute um if I don't care about scoring a single image and categorizing it I could do the pair wise stuff that we talked about I give it two images and ask them to find the difference between them and it can still give you a bunch of categories. So

**中文**

计算相似度，并在这组类别上做分类。关于 clip 和 contrastive learning，有什么问题吗？&gt;&gt; 是否可以用各种 similarity functions，做类似分类打分的评分？哦，还是这只是……&gt;&gt; 嗯，可以，任何 similarity function 都可以打分，对吧？取一张图像，得到 embedding，现在用的是 cosign similarity \[字幕疑误，可能指 cosine similarity，余弦相似度\]，也可以是，嗯，kernel similarity，对吧？这些计算也都非常快。如果我不关心对单张图像打分和分类，也可以做我们讨论过的 pairwise 方法：给它两张图像，让它找出两者之间的差异，它仍然可以给出一组类别。所以

### [1:06:56](https://www.youtube.com/watch?v=u-H43tRgYJg&t=4016s) · b000084

**English**

now you have a a distance function over pairs instead of one image. So again this this function right this function G can be quite general as long as you can uh implement it in things like PyTorch as long as you can differentiate through it uh it can be used to be optimized and also to to do retrieval.

**中文**

现在，你有一个针对图像对的 distance function，而不是针对一张图像。再说一次，这个函数，对吧，这个 G 函数可以非常通用，只要能用 PyTorch 之类的工具实现，只要能够对它求导，就可以用来优化，也可以用于 retrieval。

### [1:07:28](https://www.youtube.com/watch?v=u-H43tRgYJg&t=4048s) · b000085

**English**

Okay, let me um wrap up this part by by kind of digging deeper into what clip and these other alignment like methods actually learn. Um so remember we had this kind of diagram where A and B have this vin diagram where there's some shared information between them which is in contrast to the unique information in them. Well, I'm going to give an intuition. I'm not going to go into too much mathematical detail, but one way of thinking about what this shared information is is this concept of mutual information. Now, mutual information is a formal measure that essentially says I'm going to look at both my modalities and I compute the ratio of two terms. One is a joint distribution between them. So, this is a distribution telling me which elements in my modalities are likely to co- occur together. Those that are higher have higher joint likelihood. Those that don't happen together have

**中文**

好，我来，嗯，最后深入一点，看看 clip 和其他类似 alignment 的方法究竟学到了什么，以此结束这一部分。嗯，还记得我们有这种图，A 和 B 构成一个 vin diagram \[字幕疑误，可能指 Venn diagram，维恩图\]，它们之间有一些共享信息，与各自独有的信息相对。我会给出一个直觉，不会深入太多数学细节。理解共享信息的一种方式，是互信息（mutual information）这个概念。mutual information 是一种形式化度量，基本上是说，查看两个模态，计算两项的比值。一项是它们之间的联合分布（joint distribution）。这个分布告诉我，模态中的哪些元素可能一起出现。数值较高的具有更高的联合似然（joint likelihood），不会一起出现的则具有

### [1:08:25](https://www.youtube.com/watch?v=u-H43tRgYJg&t=4105s) · b000086

**English**

lower joint likelihood. That is a joint distribution. And I'm going to compare that to the product of marginal distributions. Product of marginal distributions can be thought of as basically saying I have everything in X, everything in Y. I randomly pair them up. Right? So it's not going to capture any joint distribution, but I randomly pair them up. So mutual information can be thought of as a difference between the actual pairings in my data where this corresponds to this the actual pairing versus a random assortment random way of pairing them up. So for data sets in which information is really large uh that ratio will also be very large. For data sets which are completely independent the two circles don't overlap completely independent that basically means even the paired data that you observe and a random pairing that you get from your data is going to be the same right there's zero mutual information at intuitive level u you can read into

**中文**

更低的 joint likelihood。这就是 joint distribution。我要把它与边缘分布的乘积（product of marginal distributions）比较。product of marginal distributions 可以理解为：我拥有 X 中所有东西、Y 中所有东西，然后随机把它们配对，对吧？所以它不会捕获任何 joint distribution，只是随机配对。因此，mutual information 可以理解为，数据中的实际配对，也就是这个对应那个的实际配对，与随机组合、随机配对方式之间的差异。所以，对信息非常多的数据集，呃，这个比值也会非常大。对完全独立的数据集，两个圆不重叠、完全独立，这基本上意味着，即使你观察到的 paired data，与从数据中随机配对得到的数据，也会一样，对吧？直观上，mutual information 为零。呃，你们可以阅读

### [1:09:20](https://www.youtube.com/watch?v=u-H43tRgYJg&t=4160s) · b000087

**English**

the mathematical details. Well, one can show that um these clip-like losses, specifically this type of of of clip loss, uh actually focuses on capturing the shared information, but more formally, it provably learns this mutual information that you have between these modalities, right? I can uh give you a a quick proof of this um but not required, won't won't be in the homeworks or the exams. But if you think about what this info inc loss looks like, which is that it's scoring this function f, right? This function f is the one that you're learning using cosine similarity. There's a function f that scores highly positive pairs, right? The similarity for positive pairs should be very high and it scores very low negative pairs, right? The the similarity of negative pairs should be very low, right? Okay,

**中文**

数学细节。可以证明，嗯，这些类似 clip 的 losses，具体来说是这种 clip loss，呃，确实专注于捕获共享信息；更正式地说，可以证明它会学习这些模态之间的 mutual information，对吧？我可以给你们一个简短证明，嗯，但不要求掌握，不会出现在作业或考试中。不过，想一下这个 info inc loss \[字幕疑误，可能指 InfoNCE loss\] 的形式，它是在对这个函数 f 打分，对吧？这个 f 就是你使用 cosine similarity 学习的函数。函数 f 会给 positive pairs 很高的分数，对吧？positive pairs 的相似度应该非常高，而给 negative pairs 很低的分数，对吧？negative pairs 的相似度应该非常低，对吧？好，

### [1:10:17](https://www.youtube.com/watch?v=u-H43tRgYJg&t=4217s) · b000088

**English**

so you can actually think of that function as a critic function which takes in two modalities A and B which are either the true parents and that should be as high as possible the output or it's a randomly sampled pair right negative pair and it should be as low as possible that output. So in other words it can be thought of as a classifier can be thought of as a classifier that outputs something between zero and one. It outputs one if it's a positive pair and it outputs zero if it's negative pair. Right? Based on what we know about these positive and negative pairs, you can also make the argument that uh it outputs one for positive pairs which are sampled from the joint distribution between A and B because joint distributions exactly are the ones which have high likelihood for these positive pairs. And otherwise this model would output zero a very low score for samples A and B uh sampled from the product of marginalss. Right? P of A times P of B.

**中文**

所以实际上可以把它看作一个评判函数（critic function），接收两个模态 A 和 B。它们要么是 true parents \[字幕疑误，可能指 true pairs，真实配对\]，此时输出应该尽可能高；要么是随机采样的一对，也就是 negative pair，此时输出应该尽可能低。换句话说，可以把它看成一个分类器，一个输出介于零和一之间的分类器。如果是 positive pair，就输出一；如果是 negative pair，就输出零。对吧？根据我们对这些正负样本对的了解，也可以认为，它对从 A 和 B 的 joint distribution 采样的 positive pairs 输出一，因为 joint distributions 恰恰给这些 positive pairs 较高的似然。否则，对从 product of marginalss \[字幕疑误，可能指 product of marginals，边缘分布乘积\] 中采样的 A 和 B，模型会输出零，也就是很低的分数。对吧？P of A 乘 P of B。

### [1:11:15](https://www.youtube.com/watch?v=u-H43tRgYJg&t=4275s) · b000089

**English**

Because again a definition of multiplying these two marginals together is you randomly sample something from A and you randomly sample something from B and you pair them up without regard for whether it was the actual pairing or not. And that's the definition of a negative pair. So uh that can be thought of as a function that you're learning in contrastive learning uh to basically train a binary classifier that scores samples from the joint distribution very high positive pairs and score samples that you get from the product of marginalss very low which are your negative pairs. And you can show that also when this is optimally trained uh what this classifier has to end up learning is exactly that ratio right the ratio we're given a particular A and B the ratio that it estimates that it came from a joint distribution versus the ratio that it came from these product of marginal distributions. Uh so that's actually what um these models end up learning

**中文**

因为，把这两个边缘分布相乘的定义，就是从 A 随机采样一个东西，再从 B 随机采样一个东西，把它们配对，而不考虑是否为实际配对。这就是 negative pair 的定义。所以，呃，可以把 contrastive learning 中学到的函数理解为，基本上训练一个二分类器（binary classifier），给来自 joint distribution 的样本，也就是 positive pairs，很高的分数；给来自 product of marginalss \[字幕疑误，可能指 product of marginals，边缘分布乘积\] 的样本，也就是 negative pairs，很低的分数。而且可以证明，当它被最优地训练时，这个 classifier 最终必须学到的，恰好就是那个比值，对吧？给定某个 A 和 B，它估计其来自 joint distribution 与来自这些 product of marginal distributions 的比值。呃，所以这实际上就是这些模型最终学到的东西

### [1:12:13](https://www.youtube.com/watch?v=u-H43tRgYJg&t=4333s) · b000090

**English**

when you train it using contrastive learning. And you can then plug this far which is the function that you've learned back into your objective function law uh L which essentially gives you this equation which is that your L-star which is the objective function once this has converged is essentially at least this expectation term and you see this ratio of likelihoods right P of A time P of B over the joint distribution of both A and B and we saw that it was actually very similar to So the mutual information that we just saw, right? So in fact you can show that this loss is at least uh negative mutual information plus log n where n is the batch size number of samples. In other words, your mutual information is at least your loss, right? Or negative loss, which is your objective. Um and what that means

**中文**

当你用 contrastive learning 训练它时。然后可以把这个 far \[字幕疑误，可能指 f\*\]，也就是学到的函数，代回目标函数 law，呃，L \[字幕疑误，可能指 loss L\]，基本上得到这个方程：L-star，也就是收敛后的目标函数，基本上至少等于这个 expectation 项。你会看到这个似然比，对吧？P of A 乘 P of B，除以 A 和 B 的 joint distribution。我们看到，它实际上与刚才看到的 mutual information 非常相似，对吧？因此，实际上可以证明，这个 loss 至少等于负 mutual information 加 log n，其中 n 是 batch size，也就是样本数量。换句话说，mutual information 至少等于 loss，对吧？或者说负 loss，也就是你的目标。嗯，这意味着

### [1:13:07](https://www.youtube.com/watch?v=u-H43tRgYJg&t=4387s) · b000091

**English**

is that basically NCE maximizes a lower bound on your mutual information. So uh the best that you can learn is the total amount of mutual information between your modalities A and B. Uh again not not required for for the homeworks or or for the um midterms but good to know. Key takeaway is that you can actually prove that um these contrastive learning methods are learning some classifier that separates out data samples from the joint distribution which is your positive pairs and data samples from your product of marginal distributions which are your negative pairs. And that ratio is something very consequential and important in statistics and machine learning known as a mutual information. And that basically means that contrastive learning is basically learning as best as it can is bounded by the total mutual information in your data.

**中文**

基本上，NCE 在最大化 mutual information 的一个下界（lower bound）。所以，呃，你能学到的最好结果，就是模态 A 和 B 之间 mutual information 的总量。呃，再说一次，作业或期中考试不要求掌握，但知道这一点很好。关键要点是，实际上可以证明，这些 contrastive learning 方法在学习某个 classifier，它把 joint distribution 中的数据样本，也就是 positive pairs，与 product of marginal distributions 中的数据样本，也就是 negative pairs 区分开。这个比值是统计学和机器学习中非常重要、影响很大的东西，称为 mutual information。这基本上意味着，contrastive learning 能学到的最佳内容，受数据中 mutual information 总量的限制。

### [1:14:05](https://www.youtube.com/watch?v=u-H43tRgYJg&t=4445s) · b000092

**English**

But then there's also very important implications which is that if you want to use alignment to learn better representations, it really matters how much mutual information there is, how much shared information there is in your data. So ideally right if this is the perfect scenario where your modalities A and B overlap exactly so that alignment captures this thing in the middle and that information in the middle is what you care about for downstream tasks right either downstream retrieval classification whatever tasks that's perfect right your contrasted learning learns that overlap in the middle is nothing more nothing less all that you need for your task Um, in other words, this is the multiv-view redundancy assumption where the mutual information between X1 and X2, which is what you learn in these alignment based contrasted learning

**中文**

但这也有非常重要的含义：如果想用 alignment 学习更好的表示，数据中有多少 mutual information、多少共享信息，就非常重要。理想情况下，如果这是一个完美场景，模态 A 和 B 恰好重叠，因此 alignment 捕获中间这部分，而中间的信息正是你在 downstream tasks 中关心的，无论是 retrieval、classification 还是其他任务，那就很完美，对吧？contrasted learning \[字幕疑误，可能指 contrastive learning\] 学到中间的重叠部分，不多不少，恰好是任务所需的全部。嗯，换句话说，这就是多视图冗余假设（multiv-view redundancy assumption）\[字幕疑误，可能指 multi-view redundancy assumption\]：X1 和 X2 之间的 mutual information，也就是这些基于 alignment 的 contrasted learning

### [1:15:03](https://www.youtube.com/watch?v=u-H43tRgYJg&t=4503s) · b000093

**English**

methods is exactly the information between X1 and Y and also X2 and Y. But why is the task that you care about? Uh this spells trouble which is that what you care about learning important for your downstream task is uh much more than the actual shared information between them. Right? This is trouble because there's not enough signal. Alignment and contrasted learning is going to learn that little bit of overlap over there but it's not enough. You're losing a lot of information important for your task if you do alignment and contrasted learning. So you're in trouble there. And this other setting, you're also in trouble because there's way too much overlap in your data such that contrasted learning and alignment learns too much uh learns too much, learns too much redundant features and is not specific enough uh to be used for the downstream tasks that you care about. So that's when things are just right. There's also extremes when there's not

**中文**

方法学到的内容，恰好等于 X1 与 Y 之间的信息，也等于 X2 与 Y 之间的信息。但 why \[字幕疑误，可能指 Y\] 是你关心的任务。呃，这就意味着麻烦：你关心的、对 downstream task 重要的学习内容，呃，远远多于它们实际共享的信息。对吧？这很麻烦，因为信号不够。alignment 和 contrasted learning \[字幕疑误，可能指 contrastive learning\] 会学到那里那一点重叠，但这不够。如果做 alignment 和 contrasted learning，你会丢失很多对任务重要的信息。所以这里会遇到问题。而在另一种设定中，也会遇到问题，因为数据中的重叠太多，使得 contrasted learning 和 alignment 学得太多，呃，学得太多，学到了过多冗余特征，却不够有针对性，无法用于你关心的 downstream tasks。所以，那是恰到好处的情况。也存在一些极端情况，信息不

### [1:15:59](https://www.youtube.com/watch?v=u-H43tRgYJg&t=4559s) · b000094

**English**

enough information or too much information and too much noise. People

**中文**

足，或者信息太多、噪声太多。人们

### [1:16:11](https://www.youtube.com/watch?v=u-H43tRgYJg&t=4571s) · b000095

**English**

can also uh people have also shown this in practice which is that you can basically construct synthetic data which overlap in different degrees and also design where the task is and you get some very cool plots like this one over here right uh you start by increasing the information so here there's no overlap on the on the left side the mutual information is zero so two variables are independent they don't overlap and you're slowly starting to increase the overlap between uh x1 and x2 right so they're becoming closer and closer and they overlap more and more at first when they're completely independent they don't overlap and you bring them closer and overlap with each other performance improves right this is the range of going from not enough overlap to getting more and more overlap and finally having a really good uh representation learn from alignment and then if you start making them overlap even more afterwards. That's when you go into this range where there's too much

**中文**

也可以，呃，人们也在实践中展示了这一点：基本上可以构造重叠程度不同的合成数据（synthetic data），并设计任务的位置，然后得到像这里这样很有意思的图，对吧？先逐渐增加信息。这里左侧没有重叠，mutual information 为零，所以两个变量独立，不重叠。然后逐渐增加 x1 与 x2 之间的重叠，对吧？它们越来越近，重叠越来越多。最初它们完全独立、不重叠，随着你让它们靠近、彼此重叠，性能会提高，对吧？这个区间就是从重叠不足，到重叠越来越多，最终通过 alignment 学到非常好的表示。之后，如果继续让它们更多地重叠，就会进入这个区间，那里有太多

### [1:17:08](https://www.youtube.com/watch?v=u-H43tRgYJg&t=4628s) · b000096

**English**

noise. So you start seeing performance to drop off uh when those representations are used for downstream tasks. Okay. So to really summarize this part um this you know information uh sorry this this multimodal alignment really arise on the assumption that this shared information is what's important. the overlap between them. For example, what is both in the image and also in the caption, it can be formalized by mutual information. Um, which basically means that you know if if that is a representation important for your downstream tasks, then you're golden, right? It learns the mutual information, it helps you learn better representations. Uh, but otherwise, you know, you can be in trouble either because you're learning too much or you're learning too little.

**中文**

噪声。所以，当这些表示被用于 downstream tasks 时，就会开始看到性能下降。好，真正总结一下这部分，嗯，这个信息，呃，抱歉，这个 multimodal alignment 实际上依赖这样一个假设：共享信息才是重要的，也就是它们之间的重叠。例如，同时存在于图像和描述中的内容，可以通过 mutual information 形式化。嗯，这基本上意味着，如果它是对 downstream tasks 重要的表示，那就非常理想，对吧？它学习 mutual information，帮助你学习更好的表示。呃，否则，你可能会遇到问题，要么学得太多，要么学得太少。

### [1:18:01](https://www.youtube.com/watch?v=u-H43tRgYJg&t=4681s) · b000097

**English**

Okay, let me end there for today. We are at time. Um, does yes question&gt;&gt; as in

**中文**

好，今天就到这里。时间到了。嗯，有……请说，有问题。&gt;&gt; 就是

### [1:18:22](https://www.youtube.com/watch?v=u-H43tRgYJg&t=4702s) · b000098

**English**

like you're doing it? That seems like the here.&gt;&gt; Yeah.&gt;&gt; Oh, I think that's a typo. That should say alignment. Sorry. Yeah. Uh, but you I think you're asking a very good broader question which is how does fusion and alignment uh these two concepts interact with each other, right? Um, fusion as we discussed was all about learning one joint representation. alignment is keeping things separate um and and yet align using these similarity functions. Um there are several several things first of all uh for homework two I'm sure some of you have seen a reading assignment there's this paper on a line before a fuse and I'm sure there's also other papers saying fuse before a line and then so one way of thinking about it is what do you do first right do you do you kind of get these data and get features that are aligned so they're semantically

**中文**

比如你在做这个？那似乎是这里的……&gt;&gt; 是的。&gt;&gt; 哦，我想那是个笔误。那里应该写 alignment。抱歉。是的。呃，但我想你问了一个很好的、更广泛的问题，就是 fusion 和 alignment 这两个概念如何相互作用，对吧？嗯，正如我们讨论的，fusion 是学习一个 joint representation。alignment 则是保持独立，嗯，同时用这些 similarity functions 进行对齐。嗯，有几个方面。首先，作业二里，我相信一些人已经看到了一项阅读任务，有一篇关于 a line before a fuse \[字幕疑误，可能指 Align Before Fuse\] 的论文。我相信也有其他论文说 fuse before a line \[字幕疑误，可能指 fuse before align\]。所以一种思考方式是，先做什么，对吧？是先获取这些数据，得到对齐的特征，让它们在语义上

### [1:19:19](https://www.youtube.com/watch?v=u-H43tRgYJg&t=4759s) · b000099

**English**

similar they're nearby in embedding space and then do fusion on top of that right that's one very viable alternative or you can also start doing fusion first and then start doing contrastive learning maybe on the fused features. Um, and of course there's also settings which do fusion without alignment and alignment without fusion and vice versa. Um, so I I would say it's it's kind of a I don't have the answer. I think it's a it's open question. Uh there's really pros and cons to each. Sometimes they they both have to be done in the same system. Uh sometimes no.&gt;&gt; You could just take your online

**中文**

相似，在 embedding space 中接近，然后在此基础上做 fusion，对吧？这是一种非常可行的选择。也可以先做 fusion，然后开始做 contrastive learning，也许作用于融合后的特征。嗯，当然，也有做 fusion 而不做 alignment，以及做 alignment 而不做 fusion 的设定，反过来也一样。嗯，所以我会说，这有点像……我没有答案。我认为这是一个开放问题。呃，每种方式确实都有优缺点。有时二者必须在同一个系统中完成，有时则不需要。&gt;&gt; 你可以直接取你的 online \[字幕疑误，可能指 aligned 表示\]

### [1:19:59](https://www.youtube.com/watch?v=u-H43tRgYJg&t=4799s) · b000100

**English**

And then&gt;&gt; yes, you could do that as well, right? Uh so you could align your features as we discussed some like over here. Uh you could align your features if it captures the the mutual information really well and your task Y also just so happens to be in that shared space, then alignment is actually a very good training signal for downstream tasks, right? That's why um that's why you know we saw a clip and these clip representations were actually very useful training signal uh because most of the times what I care about in the image is also what somebody would describe in the caption right it's purposely discarding the background and the texture and time of day when these things are just not very important is really just looking at all the people and the objects and the categories. So when that assumption holds it can actually work for very powerful

**中文**

然后……&gt;&gt; 是的，也可以这么做，对吧？呃，可以像我们讨论的这里这样，对齐你的特征。如果对齐后的特征很好地捕获了 mutual information，而任务 Y 又恰好位于这个共享空间中，那么 alignment 实际上就是 downstream tasks 非常好的训练信号，对吧？这就是为什么，嗯，我们看到 clip，这些 clip 表示实际上是很有用的训练信号，因为大多数时候，我在图像中关心的东西，也正是别人会在描述中提到的东西，对吧？它刻意丢弃背景、纹理和一天中的时间，因为这些东西并不那么重要，而真正关注所有人物、物体和类别。所以，当这个假设成立时，它确实可以得到非常强大的

### [1:20:54](https://www.youtube.com/watch?v=u-H43tRgYJg&t=4854s) · b000101

**English**

representations but when it doesn't then you got to do more fusion. Yeah. Yeah. Also this uh and in fact this doesn't really capture anything about synergy right when there's synergy when there's unique information. This is only just looking at the the overlap in information space. is not looking at the other uniqueness and synergy that we also discussed as other possible information sources.&gt;&gt; Yeah. Like for the figure on the right like let's say like when the when they have like excess mutual information but the task only you like only uses a subset of that um like what is a way to like reduce um like to reduce their overlap so that we can use this information in a like in a more efficient way.&gt;&gt; Uh good question.

**中文**

表示；但如果不成立，就需要做更多 fusion。是的，是的。另外，这实际上也没有捕获任何 synergy，对吧？当存在 synergy、存在独有信息时，它只关注信息空间中的重叠，不关注我们也讨论过的其他可能信息来源，也就是独有性和 synergy。&gt;&gt; 是的。比如右边的图，假设它们有过多 mutual information，但任务只使用其中一个子集，那么有什么方法可以减少，嗯，减少它们的重叠，让我们能更高效地使用这些信息？&gt;&gt; 呃，好问题。

### [1:21:48](https://www.youtube.com/watch?v=u-H43tRgYJg&t=4908s) · b000102

**English**

So one way is to do data augmentation. Um so in fact a lot of these you can check out some of the papers. Uh a lot of these principles are designed a lot of the principles for data augmentation are designed with this. So for example I take an image right and I'm trying to do some classification parts. I know I can rotate it turn into grayscale uh crop it out and drop some pixels. Why why can I do that? All of those augmentations are basically just providing different views of your data, right? And these different views they some information is outside and some is overlapping with the original image and I'm assuming that what is overlapping with the original image is just the object in question right I can make grayscale the object still stays there and some other things over this I can rotate it like using another vend diagram but at the same time it still overlaps with this. We're trying to like focus the data more into the the overlap.&gt;&gt; Right.&gt;&gt; Right. Right.

**中文**

一种方法是数据增强（data augmentation）。嗯，实际上，很多这些内容可以去看一些论文。呃，很多原则，很多 data augmentation 的原则，就是围绕这一点设计的。比如，我取一张图像，对吧，想做一些分类。我知道可以旋转它、变成灰度图、裁剪、丢掉一些像素。为什么能这样做？所有这些 augmentations 基本上都是在提供数据的不同视图（views），对吧？这些不同 views 中，一些信息在外面，一些与原图重叠。我假设与原图重叠的部分，就是所关注的物体，对吧？可以变成灰度图，物体仍然在那里，还有这边其他一些东西。我可以旋转它，比如用另一个 vend diagram \[字幕疑误，可能指 Venn diagram，维恩图\]，但同时仍然与这里重叠。我们是在尝试让数据更集中到重叠部分。&gt;&gt; 对。&gt;&gt; 对，对。

### [1:22:45](https://www.youtube.com/watch?v=u-H43tRgYJg&t=4965s) · b000103

**English**

&gt;&gt; Uh but again, that's not that's that's good intuition, but it's also not easy to do in practice, right? Because sometimes you cannot you don't know what uh what is would would stay in the middle and maybe what also goes too much or too little. Great. All right. Thanks. You're all free to go and

**中文**

&gt;&gt; 呃，不过，这不是……这是很好的直觉，但在实践中也不容易做到，对吧？因为有时你无法……你不知道什么会留在中间，也不知道什么可能变得太多或太少。很好。好，谢谢。大家可以走了，还有
