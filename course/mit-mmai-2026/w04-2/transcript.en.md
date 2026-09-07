# Lecture 5 – Multimodal Alignment (MIT How to AI Almost Anything/Multimodal AI, Spring 2026)

_English transcript_

- Channel: Paul Liang
- Source: [YouTube](https://www.youtube.com/watch?v=u-H43tRgYJg)
- Duration: 1:23:04
- Caption source: automatic
- Status: complete
- Chinese translation: 103/103
- Translation provider: codex
- Generated: 2026-09-07T07:53:12+00:00

## Transcript

### [00:00](https://www.youtube.com/watch?v=u-H43tRgYJg&t=0s) · b000001

Welcome back. Let's get started. So, several announcements uh before we begin. So, thank you all for submitting your project proposals. Uh we are taking all the project proposals. We're making a spreadsheet and we'll assign several mentors for every project. Uh either myself or the TAs and the hope is that uh we can meet with you all at least once a week to track progress on the projects. Uh so those project mentors will be announced to all the teams uh this week. Uh hopefully you can meet with us every week to help you all in fact progress. Uh just also for planning purposes as I mentioned we have some credits. Um you can try to use some of these KI models. They claim to be quite state-of-the-art multimodal models. So we have 40 teams about $50 of credits for for Kimi and then 40 teams with $40 of credits for anything else that you

### [00:56](https://www.youtube.com/watch?v=u-H43tRgYJg&t=56s) · b000002

need for the course including compute GPUs or other API calls. Okay? And make sure to keep working through homework 2. Uh that'll be due next Wednesday. Um and then we'll have homework three out after that. All right. Any questions about these announcements? Yes,&gt;&gt; the credits are uh delegated only for the projects, right? Or is it should it be approximately?&gt;&gt; Uh you can you can use them if you want to use for the homeworks, but I think this will be the the maximum that we can give the credits. All right. So, let me just quickly recap a little bit of multimodal fusion. Um I think it went fairly quickly on Tuesday. Let me just recap in a couple of slides before I move on to this next topic that we'll be talking about which is on alignment. But as you recall, fusion is all about taking in different data

### [01:52](https://www.youtube.com/watch?v=u-H43tRgYJg&t=112s) · b000003

modalities and learning some joint representation. And ideally, this joint representation summarizes the ways that these different data modalities interact with each other. And we saw a spectrum where first you can take it for example really good encoders for your modality for passing it through a vision encoder for images passing it through a text encoder for your text to get features right these features summarize some semantic content so they're already quite homogeneous then the fusion can do less heavy lifting the fusion can be more lightweight we learn disjoint representation we call that fusion with abstract modalities at the same time another paradigm is to directly do fusion with raw modalities where instead of defining encoders for each you start with your raw data for your modalities which are more heterogeneous and both representation learning and fusion between the modalities are done together. So now the fusion does more heavy lifting. Uh these are can also be

### [02:50](https://www.youtube.com/watch?v=u-H43tRgYJg&t=170s) · b000004

called kind of more late fusion where you first extract features and fusion is done later in the model or early fusion in which fusion happens early on in the model more close to the data and there's more space for how the fusion operates. Uh several pros and cons for each. Late fusion typically means the fusion is more lightweight can be more interpretable uh but it cannot be that expressive. Early fusion gives the opportunity for the fusion to be more expressive, but usually the fusion is larger and more complex and less understandable. And then as a quick recap, we also saw several basic concepts for fusing different representations. Uh we saw the basic concept where focusing simply on the univariat case we saw uh linear fusion and linear fusion typically involves a constant with some error term additive terms which are just weighted functions of modality one plus weighted

### [03:47](https://www.youtube.com/watch?v=u-H43tRgYJg&t=227s) · b000005

functions of modality 2. That's a simple way of doing fusion and it's at the same time still very powerful because you have different weights that are assigned to different modalities. Multiplicative fusion further generalizes this where now you start considering multiplicative interactions between A and B. Right? And we saw the example where this can be seen as the weight for B is W3 \* X A. So the weight which modality B takes in the fusion actually depends on X A and vice versa the weight of X A is W3 \* X of B. The weight for A depends on B. So now you get these nonlinear relationships in multiplicative fusion and usually it's a good guideline to have both lower order terms so just additive functions uh and multiplicative terms. So these are the higher order interactions between your modalities. We saw the case when you go to higher dimensions uh this can become more

### [04:43](https://www.youtube.com/watch?v=u-H43tRgYJg&t=283s) · b000006

expressive but also more complex. So you saw this trick of adding a one behind your modalities doing this outer product which is basically your your vector transpose times a vector. So 5x 1 \* 1x 5 gives you this 5x5 matrix of which 4x4 are your pair-wise uh biodal interactions. You have two 4x1's which are your two unimodal interactions and you have the one by one which is the bias. Right? So adding this one uh as a constant to your vector and then doing this outer product is a trick to get both a higher order and lower order interactions in your data. And in the three modality case, we have this uh quite beautiful tensor that you can build where there's a cube of these 4x4x4 trrimodal interactions and you have your faces which are 4x4 pair-wise

### [05:38](https://www.youtube.com/watch?v=u-H43tRgYJg&t=338s) · b000007

biodal between AB, AC, and BC. You have your three unit modal vectors and you have the the one uh vector hidden at the back. Right? So this is great but sometimes this can also get very large and very expensive. So these are you know five dimensional vectors this becomes 5x 5x 51 125 right. So this tensor itself can be large and the more multiplicative interactions you do among your data the obviously the more dimension uh the higher the dimension the resulting factor would be and that's where we saw this idea of essentially doing low rank fusion. This idea that you want to do these multiplicative interactions and form these higher order tensors but you don't have to keep all the dimensions. You can do low rank approximations. uh so you can approximately represent

### [06:33](https://www.youtube.com/watch?v=u-H43tRgYJg&t=393s) · b000008

these higher order interactions but still stay quite efficient and we saw this animation where let's say you have two modalities you are doing this outer product with the one that's your Z representation and not only is Z big the other big bottleneck is the weight matrix W on top of Z that brings it to the next dimension H right so if Z is 5 by 5 that's 25 If this H is three, then this W is 5 by 5 by 3, right? So even larger. And we saw how we could use low rank approximations instead of learning this entire W, rather view W as a summation of these little vectors that have taken out of product with each other. So each of these will be 5 by3 outer product with 5 by3 that gives you 5 by 5 by 3, right?

### [07:29](https://www.youtube.com/watch?v=u-H43tRgYJg&t=449s) · b000009

And how many of these little vectors that you add up essentially is the rank of that tensor. Right? Two of them means you're only considering these these tensors or rank two. Three of them is you're considering only tensors or rank three. Uh and essentially in most of machine learning even though your your matrices are very high in dimension in practice when you optimize these matrices and these parameters they end up with pretty low rank solutions. So that's a easy way of reducing the dimensionality and becoming more efficient while still maintaining good amount of precision and that's what we can get with low rank fusion where you can essentially use these lower rank factors multiply them with your data. You can read these papers to show that uh this computation is equivalent. So you get all the benefits of these higher order interactions while only approximating

### [08:23](https://www.youtube.com/watch?v=u-H43tRgYJg&t=503s) · b000010

them with these uh low rank factors. Okay. And you'll get some practice in your homework. Um this can be implemented in a differentiable manner in PyTorch. You can optimize what that rank is. Right? These this rank goes to the full dimension of the matrix. you recover all possible weight matrices but in practice usually low rank is sufficient. Any questions about these higher order interactions fusion and these low rank approximations.

### [09:04](https://www.youtube.com/watch?v=u-H43tRgYJg&t=544s) · b000011

Okay. And then we saw um you know so far in these in these methods each of these weights right that we learned that weight how much a modality contributes to the fusion is static and what that means is that it is the same weight w1 always applied to x plus the same weight w2 always applied to xb right so we then saw uh these weights extended to become more dynamic so we call this ga fusion where perhaps the weight for XA should depend itself on what XA is and the weight for XB should depend itself on what W XB is right and it could also depend on the other modality as well. So this gives you a formulation where you're doing fusion in the additive setting. Your output Z is still a weighted function times X A except it's

### [09:59](https://www.youtube.com/watch?v=u-H43tRgYJg&t=599s) · b000012

not a static weight W1 that is the same for all XA but rather a function that depends on the current X A and XB. Right? So this function can be learned depending on what X A and XB is. That output could be different. Uh likewise the weight for XB could depend on another function that is learned G of B that depends on what the current A and B is. So the intuition here is that depending on what it is sometimes A is more important sometimes B is more important we should not give global weights to each one of them but you want to have weights that depend on the current importance as scored by these uh GA and GB models. So these A and G and GB can be seen as attention functions and the gating instead of being a single weight now depends per data point that you give to the model.

### [10:56](https://www.youtube.com/watch?v=u-H43tRgYJg&t=656s) · b000013

By the way, somebody asked a question. So um all of these slides are on Canvas and uh they're they're kind of uploaded before class. So this is on Canvas. And a quick note about the the website. The website is meant to be public facing uh so it's not going to be updated as sporadically and I have to edit all the videos before I can put them for the public. So all these slides and recordings and syllabus and homeworks are all on canvas. That will be our primary medium uh where everything is centralized.

### [11:29](https://www.youtube.com/watch?v=u-H43tRgYJg&t=689s) · b000014

Great. Any questions about dynamic fusion? Yes. when you learn these. So this uh establishing like GB is that involves some domain knowledge like for example someone that that person that presented the other day about uh like ocean dynamics and things like that. Would that involve having some like coming in with some knowledge about that function do or is it very much just like attention determining kind of with no yeah like adop knowledge?&gt;&gt; Yeah, I mean it could be both. It could be both um purely data driven. So this recovers as you've already pointed out some of these attention functions that we see today. It could also depend um on some domain knowledge. Uh on Tuesday, I'm just recapping here. But on Tuesday, we also further gave this example where this GA and GB need not be symmetric, right? So you could have a primary modality A. Nowadays, language is very

### [12:25](https://www.youtube.com/watch?v=u-H43tRgYJg&t=745s) · b000015

dominant. You have very good language models and language representations. So I'm not going to modify language too much but I'm going to only modify and learn this GA and GB for my audio and video modalities right so that is some sort of domain knowledge based on the fact that language is very dominant for communication and I just want to learn these gates for the non-verbal audio and video yeah so it need not be symmetric need not be fully data driven absolutely there's space for for some domain knowledge in this

### [12:58](https://www.youtube.com/watch?v=u-H43tRgYJg&t=778s) · b000016

Okay, so these are all examples of um of of you know how we can inject and how we can design these fusion methods very carefully and of course um we also saw the other extreme being this early fusion. We contaminate your data or your features very early on and you let the fusion and your prediction model do most of the heavy lifting and try to design uh models that you hope are able to capture that fusion. uh also a very straightforward approach easy to implement should probably try out for any application that you're working on. Uh so concatenate at the data level or feature level and and just design what is treat them as basically one single modality from then on afterwards and design the best model that is fusing and predicting them. A big question of course then becomes what is this model learning right? We're hoping that your model will learn something interesting and something

### [13:56](https://www.youtube.com/watch?v=u-H43tRgYJg&t=836s) · b000017

nonlinear about the how the modalities interact. Uh but how can we measure whether the model is actually successful at doing that? So I want to highlight a paper that I like very much it falls under this bucket of not just developing new methods but really trying to probe and understand how existing methods perform. So it is a paper that's called you know how to measure what non-additive interactions are learned by your model. So it assumes that you have some function f which is your fusion function that you've already learned on top of a and b and this function f predicts your label. Right? The goal to analyze how much non-additive complex interactions this model learns is to simply project this model in to the simplest and closest additive function.

### [15:02](https://www.youtube.com/watch?v=u-H43tRgYJg&t=902s) · b000018

dance party going on over there. So how do you project this function f arbitrary? It can be anything that you learned neuronet networks, transformers, huge foundation models. How can we find the nearest approximation of this function that is simply an additive combination f of a on x a plus f of b on xb? Right? If I can find this closest additive function and measure the difference to that function, then I can summarize how much of my function was just purely additive, which is this f of a plus f of b and how much of it was non-additive that was actually learning any of these complex tensors or dynamic fusions between your modalities. So it turns out from statistics there is actually a very simple way of finding this closest additive function and this is what it looks like. So the closest additive function is the summation of two terms of course because it's

### [15:58](https://www.youtube.com/watch?v=u-H43tRgYJg&t=958s) · b000019

additive and the first term is you take your fusion f of x a plus xb uh sorry f of xa and xb and take an expectation over xb expectation basically means feed all possible xbs that you have in your data set into this model and take an average over all your xbs right by definition taking expectation over xb marginalizes xb B out and that gives you a function over f of a and x of a. Uh likewise for the other term I'm going to take an expectation of the fusion over all x of a right feed in all possible x a see what the output is and take an average over all xas again by definition that marginalizes x a away from the function and that gives you a function f of b only over modality b right so you can actually show that this is the nearest uh additive function

### [16:54](https://www.youtube.com/watch?v=u-H43tRgYJg&t=1014s) · b000020

that works for any particular input function f that you And visually it looks something like this right it can take uh all these sort of complex functions like neuron nets uh pre-trained models like your multimodal vert pre-trained models or language models it can even take you know svms and other kernel functions essentially projecting them into the space of functions that are purely additive functions f of a plus f of b uh so they call this emap or empirically multimodal additive projection Yes.

### [17:29](https://www.youtube.com/watch?v=u-H43tRgYJg&t=1049s) · b000021

What you comput?&gt;&gt; Um it depends on distance function but you can think about as nearest and in the square distance between the yhat produced by the function f with the yhat produced by this space of um additive functions. So it's the claim that across all distance functions this map gives you the&gt;&gt; yeah I mean I didn't I don't know whether it's across all distance functions but the paper includes uh some proof of this right for some distance functions.

### [18:00](https://www.youtube.com/watch?v=u-H43tRgYJg&t=1080s) · b000022

So that means in practice we can take some fancy fusion function that you've learned or claim to be good and you can do this EMAP projection into your f of a plus f of b where each of them are expectations over the other modality and of course there'll be some difference there'll be some difference mu which is the difference in the predictions that you did not capture using this additive projections another question is how much of these models are captured using an additive function and how How much of it is not? So how much is new? So they took a bunch of models uh some of these are very complex models and they find that surprisingly you can capture quite a bit using just the additive approximation. So that's measured by the difference in performance between the original fusion model and the additive projection which is this line over here called EMAP. So

### [18:56](https://www.youtube.com/watch?v=u-H43tRgYJg&t=1136s) · b000023

sometimes you see 91.3 drop to 91.1. Sometimes you see 74.4 drop to 74.2. You see uh 53.4 drop to 51.0. So you're seeing some performance drop when you start doing this additive approximation. But surprisingly sometimes it is not too much. Right? So this is um this is a hard truth. Right? Sometimes you try to design really complexion. You think you're successful. You think you have this beautiful fusion algorithm. Well, it's always good to do a check to see how much of it is simply learning good additive models of your data and how much of it is actually going beyond additive and learning these complex interactions. Right? I mean there's two reasons why it's not successful at learning these complex interactions. One possibility is that these complex interactions are just not present in your data to begin with

### [19:52](https://www.youtube.com/watch?v=u-H43tRgYJg&t=1192s) · b000024

and your data set to predict a label can be pretty much solved using adequate combinations. That's one hypothesis. The data itself is not complex enough. Second hypothesis is that the data is complex enough but the way that you are designing or training the model means the model is not successful at capturing those complex interactions. uh you can get some intuition also on uh what the performance numbers look like right if in this case I think um I don't know why this INT data set I don't remember what it was but in this case the performance is already 91.3 it dropped to 91.1 that means probably this data set doesn't have complex interactions so both your multimodal models and your additive models are already very good more than 90%. this other data set for example TV vis um the best additive model is 51 the best multimodal model is 53.4 more probably

### [20:48](https://www.youtube.com/watch?v=u-H43tRgYJg&t=1248s) · b000025

means that this data set contains complex interactions but uh these folks are not successful at training a model that capture these interactions otherwise you'd be getting 80 90% instead of 53% performance.

### [21:07](https://www.youtube.com/watch?v=u-H43tRgYJg&t=1267s) · b000026

Okay. So these kind of um these kind of sanity checks uh these kind of diagnostic tools are always very useful uh because we don't want to just train models but we also want to really understand what these models are learning. Any questions about this?

### [21:30](https://www.youtube.com/watch?v=u-H43tRgYJg&t=1290s) · b000027

Yeah.

### [21:36](https://www.youtube.com/watch?v=u-H43tRgYJg&t=1296s) · b000028

Well, additive fusions themselves can also be very powerful, right? They they give these kind of late fusion approaches where you just, you know, put A through a classifier, B through a classifier, add them up. If they work well, like for example, in these cases, they're at 91% performance. Yes, we should definitely use them. They're efficient, they're interpretable. Um, they of course don't work well in some settings. So, that's one story, right? Sometimes they don't work well. But I think a bigger more important story here is that uh one should not just design models that seem complex and and seem to work well on the surface without really understanding what they're learning deep inside. And therefore I like these kind of works which are challenge the assumptions and go back and quantify exactly what these models are learning and in this case challenging the hypothesis that you need all these complex interactions when in fact they don't seem to be very prominent in practice. Yes.

### [22:30](https://www.youtube.com/watch?v=u-H43tRgYJg&t=1350s) · b000029

&gt;&gt; Does that suggest we just start with this or let's start with like an additive fusion before you go to&gt;&gt; Yes, always a good baseline. Things like early fusion, late fusion, additive fusion, just concatenating is always a good baseline. That's why we we push you all to do it for for homework too. And then likewise for the midterm where people have to run you all have to run like strong baselines and then you start uh going complex.

### [23:01](https://www.youtube.com/watch?v=u-H43tRgYJg&t=1381s) · b000030

Yes.

### [23:15](https://www.youtube.com/watch?v=u-H43tRgYJg&t=1395s) · b000031

&gt;&gt; These are accuracies. These are accuracies. Um so the point being that um I mean ideally they should have ran all this with you know confidence intervals and and cross validation but the point being that sometimes it's not too much of a difference between a a proper you know complex model versus the the model that's just doing linear combinations. Um I mean of course sometimes maybe this 2% can make a difference. Uh but that's up to up to you and up to the domain.

### [23:54](https://www.youtube.com/watch?v=u-H43tRgYJg&t=1434s) · b000032

So one extension from this to really force to really force the model to um you know start learning these interactions is also not to do all this fusion at the same time but to do this fusion stage wise right fusion can also be done in a stage-wise manner. uh to see what that means. You know, one approach you could do that's in follow-ups to this work as well is that you have your you know two or three modalities. You first start by pushing the model to learn as much unimodal information as possible. Right? So basically you train unimodal classifiers uh where XA is taken to predict label, XB is taken to predict a label, XC is taken to predict a label all separately and then you add them up. Right? So that gives you the uh the best unimodal models and when you start adding them up the best additive models

### [24:51](https://www.youtube.com/watch?v=u-H43tRgYJg&t=1491s) · b000033

right you first train that that's stage one once you've trained that you then train stage two which is then you start looking at B and C combinations B uh A and C B and C A and B combinations and start adding these biodal and then you start combining all three of them and you learn this triangle and how you learn it through these three stages is that you would first take the label Y and you would measure the difference between your target label and what the best additive function learns, right? So try to push the additive function to be as good as a label as possible. And then you compute the difference, the difference that is not captured by the additive models. You call that the residual and you use the residual and try to learn that residual using a biodal ver. Right? So the residual is y minus y unimodal. You compute a difference between that residual and y

### [25:47](https://www.youtube.com/watch?v=u-H43tRgYJg&t=1547s) · b000034

biodal. So the output predicted using pairs of modalities. And then you see there's again some error. Uh you treat that as a residual again which is y minus unimodal minus biodal. And then you fit that residual using the the three modality terms. So you can treat this fusion also stage wise. Uh this is really good because now you're guaranteed for each stage you get better and better because you're only fitting the residual using the next modality. So you either get better and the residual decreases or if nothing is learned the error is the same. So you're guaranteed to either get better not worse. That's good. And you can also stop wherever you want. Right? If you think this residual at the start is 10, that's too large. I'm going to fit it to biodal. If I fit bodal the residual becomes two uh that's good enough. Uh then you don't have to do this. So you can basically do this

### [26:44](https://www.youtube.com/watch?v=u-H43tRgYJg&t=1604s) · b000035

stage wise fusion and decide wherever you want to stop and find the right balance between what you use and what the error is.

### [26:57](https://www.youtube.com/watch?v=u-H43tRgYJg&t=1617s) · b000036

All right. So that's that's stage wise fusion. Uh good way of dealing with with problems in which data is very complex. You want to do fusion stage wise, you want to determine when to stop and you don't want fusion to uh to make things worse because sometimes fusion does make things worse. Sometimes uh you have these like three modality fusions, they take up a lot of parameters and these parameters are hard to optimize. Sometimes you see adding more modalities can also make things worse.

### [27:31](https://www.youtube.com/watch?v=u-H43tRgYJg&t=1651s) · b000037

Okay, so to summarize uh both recapping Tuesday and also adding a little bit more content that I wasn't able to cover on Tuesday, multimodal fusion, the purpose is to learn this joint representation that models how two different modalities interact, right? And the goal is really to try to model all the interactions that are necessary in the data but nothing more, nothing less, still remaining reasonably compact, efficient and understandable to downstream users. We saw two spectrums. One where you first start extracting features from your modalities, right? Using good unimodal encoders and features that are more semantically meaningful and more likely to be homogeneous in nature. And on the other extreme there's also a paradigm where you have raw data you're doing fusion earlier when the data is more heterogeneous but this gives you benefits because now the fusion and representation learning can be learned

### [28:27](https://www.youtube.com/watch?v=u-H43tRgYJg&t=1707s) · b000038

end to end together. And we saw different methods along this spectrum extreme being late fusion when you're already predicting a label and then you're you're combining the labels in some way. We saw additive fusion um going beyond additive first order you saw multiplicative three modalities was tensor and it can go to even higher order polomials between modalities. Uh some of this can be very expensive. So we saw low rank approximations of them and all of these still maintain the same weights for your modalities right same W1 for X A W2 for XB. So we then saw settings in which your weights are dynamically changing given your current A and B. So those are gated fusion or dynamic and modality shifting fusion.

### [29:24](https://www.youtube.com/watch?v=u-H43tRgYJg&t=1764s) · b000039

And then we'll see some of these um which are more early fusion methods later on in the semester when we talk about how these transformers and multimodal transformers can be used to do much earlier fusion. Right? Any last questions about fusion? Yes.

### [29:54](https://www.youtube.com/watch?v=u-H43tRgYJg&t=1794s) · b000040

So for example problem here would be the classification your classes might be like the cat&gt;&gt; it can be cross entropy difference in cross entropy error um great you can any mean square error cross entropy error and any other any loss function that you use um can be done with Yes. Great. Yes.&gt;&gt; Question about this slide. So, yeah. No, the one the one that you have.&gt;&gt; Okay.&gt;&gt; Um, so you you talk briefly about compute for those different approaches. Um so do we have a good understanding like what is the difference between those approaches magnitude as we progress more towards

### [30:50](https://www.youtube.com/watch?v=u-H43tRgYJg&t=1850s) · b000041

heterogeneous modalities.&gt;&gt; Uh do we have a good understanding? Uh if you mean do we have a good theoretical understanding and guarantees? No, because these things are hard to come by in in deep learning or anything where you know neuronets \[snorts\] and non-convex optimization is evolved. Do we have good intuitions? Um I think it comes with practice, right? Comes with I mean that's the purpose of this course where you're going to try a bunch of different fusion methods for homework two maybe for your project if you're focusing on fusion. Um and then you'll start seeing for example you plot compute right a lot of these as you go from this to this roughly speaking you'll need more and more compute uh because the fusion the the the fusion parameters is larger and then you can see for yourself whether performance gets better or worse right so not necessarily always performance gets better but also sometimes those

### [31:45](https://www.youtube.com/watch?v=u-H43tRgYJg&t=1905s) · b000042

don't work at all and you have to start doing early fusion using huge models right Um I mean there's general guidelines right general guidelines is that simple baselines are always very helpful simple early fusion late fusion baselines um you know simple baselines based on pre-trained models are always very helpful and then comes these task specific requirements which is how much compute or how much are you willing to use a black box which is something that really tells you here are the fusions that's happening at this stage and here is the interaction. So there's a lot of considerations there as well.

### [32:29](https://www.youtube.com/watch?v=u-H43tRgYJg&t=1949s) · b000043

We are trying to build up um I mean a key a key vision uh that some of the work we're doing is is to kind of build up a more formal understanding of these. So you can search up some of the papers that we have. Um and what story we can essentially tell is that if you have some data right X1, X2 and Y you have some samples you can first quantify some statistics from your data and these statistics might say there is this amount of synergy between your modalities for these certain elements right we are we are on our path towards developing such a framework and we already have some early evidence to show that this exists and then based on that knowledge for example there's this much of bits of synergy that has to be fused we can then approximately prescribe which fusion method is the most useful right so sometimes you find that uh you quantify and most of the

### [33:25](https://www.youtube.com/watch?v=u-H43tRgYJg&t=2005s) · b000044

information is very unique in X1 in which case you don't need all these fancy methods right just use X1 unimodal and then sometimes you quantify and find there's lots of synergy between A and B uh between one and two uh then you have to use maybe some more complex fusion method it's not a perfect mapping but uh it helps give you some intuition uh and more work needs to be done in this. So if you want to do a project in this space that's also highly encouraged. So more more rigorous more more more foundational principles.

### [34:01](https://www.youtube.com/watch?v=u-H43tRgYJg&t=2041s) · b000045

All right. Any final questions about fusion? Okay. Very good. So now we'll move on to what this today's lecture was actually planned for which is to discuss alignment. Uh fusion and alignment are perhaps the two biggest core concepts right uh in multimodal. So we'll cover basics of multimodal alignment. We'll cover contrastive learning as a common approach of explicitly enforcing alignment uh in a discrete setting. We'll cover a little bit continuous alignment and then we'll cover this very new theme of what we call implicit alignment, right? Where alignment emerges from training models without explicitly enforcing it using your objective functions like contrastive learning. So what is alignment? So alignment aims to identify and model all different ways in which different elements in your

### [34:57](https://www.youtube.com/watch?v=u-H43tRgYJg&t=2097s) · b000046

modalities are connected with each other. And we'll give a more formal version of what connected means. But you can intuitively think of it as you know overlapping information or representing some underlying similar concept. There's three sub challenges for alignment. The first case being the most simple where you can segment your modalities into discrete elements. Right? So words that a person is speaking, objects that are in the image that are being referenced, uh facial expressions that a person is making across something. So once you can uh explicitly separate your modalities into elements, then you can think of alignment as basically this this matching problem. For example, which word in the caption references this chair in the image and then which other word references this other part of the image. often times alignment is this this matching problem between semantically similar elements across

### [35:54](https://www.youtube.com/watch?v=u-H43tRgYJg&t=2154s) · b000047

your two modalities. So discrete alignment or learning these discrete connections is the easiest case. This problem becomes more challenging when your elements are more continuous whereas higher resolution continuous it is not clear what the granularity is. Right? So for example, aligning video to text or aligning sensor data to text is more difficult because it's not really clear what the semantic boundaries are in video and sensors. It is not as clear as you know here's a word that I'm saying in my sentence. So we cover both of these today. Uh I also want to complete the story and note that in this two settings alignment is the end goal where the goal is to find out which word references this part of the image or which word references which part of the video. Alignment is the end goal. There is a third sub challenge where alignment is used as an

### [36:51](https://www.youtube.com/watch?v=u-H43tRgYJg&t=2211s) · b000048

intermediate step to learn better downstream representations and we call that contextualized or line representations. So over here I draw you know most of these alignments are in gray. How do you use the alignment to learn better representations? For example, as you all seen language models today, we have these words and we know how they align and are contextualized with other words in the context. This is critical to learn more powerful sentence representations. Right? In multimodal LLMs, we have all these words and questions that are contextualized with previous words and also contextualized with parts of the image depending on how the alignment happens. It is this alignment and contextualization that allows you to train better multimodal LLMs. So this is where alignment is used implicitly as an intermediate step to learn better representations. We'll cover a lot more of this in the next two weeks where we'll cover you know these

### [37:46](https://www.youtube.com/watch?v=u-H43tRgYJg&t=2266s) · b000049

multimodal transformers and foundation models. Today we'll stick with um just where alignment is a goal of learning discrete and continuous alignment between modalities. Any questions about this this road map?

### [38:08](https://www.youtube.com/watch?v=u-H43tRgYJg&t=2288s) · b000050

Okay. So starting with discrete alignment. So the goal here is to identify and model these connections between discrete elements across modalities, right? And you want to think about these connections as some amount of information that is shared with a similar semantic meaning between them. Again, I'll use these uh these these you know triangles and circles A and B. And you want to think of these connections as capturing what is shared and basically ignoring what is unique, right? Anything that is unique will basically be discarded once you start doing alignment. Yes.&gt;&gt; Um would it be possible for you to get practical examples with um each challenge? So I guess like in this case modality a could be laby pictures. So um modality like each unique um feature would be like one CT image for example.

### [39:05](https://www.youtube.com/watch?v=u-H43tRgYJg&t=2345s) · b000051

&gt;&gt; Well we'll get to that next slide. um which is one example is I mean the easier example is basically vision and text uh image and text. So this is a image and your caption could be a woman reading newspaper right image is segmented into bounding boxes of different objects woman newspaper the caption is segmented into tokens um and woman text corresponds to that part of the image newspaper text corresponds to that part of the image. Uh it's interesting to note what was the alignment between the word reading and the MHV anybody? Yes.&gt;&gt; Probably eyes or the hands or the combination of them&gt;&gt; perhaps? Any other takers? What would the word reading map to? Yeah,&gt;&gt; you like the head tilted down&gt;&gt; maybe. But even head tilted down, eyes, if you don't see what is the newspaper,

### [40:02](https://www.youtube.com/watch?v=u-H43tRgYJg&t=2402s) · b000052

the target, you don't know whether the person is reading or just like staring at something or falling asleep, right?&gt;&gt; Color of what pixels?&gt;&gt; Oh, the news. So if red was a phone, it would probably be dark. If it was a newspaper, it's probably lighter.&gt;&gt; Uhhuh.&gt;&gt; Interesting. Well, I mean the short answer is that it's ambiguous. Uh this is not a onetoone mapping. probably it will be the reading should align to a function of of course the the woman's face and gaze direction at the same time also uh the newspaper and maybe the color newspaper has to be there to know that there's some target that there is reading so alignment is often not just one to one in the case of women newspaper it's one to one sometimes it is one to many this word maps to many things and it can also be the relationship between different things the relationship in this case between the

### [40:57](https://www.youtube.com/watch?v=u-H43tRgYJg&t=2457s) · b000053

and a newspaper right but that's uh an example that I was going to give uh and here I also want to highlight several intuitions of why this alignment why these connections exist right and how we can discover them right one is through from a more statistical perspective right based on association if I always see you know the word newspaper in these captions with various newspapers in different you know images where newspapers exist this then with enough data you can identify this association that the common word in all of these captions newspaper maps to the common object in all of these images which is the photo of a newspaper. Uh so that's from a correlation perspective a co-occurrence perspective how we can discover the alignment. uh but also that gives some semantic meaning which is that you know this newspaper the word newspaper actually

### [41:53](https://www.youtube.com/watch?v=u-H43tRgYJg&t=2513s) · b000054

means something and the image of the newspaper actually means something. So this identifies the correspondence which has the same meaning between those two terms that just so happen to be expressed one in text one in image. Uh beyond these uh I you know singular co- occurrences like we saw the onetoone mapping between women and newspaper we also have other you know pairwise or higher order interactions between higher order connections between one modality and another. So we saw the example of reading right this idea of reading in text uh really maps to this dependency where there's this eyes and this directed mapping to the newspaper right and likewise from a semantic perspective there's some relationship between the eyes and the newspaper that indicates you know the function of the eyes which is which is to read so there's different levels in which these connections exist

### [42:48](https://www.youtube.com/watch?v=u-H43tRgYJg&t=2568s) · b000055

onetoone associations is the easiest and most clear but at the same time there are higher order pair-wise functionality that needs to be captured uh during alignment. Okay, but how exactly do we capture this? Uh a general way of capturing this is through what we call um paired data, right? If you have lots of paired data, in this case, paired data between images and text. So pairing basically mean that image corresponds to this caption. Image two corresponds to this other caption. I can then start learning these representations where A and B are each encoded by F of A and F of B. This encodes them into representations Z A and ZB. And the goal is to define a similarity function G

### [43:43](https://www.youtube.com/watch?v=u-H43tRgYJg&t=2623s) · b000056

that captures the fact that ZA and ZB are connected with each other and perhaps other ZA and ZB are not connected with each other. So that's a general way of capturing alignment, right? A and B come in one encoder for each F of A F of B. This gives you features Z of A, Z of B and there is some similarity function G scoring whether they are aligned or not or the extent to which they are aligned. Okay. Uh you'll see that now this is different from fusion right in fusion you have A and B and you're bringing them together into one joint representation Z. Uh but now in alignment you have A and B. You're learning two separate representations Z of A and Z of B and you are computing some alignment or some similarity function between them. Yeah.&gt;&gt; Would attention kind of piggyback on these statistical um co occurrences

### [44:39](https://www.youtube.com/watch?v=u-H43tRgYJg&t=2679s) · b000057

like between reading for example and data.&gt;&gt; Uh yes yes alignment would would capture some of this. So that's how we'll talk about um you know how this alignment can be learned using attention uh but using that how you also learn these downstream representations later when we talk about this uh next week. Yeah. But yes attention and is one way of learning that. Okay. So any question about this this paradigm and how it differs from fusion. Right now we're not learning one joint representation that fuse us but we're learning and keeping separate representations Z of A Z and B and you are uh keeping them consistent using this this similarity function.

### [45:28](https://www.youtube.com/watch?v=u-H43tRgYJg&t=2728s) · b000058

All right. So you can think of these encoders as or you can define them however you want. These encoders are designed to capture you know the heterogeneity. It's it's you know it's adapted to the different data modalities and their individual structures. But once Z of A Z of B are learned then this uh coordination function G essentially captures the the connections uh between them. And a general way of of learning this learning this alignment function is to define a loss function. uh loss function is going to be first put f of a um on madata da and then you put f of b on madata db that gives you representations and then you score them with g right g is the function that scores the the similarity between them what are the trainable parameters you' be trainable parameters

### [46:23](https://www.youtube.com/watch?v=u-H43tRgYJg&t=2783s) · b000059

data inside this g function so in fact that similarity function could also have trainable parameters okay uh and Then you will of course have the trainable parameters data for f of a your encoder for a and f of b your encoder for b. Right? So those are the trainable parameters and you would optimize them uh to in this case maximize this g if g is similarity or minimize it if g is some some distance function.

### [46:55](https://www.youtube.com/watch?v=u-H43tRgYJg&t=2815s) · b000060

So what are some examples of g? um G can be cosine similarity, right? So G takes in Z and ZB can be cosine similarity that essentially takes a dotproduct between A and B uh perhaps normalized by their by their magnitudes. Right? So that keeps it nice and intuitive between between uh negative 1 positive one uh normalized by the magnitudes that captures a linear notion of similarity. So whether these two vectors point in the same direction in representation space we can also extend it to kernel similarities. Folks have taken machine learning have seen kernels. Kernels are any function that scores uh given these two vectors score some distance between them. Right? These kernels can be linear in which you recover the dotproduct between these two vectors. So where they

### [47:51](https://www.youtube.com/watch?v=u-H43tRgYJg&t=2871s) · b000061

point in the same direction but they can also be polomial exponential RBF the only differences between these other kernel functions is the space in which you're computing these similarities in you first transform them to some polinomial space and then compute these similarities or do you keep them in the original space and compute those similarities in the original space. uh there are benefits of transforming them into different representation spaces and basically thought of as learning similarity in some nonlinear function of the vectors instead of in the original space that they came in. So any of the kernel functions can be used for similarity correlation can also be used. So in this case, I may not care about just whether these two points themselves, right? Whether these two points are close by or they're pointing in the same direction, but I care about the whole distribution, right? I care about this whole

### [48:48](https://www.youtube.com/watch?v=u-H43tRgYJg&t=2928s) · b000062

distribution of points in my first modality and the distribution in the second and whether they're correlated with each other, right? So that could be a notion of similarity. Similarly, I might care about Yes.

### [49:09](https://www.youtube.com/watch?v=u-H43tRgYJg&t=2949s) · b000063

Yeah, I'll give some examples. But uh let me talk about this first before we go to distribution. Let me talk about the pair wise case first. Um sometimes I don't care about whether let's say I'm apple orange and apple orange, right? Apple orange in text, apple orange in en invision. I may not care that the word embedding for apple is close to the image embedding of apple. Doesn't really matter where they are. But what I might care about is that the relationship between the word embeddings of apple and oranges are consistent with the relationship between the image embeddings of apples and oranges. Right? Specifically that this transformation represents keeping the shape by changing the color. Right? Right? So I may not care about the individual locations of points themselves, but I care about the the order or the pair wise relationships distances between for example apple orange in text and apple orange in um in

### [50:04](https://www.youtube.com/watch?v=u-H43tRgYJg&t=3004s) · b000064

images. Uh if we send it to the three threepoint case I might care that apple orange are nearby but very far away from table in word embeddings and likewise apple orange are nearby but very far away from table in the visual embeddings. Right? So now you start seeing it is sometimes these pair-wise and three-way relationships between the points more important than the specific location of the individual points themselves. Make sense? Yeah.

### [50:55](https://www.youtube.com/watch?v=u-H43tRgYJg&t=3055s) · b000065

it can still be trained. Um I mean this paradigm would still work, right? You will put a uh text through a text model, you get text embeddings. You put B images through a image model, you get image embeddings. And now I have a bunch of text embeddings representing apple, orange, and table. I get my image embeddings representing apple, orange, and table. And all I'm doing is computing this differentiable function which is the pair wise distances between apple orange and table for text and the pair wise distances between apple orange and table for images and I'm trying to structure them in some coherent way right and that is your function jeep right um in fact one slide in the back for this um I mean this is what uh it looks like right so my care that my image embeddings apple orange and elephant are structured in this way. Apple orange close together elephant far away and

### [51:52](https://www.youtube.com/watch?v=u-H43tRgYJg&t=3112s) · b000066

likewise for text embedding apple orange close together elephant far away. How do you do that? Um I won't get into details but you can define kernels for each right so this function basically says I'm going to look at all pairwise distances between all the image embeddings that I have. This will say I'm going to look at all pair wise distances between the word embeddings that I have. Those two give you some summary as some kernel and my similarity is how these two kernels which basically means a pair wise graph of distances how similar they are right you can maximize that to ensure similarity.

### [52:33](https://www.youtube.com/watch?v=u-H43tRgYJg&t=3153s) · b000067

I saw. Yes.&gt;&gt; The ground truth label is somehow implicit. I think in the that function it's just using the embeddings of the two modities but we don't actually like is it not also in the last but

### [53:07](https://www.youtube.com/watch?v=u-H43tRgYJg&t=3187s) · b000068

uh so I think asking two questions here one question is uh the loss is has to be defined right so in this case the loss has to be defined beforehand it is not going to automatically learn that sometimes you care about pair-wise losses sometimes you care about correlation sometimes you care about cosine similarity you have to specify what the loss is so you have to specify what G Um but G can be anything any of these that we just discussed.&gt;&gt; Yes.&gt;&gt; There is a different that actually when are they

### [53:49](https://www.youtube.com/watch?v=u-H43tRgYJg&t=3229s) · b000069

in a supervised manner image and Apple text they should be a positive.&gt;&gt; Yeah. Yeah. So, so we started by saying that um you have paired data, right? So, apple image, apple text, orange image, orange text. So, so you need to have paired data at least in this current setting, you have supervision based on a pair data. Uh but note that the the requirements for what it need to be paired depends on the similarity function. If a similarity function is scoring that you know apple have to be similar and orange have to be similar then your pairing has to come at these individual objects. If for example I only care that uh the whole structure is the same for example if I care about these three pair wise distances being the same then I don't need actually paired data between uh I just need my three embeddings of apple orange

### [54:46](https://www.youtube.com/watch?v=u-H43tRgYJg&t=3286s) · b000070

elephant on one side and I can have three embeddings of orange apple elephant on the other side I don't need the pairing between the three if I'm doing a a triplet wise similarity function like this but if I carry that apple and apple must be nearby. Then I need Yes, this is apple. This is orange. This is elephant. Then I need that.

### [55:18](https://www.youtube.com/watch?v=u-H43tRgYJg&t=3318s) · b000071

Okay. Any other questions? Great. Uh so we see yeah several things um lots of different choices for the similarity function. lots of uh different functions may been proposed throughout your really just depends on the setting whether you care about individual points being aligned whether you care about the um the global structure right the other case is the more global structure being aligned you care about pairwise relationships being aligned um all that can change what your what your similarity function is and it also changes your requirements for your supervised data right you basically need supervised data at the resolution at which you want the pairing to be achieved in a similarity function. And also want to emphasize all this again learn to end right. So your loss function which you're trying to optimize

### [56:14](https://www.youtube.com/watch?v=u-H43tRgYJg&t=3374s) · b000072

is the function similarity function G on top of your two embeddings ZA and ZB but each of those two embeddings are also functions of your unit model encoders F of A modala TA F of B or Madala TB. So all this can be back propagated and trained end to end. Of course, if you see benefits of pre-training f of a and f of b uh that also works. So using that let's let's give the concrete algorithm which is you know nowadays people call it contrastive learning. Uh but again there's much more general similarity functions than just contrastive learning which is that you start with some paired data for example images and text. uh in the standard version of contrastive learning they care about having each image and text representation being very close to each other. So for that to happen you need

### [57:08](https://www.youtube.com/watch?v=u-H43tRgYJg&t=3428s) · b000073

paired data for each image and text right. So as an example here you would have image of that and you say text caption in blue car image and that's yellow bus image and airplane and this image that says bowl of cats. Um so using this paired data you would define each of the correspondences as positive pairs. Uh so there's four positive pairs here and anything that is not a positive pair which is a random permutation will be negative pair. Okay. So there's um 12 negative pairs here. So positive pairs in green, negative pairs in red. And then in contrasted learning, the idea is to again score this alignment between modalities by bringing positive pairs which are connected close together and pushing together negative pairs

### [58:04](https://www.youtube.com/watch?v=u-H43tRgYJg&t=3484s) · b000074

which are far apart. Okay. And what that might look like is uh using this kind of hinge loss formulation is to maximize this function where G your similarity is scored on ZA and ZB plus which are your positive pairs. Uh that's going to be a positive dependence. So you're going to maximize the similarity and it's going to maximize a negative. So in other words, minimize the similarity of G uh between ZA and ZB minus which are your negative pairs. So four terms go into adding up the similarity between positive pairs that's maximized and 12 terms go into adding up to these um similarity functions for negative pairs which are minimized.

### [58:52](https://www.youtube.com/watch?v=u-H43tRgYJg&t=3532s) · b000075

And in the um in contrastive learning, these coordination functions are are cosign similarity. And while you know contrasted learning became popular with clip nowadays, but even even back in like 20 2010s, people people were doing this albeit at a smaller scale. And once you start aligning your data like this, you actually see very interesting observations, right? So you could essentially do retrieval. Uh one really powerful thing about these alignment methods is that you can you know score a feature or your image and retrieve what is nearest in text. Uh you can do this crossodal retrieval. So you can also do this crossodal arithmetic. Uh so what's happening here is that you take a image of a blue car, you embed it into your feature space, you subtract the feature embedding of blue text and then you add the feature embedding of uh red the word

### [59:49](https://www.youtube.com/watch?v=u-H43tRgYJg&t=3589s) · b000076

red, right? And that gives you a new feature and you can score the nearest similarities and you can retrieve uh nearest images of red cars, right? And this is only possible this kind of arithmetic minus saying some concept adding some concept is only possible when these two representation spaces are well aligned. Right? So blue text actually means something in the context of your images and the red word actually means something in the context of your images. You can take a blue image minus the word blue plus the word yellow to get yellow cars. You can do this from yellow buses to red buses. Uh you can do things like airplane photo of a plane minus the word flying plus sailing and you treat images of sailboats and even this cute bowl of cats minus the word bowl plus the word box to get a box of cats.

### [1:00:48](https://www.youtube.com/watch?v=u-H43tRgYJg&t=3648s) · b000077

So you know early signs of contrastive learning of course this was just done with small low resolution images and just one word or or one word or you know one adjective and one one uh one object for for your text. And nowadays people have really scaled this up using clip and other forms of of free training where you can get a huge bank of images and get a huge bank of their captions, right? You can get this from Wikipedia. You can get it from Instagram, Flickr and other image retrieval data sets. You have a huge bank. You put them in a batch. Everything that is in the diagonal are basically positive pairs, right? Those are examples where the image actually corresponds to the caption and everything off diagonal are basically negative pairs. Right? In this uh big batch by batch uh matrix and each of these entries in the batch obviously

### [1:01:44](https://www.youtube.com/watch?v=u-H43tRgYJg&t=3704s) · b000078

passing your images to your imaging encoders you get n image embeddings. Uh you put your caption through a text encoder you get n of those text embeddings. And each of these entries are the cosine similarity between uh image embedding I with text embedding J. Right? And everything in a diagonal those cosine similarities represent positive pairs. Everything off diagonal represents negative pairs. And the contrastive learning loss would essentially be uh no longer this this uh hinge loss but rather this ratio where on the top which you are maximizing because it's a loss with a negative. So you're actually maximizing that term the similarity of positive pairs and on the bottom you're minimizing the similarity uh technically you should only minimize it over negative pairs but for implementation efficiency reasons you minimize the sum of similarities across

### [1:02:39](https://www.youtube.com/watch?v=u-H43tRgYJg&t=3759s) · b000079

all negative pairs and that one positive pair. It's much easier to implement efficient on GPU kernels and even adding one positive pair the denominator doesn't really make a difference in practice. is still going to be dominated by about a negative pair losses. Okay. And the similarity function is still cosine similarity. So each of these are just I uh I embedding for image dotproduct embedding for text.

### [1:03:12](https://www.youtube.com/watch?v=u-H43tRgYJg&t=3792s) · b000080

Okay. So people find that uh once you train the model in this way your encoders which are what you're being what you're training uh your encoder for language and coding for vision they're really good encoders for downstream tasks and again the key idea is that you have these embeddings that are aligned but are separate right it's not fusion but you're keeping them separate but aligned with each other and of course nowadays you can do much better crossal retrieval with these larger models. So, you could give it um give it an image. For example, this image is look like a television studio. You can give it a bunch of possible captions, right? A photo of a television studio, a photo of a podium, a photo of a conference room, lecture room, and so on. And you embed the image, get a feature. You embed each of these possible captions. You get a

### [1:04:09](https://www.youtube.com/watch?v=u-H43tRgYJg&t=3849s) · b000081

feature and you basically score for each one what the cosign similarity is. Use that as a way to rank what is the most likely caption. So it does say a photo of a television studio. Uh here you can even find the closest caption which is a photo of a Siberian husky even though it doesn't look like a real world husky. Uh but I think it sometimes still makes mistakes. Right? In this case when clip was first released you gave it a images of these different shapes and sizes. Uh it was still not very good at counting. So it gave for example photo of three objects as the most likely instead of four objects. Uh but now these models are again much better at counting. So you can essentially learn these align representations and use them to get really good features useful for downstream tasks. You can do retrieval by scoring a similarity based on the alignment function scoring a similarity across the modalities. And not only can

### [1:05:05](https://www.youtube.com/watch?v=u-H43tRgYJg&t=3905s) · b000082

you do retrieval, you can also kind of do this classification where uh you can give it a bunch of possible categories and let it classify by choosing which one has the highest ranked similarity with the image. That's why some people might have seen that when clip first came out, it was a big win for what we call open set or open domain classification, right? Traditionally, if you want to classify an image into different categories, you had to prespecify what the categories were, right? 10 types of digits or 50 types of of cats and dogs. You had to prespecify what these categories were. uh which either means it was either too big, a lot of them are not used, you're wasting parameters or sometimes too small and you don't are not able to classify new categories. So one of the power of these models is that you could basically give it an image, give it any number of categories, just write a caption for each category, any number any category that you want and you can

### [1:06:02](https://www.youtube.com/watch?v=u-H43tRgYJg&t=3962s) · b000083

still score the similarity and do classification over that set of categories. Any questions about clip and contrastive learning?&gt;&gt; Is there scoring with like similar classification scoring using very similarity functions? Oh, is that just&gt;&gt; um you can yeah any any similarity function you can score right take a image get the embedding right now it's cosign similarity it can be it can be um it can be kernel similarity right all of that is also super fast to compute um if I don't care about scoring a single image and categorizing it I could do the pair wise stuff that we talked about I give it two images and ask them to find the difference between them and it can still give you a bunch of categories. So

### [1:06:56](https://www.youtube.com/watch?v=u-H43tRgYJg&t=4016s) · b000084

now you have a a distance function over pairs instead of one image. So again this this function right this function G can be quite general as long as you can uh implement it in things like PyTorch as long as you can differentiate through it uh it can be used to be optimized and also to to do retrieval.

### [1:07:28](https://www.youtube.com/watch?v=u-H43tRgYJg&t=4048s) · b000085

Okay, let me um wrap up this part by by kind of digging deeper into what clip and these other alignment like methods actually learn. Um so remember we had this kind of diagram where A and B have this vin diagram where there's some shared information between them which is in contrast to the unique information in them. Well, I'm going to give an intuition. I'm not going to go into too much mathematical detail, but one way of thinking about what this shared information is is this concept of mutual information. Now, mutual information is a formal measure that essentially says I'm going to look at both my modalities and I compute the ratio of two terms. One is a joint distribution between them. So, this is a distribution telling me which elements in my modalities are likely to co- occur together. Those that are higher have higher joint likelihood. Those that don't happen together have

### [1:08:25](https://www.youtube.com/watch?v=u-H43tRgYJg&t=4105s) · b000086

lower joint likelihood. That is a joint distribution. And I'm going to compare that to the product of marginal distributions. Product of marginal distributions can be thought of as basically saying I have everything in X, everything in Y. I randomly pair them up. Right? So it's not going to capture any joint distribution, but I randomly pair them up. So mutual information can be thought of as a difference between the actual pairings in my data where this corresponds to this the actual pairing versus a random assortment random way of pairing them up. So for data sets in which information is really large uh that ratio will also be very large. For data sets which are completely independent the two circles don't overlap completely independent that basically means even the paired data that you observe and a random pairing that you get from your data is going to be the same right there's zero mutual information at intuitive level u you can read into

### [1:09:20](https://www.youtube.com/watch?v=u-H43tRgYJg&t=4160s) · b000087

the mathematical details. Well, one can show that um these clip-like losses, specifically this type of of of clip loss, uh actually focuses on capturing the shared information, but more formally, it provably learns this mutual information that you have between these modalities, right? I can uh give you a a quick proof of this um but not required, won't won't be in the homeworks or the exams. But if you think about what this info inc loss looks like, which is that it's scoring this function f, right? This function f is the one that you're learning using cosine similarity. There's a function f that scores highly positive pairs, right? The similarity for positive pairs should be very high and it scores very low negative pairs, right? The the similarity of negative pairs should be very low, right? Okay,

### [1:10:17](https://www.youtube.com/watch?v=u-H43tRgYJg&t=4217s) · b000088

so you can actually think of that function as a critic function which takes in two modalities A and B which are either the true parents and that should be as high as possible the output or it's a randomly sampled pair right negative pair and it should be as low as possible that output. So in other words it can be thought of as a classifier can be thought of as a classifier that outputs something between zero and one. It outputs one if it's a positive pair and it outputs zero if it's negative pair. Right? Based on what we know about these positive and negative pairs, you can also make the argument that uh it outputs one for positive pairs which are sampled from the joint distribution between A and B because joint distributions exactly are the ones which have high likelihood for these positive pairs. And otherwise this model would output zero a very low score for samples A and B uh sampled from the product of marginalss. Right? P of A times P of B.

### [1:11:15](https://www.youtube.com/watch?v=u-H43tRgYJg&t=4275s) · b000089

Because again a definition of multiplying these two marginals together is you randomly sample something from A and you randomly sample something from B and you pair them up without regard for whether it was the actual pairing or not. And that's the definition of a negative pair. So uh that can be thought of as a function that you're learning in contrastive learning uh to basically train a binary classifier that scores samples from the joint distribution very high positive pairs and score samples that you get from the product of marginalss very low which are your negative pairs. And you can show that also when this is optimally trained uh what this classifier has to end up learning is exactly that ratio right the ratio we're given a particular A and B the ratio that it estimates that it came from a joint distribution versus the ratio that it came from these product of marginal distributions. Uh so that's actually what um these models end up learning

### [1:12:13](https://www.youtube.com/watch?v=u-H43tRgYJg&t=4333s) · b000090

when you train it using contrastive learning. And you can then plug this far which is the function that you've learned back into your objective function law uh L which essentially gives you this equation which is that your L-star which is the objective function once this has converged is essentially at least this expectation term and you see this ratio of likelihoods right P of A time P of B over the joint distribution of both A and B and we saw that it was actually very similar to So the mutual information that we just saw, right? So in fact you can show that this loss is at least uh negative mutual information plus log n where n is the batch size number of samples. In other words, your mutual information is at least your loss, right? Or negative loss, which is your objective. Um and what that means

### [1:13:07](https://www.youtube.com/watch?v=u-H43tRgYJg&t=4387s) · b000091

is that basically NCE maximizes a lower bound on your mutual information. So uh the best that you can learn is the total amount of mutual information between your modalities A and B. Uh again not not required for for the homeworks or or for the um midterms but good to know. Key takeaway is that you can actually prove that um these contrastive learning methods are learning some classifier that separates out data samples from the joint distribution which is your positive pairs and data samples from your product of marginal distributions which are your negative pairs. And that ratio is something very consequential and important in statistics and machine learning known as a mutual information. And that basically means that contrastive learning is basically learning as best as it can is bounded by the total mutual information in your data.

### [1:14:05](https://www.youtube.com/watch?v=u-H43tRgYJg&t=4445s) · b000092

But then there's also very important implications which is that if you want to use alignment to learn better representations, it really matters how much mutual information there is, how much shared information there is in your data. So ideally right if this is the perfect scenario where your modalities A and B overlap exactly so that alignment captures this thing in the middle and that information in the middle is what you care about for downstream tasks right either downstream retrieval classification whatever tasks that's perfect right your contrasted learning learns that overlap in the middle is nothing more nothing less all that you need for your task Um, in other words, this is the multiv-view redundancy assumption where the mutual information between X1 and X2, which is what you learn in these alignment based contrasted learning

### [1:15:03](https://www.youtube.com/watch?v=u-H43tRgYJg&t=4503s) · b000093

methods is exactly the information between X1 and Y and also X2 and Y. But why is the task that you care about? Uh this spells trouble which is that what you care about learning important for your downstream task is uh much more than the actual shared information between them. Right? This is trouble because there's not enough signal. Alignment and contrasted learning is going to learn that little bit of overlap over there but it's not enough. You're losing a lot of information important for your task if you do alignment and contrasted learning. So you're in trouble there. And this other setting, you're also in trouble because there's way too much overlap in your data such that contrasted learning and alignment learns too much uh learns too much, learns too much redundant features and is not specific enough uh to be used for the downstream tasks that you care about. So that's when things are just right. There's also extremes when there's not

### [1:15:59](https://www.youtube.com/watch?v=u-H43tRgYJg&t=4559s) · b000094

enough information or too much information and too much noise. People

### [1:16:11](https://www.youtube.com/watch?v=u-H43tRgYJg&t=4571s) · b000095

can also uh people have also shown this in practice which is that you can basically construct synthetic data which overlap in different degrees and also design where the task is and you get some very cool plots like this one over here right uh you start by increasing the information so here there's no overlap on the on the left side the mutual information is zero so two variables are independent they don't overlap and you're slowly starting to increase the overlap between uh x1 and x2 right so they're becoming closer and closer and they overlap more and more at first when they're completely independent they don't overlap and you bring them closer and overlap with each other performance improves right this is the range of going from not enough overlap to getting more and more overlap and finally having a really good uh representation learn from alignment and then if you start making them overlap even more afterwards. That's when you go into this range where there's too much

### [1:17:08](https://www.youtube.com/watch?v=u-H43tRgYJg&t=4628s) · b000096

noise. So you start seeing performance to drop off uh when those representations are used for downstream tasks. Okay. So to really summarize this part um this you know information uh sorry this this multimodal alignment really arise on the assumption that this shared information is what's important. the overlap between them. For example, what is both in the image and also in the caption, it can be formalized by mutual information. Um, which basically means that you know if if that is a representation important for your downstream tasks, then you're golden, right? It learns the mutual information, it helps you learn better representations. Uh, but otherwise, you know, you can be in trouble either because you're learning too much or you're learning too little.

### [1:18:01](https://www.youtube.com/watch?v=u-H43tRgYJg&t=4681s) · b000097

Okay, let me end there for today. We are at time. Um, does yes question&gt;&gt; as in

### [1:18:22](https://www.youtube.com/watch?v=u-H43tRgYJg&t=4702s) · b000098

like you're doing it? That seems like the here.&gt;&gt; Yeah.&gt;&gt; Oh, I think that's a typo. That should say alignment. Sorry. Yeah. Uh, but you I think you're asking a very good broader question which is how does fusion and alignment uh these two concepts interact with each other, right? Um, fusion as we discussed was all about learning one joint representation. alignment is keeping things separate um and and yet align using these similarity functions. Um there are several several things first of all uh for homework two I'm sure some of you have seen a reading assignment there's this paper on a line before a fuse and I'm sure there's also other papers saying fuse before a line and then so one way of thinking about it is what do you do first right do you do you kind of get these data and get features that are aligned so they're semantically

### [1:19:19](https://www.youtube.com/watch?v=u-H43tRgYJg&t=4759s) · b000099

similar they're nearby in embedding space and then do fusion on top of that right that's one very viable alternative or you can also start doing fusion first and then start doing contrastive learning maybe on the fused features. Um, and of course there's also settings which do fusion without alignment and alignment without fusion and vice versa. Um, so I I would say it's it's kind of a I don't have the answer. I think it's a it's open question. Uh there's really pros and cons to each. Sometimes they they both have to be done in the same system. Uh sometimes no.&gt;&gt; You could just take your online

### [1:19:59](https://www.youtube.com/watch?v=u-H43tRgYJg&t=4799s) · b000100

And then&gt;&gt; yes, you could do that as well, right? Uh so you could align your features as we discussed some like over here. Uh you could align your features if it captures the the mutual information really well and your task Y also just so happens to be in that shared space, then alignment is actually a very good training signal for downstream tasks, right? That's why um that's why you know we saw a clip and these clip representations were actually very useful training signal uh because most of the times what I care about in the image is also what somebody would describe in the caption right it's purposely discarding the background and the texture and time of day when these things are just not very important is really just looking at all the people and the objects and the categories. So when that assumption holds it can actually work for very powerful

### [1:20:54](https://www.youtube.com/watch?v=u-H43tRgYJg&t=4854s) · b000101

representations but when it doesn't then you got to do more fusion. Yeah. Yeah. Also this uh and in fact this doesn't really capture anything about synergy right when there's synergy when there's unique information. This is only just looking at the the overlap in information space. is not looking at the other uniqueness and synergy that we also discussed as other possible information sources.&gt;&gt; Yeah. Like for the figure on the right like let's say like when the when they have like excess mutual information but the task only you like only uses a subset of that um like what is a way to like reduce um like to reduce their overlap so that we can use this information in a like in a more efficient way.&gt;&gt; Uh good question.

### [1:21:48](https://www.youtube.com/watch?v=u-H43tRgYJg&t=4908s) · b000102

So one way is to do data augmentation. Um so in fact a lot of these you can check out some of the papers. Uh a lot of these principles are designed a lot of the principles for data augmentation are designed with this. So for example I take an image right and I'm trying to do some classification parts. I know I can rotate it turn into grayscale uh crop it out and drop some pixels. Why why can I do that? All of those augmentations are basically just providing different views of your data, right? And these different views they some information is outside and some is overlapping with the original image and I'm assuming that what is overlapping with the original image is just the object in question right I can make grayscale the object still stays there and some other things over this I can rotate it like using another vend diagram but at the same time it still overlaps with this. We're trying to like focus the data more into the the overlap.&gt;&gt; Right.&gt;&gt; Right. Right.

### [1:22:45](https://www.youtube.com/watch?v=u-H43tRgYJg&t=4965s) · b000103

&gt;&gt; Uh but again, that's not that's that's good intuition, but it's also not easy to do in practice, right? Because sometimes you cannot you don't know what uh what is would would stay in the middle and maybe what also goes too much or too little. Great. All right. Thanks. You're all free to go and
