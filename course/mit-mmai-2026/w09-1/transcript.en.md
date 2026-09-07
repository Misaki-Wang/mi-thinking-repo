# Lecture 9 – Multimodal Reasoning (MIT How to AI Almost Anything/Multimodal AI, Spring 2026)

_English transcript_

- Channel: Paul Liang
- Source: [YouTube](https://www.youtube.com/watch?v=Vhe_bX8mV2s)
- Duration: 1:17:35
- Caption source: automatic
- Status: complete
- Chinese translation: 94/94
- Translation provider: codex
- Generated: 2026-09-07T07:49:34+00:00

## Transcript

### [00:00](https://www.youtube.com/watch?v=Vhe_bX8mV2s&t=0s) · b000001

All right, folks. Welcome back. Hope you had a great spring break. So, uh, one more assignment was released. It is the project midterm report. Uh, the requirements for the project midterm reports are that you should have finalized your idea. You should have uh finalized your data sets and baseline models and ideally already started you know processing your data sets and running baselines. Baselines meaning methods that are prior state-of-the-art methods that's already exist that are precursor to the methods that you are proposing they're hoping to improve upon. You should be running those on your data sets uh before the midterm. You should be colleating those results, numerical results, and also analyzing what works and what doesn't. So doing some error analysis and use that as a way to inform

### [00:57](https://www.youtube.com/watch?v=Vhe_bX8mV2s&t=57s) · b000002

what you're going to do next for your project. Okay, so those are the main requirements for for the midterm report. Um to also clarify what I mean by baselines, I'm sure a lot of you are working on some new data set, some new task, right? A baseline doesn't mean a prior model that was developed for that data set. You can find any data set that no one has trained LLM on LLM training on that data set will not be a new contribution. That would be a baseline. So even if the model itself had never been applied through that data set, it is your job to find what is the most suitable model and apply it to that data set and see how it works and outline it errors and then for the final project to propose something new on top of that existing baseline. Okay. So just because u a method has not been applied to that data set, it doesn't mean it's not a baseline doesn't mean that's new contribution. that has

### [01:54](https://www.youtube.com/watch?v=Vhe_bX8mV2s&t=114s) · b000003

to be something that you kind of get working um for this midterm report. Uh specific logistics and the detailed write up for the assignment has been posted on canvas. I think it was a six-page report. So four pages for the proposal. Now it's six pages. So it's two extra pages for you to detail your results from running these approaches. what early results you're getting and any error analysis and why these existing methods are are not working well. Sounds good. Any questions about the midterm report?

### [02:32](https://www.youtube.com/watch?v=Vhe_bX8mV2s&t=152s) · b000004

&gt;&gt; There's still like each group submit one. Yes, each group submits one on Canvas and I think there's an option to tag your tag your teammates or you can just submit it by yourself and you can share with your teammates the the score and the the feedback. Uh speaking of which, we just released the scores and the feedback for the proposal. Everyone did really well. Everyone got most most people got above 90 or 91. Uh so if you don't see a score on your canvas and if you weren't the one who submitted just ask uh your teammate who submitted for the score and for the feedback.

### [03:10](https://www.youtube.com/watch?v=Vhe_bX8mV2s&t=190s) · b000005

Great. Uh continue meeting with myself and TAs who are in charge of your projects. We're still going to be holding office hours every Tuesday and Thursday to um hear about your progress. Yes.&gt;&gt; Oh yeah. Just another small question about the the term report like if we had some like small like small different ideas from our proposal is that going to be okay like if we like search for more data then we found that like a better data set instead of the original one that we proposed for like the pipeline their core architecture like we kind of modified it.&gt;&gt; Yeah.&gt;&gt; Absolutely.&gt;&gt; Okay. Yeah. Thank you.&gt;&gt; Yeah. If there's any um new ideas, new data sets, new baselines, new topics, it's all okay. I mean, team members might also be slightly different. I don't know who's recently added or dropped the class. So, team members might also change. So, that's all good.&gt;&gt; Thank you so much.&gt;&gt; All right. Um but yeah, I looked through everyone's

### [04:07](https://www.youtube.com/watch?v=Vhe_bX8mV2s&t=247s) · b000006

project proposals. Yeah, all the ideas were great. All very fascinating. uh the only issue as I mentioned was you know most of you are working on some new data set some new tasks and direct application of you know method A to your task B uh that should be the expectation for the midterm report right applying LLM or applying a genic AI or applying multimodal fusion these are baseline they already exist so that should be part of the midterm report um you know apply them see how they work most likely they won't work super well first time off the shelf and that gives you a bottomup way of uh analyzing its errors and identifying what next to do to improve that. We'll come up with something new. Great. Let me also recap the schedule we've seen for the first half. The first half of the class was mostly the foundations. We really covered the basics of multimodal AI, specifically fusion,

### [05:02](https://www.youtube.com/watch?v=Vhe_bX8mV2s&t=302s) · b000007

alignment, representation learning, transformers, generative models. I I really view these as all uh the basic foundations. So, congrats on getting through all of that. Uh, commentator in the midterm, which again, we're not going to release the grades yet because people are doing a makeup midterm this week. Needless to say, don't discuss the midterm with those who haven't done it yet. But from what I've seen, you know, everyone did really well. So, average scores are already high. Um, no thanks to the 10 bonus points, but average score really good. So, congrats. So, that was the first half of the semester, more on these foundations. As a precursor to this second half of the semester, it will mostly be about advanced topics and applications. So starting today and next week, we're going to cover reasoning. So reasoning goes beyond single step prediction or just outputs to methods that can rethink across multiple steps, synthesize information, and build up more complex

### [05:59](https://www.youtube.com/watch?v=Vhe_bX8mV2s&t=359s) · b000008

logical arguments. and and you've seen the great applications of reasoning nowadays for things like math and coding and solving long complicated tasks that is the new frontier of AI. So the next two weeks will be about reasoning. I'll cover some work in RL and the basics of you know using RL to train train the sequence models like language models and this multimodal extensions and then Dimmitri will be covering some work in explainable reasoning and prescriptive reasoning. So prescriptive reasoning not just outputting something but you know outputting actions then actionable goal for people to use alongside confidence intervals and uncertainty predictions so people really know when to trust the model and when not to trust the model. So those next two topics will really be about explanability and trust in reasoning and using that to make real world life decisions. And then after reasoning, I'll cover uh interactive agents. Right? Another huge application

### [06:55](https://www.youtube.com/watch?v=Vhe_bX8mV2s&t=415s) · b000009

of reasoning is to be able to use these models to output multiple sequences of sets uh not just on your computer but can actually be executed, right? Executed like taking actions on the web or taking real robot actions in the real world or to control some physical system like in manufacturing or even in your nuclear nuclear plants. Uh so that will bring the discussion to interaction and agents right a lot of which are are built on top of multimodal systems. We'll cover some of that in week 11 and 12. And then we have an exciting two weeks of these um applicationoriented lectures where where Sunuk will be discussing uh applications of these interactive agents in manufacturing. Right? That's a domain where lots of multimodal data lots of closed loop systems where it makes sense to use agents to automate and improve the optimization or improve the throughput or to reduce uh reduce dangers for example. So in manufacturing and design

### [07:53](https://www.youtube.com/watch?v=Vhe_bX8mV2s&t=473s) · b000010

and Tininoa will discuss some of these applications in more open-ended settings in cities and transportation again an area where there's all sorts of multimodal data from vision to graphs to sensor data to tabular data uh and also all sorts of applications and how do you analyze \[clears throat\] analyze data from a city how do you you know optimize certain throughput measures for a city and so on and finally week 14 I'll come back and discuss some more advanced topics, advanced topics like cross modal transfer, right? Why is it that nowadays you can train a language model and it can directly work well for robotics without ever having seen a robot? How can you take a language model and use it to release smell, analyze smell data and really smell? That's some of the stuff that we're doing. So all this falls into this exciting area called cross model transfer where you can train on one modality and somehow the model magically is able to transfer to some other

### [08:49](https://www.youtube.com/watch?v=Vhe_bX8mV2s&t=529s) · b000011

modality even without training on it. And finally, uh, self-evolving agents. I talked a little bit about this, I think, right before spring break, and a lot of people showed excitement, right? The next frontier of these, uh, reasoning models and agentic models are those that go beyond how humans supervise and how humans design rewards agents that can supervise themselves, propose new tasks for themselves, design reward functions for themselves, and recursively improve over time. And finally, week 15, 12th of May would be your project presentations. Uh, so by then you should have finished your projects. We're going to do a little bit of a poster session in the third floor atrium. uh every team will prepare a poster and it'll be open to obviously everybody else in the class but also general uh members of the MIT community who are interested to see what amazing work all

### [09:46](https://www.youtube.com/watch?v=Vhe_bX8mV2s&t=586s) · b000012

of you are doing. So that will be 12th of May also last day of class and then the midterm reports will be due about a week after that. I have to check when is the last date for assignments. Okay. Uh so no more final just the project midterm report. due I think next week and then the final presentation and report due last week of class and two homeworks homework four and five um these will be one will be a really short homework and one will be a standard homework just to make sure you all have time for the final projects uh we haven't decided which is which one of the homeworks will be about reinforcement learning and reasoning the other homework will be about interactive agents One of them will be much shorter \[clears throat\] than usual maybe one week and the other one will be a standard homework of about two weeks.

### [10:42](https://www.youtube.com/watch?v=Vhe_bX8mV2s&t=642s) · b000013

Great. Any questions about the schedule and topics for the second half of the semester? Some of these are of course inspired by the topics that um people have filled in in the midterm on topics they wanted to see. uh most likely week 14 you'll be you know not a full lecture on one topic but you'll break down like 20 minutes 20 minutes for for different subtopics that are that are of interest to people. Okay. Okay. Jumping into today's lecture. So today's lecture will be about reasoning and reinforcement learning as a way of incentivizing and enabling reasoning in these frontier models. So I'll cover first of all obviously what is reasoning and how reasoning differentiates is different from singlestep prediction and supervised learning and then I'll cover some basics of reinforcement learning culminating in everyone at least having a high level idea of how these modern PO

### [11:38](https://www.youtube.com/watch?v=Vhe_bX8mV2s&t=698s) · b000014

and GRPO methods work for incentivizing LLMs to reason and then we'll extend it to how we can do uh reasoning over different modalities and I'll give some very specific case study from some of our research on building multimodal models that can reason over over multimodal medical data. So first of all uh intuitive definition for reasoning it is to combine knowledge usually through multiple inferential steps that exploits in some way the structure of your problem right so several key words over here uh first of all the idea of combin combining knowledge right across multiple steps right you do a do a math problem for example it's often many different lemas each lema to be combined sequentially or in parallel until you can actually get more informative statements and you finally get to your food, right? If you're doing some of these long or any task that you do, for example, cooking something, you got to follow a sequence

### [12:33](https://www.youtube.com/watch?v=Vhe_bX8mV2s&t=753s) · b000015

of steps in line in order until you finally complete that task. So, reasoning usually involves a series of actions, a series of steps, each perhaps getting more and more complicated and accumulating information from from previous steps. And of course most of the times when you think about reasoning there is some uh structure of the problem that we are exploiting right whether it's a symbolic structure in mathematics whether it is um some other structure in real world robotics tasks there often some sequential or treebased or graphical structure of the problem that we are leveraging. So visually and also how this ties in with the first half of the semester. So we've seen how to represent different modalities, different elements across your modalities. You can fuse them, you can coordinate them using a line representations and so on. Uh we saw how

### [13:29](https://www.youtube.com/watch?v=Vhe_bX8mV2s&t=809s) · b000016

to extend it from one element to a sequence. So we saw all these sort of a line representations. So it could be multiple word that you're typing in context, multiple images that you have as input. And so you have all these local sources of information coming in through time. And reasoning is really all about you know having multiple inferential steps on different aspects of the problem and then combining it systematically in some way to lead to higher order inferences to solve these more difficult tasks.

### [14:02](https://www.youtube.com/watch?v=Vhe_bX8mV2s&t=842s) · b000017

So we think about uh reasoning we often also think about this challenge of compositionality. Compositionality is very similarly defined, right? It's really about how to represent individual elements and how do you combine these elements so that you can lead to more semantically meaningful information in a combination. So uh I think I've shown you some of these examples where you can create these compositional uh compositional data sets where one way of combining data so uh plants surrounding a light bulb is very natural, right? You see this all the time when you look at photos. So in uh these visual language models can recognize this and generate this image very easily. But then you take the same objects and you just combine them in a different way. Right? So a light bulb surrounding some plants. So you have these, you know, these plants inside of a light bulb. This is something that is almost never seen in the real world.

### [14:58](https://www.youtube.com/watch?v=Vhe_bX8mV2s&t=898s) · b000018

Never seen in the real world. And therefore all these DLMs you know if they're trying to do question answering or trying to generate this image uh they fail really terribly. So clip vision language transformers all these multimodal bird models pre-train models they all get close to zero chance zero random chance when trying to to classify these images. So this is a reasoning problem right there's a reasoning problem. It is a problem of how do you get these models to really combine information in the right way where one way of combining it is is super common and is really seen in the world a lot and the other way of combining is super rare and not often seen.

### [15:42](https://www.youtube.com/watch?v=Vhe_bX8mV2s&t=942s) · b000019

&gt;&gt; Uh people have obviously shown this for other examples. If you have a uh astronaut riding a horse, that's kind of rare, but still models can generate it. If you switch it to a horse riding an astronaut, then uh at least in 2022, 2023, these models will not be able to generate that image. So that's a challenge with the model's reasoning capabilities, right? It is not able to combine these two individual logical evidences \[clears throat\] in the right way. Whereas you know for us people this is almost trivial right and of course there's all sorts of examples right pre like 2023 2024 almost every other paper written on LLMs was uh the inability to read them they could not count how many Rs was in the word strawberry they sometimes would struggle with very simple uh mathematical equations like 2 plus 3 if you started

### [16:39](https://www.youtube.com/watch?v=Vhe_bX8mV2s&t=999s) · b000020

prompting it in Chinese instead of English all these really brutal cases of uh models not being able to reason. Uh but then of course came a came a turning point uh with several key works. Um of course unless you've been living under a rock, you probably know and heard of what train of thought prompting is. So that's an example of reasoning, right? You give the model maybe a question and in this case it's a mathematical question requires some reasonable amount of these logical inferences, right? They got to add two numbers together. They got to solve some equations. And they at least got to do a couple of steps of algebra to solve the problem. So if you just do standard prompting, the model gets it wrong. But if you just uh add for example, let's think step by step, then the model start getting it correct, right? With train of thought prompters, right? The model not

### [17:33](https://www.youtube.com/watch?v=Vhe_bX8mV2s&t=1053s) · b000021

only gets it correct, but the model is actually able to explicitly verbalize each step of their thinking, each step of, you know, they have 23 apples, they use 20, so 23 - 20 goes to three, and they bought six more. 3 + 6 equals to 9. So the model is prompted to explicitly verbalize each step of his reasoning which essentially follows this chain sequential structure and that helps the model answer the question correctly.

### [18:10](https://www.youtube.com/watch?v=Vhe_bX8mV2s&t=1090s) · b000022

People have extended train of thought to all sorts of acts of thought. So chain of thought. So consistency chain of thought, tree of thoughts, graph of thoughts and this is really where uh the structure as I mentioned the structure of the problem comes in right certain types of problems it lends itself very well to sequential reasoning. So in math for example we saw previously you know 23 apples minus 20 equals to three that's the first step and then the next step is to add six apples equals to 9. So it's a very linear chain, right? Some problems naturally are are tree based, right? How you reason and how you solve the problem is very tree based, which basically means at some current state, you explore over several states, you start recursing and maybe you reach a dead end, you backtrack, you do all sorts of breath or deferred search. Uh so you do this kind of search, right? So one example is maybe you're playing

### [19:06](https://www.youtube.com/watch?v=Vhe_bX8mV2s&t=1146s) · b000023

Sudoku. uh maybe you're trying to do some crossword all sorts of things whereas some path you have to diverge try different things and have the model numerate and also backtrack and it gets stuck until it finally finds some answer. So that's a another very common type of reasoning. So people have embedded that into language models as well. So tree of thoughts is also a prompting based approach. Right now it's just prompting the model to basically generate the search tree, try out different paths in the search tree when it's stuck, backtrack and recurse on the ones where it's not stuck. So also a simple way of you know embedding reasoning into these models.

### [19:53](https://www.youtube.com/watch?v=Vhe_bX8mV2s&t=1193s) · b000024

These have been extended to to multimodal settings. Uh so this is a paper that I like very much. is called socratic models composing zerosot multimodal reasoning with language and what this model basically does is that it takes all sorts of models right the llm which has some unique reasoning ability it has a vision language model which is able to convert the image into language it has a audio language model which can convert um audio and sounds and caption that in language and it has some you know vision language action model which can take language and outputs actions. So language is the medium right this multimodal setting language is a medium the bottleneck over which reasoning happens and with language as a reasoning medium you can do all sorts of tasks across different modalities for example here's an image captioning example

### [21:02](https://www.youtube.com/watch?v=Vhe_bX8mV2s&t=1262s) · b000025

So you prompted by saying your intelligent bot. You give it some templates. Some of these templates give also include in context examples, right? So you can start applying it to do all sorts of image captioning, identifying people, identifying objects, having open-ended dialogue with this image. Nothing you haven't really seen from from the vision language models we saw in the first half of the semester. But going beyond that, it can also do robotic perception and planning. So now you start getting more into having a model out of multiple sets and taking the executing those steps. So I show this video. So maybe the task is to move move all the blocks to different corners counterclockwise. That's a pretty accurate task. So another generate plan would first break it down into move the green block where move the yellow block where and then move the blue block where

### [21:59](https://www.youtube.com/watch?v=Vhe_bX8mV2s&t=1319s) · b000026

and then it will actually execute each of these steps in sequence. Another example stack of blocks on top of each other. You see other lamb is planning out individual steps to first put the yellow block and then put the blue block on top of it and then put the green block further on top of it and then executing those actions.

### [22:38](https://www.youtube.com/watch?v=Vhe_bX8mV2s&t=1358s) · b000027

and and more, right? So, it's using okay again none of this is really of amps. It's using just the innate ability of your language model to take in that task. For example, you know, a range order of blocks counterclockwise. It takes in the current image and this model is prompted to plan out each of the individual steps that it has to take, right? how we should move the green block, how we should move the yellow block, how we should move the blue block. Right? So that's all your steps over there. And then that is sent to an action model which then outputs in this case is connected to the robot simulator is going to adjust the degrees of freedom on the robot hand uh to actually execute each of those actions in sequence. So that's an example of reasoning. And finally, here's a another example. So now it's going to video video reasoning. So uh I'm going to show you some examples. But at the high level,

### [23:34](https://www.youtube.com/watch?v=Vhe_bX8mV2s&t=1414s) · b000028

what this is going to do is that it's going to parse this scene and it's going to keep track of all the objects in that scene, right? You know that you're watching a TV that you have a remote in your hand. And after a while, you put the remote down. It's going to keep track of a of a state, a memory state of all of the objects and actions. And then maybe after a couple of minutes, you ask the model, where did I put the remote? can find it. It should be able to retrieve that you have put it uh at some particular location from its world state history. So here's the example.

### [24:18](https://www.youtube.com/watch?v=Vhe_bX8mV2s&t=1458s) · b000029

So it's storing at each time the location, the action, the objects, and this can basically be a log of your whole day. Imagine you're wearing a glasses. You can log visually everything that you're doing. And obviously storing vision is very expensive. Storing video is very expensive. So you want to just summarize it into a compact summary. And then you can go back and ask questions like, how much time did I spend doing this and that? Uh where did I put my keys? I might have forgotten them. And you can then start asking questions. So, why did I go to the front porch?

### [24:59](https://www.youtube.com/watch?v=Vhe_bX8mV2s&t=1499s) · b000030

Where did I leave my mouth? Is it going to extract my brain?

### [25:10](https://www.youtube.com/watch?v=Vhe_bX8mV2s&t=1510s) · b000031

\[clears throat\]

### [25:22](https://www.youtube.com/watch?v=Vhe_bX8mV2s&t=1522s) · b000032

So temporal reasoning when did something last happened. You get the idea. It's able to to answer all sorts of questions about about this long context and it's able to do so. Uh sometimes these question are easier just by identifying something. Sometimes they require for example chaining together a sequence of events that are stored in this in this history. So there are many debates surrounding reasoning. Um it is kind of seen as a holy grail of AI, right? Being able to reason, be able to think, being able to do math, being able to take actions over a long sequence like people cans. Really been the holy grail of AI. And uh it's really you know people approaching it from different spectrums right there are some people who believe that reasoning will emerge just from data. You give the model all sorts of examples of theorems being proved and give the model all sorts of examples of

### [26:19](https://www.youtube.com/watch?v=Vhe_bX8mV2s&t=1579s) · b000033

robots moving around and videos of you know robots cleaning or people cleaning the house that all this reasoning would somehow be merged and learned by the model. And then you have people who are uh staunch believers that reasoning has to be top down. It has to be injected into the model. There has to be some symbolic structure. There has to be you know theorem provers. There has to be you know you know world models inside the model so that it can plan within it. So this is the one that goes with more symbolic structure and planning for reasoning. And the other side is more bottom up datadriven. Um I mean obviously most most progress nowadays is here right even though you might think that most progress is here datadriven LMS but in fact we are injecting a lot of structure into these language models it's not pure language model zero shot reasoning nowadays it's

### [27:14](https://www.youtube.com/watch?v=Vhe_bX8mV2s&t=1634s) · b000034

a lot of hybrid symbolic approaches that are slowly making their way into these models right I gave the example of train of thought right chain of thought is an example of injecting some sequential structure in how the language model outputs users dependencies from previous outputs. Right? When chain of thought doesn't work really well, tree of thoughts is a way of embedding search and a classic symbolic AI algorithm search into the output of language models. So it seems data driven but you know on the output side of the models and on the training side you will see that there's a lot of ways where whereby structure is injected to enable reasoning. Of course, I'm also not saying it has to be fully structured. Obviously, no one does this anymore, but you're still going to use, you know, MLMs and multimodal models as key components in today's reasoning systems. So, what are some of the main decisions

### [28:11](https://www.youtube.com/watch?v=Vhe_bX8mV2s&t=1691s) · b000035

that we have to make in order to enable AI to reason? Well, one big thing is uh differentiability, right? You're going to see this a lot when you look at paper says that AI reason, right? By definition, reasoning is symbolic. It's discrete, right? is a discrete number of steps. Each step is a discrete number of actions. If I want to search over all these possible steps and actions, this by nature is very discreet, right? Uh that makes it not super compatible sometimes with your AI models because in AI models, sorry, in deep learning, you often need differentiability, right? You need differentiable forward passes so that you can back propagate and update gradients. So that will be a big point of contention. You read a lot of stuff that start with some reasoning structure that is partly symbolic not differentiable and to make some relaxations to make it differentiable so it's compatible with deep learning. Another uh key thing which follows a

### [29:08](https://www.youtube.com/watch?v=Vhe_bX8mV2s&t=1748s) · b000036

little bit on the first one is in the concepts right the concepts that you use to reason over are they discrete or continuous right discrete gives interpretability it gives a small set of possibilities but it's not differentiable often times there is a need for continuous relaxations and finally what is the best m mix of knowledge and data which part should be learned by the model and which part should be injected by human expert knowledge

### [29:39](https://www.youtube.com/watch?v=Vhe_bX8mV2s&t=1779s) · b000037

And there's many implications, right? There's many implications based on all these decisions on the model that you end up training. How intercredible it is, how robust is it, how efficient it is, how many samples it needs to achieve performance. So that's a precursor example. So now let's jump deep into reasoning and specifically the sub challenges of reasoning. So I like to think of any problem as kind of having these perpendicular dimensions right perpendicular dimensions that break down the problem to into each of these sub problems. So one very important sub problem as I motivated in reasoning is the structure of the problem. Is it a single step identification? So most people maybe refer to this as perception. Is there a person perceiving something? And then you have things like you know temporal or sequential like your train of thought style you have

### [30:35](https://www.youtube.com/watch?v=Vhe_bX8mV2s&t=1835s) · b000038

hierarchical you have these trees or tree of thought search and you also have interactive problems where it's not just enough to to search and then finish by searching maybe changes the state taking action changes the state and you have to repeat multiple times in that environment. So that's what we we termed as interactive concepts. Concepts are you know we break down reasoning into individual steps right each step how do you parameterize the information right are these in words so nowadays when you do LLM reasoning most of the reasoning is done with word as a concept each word is a is a concept that you're reasoning over when you do reasoning over other modalities it may or may not be words it could be latent representations it can be attention maps it can be bounding boxes other basic concepts in reasoning.

### [31:32](https://www.youtube.com/watch?v=Vhe_bX8mV2s&t=1892s) · b000039

Inference tells you how to combine concepts, right? So a lot of these uh can be the if then relationships. If A happens then b. So that if then is a relation, right? Uh and and ors are also possible relations when you're trying to combine information. So when proving something lema one is true and lema two is true or lema one is true or lema two is true. So these are ways of combining concepts and finally a big sub challenge is how to inject the knowledge right what kind of knowledge there usually has to be some human expert who is um defining all of these so not going to cover everything we have the survey paper which covers everything but we're not going to cover everything in class we're going to focus more on really what is I guess state-of-the-art today which is to mostly use language as a medium for reasoning, right? Using the

### [32:28](https://www.youtube.com/watch?v=Vhe_bX8mV2s&t=1948s) · b000040

power of pre-training LLMs. But then the question becomes, how do you incentivize and train these multimodal LLMs to reason uh in an accurate and robust manner?

### [32:44](https://www.youtube.com/watch?v=Vhe_bX8mV2s&t=1964s) · b000041

So the setup usually looks like this. Input can be uh you know text prompt perhaps also with images, videos, any other modalities and this input obviously would also include the question which um necessitates necessitates reasoning right so it's a maybe a hard question and reasoning usually as you've seen is across all of these step one two three uh step one two and three and so on right multiple steps and after the model has reasoned sufficiently over uh number of steps it is happy with it will stop reasoning and it will output some final answer. So this uh can be thought of as a general schematic. What is important could be just a final output. For example, we have lots of calculations in math and just one final answer. But sometimes we also want to score the quality of the intermediate reasoning as well.

### [33:38](https://www.youtube.com/watch?v=Vhe_bX8mV2s&t=2018s) · b000042

Method one as we've seen is just direct right? If you will just give us the input things like think step by step or think methodically or you give us part of the input some in context examples of the model doing this uh step-by-step reasoning then you don't really have to change the model. You don't have to change its parameters. You don't have to train it any further and the model will still do reasonably well. Right? So this is all your stuff like various prompting based chain or any thought based prompting approaches. Method two is what we call supervised fine tuning. Supervised fine-tuning basically assumes that you're going to collect some data set that has not just input output examples without the reasoning but data examples of input reasoning steps output right. So you get full supervision when data set with full supervision over what reasoning. So in

### [34:33](https://www.youtube.com/watch?v=Vhe_bX8mV2s&t=2073s) · b000043

the case of math maybe you will just get you know examples of of well annotated workings of how each step should reason in the case of robotics would maybe have the prompt where you're moving the blocks counterclockwise and you would have real annotations of where each block should be placed as the reasoning steps. \[snorts\] So if you're able to curate such a data data set uh basically meaning assuming you have these reasoning traces then you can do a supervised fine-tuning which basically means you're training your model to auto regressively predict given the input not just the output but also each step in the reasoning right so fairly straightforward uh there's a trade-off of course depending on how large this data set you collect with the reasoning traces if it's zero zero then you're just doing direct prompting. If it's small like five or 10 then you would do kind of in context learning where you just give examples as the inputs and if it's

### [35:30](https://www.youtube.com/watch?v=Vhe_bX8mV2s&t=2130s) · b000044

larger then you'll probably update the model using Laura and do supervised functioning right the classic uh training of LLMs just treating the reasoning as the target of course the interesting thing happens when you don't have such a data set or where it's very expensive to get all of these reading traits need so you only have inut output pairs very difficult to get the reasoning traces. How do you still get the model to get better at doing this intermediate reasoning before giving the output? So that's where reinforcement learning comes in and that will be today's focus. Right? Reinforcement learning is a way of training these models even without these intermediate reasoning sets given only perhaps the output or as you see what we mean a reward function scoring the quality of the reasoning and the outputs using that as a signal to train

### [36:26](https://www.youtube.com/watch?v=Vhe_bX8mV2s&t=2186s) · b000045

a model to automatically infer what these reasoning steps are. Right? Often times just having the output is easy. A reward function is often also easy. Right? reward function could be uh does the does a theorem type check right or does a theorem pass a theorem verifier that is much easier to evaluate rather than actually writing out the theorem uh in code it could be does the model does the code that you write pass the test cases so what percentage of the test cases does it pass really easy to evaluate and therefore define a reward for all sorts of code that a model may have written but it is very difficult to write the code itself often times this reward function or as we call it verifier is much more accessible than actual uh actual ground truth reasoning. Okay, any questions about uh this setup before we dive into the details?

### [37:27](https://www.youtube.com/watch?v=Vhe_bX8mV2s&t=2247s) · b000046

\[clears throat\]

### [37:35](https://www.youtube.com/watch?v=Vhe_bX8mV2s&t=2255s) · b000047

All right, great. So, we'll discuss reinforcement learning. Uh, a topic which is which always been useful, right? You know, key area of AI, key area of computer science, uh, but really blown up in popularity over, you know, 2025 and 2026 because of its implications and use in training language models. So in reinforcement learning uh the basic setup is this right? We think about it as an agent in some environment right agent can be thought of as taking a bunch of possible states in the environment. Uh sorry let me go to here. So uh agent can be thought of as you know being in a potential number of states in the environment right usually we think of these environments as some of these like grid world environments where the agent is maybe some character

### [38:31](https://www.youtube.com/watch?v=Vhe_bX8mV2s&t=2311s) · b000048

that's moving up down left right so the states will just be different locations in that environment right one one two two one two2 different locations actions are just different things that the agent could do it could move up down left right and so on transition functions basically Say if the model is in some state and it takes some action what next state would it go into right most of the times that's deterministic if it's going forward go forward one step but sometimes there might be some randomness involved in the transition so that's a transition function the reward function is very important basically says you know when the uh agent is in some state takes some action and goes to some next state what reward would it get you think about it as some some parts in this math have a negative reward because they fall into a hole and some parts of the map have positive reward because they get some diamond. Right? So that's a reward

### [39:29](https://www.youtube.com/watch?v=Vhe_bX8mV2s&t=2369s) · b000049

function and there's some state which a model starts in and some discount factor and horizon. These are not super important but you can think about this as basically constraints on how long the agent would interact with the environment total. So it wouldn't really go on forever. So we sometimes draw it as this, right? agent takes some action in the environment and it goes to some new state and it gets some reward as a result of taking that action and this happens across multiple steps. There are some important things that we care about in reinforcement learning, right? The most important thing is what we call this reward or return. A return basically means, you know, when I'm taking an action right now, what is the immediate reward that I get, right? That's R and T plus one, right? At the next time step, but more importantly, what are also future rewards I might get? Is it the long-term rewards that I really care about? Sometimes you might

### [40:26](https://www.youtube.com/watch?v=Vhe_bX8mV2s&t=2426s) · b000050

have to sacrifice some reward in the short term to get more rewards in the long term. Sometimes you don't care about it. Sometimes you want big amounts of reward in the short term and you don't care about the long term. There's various trade-offs, various trade-offs and whether you want short-term rewards or long-term reward. We want to have some definition of you know maximizing long-term rewards, right? And then a policy is another very key aspect. Policy basically tells the agent how to act. How to act is basically a distribution where given any state what action I should take right so it's a distribution over next states a next actions given particular states we usually refer to the policy as time and your goal is to find the policy which basically maximizes your return overall different ways of acting over all different actions that you could take which is the one that would lead to not just immediate reward maximize in

### [41:23](https://www.youtube.com/watch?v=Vhe_bX8mV2s&t=2483s) · b000051

the short term term but long term the reward also being mass. You can think of the analogy to your language models, right? In this case, the states are basically words, right? Context, things that the model has interacted with you so far. That's your current state. Actions are basically different tokens that you can generate, right? Policy is basically the response, right? Over all the actions, all the words that a model could generate, what is the right sequence of words that it should generate? And the return is ideally long-term not just to make you happy to pursue you in the one response but to actually lead to some meaningful interaction and lead to some meaningful outcome in the long term. So you can think about this as a context of LLMs and almost any any problem can be thought of using this setup.

### [42:17](https://www.youtube.com/watch?v=Vhe_bX8mV2s&t=2537s) · b000052

Of course uh there's some distinction between RL and supervised learning. I think it's quite obvious, right? RL cares about uh making decisions over a sequence not just focusing on the immediate reward uh one prediction but over multiple predictions but multiple words multiple responses that the model has to generate. Uh thereby you care about maximizing some cumulative reward. Uh sometimes the rewards are very sparse. Sometimes the model interacts with the user over multiple turns before the user is asked to rate whether they liked or disliked the conversation. So the rewards can be very fast and as you'll see that's a big challenge with RL and there's several challenges. Uh one quick thing is that there's actually a intersection between RL and supervised learning which is called imitation learning. So that's you can think about that as the first RL algorithm imitation learning and that's also used to train a lot of models

### [43:15](https://www.youtube.com/watch?v=Vhe_bX8mV2s&t=2595s) · b000053

today. What application learning basically mean as let's say I care about learning some policy right which means uh given some state what actions to take in fact I'm going to make it more concrete so I use the example of a self-driving car that's also an example of reinforcement learning so the state could be whatever the car sees in the image actions could be like how to turn the wheel whether to accelerate or decelerate and so on so what's a easy way of training this right well but One way is to just get human drivers to give you data, right? Put a dash cam and all the drivers assume they're driving well. So you can basically see, you know, the sequence of uh driving scenarios that real human experts go through and you can also log where they turn their wheel, how much they accelerated, decelerated. So you get a sequence of state action trajectories from the expert, right? for every state as zero

### [44:11](https://www.youtube.com/watch?v=Vhe_bX8mV2s&t=2651s) · b000054

what action they took next state next action next state next action as well. Uh and then you can basically train this assuming this is a data set just train it as supervised learning which basically means pair it up into data sets as zero. The first action is a ground truth. Right? Here's what the human driver did when they saw this. Here's what the human driver did when they saw this. Put this data set and train a model. Right? If you do this, you're most likely going to train a pretty good model. You be able to train a pretty good model that imitates how human drivers run. But the big danger is when you start straying away from the sequence of demonstrations that the human experts see. If you just even go a little bit, maybe you veer a little bit towards the sidewalk. If you've never seen how human drivers recover from going onto the sidewalk and coming back, then you're basically in this setting where your

### [45:08](https://www.youtube.com/watch?v=Vhe_bX8mV2s&t=2708s) · b000055

model has never seen how, you know, what distribution it is and it could do all sorts of very dangerous actions, right? they could further keep driving on the sidewalk or you could start driving to people's houses. It was never seen examples of how human experts recover. So imitation learning basically is good uh if you're confident the model will stay in the exact same distributions as the expert trajectories, but once it starts veering off course, you have no guarantees of how you'll recover. So never really works in safety critical situations fully but often very useful to initialize your model. I mean you see this analogy with language models today right which is that pre-training can be thought of well pre-training would be just training of internet data instruction tuning right the second stage instruction tuning instruction fine-tuning can be thought of as imitation learning right where you get humans to annotate what questions

### [46:05](https://www.youtube.com/watch?v=Vhe_bX8mV2s&t=2765s) · b000056

they expect the model to answer and how they would answer the question so that's your states and actions and then you just imitate right you train a model on these human annotated instructions and expert completions. So that was the second stage of training. And then as we'll see, we now have a third stage which is to use reinforcement learning to further fine-tune the model and steer the model towards settings where it may not have seen uh in instruction tuning or imitation learning. So you must think of it as a third stage.

### [46:41](https://www.youtube.com/watch?v=Vhe_bX8mV2s&t=2801s) · b000057

Any questions so far about the differences between supervised learning, reinforcement learning, and this imitation learning, which is kind of a mix of

### [47:11](https://www.youtube.com/watch?v=Vhe_bX8mV2s&t=2831s) · b000058

Okay. So I'm going to just explain one arrow algorithm uh the simplest one. The simplest one also turns out to be what is enough for for you know training LLMs. And I'm going to explain it using this example uh this pong example just to give you more examples of you know RL settings. So in this case the states are you know there's this game board which is visible and the model is controlling one of these paddles right maybe the human is controlling the other one. So the actions are very simple. Just move up and down. Move up and down. And the reward is one if you are able to successfully shoot the ball over your opponent's paddle and negative one if the opponent uh shoots their ball over across your paddle. Right? So states, actions, rewards, you know, that's first thing you want to think about when you want to frame something as a as a

### [48:09](https://www.youtube.com/watch?v=Vhe_bX8mV2s&t=2889s) · b000059

reinforcement learning problem. Most of the time it's quite straightforward. So let's say you want to train a train a model for this. So ideally maybe you would just start by defining some neuronet right it takes in a state which is this this vision this this image of the of the game board right 32 by 32 that goes some input layer maybe a CNN whatever and it outputs something. What should it output? Well, because we want to train this AI model to play the game and so it should output the actions, right? So you can think about this neuronet network as the policy model pi that takes in states and outputs actions. In this case, action is just up or down. Binary classification, which also means that you can just have one neuron that outputs some probability of up down is just one minus that. Okay. Um, and the network as we mentioned the

### [49:06](https://www.youtube.com/watch?v=Vhe_bX8mV2s&t=2946s) · b000060

reward is that it sees a plus one if it scored a point against the opponent and minus one if the opponent scored a point against you. So how do we train a model? So again go back to the idea of imitation learning. Let's say you had for example an expert that told you at every state the annotated for you whether they move up or down. Right? This is probably very hard to get. it will never cover all states because it's all possible configurations of where is where paddles are. So it's going to be pretty hard. But if you had such a model, you would just do binary classification, right? Given the states in those expert trajectories, can you output what the action is? And that basically means maximize the log probabilities of predicting that particular uh label yi action yi given x i. So that's basically your your uh maximizing your lock likelihood binary cross entropy.

### [50:03](https://www.youtube.com/watch?v=Vhe_bX8mV2s&t=3003s) · b000061

So but however we don't have uh these actual trajectories right so what do we do so in RL a key aspect is what we call exploration exploration basically means you know if I don't know what the expert should do right there's no trained signal what I can do is I can just do trial and error I can just try out various things in the environment and just hope for the best sometimes I might be lucky I get some positive rewards Sometimes I may be unlucky, I get negative rewards, but I'm going to just try different things, hope for the best, and see what it gives me and maybe use that to learn. So I might just run according to the current policy. It's a random policy at the beginning. So it's basically just random actions. Sometimes you are lucky and you win and sometimes over a sequence of actions you are unlucky and you lose, right? I purposely annotate, you know, four actions before

### [51:00](https://www.youtube.com/watch?v=Vhe_bX8mV2s&t=3060s) · b000062

you win and lose because as you've seen from most of these these problems, you're going to take a bunch of actions before you observe a reward. You have this sparse reward problem. In this case, you might have to move the paddle a couple of times until you either see the ball go over and you get a plus one and you have the ball come over to your side and you get a negative one. So, some sequences you win, some sequences you lose. So then a very straightforward thing to do is that I'm just going to assume all the actions that I did in the sequence of actions leading to me winning were good, right? I mean after all I won, right? I I won at the end. So I'm just going to assume all of those actions were good. So I'm going to maximize the log prop of all the actions in that sequence, all four actions in that sequence because I wanted them. And I'm going to assume for all the other sequences where I lost

### [51:58](https://www.youtube.com/watch?v=Vhe_bX8mV2s&t=3118s) · b000063

all of the actions in those sequence were bad. Right? So I'll minimize the log prob or otherwise maximize negative one times the lock prob for the actions of those actions in those. And this is a big assumption. It's a big assumption because in the end you know this might be a very long sequence of actions right? You don't actually know which action here contributed to you winning or losing. So assigning the equal credit equal either winning credits or equal losing credit to each of those actions is a very strong but we'll see actually works in practice. So in a general case you can think about it as you know you take a bunch of actions you start by exploring your environments some sequence of actions are good and you win some are bad and you lose and regardless of what you do you're maximizing your lock probability scaled by the reward r right uh reward r

### [52:54](https://www.youtube.com/watch?v=Vhe_bX8mV2s&t=3174s) · b000064

so in the winning case the reward is plus one and the losing case the reward was negative one here's a general general way of optimizing this model and in fact that is a classic reinforcement learning algorithm. It is called the reinforce algorithm and this is basically the algorithm but I kind of gave you the intuition behind it which is that you have some policy model pi in this case it was a neuron net some states output some actions uh and then you just keep iterating right you just generate a random episode which basically means you know that sequence of up down actions and you wait until you get a reward R and you're basically updating your model with the gradient of the log probabilities scaled by the reward. In this case, the reward

### [53:50](https://www.youtube.com/watch?v=Vhe_bX8mV2s&t=3230s) · b000065

notation was G. So the exact same argument is possibly 4,000. One thing I want to highlight here before kind of giving intuition for why it works is this idea, right? So how do you decide what actions to take? I said at the beginning that you know when you don't know what to do when uh the experts aren't given to you you just want the model to explore right you just randomly take all sorts of actions and hope for the best some sequence of actions lead you to high reward and you'll increase the lock props of those actions some sequence of actions lead to low reward and you minimize the lock probability of those actions right so to start you're going to explore but after as you're training a model the model gets better and better right the model gets better and better which basically means your your your pie your policy model is going to increasingly decide to take good actions that have high rewards instead of bad actions. So you don't

### [54:47](https://www.youtube.com/watch?v=Vhe_bX8mV2s&t=3287s) · b000066

want to explore too much anymore and then you want to instead follow what your model is outputting as actions for each of the states. Right? So that's a very key concept in reinforcement learning. It is this exploration and exploitation trade-off. Right? When your model isn't good, you want to incentivize the model to explore. so that it sees all different cases and hope for the best and some positive reward will come. When you get increasingly confident that your model becomes better, you want to exploit exploit what the model is giving you as the actions instead of exploring too much. Uh so this is formalizing this epsilon greedy thing which basically means that you start with a higher exploration factor with probability one right you start exploring and then eventually you go down with probability epsilon you start exploring and you instead follow your model.

### [55:42](https://www.youtube.com/watch?v=Vhe_bX8mV2s&t=3342s) · b000067

So the intuition behind these policy gradients is again this equation. um if the reward is high, I'm going to increase the probability of the actions that I see. And if the reward is low or the reward is negative, I'm going to decrease the probability of the actions that I took. Right? The intuition is that even though there's a very very long sequence of actions that may have happened before you see the reward in expectation the average reward for each of those actions is basically just the final reward divided by um by the length of the sequence. So in expectation it is going to just incentivize you know the good actions and it would penalize the poor actions.

### [56:33](https://www.youtube.com/watch?v=Vhe_bX8mV2s&t=3393s) · b000068

Uh any questions? Okay. So, one downside of these policy gradients uh is this idea that a raw rewards may not be super meaningful, right? Sometimes the rewards may all be positive because your game by definition just always give positive rewards. Sometimes your rewards are all negative because by definition your game just always give negative rewards. So the raw rewards are not super important. Uh what is important is how the rewards change relative to some baseline over time. So people find that one very critical thing to get these methods to work is to wait not just by the reward but the reward minus some baseline reward. You think about the baseline as some rolling average or exponential moving average of the rewards that you have seen so far,

### [57:30](https://www.youtube.com/watch?v=Vhe_bX8mV2s&t=3450s) · b000069

right? And then this difference is just whether compared to this baseline, my current reward is better or the current reward is worse. So now this basically helps you scale all your rewards to something that is on average zero and it's just slightly positive and slightly negative.

### [57:57](https://www.youtube.com/watch?v=Vhe_bX8mV2s&t=3477s) · b000070

Okay, we're almost there. So this is essentially what is being done in a lot of these LLMs. Uh so to see how this applies \[clears throat\] to LLM. So again step zero you will pre-train your LLM using using you know just unsupervised data and then in step two you would sorry you will first pre-train LLM with all sorts of unlabelled data and then you will do supervised fine tuning using instruction data and then you will have this stage three right this we're talking I'm talking about this stage three which is this post training some people call it post training which is that you would um give the model some prompts and then ask the LLM to basically generate using its current policy different sequence of words. So maybe the first thing I was doing is this up down in the palm but you can think about it as words in some response and then it might be another set of words in some response another

### [58:55](https://www.youtube.com/watch?v=Vhe_bX8mV2s&t=3535s) · b000071

sequence of words in a third response right so you're basically sampling multiple responses from your model uh humans would rank this by some quality right so it gives some reward to these sometimes it's you know just reward for each response sometimes it's a pair-wise ranking but with pair wise ranking you can basically recover the rewards for each sequence. Um that gives you a limited number of rewards which means that sometimes it's useful to train a reward model which basically means if a person has annotated these 10 responses to these 10 rewards just train a model that maps these 10 responses to those 10 results. Right? is just a classification problem which means that this reward model can then be applied to future responses and predict the risk rewards for those future responses. That's the intuitive idea behind a reward model. And then once you have the reward model, you can just use RL which

### [59:52](https://www.youtube.com/watch?v=Vhe_bX8mV2s&t=3592s) · b000072

is the policy gradient method that I showed which is to basically update the model increase the lock probabilities scaled by positive rewards or decrease the lock probabilities of the actions scale by negative rewards. Right? That would be used to do this stage three post-training of the model or some people call it reinforcement learning fine tuning of the model to maximize these rewards. Any questions about this quiet group today?

### [1:00:31](https://www.youtube.com/watch?v=Vhe_bX8mV2s&t=3631s) · b000073

Are people confused or lost? Too easy? Too hard? Okay. Uh several several key things that are good to know, right? Um this is the part where I was showing the reward model, which is that you have a bunch of prompts and then the human might score the rewards for some of them, right? Maybe humans would say this response is really good or this way of answering a question is bad and so on. Uh but that is not generalizable and that data set is often small. The reward model is basically it's a another neuronet network that takes in the the text and tries to predict what the human annotated rewards were. Right? So this reward model can then be used to label the rewards or other prompts and other responses that you get. So this makes it more generalizable. And of course you can also see how this is more generalizable than your supervised earning, right? Because in

### [1:01:27](https://www.youtube.com/watch?v=Vhe_bX8mV2s&t=3687s) · b000074

supervised learning all you get is the person annotating a couple of completions. Now you can get the model to reward not just that completion that the person wrote but any possible combination of uh of completions that anybody or any model generated. So this is why people sometimes say that uh instruction fine-tuning causes the model to sometimes memorize memorize how people conceive it the us but in reinforcement learning the model can truly generalize. It can assign rewards to other ways of solving the task which makes the model more adept at maybe finding other solutions that may also have high rewards or solutions that uh people didn't provide to the model which are also alternative solutions.

### [1:02:20](https://www.youtube.com/watch?v=Vhe_bX8mV2s&t=3740s) · b000075

Uh this part I mentioned as well. Sometimes it's much easier to have people compare whether one response is better than the other than to give objective numbers as the reward to each model. Right? This eight versus 1.2 is hard to assign, but it's clear that that is better than this. Uh you can take ranking data as a reward and convert it into the raw rewards.

### [1:02:52](https://www.youtube.com/watch?v=Vhe_bX8mV2s&t=3772s) · b000076

Okay. And I won't go into uh too much detail about this but that is basically the idea behind relevant things GPPO GRPO approaches which are state-of-the-art all of them are just based on the idea of this policy optimization right you have your Q which is your prompt your policy model is your language model you're going to sample a bunch of responses from the language model a group of responses that's the group hyperparameter in gpo for each of the uh responses the model is going to go through a reward model to predict what are the rewards R1 through RG let's say G rewards this reference model I'll say a little bit about it it is where the uh P in pol stands for proximal policy optimization policy optimization is the algorithm

### [1:03:47](https://www.youtube.com/watch?v=Vhe_bX8mV2s&t=3827s) · b000077

that we discussed the proximal term is basically you think of the reference model as a copy of the model's parameters in the previous step. And this KL basically means I don't want the new update to the model to be too different from the weights of the previous model. So I'm going to add a KL term between the new model and a frozen copy of the model from the previous step. So it doesn't change too much, right? We've already pre-trained a very good model. These things should only just be fine-tuning the model a little bit instead of changing the model too much. So that's a reference model and a KL. So a bunch of rewards. The bunch of rewards are used to estimate these A's. These A's are what we call advantages which I covered over here. Um as I emphasize sometimes the raw rewards aren't very useful right because the raw rewards themselves can

### [1:04:43](https://www.youtube.com/watch?v=Vhe_bX8mV2s&t=3883s) · b000078

always be positive or can always be negative. So it always makes sense to subtract a baseline which is the exponential moving average of the rewards that you have seen over time. It's basically standardizing them to be zero mean and kind of variance variance around zero. So some people use the advantage to refer to the reward minus the exponential moving average tracking of the baseline reward.

### [1:05:14](https://www.youtube.com/watch?v=Vhe_bX8mV2s&t=3914s) · b000079

So there are those advantages and then the advantages are used to scale the log likelihoods and to update the policy model. Okay. So that's the uh that's GRP algorithm. Any question about this?

### [1:05:47](https://www.youtube.com/watch?v=Vhe_bX8mV2s&t=3947s) · b000080

uh just want to end with some some interesting quotes. Obviously when when when IB R1 came out everyone was losing their minds but uh people who have been doing RL for a long time came out and said yeah you know the reason why no one has tried GRPO before is uh we have in reinforce which is the algorithm the most simple version of the algorithm we derived right in reinforce you update the policy by subtracting a baseline right reward minus baseline which is typically the average reward from several trajectories to reduce the variance. Now in fact theory shows us that the ideal baseline is the total expected future reward from a state often called the value. I didn't get into this but you can read into it. Using a value function as the baseline is known as actor critic. PO is a stable version of that. So PO as we discussed P

### [1:06:43](https://www.youtube.com/watch?v=Vhe_bX8mV2s&t=4003s) · b000081

proximal policy optimization proximal is the one that has the KL term. So the model update doesn't differ too much from the previous frozen copy of the model weights. So in traditional reinforce the baseline can be any function of the current state and traditionally it's just a reward for the trajectories in a single batch. Right? So that's the baseline rewards across your batch. In GRPO this baseline is computed over thousand samples generated for each prompt which is novel. So a lot of it is um these kind of age-old ideas that have been around in in reinforcement learning that uh nowadays apply to language models which is nice, right? Which means that you know all of these thousands and thousands of papers uh building upon these RL reasoning or usually minor modifications from the traditional RL literature. um which is kind of one way

### [1:07:41](https://www.youtube.com/watch?v=Vhe_bX8mV2s&t=4061s) · b000082

of cable climbing the research.

### [1:07:53](https://www.youtube.com/watch?v=Vhe_bX8mV2s&t=4073s) · b000083

Okay, let me go into some application. Um there was a feedback there was some feedback of maybe a lectur at some points being a bit too algorithmic and wanting to see more applications. So show you one example of how we have been recently applying this um you know GRPO and using RL to train multimodal LLMs to train a clinical reasoning foundation model. So ideally what we wanted you know we started out to do this project what we wanted the model to do was to synthesize all of this medical data. So as uh we remember Dimmitri pointed out right there's you know sensors like ECG medical sensors there's all sorts of images all sorts of text historical patient and doctor conversations and clinical records and nowadays with the

### [1:08:49](https://www.youtube.com/watch?v=Vhe_bX8mV2s&t=4129s) · b000084

power of these uh these models you can not just make a prediction about the disease but you can also do things like have the model explain right in reasoning why it is this disease and rule out disability diseases and to uh explain that here are some ways of you know treating or diagnosing the patient. You can also have the model highlight regions. So now it's reasoning not just in text but also reasoning in vision. So for example highlighting some part of the X-ray or highlighting some part of the pathology, right? With small bounding boxes showing the tumor, right? This can help doctors verify the presence of maybe a a tumor. Um and it can also help you know converse with the doctor and patient to do diagnosis. So that's what we wanted the model to do. The base model nothing really special. Text can go through directly into the tokenizer. Vision can be encoded using a vision encoder and then

### [1:09:45](https://www.youtube.com/watch?v=Vhe_bX8mV2s&t=4185s) · b000085

adapted using a projection layer into the model. And likewise for any of your time series and sensing data that can go through some encoder and then get projected using an adapter into your uh LLM. Right? So the this multimodal LLM is the backbone. So several things first of all where we get the data and how do we use RL to train this multimodal model. uh data wise my my student David did a lot of hard work in curating some extremely large data sets I think I covered this in the first second week of class as we're going through data sets but this is a huge multimodal clinical data set covering all the modalities that I showed previously uh in all sorts of uh conditions clinical conditions uh but one important key note is that it has the input modalities right sensing

### [1:10:42](https://www.youtube.com/watch?v=Vhe_bX8mV2s&t=4242s) · b000086

steps and imaging and it has the final diagnosis. So whether the person has COVID or pneumonia or cancer uh but it doesn't have a reason doesn't have the step-by-step reasoning. So that's why you want to train a model to output. So how we train a model? First part was you know some stuff you had to do which was the multimodal training. In this case time series was causing us some problems. So we had to fine-tune these time series encoders to get them to be better and then inject them into the other lens using some adapter. And then the second part which is the key that I'll focus on was how we train this model for reasoning. So as we discussed in reasoning the big step is to define the rewards define both reward functions because you only have the input and the output. you don't have these

### [1:11:38](https://www.youtube.com/watch?v=Vhe_bX8mV2s&t=4298s) · b000087

intermediate reasoning places. How you end up incentivizing a model to get the reasoning out is to you find good reward functions. So the reward function should be high for good reasoning examples and the reward function should be low for bad reasoning examples. Right? Then when you start using RL, the model would maximize the reward and ideally give out good reasoning examples corresponding to high reward. So there were some rewards that we're building upon and some uh new rewards that we um we also developed. One reward that is very common is the accuracy of the alpha. Right? So the model is going to reason and then upput the answer. You have the label for the answer. Right? In this case the answer is like tumor or no tumor. So obviously the model should get the answer correct. The model get the answer wrong. It's probably reasoning was wrong. So the accuracy reward is just one if the final answer was correct and zero if the model got the answer

### [1:12:34](https://www.youtube.com/watch?v=Vhe_bX8mV2s&t=4354s) · b000088

wrong. Pretty simple. Uh because we are working in the multimodal setting, we also define a semantic alignment reward. So the model will be outputting some text description of the reasoning and also sporadically pointing to the image via some bounding box. So you want a semantic alignment between the reasoning in text and the visual bounding box that the model was highlighting. Right? So this can be measured as the um uh IOU intersection over union between the ground truth uh segmented part of the image and where the model predicted the bounding box to be uh inside the image. So you can think about this as a as a visual reward incentivized visual reason. And then another reward that we had was length. So sometimes you want these models to uh to actually say something like pretty at a length that was useful. So we gave the reward of up to one of

### [1:13:32](https://www.youtube.com/watch?v=Vhe_bX8mV2s&t=4412s) · b000089

the models reasoning is at least 100 tokens uh but no more if it's longer, right? So you don't want the model to um give too long reasoning as well. And a bunch of people really play around with this. A lot of people study how do you incentivize the model to reason at the right number of steps and not too long or not too short. Bunch of work gone into designing those rewards. And finally we scaled each of these 0.6 for the accuracy reward 2 for the visual uh bounding box reward and 2 for the length reward.

### [1:14:14](https://www.youtube.com/watch?v=Vhe_bX8mV2s&t=4454s) · b000090

&gt;&gt; \[clears throat\]&gt;&gt; So yes, so then we trained it and there's some other minor details in the paper which I don't get into but you can see what the model is able to output. So it's able to take an image and so only this and the answer like you know past tumor is given to the model for training right all of this is automatically inferred as reasoning by the model. So the model is able to say well first the model is able to draw the bounding box around the tumor and then also explain that the tumor appears as a round or well circumscribed lesion. Tumors are often characterized as having these these boundaries which are distinct from the surrounding brain tissue. So the model is able to do all this explanation and also highlight the part of the X-ray which is very suspicious. So that's good. Here's another example. Uh now the model is taking in both X-ray and I think

### [1:15:11](https://www.youtube.com/watch?v=Vhe_bX8mV2s&t=4511s) · b000091

these are some of these ICU sensing readings and a model is able to identify that the patient has been on mechanical ventilation for 96 hours. It's able to infer that from from some of the time series readings very surprising uh which is a quite long condition indicating a complex respiratory condition. The ECG and other lab results do not show any immediate critical issue. So now it's reasoning over the ECG data but the patient's hemot hemotric and hemoglobin levels are low which could be a sign of anemia or other underlying conditions requiring treatment and so on. So and then finally the model gets the right answer which is that the patient has to stay in the ICU for more than 12 days. So all of this reasoning over for example some of the medical history and some of these ECG and lab

### [1:16:05](https://www.youtube.com/watch?v=Vhe_bX8mV2s&t=4565s) · b000092

values and also highlighting the the the X-ray was done by the model.

### [1:16:15](https://www.youtube.com/watch?v=Vhe_bX8mV2s&t=4575s) · b000093

All right we are out of time. Uh but yes summary is you know we started looking at reasoning we looked at different dimensions of reasoning you know about this multi-step problem each with intermediate levels of evidence how you combine it over multiple steps solve harder problems probably the biggest frontier in AI nowadays so very important to know about um and then we started you know obviously we we said this prompt based approaches to reasoning which don't involve any training if you have the reasoning example You can do supervised fine-tuning, but often times you only have the input and the answer and you don't have all this reasoning. So reinforcement learning is a way of incentivizing the model to output all this reason. And the biggest things to do with practice are to define reward functions. Maybe some examples, right? Maybe getting the answer correct, you know, having some keywords correct. Uh

### [1:17:13](https://www.youtube.com/watch?v=Vhe_bX8mV2s&t=4633s) · b000094

people really like to play with the length of these models. So defining reward functions and then you can just plug into some of these existing RL algorithms um which we covered. They're all called policy. The PO and all of these XXPO algorithms are called policy optimization algorithms. Right.
