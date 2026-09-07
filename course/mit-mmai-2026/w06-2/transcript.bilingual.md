# Lecture 8 – Modern Generative AI (MIT How to AI Almost Anything/Multimodal AI, Spring 2026)

_Bilingual transcript · 双语讲稿_

- Channel: Paul Liang
- Source: [YouTube](https://www.youtube.com/watch?v=LGBQ0c_4HBA)
- Duration: 1:15:23
- Caption source: automatic
- Status: complete
- Chinese translation: 91/91
- Translation provider: codex
- Generated: 2026-09-07T07:50:06+00:00

## Transcript · 讲稿

### [00:00](https://www.youtube.com/watch?v=LGBQ0c_4HBA&t=0s) · b000001

**English**

This will be the final lecture uh of new content before the midterm. We're going to continue and finish our discussion on generative AI, especially multimodal generative AI. Before that, couple of announcements. First, David sent out an announcement for getting access to course compute credits. So, some forms that you got to fill out and we'll send you these API keys that you can then use. We have some credits from from Kimy's new foundation models and some other credits that you can use for any of these um these other models. Another very important announcement, uh, Edgar sent out a Google form, uh, collating responses for everybody who needs any extra accommodation for their midterms. Uh, there's been too many emails and people coming up to me after class for me to keep track. So, there's a form. Every request for any accommodation for the midterms will go in there. Okay. Uh it includes any extra timing that you need or any other uh accommodations with

**中文**

这将是期中考试前最后一节讲新内容的课，呃。我们将继续并结束关于生成式 AI（generative AI）的讨论，尤其是多模态生成式 AI（multimodal generative AI）。在那之前，有几个通知。首先，David 发了一则关于获取课程计算额度的通知。所以，有一些表格需要你们填写，然后我们会把这些 API 密钥发给你们，你们就可以使用了。我们有一些来自 Kimy 的新基础模型（foundation models）的额度，还有一些可用于这些，嗯，其他模型的额度。另一个非常重要的通知，呃，Edgar 发了一个 Google 表单，呃，用来汇总所有需要为期中考试安排额外便利措施的同学的回复。呃，邮件太多了，课后也有太多人来找我，我实在记不过来。所以现在有一个表单。所有关于期中考试便利安排的申请都要填在那里。好。呃，包括你需要的任何额外考试时间，或者其他有关

### [00:54](https://www.youtube.com/watch?v=LGBQ0c_4HBA&t=54s) · b000002

**English**

respect to room or testing environment that you need. Um there's as you can see from the form there's also several options for taking a replacement midterm at this point given that some people are away for the whole of next week. Seems like the replacement midterms will take place uh first week after you come back from spring break. So, it' be a couple of options. Monday through Friday, free to take as many options as you can make um the week after spring break. All right. Any questions with regards to um these two announcements for course credits and for any accommodations for your midterms? Yes.

**中文**

考场或考试环境的便利安排。嗯，正如你们在表单中看到的，考虑到有些人下周整周都不在，目前也提供了几个参加替代期中考试的时间选项。看来替代期中考试将在你们春假回来后的第一周举行，呃。所以，会有几个选项。从周一到周五，春假后的那一周，你们能参加哪些时间，就尽量多选一些，嗯。好。关于这两则通知，也就是课程额度和期中考试的便利安排，大家有什么问题吗？有，请说。

### [01:38](https://www.youtube.com/watch?v=LGBQ0c_4HBA&t=98s) · b000003

**English**

I'll check with David. He should have posted it. Maybe he will do it later today. But be on the lookout for an announcement from David about um a form for you to fill out information to get course credits. Um everybody else, I mean again to clarify, I mean these midterm accommodations are for those who have formal departmental um events or or formal know letters from the the office of student affairs. Um, everybody else, you're expected to be here for the midterm on Thursday and I will not be able to give accommodations for people who have travel that is not prescribed by the institute or accommodations outside those approved by the institute.&gt;&gt; All right.&gt;&gt; Is there any information about the term?&gt;&gt; I'll be doing a midterm review next Tuesday and the midterm review next Thursday. What kind of information are you looking

**中文**

我会和 David 确认一下。他应该已经发了。也许他今天晚些时候会发。不过请留意 David 的通知，嗯，里面会有一个表单，让你们填写信息以获得课程额度。嗯，至于其他所有人，我是说，再澄清一下，我是说，这些期中考试便利安排是面向有正式院系活动，或者有学生事务办公室正式证明信的同学。嗯，其他所有人，你们都应该在周四到这里参加期中考试。对于并非学校规定的出行，或者学校批准范围之外的便利安排，我无法提供。&gt;&gt; 好。&gt;&gt; 有关于 term \[字幕疑误，可能指 midterm\] 的信息吗？&gt;&gt; 我会在下周二进行期中复习，下周四也进行期中复习。你想了解什么样的

### [02:35](https://www.youtube.com/watch?v=LGBQ0c_4HBA&t=155s) · b000004

**English**

for? It's a standard midterm. There will be some multiple choice, some short answer questions, some technical questions, and some open-ended questions. It will cover what we discuss in class up until today's lecture. So, next Tuesday, no more new information. It will be a review, and next Thursday will be the midterm.&gt;&gt; I'm going to make sure that even with the accommodations of 1.5 times duration, we'll be able to finish everything in the class. So midterm will probably take 50 minutes. People who have accommodations can go up to 1.5 time 75 minutes. You'll be done within the class period. You'll be performed here.

**中文**

信息？这是一次标准的期中考试。会有一些选择题、一些简答题、一些技术题，以及一些开放式问题。范围涵盖我们课堂上讨论的内容，直到今天这节课为止。所以，下周二不再讲新内容。那节课会复习，下周四是期中考试。&gt;&gt; 我会确保，即使有考试时长为 1.5 倍的便利安排，我们也能在这节课内完成所有内容。所以期中考试大概需要 50 分钟。有便利安排的同学可以延长到 1.5 倍，也就是 75 分钟。你们会在这节课的时间内完成。你们会在这里被进行 \[原文表述不清\]。

### [03:17](https://www.youtube.com/watch?v=LGBQ0c_4HBA&t=197s) · b000005

**English**

All right. Any final questions about announcements? Yes.&gt;&gt; We're going to be lecturing the same day.&gt;&gt; No, it just be a midterm. No, no lectures. All right. So let me finish our discussion of these uh these generative models. Uh as you recall from last Tuesday we started discussing text to image generation. We started giving an introduction to some of these latent variable generative models and VAEs. We'll continue that discussion recap a little bit and then move on to diffusion models and flow matching which are so-called state-of-the-art generative models. Today we'll extend uh their application from images to other modalities and see that there's uh some unification going on. Lots of the generative models can now be applied for all sorts of modalities as is a theme of our class and then I'll discuss how we can better control and some potential ethical concerns of using these

**中文**

好。关于这些通知，还有最后的问题吗？有，请说。&gt;&gt; 同一天还会讲课吗？&gt;&gt; 不，那天只有期中考试。不，不讲课。好。那么让我结束关于这些，呃，这些生成模型（generative models）的讨论。呃，你们记得，上周二我们开始讨论文本到图像生成（text to image generation）。我们开始介绍一些潜变量生成模型（latent variable generative models）和变分自编码器（variational autoencoders, VAEs）。我们会继续这个讨论，稍微回顾一下，然后讲扩散模型（diffusion models）和流匹配（flow matching），也就是所谓最先进的生成模型。今天我们会把它们的应用从图像扩展到其他模态（modalities），看看其中正在发生的一些统一化。许多生成模型如今可以应用于各种模态，这也是我们课程的一个主题。然后我会讨论如何更好地控制它们，以及使用这些

### [04:13](https://www.youtube.com/watch?v=LGBQ0c_4HBA&t=253s) · b000006

**English**

generative models. So again as a quick recap uh where we are in this 3-week discussion on these latest multimodal foundation models is that we started looking at multimodal data nowadays multimodal contextual sequential data like you know text that you're typing to your language models or visual frames that these models are seeing. And we first saw how we could essentially use these multimodal transformers to learn the alignment between different elements in your modalities. For example, different words in the context with different visual frames or different time steps in the sensor reading. How to align those different uh individual elements and use that to learn better representations. That's really useful for contextualizing your data, fusing your data, and using that to make predictions. Of course, now we're in this foundation model era where we have the power of language models that allow you to flexibly ask any

**中文**

生成模型的一些潜在伦理问题。所以，再快速回顾一下，呃，我们这三周关于最新多模态基础模型的讨论进行到了哪里：我们一开始看的是多模态数据，如今的多模态上下文序列数据（multimodal contextual sequential data），比如你输入到语言模型中的文本，或者这些模型看到的视觉帧。我们首先看了如何基本上使用这些多模态 transformers 来学习不同模态中各个元素之间的对齐（alignment）。例如，上下文中的不同词语与不同视觉帧，或者传感器读数中的不同时间步。如何对齐这些不同的，呃，单个元素，并利用这一点学习更好的表征（representations）。这对于为数据赋予上下文、融合数据，以及利用这些数据进行预测非常有用。当然，我们现在处于基础模型时代，语言模型的能力让你可以灵活地提出任何

### [05:11](https://www.youtube.com/watch?v=LGBQ0c_4HBA&t=311s) · b000007

**English**

question and receive any response and a further rounds of interaction and dialogue with these models. So we then saw how we could connect these pre-trained language models with multimodal data as input and we saw all these adapters that could be used to condition language models with respect to basically any modality right images, video, audio and so on. So at this point you basically have multimodal language models multimodal as input language channel that allows you to ask and answer and uh hold an interaction about those modalities. And finally on Tuesday we we started to look at finishing this this whole schematic by adding multimodal generation on the output as well. And we saw two examples of how you could in addition to generate text as a response, put some of the generated text or the context that the model generates into either a textto image retrieval model. So that model

**中文**

问题，获得任何回应，并与这些模型进行进一步的多轮互动和对话。所以，我们接着看了如何把这些预训练语言模型（pre-trained language models）与作为输入的多模态数据连接起来，也看了所有这些适配器（adapters），它们可以让语言模型以基本上任何模态为条件，对吧，图像、视频、音频等等。所以到了这里，你基本上就有了多模态语言模型：多模态作为输入，语言通道让你能够围绕这些模态提问、回答，并进行互动。最后，在周二，我们开始通过在输出端也加入多模态生成，来补全整个示意框架。我们看了两个例子，说明除了生成文本作为回答以外，你还可以把部分生成文本，或者模型生成的上下文，送入一个文本到图像检索模型（text to image retrieval model）。所以那个模型

### [06:08](https://www.youtube.com/watch?v=LGBQ0c_4HBA&t=368s) · b000008

**English**

will retrieve images from some large database uh that is relevant to the text that it's outputting. And we also started seeing uh how we can also staple textto image generation models. So how these models can generate even images pixel by pixel conditioned on the context and the text that is currently generating. So that's basically part three and that allows you to complete the loop from multimodal input learning these summarized representations of multimodal data and also having multimodal output conditioning both language models and conditioning uh image generative models on the output. So you have multimodal input, multimodal output, which obviously is necessary for for more general and interactive AI systems.

**中文**

会从某个大型数据库中检索与它正在输出的文本相关的图像，呃。我们也开始看，呃，如何把文本到图像生成模型接上去。所以，这些模型如何以当前正在生成的上下文和文本为条件，甚至逐像素地生成图像。这基本上就是第三部分，它让你能够完成这个闭环：从多模态输入，学习多模态数据的这些概括表征，再到多模态输出，同时为语言模型以及输出端的图像生成模型提供条件。所以你就有了多模态输入和多模态输出，这显然是更通用、更具交互性的 AI 系统所必需的。

### [06:57](https://www.youtube.com/watch?v=LGBQ0c_4HBA&t=417s) · b000009

**English**

So again, as a quick recap, we saw some details of both of these. On the retrieval side, we saw that you can start by training these models with interled image and text context. So you might you know there's these like visual storytelling data sets where you have an image and you have some description of what's happening in the image may not be perfect and also may provide more information. They have another image and more descriptions of that images. So all these interle sequences of image and text going to the input of your model. Uh text can directly be tokenized into the model. image needs to go through image encoders and then the adaptors that you will train so that they can also be interpreted as tokens by the model. So you have these interleaf series of image and text representations and then at some point the model starts synthesizing that context and predicting some output right by answering a question or predicting the next context

**中文**

所以，再快速回顾一下，我们看了这两种方法的一些细节。在检索方面，我们看到，可以先用 interled \[字幕疑误，可能指 interleaved，交错排列的\] 图像和文本上下文来训练这些模型。所以你可能，你知道，有一些视觉故事叙述数据集（visual storytelling datasets），其中有一张图像，还有一些描述图像中正在发生什么的文字，这些描述可能不完美，也可能提供更多信息。然后又有另一张图像，以及关于那张图像的更多描述。所以，这些图像和文本的 interle \[字幕疑误，可能指 interleaved\] 序列都输入到模型中。呃，文本可以直接转换成词元（tokens）输入模型。图像需要经过图像编码器（image encoders），然后经过你要训练的适配器，这样它们也能被模型解释为 tokens。所以你会得到这些 interleaf \[字幕疑误，可能指 interleaved\] 的图像和文本表征序列，然后在某个时刻，模型开始综合这些上下文并预测某个输出，对吧，比如回答一个问题，或者预测接下来的上下文

### [07:54](https://www.youtube.com/watch?v=LGBQ0c_4HBA&t=474s) · b000010

**English**

and that context can be used in two paths. One path is for retrieval. So you can look at those text token similarities and use that to score a similarity with respect to image embeddings from a set of images, right? And we saw that's where clip and these align representations are very powerful because they essentially allow you to learn representation spaces where the language context embedding and your image context embedding that are semantically similar are very nearby and things that are different are very far apart. So that's how you can use similarities. We essentially score and find the nearest neighbor image embedding and therefore retrieve the nearest image that corresponds to that completion. So if you're asking about uh some cookies that you have baked, you took a photo, you're asking how should I display these at the farmers market, the model can use those as context and say, you know, I think you should arrange it

**中文**

而这些上下文可以用于两条路径。一条路径是检索。所以，你可以查看那些文本 token 的相似度，并用它来对一组图像中的图像嵌入（image embeddings）进行相似度评分，对吧？我们看到，这正是 clip \[字幕疑误，可能指 CLIP\] 和这些 align \[字幕疑误，可能指 aligned，或模型名 ALIGN\] 表征非常强大的地方，因为它们基本上让你能学到这样的表征空间：语义相似的语言上下文嵌入和图像上下文嵌入彼此非常接近，而不同的东西则相距很远。所以，你可以这样利用相似度。我们基本上会评分并找到最近邻（nearest neighbor）的图像嵌入，从而检索出与该补全文本对应的最近图像。所以，如果你在问一些自己烤的饼干，呃，你拍了一张照片，然后问，应该怎样在农贸市场上陈列它们，模型就可以把这些作为上下文，然后说，你知道，我觉得你应该这样摆放它们

### [08:50](https://www.youtube.com/watch?v=LGBQ0c_4HBA&t=530s) · b000011

**English**

uh by stacking them on top of each other and using a string to tie them together. That could be the text that the model generates. And of course it's very useful to find a visualization of that. So it will retrieve uh the nearest image using your pre-trained clip model of that image describing that uh that caption. So that's a possible retrieval path. We also discussed the generation path, right? You might the model might also complete I think you should space these cookies out evenly and put some you know sugar on top of it. So that may not exist within your database, but the model can use a text to image generation model to essentially generate pixel by pixel an image corresponding to that input caption. Right? So that's what this might look like. And then you can have the model maybe choose whether the retrieved or the generated one or have the user choose whether the retrieved or generated image is more suitable. Uh naturally there's pros and cons to

**中文**

呃，把它们一层层叠起来，再用一根绳子绑在一起。这可能就是模型生成的文本。当然，能找到一种可视化展示会非常有用。所以，它会用你预训练的 clip 模型，检索最接近、能描述那段说明文字的图像，呃。所以这是一条可能的检索路径。我们也讨论了生成路径，对吧？你可能，模型也可能补全成：我觉得你应该把这些饼干均匀摆开，再在上面撒些，你知道，糖。所以，这样的图像可能并不存在于你的数据库里，但模型可以使用文本到图像生成模型，基本上逐像素生成一张与输入说明文字对应的图像。对吧？所以它可能看起来就是这样。然后你可以让模型来选择检索到的图像还是生成的图像，或者让用户选择哪一种更合适。呃，自然，这两种方式都有

### [09:48](https://www.youtube.com/watch?v=LGBQ0c_4HBA&t=588s) · b000012

**English**

both retrieval. You're guaranteed that the images are correct and from some database. No hallucinations possible, but you're limited by the set of images that you can retrieve from generation. You're no longer limited by the set of images you can retrieve from. It can generate any possible image, various resolutions and fidelities. Uh but then you have the possibility of hallucinations and uh inappropriate generations.

**中文**

优缺点。检索方面，你能保证图像是正确的，并且来自某个数据库。不可能产生幻觉（hallucinations），但你会受限于可以检索的图像集合。生成方面，你不再受限于可检索的图像集合。它可以生成任何可能的图像，具有不同的分辨率和保真度（fidelities）。呃，但这样就可能出现幻觉，以及不恰当的生成内容。

### [10:19](https://www.youtube.com/watch?v=LGBQ0c_4HBA&t=619s) · b000013

**English**

So, and we saw some examples, some of these multimodal dialogue models that that started in the past couple of years and now have become the staple of almost any frontier model that you have today, which can essentially allow you to interact across multiple steps through both language based chat and visual input and output. Any questions about this recap so far? completing a story of multimodal input and output representations, decoding language models and adding text to image models on the output.

**中文**

所以，我们还看了一些例子，一些在过去几年里开始出现的多模态对话模型，如今它们已经成为几乎所有前沿模型（frontier models）的标配，基本上让你能够通过基于语言的聊天以及视觉输入和输出，进行多步互动。目前关于这段回顾有什么问题吗？补全多模态输入和输出表征的整个故事，解码语言模型，并在输出端加入文本到图像模型。

### [10:58](https://www.youtube.com/watch?v=LGBQ0c_4HBA&t=658s) · b000014

**English**

Okay, great. So, we also saw as a recap um we went to some technical detail or began to go into some technical detail about how these text to image generation models actually work nowadays. They are they're really state-of-the-art. You can take in text of any combination of objects in any combination. And even though some of these are really rare combinations, these models can still generate very realistic images. And we saw these uh these general schematics where uh usually these images are encoded using some encoder like clip. So you get image embeddings that are nearby text embeddings, right? And that makes it really easy for step two, which is to take in some caption, pass that through a text tokenization model to get text embeddings and use that to predict the image embeddings that it should correspond to, right? And obviously having these image embeddings already very close text embeddings makes

**中文**

好，很好。所以，作为回顾，我们还看了，嗯，我们进入了一些技术细节，或者说开始进入一些技术细节，了解当今这些文本到图像生成模型究竟如何工作。它们真的处于最先进的水平。你可以输入描述任意对象组合、任意组合方式的文本。即使其中一些组合非常罕见，这些模型仍然可以生成非常逼真的图像。我们也看了这些，呃，这些总体示意图，通常这些图像会通过某个编码器来编码，比如 clip。因此你得到的图像嵌入会靠近文本嵌入（text embeddings），对吧？这让第二步变得非常容易，也就是接收一段说明文字，让它经过一个文本词元化（tokenization）模型，得到文本嵌入，再用它预测应该对应的图像嵌入，对吧？显然，让这些图像嵌入已经非常接近文本嵌入，会使

### [11:55](https://www.youtube.com/watch?v=LGBQ0c_4HBA&t=715s) · b000015

**English**

this prediction much easier than if these embeddings were trained independently. So that's the power of these align representations. Once you can use these text embeddings to predict the image embeddings, the final step is to actually decode the image embeddings back into raw image pixel space. That's usually done by diffusion model. Nowadays, we also emphasize that um usually within these image embeddings there's some quantization going on. Why? Because if these image embeddings are continuous and highdimensional, it's often very hard to predict them as a prediction target, right? Predicting highdimensional vectors that are continuous is often very difficult. You can use metrics like mean square error, mean absolute error, but they end up basically just predicting the average of the vector instead of each dimension of the vector equally. So we saw how most of the times there's

**中文**

这个预测比独立训练这些嵌入时容易得多。所以，这就是这些 align 表征的力量。一旦你能用这些文本嵌入预测图像嵌入，最后一步就是把图像嵌入真正解码回原始图像像素空间。这通常由 diffusion model 来完成。如今，我们还强调，嗯，这些图像嵌入内部通常会进行某种量化（quantization）。为什么？因为如果这些图像嵌入是连续且高维的，那么把它们作为预测目标往往很难，对吧？预测连续的高维向量通常非常困难。你可以使用均方误差（mean square error）、平均绝对误差（mean absolute error）之类的指标，但最后它们基本上只是在预测向量的平均值，而不是同等地预测向量的每一个维度。所以我们看到，大多数时候会有

### [12:51](https://www.youtube.com/watch?v=LGBQ0c_4HBA&t=771s) · b000016

**English**

some vector quantization going on within the visual embedding space where the image encoders and decoders within these latent features, right? They first learn some continuous features and they do something like clustering to convert this whole space of continuous features into a into a fixed set of discrete tokens. For example, 8,000 discrete tokens. You can think about them as visual tokens, right? So it might be the first token might be 98, three, 990 and so on. And a different image that is encoded into the image feature space before being decoded is going to map to another set of discrete visual tokens. Visual tokens are now much easier to predict because you can basically predict visual tokens as a 8,000 way classification problems with a 8,000 way softmax um which is known to be much

**中文**

某种向量量化（vector quantization）发生在视觉嵌入空间中，也就是图像编码器和解码器的这些潜在特征内部，对吧？它们先学习一些连续特征，然后做类似聚类（clustering）的操作，把整个连续特征空间转换成一个固定的离散 token 集合。例如，8,000 个离散 tokens。你可以把它们看作视觉词元（visual tokens），对吧？所以，第一个 token 可能是 98、three、990，等等。而另一张图像在解码之前被编码到图像特征空间时，会映射到另一组离散视觉 tokens。视觉 tokens 现在更容易预测，因为你基本上可以把它们当作一个 8,000 类的分类问题（classification problem），通过一个 8,000 路的 softmax 来预测，嗯，众所周知，这会

### [13:48](https://www.youtube.com/watch?v=LGBQ0c_4HBA&t=828s) · b000017

**English**

more stable. Classification is much more stable than highdimensional regression of continuous vectors. There was a question about this on Tuesday and I mentioned that you know we also saw this earlier in continuous alignment where even other modalities like speech if you want to do pre-training is really common to learn embeddings they're continuous which makes them very hard to predict during pre-training but you will first do K means clustering get the cluster ids so in this case maybe just one two three assuming there's three clusters and when you're doing your pre-training you would mask out certain regions and try to reconstruct those regions not by predicting the raw continuous signal but rather predicting the cluster corresponding to that signal. So it just becomes a three-way classification problem when you're doing math prediction. So these kind of vector quantized models or in this case hidden unit models are

**中文**

稳定得多。分类比连续向量的高维回归（high-dimensional regression）稳定得多。周二有人问过这个问题，我提到，你知道，我们之前讲连续对齐（continuous alignment）时也见过这一点，即使是语音这样的其他模态，如果你想做预训练，学习连续嵌入也是非常常见的，这会让它们在预训练期间很难预测。但你会先做 K means 聚类，得到聚类 ids，所以这个例子中可能就是一、二、三，假设有三个聚类。然后在预训练时，你会遮蔽（mask out）某些区域，并尝试重建这些区域，但不是预测原始连续信号，而是预测该信号对应的聚类。所以，当你进行 math prediction \[字幕疑误，可能指 masked prediction，掩码预测\] 时，它就只是一个三分类问题。所以，这类向量量化模型，或者在这里叫作隐藏单元模型（hidden unit models），在

### [14:45](https://www.youtube.com/watch?v=LGBQ0c_4HBA&t=885s) · b000018

**English**

are very common when it comes to both generating and doing self-supervised learning over continuous data.

**中文**

连续数据的生成和自监督学习（self-supervised learning）中都非常常见。

### [14:59](https://www.youtube.com/watch?v=LGBQ0c_4HBA&t=899s) · b000019

**English**

So once you've once you've clustered and discretized your image embedding space then the key part of these models which basically converting from caption into your images your image embeddings becomes much easier. It basically means I'm going to take in some text caption that you took in that you're giving and predict the first visual token. So number 56 and then auto reggressively predict the second visual token 73 auto reggressively predict the next visual token 67 and so on until you predict all the visual tokens and then you decode those visual tokens into a raw image.

**中文**

所以，一旦你对图像嵌入空间做了聚类和离散化，这些模型的关键部分，也就是基本上把说明文字转换成图像、图像嵌入的部分，就会容易得多。它基本上意味着，我会接收你输入、你提供的一段文本说明，然后预测第一个视觉 token。所以是数字 56，然后以自回归（autoregressive）的方式预测第二个视觉 token 73，再以自回归方式预测下一个视觉 token 67，依此类推，直到预测完所有视觉 tokens，再把这些视觉 tokens 解码为原始图像。

### [15:42](https://www.youtube.com/watch?v=LGBQ0c_4HBA&t=942s) · b000020

**English**

Right? So how is this decoding done? Um well at first people use these autoenccoders that take in these images predict what the visual tokens are and then use the visual tokens to reconstruct these images. And we started discussing these variational autoenccoders. Uh but nowadays most people use diffusion models which can be thought of as a non-trivial extension of autoenccoders but following the same principles. Now they are able to do much higher resolution generation of images.

**中文**

对吧？那么，这种解码是如何完成的？嗯，最初人们使用这些自编码器（autoencoders），接收图像，预测视觉 tokens 是什么，然后用这些视觉 tokens 重建图像。我们开始讨论了这些变分自编码器。呃，但如今大多数人使用 diffusion models，可以把它们看作 autoencoders 的一种非平凡扩展，不过遵循相同的原理。现在，它们能够生成分辨率高得多的图像。

### [16:19](https://www.youtube.com/watch?v=LGBQ0c_4HBA&t=979s) · b000021

**English**

any re any questions about these um highle concepts mostly as a recap before we jump back into the technical details

**中文**

在我们重新进入技术细节之前，对于这些，嗯，highle \[字幕疑误，可能指 high-level，高层次\] 概念有什么问题吗？这主要是一次回顾。

### [16:33](https://www.youtube.com/watch?v=LGBQ0c_4HBA&t=993s) · b000022

**English**

again the important thing is um again I want to keep at a high level before going back in details this figure right you want to have a path that takes images learns really good features that represent the image semantically And at the same time is it's discretized so you can very easily predict what these features are. So we have image encoder and decoder. Nowadays encoders are through clip decoders are through state-of-the-art diffusion models. And the other big step is how to align input text caption to predict these image embeddings so that you can actually generate images condition on the text. So that's why there's a path from the text encoder to text embeddings to predict these visual embeddings.

**中文**

再强调一下，重要的是，嗯，我想在回到细节之前先保持在宏观层面，就是这张图，对吧。你希望有一条路径，接收图像，学习能从语义上代表图像的优质特征。同时，这些特征又经过了离散化，所以你可以非常容易地预测它们是什么。因此，我们有图像编码器和解码器。如今，编码器通过 clip 实现，解码器通过最先进的 diffusion models 实现。另一个重要步骤，是如何对齐输入的文本说明以预测这些图像嵌入，这样你才能真正以文本为条件生成图像。所以才会有一条从文本编码器到文本嵌入，再到预测这些视觉嵌入的路径。

### [17:17](https://www.youtube.com/watch?v=LGBQ0c_4HBA&t=1037s) · b000023

**English**

and individual components. We've seen clip how we can learn embeddings of images that are semantically similar to their captions by by bringing those embeddings close together with high similarity. We've seen text encoder and transformers nowadays autoressive transformers. We'll spend the rest of lecture discussing what these diffusion models are, how you can actually go from latent phase to generate images at really high resolution.

**中文**

以及各个组件。我们看过 clip，了解了如何通过让这些嵌入靠近、具有高相似度，来学习在语义上与说明文字相似的图像嵌入。我们看过文本编码器和 transformers，如今是 autoressive transformers \[字幕疑误，可能指 autoregressive transformers\]。接下来这节课的剩余时间，我们会讨论这些 diffusion models 是什么，以及如何真正从 latent phase \[字幕疑误，可能指 latent space，潜在空间\] 出发，生成非常高分辨率的图像。

### [17:48](https://www.youtube.com/watch?v=LGBQ0c_4HBA&t=1068s) · b000024

**English**

All right. So, jumping back into the technical details, we started looking at um introducing these generative models last Tuesday. We explained basically how the key of generative models is to essentially model P of X where X is some data that you're trying to generate can be images, can be text, videos and so on. And often times you want to basically define a a parameterized form for P of X. You want it to be expressive as possible to cover the high dimensionality and high resolution of your data X. So you want P of X to be very expressive, but at the same time you want P of X to be something that you can actually compute using your your neuronet networks and your AI methods. So you cannot be too expressive and too complicated. And basically different choices of P of X uh comes at a core of how people design these generative models. Usually once you define P of X the training objective basically looks like

**中文**

好。那么，回到技术细节，我们上周二开始介绍这些生成模型。我们基本上解释了，生成模型的关键是对 P(X) 建模，其中 X 是你试图生成的某种数据，可以是图像、文本、视频等等。而且通常，你基本上想为 P(X) 定义一个参数化形式（parameterized form）。你希望它尽可能具有表达能力，以涵盖数据 X 的高维度和高分辨率。所以你希望 P(X) 非常有表达能力，但同时又希望 P(X) 是你能用神经网络（neural networks）和 AI 方法实际计算的东西。因此不能表达能力过强、过于复杂。基本上，对 P(X) 的不同选择，是人们设计这些生成模型的核心。通常，一旦定义了 P(X)，训练目标基本上就是

### [18:45](https://www.youtube.com/watch?v=LGBQ0c_4HBA&t=1125s) · b000025

**English**

maximizing P of X for data that you actually see in the world. Right? So you have a real image you should be able to pass it through your generative model estimate P of X to be really high. If you have a noisy image you want to be able to pass it through your model and estimate P of X to be really low. So we call that maximizing likelihood of the actual data that you see that you're hoping to model and to reproduce. Uh several other key points is that you might also want to give it a new X to evaluate what P of X is. So real images it should be high. Fake images or noise it should be low. And you might also want to sample from P of X. So once you've learned this P of X, not only do you want to score it for the existing training images that you're using to train this generative model, you also want to be able to sample new images, new images that are realistic. And often times uh you might want to sample a new image also condition on some other information like condition like on the

**中文**

最大化你在现实世界中实际看到的数据的 P(X)。对吧？所以，如果你有一张真实图像，就应该能够把它输入生成模型，并估计出很高的 P(X)。如果你有一张噪声图像，你希望把它输入模型后，估计出的 P(X) 很低。所以，我们把这叫作最大化你实际看到、希望建模并复现的数据的似然（likelihood）。呃，另外几个关键点是，你可能也希望给它一个新的 X，来评估 P(X) 是多少。所以，真实图像应该很高，假图像或噪声应该很低。你可能还想从 P(X) 中采样（sample）。所以，一旦学到了这个 P(X)，你不仅想对用于训练该生成模型的现有训练图像评分，还希望能够采样出新图像，逼真的新图像。而且通常，呃，你可能还想在其他信息的条件下采样一张新图像，比如以你提供的

### [19:43](https://www.youtube.com/watch?v=LGBQ0c_4HBA&t=1183s) · b000026

**English**

caption that you're giving or condition on some style or stylistic attribute or condition on some presence of certain objects in that image. So often times there's some conditioning that you want these models to give you as well. We saw that a very common way of defining these P of X is to define it using this hierarchy uh which is called a latent variable model. We first assume that X is your data that's often really high dimensional really complex but they can be broken down into some basic latent variables which we call Z. Right? So we're looking at images of people's faces. Z could be the length of their hair. It could be whether they're wearing glasses. Could be whether they're wearing earrings. So these are different usually what we call factors of variation or different dimensions in your data X that you want to capture using these Z's. So we call these latent

**中文**

说明文字为条件，或者以某种风格或风格属性为条件，或者以图像中存在某些对象为条件。所以通常，你也希望这些模型能够提供某种条件控制（conditioning）。我们看到，定义这些 P(X) 的一种非常常见的方式，是用这种层次结构，呃，它叫作潜变量模型（latent variable model）。我们首先假设 X 是你的数据，它通常维度很高、非常复杂，但可以分解成一些基本潜变量，我们称为 Z。对吧？假设我们在看人的面部图像。Z 可以是头发长度，也可以是是否戴眼镜，还可以是是否戴耳环。所以，这些通常就是我们所说的变化因素（factors of variation），或者数据 X 中不同的维度，你希望用这些 Z 来捕捉。因此我们称它们为潜

### [20:37](https://www.youtube.com/watch?v=LGBQ0c_4HBA&t=1237s) · b000027

**English**

variable models where Z's are your latent variables. Uh usually these Z's are not observed because it's often very hard to go through and annotate you know whether people are wearing glasses or what color or length of hair they have. Z is usually unobserved. We want to ideally just infer them from lots of data X without Z's. So then we saw our first um and also speaking of which these Z's can be useful features as well, right? If you're successful at learning these generative models that take in data X and can also infer these latent variable Z, then you can usually use those representations for downstream tasks. Because if your downstream pass is to identify which one of it is your friend, then you're also going to implicitly check their hair color and whether they're wearing glasses, right? If you're trying to whether you know identify an actress or actor, these are very useful. That's why nowadays there's this convergence where all these large

**中文**

变量模型，其中 Z 就是潜变量。呃，这些 Z 通常没有被观测到，因为逐一检查并标注，你知道，人们是否戴眼镜，或者头发是什么颜色、多长，往往非常困难。Z 通常是未观测的。理想情况下，我们希望只根据大量没有 Z 的数据 X 来推断它们。所以，我们接着看到了第一个，嗯，顺便说一下，这些 Z 也可以是有用的特征，对吧？如果你成功学到了这些生成模型，它们接收数据 X，也能推断这些潜变量 Z，那么通常就可以把这些表征用于下游任务（downstream tasks）。因为如果你的下游 pass \[字幕疑误，可能指 task\] 是辨认其中哪一个是你的朋友，那么你也会隐式地检查他们的发色，以及是否戴眼镜，对吧？如果你试图，你知道，辨认一个女演员或男演员，这些特征非常有用。这就是为什么如今出现了这种趋同：所有这些大

### [21:34](https://www.youtube.com/watch?v=LGBQ0c_4HBA&t=1294s) · b000028

**English**

scale foundation models nowadays they're basically just learning P of X for example using auto reggressive next token prediction or self-supervised learning just using X and by modeling P of X really well and maximizing likelihood they automatically learn all your Z's. They automatically learn sentence structure in your text. They automatically learn how to classify documents. they automatically learn what the language is and they can translate between different languages. It can all be seen as X being your raw data and Z being a problem of learning these unobserved latent variables which are then useful for downstream prediction tasks.

**中文**

规模基础模型，如今基本上都只是在学习 P(X)，例如通过自回归的下一个 token 预测（next token prediction），或者只使用 X 的自监督学习。通过很好地建模 P(X) 并最大化似然，它们就会自动学到所有这些 Z。它们自动学会文本中的句子结构，自动学会如何对文档分类，自动学会语言是什么，并能在不同语言之间翻译。所有这些都可以看作：X 是原始数据，而 Z 是学习这些未观测潜变量的问题，这些潜变量随后可以用于下游预测任务。

### [22:22](https://www.youtube.com/watch?v=LGBQ0c_4HBA&t=1342s) · b000029

**English**

All right. So we saw our first example of a generative model starting very simple as a mixture of Gaussians assuming that Z is just categorical. So in this case just one, two or three. Uh it might represent people with short hair, long hair and no hair, right? And you start by first defining these data variables categorical. And you're then going to define that was Z and you have to define what is X given each Z. And in this case X given each Z is just a simple Gaussian, right? With a single mean and variance. So there's a Gaussian centered around the people without hair. There's a Gaussian centered around people with short hair and a Gaussian um of the images of people with long hair. And we saw they were simple because there's basically only uh six parameters in a model. There's three means for the three Gaussians and three coariances for your three Gaussians. Simple but yet very expressive. Right? If you have data

**中文**

好。所以，我们看了第一个生成模型的例子，从非常简单的高斯混合（mixture of Gaussians）开始，假设 Z 只是类别型（categorical）的。所以在这里就是一、二或三。呃，它可能代表短发、长发和没有头发的人，对吧？你首先把这些数据变量定义为类别型。然后你会定义，那是 Z，你还必须定义每个 Z 给定时的 X 是什么。在这个例子里，给定每个 Z 的 X 就是一个简单的高斯分布（Gaussian），对吧？只有一个均值和方差。所以，有一个 Gaussian 以没有头发的人为中心，一个以短发的人为中心，还有一个，嗯，是长发人的图像的 Gaussian。我们看到它们很简单，因为模型基本上只有，呃，六个参数。三个 Gaussian 各有一个均值，以及三个 Gaussian 各有一个协方差（covariance）。简单，但仍然很有表达能力。对吧？如果你的数据

### [23:20](https://www.youtube.com/watch?v=LGBQ0c_4HBA&t=1400s) · b000030

**English**

that looks like this, you know, a mixture of Gaussians with uh three latent var with latent variable of three three options essentially allows you to cluster your data into three forms and fit three Gaussians, one for each form. So it's a relatively simple model and because of its simplicity, it can be computed basically almost exactly, right? Then usually what these approaches do the goal is to just estimate what the three means are and what the three variances are. Right? So they iteratively go between first using whatever my current mean and variance are. So the positions of my three Gaussians to first infer for each data point which Gaussian it belongs to. Okay, this is called the expectation step. Assigning every data point to the Gaussian that it belongs to. And once you do that, you can then use the information of which data point was

**中文**

看起来像这样，你知道，一个高斯混合，呃，有三个潜在变，有一个具有三、三个选项的潜变量，基本上就能让你把数据聚成三种形式，并拟合三个 Gaussian，每种形式对应一个。所以这是一个相对简单的模型，而且由于它很简单，基本上几乎可以精确计算，对吧？通常这些方法的目标，就是估计三个均值和三个方差分别是多少。对吧？所以它们在两步之间迭代：首先使用当前的均值和方差，也就是这三个 Gaussian 的位置，先推断每个数据点属于哪个 Gaussian。好，这叫作期望步骤（expectation step）。把每个数据点分配给它所属的 Gaussian。一旦完成这一点，你就可以利用哪个数据点被

### [24:16](https://www.youtube.com/watch?v=LGBQ0c_4HBA&t=1456s) · b000031

**English**

assigned to which Gaussian to reestimate the mean and variances of that Gaussian. Right? Reestimating the mean is just taking the sample mean of the data points assigned to that Gaussian. And reestimating the variance is just computing the sample variance of the points assigned to that Gaussian. And you do this for each of the three Gaussians. And once you converge, you know, at first these Gaussians are all over the place. The assignments are all over the place. But as you iterate between these two steps, you can both assign your points to the right Gaussian and then also estimate the parameters of that Gaussian, its mean and variance to perfectly capture density of those points assigned to the Gaussian. So essentially, you know, visually if your data looks like this three multimodal distributions with three distinct peaks, what these models are learning is one Gaussian for first peak, one Gaussian for the second, and one Gaussian for the third peak.

**中文**

分配给哪个 Gaussian 的信息，重新估计该 Gaussian 的均值和方差。对吧？重新估计均值，就是对分配给该 Gaussian 的数据点求样本均值。重新估计方差，就是计算分配给该 Gaussian 的点的样本方差。对三个 Gaussian 中的每一个都这样做。直到收敛，你知道，一开始这些 Gaussian 到处都是，分配也很混乱。但随着你在这两步之间迭代，你既能把点分配到正确的 Gaussian，又能估计该 Gaussian 的参数，也就是均值和方差，从而完美捕捉被分配到它的那些点的密度。所以基本上，你知道，从视觉上看，如果你的数据像这样，是三个具有三个独立峰值的多峰分布（multimodal distributions），那么这些模型学到的就是：一个 Gaussian 对应第一个峰，一个对应第二个峰，一个对应第三个峰。

### [25:11](https://www.youtube.com/watch?v=LGBQ0c_4HBA&t=1511s) · b000032

**English**

So that's a very simple example of a generative model. How you would generate data from this is that well you would first sample Z. So sampling Z basically just means picking a random number between 1, two and three representing no hair, long hair or short hair. That tells you which gaussium it belongs to. Let's say one. Then you go into that Gaussian and you then sample from that first Gaussian, right? A data point X. That's X given Z. Uh so it's very easy to sample from. You can also do controllable sampling. If I want people without hair, I know which gin to go into. I want to generate people with hair long hair, I know which G to go into. So hopefully that gives you a intuitive simple intuitive but will split up to more complex models. The first of all the power of these latent variables Z very simple three latent variables but can capture one variation of how your

**中文**

所以，这是一个非常简单的生成模型例子。如何用它生成数据呢？你首先采样 Z。所以，采样 Z 基本上就是在 1、two 和 three 之间随机选一个数，分别代表没头发、长发或短发。这就告诉你它属于哪个 gaussium \[字幕疑误，可能指 Gaussian\]。假设是一。然后你进入那个 Gaussian，从第一个 Gaussian 中采样，对吧？得到一个数据点 X。这就是给定 Z 的 X。呃，所以它很容易采样。你也可以做可控采样（controllable sampling）。如果我想要没有头发的人，我知道该进入哪个 gin \[字幕疑误，可能指 Gaussian\]。我想生成有头发、长头发的人，我知道该进入哪个 G。所以，希望这能给你一个直观、简单、直观的理解，但后面会拆分到更复杂的模型。首先是这些潜变量 Z 的力量，非常简单的三个潜变量，却能捕捉你的

### [26:08](https://www.youtube.com/watch?v=LGBQ0c_4HBA&t=1568s) · b000033

**English**

data changes this hierarchy of X given Z in this case a Gaussian right still very simple but can be quite expressive right if you go into a Gaussian with a mean and variance you know the structure of data for that uh for that latent variable we saw the sampling process which is the first sample Z and then sample from the Gaussian X given So that's how you would generally sample from latent variable models. And we also saw how to essentially maximize your likelihood which in this case is just about iterating between assigning a point to a Gaussian and then estimating the parameters of the Gaussians for the points that it was assigned to.

**中文**

数据如何变化的一种变化因素。给定 Z 的 X 这一层次结构，在这里是一个 Gaussian，对吧，仍然非常简单，但可以很有表达能力，对吧。如果你进入一个具有均值和方差的 Gaussian，你就知道那个，呃，那个潜变量对应的数据结构。我们看了采样过程，也就是先采样 Z，然后从 Gaussian 中采样给定……的 X \[原文在此缺失条件\]。所以，这就是通常从潜变量模型中采样的方法。我们也看了如何基本上最大化似然，在这个例子中，就是在把一个点分配给某个 Gaussian，与根据分配给各 Gaussian 的点估计其参数之间反复迭代。

### [26:52](https://www.youtube.com/watch?v=LGBQ0c_4HBA&t=1612s) · b000034

**English**

Any questions about this? I know it's part recap, part going into a bit more detail. Yes. For those uh continuous data for example audio data how important is the minimum segments length?&gt;&gt; Um are you talking about this slide?&gt;&gt; Yeah like for those data if you want to learn the representation vector how important is the seven you pay? Oh, it be very important. Yeah.&gt;&gt; Yeah. I mean like uh is there any like conclusion about there like some limits that if you put down limits then it's fine.&gt;&gt; I'm not an expert in audio and speech uh but from what I see so when this paper came out as you see from the the image they had a fixed window right it was

**中文**

关于这一点有什么问题吗？我知道这部分既是回顾，也补充了一些细节。有，请说。对于那些，呃，连续数据，比如音频数据，最小片段长度有多重要？&gt;&gt; 嗯，你是在说这张幻灯片吗？&gt;&gt; 对，比如对于这些数据，如果你想学习表征向量，seven you pay \[原文不清，可能涉及片段划分\] 有多重要？哦，会非常重要。对。&gt;&gt; 对，我是说，呃，有没有什么结论，比如某些界限，只要把界限设好就没问题。&gt;&gt; 我不是音频和语音方面的专家，呃，但根据我看到的，当这篇论文发表时，正如你从图里看到的，他们使用了固定窗口，对吧，它是

### [27:50](https://www.youtube.com/watch?v=LGBQ0c_4HBA&t=1670s) · b000035

**English**

always maybe five hertz. So every 5 seconds you do sample something. Um and that was your window. Of course it's not ideal, right? Ideally you want maybe a window that says this is a word. This is a pause. This next word a pause or next word. You ideally want these semantically meaningful boundaries in your data. Some can be longer. Some can be shorter because maybe you pause longer or you say a shorter word. Uh but that that's a difficult question. I mean I think people are definitely working on that dynamic boundaries otherwise I know some people also go to the other limit which is to each time step is one one one data point right or or one each data point is one time step in your sequence model so these are ultra high frequency models um but yeah I mean it's definitely a very very important hyperparameter

**中文**

可能始终是 five hertz。所以每 5 秒采样一次东西 \[原文频率与间隔表述不一致\]。嗯，那就是你的窗口。当然，这并不理想，对吧？理想情况下，你可能希望一个窗口表示这是一个词，这是一个停顿，下一个词，一个停顿，或者下一个词。理想情况下，你希望数据中有这些语义上有意义的边界。有些可以更长，有些可以更短，因为你可能停顿得更久，或者说了一个更短的词。呃，但这是一个困难的问题。我是说，我想人们肯定在研究这种动态边界。另外，我知道有些人也走向另一个极端，也就是每个时间步是一个、一、一个数据点，对吧，或者每个数据点就是序列模型中的一个时间步。所以这些是超高频模型，嗯。不过，是的，我是说，这绝对是一个非常、非常重要的超参数（hyperparameter），

### [28:46](https://www.youtube.com/watch?v=LGBQ0c_4HBA&t=1726s) · b000036

**English**

before you start defining what model you develop on top of that. Same thing for for anything else, right? Uh for language models, a big reason why they work is because of their tokenization, right? Lots of work going into tokenizing. And of course, they don't tokenize by characters, which was the case back in like, you know, 20 years ago. They don't tokenize by words also. They tokenize by subwords, right? So eat, drink, and the eating, drinking are kind of separated out. So you can get the the verbs and also the ing. So they have all these like subwords that people study and then when you go to video it's even harder to tokenize. So yeah it's very very important step.

**中文**

在你开始定义要在其上构建什么模型之前，就得考虑。其他任何东西也一样，对吧？呃，对语言模型而言，它们有效的一个重要原因就是 tokenization，对吧？人们在 tokenization 上投入了大量工作。当然，它们不是按字符来划分 tokens，这种做法大概是，你知道，20 年前的事了。它们也不是按词来划分，而是按子词（subwords），对吧？所以 eat、drink，以及 eating、drinking，会以某种方式被拆开。这样你就能得到动词部分，也能得到 ing。所以，人们研究了所有这些 subwords。然后到了视频，tokenization 就更难了。所以，是的，这是非常、非常重要的一步。

### [29:33](https://www.youtube.com/watch?v=LGBQ0c_4HBA&t=1773s) · b000037

**English**

Okay. So that was mixture of gaussians and then we started seeing how we can extend mixture of gaussians or gaussian mixture models to variational autoenccoders. Right. So if mixture of Gaussian were kind of uh kind of on the left where Z is really simple and Z is just a categorical 1 2 3 and X given Z was just a fixed Gaussian with a mean and variance. You can think of VAE as upgrading on two fronts. First of all, the Z's are usually now continuous, right? Continuous, higher dimensional. Usually we say we put a prior on Z as you know if Z is a D- dimensional vector, then the Z should come from a Gaussian with mean zero and with identity variance. So basically D standard Gaussians. So that's your prior Z. But more importantly, look at what X given Z is. So X given Z instead of just being a Gaussian with a fixed mean and variance, X given Z is now going to be a

**中文**

好。所以，那就是高斯混合，接着我们开始看，如何把高斯混合，或者高斯混合模型（Gaussian mixture models），扩展到变分自编码器。对。如果高斯混合大致在左边，Z 非常简单，只是类别型的 1、2、3，而给定 Z 的 X 只是一个具有均值和方差的固定 Gaussian。那么，你可以把 VAE 看作在两个方面做了升级。首先，Z 现在通常是连续的，对吧？连续的、维度更高的。通常我们说，会为 Z 设定一个先验（prior），你知道，如果 Z 是一个 D 维向量，那么 Z 就应该来自均值为零、方差为单位阵的 Gaussian。所以基本上是 D 个标准 Gaussian。这就是 Z 的先验。但更重要的是，看看给定 Z 的 X 是什么。给定 Z 的 X 不再只是一个均值和方差固定的 Gaussian，现在它会是一个

### [30:29](https://www.youtube.com/watch?v=LGBQ0c_4HBA&t=1829s) · b000038

**English**

a neon network. A neuronet network that takes in the current value of Z's and predicts a distribution over X. Right? It's still a Gaussian distribution but with two key differences. First, it's conditioned on the Z's, which means that a Gaussian is different for every data point and not the same for all data points like we saw in Gausian mixture models. So that's immediately much more expressive, right? The ability of the Gaussian shape and parameter and mean and variance to change for every data point. Second of all, the fact that now the mean and variance that now changes across the data points are also learned through a neural network. So these parameters can be nonlinear functions, nonlinear transformations immediately becomes much more expressive. Okay, so ter misses right now the mean and variance for for the latent variables are changing for every data point and also learned by our neuronet network and not fixed uh which immediately makes it

**中文**

一个 neon network \[字幕疑误，可能指 neural network\]。一个神经网络，接收 Z 当前的值，并预测 X 上的分布。对吧？它仍然是 Gaussian，但有两个关键区别。首先，它以 Z 为条件，这意味着每个数据点的 Gaussian 都不同，而不像我们在 Gaussian mixture models 中看到的那样，所有数据点都一样。所以，表达能力立刻强了很多，对吧？Gaussian 的形状、参数、均值和方差可以随每个数据点变化。其次，现在这些会随数据点变化的均值和方差，也是通过神经网络学习的。因此，这些参数可以是非线性函数（nonlinear functions）、非线性变换（nonlinear transformations），表达能力立刻变得更强。好，所以 ter misses \[原文不清\]，现在潜变量的均值和方差会随每个数据点变化，而且由我们的神经网络学习，并非固定的，呃，这立刻使它

### [31:26](https://www.youtube.com/watch?v=LGBQ0c_4HBA&t=1886s) · b000039

**English**

much more expressive. Uh but the same yes&gt;&gt; uh just uh maybe to clarify for myself right um the the five features in the input layer are they gian that we've already learned or are they just like the objective of learning gins and then that's transformed like the the mean variance of that is transformed and that not sure I really answer your question but after I cover the main method maybe we see your question is answered Okay, so here's the method. Uh, usually these VAEs have a encoder and decoder, right? The encoder is what takes in your X, your raw data and encodes that into your latent variable Z, right? Usually this is a neural network. We call it Q with some parameters. It outputs a distribution Z given your

**中文**

具有强得多的表达能力。呃，但同样，有，请说。&gt;&gt; 呃，只是，也许是给我自己澄清一下，对吧，嗯，输入层的五个特征，是我们已经学到的 gian \[字幕疑误，可能指 Gaussian\]，还是说，它们只是学习 gins \[字幕疑误，可能指 Gaussians\] 的目标，然后再进行变换，比如它的均值和方差被变换，然后那个……我不确定自己是否真的能回答你的问题，但等我讲完主要方法之后，也许我们可以看看你的问题是否得到了解答。好，这就是方法。呃，通常这些 VAEs 有一个编码器和一个解码器，对吧？编码器接收 X，也就是原始数据，并把它编码为潜变量 Z，对吧？通常这是一个神经网络。我们称它为带有一些参数的 Q。它输出一个给定你的

### [32:23](https://www.youtube.com/watch?v=LGBQ0c_4HBA&t=1943s) · b000040

**English**

input X. That's your encoder. And you also have a decoder. A decoder which goes from your latent variable Z back to your raw data X. So it decodes the latent variables and decodes sorry it decodes the raw data given your latent variables. So there's another neon network we call it P with a different set of parameters data and is decoding X given Z. Right? This encoder decoder structure. Uh if I kind of unroll it, it looks something like this. uh you have X encoded into E encoded into your latent variables Z and then you decode Z back into your raw data X right or in this case it'll be Xhat because it might be slightly different from the original input X.

**中文**

输入 X 的 Z 分布。这就是编码器。你还有一个解码器。解码器从潜变量 Z 回到原始数据 X。所以，它解码潜变量，并且解码，抱歉，是根据潜变量解码原始数据。因此，还有另一个 neon network \[字幕疑误，可能指 neural network\]，我们称为 P，它有一组不同的参数 data \[字幕疑误，可能指 theta\]，并解码给定 Z 的 X。对吧？这种编码器—解码器结构（encoder-decoder structure）。呃，如果我把它展开，大概就是这样。呃，你有 X，把它编码成 E，再编码成潜变量 Z，然后把 Z 解码回原始数据 X，对吧？或者在这里是 Xhat，因为它可能与原始输入 X 略有不同。

### [33:09](https://www.youtube.com/watch?v=LGBQ0c_4HBA&t=1989s) · b000041

**English**

This stuff all over here is just basically showing that um I want my latent representation Z to not just be a vector but rather to be a distribution. And what that basically means is that the encoder instead of directly outputting just what a single vector is is that it will output the mean and variance. It will learn the mean and variances that I can then sample a vector from that Gaussian with that mean and variance. And the vector that I sample is my latent vector Z. Right? So how exactly inference pass works is that you take a data point X. You will use the encoder which is Q with the parameters five. You will learn two Dimensional vectors. A D- dimensional mean vector mu and a D- dimensional variance vector sigma. Right? Ignoring coariance for now. You learn a dimensional vector sigma. That will define what the Gaussian is. To sample a

**中文**

这里所有这些内容，基本上只是在说明，嗯，我希望潜在表征 Z 不只是一个向量，而是一个分布。这基本上意味着，编码器不会直接只输出一个向量，而是会输出均值和方差。它会学习均值和方差，然后我可以从具有该均值和方差的 Gaussian 中采样一个向量。而我采样出的那个向量，就是潜在向量 Z。对吧？那么，具体的推断过程（inference pass）如何工作呢？你取一个数据点 X。使用编码器，也就是带有参数 five \[字幕疑误，可能指 phi\] 的 Q。你会学习两个维度向量。一个 D 维均值向量 mu，以及一个 D 维方差向量 sigma。对吧？暂时忽略协方差。你学习一个维度向量 sigma。这就定义了 Gaussian 是什么。要从这个 Gaussian 中采样一个

### [34:06](https://www.youtube.com/watch?v=LGBQ0c_4HBA&t=2046s) · b000042

**English**

latent vector Z from that Gaussian, you use this trick where you first sample epsilon which is dimensional noise from mean zero variance one. You multiply that with sigma that scales the variance to be sigma and you add it to the mean and that gives you a vector sampled from a gaussian centered at that mean. So in other words, z will be mu plus you know sigma time epsilon noise. So that gives you a Z vector and then you would take a Z vector pass it through the decoder to then get the reconstructor X which is Xhat right. Uh I saw a question

**中文**

潜在向量 Z，你会使用这个技巧：先采样 epsilon，也就是来自均值为零、方差为一的分布的维度噪声。把它乘以 sigma，将方差缩放为 sigma，再把它加到均值上，就得到一个从以该均值为中心的 Gaussian 中采样出的向量。所以，换句话说，z 就是 mu 加上，你知道，sigma 乘以 epsilon 噪声。这样你就得到了一个 Z 向量，然后把 Z 向量传入解码器，得到重建的 X，也就是 Xhat，对吧。呃，我看到有个问题。

### [34:53](https://www.youtube.com/watch?v=LGBQ0c_4HBA&t=2093s) · b000043

**English**

steps would one be able to replace what is here with concept or is that just&gt;&gt; yes you can. So exactly. So two two main differences, right? If you look at this, the encoder is predicting the mean and variance, right? Mu and sigma, right? That Gaussian distribution for this X. If I swap it out with a different X, I'm going to get another different mean and sigma, right? So I'm going to get as many means and these are variances as as number of data points that I have in my data set, right? which is a big increase in expressivity compared to Gaussian mixture models where we remember we only had basically three means for the entire data set, right? Three means because you know our dimension of Z was three, right? So that was three Gaussians that fit the entire data set. This is a slightly different small Gaussian that fits locally uh the distribution of each

**中文**

步骤，能不能把这里的东西替换成 concept，还是说这只是……&gt;&gt; 可以。所以，正是如此。两个、两个主要区别，对吧？如果你看这里，编码器在预测均值和方差，对吧？Mu 和 sigma，对吧？这个 X 对应的 Gaussian。如果我换成另一个 X，就会得到另一个不同的均值和 sigma，对吧？因此，我会得到与数据集中的数据点数量一样多的均值和这些方差，对吧？与 Gaussian mixture models 相比，这在表达能力上有很大的提升。还记得，在那个模型中，整个数据集基本上只有三个均值，对吧？三个均值，因为，你知道，Z 的维度是三，对吧？所以，是三个 Gaussian 来拟合整个数据集。这里则是一个略有不同的小 Gaussian，它局部拟合每个

### [35:50](https://www.youtube.com/watch?v=LGBQ0c_4HBA&t=2150s) · b000044

**English**

data point and potential nearby data points around it.

**中文**

数据点以及它周围可能存在的邻近数据点的分布。

### [35:59](https://www.youtube.com/watch?v=LGBQ0c_4HBA&t=2159s) · b000045

**English**

uh we'll see some tricks of alleviating overfitting right um there's definitely a big increase in expressivity but yes you're right um there are if you don't train this well in fact if you don't define this mean and variance then you will could be prone to overfitting which I'll discuss in a bit so how to train this model two key steps right so one is a reconstruction objective if I take in an x image image that I have and I pass it through the encoder to estimate the mean and variance. I sample latent vector Z from it and then I decode it back to my image. Ideally, the decoded image should be as close as possible to the original image. Right? It's a reconstruction objective. Another key objective which I didn't go into too much detail on Tuesday is this prior objective. Right? If you recall, we started by saying I'm going to assume that these latent variables Z all come

**中文**

呃，我们会看到一些缓解过拟合（overfitting）的技巧，对吧。嗯，表达能力确实有很大的提升，但没错，你说得对，嗯，如果没有训练好，实际上，如果没有定义这个均值和方差，就可能容易过拟合，我一会儿会讨论。那么如何训练这个模型？两个关键步骤，对吧。一个是重建目标（reconstruction objective）：如果我输入一张 x 图像，我拥有的一张图像，并让它经过编码器来估计均值和方差，再从中采样潜在向量 Z，然后把它解码回图像。理想情况下，解码后的图像应该尽可能接近原始图像。对吧？这是重建目标。另一个关键目标，也就是我周二没有详细讲的，是这个先验目标（prior objective）。对吧？如果你还记得，我们一开始说，我要假设这些潜变量 Z 全都来自

### [36:55](https://www.youtube.com/watch?v=LGBQ0c_4HBA&t=2215s) · b000046

**English**

from a standard Gaussian distribution, right? With mean zero and variance one. So even though I'm learning all lots of little little Gaussian Z, I want overall all of these um little Gaussians that I learn on average across all of my entire data set to marginalize and to become very similar to this big prior which is uh just centered at zero with unit variance. We call this a regularization or prior objective. Right? This is actually very important to address your question over there because if you have lots of little Gaussian features centered at your data point you might end up learning a latent space with lots of holes basically with lots of holes that basically learn distributions for your observed points but don't put any probability density on points that you don't observe. Putting this prior essentially smoothests out the entire latent distribution so that even you don't observe a data point as some sort

**中文**

一个标准 Gaussian，对吧？均值为零，方差为一。所以，尽管我在学习很多、很多小小的 Gaussian Z，我希望总体上，跨整个数据集平均来看，我学到的所有这些小 Gaussian 在边缘化（marginalize）之后，都变得非常接近这个大先验，也就是，呃，以零为中心、方差为一。我们称之为正则化（regularization）或先验目标。对吧？这对于回答你刚才的问题其实非常重要，因为如果你有很多以数据点为中心的小 Gaussian 特征，最后可能学到一个有很多空洞的潜在空间（latent space），基本上有很多空洞，只为观测到的点学习分布，却不给未观测到的点分配任何概率密度。加入这个先验，基本上会平滑整个潜在分布，这样即使你没有观测到某个数据点，作为某种

### [37:52](https://www.youtube.com/watch?v=LGBQ0c_4HBA&t=2272s) · b000047

**English**

of mass, it will still have some distribution. This is a visualization here. So it's comparing the latent space of VAE with this K loss with the prior. You see everything is kind of smoothed out. It's round and this round basically means it's centered at zero and the variance in one in all dimensions. And if you don't have this K loss, you do end up learning a lot of points um that don't obey the smoothness, right? You have a lot of them clustered in one side. You have various gaps in the middle and that can be bad because if you sample from this, if you sample from somewhere in the middle, you might end up generating an image that does not look real, right? So that's a that's a big issue and why some of these smoothing prior are needed on these latent spaces. Yeah.

**中文**

质量，它仍然会有某种分布。这里有一个可视化。它在比较带有这个 K loss \[字幕疑误，可能指 KL loss\]、带有先验的 VAE 潜在空间。你会看到，所有东西都在某种程度上被平滑了。它是圆的，这个圆基本上意味着它以零为中心，所有维度上的方差都是一。如果没有这个 K loss，你最终确实会学到很多不满足这种平滑性的点，对吧？很多点会聚集在一侧，中间有各种空隙。这可能不好，因为如果你从这里采样，如果你从中间某处采样，最终可能生成一张看起来不真实的图像，对吧？所以，这是个大问题，也是这些潜在空间需要某些平滑先验的原因。对。

### [38:41](https://www.youtube.com/watch?v=LGBQ0c_4HBA&t=2321s) · b000048

**English**

have the but why are there&gt;&gt; um for simplicity because I mean these neuronet networks are function approximators right so any you any any any vector that comes in these neuronet networks are able to learn shifting and scaling and any multiplicative transformations to your data so that eventually you can impose a standard prior on your a standard Gaussian prior or latent variables without losing expressivity, right? Because if you feel it should be mean two, this minus two can be very easily learned in the encoder. If you think the variant should be five, this division by one over root five can be very easily learned by the encoder. So you can basically just impose the most basic prior and let any constants be absorbed by the training of the encoder.

**中文**

有那个，但为什么有……&gt;&gt; 嗯，为了简单起见，因为，我是说，这些神经网络是函数逼近器（function approximators），对吧？所以，任何，你，任何、任何、任何输入向量，这些神经网络都能学习对数据进行平移、缩放以及任何乘法变换。因此最终，你可以对你的，标准 Gaussian 先验，或者潜变量施加一个标准先验，而不损失表达能力，对吧？因为如果你觉得均值应该是二，那么这个减二的操作可以很容易地由编码器学到。如果你觉得方差应该是五，那么这个除以五的平方根的倒数的操作，也可以很容易地由编码器学到。所以，你基本上可以只施加最基础的先验，让任何常数都被编码器的训练吸收。

### [39:39](https://www.youtube.com/watch?v=LGBQ0c_4HBA&t=2379s) · b000049

**English**

Yes,&gt;&gt; just on the interation of the two graphs on the right. Aside from seeing that the top one smoother, are there other functional interpretations get?

**中文**

有，请说。&gt;&gt; 只是关于右边两张图的解读。除了看到上面那张更平滑之外，还能得到其他功能方面的解释吗？

### [39:58](https://www.youtube.com/watch?v=LGBQ0c_4HBA&t=2398s) · b000050

**English**

&gt;&gt; What do you mean by functional interpretations?&gt;&gt; Like the side problem ascertaining how smooth it is, right? like are there is there anything to the density of them the interpretating the clustering like can we read into other aspects of it? Oh yes yes yes. Um if I recall so this is from a blog post that was just describing training tricks for for VAEEs. Um so this was so usually when people train these VA they take something amnest right your digits you know uh zero through nine uh they don't use the labels themselves they use the raw images. So they pass a raw image in, they learn the latent features and decode the image and then they basically take all the latent vectors and they plot two dimensional PCA and they cluster it by by coloring it which of the 10 digits it belong to. Right? So ideally you do want to space where for example all the one digits are top left or all the seven digits are another cluster by nearby because one and seven

**中文**

&gt;&gt; 你说的功能方面的解释是什么意思？&gt;&gt; 比如，除了判断它有多平滑之外，对吧？比如，它们的密度有没有什么含义，如何解释聚类，我们能从其他方面解读它吗？哦，可以，可以，可以。嗯，如果我没记错，这是来自一篇博客文章，专门介绍 VAEEs \[字幕疑误，可能指 VAEs\] 的训练技巧。嗯，所以这是，通常人们训练这些 VA \[字幕疑误，可能指 VAEs\] 时，会用类似 amnest \[字幕疑误，可能指 MNIST\] 的东西，对吧，就是数字，你知道，呃，零到九。他们不使用标签本身，而是使用原始图像。所以，他们输入一张原始图像，学习潜在特征，再解码图像。然后基本上把所有潜在向量拿出来，画出二维主成分分析（principal component analysis, PCA）图，并通过着色，根据它属于 10 个数字中的哪一个来显示聚类。对吧？所以，理想情况下，你确实希望有一个空间，比如所有数字一都在左上角，或者所有数字七形成另一个邻近的聚类，因为一和七

### [40:55](https://www.youtube.com/watch?v=LGBQ0c_4HBA&t=2455s) · b000051

**English**

look kind of similar to each other and then maybe nine is nearby as well but then like five is very different. So ideally you want this this clustering within these uh these latent variables or in this case latent variables are are your class categories. Yes. Yes. So the intuition for the KR loss is that um we first know first define a prior on Z. In this case, a good prior on Z is just something where this whole space of representations of Z. Whole space meaning if I take all the Z's that I learned across my entire data set and also for other data points that I never observe. I want this whole space to roughly be well smoothed and well shaped. Right? So a good way of saying that is that it should be centered at zero and have unit variance. So basically looks like a ball centered around zero. So how I can impose that is that I can take all these q of z given

**中文**

看起来有点相似，然后九可能也在附近，但五就很不一样。所以，理想情况下，你希望这些，呃，这些潜变量中有这样的聚类，或者在这个例子里，潜变量是你的类别。是的。是的。所以，KR loss \[字幕疑误，可能指 KL loss\] 的直觉是，嗯，我们首先知道，先为 Z 定义一个先验。在这里，Z 的一个好先验就是，让这整个 Z 表征空间，整个空间的意思是，如果我取整个数据集中学到的所有 Z，也包括那些我从未观测到的其他数据点。我希望整个空间大致是平滑且形状良好的。对吧？所以，一个好的表述方式是，它应该以零为中心，并具有单位方差。因此基本上看起来就像一个以零为中心的球。那么，我可以如何施加这一点呢？我可以取所有这些给定

### [41:53](https://www.youtube.com/watch?v=LGBQ0c_4HBA&t=2513s) · b000052

**English**

x's which basically means I know given an x I learn a distribution over z for that x I give it a different x I learn a distribution of z for that x and all these little small distributions of z's that I learned and in expectation over all the x's right that marginalized in expectation over all the x's it should look like this entire space and that should look like a a unit gaussian Okay. Um, so there's expectation over X going on here. So over all the X's on average all all of these Z's should look like this. This ball on the top right. KL over here is um is basically a measure of how close two distributions are. Um I can there's an equation for it but you can essentially think about it as how close two distributions are with respect to each other.

**中文**

x 的 q(z)，这基本上意味着，我知道，给定一个 x，我会为这个 x 学习一个 z 的分布；给它一个不同的 x，我又为那个 x 学习一个 z 的分布。所有这些学到的小小的 z 分布，在对所有 x 取期望（expectation）时，对吧，对所有 x 取期望并边缘化之后，应该看起来像这整个空间，而它应该看起来像一个单位 Gaussian。好。嗯，所以这里有一个对 X 取期望的过程。因此，对所有 X 平均来看，所有这些 Z 应该看起来像这样，右上角这个球。这里的 KL，嗯，基本上是衡量两个分布有多接近的一种度量。嗯，我可以，有一个对应的公式，但你基本上可以把它理解为两个分布彼此有多接近。

### [42:51](https://www.youtube.com/watch?v=LGBQ0c_4HBA&t=2571s) · b000053

**English**

Yes.&gt;&gt; Okay. So, how do people go about picking that dimension like the D maybe in digit it just makes sense to 10? What's a good even way about size of that?&gt;&gt; So, even in handwriting it wouldn't be 10. Um it could be much more. So you again the intuition of Z is that Z is this latent variable that should capture all the different you know factors of variation right so in the handwritten case one important factor is this categorical distribution 0 through9 what it is another one could be the the style of handwriting another one could be the thickness of the stroke right or the intensity of the color so it's going to be actually quite a lot um so Z is usually a hyperparameter I mean if your data is you know 300 dimensional Z makes sense to be something 64, right? So, he's doing like, you know, four to five times compression and then going back

**中文**

有，请说。&gt;&gt; 好。那么，人们是怎么选择这个维度，比如 D 的？也许对于数字，设成 10 就很合理？有什么好的办法来考虑它的大小？&gt;&gt; 所以，即使是手写数字，也不会是 10。嗯，它可能大得多。所以，再次来说，Z 的直觉是，Z 是这个潜变量，应该捕捉所有不同的，你知道，变化因素，对吧。因此，在手写数字的例子中，一个重要因素是 0 到 9 这个类别分布，也就是它是什么数字；另一个可能是书写风格；还有一个可能是笔画粗细，对吧？或者颜色的强度。所以实际上会有相当多。嗯，因此 Z 通常是一个超参数。我是说，如果你的数据是，你知道，300 维，那么 Z 设成 64 之类就很合理，对吧？所以，它在做大概，你知道，四到五倍的压缩，然后再回到

### [43:47](https://www.youtube.com/watch?v=LGBQ0c_4HBA&t=2627s) · b000054

**English**

out, right? Uh for for BERT, for example, some of the latent vectors, you know, BERT was trained with like about 70,000 token size and hidden bettings for like 768.&gt;&gt; So, so 100 times to create a bottleneck. So, that actually suspicion,&gt;&gt; right?&gt;&gt; But there's no like move something.&gt;&gt; No. Yeah.&gt;&gt; Yes. Maybe something but I don't get exactly how we mean and the variance from it what we to do here.&gt;&gt; Let me show you this um this visualization. I was going to let me explain this a little bit. So again visually so you could have an image. So again go going with these images. Uh they're encoded. uh your Z may not correspond exactly to these per dimension but you know intuitively if they are trained well you could think of Z as having multiple

**中文**

外面，对吧？呃，比如 BERT，一些潜在向量，你知道，BERT 训练时的 token size 大约是 70,000，而 hidden bettings \[字幕疑误，可能指 hidden embeddings，隐藏嵌入\] 大约是 768。&gt;&gt; 所以，所以是 100 倍，来形成一个瓶颈（bottleneck）。所以，这实际上是 suspicion \[原文不清\]，&gt;&gt; 对吧？&gt;&gt; 但没有类似 move something \[原文不清\]。&gt;&gt; 没有。对。&gt;&gt; 有。也许是某个东西，但我不太明白，我们具体如何从中得到均值和方差，这里要做什么。&gt;&gt; 让我给你看这个，嗯，这个可视化。我本来打算，让我稍微解释一下。所以，再从视觉上看，你可以有一张图像。还是继续用这些图像。呃，它们被编码。呃，你的 Z 可能不会在每个维度上都精确对应这些因素，但你知道，直觉上，如果训练得好，可以把 Z 看作有多个

### [44:44](https://www.youtube.com/watch?v=LGBQ0c_4HBA&t=2684s) · b000055

**English**

dimension maybe one dimension captures smile one dimension captures beard one dimension captures glasses and so on and each of them right is basically learning a small little Gaussian that is centered at some mean and with some variance. So in this case you encode this maybe this is the pattern that you get out right uh but of course there might be images that are very similar to this right you could kind of shift the hair color a little bit more to the right of the Gaussian so maybe the hair color becomes more more dark you could uh shift the beard a little bit more to the right of the Gaussian so the beard becomes longer right so now you have the exact same image but now hair changes beard changes everything else is the same position in the Gaussian right so that's what I mean by these uh these little little gaussians over Um so here's another example right so you might have these gaussians and then you can sample from different locations and sampling basically means just

**中文**

维度，也许一个维度捕捉微笑，一个维度捕捉胡须，一个维度捕捉眼镜，等等。而其中每一个，对吧，基本上都在学习一个小小的 Gaussian，它以某个均值为中心，并具有某个方差。所以，在这个例子里，你编码这个，也许得到的就是这个模式，对吧。呃，但当然，可能会有一些与它非常相似的图像，对吧？你可以把发色稍微向 Gaussian 的右边移一点，也许发色就会更深；你可以把胡须稍微向 Gaussian 的右边移一点，胡须就会变长，对吧？所以现在你有完全相同的图像，但发色变了，胡须变了，其他所有东西在 Gaussian 中的位置都相同，对吧？所以，这就是我所说的这些，呃，这些小小的 Gaussians，覆盖……嗯，这里还有一个例子，对吧？你可能有这些 Gaussians，然后可以从不同位置采样，而采样基本上就是

### [45:37](https://www.youtube.com/watch?v=LGBQ0c_4HBA&t=2737s) · b000056

**English**

getting a value so for example extracting 0.17 from that from that Gaussian or 0.23 from that Gaussian. So that gives you a vector Z which is actually a vector of numbers and then once you decode it it will be different images ideally with the change that you wanted when you change that single variable. Yes,

**中文**

取一个值，比如从那个 Gaussian 中取出 0.17，或者从那个 Gaussian 中取出 0.23。这样你就得到一个向量 Z，它实际上就是一个由数字组成的向量。然后一旦把它解码，就会得到不同的图像，理想情况下，具有你改变那个单独变量时想要的变化。对，

### [46:07](https://www.youtube.com/watch?v=LGBQ0c_4HBA&t=2767s) · b000057

**English**

if you train the model well. Yes. Um people have shown actually quite a lot. If you look at VAE and our to division models which are even more better um even like you know five years ago they could train very easily know changing various aspects of faces. That was a big big way of testing it. Um for these digits you could keep the digit but change the style. So different ways of writing the letter nine. Or it could keep the style but change a digit. So zero, one, two, three with the same slant with the same handwriting. You kind of change it across different different variations.&gt;&gt; Yeah.

**中文**

如果模型训练得好。是的。嗯，人们实际上已经展示了很多例子。如果你看 VAE 和 our to division models \[字幕疑误，可能指 diffusion models\]，后者甚至更好，嗯，即使在，你知道，五年前，他们也能非常容易地训练出能改变人脸各个方面的模型。这是测试它们的一种非常、非常重要的方法。嗯，对于这些数字，你可以保持数字不变，但改变风格。所以，是书写字母 nine 的不同方式。或者保持风格不变，但改变数字。所以，零、一、二、三，具有相同的倾斜度、相同的笔迹。你可以在不同、不同的变化因素之间做改变。&gt;&gt; 对。

### [46:46](https://www.youtube.com/watch?v=LGBQ0c_4HBA&t=2806s) · b000058

**English**

&gt;&gt; Do you actually already know which categories are supposed to be trained on? And do you already know the range? Smile. Should it go one to one and a positive value? You wouldn't you wouldn't know any of these. You wouldn't know any of these. Remember these are these are latent variables. So the only thing you are given is lots of faces. That's all you're given. You're not given for each face labels for whether a person is smiling or not or the length of the hair. You're not given all of this.&gt;&gt; But it's just like you look at one face at a time. So on the first case, you probably don't. And then that violates as you Yeah. Yeah. Yeah. Yeah. Because it's a reconstruction objective, right? So two two key things. So there's a bottleneck and a reconstruction objective. The bottleneck is important because now you're forcing let's say let's say my Z

**中文**

&gt;&gt; 你实际上已经知道应该训练哪些类别了吗？你也已经知道取值范围了吗？微笑。它应该从一到一，再到一个正值吗？你不会，你不会知道这些。你不会知道这些。记住，这些是，这些是潜变量。所以，你得到的唯一东西就是大量人脸。你只有这些。并不会为每张脸提供这个人是否在微笑，或者头发长度的标签。所有这些都没有提供给你。&gt;&gt; 但这就像是每次只看一张脸。所以，在第一个例子中，你可能不知道。然后随着你……这就违反了……对。对。对。对。因为这是一个重建目标，对吧？所以有两个、两个关键点。有一个瓶颈，还有一个重建目标。瓶颈很重要，因为现在你在强制，假设，假设我的 Z

### [47:42](https://www.youtube.com/watch?v=LGBQ0c_4HBA&t=2862s) · b000059

**English**

is maybe just 10, right? I'm forcing like 100,000 images through these 10 dimensions. If these 10 dimensions end up memorizing each face, then you will have very bad reconstruction. This bottleneck forces the model to isolate one dimension just to capture like the first PCA right which is how the hair changes and then the second dimension will capture the second most important PCA which is maybe the glasses. So this bottleneck is is is crucial. Uh that's why the smaller and then bigger the bottleneck plus the reconstruction in the reconstruction is good. And then this prior essentially smooths out the space so that you are you're basically saying you know this this glasses very variable is kind of smooth and there's no pockets where suddenly the glasses disappear. So it's kind of smooth and you can interpolate between it. I guess glasses was the best example because it's not continuous but maybe the length of the hair should be smoothly interpolating for interpolating from

**中文**

可能只有 10，对吧？我在强迫大约 100,000 张图像通过这 10 个维度。如果这 10 个维度最终只是记住每张脸，那么重建效果会很差。这个瓶颈迫使模型隔离出一个维度，专门捕捉类似第一个 PCA 的东西，对吧，也就是头发如何变化。然后第二个维度会捕捉第二重要的 PCA，也许就是眼镜。因此，这个瓶颈是、是、是至关重要的。呃，这就是为什么先变小再变大，瓶颈加上重建，重建是好的。然后，这个先验基本上会平滑空间，所以你实际上是在说，你知道，这个眼镜变量有某种平滑性，不会出现一些小区域，让眼镜突然消失。所以它是相对平滑的，你可以在其间做插值（interpolate）。我想眼镜是最好的例子，因为它不是连续的，但也许头发长度应该可以平滑插值，从

### [48:39](https://www.youtube.com/watch?v=LGBQ0c_4HBA&t=2919s) · b000060

**English**

from short to long.&gt;&gt; Yes.&gt;&gt; When you speak of smoothness, are you specifically speaking to how these gas there's like much less sparity between the data points? Is that&gt;&gt; Yeah. Yeah. Um not not too many gaps in the data points. Did you have&gt;&gt; um so theians that are blue on the next slide are they are they are they like based on the data&gt;&gt; these are the posteriors. Yeah. So these are XQ and Z's. Yeah. Yeah.

**中文**

从短到长。&gt;&gt; 有，请说。&gt;&gt; 当你说平滑性时，你具体是指这些 gas \[字幕疑误，可能指 Gaussians\]，也就是数据点之间的 sparity \[字幕疑误，可能指 sparsity，稀疏性\] 小得多吗？是这个意思吗？&gt;&gt; 对。对。嗯，数据点之间没有太多空隙。你有……&gt;&gt; 嗯，所以下一张幻灯片中蓝色的 theians \[字幕疑误，可能指 Gaussians\]，它们，它们，它们是基于数据的吗？&gt;&gt; 这些是后验（posteriors）。对。所以这些是 XQ 和 Z。对。对。

### [49:20](https://www.youtube.com/watch?v=LGBQ0c_4HBA&t=2960s) · b000061

**English**

Okay. So let me recap. So encoder decoder structure with a bottleneck. And bottleneck is key so that you're actually learning individual factors of variation instead of uh memorizing your data. The latent variable Z is actually quite simple with a prior but your P of X given Z uh is quite both both a Z given X and X given Z can be quite expressive because you have neuronet networks as the encoder and decoder. objectives first for reconstruction image comes in encoder decoded to reconstruct the image and then a prior latent variable Z. So this essentially smooths out your latent space with this like rounding without too many gaps within this latent space and that permits sampling right from anywhere within the space ideally there's no gaps and also disentanglement right so that different factors so ideally you have this interpretable structure within the

**中文**

好。那么让我回顾一下。带有瓶颈的编码器—解码器结构。瓶颈是关键，这样你才能真正学习各个独立的变化因素，而不是，呃，记住数据。潜变量 Z 实际上相当简单，带有一个先验，但你的给定 Z 的 P(X)，呃，相当，给定 X 的 Z 和给定 Z 的 X 都可以很有表达能力，因为你使用神经网络作为编码器和解码器。目标首先是重建：图像输入，经过编码器，解码以重建图像；然后是潜变量 Z 的先验。所以，这基本上通过这种类似圆整的方式平滑潜在空间，让潜在空间内部没有太多空隙。这就允许采样，对吧，理想情况下可以从空间中的任何位置采样，没有空隙。还有解耦（disentanglement），对吧，让不同因素，所以理想情况下，你的

### [50:17](https://www.youtube.com/watch?v=LGBQ0c_4HBA&t=3017s) · b000062

**English**

Z's where all of them mean something slightly different and they're in some sense all kind of perpendicular to each other so you can mix and match them however you again enabled by by the bottleneck right that minimizes the redundancy by forcing the model to use a bottleneck and also this prior kind of forces each of them to have zero co-variance with each other any final questions about VAES okay to more recent models uh diffusion models I'm sure all of you have heard the term, but it's good to explain diffusion models uh building on the foundation for VAEs because they essentially also follow this encoder decoder structure except there are several key differences. So we're still using X to represent data. So on the left uh on the

**中文**

Z 中会有这种可解释的结构，其中每个分量的含义都有些不同，而且从某种意义上说，它们彼此都近似垂直，所以你可以任意混合搭配它们。这再次由瓶颈实现，对吧，通过强制模型使用瓶颈来最小化冗余。而且，这个先验也在某种程度上迫使它们彼此之间具有零协方差。关于 VAES \[字幕疑误，可能指 VAEs\]，还有最后的问题吗？好，接下来讲更新的模型，呃，diffusion models。我相信你们都听说过这个术语，不过，基于 VAEs 的基础来解释 diffusion models 很有帮助，因为它们基本上也遵循这种编码器—解码器结构，只是存在几个关键区别。所以，我们仍然用 X 来表示数据。所以在左边，呃，在

### [51:14](https://www.youtube.com/watch?v=LGBQ0c_4HBA&t=3074s) · b000063

**English**

left over there that's that's an image maybe we're trying to generate but now we're going to introduce this subscript know x0 right this zero is going to represent or more generally this t is going to represent some time dimension in these diffusion models right there's still an encoding process and a decoding process so it shares similarities with ees but now this encoding and decoding is done across multiple steps and there's a very specific way of encoding into your latent space and decoding from a latent space right so specifically encoding which I'm writing here as this q function so still using the q for encoding first it's going to get x1 given x0 and then x2 given x1 so it's going to keep encoding and each encoding step is basically adding a little bit of noise to your data to the previous step of data right so I'm still using q encoding but notice there aren't any parameters now but encoding doesn't have any parameters that you have to train

**中文**

左边那里，那是一张我们可能想生成的图像。但现在我们要引入这个下标，你知道，x0，对吧。这个零将表示，或者更一般地，这个 t 将表示 diffusion models 中的某个时间维度，对吧。仍然有一个编码过程和一个解码过程，所以它与 ees \[字幕疑误，可能指 VAEs\] 有相似之处，但现在编码和解码是跨多个步骤完成的，而且编码到潜在空间、从潜在空间解码，都采用一种非常具体的方式，对吧。所以，具体来说，编码，我在这里写成这个 q 函数，因此仍然用 q 表示编码，首先得到给定 x0 的 x1，然后是给定 x1 的 x2。它会不断编码，而每个编码步骤基本上就是往数据中、往前一步的数据中加入一点噪声，对吧。所以我仍然用 q 表示编码，但注意，现在没有任何参数，编码没有任何需要训练的参数，

### [52:11](https://www.youtube.com/watch?v=LGBQ0c_4HBA&t=3131s) · b000064

**English**

because adding noise is basically Okay, just code that up and add noise to your data. There's no parameters to train. So you see it slowly start to increase adding noise. The image is going to become more and more blurry until eventually it reaches a state of XT which can be thought about as your latent variable which is purely noise purely Gaussian noise. That's your encoding steps. Uh people also call it diffusion process. And of course what is this key is not about adding noise to data. It is to generate data from noise your latent variables. So that can be thought of as the decoding step. Okay. It's going to start from the most noisy version X big T. And now you actually have to start learning something. You start learning something and what you are trying to learn is how to remove the noise that you have added at every time step. So that can be thought of as a as a

**中文**

因为添加噪声基本上就是，好，把它写成代码，然后向数据添加噪声。不需要训练任何参数。所以你会看到，它逐渐开始增加噪声。图像会变得越来越模糊，直到最终到达 XT 状态，你可以把它看作潜变量，它完全是噪声，完全是高斯噪声（Gaussian noise）。这就是编码步骤。呃，人们也把它叫作扩散过程（diffusion process）。当然，关键并不是向数据添加噪声，而是从噪声，也就是潜变量中生成数据。所以，这可以看作解码步骤。好。它从噪声最多的版本 X 大写 T 开始。现在你确实需要开始学习一些东西。你开始学习，而你试图学习的是，如何移除每个时间步所添加的噪声。因此，这可以看作一个，一个

### [53:06](https://www.youtube.com/watch?v=LGBQ0c_4HBA&t=3186s) · b000065

**English**

function P. Now it has parameters data. So that's going to be a neon network parameters that you're trying to learn parameters data. And what it's essentially giving is xt minus one. So this previous time step with a little bit less noise given xt the time step with more noise. Okay. And that is going to go through across multiple steps across your teps. Uh essentially going back to x0 which is your original image. So that can be thought of as the multi-step decoding process. Decoding from noise, trying to train a model to remove a little bit of noise each time until you get back the original clean data. U people also call this reverse diffusion process.

**中文**

函数 P。现在它有参数 data \[字幕疑误，可能指 theta\]。所以，那会是你试图学习的 neon network \[字幕疑误，可能指 neural network\] 参数，参数 data。它基本上给出的是 xt minus one，也就是在给定噪声较多的时间步 xt 时，得到前一个噪声稍少的时间步。好。它会经过多个步骤，经过你的 teps \[字幕疑误，可能指 steps\]。呃，基本上回到 x0，也就是原始图像。所以，这可以看作多步解码过程。从噪声中解码，训练一个模型，每次去除一点噪声，直到恢复原始干净数据。呃，人们也把它叫作反向扩散过程（reverse diffusion process）。

### [53:52](https://www.youtube.com/watch?v=LGBQ0c_4HBA&t=3232s) · b000066

**English**

So that's the setup. Um as I mentioned encoding by adding noise each of these Q functions that give you XT given XT minus one. So that's encoding one step further into the diffusion process is basically just adding noise or you can think about it as defining a Gaussian uh centered at um xt minus one with some scaling factor and adding some variance to it. Right? So it's defining a gaussian centered at the previous data point with some variance and you're sampling from it. So the variance that you add adds noise to the previous image. So that's encoding process. no parameters to be learned. This alpha t is basically a scheduling parameter. Uh you basically add a little bit less noise at the beginning and you add bigger noise later, right? Or you can think about it as sampling from a gaussian with a smaller variance at the beginning that adds less noise. Sampling with a variance with a sampling from

**中文**

所以，这就是基本设定。嗯，正如我提到的，编码是通过添加噪声完成的，每一个给出给定 XT minus one 的 XT 的 Q 函数，也就是在 diffusion process 中进一步编码一步，基本上都只是在添加噪声。或者你可以把它看作定义一个 Gaussian，呃，以带有某个缩放因子的 xt minus one 为中心，再加入一些方差。对吧？所以，它定义了一个以先前数据点为中心、带有某个方差的 Gaussian，然后从中采样。因此，你加入的方差会给前一张图像添加噪声。这就是编码过程，没有需要学习的参数。这个 alpha t 基本上是一个调度参数（scheduling parameter）。呃，你基本上在开始时加入少一点的噪声，后面加入更大的噪声，对吧？或者，可以把它理解为，一开始从方差较小的 Gaussian 中采样，因此添加的噪声较少。用一个方差采样，从一个

### [54:50](https://www.youtube.com/watch?v=LGBQ0c_4HBA&t=3290s) · b000067

**English**

Gaussian bigger variance later that adds more noise. And this decoding process is basically you can think about it as removing noise, right? So for each of those P of theta, you're going to learn a function to remove the noise that was added from the previous step. Any questions about the setup? So of course the key trick is how to actually learn this model. How to learn those P of thetas. Again the Q adding noise is just a fixed function. How to learn this P of thetas that gradually remove noise. Well, the mathematics behind this is actually fascinating similar to the mathematics behind variational autoenccoders and therefore the training objective that you end up deriving is also very similar to VAE. Okay, it is um oh sorry let me let me first say this. So again the the model itself

**中文**

方差更大的 Gaussian 中在后期采样，就会加入更多噪声。而这个解码过程，基本上可以看作去除噪声，对吧？所以，对于每个 P of theta，你要学习一个函数，去除前一步添加的噪声。关于这个设定，有什么问题吗？当然，关键技巧是如何真正学到这个模型，如何学习这些 P of theta。再次强调，Q 添加噪声只是一个固定函数。如何学习这些逐渐去除噪声的 P of theta 呢？嗯，背后的数学实际上非常有意思，与变分自编码器背后的数学相似，因此最终推导出的训练目标也和 VAE 非常相似。好，它是，嗯，哦，抱歉，让我先说这个。所以，再次来说，模型本身

### [55:47](https://www.youtube.com/watch?v=LGBQ0c_4HBA&t=3347s) · b000068

**English**

is very similar to VAE with several key differences. First of all, the latent dimension is the same throughout, right? There is no longer a bottleneck, right? The latent dimension is the same as the original image, which is the same as the noisy version of the image all the way until the full noise. So, the dimension is exactly equal to the data dimension in the first iterations of diffusion models. The encoder Q is not learned, but it's predefined as a delta distribution centered around the image. In the previous time step, we discussed this. Um so there's no learning in the encoder and these Gaussian parameters vary over time so that the final distribution the final latent states that you learn again becomes a standard Gaussian. So how to learn this? I'm going to skip the math but essentially it ends up being several training objectives that are the same as EAS to be honest. So you're going to see some reconstruction terms like this right. Right? How to

**中文**

与 VAE 非常相似，但有几个关键区别。首先，潜在维度始终相同，对吧？不再有瓶颈，对吧？潜在维度与原始图像相同，也与图像的带噪版本相同，一直到完全变成噪声。所以，在最初几代 diffusion models 中，这个维度与数据维度完全一致。编码器 Q 不是学出来的，而是预先定义为一个以图像为中心的 delta distribution \[原文如此，与前文 Gaussian 的说法不一致\]。在前一个时间步，我们讨论过这个。嗯，所以编码器中没有学习过程，而且这些 Gaussian 参数会随时间变化，使得最终的分布、最终学到的潜在状态再次成为标准 Gaussian。那么，如何学习这个呢？我会跳过数学，但基本上，最终得到的是几个训练目标，老实说，与 EAS \[字幕疑误，可能指 VAEs\] 相同。所以你会看到一些像这样的重建项（reconstruction terms），对吧。对吧？如何

### [56:43](https://www.youtube.com/watch?v=LGBQ0c_4HBA&t=3403s) · b000069

**English**

interfer these reconstruction terms is basically that if I take in X0, right? I first sample under this. So I take in X0, I predict what X1 will be, which is a noisy version of X0. And then I'm going to put that through the dnoising step of that X1 and try to reconstruct the original X0. Right? So it's exactly the reconstruction objective. X0 comes in, I add noise to get X1 and I pass it through the removal of noise to go back to X0 and I see how well that matches the original X0. So that's a reconstruction term. There's going to be a prior matching term which is that this final prior, right? This uh distribution over XT uh is going to be some standard Gaussian, right? Again you have this prior matching term helps out to smooth this final distribution. So you can basically

**中文**

理解这些重建项呢？基本上就是，如果我输入 X0，对吧，先按照这个分布采样。所以我输入 X0，预测 X1 会是什么，它是 X0 的带噪版本。然后，我会让那个 X1 经过一次去噪（denoising）步骤，尝试重建原始 X0。对吧？所以这正是重建目标。X0 输入，我添加噪声得到 X1，再通过去除噪声回到 X0，然后看它与原始 X0 匹配得有多好。所以，这是一个重建项。还会有一个先验匹配项（prior matching term），意思是，最终的这个先验，对吧，这个，呃，XT 上的分布，会是某个标准 Gaussian，对吧？同样，你有这个先验匹配项，帮助平滑最终分布。所以，你基本上可以

### [57:38](https://www.youtube.com/watch?v=LGBQ0c_4HBA&t=3458s) · b000070

**English**

sample from any noise vector in this space and it would all come up to be a good image. Again we want this final latent space to be smooth without any holes in it. So anything that we sample we can decode back into an image. So reconstruction term with a prior term up to now exactly the same as VAE. Um it's perhaps unsurprising. You can guess what the last term is. is that you're going to have all these intermediate reconstruction terms, right? Not just for the very first time step, but for all of these intermediate time steps. So at any time step over here, I'm going to say uh if I take in XT minus one, I'm going to add noise to get XT. And for what I predict at XT, I'm going to dn noiseise it back to XT minus one. And how closely that matches the original input image that was less noisy. can be thought of as all of these little reconstruction terms across all your steps and a final prior over your latent

**中文**

从这个空间中的任意噪声向量采样，而它们都能产生一张好图像。再次强调，我们希望最终潜在空间是平滑的，没有任何空洞。所以，我们采样出的任何东西，都能被解码回一张图像。因此，到目前为止，重建项加上先验项，与 VAE 完全相同。嗯，这也许并不令人意外。你可以猜到最后一项是什么，就是你会有所有这些中间重建项，对吧？不仅针对第一个时间步，也针对所有中间时间步。所以，在这里的任意时间步，我会说，呃，如果我输入 XT minus one，就添加噪声得到 XT。对于在 XT 处预测出的东西，我会将其去噪，回到 XT minus one。然后看它与原先噪声较少的输入图像有多接近。这可以看作贯穿所有步骤的这些小重建项，再加上潜

### [58:35](https://www.youtube.com/watch?v=LGBQ0c_4HBA&t=3515s) · b000071

**English**

variables. So you can essentially think of it as a as a multi-level VA. Yeah.&gt;&gt; Can you So do all do all images at the variable kind of ging noise uh in the same number of steps? Um, good question. I would assume they are they could be different. Uh, but you can at some point you can keep adding noise and it wouldn't really change from Gaussian noise. So you can always pad it to the largest amount of T. Again T is some hyperparameter that you have to define here.

**中文**

变量上的一个最终先验。所以，你基本上可以把它看作一个，一个多层 VA \[字幕疑误，可能指 VAE\]。对。&gt;&gt; 能不能，所以所有、所有图像在变量处变成噪声，呃，都需要相同数量的步骤吗？嗯，好问题。我会假设它们可能不同。呃，但在某个时候，你可以继续添加噪声，它也不会真正偏离 Gaussian noise。因此，你总可以把它补齐到最大的 T。再次强调，这里的 T 是一个必须定义的超参数。

### [59:23](https://www.youtube.com/watch?v=LGBQ0c_4HBA&t=3563s) · b000072

**English**

Any other questions? So think about it as the same as VAEEs. Instead of being a one encoder and then decoder VAE in which you have one reconstruction objective and one prior objective, now you have multiple steps. Each step is adding noise and each reverse step is removing noise. So you have all these little steps of reconstruction, right? The adding noise and then removing noise should be the same as the original input. You do this over multiple times. ly add all these terms up and your eventual prior uh eventual latent variable should again respect some prior to make sure the latent space is smooth.

**中文**

还有其他问题吗？所以，可以把它看作与 VAEEs \[字幕疑误，可能指 VAEs\] 相同。它不再是一个编码器接一个解码器的 VAE，只有一个重建目标和一个先验目标，现在你有多个步骤。每一步添加噪声，每一个反向步骤去除噪声。所以，你有所有这些小的重建步骤，对吧？添加噪声再去除噪声之后，应该与原始输入相同。你重复做很多次。把所有这些项加起来，最终的先验，呃，最终的潜变量也应该遵循某个先验，确保潜在空间平滑。

### [1:00:07](https://www.youtube.com/watch?v=LGBQ0c_4HBA&t=3607s) · b000073

**English**

Okay, so intuition is to again for each of those D noisy steps, it's a neuronet network to predict the cleaner image XT minus one from the noisy image XT at time t right that is consistent with the noise adding process. So that those are intuitions of each of the the models that you train during diffusion.

**中文**

好，所以直觉还是，对于每个 D noisy \[字幕疑误，可能指 denoising\] 步骤，都用一个神经网络，从时间 t 的带噪图像 XT 预测更干净的图像 XT minus one，对吧，并且与添加噪声的过程一致。所以，这些就是 diffusion 期间训练的各个模型的直觉。

### [1:00:35](https://www.youtube.com/watch?v=LGBQ0c_4HBA&t=3635s) · b000074

**English**

So several interpretations uh in fact people have shown us three equivalent interpretations which is that basically for every time step for every noisy it basically trains diffusion models so that at every noisy step no matter very little bit of noise or a lot of noise can you successfully reconstruct the original clean image. That's one way of interpreting it. Another way of interpreting it is for every step can I predict what was the noise that was just added. Right? If I can predict what was the noise that I just added then I can just reverse it and remove the noise that was just added. So that can be thought of as noise prediction. First one is original image prediction. Second one is noise prediction. And the third one is some people will call it as velocity function which basically I guess good schematics. So you have a partially noisy image. You can either think about it as predicting the clean image,

**中文**

所以，有几种解释，呃，实际上人们展示了三种等价的解释。基本上，对于每个时间步、每个带噪的，基本上训练 diffusion models，使它在每个带噪步骤中，无论噪声很少还是很多，都能成功重建原始干净图像。这是一种理解方式。另一种理解方式是，在每一步，我能否预测刚刚添加了什么噪声。对吧？如果我能预测刚刚添加的噪声是什么，就可以把它逆转，去除刚刚添加的噪声。所以，这可以看作噪声预测（noise prediction）。第一种是原始图像预测（original image prediction），第二种是噪声预测。第三种，有些人称之为速度函数（velocity function），基本上，我想，这里有个很好的示意图。所以，你有一张部分带噪的图像。你可以把它看作预测干净图像，

### [1:01:31](https://www.youtube.com/watch?v=LGBQ0c_4HBA&t=3691s) · b000075

**English**

you can think about it as predicting the noise lesser or you can think about predicting the next step of the noisy image. Right? All of these are are equivalent interpretations to each other. Um, but of course some people make the argument that predicting the original clean image is easier than predicting a slightly less version, a slightly less noisy version of the image. and is also easier than predicting the noise itself. Even though they're equivalent, the the raw image is uh the real image is kind of in a lower dimensional space um a semantically meaningful space which makes it easier to predict. Yes.

**中文**

也可以把它看作预测 noise lesser \[原文不清\]，或者预测带噪图像的下一步。对吧？这些都是相互等价的解释。嗯，不过当然，有些人认为，预测原始干净图像比预测图像一个稍少的版本、噪声稍少的版本更容易，也比预测噪声本身更容易。尽管它们等价，原始图像，呃，真实图像位于某种更低维的空间，一个语义上有意义的空间，这让它更容易预测。有，请说。

### [1:02:14](https://www.youtube.com/watch?v=LGBQ0c_4HBA&t=3734s) · b000076

**English**

Why? Because um almost all data is almost all data that we care about that is high dimensional actually lies on a lower dimensional manifold. Right? That's why you can do PCA and you can see the first couple of components are very large and it then drops down very quickly. That's why you can do autoenccoders where you encode your data into smaller dimensions and then decode it. Right? It's not the case for noise. Like epsilon is just actual Gaussian noise. Noise is going to is not compressible. If you do PCA or noise, you see all the principal vectors are are just uniform and the same as the full dimension of your noise. So even though these three limitations using a noisy image to predict the original clean image to predict a slightly less noisy version of it or to predict the immediate noise added they all mathematically should turn out to be the same. But what is easiest in practice is to predict the original

**中文**

为什么？因为，嗯，几乎所有数据，几乎所有我们关心的高维数据，实际上都位于一个更低维的流形（manifold）上。对吧？这就是为什么你可以做 PCA，并看到前几个主成分很大，然后迅速下降。这也是为什么你可以使用 autoencoders，把数据编码到更小的维度，再解码。对吧？噪声不是这样。比如 epsilon 就是真正的 Gaussian noise。噪声会，是不可压缩的。如果对噪声做 PCA，你会看到所有主向量都是均匀的，并且与噪声的完整维度一样。所以，尽管这三种 limitations \[字幕疑误，可能指 formulations\]，也就是用带噪图像预测原始干净图像、预测一个噪声稍少的版本，或者预测刚刚添加的噪声，在数学上应该都相同。但在实践中，最容易的是从每一个可能的带噪步骤预测原始

### [1:03:11](https://www.youtube.com/watch?v=LGBQ0c_4HBA&t=3791s) · b000077

**English**

clean version of the image from every possible noisy step. Okay. Okay. So these uh these models are are amazing, right? These models allow you to have super super high resolution generation. Um they in my opinion I mean people don't really know why exactly but I have some intuition. So you think about these VAEEs, they have a single step encoding and decoding and sometimes this singlestep encoding and decoding is insufficient, right? Takes the data to like Gaussian vectors too quickly and decodes the Gaussian vectors to data too quickly, right? You can think about these diffusion models as really doing this gradual process, gradual process that goes from raw data to a little bit noisier version and then trying to remove that. It's a simpler problem and then it goes add a little bit more noise

**中文**

干净图像。好。好。所以，这些，呃，这些模型非常惊人，对吧？它们能让你生成超级、超级高分辨率的图像。嗯，在我看来，我是说，人们其实并不确切知道为什么，但我有一些直觉。你想想这些 VAEEs \[字幕疑误，可能指 VAEs\]，它们只有一步编码和一步解码，有时候这种单步编码和解码并不够，对吧？把数据转换成 Gaussian 向量太快，把 Gaussian 向量解码成数据也太快，对吧？你可以把这些 diffusion models 看作真正执行了一个渐进过程，从原始数据到噪声稍多一点的版本，然后尝试去掉那些噪声。这是一个更简单的问题，然后它再添加一点噪声，

### [1:04:08](https://www.youtube.com/watch?v=LGBQ0c_4HBA&t=3848s) · b000078

**English**

removes it slightly simpler problem. So this really helps the model train.&gt;&gt; Yeah.&gt;&gt; I wonder the first few den noising steps causely kind of like almost like anchoring the final diffused uh image like are you already like going down the path the moment you start?&gt;&gt; Yeah. Yeah. Yeah. They have some important scheduling factors. Um so you want to basically kind of um add smaller noise at the beginning of the fusion process because that's when the model is just starting to to learn to train and then you gradually increase noise when your samples get noisier because if your sample is really very noisy adding more noise kind of doesn't really change it that much. So there's some important scheduling process. Um there are some lots of cool animations as well showing that um yeah it's important to add little noise at the beginning and more noise at the end. And in fact, one of you asked a questions about how to set

**中文**

再把它去掉，又是一个稍微更简单的问题。所以，这确实有助于模型训练。&gt;&gt; 对。&gt;&gt; 我想知道，最初几个 den noising \[字幕疑误，可能指 denoising\] 步骤，在因果上是不是有点像锚定最终扩散出的图像，也就是说，一开始你就已经走上某条路径了吗？&gt;&gt; 对。对。对。它们有一些重要的调度因素。嗯，所以，你基本上希望在 fusion \[字幕疑误，可能指 diffusion\] 过程开始时加入较小的噪声，因为那时模型才刚开始学习、训练。然后随着样本变得更嘈杂，逐渐增加噪声，因为如果样本已经噪声很大，再加更多噪声，其实不会让它变化太多。所以，有一个重要的调度过程。嗯，也有很多很酷的动画展示这一点，嗯，是的，在开始时加入较少噪声、最后加入更多噪声很重要。事实上，你们中有一位问过如何设置

### [1:05:06](https://www.youtube.com/watch?v=LGBQ0c_4HBA&t=3906s) · b000079

**English**

the t right the number of time steps t as how many steps of adding noise and how many steps are removing removing noise. So people have basically shown that in fact there is no hyperparameter t you can basically take it for t to be in the limit of infinity right you can interpret this not as a fixed 10 times but rather in the limit infinitely adding noise infinitely removing noise um and there's a connection between that and differential equations uh specifically you know continuous time differential equations if people are interest if people are interested

**中文**

t，对吧，也就是时间步数量 t，添加噪声需要多少步，去除、去除噪声需要多少步。人们基本上已经表明，实际上可以没有超参数 t，你基本上可以把 t 取到无穷大的极限，对吧。你可以不把它理解为固定做 10 次，而是理解为在极限中无限地添加噪声、无限地去除噪声。嗯，这与微分方程（differential equations）有联系，呃，具体来说，你知道，是连续时间微分方程（continuous-time differential equations），如果有人感兴，如果有人感兴趣的话。

### [1:05:46](https://www.youtube.com/watch?v=LGBQ0c_4HBA&t=3946s) · b000080

**English**

Okay, so diffusion models are are state-of-the-art and then just also very quickly for interest people have also extended diffusion models to flow matching models. Uh again it's small subtle differences. If you read some blog posts you'll see that some people say flow matching models are are special cases diffusion models. Uh you can think about it as diffusion models generating data by adding noise each time and then learning to reverse the removal of noise right remove reverse the the step by removing noise each time. Flow matching can be thought of as taking some of these diffusion models to the limit and viewing this whole sequence as a differential equation and just directly learning some of the parameters of this differential equation. So it removes a lot of the bottlenecks in diffusion models in a sense that they originally very slow to sample from because you got to add noise t times and you got to run this removal of noise t times. So that was very inefficient. Flow matching

**中文**

好，所以 diffusion models 是最先进的模型。然后，也很快补充一下，供感兴趣的人了解，人们还把 diffusion models 扩展到了 flow matching 模型。呃，同样，只是一些细微差别。如果你读一些博客文章，会看到有人说 flow matching 模型是 diffusion models 的特例。你可以把 diffusion models 看作通过每次添加噪声，再学习逆转去除噪声来生成数据，对吧，通过每次去除噪声来逆转那个步骤。Flow matching 可以看作把其中一些 diffusion models 推向极限，把整个序列视为一个微分方程，然后直接学习这个微分方程的一些参数。所以，它消除了 diffusion models 中的很多瓶颈，因为它们原本采样很慢：你得添加噪声 t 次，还得运行去噪 t 次。所以那非常低效。Flow matching

### [1:06:41](https://www.youtube.com/watch?v=LGBQ0c_4HBA&t=4001s) · b000081

**English**

solves some of those problems. Um I'm not going to go too much into the algorithm. Uh but you can think about it as a significantly sped up continuous time limit of diffusion models and it becomes easier to train and gives higher quality results.

**中文**

解决了其中一些问题。嗯，我不会深入讲这个算法。呃，但你可以把它看作 diffusion models 的一个显著加速的连续时间极限，它更容易训练，并且能得到质量更高的结果。

### [1:07:05](https://www.youtube.com/watch?v=LGBQ0c_4HBA&t=4025s) · b000082

**English**

Okay. So that was that was the end of the the more technical parts. I'm going to go back to the high level. So nowadays with diffusion models, you can condition them on text, condition them on frozen embeddings. They all work really well. Nowadays, people also combine diffusion models. They don't just do diffusion at the raw pixel level, but they combine it with VAE, right? If you remember, one of the biggest things about diffusion models is that the dimension stays the same each time you add noise and remove noise, right? Whereas in VAE, you first take the raw data, high dimensional, you learn some bottleneck and then you decode it. So you can combine that right some of these are latent diffusion models basically first do a VAE right you see your data X you first do an encoder that's your VAE bring it from high dimensional to latent space and then you do the fusion and latent space right that dimensional latent space is kept the same during diffusion process

**中文**

好。所以，这就是更偏技术部分的结束。我会回到宏观层面。如今，你可以让 diffusion models 以文本为条件，以冻结的嵌入（frozen embeddings）为条件。它们都效果很好。如今，人们还会把 diffusion models 组合起来。他们不只在原始像素层面做 diffusion，而是将其与 VAE 结合，对吧？如果你还记得，diffusion models 的一个最重要特点是，每次添加噪声和去除噪声时，维度都保持不变，对吧？而在 VAE 中，你先输入高维原始数据，学习一个瓶颈，然后再解码。所以你可以把它们结合起来，对吧，其中一些就是潜在扩散模型（latent diffusion models）：基本上先做 VAE，对吧，你看到数据 X，先通过编码器，这就是 VAE，把它从高维带到潜在空间，然后在潜在空间中做 fusion \[字幕疑误，可能指 diffusion\]，对吧，diffusion 过程中潜在空间的维度保持不变，

### [1:08:00](https://www.youtube.com/watch?v=LGBQ0c_4HBA&t=4080s) · b000083

**English**

and then once you're done you have the Z and you decode it using the VAE decoder back to the original input space right so it's kind of combining Best of both worlds VAE's ability to encode and decode into bottlenecks and diffusion models ability to uh to do this high quality reconstruction of the latent space. Yeah, nowadays state-of-the-art results on conditioning using any text words are still a challenge but you know they're also getting there. uh you can condition this on semantic maps. So you could paint it and say I want that to be the background, that to be the river, that to be the trees and it can generate data condition on that latent space. You can condition it based on bounding boxes. So you write about a bunch of boxes and you want people here, trees here, it can generate according to that.

**中文**

然后完成之后，你得到 Z，再用 VAE 解码器把它解码回原始输入空间，对吧。所以，它有点像是结合了两者的优点：VAE 编码到瓶颈并从中解码的能力，以及 diffusion models 对潜在空间进行高质量重建的能力。对，如今，以任意文本词语为条件来取得最先进的结果仍然是个挑战，但你知道，它们也正在接近。呃，你可以让它以语义图（semantic maps）为条件。所以你可以画出来，说我希望那部分是背景，那部分是河流，那部分是树木，它就能以那个潜在空间为条件生成数据。你还可以基于边界框（bounding boxes）来设置条件。所以你画出一堆框，希望这里有人、这里有树，它就可以据此生成。

### [1:08:57](https://www.youtube.com/watch?v=LGBQ0c_4HBA&t=4137s) · b000084

**English**

And finally um just a couple minutes before I finish, people have applied diffusion models to text as well. This is perhaps one of the fastest growing areas of research today in large language models is to go from auto reggressive language models to what are called diffusion language models. You see auto reggressive language models I mean like the ones that you have in transformers. You start with the beginning of sentence you decode one word goes back decode the next word and then so on. This is a you know forward to backward generation process. some it can be slow and the model cannot go back and correct itself right if it's generated something you cannot correct itself back at time time step number two for example so diffusion models they essentially work something like this where you kind of think about it as you know all noise at the beginning right a whole sequence the sequence of of noise and then this diffusion process takes

**中文**

最后，嗯，在我结束前的这几分钟，人们也把 diffusion models 应用到了文本上。这或许是当今大语言模型（large language models）中发展最快的研究领域之一，也就是从自回归语言模型（autoregressive language models）转向所谓的扩散语言模型（diffusion language models）。你看，自回归语言模型，我指的是 transformers 中的那类模型。你从句子开头开始，解码一个词，再回去解码下一个词，然后继续。这是一个，你知道，从前向后的生成过程。有时它可能很慢，而且模型不能回头纠正自己，对吧？如果它已经生成了某些东西，就不能回到比如第二个时间步纠正自己。所以，diffusion models 基本上这样工作：你可以把它看作，你知道，一开始全是噪声，对吧，整个序列都是噪声序列，然后这个 diffusion process 会接收

### [1:09:52](https://www.youtube.com/watch?v=LGBQ0c_4HBA&t=4192s) · b000085

**English**

the noise and removes noise each time until you eventually decode the full sentence in parallel Right? So each time you might fill in one word which is essentially removing noise. So that's filling in a word and then you fill in another word and you fill in another word fill in another word in parallel. Um so this basically means if I filled in this word I can even change it afterwards right when you fill in some word I can change it right it's not uh it's not strictly uh forward to backward generation process. Yeah. How does uh this like kind of opposite way of of generating text sequences change interpretability of models because a lot of inter techniques are based on the token position something like that. Um yeah this kind of put a wrench in that&gt;&gt; I would say I mean there's there's pros

**中文**

噪声，每次去除噪声，直到最终并行（in parallel）解码出完整句子。对吧？所以每次你可能填入一个词，这基本上就是去除噪声。也就是填入一个词，然后再填入另一个词，再填入另一个词，并行地填入另一个词。嗯，所以这基本上意味着，如果我填入了这个词，之后甚至还可以修改它，对吧？当你填入某个词时，我可以修改它，对吧？它不是，呃，它不是严格的，呃，从前向后的生成过程。对。这种有点反向的文本序列生成方式，会如何改变模型的可解释性（interpretability）？因为很多 inter techniques \[字幕疑误，可能指 interpretability techniques\] 都基于 token 位置之类的东西。嗯，是的，这有点打乱了那些方法。&gt;&gt; 我会说，我是说，有优

### [1:10:49](https://www.youtube.com/watch?v=LGBQ0c_4HBA&t=4249s) · b000086

**English**

and cons right? Um the biggest reason why people want to do this as I said uh you can fix earlier mistakes that's really powerful it can be faster right you're basically taking your whole sequence of 10 words you treat them as noise and then you in parallel generate a whole 10 words faster people don't really do this because of interpretability or at the same time people don't use language models at all because of interpretability so I would say both are equally on interpretable right uh you have the same difficulties on of running like mechanistic interpretability or sapes on either of these these models.

**中文**

点，也有缺点，对吧？嗯，人们想这样做的最大原因，正如我说的，是可以修正早先的错误，这非常强大；也可以更快，对吧？你基本上把整个 10 个词的序列当作噪声，然后并行生成整整 10 个词，更快。人们其实不是因为可解释性才这么做的，或者与此同时，人们使用语言模型也完全不是因为可解释性。所以，我会说，两者同样 on interpretable \[字幕疑误，可能指 uninterpretable，不可解释\]，对吧？呃，在这两类模型上运行机制可解释性（mechanistic interpretability）或者 sapes \[字幕疑误，可能指 SAEs\]，都会遇到同样的困难。

### [1:11:24](https://www.youtube.com/watch?v=LGBQ0c_4HBA&t=4284s) · b000087

**English**

But the biggest benefits here is that you know can fix earlier mistakes because it's not strictly left to right auto reggressive and usually faster. Uh last Tuesday someone over there asked me about different types of noise and I said usually for continuous data like images you're adding Gaussian noise that's supernatural Gaussian noise in text. The biggest bottleneck and biggest challenge of applying diffusion models to text is to figure out what kind of noise to add, right? Because if you have a token embedding, adding Gaussian noise doesn't make sense and removing Gaussian noise doesn't make sense. So because the tokens are discrete, the noise that you add in each step of diffusion and the noise that you're trying to remove at each step of diffusion should be categorical, right? So that can be thought of as u either substituting a token, substituting a character, randomly sampling another word. That's the procedure of adding noise and

**中文**

但这里最大的好处是，你知道，可以修正早先的错误，因为它不是严格从左到右的自回归，而且通常更快。呃，上周二那边有位同学问过不同类型噪声的问题，我说，通常对于图像这样的连续数据，你会添加 Gaussian noise，这很 supernatural \[字幕疑误，可能指 super natural，非常自然\]。文本中的 Gaussian noise。把 diffusion models 应用于文本的最大瓶颈和最大挑战，是弄清楚应该添加什么类型的噪声，对吧？因为如果你有一个 token 嵌入，添加 Gaussian noise 没有意义，移除 Gaussian noise 也没有意义。所以，因为 tokens 是离散的，你在 diffusion 每一步添加的噪声，以及每一步试图去除的噪声，都应该是类别型的，对吧？因此，可以把它看作，呃，替换一个 token、替换一个字符，或者随机采样另一个词。这就是添加噪声和

### [1:12:21](https://www.youtube.com/watch?v=LGBQ0c_4HBA&t=4341s) · b000088

**English**

removing noise. Um although to to be to be fair that's called discrete diffusion language models. Some people have been looking at continuous diffusion language models. So how do you use other types of noise and whether that can make things even better? So still open question. Right. Then finally, people have really scaled up some of these diffusion models for text. Lada is a popular approach. Uh Llama was the meta language model. This is Lada large language diffusion models. And you see what they essentially uh get is that you know you have a sequence of text adding noise can be thought of as you know randomly masking and dropping out and adding noise to each token. until you eventually reach full noise. That's the adding noise part. And then the noise removal is starting from full

**中文**

去除噪声的过程。嗯，不过公平地说，这叫作离散扩散语言模型（discrete diffusion language models）。有些人一直在研究连续扩散语言模型（continuous diffusion language models）。所以，如何使用其他类型的噪声，以及这是否能让结果更好？这仍然是开放问题。对。然后最后，人们确实把一些用于文本的 diffusion models 扩大到了很大的规模。Lada \[字幕疑误，可能指 LLaDA\] 是一种流行方法。呃，Llama 是 meta 的语言模型。这是 Lada，大语言扩散模型（large language diffusion models）。你看到，它们基本上得到的是，你知道，你有一个文本序列，添加噪声可以看作，你知道，随机遮蔽、丢弃，并向每个 token 添加噪声，直到最终达到完全噪声。这是添加噪声的部分。然后，去噪是从完全

### [1:13:18](https://www.youtube.com/watch?v=LGBQ0c_4HBA&t=4398s) · b000089

**English**

noise and slowly adding uh adding back one word or you know fixing one character at a time until you get back the actual sentence.

**中文**

噪声开始，慢慢添加，呃，每次加回一个词，或者，你知道，修正一个字符，直到恢复真正的句子。

### [1:13:31](https://www.youtube.com/watch?v=LGBQ0c_4HBA&t=4411s) · b000090

**English**

All right, one last slide before before I finish to really bring it back to, you know, some of the things we talked about. uh there's another paper called MA multimodal large diffusion language models also quite relevant. So now it's applying diffusion to multimodal models. So you have the same things you have your text EQA, you have your multimodal reasoning, you have your text to image generation. The biggest difference now is that you have a sequence of text and a sequence of images. Instead of going through transformers, they go through diffusion models, right? So the text part by adding noise, you would maybe drop out different tokens and add your, you know, discrete text noise. The series of image tokens, you would add noise by adding Gaussian noise, right? Because that's continuous until both your concatenated sequence of text and image until both becomes pure noise. That's a forward

**中文**

好，结束之前的最后一张幻灯片，真正把话题带回到，你知道，我们讨论过的一些内容。呃，还有一篇论文叫 MA \[字幕疑误，可能指 MMaDA\]，多模态大扩散语言模型（multimodal large diffusion language models），也很相关。所以，现在是把 diffusion 应用到多模态模型中。你有相同的东西，有文本 EQA，有多模态推理（multimodal reasoning），有文本到图像生成。现在最大的区别是，你有一个文本序列和一个图像序列。它们不再经过 transformers，而是经过 diffusion models，对吧？所以，文本部分在添加噪声时，你可能会丢弃不同的 tokens，再添加，你知道，离散文本噪声。对于图像 token 序列，你会通过加入 Gaussian noise 来添加噪声，对吧？因为它是连续的，直到拼接（concatenated）起来的文本和图像序列都变成纯噪声。这就是前向

### [1:14:27](https://www.youtube.com/watch?v=LGBQ0c_4HBA&t=4467s) · b000091

**English**

encoding part. And then in the decoding part, you're going to train the model to uh remove a little bit of noise each time, right? From the image, you remove the Gaussian noise until you get back the image sequence. From text, you remove the categorical noise and add back in the words one by one until you get back the original text sequence. So that's the uh the pre-training that you do for some of these recent multimodal diffusion language models. Okay. And of course, lots of resources. This is perhaps the fastest growing space last year and this year. So lots of resources for training, evaluating diffusion models and applying them for all sorts of modalities and multimodal problems. All right, I'll stop here and that's all we'll cover for the midterm. Uh let me know if there's any any questions about the lecture or about your projects and homeworks. Yes.

**中文**

编码部分。然后在解码部分，你会训练模型，呃，每次去除一点噪声，对吧？对于图像，你移除 Gaussian noise，直到恢复图像序列。对于文本，你移除类别型噪声，并把词逐个加回来，直到恢复原始文本序列。所以，这就是这些近期多模态扩散语言模型中的一些模型所做的预训练。好。当然，还有大量资源。这或许是去年和今年发展最快的领域。所以，有很多关于训练、评估 diffusion models，以及把它们应用于各种模态和多模态问题的资源。好，我就讲到这里，这些就是期中考试涵盖的全部内容。呃，关于这节课，或者你们的项目和作业，如果有任何问题，请告诉我。有，请说。
