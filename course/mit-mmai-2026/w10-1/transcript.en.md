# Lecture 10 – Multimodal Interaction (MIT How to AI Almost Anything/Multimodal AI, Spring 2026)

_English transcript_

- Channel: Paul Liang
- Source: [YouTube](https://www.youtube.com/watch?v=Sk_TYpA6DWA)
- Duration: 1:14:09
- Caption source: automatic
- Status: complete
- Chinese translation: 89/89
- Translation provider: codex
- Generated: 2026-09-07T07:59:17+00:00

## Transcript

### [00:00](https://www.youtube.com/watch?v=Sk_TYpA6DWA&t=0s) · b000001

Okay. So, first a recap of some assignments. Uh, we've graded the midterm, most of them, apart from the couple of you who did their makeups last week. Um, everyone did really well. Mean was 84, median was 85.7. Couple of folks scored above 100 with the bonus question. So, everyone did really well. Congratulations. Uh, the project midterm is due today. So that will be submitted in groups. Just go into Canvas, have one person in the group submit on behalf of everyone else and to tag your groupmates names on Canvas so they get to see all the feedback and grades. Uh just as a recap, this project midterm should be six pages and it should cover an introduction and motivation to your problem. uh the data sets they're going to be using processed baseline methods already run on the data

### [00:55](https://www.youtube.com/watch?v=Sk_TYpA6DWA&t=55s) · b000002

sets and with some preliminary results on the baseline methods when they work when they fail error analysis and use that as a as a segue for motivating your approach okay so that's your assignment that's due for the project midterm today yes uh I think we have to grade a couple couple stragglers who just finished their makeups late last week. Should be out soon. The median is 84, median is 85.7. Couple people got above 100. So overall grades were were very good. Um so after your project midterm is submitted today, we'll be releasing homework four either tomorrow or Thursday. It would be about uh using RL design designing reward functions and training reasoning based multimodal models. It' be a shorter homework probably one and a half weeks to be a

### [01:53](https://www.youtube.com/watch?v=Sk_TYpA6DWA&t=113s) · b000003

shorter one as people ramp up their their projects and then we'll have one final homework which is homework five on interactive agents which will also be a a slightly shorter one and a half week homework. Okay. Uh and just to recap, the final uh the final other assignment that will be due will be the final project report which will be the last week of class with a poster presentation that Tuesday of class and then the project final report will be due a few days after that. Okay. So just project midterm homework four and five both relatively shorter homeworks and your final final reports. Any questions about the assignments?

### [02:37](https://www.youtube.com/watch?v=Sk_TYpA6DWA&t=157s) · b000004

All right. So let me quickly recap. Uh last week we started discussing reasoning and reasoning refers to this type of problems where you have to synthesize different forms of information. You have to combine it usually over multiple inferential steps that takes into account some structure of the problem. Uh so we gave a schematic like this where linking it to the first half of the semester. We looked at you know for different modalities how do you look at individual elements so one word one image and how do you learn these local representations across these basic elements. We saw examples of a fuse representations or a line representations and so on. And then we extended this to uh more elements. So maybe a sequence of words that a person is saying or sequence of objects in an image. Now you have this alignment problem where you have to match up information from one of these elements to another.

### [03:33](https://www.youtube.com/watch?v=Sk_TYpA6DWA&t=213s) · b000005

And often times that gives you multiple degrees and resolutions of information that you then have to reason over. How do you reason over these multiple steps of information systematically in order to make the right uh prediction or multi-step decision? So that's the definition of reasoning. Uh obviously most people have seen reasoning in language models. So in reasoning and language models you have some input which is some question or some prompt and reasoning can be seen as just multiple linear chains of thought right uh step one step two step three this is commonly seen in for example solving a math question where you have multiple steps of equations or writing code where you may have to start planning out the structure of your code before filling out individual pieces of code. So you have multiple reasoning steps before you go to the output. And we also saw at a high level different uh three different ways of

### [04:29](https://www.youtube.com/watch?v=Sk_TYpA6DWA&t=269s) · b000006

achieving reasoning. One way is to just directly prompt your model. Prompt your model to uh think step by step to break down the problem without training the model or without updating the model in any way. Right? This has worked in language and it has also worked in many multimodal settings. We saw these examples where in robotics for example, you want the robot to clean up your kitchen, right? That's just a language prompt and the lang the robot has some uh based on the the language model inside of it has some basic information that cleaning up the kitchen requires washing the dishes and then loading the dishwasher and then you know vacuuming the space for example. So those would be your intermediate steps and then each of these local steps could then be executed by a robot right a particular action of you know pressing the button on dishwasher or pressing a button on the the vacuum machine. So that's direct

### [05:24](https://www.youtube.com/watch?v=Sk_TYpA6DWA&t=324s) · b000007

prompting zeroot reasoning. We also saw how if you have these intermediate reasoning traces given as supervision right so either annotated by a human or through maybe textbooks or other examples then you could do supervised fine-tuning. So given the input you would just auto reggressively predict the first reasoning step then the second and the third until you get to your output. That is called your supervised fine-tuning approach of achieving reasoning requires having access to your your reasoning steps, reasoning traces.

### [06:00](https://www.youtube.com/watch?v=Sk_TYpA6DWA&t=360s) · b000008

And the third method which we primarily went in depth last week was using reinforcement learning. In this setting, you're not going to assume access to your reasoning traces. They only have a particular input and some particular output. You don't have these intermediate reasoning steps in the middle. oftentimes because it is difficult to get human annotations or to curate these reasoning steps. Now, reinforcement learning is really powerful because it can automatically infer these intermediate reasoning steps. All it needs is some metric on the output telling you whether these outputs are good and these other outputs are bad. We call that a reward function, right? Right? And just by optimizing this reward, the model can use reinforcement learning to automatically infill these uh intermediate reasoning steps.

### [06:51](https://www.youtube.com/watch?v=Sk_TYpA6DWA&t=411s) · b000009

We saw this uh really simple example of you know playing pong, right? So you have this kind of game where you kind of control the paddle and push the ball over to the other side is a classic example of reinforcement learning because you are moving the paddle up and down. Those are the actions you can take at every step, right? Sometimes you're lucky and a sequence of actions allows you to score a point against the opponent and you get a reward of plus one only after a long sequence of actions. And sometimes you're unlucky. You take a sequence of actions and the opponent scores a point against you. So you lost a point. You got a reward of negative one. So it's a classic example of reinforcement learning where there are some latent actions that you don't know what they are. They're not annotated, but only after a long sequence of actions, you observe some reward function, right? And we saw that a general way of essentially an algorithm for reinforcement learning is

### [07:48](https://www.youtube.com/watch?v=Sk_TYpA6DWA&t=468s) · b000010

called policy gradients. You're simply going to look at the reward, right? Plus one or negative one and weight that the log likelihood of updating these actions. So for the sequence where you won and you got a plus one reward, you maximize the lock probabilities of all these four actions scaled by the reward plus one. Right? So you're increasing the probability of those four actions. For the trajectory where you lost and you got a reward of negative one, you're going to also maximize the lock probabilities of those actions scale by the reward. But because the reward is negative one, that is equivalent to minimizing lock probabilities of those actions. So you're preventing the model from taking those actions again. It's essentially assuming equal credit, right? Each for each of the plus one or negative one, you're assuming equal 0.25 or negative 0.25 credit over your sequence of four actions.

### [08:46](https://www.youtube.com/watch?v=Sk_TYpA6DWA&t=526s) · b000011

So that's essentially the policy gradient algorithm, right? you have is your objective function which is equivalent to the log probabilities. So log pi which is your policy that outputs actions given states scaled by the reward which is R. Right? So intu intuitively the reward is positive you increase the probability of the actions that led to that positive reward. And if the reward is negative then you decrease the probability of the actions that led to that reward.

### [09:22](https://www.youtube.com/watch?v=Sk_TYpA6DWA&t=562s) · b000012

We also briefly mentioned how the raw reward itself may not be super meaningful. Right? Sometimes just by design of the environment rewards are always positive or always negative. Which means what is more important is whether the reward that you currently have is higher or lower relative to some baseline. So what that means is that you often take a reward minus a baseline reward which can be seen as the moving average of the rewards that it has seen so far. So that kind of standardizes everything towards zero using this moving average and just seeing for every step is the reward higher or lower right and that is the difference. If it's higher than the mean the reward will be positive and you're upweing the actions in that sequence. If it's lower than the mean, this will be negative and you're downweing the probabilities of the actions in that sequence. So commonly used baseline is some

### [10:19](https://www.youtube.com/watch?v=Sk_TYpA6DWA&t=619s) · b000013

exponential moving average of the rewards. And finally, as a final recap of last Tuesday, this is essentially the fundamentals of all this reinforcement learning for large language models that you see today, right? your gpo and other policy optimization algorithms. So what's happening here is that usually you have Q. This is your policy model. Your policy model in this case is your large language model where given a state which is the current state of the dialogue and all the history back and forth so far. Actions are just next tokens you can generate over the next sequence length. Right? So that's a policy model outputting actions given states. In this case both actions and states are are natural language. You would first sample multiple outputs. O1 through OG. G is your group size in your GRPO. These are G possible responses

### [11:16](https://www.youtube.com/watch?v=Sk_TYpA6DWA&t=676s) · b000014

that the model can currently output. Each of these outputs go into a reward model. So in some settings, the reward is trivial, right? In that example of palm, the reward is just plus one if you shot the ball over your opponent or negative one if the opponent shot the ball over your side. Uh, of course, in natural language and dialogue, the reward is not so easy to define. So sometimes people train a reward model which basically means you know they've collected data how people score dialogues with language models. These are good examples of conversations, useful examples. These are bad examples of conversations. You have that data. You can basically train a reward model that tells you for each of these possible completions of the dialogue what the reward is, right? Good or bad. So that part can be learned using a separate neural network. That's a reward model. This reference model as we discussed previously is the basically a previous

### [12:13](https://www.youtube.com/watch?v=Sk_TYpA6DWA&t=733s) · b000015

frozen copy of your policy which is your language model right and there's a KL term over there basically meaning these you know reinforcement learning updates for your language model shouldn't change too much compared to previous copies and frozen versions of the model these models are already pre-trained they're already pretty good I just want to view this reinforcement learning as a final fine-tuning stage so I don't want to change the model parameters to which therefore there's a KL regularization here. So reward models give you these different rewards R1 through RG one for each of the utterances or responses and then you get advantages. Advantages are what we saw in this previous slide which is the fact that the rewards themselves may not be the most informative. I should subtract some exponential moving average of the rewards over time. So this helps you to zero normalize each of the rewards into something which we call

### [13:09](https://www.youtube.com/watch?v=Sk_TYpA6DWA&t=789s) · b000016

advantages. So is it better on average than the average reward or lower than average than the average reward and that is used to update the policy model using a policy gradient equation. Okay. So basically the advantages scaled by your log probabilities of the tokens that you've generated in each of these responses. So that's what the buzz was all about in 2025. Reinforcement learning for large language models kind of explain basically from the basics of reinforcement learning from first principles with a bunch of curistics in the large language model world.

### [13:52](https://www.youtube.com/watch?v=Sk_TYpA6DWA&t=832s) · b000017

And finally uh final recap of last week both myself and Dimmitri gave some examples of how these kind of reasoning based LMS are able to make predictions but also be explainable in some way right explainable uh you know outlining the key details and medical data so that you know you can give it to the doctors or give it to the to the patients so they have more control and trust over the model. So I show some examples where you know given these visual X-rays the models could start captioning what is happening in the X-ray. Even given some of these uh medical time series the model could start explaining what time series it is and based on that whether the patient uh has high risk or low risk for certain diseases. All of this is inferred by reinforcement learning. Right? The model only has access to the input image and the sensor readings. And

### [14:49](https://www.youtube.com/watch?v=Sk_TYpA6DWA&t=889s) · b000018

the model is scored whether it gets the final answer correct or incorrect. It's multiple choice question of how how long the patient will stay in the hospital. So that's a multiple choice reward. And by using reinforcement learning to optimize the reward, the model is able to uh automatically infer all these intermediate reasoning steps that seem to be pretty good and at the same time maximizes the reward of answering the question correctly.

### [15:21](https://www.youtube.com/watch?v=Sk_TYpA6DWA&t=921s) · b000019

All right. Uh so all that was a recap of of last week you know looking at reinforcement learning reasoning and using reasoning as a medium for explanability across various multimodal tasks.&gt;&gt; Any uh final questions about last week before we move on to this week's content?&gt;&gt; Yes.&gt;&gt; Yeah. So usually the reward is simply plus one or zero if the output is correct or not but it's still not very unless you put the rewards for length of the generated phrase. So why does having zero and one actually stimulates the heat and not stimulates the briefly answering but correct?&gt;&gt; Yes, great question. Uh so to clarify the rewards may not just be zero and one. So in this work that we did reward was actually quite complicated. There

### [16:16](https://www.youtube.com/watch?v=Sk_TYpA6DWA&t=976s) · b000020

were three terms right and each of them had a different weight. There was a weight of 6 to the first term which is whether the answer was correct. That's the most important. There's a weight of 02 on whether uh the textual reasoning matched the visual bounding box. Right? So this is highlighting some pacemaker. The text should be discussing something about a pacemaker. So there was some vision language alignment reward and there was another reward which was the length reward. Uh people find that the length reward somehow makes a quite a big difference in these models. So you want it to be maybe above a certain word limit but below something else. Um so it was like 6 for the accuracy 2 for the visual text alignment and 2 for for the length. And it can be even more complicated right uh you know lot of works you know since this stuff came out

### [17:13](https://www.youtube.com/watch?v=Sk_TYpA6DWA&t=1033s) · b000021

naturally one area where people innovated was to design good reward functions for various settings reward functions can be learned by the model it can be a human in the loop it can be um I mean your answer your question have two parts so first of all yeah it can be quite complex rewards and then also but in the end the rewards are still Even if you add up all these different things, they're just a number, right? I guess it's quite magical how just optimizing a number can lead to all of these things coming out, right? Um, which is a mystery. There's a debate among you know SIS since this stuff became popular in 2025 whether reinforcement learning and reasoning is actually adding new capabilities to the model or was it surfacing capabilities in the model that were already there just kind of making it more obvious to the surface. Okay, I think some people have a very hard time imagining just by maximizing this scalar quantity that you

### [18:11](https://www.youtube.com/watch?v=Sk_TYpA6DWA&t=1091s) · b000022

can somehow generate all of these beautiful explanations. So there are a lot of experiments that show uh even if you don't do RL you do maybe better sampling or you do better prompting you know the model can already get somewhere close to this reasoning capabilities. So perhaps a lot of the heavy lifting might have been done during pre-training or instruction tuning and maybe not in reinforcement learning. uh but that that is still open question obviously made very difficult because I mean none of these models you know what the pre-training data is or you know how they're structured too&gt;&gt; could you speak at all to the faithfulness of models we see that that's actually the cause of policy&gt;&gt; yes um just like language model hallucinations there might be hallucinations what we did is that We actually got a doctor to annotate and

### [19:08](https://www.youtube.com/watch?v=Sk_TYpA6DWA&t=1148s) · b000023

everything in pink highlighted here was what doctors annotated as uh feeling that they were useful and also accurate. Uh and then we had some metrics I think it was about 80 80ish% accurate um in the reasoning. So of course every five one of them might be mis accurate. I think Denitri also gave a another perspective on how they were doing it which is that they were using image captioning models on the image to get descriptions of the image and they were using some of the you know sense signal processing features right looking at the mean and the variance of the time series and presenting that to a doctor um and using LLM to kind of summarize and explain everything so they're also getting something like 80 90% accuracy so I wouldn't say it's always going to be 100% Um but it's getting there and of course you would expect the reasoning to become more and more faithful over time as as models improve

### [20:04](https://www.youtube.com/watch?v=Sk_TYpA6DWA&t=1204s) · b000024

and as you train the model more right that's key right at first you don't train the model just doing zero shot then yes it's going to be much worse when you start maximizing the rewards the faithfulness gets better

### [20:24](https://www.youtube.com/watch?v=Sk_TYpA6DWA&t=1224s) · b000025

okay So now we have seen models that take in arbitrary inputs and are able to generate all these different steps and give some output and naturally how do you build these uh build these models such that there's a feedback loop right as it generates a reasoning step you know it goes back new information to the model can generate new reasoning steps and then it takes new actions and more information goes back to the model so naturally you know there's a very close connection with models that do multi-step reasoning with models that are agentic, right? Agentic in the sense that there's a closed loop feedback from the actions that they're taking to new states in which they take new actions and go through new states. So that's a high level intuition of uh AI agents. I think this is a very messy space and everyone you know if reasoning was kind of the big thing in 2025 agents was 2025

### [21:20](https://www.youtube.com/watch?v=Sk_TYpA6DWA&t=1280s) · b000026

2026 and nowadays these uh continual learning evolutionary agents are a big thing this year. So we're doing active research in this but I also think it's a very messy space. Um I'm going to give my attempt at kind of categorizing this space and we'll see a couple in this lecture and also a couple in the final special topics lectures later in the semester. So one dimension you can think about these agents as how they grounded right there are agents that are purely language based right agents for answering questions about a document or about you know working uh to summarize different passages so manipulating text that's kind of the first level of grounding and then you have agents that are more operating in the digital space so you can think of these as agents that are manipulating spreadsheets and powerpoints on your computer or browsing through web pages and making some, you know, actions that can change things on

### [22:17](https://www.youtube.com/watch?v=Sk_TYpA6DWA&t=1337s) · b000027

a computer. Okay, so going beyond just manipulating text to manipulating actions in a digital space. Uh, and then you have embodied agents. So now these agents start having a body, right? It may not be a humanoid, but it could be like a a Roomba, it could be like a robot dog, it could be a gripper, robot hand, it could be a humanoid. Um, and now they have some body. So in which they're acting on the environment and receiving feedback from the environment. And finally, you have these like world models, right? Where models are much more grounded in the entire world. So these could be much totally humanoids that can not just do a single task in some manufacturing environment but actually going around helping people, helping us in schools, workplaces, hospitals and so on. So that's one degree of categorization. Another degree of categorization is the structure of these agents.

### [23:14](https://www.youtube.com/watch?v=Sk_TYpA6DWA&t=1394s) · b000028

At the most simple level, you have just a model, right? Agents where it's basically just the model either large language model or vision language model or other multimodel LLMs where they basically interact through prompting or images and the output actions that are being taken in the world. So that's the kind the first most simplistic layer of these agents. You then have another layer of agents where there is some workflow around these agents, right? Maybe a workflow will be a set of pools that you give the model access to. It could be a set of APIs where the model can write code to interface with, right? These are workflows. These are things on top of the base model, but also other tools, no applications, memory systems, file systems that you're giving a model access to. this workflow often times these workflows are designed by the person right so if I want to use if I want the model to use a calculator to do

### [24:11](https://www.youtube.com/watch?v=Sk_TYpA6DWA&t=1451s) · b000029

mathematics better then I can design this calculator wrapper and API on top of the model but that changes when the agent can automatically optimize its own workflow right now we have seen a lot of progress in these frameworks where the agent is not just limited to the one calculator tool you give access to basically everything on the computer and it could automatically figure out right in this case I should be using a calculator in this other case I should be using a spreadsheet in this other case I have to draw a diagram so it automatically orchestrate uh the tools at his disposal and optimize that for some particular task right so that's kind of workflow optimization goes another level of of autonomy and finally these self-evolving agents where not only can the agent optimize on workflow but also optimize tasks that is trying to tackle spawn out new agents that each have different

### [25:07](https://www.youtube.com/watch?v=Sk_TYpA6DWA&t=1507s) · b000030

tasks. Uh delegate own memory system so that you can store information. All of these without having the user say you have to use a memory or you have to spawn different sub aents. Uh and of course that's the frontier where you're going towards even more autonomy and it's possible these agents can do much more than initial user instructed them to do. Okay. So that can be thought of as a structure just like the reasoning structure that we discussed. And finally we have perhaps also very key which is the interaction with people right and as for example industry is really iterating on you know better base models better agentic workflows I think it's obviously very important for for us to think about and different businesses to think about how to integrate these agents into their workflows. Um, we've seen examples of autonomous agents, right? Models that basically

### [26:04](https://www.youtube.com/watch?v=Sk_TYpA6DWA&t=1564s) · b000031

operate by themselves. They try to complete the entire task and at the end they maybe return the output either success or failure to the user. Everyone knows that this can be useful sometimes but most of the times doesn't work super well, right? Then you have examples like human in the loop where the agents don't try to solve the entire problem but they only try to maybe take a small step that the humans delegate to the agent or maybe proactively decide to take a step which you know the agent believes that the user needs help with. So human in the loop can be both reactive and proactive, right? Reactive in the sense that humans are delegating some small part to the agent and proactive if the agent kind of intervenes and knows that this is a part that they are confident automating and it saves the time of the user. I mean over here most of you have probably seen a very big difference between for example how Devon turned out and how cursor turned out right back

### [27:01](https://www.youtube.com/watch?v=Sk_TYpA6DWA&t=1621s) · b000032

when these coding agents were really popular. Devon's approach was to try to build the most autonomous and most accurate coding agent. Right? So given a problem or any hard problem that the coder threw threw at these agents, they'll try to think, they'll try to do things. And these were very expensive, very complicated models. And of course, it was great when they succeeded, but oftentimes they failed. And when they failed, this dump this huge compiler trades and failed test cases back to the coder. And the coder had no idea what to do with it. Even when the answers seem correct, there might be very subtle bugs because it's huge chunks of code might be very subtle bugs inside of it. So that was Devon's approach. Try to be overly autonomous, you know, spend a lot more time engineering the models and at this and it was not the best use or interface for the user. And then we had examples like cursor and cloud code where the models wouldn't really try to

### [27:54](https://www.youtube.com/watch?v=Sk_TYpA6DWA&t=1674s) · b000033

automate everything, but they just try to automate kind of one small step of the problem. they'll kind of be like autocomplete for your code, right? They see that you're trying to write a sorting function and maybe they just automatically ask if you want to fill out the sorting function for you and the user could see this small kind of like transparent piece of code they had written and just accept it or reject it. Or if they saw something that was a PR or a bug fix, they will maybe suggest how they will do it again and ask the user whether they should accept or reject that uh that proposed solution. So these agents are much more human in the loop, right? just kind of proactive. They kind of decide when they could help the user and give out that small piece of help. And first of all, that made these models much easier to train. They just had to write small pieces of code. And at the same time, it was also much better user experience, right? You're not looking at huge chunks of of

### [28:44](https://www.youtube.com/watch?v=Sk_TYpA6DWA&t=1724s) · b000034

compiler dumps, but just small pieces of code and you could very quickly verify whether it was good or bad. And of course, most importantly, you've got all this user data while interacting with cursor, right? You've got all these accept, reject, fixing bugs in in cursors code. You've got all this interactive data that helps them improve the model. So, those are examples of going from autonomous to human in the loop and of course eventually, you know, co-living and coexisting with with AI agents.

### [29:17](https://www.youtube.com/watch?v=Sk_TYpA6DWA&t=1757s) · b000035

Any questions? Yeah.&gt;&gt; Do you think people are bottleneck like individually?&gt;&gt; I think in many settings they are, right? We're obviously much slower in our reading, in our typing capabilities than AI can be, right? uh but at the same time there's going to be many settings in which the human decision maker cannot be taken out of the equation. So while those policies and laws are in place, it'll be bottlenecked by human processing speed and human judgment speed. Same reason why um I mean same analogy as you know right now we have this weird mix where we have like 10% self-driving cars 90% human drivers and there's conflicts but it was 100% self-driving

### [30:12](https://www.youtube.com/watch?v=Sk_TYpA6DWA&t=1812s) · b000036

would obviously have much better and much safer roads I don't know I'm assuming don't quote me on that&gt;&gt; okay so Let's start diving into some of these these agentic models, right? Starting with language agents and digital agents. Uh and then we'll move towards some of these more embodied agents. But many of the same principles apply, right? And of course there's a huge demand for these language agents, right? Many tasks that people do for for for work, for profit, for creativity, they're all done on the computer, right? And many of these are done on various applications, on various websites on the computer, right? and and all this research in AI just started because there's such a huge opportunity to automate a lot of these menial tasks on a computer so you can save people's time have them work on more complex

### [31:08](https://www.youtube.com/watch?v=Sk_TYpA6DWA&t=1868s) · b000037

interesting tasks right so so tasks like you know going through and checking how much uh uh credits you're using on AWS or you know setting up different configurations on these different browsers tasks like you know logging data into your spreadsheets and then organizing and visualizing them and and making PowerPoint. I think people have summarized that probably 80% of of the workforce is doing some of these uh tasks that could be reasonably automated by AI agents. So that's where the first setting um first set of environments were designed for. So web arena is uh one of the very early environments where users would just give instructions to some of these AI agents. For example, uh if you're doing this online shopping task, right, maybe your task is to purchase a set of earphones with at least 4.5 stars in rating and ship it to you and give that

### [32:05](https://www.youtube.com/watch?v=Sk_TYpA6DWA&t=1925s) · b000038

instruction to the agent. And the agent should be able to to see visually what is on the web page, right? You know, which are the earphones and how many stars they have and how many ratings and the price. And the agent should be able to kind of click and scroll and type and do all the things that you would do on this web page, right? So ideally it should search for earphone. It should filter, look at the stars, add it to your cart, might have your address already saved there, and then you check out and maybe right before you check out, you confirm with the user this is something that they that they want.

### [32:41](https://www.youtube.com/watch?v=Sk_TYpA6DWA&t=1961s) · b000039

So this is the promise of of AI agents and the web arena environment was a big step in this direction. So they got data from various kind of websites. So, online shopping, uh, Reddit, GitLab, uh, all these kind of environments and these were basically clones of the, uh, actual websites, right? Because if you actually use, for example, Amazon or or GitHub, you would kind of get banned after a while for too much traffic. So, it was a kind of clone of the website. But uh they were logging data to give real to actually get realistic scenarios from actual products that people would be buying or actual uh pull requests that people were making on GitHub. Now these tasks are easy for humans. So humans can do them at 78% success rates and in fact even higher I think when they're doing these user studies. Most of the failures were just people forgetting to kind of click checkout at

### [33:36](https://www.youtube.com/watch?v=Sk_TYpA6DWA&t=2016s) · b000040

a final step or making booking mistakes. So these tasks are pretty easy for people and at that time it was quite difficult for LLM agents in 2014 about 14% success rate for these LLM agents. Right? So the first iteration of these agents operated purely on text. So instead of actually seeing the website uh they would just operate using HTML, right? And all of you probably know HTML. It's super messy. It has lots of these tags, lots of redundant characters. Um, the spatial layout is not conveyed at all, right? No one can look at HTML and tell you what's on the top left or bottom right of of the image. The context length was huge, right? So, one HTML page, if you're just storing in text, can easily fill up 100k tokens, right? So, the model, even the longest models with context lengths, wouldn't really be

### [34:31](https://www.youtube.com/watch?v=Sk_TYpA6DWA&t=2071s) · b000041

able to store multiple links between multiple pages. So there was an interest in going beyond just language models and LM agents operating on HTML to multimodal agents that can see and perceive these websites and their kind of spatial information and their color information and their overall user interface and layout. Uh just like how people can, right? You compare this website with HTML. Of course, this is how we operate. And if you have a model that you know looks at this image, you can just encode it using one visual encoder and get one representation instead of wasting 100k tokens on processing HTML.

### [35:18](https://www.youtube.com/watch?v=Sk_TYpA6DWA&t=2118s) · b000042

So after web arena came visual web arena. So visual web arena was a benchmark that followed some of the procedures for web arena right so tasks are quite similar. There were web browsing, there was commenting, there was online shopping, there was coding. Um, tasks were very similar. But now all of these tasks now require visual information, right? And the goal is to train vision language model agents and could process these visual websites and solve tasks based on vision. So it was designed to benchmark and track the progress of these multimodel agents. It's still access to different information sources. There was the the raw visual output. There is the HTML and there's this thing in between which is called the accessibility tree of a of a website which is something in between. It's like a cleaned up version of HTML that makes it much easier to read by a

### [36:13](https://www.youtube.com/watch?v=Sk_TYpA6DWA&t=2173s) · b000043

human. So they benchmark these approaches as well. And over here you can see the list of actions that a lot of these uh AI agents for the web can accomplish, right? Things like click over some element, hover over an element that sometimes can be different from clicking uh you know opening up a new tab, going back and forth between tabs, scroll through different websites. Um so these are different tasks. This is action space of these agents.

### [36:44](https://www.youtube.com/watch?v=Sk_TYpA6DWA&t=2204s) · b000044

So, Web Arena contains all sorts of different tasks across different sites, shopping, Reddit, Losify, uh some of these bargaining websites. And these are distribution of tasks by difficulty, right? So, easy tasks can be solved using humans using a couple of actions and couple of clicks. Hard tasks require many more clicks. And also visual difficulty. For example, this is measured by how many objects and object bounding boxes were on these websites. So the more cluttered the website was, the more visually difficult it was. So here's an example in visual web arena. So now you have some some visual input and also in the task and also visual input on the website. So maybe a task is let's say you're chatting with somebody at a at a networking event and you want to you know keep their contact. So, you took a photo of their name tag and your task is to buy the cheapest

### [37:42](https://www.youtube.com/watch?v=Sk_TYpA6DWA&t=2262s) · b000045

color photo printer and send it to Emily's place as shown in the image, right? And the image is even upside down with their address on it. So, the model should go through, search for printer, color printer, sort by cheapest, order it, and then uh send it to to your new acquaintances place. Right? So you have to fill in the address with the address you deduced from the image.

### [38:23](https://www.youtube.com/watch?v=Sk_TYpA6DWA&t=2303s) · b000046

Okay. So how to evaluate right. So a lot of these agents are evaluate in this way. So you have these input tasks, the websites, you have the task and then you let the agent kind of go through and and basically the agent has to self-report that it has completed the task and once it has completed a lot of methods basically do this automatic evaluation right where they're basically using things like reg x or if else statements to check whether the final state that the action the final state that the agent is in matches what is desired. So if you're if you're trying to for example search uh search for something then you basically will check that there's an exact match between the output that you searched and the search term that you gave. Right? If uh you're trying to navigate to a certain URL then you check that the URL is correct and

### [39:21](https://www.youtube.com/watch?v=Sk_TYpA6DWA&t=2361s) · b000047

that it includes for example that the price is 5,000. So it checks that. So it's basically doing all of these you know final checks to check that it meets the specifications of the task. So that will be a final reward function. So since visual arena a lot of other environments have also been released. So OS atlas is one that goes even beyond just simple websites to all sorts of computer operating systems. uh it includes for example uh when you're using your browser right Linux I'm sorry your your desktop Linux desktop Mac OS desktop Windows desktop it includes on your mobile phone different user interfaces applications browsers that you might be using on your phone all these forms of visual information is included in this benchmark and all sorts of tasks are defined for these different environments

### [40:19](https://www.youtube.com/watch?v=Sk_TYpA6DWA&t=2419s) · b000048

All right. Any uh any questions about these different web agent environments? Yes.&gt;&gt; I guess in the previous case it say what it ends up learning is a special thing cheaper printer and then say there's a new cheaper printer that comes out in the market. Will it go back to the original one or does it actually learn the path to find the cheapest people?&gt;&gt; Ah, great question. Current agents, no, right? Because these agents are I mean, if you delegate and you give them the task and it does and it searches for the cheapest printer today, uh they're not going to be proactive enough to alert you next week that another cheap printer came out on the market. It probably wouldn't make sense because you already bought the printer. Um, so we don't yet have these kind of more proactive agents, right? I mean comes up with very

### [41:15](https://www.youtube.com/watch?v=Sk_TYpA6DWA&t=2475s) · b000049

interesting research questions which is how do you save time and cute when agents always running now you're prompting they're using a token so they cannot be searching and finding the news for new printers each time right and also when when do they react when do they proactively suggest things to you? In this case, you've clearly already bought the printer, so you might not be interested in buying another one. But if you know, uh, paper becomes cheaper. Are they going to ask you to buy it? I mean, then you get into all these, you know, advertising, right? Which is how Open AI and probably is going to make make money in the future. They have to resort to advertising.&gt;&gt; Yes. Is there any like wish list agents or something like that where you know markdown file things that would want to buy right now and that is there like an architecture that could kind of you know test against your goals right which is buying this thing but not at a specific

### [42:10](https://www.youtube.com/watch?v=Sk_TYpA6DWA&t=2530s) · b000050

price and it just kind of like continuously scans the internet.&gt;&gt; Yeah.&gt;&gt; Yeah. I mean similar to to uh the other student's question which is I think it's possible um computationally how would you designate agent to kind of keep searching and keep going through your wish list that provides some computational challenges but if there is a list to begin with then it's probably going to be easier right because it doesn't have to search through everything you just keep monitoring price or printer so I would assume that's that's pretty possible to build Yeah.

### [42:49](https://www.youtube.com/watch?v=Sk_TYpA6DWA&t=2569s) · b000051

&gt;&gt; Yes.&gt;&gt; Um I don't know what they are. Do you want to speak to it more?&gt;&gt; What do you call it? Data scraping.&gt;&gt; Yeah. Someone scrape signals for like stuff like that using a sounds because it could be scraping for a printer versus scraping for some other information. Yeah, I mean I'm sure it's easy to set up a bot that you know just tags a search term onto Google search or Google news or Twitter and searches every hour and refreshes your feed. So you may not even need agentic models for that.

### [43:37](https://www.youtube.com/watch?v=Sk_TYpA6DWA&t=2617s) · b000052

Cool. Okay. So, so we saw some of the uh the new environments, right? Language based environments, visual environments. We saw how accessibility trees and HTMLs were um usually unnecessary, usually lots of overly large context tokens and it's much more natural to work with uh images, right? Directly looking at the website. But of course, processing these websites are difficult, right? These are much different from natural images. So, you know, we still don't really have a really perfect encoder that we have for imageet. We have good encoders, but we don't have really good encoders for some of these websites, especially when user interfaces and design patterns and different text is all super small. Um, there's quite a lot of challenges in designing visual encoders for websites, but nevertheless, there's been lots of

### [44:31](https://www.youtube.com/watch?v=Sk_TYpA6DWA&t=2671s) · b000053

good progress. Uh this S Soom is called set of marks is a is a nice approach. You can think about it as object recognition for websites. So it's going to go through and it's going to look at all the text and all the links and all the places that you can click on and all the embedded images on your website. Right? So basically object recognition and segmentation for your websites in this case. Yeah, these are all the set of marks that a pre-trained model is highlighting along with the numbers and their locations of where these uh these things are. So that can be a good representation, right? Um and allows the model to basically decide, you know, over my action space which of these I should click or zoom in or or to click on. So then given this original web page you can first parse the web page by running

### [45:27](https://www.youtube.com/watch?v=Sk_TYpA6DWA&t=2727s) · b000054

these set of marks model to get all the possible actions and then give this particular query that's the task that you're supposed to complete to the agent and the agent can output a particular action. So here are some baseline agents. Um text only agents don't perform super well 10% pass completion rate text plus captions. So this would take the website and basically caption it using a best image captioning model and that brings everything to text and you operate LLM agent over it about 15%. Multimodal models are basically your adapter style models that have LLM agent and your website goes to an image and is adapted into LLM agents. So higher maybe 18%. And having set of marks on top of these visual representations that's a little bit better. So now it's like closer to like 19%. Of course, still a big gap to uh human

### [46:24](https://www.youtube.com/watch?v=Sk_TYpA6DWA&t=2784s) · b000055

performance which is you know almost uh above 80 85%. Yeah. And also you know you could look at some of these results in more detail but uh closed source models still work the best. For example GP4 as backbone and some of these visual backbones based on your clip- like models. Blip is just a modification of clip models. Um these were were getting the best. So the closed source models were still uh quite good at these agents. Overall best is multimodal model using vision and set of marks. So the object detection on top of these web pages for the encoder and that get 16% performance.

### [47:14](https://www.youtube.com/watch?v=Sk_TYpA6DWA&t=2834s) · b000056

Still a lot of good examples of success. So over here the task is you know you're on this uh this Reddit you don't like one of the posts uh that someone posted on this subreddit can you help me block them? So the model is able to go onto the homepage search for the subreddit navigate to the list of forums look for a particular thing you're looking for look for the profile click on a block button and confirm blocking the user. So there's some successful examples of even solving some of these sixstep uh agentic tasks which is quite difficult.

### [47:55](https://www.youtube.com/watch?v=Sk_TYpA6DWA&t=2875s) · b000057

All right. So what are some main challenges? Still main challenges that are still faced today. Perhaps the biggest challenge is how do agents perform this long horizon reasoning and planning. These tasks are still relatively simple, six, seven tasks and you know isolated for certain websites. Uh but real world tasks can be much much longer especially in their in the real world especially when they involve different websites when people are involved. These tasks will require much more steps of planning and executing each step. If the plan at the beginning was incorrect, how does the model replan and backtrack and try again? Right? When they are interfered and they get stuck, how do they figure out how to, you know, at inference time, how do they figure out how to succeed and get unstuck on different problems? So long horizon reasoning and planning

### [48:53](https://www.youtube.com/watch?v=Sk_TYpA6DWA&t=2933s) · b000058

is perhaps one of the biggest challenges in agent space. And the other big challenge is also failures in visual or by extension multimodal processing. Right? The LLM parts are usually in charge of this reasoning and planning but the other modalities are in charge of you know perception right we saw examples of how even these visual websites they're quite hard to process by different approaches and this not even getting to the complexities of real world vision or real world robotics and different sensors in the real world. So biggest challenge are language based long horizon reasoning and planning and from multimodal perspect perspective how do you do perception of these other modalities

### [49:41](https://www.youtube.com/watch?v=Sk_TYpA6DWA&t=2981s) · b000059

&gt;&gt; questions? Yeah&gt;&gt; um today or maybe 20 years ago started using the started adopting first sites to mobile, right? And like mobile.com, I guess would be like a slightly modified website. Do you have any data on like what websites do agents do? Well, so that we kind of like have some sort of like intuition like what visual cues work better, what kind of like layout works better so that you can have like this new wave of websites that if my agent browses it, it like a slightly different one.&gt;&gt; Yeah, it's a fascinating question. Um, I know this is active area of research, but I'm not really caught up with the specifics, right? Seeing people try to build,

### [50:38](https://www.youtube.com/watch?v=Sk_TYpA6DWA&t=3038s) · b000060

well, first I've seen people curate more and more data sets that are tailored for benchmarking and training agents. So I gave these examples but these have not really curated um you know the the websites or user interfaces very nicely right some people who spend their whole careers you know in HCI and data visualization designing layouts right front-end layouts now they're starting to curate different tonomies of how front end layouts can look like and studying which ones are more suitable and lead to higher performance of AI models. uh so I'm sure they have uh some exciting findings over there. Yeah. Of course at the same time you know it can't affect human perception of it. So it may be maybe in the end that you know there's a human version of websites and also AI version of websites right that that's a different&gt;&gt; Sure.&gt;&gt; How do you swear that

### [51:34](https://www.youtube.com/watch?v=Sk_TYpA6DWA&t=3094s) · b000061

LM agents are so good at front end development but so bad websites? I feel like they're quite good at sex.&gt;&gt; I don't know. Do people think they have an answer to that?&gt;&gt; Where's the text? Great. Twitter text, but like navigating the website&gt;&gt; perhaps. Yeah. But you know if the these LM coding agents are outputting HTML for websites in text so the question is you know why can't they process HTML as easily as they they generated it right. Um yeah I'm not sure.

### [52:26](https://www.youtube.com/watch?v=Sk_TYpA6DWA&t=3146s) · b000062

Okay so for reasoning and planning. So this is where again it links with what we've been discussing last week which is that how many of these objectives right these are very complex objectives they acquire long horizon planning. So nowadays most of these agents have a module that is just specialized at planning right it breaks down these complex objectives into high level plans right each one step at a time. So once you have this high level plan, you can then merge it with the observed web page and ideally do some really powerful visual processing either in visual space or some other abstract space that is most suitable for agents to get a representation of the web page given the plan and given the representation together come up with a low-level action. Right? So whereas high level plans to be like you know navigate to a certain website or something that is easier to understand more semantically meaningful low-level

### [53:23](https://www.youtube.com/watch?v=Sk_TYpA6DWA&t=3203s) · b000063

actions would actually be you know click on this coordinate with a search bar and type these characters. So those are low-level actions that can actually be operated by the agent. Um and then you would recurse, right? Recurse by going to the next observed web page that that action would then take you to look at the next high level plan and again get the next low-level action. So these are the loops that people are usually developing in these web-based agents. Uh I give an example. So without reasoning, you might give a model a task like buy the highest rated product from this Nintendo Switch pouch category within a budget under $60. Right? So the model takes in this instruction. If it doesn't plan, just tries to do everything in one step. It tries to search for something and then for some reason it gets stuck. It gets confused. It doesn't know what to do and it stops.

### [54:20](https://www.youtube.com/watch?v=Sk_TYpA6DWA&t=3260s) · b000064

Whereas ideally, you know, this is the model with a planning component. So first of all you would take the task you would break it down and say first search for Nintendo Switch pouch and then you should filter by a certain price and then you should proceed to your checkout for example. So the model then is able to execute each of these steps one by one. Right? First action is a searching action then is a clicking action and then is another clicking action adding to the cart and then another clicking action checkout. So that's the power of being able to plan out individual steps one by one so that the model can more systematically execute each of these actions. How to plan? You know I've given a lot of examples in the reasoning space right you can either just do a zero shot you can do SFT if you had for example ground truth plans that people have annotated you can do reinforcement learning uh given these final rewards as an

### [55:15](https://www.youtube.com/watch?v=Sk_TYpA6DWA&t=3315s) · b000065

incentive to infer these intermediate step-by-step plans here I'm just showing more examples um some of these are mixed of prompting based some of these are mixed of using tools these are all just kind of important papers in improving the planning capabilities of the web agents.

### [55:39](https://www.youtube.com/watch?v=Sk_TYpA6DWA&t=3339s) · b000066

All right,

### [55:45](https://www.youtube.com/watch?v=Sk_TYpA6DWA&t=3345s) · b000067

we discussed um some part of you know difference between fully autonomous agents and human loop agents. So naturally, you know, we want these agents sometimes to do everything, but sometimes the agents can also just generate different steps and have the person check whether they're on the right track. So if for example, uh this is a hard question. What is the price range of wireless earphones in this online market? Right? So the model might start planning and it searches for wireless earphones and it tries to look for price range but the price range isn't directly annotated on the website. Right? So the model gets stuck. Ideally what a human annotated plan would be is to search for earphones to sort it from low to high. Right? There's a sort button from low to high and then you get the first item and then you click sort again from high to low. You get the first item. So that gives you the lowest price and the highest price and then you

### [56:42](https://www.youtube.com/watch?v=Sk_TYpA6DWA&t=3402s) · b000068

kind of return those two numbers, right? That's ideally what a human plan would do. So models that don't plan get it wrong because you can't directly search for a price range. Models that uh even if you give it some examples, it just finds the price of either the lowest or the highest, not both. And here's an approach that we've developed for applying some of these few shot plans with human clarification. So the model might get the first plan correct and then the model struggles to ban the second step. So you give the model one human demonstration. So you take what the human has annotated as the right second step and give it to the model. Reveal it to the model. Right? that you have to first sort the earphones from low to high and then the model can continue on to generate the rest of the

### [57:39](https://www.youtube.com/watch?v=Sk_TYpA6DWA&t=3459s) · b000069

plan correctly, right? Automatically learns that it also has to sort the earphones from high to low. So even just one step of clarification from a human plan, they kind of steer the model in the right direction and have the model complete the rest of the task.

### [58:00](https://www.youtube.com/watch?v=Sk_TYpA6DWA&t=3480s) · b000070

&gt;&gt; Yeah. Sorry, I know the questions are like uh but when you're like you have planning modes with cloud code and things like that is it asking for these clarifications based off of like some low confidence. So it generates this plan and then it's doing this exact intervention intervention based off of what surface does confidence on that set.&gt;&gt; Exactly. Great question. um which links to my next slide which is when should a model uh defer or ask clarifications from people right I don't know of course how cloud code works or I guess we do know now with a leak uh so you know a lot of ways of finding out how the model defer is to basically estimate the uncertainty right uh what is uncertainty basically means you know when the model the model's always going to output something right ideally when the model is uncertain it will say I don't know But that capability is not yet in many models and that's a very difficult

### [58:57](https://www.youtube.com/watch?v=Sk_TYpA6DWA&t=3537s) · b000071

capability. But uncertainty basically means when the model outputs something how constant it is in that right. So one way of measuring uncertainty is just to resample the model multiple times with different temperature uh temperature settings. So the same temperature setting resample multiple times. If the model across multiple samples always says the same thing then you can empirically take it as a model being quite confident because it's repeatable. It's always saying that if you resample the model multiple times and each time it says something different, then you can take that as an approximation of the model not being super confident, right? Uh same thing applies to classifiers, right? Whether your softmax classifier is very peaked. So, so sampling from the softmax multiple times gives you the same output or if your softmax is more uniform, then you sample new outputs from the model every time you get different outputs. So uncertainty estimation is something

### [59:53](https://www.youtube.com/watch?v=Sk_TYpA6DWA&t=3593s) · b000072

that's quite critical in figuring out when the model should defer and get clarification from people. This kind of sampling method is also good because it requires only blackbox access to the model. You don't have to see model internals. You only have to be able to sample from it. Right? Downside is that it's slower. If you had pure access to the model, then you could look at right token probabilities in the final layer. Did that answer a question?&gt;&gt; Uh yeah, I think the last part is having some problems with if you're building a rafter,&gt;&gt; right?&gt;&gt; They have to do sampling based, right? Um sampling multiple times, seeing seeing what they what they say and now it's increasingly common, right? Not only is it common to resample for uncertainty, this resampling for RL training is super common. um resampling for various inference time search. So

### [1:00:52](https://www.youtube.com/watch?v=Sk_TYpA6DWA&t=3652s) · b000073

super common. That's why these models are using so many tokens and are so slow nowadays.&gt;&gt; Yeah.

### [1:01:04](https://www.youtube.com/watch?v=Sk_TYpA6DWA&t=3664s) · b000074

Any further questions?&gt;&gt; Okay. Uh speaking of inference time search that is also a key ability that uh people are trying to build into these models right agentic models right we saw at a high level how the model can decompose complex instructions into individual plans and sometimes the model refers to search right because you can always cannot just always rely on planning before you do something when you're actually doing the task there might be different possible outcomes if you're uncertain you can just try both and see which one leads you to the right outcome, right? That's going to be quite important for for methods to work robustly in the real world. So here's an example task also quite difficult. How many times did I purchase this product? So that requires a model to first

### [1:01:55](https://www.youtube.com/watch?v=Sk_TYpA6DWA&t=3715s) · b000075

navigate to my account, look at uh my orders, right? Uh so go to my orders and you can also try clicking into my downloadable products or my wish list. that the model should know understand that that's not the right search path right within my orders. Um there's a lot of things to try. For example, the model could try actually viewing each of orders and it has to then click inside and check whether uh it was the same product as the one that I am asking about. And then he has to go through all of these orders. Right? That's why you can see it's a quite quite a hard task. So for each of them it should click and for some of them it should tally and for some of them it shouldn't tally because it was a different product. So this is all you know a complex real-time search problem where certain trajectories the model should prune with some value

### [1:02:51](https://www.youtube.com/watch?v=Sk_TYpA6DWA&t=3771s) · b000076

function which you can think about as your reward estimating how likely going down this search path would be in solving the task and some other ones it will also prune and some of the other ones it would it would keep searching. So here's a good example right you'll have over here on the x- axis number of times you are searching and in this case searching just basically means uh how many times you are sampling action trajectories from the model right in this uncertainty uh manner. So you each time you sample sampling four times basically means you give the agent four tries right to sample four trajectories each time the model would try one of these four in parallel and you just take the one that succeeds if any one of these four succeeds right so in green line this is the model that we started with which is Gemini plus your set of marks and this red line is uh the

### [1:03:47](https://www.youtube.com/watch?v=Sk_TYpA6DWA&t=3827s) · b000077

state-of-the-art model so back then it was GPT4V with your visual encoder and you start with one sampling exactly where the model starts. But if you sample more times and you just take this best of n right majority best of n then eventually the more times you sample you see this monotonic increasing trajectory as you know more and more likely to get uh one successful trajectory over those samples. Right? There's a very you know preliminary result promising these these folks show some of these results. But that also means that a key research question is to well how to decide what to sample efficiently so that the model doesn't grow slowly as you have more samples but uh grows much faster as you have more samples. And that requires the model to learn a good value function, right? To prioritize what to search over and also a good ranking function to

### [1:04:42](https://www.youtube.com/watch?v=Sk_TYpA6DWA&t=3882s) · b000078

determine which of the trajectories are are the best. Okay, this uh it's called best of end sampling. Um yeah, very very important nowadays as well.

### [1:05:04](https://www.youtube.com/watch?v=Sk_TYpA6DWA&t=3904s) · b000079

All right, one final one final thing that I want to show. So we've discussed of course the base agents agents with you know planning one of these high level tasks with humor in the loop clarification with searching strategy so you're sampling output multiple times obviously memory is going to be so critical for these agents right uh these agents are operating over longer and longer horizons if they're searching and using human feedback those are just going to all add to the model's context length And we know that as these models their context length increases right you have slower slower inference which is you know scales as n square with a context length and also more critically you tend to forget information you can forget information from the past with a long context ago. So nowadays a lot of people are integrating memory into these

### [1:05:59](https://www.youtube.com/watch?v=Sk_TYpA6DWA&t=3959s) · b000080

models. Ideally, a memory based agent will be able to dynamically decide when to store things into memory and also more importantly to throw things away from memory so that roughly the memory usage and the context window stays at a constant state despite the agent being run over very long durations. \[clears throat\] So one thing that some folks in my group did was to build this um memory efficient agent which basically adds this internal state to the context window of the agent and this internal state is always being updated with the most recent information and at some duration the agent decides to also throw away this internal state. So what it looks like is this. So at every iteration from perm t minus one to t is taking the previous queries and

### [1:06:55](https://www.youtube.com/watch?v=Sk_TYpA6DWA&t=4015s) · b000081

information and context at time t minus one and storing it at the internal state of time t right and this recurses uh the internal state at time t is used to perform the next step of decision making and once the next step of decision making is done it's going to restore all the query and the current state into the internal state of time t + 1. So the internal states capacity or length is always fixed and it's always being updated and you know removed at each step. So visually it looks like this. The existing models on the left they always just accumulate more and more information whereas our models just keep one internal state and force the model to throw previous information away.

### [1:07:49](https://www.youtube.com/watch?v=Sk_TYpA6DWA&t=4069s) · b000082

So in answering multiple questions, you see it's able to process documents faster, keep a shorter state, and get uh more questions more accurately.

### [1:08:05](https://www.youtube.com/watch?v=Sk_TYpA6DWA&t=4085s) · b000083

All right, we're almost out of time. So, um, any questions about this this memory agent?&gt;&gt; Yeah, sure.&gt;&gt; Yeah. So, when you have an internal stage, is it like a markdown file just like condenses what it's seeing or is it actual like vector that represents what it's doing? It's not a markdown file. It's just text, right? The context text. Yeah. Uh we have some recent work on kind of extending some of these to to more um more agentic workflows where now you you have access to various uh markdown files. You have access to some you know summarization codes and so on. So makes this even more efficient and also for multiple agents. So they can keep each uh reading and

### [1:09:02](https://www.youtube.com/watch?v=Sk_TYpA6DWA&t=4142s) · b000084

writing to this shared memory and this shared memory has this uh this markdown file. Exciting stuff. All right. Okay. One final thing I want to mention is also the extension to the real world. Right. I mean most of the principles still apply. So you have visual inputs that the robots are seeing, right? You have natural language instructions that people are giving to these agents and you have these agents that want to have you take various forms of actions, right? So vision goes to vision transformer and adapted into the llama model. These are your adapter style approaches. Uh is a vision language model and the biggest difference is now it's a action output, right? So not text output but an action output. And in this case action output usually means various degrees of freedom on the robot your joints or your force or your torque

### [1:09:59](https://www.youtube.com/watch?v=Sk_TYpA6DWA&t=4199s) · b000085

angles. Uh these are numerical outputs right so this called a VA vision language input and action output. Uh so it inherits a lot of the good properties of you know language based reasoning uh you know quick fine-tuning from base language models uh quick adaptation to different types of robots by just kind of again fine-tuning the the action decoder right you can do your Laura you can do your quantization all the standard techniques on language models so that these uh run efficiently so these are called VLA models um the most important part right I can I put the paper over here I'm not a robotics person but the most important part is perhaps that action d decoder or they call it d tokenizer right that is basically where the innovation is um from understanding it's very difficult to get language models to output numbers

### [1:10:56](https://www.youtube.com/watch?v=Sk_TYpA6DWA&t=4256s) · b000086

right all of you probably know that just even ask you to add a couple of numbers or do you know matrix or uh multiplication of different decimal points is often quite difficult. So this action detokenizer nowadays is done using using some diffusion model right diffusion model as you all recall is a generative model for much more suitable for continuous data. We saw when we introduced diffusion models they can defy images. So they can use calcium noise and decode and d noiseise image pixels. Uh so the diffusion models are very suitable for continuous data. So a lot of these action detoizers actually use diffusion models to essentially output these continuous action spaces like changes in your angles and your joints and your rotations of your robot. But otherwise everything else is the same, right? You have visual input, you have natural language instructions, you

### [1:11:54](https://www.youtube.com/watch?v=Sk_TYpA6DWA&t=4314s) · b000087

have these continuous action outputs. This whole thing can be trained. Usually it is a vision encoder can be fine-tuned to make it adaptable to your robotic seeds. The adapter which is the visual representation to the language model. The adapter will be fine-tuned. Most of the language model itself will be frozen and the action decoder using the fusion model would also be be either trained or fine-tuned. Great. Yeah. So there's more more examples. This paper includes you know large scale data with vision language input and ground truth actions. It includes open source code and includes uh various ways of kind of fine-tuning a model for different tasks.

### [1:12:47](https://www.youtube.com/watch?v=Sk_TYpA6DWA&t=4367s) · b000088

Right. Okay. So that's it. So summary, we've seen a couple of examples of, you know, AI agents uh starting from just language processing agents to digital agents and embodied agents. You know, these are just different examples of the the visual input space and the action space being different. We saw some examples of LLM and parts of these workflows, right? Some of the key things we highlighted were the planning capabilities of these models, right? taking in long instructions and using similar stuff that we saw last week of using either SFT or prompting or reinforcement learning to get the model to output step-by-step actions. Right? So this reasoning is very important. Visual representation is very important still a big challenge. Uh how to make it more human in the loop and how does it use search to try out different trajectories

### [1:13:44](https://www.youtube.com/watch?v=Sk_TYpA6DWA&t=4424s) · b000089

and that's a good way of improving performance. Right? and saw some examples how to interact like either autonomously or or keep human loop. Okay, we have a couple minutes left. Any final questions about this? If not, um remember to submit your project midterms and uh be on lookout for homework 4 that will be out later this week. Right. Thanks everyone.
