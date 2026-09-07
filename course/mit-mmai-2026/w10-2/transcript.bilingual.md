# Lecture 11 – Cross-Modal Transfer (MIT How to AI Almost Anything/Multimodal AI, Spring 2026)

_Bilingual transcript · 双语讲稿_

- Channel: Paul Liang
- Source: [YouTube](https://www.youtube.com/watch?v=IDaMEG_zY6A)
- Duration: 1:08:37
- Caption source: automatic
- Status: complete
- Chinese translation: 83/83
- Translation provider: codex
- Generated: 2026-09-07T07:59:05+00:00

## Transcript · 讲稿

### [00:01](https://www.youtube.com/watch?v=IDaMEG_zY6A&t=1s) · b000001

**English**

All right folks, welcome back. So uh today we'll be talking about uh crossmodal transfer last lecture on foundational and core concepts and then rest of the lectures will mostly be about application oriented topics. Uh midterm results and grades have been released and um the homework should also be up today and due in one and a half weeks and thanks everyone for submitting their uh midterm report. We'll look through those and give you all feedback in the next week or so as you prepare for the final reports. All right. So crossodal transfer um as an overview we will discuss the basics of crossodal transfer and we'll show how crossodal transfer can be achieved via three different approaches fusion based

**中文**

好了，各位，欢迎回来。那么，呃，今天我们要讲跨模态迁移（crossmodal transfer），这是基础和核心概念的最后一讲，之后的课程大多会讨论面向应用的话题。呃，期中考试结果和成绩已经公布，作业应该也会在今天发布，一周半后截止。感谢大家提交期中报告。我们会阅读这些报告，在接下来一周左右给大家反馈，帮助你们准备最终报告。好了。那么，crossodal transfer \[字幕疑误，可能指 crossmodal transfer\]，概括来说，我们会讨论它的基础，并展示如何通过三种不同的方法实现：基于融合（fusion）的

### [00:57](https://www.youtube.com/watch?v=IDaMEG_zY6A&t=57s) · b000002

**English**

approaches alignment based approaches and translation based approaches. So at a high level what is crossodal transfer? Crossodal transfer or transference aims to transfer knowledge between modalities usually from a primary modality to a secondary modality where the one that you really care about has a very limited resources or very noisy or lots of missing data. So one way is you know if you care about making some prediction in this primary modality let's say medical images right it's very difficult to get medical images it's very difficult to get them annotated there's privacy concerns you get a lot of data how can you use natural images as a way of helping transfer information towards a task that you care about more broadly how can you even use things like medical textbooks largecale databases that are not exactly in a domain of the task that you care

**中文**

方法、基于对齐（alignment）的方法，以及基于翻译（translation）的方法。那么，从整体上说，什么是 crossodal transfer \[字幕疑误，可能指 crossmodal transfer\]？Crossodal transfer 或 transference 旨在模态之间迁移知识，通常是从一个主要模态迁移到一个次要模态，其中你真正关心的那个模态资源非常有限，或者噪声很大，或者有大量缺失数据。一种情况是，如果你关心在这个主要模态上进行某种预测，比如医学图像，对吧，医学图像很难获取，也很难标注，还存在隐私问题。你得到大量数据，怎样利用自然图像来帮助把信息迁移到你关心的任务上？更广泛地说，你甚至怎样利用医学教科书、大规模数据库这类东西，它们并不完全处于你关心的任务领域

### [01:54](https://www.youtube.com/watch?v=IDaMEG_zY6A&t=114s) · b000003

**English**

about but for where there is some overlap in information and with transfer is possible. Right? So we call that transfer learning or transferring knowledge. That's one way of achieving crossodal transfer. Another way of achieving cross modal transfer is through this idea of co-learning. Co-learning basically means again you have this modality that you care about making predictions in. Can I use some extra information to train the model with an input or some extra information to train my model as a prediction target in the output? Right? So you see I use a I use dotted lines over here to indicate the fact that this extra modality is provided during training either as an extra input signal or as an extra prediction target during training. But during testing and during inference, you still only have this primary modality that you care about, right? That makes it fair to compare to other approaches during testing. Right?

**中文**

之内，但其中的信息存在某种重叠，因此有可能进行迁移，对吧？我们称之为迁移学习（transfer learning），或者知识迁移。这是实现 crossodal transfer \[字幕疑误，可能指 crossmodal transfer\] 的一种方式。另一种实现跨模态迁移的方式是协同学习（co-learning）。Co-learning 基本上也是指，你有一个希望在其中进行预测的模态。我能否把一些额外信息作为输入来训练模型，或者把一些额外信息作为输出中的预测目标来训练模型？对吧？你们可以看到，我在这里用了虚线，表示这个额外模态是在训练期间提供的，要么作为额外输入信号，要么作为额外预测目标。但在测试和推理期间，你仍然只有这个你关心的主要模态，对吧？这样在测试时，就能公平地与其他方法比较，对吧？

### [02:51](https://www.youtube.com/watch?v=IDaMEG_zY6A&t=171s) · b000004

**English**

If you're giving additional information when you're deploying the model, then you're making unfair comparisons. But you can add more information than you want during training. And finally, a third way of achieving transfer that we'll talk about is this idea of model induction. So in this case you are keeping two models separate right you don't want to for example adjust the architecture of your model to take in an additional input or you don't want to adjust your training objective to make some extra prediction on the output. So in this case transfer is achieved by keeping both of these models separate but as you can see later down the line there will be some way of inducing behavior between them so that transfer is possible. All right. So three types. First transfer where you start with a base model that is very powerful and you adapt it to the task that you care about with much more limited data. Co-learning where

**中文**

如果你在部署模型时提供额外信息，那么比较就不公平了。但在训练期间，你可以添加比你想要的更多的信息。最后，我们要讨论的第三种迁移方式是模型归纳（model induction）。在这种情况下，你把两个模型保持为独立的，对吧？例如，你不想调整模型架构来接收额外输入，或者不想调整训练目标来在输出端进行额外预测。因此，这种情况下，迁移是通过保持两个模型独立来实现的，但正如稍后你们会看到的，会有某种方式在它们之间诱导行为，从而使迁移成为可能。好了，三种类型。第一种是迁移，你从一个非常强大的基础模型出发，用少得多的数据将它适配到你关心的任务。Co-learning 则是

### [03:48](https://www.youtube.com/watch?v=IDaMEG_zY6A&t=228s) · b000005

**English**

fundamentally you are modifying the training of the model that you care about either using some additional extra input or an extra output prediction target. And model induction where you're keeping models separate but allowing them to induce behavior between each other. Transfer is perhaps the easiest, right? We've clearly all seen examples of transfer nowadays where you have pre-trained models, for example, language models or birds or other information in the way of the model parameters. That is the modality that has much more abundant data. Then a question becomes how do you adapt it quickly to a modality with much more limited data, right? how to use that as some either initial parameters or initial knowledge so that it can be subsequently used for your downstream model right I'm not going to cover everything that we've already seen for example you can always obviously

**中文**

从根本上修改你关心的模型的训练，使用额外输入或者额外的输出预测目标。而 model induction 是保持模型独立，但允许它们相互诱导行为。迁移可能是最容易理解的，对吧？显然，如今我们都见过迁移的例子：你有预训练模型，例如语言模型，或者 birds \[字幕疑误，可能指 BERT\]，或者以模型参数形式存在的其他信息。那是数据丰富得多的模态。于是问题就变成，如何迅速把它适配到数据少得多的模态，对吧？如何把它用作初始参数或初始知识，以便随后用于下游模型，对吧？我不会把我们已经看过的所有内容都讲一遍，例如，显然你总可以

### [04:44](https://www.youtube.com/watch?v=IDaMEG_zY6A&t=284s) · b000006

**English**

initialize right your your model with a pre-trained model like a lamb parameters or bird parameters or vision model parameters and then you can start fine-tuning what are the tasks that you care about using the very limited data that you have right it can be done using fine-tuning in context learning, instruction tuning, everything that we've seen so far in class. Right? Just as a recap, this was all the schematics in which we saw learning being possible. Supervised learning, multimodal learning where multimodal comes in as inputs and for the same task. Multitask learning where there's a single input and multiple outputs. transfer learning where X predicts Y1 and you're adapting it to predict Y2. Right? So now the task may be slightly different but the base input is the same. Crossodal learning refers to the setting where X1 predicts a single task

**中文**

用预训练模型来初始化你的模型，比如 lamb \[字幕疑误，可能指 LLaMA\] 参数、bird \[字幕疑误，可能指 BERT\] 参数，或者视觉模型参数，然后用你拥有的非常有限的数据，针对关心的任务开始微调，对吧？这可以通过微调（fine-tuning）、上下文学习（in-context learning）、指令微调（instruction tuning），以及目前课上讲过的所有方法来完成。对吧？简单回顾一下，这些是我们见过的能够进行学习的各种示意图。监督学习（supervised learning）；多模态学习（multimodal learning），其中多个模态作为输入，服务于同一个任务；多任务学习（multitask learning），其中有单个输入和多个输出；transfer learning，其中 X 预测 Y1，而你将它适配为预测 Y2。对吧？现在任务可能略有不同，但基础输入相同。Crossodal learning \[字幕疑误，可能指 crossmodal learning\] 指的是 X1 预测某一个任务

### [05:41](https://www.youtube.com/watch?v=IDaMEG_zY6A&t=341s) · b000007

**English**

and X2 predicts the same task or different input for the same task. Right? That's crossodal learning. And of course you have a unsupervised learning where X predicts some some subp part of X say X prime not the label and subsequently it is adapted to predict the label. So all of these approaches technically fall under you know this first way of doing cross model transfer which is to do transfer learning. Uh nowadays there's a lot of exciting work um in achieving much larger scale transfer. Large scale transfer in the sense that we have models that are trained on extremely diverse multimodal environments and also multitask environments. Right? So you might think of trying to train a generalist model that is able to use language and speech and gestures to predict something about humans that is able to use image and

**中文**

而 X2 预测同一个任务的情形，也就是同一任务使用不同输入，对吧？这就是 crossodal learning \[字幕疑误，可能指 crossmodal learning\]。当然，还有无监督学习（unsupervised learning），其中 X 预测 X 的某个子部分，比如 X prime，而不是标签，随后再适配为预测标签。因此，从技术上说，所有这些方法都属于实现 cross model transfer \[字幕疑误，可能指 crossmodal transfer\] 的第一种方式，也就是 transfer learning。呃，如今有很多令人兴奋的工作，试图实现规模大得多的迁移。所谓大规模迁移，是说我们有在极其多样的多模态环境以及多任务环境中训练的模型。对吧？你可以考虑训练一个通用模型（generalist model），它能够利用语言、语音和手势来预测与人有关的某些东西，能够利用图像和

### [06:37](https://www.youtube.com/watch?v=IDaMEG_zY6A&t=397s) · b000008

**English**

text to do some multimedia tasks like doing crossodal retrieval that is able to use force and propriioception. These are robotic sensors that is able to help control a robot and so on. So this generalization across different modalities and tasks can be very helpful especially for settings in which data is very low in resource. It's very difficult to get robotics data in the form of sensors. But perhaps seeing videos on the internet about how a robot is moving can help you train that model. It might be very difficult to get sensor data and tabular data in healthcare. But perhaps seeing tabular data in the form of other spreadsheets and other tables from research papers can help you learn better tabular representations for healthcare. That is a promise for why it's very appealing to train larger scale multimodal and multitask approaches even though the task that you

**中文**

文本来完成一些多媒体任务，比如 crossodal retrieval \[字幕疑误，可能指跨模态检索 crossmodal retrieval\]，还能够利用力和 propriioception \[字幕疑误，可能指本体感觉 proprioception\]。这些是机器人传感器，能够帮助控制机器人，等等。因此，这种跨不同模态和任务的泛化可能非常有帮助，尤其是在数据资源非常少的情形中。获取传感器形式的机器人数据非常困难。但也许观看互联网上机器人如何运动的视频，就能帮助你训练那个模型。在医疗保健领域，获取传感器数据和表格数据可能非常困难。但也许查看其他电子表格以及研究论文中其他表格形式的数据，可以帮助你为医疗保健学到更好的表格表示。这就是训练更大规模多模态和多任务方法很有吸引力的潜力所在，即便你

### [07:32](https://www.youtube.com/watch?v=IDaMEG_zY6A&t=452s) · b000009

**English**

care about may only be in one single vertical. So here are some papers, some that we did, some that other people have did as well in trying to scale up some of these multimodel and multitask models. At a high level, one key of achieving transfer is to share parameters, right? If you start sharing parameters, you start sharing your architectures that allows information to flow between different modalities and tasks and therefore achieve transfer. So how can we share parameters? If you look at all of these modalities, right, they may seem very different, but at a first order approximation, they can all be seen as a sequence, right? And that's perhaps the dominant paradigm of many of these frontier models today, which is to treat different modalities as sequences, right? Language, sequence of words, speech, sequence of signals,

**中文**

关心的任务可能只属于某一个垂直领域。这里有一些论文，有我们做的，也有其他人做的，都在尝试扩大这些 multimodel \[字幕疑误，可能指 multimodal\] 和多任务模型的规模。从整体上说，实现迁移的一个关键是共享参数，对吧？如果你开始共享参数，开始共享架构，就能让信息在不同模态和任务之间流动，从而实现迁移。那么，我们如何共享参数？如果你看看所有这些模态，对吧，它们可能看起来非常不同，但在一阶近似下，都可以被看作序列，对吧？这可能也是如今许多前沿模型的主导范式：把不同模态当作序列，对吧？语言是词的序列，语音是信号的序列，

### [08:28](https://www.youtube.com/watch?v=IDaMEG_zY6A&t=508s) · b000010

**English**

vision, video, a sequence of frames or individual gestures, even some of the sensing data. These are time series, but they can be seen as a sequence of of time points, right? Given that they're all based on sequences, uh it seems obviously very natural to use transformers and other sequence models to try to encode them. So perhaps it's even possible to use the same transformer to encode all of these with the same transformer architecture with the same model parameters to encode language and vision and audio and sensing data and more. the same model, right? That's why I use the the same color to depict it. Of course, it's not that extreme in the sense that you always use the exact same model, but what I've shown here are basically identifiers, right? You probably want to uh and we found this to be very helpful to add an identifier that basically identifies what modality

**中文**

视觉、视频是帧的序列，或者单个手势的序列，甚至包括某些传感数据。这些是时间序列，但也可以看成时间点的序列，对吧？既然它们都基于序列，呃，用 transformers 和其他序列模型来尝试编码它们，显然似乎很自然。因此，也许甚至可以使用同一个 transformer，以同样的 transformer 架构、同样的模型参数，来编码所有这些东西，包括语言、视觉、音频、传感数据以及更多内容。同一个模型，对吧？这就是我用同一种颜色来表示它的原因。当然，并不是极端到你始终使用完全相同的模型，但我这里展示的基本上是标识符，对吧？你可能希望，呃，我们发现这样非常有帮助，添加一个标识符，基本上用来标明这个模态

### [09:25](https://www.youtube.com/watch?v=IDaMEG_zY6A&t=565s) · b000011

**English**

it came from. So, you use for example one embedding uh to identify that this is language, right? when looking at human communication and this is also language when looking at different websites. Uh this is uh sensing data you're looking at force and is also sensing data when you're looking at a medical sensor. Right? These can all be the same indicator that indicates the same modality is present in both. Right? So in practice these modality embeddings are basically one hot vectors. Right? where language is 1 0 0 0 vision could be 0 1 0 0 0 audio will be 0 0 1 0 0 so it can be a one hot uh embedding that just indicates what modality it is so with yes&gt;&gt; so um is it just that transformers are now

**中文**

来自哪里。比如，你用一个嵌入（embedding）来标明这是语言，对吧，在观察人类交流时；而在查看不同网站时，这也同样是语言。呃，这是传感数据，你在查看力；而当你查看医疗传感器时，这也是传感数据，对吧？它们都可以用同一个指示符，表示两者包含相同模态，对吧？因此，在实践中，这些模态 embeddings 基本上是独热向量（one-hot vectors），对吧？其中语言是 1 0 0 0，视觉可能是 0 1 0 0 0，音频是 0 0 1 0 0，所以它可以是一个 one-hot embedding，只是标明这是哪个模态。所以，有——请说。&gt;&gt; 所以，呃，是不是仅仅因为 transformers 现在是

### [10:19](https://www.youtube.com/watch?v=IDaMEG_zY6A&t=619s) · b000012

**English**

this kind of encoding model and we wouldn't or is it also to have I guess unified model architecture that does multimodal encoding.&gt;&gt; Oh yeah, I'll get to multimodal encoding. Um but at least in the unimotal&gt;&gt; same&gt;&gt; yeah on the unimotal side um transformers is one way I one example is one way of potentially having a path towards a generalist AI where the same model can encode everything. Um we did this stuff in 2021 2022 when transformers were the dominant paradigm. Uh now if we were to revisit this you know perhaps you could use something like diffusion models right uh where diffusion models have clearly been able to do better on encoding vision and some of the sensing data. You know language is still kind of in the air whether you

**中文**

这种编码模型，而我们不会，还是也为了，我想，拥有一个执行多模态编码的统一模型架构？&gt;&gt; 哦，是的，我会讲到多模态编码。呃，但至少在 unimotal \[字幕疑误，可能指 unimodal\]——&gt;&gt; 相同的——&gt;&gt; 对，在单模态这一侧，呃，transformers 是一种方式，我，一个例子，是一种可能通向通用 AI 的途径，同一个模型可以编码所有东西。呃，我们在 2021、2022 年做这些工作，当时 transformers 是主导范式。呃，如果现在重新考虑这个问题，也许你可以使用扩散模型（diffusion models）之类的东西，对吧？Diffusion models 显然已经能够在视觉和一些传感数据的编码上做得更好。至于语言，现在仍然悬而未决，你是否

### [11:16](https://www.youtube.com/watch?v=IDaMEG_zY6A&t=676s) · b000013

**English**

want to use transformers or diffusion. Uh but you see that diffusion language models are becoming popular. Um but I think there is also still a path towards having one generalized architecture for everything. Here we just decided to use a transform. So you embed each of these modalities and append it with a modality encoding. It tells you what modality it is. Then you apply unimodal transformers over that sequence. Right? And what these will do is that it will just learn these you know pair-wise interactions within that same modality. So you look at how every force sensor reading you know aligns or interacts with other force sensor readings in the same modality and then separately you look at you know language words interact with other words in the context. Okay so these are unimodal transformers. Once you extract those representations you can then apply your multimodal

**中文**

想使用 transformers 还是 diffusion。不过，你们可以看到扩散语言模型（diffusion language models）正在流行起来。但我认为，仍然存在一种途径，可以用一个通用架构处理所有东西。这里我们只是决定使用一个 transform \[字幕疑误，可能指 transformer\]。所以，你为每一种模态生成 embedding，并附加模态编码。它告诉你这是什么模态。然后，对这个序列应用单模态 transformers，对吧？它们所做的，就是学习同一模态内的这些两两交互。所以，你会考察每一个力传感器读数如何与同一模态中的其他力传感器读数对齐或交互，然后另外考察语言中的词如何与上下文中的其他词交互。好了，这些是单模态 transformers。提取这些表示之后，你就可以应用多模态

### [12:12](https://www.youtube.com/watch?v=IDaMEG_zY6A&t=732s) · b000014

**English**

transformers. So these are the ones that we saw where instead of just doing self attention within each modality's own sequence, you're doing cross attention between the sequence in one with the sequence of the other. So for example, this cross attention, it will look at how every embedding of your entries within a table interacts with every embedding of each of the time steps in your sensor. That's your pair wise cross attentions. And for things that involve two modalities, you would just do three choose two sets of cross attention between each of the pairs within those three modalities. And again, what's really cool is that you can again define the same model, right? The same model with the same architecture with the same parameters is surprisingly able to encode how speech and gesture should fuse together and at the same time represent how force and

**中文**

transformers。这些就是我们看过的那种：不是仅在每个模态自己的序列内做自注意力（self-attention），而是在一个模态的序列与另一个模态的序列之间做交叉注意力（cross-attention）。比如，这个 cross-attention 会考察表格中各个条目的每个 embedding 如何与传感器中每个时间步的每个 embedding 交互。这就是两两的 cross-attention。对于涉及两个模态的东西，你就在那三个模态的每一对之间做三选二组 cross-attention。而且，非常酷的是，你又可以定义同一个模型，对吧？同一个模型，具有相同架构和相同参数，竟然既能够编码语音和手势应当如何融合，同时又能表示力和

### [13:08](https://www.youtube.com/watch?v=IDaMEG_zY6A&t=788s) · b000015

**English**

propioception should be fused together. Right? So it's the same color exact same model. Uh so how does this work? Oh, and of course once you have obtained representations from each of those um those multimodal transformer outputs, you would then have the unimodal representations and the multimodal representations and you would define different classification heads for your task, right? With the tasks could be quite different across domains. So you can think about this as a huge multimodal multitask approach. Uh so over here it's called a high MMT. Um the huge multimodal and multitask approach are the same model the same parameters encoding all pairs of different modalities and making able being able to make predictions on on different tasks. What can be also really cool is um you take this model and you

**中文**

propioception \[字幕疑误，可能指 proprioception\] 应当如何融合，对吧？所以是相同颜色，完全相同的模型。呃，那么它效果如何？哦，当然，一旦你从每个多模态 transformer 的输出中获得表示，就会同时拥有单模态表示和多模态表示，然后为你的任务定义不同的分类头（classification heads），对吧？不同领域中的任务可能很不一样。因此，你可以把它看成一种巨大的多模态多任务方法。呃，这里它叫作 high MMT \[字幕疑误，可能指 HighMMT\]。这个巨大的多模态多任务方法使用同一个模型、同一套参数，编码所有不同模态对，并能够对不同任务进行预测。还有一件非常酷的事，就是你拿这个模型，然后

### [14:05](https://www.youtube.com/watch?v=IDaMEG_zY6A&t=845s) · b000016

**English**

transfer it to some other task right to time series and table. So some other task with a new set of modalities and a new prediction task. So now you're getting generalization both in the input and in the output. Right? Obviously if you were to do this completely do it again with a new model you would just have to train from scratch. But if you use this model that you've already trained then this is giving you a good prior for what it would look like to fuse time series and tables for that prediction task. So how does it work? This is showing uh transfer performance right. So if you don't transfer at all, so you use zero source tasks and you just train a model from scratch on these data sets, you get about 68%. If you start training more and more models, sorry, you start training a model with more and more um pre

**中文**

把它迁移到其他任务，对吧，比如时间序列和表格。也就是另一个任务，具有一套新的模态和一个新的预测任务。现在，你在输入和输出两方面都获得了泛化，对吧？显然，如果你完全重新做一遍，使用一个新模型，就只能从头训练。但如果使用这个已经训练好的模型，它就能为你提供一个良好的先验，帮助理解针对那个预测任务融合时间序列和表格会是什么样子。那么效果如何？这里展示的是迁移性能，对吧？如果完全不做迁移，也就是使用零个源任务，只在这些数据集上从头训练模型，你得到大约 68%。如果开始训练越来越多的模型，抱歉，是开始用越来越多的预

### [15:00](https://www.youtube.com/watch?v=IDaMEG_zY6A&t=900s) · b000017

**English**

pre-training data sets, uh for example, one, two, three, you get monotonically better performance. And then for some of these other tasks as well. So if you don't turn on pre you get 63 and if you monotonically uh train on more and more tasks involving different modalities and prediction tasks you get monotonically better performance. Right? So this is um showing strong results on transfer across different settings can be particularly appealing and we find that uh the performance improvement correlates very well with how little data you have in this target task. Right? The less data you have in this target task, the more this pre-training on different tasks will help and the more data, the less the performance improvement will be. We also show some multitask results in in the paper showing that essentially if

**中文**

预训练数据集来训练一个模型，比如一个、两个、三个，你会得到单调提升的性能。在另一些任务上也是如此。如果不开启 pre \[原文如此，可能指预训练\]，你得到 63；如果在越来越多涉及不同模态和预测任务的任务上训练，就会得到单调提升的性能，对吧？因此，这展示了跨不同情形迁移的强劲结果，可能特别有吸引力。我们发现，性能提升与你在目标任务中拥有的数据有多少，很好地相关，对吧？目标任务的数据越少，在不同任务上的这种预训练帮助越大；数据越多，性能提升就越少。我们也在论文中展示了一些多任务结果，基本上表明，如果

### [15:56](https://www.youtube.com/watch?v=IDaMEG_zY6A&t=956s) · b000018

**English**

you have for example all of these tasks right they train separate models on each or you could train some unified multimodal multitask model and oftent times you get either the same performance or usually better performance. So it's able to do this multitask and transfer learning. Yes.&gt;&gt; Can you really say it's better if there's like no description of confidence interval between that's how we do it people 67%&gt;&gt; I don't see a difference.&gt;&gt; Yes. This is a data set where there's more data and this one is a bit more obvious. I think we have some confidence intervals in the paper. So at least there was some there was some

**中文**

你有，比如说，所有这些任务，对吧，可以在每个任务上分别训练模型，也可以训练某个统一的多模态多任务模型，而很多时候你会得到相同的性能，或者通常更好的性能。因此，它能够进行这种 multitask learning 和 transfer learning。请说。&gt;&gt; 如果没有描述这些结果之间的置信区间（confidence interval），你真的能说它更好吗？就是我们这样做，人们，67%。&gt;&gt; 我看不出区别。&gt;&gt; 是的。这个数据集的数据更多，而这一个要明显一些。我想论文里有一些置信区间。所以，至少存在一些，存在一些

### [16:52](https://www.youtube.com/watch?v=IDaMEG_zY6A&t=1012s) · b000019

**English**

statistically significant improvement uh with more transfer and then um we did this in 2022. So now now we have even more data and people have showed that it's kind of large scale multimodal multitask training does work better at large scale as well. Yeah. Um so yeah so another reference that is very interesting is this paper called go. It's called a generalist agent. Uh they did it primarily for for robotics where they showed that you could kind of train these models for classifying images, right? That gives the model visual capabilities and then you can transfer to model to classify um different objects that robot can see. So now it's starting to do towards robotics and show that the same model can also do robotic control. So it has better visual capabilities. They can start taking better actions. So start transferring from various visual tasks to to embodied tasks as well. That's another reference.

**中文**

随着迁移增加而出现的统计显著提升。然后，呃，我们是在 2022 年做这项工作的。现在我们有更多数据，人们也已经表明，这种大规模多模态多任务训练在更大规模下也确实效果更好。是的。那么，另一个非常有意思的参考是这篇叫作 go \[字幕疑误，可能指 Gato\] 的论文。它叫作《A Generalist Agent》。他们主要针对机器人开展这项工作，展示了你可以训练这些模型来对图像分类，对吧？这会赋予模型视觉能力，然后你可以迁移模型，去分类机器人能够看到的不同物体。这样就开始走向机器人领域，并展示同一个模型也能执行机器人控制。它有了更好的视觉能力，就能开始采取更好的行动。因此，也开始从各种视觉任务迁移到具身任务（embodied tasks）。这是另一个参考。

### [17:51](https://www.youtube.com/watch?v=IDaMEG_zY6A&t=1071s) · b000020

**English**

Of course, this is making a lot of assumptions here. Um we don't yet know whether this is going to be the dominant approach, right? Uh if you look at this, you know, obviously a lot of people are trying to build unified multimodal multitask approaches. Um we just saw the latest model from Meta yesterday. So Meta they they branded or first model that Meta Super Intelligence Labs released they branded it as a as a natively multimodal model right uh which basically means you know you have a set of approaches nowadays at some frontier labs where they train a language model they pre-train it and they staple adapters right onto the language model right the adapter for vision and adapter into LLM an adapter for audio adapter for speech recognition and so on. So that's probably the dominant paradigm done by most Frontier Labs. And then Meta released this and they said it's a

**中文**

当然，这里做了很多假设。我们还不知道这是否会成为主导方法，对吧？如果你看看这个，显然很多人正在尝试构建统一的多模态多任务方法。我们昨天刚看到 Meta 的最新模型。Meta 把它，或者说 Meta Super Intelligence Labs 发布的第一个模型，称为原生多模态模型（natively multimodal model），对吧？这基本上意味着，如今一些前沿实验室采用一套方法：先训练一个语言模型，预训练它，然后把适配器（adapters）钉到语言模型上，对吧？视觉的 adapter，接入大语言模型（LLM）的 adapter，音频的 adapter，语音识别的 adapter，等等。这可能是大多数前沿实验室采用的主导范式。然后 Meta 发布了这个，说它是一个

### [18:48](https://www.youtube.com/watch?v=IDaMEG_zY6A&t=1128s) · b000021

**English**

natively multimodal model which leads me to believe what they're trying to push is models that are more unified and can directly process all of these modalities to begin with during pre-training uh rather than only pre-training on language and then stapling other modalities on top. But jury is still up in the air. I think the model that meta released didn't show the best results on many things. So jury is still up in the air which which approach is better.&gt;&gt; How many parameters?&gt;&gt; I don't think they really thought

**中文**

原生多模态模型，这让我相信，他们正在推动的是更统一的模型，从预训练一开始就能够直接处理所有这些模态，而不是只在语言上预训练，再把其他模态钉上去。但现在仍然没有定论。我觉得 Meta 发布的模型在很多方面并没有展示最好的结果。所以究竟哪一种方法更好，仍然没有定论。&gt;&gt; 有多少参数？&gt;&gt; 我觉得他们并没有真正想过

### [19:23](https://www.youtube.com/watch?v=IDaMEG_zY6A&t=1163s) · b000022

**English**

&gt;&gt; um I think this these type of approaches also make a nice contrast with the reasoning based approaches we saw in the last two weeks. Right? Reasoning is very much about compositionality, right? modularity. You might try to build things each with different capabilities and then how you can orchestrate them in the right way. Whereas some of these other approaches like this generalist agent, they try to build everything unified into one big model instead of having many modular components.

**中文**

&gt;&gt; 呃，我觉得这类方法也与我们过去两周看到的基于推理（reasoning）的方法形成了很好的对照，对吧？Reasoning 很大程度上关注组合性（compositionality），对吧，模块化（modularity）。你可能会尝试构建各自具有不同能力的东西，然后考虑怎样以正确方式编排它们。而另一些方法，比如这个 generalist agent，则试图把所有东西统一到一个大模型中，而不是使用许多模块化组件。

### [19:57](https://www.youtube.com/watch?v=IDaMEG_zY6A&t=1197s) · b000023

**English**

So some what are some assumptions of these models which um I'm not fully satisfied with. So a lot of them assume that you know all these modalities despite being very different they can be viewed as sequences right language is a sequence tabular data is a sequence even some things like protein structures people are doing protein structure language models they also view it as a sequence so serializing everything uh obviously loses a lot of structure in your data and may or may not be the best approach it also assumes that the differences between modalities. They spent a lot of time discussing that heterogeneity is a very key concept uh a key driving principle in multimodal research and they're assuming that all of this heterogeneity can be just encoded by this modality specific embedding right that this is like ones and zeros and this is zero one zeros and

**中文**

那么，这些模型有哪些假设是我不完全满意的？很多模型假设，虽然所有这些模态非常不同，但它们都可以被看作序列，对吧？语言是序列，表格数据是序列，甚至蛋白质结构之类的东西，人们在做蛋白质结构语言模型时，也把它看作序列。因此，把一切序列化，显然会丢失数据中的大量结构，未必是最好的方法。它还假设模态之间的差异。他们花了很多时间讨论异质性（heterogeneity）是多模态研究中非常关键的概念，是一个关键驱动原则，而他们却假设所有这些 heterogeneity 都能仅由这个模态特定的 embedding 编码，对吧？比如这个是一些 1 和 0，那个是 0 1 0，还有

### [20:52](https://www.youtube.com/watch?v=IDaMEG_zY6A&t=1252s) · b000024

**English**

zero one zeros and um obviously that indicator function uh probably is not enough to capture all different ways which the data are different and of course this uh this fully shared multimodal model as opposed to more modular compositional approaches is still a big debate. Here are just uh all a bunch of other references right I organized them into this schematic. Uh so perceiver was perhaps one of the first approaches in this space uh by deep mind where they came up with a unified architecture different parameters right but unified architecture that can process all different modalities right edge video audio sensors I'm using that as shorthand notation and uh I'm using kind of squares to indicate that the architecture is the same but different

**中文**

0 1 0。显然，那个指示函数可能不足以捕捉数据存在差异的所有不同方式。当然，这种完全共享的多模态模型，与更加模块化、具有组合性的方法相比，仍然存在很大争论。这里还有一堆其他参考，对吧？我把它们整理成了这个示意图。Perceiver \[原文为 perceiver\] 可能是这个领域最早的方法之一，由 deep mind \[原文如此\] 提出。他们提出了一个统一架构，参数不同，对吧，但架构统一，可以处理各种不同模态，对吧，edge \[字幕疑误，可能指 image\]、视频、音频、传感器，我用这些作为简写。然后，我用方块表示架构相同，但用不同

### [21:49](https://www.youtube.com/watch?v=IDaMEG_zY6A&t=1309s) · b000025

**English**

colors to represent the parameters are different right so same architecture shared backbone just fine-tune it differently for different modalities. Still good because now convergence and architecture is something good because now you have just one architecture that people can make much more efficient or people can do the same theoretical analysis. So that's perceiver and then came a generation of methods like multimodel and vit a lot of these v vision language bird approaches they basically work on image and language they have both the same architecture and the same parameters the same model can encode both image and text uh and there were extensions to polyvit where you could have the same model to encode image and vision and audio right and then came uh these are you Think about these are unified encoders for unimodal learning. So it's still about vision tasks and language tasks

**中文**

颜色表示参数不同，对吧？所以，相同架构，共享骨干网络（backbone），只是针对不同模态以不同方式微调。这仍然很好，因为现在架构趋于一致是件好事：你只有一种架构，人们可以把它做得高效得多，或者进行同样的理论分析。这就是 perceiver。然后出现了一代方法，比如 multimodel 和 vit \[名称按原字幕保留\]，以及很多这些 v，vision language bird \[字幕疑误，可能指视觉语言 BERT\] 方法。它们基本上处理图像和语言，既有相同架构，又有相同参数，同一个模型可以编码图像和文本。后来又扩展到 polyvit，同一个模型可以编码图像、视觉和音频，对吧？然后出现了，呃，你可以把这些看作单模态学习的统一编码器。因此，它仍然围绕视觉任务、语言任务

### [22:46](https://www.youtube.com/watch?v=IDaMEG_zY6A&t=1366s) · b000026

**English**

and audio tasks. It's just how similar architectures and the parameters are is solving different unimodal tasks. Right? So the the Y's are still you know one modality to a Y another modality to a different Y. Maybe another set of approaches which are more multimodal and multitask learning right. So you have for example uh all your vision language birdlike approaches where they take an image and text and they learn a fused representation that can operate across multiple image and text tasks right image text for one task and image text for another task. So with the same architecture, same parameters and I mean the same logic extends for all these other things, right? Uh it's just how broadly they can go in the modalities and tasks that they support, right? So a bunch of all these methods that have been making the inroads in

**中文**

以及音频任务。只是架构和参数有多相似，用来解决不同的单模态任务，对吧？所以，这些 Y 仍然是，一个模态对应一个 Y，另一个模态对应另一个 Y。也许还有另一组方法，更侧重多模态和多任务学习，对吧？例如，所有那些 vision language birdlike \[字幕疑误，可能指类似视觉语言 BERT 的\] 方法，它们接收图像和文本，学习一个融合表示，可以用于多个图像和文本任务，对吧？图像加文本用于一个任务，图像加文本又用于另一个任务。使用相同架构、相同参数，我的意思是，同样的逻辑可以扩展到所有这些其他东西，对吧？只是在于它们所支持的模态和任务能够覆盖多广。因此，有一大批这样的方法正在取得进展，

### [23:42](https://www.youtube.com/watch?v=IDaMEG_zY6A&t=1422s) · b000027

**English**

achieving more generalization, multimodal multitask generalization. What are some open challenges I see in this space? Um, a lot of tasks still are very low resource. So most of all this advances have been still been operating in the digital space where people are still working with image and text and audio data. Having this extend to the real world is still a challenge. Beyond language and vision is still a challenge especially to settings where some modalities deep learning and transformers are not the state-of-the-art right so for tabular and time series we're still always jumping between whether deep learning and transformers and foundation models are good or are traditional approaches like traditional tabular and time series approaches are better. uh this naturally adds more complexity

**中文**

实现更多泛化，也就是多模态多任务泛化。我认为这个领域有哪些开放挑战？呃，很多任务的资源仍然非常少。因此，这些进展大多仍发生在数字领域，人们仍然在处理图像、文本和音频数据。把它扩展到现实世界仍然是个挑战。超越语言和视觉仍然是个挑战，尤其是在某些模态中，深度学习（deep learning）和 transformers 并不是当前最先进的方法，对吧？所以，对于表格和时间序列，我们仍然不断在两种判断之间来回：究竟 deep learning、transformers 和基础模型（foundation models）更好，还是传统方法，比如传统表格和时间序列方法更好。呃，这自然会增加更多复杂性，

### [24:41](https://www.youtube.com/watch?v=IDaMEG_zY6A&t=1481s) · b000028

**English**

in the sense that these are larger models they're require more data and more data hungry but at the same time as I mentioned there's a particular appeal when architectures converge because now the whole community can just focus on making more efficient one architecture and doing theoretical analysis and good optimization of one architecture and we'll discuss more about interpretability maybe later on in the class but obviously these are still huge blackbox approaches

**中文**

因为这些模型更大，需要更多数据，对数据的需求更强。但同时，正如我提到的，架构趋于一致具有独特的吸引力，因为现在整个社区都可以专注于提升一种架构的效率，对一种架构进行理论分析和良好的优化。我们也许会在这门课稍后讨论更多可解释性（interpretability）问题，但显然，这些仍然是巨大的黑箱（blackbox）方法。

### [25:15](https://www.youtube.com/watch?v=IDaMEG_zY6A&t=1515s) · b000029

**English**

Any questions about this multimodal and multipass learning?

**中文**

关于这种多模态和 multipass learning \[字幕疑误，可能指 multitask learning\]，有什么问题吗？

### [25:30](https://www.youtube.com/watch?v=IDaMEG_zY6A&t=1530s) · b000030

**English**

Okay, so that's one way of achieving transfer, right? How do you design? I think we've covered here. How do you design the same architecture with the same parameters that are shared as much as possible and by definition once you start sharing parameters transfer happens because of the common parameters between one modality and one task and another. So this doesn't involve any additional training objective and so on apart from just doing multitask learning. So a second set of approaches for achieving transfer is what we call co-learning. Co-learning essentially means that you're trying to transfer information from your secondary modalities to your primary modality by adjusting the representation space itself during training. So this is a general setup. A is something that you care about, right? This is the one that you actually care about making

**中文**

好了，这就是实现迁移的一种方式，对吧？你如何设计？我想我们这里已经讲过了。如何设计同样的架构，使用尽可能共享的相同参数？按照定义，一旦开始共享参数，迁移就会发生，因为一个模态和任务与另一个模态和任务之间具有共同参数。因此，除了执行 multitask learning，它不涉及任何额外训练目标之类的东西。实现迁移的第二组方法，是我们所称的 co-learning。Co-learning 基本上是指，你试图在训练期间调整表示空间本身，把信息从次要模态迁移到主要模态。这是一般设定。A 是你关心的东西，对吧？这是你真正关心在其中进行

### [26:25](https://www.youtube.com/watch?v=IDaMEG_zY6A&t=1585s) · b000031

**English**

predictions in. and B is some extra modality that you have access to during training. It's only available during training. How do you use that to learn a better representation during training? Right? Afterwards, you throw this away and you are left with a better model that you can use for inference during test time. The important thing is that you no longer have access to this after training. you've enriched the representation so that during test time you're still making a fair comparison with baselines that only use this modality.

**中文**

预测的那个。而 B 是训练期间可以访问的某个额外模态。它只在训练期间可用。你如何利用它，在训练期间学到更好的表示，对吧？之后，你把它丢掉，留下一个更好的模型，可以在测试时用于推理。关键在于，训练之后你就无法再访问它了。你已经丰富了表示，因此测试时，你仍然可以与只使用这个模态的基线（baselines）公平比较。

### [27:02](https://www.youtube.com/watch?v=IDaMEG_zY6A&t=1622s) · b000032

**English**

So there's there are going to be three ways of achieving co-learning that are broadly covered. These are multimodal approaches that you've all seen uh fusion, alignment and translation. And we'll start by seeing how fusion can enable code learning. So here is how you can use fusion to do code learning. So you first start during training by training a fusion model with both modalities A and D. Right? So the multimodel data during training and you're training a fusion model to predict your label Y. This can be any any fusion model we've seen, right? Uh additive, multiplicative, early, late fusion, whatever. Right? That's during training. Now during testing I'm going to use the same fusion model but I'm going to input zeros for modality B right so input zeros or input the average or the median

**中文**

因此，我们会大致介绍三种实现 co-learning 的方式。这些都是你们已经见过的多模态方法：fusion、alignment 和 translation。我们先来看 fusion 如何实现 code learning \[字幕疑误，可能指 co-learning\]。这里展示如何使用 fusion 来进行 code learning。首先，在训练期间，用 A 和 D 两个模态训练一个融合模型，对吧？也就是训练期间的 multimodel \[字幕疑误，可能指 multimodal\] 数据，你训练一个融合模型来预测标签 Y。这可以是我们见过的任何融合模型，对吧？加性、乘性、早期融合、后期融合，什么都可以，对吧？这是训练期间。现在，在测试期间，我会使用同一个融合模型，但给模态 B 输入零，对吧？输入零，或者输入平均值、中位数，

### [27:59](https://www.youtube.com/watch?v=IDaMEG_zY6A&t=1679s) · b000033

**English**

or anything where you know you don't actually have modality at testing so replace it with some constant or or dynamic value like the average or something okay so now you see that during testing this is a model that only operates on modality TA but this is a model that you know was trained using multimodal fusion with both A and B during training. So this is a multimodal co-learning setting. If you look at the contrast with um unimodal learning, you look at a contrast with unimodal learning, you have modality A prediction Y during training and then modality A same modality uh making inference on the model during testing. Okay, so that's a training and testing setup. Now, in testing, both of these are fair comparison, right? In testing, they're only just taking a modality A and making a prediction. They're fair comparison.

**中文**

或者任何东西，因为你在测试时实际上没有那个模态，所以用某个常数，或者像平均值这样的动态值替换它，好吗？现在你们看到，在测试期间，这个模型只处理模态 TA \[字幕疑误，可能指 A\]，但这个模型在训练期间使用了 A 和 B 两者进行多模态融合训练。因此，这是一个多模态 co-learning 设定。如果与单模态学习对照，看看与单模态学习的对照，你在训练期间用模态 A 预测 Y，然后在测试期间用模态 A，同一个模态，在模型上进行推理。好了，这就是训练和测试设定。现在，在测试中，这两者是公平比较，对吧？在测试中，它们都只接收模态 A，然后进行预测。比较是公平的。

### [28:55](https://www.youtube.com/watch?v=IDaMEG_zY6A&t=1735s) · b000034

**English**

The question then becomes, if I know I want to just predict on modality A, should I train a unimodal model on A or should I bother training a multimodal model with A and B during training and replace me with zeros. So only text is used at test time and there's a lot of findings that show that multimodal code learning can outperform language only training with fair comparison during testing. Having that additional modality be during training and training a fusion model instead of a language model can actually lead to better performance when evaluated.

**中文**

于是问题变成，如果我知道自己只想在模态 A 上进行预测，我应该在 A 上训练一个单模态模型，还是应该费力在训练期间用 A 和 B 训练一个多模态模型，再用零替换 me \[字幕疑误，可能指 B\]？因此，测试时只使用文本，而很多发现表明，在测试时公平比较的情况下，多模态 code learning \[字幕疑误，可能指 co-learning\] 能够胜过仅使用语言的训练。在训练期间加入额外模态 be \[字幕疑误，可能指 B\]，训练融合模型而不是语言模型，实际上可以在评估时获得更好的性能。

### [29:40](https://www.youtube.com/watch?v=IDaMEG_zY6A&t=1780s) · b000035

**English**

Yes,&gt;&gt; I guess my mind immediately goes like covering distributions perhaps having another modality exposes you to distribution both. What do you think is thing that drives this enrichment? Yeah, I think there's both um information and regularization effects, right? I think all cases, one is about does it provide more information into the parameters during training and the other one is that is the model being regularized better so that it's not about adding more information but it's about you know shaping among the information that you have shaping the model predictor that is the best at using that information. So enrichment argument is that for example right now if you're kind of listening to me speak you're seeing you know seeing my lips and you're hearing my voice and then

**中文**

请说。&gt;&gt; 我想，我立刻想到的是覆盖分布，也许另一个模态能让你接触到两边的分布。你认为是什么在驱动这种丰富化？&gt;&gt; 是的，我认为既有信息效应，也有正则化（regularization）效应，对吧？我想在所有情况下，一方面是，它是否在训练期间向参数提供了更多信息；另一方面是，模型是否得到了更好的 regularization，因此重点不在添加更多信息，而在于，在你拥有的信息之中，塑造一个最善于利用这些信息的模型预测器。所以，丰富化的论点是，例如，现在如果你在听我讲话，你看得到我的嘴唇，也听得到我的声音，然后

### [30:36](https://www.youtube.com/watch?v=IDaMEG_zY6A&t=1836s) · b000036

**English**

obviously if you close your eyes you can kind of imagine what I'm looking like and what I'm expressions might look like right or if you uh close your ears and you just see me you can also kind of make up what I am um might be saying just by looking at my lips move right so there is more information probably being provided and there's some mechanism in these models when they're doing fusion they kind of you know cross predicting one modality from the other and therefore even though at testing I don't give you B you can probably use A to hallucinate B and that gives you extra signal um there are probably also regularization effects um when I say regularization you want want to think about it as you know most of machine learning you have data X and Y and there's going be many different functions, many different hypotheses that fit your data that can make predictions Y from X, right? But among

**中文**

显然，如果闭上眼睛，你也能大致想象我的样子，以及我的表情可能是什么样，对吧？或者，如果你捂住耳朵，只看着我，也能仅仅通过看我的嘴唇运动，大致补出我可能在说什么，对吧？所以，可能确实提供了更多信息，而且这些模型在做 fusion 时存在某种机制，它们会从一个模态交叉预测另一个模态。因此，即便测试时我不给你 B，你也可能用 A 来幻构（hallucinate）B，这会给你额外信号。呃，可能也有 regularization 效应。我说 regularization 时，你可以这样理解：在大多数机器学习中，你有数据 X 和 Y，而有许多不同函数、许多不同假设，都能拟合你的数据，都能从 X 预测 Y，对吧？但在

### [31:32](https://www.youtube.com/watch?v=IDaMEG_zY6A&t=1892s) · b000037

**English**

all of these possible hypotheses, some are better than others, right? Some generalize better, some can be trained better and overwhelming argument is that hypotheses that are more simple, right, are preferred, right? Complex hypothesis tend to overfitit to your data and usually simple ones that are not overly simple. So you get high training error, but good simple ones tend to generalize better. And sometimes giving different views of your data allow you to kind of you know break this tie among particularly complex hypothesis for A may not fit something for B. And if you have the model fit both, you'll end up choosing a one that is simpler and more consistent with the world and therefore both. But I don't have a rigorous theoretical argument for all this. I think a lot of these are empirical findings. Would be great if we had more theory for this. I mean for multimodal AI in general or frontier AI in general.

**中文**

所有这些可能的假设中，有些比其他的更好，对吧？有些泛化得更好，有些更容易训练。一个占主导的论点是，更简单的假设更受偏好，对吧？复杂假设往往会过拟合你的数据，而通常简单的假设，只要不是过于简单，以至于训练误差很高，好的简单假设往往泛化得更好。有时，给出数据的不同视图，能让你打破这些假设之间的平局：对于 A 特别复杂的假设，可能无法拟合 B 中的某些东西。如果让模型同时拟合两者，最终就会选出一个更简单、更符合世界、因此也更符合两者的假设。但我对这些没有严格的理论论证。我觉得这里很多都是经验发现。如果能有更多理论就好了。我的意思是，对于多模态 AI，或者一般的前沿 AI 都是如此。

### [32:28](https://www.youtube.com/watch?v=IDaMEG_zY6A&t=1948s) · b000038

**English**

I saw yes never trade on zeros. So it's completely out of so I mean you can build it always instead.&gt;&gt; Yeah.&gt;&gt; What's the standard?&gt;&gt; Yeah. Um, I've seen fill with zeros. I've seen fill with the average value. I've seen fill with noise. Um, well, I've not seen fil with noise that much actually. I've seen a lot of fil with zeros in the average value.&gt;&gt; Uh,&gt;&gt; you don't have a relationship?&gt;&gt; Not not in a lot of these papers that I that we've we've seen. Um,&gt;&gt; I'm thinking if you like pretty bad, you should train on both without data and with&gt;&gt; Yeah. Yeah. Yeah. There's a whole community on dealing with noisy and missing modalities, right? Which come from this from a different angle, right? In their case, it is by necessity that B will be not visible during testing. So

**中文**

我看到，是的，从来不在零上 trade \[字幕疑误，可能指 train\]。所以它完全在……之外，我的意思是，你可以始终改成构建它。&gt;&gt; 对。&gt;&gt; 标准做法是什么？&gt;&gt; 对。呃，我见过填零，也见过填平均值。我见过填噪声。嗯，其实填噪声我见得并不多。大量的做法是填零和平均值。&gt;&gt; 呃。&gt;&gt; 没有一种关系吗？&gt;&gt; 在我们看过的这些论文中，很多并没有。&gt;&gt; 我在想，如果你，比如，非常差，你应该在没有数据和有数据两种情况下都训练——&gt;&gt; 对，对，对。有一整个研究社区在处理含噪和缺失模态，对吧？他们是从另一个角度看这个问题的，对吧？在他们的情形中，B 在测试期间不可见是不得已的。所以

### [33:25](https://www.youtube.com/watch?v=IDaMEG_zY6A&t=2005s) · b000039

**English**

they can expose the model to all forms of perturbations on noisy B and missing B and um and achieve something better, right? Uh so they come at it noisy missing modality community kind of come at it from a different angle and I'm sure they also have really good results. Yeah, here it's just various people have made the finding that no even if you just don't put anything it's better this multimodal model is better than just single modality model. Yes,&gt;&gt; seems paradoxical because on one hand B is but on the other when you're testing it B doesn't have much influence in the outcome.

**中文**

他们可以让模型接触针对含噪 B 和缺失 B 的各种扰动，从而取得更好的结果，对吧？所以，研究含噪和缺失模态的社区是从另一个角度切入的，我相信他们也有非常好的结果。是的，这里只是不同的人发现，即便什么也不放进去，仍然更好，这个多模态模型仍然比单模态模型好。请说。&gt;&gt; 这似乎有些矛盾，因为一方面 B 是，但另一方面，在测试它时，B 对结果没有太大影响。

### [34:08](https://www.youtube.com/watch?v=IDaMEG_zY6A&t=2048s) · b000040

**English**

We're not saying B doesn't have much influence on the outcome, right? Because we're comparing this setting where only A is given at testing, right? and filling E with zeros versus a setting where only A is given and a model was always unimodal to begin with. Right? So, we're only comparing these two. We're not really comparing A B like to to answer your question, you'll be comparing A with missing B versus A with B present, right? That would ablate the effect of B, right? So, let's say you have um A and B together during testing. That would be the best 90%. Okay. And then I zero out B, that might be 60%. Right? So now I know B's contribution is about 30%. Right? And then I compare with a model that was just always unit model A. I'm saying that's 50 50%. Right? So it's 60% versus 50%, 10% was the contribution of

**中文**

我们并没有说 B 对结果没有太大影响，对吧？因为我们比较的是这种设定：测试时只给 A，并用零填充 E \[字幕疑误，可能指 B\]，与另一种只给 A、而模型从一开始就一直是单模态的设定，对吧？所以，我们只比较这两者。我们并没有真正比较 A B，比如要回答你的问题，你需要比较 A 加缺失的 B，与 A 加存在的 B，对吧？那样才是在消融（ablate）B 的影响，对吧？假设测试期间你同时有 A 和 B，那会是最好的，90%。好了，然后我把 B 置零，可能变成 60%，对吧？现在我知道 B 的贡献大约是 30%，对吧？然后我再与一个始终只是 unit model \[字幕疑误，可能指 unimodal\] A 的模型比较。我说它是 50，50%，对吧？所以是 60% 对 50%，10% 是

### [35:05](https://www.youtube.com/watch?v=IDaMEG_zY6A&t=2105s) · b000041

**English**

having additional B during training, right? And if you also have B during testing, which is obviously the ideal setting, D, you get 90%, right? So here is um perhaps some 2014 did this paper multimodal learning with deep machines um kind of just showed this as an afterthought right so in this setting this was before deep learning kind of kind of became really popular and people were still working on bolster machine RBMs I don't know people know what that is uh but these are joint probabilistic models right so you learn a joint distribution over uh in this case image and text. Okay. So you had image only models and you had all of these uh these uh these image only models and you had this multimodal model and for this multimodal model you see here over here generated text right so it didn't

**中文**

训练期间额外拥有 B 的贡献，对吧？而如果测试期间也有 B，显然这是理想设定，D \[原文如此\]，你会得到 90%，对吧？这里也许是 2014 年的这篇论文，multimodal learning with deep machines \[标题按原字幕保留\]，他们只是顺带展示了这一点。这是在深度学习真正流行之前，人们还在研究 bolster machine RBMs \[字幕疑误，可能指 Boltzmann machine、受限玻尔兹曼机 RBMs\]，不知道大家是否知道那是什么，但这些是联合概率模型，对吧？你学习一个联合分布，在这个例子中是图像和文本的联合分布。好了。所以，你有仅图像模型，还有所有这些，呃，这些仅图像模型，以及这个多模态模型。对于这个多模态模型，你看这里写着生成的文本，对吧？所以，它并没有

### [36:01](https://www.youtube.com/watch?v=IDaMEG_zY6A&t=2161s) · b000042

**English**

actually have text during testing because there' be unfair comparison with all these other models that only have access to the image. So this model they handicapped it by removing the text right only having the image removing the text and having it kind of self-generate the text right and it was able to outperform with a good margin uh methods that were just unimodal to begin.

**中文**

在测试期间真正拥有文本，因为那样与所有这些只能访问图像的其他模型比较就不公平。因此，他们通过移除文本来限制这个模型，对吧？只保留图像，移除文本，让它自己生成文本，对吧？结果它能够以相当大的优势，胜过那些从一开始就只是单模态的方法。

### [36:32](https://www.youtube.com/watch?v=IDaMEG_zY6A&t=2192s) · b000043

**English**

Uh here's another method um also a very seminal paper multimodal deep learning from again way back 2011. uh they showed this for uh perhaps one of the first examples that that I gave for multimodal this mgherk effect right so where people were were verbalizing different sounds so you see their lips moving and you hear the different audio and some of it was ambiguous right like ba and ga they sound exactly the same but you have to look at the lips right so they also had a similar setting where they train with audio and video right to get some shared representations and Then during testing uh they remove one or remove the other right and the goal is that even by masking one out or the other uh does it get better representations than with just unimodal your data right without the multimodal training.

**中文**

呃，这里还有另一种方法，也是一篇非常有开创性的论文，multimodal deep learning，同样要追溯到 2011 年。他们针对，可能是我给大家讲过的最早几个多模态例子之一，这个 mgherk effect \[字幕疑误，可能指 McGurk effect\]，展示了这一点。人们发出不同声音，你看到他们的嘴唇移动，也听到不同音频，其中一些是有歧义的，对吧？比如 ba 和 ga，它们听起来完全一样，但你必须看嘴唇，对吧？他们也采用了类似设定：用音频和视频训练，以获得某种共享表示，然后在测试期间，移除其中一个，或者移除另一个。目标是，即便遮掉其中一个，它是否也能比仅使用单模态数据、没有多模态训练时获得更好的表示。

### [37:31](https://www.youtube.com/watch?v=IDaMEG_zY6A&t=2251s) · b000044

**English**

&gt;&gt; All right. Any more questions about co-learning via fusion?&gt;&gt; Yes. I I know you don't like questions like these asking, but um so let's say uh you grew up blind. Okay.&gt;&gt; Okay.&gt;&gt; And my guess or my my task is to guess your or I grew up blind. My guess is to uh guess your mental state and Tom has all his senses. Say they all work perfectly well. Should we expect that if I take away one of Tom's senses, let's say take away his sight, that he's more likely to pick up on your mental state because he has a superation.

**中文**

&gt;&gt; 好了，关于通过 fusion 实现 co-learning，还有问题吗？&gt;&gt; 有。我知道你不喜欢被问这类问题，不过，假设，呃，你从小失明。好吗？&gt;&gt; 好。&gt;&gt; 而我的猜测，或者我的任务，是猜测你的，或者说我从小失明。我的任务是猜测你的心理状态，而 Tom 的所有感官都健全。假设它们都运作得非常好。如果我拿掉 Tom 的一种感官，比如拿掉他的视觉，我们是否应该预期，他更有可能察觉你的心理状态，因为他有一种 superation \[原文含义不明\]。

### [38:17](https://www.youtube.com/watch?v=IDaMEG_zY6A&t=2297s) · b000045

**English**

&gt;&gt; Maybe why do you say I don't have these questions? because in the past I think you like I've asked like cognitive related questions and you were like ah&gt;&gt; I I think I I uh I don't think cognitive um cognitive insights are useful for training frontier AI models right I think these questions are very interesting um I think if you talk about human I think another big aspect is this idea of plasticity right if you grew up blind your brain And there's evidence to show that, you know, from neuroscience that your brain probably would have rewired itself to heighten your other senses to make up for your lack of vision, right? And therefore, your maybe smell is or sense of touch or hearing is better. None of which are useful for detecting my emotion though. Um, so I'm not sure. I think in this case, I think it's going

**中文**

&gt;&gt; 也许。为什么说我不喜欢这些问题？&gt;&gt; 因为以前我问过一些认知相关的问题，我觉得你会说，啊——&gt;&gt; 我想，我，呃，我不认为认知方面的见解对训练前沿 AI 模型有用，对吧？我觉得这些问题很有趣。我想，如果讨论人类，还有一个很重要的方面，就是可塑性（plasticity），对吧？如果你从小失明，你的大脑，而且神经科学有证据表明，你的大脑可能已经重新连接自己，增强其他感官，以弥补视觉缺失，对吧？因此，你的嗅觉，或者触觉、听觉，也许会更好。不过，这些都无助于检测我的情绪。所以我不确定。我觉得在这种情况下，它会

### [39:15](https://www.youtube.com/watch?v=IDaMEG_zY6A&t=2355s) · b000046

**English**

to be I mean, it's not even a fair comparison. How if you're blind, grew up blind, how would you detect my emotion? What was the control procedure to detect my emotion that both you and&gt;&gt; I'm humanal in that case? Like all I have is hearing or he's both.&gt;&gt; Oh, so I'm speaking.&gt;&gt; Yeah. Yeah. You're&gt;&gt; okay.&gt;&gt; I'm trying to guess like what what's the quality of your mental state from your utterances?&gt;&gt; I see.&gt;&gt; Yeah.&gt;&gt; You should do such a study.&gt;&gt; Do such a study. I think people probably would have already, right? Um I mean this whole plasticity argument you know blind people who have grew up blind I think sharper hearing or sharper smelling and touching I think has been experimentally proven. Not sure whether it's been done for emotion. I mean that could be another hypothesis for for some of this right which is this plasticity argument that you know handicapping a model by dropping out B um

**中文**

是，我的意思是，这甚至不是公平比较。如果你失明，从小失明，你会如何检测我的情绪？检测我的情绪的对照程序是什么，你和——&gt;&gt; 那种情况下我是 humanal \[字幕疑误，可能指 unimodal\] 吗？比如我只有听觉，而他两者都有。&gt;&gt; 哦，所以我在说话。&gt;&gt; 对，对，你在——&gt;&gt; 好。&gt;&gt; 我在试着从你的话语中猜测，你的心理状态是什么样的。&gt;&gt; 明白了。&gt;&gt; 对。&gt;&gt; 你应该做这样的研究。&gt;&gt; 做这样的研究。我想可能已经有人做过了，对吧？我的意思是，整个 plasticity 的论点，从小失明的人听觉更敏锐，或者嗅觉、触觉更敏锐，我想已经得到实验验证了。不确定是否有人针对情绪做过。我的意思是，这也可能是其中一些现象的另一个假设，就是 plasticity 的论点：通过丢弃 B 来限制模型，呃，

### [40:12](https://www.youtube.com/watch?v=IDaMEG_zY6A&t=2412s) · b000047

**English**

handicapping a model by dropping out B has you know forces the model to kind of recreate B right so it be interesting question to see right now I'm just training with both A and B and I'm just handicapping at a testing what if there was a curriculum as Ako mentioned right uh if you kind So exposed the model to to missing the maybe 80% of the time and the 90% of the time and 100% of the time and then maybe that would influence what the performance is right&gt;&gt; isn't sufficient right you still get bias from mod that wouldn't get it at all like if you're flying from the start&gt;&gt; yeah so I think this is like blind from the start right this is kind of like maybe Well, not really because I mean Yeah.&gt;&gt; I think what&gt;&gt; Yeah. Yeah. And the brain has access to to vision. So I don't even think this is blind to the star. Something like like

**中文**

通过丢弃 B 来限制模型，会迫使模型在某种程度上重建 B，对吧？所以，值得研究的一个有趣问题是：现在我只是同时用 A 和 B 训练，只在测试时限制它；如果像 Ako 提到的那样，有一个课程（curriculum）呢？如果你让模型接触缺失的情形，也许 80% 的时间缺失，然后 90% 的时间，再到 100% 的时间，也许这会影响性能，对吧？&gt;&gt; 这还不充分，对吧？你仍然从模态中获得偏置，而另一种完全得不到，比如从一开始就 flying \[字幕疑误，可能指 blind\]。&gt;&gt; 对，所以我觉得这就像从一开始就失明，对吧？这有点像，也许，嗯，也不完全，因为，我的意思是，对。&gt;&gt; 我觉得——&gt;&gt; 对，对。而大脑能访问视觉。所以我甚至不觉得这算是从一开始就失明。类似，类似

### [41:08](https://www.youtube.com/watch?v=IDaMEG_zY6A&t=2468s) · b000048

**English**

that. Yeah. Okay. Um so I think that's that's a really good segue to the second way of doing co-learning. So if you see this first way, right? Um it's cold learning via fusion. you're only ever having one objective which is to just make prediction on the label. Right? As you see for these other two ways of doing co-learning, you can add more objectives, right? To explicitly align or translate your data to encourage this kind of plasticity or this kind of hallucination of other modalities in addition to just your task. So the second approach is called co-learning via alignment. Right? Same setting. you have a that you care about and it's not very good. So you introduce B during training and co-learning happens right but to get a better representation but instead of just relying on fusion with respect to the

**中文**

那样。对。好了。我觉得这很好地引出了第二种 co-learning 方式。如果你看第一种方式，对吧，它是通过 fusion 进行 cold learning \[字幕疑误，可能指 co-learning\]，你始终只有一个目标，就是对标签作预测，对吧？而在另外两种 co-learning 方式中，你可以添加更多目标，对吧？显式地对齐或翻译数据，除了任务本身之外，还鼓励这种 plasticity，或者这种对其他模态的幻构。因此，第二种方法叫作通过 alignment 进行 co-learning，对吧？设定相同，你有自己关心的 a，但它不太好。所以在训练期间引入 B，进行 co-learning，以获得更好的表示。但不再只是依靠面向

### [42:04](https://www.youtube.com/watch?v=IDaMEG_zY6A&t=2524s) · b000049

**English**

task now you can add alignment objectives between A and B so that the resulting representation is better right then if folks uh remember alignment are these approaches where instead of fusing it into one embedding you keep A and B as separate embeddings and you have this similarity function between them. So you bring for example positive pairs where A and B are have similar meaning closer together and you push negative pairs where A and B are of different meaning further apart.

**中文**

任务的 fusion，现在你可以在 A 和 B 之间添加 alignment 目标，让得到的表示更好，对吧？如果大家还记得，alignment 指的是这样一些方法：你不把它们融合成一个 embedding，而是将 A 和 B 保持为独立的 embeddings，并在它们之间设置一个相似度函数。比如，把 A 和 B 含义相似的正样本对拉近，把 A 和 B 含义不同的负样本对推远。

### [42:36](https://www.youtube.com/watch?v=IDaMEG_zY6A&t=2556s) · b000050

**English**

So there are a lot of examples of this right I think this is probably one of the earliest ones I could find where you're trying to learn this paper is called zeroot learning through crossodal transfer. So already kind of ticks a lot of these boxes, right? Cross motor transfer and is able to use this transfer to do very quick generalization zero shot to a new new task. So the setting is that you have a bunch of images and these were still rather simplistic bar 10 images and you had a bunch of uh uh categories for these images, right? Categories were just a word for example auto, horse and doll, right? And alignment essentially allows you to learn this joint representation space where um your cluster of image embeddings for your image images of dogs are all very close to the uh the word

**中文**

这方面有很多例子，对吧？我想这可能是我能找到的最早几个例子之一，你试图学习，这篇论文叫作 zeroot learning through crossodal transfer \[字幕疑误，可能指 Zero-Shot Learning Through Cross-Modal Transfer\]。所以，它已经符合其中很多点，对吧？Cross motor transfer \[字幕疑误，可能指 crossmodal transfer\]，能够利用这种迁移，对一个新任务进行非常快速的零样本（zero-shot）泛化。因此，这个设定是，你有一批图像，这些还是相当简单的 bar 10 \[字幕疑误，可能指 CIFAR-10\] 图像，并且有这些图像的一批类别，对吧？类别只是一个词，比如 auto、horse 和 doll \[字幕疑误，可能指 dog\]，对吧？Alignment 基本上让你学到这种联合表示空间，其中，狗图像的 image embeddings 簇都非常接近那个词的

### [43:32](https://www.youtube.com/watch?v=IDaMEG_zY6A&t=2612s) · b000051

**English**

embedding for the word dog. Likewise, your cluster of image embeddings for horse are very close to the word embedding for horse. Likewise for auto and so on. Right? This is the kind of representation space that you will get during uh representation alignment. Right? So we've seen this in clip and all these contrastive learning stuff. Now this paper is able to show that now if you take a new image from an unknown class, right? So you've never seen an image before, right? The image of a cat. First you would embed it into this representation space. If your visual encoders are trained well then it will be embedded nearby the image embeddings for dot right because visually similar images will get embedded into similar similar embedding spaces right and more importantly because your presentation space also contains word embeddings and the word embeddings are shaped well you would have the word embedding for cat

**中文**

embedding，也就是 dog 的词 embedding。同样，horse 图像的 embeddings 簇非常接近 horse 的词 embedding。auto 等等也是如此，对吧？这就是在表示对齐（representation alignment）期间会得到的那种表示空间。我们已经在 clip 和所有这些对比学习（contrastive learning）方法中见过它。这篇论文能够展示，如果现在拿来一张未知类别的新图像，对吧，你以前从未见过这种图像，一张猫的图像，首先把它嵌入这个表示空间。如果视觉编码器训练得很好，它就会被嵌入到 dot \[字幕疑误，可能指 dog\] 的图像 embeddings 附近，因为视觉上相似的图像会被嵌入相似的 embedding 空间，对吧？更重要的是，因为表示空间也包含词 embeddings，而且词 embeddings 的结构塑造得很好，cat 的词 embedding 就会

### [44:28](https://www.youtube.com/watch?v=IDaMEG_zY6A&t=2668s) · b000052

**English**

very close to the word embedding for dog right so visually the visual embeddings go to where the right position is where all the visual embeddings And then a word embedding for cat also goes into the right position relative to other word embeddings. Which basically means if you just do nearest neighbor of the image embedding with the words, you will be able to predict that this is a cat using zeroot, right? Without ever training a model to predict cat for this image, right? So that's uh what they mean by zero shot transfer. And again the key idea is that if you have this embedding space where the images and their embeddings and the text and embeddings are all aligned then you can leverage the structure right so that you could do very quick inference for new images.

**中文**

非常接近 dog 的词 embedding，对吧？所以，从视觉上说，视觉 embeddings 会到达正确的位置，所有视觉 embeddings 所在的位置。而 cat 的词 embedding 也会到达相对于其他词 embeddings 的正确位置。这基本上意味着，如果你只在图像 embedding 与词之间做最近邻（nearest neighbor）搜索，就能用 zeroot \[字幕疑误，可能指 zero-shot\] 预测这是一只猫，对吧？无需曾经训练一个模型，针对这张图像预测 cat，对吧？这就是他们所谓的 zero-shot transfer。关键思想仍然是，如果你有这样一个 embedding 空间，其中图像及其 embeddings、文本及其 embeddings 都对齐，那么你就可以利用其中的结构，对新图像进行非常快速的推理。

### [45:18](https://www.youtube.com/watch?v=IDaMEG_zY6A&t=2718s) · b000053

**English**

Uh again recall this falls under the co-learning because only images are used at test time right the model only ever just takes in this image and makes a prediction is not using image and text or using any additional information so it's fair comparison and in this case it was able to perform zeroot image classification.

**中文**

呃，再回顾一下，这属于 co-learning，因为测试时只使用图像，对吧？模型始终只是接收这张图像并进行预测，没有使用图像加文本，也没有使用任何额外信息，所以比较是公平的。在这个例子中，它能够执行 zeroot \[字幕疑误，可能指 zero-shot\] 图像分类。

### [45:44](https://www.youtube.com/watch?v=IDaMEG_zY6A&t=2744s) · b000054

**English**

Any questions about this?

**中文**

关于这个有什么问题吗？

### [45:51](https://www.youtube.com/watch?v=IDaMEG_zY6A&t=2751s) · b000055

**English**

So this kind of training objective can be also used to enable enable crossodal transfer. Um okay possibly related to some of these these plasticity or prediction arguments that we were talking about. Nowadays this is very common right nowadays has really been scaled up. So when clip was done you know image text alignment obviously people showed that you know given a new image you could also classify into other categories right but at the same time the image embedding of clip could be used for other image tasks right not just to score similarities with text but it was also generally useful for other object detection or segmentation tasks and likewise the text embeddings for a clip were also separately useful for other text classification tasks. So also all evidence of of co-learning.

**中文**

所以，这种训练目标也能用于实现 crossodal transfer \[字幕疑误，可能指 crossmodal transfer\]。呃，好吧，这可能与我们刚才讨论的一些 plasticity 或预测论点有关。如今这非常常见，而且规模确实已经大幅扩大。当 clip 做图像文本对齐时，显然，人们展示了给定一张新图像，你也能把它分类到其他类别，对吧？但与此同时，clip 的图像 embedding 也可以用于其他图像任务，对吧？不只是给它与文本的相似度打分，它也普遍适用于其他物体检测（object detection）或分割（segmentation）任务。同样，clip 的文本 embeddings 也可以独立用于其他文本分类任务。所以，这些也都是 co-learning 的证据。

### [46:54](https://www.youtube.com/watch?v=IDaMEG_zY6A&t=2814s) · b000056

**English**

Uh now people have also done this for other settings. So robotics vision and touch prediction is very common right? If you have a what the robot sees and what the robot feels, then ideally you want to train this model such that you when I deploy the robot, it can still operate without the sense of touch, right? Maybe when the touch sensors are off and it can still operate without the vision, for example, when the camera is being occluded, right? So you want to maybe train with more modalities and have it deploy the inference when a bunch of modalities are missing and only one of them is present. So a lot of these methods for example they use crossmodal prediction where they predict vision from touch or touch from vision. So they end up with this good align embedding space. So no matter which one you use right one or the other it still makes a good prediction.

**中文**

现在，人们也在其他情形中做了这件事。例如，机器人视觉和触觉预测非常常见，对吧？如果你拥有机器人看到的东西以及它感受到的东西，那么理想情况下，你希望这样训练模型：部署机器人时，它即使没有触觉也能工作，对吧？也许触觉传感器关闭了；它也能在没有视觉时继续工作，比如摄像头被遮挡时，对吧？因此，你可能希望用更多模态训练，并在许多模态缺失、只剩一个模态时部署它进行推理。所以，这些方法中有很多会使用跨模态预测（crossmodal prediction），例如从触觉预测视觉，或从视觉预测触觉。最终，它们得到一个良好的对齐 embedding 空间。因此，无论使用哪一个，对吧，这个或那个，它仍然能做出良好预测。

### [47:50](https://www.youtube.com/watch?v=IDaMEG_zY6A&t=2870s) · b000057

**English**

Yeah. So here's some examples of uh doing vision touch alignment for robotics.

**中文**

是的。这里是一些为机器人进行视觉触觉对齐的例子。

### [48:03](https://www.youtube.com/watch?v=IDaMEG_zY6A&t=2883s) · b000058

**English**

Okay, last way of doing co-learning which is very similar to alignment is this idea of translation. So fusion and alignment we saw this extra modality B that was supplementing it at the input level. Uh in this translation space you have this other modality B that is being a prediction target right it's supplementing it at the output level. So during training you would have a you learn some embedding you would use that to predict B while at the same time predicting your label you're doing this multitask prediction and then you once you've done you're just using this pathway you're just using A right so B is only provided as a training signal and then subsequently uh removed and not used during testing.

**中文**

好了，最后一种 co-learning 方式，与 alignment 非常相似，就是 translation。对于 fusion 和 alignment，我们看到额外模态 B 在输入层面起补充作用。而在这种 translation 情形中，另一个模态 B 是预测目标，对吧？它在输出层面起补充作用。因此，在训练期间，你有 a，学习某个 embedding，用它预测 B，同时预测你的标签，进行这种多任务预测。然后，完成之后，你只使用这条路径，只使用 A，对吧？所以，B 仅作为训练信号提供，随后被移除，在测试期间不使用。

### [48:58](https://www.youtube.com/watch?v=IDaMEG_zY6A&t=2938s) · b000059

**English**

uh a little evidence for this. So we we did um one work back then when we're looking at human spoken language. So we uh did exactly the example we discussed where you know a person was saying something and instead of learning these representations so it will always require you to look at the person's what they say and their voice we learn these kind of crossmodal predictive representations. So you took the language that a person was saying, you learn a representation that was able to imagine what their facial expressions were like, right? In this case, you probably imagine that the person was smiling and at the same time use that representations to predict the sentiment, right? Positive or negative. So this is an example of crossmodel translation because you know your your other modality is used as a prediction target and when you're doing inference on a model that you've trained it will just be language coming in going to the representation and making a prediction.

**中文**

呃，这里有一点证据。当时，我们在研究人类口语时做过一项工作。我们做的正是刚才讨论的那个例子：一个人在说话，不是学习那种始终要求你查看这个人所说的话以及声音的表示，而是学习这种跨模态预测表示。你拿到一个人说出的语言，学习一个能够想象其面部表情是什么样的表示，对吧？在这个例子中，你可能会想象这个人在微笑，同时使用那个表示来预测情感（sentiment），对吧？正面还是负面。因此，这是 crossmodel translation \[字幕疑误，可能指 crossmodal translation\] 的例子，因为另一个模态被用作预测目标。而当你对训练好的模型进行推理时，只会有语言输入，进入表示，然后做出预测。

### [49:56](https://www.youtube.com/watch?v=IDaMEG_zY6A&t=2996s) · b000060

**English**

So you would not need vision at test time. Uh one thing we found that in some of these translation approaches sometimes a model can tend to ignore the prediction of the other modality. Right? If it's just easy to detect the sentiment was positive and this objective was really hard, the model just wouldn't do it. So another signal you can give to the model is not just forward translation but also backward translation. So you would have the model taking in language, predict the embedding, imagine what the person's facial expressions are using what the model predicted as the facial expressions, predict back the embedding and predict what the language would be given those facial expressions, right? And you want the this whole cycle of language to predicted vision back to the language to be consistent with the original snippet of text.

**中文**

所以，测试时不需要视觉。我们发现，在某些 translation 方法中，模型有时会倾向于忽略对另一个模态的预测，对吧？如果检测正面情感很容易，而这个目标很难，模型就不会去做。因此，你可以给模型的另一个信号，不仅是正向翻译（forward translation），还有反向翻译（backward translation）。让模型接收语言，预测 embedding，想象那个人的面部表情，再使用模型预测出的面部表情，反过来预测 embedding，并预测给定那些面部表情时语言会是什么，对吧？你希望整个从语言到预测视觉、再回到语言的循环，与原始文本片段保持一致。

### [50:52](https://www.youtube.com/watch?v=IDaMEG_zY6A&t=3052s) · b000061

**English**

So we call it cyclic translations from visual back to language. Uh but all this is just to learn better representations so that you know again during testing you can do this co-learning where you use the representation and you don't use vision to predict the label.

**中文**

所以，我们把它称作从视觉返回语言的循环翻译（cyclic translations）。但所有这些都只是为了学习更好的表示，这样在测试期间，你仍然可以进行这种 co-learning：使用这个表示，不使用视觉，来预测标签。

### [51:18](https://www.youtube.com/watch?v=IDaMEG_zY6A&t=3078s) · b000062

**English**

Great. Uh several other examples. This is quite useful for compositionality uh and reasoning. So in some of these visual reasoning problems um it is very helpful for the model to kind of explicitly verbalize right all these very complex relationships like for example explicitly verbalizing that this is a red cross that is below a square instead of just processing the image. So sometimes it helps to translate the image to the text. Uh people have done this for pre-training as well. So BERT was taking text masking things out and predicting what the missing tokens were. Uh series of approaches that use visual supervision to pre-train language models, right? So you can try to imagine what humans look like, what uh speaking

**中文**

很好。呃，还有几个其他例子。这对 compositionality 和 reasoning 很有用。在一些视觉推理问题中，让模型显式地用语言描述所有这些非常复杂的关系，会很有帮助。比如，显式地说出这是一个位于正方形下方的红色十字，而不只是处理图像。因此，有时把图像翻译成文本会有帮助。人们也把这用于预训练。BERT 接收文本，遮掉一些内容，再预测缺失的 tokens 是什么。有一系列方法使用视觉监督（visual supervision）来预训练语言模型，对吧？你可以尝试想象人类看起来是什么样，呃，说话

### [52:14](https://www.youtube.com/watch?v=IDaMEG_zY6A&t=3134s) · b000063

**English**

and listening look like. basically imagining what things look like um as a crossmodal prediction training objective instead of just predicting text. Some data sets that people use for this include these visual storytelling data sets where you have paired images and nice descriptions also large scale video data sets where you have no visual scenes happening while people are speaking. So you have this paired data. So now this crossodal training is done. uh you are just using the the subsequently trained language model and you know text classification during testing.

**中文**

和倾听是什么样。基本上，就是想象事物看起来的样子，把它作为 crossmodal prediction 的训练目标，而不是仅仅预测文本。人们为此使用的一些数据集包括视觉故事讲述（visual storytelling）数据集，其中有配对的图像和很好的描述；还有大规模视频数据集，其中人们说话时没有视觉场景发生 \[原文如此\]。所以，你有这种配对数据。现在，这种 crossodal \[字幕疑误，可能指 crossmodal\] 训练完成之后，你只使用随后训练出来的语言模型，在测试期间进行文本分类。

### [52:56](https://www.youtube.com/watch?v=IDaMEG_zY6A&t=3176s) · b000064

**English**

One final example where co-learning can be very helpful is when your original prediction task has very low resolution. Right? So here's a example of some work in the more medical space uh over here trying to use breathing signals to predict whether a person has some disease right uh in fact people can show that just from how people are breathing when they're sleeping predict whether they are showing signs of Parkinson's disease or Alzheimer's disease amazing stuff so over here you have um breathing signals you have a breathing encoder PD is Parkinson's disease and you are training a classifier for whether the likelihood of somebody has some disease and also the severity of that disease. Right? This seems like a very classic supervised learning problem. But obviously this is really hard to train because you have hours, tens of

**中文**

最后一个 co-learning 非常有帮助的例子，是原始预测任务的分辨率非常低的情况，对吧？这里是医疗领域的一项工作示例，试图使用呼吸信号预测一个人是否患有某种疾病，对吧？实际上，人们能够证明，仅凭睡眠时的呼吸方式，就能预测人们是否表现出帕金森病（Parkinson's disease）或阿尔茨海默病（Alzheimer's disease）的迹象，非常惊人。所以，这里有呼吸信号，有一个呼吸编码器，PD 是 Parkinson's disease，你训练一个分类器，预测某人患有某种疾病的可能性，以及疾病的严重程度，对吧？这看起来是个非常经典的监督学习问题。但显然，它非常难训练，因为你有数小时、数十

### [53:52](https://www.youtube.com/watch?v=IDaMEG_zY6A&t=3232s) · b000065

**English**

hours of people sleeping, right? People sleep 8 to 10 hours a day. You have a lot of hours and you only have like a single bit supervision of whether they have Parkinson's. Right. Right. one for some people, zero for most people. So that is a very very uh discrepant ratio between how much data you have and a very little signal that you have. So it can be helpful to add another modality as a prediction objective. Ideally another modality with the same information resolution as the input. Right? So there is no longer this discrepancy and you actually have a rich training signal to lend better representations. So over here you can for example try to predict the EEG the brain waves right because brain waves that a person is um is showing when they're sleeping is at a similar information density to their you know other breathing signals. So now this

**中文**

小时的人类睡眠数据，对吧？人每天睡 8 到 10 小时。你有很多小时的数据，却只有大约一个比特的监督信号，表示他们是否患有帕金森病，对吧？对。某些人是 1，大多数人是 0。因此，数据量与极少的监督信号之间比例非常悬殊。所以，把另一个模态作为预测目标添加进来可能会有帮助。理想情况下，是与输入具有相同信息分辨率的另一个模态，对吧？这样就不再有这种差距，而且你实际上拥有丰富的训练信号，可以学到更好的表示。因此，这里例如可以尝试预测脑电图（electroencephalogram, EEG），也就是脑波，对吧？因为一个人在睡眠时表现出的脑波，与其他呼吸信号具有类似的信息密度。所以，现在这个

### [54:49](https://www.youtube.com/watch?v=IDaMEG_zY6A&t=3289s) · b000066

**English**

signal is very high information very high density forces the model to learn better representations which can be useful for predicting your Parkinson's disease that you actually care about. So here's what it is. That was the audio of people breathing. Lots of data, high resolution. You predict EG activity throughout the night as an extra signal, right? About similar resolution, same time frame, same sampling rate. Uh that gives you good features. Um but even though you don't really care about whether you're predicting EEG correctly, the features themselves are now more useful for your disease prediction. So cross model prediction can be useful to also deal with um data that comes in at very different resolutions and to get more training signal for your models.

**中文**

信号的信息量很高、密度很高，会迫使模型学习更好的表示，而这些表示可以用于预测你真正关心的帕金森病。因此，这里就是具体情况。那是人们呼吸的音频。大量数据，高分辨率。你把预测整夜的 EG \[字幕疑误，可能指 EEG\] 活动作为额外信号，对吧？分辨率大致相似，相同时间范围，相同采样率。呃，这会给你良好的特征。即使你实际上并不关心 EEG 是否预测正确，这些特征本身现在对疾病预测更有用。因此，cross model prediction \[字幕疑误，可能指 crossmodal prediction\] 也可以帮助处理分辨率差异很大的数据，并为模型获得更多训练信号。

### [55:49](https://www.youtube.com/watch?v=IDaMEG_zY6A&t=3349s) · b000067

**English**

Any final questions?&gt;&gt; Yes.&gt;&gt; Why did they choose the modality not the reasoning behind it. Like that seems kind of like a shot in the dark, but like&gt;&gt; Yeah.&gt;&gt; Yeah.&gt;&gt; Yeah. Yeah.&gt;&gt; Um people have I'm sure it was a mix of some doctors and some reported medical literature showing that this was possible plus I mean obviously you get access to data. So you know through collaborators um probably these folks um found a right partnership with the right collaborator who was able to both you know give theoretical backing that this was possible and would give access to data sets where this is possible but I think um this is what 2022 so probably was done in 2020 because journal takes a long time and recently people have shown that like recording

**中文**

最后还有什么问题吗？&gt;&gt; 有。&gt;&gt; 他们为什么选择这个模态，不是背后的推理。就是，这看起来有点像盲目尝试，但是——&gt;&gt; 对。&gt;&gt; 对。&gt;&gt; 对，对。&gt;&gt; 呃，人们已经，我相信这结合了一些医生的意见，以及一些已发表的医学文献，表明这是可能的；另外，显然你还得能获得数据。所以，通过合作者，这些人可能找到了合适的合作关系，找到了合适的合作者，对方既能提供理论支持，说明这可行，也能提供可以这样做的数据集。不过，我想，这是哪年，2022 年，所以可能是在 2020 年做的，因为期刊发表需要很长时间。而最近人们已经表明，记录

### [56:44](https://www.youtube.com/watch?v=IDaMEG_zY6A&t=3404s) · b000068

**English**

your sleep can indicator of so many things so many types of um uh know cognitive you know related diseases breathing, heart rate, lung related diseases. Yeah, cool stuff. Okay, great.

**中文**

你的睡眠可以指示很多事情，很多种，呃，你知道，认知相关疾病、呼吸、心率、肺部相关疾病。是的，很酷的东西。好了，很好。

### [57:11](https://www.youtube.com/watch?v=IDaMEG_zY6A&t=3431s) · b000069

**English**

All right. In the last uh last 15 minutes, I'll cover this third part. So very exciting. So first uh as a recap you know we've seen transfer right. So you have you know really big based models that you can then start you know fine-tuning or doing multitask learning transfer to other settings that you care about. Um this is really good when you have good pre-trained models and you don't mind you know keeping to fine-tune or adding prediction heads to your model. And then we saw co-learning which actually had to dive the deepest right you actually had to open up the representation layer to add for example a fusion signal or an alignment objective or a prediction objective. So you actually had to dig deep and open up the box of the model. And then nowadays uh there's a lot of work at the model wrapper level uh which you can think about as inducing behaviors um without actually opening up and modifying the model itself right um

**中文**

好了，在最后，呃，最后 15 分钟，我会讲第三部分。非常令人兴奋。首先回顾一下，我们已经看过 transfer，对吧？你有非常大的基础模型，然后可以开始微调，或者做 multitask learning，迁移到你关心的其他情形。当你有良好的预训练模型，而且不介意继续微调或给模型添加预测头时，这非常有用。然后我们看了 co-learning，它实际上需要深入得最深，对吧？你必须打开表示层，添加比如融合信号、alignment 目标或预测目标。因此，你确实必须深入进去，打开模型这个盒子。而如今，有很多工作发生在模型包装层（model wrapper）层面，你可以把它理解为诱导行为，而不真正打开并修改模型本身，对吧？呃，

### [58:08](https://www.youtube.com/watch?v=IDaMEG_zY6A&t=3488s) · b000070

**English**

especially nowadays you know people want to do all sorts of things at the API or wrapper or or harness level so we call this model induction but uh in fact a lot of this stuff you know is done way back in the day so I'll show you one example of a model induction approach where you and have the model improve and share information with other models and get better over time. Um so the high level definition is that you keep individual unimodal models separate but you're trying to induce some common behavior across them. Okay. So this paper is called uh selfraining. Self training is a warm-up which algorithm that I'll show you which achieves model induction within a single modality and then we'll extend it to co-raining which is basically self training across uh two modalities. Self training approach probably been a long for a very long time and this p

**中文**

尤其是现在，人们希望在 API、wrapper 或 harness 层面做各种事情。所以我们把它称作 model induction，但实际上，其中很多东西很久以前就有人做了。我会展示一个 model induction 方法的例子，你可以让模型改进，与其他模型共享信息，并随着时间变得更好。整体定义是，你保持各个单模态模型独立，但试图在它们之间诱导一些共同行为。好了。这篇论文叫作 selfraining \[字幕疑误，可能指 self-training\]。自训练（self-training）是我要展示的一个热身算法，它在单一模态内实现 model induction，随后我们会把它扩展到 co-raining \[字幕疑误，可能指 co-training\]，基本上就是跨两个模态的 self-training。Self-training 方法可能已经存在很长时间了，而这篇 p

### [59:04](https://www.youtube.com/watch?v=IDaMEG_zY6A&t=3544s) · b000071

**English**

this paper which actually made it more applicable to deep learning and was quite rigorous in its analysis but this stuff existed for a long time. So how can transfer happen? So we're going to start with um some data, some label data, right? X and Y label data. And we're going to have assumed that we're going to assume that we have a bunch of unlabelled data, right? What selftraining does is that it first trains a classifier on the label data that we have, right? probably an imperfect classifier because often times you have very little limited data to begin with. You're going to use the classifier to label some unlabelled data in your pool of unlabelled data, right? You're going to label it and specifically you're going to label the ones that are the model is the most confident on, right? So as you're labeling, you know, usually some soft

**中文**

这篇论文实际上让它更适用于 deep learning，并且分析相当严谨，但这些东西已经存在很长时间了。那么，迁移如何发生？我们从一些数据、一些带标签数据开始，对吧？X 和 Y，带标签数据。我们假设有一批无标签数据，对吧？Self-training 首先在已有的带标签数据上训练一个分类器，对吧？这可能是一个不完美的分类器，因为通常一开始你拥有的数据非常少、非常有限。然后你会用分类器，给无标签数据池中的一些无标签数据打标签，对吧？你会给它们打标签，具体来说，会给模型最有信心的那些数据打标签，对吧？在打标签时，通常会有一些 soft

### [1:00:00](https://www.youtube.com/watch?v=IDaMEG_zY6A&t=3600s) · b000072

**English**

max. You can look at softmax or confidence to see if it's you know uniform softmax probably not going to be a good label that it generates very confident softmax I'm going to use that to to label the data right and this allows you to kind of self-label some of these unlabelled data points that you have and essentially you can add it to your training set thereby enlarging your training data set. Okay. And then you would go back to step one which is to now train and update this classifier that you have on this slightly enlarged training set consisting of the original label samples which you know are 100% labels good labels and also this expanded set of labels you have made yourself using your model. So you then retrain your classifier on this larger training set. Go back and label more of these unlabelled samples that you have left. uh choose the most confident ones and use this to keep iteratively enlarging your training set, training

**中文**

max。你可以查看 softmax 或置信度：如果 softmax 分布均匀，它生成的标签可能就不好；如果 softmax 非常有信心，我就用它来给数据打标签，对吧？这让你能够对现有的一些无标签数据点进行自标注，基本上可以把它们加入训练集，从而扩大训练数据集。好了。然后回到第一步，在这个略微扩大的训练集上训练并更新现有分类器。这个训练集由原始带标签样本组成，你知道这些是 100% 的标签、好的标签，还包括你用模型自己生成的这批扩展标签。因此，你在这个更大的训练集上重新训练分类器。再回去给剩余的更多无标签样本打标签，选择最有信心的那些，用这种方式不断迭代地扩大训练集，训练

### [1:00:56](https://www.youtube.com/watch?v=IDaMEG_zY6A&t=3656s) · b000073

**English**

your model, labeling more and and so on. And uh and during testing you would just you know use the classifier. So this self training this algorithm has been along around for a long time. Of course nowadays we see this a lot in in your data augmentation right for example you're using a model to generate model to generate more data that you're adding to your training set. We see this a lot in your LLMs. We're using LLMs to filter out or generate better examples that you're then adding to the training. But even in classification space, right, this has um been around for a while, right? You can think about what it looks like visually where you have uh originally your label samples, two colors, and you have your classifier. You might uh have some unlabelled samples. That's what they look like. And you can see that some of them are wrongly labeled, right? And that by the

**中文**

模型，标注更多数据，等等。在测试期间，你就使用这个分类器。因此，这个 self-training 算法已经存在很长时间了。当然，如今我们在数据增强（data augmentation）中经常看到它，比如用模型生成，模型生成更多数据，再加入训练集。我们在 LLMs 中经常看到这种做法。我们使用 LLMs 筛选或生成更好的例子，然后加入训练。但即使在分类领域，这也已经存在一段时间了，对吧？你可以从视觉上理解：最初有带标签样本，两种颜色，以及一个分类器。你可能还有一些无标签样本。它们看起来是这样。你会看到其中有些被错误标注了，对吧？而那是由

### [1:01:52](https://www.youtube.com/watch?v=IDaMEG_zY6A&t=3712s) · b000074

**English**

current classifier and your model with pseudo label the ones that are most confident, right? And in this case visually, you want to think about the ones that is most confident as being the furthest away from decision boundary, right? You're super confident those should be red and you're super confident those two should be blue. And then those two in the middle, you're not very confident, right? So you don't want to label the ones that you're not confident. definitely label the ones that you are super confident. So those slightly shaded red and blue become labeled by your model and add it to your data set. You retrain it, right? Because there's a bunch of blue points over there. You retrain it and now your decision boundary moves a little bit, right? Moves uh rotates a little bit towards this side, right? Then once it starts rotating towards this side, you can see just as an example, it used to get that red triangle incorrect. But now it gets both these red and blue

**中文**

当前分类器造成的。你的模型会给最有信心的那些样本生成伪标签（pseudo-label），对吧？在这个视觉示例中，你可以把最有信心的那些理解为离决策边界（decision boundary）最远的样本，对吧？你非常确信那些应该是红色，也非常确信那两个应该是蓝色。中间那两个你不太有信心，对吧？所以，不要给没有信心的那些样本打标签。一定给那些非常有信心的样本打标签。于是，那些颜色稍浅的红点和蓝点就被模型标注，并加入数据集。你重新训练，对吧？因为那里有一批蓝点。重新训练之后，决策边界就稍微移动了一点，对吧？朝这一边稍微旋转了一点。然后，当它开始朝这一边旋转，你会看到，仅举个例子，它原本把那个红色三角形分错了。但现在，它把这两个红色和蓝色

### [1:02:42](https://www.youtube.com/watch?v=IDaMEG_zY6A&t=3762s) · b000075

**English**

triangles correct because of this uh sequence of pseudo labeling. So now that is correctly labeled. Okay. So several key ideas here, right? It's about the model. Not really changing a model itself. you're just using a model as the API to label more data points based on confidence and these can then be added to improve the training of different models. Right? This idea that you're labeling only the most confident ones and gradually shifting the model boundary is important over time because if you just labeled everything and give it to your model, it will be the same performance as the original model.

**中文**

三角形都分对了，这是这一连串伪标注（pseudo-labeling）的结果。所以，现在它被正确标注了。好了，这里有几个关键思想，对吧？重点在于模型，并不是真的改变模型本身。你只是把模型当作 API，基于置信度给更多数据点打标签，然后可以把这些数据点加进去，改进不同模型的训练，对吧？只标注最有信心的样本，并逐步移动模型边界，这一点随着时间推移很重要。因为，如果你直接给所有数据打标签，再交给模型，它的性能就会与原始模型相同。

### [1:03:31](https://www.youtube.com/watch?v=IDaMEG_zY6A&t=3811s) · b000076

**English**

So um code training is another very famous perhaps the most famous multimodal algorithm from a paper from 1998 right um and it's a very theoretically grounded method that allows you to essentially improve two classifiers on two modalities over time right it's an extension of selftraining to two views so you have x1 x2 you're going to have two classifiers and again you have some label multimodal data and a lot of unlabelled data, right? Uh there are several key assumptions where redundancy is very important, right? As you'll see, uh redundancy where both views have similar information is going to be very important. And so what the coderaining algorithm does is that you would train classifiers f\_sub\_1 and f\_sub\_2. F\_sub\_1 on the first modality

**中文**

所以，code training \[字幕疑误，可能指协同训练 co-training\] 是另一个非常著名，也许是最著名的多模态算法，来自 1998 年的一篇论文，对吧？它是一种具有非常扎实理论基础的方法，基本上让你能够随着时间逐步改进两个模态上的两个分类器，对吧？它是 self-training 向两个视图的扩展。所以你有 x1、x2，会有两个分类器，同样也有一些带标签多模态数据，以及大量无标签数据，对吧？这里有几个关键假设，其中冗余性（redundancy）非常重要，对吧？正如你们将看到的，两个视图具有相似信息的 redundancy 会非常重要。因此，coderaining \[字幕疑误，可能指 co-training\] 算法的做法是，训练分类器 f\_sub\_1 和 f\_sub\_2。F\_sub\_1 在第一个模态的

### [1:04:26](https://www.youtube.com/watch?v=IDaMEG_zY6A&t=3866s) · b000077

**English**

is labeled data and F\_sub\_2 on the second modality's label data and you will essentially use F1 and F\_sub\_2 to self label data from the other modality. So your classifier F\_sub\_1 will be used to label the most confident samples and assign that label to train F\_sub\_2, right, the other classifier. And then you're going to use your classifier f\_sub\_2 to label the examples where it is most confident on and use that label to then subsequently train F1. Right? So you have this cross trainining going on. Right? The first modality classifier labels something that second modalities classifier is trained on. Second modalities classifier labels something that the first classifier is trained on. Right? So now you have this exchange of information between the two modalities and you

**中文**

带标签数据上训练，F\_sub\_2 在第二个模态的带标签数据上训练，然后基本上用 F1 和 F\_sub\_2 为另一个模态的数据自动打标签。所以，你的分类器 F\_sub\_1 用来标注最有信心的样本，并把那个标签用于训练 F\_sub\_2，对吧，也就是另一个分类器。然后，你会用分类器 f\_sub\_2 标注它最有信心的例子，再用那个标签随后训练 F1，对吧？所以，你在进行这种交叉训练，对吧？第一个模态的分类器给某些东西打标签，第二个模态的分类器用这些东西训练；第二个模态的分类器给某些东西打标签，第一个分类器用这些东西训练，对吧？现在，两个模态之间就有了这种信息交换，而你

### [1:05:22](https://www.youtube.com/watch?v=IDaMEG_zY6A&t=3922s) · b000078

**English**

repeat until you have no more samples left. And this has provable guarantees to um essentially get better and better F1 and F2 classifiers over time.

**中文**

不断重复，直到没有剩余样本。而且，这具有可证明的保证，基本上能够让 F1 和 F2 分类器随着时间变得越来越好。

### [1:05:40](https://www.youtube.com/watch?v=IDaMEG_zY6A&t=3940s) · b000079

**English**

Right? Any questions about code training?

**中文**

对吧？关于 code training \[字幕疑误，可能指 co-training\]，有什么问题吗？

### [1:05:51](https://www.youtube.com/watch?v=IDaMEG_zY6A&t=3951s) · b000080

**English**

Modern instantiations are numerous, right? Uh in video people use classifiers for RGB to label data for a video classifier to train on uh sorry optical flow classifier to train on and then they use optical flow classifier to train the RGB model. So it's kind of co-raining can lead to really good performance. Here's an example. Another example of co-raining between different language models, right? You have a GBT3 model that label some examples that BERT can be fine- tuned on and BERT allows you to get some embeddings for confidence samples that you know the large language model can be further fine-tuned on. So various forms of information exchange between different language models. Nowadays a lot of these multi- aent LLMs debates are also seen as co-raining right one

**中文**

现代实例非常多，对吧？在视频中，人们使用 RGB 分类器来标注数据，供视频分类器训练，抱歉，是供光流（optical flow）分类器训练，然后再用 optical flow 分类器来训练 RGB 模型。所以，这种 co-raining \[字幕疑误，可能指 co-training\] 能够带来很好的性能。这里是一个例子。另一个例子是不同语言模型之间的 co-raining，对吧？你有一个 GBT3 \[字幕疑误，可能指 GPT-3\] 模型，标注一些例子，BERT 可以在这些例子上微调；而 BERT 可以让你为高置信度样本获得一些 embeddings，大语言模型又可以在这些样本上进一步微调。因此，不同语言模型之间存在各种形式的信息交换。如今，很多多智能体（multi-agent）LLMs 辩论也被看作 co-raining，对吧？一个

### [1:06:48](https://www.youtube.com/watch?v=IDaMEG_zY6A&t=4008s) · b000081

**English**

language model you know labels some some data and gives it to another language model to then make an inference on and they label some data and the other language model makes inference on. So all these are examples of of code training where you have different APIs keeping them the same not really updating the model but having exchange of information between them.

**中文**

语言模型标注一些数据，交给另一个语言模型进行推理；它们再标注一些数据，另一个语言模型再进行推理。所以，这些都是 code training \[字幕疑误，可能指 co-training\] 的例子：你有不同的 API，保持它们不变，并不真正更新模型，而是让它们交换信息。

### [1:07:18](https://www.youtube.com/watch?v=IDaMEG_zY6A&t=4038s) · b000082

**English**

All right. Uh so to summarize lots of ways in which you know you're not just limited to supervised training or or fine-tuning reasoning for a particular modality or task that you care about, right? Lots of ways of looking at transfer, right? You starting from one model and you're expanding what is transferred to by making it more multimodal and multitask in during transfer. uh this usually requires some amount of fine-tuning and adding classification heads and adding you know new inputs.co-learning which is this new setting where you have a classification that you care about and you're adding and modifying the training process so that another modality is reduced either through fusion or alignment or through you know cross model prediction during training and finally induction based approaches where each of these approaches start as APIs and and the

**中文**

好了。总结来说，有很多方式，你不只是局限于针对自己关心的某个模态或任务进行监督训练，或者微调推理，对吧？看待迁移的方式有很多。你从一个模型开始，在迁移期间让它更加多模态、更加多任务，从而扩展迁移的对象。这通常需要一定程度的微调、添加分类头，以及添加新输入。Co-learning 是一种新设定：你有自己关心的分类任务，通过添加和修改训练过程，让另一个模态在训练期间通过 fusion、alignment，或者 cross model prediction \[字幕疑误，可能指 crossmodal prediction\] 被 reduced \[原文如此，可能指 introduced\]。最后是基于 induction 的方法，其中每一种方法都以 API 的形式开始，而这些

### [1:08:15](https://www.youtube.com/watch?v=IDaMEG_zY6A&t=4095s) · b000083

**English**

models are kept the same they're making predictions but it's how the predictions are being exchanged and the prediction level to to improvement over time. \[clears throat\] All right, that's all folks. Um, any final questions about co-learning? If not, um, see you next week.

**中文**

模型保持不变，它们进行预测，但关键在于预测如何被交换，以及在预测层面如何随着时间带来改进。\[清嗓子\] 好了，各位，就这些。关于 co-learning，最后还有什么问题吗？如果没有，下周见。
