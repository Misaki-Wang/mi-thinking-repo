# Lecture 4 – Multimodal Fusion (MIT How to AI Almost Anything/Multimodal AI, Spring 2026)

_Bilingual transcript · 双语讲稿_

- Channel: Paul Liang
- Source: [YouTube](https://www.youtube.com/watch?v=0SOieOIe4HI)
- Duration: 35:01
- Caption source: automatic
- Status: complete
- Chinese translation: 40/40
- Translation provider: codex
- Generated: 2026-09-07T07:42:35+00:00

## Transcript · 讲稿

### [00:01](https://www.youtube.com/watch?v=0SOieOIe4HI&t=1s) · b000001

**English**

Wait. So, um as I mentioned, I'll lecture for about for about 30-35 minutes and I want to save some time for Edgar to to run through a quick tutorial about implementing some of these uh multimodal fusion methods and giving a kind of pre-tutorial for homework two. Um so I'll be talking about multimodal fusion. Uh you have probably already seen a a glimpse of this from Demetrius' lecture last Thursday, the power of using different data modalities in his context for for healthcare applications. So, couple of quick updates. Uh as I mentioned at the beginning of class, just to recap again, project proposal due today, so be with me later for the 5:00 p.m. We're just staying in the same Zoom link, office hours if you need any more feedback. Uh I'm hoping to meet with every group at least once either today or on Thursday for their project ideas. Uh some other good news, we have been able to secure some compute credits uh for your course projects. I'm assuming based on this number that we'll

**中文**

等等。那么，嗯，正如我提到的，我会讲大约、大约 30-35 分钟，我想留一些时间给 Edgar，让他快速讲解一个关于实现这些多模态融合（multimodal fusion）方法的教程，也算是作业二的预备教程。嗯，所以我要讲的是 multimodal fusion。呃，你们可能已经从 Demetrius 上周四的讲座中初步看到了，在他的医疗应用场景中，使用不同数据模态（data modalities）的力量。那么，先快速更新几件事。呃，正如我在上课开始时提到的，再回顾一下，项目提案今天截止，所以稍后下午 5:00 来找我。我们就留在同一个 Zoom 链接里，如果你们还需要反馈，那就是答疑时间。呃，我希望今天或周四至少和每个小组见一次，讨论你们的项目想法。呃，还有一些好消息，我们已经为你们的课程项目争取到了一些计算额度。我根据这个人数估计，我们会有

### [00:56](https://www.youtube.com/watch?v=0SOieOIe4HI&t=56s) · b000002

**English**

have uh roughly 40 groups for the class. We have roughly about 80 registered students, uh 80-90 registered students, so that'll be about at most 40 groups. So, we may be able to secure 40 \* $50 of Kimi credits. Have folks heard of the Kimi language model series? Anybody raise their hands? It's one of the um it's one of the Chinese companies, one of the up-and-rising Chinese companies uh building language models and building multimodal language models. So, they've kindly donated $40 worth of credits and I also have been able to secure 40 \* $40 worth of credits for you to use in any other LLM API uh or compute API. So, roughly that'll be 40 \* \* $90 per per group if there's about 40 groups. Um so you can budget that into your planning for the course project. Um and as I mentioned, homework two was released last week, that'll be due next

**中文**

大约 40 个小组。我们大约有 80 名注册学生，呃，80-90 名注册学生，所以最多大约是 40 个小组。因此，我们可能能争取到 40 \* $50 的 Kimi 额度。大家听说过 Kimi 语言模型（language model）系列吗？有人举手吗？它是一家，嗯，是一家中国公司，一家正在崛起的中国公司，正在开发语言模型和多模态语言模型。所以，他们慷慨地捐赠了价值 $40 的额度，我也为你们争取到了 40 \* $40 的额度，可以用于任何其他大语言模型（Large Language Model, LLM）API 或计算 API。所以，如果大约有 40 个小组，那大致就是每组 40 \* \* $90。嗯，你们可以把这个预算纳入课程项目的规划。嗯，正如我提到的，作业二上周已经发布，将于下周

### [01:52](https://www.youtube.com/watch?v=0SOieOIe4HI&t=112s) · b000003

**English**

Wednesday. Uh so, be sure to be uh working on that. So, in today's lecture, we are going to cover some basics of multimodal fusion, starting from different ways different modalities interact, and using that as a formal paradigm for understanding what uh good ways of fusing them exist and out there. We'll broadly categorize this into early, intermediate, and late fusion uh as a general taxonomy. And then we'll go into a bit deeper methods that are based on a dynamic fusion, so where the fusion can also adjust according to different data points and input samples. And finally, I'll cover a little bit on how do you quantify the success of fusion, and whether you can be sure what your model is actually learning. Um can't see everybody's faces, but raise your hand on Zoom if you have a question in the middle of this this uh lecture. So, at a high level, uh multimodal fusion is, you know, one of the biggest challenges in multimodal learning,

**中文**

三截止。呃，所以一定要开始做。那么，今天的讲座中，我们会介绍 multimodal fusion 的一些基础知识，从不同模态之间相互作用的不同方式开始，并以此作为一个形式化范式，来理解有哪些好的融合方式。我们会按照一个总体分类，把它大致分为早期融合（early fusion）、中间融合（intermediate fusion）和后期融合（late fusion）。然后，我们会深入一点，介绍基于动态融合（dynamic fusion）的方法，也就是融合还可以根据不同的数据点和输入样本进行调整。最后，我会稍微介绍一下如何量化融合的成功程度，以及你是否能确定模型实际上在学习什么。嗯，我看不到所有人的脸，不过，如果你们在这次、这次讲座中途有问题，就在 Zoom 上举手。那么，从宏观上看，multimodal fusion 是，你知道，多模态学习（multimodal learning）中最大的挑战之一，

### [02:51](https://www.youtube.com/watch?v=0SOieOIe4HI&t=171s) · b000004

**English**

right? You have to learn representations. You often have to learn representations that models how different data modalities interact with each other. And it really goes back to the key principles of multimodal, which is that data is often uh heterogeneous. So, from data that's more similar to each other, and which is easier to fuse, or to uh settings in which your data modalities are much more heterogeneous, in which case it becomes harder to fuse them together. So, you can think about it as, you know, if it's more homogeneous, assuming you might have already extracted some features from your modalities, and the features that you extract represent more semantic information, and there's opportunity for them to be more homogeneous with each other. Whereas, fusion in raw modalities, you're often fusing at the level of raw data, which is often more heterogeneous and different from each other. So, if you're already working with pre-extracted features, or in other words, abstract

**中文**

对吧？你必须学习表征（representations）。你通常必须学习能够建模不同数据模态如何相互作用的表征。而这确实可以追溯到多模态的关键原则，也就是数据往往是异质的（heterogeneous）。所以，从彼此更相似、也更容易融合的数据，到数据模态差异大得多的场景，在后一种情况下，将它们融合到一起就会更困难。所以，你可以这样理解，你知道，如果它们更加同质（homogeneous），假设你可能已经从各个模态提取了一些特征（features），而你提取的特征代表更多语义信息，那么它们就有机会变得更加同质。而在原始模态中进行融合时，你通常是在原始数据层面进行融合，这些数据往往更异质，彼此差异更大。因此，如果你已经在使用预先提取的特征，或者换句话说，抽象

### [03:42](https://www.youtube.com/watch?v=0SOieOIe4HI&t=222s) · b000005

**English**

modalities, the fusion can be more simple, uh but also more constrained. On the other hand, if you're working directly with raw data, you might need to design a more complicated fusion method, but at the same time you have the opportunity for it to be more expressive. So, there's various trade-offs on how much feature extraction to extract in this unimodal data before you do the fusion, or do you just directly do fusion from from raw data? Uh but at a high level, the purpose of fusion is to learn these joint representations combining your data modalities that exploits how these different modalities interact with each other. So, what do I mean by interactions? Um We've already seen some some glimpse of interactions. I like to think of it as again three settings in which they all require different types of fusion. Right? One setting is when you're very much looking at the overlapping information between the two modalities for your task, which we term redundancy. All

**中文**

模态，融合可以更简单，呃，但也会受到更多限制。另一方面，如果你直接处理原始数据，可能就需要设计更复杂的融合方法，但与此同时，它也有机会拥有更强的表达能力。所以，在融合之前，要对这些单模态（unimodal）数据做多少特征提取（feature extraction），或者是否直接从、从原始数据进行融合，这其中存在各种权衡。呃，不过从宏观上看，融合的目的是学习这些结合数据模态的联合表征（joint representations），利用不同模态之间相互作用的方式。那么，我说的相互作用（interactions）是什么意思？嗯，我们已经初步见过一些、一些相互作用。我还是喜欢把它看作三种场景，每一种都需要不同类型的融合。对吧？一种场景是，你主要关注两个模态中与任务有关的重叠信息，我们称之为冗余（redundancy）。好，

### [04:36](https://www.youtube.com/watch?v=0SOieOIe4HI&t=276s) · b000006

**English**

right? The type of fusion we design when there's redundancy is going to be very different from the fusion that you design for other types of interactions. So, an example of redundancy is when you're saying something positive with a smile on your face, um and that is the positive present in both. That's very indicative. Another type of interaction, as you recall, is this uniqueness, where there's information in one that's not in the other. And in this case, uh for example, you're saying something positive but with neutral facial expressions. It's really about identifying which modality has the positive information. So, fusion in this case, the purpose is to identify which of the modalities has the unique information and which of the ones you should ignore. And the third type of interaction, which again calls for its own type of fusion methods, is called synergy, where uh this information isn't present in either of the modalities to begin with, but it is emerging as a result of this

**中文**

对吧？存在 redundancy 时，我们设计的融合类型，与针对其他相互作用类型设计的融合会很不一样。所以，redundancy 的一个例子是，你面带微笑地说着积极的话，嗯，积极信息同时存在于两者中。这很有指示性。你们还记得，另一种相互作用是独特性（uniqueness），也就是一个模态中有另一个模态中没有的信息。在这种情况下，呃，例如，你说着积极的话，但面部表情是中性的。这里真正要做的是识别哪个模态具有积极信息。因此，在这种情况下，融合的目的是识别哪个模态具有独有信息，以及哪些模态应当忽略。第三种相互作用，同样也需要它自身对应的融合方法，称为协同（synergy），也就是，呃，这种信息最初并不存在于任何一个模态中，而是由于这种

### [05:31](https://www.youtube.com/watch?v=0SOieOIe4HI&t=331s) · b000007

**English**

fusion between them. So, the example I like to give is when you're saying something positive with angry expressions, and together you're you're likely to think that the person is actually being sarcastic. So, different types of interactions intuitively give rise to different types of fusion methods, and different fusion methods are suitable in different settings. So, what then are at a high level different types of fusion methods? Again, I emphasized one important consideration is whether you first use encoders to extract features. If you do, then that gives you a chance to bring these features closer together, they're already more homogeneous, and design more simple fusion approaches. So, some of the heavy lifting to deal with the heterogeneity is done by these unimodal encoders. You extract features, and now you're doing feature-level fusion. So, I'll focus on this part first. Um as an example, images, you might pass

**中文**

模态之间的融合而涌现出来。所以，我喜欢举的例子是，你带着愤怒的表情说着积极的话，把两者结合起来，你、你很可能会认为这个人实际上是在讽刺。所以，直观上，不同类型的相互作用会产生不同类型的融合方法，而不同的融合方法适用于不同的场景。那么，从宏观上看，有哪些不同类型的融合方法？再说一次，我强调过，一个重要考虑因素是，你是否先用编码器（encoders）提取特征。如果是，这就给了你机会让这些特征彼此更接近，它们已经更加同质，你也就可以设计更简单的融合方式。因此，处理异质性（heterogeneity）的一部分繁重工作，是由这些单模态编码器完成的。你提取特征，现在做的是特征层面的融合（feature-level fusion）。所以，我先重点讲这一部分。嗯，举个例子，对于图像，你可以先把

### [06:27](https://www.youtube.com/watch?v=0SOieOIe4HI&t=387s) · b000008

**English**

them first to some vision transformer or CNN. Uh for language, you pass them to your word embeddings, pre-trained sentence representations like BERT or your language models. These can be any of the unimodal encoders that we basically saw uh last week in lecture, where we had, you know, a deep discussion on different types of inductive biases and different types of architecture that works the best for images and language and graphs and so on. So, we'll first cover fusion in this setting, where I'm assuming you have good unimodal encoders, allowing you to extract features. These features are semantically meaningful, which means they're often already quite close to each other, right? You have image representations representing the objects like your cats and dogs, and you have your language representation of uh these cats and dogs. So, they're already very close together. How do you do fusion? I also want to note that these unimodal encoders can be jointly learned with the

**中文**

它们传给某个视觉 Transformer（vision transformer）或卷积神经网络（Convolutional Neural Network, CNN）。呃，对于语言，你可以把它们传给词嵌入（word embeddings）、像 BERT 这样的预训练句子表征（pre-trained sentence representations），或者你的语言模型。这些可以是我们上周课堂上基本已经见过的任何单模态编码器，当时我们，你知道，深入讨论了不同类型的归纳偏置（inductive biases），以及最适合图像、语言、图等数据的不同架构。所以，我们先介绍这种场景下的融合，我假设你有很好的单模态编码器，可以提取特征。这些特征在语义上是有意义的，这意味着它们通常已经彼此很接近，对吧？你有表示猫、狗等对象的图像表征，也有这些猫和狗的语言表征。所以，它们已经非常接近了。你要如何融合？我还想指出，这些单模态编码器可以和

### [07:24](https://www.youtube.com/watch?v=0SOieOIe4HI&t=444s) · b000009

**English**

fusion network. So, these two unimodal encoders and your fusion can be trained end-to-end for some objective, or these unimodal encoders can also be pre-trained. Pre-trained and frozen, for example, using a pre-trained BERT model or pre-trained vision transformer model for your language and vision modalities. So, given these features, there is usually two levels, two extremes, and often times most types of fusion will fall in the middle. Uh you have early fusion and late fusion. Right, in early fusion, what that happens is that you have these features, you concatenate them early on, all right, where concatenation is the fusion operator, and then you give it to some classification model. Now, we call this early fusion intuitively because fusion is done very early at the feature level or even at the raw data level, uh before a model makes a prediction on these labels.

**中文**

融合网络（fusion network）联合学习。因此，这两个单模态编码器和你的融合部分，可以针对某个目标进行端到端（end-to-end）训练；或者这些单模态编码器也可以是预训练的。预训练并冻结（frozen），例如，对语言和视觉模态使用预训练的 BERT 模型或预训练的 vision transformer 模型。因此，给定这些特征，通常有两个层次、两个极端，而大多数融合类型往往位于中间。呃，你有 early fusion 和 late fusion。对，在 early fusion 中，发生的事情是，你有这些特征，在一开始就把它们拼接（concatenate）起来，好吧，其中拼接（concatenation）就是融合算子（fusion operator），然后把它交给某个分类模型。我们直观地把它叫作 early fusion，是因为融合发生得很早，在特征层面，甚至在原始数据层面，呃，在模型对这些标签做出预测之前。

### [08:19](https://www.youtube.com/watch?v=0SOieOIe4HI&t=499s) · b000010

**English**

On the other extreme, you also have late fusion. Late fusion describes a setting where you make predictions uh YA for modality A and predictions YB for modality B. So, it directly goes to the prediction level or the final layer of the prediction level, for example, the softmax label uh level, and then fusion is only done at a very late stage after predictions have already been made. Uh so, these are two extremes. They are, again, different pros and cons to each. Early fusion uh can be very expressive because you're concatenating the data at the beginning. So, you're leaving room for your model to essentially learn all the ways in which different features in your two modalities can interact and combine with each other. Uh so, it can be much more expressive. Uh the downside is that often it's not very understandable. It's very black box because uh you only concatenate your data, you don't really have control over which features are interacting with which

**中文**

另一个极端是 late fusion。late fusion 描述的是这样一种场景：你对模态 A 做出预测 YA，对模态 B 做出预测 YB。因此，它直接进入预测层面，或者预测层面的最后一层，例如 softmax 标签层面，然后只有在预测已经做出之后，才在非常晚的阶段进行融合。呃，所以，这是两个极端。再说一次，它们各有不同的优缺点。early fusion 可以有很强的表达能力，因为你在一开始就把数据拼接起来了。因此，你给模型留下了空间，让它基本上能够学习两个模态中的不同特征相互作用、彼此组合的所有方式。呃，所以，它可以有强得多的表达能力。呃，缺点是，它通常不太容易理解。它很像一个黑箱（black box），因为你只是拼接数据，并不能真正控制哪些特征与哪些

### [09:18](https://www.youtube.com/watch?v=0SOieOIe4HI&t=558s) · b000011

**English**

other ways uh with other features. And at the same time, this can also result in your prediction model, your your fusion model being much more uh larger in parameters, right, because you're basically operating on the concatenation of your data. Late fusion is better because now you can really understand what each modality was predicting, and each of these prediction models is uh you know, smaller, fewer parameters. Smaller, fewer parameters because they only operate on single modalities. Uh the downside then is that this does not lead for very expressive fusion. You're only combining the labels and taking a vote over the labels instead of being more expressive in your fusion. So, these are two extremes. Um but in the more general case, you know, you often have methods that take in some set of features, define some fusion method, uh get some other set of features, and this can be really

**中文**

其他方式，呃，与其他特征发生相互作用。同时，这也可能导致你的预测模型、你的、你的融合模型参数规模大得多，对吧，因为你基本上是在拼接后的数据上操作。late fusion 在这方面更好，因为现在你确实可以理解每个模态在预测什么，而且每一个预测模型都，呃，你知道，更小，参数更少。更小、参数更少，因为它们只处理单个模态。呃，那么缺点就是，这不能带来表达能力很强的融合。你只是组合标签，并对标签进行投票，而不是让融合有更强的表达能力。所以，这是两个极端。嗯，但在更一般的情况下，你知道，通常有一些方法，接收一组特征，定义某种融合方法，呃，得到另一组特征，而这可以非常

### [10:14](https://www.youtube.com/watch?v=0SOieOIe4HI&t=614s) · b000012

**English**

flexible interpolating between super early fusion and and super uh late fusion. So, to see some of these fusions in practice, I am going to start simple where um we just study a univariate case. So, assume you have XA, XB, and Y, right? So, we have two modalities such as one dimension, so one number for each, and your label Y is also just one number, so one. So, in the most general setting, uh you consider you consider linear uh fusion, which is basically linear regression, right? You can have Y, which is your label, equal to some intercept W0 that doesn't depend on your data XA and XB. You have some error, which is your residual term, which is all the error um which you cannot capture using your data XA and XB. You can have additive terms, so W1 XA

**中文**

灵活，在非常早的融合与非常、非常晚的融合之间进行插值。所以，为了看看这些融合在实际中如何运作，我会从简单的情况开始，嗯，我们只研究一个单变量（univariate）的情况。假设你有 XA、XB 和 Y，对吧？我们有两个模态，比如各是一维，也就是每个只有一个数，而标签 Y 也只是一个数，所以一个。那么，在最一般的场景中，呃，你考虑、你考虑线性融合（linear fusion），它基本上就是线性回归（linear regression），对吧？你的 Y，也就是标签，可以等于某个截距（intercept）W0，它不依赖于数据 XA 和 XB。你有一些误差，也就是残差项（residual term），它包含了所有，嗯，无法利用数据 XA 和 XB 捕捉的误差。你可以有加性项（additive terms），也就是 W1 XA

### [11:11](https://www.youtube.com/watch?v=0SOieOIe4HI&t=671s) · b000013

**English**

plus W2 times XB. So, these are your additive terms that are basically linear combinations of XA and XB. And finally, the interesting multimodal case, or the fusion case, is this multiplicative term where uh you have a feature which is the multiplication of XA and XB. That's a new feature, and there's some associated weight W3 that you can learn on top of this uh new feature. So, in the most general setting, you can have intercepts, which are just bias terms, additive linear combinations of A and B with a weights W1, W2, and this multiplicative term XA \* XB with some weight W3. Right? And these are fairly interpretable, so I'm just going to go with this example just to demonstrate this. Let's say you're trying to rate how much people like these books. Right? And you're basically looking at video reviews of them reviewing the books to determine how much they like

**中文**

加上 W2 乘以 XB。所以，这些就是加性项，基本上是 XA 和 XB 的线性组合。最后，有趣的多模态情况，或者说融合情况，是这个乘性项（multiplicative term），其中，呃，你有一个特征，它是 XA 和 XB 的乘积。这是一个新特征，而你可以在这个新特征之上学习一个与之对应的权重 W3。所以，在最一般的情况下，你可以有截距，也就是偏置项（bias terms）；带有权重 W1、W2 的 A 和 B 的加性线性组合；以及带有某个权重 W3 的乘性项 XA \* XB。对吧？这些都相当容易解释，所以我就用这个例子来演示。假设你想评估人们有多喜欢这些书。对吧？你基本上是在看他们评论这些书的视频评论，以确定他们有多喜欢

### [12:08](https://www.youtube.com/watch?v=0SOieOIe4HI&t=728s) · b000014

**English**

it. So, Y is the score of the book 0 to 100, higher is better, that they like the book. XA could be a feature where you're recording how much time they're smiling when reviewing the book. So, that's a continuous variable from 0 to 100%. And XB, just for the sake of um heterogeneity, assume it is a binary variable. Assuming zero if this person is not a professional critic, and one if the person is a professional critic. Right? So, you have a binary variable 0 or 1 for XB, you have a continuous variable XA for percentage of time smiling, and you have a continuous regression score Y, which is the score of how much they like the book. So, if you imagine fitting these different models, right? And each of these weights in this fusion term carry different intuitive meanings. So, W0 is basically the average score when the person is never smiling and when the person is not a

**中文**

它。因此，Y 是书的评分，0 到 100，越高越好，表示他们喜欢这本书的程度。XA 可以是一个特征，记录他们在评论这本书时有多少时间在微笑。所以，这是一个从 0 到 100% 的连续变量（continuous variable）。而 XB，只是为了，嗯，体现异质性，假设它是一个二元变量（binary variable）。假设这个人不是专业评论家时为零，是专业评论家时为一。对吧？所以，XB 是一个取值为 0 或 1 的二元变量，XA 是微笑时间百分比这个连续变量，还有一个连续的回归分数 Y，表示他们有多喜欢这本书。因此，想象一下拟合这些不同的模型，对吧？融合项中的每一个权重都有不同的直观含义。所以，W0 基本上就是当这个人从不微笑，而且不是

### [13:04](https://www.youtube.com/watch?v=0SOieOIe4HI&t=784s) · b000015

**English**

critic. When XA and XB are zero, everything else reduces to just W0. W1 are the effects, so the relationship between how much a person smiles and how much they like the book. And also the relationship between XB, how much whether a person is a critic and whether they like the book. Right? And W3 is the fusion. It is the interaction effect from XA and XB. And epsilon is the error. So, you can think about fitting each of these terms, assuming we start simple, just using percentage of time a person is smiling to predict whether they like the book. So, you could fit this model. It's basically a linear regression model, where W0 is the intercept, and W1 is the slope, right? Intercept of 4.6, meaning if they never smile at all in the video, the audience score was 4.6 out of 10. And W1, meaning, you know, for one extra unit of the person smiling in the video,

**中文**

评论家时的平均分数。当 XA 和 XB 都为零时，其他所有东西都化简掉，只剩 W0。W1 是效应，也就是一个人微笑的多少与他有多喜欢这本书之间的关系。还有 XB，也就是一个人有多、是否是评论家，与是否喜欢这本书之间的关系。对吧？而 W3 就是融合。它是来自 XA 和 XB 的交互效应（interaction effect）。epsilon 是误差。因此，你可以考虑拟合这些项中的每一项，假设我们从简单的情况开始，只用一个人微笑的时间百分比来预测他是否喜欢这本书。那么，你可以拟合这个模型。它基本上是一个线性回归模型，其中 W0 是截距，W1 是斜率（slope），对吧？截距是 4.6，意思是如果他们在视频里完全不笑，观众评分就是 10 分中的 4.6 分。而 W1 的意思是，你知道，这个人在视频中微笑每增加一个单位，

### [14:01](https://www.youtube.com/watch?v=0SOieOIe4HI&t=841s) · b000016

**English**

uh the score increases by 1.2. Right? So, that's fairly intuitive, uh W0 and W1. Now, you can think of having a regression model which is purely additive. So, this is just additive fusion. W1 \* XA + W2 \* XB. It's purely additive fusion. And what that would look like is this. Right? Again, I'm plotting the relationship between XA and Y. First of all, consider the setting when XB is zero. So, this term goes away. That basically says, when the person is not a critic, they have an intercept of 5.2, and they have a slope of 1.2 1.19. Right? Basically saying that, when a person is not a critic, the more they smile, the more they enjoy the book by roughly 1.2 slope. And what's interesting is now when you have this XB variable non-zero. So, when this XB variable is one, so when the person is a critic, so they

**中文**

呃，分数就增加 1.2。对吧？所以，W0 和 W1 是相当直观的。现在，你可以考虑一个纯加性的回归模型。所以，这就是加性融合（additive fusion）。W1 \* XA + W2 \* XB。这是纯粹的 additive fusion。它看起来会是这样。对吧？我再次画出 XA 和 Y 之间的关系。首先，考虑 XB 为零的情况。那么，这一项就消失了。这基本上是在说，当这个人不是评论家时，他们的截距是 5.2，斜率是 1.2 1.19。对吧？基本上就是说，当一个人不是评论家时，他笑得越多，就越喜欢这本书，斜率大约是 1.2。有趣的是，现在这个 XB 变量不为零了。所以，当 XB 为一，也就是当这个人是评论家时，也就是他们

### [14:58](https://www.youtube.com/watch?v=0SOieOIe4HI&t=898s) · b000017

**English**

review books as a profession, you see this entire slope go down. Right? The slope is the same. It's just shifted by down parallel, in this case by the amount of W2, which is minus 1.7. And that basically means two things. First of all, um the relationship between how much a person smiles and the score that they gave is the same. It's 1.19. It's the same positive effect whether the person was a critic or was not critic. Right? And then what this second thing means is that when a person is a critic, on average their scores are minus 1.69 lower. Right? So, when XB is one, when they are a critic, when they review books professionally, their score reduces by 1.69 uh on average. So, you get these effects visually, right? Two lines, they're parallel, it's just that one is lower than the other when the XB variable is one.

**中文**

以评论书籍为职业，你会看到这整个斜率向下移动。对吧？斜率是一样的。只是平行向下移动了，在这里移动的量是 W2，也就是负 1.7。这基本上意味着两件事。首先，嗯，一个人微笑的多少与他给出的评分之间的关系是一样的。是 1.19。无论这个人是不是评论家，都是同样的正向效应。对吧？然后，这第二件事的意思是，当一个人是评论家时，平均来说，他们的分数低负 1.69。对吧？所以，当 XB 为一，当他们是评论家、以评论书籍为职业时，他们的分数平均降低 1.69。因此，你可以直观地看到这些效应，对吧？两条线是平行的，只是当 XB 变量为一时，其中一条比另一条更低。

### [15:54](https://www.youtube.com/watch?v=0SOieOIe4HI&t=954s) · b000018

**English**

So, that's the kind of functions that you can learn with additive fusion. Again, in this very simple one-dimensional case. Now, of course, the interesting case happens when you have both additive and multiplicative terms. Like additive, which is W1XA + W2XB, multiplicative, which is this W3 term uh as a coefficient for that XA \* XB. So, unsurprisingly, you can run through this example, and you can start seeing that you can model functions like this. And what's happening here? Again, let's consider the simple case, uh the line in red when the person is not a critic. So, XB is zero, this term goes away, and this term also goes away. Then you recover the original linear function, which is that when the person is not a critic, they have some baseline score, which is the intercept, and they have this baseline um

**中文**

所以，这就是你能够用 additive fusion 学到的函数类型。同样，这是在这个非常简单的一维情况下。当然，有趣的情况发生在你同时拥有加性项和乘性项时。比如加性项，也就是 W1XA + W2XB；乘性项，也就是这个 W3 项，呃，它是 XA \* XB 的系数。所以，不出所料，你可以顺着这个例子算下去，然后开始看到，你能够对这样的函数进行建模。那么，这里发生了什么？我们再次考虑简单的情况，呃，当这个人不是评论家时，对应红色的线。所以，XB 为零，这一项消失了，这一项也消失了。然后，你就恢复了原来的线性函数，也就是，当这个人不是评论家时，他们有某个基准分数，也就是截距，还有这个基准，嗯，

### [16:50](https://www.youtube.com/watch?v=0SOieOIe4HI&t=1010s) · b000019

**English**

baseline slope, which is 0.68, right? The more they smile, the more they enjoy the book. You also have now when you have this score, when the person is a critic, when this is one and when this is one, first of all, W2 is negative. So, as a whole, when people are critic, they reduce by minus 2.9. Right? They are in general more harsh when they are a critic. And then also look at this multiplicative When this XB is one, you get a new coefficient in front of XA, which is W3. So now the XA coefficient becomes W1 plus W3, and we see that in this case W3 was learned to be 1.29. Which basically means when a person is a critic and when they smile more, that actually changes the relationship between how much a person smiles and how much they enjoy the book. So overall, this change in the relationship allows you to basically

**中文**

基准斜率，也就是 0.68，对吧？他们笑得越多，就越喜欢这本书。现在你还有，当你有这个分数，当这个人是评论家，当这里是一、这里也是一时，首先，W2 是负的。所以，总体来说，当人们是评论家时，他们会减少负 2.9。对吧？当他们是评论家时，通常会更苛刻。然后，再看这个乘性项。当这个 XB 为一时，你会在 XA 前面得到一个新的系数，也就是 W3。因此，现在 XA 的系数变成了 W1 加 W3，我们看到，在这个例子中学到的 W3 是 1.29。这基本上意味着，当一个人是评论家，而且笑得更多时，这实际上改变了一个人微笑的多少与他有多喜欢这本书之间的关系。所以，总体而言，这种关系上的变化基本上让你能够

### [17:47](https://www.youtube.com/watch?v=0SOieOIe4HI&t=1067s) · b000020

**English**

rotate these two lines so that they're no longer uh parallel to each other and it's just a shift, but also changing. The presence of XB changes the relationship between XA and Y. So in this case, the intuitive thing happening is that when a person is a critic and they really don't smile, then they really score the book really low. But when a person is a critic, when they smile more, that means they really enjoy the book and they score the book higher. So basically critics are more extreme both in the negative and in the positive scenarios uh compared to people who are not critics. So, that's an intuitive representation graphically of what this multiplicative interaction looks like. Key idea is that it is no longer the same relationship between XA and Y, but XB as a variable is able to change the relationship, the linear relationship between XA and Y. That's why you have this rotation going on.

**中文**

旋转这两条线，使它们不再，呃，彼此平行，也不只是平移，而是还会改变。XB 的存在改变了 XA 和 Y 之间的关系。因此，在这个例子中，直观上发生的是，当一个人是评论家，而且确实不怎么笑时，他给这本书的评分真的很低。但当一个人是评论家，而且笑得更多时，就意味着他确实很喜欢这本书，会给这本书更高的评分。所以，基本上，与不是评论家的人相比，评论家在负面和正面这两种情况下都更加极端。呃，这就是这种乘性交互（multiplicative interaction）的直观图形表示。关键在于，XA 和 Y 之间不再是同样的关系，而 XB 作为一个变量，能够改变 XA 和 Y 之间的关系，也就是线性关系。这就是这里发生旋转的原因。

### [18:47](https://www.youtube.com/watch?v=0SOieOIe4HI&t=1127s) · b000021

**English**

Any questions so far based on this visual, but also very simple explanation of additive and multiplicative fusion?

**中文**

到目前为止，对于这个直观、同时也非常简单的加性融合和乘性融合（multiplicative fusion）的解释，大家有什么问题吗？

### [19:01](https://www.youtube.com/watch?v=0SOieOIe4HI&t=1141s) · b000022

**English**

Great. So to summarize, a lot of fusion is about uh capturing both additive and multiplicative terms. You can also think of it as a first order and higher order terms. A first order interaction would just be function of A plus function of B. Multiplicative, or in this case second order, would be functions of XA times XB. And of course, you have the general setting where you can have both additive and multiplicative terms. So, you have the first order terms and the second order terms.

**中文**

很好。那么总结一下，很多融合方法都在于，呃，同时捕捉加性项和乘性项。你也可以把它们看作一阶项（first order terms）和高阶项（higher order terms）。一阶交互就是 A 的函数加上 B 的函数。乘性交互，或者在这个例子中是二阶交互（second order），就是 XA 乘以 XB 的函数。当然，你也有同时包含加性项和乘性项的一般情况。所以，你有一阶项和二阶项。

### [19:37](https://www.youtube.com/watch?v=0SOieOIe4HI&t=1177s) · b000023

**English**

Uh as I mentioned in the general setting, it need not just be a linear function, W1 times XA. It can be a general, you know, general function, f of A uh plus f of B. And they're added together. So, what happens when you go to more than one dimension? So, let's say XA and XB are now multi-dimensional. So, in this case, they're four dimensions. One way of doing this multiplication is basically element-wise. Right? You have a function on the four elements of A, you have a function on the four elements of B. You take these four elements, you do element-wise product, you get the same four-dimensional feature, which is element-wise product, and that could also go through some other function. So, that is the most direct extension, element-wise product to capture um the element-wise interactions between A and B. Of course, that doesn't capture all of the interactions, right? If you have a

**中文**

呃，正如我在一般情况下提到的，它不必只是线性函数 W1 乘以 XA。它可以是一般的，你知道，一般函数，A 的 f，呃，加上 B 的 f。它们相加。那么，当维度超过一维时，会发生什么？假设 XA 和 XB 现在是多维的。所以，在这个例子中，它们是四维的。一种做这种乘法的方法基本上是逐元素的（element-wise）。对吧？你对 A 的四个元素有一个函数，对 B 的四个元素有一个函数。你取这四个元素，做逐元素乘积（element-wise product），得到同样是四维的特征，也就是 element-wise product，而它还可以再经过某个其他函数。所以，这是最直接的扩展，通过 element-wise product 来捕捉，嗯，A 和 B 之间逐元素的相互作用。当然，这并不能捕捉所有相互作用，对吧？如果你有一个

### [20:34](https://www.youtube.com/watch?v=0SOieOIe4HI&t=1234s) · b000024

**English**

four-dimensional vector A and a four-dimensional vector B, in fact, there are 16 16 different pairwise interactions uh between those four by four features. And there's a name to this. It is called bilinear fusion. Uh instead of element-wise product, what we're essentially doing is an outer product, right? You take a four by one vector and a uh a one by four vector, you do outer product, you get a four by four matrix, which basically represents how each of the four dimensions are interacting with each of the other four representations. So, more expressive, need not assume that only the elements in the same in the same dimension order are interacting with each other. So, that's called bilinear fusion was found to be very powerful in capturing uh you know, expressive and useful multimodal interactions.

**中文**

四维向量 A 和一个四维向量 B，实际上，这四乘四个特征之间有 16、16 种不同的成对交互（pairwise interactions）。这有一个名称，叫作双线性融合（bilinear fusion）。呃，我们实际做的并不是 element-wise product，而是外积（outer product），对吧？你取一个四乘一的向量和一个，呃，一乘四的向量，做 outer product，得到一个四乘四的矩阵，它基本上表示四个维度中的每一个如何与另外四个表征中的每一个发生相互作用。因此，它的表达能力更强，不必假设只有相同、相同维度顺序上的元素才会相互作用。所以，这叫 bilinear fusion，研究发现它在捕捉，呃，你知道，表达能力强且有用的多模态交互方面非常强大。

### [21:28](https://www.youtube.com/watch?v=0SOieOIe4HI&t=1288s) · b000025

**English**

Uh we also mentioned that sometimes you don't just want the multiplicative terms, you also want the additive terms, right? You want not just the high order, but also the lower order. And there's a trick of doing this. If you have two vectors representing XA and XB, which are four-dimensional, you just append a one, which is a constant one vector at the back. So, now it's five-dimensional. And then you do your bilinear product. So, what that would look like is XA with the one concatenated transpose times XB with a one um vector, right? So, this would be a 5 by 1 times 1 by 5, which gives you a 5 by 5 matrix. And this 5 by 5 matrix uh is basically made out of of of of a 4 by 4 region, which is the XA XB multiplicative interaction, or you can call them bimodal interactions. They will have a term, which is the XA times the one, which is the XA vector, the XB times the one, which is the XB vector, and the one times the one, which is the

**中文**

呃，我们还提到，有时候你不只想要乘性项，也想要加性项，对吧？你不仅想要高阶项，也想要低阶项。有一个技巧可以做到这一点。如果你有两个分别表示 XA 和 XB 的四维向量，只要在末尾追加一个一，也就是一个常量一向量。那么，它现在就是五维的。然后，你做双线性乘积（bilinear product）。它看起来就是：拼接一个一后的 XA 的转置，乘以带有一个一的 XB，嗯，向量，对吧？所以，这会是一个 5 乘 1 乘以 1 乘 5，得到一个 5 乘 5 的矩阵。这个 5 乘 5 的矩阵，呃，基本上由一个、一个、一个、一个 4 乘 4 的区域构成，这个区域是 XA XB 的乘性交互，或者你可以称之为双模态交互（bimodal interactions）。它们还会有一项，也就是 XA 乘以一，即 XA 向量；XB 乘以一，即 XB 向量；以及一乘以一，也就是

### [22:24](https://www.youtube.com/watch?v=0SOieOIe4HI&t=1344s) · b000026

**English**

constant vector. So, this trick of appending the one essentially gives you the higher order interactions, but also the lower order interactions and also the constant bias term, uh which is everything that you need for for for learning the um your label. In three dimensions uh with in three modalities, this works as well. Uh you can append a one, and you can essentially do this outer product now with three vectors. So, XA with a one, XB with a one, and XC with a one, and you get this very pretty diagram, which we called a tensor fusion. You have this 4 by 4 by 4 block here which is capturing the three-way interactions. Right, there 64 of them three-way interactions. There's a 4 by 4 which is between XA and B. 4 by 4 between XA and C and a 4 by 4

**中文**

常量向量。因此，这个追加一的技巧，实际上既给了你高阶交互，也给了你低阶交互，还给了你常量偏置项，呃，这就是学习你的，嗯，标签所需要的全部东西。在三维，呃，有三个模态时，这也同样适用。呃，你可以追加一个一，然后基本上对三个向量做这个 outer product。所以，XA 加一个一，XB 加一个一，XC 加一个一，你就得到这个非常漂亮的图，我们称之为张量融合（tensor fusion）。这里有一个 4 乘 4 乘 4 的块，用来捕捉三路交互（three-way interactions）。对，一共有 64 个三路交互。XA 和 B 之间有一个 4 乘 4 的区域。XA 和 C 之间有一个 4 乘 4，另一个 4 乘 4

### [23:19](https://www.youtube.com/watch?v=0SOieOIe4HI&t=1399s) · b000027

**English**

between XB and C. These are your bimodal interactions and you also have your unimodal which is just XA, B, C and you have the one at the end. Right, just that the constant term one. So, it's a nice way of getting your bias, unimodal, bimodal and trimodal which we call tensor fusion and you have some very fancy diagrams that we drew. So, this is great. We found that these methods are very expressive. They give really good performance. In this case, we were doing this tensor fusion for combining human spoken language which is text with your facial expressions which is video with audio which is their voice. Right, and they were very good at learning these three-way interactions and giving really good performance on understanding what people were saying and their sentiment and emotions when they were saying it. Of course, one big challenge is that if

**中文**

位于 XB 和 C 之间。这些就是你的双模态交互，还有单模态部分，也就是 XA、B、C，最后还有那个一。对，就是常数项一。因此，这是一个很好的方式，可以得到偏置、单模态、双模态和三模态部分，我们称之为 tensor fusion，而且我们画了一些非常精美的图。所以，这很好。我们发现，这些方法的表达能力很强。它们的表现非常好。在这个例子中，我们用 tensor fusion 来结合人类口语，也就是文本；面部表情，也就是视频；以及音频，也就是他们的声音。对，它们非常擅长学习这些三路交互，并且在理解人们说了什么，以及说话时的情感倾向（sentiment）和情绪（emotions）方面，表现非常好。当然，一个很大的挑战是，如果

### [24:15](https://www.youtube.com/watch?v=0SOieOIe4HI&t=1455s) · b000028

**English**

you include this as a layer in your neural network, right? Because your data will come in, you will form this tensor and that will be your new new input to your model, then first of all, this is very high dimensional. Right, this is basically 5 by 5 by 5 125 dimensions. So, that's really very high dimensional and it scales even more quadratically with the number of modalities and the dimension of each modality. And also, if you want to take this as a layer and go to your next layer, say your next layer is is dimension 10 for example. For example, your 10 dimensional softmax layer, then the weight matrix will be 125 by 10. That brings it to the next layer. Right? Because this is 125 dimensions, and your softmax layer could be 10. So, not only is this tensor very large in dimension, your subsequent weight matrix will also be very large in in dimension.

**中文**

你把它作为神经网络（neural network）中的一层，对吧？因为数据会进来，你会构造这个张量（tensor），它将成为模型的新、新输入，那么首先，它的维度非常高。对，这基本上是 5 乘 5 乘 5，125 维。所以，这确实是非常高维的，而且随着模态数量和每个模态维度的增加，它还会以更大的二次方规模增长。另外，如果你想把它作为一层，再进入下一层，比如说下一层的维度是、是 10。例如，你的 10 维 softmax 层，那么权重矩阵（weight matrix）就会是 125 乘 10。它把数据映射到下一层。对吧？因为这里是 125 维，而 softmax 层可以是 10。所以，不仅这个张量的维度非常大，后续权重矩阵的维度也会非常大。

### [25:12](https://www.youtube.com/watch?v=0SOieOIe4HI&t=1512s) · b000029

**English**

Uh so, what do you do? Well, there's a trick to some of these higher-order interactions. And the trick is essentially to use low-rank approximations. Right? Power of these low-rank approximations basically says that I can have very high-dimensional matrices or high-dimensional tensors, but instead of representing all the entries, I'm going to use low-rank representations to basically, you know, represent and store much fewer parameters than I actually need. Right? And when your low-rank approximation is good, then you're not going to lose a lot of precision and accuracy, and yet you can still store at much lower dimensions. So, what do I mean by this? So, I'm just going to go back to the two-dimensional or two-modality case, just so it's easier to visualize. We saw tensor fusion where you had a vision representation with a one and a language representation with a one. You're doing

**中文**

呃，那么怎么办？对于其中一些高阶交互，有一个技巧。这个技巧基本上就是使用低秩近似（low-rank approximations）。对吧？这些 low-rank approximations 的力量基本上在于，我可以有非常高维的矩阵或高维张量，但我不会表示所有元素，而是使用低秩表征（low-rank representations），基本上，你知道，用远少于实际所需的参数进行表示和存储。对吧？当 low-rank approximation 足够好时，你就不会损失很多精度和准确率，同时仍然可以用低得多的维度来存储。那么，我是什么意思？我先回到二维或者双模态的情况，只是为了更容易可视化。我们见过 tensor fusion，其中有一个加了一的视觉表征和一个加了一的语言表征。你在做

### [26:07](https://www.youtube.com/watch?v=0SOieOIe4HI&t=1567s) · b000030

**English**

this outer product, which gives you this matrix of bimodal, unimodal, and the one at the bias term, right? And then if you have some next hidden layer in your model, then not only is this matrix large, but this weight matrix that does the linear mapping from the Z to H is even larger. This will basically be the dimension of Z repeated by H, right? Z by H. So, this weight matrix is large. So, what are low-rank approximations? Uh well, one low-rank approximation is basically your SVD, right? Or a way of representing your matrix W as not all matrices of dimension W, but as, you you outer products of individual vectors. So, what that would look like is that you will first do this low-rank decomposition of your weight W. So, it's not the entire matrix, but just an an approximation of several outer products of different vectors.

**中文**

这个 outer product，它给出这个包含双模态、单模态以及偏置项处的一的矩阵，对吧？然后，如果模型里还有下一个隐藏层（hidden layer），那么不仅这个矩阵很大，执行从 Z 到 H 的线性映射（linear mapping）的权重矩阵还要更大。它基本上会是 Z 的维度重复 H 次，对吧？Z 乘 H。所以，这个权重矩阵很大。那么，什么是 low-rank approximations？呃，一种 low-rank approximation 基本上就是奇异值分解（Singular Value Decomposition, SVD），对吧？或者说，是一种表示矩阵 W 的方式，不是把它表示成所有维度为 W 的矩阵，而是表示成，你、你，单独向量的 outer products。那么，它会是这样：你首先对权重 W 进行低秩分解（low-rank decomposition）。所以，不是整个矩阵，而只是若干不同向量的外积构成的一个、一个近似。

### [27:05](https://www.youtube.com/watch?v=0SOieOIe4HI&t=1625s) · b000031

**English**

You would decompose your input tensor Z because Z is directly represented by your two input modalities. I'm actually not going to create Z and just keep the original vectors, and I'm going to rearrange the computation. So, what does that look like? It looks something like this, where my weight matrix W can actually be represented by a summation of different low-rank factors that uh when taken outer product with each other equal to your original matrix W. Right? Visually, it looks like this. So, this W can be represented as a summation of different low-rank factors. Right? Each of these is outer product uh dimension of your first modality times H times dimension of the second modality times H. If you do a outer product, this H dimension remains, and you do a outer product to get this square, which is your dimension of your first

**中文**

你会分解输入张量 Z，因为 Z 是由两个输入模态直接表示的。我实际上不会创建 Z，而是只保留原始向量，并重新安排计算。那么，这是什么样的？大概是这样，我的权重矩阵 W 实际上可以表示为不同低秩因子（low-rank factors）的和，这些因子相互做 outer product 后，等于原来的矩阵 W。对吧？从图上看，就是这样。所以，这个 W 可以表示为不同 low-rank factors 的和。对吧？其中每一个都是 outer product，呃，第一个模态的维度乘 H，乘以第二个模态的维度乘 H。如果你做一个 outer product，这个 H 维度保留下来，然后做 outer product 得到这个方形，也就是第一个

### [28:03](https://www.youtube.com/watch?v=0SOieOIe4HI&t=1683s) · b000032

**English**

modality times dimension of your second modality. Of course, one outer product is not enough to represent all of these weight matrices, but if you have several additions of these outer products, then you can start approximating these weight matrices to arbitrary precision. Right? But in practice, we find that most of these weight matrices that you learn in neural networks, their rank is actually surprisingly low. They can have dimensions, you know, 700, 800, but their rank is typically 10 or 50. If you do a SVD, for example, the eigenvalues really drop off after 10 or 50. So, you can actually save substantial memory. So, I'll represent all these weight matrices as a summation of different outer products. Each of these will be your trainable parameters. I'm going to instead of creating this Z tensor, I'm just going to keep it as uh your individual vectors. And we've shown that the multiplication

**中文**

模态的维度乘以第二个模态的维度。当然，一个 outer product 不足以表示所有这些权重矩阵，但如果你把若干个这样的 outer products 相加，就可以开始以任意精度近似这些权重矩阵。对吧？但在实践中，我们发现，在神经网络中学到的大多数权重矩阵，它们的秩（rank）实际上出人意料地低。它们的维度可能是，你知道，700、800，但它们的秩通常是 10 或 50。例如，如果你做 SVD，特征值（eigenvalues）\[术语疑误，此处可能指奇异值（singular values）\]在 10 或 50 之后就会明显下降。所以，你实际上可以节省大量内存。因此，我会把所有这些权重矩阵表示成不同 outer products 的和。其中每一个都会是你的可训练参数（trainable parameters）。我会，不去创建这个 Z 张量，而只是把它保留为，呃，各个独立向量。我们已经证明，这个乘法

### [28:59](https://www.youtube.com/watch?v=0SOieOIe4HI&t=1739s) · b000033

**English**

is essentially equivalent to your first modality multiplied by the factors of the first modality times the second modality multiplied by the factors of the second modality. Right? So, it becomes much faster computation that does not require explicitly forming this matrix and learning the entire weight vector.

**中文**

基本上等价于，第一个模态乘以第一个模态的因子，再乘以第二个模态乘以第二个模态的因子。对吧？所以，计算会快得多，不需要显式构造这个矩阵，也不需要学习整个权重向量。

### [29:30](https://www.youtube.com/watch?v=0SOieOIe4HI&t=1770s) · b000034

**English**

So, details are are in these papers. Um you can refresh some of your linear algebra about low-rank approximations, but it is a general approach of dealing with very large neural network parameters. And nowadays, you know, from this citation here as well, I'm sure some of you have seen uh Laura and other ways of fine-tuning, the same idea exists, right? If you have these huge language models with huge weight matrices that are 700 by 700, you don't have to update all of those parameters. You can essentially do a low-rank approximation and update your 700 by 10 times 10 by 700 uh set of parameters. So, you're actually substantially reducing the parameters that you're actually updating.

**中文**

所以，细节在这些论文里。嗯，你可以复习一下线性代数中关于 low-rank approximations 的知识，不过，这是一种处理规模非常大的神经网络参数的通用方法。而如今，你知道，也从这里的这篇引用来看，我相信你们当中有些人见过，呃，Laura \[字幕疑误，可能指 LoRA\] 和其他微调（fine-tuning）方式，同样的思想也存在，对吧？如果你有这些庞大的语言模型，其中有 700 乘 700 的巨大权重矩阵，你不必更新所有这些参数。你基本上可以做一个 low-rank approximation，然后更新你那组 700 乘 10 再乘以 10 乘 700 的参数。所以，你实际上大幅减少了真正需要更新的参数。

### [30:16](https://www.youtube.com/watch?v=0SOieOIe4HI&t=1816s) · b000035

**English**

So, this is very useful for for multimodal learning, especially because when you have different modalities, you start learning the interactions between them. Your additive, multiplicative, and other higher-order multiplications between them, they get very complicated very quickly. These low-rank approximations are are a lifesaver. And you'll see some of this in your homework as well. I want to just quickly cover uh some other aspects of fusion. So everything we've seen so far involved XA XB and basically what we call a static weight. So the weights W1 times XA plus W2 times XB, these weights W1 and W2 are basically the same for all data points, right? It's just a fixed given weight. Of course, you can further extend it to have weights that are dependent on your data. So sometimes they call them gates that you know take in the current XA and

**中文**

所以，这对于、对于 multimodal learning 非常有用，尤其是因为当你有不同的模态时，就会开始学习它们之间的交互。它们之间的加性、乘性以及其他高阶乘法，会很快变得非常复杂。这些 low-rank approximations 真是救星。你们在作业中也会看到其中一些内容。我想快速介绍一下，呃，融合的其他一些方面。所以，到目前为止，我们看到的一切都涉及 XA、XB，以及基本上我们所说的静态权重（static weight）。也就是权重 W1 乘以 XA 加 W2 乘以 XB，这些权重 W1 和 W2 基本上对所有数据点都是一样的，对吧？它就是一个固定的给定权重。当然，你可以进一步扩展，让权重依赖于数据。所以，有时候它们被称为门（gates），它们，你知道，接收当前的 XA 和

### [31:13](https://www.youtube.com/watch?v=0SOieOIe4HI&t=1873s) · b000036

**English**

XB depending on what the current data is, learn data dependent or data adaptive weights that are then used to for the fusion process. So this can be seen as a function where Z is your output feature instead of just having a fixed W1 times XA plus W2 times XB, you would have a function G of A that is trainable that takes in XA and XB which is your current data that outputs some weight which is used to multiply XA and likewise perhaps another fusion G of B, I'm sorry, another function G of B that outputs another weight that is used to to weight your XB. So G of A and G of B can be seen as learnable functions. You can think of them as attention functions or gating functions that in some data dependent way adjust the weights of the fusion for your modalities. Right? Uh

**中文**

XB，根据当前数据是什么，学习依赖数据（data dependent）或数据自适应（data adaptive）的权重，然后把这些权重用于融合过程。所以，这可以看作一个函数，其中 Z 是输出特征。你不再只有固定的 W1 乘以 XA 加 W2 乘以 XB，而是有一个可训练的 A 的函数 G，它接收 XA 和 XB，也就是当前数据，输出某个权重，用来乘以 XA；类似地，可能还有另一个 B 的融合 G，抱歉，另一个 B 的函数 G，输出另一个权重，用来给 XB 加权。因此，A 的 G 和 B 的 G 可以看作可学习的函数。你可以把它们看作注意力函数（attention functions）或门控函数（gating functions），以某种依赖数据的方式调整各个模态的融合权重。对吧？呃，

### [32:10](https://www.youtube.com/watch?v=0SOieOIe4HI&t=1930s) · b000037

**English**

Of course, if you if your gate doesn't depend on your data, then you recover the original scenario previously discussed where there's just one weight for the whole data set and you don't have this data dependent manner. So what what do these depend on? Well, nowadays it can be soft attention, it can be hard attention where the attention gates are soft or hard, zeros or ones. It can depend on the current modality, it can depend on the other modalities or depend on both modalities. So, various design decisions in again making these weighted gating functions more expressive and more data dependent.

**中文**

当然，如果你、如果你的门不依赖数据，那么就回到了前面讨论过的原始场景，即整个数据集只有一个权重，没有这种依赖数据的方式。那么，它们依赖什么呢？如今，它可以是软注意力（soft attention），也可以是硬注意力（hard attention），其中注意力门是软的或硬的，是零或一。它可以依赖当前模态，也可以依赖其他模态，或者依赖两个模态。所以，这里同样有各种设计选择，用于让这些加权门控函数具有更强的表达能力，更依赖于数据。

### [32:57](https://www.youtube.com/watch?v=0SOieOIe4HI&t=1977s) · b000038

**English**

Sometimes we don't want to learn these gating functions that treat all modalities equally. All right, sometimes we have this scenario where you have a primary modality. Nowadays, that's usually language because you have really powerful language models and you have lots of language data. So, you don't want to change these language representations too much because they're the most powerful. You just want to use other, for example, non-verbal or non-language modalities to shift the representations of language a little bit. All right, so we can call this shifting-based fusion. Uh it is very popular nowadays. Again, as I mentioned, when a or your primary modality is language and language models, you don't want to adjust those too much. Any other visual or auditory information can be used to shift the modality slightly. So, in this uh in this non-symmetric case. Uh so, one example we showed is that sometimes you have these ambiguous words like wow.

**中文**

有时候，我们不想学习这种平等对待所有模态的门控函数。好，有时候我们会遇到这样一种场景：你有一个主要模态（primary modality）。如今，它通常是语言，因为你有非常强大的语言模型，也有大量语言数据。所以，你不想过多改变这些语言表征，因为它们是最强大的。你只是想用其他模态，例如非言语或非语言模态，让语言表征稍微偏移一点。好，所以我们可以称它为基于偏移的融合（shifting-based fusion）。呃，它现在非常流行。正如我提到的，当一个，或者你的主要模态是语言和语言模型时，你不想对它们做太多调整。任何其他视觉或听觉信息都可以用来让这个模态稍微偏移一点。所以，在这个，呃，在这种非对称的情况下。呃，我们展示的一个例子是，有时候你会遇到像 wow 这样有歧义的词。

### [33:54](https://www.youtube.com/watch?v=0SOieOIe4HI&t=2034s) · b000039

**English**

Wow can be very good wow or very bad wow, right? So, the word itself is ambiguous but very informative. You can basically learn a shifting in this word vector space depending on whether the person was showing negative expressions or positive expressions when saying the word wow. So, that's another way of doing this this fusion. All right. I will cover the rest of fusion um on Thursday. I want to give a little bit of time for Edgar in the last 20 minutes or so to cover some um some tutorial and some information uh you need for for homework two. Right? If there's uh no other questions, if there's any other questions about some of these basic concepts of fusion, you'll see some of these, you know, implementations of early fusion, late fusion, tensor fusion, and a low-rank approximation of tensor fusion in your

**中文**

wow 可以是非常好的 wow，也可以是非常糟糕的 wow，对吧？所以，这个词本身有歧义，但信息量很大。你基本上可以根据这个人在说 wow 时表现出的是负面表情还是正面表情，在这个词向量空间（word vector space）中学习一个偏移。所以，这是做这种、这种融合的另一种方式。好。我会在周四介绍融合的其余部分，嗯。我想在最后大约 20 分钟里留一点时间给 Edgar，让他讲一些，嗯，一些教程和一些你们做作业二所需要的信息。对吧？如果没有其他问题，如果对于这些融合的基本概念还有其他问题，你们会看到其中一些，你知道，early fusion、late fusion、tensor fusion，以及 tensor fusion 的 low-rank approximation 的实现，就在你们的

### [34:50](https://www.youtube.com/watch?v=0SOieOIe4HI&t=2090s) · b000040

**English**

homework two, so I just wanted to be sure to to cover it uh today. All right? Any questions?

**中文**

作业二中，所以我只是想确保今天把它讲到。好吗？有什么问题吗？
