# Lecture 12 – Self-Evolving AI (MIT How to AI Almost Anything/Multimodal AI, Spring 2026)

_English transcript_

- Channel: Paul Liang
- Source: [YouTube](https://www.youtube.com/watch?v=FhcHTSjvuKk)
- Duration: 1:16:09
- Caption source: automatic
- Status: complete
- Chinese translation: 94/94
- Translation provider: codex
- Generated: 2026-09-07T08:06:39+00:00

## Transcript

### [00:00](https://www.youtube.com/watch?v=FhcHTSjvuKk&t=0s) · b000001

All right,&gt;&gt; welcome back everyone. Almost the end of the semester. So, couple of announcements. Uh, so please fill out course evaluations and give us feedback. This is the first time we're running this course. Um, so definitely let us know how it can be improved in future years and also more importantly what you enjoyed the most about the course so that we can keep it. um already asked you all for a round of feedback uh during the midterm so you can incorporating some of that to the homeworks and also making for example a lecture something a bit more detailed about specific concepts. Uh homework five will be due this Friday. It's about LLM and multimodal agents. Some very interesting readings and getting some hands-on experience implementing these agents in in this Discord server. That should be fun. let us know if there's any uh questions or

### [00:56](https://www.youtube.com/watch?v=FhcHTSjvuKk&t=56s) · b000002

problems getting that in on time. And for the project, try to meet with myself and the TAs this week after class on Tuesday and Thursday if you need any more advice. Um we've given a round of feedback to the midterm reports. Everyone did super well. Um but just make sure you wrap up some of the final experiments and to really analyze, you know, what you found, right? If they work really well, congrats. analyze why it worked well. It didn't work so well. Also, let's try to figure out um what went wrong. And you're not going to be graded by the quality of of the results, but you'll be graded on the depth of your analysis um of the results. And of course, also the novelty of the approaches and how well you wrote the whole paper and report. So, instructions are online. So, make sure you meet with us if you need any feedback. Yes.

### [01:48](https://www.youtube.com/watch?v=FhcHTSjvuKk&t=108s) · b000003

Um, if you have late days, sure. Presentations will be next Tuesday, May 12th. Um, honestly, we haven't decided whether we want to do posters or in-class presentations. Benefit of posters is that it's more casual. You can walk around and talk to people. And we just be usually presenting to myself and one or two TAs as we go by your poster. Downside is that it takes a couple days to print a poster. I I don't know what's the logistics here, but it might if you need a poster by Tuesday, you might need to get it printed by the weekend, so you get a few fewer days. Um, the other alternative is just do in-class presentations. You know, everyone comes up, every team comes up, maybe every team has like five minutes to present. Uh, and you're presenting to the whole class. Maybe a little bit less interactive, but um, you can be working on your slides until 10 seconds before you present.

### [02:46](https://www.youtube.com/watch?v=FhcHTSjvuKk&t=166s) · b000004

Do people have a preference? Who prefers hoster? Wait, keep your hands up. One, two, three, four, five, six, seven, eight. Who present? Uh, who prefers in-class presentations? One, two, three, four, five, six, six, seven. Wow. Okay. Almost equal. Why not be here before presentation?&gt;&gt; Why do you offer presentations and periods?&gt;&gt; Because you have more time to do a better piece of work on Tuesday, which is quite soon.&gt;&gt; Uhhuh. Any arguments for why you want to do posters? Saw some pens here.&gt;&gt; Less pressure.&gt;&gt; Okay.

### [03:38](https://www.youtube.com/watch?v=FhcHTSjvuKk&t=218s) · b000005

you're too freaking&gt;&gt; well I'm there's technically like 50 60 people in the class um based on the homeworks and the submissions like many people don't come to class okay posters&gt;&gt; I think it also like makes you think about what you post and What do you think?&gt;&gt; I think posters for next week.

### [04:18](https://www.youtube.com/watch?v=FhcHTSjvuKk&t=258s) · b000006

&gt;&gt; Wow. I mean, I don't mind. Um, so you prefer homework five due later and posters. Okay. Okay. Is there is there a guideline on when the last day of class has to be? Because one thing we're trying to figure out is also logistics, right? if um I think it's like 25 groups if they all present for five minutes which is at the bare minimum to even get through all of the content right that would be that would even be more than the class time. Um the alternative is maybe do people who want to do do presentations they can do it on Tuesday and people who want to do posters can do it on Thursday. Half the class present on one half class presenting on the other possibility. Did you have any thoughts? You raise your hand.

### [05:11](https://www.youtube.com/watch?v=FhcHTSjvuKk&t=311s) · b000007

register and two students who make it class today uh chat as all five to be dropped. \[laughter\]&gt;&gt; I don't think we can drop it but we can maybe extend it by a few days. Okay. If people want, maybe we can extend homework 5 by a few days and then we can do a in uh we can do a poster in class on May 12th uh where it's going to be more casual, you know, walking around um present for a couple of minutes per group.&gt;&gt; Okay.

### [05:51](https://www.youtube.com/watch?v=FhcHTSjvuKk&t=351s) · b000008

&gt;&gt; Yeah. Um I don't know about end of next week. I I'll figure out some timeline, but&gt;&gt; you'll be&gt;&gt; I can I can think about extending it.&gt;&gt; Any other requests?&gt;&gt; Um if I extend homework five, then if people have time to make the posters by this weekend, can probably do a poster. I think that'll make it easier as well where people are walking around and mingling.&gt;&gt; You have advice on posters in&gt;&gt; Does MIT have a poster printing service? Do people know?

### [06:27](https://www.youtube.com/watch?v=FhcHTSjvuKk&t=387s) · b000009

&gt;&gt; I think it's 35.&gt;&gt; Yeah, you can go through FedEx and it's like 35 bucks. And how long would that take?&gt;&gt; Say less than 24 hours.&gt;&gt; Okay. I mean, we can cover the costs. Um, if you all can find a poster printing service. Um but okay we we'll look at this feedback and we'll we'll put announcement on pata by tomorrow

### [07:06](https://www.youtube.com/watch?v=FhcHTSjvuKk&t=426s) · b000010

&gt;&gt; maybe I need to check with my admin&gt;&gt; okay okay let's move on uh I'll take all this feedback and we'll make an announcement on homework five due date and we'll make an announcement on uh the format of of next Tuesday right but at least until maybe towards this Friday like keep working on it get the good results and then we'll let you know whether it should be a slide format or poster format even slides will be like four to five slides my poster will just be the same four to five slides and a poster format great and the final report will be due um in a week from next Tuesday uh you know giving you some time to further work on the report and to take in account any feedback that we give um during the presentations All right. So, this week was um casual discussion of several advanced topics. Uh I'll present a couple and then based on your interest, you can ask more questions and then dive deeper.

### [08:02](https://www.youtube.com/watch?v=FhcHTSjvuKk&t=482s) · b000011

Otherwise, we can just move on to the next advanced topic. Um but first let me just recap the course material just because it's the end and you want to make sure everyone gets the key material in and then we'll discuss um we discussed quite a bit topics where you kind of adapt these large language models where you pre-train language models and you adapt other modalities into them but it's more and more interest in training uh natively multimodal models directly not from language first but with all modalities directly from the beginning. a mixture of experts is also a big component of these native multimodal models. We'll cover some more advanced fusion techniques. We mostly covered fusion techniques based on different architectures but also lots of ways of uh designing different training objectives to improve fusion. Uh then we'll talk we talked about agents multimodal agents but we still left it as you know agents that are programmed to do a particular task. But as most of

### [08:58](https://www.youtube.com/watch?v=FhcHTSjvuKk&t=538s) · b000012

you have seen in today's field of AI, there's this trend of building agents that are able to automatically evolve, not fixed to the set of tasks they were programmed to, but automatically proposing newer, harder tasks for themselves and getting exponentially better over time beyond what you programmed them to do. So very exciting opportunity uh but also of course lots of risks with such agentic models. And then we'll discover we'll discuss some work on using AI to extend human senses going beyond vision language to other modalities like touch, smell, and taste. And we'll wrap it up with u you know building AI models that are uh much more adept at interacting with people and what are the principles you should be designing these AI models with so that they are actually bring about benefits to people instead of replacing them.

### [09:50](https://www.youtube.com/watch?v=FhcHTSjvuKk&t=590s) · b000013

All right. So as a key recap of um in 10 minutes of the most important content I would say from the class right we started by defining what a modality is and we discussed how you know modalities are usually obtained from a sensor raw modalities closer to the sensor and most of AI is about taking raw data and processing and abstracting and learning representations from raw data to get them into more abstract modalities. Right? They give examples like raw speech will be a raw modality, image will be a raw modality, very difficult to process, high dimensional, but then you can start extracting things like language, detecting objects and also getting past labels, right? Sentiment and objects. We saw that multimodal was the key scientific study that has three key principles, right? It is about dealing with uh problems that have many modalities and therefore they become very heterogeneous. different modalities

### [10:47](https://www.youtube.com/watch?v=FhcHTSjvuKk&t=647s) · b000014

being different from each other and that causes difficulty in processing them and at the same time they show interconnections. Interconnections can be broken down into connected information right so same information that's exhibited differently in different modalities and also interacting information how the information fuses and combines to bring about new information. So about heterogeneity, we also discussed that it can be seen as a spectrum from more similar to more different. Similar being examples like images from two different cameras to text from two different languages all the way to language and vision, language and sensing, right? More and more different modalities. And we presented this idea of a modality profile to really decompose the properties of each modality and use that as a way of measuring what is similar and what is different. Right? Looking at what are the base elements, the

### [11:42](https://www.youtube.com/watch?v=FhcHTSjvuKk&t=702s) · b000015

elemental word, elemental object region and how the elements differ, how the element distribution differs, right? Low frequency versus high frequency is another big area of heterogeneity. The structure if something is spatial. You've seen examples of using models that exhibit spatial invariance data that is tree structured or uh linear chain structure. You have methods that are dealing with these temporal invariances. Information, we've seen throughout the class using entropy and information theory as a way of measuring information. Uh noise, how differently noise exhibits in different modalities and what tasks are they suited for. Right? These are ways of decomposing a data source into its profiles and therefore you can use that to measure how similar or different they are with other modalities. Connections we saw are primarily a way of measuring the shared information that

### [12:40](https://www.youtube.com/watch?v=FhcHTSjvuKk&t=760s) · b000016

is connected that relates to two modalities right and that is in contrast to information that is unique in one and not present in the other. modalities are again can be at a spectrum from super strong a lot of overlapping information to weaker and even independent right and to give you any example there's often a clear relationship between certain words and certain object regions there are examples of onetoone connections but at the same time there are examples of many to many connections for example the word right right refers to a relationship between two objects and cannot be detected just from a single object. So connections, we saw how, you know, they're primarily learned by approaches like contrastive learning or you're maximizing mutual information between the positive pairs, right? Words and images that contain visual

### [13:36](https://www.youtube.com/watch?v=FhcHTSjvuKk&t=816s) · b000017

representations of those words and words other images without those words. So we saw contrastive learning as a way of capturing connected information. And finally the idea of interactions right we start with data with some overlap for some task right how different information regions become important for these downstream tasks. So we saw redundancy was an example of common information between modalities right positive words with positive expressions uniqueness was an example of you know how do you select which modality right a should be used but b should not be used right so for example you're saying positive words with neutral expressions out of which one of them should be chosen and we discuss a lot of methods in fusion that are based on dynamic attention Right? Sometimes you give attention to one, sometimes you give attention to the other. All of that is

### [14:33](https://www.youtube.com/watch?v=FhcHTSjvuKk&t=873s) · b000018

trying to solve the problem of identifying which one has the right unique information. And finally, we also saw synergy. Synergy is the coolest example where the information only emerges when you start fusing the modalities together. So you might give positive expression but you show negative you say positive word but you give negative expressions and the person is actually being sarcastic because of the difference in spoken language and non-verbal expressions.

### [15:06](https://www.youtube.com/watch?v=FhcHTSjvuKk&t=906s) · b000019

So that was a key takeaway from the first few lessons in the course, right? How to reason about heterogeneity. Uh and based on how heterogeneous a modality is, what are the right architectures to design for it? When do you use convolutional networks, when do you use transformers, when do you use graph neuronet networks and so on. Uh we saw connections and we saw how kind of contrastive learning is a way of bridging modalities and learning the common information between them. and interactions. We saw different ways of uh designing complicated fusion approaches to better learn the right interactions between modalities.

### [15:46](https://www.youtube.com/watch?v=FhcHTSjvuKk&t=946s) · b000020

And then we spend the bulk of the class discussing the core technical challenges in multimodal AI, right? Starting with these modalities, what are the core technical challenges that need to be solved to combine them and to integrate them into representations and predictions? And we saw at a high level six challenges. First key challenge was to represent how do you represent these modalities uh through fusion. So fusing two modalities into one representation through coordination modalities as separate representations but coordinating them through some similarity function and even vision. How do you take into account the latent factors and go from two modalities into multiple representations each dealing with a different part of information and then we covered alignment in the most simple case if you have multiple

### [16:41](https://www.youtube.com/watch?v=FhcHTSjvuKk&t=1001s) · b000021

elements and your elements are discrete so they're easily segmented alignment is all about matching right matching one word with some object region matching one word with uh the speech signal that you spoke that word it's all about this matching problem that aims to identify elements of similar information across modalities. Uh then that problem became more difficult when your elements were not discrete. So they were continuous. So in that case it's called continuous alignment and you have to take into account the granularity and segmentation across your elements.

### [17:23](https://www.youtube.com/watch?v=FhcHTSjvuKk&t=1043s) · b000022

Finally, whereas the first two the goal is to just discover the alignment to discover the matching. We also discuss align representations. So you use the matching, you use what is aligned with what in order to learn better representations. And this is the backbone of most of these transformer architectures today where you are taking in words, you're contextualizing them with which are similar words it should be aligned to, right? that's your attention and using that to obtain better representations weighted by those alignment values. So this uh led into transformers and also multimodal transformers where you can start contextualizing words through different visual regions of the image. So then we start talking about multimodal transformers based on these contextualized representations various ways of uh pre-training fine-tuning you know instruction tuning on them.

### [18:18](https://www.youtube.com/watch?v=FhcHTSjvuKk&t=1098s) · b000023

Um and then we start talking about reasoning, right? Reasoning is all about methods that don't just make a single prediction, right? Because the problems are much harder than making a single prediction like a classification label, but problems that require the model to break it down into multiple inferential steps, reason about each one, get the answer, propose all of these multiple steps to lead to um higher order inferences. So that was called reasoning. And we started this discussion of how we can train models to reason, right? In the past, reasoning was done by multiple layers of neuronet networks, right? Where each layer had more abstract information from the previous layer. Uh but nowadays with language models and with neurosyolic AI, we have this new opportunity of actually doing reasoning in an interpretable and explainable manner, right? Uh and that requires for example looking at what are

### [19:16](https://www.youtube.com/watch?v=FhcHTSjvuKk&t=1156s) · b000024

the intermediate representations in reasoning, right? Reasoning using attention maps, reasoning using language as a medium, breaking things down step by step, um looking at the structure of reasoning, right? We do a lot of linear chain reasoning A then B then C like your train of thoughts. But many settings in the real world require kind of tree structured reasoning where you're searching over different possibilities, many of which diverge at paths in time. And finally, the fact that reasoning often comes through external knowledge, right? So this can be forms of human reasoning and then using a model to do SFT. It can be in the form of really good reward functions and verifiers and then incentivizing reasoning using reinforcement learning. Right? So we spent a couple of lectures discussing how we can use reinforcement learning to uh achieve reasoning in LLM and multimodal LLMs.

### [20:13](https://www.youtube.com/watch?v=FhcHTSjvuKk&t=1213s) · b000025

So that was reasoning and then we discussed generation right generation was a challenge where you want to you know get high quality photorealistic real data generated using AI models and some examples include summarizing translating for example text to image translation or even creation right you start from a frame and you generate the entire video and we cover some core concepts in using um several approaches like using varational autoenccoders to generate data and then we start talking about diffusion models to generate data and flow matching uh to generate data. All these fall under generation and nowadays virtually all of these models are multimodal in nature where it's either text conditioning or or latent variable conditioning and the model is able to generate and follow

### [21:11](https://www.youtube.com/watch?v=FhcHTSjvuKk&t=1271s) · b000026

instructions to generate pretty realistic images. Right? So this is the part where we discussed VAE um diffusion models and flow matching models. Challenge five, we didn't dive too much into it. We only had one lecture on crossmodal transfer. But if you recall this setting extremely practical in the real world, right? Many settings you have some modality that you care about making a prediction on uh be it medical, financial, construction, other domains. And you're often faced with a problem where you don't have that much data, right? And you might have another modality with more data, right? Online textbooks, pre-trained language models, natural images that are of slightly different distribution to the one that you actually care about. So crossodal transfer was all about, you know, leveraging these other external data sources to learn more powerful

### [22:08](https://www.youtube.com/watch?v=FhcHTSjvuKk&t=1328s) · b000027

representations that are enriching your modality that you care about in order to do better. So we saw several approaches um transfer learning multitask learning and training the same base model with different prediction heads uh was a general approach to do that. this idea of co-learning where you either introduce this extra modality during training, right? And you start maybe fusing or aligning these representations or you introduce this extra modality as a prediction target, right? So you use language to predict the vision, right? This allows you to get a better enriched representation with both language and visual information. At the same time, because it's a prediction target, you throw it away after training. you just have a language backbone that is enhanced by vision. We call that co-learning. We discussed several ways of doing it. And finally, model induction, right? These are these are

### [23:06](https://www.youtube.com/watch?v=FhcHTSjvuKk&t=1386s) · b000028

the settings where you may not want to update the model, but if you have APIs, you can still use APIs and interchange information uh at the output layer, right? We discussed a co-raining algorithm which um kind of uses one classifier to label the data that is being fed into some other classifier. So that only requires blackbox access without modifying the representations itself. So that was transference or crossodal transfer. And finally challenge six isn't really a technical challenge in its own. Doesn't propose new methods or new algorithms but it's called quantification. Right? uh you know having deeper empirical and theoretical studies about different multimodal phenomena, different ways of training models that is obviously sorely needed in a field that is largely um empirical and think about as a science of of multimodal

### [24:02](https://www.youtube.com/watch?v=FhcHTSjvuKk&t=1442s) · b000029

um and we've kind of discussed and interspersed this into various lectures. We've discussed ways of measuring heterogeneity and how that influences the approaches you will develop. uh we've discussed some ways of measuring different ways that modalities interact and using that to design different fusion approaches and we'll cover a little bit of stuff today you know as I mentioned not everything is about the architecture a lot of challenges and opportunities also arise in how you optimize the model right it's not super easy to to optimize large large multimodal models all right so a summary of all six core challenges In uh in this layout, representation and alignment are almost always needed followed by reasoning, right? If the problem is complex enough and require systematic uh step-by-step solution of the problem. Uh otherwise, generation and transference

### [24:58](https://www.youtube.com/watch?v=FhcHTSjvuKk&t=1498s) · b000030

to generate more data or to transfer information and quantification is the the magnifying glass that aims to deeply understand uh the methods we develop. So, any questions about the recap of the core material before we move on?

### [25:23](https://www.youtube.com/watch?v=FhcHTSjvuKk&t=1523s) · b000031

I hope you also found the um other instructor's lectures very useful. So, Dimmitri cover a lot of ways of how fusion approaches can be applied in real world healthcare data and also cover some approaches of uh of both predictive reasoning and prescriptive reasoning. reasoning about how you can optimize different outcomes and then uh Sanuk and Zinhua hopefully most of you all were there for the lectures but they really discussed how some of these multimodal approaches can be used in manufacturing and transportation right but at the core a lot of these fusion and alignment approaches can be used and also reasoning approaches like how agents can be used in in manufacturing great So, uh, let's dive in into some advanced topics. As I mentioned, it's going to be a sampling. I have lots of slides. Feel free to stop me if there's more interest

### [26:19](https://www.youtube.com/watch?v=FhcHTSjvuKk&t=1579s) · b000032

or roll your eyes if you want me to move faster to the next advanced topic. Um, but one topic which is quite interesting and personally I feel should be the way these models are trained is called native multimodal models. Right? Uh you might have seen Llama Llama 4. This was from last year but Meta has a new generation of models which they also claim are are natively multimodal. Um if you have seen like kind of a lot of startups a lot of role model startups from Yan Lun from Feay they all claim native multimodal understanding. So what does that mean right? Uh the biggest distinction is the fact that you look at frontier labs nowadays, most labs still train language models first and they staple multimodal on top of that, right? They add visual encoder into the representations of these frozen language models. Uh so you can get visual

### [27:15](https://www.youtube.com/watch?v=FhcHTSjvuKk&t=1635s) · b000033

understanding and they staple diffusion model outputs on the output of the model so you can get image generation like the ones you have in your your OpenAI models. So this can be thought of as training language models first and everything else as an afterthought. Uh and therefore it works really well when the visual inputs that a model is taking in or the visual outputs that you want the model to output uh can be expressed in natural language. Right? I have a feeling that they're probably doing very detailed captioning of these images into language and they feed it into language only model and we want the model to output some image. is also very detailed image prompt expanded in different ways maybe using agents and then you know the text goes into a uh image generation model. So native multimodal models you know try to go by it in a different route where you don't train a language model first and instead you know you

### [28:10](https://www.youtube.com/watch?v=FhcHTSjvuKk&t=1690s) · b000034

could train a vision model first right actually train everything using video next frame prediction for visual physical understanding or maybe jointly right vision language joint understanding right um like the common commonly used motivation is that this is how how humans learn it's how babies learn before they start talking it's how animals animal and you know species don't use language like humans do is how they learn to to move around and communicate and interact and and survive and evolve in the world. So several approaches for this. So these are some of these um from meta. If I were to draw a schematic, right? So these non-native models, you have LLN, you have text, you train an image encoder which then goes into a linear adapter as we've seen and that goes into the token input space of language models, right? Blue means blue

### [29:06](https://www.youtube.com/watch?v=FhcHTSjvuKk&t=1746s) · b000035

means language model is frozen and orange means uh these are trained. So these are non-native ELMs. Most of them currently use the structure. Um and of course native models would be you know instead of having LLM frozen LLMs can be in orange. So they can be trained fine-tuned or perhaps even trained from scratch right from scratch directly with language and vision input. Uh so let them train from scratch with multimodal input. There are also different ways of doing it. uh late fusion approaches were still kind of take an image encoder, pass it through a linear mapping and then a fusion is done later after you've extracted really good image features. Um there are also approaches that do early fusion. So image patches without going through an image encoder first and directly in um either raw pixel space or through a linear mapping going through a

### [30:03](https://www.youtube.com/watch?v=FhcHTSjvuKk&t=1803s) · b000036

language model, right? That's more early fusion, right? It's not visual processing the late fusion but rather directly almost raw image data going into these um these LLMs. Although at this point it probably shouldn't be considered LLM anymore. It will be a model that takes in literally both raw text data and raw image data. So that will look like this early fusion. Um yeah I mean still jury's out what is the best approach really people think that we've exhausted a lot of text data and this approach of adapting you know other modalities into text is giving you good performance on domains where it's very easily captionable. Um but in other domains clearly we're we're probably hitting some plateau and therefore a lot of investment in approaches that um start direct multimodal training.

### [31:01](https://www.youtube.com/watch?v=FhcHTSjvuKk&t=1861s) · b000037

So I like this paper a lot. It's called scaling laws for native multimodal models. I want to discuss it a little bit. Um but first to give some background on scaling laws. Scaling laws are are a great example of science scientific research for today's foundation models right and what they essentially do is that they prescribe a law the power law of relationship that tells you right as I get more data or if I increase the parameter size of my model or if I increase the duration that which I train the model can I estimate how fast or how slow my loss will decrease. And this is obviously very important because if you're able to predict how much your loss will go down by if you collect 10 more terabytes of data or if you train your models for two extra months or if you increase your model from one trillion to 10 trillion parameters, if you can estimate how much

### [31:59](https://www.youtube.com/watch?v=FhcHTSjvuKk&t=1919s) · b000038

your loss will go down by, then you can make better decisions under compute constraints because you clearly can't try everything and see where the loss will be. So that's why it's a great example of science uh a scientific understanding of how these models work right and so some of these early scaling law models what they did follow chinchilla scaling law uh done by industry so they just train models of increasingly large sizes uh with increasingly more data and for increasingly long duration right and they empirically just plot how the training curve decreases right sometimes it plateaus sometimes it goes down more and sometimes as it goes down even more. And with that, they're actually able to write an equation that tells you, you know, as a function of number of data points, number of parameters or training duration to estimate what the loss will be, right? So they like showing these plots. So parameters here are very few

### [32:53](https://www.youtube.com/watch?v=FhcHTSjvuKk&t=1973s) · b000039

parameters as you see um x-axis is how long you're training for. Y-axis is your loss. So lower is better down here. Lower is better. And these colors show model families of uh down here darker fewer parameters upper they're lighter yellow more parameters. So you start with some of these dark colors they start with a validation loss of six and you can start training them more. they eventually go to something like 4.5, right? And then they plateau and then you increase the number of parameters. Uh first notice that the loss increases, right? As you have a bigger model, the initial loss is higher because it's a lot more random parameters. But as you train the model for longer, their validation loss goes down to four and then it goes down to three and a half and then three, right? And the largest model that you train with 10 to the 11 parameters the loss at the beginning is super high like I don't know 10 or 20

### [33:49](https://www.youtube.com/watch?v=FhcHTSjvuKk&t=2029s) · b000040

and then as you train it for longer it eventually comes down to a loss of 1.75 over here in yellow right so this is kind of if you if you look at the uh envelope of these plateaus can kind of get this straight line relationship telling you that first of all training for longer helps but training for longer only helps if your model is large enough Right? So eventually you can get down to to this loss. So then you can start interpolating and you know for any other model if you decide maybe I want a model of this number of parameters and I have the compute budget to train for this long what my validation loss will be. Okay. So that's some background and u in equation form it looks something like this. So the loss is a function of model parameters uh data set. Um in this case it didn't include uh training time. Um but this is equal

### [34:45](https://www.youtube.com/watch?v=FhcHTSjvuKk&t=2085s) · b000041

to first of all there's a floor right you know there's um E is the minimum loss right it's like a floor right it will never get below this loss right um and then uh two factors there's a and b these are parameters that you will estimate a is divided by n so that's a dependence on number of model parameters so n over there of course the model parameters increases a divided by n will decrease right so n is one important parameters And D is the data set size. Again it's B over D. So D data set size as that increases B over D eventually goes down. Right? So loss will be a minimum loss plus how much it decreases by number of parameters plus how much it decreases by size of data set. Right? Um so then no the parameters that you estimate N and D are given. Right? You know what number of model parameters is you know how many data points there are. know what the

### [35:43](https://www.youtube.com/watch?v=FhcHTSjvuKk&t=2143s) · b000042

loss is. You're just doing linear regression to compute E, A and B, right? That's how people get scaling loss, right? Get a bunch of combinations of N D loss and D loss different configurations and you estimate EA and B using linear regression. So that's unimodal scaling and this paper proposed a modification of E scaling loss to study multimodal scaling. Right? So now you have again loss you have your model size n which is the number of parameters of your multimodal model and you have di and dj which are uh data set sizes of your two modalities data set I for the first modality data set j for the second modality uh they can be the same they can be different okay so what does this equation look like so

### [36:37](https://www.youtube.com/watch?v=FhcHTSjvuKk&t=2197s) · b000043

first it boils down to the average loss of the first modality and the second modality. So this you can think about it as the average loss if both modalities were modeled independently right without any interaction between them. You then subtract C which is the maximum level of synergy right the more synergy there will be before the between the modalities the larger amount you subtract the loss goes down more there's a max amount of synergy that these two modalities exhibit there is again a factor of a divided by n so you know this goes down by your number of model parameters it's a dependence on number of model parameters or your model size and finally this represents the competition in the optimization process. So this is the parameter that depends on the summation

### [37:33](https://www.youtube.com/watch?v=FhcHTSjvuKk&t=2253s) · b000044

of your two data set sizes. Right? If your data sets are too small, there might be more competition between your modalities and that hurts optimization. That's what they found. But as you increase uh both modalities data set sizes that eventually this gets lower and lower, right? So good example of um you know using some of these multimodal concepts like synergy right that tells you that's that's a positive thing right synergy is a positive thing that tells you how much your loss will go down by as there's more synergy and also competition right that's a bad thing so you got to have more data points to get rid of the competition and then this this loss will go down any questions about these scaling loss

### [38:31](https://www.youtube.com/watch?v=FhcHTSjvuKk&t=2311s) · b000045

Yeah. So as I mentioned um you would first let's let's go for the simpler case. Okay. So in this case uh you would train models of different sizes different ends on different data sets these and get different losses L's. Right. And you do it enough, you get a data set of L and D pairs, triplets, right? And then you will fit linear regression to fit the coefficients E A and B, right? It's a linear function with respect to one over N and one over D, right? And here as well, you would uh you would train models of different sizes N with different pairs of multimodal data sets of different sizes, the RDJC.

### [39:12](https://www.youtube.com/watch?v=FhcHTSjvuKk&t=2352s) · b000046

So the question would then be know if you have a large enough data set of model sizes and data set sizes and losses could you fit any function right why does it have to be this specific form right you could technically fit any function right uh but people have found that first of all these power law relationships are quite natural right so one over something is quite natural and then you can try different configurations for example instead of doing one over n you try one over login for example and then you can uh essentially look at the the the fit error and also the held out error right the held out error on a new model size or a new data set size right and then that I think they found these these settings work best compared to other relationships between ND and loss yes&gt;&gt; so

### [40:07](https://www.youtube.com/watch?v=FhcHTSjvuKk&t=2407s) · b000047

that like these this because there is actually like the data set where you didn't and then this is sort of like another or maybe&gt;&gt; oh yeah it it is so the base model is some transformer right you train a transformer on lots of data sets or multimodel data sets after you train a transformer to convergence you point loss Right? But then once you have n d and the loss that can just be put into like a like a linear regression solver or a spreadsheet, right? That would just get e a and b. So it will be metal learning if this computation of these coefficients will then update the transformer then that is metal learning right but in this case because you really just train a transformer to convergence you've got in a loss you're

### [41:04](https://www.youtube.com/watch?v=FhcHTSjvuKk&t=2464s) · b000048

just kind of just basically comput statistics right you do linear linear models um great Okay. Um, so, so they found lots of really cool things. And for context, this was a kind of the early fusion transformer. So, you had a big transformer and I believe they did it for text and speech. So, you had a bunch of text and then you had, you know, speech, you know, audio and then more text, more audio. Uh, that's why it made sense to have DI and DJ of different sizes, right? It's not uh these fusion models where you have to have two modalities with the same amount of data each. Um so what do they found? So they found that early fusion models hold small advantage on small scales. On larger scales, both architectures perform similarly to the extent that you

### [42:00](https://www.youtube.com/watch?v=FhcHTSjvuKk&t=2520s) · b000049

could even do uh late fusion or early fusion. Uh and sometimes you don't even need image encoders and the scaling law still works. Uh so native multimodal models scale similarly to unimodal LLMs with um slightly different scaling exponents depending on how much you know how much data there was or how much synergy there was between your modalities. One thing they also found was that um oh so they also tried native multimodal models, dense models, dense transformer models versus mixture of expert transformer models and they actually found that um a mixture of expert transformer models actually scale much better. So yeah, some of these are are increasingly um mixture of expert models. So they show much lower loss.

### [42:55](https://www.youtube.com/watch?v=FhcHTSjvuKk&t=2575s) · b000050

Oh, they also found that modality aware experts uh which means that you have different experts for different modalities actually performs worse than modality agnostic design. So it's best to have experts that are shared uh for both image and text tokens at least in this setting. So that couple of interesting findings about how you should design mixture expert models. Uh so a little bit of a bit of a background I think you know if people don't know this but nowadays most of these models are super heavily over parameterized they can contain trillions of parameters but not all of the parameters are activated when you type in a prompt or as it does inference right you have this mixture of experts mechanism where these experts can be seen as you know transformer blocks attention heads many of them uh train in parallel and when you're doing inference there's a router which basically routes your your query keys and values to one

### [43:52](https://www.youtube.com/watch?v=FhcHTSjvuKk&t=2632s) · b000051

of these experts or a small subset of these experts, right? Um in practice only about 10% of these experts are activated for each query which allows you to still train extremely large models that in theory have the information is some expert but you know inference for seed only one one subset of them are activated. So deepseat model for example 600 billion parameters only 37 billion parameters activated uh during each inference pass.

### [44:27](https://www.youtube.com/watch?v=FhcHTSjvuKk&t=2667s) · b000052

We also did some cool work on that is used by some people on these multimodal interaction experts. So we started you know quantifying given a data point uh of two modalities is it redundant is it more unique is it more synergistic and as we've seen in our discussion on fusion different types of interactions can often require different fusion approaches right information makes a lot of sense to do contrastive learning because it's a shared information so contrastive learning captures that mutual information unique information it makes sense to have these dynamic attention weights. So sometime sometimes you assign a weight of one to a modality and zero to the other and sometimes one to the other, zero to the first one. So that captures unique information and synergy helps you know when you are trying to learn more complicated interactions, right? So you saw these different different types of fusion

### [45:23](https://www.youtube.com/watch?v=FhcHTSjvuKk&t=2723s) · b000053

approaches. So we developed this uh this approach that allows you to route different data points to different expert heads and they're then combined uh at prediction and it works for you know native models it works for adapter based models and works for all sorts of models. So here's an example where you took a sarcasm which has a lot of synergy and if you just use a single model like your clip or or blip model these sorry these are video LLMs they do really well on redundancy and uniqueness but they do very poorly on synergy this almost that random chance and if you start training some of these expert models redundancy and uniqueness you get a little bit better but for synergy you get a lot better dedicated expert head just for for data points with synergy get a lot better, right? And we also showed this to be better for for other settings where you know you have

### [46:20](https://www.youtube.com/watch?v=FhcHTSjvuKk&t=2780s) · b000054

figurative language, you have cartoons, you have humor where there isn't a very clear overlap uh between your modalities.

### [46:33](https://www.youtube.com/watch?v=FhcHTSjvuKk&t=2793s) · b000055

Okay. Any Yes.

### [46:49](https://www.youtube.com/watch?v=FhcHTSjvuKk&t=2809s) · b000056

How do you label something like based on your example as always kind of take a

### [47:09](https://www.youtube.com/watch?v=FhcHTSjvuKk&t=2829s) · b000057

Yeah. Um it's a hard question. So we've been doing a line of work on uh given data points, right? In sarcasm sometimes people are showing like actually face is face very angry but saying very positive things like sarcasm synergy. There's alo settings where this saying like in language you can detect synergy detect sarcasm. So that wouldn't be synergy it would just be you know language information. uh but in general we've been doing a lot of work on if you have multimodal data how do you use information theory to quantify which data points are unique which data points are redundant which data points are synergistic at a high level you can think about redundancy as data points which show information with each other and there's ways of developing pointwise mutual information because instead of a whole data set you want to know for every point what is overlap information mutual information way of doing that. U and by

### [48:06](https://www.youtube.com/watch?v=FhcHTSjvuKk&t=2886s) · b000058

extension uh unique information to be something like conditional entropy, right? And then synergy is is very tricky because if you just go by mutual information and conditional entropy, you don't get the synergy, right? In information theory, you can never estimate information arising from two modalities that wasn't present in the two random variables to begin with. Um so people actually talk about this more on Thursday. It goes a bit more mathematical, but there's a sub area of information theory called information decomposition that aims to study a question which is how do you take the total information and decompose it into redundant unique synergistic components where synergy can be thought of as the total information minus um you know this worst combination of unimodal information. But long story short, there are ways of

### [49:03](https://www.youtube.com/watch?v=FhcHTSjvuKk&t=2943s) · b000059

using statistics and major theory to measure these. Um, we did some formal work and then in this case there was some approximations that we made to get it to scale.&gt;&gt; Right? So you basically label the training data and then for each height you train a model that's just to interact with that.&gt;&gt; Yeah. So this So for example there's like 20% redundance you would take that 20% of the data and you would fine-tune a separate edge right or during training you'd be routed to that separate expert this is like 50% of the data and then for those data points you get routed to that head and then so on so different parts of the model will be activated depending on um which information they would routed to&gt;&gt; right and so typically this kind of model isn't the same backbone and then you fine tune the

### [49:59](https://www.youtube.com/watch?v=FhcHTSjvuKk&t=2999s) · b000060

sort of on type of uh interaction or or would you like actually like take a project?&gt;&gt; In this case, it took all the same models as um transformer architecture. Um but we did assign more layers. We found it more useful to assign more layers to synerg layers. Um but I I think it'll be possible and people have tried this separately and actually have actually different models different models be activated.&gt;&gt; Yeah.&gt;&gt; So you could for example think about you would learn a contrasted representation for redundancy and the contrasted representation is only activated for redundancy and for this it could be more transformer fusion layers. So it could uh it could be different models. In this case, it was the same on architecture

### [50:55](https://www.youtube.com/watch?v=FhcHTSjvuKk&t=3055s) · b000061

with different parameters dedicated to different heads.

### [51:08](https://www.youtube.com/watch?v=FhcHTSjvuKk&t=3068s) · b000062

Okay, any other questions? All right. Uh, so I want to highlight also some work in optimization. So um you know sometimes you think adding more modality should always help but that is not the case right sometimes actually in many cases adding modalities can hurt so this is an example of a video classification based on RGB based on audio features based on optical flow and these are just people doing different sports activities right you would think that the sound of what they're doing would help and of is optical flow it's um it's a visual modality that tracks know the movements of the people better than your standard RGBs. When you start fusing them, things get worse. More examples like this. Uh sometimes you train models and you you thought you

### [52:06](https://www.youtube.com/watch?v=FhcHTSjvuKk&t=3126s) · b000063

train a model to look at the image and answer a question about the image. For example, what color is the banana or how many people are there and the model actually doesn't. Right? Here's a cool example where you give the model yellow banana, ask what's the color, it gets it correct, yellow. And then you replace a banana with a green one. You ask what's the color, it still says yellow. Just because almost all the bananas, the models I've seen were yellow. So lots of examples like this. Um how many people in the image? Most models answer two because when these data sets were cured, when you start asking many people, the most common answer was two. And this can also lead to other issues. Um you know models have been known to right for example over here they're trying to caption this image and it's um and they just say a man sitting at a desk with a laptop computer uh and and the the man is incorrect and the model you look at the heat map it only looks

### [53:02](https://www.youtube.com/watch?v=FhcHTSjvuKk&t=3182s) · b000064

at the computer. So red heat map and it automatically deduces the identity of the person without actually having any attention on the person. So here's an example of a a gender bias uh in these models. So basically these models are actually you know sometimes you think they they combine information well and sometimes you think they will look at all the modalities but sometimes they don't and when they start fusing they can actually lead to worse performance. So how to fix some of these? Well one is to make sure the data set is is mostly balanced. So after this first version of VQA data set are released there were a lot of data sets that came and the balanced version of VQA. So for every question you will have a image that gave one answer and an image that gave the other answer. So is the umbrella upside down? You will have yes and you also have a no case. Right? Here's a good example because if you get a question is

### [54:00](https://www.youtube.com/watch?v=FhcHTSjvuKk&t=3240s) · b000065

the umbrella upside down no one asks this question unless the umbrella is actually upside down. Right? So the models have also figured out those shortcuts. So when you start balancing it with the other case then you get more balanced training. Uh so you can balance modalities and balance the data. You can also balance the training. So this involves uh you know developing models that actually pay attention to both. One way of doing that is to improve the optimization of these models. Right? uh these models are usually difficult to optimize and the reason why they kind of take a shortcut and only look at the question without looking at the image is again because of heterogeneity right uh these models you know they are really powerful language models they are very adept at processing text and having them to look at the image and combine it with the text is just a lot of heavy effort so if the

### [54:55](https://www.youtube.com/watch?v=FhcHTSjvuKk&t=3295s) · b000066

model can't find a shortcut to reduce it loss uh it will find a shortcut to reduce it loss uh different modalities also overfitit and generalize at different rates right so by the time it's learned and has a low perplexity on language right the loss might still be high on image so they then start to ignore it so how to fix things like these people have come up with all sorts of optimization objectives we improve their training to balance it one key idea here is to compute this overfitting to generalization ratio, right? What that means is that you know when you're training a multimodal model on two modalities, you also keep unimodal models, right? So just train on XA or the loss curve look like like your loss curve or your scaling law. You could do that nowadays as well. And if you train XB just separately, what will be the

### [55:51](https://www.youtube.com/watch?v=FhcHTSjvuKk&t=3351s) · b000067

loss curve and scaling law? Then you look at when you train your multimodal model with both A and B, right? and you track the loss curve for each of the modalities in the multimodal model. Okay, then you can start by comparing what was the loss of a in the multimodal case for that epoch compared to the loss of a if you just trained it unimotally, right? For that epoch. So you get some difference, right? You'll find that sometimes the modalities are learning faster than they they would be in the unimodal case and sometimes the modalities are learning more slowly than they would be in the unimodal case. Right? So once you find that you can then rebalance the training. Right? For example, you could add to the loss term. you could um you don't have to update every epoch and you can delay the update of the model in a way such that you know the multimodal training is is as close as possible to the unimodal training.

### [56:48](https://www.youtube.com/watch?v=FhcHTSjvuKk&t=3408s) · b000068

So some some ideas here. I mean not the biggest fan of this approach obviously because you have to train not just one model but now three models. So it doesn't scale very well. Uh but you know lots of works have followed up and usually done things in a similar vein. It's all about how do you balance the training either by adjusting the gradients or by adjusting the scheduling or learning rates. Uh but the key idea is just balance the training so that your models don't overfit on one and then ignore the others.

### [57:23](https://www.youtube.com/watch?v=FhcHTSjvuKk&t=3443s) · b000069

All right. Any um questions about some of these other fusion approaches? Mixture of experts improving optimization. Who finds this a challenge when you're doing your project or your homeworks? You come in, you gather your multimodal data, it's all happy and then you train unimodal models and the multimodal model uh doesn't get better. Who has face that issue? Quite a few of you. How do you fix it or is it still a problem? Wow, you two.

### [58:00](https://www.youtube.com/watch?v=FhcHTSjvuKk&t=3480s) · b000070

Any folks had the issue and then managed to fix it or what improved training?

### [58:11](https://www.youtube.com/watch?v=FhcHTSjvuKk&t=3491s) · b000071

&gt;&gt; How much worse? And what do you think the problem is?

### [58:19](https://www.youtube.com/watch?v=FhcHTSjvuKk&t=3499s) · b000072

&gt;&gt; They're like, well, maybe the training like am I really having information here worth it? Um because a lot of There's a modality who just does all the work and adding audio.

### [58:41](https://www.youtube.com/watch?v=FhcHTSjvuKk&t=3521s) · b000073

Um, we're trying not to add something to the loss make it think about what I care about in the past.&gt;&gt; In our case, it's retrieval and like contrasting on what question might about the data in here.

### [59:10](https://www.youtube.com/watch?v=FhcHTSjvuKk&t=3550s) · b000074

&gt;&gt; What about you?&gt;&gt; It's more like it's very balanced. So, it's I think I fixed this at first.&gt;&gt; Okay. Sounds like I should cover this earlier in the class next time. People are having a lot of these issues. Anyone else want to share if they have issue with uh training and then maybe it's the data set's imbalance or the model's imbalanced and multimodal doesn't doesn't outperform unimodal.

### [59:41](https://www.youtube.com/watch?v=FhcHTSjvuKk&t=3581s) · b000075

Do you want to share? You raise your hand just now.

### [59:52](https://www.youtube.com/watch?v=FhcHTSjvuKk&t=3592s) · b000076

existence

### [1:00:07](https://www.youtube.com/watch?v=FhcHTSjvuKk&t=3607s) · b000077

contributing to the so

### [1:00:17](https://www.youtube.com/watch?v=FhcHTSjvuKk&t=3617s) · b000078

&gt;&gt; some of the sanity checks I like to do is um you train unimodal models say A and B which you all should have done in the in the midterm report and then you start analyzing right if if A gets 50%. right 50% correct 50% wrong. What are the errors? what are the top top 10 errors you know with the wrong but also most confidently wrong and then you can start visualizing some of them and then for B let's say get 60% right 40% errors right so again look at what are the errors that B makes right on modality B right is it do they overlap in the errors do they make very different errors right then you get a good idea of you know whether it's complimentary or you know redundant that's one thing right doing error analysis looking at you know the errors that different unit model models make. During fusion we also discuss you know one way of dealing with this is also the stage wise approach. You know you train a model on the best performing one.

### [1:01:14](https://www.youtube.com/watch?v=FhcHTSjvuKk&t=3674s) · b000079

Language is probably the best performing one for most cases and then you get 70% and you get 30% error and then for that 30% you optimize it based on maybe vision and maybe reduce the 30% to 20%. Maybe 20% you add audio so on and then maybe reduce 15%. So if you're only ever optimizing the mistakes that a model makes then um then in theory it should the reduction should happen right how much is not clear but in theory it should reduce right we call that the stage wise stage wise fusion we discussed during the the fusion lecture great um okay let's see what we can cover about some these these evolving agents. Um but yeah I think I left you know at some point we're discussing this this this general paradigm right we have multimodal data we're doing fusion and

### [1:02:11](https://www.youtube.com/watch?v=FhcHTSjvuKk&t=3731s) · b000080

alignment to get representations and because most of these multimodal LLMs condition on these representations you can start asking questions getting answers we talk about generating more data so we have this really multimodal input multimodal output models but one issue is that the reasoning context is getting longer and longer So these models have to take in all sorts of information and they can become much more expensive and they can also start forgetting uh previous information. So if you already recall I introduced this approach called mem1 which is an approach of an agent that manages it on memory right it's using RL to taking actions but also these actions include what to store into memory and what to throw away from memory right so if you do that then you only ever have this constant internal state that summarizes all the information without your context

### [1:03:06](https://www.youtube.com/watch?v=FhcHTSjvuKk&t=3786s) · b000081

growing longer and longer over time. So these agents can get faster, they can become more accurate, and they use less memory. Here's an example of a agent that is able to manage its own memory by absorbing memory management into its training process, right? Then everything is trained using reinforcement learning. So that got us thinking so if memor is agent that learns to manage it memory, right? And you've seen other agents, you know, manage tools, APIs, configurations, but at the end of the day, most of the time it is still, you know, you the user delegating what to do, right? Use these tools, right? Here are the tools you have access to, right? It's still very much handwritten, right? We call this a harness, right? People might be familiar. This is called the harness, right? So when you give a tool to a model, you're not actually updating the parameters of the language model. Parameters are the same. it is just um the wrapper around the model. You're

### [1:04:02](https://www.youtube.com/watch?v=FhcHTSjvuKk&t=3842s) · b000082

giving it access to different tools and APIs that it can use. That's technically called the harness of a model. And most of you might have seen the cloud code leak, right? Well, cloud code for example is a harness. Um its biggest contribution the model itself is the opus model or you know the actual language model. But what gets cloud code to be so so useful is the wrappers around the model, right? What to do when you type in this? What are the guard rails when it does this? What to do when it's wrong? How does it reflect? How does it manage this context over extremely long code bases? Uh that is all part of the harness of the model. And well, cloud code harness of 60,000 lines of code, right? Extremely handgineer probably took lots of engineers writing them. It's probably a big win for the neurosy symbolic community because for them it's like you know these models are not just the base model but actually so much of it was if

### [1:04:57](https://www.youtube.com/watch?v=FhcHTSjvuKk&t=3897s) · b000083

else statements 60,000 lines of if else's conditional statements uh outside the base language model itself but nowadays we are you know we have this new opportunity where you know instead of we've seen examples of updating the model right training a model using SFT RL making the models become better the next evolution solution is to also train the harness, right? How can the models harness and the wrappers around it get better automatically over time? And can the models also write their own harness? So that's kind of the idea behind these sub evolving agents, right? And as I mentioned, these harness includes memory, it includes tools, APIs. You know, the first question is how can these agents automatically decide what to do, you know, as a wrapper outside the base model. So that's self-evolving agents and we've also taken this a step further where you know in many settings it's not just enough for one agent right

### [1:05:53](https://www.youtube.com/watch?v=FhcHTSjvuKk&t=3953s) · b000084

how can multiple agents each with access to language models and their harnesses and other tools get better and evolve over time so we call that self-evvolving multi- aent systems so let me give us some some you know examples of this so this probably started with uh you know alpha evolve and some of the work from Google and how agents can evolve and become better at coding and design new algorithms uh how agents can be used to discover new math and prove new theorems. So these are examples where you need the model to evolve, right? Because if you don't if your model is just being trained and instructed and instruction tuned based on the mathematics that we know, we don't have an high expectation that it would go out and prove theorems that were not in its instruction data set, instruction tuning

### [1:06:50](https://www.youtube.com/watch?v=FhcHTSjvuKk&t=4010s) · b000085

data set, right? So evolution basically means that you know the models are actually searching and learning how to improve its own model parameters and improve its own harnesses and improve its own context over time. So to make this more concrete um alpha evolve is probably one of the first approaches in this space. Uh and then open evolve is kind of the open source attempt to open source the production of alpha evolve. Alpha evolves is by Google so it's not open source. So you start just by a human defining something right defining some task it could be uh usually it's some some definition of the task for example optimize this algorithm right and it also usually comes with evaluation so optimizing algorithm it could be the runtime of the algorithm right so that's a specification and the the the approach

### [1:07:45](https://www.youtube.com/watch?v=FhcHTSjvuKk&t=4065s) · b000086

you know starts by taking in the problem definition it first samples uh different prompts, right? These are prompts that are, you know, basically designed uh based on the the context uh of the problem and then based on these prompts, it goes into the language models and they can be multiple language models that are each trying out different approaches. So some may try to optimize the program in this way, some it may optimize the algorithm in some other way and try out all sort of the heristics. There's usually an evaluator. So they can call an evaluation function to uh in this case get the runtime of the algorithm and then it sends all this to a database. The database will log what prompts the model has tried and designed for itself. What are the actual solutions the model proposed which is the code. It will also log the evaluation how good that code was. So what was the runtime of the algorithm and all that gets sent into a prompt

### [1:08:42](https://www.youtube.com/watch?v=FhcHTSjvuKk&t=4122s) · b000087

database. So it has knowledge and memory of its previous attempts. Then a model starts sampling more prompts based on this this database based on what it's tried. It will usually propose something new uh to try next based on a trajectory of things that work right. All of this is done by by language models. So uh yeah the the programs that the model writes all looks like this. It's just you know code and what are some things that I can solve. So left is uh is talking about real analysis problems. um the bound integrals bound different mathematical functions uh and then these C are these are the constants in the bound right the goal is to get the best approximation as possible so you want the C to be to be lower and you can actually improve upon the uh best known um constant factors in these approximations

### [1:09:37](https://www.youtube.com/watch?v=FhcHTSjvuKk&t=4177s) · b000088

and then for geometry there's a lot of these problems like uh bin packing or square packing problems you know again these are problems where there is some constant factor and they're trying to improve it. They're actually able to improve some of these and here are some again more mathematics you know again other constant factors that these were you know actually able to be automatically discovered by by these um models. So in alpha evolve it was mostly about just you know language models taking in you know a list of trials that the previous language models have done and then sampling uh you proposing a new task. Uh there's been more structured ways to do it as well. So this shinka evolve work um basically organizes this evolution as a tree. So it starts from some attempts. tests are code that a

### [1:10:33](https://www.youtube.com/watch?v=FhcHTSjvuKk&t=4233s) · b000089

model generates or text that a model generates and then it's more structured. So it defines maybe specific ways of modific modifying something, right? Uh and that gives you a tree and then it you know sometimes the tree is pruned out because it's too big. Sometimes the model continues on. Um but yeah, it's basically optimization of of this you know previous evolution strategies to make it more structured. So as you see here um yeah and these models get better and better you know you usually see these jagged step as the model you know proposes more attempts and then evaluates them and then another set of models propose next attempts synthesizing what the model has tried before you get better and better.

### [1:11:27](https://www.youtube.com/watch?v=FhcHTSjvuKk&t=4287s) · b000090

So in these as you see the model is fixed right the the model parameters are never updated right the model parameters is still just the base language model is never updated it's just wrappers around it right so you can think about this as evolution at the level of the harness or the level of the you know context the model itself stays the same and then there's other approaches which actually evolve the model so uh There was alpha evolve and there was now theta evolve. So alpha evolve just basically you can think about as a fancy way of prompting the model to try different things and then based on the attempts further prompted to try more things. The base model is always fixed but you can of course use the success rate of what the model proposes as a signal to do reinforcement learning on the base model parameters itself. So now the evolution is getting back propagated to the to the

### [1:12:23](https://www.youtube.com/watch?v=FhcHTSjvuKk&t=4343s) · b000091

model weights right. So ttt discover theta evolve. We actually train the model at test time with improvement scores as a reward signal for um for reinforcement learning. Okay. So so kind of this is what what it looks like. Um so you have the language model um that outputs different responses and usually these are just you know different codes that it could write right different ways of optimizing some program or proving some math and this goes into a verifier which verifies and gets the guess the value of the current runtime or something they're trying to optimize and this together with um no it gets sent into a database so the database logs all the attempts, all the code, all the current status, how much they've progressed. This gives a new

### [1:13:17](https://www.youtube.com/watch?v=FhcHTSjvuKk&t=4397s) · b000092

prompt of what the model should try next and that goes into the model which then actually tries it, right? So that's the loop, but now is the verification signal, right? How much it has evolved successfully over each iteration used as a reward signal to train the the actual model weights. So not just a harness everything else everything here is at the heart define it the model weights is also getting better. Uh let me wrap up and we can recap this you know at the beginning of next lecture if people are interested. Um we've also built um built a framework that is widely used is called coral. Coral now extends this evolution to multi- aent sets right. So same idea right multi- aent can be very helpful you because a single LLM can just output one trial and one attempt but multiple agents can output many attempts and they

### [1:14:16](https://www.youtube.com/watch?v=FhcHTSjvuKk&t=4456s) · b000093

can also be kind of seated with different specializations right um so you start at the top with a configuration so again optimize from a piece of software you have a evaluation that tells you the current uh runtime of the software this framework seats multiple agents each of them can have their own expertise And they each can autonomously perform different tasks, right? There's a shared memory among all agents that these individual agents can read from. They can, you know, actually take an action which is to in this case write some code or make some modification to the database. They can run evaluations to see the current state of the system and they can write to this shared memory. What is this shared memory? This is something that is accessible to all the agents. It includes previous attempts. each agent what were their attempts and what was their success rate. uh different notes. For example, one of Ben

### [1:15:12](https://www.youtube.com/watch?v=FhcHTSjvuKk&t=4512s) · b000094

is telling a note that you know smaller batch size actually improves the runtime for example and different skills that it learns, right? And this uh this heartbeat monitor is one that just periodically checks in on all these agents and prunes the ones which are not improving and creates new ones uh based on the ones that um um you know are most promising directions. So yeah, really good results and I'm running out of time. So we can discuss more of this and we'll talk about other advanced topics on Thursday. But um just a recap of of the assignments for the week, course evaluations, and we'll send announcement tomorrow on final this decision on homework five due date and logistics for next Tuesday's presentation. All right, I'll be around if people have more questions and if people want to discuss their projects, right? Otherwise, thanks everyone.
