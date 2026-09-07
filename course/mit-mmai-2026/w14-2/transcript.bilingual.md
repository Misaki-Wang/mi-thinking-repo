# Lecture 13 – Human-AI Interaction (MIT How to AI Almost Anything/Multimodal AI, Spring 2026)

_Bilingual transcript · 双语讲稿_

- Channel: Paul Liang
- Source: [YouTube](https://www.youtube.com/watch?v=UJra8aMCHXg)
- Duration: 50:24
- Caption source: automatic
- Status: complete
- Chinese translation: 59/59
- Translation provider: codex
- Generated: 2026-09-07T08:06:37+00:00

## Transcript · 讲稿

### [00:00](https://www.youtube.com/watch?v=UJra8aMCHXg&t=0s) · b000001

**English**

Welcome back. Let's get started. Um, so as you all saw the announcement I just posted, by popular demand, we'll extend homework 5 deadline to next Wednesday instead of this Friday. Uh, but try to get that in as soon as possible. And if you still have late days afterwards, you can start using the late days from next Wednesday. Uh for the project we also felt there were a bit too many logistical constraints around poster printing. You require people getting it at two days in advance and you have to buy a bunch of poster poster stands. So we decided to just go with in-class presentations. Uh instructions are the same. So two minutes per student. So for a two people team that will be four minutes. For a three people team that will be six minutes. Um, ideally everyone speaks for for some amount during the presentations. So, it doesn't have to be exactly equal, but um, there

**中文**

欢迎回来。我们开始吧。嗯，正如大家看到的我刚发布的通知，应大家要求，我们把作业 5 的截止日期从本周五延长到下周三。不过，尽量尽快交上来。如果之后你们还有延期天数（late days），可以从下周三开始使用。呃，关于项目，我们也觉得海报打印有点太多后勤方面的限制。要求大家提前两天拿到海报，还得买一堆海报、海报架。所以我们决定直接采用课堂展示。呃，要求还是一样，每位学生两分钟。所以两人小组就是四分钟，三人小组就是六分钟。嗯，最好每个人在展示中都讲一段时间。不一定要完全平均，但，嗯，应该

### [00:58](https://www.youtube.com/watch?v=UJra8aMCHXg&t=58s) · b000002

**English**

should be signs that, you know, everyone contributed to the project. Um, do the math, there's going to be about 50 to 60 students last I checked. So, we might go for about 100 120 minutes. So, we're going to start um at 2:30 on time and we might have to go on till 4:30. We are going to have the TAs put up a schedule for the presentation. So, which team goes first, which team goes second, we're going to release that over the weekend. And if you have any conflicts, so if you have to go exactly at 4, uh, let us know and we'll put you earlier to present. And those who are scheduled to present later, I don't mind if you want to come to class a little bit late. Uh, so you don't have to stay for for too long. Unfortunate, but uh, class ended up being more popular than than I expected. So that'll be next Tuesday in class, you know, in-class presentations and you don't have to worry about, you know, being nervous or anything. It's going to be a chill, casual presentation. People

**中文**

能看出来，你知道，每个人都为项目作出了贡献。嗯，算一下，我上次查看时大概有 50 到 60 名学生。所以可能需要大约 100、120 分钟。因此我们会在 2:30 准时开始，可能得一直进行到 4:30。我们会让助教（TAs）制定展示时间表，哪个小组先讲，哪个小组第二个讲，会在周末公布。如果你们有时间冲突，比如必须在 4 点整离开，呃，告诉我们，我们会把你们安排在前面。安排在后面展示的同学，如果想稍晚一点来上课，我不介意。这样你们就不用待太久。不太理想，不过这门课最后比我预想的更受欢迎。所以就是下周二在课堂上，进行课堂展示，不用担心紧张之类的。这会是轻松、随意的展示。大家

### [01:55](https://www.youtube.com/watch?v=UJra8aMCHXg&t=115s) · b000003

**English**

will ask questions. It's not going to be very strict. Instructions are all updated on on Canvas. There'll be 100 points for the report, 100 points for the presentation, and as you all have seen for the grading scheme, I'm not super strict, so don't worry too much about it. Yes,&gt;&gt; it's always better than&gt;&gt; No, I mean during transition time, you know, might have like one or two questions squeezed in. Okay, nothing to worry about. And then a final report will be due the following Tuesday. Okay. Any other questions about um logistics and these last few assignments? Homework four will be graded by this weekend. So, that'll be out. And then once you all submit homework five next Wednesday, we should grade it by end of next week. Most grades should be in by by end of next week or or earlier in um the following week.

**中文**

会提问。不会特别严格。要求都已在 Canvas 上更新。报告 100 分，展示 100 分，而且大家从评分方案也看到了，我不是特别严格，所以不用太担心。是的，&gt;&gt;这总比……好&gt;&gt;不，我是说在切换的时候，你知道，可能会挤进去一两个问题。好，没什么可担心的。然后最终报告在再下一个周二截止。好。关于安排以及最后这几项作业，还有其他问题吗？作业四会在本周末之前批完，成绩会公布。等大家下周三提交作业五后，我们应该会在下周结束前批完。大部分成绩应该会在下周结束前，或者再下一周较早的时候出来。

### [02:49](https://www.youtube.com/watch?v=UJra8aMCHXg&t=169s) · b000004

**English**

All right. So today we have again one final lecture on advanced topics. We are going to talk about human AI interaction. So how AI can be used to better understand human senses and even extend human sensory perception. uh it's going to focus primarily on AI for smell, taste, temperature, and touch. These uh these are very exciting human senses that I think are very underststudied by today's AI models. Um and then we'll cover a little bit about different guidelines for human AI interaction, especially when you are doing multimodal interaction and we'll cover some in the remaining time cover some work on ethics and safety. So you've seen this picture. So we've u been leading up towards these multimodal foundation models that can flexibly integrate data modalities right language vision audio but of course it's more human senses to be perceived. Uh we've discussed how to learn representations from these modalities right uh learning

**中文**

好。那么今天我们还有最后一堂高级主题讲座。我们要讲人类与人工智能交互（human AI interaction），也就是如何使用 AI 更好地理解人的感官，甚至扩展人的感知能力。呃，主要会聚焦于嗅觉、味觉、温度和触觉方面的 AI。这些是非常令人兴奋的人类感官，我认为当今 AI 模型对它们的研究非常不足。嗯，然后我们会稍微介绍一些 human AI interaction 的不同准则，尤其是在进行多模态交互（multimodal interaction）时，剩余时间里还会介绍一些伦理与安全方面的工作。大家见过这张图。我们一直在逐步走向这些多模态基础模型（multimodal foundation models），它们能够灵活整合数据模态，对吧，语言、视觉、音频，但当然还有更多人类感官需要感知。呃，我们讨论过如何从这些模态中学习表征（representations），对吧，呃，学习

### [03:46](https://www.youtube.com/watch?v=UJra8aMCHXg&t=226s) · b000005

**English**

basic representations aligning them across sequences and fusing these modalities to get more powerful representations. And then we also saw how these representations could be fed into language models so that you could have flexible question answering open-ended prediction reasoning capabilities everything that you inherit from language models but now condition on these other modalities. Uh so that was this part and we also saw how we could perform both multimodal fusion input representation learning and also decoding so multimodal generation. So you can also get uh capabilities like generating more images or videos and uh outputting more modalities as well. And this could be done across multiple reasoning steps. Right? This is essentially the frontier of today's foundation models with multimodal input, multimodal reasoning across multiple steps. And finally the human aspect is you can think of it as this icon where all this is done in the loop with people inside

**中文**

基础表征，在序列之间对齐它们，并融合这些模态来得到更强大的表征。然后我们也看到了如何把这些表征输入语言模型（language models），这样就能获得灵活的问答、开放式预测、推理能力，所有从 language models 继承的能力，但现在以这些其他模态为条件。呃，那就是这一部分。我们也看到了如何同时进行多模态融合（multimodal fusion）、输入表征学习（representation learning），以及解码（decoding），也就是多模态生成（multimodal generation）。所以你也能获得生成更多图像或视频等能力，以及输出更多模态。而且这可以跨多个推理步骤进行。对吧？这基本上就是当今 foundation models 的前沿：多模态输入，跨多个步骤的多模态推理。最后，人这一方面，可以把它看成这个图标，所有这些都是在人参与其中的循环中完成的

### [04:44](https://www.youtube.com/watch?v=UJra8aMCHXg&t=284s) · b000006

**English**

of them where they're constantly sensing from the environment. they're sensing from people and they're outputting language and other interactive mediums to uh change people's perception or to improve people's capabilities. So, so what are some examples of that? So, we've looked at a lot of modalities that are more digital in nature like language, vision, and audio. I'm going to discuss some of our groups and also the broader community's work in AI for other modalities. So, starting with smell, right? Smell is such an exciting modality. It's what allows us to detect nice foods and beverages. It helps us and animals detect dangers and it's also a very critical part of health, right? Many diseases which manifest a change in hormones or bodily states can actually lead to changes in smell of different patients. So um there's been a long line of work and we are contributing to this

**中文**

，它们不断感知环境，感知人，并输出语言和其他交互媒介，来改变人的感知，或增强人的能力。那么，有哪些例子呢？我们看过很多本质上更偏数字化的模态，比如语言、视觉和音频。我将介绍我们团队以及更广泛研究社区在其他模态 AI 方面的一些工作。先从嗅觉开始，对吧？嗅觉是非常令人兴奋的模态。它让我们能够发现美味的食物和饮料，帮助我们和动物察觉危险，也是健康中非常关键的一部分，对吧？很多表现为激素或身体状态变化的疾病，实际上会导致不同患者的气味发生变化。所以，嗯，长期以来一直有一系列工作，我们也在为这一

### [05:40](https://www.youtube.com/watch?v=UJra8aMCHXg&t=340s) · b000007

**English**

line of work on building AI systems can detect smell. So this is using smell as an input and afterwards I'll discuss smell as an output. Uh but first of all smell as an input, right? So what does that entail? This is a quick demo video. So you have a bunch of spices all have pretty strong smells and you portion out a little bit of each slice and you bring it to this AI machine that is able to sniff out what these substances are. Right? How it sniffs out is that this blue chip over here is a smell sensing device. It's a smell sensing chip that captures different VOCC's. These are volatile organic compounds, mixtures of carbon, oxygen, hydrogen. And the box over there is to seal in the gases released by the substance. And based on what the AI platform acts as similarity with its prior database, it is becoming much more confident of its similarity with oregano within the first minute. So that similarity goes higher and higher and it

**中文**

方向作贡献，构建能够检测气味的 AI 系统。这里是把气味作为输入，之后我会讨论把气味作为输出。不过首先，气味作为输入，对吧？这涉及什么呢？这是一个简短的演示视频。你有一堆香料，气味都相当浓烈，你从每个 slice \[字幕疑误，可能指 spice\] 中分出一点，把它拿到这台 AI 机器前，它就能嗅出这些物质是什么。对吧？它怎么嗅出来呢？这里的蓝色芯片是一个气味感知设备，是一块捕捉不同 VOCC's \[字幕疑误，可能指 VOCs\] 的气味感知芯片。这些是挥发性有机化合物（volatile organic compounds），碳、氧、氢的混合物。那边的盒子用来封住物质释放的气体。根据 AI 平台与先前数据库进行的相似性判断，在第一分钟内，它越来越确信这与牛至相似。所以相似度越来越高，它

### [06:37](https://www.youtube.com/watch?v=UJra8aMCHXg&t=397s) · b000008

**English**

spends the last minute being much more confident that this oregano. So detecting this size space only on the smells released um from the substance alone, not through vision or not through language or not through any other other perceptual modality. So here is just the video in static form. That's the little container with the substance. That blue chip over there is a commercial gas sensing chip. So that cost about $20. It captures about six VOCC's. So carbon monoxide is one, ethanol is one, um hydrogen and are other examples of volatile organic compounds. And that over here is the circuit. And in addition to capturing VOCC's, there's several other sensors at the back over there. Those three round sensors, they sense temperature, humidity, and pressure. Okay, these are also things that are known to change when you put a substance, right? They

**中文**

在最后一分钟更加确信这是牛至。所以，检测这个 size space \[字幕疑误，可能指 spice，香料\]，只依据物质本身释放的气味，而不是通过视觉、语言或任何其他感知模态。这里就是视频的静态画面。那是装有物质的小容器。那边的蓝色芯片是商用气体感知芯片，价格大约 $20。它能捕捉大约六种 VOCC's \[字幕疑误，可能指 VOCs\]。一氧化碳是一种，乙醇是一种，嗯，氢和……是挥发性有机化合物的其他例子。这里是电路。除了捕捉 VOCC's，后面还有其他几个传感器。那三个圆形传感器测量温度、湿度和气压。好，这些也是我们知道放入一种物质时会发生变化的东西，对吧？它们

### [07:33](https://www.youtube.com/watch?v=UJra8aMCHXg&t=453s) · b000009

**English**

can affect the humidity within the local environment. Uh, but to us, you know, we're not really sensing people or AI people. So to us, these are all just time series data. So you have time steps. These are being read out at one reading per second, so one hertz. So you see these jagged ups and downs for different gases and for different atmospheric conditions. So to us, it's a multimodal problem involving lots of time series. And then you can throw all your favorite AI machinery at it to extract information from these time series and to make your predictions which in this case is like a softmax. So before I talk about the model of course the data is key right without large scale data about how different substances smell there's no way you can even train a model to do this sort of detection. So building upon you know prior work which really looked at collecting small data sets for

**中文**

会影响局部环境的湿度。呃，但对我们来说，你知道，我们其实不是做感知的人或者做 AI 的人。所以对我们来说，这些都只是时间序列数据（time series data）。你有时间步。这些数据以每秒一次的频率读取，也就是一赫兹。所以你会看到不同气体、不同大气条件下这些锯齿状的起伏。对我们来说，这是一个涉及许多 time series 的多模态问题。然后你就可以用上所有你喜欢的 AI 方法，从这些 time series 中提取信息并作出预测，在这里就像是一个 softmax。不过在讲模型之前，数据当然是关键，对吧？没有关于不同物质气味的大规模数据，你根本没办法训练模型来做这种检测。所以，基于以前那些主要收集小型数据集、针对

### [08:29](https://www.youtube.com/watch?v=UJra8aMCHXg&t=509s) · b000010

**English**

individual smells. So just detecting is it apple or banana uh we really scaled up data collection. So we created smell net um inspired by image net and how it really catalyzed a field of AI for computer vision. So there's 50 substances 10 types of nuts, spices, herbs, fruits and vegetables. For each of these substances, we portion our little amounts in that container. We brought it to this smell sensing platform for 10 minutes. So that gives you 600 readings as a time series. These are your VOCC's, carbon monoxide, VOCC's, atmospheric conditions. And we repeated this over different environments. So sometimes indoors, sometimes outdoors, sometimes in spring, sometimes in winter when there's people breathing over it, when there's no people breathing over it. to really expose the readings to in the wall settings where you can actually uh want where you actually want to deploy these

**中文**

单独气味的工作，比如只是检测这是苹果还是香蕉，我们真正扩大了数据收集的规模。我们创建了 smell net \[字幕疑误，可能指 SmellNet\]，灵感来自 image net \[字幕疑误，可能指 ImageNet\]，以及它如何真正推动了计算机视觉（computer vision）AI 领域的发展。这里有 50 种物质，坚果、香料、香草、水果和蔬菜各 10 种。对于每种物质，我们分出一点放进那个容器，拿到气味感知平台上测量 10 分钟。这样就得到一个有 600 次读数的 time series。这些是 VOCC's \[字幕疑误，可能指 VOCs\]、一氧化碳、VOCC's、大气条件。我们在不同环境中重复这个过程，有时在室内，有时在室外，有时在春天，有时在冬天，有人在上面呼吸时、没有人在上面呼吸时。这样才能让读数真正接触 in the wall \[字幕疑误，可能指 in the wild，真实环境\] 的场景，也就是你实际上想要部署这些

### [09:26](https://www.youtube.com/watch?v=UJra8aMCHXg&t=566s) · b000011

**English**

smell sensors. Right? So we believe that you know just having controlled in the lab conditions won't be sufficient for getting true in the wild generalization and then we labeled uh with textual description what it was. So this was strawberry and we took a photo of it in its environment that we collected a smell and we also paired it up with other chemical information and that gives you a smell net. Uh like was with any data sets we could basically went through the homework 1 2 3 4 5 that you all went through. So homework one for us was just visualizing the data right visualizing and trying out different pre-processing methods to see whether it's actually giving a good signal. So PCA on this data shows first you did PCA across your five broad categories. So there's some clear separation for example in purple those were fruits pretty well separated over here. Uh but some of these between red

**中文**

气味传感器的场景，对吧？所以我们认为，仅仅有实验室里的受控条件，不足以获得真正的真实环境泛化（in the wild generalization）。然后我们用文字描述来标注它是什么。所以这个是草莓，我们在收集气味的环境里给它拍了一张照片，还为它配上其他化学信息，这就构成了 smell net \[字幕疑误，可能指 SmellNet\]。呃，像处理任何数据集一样，我们基本上也经历了你们经历过的作业 1、2、3、4、5。对我们来说，作业一就是可视化数据，对吧，可视化并尝试不同的预处理（pre-processing）方法，看看它是否真的提供了良好的信号。对这些数据做主成分分析（PCA），首先是在五个大类别之间做 PCA。可以看到一些明显的分离，比如紫色的是水果，在这里分得相当开。但其中一些，比如红色

### [10:22](https://www.youtube.com/watch?v=UJra8aMCHXg&t=622s) · b000012

**English**

and orange so vegetables and nuts were not very well separated and that correlated with what kind of performance we were getting in detecting those substances. If you go deeper into the 10 specific types of fruits, uh again you do PCA on these sensor readings, some some fruits were very well separated and some were were confounded and overlapping with each other.&gt;&gt; Yes.&gt;&gt; Do you think this is because&gt;&gt; definitely I mean one of the key limitations is that and I'll talk about some of the other broader work in different types of sensing and it trade-offs. Uh but this is a portable low resolution sensor right and on the other hand there are also um non-portable large expensive high resolution sensors right this is a common trade-off that you get anywhere right cheap low cost low resolution you can bring out

**中文**

和橙色，也就是蔬菜和坚果，就没有很好地分开，这也与我们检测这些物质时得到的性能相关。如果进一步看 10 种具体水果，同样对这些传感器读数做 PCA，有些水果分得很好，有些则混淆在一起，相互重叠。&gt;&gt;是的。&gt;&gt;你觉得这是因为……&gt;&gt;当然，我是说，一个关键限制是，我之后也会讲一些其他更广泛的工作，涉及不同类型的感知及其权衡。不过这是一个便携式低分辨率传感器，对吧？另一方面，也有不便携、体积大、昂贵的高分辨率传感器。这是到处都存在的一种常见权衡，对吧？便宜、低成本、低分辨率，可以带到

### [11:18](https://www.youtube.com/watch?v=UJra8aMCHXg&t=678s) · b000013

**English**

everywhere versus really expensive ones so what can you do well what can you do here what is the multimodal research challenge that deals with different data, some of which is low cost, noisy, imperfect, and how to leverage uh larger scale, higher quality data. Well, we could uh pre-train some other similarly task that like automatically bootstrap our current data set. Um we also looking at this use a method to create a more interpretable distribution. So right now it seems like uh you have like a spread that goes um weirdly along the y axis.

**中文**

任何地方，与那些非常昂贵的设备相比。那么你能做什么呢？在这里能做什么？哪个多模态研究挑战涉及处理不同的数据，其中一些成本低、有噪声、不完善，以及如何利用规模更大、质量更高的数据？嗯，我们可以预训练（pre-train）某种其他相似任务，自动为当前数据集进行自举（bootstrap）。嗯，我们也在考虑用一种方法创建更可解释的分布。目前看起来，你有一种沿 y 轴奇怪地延展的分布。

### [12:13](https://www.youtube.com/watch?v=UJra8aMCHXg&t=733s) · b000014

**English**

So perhaps if you can reshape that distribution uh you might be able to use um or get exactly the method but you might be able to use a method to go ahead and make a better composition.&gt;&gt; I think you got some important keywords but who remembers the there are six core multimodal challenges like which challenge deals with the fact where you want to do prediction but your data is imperfect and noisy and how do you leverage higher quality external databases? Yes, transference um of which you did mention specific approaches for transference which is alignment right. So that's exactly what we did. uh ignore that part first. Let me just dive into this part. So we have sensor representations which are the ones that we got right low cost sensors and these are your six time series separately. GCMS is um is a technique in chemistry.

**中文**

所以也许如果能重塑这个分布，你可能可以使用，嗯，或者得到确切的方法，但你可能可以用一种方法，进一步得到更好的组合。&gt;&gt;我觉得你说到了一些重要关键词，不过谁还记得，六个核心多模态挑战中，哪个挑战处理的是你想进行预测，但数据不完善且有噪声，以及如何利用更高质量的外部数据库？是的，迁移（transference）。嗯，你确实提到了 transference 的具体方法，也就是对齐（alignment），对吧。这正是我们所做的。呃，先忽略那部分，我直接讲这部分。我们有传感器表征，就是我们得到的那些，对吧，低成本传感器产生的，这些分别是六个 time series。GCMS 是，嗯，是化学中的一种技术。

### [13:10](https://www.youtube.com/watch?v=UJra8aMCHXg&t=790s) · b000015

**English**

It's called gas chromatography mass spectroscopy. Some of you might be remember your your chromatography from kind of high school chemistry where you took a substance and made it into a liquid and you put the paper and you see how the color separated in the paper. You all remember that right? That was this approach that essentially gave you any substance and allows you to decompose that substance into um mixture of individual elements. Right? Each element has a different density and therefore they travel different amounts on that paper. Uh so these are you know state-of-the-art chemistry tools. They are huge machines. They can put in anything like cashew, apples, oranges, any types of fruits and you'll break it apart into it exact components and those exact mixtures, right? Which is perfect. But the downside is that these are huge machines. So huge you can't bring around everywhere. You can't scale up data collection as you could with these sensors. So what can you do? You can

**中文**

它叫气相色谱质谱技术，原文是 gas chromatography mass spectroscopy \[术语疑误，通常为 gas chromatography–mass spectrometry，GCMS\]。你们有些人可能还记得高中化学里的色谱法，把一种物质变成液体，放上纸，观察颜色如何在纸上分开。大家都记得，对吧？这种方法基本上让你拿到任何物质后，把它分解成各个单独元素的混合物。对吧？每种元素的密度不同，因此在纸上移动的距离不同。呃，所以这些是最先进的化学工具，是巨大的机器。可以放入任何东西，比如腰果、苹果、橙子、任何种类的水果，它会把它拆解成精确的组成成分和那些确切的混合物，对吧？这很好。但缺点是机器非常大，大到无法随身带到各处。你也无法像使用这些传感器一样扩大数据收集规模。那能做什么呢？你可以

### [14:09](https://www.youtube.com/watch?v=UJra8aMCHXg&t=849s) · b000016

**English**

take some of these sensor representations that you collect in the wild and you can collect some of this GCMS data not for everything but for some of them and the good thing is that you know he has also released GCMS databases online for the most common foods like teas and coffees and fruits and vegetables and you can then start aligning them in representation space you can do contrastive learning and align them in representation space so your sensor representations are close to the corresponding GCMS representations right? The chemistry representations for the ones in which you have paired data and naturally you're going to have a lot more sensor representations because this is easy to collect. U so they're not going to have corresponding GCMS data but because you learn this well-shaped representation space uh they're leveraging what they know about other GCMS to roughly position themselves in a better location in that representation space. So this was what we saw in in

**中文**

拿一些在真实环境中收集的传感器表征，再收集一些 GCMS 数据，不需要所有样本都有，只要其中一部分有。好处是，你知道，他也在网上发布了 GCMS 数据库，涵盖最常见的食物，比如茶、咖啡、水果和蔬菜。然后你就可以开始在表征空间（representation space）中对齐它们，可以做对比学习（contrastive learning），在 representation space 中对齐，让传感器表征接近相应的 GCMS 表征，对吧？也就是那些有配对数据的样本的化学表征。自然，你会有更多传感器表征，因为这很容易收集。所以它们不会有对应的 GCMS 数据，但因为你学到了这个形态良好的 representation space，它们会利用从其他 GCMS 中获得的知识，大致把自己放到该空间中更好的位置。所以这就是我们在

### [15:06](https://www.youtube.com/watch?v=UJra8aMCHXg&t=906s) · b000017

**English**

transference, right? Specifically the co-learning of transference where you took the weak modality and you aligned it with the strong modality to learn a common embedding space and then afterwards uh you can throw away the strong modality during inference and just do inference using the weaker modality. uh several other things that we tried. Um these were more pre-processing but you know the sensing data itself the absolute values were not super important because the absolute value changes every day depending on your temperature or your humidity uh but the relative values are more important. So the relative values of how it changes actually gives you more information about what the substance is. So we did this kind of first order temporal difference which essentially tracks the relative changes instead of the absolute readings right by taking XT minus XT in couple of uh

**中文**

transference 中见过的，对吧？具体来说，就是 transference 中的共同学习（co-learning）：拿较弱的模态与较强的模态对齐，学习一个共同的嵌入空间（embedding space），之后在推理（inference）时可以丢掉较强的模态，只用较弱的模态进行 inference。呃，我们还尝试了其他几件事。嗯，这些更多属于 pre-processing，但感知数据本身的绝对值并不是特别重要，因为绝对值每天都会随着温度或湿度而变化，相对值更重要。变化的相对值实际上能提供更多关于物质是什么的信息。所以我们做了这种一阶时间差分（first order temporal difference），基本上跟踪相对变化，而不是绝对读数，对吧，方法是用 XT 减去几个

### [16:02](https://www.youtube.com/watch?v=UJra8aMCHXg&t=962s) · b000018

**English**

windows ago. So uh and then you also try different approaches of MLP. Naturally they don't work very well because they don't capture the sequential nature of time series data. CNN's in this case are 1D CNN's right because it's a 1D signal. LSTMs sent former which is kind of our transformer and you see that in most cases the contrastive approach outperforms the regular approach uh and overall this transformer LSTM work better than 1D CNN's and MLBs so that's an example of how you would kind of reason about different modalities even though it's technically a unimodal problem to begin with it's only just time series uh but leveraging for example this external database of GCMS higher quality chemical repres representations to do transference is an example of how you would um you know think about these multimodal challenges and choose an approach in practice.

**中文**

窗口之前的 XT。然后还尝试不同的多层感知机（MLP）方法。自然，它们效果不太好，因为它们无法捕捉 time series data 的序列特性。这里的卷积神经网络（CNN's）是 1D CNN's，对吧，因为它是 1D 信号。长短期记忆网络（LSTMs）、sent former \[字幕疑误，可能指 ScentFormer\]，也就是我们的 transformer。你可以看到，大多数情况下，contrastive 方法优于常规方法，总体上 transformer、LSTM 比 1D CNN's 和 MLBs \[字幕疑误，可能指 MLPs\] 更好。所以这就是一个例子，展示如何思考不同的模态，尽管从技术上说，它一开始是个单模态（unimodal）问题，只是 time series，但利用例如这个 GCMS 外部数据库中质量更高的化学表征来进行 transference，就是如何思考这些多模态挑战，并在实践中选择方法的例子。

### [17:05](https://www.youtube.com/watch?v=UJra8aMCHXg&t=1025s) · b000019

**English**

So we also made a point to train a general model. So we have 50 substances. You think of that as obviously we're not quite there yet but it's a step towards a general purpose smell detector which you can then fine-tune. you can fine-tune the the model. Um, in this case, you could fine-tune a whole model, but you know, as people scale the model up, you could then start fine-tuning just the prediction head for specific tasks. So, here is an example of fine-tuning it specifically for detecting peanuts. So, there's peanuts and no peanuts, right? So, you can bring it to different cakes and peanut butters and candy bars, and that'll be useful for essentially detecting whether there's peanuts through smell in case somebody's allergic to it. Uh and this turned out to obviously be harder than we thought. You know, if you start cooking and roasting and salting these peanuts and incorporate them into dishes, uh the problem becomes quickly very very difficult. So, we're still working on this.

**中文**

所以我们也特意训练了一个通用模型。我们有 50 种物质。你可以把它看成，显然我们还没完全做到，但这是向通用气味检测器迈出的一步，之后可以对它进行微调（fine-tune）。你可以 fine-tune 这个模型。嗯，这里可以 fine-tune 整个模型，但随着模型规模扩大，可以开始只针对特定任务 fine-tune 预测头（prediction head）。这里是一个专门 fine-tune 来检测花生的例子，有花生和没有花生，对吧？你可以把它带到不同的蛋糕、花生酱和糖果棒前，基本上通过气味检测是否含有花生，以防有人过敏。呃，这显然比我们预想的更难。如果你开始烹煮、烘烤、给这些花生加盐，再把它们加入菜肴，问题很快就会变得非常非常困难。所以我们还在研究。

### [18:03](https://www.youtube.com/watch?v=UJra8aMCHXg&t=1083s) · b000020

**English**

&gt;&gt; Yeah.&gt;&gt; Cuban smell is like notoriously common. Um is there some notion of that?&gt;&gt; Um I'm not sure. I think VOCC's are of course a very coarse representation right um it's not decomposing exactly into these substances but rather the gases that the substances released so there is some correlation but it's not detecting the substances themselves um talking about compositional I'll show this this other work uh which we then started looking at smell generation right generation is where you have to deal with this compositionality because you cannot go around collecting you know pockets of smells of all substances in the world that will not scale that will not allow you to do general purpose transmission just like how you cannot you know send photos by having a f every single photograph in the world you need to decompose it into

**中文**

&gt;&gt;是的。&gt;&gt;Cuban 气味 \[字幕疑误，可能指 cumin，孜然\] 是出了名的常见。嗯，有没有某种关于这一点的认识？&gt;&gt;嗯，我不确定。我认为 VOCC's \[字幕疑误，可能指 VOCs\] 当然是非常粗略的表征，对吧，它并不是精确分解成这些物质，而是物质释放出的气体，所以存在一些相关性，但它并不检测物质本身。说到组合性（compositional），我来展示另一项工作，我们接着开始研究气味生成。生成时必须处理这种组合性（compositionality），因为你不能到处收集世界上所有物质的一小包气味，那无法扩展，也无法实现通用传输。就像你不能通过拥有世界上每一张照片来发送照片，你需要把它分解成

### [18:57](https://www.youtube.com/watch?v=UJra8aMCHXg&t=1137s) · b000021

**English**

its most principal components right in image generation is RGB so what is the equivalent uh base dimensions for smell generation so we've been exploring that so we started with these spices uh but we also have these aroma oils You get these from Whole Foods. We did get these from Whole Foods. This is a aroma oil for pear. So, some of them smell very much like their real world counterparts. Some of them smell slightly different. So, you can start putting these sensors and measuring how similar the real substance in the aroma oil is. That's the sensor. And if they're similar, you can put these aroma oils into some of these wearable devices that have little canisters that release uh the aroma oils according to some prespecified duration. So you can release one oil for one second and then another oil for half a second followed by a third one for two seconds. So you

**中文**

最主要的组成部分，对吧？在图像生成中是 RGB，那么气味生成对应的基础维度是什么？我们一直在探索这一点。我们从这些香料开始，但也有这些香氛油。你能在 Whole Foods 买到，我们确实就是从 Whole Foods 买的。这是梨的香氛油。有些闻起来非常像现实世界中的对应物，有些略有不同。所以你可以开始放置这些传感器，测量真实物质与香氛油有多相似。那是传感器。如果它们相似，你可以把这些香氛油放入一些可穿戴设备（wearable devices）中，它们有小罐子，会按照预先指定的时长释放香氛油。比如一种油释放一秒，另一种释放半秒，接着第三种释放两秒。这样你

### [19:52](https://www.youtube.com/watch?v=UJra8aMCHXg&t=1192s) · b000022

**English**

can implicitly get all sorts of of mixtures of the 12 12 base smells, right? Uh and right now it's 12 because this necklace fits 12. But if you wanted something less portable, for example, something that stood on your your desk, you could have more. If you want something that's even more portable, we're trying to put it on the back of your phone so that you know you can just maybe use five or six and that will fit on the back of your phone. They wouldn't have to wear this necklace. So what are the core questions here? So if you want to take any substance and transmit it to your friend who's wearing this necklace, first you have to decide what the 12 smells are, right? Okay, the 12 smells that are that are existing on the necklace and that has to be chosen carefully because you want it to cover all different types of smells so there sufficient coverage and also the fact that you know these smells when they mix together they actually give you pleasant

**中文**

就能以隐式的方式得到这 12、12 种基础气味的各种混合，对吧？现在是 12 种，因为这条项链装得下 12 种。但如果你想要便携性低一些的东西，比如放在桌上的设备，就可以有更多。如果想要更便携的，我们正在尝试把它放到手机背面，这样也许只用五六种，就能装在手机背面，他们就不用戴这条项链了。那么这里的核心问题是什么？如果你想取任何一种物质，把它传给戴着这条项链的朋友，首先必须决定这 12 种气味是什么，对吧？好，就是项链上现有的 12 种气味，必须仔细选择，因为你希望它覆盖各种不同类型的气味，有足够的覆盖范围，而且这些气味混合在一起时，确实能产生令人愉悦的、

### [20:46](https://www.youtube.com/watch?v=UJra8aMCHXg&t=1246s) · b000023

**English**

expected um fruit smells. Um so that's what we did. We first decided on these 12 base smells through a mixture of reading the literature, talking to people who makes perfumes for a living. We came up with a set that we're quite happy with. Took a couple of iterations. And then the question becomes, how do you when given a real substance break it down to these 12? We find that well your pre-trained models are actually surprisingly good at this. So you can just take a photo. In this case, the photo is a of a salad. You can optionally give a description of it. So maybe today you added more chicken or you added more more paprika to it to give an optional description. uh this would be complimentary information in the language modality that is not evident in the image and you prompt a multimodal LLM in this case you just use know your quen models you prompt your

**中文**

预期的水果气味。嗯，这就是我们做的。我们首先结合阅读文献，以及与以调香为业的人交谈，确定了这 12 种基础气味。经过几轮迭代，得出了一组我们相当满意的气味。然后问题变成，给定一种真实物质，如何把它分解成这 12 种？我们发现，预训练模型（pre-trained models）在这方面其实好得令人惊讶。你只需拍张照片，这里是一张沙拉照片，也可以选择提供描述。比如今天多加了鸡肉，或者多加了红椒粉，可以提供一段可选描述。这就是语言模态中的补充信息，在图像中并不明显。然后提示一个多模态大语言模型（multimodal LLM），这里你就用 quen 模型 \[字幕疑误，可能指 Qwen\]，提示你的

### [21:40](https://www.youtube.com/watch?v=UJra8aMCHXg&t=1300s) · b000024

**English**

multimodal LLM to break down this food into these four base notes give it what these four base notes are right and then it'll start doing it reasoning and it will output essentially 12 numbers in this case it output eucalyptus for 10 seconds red clover for some duration sage. These are your herbs and your spices. And then strawberry, onion. So this is what the model outputs. It's a list of 12 numbers which can be sent to the wearable necklace and then released releasing those smells according to those to those durations. So you find this works surprisingly well. Even the zeroot case works surprisingly well because I mean these these models have seen all your cookbooks and all your recipes and all your online descriptions of how things smell. So, um I don't know. I found it surprising that it worked so well. Maybe some people might find it not that surprising. And yes,

**中文**

multimodal LLM 把这份食物分解成这四种基调，告诉它这四种基调是什么，对吧？然后它会开始推理，基本上输出 12 个数字。这里它输出的是桉树 10 秒，红三叶草某个时长，鼠尾草。这些是香草和香料。然后是草莓、洋葱。这就是模型输出的内容，是一个由 12 个数字构成的列表，可以发送给可穿戴项链，然后按照这些时长释放气味。你会发现效果好得令人惊讶。甚至 zeroot \[字幕疑误，可能指 zero-shot，零样本\] 情况下也出奇地好，因为这些模型看过你所有的烹饪书、菜谱，以及网上对各种东西气味的描述。所以，嗯，我不知道，我觉得它效果这么好很令人惊讶。也许有些人觉得没那么意外。是的，

### [22:37](https://www.youtube.com/watch?v=UJra8aMCHXg&t=1357s) · b000025

**English**

&gt;&gt; our experience I I got to try it recently and it felt like there was like a peak moment when it became the the object that we were like the dish that we were that like would they all come together at a certain point that dish?&gt;&gt; I don't know.&gt;&gt; Why don't you describe your experience? What dish did you put? What happened at the start, at the peak, at the end?&gt;&gt; Well, like Alu asked me like what I wanted to smell. I think I said&gt;&gt; like I actually don't even remember what I asked. Oh, but&gt;&gt; I remember feeling like smelling the distinct smells and then all of a sudden they like became compositional and they became the dish and then it fell apart again. It was really It was honestly kind of trippy. It was cool.&gt;&gt; Yeah. Cool. Now, when we tried this out with lots of people, um, we had a bunch of experiments where I was just smelling foods and I think that as a whole went

**中文**

&gt;&gt;我们的体验，我最近有机会试了一下，感觉有一个高峰时刻，它变成了那个物体，就是我们那道菜，我们那个……它们会不会在某个时刻组合起来，成为那道菜？&gt;&gt;我不知道。&gt;&gt;不如你描述一下自己的体验？你选了什么菜？开始时、高峰时、结束时分别发生了什么？&gt;&gt;嗯，Alu 问我想闻什么，我想我说的是……&gt;&gt;其实我甚至不记得我提了什么。哦，不过……&gt;&gt;我记得先闻到了各自独立的气味，突然间它们就像组合到了一起，变成了那道菜，然后又散开了。真的，说实话，有点迷幻，很酷。&gt;&gt;是的，很酷。后来我们让很多人试用，做了一系列实验，我只是在闻食物，我觉得整体上

### [23:35](https://www.youtube.com/watch?v=UJra8aMCHXg&t=1415s) · b000026

**English**

pretty well. Um, in fact, the more complicated the food, the better it worked. If someone just said someone I think just said vanilla and they just output a mint because vanilla is too basic of a substance that it was not easy to be broken down into these tall base notes. And then but if you start saying things like you know your pizzas, your cheeseburgers, your spicy foods um because it's first of all it's quite subjective right then and it's actually easier to be broken down into these these components. And then we also another set of experiments where people talked about their memories and some people would say a memory of a conference. Somebody said that and they actually cried when they when they smelled this and it triggered some memory of a really memorable event in the past. um which is a cool example because again memories are quite subjective. I think smell can as a modality interactive modality actually can trigger a lot of memories and it's a

**中文**

效果相当好。事实上，食物越复杂，效果越好。如果有人只说，我记得有人只说了香草，它就只输出了薄荷，因为香草是一种太基础的物质，不容易分解成这些 tall base notes \[字幕疑误，可能指 twelve base notes，12 种基调\]。但如果你开始说披萨、芝士汉堡、辛辣食物之类的，嗯，首先这相当主观，对吧，而且实际上更容易分解成这些组成部分。我们还做了另一组实验，让人们谈论自己的回忆，有些人会说起参加某次会议的回忆。有个人说了这个，闻到之后真的哭了，因为这触发了过去某件特别难忘的事的记忆。这是一个很酷的例子，因为回忆同样非常主观。我认为嗅觉作为一种模态、一种交互模态，确实能触发很多回忆，而且这是一个

### [24:29](https://www.youtube.com/watch?v=UJra8aMCHXg&t=1469s) · b000027

**English**

perfect example where we don't have a right answer. It's fine if the model is wrong but it's bring about positive experience for the user. So that was zero shot. Uh naturally because smell is so subjective we added a step where uh someone can refine it right some people are more sensitive to cumin or to onion. So you can say this smell is too strong or it's too sweet and you reduce it and you naturally you can start converting that into language or use reinforcement learning to update the 12 base smells. Um so again stuff that you have seen in class but applied applied to this setting and we find that after you know a couple of steps of refinement um the perception of a similarity with the original substance or the target substance becomes much much better. So uh I'll skip some of these details but for the paper if you're interested a lot of it came down to how we get people

**中文**

没有标准答案的绝佳例子。模型即使错了也没关系，但它为用户带来了积极体验。这就是零样本（zero shot）。呃，自然，因为气味非常主观，我们加了一个让人进一步调整的步骤，对吧，有些人对孜然或洋葱更敏感。你可以说这个气味太浓，或者太甜，然后降低它，自然也可以开始把这些转换成语言，或者使用强化学习（reinforcement learning）来更新这 12 种基础气味。嗯，所以还是课堂上见过的东西，只是应用在这个场景中。我们发现，经过几步调整之后，人们感受到的与原始物质或目标物质的相似度就会好得多。呃，我会跳过一些细节，但如果你对论文感兴趣，其中很多工作归结为如何让人们

### [25:25](https://www.youtube.com/watch?v=UJra8aMCHXg&t=1525s) · b000028

**English**

to describe smells because naturally language models need to have a use a good vocabulary to prompt the model to decompose it into the smells correctly. So a lot of work in essentially collecting the alignment. We think of it as an alignment problem between smell data and language data. That also allowed us to obtain these 12 base smells. As you can see, they really cover um all your all your base tastes and all your base smells, right? From from smoky to warm to refreshing to sweet to spicy. We find that the learning procedure helps a lot. So, um you know, adding these multiple steps of refining and learning helps and afterwards the model can learn from how the user refineses. So if I always say I'm very sensitive to spicy things then afterwards you will not have to refine it. The model can automatically do it zero shot better than at the beginning. So it's becoming more personalized.

**中文**

描述气味，因为 language models 自然需要使用一套好的词汇来提示模型，把它正确分解成各种气味。因此，大量工作基本上是在收集 alignment 所需的信息。我们把它看成气味数据与语言数据之间的 alignment 问题。这也让我们得到了这 12 种基础气味。可以看到，它们确实覆盖了所有基础味觉和基础气味，对吧？从烟熏、温暖，到清新、甜、辛辣。我们发现学习过程帮助很大。加入这些多步骤的调整和学习会有帮助，之后模型还能从用户的调整方式中学习。所以如果我总是说自己对辛辣的东西非常敏感，之后就不用再调整。模型可以自动完成，zero shot 的效果比一开始更好。所以它会变得更加个性化。

### [26:22](https://www.youtube.com/watch?v=UJra8aMCHXg&t=1582s) · b000029

**English**

I also compared it to human mixing. So we actually got some human perfume experts who actually study smells and their mixtures for living. So when given a substance they would mix different liquids and perfumes to give you the recreation. And we see how this AI approach compares with the human approach of of mixing these maps. And we get obviously human is better in some cases. But in terms of uh you know the amount of time that you save, the amount of effort that you save, um the AI is helping a lot. As we put this out a lot of you know perfume companies approached us because they were interested.

**中文**

我还把它与人工调配进行了比较。我们实际上找来了一些专业调香师，他们以研究气味及其混合为业。给定一种物质，他们会混合不同液体和香水，重现它的气味。我们比较了这种 AI 方法与人工混合这些 maps \[字幕含义不明\] 的方法。显然，有些情况下人做得更好。但就节省的时间和精力而言，AI 帮助很大。我们发布这项工作之后，很多香水公司找到了我们，因为他们很感兴趣。

### [27:06](https://www.youtube.com/watch?v=UJra8aMCHXg&t=1626s) · b000030

**English**

Any other questions? Um I want to cover some also very exciting work. This is from colleague Jaz Brooks who is joining MIT in the fall as faculty and he is approaching this from the HCI that is intelligent with AI embedded inside of it to further modulate different human senses. So he's done work in smell, taste, temperature uh which I'll briefly cover. So, one thing that we just showed was aroma, the approach that we did, which actually delivers smell sensations basically with chemicals, right? You actually have to have a canister of a certain oil and different types of oils and they actually released to your nose. So, it's going through the natural pathway of how people smell. It requires chemicals. The major downside, of course, is that these are actual liquids. It may not be super portable and it may be bulky sometimes. So it's actually a very exciting line of work where you could deliver smell

**中文**

还有其他问题吗？嗯，我还想介绍一些同样令人兴奋的工作。这来自同事 Jaz Brooks，他今年秋天将加入 MIT 任教。他从人机交互（HCI）的角度切入，让它具备智能，并在其中嵌入 AI，进一步调节人的不同感官。他做过嗅觉、味觉、温度方面的工作，我会简要介绍。我们刚刚展示的一种方法是 aroma，也就是我们做的方法，基本上通过化学物质传递嗅觉感受，对吧？你确实需要装有某种油以及不同类型油的小罐子，实际把它们释放到鼻子里。这走的是人闻到气味的自然路径，需要化学物质。主要缺点当然是它们是真实液体，可能不那么便携，有时也会很笨重。所以有一条非常令人兴奋的研究路线，可以在

### [28:02](https://www.youtube.com/watch?v=UJra8aMCHXg&t=1682s) · b000031

**English**

sensations without chemicals, without actual gases and smells and spices. And that can be done by simulating this trigeminal nerve, something that biologists studied. Most of you probably have heard of theactory bulb, which is kind of deep inside your nose, and that's where smell is actually being processed. But a trigeminal nerve which is at the opening of the nose is actually a nerve that connects to the factory ball. So by delivering precise electrical stimulations to this nerve, you can actually induce a smell that a person will perceive. Okay. Uh so for example, if you're sniffing vinegar, it's not that a vinegar actually goes into theactory bulb. It's the fact that the vinegar as chemicals it stimulates the trigeminal nerve which is the opening of the nose that delivers some reaction and electrically or goes through your nervous system and is sent

**中文**

没有化学物质、没有实际气体、气味和香料的情况下传递嗅觉感受。这可以通过模拟三叉神经（trigeminal nerve）来实现，这是生物学家研究的东西。大多数人可能听说过 theactory bulb \[字幕疑误，可能指 olfactory bulb，嗅球\]，它在鼻子深处，是实际处理气味的地方。但鼻孔开口处的 trigeminal nerve 实际上是一条连接到 factory ball \[字幕疑误，可能指 olfactory bulb\] 的神经。因此，通过对这条神经施加精确的电刺激（electrical stimulations），你实际上可以诱发一种人能感知到的气味。好。比如你在闻醋，并不是醋真的进入 theactory bulb \[字幕疑误，可能指 olfactory bulb\]，而是醋作为化学物质刺激鼻孔开口处的 trigeminal nerve，产生某种反应，以电的形式，或者通过神经系统，被发送

### [28:57](https://www.youtube.com/watch?v=UJra8aMCHXg&t=1737s) · b000032

**English**

to the bulb. So they've developed this approach which you can essentially wear as a nose clip very interesting small nose clip that is positioned exactly to simulate this um trigeminal nerve at the opening of the nose. So there's like two magnets. The two circular things are magnets. You you put it through your nose and it clips on. And then some of these are little little circuit boards that uh have electrodes that stimulate the trigeminal nerve. And if you program this correctly, it's actually really amazing that it can release small pulsive electrical stimulations um that can allow you to basically smell different things. Faux system, you know, talk to Jazz when he comes. He'll be a co-instructor or guest lecture for this course next year. Um, but I'm not going to go through all of his slides. They're quite complicated, right? Some complications

**中文**

到嗅球。所以他们开发了这种方法，你基本上可以像鼻夹一样戴着它，是一个非常有趣的小鼻夹，佩戴位置正好位于鼻孔开口处，可对三叉神经（trigeminal nerve）进行刺激 \[原字幕 simulate 疑为 stimulate\]。这里有两个磁铁，那两个圆形的东西是磁铁。你把它穿过鼻子，它就夹住了。然后其中一些是小电路板，带有刺激 trigeminal nerve 的电极。如果编程正确，真的很神奇，它可以释放小的脉冲电刺激，基本上让你闻到不同东西。Faux system \[字幕含义不明\]，你知道，等 Jazz 来了可以和他聊聊。明年他会成为这门课的共同授课教师或客座讲师。不过我不会逐一讲他的所有幻灯片，它们相当复杂，对吧？这里的一些复杂之处

### [29:54](https://www.youtube.com/watch?v=UJra8aMCHXg&t=1794s) · b000033

**English**

here are modeling the airflow. In order to make it really precise, you literally have to use some computer graphics to model the airflow of the room. You need to track where your head poses because depending on different head pose, you actually have to release the electrical stimulation differently. for left and right because our smell is very spatial, right? You can actually smell left and right to recreate that spatial sensation. You actually have to perform left and right um stimulation differently, right? So all of that are just different factors, different conditionals that go in to tell you what is the right electrical stimulation uh and the intensity and the duration to stimulate. All of this has some lots of work that gone into this, but eventually it gets sent via Bluetooth to your the thing that you're wearing on the nose. And another key part is that it has to be synchronized to your breathing rate.

**中文**

在于气流建模。为了做到非常精确，你实际上必须使用一些计算机图形学（computer graphics）方法来模拟房间里的气流。你需要跟踪头部姿态（head pose），因为根据不同的 head pose，实际上必须以不同方式对左右两侧施加电刺激，因为我们的嗅觉非常具有空间性，对吧？你确实可以闻出左右，为了重建那种空间感受，左右两边的刺激必须不同，对吧？所有这些都是不同因素、不同条件，输入进去告诉你什么是正确的电刺激，以及刺激的强度和时长。这其中投入了大量工作，但最终它会通过 Bluetooth 发送到你戴在鼻子上的东西。另一个关键点是它必须与你的呼吸频率同步。

### [30:52](https://www.youtube.com/watch?v=UJra8aMCHXg&t=1852s) · b000034

**English**

So you want to stimulate it as the person is breathing in. Also a very interesting finding. So you have to measure the breathing rate by extracting a respiratory signal uh which can be done and then stimulating at a precise environment where someone breathes in. So looks very simple intuitive but actually quite quite complicated. Uh and the exact way that the electrical stimulation is done and it's through a lookup table. So there are people who are studying this trigeminal nerve. So they distilled different electrical patterns that map to different smells of foods. So right now it's still a lookup table right when you want to smell this thing it looks up the right electrical waveform and then you modify it based on all these other factors like left right you know air flow breathing rate uh but it's still a lookup table so one natural question is that you know to go beyond a lookup table beyond a dictionary uh you

**中文**

所以要在人吸气时施加刺激。这也是一个很有趣的发现。因此必须通过提取呼吸信号（respiratory signal）来测量呼吸频率，这是可以做到的，然后在人吸气的精确环境下进行刺激。看起来很简单、直观，但实际上相当复杂。呃，电刺激的具体方式是通过查找表（lookup table）来确定的。有些人在研究这条 trigeminal nerve，他们提炼出不同的电模式，对应不同食物的气味。所以目前它仍然是一个 lookup table，对吧？当你想闻这个东西时，它就查找正确的电波形（electrical waveform），然后根据其他因素，比如左右、气流、呼吸频率进行修改。但它仍然是 lookup table，所以一个很自然的问题是，如何超越 lookup table、超越字典，你

### [31:47](https://www.youtube.com/watch?v=UJra8aMCHXg&t=1907s) · b000035

**English**

can start using AI right where the AI model takes in a smell and it predicts what is the right electrical waveform and then sent to the nose to to stimulate it, which I think is super exciting, but of course very scary. In case something goes wrong, then you say goodbye to your nose. Yeah. Okay. And and they actually find that um this, you know, when users try this out, they can actually well these are mostly evaluated through user studies, right? You actually smell the substance like a real real food and then you wear this nose clip and you smell the recreation and that actually that actually works.

**中文**

可以开始使用 AI，对吧？AI 模型接收一种气味，预测正确的 electrical waveform，然后发送到鼻子来进行刺激。我认为这非常令人兴奋，但当然也很吓人。万一出什么问题，你就得跟鼻子说再见了。是的，好。他们实际上发现，用户试用时确实可以……这些主要通过用户研究（user studies）来评估，对吧？你实际闻一下某种物质，比如真正的食物，然后戴上鼻夹，闻重建出来的气味，这确实、确实有效。

### [32:31](https://www.youtube.com/watch?v=UJra8aMCHXg&t=1951s) · b000036

**English**

Any other questions about smell before I move on a taste? Yeah.&gt;&gt; Much transference is there from like the world of spatial audio.&gt;&gt; Great question. Um so some of this left right order concentration estimation remember when jazz was giving his job talk here you actually did use quite a bit of techniques from from um not spatial audio but from computer graphics right because that's another area where you need kind of spatial continuity when you generate generate um you know images so they do do quite a quite a bit of this yeah specifically in the details I'm not super So taste of course another exciting modality where where you could potentially use AI and

**中文**

在我转到味觉之前，关于嗅觉还有问题吗？是的。&gt;&gt;从空间音频（spatial audio）领域能迁移多少东西过来？&gt;&gt;好问题。嗯，关于一些左右 order 浓度估计 \[字幕疑误，order 可能指 odor，气味\]，我记得 Jazz 在这里做求职报告时，确实使用了不少技术，不是来自 spatial audio，而是来自 computer graphics，对吧？因为那也是一个在生成图像时需要某种空间连续性（spatial continuity）的领域。所以他们确实用了相当多这方面的方法。是的，具体细节我不是特别……那么味觉当然是另一个令人兴奋的模态，可以用 AI 和

### [33:26](https://www.youtube.com/watch?v=UJra8aMCHXg&t=2006s) · b000037

**English**

interactive systems to modulate how we taste different substances. So there are a lot of approaches \[snorts\] for taste. Um you see from this from this you know overview here anything that you know you put food inside for example a coffee machine spoon all sorts of spoons glasses cups uh you know modifying the food itself right by adding different chemicals by adding different compounds you know people have done all sorts of things to uh to modify taste based on changing of food and also changing the the the medium in which food is delivered into your mouth. But all of this is actually before eating. If you think about it, all of this only modifies the food or the medium, the cup, the spoon, all of this modifies before eating, right? Before the food actually goes into your mouth. Well, one issue of that is that taste is actually

**中文**

交互系统来调节我们如何品尝不同物质。所以味觉方面有很多方法。\[哼鼻声\] 嗯，从这里这张概览图能看到，任何放食物的东西，比如咖啡机、勺子、各种勺子、玻璃杯、杯子；也可以通过加入不同化学物质、不同化合物来修改食物本身。人们做了各种各样的尝试，通过改变食物，以及改变把食物送入口中的媒介来修改味觉。但这些实际上都发生在进食之前。想一想，所有这些只是在修改食物或媒介，杯子、勺子，都是在进食之前修改，对吧？在食物真正进入嘴巴之前。这里有个问题，味觉实际上是在

### [34:22](https://www.youtube.com/watch?v=UJra8aMCHXg&t=2062s) · b000038

**English**

perceived inside the mouth. So if you want to perform high resolution and actually accurate timely modification of taste, it has to actually modify things inside the mouth. actually very challenging because if you're chewing and you're opening and closing your mouth actually very difficult to build uh intelligent systems that go inside the mouth and there's several other technical challenges that Jazz wrote here as well you can see the notes in the slides that I put online which is uh the saliva is very val variable it's very subjective there's not a lot of space inside your mouth to actually make a lot of modifications um so how can you actually develop systems that you know modify taste not just before eating modifying the food or the soup but actually modify it during eating right when you're actually chewing in between chews after you're swallowing and modify the aftertaste. Uh that would really give very high precise sensory experiences of modifying taste.

**中文**

口腔内部感知的。所以如果你想进行高分辨率、真正准确且及时的味觉修改，就必须实际改变口腔内部的东西。这非常有挑战性，因为你在咀嚼、张嘴闭嘴，要构建进入嘴巴内部的智能系统真的很困难。Jazz 在这里还写了其他一些技术挑战，你可以看我放到网上的幻灯片备注，比如唾液变化很大，非常主观，嘴里也没有太多空间进行大量修改。那如何开发系统来修改味觉，不只是在吃之前修改食物或汤，而是在吃的过程中修改，对吧？在咀嚼时、两次咀嚼之间、吞咽之后，修改余味（aftertaste）。那确实能带来非常精确的味觉修改感官体验。

### [35:16](https://www.youtube.com/watch?v=UJra8aMCHXg&t=2116s) · b000039

**English**

So this is again a very cute approach where you have something that's wearable on the back of your head and this delivers into your mouth through little tubes that is sent to the left and right of your mouth and this allows you to develop a system that modifies the perception of taste directly during eating. So I'll play this video quickly. So it directly delivers a taste modulator into their mouth and there's several chemicals in the back and it's sent through this tube uh through some you know intelligent AI that's controlling it you know directly into the mouth. So you can actually taste different things in between different chews and in between different swallows. So one very cool application is that maybe you are trying to go on a diet so you like drinking Coke and you can actually have this app on your phone that can has a slider for sweetness. You can increase the sweetness or decrease the sweetness. So if you drink Coke, you program the system to decrease the

**中文**

所以这又是一个很可爱的方法，在后脑勺戴一个设备，通过送到嘴巴左右两侧的小管子，将东西送入口中，让你构建一个在进食过程中直接修改味觉感知的系统。我快速播放一下这个视频。它直接把味觉调节剂（taste modulator）送入嘴里，后面有几种化学物质，通过管子，在某种智能 AI 的控制下，直接送入口腔。所以你实际上可以在不同的咀嚼之间、不同的吞咽之间尝到不同东西。一个很酷的应用是，也许你正在尝试节食，又喜欢喝 Coke。你可以在手机上装一个带甜度滑块的应用，增加或降低甜度。如果你喝 Coke，就把系统编程为降低

### [36:13](https://www.youtube.com/watch?v=UJra8aMCHXg&t=2173s) · b000040

**English**

sweetness that's delivered into your mouth. You feel ah this is gross and then you throw away the Coke. So that helps you save up of some calories. Um they try to experiment in VR where you can just, you know, VR you want to make immersive experiences where people are actually eating things, but you don't want to have all different fruits and vegetables that you have to give to people to eat. So you just want to start with one. For example, a blackberry. So if you just don't modify anything, they just taste a blackberry. But what if you want the person to physically eat a blackberry, but to get a sensation that they're eating an a lemon, right? In the in the VR system. So you can take whatever the person is eating and then you program it to decrease sweetness. So you take the sweet and sour of the blackberry, remove the sweetness, you get something sour like lemon. You can modify the sour into sweet using a different type of um of liquid chemical and you can get the sensation of a

**中文**

送入口中的甜度。你觉得，啊，这真难喝，然后把 Coke 扔掉。这样就帮你少摄入一些热量。他们尝试在虚拟现实（VR）中做实验，你希望在 VR 里创造沉浸式体验，让人真正吃东西，但又不希望必须准备各种不同的水果蔬菜给人吃，所以只想从一种开始，比如黑莓。如果什么都不改，他们尝到的就是黑莓。但如果你想让人实际上吃黑莓，却在 VR 系统中感觉自己吃的是柠檬呢？你可以拿人正在吃的东西，编程让它降低甜度。把黑莓的酸甜味去掉甜味，就得到像柠檬一样酸的东西。也可以使用另一种液体化学物质把酸味变成甜味，得到

### [37:08](https://www.youtube.com/watch?v=UJra8aMCHXg&t=2228s) · b000041

**English**

strawberry. And you can do other weird and crazy things like you know getting apples, getting different types of coffees and you know removing umami, adding bitter, removing bitter and so on. Yeah. which person sees it sends a signal to the sensor to get the&gt;&gt; um it could everything that that they've done here is mostly hardcoded right so is that if statements there's no um there's no AI yet it's more you want to decrease the sweetness by this amount then you would release that substance which is kind of a sweetness suppressor um but but that's the opportunity right you know I think a really good opportunity is let's You could use a VLM that's actually seeing what the the physical scene is and then in real time it is able to to maybe generate right based on a person's attention what they're looking at it could generate uh the right intervention.

**中文**

草莓的感觉。还可以做其他奇怪而疯狂的事情，比如得到苹果、不同种类的咖啡，去掉鲜味（umami）、增加苦味、去掉苦味，等等。是的。哪个人看到它，就向传感器发送信号来得到……&gt;&gt;嗯，可以，他们在这里做的一切大多是硬编码（hardcoded）的，对吧？就是 if 语句，还没有 AI。更多是你想把甜度降低这么多，就释放那种物质，它相当于一种甜味抑制剂。不过这就是机会，对吧？我认为一个很好的机会是，我们可以用视觉语言模型（VLM）实际观察物理场景，然后实时地，也许根据一个人的注意力、他们正在看的东西，生成合适的干预（intervention）。

### [38:08](https://www.youtube.com/watch?v=UJra8aMCHXg&t=2288s) · b000042

**English**

Any other questions? So very cool. You know, in theory, the person could be doing all sorts of all sorts of things in the in the in the experience, but you know, in this case, you can just compress it to three props, right? One blueberry, one apple, and maybe one one milk. So, that saves a lot of time and engineering effort. But yeah, I think, you know, having truly integrating intelligence AI into this will allow it to really generate anything, right? That's the difference between generating anything and just programming it to generate only the sensation of a couple of fruits.

**中文**

还有其他问题吗？所以非常酷。理论上，人可以在体验里做各种各样的事，但这里可以把它压缩成三个道具，对吧？一颗蓝莓、一个苹果，也许再来一份牛奶。这样节省了很多时间和工程工作。不过，是的，我认为真正把智能 AI 整合进来，就能让它真正生成任何东西，对吧？这就是生成任何东西，与只把它编程成生成几种水果的感觉之间的区别。

### [38:44](https://www.youtube.com/watch?v=UJra8aMCHXg&t=2324s) · b000043

**English**

And these are things that you can look up more if you're interested. These are these are well-known chemicals that can increase the perception of sweetness or mask out sweetness and and other other taste profiles. All right, one final thing. Um, temperature temperature is also a critical component of many immersive experiences. So, if you want to imagining you're you're playing a game or the environment where it's really hot versus very cold, you want to be able to feel that sensation. So, traditionally people did this using like actual, you know, heat lamps, right? You could have a ton of heat lamps that was around you and that give you obviously the physical temperature would increase and you would feel hotter. Or you could have a bunch of your ACs and the physical temperature would decrease and you would feel cooler. Uh but naturally these are very high power they actually modify the

**中文**

这些东西，如果感兴趣可以进一步查阅。它们都是众所周知的化学物质，可以增加甜味感知，或者掩盖甜味以及其他味觉特征。好，最后一件事。嗯，温度，温度也是许多沉浸式体验的关键组成部分。如果你想，想象自己正在玩游戏，或者身处一个很热或很冷的环境，你希望能感受到那种感觉。传统上，人们用真实的加热灯之类的东西来实现，对吧？可以在周围放很多加热灯，显然物理温度会上升，你会觉得更热。也可以放很多空调，物理温度下降，你会觉得更凉。不过自然，这些功耗都很高，因为它们实际上改变了

### [39:42](https://www.youtube.com/watch?v=UJra8aMCHXg&t=2382s) · b000044

**English**

temperature and that's why you use so much high power and they're not very wearable and efficient. So is there a fundamentally different approach to this? Well, this is a paper that they did called trigeminal based temperature illusions. So, it again um deals with the trigeminal nerve which as we're talking about oraction is a nerve in the nose. And in fact, if you simulate the nose in the right way, you can actually feel more hot or more cool without actually changing the temperature around you. Right? So again there's you know chemists have found that this nerve inside of you you know it's there some chemistry you can put some chemical simulation to that nerve and it would allow you to perceive changes in temperature and what are these chemicals well you know what they are one is spicy food and one is uh

**中文**

温度，所以才需要这么高的功率，而且不太适合穿戴，也不高效。那么有没有一种根本不同的方法？这就是他们的一篇论文，叫 trigeminal based temperature illusions，基于三叉神经的温度错觉。它同样涉及 trigeminal nerve，也就是我们谈到 oraction \[字幕疑误，可能指 olfaction，嗅觉\] 时说的鼻子里的神经。事实上，如果用正确的方式模拟鼻子，你可以在不改变周围温度的情况下，实际感到更热或更凉。对吧？同样，化学家发现，你体内这条神经，有一些化学作用，你可以对它进行某种化学模拟，就能让你感知温度变化。这些化学物质是什么呢？你们知道，一种是辛辣食物，另一种是，呃，

### [40:35](https://www.youtube.com/watch?v=UJra8aMCHXg&t=2435s) · b000045

**English**

minty minty so capsic for spicy or hot sauce and um things like eucalypt mints basically Right? That's why you feel really hot when you eat things that are spicy and you feel really cool when you eat a mint. So you can render the cool winds by emitting eucalypt directly if you emit it directly into your nose and you stimulate the nerve at a very precise location. You can actually feel a very strong cooling sensation. And likewise, if you want to go into a hot area, you release a little puff of capsic um capsic and you know when delivered right, you will also feel a hot sensation. Okay, but with that key idea, I think the rest really follows. So you have some environment and it's programmed to modify the temperature in a certain way.

**中文**

薄荷、薄荷味的东西，所以辛辣或辣酱对应 capsic \[字幕疑误，可能指 capsaicin，辣椒素\]，还有 eucalypt \[字幕疑误，可能指 eucalyptol，桉叶油醇\]、薄荷之类的东西，基本上就是这样，对吧？这就是为什么吃辛辣的东西会觉得很热，吃薄荷糖会觉得很凉。所以你可以通过直接释放 eucalypt 来呈现凉风，如果把它直接释放到鼻子里，在非常精确的位置刺激神经，你实际上能感受到非常强烈的清凉感。同样，如果想进入一个炎热区域，就释放一小股 capsic，嗯，capsic；如果传递方式正确，你也会感到热。好，有了这个关键想法，我觉得剩下的都顺理成章了。你有一个环境，并把它编程成以某种方式改变温度。

### [41:30](https://www.youtube.com/watch?v=UJra8aMCHXg&t=2490s) · b000046

**English**

So that goes into this this timer which then can you know it's a wearable timer which you can then release a schedule of a little peak of you know one substance capsic for hot and another puff another substance eucalyptal for cooling sensation and they show that you can get by by just using one uh microl very little less than a milliliter so microl liter of that liquid is enough to give you that sensation. Right. So, here's the video that you've already seen. You know, in a cool environment, you would release one liquid and in a hot environment, you release something else.

**中文**

然后它进入这个计时器，这是一个可穿戴计时器，接着你可以按时间表释放一点某种物质，capsic \[字幕疑误，可能指 capsaicin，辣椒素\] 用来产生热感，再释放一股另一种物质 eucalyptal \[字幕疑误，可能指 eucalyptol，桉叶油醇\] 来产生凉感。他们展示，只需要一 microl，非常少，不到一毫升，也就是一微升（microl liter）的这种液体，就足以带来那种感觉。对。这是大家已经看过的视频。在凉爽环境中释放一种液体，在炎热环境中释放另一种。

### [42:22](https://www.youtube.com/watch?v=UJra8aMCHXg&t=2542s) · b000047

**English**

Great. So, all of these follow very similar ideas, right? allowing us to build AI systems that interface with our bodies in different ways. We started with smell where smell sensing and then we moved to smell generation with actual liquid chemicals. Right? So the question there was how could you decompose all sorts of foods and beverages using these multimodal LLM into a base set of these liquid chemicals and then can be released to recreate that substance. And then we went into some of these u these these approaches that really start looking at human biology where instead of releasing liquid chemicals you could stimulate the nerve that's responsible for oldaction using some of the electrical stimulants. Uh so you saw the smell taste going into the mouth and also temperature uh different ways of retargeting the nerve to allow us to feel different sensations.

**中文**

很好。所以所有这些都遵循非常相似的思路，对吧？让我们构建以不同方式与身体连接的 AI 系统。我们从嗅觉开始，先是气味感知，然后是使用真实液体化学物质进行气味生成。对吧？问题在于，如何利用这些 multimodal LLM，把各种食物和饮料分解成一组基础液体化学物质，再通过释放它们来重建那种物质。之后我们介绍了这些真正开始关注人体生物学的方法，不释放液体化学物质，而是使用电刺激来刺激负责 oldaction \[字幕疑误，可能指 olfaction，嗅觉\] 的神经。所以你看到了嗅觉、进入口腔的味觉，还有温度，用不同方式重新针对神经，让我们产生不同感受。

### [43:17](https://www.youtube.com/watch?v=UJra8aMCHXg&t=2597s) · b000048

**English**

Uh so I think it's a cool example of combining intelligence with wearables and leading to h new interesting experiences for people. Um but at the same time not a lot of AI has been integrated into these things. So lots of opportunities. All right. Any further questions?

**中文**

呃，我认为这是把智能与可穿戴设备结合，为人们带来有趣新体验的一个很酷的例子。不过与此同时，这些东西中还没有整合太多 AI，所以有很多机会。好，还有其他问题吗？

### [43:42](https://www.youtube.com/watch?v=UJra8aMCHXg&t=2622s) · b000049

**English**

Who finds this exciting? Who finds it scary and very dangerous?&gt;&gt; I think for me it's, you know, people are already um really plugged in the sound. So I imagine like what other ways will we like mask ourselves from the environment?&gt;&gt; Like do we always want to smell the roses?&gt;&gt; And maybe Yeah, that isn't super awesome.&gt;&gt; Yeah.&gt;&gt; And it kind of would. But&gt;&gt; so how how would you extend this and how would you how would you deploy this in your ideal world? I feel like it's the same thing with like choosing what not to engage in. I think they're being wearable. It's like pretty suffers from the same positive.&gt;&gt; Yeah. Any other thoughts? How would you all maybe extend this, you know, combining AI into this, making it more general, and what how would you deploy this?

**中文**

谁觉得这令人兴奋？谁觉得这很吓人、很危险？&gt;&gt;我觉得对我来说，人们已经非常沉浸在声音里了。所以我在想，我们还会以哪些方式把自己与环境隔开？&gt;&gt;比如，我们是否总想闻到玫瑰香？&gt;&gt;也许，是的，那并不是特别棒。&gt;&gt;是的。&gt;&gt;而且它多少会。但……&gt;&gt;那么你会如何扩展这个，在你理想的世界里会如何部署它？我觉得这和选择不参与什么是同一回事。我认为它们是可穿戴的，就像相当程度上也受到相同积极因素的影响。&gt;&gt;是的。还有其他想法吗？你们会如何扩展它，比如把 AI 结合进来，让它更通用，以及会如何部署它？

### [44:42](https://www.youtube.com/watch?v=UJra8aMCHXg&t=2682s) · b000050

**English**

What do you think? I think it's really cool, but I gota get the right the Ray brand short story.&gt;&gt; Sorry, what is that?&gt;&gt; Explain more.&gt;&gt; There's like some short story where like they have a room that's like it can see Safari like exactly it's it's kind of like step. All

**中文**

你觉得呢？我觉得它很酷，但我得找对那个 Ray brand 短篇小说 \[字幕疑误，可能指 Ray Bradbury\]。&gt;&gt;抱歉，那是什么？&gt;&gt;再解释一下。&gt;&gt;有个短篇小说，里面有个房间，可以看到 Safari，就像完全一样，有点像 step。好

### [45:16](https://www.youtube.com/watch?v=UJra8aMCHXg&t=2716s) · b000051

**English**

right.

**中文**

的。

### [45:26](https://www.youtube.com/watch?v=UJra8aMCHXg&t=2726s) · b000052

**English**

Okay. So, um let's get some of these slides.

**中文**

好。那么，嗯，我们来看一些幻灯片。

### [45:37](https://www.youtube.com/watch?v=UJra8aMCHXg&t=2737s) · b000053

**English**

All right. Uh so one thing I also want to discuss you know we've been doing a lot of work in capture a sense of touch that's also a very interesting modality. Uh so over here you know the primarily we're building these sensors that can allow you to wear gloves that capture the sense of touch. Um these are based on PSO resistive sensing. So anytime you push your hand against something and you feel pressure uh the gloves will get pushed closer to each other. And when two layers of circuits are being pushed closer to each other uh their resistance between them increases. So that's how you get a sensor reading from them. And the question really becomes how many of these sensors can you put right our fingertips are extremely sensitive. Our palms are very sensitive but less sensitive. So question is how many of these you know sensors can you pack into uh square centimeter and also how often can these tactile sensors give you uh

**中文**

好。呃，我还想讨论的一件事是，我们一直在做很多捕捉触觉的工作，这也是一种非常有趣的模态。在这里，我们主要构建传感器，让你能戴上捕捉触觉的手套。它们基于 PSO resistive sensing \[字幕疑误，可能指 piezoresistive sensing，压阻式感知\]。每当你把手按向某个东西，感受到压力，手套就会被压得更靠近。当两层电路被压得更靠近时，它们之间的电阻会增加。你就是这样获得传感器读数的。问题就变成了，你能放多少个这样的传感器，对吧？我们的指尖极其敏感，手掌也很敏感，但没那么敏感。所以问题是，每平方厘米能塞进多少这样的传感器，以及这些触觉传感器能够以多高的频率提供

### [46:34](https://www.youtube.com/watch?v=UJra8aMCHXg&t=2794s) · b000054

**English**

log information right so basically the spatial and temporal resolution of these sensors so it built some really powerful fingertip sensors that can be up to 30 by 30 just on your fingertips so very high resolution and running at uh more than 100 uh hertz right and for vision most of the vision visual video information that we get is 30 Hz. So 100 Hz means three times faster than vision. So this is going to be extremely important for robots that can essentially use vision to manipulate objects but also use touch as a very quick reactive sensory channel in order to manipulate objects. You know if they something slips, how do you quickly react and pick it back? These are all examples of where touch is really important and where vision is just too slow to uh make a decisive action.

**中文**

记录信息，对吧？基本上就是传感器的空间和时间分辨率（spatial and temporal resolution）。所以做了一些非常强大的指尖传感器，仅在指尖就能达到 30 × 30，分辨率很高，而且运行频率超过 100 赫兹，对吧？视觉方面，我们获得的大多数视觉视频信息是 30 Hz。所以 100 Hz 意味着比视觉快三倍。这对机器人会极其重要，它们基本上可以用视觉操纵物体，同时也把触觉作为一个反应非常快的感知通道来操纵物体。比如东西滑落了，如何迅速反应并把它抓回来？这些都是触觉非常重要，而视觉太慢、无法采取果断行动的例子。

### [47:28](https://www.youtube.com/watch?v=UJra8aMCHXg&t=2848s) · b000055

**English**

So you might have seen this uh so we created some very large data sets. Uh the next frontier for a lot of these multimodal approaches will be for the physical world. So approaches that are able to uh fuse information from vision. So egocentric vision especially. So what people and what robots are seeing about the world uh with audio spatial audio and with other types of physical information like in this case about touch. So over here you see that the modalities are very synchronized right you see vision you see where people are pressing and you see the corresponding tactile pressure uh being lit up the regions where a person is pressing. So, Open Touch is a large data set we created for this that contains touch information, visual information of people doing all sorts of activities in all sorts of places and with also 3D hand post. So, that tells you exactly how the hand is moving. So, you could think about training robotic hands with

**中文**

你们可能见过这个。我们创建了一些非常大的数据集。这些多模态方法的下一个前沿将是物理世界，也就是能够融合视觉信息的方法，尤其是第一人称视觉（egocentric vision），也就是人和机器人看到的世界，与音频、spatial audio，以及其他类型的物理信息，比如这里的触觉相结合。这里可以看到，模态之间非常同步，对吧？你看到视觉，看到人在按哪里，也看到相应的触觉压力，人在按压的区域会亮起来。所以 Open Touch 是我们为此创建的一个大型数据集，包含人们在各种地方进行各种活动时的触觉信息、视觉信息，还有 3D hand post \[字幕疑误，可能指 3D hand pose，三维手部姿态\]。它会准确告诉你手如何移动。所以你可以考虑通过

### [48:25](https://www.youtube.com/watch?v=UJra8aMCHXg&t=2905s) · b000056

**English**

imitation learning to essentially copy how these people are interacting with different objects.

**中文**

模仿学习（imitation learning）来训练机器人手，基本上复制这些人与不同物体交互的方式。

### [48:38](https://www.youtube.com/watch?v=UJra8aMCHXg&t=2918s) · b000057

**English**

All right.

**中文**

好。

### [48:48](https://www.youtube.com/watch?v=UJra8aMCHXg&t=2928s) · b000058

**English**

Okay. Those are all the slides that I've mostly prepared. Um hopefully that was that was interesting. Uh covering kind of very very different from what you know we've we've typically seen, right? going from language, vision, audio, but to some of these other human senses. How do you build AI to to perceive these senses? How do you build it to interact and generate data of these senses so that people actually feel new experiences? Uh but as a core, you know, I just want to again bring it back to this to this image. This is kind of the loop which I see encapsulating most of these AI systems, right? They should be able to sense all different modalities. We talked about language video audio for most of the class but you know we also can build systems for smell and for touch ways of sensing these models should learn representations that synchronize them and then when it's outputting we've seen examples of obviously outputting

**中文**

好。这些基本上就是我准备的所有幻灯片。希望这些内容有意思。介绍的东西和我们通常见到的很不一样，对吧？从语言、视觉、音频，转向其他一些人类感官。如何构建 AI 来感知这些感官？如何构建它来交互，并生成这些感官的数据，让人真正获得新体验？不过从核心上说，我还是想回到这张图。这是我认为概括了大多数 AI 系统的循环，对吧？它们应该能够感知各种不同模态。课程的大部分时间我们讨论的是语言、视频、音频，但我们也可以构建嗅觉和触觉系统、感知方式。这些模型应当学习让它们同步的表征，然后在输出时，我们显然见过输出

### [49:45](https://www.youtube.com/watch?v=UJra8aMCHXg&t=2985s) · b000059

**English**

language and images but now you're looking examples of generating smell or generating taste and temperature sensations right and this could go on across multiple steps depending on how long the interaction is with a user or how difficult the problem is decomposing it over multiple steps right um so yes I'll be here we can you know ask any questions about this lecture about any previous lectures about research in general um if you want any feedback about your projects we can also discuss that right thanks everyone

**中文**

语言和图像的例子，但现在你看到的是生成气味，或生成味觉与温度感受的例子，对吧？这个过程可以跨多个步骤持续进行，取决于与用户交互的时间有多长，或者问题有多难，把它分解到多个步骤中，对吧？嗯，所以，是的，我会留在这里，大家可以问关于这堂课、之前任何一堂课，或一般研究方面的问题。如果你想获得项目反馈，我们也可以讨论。好，谢谢大家。
