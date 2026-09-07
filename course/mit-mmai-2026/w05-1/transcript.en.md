# Lecture 6 – Large Multimodal Models (MIT How to AI Almost Anything/Multimodal AI, Spring 2026)

_English transcript_

- Channel: Paul Liang
- Source: [YouTube](https://www.youtube.com/watch?v=H9nvkyTsrnI)
- Duration: 1:10:26
- Caption source: automatic
- Status: complete
- Chinese translation: 84/84
- Translation provider: codex
- Generated: 2026-09-07T07:55:53+00:00

## Transcript

### [00:00](https://www.youtube.com/watch?v=H9nvkyTsrnI&t=0s) · b000001

All right, folks. 2:35. Let's get started. So, welcome back. Uh, quick recap about assignments for this upcoming week. So, homework 2 will be due tomorrow. Hopefully, all of you are making progress on that. If you need any help, uh, come to my office hours or the TA's office hours today and tomorrow. Um after homework due is due is due we're going to again select um some folks to present their homeworks in class this Thursday. Uh again no pressure just to share the things that you're excited about and to share with uh with the rest of the class. Uh so that'll be this Thursday. I'll be traveling unfortunately have some last minute travel. uh but we'll do these presentations for the first 30 minutes and then the TA vault will go through some in-depth implementations of multimodal LLS. So these would help you for your homework three which will be

### [00:55](https://www.youtube.com/watch?v=H9nvkyTsrnI&t=55s) · b000002

coming out later this week. Okay. So remember to come to class on Thursday for these uh presentations for homework 2 and to look at this detailed tutorial and implementation of multimodel lls. So multimodal LLMs will be the content and focus of today's lecture at the conceptual level before diving into the implementation details on Thursday. Uh but again let me just quickly recap what we've seen so far in class and then also spend the first 30 minutes finishing up our discussion of multimodal alignment. So we started with uh two key concepts in multimodal learning. The first being fusion and the second being alignment. And recall the key differences in fusion. It is really about taking in different data modalities either at the feature level or at the raw data level and joining them into one representation. Right? This one representation which we call the fields or joint representation should capture

### [01:52](https://www.youtube.com/watch?v=H9nvkyTsrnI&t=112s) · b000003

the ways different interactions happen and appear across your two data sets. So visually it looks something like this. And we saw lots of ways about how to do fusion whether additive multiplicative with dynamic weights both at the feature level and at the raw data level. So it's all about taking in two different modalities and learning one single representation that combines the information. And then we moved on to alignment where the goal was slightly different. The goal is usually to keep your modalities separate and your representation separate but to contextualize them identifying which parts of one modality align with which parts of the other modality. So we saw that in the first case where it was simpler, we assumed that the modalities were easily discretized into individual elements. For example, words in a sentence uh object regions in some image and then a goal of alignment is to basically learn this matching which parts of the words

### [02:48](https://www.youtube.com/watch?v=H9nvkyTsrnI&t=168s) · b000004

aligns with which parts of the images. I will continue that discussion of alignment today where we'll extend this discrete alignment to continuous alignment for many data modalities like audio and video and sensors. Uh it is not very clear the segmentation into individual elements which makes alignment more challenging. And finally we also emphasize that there are types of alignment where the alignment is the end goal. Right? Learning this matching is the end goal in both the discrete and continuous case. And then there's this other subp part of alignment where learning these connections is merely an intermediate step towards learning better representations. So we call that contextualized representations and that will be our segue towards some of these transformers especially multimodal transformers that learn alignment but primarily use it to learn better representations downstream.

### [03:41](https://www.youtube.com/watch?v=H9nvkyTsrnI&t=221s) · b000005

Again a quick recap about what we saw last week on discrete alignment. uh we primarily went through the algorithm contrasted learning where again the goal was that if you have nicely segmented boundaries for example a sentence and an image or a word and object region you're learning two separate representations Z1 Z2 one for language one for vision so it's not the same as fusion because instead of learning one combined representation you're keeping these two representations separate right uh the key of course is to learn the alignment with some similarity function between them. That's why there's this arrow between these two representations. These uh these similarity functions typically look something like cosine similarity. Uh we also saw other extensions of cosine similarity to other similarity measures and not only at the sample level but also distribution level similarity measures.

### [04:36](https://www.youtube.com/watch?v=H9nvkyTsrnI&t=276s) · b000006

And one simple way of learning such a line representation is to assume that you have positive data and negative data. Positive pairs are those coming from the joint distribution. So images and their actual captions. And you want to maximize the similarity between them. So you bring those two representations closer together. That is this term on the numerator. And in contrast to these positive samples, you also have negative samples. Negative samples are those sampled from the marginal distributions. So randomly sampling an image and randomly sampling a a caption. most likely they're not going to be corresponding with each other and you want to minimize the similarity of those representations. So you want to push them far apart and that's the term at the bottom over here summing over all the negative pairs uh reducing the similarity of these representations.

### [05:31](https://www.youtube.com/watch?v=H9nvkyTsrnI&t=331s) · b000007

And we saw that uh you can actually give some uh concrete arguments that these types of contrastive learning and alignmentbased representation learning methods essentially capture the mutual information between the two modalities. And that's a formal way of looking at it. It is the ratio of data from your joint distribution. So in other words, your positive pairs divided by the ratio of uh your product of marginal distributions. In other words, randomly sampling images and text which constitute negative pairs and contrastive learning, clip, other alignment based measures primarily capture this mutual information which of course is great. And then we discussed how if the representations the information that you learn primarily lies between the shared space then this is a really good way of learning representations right uh it can be bad if the information goes beyond this

### [06:29](https://www.youtube.com/watch?v=H9nvkyTsrnI&t=389s) · b000008

shared space which means alignment doesn't give you enough signal and it's also bad if uh this shared space is too much in which case alignment gives you too much signal and too much noise in your representations. So all that is recap from from last week's discussion on alignment and the previous week's discussion on fusion. Any questions in terms of the recap before we move on to the content for today's lecture? Yes.&gt;&gt; A little more why too much overlap is a problem if your goal is just um alignment. Like I understand if you're trying to build representations that if there's too much overlap there's a lot of noise but if the goal is just alignment then shouldn't like as much overlap as possible be&gt;&gt; exactly so when I said uh too much overlap is bad what I meant is that if

### [07:24](https://www.youtube.com/watch?v=H9nvkyTsrnI&t=444s) · b000009

the shared region that alignment learns is much more they need for the task. Recall from the previous slide we had this circle with the label Y inside of it. uh so label y is too small in the context of all the shared information you learn from alignment then your align representations are capturing too much noise. Of course if you don't care about why you just care about aligning data then the goal is to try to align data as much as the shared information exists in your data. Great. So um so this as we mentioned can cause troubles when um what you care about is beyond the shared information which leads us to a quick segue into representation fision. So sometimes you can combine uh both fusion and alignment and learn more representations than the

### [08:21](https://www.youtube.com/watch?v=H9nvkyTsrnI&t=501s) · b000010

data modalities that you started with. Right? So we call that fision. Uh there's different ways of looking at fision. One way is very intuitively maybe you learn some representation that is responsible of capturing the shared information and if that's insufficient for your task then you can also learn more representations that are responsible for capturing the unique information that is not directly within the shared region. So we call that fision at the modality level. That means if you have two modalities, you have three of these uh three of these representations and you can go even deeper, right? You can go even more fine grain, right? There's obviously a lot of advantages in learning representations that are disentangled, that are clustered that each account for one different small variation in your data, but I won't get into much detail on this. So the intuition behind some of these extensions of contrastive learning is right, you might want to learn some

### [09:17](https://www.youtube.com/watch?v=H9nvkyTsrnI&t=557s) · b000011

stuff that's in both modalities. For example, if you have images and text, then usually the people are described using the caption and the objects are described using the caption. So those will be learned by your alignment based methods. That's what's in the middle. Then there is some stuff that's unique in language. For example, the specific syntactic structure or the specific grammar or even the specific language, right? That's more unique in language. And then there are some information that is unique in vision. For example, things about the texture, the depth, the perspective, all of this is not directly described in the caption, right? So that is information uh unique to images. So there's been a series of works that have been proposed that extend contrastive learning. Uh this is one of our works called factorized contrastive learning. You can think about it as in the middle you have this kind of alignment between

### [10:14](https://www.youtube.com/watch?v=H9nvkyTsrnI&t=614s) · b000012

image and text, right? So you take the image, you take the caption, you maximize the positive pairs and you minimize the negative pairs between image and text, right? Intuitively that's what learns the overlap. How do you decide what learns unique information in images? Well, by the same logic, you would define images and augmentations of the same image, right? So certain augmentations of the image constitute positive pairs. For example, certain rotations, cropping and translations. those correspond to positive pairs and certain other for example other randomly sampled images would be negative pairs. So you can do this kind of self-contrastive learning within image only and symmetrically you can do this sort of self contrastive learning within the text. So you might take uh take the caption and you maybe change out certain words that are semantically similar or

### [11:10](https://www.youtube.com/watch?v=H9nvkyTsrnI&t=670s) · b000013

you change it from present to past tense for example. Those are examples of positive pairs when augmenting the text and you can also think of negative pairs which are other randomly sampled uh captions. So that will constitute self-contrastive learning in language. So now you have this sort of vision where you have three representations. One is in charge of vision and language overlap. One in charge of vision only. One in charge of language only. Any

### [11:47](https://www.youtube.com/watch?v=H9nvkyTsrnI&t=707s) · b000014

questions? Okay. Intuitive um shown to work well uh and deal with settings where uh for example your label your tasks goes beyond requiring what is in the middle but also unique information in each modality. I will run through So this is an extension to alignment. Uh I'll run through a few more extensions to these classical alignment based methods. I'll do these fairly quickly. Um if you're interested, you know, it's more about pointing it to the right references if it's relevant to your research homeworks and projects. So another extension is the idea of global alignment. So we saw that in this case of discrete alignment, we often need supervision at the local level, right? You want to know for example this image corresponds to this caption or

### [12:45](https://www.youtube.com/watch?v=H9nvkyTsrnI&t=765s) · b000015

even better this word corresponds to this u this region of the image. So you need this kind of paired data between the two modalities that you're trying to align. That's how you get your positive pairs. How you get your negative pairs. Of course in many settings it is very hard to obtain this pair data. You might have settings where you have a bunch of images and separately a bunch of text and you don't know what is the matching between them and you still want to learn this alignment. So what to do? So we call this global alignment because now you're trying to globally align two distributions if you have samples in each but without the specific individual pairings. One general way of doing this is to jointly optimize the representations that you learn for a given alignment together with finding out what the optimal alignment is.

### [13:41](https://www.youtube.com/watch?v=H9nvkyTsrnI&t=821s) · b000016

Okay, what do I mean by that? So if I know if I am able to find an alignment a pairing of of these two data modalities then I can do my classic you know contrasted learning right what we've seen so far assuming we know what the pairing is between them but when we don't know what the pairing is between them we can try to jointly optimize over different possible pairings so that you can find both the right pairing and for that pairing what is the right align representation. Okay. So, you'll do this jointly. Um, exactly how this works, I'm not going to go into too much detail. There are fields of study that are concerned with this, but essentially you can view this as some graph matching problem where given maybe four images and four captions, you don't know what the pairing is. You can kind of search over all possible pairings,

### [14:38](https://www.youtube.com/watch?v=H9nvkyTsrnI&t=878s) · b000017

right? In the most naive case, search over all possible pairings. So each pairing can be seen as uh you know bjection between your four elements on one side and your four elements on the other side. Um so that's one parameter which is the assignment uh f your bipartite or your bjection assignment between a and b and for each possible assignment you can compute what are the weights for that assignment. So if for example this point and this point are matched together then you would try to find what is the similarity between these two points because they will be treated as a positive pair and then you would add up the weight between these two points assuming that was a positive pair right so those are your similarity weights and you essentially optimize what is um the most similar one the highest degrees of similarity across all

### [15:34](https://www.youtube.com/watch?v=H9nvkyTsrnI&t=934s) · b000018

possible uh permutations and all possible assignments of points between A and B. There are efficient ways of solving this this relaxations for this. Obviously, the exact problem is kind of empty hard. Uh but there's ways of instead of checking all assignments using linear programming by essentially setting variables Xig. So Xig represents these two are a positive pair that should be one when there's a connection otherwise zero. You can view each of these weights as again your similarity function for those positive pairs and you can essentially maximize your weights multiplied by your x's your variables indicating which of them are pairs with each other uh under certain relaxations can be seen as a linear programming problem solvable with simplex algorithm. Again details are not super important here. You can read up more about this if

### [16:32](https://www.youtube.com/watch?v=H9nvkyTsrnI&t=992s) · b000019

you want. Key idea again being a Contrasted learning and alignment requires you to have paired data at the resolution at which you want to align your data. When that is not possible, you can jointly optimize searching over different pairings in your data together with learning these align representations assuming a particular pairing. You can train both of these two together and hopefully at convergence you have learned both the pairing within your data and the aligned representations for that pairing.

### [17:09](https://www.youtube.com/watch?v=H9nvkyTsrnI&t=1029s) · b000020

One more slide before I pause for questions. Another way of extending this is instead of looking at just one to one mappings you can also look at the soft mappings. So for each element on one side what is the distribution of elements in which they are aligned to on the other side. Um soft mappings instead of onetoone mappings. Uh again there's formal ways of looking at this. You can search up this field called optimal transport which basically studies you know what is the right soft assignment of weights between your two modalities that maximize uh some particular similarity function for that assignment. And again this is called optimal transport. It can be solved pretty efficiently.

### [17:57](https://www.youtube.com/watch?v=H9nvkyTsrnI&t=1077s) · b000021

Any questions about this?

### [18:05](https://www.youtube.com/watch?v=H9nvkyTsrnI&t=1085s) · b000022

I'm not going too much detail because it's good to know and for certain specific applications where you actually don't have paired data, this can be quite useful, but it is not the most useful algorithm in all of multimodal learning today. So, I want to spend time on the the more commonly used things. Several other quick uh extensions I want to emphasize. Um one is the continuous case, right? We saw how in the discrete case it's much easier to align your your elements. Uh in a continuous case, you got to additionally deal with this problem of basically segmenting your data. So how to do that? Well, there are established algorithms um in the video space. There's established algorithms for segmenting videos into actions. So finding discrete actions that um are

### [19:00](https://www.youtube.com/watch?v=H9nvkyTsrnI&t=1140s) · b000023

represented by boundaries in the videos. For time series data, there are established methods based on change point detection. So these are algorithms that essentially tell you what is a semantically meaningful change in my time series data and at which other points is it just noise and don't correspond to any semantically meaningful change. These can be useful for taking continuous data and finding the right boundaries so that you can then start doing alignment.

### [19:31](https://www.youtube.com/watch?v=H9nvkyTsrnI&t=1171s) · b000024

Discretization is another key concept. If you have continuous data, one way is to essentially learn clusters. So, uh here's a very popular speech pre-training method. Speech data as you know is highly continuous. So if you want to do any of your masked pre-training, you have to either extend the objective from masked prediction over a discrete set of tokens to continuous prediction. But continuous prediction is often very difficult, right? Continuous regression is often very difficult. Most regression methods end up just learning the average signal instead of the boundaries of the signal. So a lot of these pre-training methods based on speech they first take in your continuous signals and then they do some clustering K means clustering in your represent uh in your representation space and once you have done your K means clustering I'm going to replace the prediction

### [20:28](https://www.youtube.com/watch?v=H9nvkyTsrnI&t=1228s) · b000025

targets with the cluster ids instead of the the continuous speech signal itself. So that means when I start applying these uh these sequence models to speech and I learn representations, I'm going to mask something out and predict what is the cluster ID that particular continuous signal belong to instead of the signal itself.

### [21:02](https://www.youtube.com/watch?v=H9nvkyTsrnI&t=1262s) · b000026

VQVA is another example of this vector quantized variational auto autoenccoders in virtually all of your generative models today that deal with um images, video, audio and all sorts of continuous data. uh you're essentially you know learning representations that first encode your data and then in the representation space uh do some clustering clustering or quantization so that these representations are no longer continuous but rather mapped to a set of discrete ids. So you end up literally being mapped to a set of discrete numbers like 98 390. Of course, the number of discrete tokens is usually extremely large in the orders of you know 2,000 to 5,000s u but is mapped to this discrete set and then it is decoded back to your image. So you can think of each of these um the

### [21:57](https://www.youtube.com/watch?v=H9nvkyTsrnI&t=1317s) · b000027

these tokens as a visual token, right? Just that how you have text tokens about you know 70,000 vocabulary of text tokens in your models. These have 8,000 visual tokens in your images. These make these u image models much easier to train and more importantly much easier to align between text and these models. Right? Because nowadays the way these models are are prompted is that you have some text that you're typing. For example, you know, generating me an image of a cat that gets encoded by a a transformer model into text tokens, these text tokens and then are aligned to these these visual tokens in the intermediate representations and then they're decoded to the image. So still they have to be converted into discrete so that the alignment can be done uh on these discrete tokens.

### [22:54](https://www.youtube.com/watch?v=H9nvkyTsrnI&t=1374s) · b000028

All right. Any questions about um ways of dealing with continuous alignment?

### [23:10](https://www.youtube.com/watch?v=H9nvkyTsrnI&t=1390s) · b000029

Okay, last extension of alignment before we start moving on to these large foundation models is this idea of implicit or emergent alignment. So everything we have seen so far worked on explicit alignment, right? So you have two data modalities. You learn features for each and then you have this function that you're defining the similarity function that explicitly is being trained to bring these positive pairs together and negative pairs apart. Right? So you're explicitly enforcing alignment using some objective function. this line of work in implicit alignment. Um, I've seen papers scattered throughout the years, but perhaps this paper in 2024 called the platonic representation hypothesis really tried to make this more formal. And it basically states that uh this hypothesis states that neuronet networks when

### [24:06](https://www.youtube.com/watch?v=H9nvkyTsrnI&t=1446s) · b000030

trained with different objectives on different data and modalities are converging to a shared statistical model of reality in their representation states. The idea that these models are converging even without explicitly forcing them to converge, right? Even these independently trained models are somehow converging and becoming more aligned in the representation spaces. So what is evidence for this? Okay, so here is a plot on the x-axis. Uh first of all each of these um these things at the top over here these are all different language models. So Bloom language models these are some set of open source language models open llama language models and then you have a llama models from 13 33 to 65 billion models. So all those are are language models. You can see that purposely these

### [25:00](https://www.youtube.com/watch?v=H9nvkyTsrnI&t=1500s) · b000031

are uh open source language models because some of these require access to the hidden representations in these models. So these are open source models. Okay. So these are all language models. Each of these dots over here are called Dino models. Dino is a computer vision model. It is a state-of-the-art model for object recognition and some other visual tasks. On the x-axis it is language performance. So you see these language models are sorted based on how well they perform on NLP tasks. Okay. Some of the larger models from meta llama models are better when it comes to language performance. Most critically this y-axis shows the alignment to dino v2. And in this case alignment is some similarity function that I'll get to later but it's one of the similarity functions that we've discussed that essentially measures for these language models. I take their hidden representation for these Dino models,

### [25:57](https://www.youtube.com/watch?v=H9nvkyTsrnI&t=1557s) · b000032

Dino V2 model, I take the hidden representation and given some paired image caption data set, what is the similarity in the language representation with the vision representation and you can see that this alignment is getting better and better as the language performance is getting better and better and also as these dino models are going from small to big which implicitly means the vision performance is getting better and better. Okay, so the alignment is increasing but critically of course llama and dino were never explicitly aligned in the first place. Right? One was like trained by by meta and Dino is trained by some other folks right these two were completely separate models completely different architectures never aligned in the first place but as the language models get better as measured by language performance and these vision models get better as measured by vision performance their alignment scores are increasing

### [26:52](https://www.youtube.com/watch?v=H9nvkyTsrnI&t=1612s) · b000033

over time. So that is their that is the empirical finding repositing this hypothesis that these representations are converging even though they come from different models trained completely separately on different data different modalities.&gt;&gt; Question&gt;&gt; does that mean that like with scale all models become world models? If you believe this representation uh this hypothesis then perhaps yeah of course there are this is a hypothesis right there's empirical evidence some empirical evidence for it there's evidence against it I'll show some other follow-up works that that say this can be quite sensitive to certain hyperparameters um but it would not be a stretch to say yes you know as all these models are being continuously trained um larger getting better on different views of the

### [27:49](https://www.youtube.com/watch?v=H9nvkyTsrnI&t=1669s) · b000034

world, they're eventually converging to perhaps one world model. Right? Each each of these models is learning one slice of that world model. Any other questions about this about these findings? Okay. And these are just um well these are other observations, right? For example, they showed alignment scores generally increasing with language performance, better alignment to clip to MAE, which are mass autoenccoders, imageet pre-train models, other clip models. Seems like as these language models are getting better, they're somehow becoming more and more similar to these vision models. Yes.&gt;&gt; Yeah. So, maybe I'll get to it later. I didn't get to the part where you're talking about whether or not they're going to be aligned with one another or they were actually just judged based on their similarities.

### [28:47](https://www.youtube.com/watch?v=H9nvkyTsrnI&t=1727s) · b000035

&gt;&gt; So they're just judged based on similarity of embeddings. So these are these models have never been trained to align to each other, right? Llama is just trained to do next token prediction during pre-training and whatever fine-tuning, instruction tuning afterwards. Dino is trained to do object recognition. So these are completely separate models. uh never been trained to align to each other. That's why we say the alignment is uh emergent or implicit. Um yeah, I mean here here just more more evidence. Um performance on language gets better, alignment gets better. Uh a quick note about the the similarity function used. The similarity function used here is this global similarity where again we saw um if you have three concepts for example right apple orange and elephant uh in images and you have

### [29:42](https://www.youtube.com/watch?v=H9nvkyTsrnI&t=1782s) · b000036

apple orange elephant in words um this alignment doesn't really care whether the image of the apple is close to the word of the apple doesn't care about that it just cares that in the images apple orange are close together and elephant is far away and separately in text apple oranges are close together and elephants are far away. So it doesn't really capture the local similarities but it rather captures the global distribution of of semantically meaningful concepts in both right and operationally they they call these kernels basically these are for your image embeddings all the image embeddings I first find is like basically a coariance matrix between them right that's what this kernel is doing is basically there's a coarance matrix telling me how all these image representations are distributed with respect to each And then for the text embeddings, I compute how all these text embeddings are distributed with respect to each

### [30:40](https://www.youtube.com/watch?v=H9nvkyTsrnI&t=1840s) · b000037

other. Kind of like your coariance matrix. And once you have those two separately trained uh matrices, uh the measure of alignment is how much these two are similar to each other. Okay. So it's measuring alignment at a more global level, right? Across bunch of text and a bunch of images. And finally, I'll end our discussion of alignment with this this quick uh video which came out uh kind of debunking some of these findings in the platonic representations and also adding on some new findings just to show that this is kind of an open area and nobody really knows what is going on and whether alignment is actually emergent or not. So I'll play this video.

### [31:52](https://www.youtube.com/watch?v=H9nvkyTsrnI&t=1912s) · b000038

As we've seen, language models getting larger, getting better, alignment is increasing. But they're showing after this calibration there's some confounders and the alignment actually disappears. Global alignment disappears, but surprisingly local alignment persists. So you come up with some other name for the hypothesis.

### [32:26](https://www.youtube.com/watch?v=H9nvkyTsrnI&t=1946s) · b000039

So perhaps you know this is probably the the key takeaway where previously in the platonic representations we saw that you took all the embeddings for A and you computed their their kernel covariance. looking at the global structure and then for B you computed the whole global structure and then we computed some similarity and they said there's some confounders in that most of that alignment and similarity goes away but these local structures persist so you're restricting it to a a small neighborhood of which points are nearby to each other this local similarity still remains similar to this local similarity in the other embedding space uh so the global alignment disappears but the local alignment persists uh which basically is to say well sometimes in alignment right the the notion of similarity function and what you're measuring can actually make a very big difference on the representations and results that you get so you got to be very careful with it. Yes,

### [33:22](https://www.youtube.com/watch?v=H9nvkyTsrnI&t=2002s) · b000040

&gt;&gt; in that case what does calibration mean? Um it's a way of basically pertur you can check out the paper in more detail but it basically perturbed the model such that the global global alignment you know kind of gets destroyed uh but the local alignment still still remains. It's a way of um yeah basically disentangling the global structure from the local structure. Any last questions about alignment? Right to to summarize, we've seen first introduction to alignment. Uh we saw the most important concept which is how to explicitly align your data using methods like contrastive learning. We showed its relationships to mutual information when it can be successful and what are potential risks. And then we discussed some extensions to alignment when for

### [34:18](https://www.youtube.com/watch?v=H9nvkyTsrnI&t=2058s) · b000041

example you don't have exact pairs. you got to do this optimal transport or you got to learn the assignment and mapping together with the alignment and also some extensions to continuous settings. Uh and finally we also saw some very exciting but also perplexing recent phenomena of implicit emergence alignment. Right? Any final questions about alignment?

### [34:52](https://www.youtube.com/watch?v=H9nvkyTsrnI&t=2092s) · b000042

Okay, let's move on to our next topic, the focus of today's lecture, which is on large multimodal foundation models. So cover some of these uh multimodal transformers, foundation models, key ways of adapting them, and then going from text generation to multimodal generation. But as a recap, uh unless you've been living under a rock, you know, we all know what large language models are. Uh they can, you know, by virtue of being pre-tuned on tons of data, you know, fine-tuned and instruction tune and nowadays adapted for test reasoning, they can answer arbitrary questions. They can engage in multi-turn open-ended dialogue. They can perform any of your classical NLP tasks, whether it's translation, part of speech tagging, document summarization, and so on. Uh nowadays they're connected with tools and search so they can retrieve news and do calculations and operate your computer in real time and with today's

### [35:49](https://www.youtube.com/watch?v=H9nvkyTsrnI&t=2149s) · b000043

better test time inference and reasoning capabilities they can do you know harder multi-step tasks like solving really hard math problems and write lots of code and check their code and write test cases and so on right of course these are these capabilities are increasing even today so of course most settings in the real world don't just use large language models. They use these large multimodal models because text is often not the only uh input that's that's required for these models to to pay attention to. Uh they need to look at images, they look at video, they need to have access to a computer, whether that's JSON representations or documents or other files. Um so obviously there's a lot of interest in these large multimodal models. And just to illustrate where I think the path for these large multimodal models are going, I'm going to just give several examples of what we might want them to do, assuming they are able to kind of see and hear this video

### [36:44](https://www.youtube.com/watch?v=H9nvkyTsrnI&t=2204s) · b000044

in addition to text. So I'm just going to play this quick video.&gt;&gt; It's just a privilege to watch your mind at work.&gt;&gt; It's just a privilege to watch your mind at work. Obviously all of you can answer and we might want a large multimodal model to answer again all sorts of questions right from basic classification questions like what is the tone of the man in the gray shirt that he's being sarcastic kind of rude uh open-ended questions like can you describe the relationship between them so these models should be able to identify that they're actually characters in Big Bang Theory the purpose is to be sarcastic and rude to be humorous but they actually really good friends with each explain why. So explain by you know through domain knowledge perhaps quoting even previous episodes. Uh so now you have this idea of reasoning and explaining not just in text but also

### [37:41](https://www.youtube.com/watch?v=H9nvkyTsrnI&t=2261s) · b000045

quoting previous visual episodes or previous auditory information. Can you also have these models generate? So use this as a scene but generate more videos in the future, right? following along their story line, generating future episodes, uh perhaps even ask counterfactual questions. We animate what the response would be if this person was from a different culture. Would they find it offensive or still as humorous? So, these are all tasks that uh some of these multimodal models today can can solve perhaps, you know, up to these last two. And of course, we're seeing quick progress towards some of these unified multimodal understanding and generation tasks as well. So the way I see how most of these models operate is in several steps. So they obviously take in multimodal data. I'm showing text, audio and video for now. But uh of course you can more extensions. It can be anything. They

### [38:38](https://www.youtube.com/watch?v=H9nvkyTsrnI&t=2318s) · b000046

have to learn multimodal representations that combine and learn the interactions and learn the alignment between them. Everything that we've seen as these basic multimodal concepts have to be inside this representation. they then have to um continue to you know be able to probe these representations. You can ask questions and get answers in response. You can give it other tasks and it can also perhaps generate other modalities in response and this goes on across multiple turns right uh in interaction with the user. So to build these models, I think there's three key parts, right? The first key part is just to learn these multimodal representations using these large scale pre-trained foundation models, learning these powerful representations. Another key part is once you have these representations, how do you quickly

### [39:33](https://www.youtube.com/watch?v=H9nvkyTsrnI&t=2373s) · b000047

condition a large language model that probably is pre-trained to basically attend to to look at to understand these representations? So the next time you are asking a question to this model, it's not just answering your question. It's actually looking at the representation of the video upon which a question is asked. So that's what we call adapting large language models uh with multimodal text generation. And finally, beyond answering your questions in text, can it also produce outputs in other modalities? Right? So for example, can you highlight previous episodes? Can you generate the next frame? All of these are are tasks that involve generating multimodal data as well. So that's part three enabling uh text and image and more broadly multimodal generation right and it's of course it's clear that this is a path to AGI because it has to be multimodal input representations multimodal output uh and

### [40:29](https://www.youtube.com/watch?v=H9nvkyTsrnI&t=2429s) · b000048

of course over long periods of time multiple interactions with people.&gt;&gt; Any questions about schematic? Yes&gt;&gt; I do. Maybe not about sematic but um it's a very stupid question maybe but how will it identify that it's being sarcastic? It cannot will it be multimodelled through boss voice processing is it visual interaction knowing that he is especially with Sheldon he's like very unemotionally in his expressions&gt;&gt; right&gt;&gt; and with the caption the like let's say like CC captions for like people with auditory problems so it's like how can it identify that it's been sarcastic&gt;&gt; so of course I'm going to train this w with data right and the model is going to be able to get us inputs But um in this case probably raw video and raw audio. So raw video you'll be able to see everything that you're seeing here. Raw audio you' be able to hear the tone

### [41:27](https://www.youtube.com/watch?v=H9nvkyTsrnI&t=2487s) · b000049

of voice which is a big indicator of sarcasm. Um and probably I mean if you train these models well with this pre-training knowledge it would have identified that through facial recognition and um that these are from you know big bang theory context right in which case there's already a prior that these people are often humorous and sarcastic with each other. Yeah I'll get into some details. Um so yes so this schematic how to first learn these representations you know they are really powerful ideally pre-trained self-s supervised how do you adapt LLM to actually attend and understand these representations and how do you go from text generation to multimodal generation so first question um of course it's no surprise that nowadays the the predominant way of learning these multimodal representations is through

### [42:24](https://www.youtube.com/watch?v=H9nvkyTsrnI&t=2544s) · b000050

your transformers Right? Most of these data, especially streaming multimodal data, for example, if there's text that you're typing into some chatbot, that can be seen as a sequence of tokens. Uh a static image is a sequence of patches and videos are a sequence of frames. And likewise, audio sensing data, they're all thing seen as a sequence nowadays of different elements. Uh so you can use the transformer self attention to essentially learn the alignments between these elements you know the different ways they're aligning and interacting with each other and use that to learn better representations for downstream tasks. Uh so that's exactly what we mean by by this kind of sub challenge right contextualized representations where we want to learn the alignment between parts of your word to parts of your face to parts of the sound. Um, but it's not just learning these alignments and giving it to the user. The goal is to use these alignments to learn these

### [43:20](https://www.youtube.com/watch?v=H9nvkyTsrnI&t=2600s) · b000051

better downstream representations so you can do better classification and detection and question answering and interaction with people. And that's what we mean as a concrete example of these contextualized representations. So one popular way of doing this today is to use these multimodal transformers. We did some early work here when back in the days and at a high level it's an extension of these unimodal transformers that probably most of you already are familiar with and we also covered in week two of the class right so again key equation is here schematically what might be happening is that let's say there's some text input some some context or prompt or or speech a person is saying and I'm going to assume for simplicity that there's just three words, three words. So that's X1 and there has to be a multiplication with W

### [44:18](https://www.youtube.com/watch?v=H9nvkyTsrnI&t=2658s) · b000052

Q and that is just you can think of it as a projection that brings whatever the text input dimension space was into some common D-dimensional space upon which this multimodal alignment will be performed. So that is a linear transformation WQ from whatever text token space into this D-dimensional space and that linear transformation will be will be learned. It's a learnable parameter. On the other side, you might have your visual or auditory information. Uh in this case, the sequence length is four instead of three. It can be different from the length of the text. Um so this might contain some information about you know vocal emphasis, uh eye rolling and maybe other set of non-verbal features. So that's x2 transposed and that would also be multiplied by some learnable parameter wk. So that parameter would bring whatever your non-verbal input

### [45:13](https://www.youtube.com/watch?v=H9nvkyTsrnI&t=2713s) · b000053

dimension is into again the same d-dimensional representation space same as this d upon which a multimodal alignment will be performed. Okay. So now you have 3x dx4 that's transposed this multiplication which is shown \[snorts\] over here. This multiplication would be over the dimensional vectors. So it's this multiplication in this multimodal embedding states of dimensions that gives you this 3x4 matrix. Uh this can be seen as your multimodal attention matrix. In this case it is a vision to language attention matrix that essentially tells you the alignment patterns, right? which of my three words should align with each of my four non-verbal expressions in order to capture these most informative interactions between them. Uh so that's a 3x4 weighted outer product. Uh we

### [46:10](https://www.youtube.com/watch?v=H9nvkyTsrnI&t=2770s) · b000054

looked at all these constants previously. There's some normalization by square root of D. So the variance goes back down by one overd. So these magnitudes don't increase too quickly with your dimension size. And your softmax basically turns each row into a set of numbers that are non- negative and sum to one. So there's a normalization constant so that these uh these attention values are easier to interpret and makes training more stable. So once you're done you basically learn the alignment between them, right? You privilege aligns 7 with vocal emphasis. So that pair is important. And the word privilege also aligns point three with eye rolling. So that pairing is important. It changes the meaning of privilege when a person is overemphasizing it or eye rolling afterwards. And likewise maybe the word

### [47:04](https://www.youtube.com/watch?v=H9nvkyTsrnI&t=2824s) · b000055

mind also you know changes and has to be aligned with uh the vocal emphasis. Okay. So that is the alignment that is the 3x4 alignment that is learned as a latent step. Right? This is not all you need as was the case for discrete alignment but this is only some intermediate step and this intermediate step is then used to actually learn better representations. So what might that look like? You would have another copy of your non-verbal features that's 4 by d through some you know some transformation again into this dimensional space that's 4 by d. So now you have a 3x4 attention matrix multiplied by your 4 byD features that gives you a final 3xd output. Right? The way you want to interpret this by the output well there's three of them. So it's a new representation for language one for each of the three words.

### [48:01](https://www.youtube.com/watch?v=H9nvkyTsrnI&t=2881s) · b000056

For the first word privilege, it's seen what are the four alignment weights with my four non-verbal features and it's taken that 7 times the vocal emphasis feature and it's taken the.3 times the eye rolling feature. So that's a new representation for privilege contextualized with the fact that there were vocal emphasis and eye rolling. Likewise, the next feature for the word mind contextualized by the weight of one with the vocal emphasis. And this goes on across all your three words.

### [48:37](https://www.youtube.com/watch?v=H9nvkyTsrnI&t=2917s) · b000057

So that's a language representation that has now been contextualized using your four alignment weights with your four verbal features. And this language representation can then be used to predict your task. in this case sarcasm. So the only supervision here that's coming from is the video comes as an input, right? Three words, four non-verbal expressions, the label with sarcasm. You have a bunch of sarcastic videos, not sarcastic videos. And all of this is trained in uh the latent space, right? So the alignment is done in the latent space. And this alignment leads to better representations that are useful for downstream tasks. That's why we call it an aligned representation.

### [49:30](https://www.youtube.com/watch?v=H9nvkyTsrnI&t=2970s) · b000058

Any questions about this? Yes.

### [49:45](https://www.youtube.com/watch?v=H9nvkyTsrnI&t=2985s) · b000059

alignment in time.&gt;&gt; Uh great question. So, so this is really a time dimension, right? So, there's three words that spoken across time. So, it's just words that a person is saying in the sequence. These are non-verbal expressions that are being um shown in the sequence. So, you emphasize the word first, then you eye roll. Um and of course uh one thing I'm leaving out here but also as standard in transformers you technically apply a position encoding to each of these right the position encoding are these kind of like cosine waves that um basically identify this is time zero this is time four um so once you have that this attention matrix does capture the time dimension right captures that I rolling is the fourth step and it's like three steps after saying the

### [50:39](https://www.youtube.com/watch?v=H9nvkyTsrnI&t=3039s) · b000060

Yes.&gt;&gt; How granular do like \[clears throat\] tokenizations get when it comes to things like like vision language features for example because like you can imagine that there's like small facial expressions that might not be captured by the current open space.&gt;&gt; Yeah. Yeah. I mean that's um that's open question, right? It's hard to design um a fixed tokenizer for images like the ones that we have for text. So different context would depend on different things. Sometimes you only have a single frame of a face in which case you have the opportunity to more fine grain tokenization. But if you have a video then you have this time dimension with multiple frames. You may not be able to do lots of tokenization within each frame. Uh this also compatible with kind of feature extraction methods. So this may not be the raw data, but if you had really good uh speech models that

### [51:35](https://www.youtube.com/watch?v=H9nvkyTsrnI&t=3095s) · b000061

extracted, you know, vocal emphasis as a concept or facial landmark models that identify your eye movements uh into discrete concepts, then that could also be as input to these downstream transformers. Let me show an example. Um this is a bit more granular than the one I was showing just now. But in this case, this was vision and text transformers trained on images and captions. So you had um those images and you had these captions and you're basically training it just to you know do some fusion and retrieval for example. And what this is showing is that for each of the words the corresponding uh attention scores, alignment scores over the pixels in the image, right? So these were the resolution of the visual tokens that they had. Then you start seeing, you know, when the when the model takes in

### [52:32](https://www.youtube.com/watch?v=H9nvkyTsrnI&t=3152s) · b000062

the word flowers and you look at the alignment scores with the image patches, it does highlight flowers. It does highlight the wall. It's looking at the background when it's looking processing the word cloudy. Uh it's you know highlighting the rug when the input token is rug and in the plant and so on. So these uh these alignment scores are reasonably interpretable in these multimodal transformers.

### [53:07](https://www.youtube.com/watch?v=H9nvkyTsrnI&t=3187s) · b000063

Okay. So how are these models typically used in a lot of these uh pre-trained models? Usually your images image stream you have vision only transformers that does self attention within vision your text stream there's um you know self attention within text you learn features and then you have these cross streams right which is the vision to language attention and language to vision attention and these are these are not the same right they can be different and then they are used for downstream tasks so those are cross model transformers and unimodal transformers. Sometimes people find that you can combine these multimodal transformers with more alignment objectives. So this model for example, one of the very first vision language models that came in a bunch of images and image patches and text with text tokens. These go into

### [54:04](https://www.youtube.com/watch?v=H9nvkyTsrnI&t=3244s) · b000064

this multimodal transformer that learns representations. And look at what objectives they designed. Right? So one objective is mass language modeling. So you present the model with the image regions and some part of the caption and the model has to predict the mass tokens right from the language context but also by looking at the visual context. Then you have the other way where you present the model with a full caption and parts of the image with masking in the image. So now the model has to kind of predict what parts of the image were masked out from the remaining parts of the image and also looking at the text. Um so these are you can think about as local alignment and then you more have more global alignment as well. So you have the entire entire image patch the entire caption and they have some positive pairs some negative pairs and try to distinguish between them. So masking words masking images and

### [55:01](https://www.youtube.com/watch?v=H9nvkyTsrnI&t=3301s) · b000065

asking whether a sentence matches the entire image. There's a line before fuse paper which was the the reading reading that we assigned. Uh you can think about this as kind of clip clip like contrastive learning. So image and text come in, they each learn some features, image features and text features. And then they use image and text contrastive learning to first align these features with positive pairs and negative pairs. And then these then go into a multimodal transformer after these features already pre-aligned by some contrastive model.

### [55:48](https://www.youtube.com/watch?v=H9nvkyTsrnI&t=3348s) · b000066

Okay, so all sorts of ways of doing these things. Um personally I think the space is quite messy and that's very empirical not a lot of structure to to to you know which alignments and which uh which embeddings are done where but it's just good to present the whole space. Any questions?

### [56:16](https://www.youtube.com/watch?v=H9nvkyTsrnI&t=3376s) · b000067

All right. So let's move on to part two. So as you discussed part one was primarily about treating different data modalities as sequences. Once you treat them as sequences these multimodal transformers are a pretty good way of learning which elements align which with other elements and using that to learn downstream representations. Now that is not useful until you can adapt language models to actually attend and look at these representations to solve tasks. So here's a general way of doing it. is called adapters. Uh how these adapters work is that usually you have maybe some pre-trained language model. Okay. Uh ideally you want to keep this pre-trained language model frozen and not update it too much because it already contains a lot of powerful information and it's probably not feasible for you to fine-tune it and do any adjustments to it anyway. And let's say you have some other data modality that you care about. Let's say

### [57:14](https://www.youtube.com/watch?v=H9nvkyTsrnI&t=3434s) · b000068

images. How these adaptors work is that you first take this image, you extract some features from it, right? Maybe from a pre-trained CNN or vision transformer. Extract some features. Now these features are not understandable by the language model. They don't even fit into the input dimension of the language model. But what you would do is that you would design these adapters. These are very simple, lightweight, sometimes can even be linear transformations which basically transforms these image embeddings into some embedding dimension that is consistent with the input dimension of your language models. Okay, which in this case are your token embedding size. And you would then append these adapted representations as a prefix to whatever language context you're putting in. Uh and that will give you basically this adapted language model, right? It still keeps most of the pre-trained elevation, but the only change is an adapter that

### [58:11](https://www.youtube.com/watch?v=H9nvkyTsrnI&t=3491s) · b000069

you've added at the beginning that projects these image embeddings into this token embedding space that the language model can take in. So how to train this? You first give it the image, you adapt it, you give it a caption, and you will auto reggressively predict that given both this image and previous words in the caption, you predict the next word. So at some point you will learn to predict red boat in the water while looking at this image. Once you've done that it can actually be very quick. You know in this case it's super lightweight. This adapter is usually just a linear transformation. So it's very efficient to train. Once you've done that you can give it other new images and ask it questions and it can start answering them correctly. Answer it blue. You can do in context learning. So uh you give it an image, you ask it a question, who invented this with the

### [59:09](https://www.youtube.com/watch?v=H9nvkyTsrnI&t=3549s) · b000070

answer the right brothers and then you give it a new image and a question who invented this answer with a with a blank and this is kind of in context learning, right? You give it one example as the prefix and then you give it the instruction for the next example and the model is able to answer Steve Jobs. And you can do now two example in context learning. So let's say you give it this image of an apple get this feature representation and you adapt it to the prefix. You then give it a caption that says this is a DAX where DAX is a madeup word. And then give it a second example of a orange image and say this is a blickicket where blickicket is again a madeup word. And these are your incontext prompts. Two examples for incontext learning. and give it a third image apple and you ask what is this then a model by by this pattern mapping

### [1:00:04](https://www.youtube.com/watch?v=H9nvkyTsrnI&t=3604s) · b000071

identify that this is a dax so that's two example in context learning&gt;&gt; yes&gt;&gt; how much do tasks like this suffer from like uh just knowing that there are kind of like developmental tasks in in the in the training data like this is a classic devel developmental task in cognitive science.&gt;&gt; Yeah.&gt;&gt; Like does it learn from there or is it actually learning that representation?&gt;&gt; Well, it probably knows this is a kind of a image binding developmental task, but it still has to actually compute the similarities between these images in these embeddings. So, it's been successful at that. It still has to do this image embedding with these two new words, this binding, the symbol binding problem, symbol grounding problem. So, it's been successful as that. Uh so it's just a quick way of showing that first of all these features are actually used by the model right this adapter has

### [1:01:01](https://www.youtube.com/watch?v=H9nvkyTsrnI&t=3661s) · b000072

succeeded and the model is able to do this this you know natural language binding problem but I agree yes the model probably knows um what this task is okay so so yeah these adapted language models uh were really key and most of them are still being used today as you probably know most of these you know Frontier models, language models are much better. They're pre-trained. They're frozen. And nowadays really much about having really good visual encoders and having good adaptation into these um pre-trained language models. So you can see some examples like this where you can start this is a very early model called Flamingo uh which is a precursor of some of these Gemini models. Uh you can give it an image and you can ask it what's happening in the image and they will say this is a picture of two teddy bears on a moon. What are they doing? They're having a conversation. What object are they using? It looks like a computer. So,

### [1:01:59](https://www.youtube.com/watch?v=H9nvkyTsrnI&t=3719s) · b000073

pretty good grounding and description of images. This one, uh, you can ask the model what it is. Uh, the model will say, "This is an Apple with a sticker on it." And the sticker says, the sticker says iPod. Uh, this was a joke because previous image recognition models, if you gave it this image, they will actually say the Apple iPod phone instead of identifying that it was a adversarial Apple with a sticker of iPod on it.

### [1:02:31](https://www.youtube.com/watch?v=H9nvkyTsrnI&t=3751s) · b000074

So based on this, because the framework is so simple, there's been a lot of open- source implementations of these adapted language models. Mini GPD4 is one example, very simple. So image comes in encoded by a pre-trained and frozen Q former and VIT. These are image representation learning models that gives you some feature. Uh this feature goes through a linear layer that basically changes dimension from the image feature embedding dimension into the language model token dimension just a linear transformation. And then the language model is Vikuna. That's a frozen model. Um, yeah, one of the open-source llama adapted language models. And so the only thing that needs to be trained in this is this orange linear transformation, right? For this to be successful, uh, two ways, well, two stages to train it. First stage is alignment. So I give it a bunch of

### [1:03:26](https://www.youtube.com/watch?v=H9nvkyTsrnI&t=3806s) · b000075

images and I give it captions of that image. So I would say this is a little purple icon that looks like a flamingo. This is a teddy bear that looks like a different icon. So, I'm just going to give it a bunch of images and there are captions and that would allow the linear layer to basically learn the mapping of visual features to token embeddings that describe the image. So, that's alignment using paired image text data. Uh you can think about that as your pre-training and in which case stage two is your finetuning or instruction tuning, right? Instruction tuning basically makes this model useful for downstream tasks because everything the model has seen during pre-training is just captioning images. Identifying this is a flamingo icon identifying this is something else. It's only able to caption images. But sometimes you want these models to actually do useful things. For example, uh assuming you

### [1:04:23](https://www.youtube.com/watch?v=H9nvkyTsrnI&t=3863s) · b000076

know it was an assistant, you might want to ask it a question. What do you think about this logo design? assuming you're some graphic designer and you want the model to say uh the logo is simple and minimalistic and you know it's well designed and and whatever. So these are actually instructions that you want the model to accomplish, right? So during stage two instruction tuning, what you're going to do is that you're going to give the model images, sample instructions you want the model to complete and human expert completions of these instructions, right? You might get a graphic designer to actually annotate some of these for you. So then you would give that as the image, you will give the instruction and you ask the model to predict this. So stage one can be seen as pre-training just aligning image and text. Stage two can be seen as um adapting it for instructions and tasks that people might actually use the model for.

### [1:05:20](https://www.youtube.com/watch?v=H9nvkyTsrnI&t=3920s) · b000077

Any questions?

### [1:05:26](https://www.youtube.com/watch?v=H9nvkyTsrnI&t=3926s) · b000078

And this works. And this works surprisingly well. Seems like a linear layer is all you need to to map between again very different visual pre-trained representations and something that can u be understood as input by these language models. More examples. Llama adapter is a large scale open-source framework that people have developed. I basically adapted all sorts of different modalities into llama open source models. So they've adapted a point clouds. So you can say generate an image from the 3D point cloud. So these 3D point clouds go in, you define an encoder for 3D point clouds, right? You get some feature and you adapt it into the input for llama. And there's some stuff they did obviously at the output as well. So it doesn't just generate text can also generate images. We'll get to that later. So you can adapt 3D point

### [1:06:23](https://www.youtube.com/watch?v=H9nvkyTsrnI&t=3983s) · b000079

clouds. You can also adapt in this case different languages. You can add some adapter tokens and uh the model can start understanding different languages.

### [1:06:37](https://www.youtube.com/watch?v=H9nvkyTsrnI&t=3997s) · b000080

Okay. So again let me also make the distinction. you know this this pre-training stage for these models and instruction quing stage the pre-training stage typically involves lots of image caption pairs right that is the easiest amount of large scale data you can get um larger and larger image caption data sets have been released over the years largest one right now is data comp 12 billion pairs of images and captions uh this allows you to basically learn these adapters that take in the image and the model is trained to just caption describe it. You can think of it as alignment problem. And stage two, uh, instruction tuning or fine-tuning, right? In this setting, now you actually want the model to do useful tasks because we don't want these vision language models to always just caption. You might ask them to um, you know, uh, solve solve math problems looking at

### [1:07:34](https://www.youtube.com/watch?v=H9nvkyTsrnI&t=4054s) · b000081

some image, you know, be able to diagnose some some x-ray and diagnose patient conditions given x-rays. So a bunch of these instruction data sets have been curated where you have the image some task and some completion the right answer and maybe a description of why that is the right answer for the task and that's usually goes into stage two of training.

### [1:08:02](https://www.youtube.com/watch?v=H9nvkyTsrnI&t=4082s) · b000082

Okay. Uh we only have five minutes left. So instead of going into stage three which would take more time uh I'll just end the lecture here and see if folks have any questions about what we've presented today. To summarize so far again we we recaped fusion we recaped alignment and then we started talking about these large multimodal models where in the first step it was about you have all these different data modalities often time treat them as sequences right it's a very natural data form especially because we're often interacting with these models through time uh once you have sequences these multimodal transformers are a good way of aligning the elements in these sequences and using the alignment to learn better representations. Extending what we discussed in the alignment where the alignment isn't the end goal but it's some intermediate step

### [1:08:59](https://www.youtube.com/watch?v=H9nvkyTsrnI&t=4139s) · b000083

to learn better representations knowing how the elements are aligned with each other. And then we discussed this second part where once you have these representations, how do you inject them into language models, right? And we saw this pretty generic framework of primarily keeping the language model frozen already. Very good. Don't want to update it too much. You don't have the resources to update it. In any case, uh you can keep the representations frozen as well and just learn this linear mapping which is what we call an adapter from these representations into the language model input space. Um and then you can train it basically with your your two stages. Right? This is a linear mapping into language model input space. You first train it by pre-training with images and captions and then you start fine-tuning it with images, instruction tasks and completions of those instructions.

### [1:09:54](https://www.youtube.com/watch?v=H9nvkyTsrnI&t=4194s) · b000084

And then um when when folks come back uh we'll discuss this third part which is you know extending multimodal input to text output to also have multimodal outputs. So you have truly interactive multimodal input output systems. All right. Um okay, you all are free to go if there's no other questions. I'll be around for office hours if folks have any questions about the homework, about the projects. Thanks everyone.
