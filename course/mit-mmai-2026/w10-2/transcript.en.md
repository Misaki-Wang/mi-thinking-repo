# Lecture 11 – Cross-Modal Transfer (MIT How to AI Almost Anything/Multimodal AI, Spring 2026)

_English transcript_

- Channel: Paul Liang
- Source: [YouTube](https://www.youtube.com/watch?v=IDaMEG_zY6A)
- Duration: 1:08:37
- Caption source: automatic
- Status: complete
- Chinese translation: 83/83
- Translation provider: codex
- Generated: 2026-09-07T07:59:05+00:00

## Transcript

### [00:01](https://www.youtube.com/watch?v=IDaMEG_zY6A&t=1s) · b000001

All right folks, welcome back. So uh today we'll be talking about uh crossmodal transfer last lecture on foundational and core concepts and then rest of the lectures will mostly be about application oriented topics. Uh midterm results and grades have been released and um the homework should also be up today and due in one and a half weeks and thanks everyone for submitting their uh midterm report. We'll look through those and give you all feedback in the next week or so as you prepare for the final reports. All right. So crossodal transfer um as an overview we will discuss the basics of crossodal transfer and we'll show how crossodal transfer can be achieved via three different approaches fusion based

### [00:57](https://www.youtube.com/watch?v=IDaMEG_zY6A&t=57s) · b000002

approaches alignment based approaches and translation based approaches. So at a high level what is crossodal transfer? Crossodal transfer or transference aims to transfer knowledge between modalities usually from a primary modality to a secondary modality where the one that you really care about has a very limited resources or very noisy or lots of missing data. So one way is you know if you care about making some prediction in this primary modality let's say medical images right it's very difficult to get medical images it's very difficult to get them annotated there's privacy concerns you get a lot of data how can you use natural images as a way of helping transfer information towards a task that you care about more broadly how can you even use things like medical textbooks largecale databases that are not exactly in a domain of the task that you care

### [01:54](https://www.youtube.com/watch?v=IDaMEG_zY6A&t=114s) · b000003

about but for where there is some overlap in information and with transfer is possible. Right? So we call that transfer learning or transferring knowledge. That's one way of achieving crossodal transfer. Another way of achieving cross modal transfer is through this idea of co-learning. Co-learning basically means again you have this modality that you care about making predictions in. Can I use some extra information to train the model with an input or some extra information to train my model as a prediction target in the output? Right? So you see I use a I use dotted lines over here to indicate the fact that this extra modality is provided during training either as an extra input signal or as an extra prediction target during training. But during testing and during inference, you still only have this primary modality that you care about, right? That makes it fair to compare to other approaches during testing. Right?

### [02:51](https://www.youtube.com/watch?v=IDaMEG_zY6A&t=171s) · b000004

If you're giving additional information when you're deploying the model, then you're making unfair comparisons. But you can add more information than you want during training. And finally, a third way of achieving transfer that we'll talk about is this idea of model induction. So in this case you are keeping two models separate right you don't want to for example adjust the architecture of your model to take in an additional input or you don't want to adjust your training objective to make some extra prediction on the output. So in this case transfer is achieved by keeping both of these models separate but as you can see later down the line there will be some way of inducing behavior between them so that transfer is possible. All right. So three types. First transfer where you start with a base model that is very powerful and you adapt it to the task that you care about with much more limited data. Co-learning where

### [03:48](https://www.youtube.com/watch?v=IDaMEG_zY6A&t=228s) · b000005

fundamentally you are modifying the training of the model that you care about either using some additional extra input or an extra output prediction target. And model induction where you're keeping models separate but allowing them to induce behavior between each other. Transfer is perhaps the easiest, right? We've clearly all seen examples of transfer nowadays where you have pre-trained models, for example, language models or birds or other information in the way of the model parameters. That is the modality that has much more abundant data. Then a question becomes how do you adapt it quickly to a modality with much more limited data, right? how to use that as some either initial parameters or initial knowledge so that it can be subsequently used for your downstream model right I'm not going to cover everything that we've already seen for example you can always obviously

### [04:44](https://www.youtube.com/watch?v=IDaMEG_zY6A&t=284s) · b000006

initialize right your your model with a pre-trained model like a lamb parameters or bird parameters or vision model parameters and then you can start fine-tuning what are the tasks that you care about using the very limited data that you have right it can be done using fine-tuning in context learning, instruction tuning, everything that we've seen so far in class. Right? Just as a recap, this was all the schematics in which we saw learning being possible. Supervised learning, multimodal learning where multimodal comes in as inputs and for the same task. Multitask learning where there's a single input and multiple outputs. transfer learning where X predicts Y1 and you're adapting it to predict Y2. Right? So now the task may be slightly different but the base input is the same. Crossodal learning refers to the setting where X1 predicts a single task

### [05:41](https://www.youtube.com/watch?v=IDaMEG_zY6A&t=341s) · b000007

and X2 predicts the same task or different input for the same task. Right? That's crossodal learning. And of course you have a unsupervised learning where X predicts some some subp part of X say X prime not the label and subsequently it is adapted to predict the label. So all of these approaches technically fall under you know this first way of doing cross model transfer which is to do transfer learning. Uh nowadays there's a lot of exciting work um in achieving much larger scale transfer. Large scale transfer in the sense that we have models that are trained on extremely diverse multimodal environments and also multitask environments. Right? So you might think of trying to train a generalist model that is able to use language and speech and gestures to predict something about humans that is able to use image and

### [06:37](https://www.youtube.com/watch?v=IDaMEG_zY6A&t=397s) · b000008

text to do some multimedia tasks like doing crossodal retrieval that is able to use force and propriioception. These are robotic sensors that is able to help control a robot and so on. So this generalization across different modalities and tasks can be very helpful especially for settings in which data is very low in resource. It's very difficult to get robotics data in the form of sensors. But perhaps seeing videos on the internet about how a robot is moving can help you train that model. It might be very difficult to get sensor data and tabular data in healthcare. But perhaps seeing tabular data in the form of other spreadsheets and other tables from research papers can help you learn better tabular representations for healthcare. That is a promise for why it's very appealing to train larger scale multimodal and multitask approaches even though the task that you

### [07:32](https://www.youtube.com/watch?v=IDaMEG_zY6A&t=452s) · b000009

care about may only be in one single vertical. So here are some papers, some that we did, some that other people have did as well in trying to scale up some of these multimodel and multitask models. At a high level, one key of achieving transfer is to share parameters, right? If you start sharing parameters, you start sharing your architectures that allows information to flow between different modalities and tasks and therefore achieve transfer. So how can we share parameters? If you look at all of these modalities, right, they may seem very different, but at a first order approximation, they can all be seen as a sequence, right? And that's perhaps the dominant paradigm of many of these frontier models today, which is to treat different modalities as sequences, right? Language, sequence of words, speech, sequence of signals,

### [08:28](https://www.youtube.com/watch?v=IDaMEG_zY6A&t=508s) · b000010

vision, video, a sequence of frames or individual gestures, even some of the sensing data. These are time series, but they can be seen as a sequence of of time points, right? Given that they're all based on sequences, uh it seems obviously very natural to use transformers and other sequence models to try to encode them. So perhaps it's even possible to use the same transformer to encode all of these with the same transformer architecture with the same model parameters to encode language and vision and audio and sensing data and more. the same model, right? That's why I use the the same color to depict it. Of course, it's not that extreme in the sense that you always use the exact same model, but what I've shown here are basically identifiers, right? You probably want to uh and we found this to be very helpful to add an identifier that basically identifies what modality

### [09:25](https://www.youtube.com/watch?v=IDaMEG_zY6A&t=565s) · b000011

it came from. So, you use for example one embedding uh to identify that this is language, right? when looking at human communication and this is also language when looking at different websites. Uh this is uh sensing data you're looking at force and is also sensing data when you're looking at a medical sensor. Right? These can all be the same indicator that indicates the same modality is present in both. Right? So in practice these modality embeddings are basically one hot vectors. Right? where language is 1 0 0 0 vision could be 0 1 0 0 0 audio will be 0 0 1 0 0 so it can be a one hot uh embedding that just indicates what modality it is so with yes&gt;&gt; so um is it just that transformers are now

### [10:19](https://www.youtube.com/watch?v=IDaMEG_zY6A&t=619s) · b000012

this kind of encoding model and we wouldn't or is it also to have I guess unified model architecture that does multimodal encoding.&gt;&gt; Oh yeah, I'll get to multimodal encoding. Um but at least in the unimotal&gt;&gt; same&gt;&gt; yeah on the unimotal side um transformers is one way I one example is one way of potentially having a path towards a generalist AI where the same model can encode everything. Um we did this stuff in 2021 2022 when transformers were the dominant paradigm. Uh now if we were to revisit this you know perhaps you could use something like diffusion models right uh where diffusion models have clearly been able to do better on encoding vision and some of the sensing data. You know language is still kind of in the air whether you

### [11:16](https://www.youtube.com/watch?v=IDaMEG_zY6A&t=676s) · b000013

want to use transformers or diffusion. Uh but you see that diffusion language models are becoming popular. Um but I think there is also still a path towards having one generalized architecture for everything. Here we just decided to use a transform. So you embed each of these modalities and append it with a modality encoding. It tells you what modality it is. Then you apply unimodal transformers over that sequence. Right? And what these will do is that it will just learn these you know pair-wise interactions within that same modality. So you look at how every force sensor reading you know aligns or interacts with other force sensor readings in the same modality and then separately you look at you know language words interact with other words in the context. Okay so these are unimodal transformers. Once you extract those representations you can then apply your multimodal

### [12:12](https://www.youtube.com/watch?v=IDaMEG_zY6A&t=732s) · b000014

transformers. So these are the ones that we saw where instead of just doing self attention within each modality's own sequence, you're doing cross attention between the sequence in one with the sequence of the other. So for example, this cross attention, it will look at how every embedding of your entries within a table interacts with every embedding of each of the time steps in your sensor. That's your pair wise cross attentions. And for things that involve two modalities, you would just do three choose two sets of cross attention between each of the pairs within those three modalities. And again, what's really cool is that you can again define the same model, right? The same model with the same architecture with the same parameters is surprisingly able to encode how speech and gesture should fuse together and at the same time represent how force and

### [13:08](https://www.youtube.com/watch?v=IDaMEG_zY6A&t=788s) · b000015

propioception should be fused together. Right? So it's the same color exact same model. Uh so how does this work? Oh, and of course once you have obtained representations from each of those um those multimodal transformer outputs, you would then have the unimodal representations and the multimodal representations and you would define different classification heads for your task, right? With the tasks could be quite different across domains. So you can think about this as a huge multimodal multitask approach. Uh so over here it's called a high MMT. Um the huge multimodal and multitask approach are the same model the same parameters encoding all pairs of different modalities and making able being able to make predictions on on different tasks. What can be also really cool is um you take this model and you

### [14:05](https://www.youtube.com/watch?v=IDaMEG_zY6A&t=845s) · b000016

transfer it to some other task right to time series and table. So some other task with a new set of modalities and a new prediction task. So now you're getting generalization both in the input and in the output. Right? Obviously if you were to do this completely do it again with a new model you would just have to train from scratch. But if you use this model that you've already trained then this is giving you a good prior for what it would look like to fuse time series and tables for that prediction task. So how does it work? This is showing uh transfer performance right. So if you don't transfer at all, so you use zero source tasks and you just train a model from scratch on these data sets, you get about 68%. If you start training more and more models, sorry, you start training a model with more and more um pre

### [15:00](https://www.youtube.com/watch?v=IDaMEG_zY6A&t=900s) · b000017

pre-training data sets, uh for example, one, two, three, you get monotonically better performance. And then for some of these other tasks as well. So if you don't turn on pre you get 63 and if you monotonically uh train on more and more tasks involving different modalities and prediction tasks you get monotonically better performance. Right? So this is um showing strong results on transfer across different settings can be particularly appealing and we find that uh the performance improvement correlates very well with how little data you have in this target task. Right? The less data you have in this target task, the more this pre-training on different tasks will help and the more data, the less the performance improvement will be. We also show some multitask results in in the paper showing that essentially if

### [15:56](https://www.youtube.com/watch?v=IDaMEG_zY6A&t=956s) · b000018

you have for example all of these tasks right they train separate models on each or you could train some unified multimodal multitask model and oftent times you get either the same performance or usually better performance. So it's able to do this multitask and transfer learning. Yes.&gt;&gt; Can you really say it's better if there's like no description of confidence interval between that's how we do it people 67%&gt;&gt; I don't see a difference.&gt;&gt; Yes. This is a data set where there's more data and this one is a bit more obvious. I think we have some confidence intervals in the paper. So at least there was some there was some

### [16:52](https://www.youtube.com/watch?v=IDaMEG_zY6A&t=1012s) · b000019

statistically significant improvement uh with more transfer and then um we did this in 2022. So now now we have even more data and people have showed that it's kind of large scale multimodal multitask training does work better at large scale as well. Yeah. Um so yeah so another reference that is very interesting is this paper called go. It's called a generalist agent. Uh they did it primarily for for robotics where they showed that you could kind of train these models for classifying images, right? That gives the model visual capabilities and then you can transfer to model to classify um different objects that robot can see. So now it's starting to do towards robotics and show that the same model can also do robotic control. So it has better visual capabilities. They can start taking better actions. So start transferring from various visual tasks to to embodied tasks as well. That's another reference.

### [17:51](https://www.youtube.com/watch?v=IDaMEG_zY6A&t=1071s) · b000020

Of course, this is making a lot of assumptions here. Um we don't yet know whether this is going to be the dominant approach, right? Uh if you look at this, you know, obviously a lot of people are trying to build unified multimodal multitask approaches. Um we just saw the latest model from Meta yesterday. So Meta they they branded or first model that Meta Super Intelligence Labs released they branded it as a as a natively multimodal model right uh which basically means you know you have a set of approaches nowadays at some frontier labs where they train a language model they pre-train it and they staple adapters right onto the language model right the adapter for vision and adapter into LLM an adapter for audio adapter for speech recognition and so on. So that's probably the dominant paradigm done by most Frontier Labs. And then Meta released this and they said it's a

### [18:48](https://www.youtube.com/watch?v=IDaMEG_zY6A&t=1128s) · b000021

natively multimodal model which leads me to believe what they're trying to push is models that are more unified and can directly process all of these modalities to begin with during pre-training uh rather than only pre-training on language and then stapling other modalities on top. But jury is still up in the air. I think the model that meta released didn't show the best results on many things. So jury is still up in the air which which approach is better.&gt;&gt; How many parameters?&gt;&gt; I don't think they really thought

### [19:23](https://www.youtube.com/watch?v=IDaMEG_zY6A&t=1163s) · b000022

&gt;&gt; um I think this these type of approaches also make a nice contrast with the reasoning based approaches we saw in the last two weeks. Right? Reasoning is very much about compositionality, right? modularity. You might try to build things each with different capabilities and then how you can orchestrate them in the right way. Whereas some of these other approaches like this generalist agent, they try to build everything unified into one big model instead of having many modular components.

### [19:57](https://www.youtube.com/watch?v=IDaMEG_zY6A&t=1197s) · b000023

So some what are some assumptions of these models which um I'm not fully satisfied with. So a lot of them assume that you know all these modalities despite being very different they can be viewed as sequences right language is a sequence tabular data is a sequence even some things like protein structures people are doing protein structure language models they also view it as a sequence so serializing everything uh obviously loses a lot of structure in your data and may or may not be the best approach it also assumes that the differences between modalities. They spent a lot of time discussing that heterogeneity is a very key concept uh a key driving principle in multimodal research and they're assuming that all of this heterogeneity can be just encoded by this modality specific embedding right that this is like ones and zeros and this is zero one zeros and

### [20:52](https://www.youtube.com/watch?v=IDaMEG_zY6A&t=1252s) · b000024

zero one zeros and um obviously that indicator function uh probably is not enough to capture all different ways which the data are different and of course this uh this fully shared multimodal model as opposed to more modular compositional approaches is still a big debate. Here are just uh all a bunch of other references right I organized them into this schematic. Uh so perceiver was perhaps one of the first approaches in this space uh by deep mind where they came up with a unified architecture different parameters right but unified architecture that can process all different modalities right edge video audio sensors I'm using that as shorthand notation and uh I'm using kind of squares to indicate that the architecture is the same but different

### [21:49](https://www.youtube.com/watch?v=IDaMEG_zY6A&t=1309s) · b000025

colors to represent the parameters are different right so same architecture shared backbone just fine-tune it differently for different modalities. Still good because now convergence and architecture is something good because now you have just one architecture that people can make much more efficient or people can do the same theoretical analysis. So that's perceiver and then came a generation of methods like multimodel and vit a lot of these v vision language bird approaches they basically work on image and language they have both the same architecture and the same parameters the same model can encode both image and text uh and there were extensions to polyvit where you could have the same model to encode image and vision and audio right and then came uh these are you Think about these are unified encoders for unimodal learning. So it's still about vision tasks and language tasks

### [22:46](https://www.youtube.com/watch?v=IDaMEG_zY6A&t=1366s) · b000026

and audio tasks. It's just how similar architectures and the parameters are is solving different unimodal tasks. Right? So the the Y's are still you know one modality to a Y another modality to a different Y. Maybe another set of approaches which are more multimodal and multitask learning right. So you have for example uh all your vision language birdlike approaches where they take an image and text and they learn a fused representation that can operate across multiple image and text tasks right image text for one task and image text for another task. So with the same architecture, same parameters and I mean the same logic extends for all these other things, right? Uh it's just how broadly they can go in the modalities and tasks that they support, right? So a bunch of all these methods that have been making the inroads in

### [23:42](https://www.youtube.com/watch?v=IDaMEG_zY6A&t=1422s) · b000027

achieving more generalization, multimodal multitask generalization. What are some open challenges I see in this space? Um, a lot of tasks still are very low resource. So most of all this advances have been still been operating in the digital space where people are still working with image and text and audio data. Having this extend to the real world is still a challenge. Beyond language and vision is still a challenge especially to settings where some modalities deep learning and transformers are not the state-of-the-art right so for tabular and time series we're still always jumping between whether deep learning and transformers and foundation models are good or are traditional approaches like traditional tabular and time series approaches are better. uh this naturally adds more complexity

### [24:41](https://www.youtube.com/watch?v=IDaMEG_zY6A&t=1481s) · b000028

in the sense that these are larger models they're require more data and more data hungry but at the same time as I mentioned there's a particular appeal when architectures converge because now the whole community can just focus on making more efficient one architecture and doing theoretical analysis and good optimization of one architecture and we'll discuss more about interpretability maybe later on in the class but obviously these are still huge blackbox approaches

### [25:15](https://www.youtube.com/watch?v=IDaMEG_zY6A&t=1515s) · b000029

Any questions about this multimodal and multipass learning?

### [25:30](https://www.youtube.com/watch?v=IDaMEG_zY6A&t=1530s) · b000030

Okay, so that's one way of achieving transfer, right? How do you design? I think we've covered here. How do you design the same architecture with the same parameters that are shared as much as possible and by definition once you start sharing parameters transfer happens because of the common parameters between one modality and one task and another. So this doesn't involve any additional training objective and so on apart from just doing multitask learning. So a second set of approaches for achieving transfer is what we call co-learning. Co-learning essentially means that you're trying to transfer information from your secondary modalities to your primary modality by adjusting the representation space itself during training. So this is a general setup. A is something that you care about, right? This is the one that you actually care about making

### [26:25](https://www.youtube.com/watch?v=IDaMEG_zY6A&t=1585s) · b000031

predictions in. and B is some extra modality that you have access to during training. It's only available during training. How do you use that to learn a better representation during training? Right? Afterwards, you throw this away and you are left with a better model that you can use for inference during test time. The important thing is that you no longer have access to this after training. you've enriched the representation so that during test time you're still making a fair comparison with baselines that only use this modality.

### [27:02](https://www.youtube.com/watch?v=IDaMEG_zY6A&t=1622s) · b000032

So there's there are going to be three ways of achieving co-learning that are broadly covered. These are multimodal approaches that you've all seen uh fusion, alignment and translation. And we'll start by seeing how fusion can enable code learning. So here is how you can use fusion to do code learning. So you first start during training by training a fusion model with both modalities A and D. Right? So the multimodel data during training and you're training a fusion model to predict your label Y. This can be any any fusion model we've seen, right? Uh additive, multiplicative, early, late fusion, whatever. Right? That's during training. Now during testing I'm going to use the same fusion model but I'm going to input zeros for modality B right so input zeros or input the average or the median

### [27:59](https://www.youtube.com/watch?v=IDaMEG_zY6A&t=1679s) · b000033

or anything where you know you don't actually have modality at testing so replace it with some constant or or dynamic value like the average or something okay so now you see that during testing this is a model that only operates on modality TA but this is a model that you know was trained using multimodal fusion with both A and B during training. So this is a multimodal co-learning setting. If you look at the contrast with um unimodal learning, you look at a contrast with unimodal learning, you have modality A prediction Y during training and then modality A same modality uh making inference on the model during testing. Okay, so that's a training and testing setup. Now, in testing, both of these are fair comparison, right? In testing, they're only just taking a modality A and making a prediction. They're fair comparison.

### [28:55](https://www.youtube.com/watch?v=IDaMEG_zY6A&t=1735s) · b000034

The question then becomes, if I know I want to just predict on modality A, should I train a unimodal model on A or should I bother training a multimodal model with A and B during training and replace me with zeros. So only text is used at test time and there's a lot of findings that show that multimodal code learning can outperform language only training with fair comparison during testing. Having that additional modality be during training and training a fusion model instead of a language model can actually lead to better performance when evaluated.

### [29:40](https://www.youtube.com/watch?v=IDaMEG_zY6A&t=1780s) · b000035

Yes,&gt;&gt; I guess my mind immediately goes like covering distributions perhaps having another modality exposes you to distribution both. What do you think is thing that drives this enrichment? Yeah, I think there's both um information and regularization effects, right? I think all cases, one is about does it provide more information into the parameters during training and the other one is that is the model being regularized better so that it's not about adding more information but it's about you know shaping among the information that you have shaping the model predictor that is the best at using that information. So enrichment argument is that for example right now if you're kind of listening to me speak you're seeing you know seeing my lips and you're hearing my voice and then

### [30:36](https://www.youtube.com/watch?v=IDaMEG_zY6A&t=1836s) · b000036

obviously if you close your eyes you can kind of imagine what I'm looking like and what I'm expressions might look like right or if you uh close your ears and you just see me you can also kind of make up what I am um might be saying just by looking at my lips move right so there is more information probably being provided and there's some mechanism in these models when they're doing fusion they kind of you know cross predicting one modality from the other and therefore even though at testing I don't give you B you can probably use A to hallucinate B and that gives you extra signal um there are probably also regularization effects um when I say regularization you want want to think about it as you know most of machine learning you have data X and Y and there's going be many different functions, many different hypotheses that fit your data that can make predictions Y from X, right? But among

### [31:32](https://www.youtube.com/watch?v=IDaMEG_zY6A&t=1892s) · b000037

all of these possible hypotheses, some are better than others, right? Some generalize better, some can be trained better and overwhelming argument is that hypotheses that are more simple, right, are preferred, right? Complex hypothesis tend to overfitit to your data and usually simple ones that are not overly simple. So you get high training error, but good simple ones tend to generalize better. And sometimes giving different views of your data allow you to kind of you know break this tie among particularly complex hypothesis for A may not fit something for B. And if you have the model fit both, you'll end up choosing a one that is simpler and more consistent with the world and therefore both. But I don't have a rigorous theoretical argument for all this. I think a lot of these are empirical findings. Would be great if we had more theory for this. I mean for multimodal AI in general or frontier AI in general.

### [32:28](https://www.youtube.com/watch?v=IDaMEG_zY6A&t=1948s) · b000038

I saw yes never trade on zeros. So it's completely out of so I mean you can build it always instead.&gt;&gt; Yeah.&gt;&gt; What's the standard?&gt;&gt; Yeah. Um, I've seen fill with zeros. I've seen fill with the average value. I've seen fill with noise. Um, well, I've not seen fil with noise that much actually. I've seen a lot of fil with zeros in the average value.&gt;&gt; Uh,&gt;&gt; you don't have a relationship?&gt;&gt; Not not in a lot of these papers that I that we've we've seen. Um,&gt;&gt; I'm thinking if you like pretty bad, you should train on both without data and with&gt;&gt; Yeah. Yeah. Yeah. There's a whole community on dealing with noisy and missing modalities, right? Which come from this from a different angle, right? In their case, it is by necessity that B will be not visible during testing. So

### [33:25](https://www.youtube.com/watch?v=IDaMEG_zY6A&t=2005s) · b000039

they can expose the model to all forms of perturbations on noisy B and missing B and um and achieve something better, right? Uh so they come at it noisy missing modality community kind of come at it from a different angle and I'm sure they also have really good results. Yeah, here it's just various people have made the finding that no even if you just don't put anything it's better this multimodal model is better than just single modality model. Yes,&gt;&gt; seems paradoxical because on one hand B is but on the other when you're testing it B doesn't have much influence in the outcome.

### [34:08](https://www.youtube.com/watch?v=IDaMEG_zY6A&t=2048s) · b000040

We're not saying B doesn't have much influence on the outcome, right? Because we're comparing this setting where only A is given at testing, right? and filling E with zeros versus a setting where only A is given and a model was always unimodal to begin with. Right? So, we're only comparing these two. We're not really comparing A B like to to answer your question, you'll be comparing A with missing B versus A with B present, right? That would ablate the effect of B, right? So, let's say you have um A and B together during testing. That would be the best 90%. Okay. And then I zero out B, that might be 60%. Right? So now I know B's contribution is about 30%. Right? And then I compare with a model that was just always unit model A. I'm saying that's 50 50%. Right? So it's 60% versus 50%, 10% was the contribution of

### [35:05](https://www.youtube.com/watch?v=IDaMEG_zY6A&t=2105s) · b000041

having additional B during training, right? And if you also have B during testing, which is obviously the ideal setting, D, you get 90%, right? So here is um perhaps some 2014 did this paper multimodal learning with deep machines um kind of just showed this as an afterthought right so in this setting this was before deep learning kind of kind of became really popular and people were still working on bolster machine RBMs I don't know people know what that is uh but these are joint probabilistic models right so you learn a joint distribution over uh in this case image and text. Okay. So you had image only models and you had all of these uh these uh these image only models and you had this multimodal model and for this multimodal model you see here over here generated text right so it didn't

### [36:01](https://www.youtube.com/watch?v=IDaMEG_zY6A&t=2161s) · b000042

actually have text during testing because there' be unfair comparison with all these other models that only have access to the image. So this model they handicapped it by removing the text right only having the image removing the text and having it kind of self-generate the text right and it was able to outperform with a good margin uh methods that were just unimodal to begin.

### [36:32](https://www.youtube.com/watch?v=IDaMEG_zY6A&t=2192s) · b000043

Uh here's another method um also a very seminal paper multimodal deep learning from again way back 2011. uh they showed this for uh perhaps one of the first examples that that I gave for multimodal this mgherk effect right so where people were were verbalizing different sounds so you see their lips moving and you hear the different audio and some of it was ambiguous right like ba and ga they sound exactly the same but you have to look at the lips right so they also had a similar setting where they train with audio and video right to get some shared representations and Then during testing uh they remove one or remove the other right and the goal is that even by masking one out or the other uh does it get better representations than with just unimodal your data right without the multimodal training.

### [37:31](https://www.youtube.com/watch?v=IDaMEG_zY6A&t=2251s) · b000044

&gt;&gt; All right. Any more questions about co-learning via fusion?&gt;&gt; Yes. I I know you don't like questions like these asking, but um so let's say uh you grew up blind. Okay.&gt;&gt; Okay.&gt;&gt; And my guess or my my task is to guess your or I grew up blind. My guess is to uh guess your mental state and Tom has all his senses. Say they all work perfectly well. Should we expect that if I take away one of Tom's senses, let's say take away his sight, that he's more likely to pick up on your mental state because he has a superation.

### [38:17](https://www.youtube.com/watch?v=IDaMEG_zY6A&t=2297s) · b000045

&gt;&gt; Maybe why do you say I don't have these questions? because in the past I think you like I've asked like cognitive related questions and you were like ah&gt;&gt; I I think I I uh I don't think cognitive um cognitive insights are useful for training frontier AI models right I think these questions are very interesting um I think if you talk about human I think another big aspect is this idea of plasticity right if you grew up blind your brain And there's evidence to show that, you know, from neuroscience that your brain probably would have rewired itself to heighten your other senses to make up for your lack of vision, right? And therefore, your maybe smell is or sense of touch or hearing is better. None of which are useful for detecting my emotion though. Um, so I'm not sure. I think in this case, I think it's going

### [39:15](https://www.youtube.com/watch?v=IDaMEG_zY6A&t=2355s) · b000046

to be I mean, it's not even a fair comparison. How if you're blind, grew up blind, how would you detect my emotion? What was the control procedure to detect my emotion that both you and&gt;&gt; I'm humanal in that case? Like all I have is hearing or he's both.&gt;&gt; Oh, so I'm speaking.&gt;&gt; Yeah. Yeah. You're&gt;&gt; okay.&gt;&gt; I'm trying to guess like what what's the quality of your mental state from your utterances?&gt;&gt; I see.&gt;&gt; Yeah.&gt;&gt; You should do such a study.&gt;&gt; Do such a study. I think people probably would have already, right? Um I mean this whole plasticity argument you know blind people who have grew up blind I think sharper hearing or sharper smelling and touching I think has been experimentally proven. Not sure whether it's been done for emotion. I mean that could be another hypothesis for for some of this right which is this plasticity argument that you know handicapping a model by dropping out B um

### [40:12](https://www.youtube.com/watch?v=IDaMEG_zY6A&t=2412s) · b000047

handicapping a model by dropping out B has you know forces the model to kind of recreate B right so it be interesting question to see right now I'm just training with both A and B and I'm just handicapping at a testing what if there was a curriculum as Ako mentioned right uh if you kind So exposed the model to to missing the maybe 80% of the time and the 90% of the time and 100% of the time and then maybe that would influence what the performance is right&gt;&gt; isn't sufficient right you still get bias from mod that wouldn't get it at all like if you're flying from the start&gt;&gt; yeah so I think this is like blind from the start right this is kind of like maybe Well, not really because I mean Yeah.&gt;&gt; I think what&gt;&gt; Yeah. Yeah. And the brain has access to to vision. So I don't even think this is blind to the star. Something like like

### [41:08](https://www.youtube.com/watch?v=IDaMEG_zY6A&t=2468s) · b000048

that. Yeah. Okay. Um so I think that's that's a really good segue to the second way of doing co-learning. So if you see this first way, right? Um it's cold learning via fusion. you're only ever having one objective which is to just make prediction on the label. Right? As you see for these other two ways of doing co-learning, you can add more objectives, right? To explicitly align or translate your data to encourage this kind of plasticity or this kind of hallucination of other modalities in addition to just your task. So the second approach is called co-learning via alignment. Right? Same setting. you have a that you care about and it's not very good. So you introduce B during training and co-learning happens right but to get a better representation but instead of just relying on fusion with respect to the

### [42:04](https://www.youtube.com/watch?v=IDaMEG_zY6A&t=2524s) · b000049

task now you can add alignment objectives between A and B so that the resulting representation is better right then if folks uh remember alignment are these approaches where instead of fusing it into one embedding you keep A and B as separate embeddings and you have this similarity function between them. So you bring for example positive pairs where A and B are have similar meaning closer together and you push negative pairs where A and B are of different meaning further apart.

### [42:36](https://www.youtube.com/watch?v=IDaMEG_zY6A&t=2556s) · b000050

So there are a lot of examples of this right I think this is probably one of the earliest ones I could find where you're trying to learn this paper is called zeroot learning through crossodal transfer. So already kind of ticks a lot of these boxes, right? Cross motor transfer and is able to use this transfer to do very quick generalization zero shot to a new new task. So the setting is that you have a bunch of images and these were still rather simplistic bar 10 images and you had a bunch of uh uh categories for these images, right? Categories were just a word for example auto, horse and doll, right? And alignment essentially allows you to learn this joint representation space where um your cluster of image embeddings for your image images of dogs are all very close to the uh the word

### [43:32](https://www.youtube.com/watch?v=IDaMEG_zY6A&t=2612s) · b000051

embedding for the word dog. Likewise, your cluster of image embeddings for horse are very close to the word embedding for horse. Likewise for auto and so on. Right? This is the kind of representation space that you will get during uh representation alignment. Right? So we've seen this in clip and all these contrastive learning stuff. Now this paper is able to show that now if you take a new image from an unknown class, right? So you've never seen an image before, right? The image of a cat. First you would embed it into this representation space. If your visual encoders are trained well then it will be embedded nearby the image embeddings for dot right because visually similar images will get embedded into similar similar embedding spaces right and more importantly because your presentation space also contains word embeddings and the word embeddings are shaped well you would have the word embedding for cat

### [44:28](https://www.youtube.com/watch?v=IDaMEG_zY6A&t=2668s) · b000052

very close to the word embedding for dog right so visually the visual embeddings go to where the right position is where all the visual embeddings And then a word embedding for cat also goes into the right position relative to other word embeddings. Which basically means if you just do nearest neighbor of the image embedding with the words, you will be able to predict that this is a cat using zeroot, right? Without ever training a model to predict cat for this image, right? So that's uh what they mean by zero shot transfer. And again the key idea is that if you have this embedding space where the images and their embeddings and the text and embeddings are all aligned then you can leverage the structure right so that you could do very quick inference for new images.

### [45:18](https://www.youtube.com/watch?v=IDaMEG_zY6A&t=2718s) · b000053

Uh again recall this falls under the co-learning because only images are used at test time right the model only ever just takes in this image and makes a prediction is not using image and text or using any additional information so it's fair comparison and in this case it was able to perform zeroot image classification.

### [45:44](https://www.youtube.com/watch?v=IDaMEG_zY6A&t=2744s) · b000054

Any questions about this?

### [45:51](https://www.youtube.com/watch?v=IDaMEG_zY6A&t=2751s) · b000055

So this kind of training objective can be also used to enable enable crossodal transfer. Um okay possibly related to some of these these plasticity or prediction arguments that we were talking about. Nowadays this is very common right nowadays has really been scaled up. So when clip was done you know image text alignment obviously people showed that you know given a new image you could also classify into other categories right but at the same time the image embedding of clip could be used for other image tasks right not just to score similarities with text but it was also generally useful for other object detection or segmentation tasks and likewise the text embeddings for a clip were also separately useful for other text classification tasks. So also all evidence of of co-learning.

### [46:54](https://www.youtube.com/watch?v=IDaMEG_zY6A&t=2814s) · b000056

Uh now people have also done this for other settings. So robotics vision and touch prediction is very common right? If you have a what the robot sees and what the robot feels, then ideally you want to train this model such that you when I deploy the robot, it can still operate without the sense of touch, right? Maybe when the touch sensors are off and it can still operate without the vision, for example, when the camera is being occluded, right? So you want to maybe train with more modalities and have it deploy the inference when a bunch of modalities are missing and only one of them is present. So a lot of these methods for example they use crossmodal prediction where they predict vision from touch or touch from vision. So they end up with this good align embedding space. So no matter which one you use right one or the other it still makes a good prediction.

### [47:50](https://www.youtube.com/watch?v=IDaMEG_zY6A&t=2870s) · b000057

Yeah. So here's some examples of uh doing vision touch alignment for robotics.

### [48:03](https://www.youtube.com/watch?v=IDaMEG_zY6A&t=2883s) · b000058

Okay, last way of doing co-learning which is very similar to alignment is this idea of translation. So fusion and alignment we saw this extra modality B that was supplementing it at the input level. Uh in this translation space you have this other modality B that is being a prediction target right it's supplementing it at the output level. So during training you would have a you learn some embedding you would use that to predict B while at the same time predicting your label you're doing this multitask prediction and then you once you've done you're just using this pathway you're just using A right so B is only provided as a training signal and then subsequently uh removed and not used during testing.

### [48:58](https://www.youtube.com/watch?v=IDaMEG_zY6A&t=2938s) · b000059

uh a little evidence for this. So we we did um one work back then when we're looking at human spoken language. So we uh did exactly the example we discussed where you know a person was saying something and instead of learning these representations so it will always require you to look at the person's what they say and their voice we learn these kind of crossmodal predictive representations. So you took the language that a person was saying, you learn a representation that was able to imagine what their facial expressions were like, right? In this case, you probably imagine that the person was smiling and at the same time use that representations to predict the sentiment, right? Positive or negative. So this is an example of crossmodel translation because you know your your other modality is used as a prediction target and when you're doing inference on a model that you've trained it will just be language coming in going to the representation and making a prediction.

### [49:56](https://www.youtube.com/watch?v=IDaMEG_zY6A&t=2996s) · b000060

So you would not need vision at test time. Uh one thing we found that in some of these translation approaches sometimes a model can tend to ignore the prediction of the other modality. Right? If it's just easy to detect the sentiment was positive and this objective was really hard, the model just wouldn't do it. So another signal you can give to the model is not just forward translation but also backward translation. So you would have the model taking in language, predict the embedding, imagine what the person's facial expressions are using what the model predicted as the facial expressions, predict back the embedding and predict what the language would be given those facial expressions, right? And you want the this whole cycle of language to predicted vision back to the language to be consistent with the original snippet of text.

### [50:52](https://www.youtube.com/watch?v=IDaMEG_zY6A&t=3052s) · b000061

So we call it cyclic translations from visual back to language. Uh but all this is just to learn better representations so that you know again during testing you can do this co-learning where you use the representation and you don't use vision to predict the label.

### [51:18](https://www.youtube.com/watch?v=IDaMEG_zY6A&t=3078s) · b000062

Great. Uh several other examples. This is quite useful for compositionality uh and reasoning. So in some of these visual reasoning problems um it is very helpful for the model to kind of explicitly verbalize right all these very complex relationships like for example explicitly verbalizing that this is a red cross that is below a square instead of just processing the image. So sometimes it helps to translate the image to the text. Uh people have done this for pre-training as well. So BERT was taking text masking things out and predicting what the missing tokens were. Uh series of approaches that use visual supervision to pre-train language models, right? So you can try to imagine what humans look like, what uh speaking

### [52:14](https://www.youtube.com/watch?v=IDaMEG_zY6A&t=3134s) · b000063

and listening look like. basically imagining what things look like um as a crossmodal prediction training objective instead of just predicting text. Some data sets that people use for this include these visual storytelling data sets where you have paired images and nice descriptions also large scale video data sets where you have no visual scenes happening while people are speaking. So you have this paired data. So now this crossodal training is done. uh you are just using the the subsequently trained language model and you know text classification during testing.

### [52:56](https://www.youtube.com/watch?v=IDaMEG_zY6A&t=3176s) · b000064

One final example where co-learning can be very helpful is when your original prediction task has very low resolution. Right? So here's a example of some work in the more medical space uh over here trying to use breathing signals to predict whether a person has some disease right uh in fact people can show that just from how people are breathing when they're sleeping predict whether they are showing signs of Parkinson's disease or Alzheimer's disease amazing stuff so over here you have um breathing signals you have a breathing encoder PD is Parkinson's disease and you are training a classifier for whether the likelihood of somebody has some disease and also the severity of that disease. Right? This seems like a very classic supervised learning problem. But obviously this is really hard to train because you have hours, tens of

### [53:52](https://www.youtube.com/watch?v=IDaMEG_zY6A&t=3232s) · b000065

hours of people sleeping, right? People sleep 8 to 10 hours a day. You have a lot of hours and you only have like a single bit supervision of whether they have Parkinson's. Right. Right. one for some people, zero for most people. So that is a very very uh discrepant ratio between how much data you have and a very little signal that you have. So it can be helpful to add another modality as a prediction objective. Ideally another modality with the same information resolution as the input. Right? So there is no longer this discrepancy and you actually have a rich training signal to lend better representations. So over here you can for example try to predict the EEG the brain waves right because brain waves that a person is um is showing when they're sleeping is at a similar information density to their you know other breathing signals. So now this

### [54:49](https://www.youtube.com/watch?v=IDaMEG_zY6A&t=3289s) · b000066

signal is very high information very high density forces the model to learn better representations which can be useful for predicting your Parkinson's disease that you actually care about. So here's what it is. That was the audio of people breathing. Lots of data, high resolution. You predict EG activity throughout the night as an extra signal, right? About similar resolution, same time frame, same sampling rate. Uh that gives you good features. Um but even though you don't really care about whether you're predicting EEG correctly, the features themselves are now more useful for your disease prediction. So cross model prediction can be useful to also deal with um data that comes in at very different resolutions and to get more training signal for your models.

### [55:49](https://www.youtube.com/watch?v=IDaMEG_zY6A&t=3349s) · b000067

Any final questions?&gt;&gt; Yes.&gt;&gt; Why did they choose the modality not the reasoning behind it. Like that seems kind of like a shot in the dark, but like&gt;&gt; Yeah.&gt;&gt; Yeah.&gt;&gt; Yeah. Yeah.&gt;&gt; Um people have I'm sure it was a mix of some doctors and some reported medical literature showing that this was possible plus I mean obviously you get access to data. So you know through collaborators um probably these folks um found a right partnership with the right collaborator who was able to both you know give theoretical backing that this was possible and would give access to data sets where this is possible but I think um this is what 2022 so probably was done in 2020 because journal takes a long time and recently people have shown that like recording

### [56:44](https://www.youtube.com/watch?v=IDaMEG_zY6A&t=3404s) · b000068

your sleep can indicator of so many things so many types of um uh know cognitive you know related diseases breathing, heart rate, lung related diseases. Yeah, cool stuff. Okay, great.

### [57:11](https://www.youtube.com/watch?v=IDaMEG_zY6A&t=3431s) · b000069

All right. In the last uh last 15 minutes, I'll cover this third part. So very exciting. So first uh as a recap you know we've seen transfer right. So you have you know really big based models that you can then start you know fine-tuning or doing multitask learning transfer to other settings that you care about. Um this is really good when you have good pre-trained models and you don't mind you know keeping to fine-tune or adding prediction heads to your model. And then we saw co-learning which actually had to dive the deepest right you actually had to open up the representation layer to add for example a fusion signal or an alignment objective or a prediction objective. So you actually had to dig deep and open up the box of the model. And then nowadays uh there's a lot of work at the model wrapper level uh which you can think about as inducing behaviors um without actually opening up and modifying the model itself right um

### [58:08](https://www.youtube.com/watch?v=IDaMEG_zY6A&t=3488s) · b000070

especially nowadays you know people want to do all sorts of things at the API or wrapper or or harness level so we call this model induction but uh in fact a lot of this stuff you know is done way back in the day so I'll show you one example of a model induction approach where you and have the model improve and share information with other models and get better over time. Um so the high level definition is that you keep individual unimodal models separate but you're trying to induce some common behavior across them. Okay. So this paper is called uh selfraining. Self training is a warm-up which algorithm that I'll show you which achieves model induction within a single modality and then we'll extend it to co-raining which is basically self training across uh two modalities. Self training approach probably been a long for a very long time and this p

### [59:04](https://www.youtube.com/watch?v=IDaMEG_zY6A&t=3544s) · b000071

this paper which actually made it more applicable to deep learning and was quite rigorous in its analysis but this stuff existed for a long time. So how can transfer happen? So we're going to start with um some data, some label data, right? X and Y label data. And we're going to have assumed that we're going to assume that we have a bunch of unlabelled data, right? What selftraining does is that it first trains a classifier on the label data that we have, right? probably an imperfect classifier because often times you have very little limited data to begin with. You're going to use the classifier to label some unlabelled data in your pool of unlabelled data, right? You're going to label it and specifically you're going to label the ones that are the model is the most confident on, right? So as you're labeling, you know, usually some soft

### [1:00:00](https://www.youtube.com/watch?v=IDaMEG_zY6A&t=3600s) · b000072

max. You can look at softmax or confidence to see if it's you know uniform softmax probably not going to be a good label that it generates very confident softmax I'm going to use that to to label the data right and this allows you to kind of self-label some of these unlabelled data points that you have and essentially you can add it to your training set thereby enlarging your training data set. Okay. And then you would go back to step one which is to now train and update this classifier that you have on this slightly enlarged training set consisting of the original label samples which you know are 100% labels good labels and also this expanded set of labels you have made yourself using your model. So you then retrain your classifier on this larger training set. Go back and label more of these unlabelled samples that you have left. uh choose the most confident ones and use this to keep iteratively enlarging your training set, training

### [1:00:56](https://www.youtube.com/watch?v=IDaMEG_zY6A&t=3656s) · b000073

your model, labeling more and and so on. And uh and during testing you would just you know use the classifier. So this self training this algorithm has been along around for a long time. Of course nowadays we see this a lot in in your data augmentation right for example you're using a model to generate model to generate more data that you're adding to your training set. We see this a lot in your LLMs. We're using LLMs to filter out or generate better examples that you're then adding to the training. But even in classification space, right, this has um been around for a while, right? You can think about what it looks like visually where you have uh originally your label samples, two colors, and you have your classifier. You might uh have some unlabelled samples. That's what they look like. And you can see that some of them are wrongly labeled, right? And that by the

### [1:01:52](https://www.youtube.com/watch?v=IDaMEG_zY6A&t=3712s) · b000074

current classifier and your model with pseudo label the ones that are most confident, right? And in this case visually, you want to think about the ones that is most confident as being the furthest away from decision boundary, right? You're super confident those should be red and you're super confident those two should be blue. And then those two in the middle, you're not very confident, right? So you don't want to label the ones that you're not confident. definitely label the ones that you are super confident. So those slightly shaded red and blue become labeled by your model and add it to your data set. You retrain it, right? Because there's a bunch of blue points over there. You retrain it and now your decision boundary moves a little bit, right? Moves uh rotates a little bit towards this side, right? Then once it starts rotating towards this side, you can see just as an example, it used to get that red triangle incorrect. But now it gets both these red and blue

### [1:02:42](https://www.youtube.com/watch?v=IDaMEG_zY6A&t=3762s) · b000075

triangles correct because of this uh sequence of pseudo labeling. So now that is correctly labeled. Okay. So several key ideas here, right? It's about the model. Not really changing a model itself. you're just using a model as the API to label more data points based on confidence and these can then be added to improve the training of different models. Right? This idea that you're labeling only the most confident ones and gradually shifting the model boundary is important over time because if you just labeled everything and give it to your model, it will be the same performance as the original model.

### [1:03:31](https://www.youtube.com/watch?v=IDaMEG_zY6A&t=3811s) · b000076

So um code training is another very famous perhaps the most famous multimodal algorithm from a paper from 1998 right um and it's a very theoretically grounded method that allows you to essentially improve two classifiers on two modalities over time right it's an extension of selftraining to two views so you have x1 x2 you're going to have two classifiers and again you have some label multimodal data and a lot of unlabelled data, right? Uh there are several key assumptions where redundancy is very important, right? As you'll see, uh redundancy where both views have similar information is going to be very important. And so what the coderaining algorithm does is that you would train classifiers f\_sub\_1 and f\_sub\_2. F\_sub\_1 on the first modality

### [1:04:26](https://www.youtube.com/watch?v=IDaMEG_zY6A&t=3866s) · b000077

is labeled data and F\_sub\_2 on the second modality's label data and you will essentially use F1 and F\_sub\_2 to self label data from the other modality. So your classifier F\_sub\_1 will be used to label the most confident samples and assign that label to train F\_sub\_2, right, the other classifier. And then you're going to use your classifier f\_sub\_2 to label the examples where it is most confident on and use that label to then subsequently train F1. Right? So you have this cross trainining going on. Right? The first modality classifier labels something that second modalities classifier is trained on. Second modalities classifier labels something that the first classifier is trained on. Right? So now you have this exchange of information between the two modalities and you

### [1:05:22](https://www.youtube.com/watch?v=IDaMEG_zY6A&t=3922s) · b000078

repeat until you have no more samples left. And this has provable guarantees to um essentially get better and better F1 and F2 classifiers over time.

### [1:05:40](https://www.youtube.com/watch?v=IDaMEG_zY6A&t=3940s) · b000079

Right? Any questions about code training?

### [1:05:51](https://www.youtube.com/watch?v=IDaMEG_zY6A&t=3951s) · b000080

Modern instantiations are numerous, right? Uh in video people use classifiers for RGB to label data for a video classifier to train on uh sorry optical flow classifier to train on and then they use optical flow classifier to train the RGB model. So it's kind of co-raining can lead to really good performance. Here's an example. Another example of co-raining between different language models, right? You have a GBT3 model that label some examples that BERT can be fine- tuned on and BERT allows you to get some embeddings for confidence samples that you know the large language model can be further fine-tuned on. So various forms of information exchange between different language models. Nowadays a lot of these multi- aent LLMs debates are also seen as co-raining right one

### [1:06:48](https://www.youtube.com/watch?v=IDaMEG_zY6A&t=4008s) · b000081

language model you know labels some some data and gives it to another language model to then make an inference on and they label some data and the other language model makes inference on. So all these are examples of of code training where you have different APIs keeping them the same not really updating the model but having exchange of information between them.

### [1:07:18](https://www.youtube.com/watch?v=IDaMEG_zY6A&t=4038s) · b000082

All right. Uh so to summarize lots of ways in which you know you're not just limited to supervised training or or fine-tuning reasoning for a particular modality or task that you care about, right? Lots of ways of looking at transfer, right? You starting from one model and you're expanding what is transferred to by making it more multimodal and multitask in during transfer. uh this usually requires some amount of fine-tuning and adding classification heads and adding you know new inputs.co-learning which is this new setting where you have a classification that you care about and you're adding and modifying the training process so that another modality is reduced either through fusion or alignment or through you know cross model prediction during training and finally induction based approaches where each of these approaches start as APIs and and the

### [1:08:15](https://www.youtube.com/watch?v=IDaMEG_zY6A&t=4095s) · b000083

models are kept the same they're making predictions but it's how the predictions are being exchanged and the prediction level to to improvement over time. \[clears throat\] All right, that's all folks. Um, any final questions about co-learning? If not, um, see you next week.
