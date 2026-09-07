# Lecture 12 – Self-Evolving AI (MIT How to AI Almost Anything/Multimodal AI, Spring 2026)

_中文讲稿_

- Channel: Paul Liang
- Source: [YouTube](https://www.youtube.com/watch?v=FhcHTSjvuKk)
- Duration: 1:16:09
- Caption source: automatic
- Status: complete
- Chinese translation: 94/94
- Translation provider: codex
- Generated: 2026-09-07T08:06:39+00:00

## 讲稿

### [00:00](https://www.youtube.com/watch?v=FhcHTSjvuKk&t=0s) · b000001

好，&gt;&gt; 欢迎大家回来。学期快结束了。所以，有几件事要通知。呃，请填写课程评价，给我们反馈。这是我们第一次开这门课。嗯，所以一定要告诉我们今后几年可以怎样改进，而且更重要的是，你最喜欢这门课的哪些部分，这样我们就能保留下来。嗯，期中时已经向大家征求过一轮反馈，呃，所以你们可以把其中一些融入作业，也比如让某节课对特定概念讲得更详细一点。呃，第五次作业本周五截止。内容是大语言模型（LLM）和多模态智能体（multimodal agents）。有一些非常有趣的阅读材料，也会让大家亲手在这个 Discord 服务器中实现这些 agents。应该会很有意思。如果有任何问题，或者

### [00:56](https://www.youtube.com/watch?v=FhcHTSjvuKk&t=56s) · b000002

无法按时提交，请告诉我们。至于项目，如果还需要建议，尽量在本周二和周四课后来找我和助教（TAs）。嗯，我们已经对期中报告给过一轮反馈。大家都做得非常好。嗯，不过一定要完成最后的一些实验，并认真分析你们发现了什么，对吧？如果效果很好，恭喜。分析为什么效果好。如果效果不太好，也让我们试着弄清楚，嗯，哪里出了问题。评分不会取决于结果的好坏，而会取决于你们对结果分析的深度。当然，也包括方法的新颖性，以及整篇论文和报告写得怎么样。说明已经放到网上了。所以，如果需要任何反馈，一定要来找我们。请说。

### [01:48](https://www.youtube.com/watch?v=FhcHTSjvuKk&t=108s) · b000003

嗯，如果你还有延期天数，当然可以。展示安排在下周二，5月12日。嗯，说实话，我们还没决定是做海报还是课堂展示。海报的好处是更轻松。大家可以四处走动，和别人交流。通常我们走到你的海报前时，你只需要向我和一两位 TAs 介绍。缺点是打印海报需要几天。我不清楚这里具体怎么安排，不过如果周二需要海报，可能周末就得打印好，所以你们会少几天时间。嗯，另一种选择就是课堂展示。大家轮流上来，每个组上来，也许每组有五分钟展示。呃，你们要面对全班展示。互动性可能稍弱一点，不过，嗯，你可以一直改幻灯片，直到展示前10秒。

### [02:46](https://www.youtube.com/watch?v=FhcHTSjvuKk&t=166s) · b000004

大家有什么偏好吗？谁更喜欢 hoster \[字幕疑误，可能指 poster，海报\]？等一下，请继续举手。一、二、三、四、五、六、七、八。谁展示？呃，谁更喜欢课堂展示？一、二、三、四、五、六、六、七。哇。好。几乎一样多。为什么不在展示之前到这里？&gt;&gt; 为什么你提供展示和 periods \[字幕含糊\]？&gt;&gt; 因为这样你就有更多时间，在周二做出更好的成果，而周二很快就到了。&gt;&gt; 嗯哼。有没有支持做海报的理由？我看到这里有几支笔。&gt;&gt; 压力小一些。&gt;&gt; 好。

### [03:38](https://www.youtube.com/watch?v=FhcHTSjvuKk&t=218s) · b000005

你太 freaking 了&gt;&gt; 嗯，我，严格来说班上大概有50、60个人，嗯，从作业和提交情况来看，很多人不来上课，好，海报&gt;&gt; 我觉得这也会让你思考自己贴出来的内容，以及，你觉得呢？&gt;&gt; 我觉得下周做海报。

### [04:18](https://www.youtube.com/watch?v=FhcHTSjvuKk&t=258s) · b000006

&gt;&gt; 哇。我是说，我都可以。嗯，所以你们希望第五次作业晚点截止，然后做海报。好。好。关于最后一节课必须在什么时候，有没有规定？因为我们还在考虑具体安排，对吧？如果，嗯，我想大概有25个组，每组都讲五分钟，而这甚至已经是把所有内容讲完的最低限度了，对吧，那样会，会超过上课时间。嗯，另一种选择是，想做展示的人周二展示，想做海报的人周四做海报。一半同学在一次课上展示，另一半在另一次课上展示，也是一种可能。你有什么想法吗？你刚才举手了。

### [05:11](https://www.youtube.com/watch?v=FhcHTSjvuKk&t=311s) · b000007

登记，还有今天来上课的两名学生，呃，chat 作为所有五个要被取消。\[字幕含糊，可能在讨论取消第五次作业\] \[笑声\]&gt;&gt; 我想我们不能取消，不过也许可以延后几天。好。如果大家愿意，也许我们可以把第五次作业延后几天，然后我们可以做一个课堂，呃，我们可以在5月12日课堂上做海报展示，呃，形式会比较轻松，大家四处走走，嗯，每组介绍几分钟。&gt;&gt; 好。

### [05:51](https://www.youtube.com/watch?v=FhcHTSjvuKk&t=351s) · b000008

&gt;&gt; 对。嗯，我不确定能不能到下周末。我会想一个时间安排，不过&gt;&gt; 你会&gt;&gt; 我可以，我可以考虑延期。&gt;&gt; 还有其他要求吗？&gt;&gt; 嗯，如果我延后第五次作业，而大家有时间在这个周末前做好海报，那大概可以做海报展示。我想这样也更方便，大家可以四处走动、交流。&gt;&gt; 你对海报有什么建议，在&gt;&gt; MIT 有海报打印服务吗？有人知道吗？

### [06:27](https://www.youtube.com/watch?v=FhcHTSjvuKk&t=387s) · b000009

&gt;&gt; 我记得是35。&gt;&gt; 对，可以去 FedEx，大概35美元。需要多久？&gt;&gt; 大概不到24小时。&gt;&gt; 好。我是说，我们可以承担费用。嗯，如果你们能找到海报打印服务。嗯，不过好，我们会看看这些反馈，然后在明天之前在 pata \[字幕疑误，可能指 Piazza\] 上发通知。

### [07:06](https://www.youtube.com/watch?v=FhcHTSjvuKk&t=426s) · b000010

&gt;&gt; 也许我需要问问行政人员&gt;&gt; 好，好，我们继续，呃，我会收集这些反馈，然后通知第五次作业的截止日期，也会通知下周二的形式，对吧。不过至少到，也许到本周五左右，继续做项目，争取好的结果，然后我们会告诉你们应该做幻灯片还是海报。即使是幻灯片，也就是四到五页，我的海报也就是把同样的四到五页改成海报格式。很好。最终报告的截止日期是，嗯，下周二之后一周，给大家一些时间继续完善报告，并考虑我们在展示期间给出的反馈。好。所以，本周是，嗯，轻松讨论几个进阶主题。我会介绍几个，然后根据你们的兴趣，大家可以多提问，再深入讨论。

### [08:02](https://www.youtube.com/watch?v=FhcHTSjvuKk&t=482s) · b000011

否则，我们就继续下一个进阶主题。嗯，不过首先我来回顾一下课程内容，因为课程快结束了，要确保大家掌握关键内容，然后我们会讨论，嗯，我们已经讨论了不少主题，主要是如何适配这些大语言模型，也就是先预训练语言模型，再把其他模态（modalities）适配进去。但现在越来越多人关注直接训练原生多模态模型（natively multimodal models），不先从语言开始，而是从一开始就直接使用所有模态。混合专家（mixture of experts）也是这些原生多模态模型的重要组成部分。我们会介绍一些更进阶的融合（fusion）技术。我们主要讲过基于不同架构的 fusion 技术，但也有很多设计不同训练目标来改善 fusion 的方法。呃，然后我们会谈，我们谈过 agents、多模态 agents，但当时还把它们视为被编程来执行特定任务的 agents。不过，正如你们大多数人

### [08:58](https://www.youtube.com/watch?v=FhcHTSjvuKk&t=538s) · b000012

在如今的 AI 领域所看到的，有一种趋势是构建能够自动演化的 agents，它们不局限于被编程指定的任务集合，而是自动为自己提出更新、更难的任务，并随时间以指数级变得更强，超越你编程让它们做的事情。所以这是非常令人兴奋的机会，呃，当然，这类智能体模型（agentic models）也有很多风险。然后我们会发现，我们会讨论一些利用 AI 扩展人类感官的工作，从视觉、语言扩展到触觉、嗅觉和味觉等其他模态。最后，我们会讲，嗯，如何构建更擅长与人互动的 AI 模型，以及设计这些模型时应该遵循哪些原则，让它们真正为人们带来益处，而不是取代人们。

### [09:50](https://www.youtube.com/watch?v=FhcHTSjvuKk&t=590s) · b000013

好。所以用10分钟重点回顾一下，嗯，我认为课程中最重要的内容，对吧。我们一开始定义了什么是模态，并讨论了模态通常如何从传感器获得，原始模态更接近传感器，而 AI 的大部分工作就是获取原始数据，加工、抽象，并从原始数据学习表征（representations），将其转化为更抽象的模态。对吧？举过一些例子，比如原始语音是一种原始模态，图像也是一种原始模态，很难处理，维度很高，但随后可以开始提取语言、检测物体，也可以得到 past labels \[字幕含糊\]，对吧？情感和物体。我们看到，多模态是一项关键科学研究，有三个关键原则，对吧？它处理包含多种模态的问题，因此这些问题具有很强的异质性（heterogeneity）。不同模态

### [10:47](https://www.youtube.com/watch?v=FhcHTSjvuKk&t=647s) · b000014

彼此不同，这使处理它们变得困难，同时它们又体现出相互联系（interconnections）。Interconnections 可以分为关联信息（connected information），也就是相同信息在不同模态中有不同表现，以及交互信息（interacting information），即信息如何融合、组合，产生新信息。关于 heterogeneity，我们也讨论过，它可以看作从较相似到较不同的一个谱系。相似的例子包括来自两个不同相机的图像，再到两种不同语言的文本，一直到语言与视觉、语言与传感，对吧？模态越来越不同。我们提出了模态画像（modality profile）这个想法，切实分解每种模态的属性，并以此衡量哪些相似、哪些不同。对吧？看看基本元素是什么，

### [11:42](https://www.youtube.com/watch?v=FhcHTSjvuKk&t=702s) · b000015

基本的词、基本的物体区域，以及这些元素如何不同，元素分布如何不同，对吧？低频与高频也是 heterogeneity 的一个重要方面。结构，如果某种东西是空间性的。你们见过使用体现空间不变性（spatial invariance）的模型的例子，树状结构或，呃，线性链结构的数据。也有处理这些时间不变性（temporal invariances）的方法。信息，我们在整个课程中都见过用熵（entropy）和信息论（information theory）衡量信息。呃，噪声，噪声在不同模态中的表现有何不同，以及它们适合哪些任务。对吧？这些是将数据源分解为各项画像属性的方法，因此可以用它来衡量它们与其他模态的相似或不同程度。我们看到，关联（connections）主要是一种衡量共享信息的方式，这些信息

### [12:40](https://www.youtube.com/watch?v=FhcHTSjvuKk&t=760s) · b000016

相互关联，涉及两种模态，对吧？与之相对的是某一种模态独有、另一种模态不存在的信息。模态之间同样可以构成一个谱系，从非常强、有大量重叠信息，到较弱，甚至独立，对吧？举个例子，某些词与某些物体区域之间往往存在明确关系，这是一些一对一关联的例子，但同时也有多对多关联，比如 right 这个词，对吧，它指两个物体之间的关系，不能仅从一个物体检测出来。所以，connections，我们看到，它们主要通过对比学习（contrastive learning）之类的方法学习，也就是最大化正样本对之间的互信息（mutual information），对吧？词语和包含这些词语视觉

### [13:36](https://www.youtube.com/watch?v=FhcHTSjvuKk&t=816s) · b000017

表征的图像，以及词语、没有这些词语的其他图像。所以我们看到，contrastive learning 是捕捉 connected information 的一种方式。最后是交互（interactions）的概念，对吧？针对某个任务，我们从存在一定重叠的数据出发，看看不同信息区域如何对这些下游任务变得重要。我们看到，冗余（redundancy）是模态间共有信息的一个例子，比如积极的词语配上积极的表情。独有性（uniqueness）则是一个例子，说明如何选择该使用哪种模态，对吧？应该用 a，而不应该用 b。比如，你说积极的词语，配上中性表情，这时应该选择其中一种。我们讨论了很多基于动态注意力（dynamic attention）的 fusion 方法，对吧？有时关注一种，有时关注另一种。所有这些都是

### [14:33](https://www.youtube.com/watch?v=FhcHTSjvuKk&t=873s) · b000018

在试图解决识别哪一种模态包含正确独有信息的问题。最后，我们还看到了协同（synergy）。Synergy 是最酷的例子，只有当你开始把模态融合在一起时，信息才会出现。所以你可能表现出积极表情，但你表现出消极，你说积极的词语，却表现出消极表情，而这个人实际上是在讽刺，因为口头语言与非语言表情存在差异。

### [15:06](https://www.youtube.com/watch?v=FhcHTSjvuKk&t=906s) · b000019

所以，这是课程前几节课的一项关键收获，对吧？如何思考 heterogeneity。呃，根据一种模态的异质程度，应该为它设计什么架构？什么时候使用卷积网络（convolutional networks），什么时候使用 transformers，什么时候使用 graph neuronet networks \[字幕疑误，可能指 graph neural networks，图神经网络\]，等等。呃，我们看到了 connections，也看到 contrastive learning 如何连接模态并学习它们之间的共有信息。还有 interactions。我们看到了设计复杂 fusion 方法的不同方式，以更好地学习模态之间正确的 interactions。

### [15:46](https://www.youtube.com/watch?v=FhcHTSjvuKk&t=946s) · b000020

然后，我们用课程的大部分时间讨论多模态 AI 的核心技术挑战，对吧？从这些模态出发，要把它们组合起来，整合为表征和预测，需要解决哪些核心技术挑战？我们从整体上看到了六项挑战。第一项关键挑战是表征，如何通过 fusion 来表征这些模态。也就是把两种模态融合成一种表征；通过协调（coordination），将模态作为独立表征，但通过某种相似度函数协调它们；甚至还有 vision \[字幕疑误，可能指 fission，分解\]。如何考虑潜在因素（latent factors），从两种模态得到多种表征，每种处理不同部分的信息。然后我们讲了对齐（alignment），最简单的情况是，如果你有多个

### [16:41](https://www.youtube.com/watch?v=FhcHTSjvuKk&t=1001s) · b000021

元素，而且元素是离散的，因此容易分割，那么 alignment 就是匹配，对吧？将一个词与某个物体区域匹配，将一个词与说出这个词时的语音信号匹配。这一切都是匹配问题，目的是识别不同模态中包含相似信息的元素。呃，当元素不是离散的，而是连续的时，问题就更难了。这种情况下称为连续对齐（continuous alignment），你必须考虑元素之间的粒度和分割。

### [17:23](https://www.youtube.com/watch?v=FhcHTSjvuKk&t=1043s) · b000022

最后，前两类的目标只是发现 alignment、发现匹配，而我们还讨论了对齐表征（align representations）。也就是利用匹配，利用什么与什么对齐，来学习更好的表征。这是如今大多数 transformer 架构的基础：输入词语，根据它应该与哪些相似词语对齐来进行上下文化（contextualizing），对吧？这就是注意力（attention），再利用这些 alignment 值加权，获得更好的表征。所以这就引出了 transformers，以及多模态 transformers，你可以通过图像中不同的视觉区域，开始对词语进行 contextualizing。然后我们开始讨论基于这些上下文化表征的多模态 transformers，以及对它们进行预训练（pre-training）、微调（fine-tuning）、指令微调（instruction tuning）的各种方式。

### [18:18](https://www.youtube.com/watch?v=FhcHTSjvuKk&t=1098s) · b000023

嗯，然后我们开始讨论推理（reasoning），对吧？Reasoning 指的是不只是做单次预测的方法，对吧？因为这些问题远比预测一个分类标签之类的单次预测难，而是要求模型把问题分解成多个推断步骤，对每一步推理，得到答案，提出所有这些步骤，以形成，嗯，更高阶的推断。所以这称为 reasoning。我们开始讨论如何训练模型进行 reasoning，对吧？过去，reasoning 是由多层 neuronet networks \[字幕疑误，可能指 neural networks，神经网络\] 完成的，每一层的信息都比前一层更抽象。呃，但如今有了语言模型和 neurosyolic AI \[字幕疑误，可能指 neuro-symbolic AI，神经符号 AI\]，我们有了以可解读、可解释的方式进行 reasoning 的新机会，对吧？呃，这就需要，比如考察

### [19:16](https://www.youtube.com/watch?v=FhcHTSjvuKk&t=1156s) · b000024

reasoning 中的中间表征是什么，对吧？利用注意力图（attention maps）推理，以语言为媒介推理，一步一步分解问题，嗯，考察 reasoning 的结构，对吧？我们做了很多线性链式推理，A 然后 B 然后 C，就像你的思绪链一样。但现实世界中的许多情境需要树状推理（tree structured reasoning），搜索不同可能性，其中很多会在不同时间点沿不同路径分叉。最后，reasoning 往往来自外部知识，对吧？它可以是人类推理的形式，然后用模型进行监督微调（SFT）。也可以是很好的奖励函数（reward functions）和验证器（verifiers），再使用强化学习（reinforcement learning）激励 reasoning。对吧？所以我们用了几节课讨论如何利用 reinforcement learning 在 LLM 和多模态 LLMs 中实现 reasoning。

### [20:13](https://www.youtube.com/watch?v=FhcHTSjvuKk&t=1213s) · b000025

这就是 reasoning，然后我们讨论了生成（generation），对吧？Generation 这项挑战是希望使用 AI 模型生成高质量、具有照片真实感的真实数据，一些例子包括总结、翻译，比如文本到图像的转换，甚至创作，对吧？从一帧开始，生成整段视频。我们讲了一些核心概念，使用若干方法，比如使用 varational autoenccoders \[字幕疑误，可能指 variational autoencoders，变分自编码器\] 生成数据，然后开始讨论用扩散模型（diffusion models）生成数据，以及用流匹配（flow matching）生成数据。这些都属于 generation，如今几乎所有这些模型本质上都是多模态的，采用文本条件（text conditioning）或潜变量条件（latent variable conditioning），模型能够生成并遵循

### [21:11](https://www.youtube.com/watch?v=FhcHTSjvuKk&t=1271s) · b000026

指令，生成相当逼真的图像。对吧？所以这一部分我们讨论了 VAE、diffusion models 和 flow matching 模型。第五项挑战，我们没有深入讲，只用了一节课讲跨模态迁移（crossmodal transfer）。不过如果你还记得，这种设定在现实世界中非常实用，对吧？很多情境下，你关心在某种模态上做预测，无论是医疗、金融、建筑，还是其他领域。你经常面临数据不多的问题，对吧？而另一种模态的数据可能更多，比如在线教材、预训练语言模型、自然图像，它们的分布与你真正关心的分布略有不同。所以 crossodal transfer \[字幕疑误，可能指 crossmodal transfer\] 就是利用这些其他外部数据源，学习更强大的

### [22:08](https://www.youtube.com/watch?v=FhcHTSjvuKk&t=1328s) · b000027

表征，丰富你关心的模态，从而做得更好。我们看到了几种方法，嗯，迁移学习（transfer learning）、多任务学习（multitask learning），以及用不同预测头（prediction heads）训练同一个基础模型，是实现这一点的通用方法。还有共同学习（co-learning）的想法，在训练时引入额外模态，对吧？然后可能开始融合或对齐这些表征；或者把额外模态作为预测目标引入，对吧？比如用语言预测视觉。这能让你获得同时包含语言和视觉信息、更丰富的表征。同时，因为它是预测目标，训练后可以丢弃，只留下一个由视觉增强的语言骨干网络（language backbone）。我们称之为 co-learning，讨论过几种实现方式。最后是模型归纳（model induction），对吧？这些是

### [23:06](https://www.youtube.com/watch?v=FhcHTSjvuKk&t=1386s) · b000028

你可能不想更新模型的情境，但如果有 APIs，仍然可以使用 APIs，在输出层交换信息，对吧？我们讨论了一种 co-raining \[字幕疑误，可能指 co-training，协同训练\] 算法，大致是用一个分类器为将输入另一个分类器的数据打标签。因此只需要黑盒访问（blackbox access），不需要修改表征本身。这就是迁移（transference），或者 crossodal transfer \[字幕疑误，可能指 crossmodal transfer\]。最后，第六项挑战本身其实并不是技术挑战。它不提出新方法或新算法，而是叫量化（quantification）。对吧？呃，就是对不同多模态现象、不同模型训练方式开展更深入的实证和理论研究。在这个很大程度上依赖实证的领域，这显然非常欠缺，而且要把它看作多模态的科学

### [24:02](https://www.youtube.com/watch?v=FhcHTSjvuKk&t=1442s) · b000029

嗯，我们也在各节课中讨论和穿插了这些内容。我们讨论了衡量 heterogeneity 的方法，以及它如何影响你要开发的方法。呃，我们讨论了一些衡量模态不同交互方式的方法，并利用这些方法设计不同的 fusion 方法，今天还会讲一点。如我所说，并非一切都关乎架构，模型如何优化也带来了很多挑战和机会，对吧？优化大型、大型多模态模型并不容易。好，这是六项核心挑战的总结。在这个布局中，表征和 alignment 几乎总是需要的，其后是 reasoning，对吧？如果问题足够复杂，需要系统地、逐步解决。呃，否则就是 generation 和 transference，

### [24:58](https://www.youtube.com/watch?v=FhcHTSjvuKk&t=1498s) · b000030

用来生成更多数据或迁移信息，而 quantification 就是放大镜，目的是深入理解我们开发的方法。那么，在继续之前，大家对核心内容的回顾有什么问题吗？

### [25:23](https://www.youtube.com/watch?v=FhcHTSjvuKk&t=1523s) · b000031

我希望大家也觉得其他老师的课很有帮助。Dimmitri 讲了很多如何把 fusion 方法应用到真实医疗数据中的方式，也介绍了预测性推理（predictive reasoning）和处方性推理（prescriptive reasoning）的一些方法，推理如何优化不同结果。然后，呃，Sanuk 和 Zinhua，希望大多数人都去听了，他们确实讨论了一些多模态方法如何用于制造业和交通，对吧？但从核心来看，许多 fusion 和 alignment 方法都可以用，reasoning 方法也是，比如 agents 如何用于制造业。很好。所以，呃，我们来深入一些进阶主题。如我所说，会挑一些来讲。我有很多幻灯片。如果特别感兴趣，随时打断我，

### [26:19](https://www.youtube.com/watch?v=FhcHTSjvuKk&t=1579s) · b000032

或者，如果希望我更快进入下一个进阶主题，也可以翻个白眼。嗯，不过有一个主题相当有趣，而且我个人觉得这些模型就应该这样训练，叫原生多模态模型（native multimodal models）。对吧？呃，你们可能见过 Llama，Llama 4。这是去年的，不过 Meta 有新一代模型，也声称它们是原生多模态的。嗯，如果你看过很多初创公司，很多来自 Yan Lun、来自 Feay 的 role model 初创公司 \[字幕疑误，role model 可能指 world model，世界模型\]，它们都声称有原生多模态理解能力。那么这是什么意思？呃，最大的区别在于，看看如今的前沿实验室，大多数仍然先训练语言模型，然后把多模态拼接上去，对吧？它们把视觉编码器（visual encoder）加入这些冻结语言模型的表征中。这样就能获得视觉

### [27:15](https://www.youtube.com/watch?v=FhcHTSjvuKk&t=1635s) · b000033

理解能力，然后在模型输出上拼接 diffusion model 的输出，从而实现图像生成，就像你们的 OpenAI 模型中的那些功能。所以可以把这理解为先训练语言模型，其他东西都事后再考虑。呃，因此，当模型接收的视觉输入，或者你希望模型生成的视觉输出，可以用自然语言表达时，它的效果非常好。对吧？我感觉，它们可能会先为这些图像生成非常详细的语言描述，再送入纯语言模型；当希望模型输出某张图像时，也会生成非常详细的图像提示词（image prompt），以不同方式扩展，也许使用 agents，然后这些文本进入图像生成模型。因此，native multimodal models 试图走另一条路，不先训练语言模型，而是，你

### [28:10](https://www.youtube.com/watch?v=FhcHTSjvuKk&t=1690s) · b000034

可以先训练视觉模型，对吧？实际上通过视频下一帧预测（video next frame prediction）训练一切，用于视觉和物理理解；或者联合训练，对吧？视觉语言联合理解。嗯，常见的动机是，人类就是这样学习的，婴儿在开始说话前就是这样学习的，动物，动物以及不使用人类这种语言的物种，就是这样学习在世界中移动、交流、互动、生存和演化的。对此有几种方法。所以这些是来自 meta 的一些，嗯。如果我画一个示意图，对吧？这些非原生模型里，你有 LLN \[字幕疑误，可能指 LLM\]，有文本，你训练一个图像编码器（image encoder），然后像我们见过的那样经过一个线性适配器（linear adapter），进入语言模型的 token 输入空间，对吧？蓝色表示，蓝色

### [29:06](https://www.youtube.com/watch?v=FhcHTSjvuKk&t=1746s) · b000035

表示语言模型被冻结，橙色表示这些部分会训练。所以这些是非原生 ELMs \[字幕疑误，可能指 LLMs\]。目前大多数都使用这种结构。嗯，当然，原生模型则是，不冻结 LLM，而可以把 LLMs 标成橙色。也就是可以训练、微调，甚至从头训练，对吧？从头直接使用语言和视觉输入训练。所以让它们从头用多模态输入训练。也有不同做法。呃，后期融合（late fusion）方法仍然是用一个 image encoder，经过线性映射（linear mapping），提取出很好的图像特征后，再进行 fusion。嗯，也有采用早期融合（early fusion）的方法。图像块（image patches）不先经过 image encoder，而是直接以原始像素空间，或经过 linear mapping，进入

### [30:03](https://www.youtube.com/watch?v=FhcHTSjvuKk&t=1803s) · b000036

语言模型，对吧？这更接近 early fusion，对吧？不是经过视觉处理再做 late fusion，而是几乎直接把原始图像数据输入这些 LLMs。不过到了这一步，它大概已经不该被叫作 LLM 了。它是一个确实同时接收原始文本数据和原始图像数据的模型。所以 early fusion 看起来就是这样。嗯，对，我是说，到底哪种方法最好还没有定论。人们认为，我们已经用尽了大量文本数据，而把其他模态适配到文本中的这种方法，在很容易用文字描述的领域表现很好。但在其他领域，显然我们可能正遇到一些瓶颈，因此很多投资都在转向直接开展多模态训练的方法。

### [31:01](https://www.youtube.com/watch?v=FhcHTSjvuKk&t=1861s) · b000037

所以我很喜欢这篇论文，叫 scaling laws for native multimodal models。我想稍微讨论一下。嗯，不过先介绍一下缩放定律（scaling laws）的背景。Scaling laws 是针对当今基础模型（foundation models）开展科学研究的一个很好的例子，对吧？它们本质上是给出一种规律，一种幂律（power law）关系，告诉你，当我获得更多数据、增加模型参数规模，或者延长模型训练时间时，能否估计损失（loss）会以多快或多慢的速度下降。这显然非常重要，因为如果你能预测，再收集10 TB 数据、再多训练两个月，或者把模型从一万亿参数扩大到10万亿参数，loss 会下降多少，如果能估计

### [31:59](https://www.youtube.com/watch?v=FhcHTSjvuKk&t=1919s) · b000038

loss 会下降多少，就能在算力约束下做出更好的决策，因为显然不可能把所有情况都试一遍，再看 loss 到哪里。因此，这是科学理解这些模型如何工作的一个很好的例子，对吧？一些早期 scaling law 模型，做法遵循业界提出的 chinchilla scaling law：训练规模越来越大的模型，使用越来越多的数据，训练越来越长的时间，对吧？然后通过实验画出训练曲线如何下降。有时进入平台期，有时下降更多，有时又下降得更多。凭借这些，它们实际上能够写出一个方程，根据数据点数量、参数数量或训练时长，估计 loss 会是多少，对吧？所以它们喜欢展示这些图。这里的参数非常少，

### [32:53](https://www.youtube.com/watch?v=FhcHTSjvuKk&t=1973s) · b000039

如你所见，参数很少。嗯，x 轴是训练时长，Y 轴是 loss。所以越低越好，下面这里，越低越好。这些颜色表示不同模型族，下面较深的颜色表示参数较少，上面较浅的黄色表示参数较多。先看一些深色模型，初始验证损失（validation loss）是6，然后可以训练更久。最后会到大概4.5，对吧？然后进入平台期，接着增加参数数量。呃，首先注意，loss 会升高，对吧？模型越大，初始 loss 越高，因为随机参数更多。但随着训练时间延长，validation loss 会降到4，然后3.5，再到3，对吧？你训练的最大模型有10的11次方个参数，初始 loss 特别高，我也不知道，可能10或20，

### [33:49](https://www.youtube.com/watch?v=FhcHTSjvuKk&t=2029s) · b000040

然后训练更久，最后降到这里黄色的1.75，对吧？所以如果看这些平台的包络线（envelope），就能得到这种直线关系，它告诉你，首先，训练更久有帮助，但只有模型足够大，训练更久才有帮助，对吧？最终就能降到这个 loss。然后可以开始插值（interpolating），对于其他模型，如果你决定，也许我要这么多参数的模型，并且有足够算力训练这么久，那么 validation loss 会是多少。好。这是一些背景，嗯，写成方程大概是这样。Loss 是模型参数和数据集的函数。嗯，这个例子没有包含训练时间。嗯，不过它等于

### [34:45](https://www.youtube.com/watch?v=FhcHTSjvuKk&t=2085s) · b000041

首先有一个下限，对吧？E 是最小 loss，就像一个底线，loss 永远不会低于它，对吧？嗯，然后有两个因素，a 和 b，它们是要估计的参数。a 除以 n，因此取决于模型参数数量。那里的 n，当然，模型参数越多，a 除以 n 就越小，对吧？所以 n 是一个重要参数。D 是数据集大小，同样是 B 除以 D。所以 D，也就是数据集大小，越大，B 除以 D 最终越低，对吧？因此 loss 等于最小 loss，加上随参数数量下降的部分，再加上随数据集大小下降的部分，对吧？嗯，然后，不，你要估计的参数，N 和 D 是给定的，对吧？你知道模型参数有多少，知道有多少数据点，也知道

### [35:43](https://www.youtube.com/watch?v=FhcHTSjvuKk&t=2143s) · b000042

loss 是多少。你只是用线性回归（linear regression）计算 E、A 和 B，对吧？人们就是这样得到 scaling loss \[字幕疑误，可能指 scaling laws\] 的。获取一堆 N、D、loss 以及 D、loss 的不同配置组合，再用 linear regression 估计 E、A 和 B。这是单模态缩放（unimodal scaling），而这篇论文提出对 E scaling loss \[字幕疑误，可能指这些 scaling laws\] 进行修改，来研究多模态缩放（multimodal scaling）。对吧？现在还是有 loss，有模型大小 n，也就是多模态模型的参数数量，还有 di 和 dj，分别是两种模态的数据集大小，数据集 I 对应第一种模态，数据集 j 对应第二种模态，它们可以相同，也可以不同。好，这个方程是什么样的？

### [36:37](https://www.youtube.com/watch?v=FhcHTSjvuKk&t=2197s) · b000043

首先，它归结为第一种模态与第二种模态的平均 loss。你可以把它理解为两种模态独立建模、彼此没有任何交互时的平均 loss。然后减去 C，也就是最大的 synergy 程度，对吧？模态之间 synergy 越强，减去的量越大，loss 下降得越多，这两种模态体现出的 synergy 有一个最大值。接着又有 a 除以 n 这一项，所以它随着模型参数数量增加而下降，取决于模型参数数量，也就是模型大小。最后，这一项表示优化过程中的竞争（competition）。这个参数取决于两个数据集大小的总和

### [37:33](https://www.youtube.com/watch?v=FhcHTSjvuKk&t=2253s) · b000044

，对吧？如果数据集太小，模态之间可能会有更多 competition，这会损害优化。这是他们发现的。但随着两种模态的数据集大小增加，这一项最终会越来越低，对吧？所以这是利用 synergy 等多模态概念的一个好例子。它告诉你，synergy 是积极因素，对吧？Synergy 是积极因素，告诉你 synergy 越多，loss 会下降多少；还有 competition，对吧？它是不利因素，因此你需要更多数据点来消除 competition，这样 loss 就会下降。对这些 scaling loss \[字幕疑误，可能指 scaling laws\] 有什么问题吗？

### [38:31](https://www.youtube.com/watch?v=FhcHTSjvuKk&t=2311s) · b000045

对。如我所说，嗯，你首先会，我们先看简单情况。好。在这种情况下，你会训练不同大小、不同 ends \[字幕疑误，可能指 N\] 的模型，使用不同的数据集 these \[字幕疑误，可能指 Ds\]，得到不同的 loss，也就是 L。对吧？做得足够多，就得到一个由 L 和 D 对、三元组组成的数据集，对吧？然后拟合 linear regression，得到系数 E、A 和 B，对吧？它相对于1除以 N 和1除以 D 是线性函数，对吧？这里也一样，你会训练不同大小 N 的模型，使用不同规模的多模态数据集对，也就是 RDJC \[字幕疑误，可能涉及 Di、Dj\]。

### [39:12](https://www.youtube.com/watch?v=FhcHTSjvuKk&t=2352s) · b000046

那么问题就是，如果你有一个足够大的数据集，包含模型大小、数据集大小和 loss，是否可以拟合任意函数？为什么一定要用这种形式，对吧？技术上可以拟合任意函数。呃，不过人们发现，首先，这些 power law 关系相当自然，对吧？1除以某个量是很自然的，然后可以尝试不同配置，比如不用1除以 n，试试1除以 login \[字幕疑误，可能指 log n\]，然后基本上可以看拟合误差（fit error）和留出误差（held out error），对吧？也就是在新的模型大小或数据集大小上的 held out error。然后我想，他们发现，相比 N、D 和 loss 之间的其他关系，这些设定效果最好。请说&gt;&gt; 所以

### [40:07](https://www.youtube.com/watch?v=FhcHTSjvuKk&t=2407s) · b000047

就是这些，这个，因为确实有那个数据集，你没有，然后这有点像另一个，或者也许&gt;&gt; 哦，对，是的，基础模型是某个 transformer，对吧？你在很多数据集或 multimodel 数据集 \[字幕疑误，可能指 multimodal datasets\] 上训练 transformer，训练到收敛后，你 point loss \[字幕含糊，可能指得到 loss\]，对吧？但一旦有了 n、d 和 loss，就可以把它们放进 linear regression 求解器或电子表格，对吧？这样就得到 e、a 和 b。如果这些系数的计算随后会更新 transformer，那就是 metal learning \[字幕疑误，可能指 meta-learning，元学习\]，对吧？但在这里，你只是把 transformer 训练到收敛，得到了 loss，你

### [41:04](https://www.youtube.com/watch?v=FhcHTSjvuKk&t=2464s) · b000048

基本上只是在计算统计量，对吧？做线性、线性模型。嗯，很好。好。嗯，所以他们发现了很多很酷的东西。交代一下背景，这是某种 early fusion transformer。你有一个大型 transformer，我记得他们针对文本和语音做了实验。你有一段文本，然后是语音、音频，再有更多文本、更多音频。呃，所以 DI 和 DJ 的大小不同是合理的，对吧？它不是那种要求两种模态各有相同数据量的 fusion 模型。嗯，那么他们发现了什么？他们发现，early fusion 模型在小规模下有一点优势。在更大规模下，两种架构表现相近，以至于你

### [42:00](https://www.youtube.com/watch?v=FhcHTSjvuKk&t=2520s) · b000049

甚至可以采用 late fusion 或 early fusion。呃，有时甚至不需要 image encoders，scaling law 仍然成立。呃，因此，native multimodal models 的缩放方式与单模态 LLMs 相似，只是缩放指数（scaling exponents）略有不同，取决于数据有多少，或者模态之间有多少 synergy。他们还发现，嗯，哦，他们还比较了 native multimodal models 中的稠密模型（dense models）、稠密 transformer 模型，与 mixture of expert transformer 模型，实际上发现 mixture of expert transformer 模型的缩放表现好得多。所以，对，其中一些越来越多地采用 mixture of expert 模型，因此呈现出低得多的 loss。

### [42:55](https://www.youtube.com/watch?v=FhcHTSjvuKk&t=2575s) · b000050

哦，他们还发现，模态感知专家（modality aware experts），也就是为不同模态设置不同专家，表现实际上比模态无关设计（modality agnostic design）更差。所以至少在这种设定下，最好让专家由图像和文本 tokens 共享。因此，这是关于如何设计 mixture expert 模型的几个有趣发现。呃，稍微介绍一点背景，我想可能有人不知道，如今大多数这类模型都高度过参数化（over parameterized），可以包含数万亿参数，但当你输入 prompt 或模型进行推理（inference）时，并不是所有参数都会激活。你有这种 mixture of experts 机制，这些专家可以看作 transformer 模块（transformer blocks）、注意力头（attention heads），其中很多同时训练，而 inference 时有一个路由器（router），基本上会把你的查询、键和值（query、keys、values）路由到其中一个

### [43:52](https://www.youtube.com/watch?v=FhcHTSjvuKk&t=2632s) · b000051

专家，或者一小部分专家，对吧？嗯，实际中，每个 query 只会激活约10%的专家，这让你仍然能训练极大的模型，理论上信息存在于某个专家中，但 inference for seed \[字幕含糊\]，只会激活其中一个子集。比如 deepseat 模型 \[字幕疑误，可能指 DeepSeek\]，有6000亿参数，每次 inference pass 只激活370亿参数。

### [44:27](https://www.youtube.com/watch?v=FhcHTSjvuKk&t=2667s) · b000052

我们也做了一些很酷的工作，有些人在使用这些多模态交互专家（multimodal interaction experts）。我们开始量化：给定一个包含两种模态的数据点，它是冗余的，还是更独有，还是更具 synergy？正如我们在 fusion 讨论中看到的，不同类型的 interactions 往往需要不同的 fusion 方法，对吧？信息，使用 contrastive learning 很合理，因为这是共享信息，所以 contrastive learning 能捕捉这种 mutual information。对于独有信息，使用动态 attention 权重很合理。有时给一种模态权重1，另一种0；有时给另一种1，第一种0。这样就捕捉了独有信息，而 synergy 则有助于学习更复杂的 interactions，对吧？所以你们看到了这些不同类型的 fusion

### [45:23](https://www.youtube.com/watch?v=FhcHTSjvuKk&t=2723s) · b000053

方法。于是我们开发了这种方法，可以把不同数据点路由到不同的专家头（expert heads），然后在预测时组合起来。它适用于原生模型，也适用于基于 adapter 的模型，适用于各种模型。这里有个例子，你用一个有很多 synergy 的讽刺任务，如果只用单个模型，比如 clip 或 blip 模型，抱歉，这些是视频 LLMs，它们在 redundancy 和 uniqueness 上表现很好，但在 synergy 上很差，几乎相当于随机猜测。如果开始训练这些专家模型，redundancy 和 uniqueness 会稍微改善，但 synergy 会好很多，专门为具有 synergy 的数据点设置 expert head，效果会好很多，对吧？我们也展示了它在其他设定下更好，比如有

### [46:20](https://www.youtube.com/watch?v=FhcHTSjvuKk&t=2780s) · b000054

比喻性语言、卡通、幽默，而模态之间没有非常明显的重叠。

### [46:33](https://www.youtube.com/watch?v=FhcHTSjvuKk&t=2793s) · b000055

好。有什么，请说。

### [46:49](https://www.youtube.com/watch?v=FhcHTSjvuKk&t=2809s) · b000056

你如何根据你的例子给某种东西打标签，总是有点像取一个

### [47:09](https://www.youtube.com/watch?v=FhcHTSjvuKk&t=2829s) · b000057

对。嗯，这是个难问题。我们一直在做一系列工作，呃，针对给定的数据点，对吧？在讽刺中，有时人们的脸看起来非常愤怒，却说着非常积极的话，就像讽刺、synergy。也有一些情境，只看语言就能检测出 synergy，检测出讽刺。那就不是 synergy，而只是语言信息。不过总体来说，我们做了很多工作，研究如果有多模态数据，如何用 information theory 量化哪些数据点是独有的、哪些是冗余的、哪些具有 synergy。从宏观上看，可以把 redundancy 理解为彼此 show information \[字幕疑误，可能指 share information，共享信息\] 的数据点，也有构建逐点互信息（pointwise mutual information）的方法，因为你想了解的不是整个数据集，而是每个点的重叠信息，mutual information 是一种办法。嗯，进一步

### [48:06](https://www.youtube.com/watch?v=FhcHTSjvuKk&t=2886s) · b000058

推广，独有信息可以看作类似条件熵（conditional entropy）的东西，对吧？然后 synergy 就非常棘手，因为如果只用 mutual information 和 conditional entropy，你无法得到 synergy，对吧？在 information theory 中，你永远无法估计两种模态产生的、原本不存在于那两个随机变量中的信息。嗯，所以人们，其实周四会多讲一些。它会更数学化一点，不过 information theory 有个子领域叫信息分解（information decomposition），研究的问题是：如何把总信息分解为 redundancy、unique、synergistic 这些部分，其中 synergy 可以看作总信息减去，嗯，单模态信息的这种最差组合。但长话短说，有一些方法可以

### [49:03](https://www.youtube.com/watch?v=FhcHTSjvuKk&t=2943s) · b000059

利用统计学和 major theory \[字幕疑误，可能指 measure theory，测度论\] 衡量这些。嗯，我们做了一些形式化工作，然后在这个例子中，为了实现规模扩展，做了一些近似。&gt;&gt; 对？所以基本上你会给训练数据打标签，然后针对每个 height \[字幕疑误，可能指 type，类型\]，训练一个专门处理这种交互的模型。&gt;&gt; 对。所以，比如有20%的 redundancy，你就取那20%的数据，微调一个单独的 edge \[字幕疑误，可能指 head，头\]，对吧？或者在训练时路由到那个单独的专家。这一类占50%的数据，那么这些数据点就会被路由到那个 head，依此类推。所以模型的不同部分会根据它们被路由到的信息而激活。&gt;&gt; 对，所以通常这种模型是不是用同一个 backbone，然后你微调

### [49:59](https://www.youtube.com/watch?v=FhcHTSjvuKk&t=2999s) · b000060

某种交互类型，或者你会真的取一个 project \[字幕含糊\]？&gt;&gt; 在这个例子中，用的都是同样的 transformer 架构模型。不过我们确实分配了更多层。我们发现，给 synerg layers \[字幕疑误，可能指 synergy 相关层\] 分配更多层更有用。但我觉得这是可行的，而且有人单独尝试过，让真正不同的模型被激活。&gt;&gt; 对。&gt;&gt; 所以，比如你可以考虑，为 redundancy 学习一个 contrasted representation \[字幕疑误，可能指 contrastive representation，对比表征\]，并且只在 redundancy 情况下激活这个表征，而这一种可以使用更多 transformer fusion 层。因此可以是不同模型。在这个例子中，架构相同，

### [50:55](https://www.youtube.com/watch?v=FhcHTSjvuKk&t=3055s) · b000061

但为不同 heads 配置了不同的专用参数。

### [51:08](https://www.youtube.com/watch?v=FhcHTSjvuKk&t=3068s) · b000062

好，还有其他问题吗？好。呃，我也想重点介绍一些优化（optimization）方面的工作。嗯，有时你会觉得增加模态总会有帮助，但事实并非如此，对吧？有时，实际上在很多情况下，增加模态会损害效果。这是一个视频分类的例子，基于 RGB、音频特征和光流（optical flow），画面中都是进行不同体育活动的人，对吧？你可能觉得，他们活动的声音会有帮助，而 of 是 optical flow，它是一种视觉模态，比标准 RGB 更能跟踪人的运动。但开始融合后，情况反而变差。还有更多这样的例子。呃，有时你训练模型，你以为你

### [52:06](https://www.youtube.com/watch?v=FhcHTSjvuKk&t=3126s) · b000063

训练了一个会看图并回答图像相关问题的模型。比如，香蕉是什么颜色，或者有多少人，但模型其实并没有这样做，对吧？这里有个很有意思的例子，给模型一根黄色香蕉，问是什么颜色，它答对了，黄色。然后把香蕉换成绿色的，再问是什么颜色，它仍然回答黄色。仅仅因为模型见过的香蕉几乎都是黄色的。所以有很多这样的例子。嗯，图里有多少人？大多数模型回答两个，因为这些数据集被 cured \[字幕疑误，可能指 curated，整理构建\] 时，问有多少人，最常见的答案是两个。这也会导致其他问题。嗯，模型被发现会，比如这里，它们试图给这张图生成描述，只说一个男人坐在桌旁，桌上有一台笔记本电脑，而“男人”是不对的。看模型的热力图（heat map），它只看了

### [53:02](https://www.youtube.com/watch?v=FhcHTSjvuKk&t=3182s) · b000064

电脑。红色 heat map，它自动推断了这个人的身份，却完全没有对这个人施加 attention。这是这些模型存在性别偏差（gender bias）的一个例子。所以基本上，这些模型其实，有时你以为它们很好地结合了信息，有时你以为它们会看所有模态，但有时并不会，而且开始 fusion 后，表现可能更差。怎么解决这些问题？一种方法是确保数据集大体平衡。第一版 VQA 数据集发布后，出现了很多数据集，以及平衡版 VQA。对于每个问题，都有一张图对应一种答案，另一张图对应另一种答案。比如，雨伞是不是倒着的？会有“是”的例子，也有“不是”的例子，对吧？这是个很好的例子，因为如果问题是

### [54:00](https://www.youtube.com/watch?v=FhcHTSjvuKk&t=3240s) · b000065

雨伞是不是倒着的，除非它真的倒着，否则没人会问这个问题，对吧？所以模型也发现了这些捷径（shortcuts）。当你开始用另一种情况平衡它，训练就会更平衡。呃，所以可以平衡模态、平衡数据，也可以平衡训练。这涉及开发真正同时关注两者的模型。一种方式是改进这些模型的 optimization，对吧？呃，这些模型通常很难优化，而它们走捷径、只看问题不看图像的原因，还是 heterogeneity，对吧？这些模型是很强大的语言模型，非常擅长处理文本，要让它们看图像并与文本结合，就需要很大的努力。所以如果

### [54:55](https://www.youtube.com/watch?v=FhcHTSjvuKk&t=3295s) · b000066

模型找不到降低 loss 的捷径，呃，它会找到降低 loss 的捷径。不同模态过拟合（overfit）和泛化（generalize）的速度也不同，对吧？当模型已经学好语言，语言的困惑度（perplexity）很低时，图像上的 loss 可能仍然很高，于是它开始忽略图像。如何解决这类问题？人们提出了各种优化目标，改善训练以达到平衡。这里一个关键想法是计算过拟合与泛化比（overfitting to generalization ratio），对吧？这意味着，在两种模态上训练多模态模型时，也保留单模态模型，对吧？只在 XA 上训练，loss 曲线是什么样，类似你的 loss 曲线或 scaling law。现在也可以这样做。如果只单独训练 XB，它的

### [55:51](https://www.youtube.com/watch?v=FhcHTSjvuKk&t=3351s) · b000067

loss 曲线和 scaling law 会是什么样？然后看同时用 A 和 B 训练多模态模型的情况，对吧？跟踪多模态模型中每种模态的 loss 曲线。好，然后可以比较某个 epoch 中，多模态情况下 a 的 loss，与只进行单模态训练时 a 在同一个 epoch 的 loss，对吧？这样就得到某个差值。你会发现，有时模态学习得比单模态情况下快，有时比单模态情况下慢，对吧？一旦发现这一点，就可以重新平衡训练。比如可以增加 loss 项，或者不必每个 epoch 都更新，而是延迟模型更新，使多模态训练尽可能接近单模态训练。

### [56:48](https://www.youtube.com/watch?v=FhcHTSjvuKk&t=3408s) · b000068

这里有一些想法。我是说，显然我不是特别喜欢这个方法，因为你不只是训练一个模型，而是要训练三个，所以可扩展性不太好。呃，不过有很多后续工作，通常都沿着类似思路展开。核心是如何平衡训练，可以调整梯度（gradients），或者调整调度（scheduling）或学习率（learning rates）。但关键想法就是平衡训练，让模型不会在一种模态上 overfit，然后忽略其他模态。

### [57:23](https://www.youtube.com/watch?v=FhcHTSjvuKk&t=3443s) · b000069

好。大家对这些其他 fusion 方法有什么问题吗？Mixture of experts、改进 optimization。谁在做项目或作业时觉得这是个挑战？你开始做，收集多模态数据，一切都很开心，然后训练单模态模型，却发现多模态模型没有更好。谁遇到过这个问题？不少人。你们怎么解决的，还是说问题仍然存在？哇，你们两个。

### [58:00](https://www.youtube.com/watch?v=FhcHTSjvuKk&t=3480s) · b000070

有没有人遇到这个问题，后来解决了，或者什么改善了训练？

### [58:11](https://www.youtube.com/watch?v=FhcHTSjvuKk&t=3491s) · b000071

&gt;&gt; 差了多少？你觉得问题是什么？

### [58:19](https://www.youtube.com/watch?v=FhcHTSjvuKk&t=3499s) · b000072

&gt;&gt; 他们就觉得，好吧，也许训练，就像，我这里真的有值得用的信息吗？嗯，因为很多，有一种模态承担了所有工作，而加入音频。

### [58:41](https://www.youtube.com/watch?v=FhcHTSjvuKk&t=3521s) · b000073

嗯，我们正尝试不往 loss 中加东西，让它考虑我过去关心的内容。&gt;&gt; 我们的情况是检索（retrieval），以及对比这里数据可能涉及什么问题。

### [59:10](https://www.youtube.com/watch?v=FhcHTSjvuKk&t=3550s) · b000074

&gt;&gt; 你呢？&gt;&gt; 更像是，它非常平衡。所以，我想我一开始就解决了这个问题。&gt;&gt; 好。看来下次应该在课程更早的时候讲这个。大家遇到了很多这类问题。还有谁愿意分享训练时的问题，也许是数据集不平衡，或者模型不平衡，导致多模态没有超过单模态。

### [59:41](https://www.youtube.com/watch?v=FhcHTSjvuKk&t=3581s) · b000075

你想分享吗？你刚才举手了。

### [59:52](https://www.youtube.com/watch?v=FhcHTSjvuKk&t=3592s) · b000076

存在

### [1:00:07](https://www.youtube.com/watch?v=FhcHTSjvuKk&t=3607s) · b000077

对这个有所贡献，所以

### [1:00:17](https://www.youtube.com/watch?v=FhcHTSjvuKk&t=3617s) · b000078

&gt;&gt; 我喜欢做的一些合理性检查（sanity checks）是，嗯，训练单模态模型，比如 A 和 B，你们在期中报告里应该都做过，然后开始分析，对吧？如果 A 达到50%，也就是50%正确、50%错误，错误是什么？最主要的10个错误是什么，不仅错，而且错得最自信的那些，然后可以把其中一些可视化。对于 B，假设60%正确、40%错误，同样看看 B 在模态 B 上犯了哪些错误，对吧？错误是否重叠？它们是否犯了很不一样的错误？这样你就能很好地判断它们是互补的还是冗余的。这是一点，做错误分析（error analysis），看看不同 unit model models \[字幕疑误，可能指 unimodal models，单模态模型\] 犯的错误。在 fusion 时，我们也讨论过，一种处理方法是分阶段方法（stage wise approach）。先在表现最好的模态上训练一个模型。

### [1:01:14](https://www.youtube.com/watch?v=FhcHTSjvuKk&t=3674s) · b000079

在多数情况下，语言可能表现最好，然后得到70%正确、30%错误，再针对这30%，也许基于视觉进行优化，可能把30%降到20%。对于这20%，再加入音频，依此类推，也许降到15%。所以如果始终只优化模型犯的错误，那么理论上应该会减少，对吧？减少多少不确定，但理论上应该减少。我们称之为分阶段融合（stage wise fusion），在 fusion 那节课讲过。很好。嗯，好，看看关于这些会演化的 agents，我们能讲多少。不过对，我想之前讲到某个地方，我们正在讨论这个通用范式，对吧？有多模态数据，做 fusion 和

### [1:02:11](https://www.youtube.com/watch?v=FhcHTSjvuKk&t=3731s) · b000080

alignment 来获得表征，而且因为大多数多模态 LLMs 都以这些表征为条件，你可以开始提问并得到答案。我们谈过生成更多数据，因此有了真正的多模态输入、多模态输出模型。但一个问题是，推理上下文（reasoning context）越来越长。所以这些模型必须接收各种信息，成本会高得多，而且可能开始忘记之前的信息。如果你还记得，我介绍过一个叫 mem1 的方法，是一个管理自身记忆（memory）的 agent 方法，利用强化学习（RL）采取行动，而这些行动也包括把什么存入 memory、从 memory 中丢弃什么。这样一来，你始终只保留一个恒定的内部状态（internal state），概括所有信息，而上下文不会

### [1:03:06](https://www.youtube.com/watch?v=FhcHTSjvuKk&t=3786s) · b000081

随着时间越来越长。因此这些 agents 可以变得更快、更准确，使用更少内存。这是一个通过把 memory management 纳入训练过程，从而能够管理自身记忆的 agent 例子，对吧？然后一切都用 reinforcement learning 训练。这让我们想到，如果 memor \[字幕疑误，可能指 mem1\] 是一个学习管理自身记忆的 agent，对吧？你们也见过其他 agents 管理工具、APIs、配置，但归根结底，大多数时候仍然是用户，也就是你，指派它们做什么，对吧？使用这些工具，这些是你能访问的工具，对吧？很大程度上仍然是手写的。我们称之为运行框架（harness），大家可能熟悉。它叫 harness，对吧？当你给模型提供一个工具时，其实并没有更新语言模型的参数。参数相同，它只是模型外面的封装（wrapper）。你

### [1:04:02](https://www.youtube.com/watch?v=FhcHTSjvuKk&t=3842s) · b000082

让它能够访问可供使用的不同工具和 APIs。这在技术上叫模型的 harness。你们大多数人可能见过 cloud code 泄露事件 \[字幕疑误，可能指 Claude Code\]，对吧？比如 cloud code 就是一个 harness。嗯，它最大的贡献，模型本身是 opus 模型，也就是真正的语言模型。但让 cloud code 如此有用的是模型周围的 wrappers，对吧？你输入这个时该做什么？做这件事时有哪些护栏（guard rails）？出错时怎么办？如何反思？如何在极长的代码库中管理 context？这些都是模型 harness 的一部分。而 cloud code 的 harness 有60,000行代码，对吧？极其依赖手工工程，可能有很多工程师编写。对于 neurosy symbolic 社群 \[字幕疑误，可能指 neuro-symbolic，神经符号\] 来说，这可能是一次重大胜利，因为对他们而言，这些模型并不只是基础模型，实际上很大一部分是 if

### [1:04:57](https://www.youtube.com/watch?v=FhcHTSjvuKk&t=3897s) · b000083

else 语句，60,000行 if else 条件语句，位于基础语言模型之外。但如今，我们有了新机会：我们已经见过更新模型的例子，通过 SFT、RL 训练模型，让模型更好，而下一步演化方案就是连 harness 也训练，对吧？模型的 harness 及其周围的 wrappers，如何随时间自动改善？模型能不能编写自己的 harness？这就是这些 sub evolving agents \[字幕疑误，可能指 self-evolving agents，自演化智能体\] 背后的想法。如我所说，harness 包括 memory、工具、APIs。第一个问题是，这些 agents 如何作为基础模型外的 wrapper，自动决定该做什么。这就是 self-evolving agents。我们还进一步推进，在很多情境下，仅有一个 agent 并不够，对吧？

### [1:05:53](https://www.youtube.com/watch?v=FhcHTSjvuKk&t=3953s) · b000084

多个 agents，每个都能访问语言模型、各自的 harnesses 和其他工具，如何随时间变得更好并演化？我们称之为 self-evvolving multi- aent systems \[字幕疑误，可能指 self-evolving multi-agent systems，自演化多智能体系统\]。让我举一些例子。这大概始于 alpha evolve，以及 Google 的一些工作，研究 agents 如何演化、变得更擅长编码、设计新算法，以及如何用 agents 发现新的数学知识、证明新的定理。这些例子需要模型演化，对吧？因为如果模型只是基于已知数学接受训练、指令和 instruction tuning，我们不会很期待它能够去证明不在其指令数据集、instruction tuning

### [1:06:50](https://www.youtube.com/watch?v=FhcHTSjvuKk&t=4010s) · b000085

数据集中的定理，对吧？所以演化基本上意味着，模型确实在搜索和学习如何随时间改进自身参数、自身 harnesses 和自身 context。具体来说，alpha evolve 可能是这个领域最早的方法之一。然后 open evolve 是一种开源尝试，试图把 alpha evolve 的实现开源。Alpha evolves 来自 Google，所以不开源。一开始由人定义某个东西，对吧？定义任务，通常是某种任务定义，比如优化这个算法。而且通常附带评估（evaluation），比如优化算法时，可以用算法运行时间（runtime）评估，对吧？这就是规格说明（specification），然后这个方法

### [1:07:45](https://www.youtube.com/watch?v=FhcHTSjvuKk&t=4065s) · b000086

首先接收问题定义，先采样不同 prompts，对吧？这些 prompts 基本上根据问题的 context 设计，然后送入语言模型，可以是多个语言模型，各自尝试不同方法。有的尝试用这种方式优化程序，有的用另一种方式优化算法，尝试各种 heristics \[字幕疑误，可能指 heuristics，启发式方法\]。通常会有一个评估器（evaluator），模型可以调用 evaluation function，在这个例子中获得算法 runtime，然后把所有内容发送到数据库。数据库记录模型尝试过、为自己设计过哪些 prompts，以及模型提出的实际解法，也就是代码。它还会记录 evaluation，代码有多好，也就是算法的 runtime。所有这些都会被送入一个 prompt

### [1:08:42](https://www.youtube.com/watch?v=FhcHTSjvuKk&t=4122s) · b000087

数据库。因此，它对之前的尝试有知识和记忆。随后，模型开始根据这个数据库、根据尝试过的东西采样更多 prompts。它通常会依据有效尝试的轨迹，提出下一步要尝试的新东西。这一切都由语言模型完成。所以，对，模型编写的程序都长这样。就是代码，以及我能解决哪些问题。左边讲的是实分析（real analysis）问题，嗯，对积分、不同数学函数求界，这些 C 是界中的常数，对吧？目标是得到尽可能好的近似，所以希望 C 更小，而你实际上可以改进这些近似中已知最好的常数因子

### [1:09:37](https://www.youtube.com/watch?v=FhcHTSjvuKk&t=4177s) · b000088

。然后在几何方面，有很多装箱（bin packing）或正方形打包（square packing）问题，同样，这些问题中有某个常数因子，它们试图改进这个因子。它们实际上改进了其中一些。这里还有更多数学例子，其他常数因子，这些模型实际上能够自动发现它们。所以在 alpha evolve 中，主要就是语言模型接收之前语言模型做过的一系列尝试，然后采样，呃，提出新任务。也有更结构化的方法。这项 shinka evolve 工作，基本上把演化组织成一棵树。从一些尝试开始，tests 是某个

### [1:10:33](https://www.youtube.com/watch?v=FhcHTSjvuKk&t=4233s) · b000089

模型生成的代码，或者生成的文本，然后它更加结构化。它可能定义修改某种东西的具体方式，对吧？呃，这就形成一棵树，然后有时树太大，会被剪枝（pruned）。有时模型继续推进。嗯，不过对，基本上是优化之前的演化策略（evolution strategies），让它更有结构。正如这里所见，嗯，对，这些模型越来越好。通常会看到这些锯齿状阶梯：模型提出更多尝试，再进行评估，另一组模型综合之前尝试过的内容，提出下一批尝试，效果就越来越好。

### [1:11:27](https://www.youtube.com/watch?v=FhcHTSjvuKk&t=4287s) · b000090

在这些方法中，如你所见，模型是固定的，对吧？模型参数从未更新，参数仍然只是基础语言模型的参数，从未更新，变化的只是它周围的 wrappers。所以可以把这看作 harness 层面或 context 层面的演化，模型本身保持不变。还有其他方法，确实会演化模型。呃，之前有 alpha evolve，现在有 theta evolve。基本上，你可以把 alpha evolve 看作一种更复杂的 prompting 方法，让模型尝试不同东西，再根据已有尝试进一步提示它尝试更多东西。基础模型始终固定，但当然可以把模型提出方案的成功率作为信号，对基础模型参数本身进行 reinforcement learning。这样，演化就被反向传播（back propagated）回

### [1:12:23](https://www.youtube.com/watch?v=FhcHTSjvuKk&t=4343s) · b000091

模型权重，对吧？所以 ttt discover、theta evolve，我们确实在测试时训练模型，用改进分数作为 reinforcement learning 的奖励信号（reward signal）。好。所以大概就是这样。嗯，有一个语言模型，输出不同 responses，通常就是它可能写出的不同代码，对吧？优化某个程序或证明某个数学问题的不同方式，然后进入 verifier，验证并得到，猜到当前 runtime 的值，或者要优化的某个指标，再连同，嗯，不，发送到数据库，记录所有尝试、所有代码、所有当前状态，以及进展了多少。这会给出一个新的

### [1:13:17](https://www.youtube.com/watch?v=FhcHTSjvuKk&t=4397s) · b000092

prompt，说明模型下一步应该尝试什么，再送入模型，模型实际尝试，对吧？这就是循环，但现在验证信号，也就是每轮成功演化了多少，会被用作 reward signal，训练实际的模型权重。因此不只是 harness，其他一切，这里的所有东西都是在核心定义它 \[字幕含糊\]，模型权重也在变好。呃，我来收个尾，如果大家感兴趣，下节课开始时可以回顾。嗯，我们还构建了一个被广泛使用的框架，叫 coral。Coral 现在把这种演化扩展到 multi- aent sets \[字幕疑误，可能指 multi-agent settings，多智能体设定\]。同样的想法，对吧？多智能体很有用，因为单个 LLM 只能输出一次试验和一次尝试，而多个 agents 可以输出很多尝试，而且它们

### [1:14:16](https://www.youtube.com/watch?v=FhcHTSjvuKk&t=4456s) · b000093

也可以被 seated \[字幕疑误，可能指 seeded，初始化\] 为不同专长，对吧？嗯，从顶部的配置开始，再次从一段软件进行优化，有 evaluation 告诉你软件当前的 runtime。这个框架 seats \[字幕疑误，可能指 seeds，初始化\] 多个 agents，每个都可以有自己的专长，并自主执行不同任务，对吧？所有 agents 之间有共享记忆（shared memory），每个 agent 都可以读取。它们可以采取行动，在这个例子中是编写代码或修改数据库。它们可以运行 evaluations，查看系统当前状态，也可以写入 shared memory。这个 shared memory 是什么？就是所有 agents 都能访问的内容，包括之前的尝试，每个 agent 尝试过什么、成功率是多少，还有不同的笔记。比如，其中一个 Ben \[字幕疑误，可能指 them\]

### [1:15:12](https://www.youtube.com/watch?v=FhcHTSjvuKk&t=4512s) · b000094

写了一条笔记，说比如更小的批量大小（batch size）实际上能改善 runtime，以及它学到的不同技能（skills），对吧？这个心跳监控器（heartbeat monitor）会定期检查所有 agents，剪除没有进步的 agents，再根据最有希望的方向创建新的 agents。所以，对，结果非常好，而我的时间快到了。我们可以进一步讨论，周四还会讲其他进阶主题。不过，嗯，回顾一下本周任务：课程评价，以及我们明天会发通知，最终决定第五次作业的截止日期和下周二展示的具体安排。好，如果大家还有问题，或者想讨论项目，我会留在这里。否则，谢谢大家。
