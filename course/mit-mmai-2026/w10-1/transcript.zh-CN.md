# Lecture 10 – Multimodal Interaction (MIT How to AI Almost Anything/Multimodal AI, Spring 2026)

_中文讲稿_

- Channel: Paul Liang
- Source: [YouTube](https://www.youtube.com/watch?v=Sk_TYpA6DWA)
- Duration: 1:14:09
- Caption source: automatic
- Status: complete
- Chinese translation: 89/89
- Translation provider: codex
- Generated: 2026-09-07T07:59:17+00:00

## 讲稿

### [00:00](https://www.youtube.com/watch?v=Sk_TYpA6DWA&t=0s) · b000001

好的。那么，先回顾一下几项作业。呃，期中考试我们已经批改了，大部分都批完了，除了你们当中上周参加补考的几位。嗯，大家都考得很好。平均分是 84，中位数是 85.7。有几位靠附加题拿到了超过 100 分。所以，大家都考得很好。恭喜。呃，项目期中报告今天截止，要以小组形式提交。进入 Canvas，让组里一个人代表其他所有人提交，并在 Canvas 上标注组员的名字，这样他们就能看到所有反馈和成绩。呃，再回顾一下，这份项目期中报告应该是六页，要涵盖你们问题的介绍和研究动机，呃，要使用的数据集，已经处理好的数据，以及已经在这些数据

### [00:55](https://www.youtube.com/watch?v=Sk_TYpA6DWA&t=55s) · b000002

集上运行过的基线方法（baseline methods），并给出 baseline methods 的一些初步结果：什么时候有效，什么时候失效，错误分析（error analysis），然后以此作为引出你们方法动机的过渡。好的，这就是今天截止的项目期中作业。是的，呃，我想我们还得批改几份晚交的，他们上周晚些时候才完成补考。成绩应该很快就会公布。中位数是 84，中位数是 85.7。有几个人超过了 100 分。所以总体成绩非常好。嗯，今天提交项目期中报告之后，我们会在明天或周四发布作业四。内容会是使用强化学习（reinforcement learning, RL），设计、设计奖励函数（reward functions），以及训练基于推理的多模态模型（multimodal models）。这次作业会短一些，大概一周半，会是

### [01:53](https://www.youtube.com/watch?v=Sk_TYpA6DWA&t=113s) · b000003

一份较短的作业，因为大家正在加紧做项目。然后我们还会有最后一次作业，也就是关于交互式智能体（interactive agents）的作业五，同样会是一份稍短的一周半作业。好的。呃，再回顾一下，最后，呃，最后另一项要交的作业是项目最终报告，会安排在课程的最后一周，那一周周二上课时进行海报展示，项目最终报告则在那之后几天截止。好的。所以就是项目期中报告、作业四和作业五，这两份作业都比较短，还有你们的最终、最终报告。关于作业有什么问题吗？

### [02:37](https://www.youtube.com/watch?v=Sk_TYpA6DWA&t=157s) · b000004

好。那么我快速回顾一下。呃，上周我们开始讨论推理（reasoning），reasoning 指的是这样一类问题：你必须综合不同形式的信息。你必须将这些信息结合起来，通常要经过多个推断步骤，并考虑问题的某些结构。呃，所以我们给出了这样一张示意图，把它和学期前半部分联系起来。我们看了，对于不同模态（modalities），如何看待单个元素，比如一个词、一幅图像，以及如何跨这些基本元素学习局部表征（local representations）。我们看过一些 a fuse representations \[字幕疑误，可能指 fused representations，融合表征\] 或 a line representations \[字幕疑误，可能指 aligned representations，对齐表征\] 等例子。然后我们把它扩展到更多元素。比如一个人说的一串词，或者图像中的一组物体。现在你就有了对齐问题（alignment problem），必须把其中一个元素的信息与另一个元素的信息匹配起来。

### [03:33](https://www.youtube.com/watch?v=Sk_TYpA6DWA&t=213s) · b000005

而这往往会给你带来多个层次和分辨率的信息，然后你必须基于这些信息进行推理。如何系统地对这些多步骤信息进行推理，以作出正确的，呃，预测或多步决策（multi-step decision）？这就是 reasoning 的定义。呃，显然大多数人都见过语言模型（language models）中的 reasoning。在语言模型的 reasoning 中，你有一个输入，也就是某个问题或提示（prompt），而 reasoning 可以被看作多个线性的思维链（chains of thought），对吧？呃，第一步、第二步、第三步。这通常出现在例如解决数学问题时，你会有多步方程运算；或者编写代码时，你可能要先规划代码结构，再填入各个代码片段。所以，在得到输出之前，你有多个推理步骤。我们还从宏观上看了不同的，呃，三种不同的

### [04:29](https://www.youtube.com/watch?v=Sk_TYpA6DWA&t=269s) · b000006

实现 reasoning 的方法。一种是直接提示你的模型。提示模型逐步思考（think step by step），把问题拆解开，而不训练模型，也不以任何方式更新模型。对吧？这在语言任务中有效，在许多多模态场景中也有效。我们看过这些例子，比如在机器人学（robotics）中，你想让机器人清理厨房，对吧？这只是一个语言提示，而语，机器人根据内部的语言模型，具有一些基本信息，知道清理厨房需要洗碗，然后把碗放进洗碗机，然后比如说给这个空间吸尘。所以，这些就是你的中间步骤，然后其中每个局部步骤都可以由机器人执行，对吧？比如按下洗碗机按钮或吸尘器按钮这样的具体动作。所以这就是直接

### [05:24](https://www.youtube.com/watch?v=Sk_TYpA6DWA&t=324s) · b000007

提示（direct prompting），zeroot reasoning \[字幕疑误，可能指 zero-shot reasoning，零样本推理\]。我们还看了，如果你有这些作为监督信息提供的中间推理轨迹（reasoning traces），对吧，也就是由人标注的，或者来自教材或其他例子，那么你就可以进行监督微调（supervised fine-tuning）。给定输入，你只需以自回归（autoregressive）方式预测第一个推理步骤，然后第二个、第三个，直到得到输出。这就叫通过 supervised fine-tuning 实现 reasoning 的方法，它要求你能获得推理步骤、reasoning traces。

### [06:00](https://www.youtube.com/watch?v=Sk_TYpA6DWA&t=360s) · b000008

第三种方法，也是我们上周主要深入讨论的方法，是使用 reinforcement learning。在这种设定中，你不会假设能获得 reasoning traces。只有某个特定输入和某个特定输出，没有中间的这些推理步骤，往往是因为很难获得人工标注或整理出这些推理步骤。现在，reinforcement learning 非常强大，因为它可以自动推断这些中间推理步骤。它所需要的，只是针对输出的某种指标，告诉你这些输出是好的，而另一些输出是坏的。我们称之为奖励函数，对吧？对吧？而只需优化这个奖励，模型就能使用 reinforcement learning 自动补全这些，呃，中间推理步骤。

### [06:51](https://www.youtube.com/watch?v=Sk_TYpA6DWA&t=411s) · b000009

我们看过这个非常简单的例子，就是玩 pong，对吧？在这种游戏中，你控制球拍，把球打到另一边。这是 reinforcement learning 的经典例子，因为你在上下移动球拍。这些就是你在每一步可以采取的动作（actions），对吧？有时候你很幸运，一连串动作让你从对手那里得了一分，而只有经过很长一串动作之后，你才会获得 +1 的奖励。有时候你不走运。你采取了一串动作，对手从你这里得了一分。所以你丢了一分，得到了 -1 的奖励。这是 reinforcement learning 的经典例子：其中有一些潜在动作（latent actions），你不知道它们是什么，它们没有被标注，而只有在经过很长一串动作之后，你才观察到某个奖励函数，对吧？我们还看到，一种通用的方法，基本上就是 reinforcement learning 的一种算法，

### [07:48](https://www.youtube.com/watch?v=Sk_TYpA6DWA&t=468s) · b000010

叫作策略梯度（policy gradients）。你只需要看奖励，对吧？+1 或 -1，然后用它来加权更新这些动作的对数似然（log likelihood）。对于你获胜并得到 +1 奖励的那段序列，你要最大化这四个动作的 lock probabilities \[字幕疑误，可能指 log probabilities，对数概率\]，并用奖励 +1 缩放。对吧？所以你是在提高这四个动作的概率。对于你输了并得到 -1 奖励的轨迹（trajectory），你同样要最大化那些动作的 lock probabilities \[字幕疑误，可能指 log probabilities\]，用奖励来缩放。但因为奖励是 -1，这就等价于最小化那些动作的 lock probabilities \[字幕疑误，可能指 log probabilities\]。所以你是在阻止模型再次采取这些动作。这本质上是假设功劳均等，对吧？对于每个 +1 或 -1，你都假设在四个动作的序列上，均等地分配 0.25 或 -0.25 的功劳。

### [08:46](https://www.youtube.com/watch?v=Sk_TYpA6DWA&t=526s) · b000011

所以，这本质上就是 policy gradient 算法，对吧？你有一个目标函数（objective function），它等价于对数概率。也就是 log pi，其中 pi 是你的策略（policy），给定状态（states）输出动作，再乘以奖励 R。对吧？所以直观地说，如果奖励为正，你就提高那些导致正奖励的动作的概率。如果奖励为负，你就降低那些导致该奖励的动作的概率。

### [09:22](https://www.youtube.com/watch?v=Sk_TYpA6DWA&t=562s) · b000012

我们还简要提到，原始奖励本身可能并没有特别大的意义。对吧？有时候，仅仅由于环境的设计，奖励总是正的，或者总是负的。这意味着，更重要的是你当前的奖励相对于某个基线（baseline）是更高还是更低。所以，你通常会用奖励减去一个基线奖励，可以把这个基线奖励看作截至目前所观察到的奖励的移动平均（moving average）。这样就利用 moving average，让一切都以零为中心进行某种标准化，并逐步看奖励是更高还是更低，对吧？这就是差值。如果高于均值，奖励就为正，你就在提高该序列中动作的权重。如果低于均值，这个值就为负，你就在降低该序列中动作的概率。所以，一个常用的 baseline 是奖励的某种

### [10:19](https://www.youtube.com/watch?v=Sk_TYpA6DWA&t=619s) · b000013

指数移动平均（exponential moving average）。最后，作为对上周二内容的最后回顾，这本质上就是你今天看到的所有面向大语言模型（large language models）的 reinforcement learning 的基础，对吧？你们的 gpo \[字幕疑误，可能指 GRPO\] 和其他策略优化（policy optimization）算法。那么，这里发生的是，通常你有 Q。这是你的策略模型（policy model）。在这种情况下，你的 policy model 就是大语言模型，给定一个状态，也就是当前对话状态，以及截至目前所有来回交流的历史。动作就是你在接下来一段序列长度中可以生成的后续词元（tokens）。对吧？所以，这是一个给定状态输出动作的 policy model。在这种情况下，动作和状态都是自然语言。你首先会采样多个输出，O1 到 OG。G 是 GRPO 中的组大小（group size）。这些是 G 个可能的回答，

### [11:16](https://www.youtube.com/watch?v=Sk_TYpA6DWA&t=676s) · b000014

也就是模型当前能够输出的回答。每个输出都会进入奖励模型（reward model）。在某些设定下，奖励很简单，对吧？在那个 palm \[字幕疑误，可能指 pong\] 的例子中，如果你把球打过对手，奖励就是 +1；如果对手把球打过你这一边，奖励就是 -1。呃，当然，在自然语言和对话中，奖励就没那么容易定义。所以有时候人们会训练一个 reward model，基本上就是说，他们收集了人们如何给与语言模型的对话评分的数据。这些是好的对话例子、有用的例子，这些是坏的对话例子。你有了这些数据，基本上就可以训练一个 reward model，告诉你对话的每个可能补全结果对应什么奖励，对吧？好还是坏。所以，这一部分可以用一个独立的神经网络（neural network）学习。这就是 reward model。这个参考模型（reference model），就像我们之前讨论过的，基本上是你的策略的一个先前

### [12:13](https://www.youtube.com/watch?v=Sk_TYpA6DWA&t=733s) · b000015

冻结副本，也就是你的语言模型，对吧？那里有一个 KL 项，基本上意味着，对语言模型进行这些 reinforcement learning 更新时，相比先前的副本和冻结版本，不应该变化太多。这些模型已经预训练过，已经相当不错。我只想把这种 reinforcement learning 看作最后一个微调阶段，所以我不想让模型参数变化 to which \[字幕疑误，可能指 too much，太多\]，因此这里有一个 KL 正则化（KL regularization）。所以，reward models 给出这些不同的奖励，R1 到 RG，每个话语或回答各有一个，然后你会得到优势（advantages）。Advantages 就是我们在上一张幻灯片中看到的，即奖励本身可能不是最有信息量的。我应该减去奖励随时间的某个 exponential moving average。所以，这能帮助你把每个奖励以零为中心进行归一化，变成我们所称的

### [13:09](https://www.youtube.com/watch?v=Sk_TYpA6DWA&t=789s) · b000016

advantages。也就是，它平均而言比平均奖励更好，还是低于平均、低于平均奖励，然后用它通过 policy gradient 方程更新 policy model。好的。所以基本上，就是 advantages 乘以你在这些回答中生成的 tokens 的对数概率。这就是 2025 年热议的那些东西。面向大语言模型的 reinforcement learning，基本上从 reinforcement learning 的基础、从第一性原理（first principles）出发，再加上大语言模型领域的一堆 curistics \[字幕疑误，可能指 heuristics，启发式方法\]，就解释出来了。

### [13:52](https://www.youtube.com/watch?v=Sk_TYpA6DWA&t=832s) · b000017

最后，呃，对上周的最后回顾，我和 Dimmitri 都给出了一些例子，说明这些基于 reasoning 的 LMS \[字幕疑误，可能指 LLMs\] 如何能够进行预测，同时在某种程度上具有可解释性（explainability），对吧？可解释，比如列出关键细节和医疗数据，这样你就可以把它交给医生，或者交给患者，让他们对模型有更多控制和信任。所以我展示了一些例子，给定这些视觉 X 光图像，模型就能开始用文字描述 X 光片中发生了什么。甚至给定某些医疗时间序列（time series），模型也能开始解释这是什么 time series，并据此判断患者对某些疾病是高风险还是低风险。所有这些都是通过 reinforcement learning 推断出来的。对吧？模型只能获得输入图像和传感器读数。而

### [14:49](https://www.youtube.com/watch?v=Sk_TYpA6DWA&t=889s) · b000018

模型的评分依据，是它最终答案答对了还是答错了。这是一道关于患者会在医院住多久的选择题。所以，这是一个选择题奖励。通过使用 reinforcement learning 优化奖励，模型能够，呃，自动推断出所有这些看起来相当不错的中间推理步骤，同时最大化正确回答问题的奖励。

### [15:21](https://www.youtube.com/watch?v=Sk_TYpA6DWA&t=921s) · b000019

好的。呃，以上都是对上周的回顾，讨论了 reinforcement learning、reasoning，以及在各种多模态任务中以 reasoning 作为可解释性的媒介。&gt;&gt; 在我们进入这周的内容之前，大家对上周的内容还有最后的问题吗？&gt;&gt; 请说。&gt;&gt; 对。通常，如果输出正确或不正确，奖励就只是 +1 或 0，但它仍然不是很，除非你针对生成语句的长度设置奖励。那么为什么 0 和 1 实际上会激发 heat \[字幕疑误，可能指详细推理\]，而不是鼓励简短但正确地回答？&gt;&gt; 是的，好问题。呃，澄清一下，奖励可能不只有 0 和 1。在我们做的这项工作中，奖励实际上相当复杂。有

### [16:16](https://www.youtube.com/watch?v=Sk_TYpA6DWA&t=976s) · b000020

三个项，对吧？每个项都有不同的权重。第一项的权重是 6，也就是答案是否正确。这是最重要的。文本推理是否与视觉边界框（visual bounding box）匹配，这一项的权重是 02。对吧？这里高亮的是某个心脏起搏器，文本就应该讨论与起搏器有关的内容。所以有一个视觉语言对齐奖励（vision language alignment reward），还有一个奖励是长度奖励（length reward）。呃，人们发现，length reward 不知怎么在这些模型中影响相当大。所以你希望它可能高于某个字数限制，但低于另一个限制。嗯，所以大致是准确性占 6，视觉文本对齐占 2，长度占 2。它还可以更复杂，对吧？呃，自从这些东西出现以后，很多工作

### [17:13](https://www.youtube.com/watch?v=Sk_TYpA6DWA&t=1033s) · b000021

很自然地，一个创新方向就是为各种场景设计好的 reward functions。Reward functions 可以由模型学习，可以有人在回路中（human in the loop），可以是，嗯，我的意思是，你的答案，你的问题有两个部分。首先，是的，奖励可以相当复杂。然后还有，但最终奖励仍然，即使你把所有这些不同的东西加起来，它们也只是一个数字，对吧？我想，只是优化一个数字就能让所有这些东西出现，确实挺神奇的，对吧？嗯，这是个谜。自从这些东西在 2025 年流行起来，SIS \[字幕疑误，可能指 scientists，科学家\] 之间一直有争论：reinforcement learning 和 reasoning 究竟是在给模型增加新的能力，还是把模型本来就有的能力显现出来，只是让它们更明显地浮到表面。好的，我觉得有些人很难想象，仅仅最大化这个标量（scalar），你

### [18:11](https://www.youtube.com/watch?v=Sk_TYpA6DWA&t=1091s) · b000022

就能以某种方式生成所有这些漂亮的解释。所以有很多实验表明，呃，即使你不做 RL，只是做更好的采样（sampling），或者使用更好的 prompting，模型也已经能够接近这样的 reasoning 能力。所以，也许很多主要工作已经在预训练（pre-training）或指令调优（instruction tuning）阶段完成了，而不是在 reinforcement learning 阶段。呃，但这仍然是个开放问题，而且显然很难回答，因为这些模型，你并不知道它们的 pre-training 数据是什么，也不知道它们的结构。&gt;&gt; 能否谈谈这些模型的忠实性（faithfulness），我们看到的那些是否实际上就是策略的成因？&gt;&gt; 是的，嗯，就像语言模型幻觉（hallucinations）一样，也可能存在 hallucinations。我们做的是，实际上请了一位医生来标注，而且

### [19:08](https://www.youtube.com/watch?v=Sk_TYpA6DWA&t=1148s) · b000023

这里所有粉色高亮的内容，都是医生标注为觉得有用、而且准确的内容。呃，然后我们有一些指标，我记得 reasoning 的准确率大约是 80，80% 左右。嗯，所以当然，每五个里可能有一个不准确。我想 Denitri 也给了另一个视角，介绍他们的做法：他们在图像上使用图像描述模型（image captioning models）来得到图像描述，也使用某些 sense signal processing features \[字幕疑误，可能指 sensor signal processing features，传感器信号处理特征\]，对吧？查看 time series 的均值和方差，并把这些展示给医生，嗯，再用 LLM 把所有内容总结和解释出来。所以他们也得到了大概 80、90% 的准确率。因此，我不会说它总能达到 100%。嗯，但正在接近，而且当然，你会预期随着模型改进，reasoning 会变得越来越忠实，

### [20:04](https://www.youtube.com/watch?v=Sk_TYpA6DWA&t=1204s) · b000024

以及随着你对模型进行更多训练，对吧？这很关键，对吧？一开始你不训练模型，只做零样本（zero-shot），那么，是的，它会差得多。当你开始最大化奖励时，faithfulness 就会改善。

### [20:24](https://www.youtube.com/watch?v=Sk_TYpA6DWA&t=1224s) · b000025

好的。现在我们已经看到了这样的模型：接受任意输入，能够生成所有这些不同的步骤，并给出某种输出。很自然地，如何构建这些，呃，构建这些模型，使其中存在反馈循环（feedback loop），对吧？当它生成一个推理步骤时，新的信息返回模型，模型就能生成新的推理步骤，然后采取新的动作，更多信息又返回模型。所以，进行多步推理的模型和具有智能体特性的（agentic）模型之间，自然有着非常紧密的联系，对吧？这里 agentic 的意思是，它们采取的动作会形成闭环反馈（closed loop feedback），进入新的状态，再采取新的动作，经过新的状态。这就是对 AI 智能体（AI agents）的宏观直觉。我觉得这个领域非常混乱，而大家，如果 reasoning 是 2025 年的大热点，那么 agents 就是 2025

### [21:20](https://www.youtube.com/watch?v=Sk_TYpA6DWA&t=1280s) · b000026

2026 年的大热点，而如今，这些持续学习（continual learning）的进化智能体（evolutionary agents）是今年的大热点。所以我们正在积极研究这个领域，但我也认为它是个很混乱的领域。嗯，我会尝试对这个领域做一些分类，我们会在这节课中看其中几类，也会在本学期稍后的最后几节专题课中看另外几类。一个维度是，你可以思考这些 agents 如何与环境建立关联（grounding），对吧？有些 agents 完全基于语言，比如回答有关文档的问题，或者总结不同段落，也就是处理文本，这是第一层 grounding。然后有些 agents 更多地在数字空间（digital space）中运行，你可以把它们理解为在电脑上操作电子表格和 powerpoints，或者浏览网页并采取一些能改变

### [22:17](https://www.youtube.com/watch?v=Sk_TYpA6DWA&t=1337s) · b000027

电脑上内容的动作的 agents。好的，也就是超越仅仅处理文本，转向在 digital space 中执行动作。呃，然后你有具身智能体（embodied agents）。现在，这些 agents 开始有身体了，对吧？它不一定是人形的，也可能像 Roomba，可能是机器狗，也可能是夹爪、机械手，也可能是人形机器人。嗯，现在它们有了某种身体，通过它作用于环境，并从环境接收反馈。最后，还有世界模型（world models），对吧？这些模型与整个世界的 grounding 更深入。所以，它们可能是更完全的人形机器人，不仅能在某个制造环境中完成单一任务，还能四处帮助人们，在学校、工作场所、医院等地方帮助我们。所以，这是一个分类维度。另一个分类维度是这些 agents 的结构。

### [23:14](https://www.youtube.com/watch?v=Sk_TYpA6DWA&t=1394s) · b000028

在最简单的层次上，你只有一个模型，对吧？这样的 agents 基本上就是模型本身，可以是大语言模型、视觉语言模型（vision language model），或者其他 multimodel LLMs \[字幕疑误，可能指 multimodal LLMs，多模态 LLMs\]。它们基本上通过 prompting 或图像进行交互，并输出在世界中执行的动作。这是这些 agents 最简单的第一层。然后还有另一层 agents，周围包裹着某种工作流（workflow），对吧？也许一个 workflow 就是你赋予模型访问权限的一组 pools \[字幕疑误，可能指 tools，工具\]。它也可以是一组 API，模型可以编写代码与之交互，对吧？这些就是 workflows。这些是在基础模型（base model）之上的东西，也包括你让模型访问的其他工具、no applications \[字幕疑误，可能为口语停顿及 applications，应用程序\]、记忆系统（memory systems）和文件系统（file systems）。这种 workflow，往往是由人设计的，对吧？所以，如果我想使用，如果我想让模型使用计算器来更好地做

### [24:11](https://www.youtube.com/watch?v=Sk_TYpA6DWA&t=1451s) · b000029

数学，那么我可以在模型之上设计这个计算器封装（wrapper）和 API。但当 agent 可以自动优化自己的 workflow 时，情况就变了。现在我们已经看到这些框架取得了很多进展，agent 不再仅限于你提供的那个计算器工具，你基本上让它访问电脑上的一切，而它可以自动判断，对吧，这种情况下我应该用计算器，另一种情况下我应该用电子表格，再一种情况下我必须画图。所以它会自动编排可用的工具，并针对某个特定任务进行优化，对吧？这种工作流优化（workflow optimization）让自主性（autonomy）又提升了一层。最后是这些自进化智能体（self-evolving agents），agent 不仅能优化 workflow，还能优化它试图处理的任务，派生出各自承担不同

### [25:07](https://www.youtube.com/watch?v=Sk_TYpA6DWA&t=1507s) · b000030

任务的新 agents。呃，委派自己的记忆系统，以便存储信息。所有这些都不需要用户说，你必须使用记忆，或者你必须派生不同的子智能体（sub-agents）。呃，当然，这是向更高自主性发展的前沿，而且这些 agents 有可能做到远远超出用户最初要求它们做的事情。好的。所以，这可以被看作一种结构，就像我们讨论过的 reasoning 结构一样。最后，我们还有一个可能也非常关键的维度，就是与人的交互，对吧？比如，业界确实在不断迭代更好的 base models、更好的 agentic workflows，我认为，我们以及不同企业思考如何把这些 agents 整合到自己的 workflows 中，显然非常重要。嗯，我们已经看到自主智能体（autonomous agents）的例子，对吧？这些模型基本上

### [26:04](https://www.youtube.com/watch?v=Sk_TYpA6DWA&t=1564s) · b000031

自行运行。它们试图完成整个任务，最后可能把结果返回给用户，要么成功，要么失败。大家都知道，这有时有用，但大多数时候效果不是特别好，对吧？然后你有 human in the loop 这样的例子，agents 不会试图解决整个问题，而可能只尝试执行人委派给 agent 的一个小步骤，或者主动决定采取某个步骤，因为 agent 认为用户在这方面需要帮助。所以 human in the loop 既可以是被动响应（reactive），也可以是主动介入（proactive），对吧？Reactive 是指人把某个小部分委派给 agent；proactive 则是 agent 主动介入，知道这一部分是它有信心自动完成的，可以节省用户时间。我的意思是，在这里，你们大多数人可能都见过一个非常大的差别，比如 Devon \[字幕疑误，可能指 Devin\] 后来的表现和 cursor 后来的表现，对吧？在

### [27:01](https://www.youtube.com/watch?v=Sk_TYpA6DWA&t=1621s) · b000032

这些编程智能体（coding agents）非常流行的时候。Devon \[字幕疑误，可能指 Devin\] 的方法，是试图构建最自主、最准确的 coding agent。对吧？给定一个问题，或者程序员抛给这些 agents 的任何难题，它们都会试着思考，试着做事。这些模型非常昂贵，也非常复杂。当然，成功的时候很棒，但它们经常失败。失败时，它们就把这巨大的 compiler trades \[字幕疑误，可能指 compiler traces，编译器跟踪信息\] 和失败的测试用例一股脑丢回给程序员。程序员根本不知道该怎么处理。即使答案看起来正确，也可能存在非常细微的 bug，因为这是大块代码，里面可能有非常细微的 bug。所以，这就是 Devon \[字幕疑误，可能指 Devin\] 的方法。试图过度自主，花更多时间在模型工程上，而在这，这并不是对用户而言最好的使用方式或界面。然后我们有了 cursor 和 cloud code \[字幕疑误，可能指 Claude Code\] 这样的例子，模型并不会真的试图

### [27:54](https://www.youtube.com/watch?v=Sk_TYpA6DWA&t=1674s) · b000033

把一切都自动化，而是只试图自动完成问题中的一个小步骤。它们有点像代码自动补全（autocomplete），对吧？它们看到你在尝试写一个排序函数，也许就会自动询问你，是否希望它帮你填完这个排序函数。用户能看到它写的这一小段透明可见的代码，然后接受或拒绝。或者，如果它们看到某个拉取请求（pull request, PR）或 bug 修复，可能会提出如何处理的建议，再询问用户是否接受或拒绝这个，呃，这个建议的解决方案。所以这些 agents 更多地采用 human in the loop，对吧？有一点主动性。它们会判断什么时候能帮助用户，并提供那一小点帮助。首先，这让这些模型更容易训练。它们只需要写小段代码。同时，用户体验也好得多，对吧？你不需要看大段的

### [28:44](https://www.youtube.com/watch?v=Sk_TYpA6DWA&t=1724s) · b000034

编译器转储信息（compiler dumps），只需要看小段代码，就能很快验证它是好是坏。当然，最重要的是，在与 cursor 交互时，你获得了所有这些用户数据，对吧？你有所有这些接受、拒绝，以及修复 cursor 代码中 bug 的数据。你获得了所有这些有助于改进模型的交互数据。所以，这些例子展示了从 autonomous 到 human in the loop 的转变，当然最终会走向与 AI agents 共同生活、共存。

### [29:17](https://www.youtube.com/watch?v=Sk_TYpA6DWA&t=1757s) · b000035

有什么问题吗？请说。&gt;&gt; 你认为人会成为瓶颈吗，就个体而言？&gt;&gt; 我认为在很多场景下会，对吧？显然，我们的阅读和打字能力比 AI 慢得多，对吧？呃，但与此同时，在许多场景中，人类决策者不能从这个过程中被移除。所以，只要那些政策和法律还在，人的处理速度和判断速度就会成为瓶颈。原因也是一样的，嗯，我的意思是，可以类比一下，现在我们有这种奇怪的混合状态，比如 10% 是自动驾驶汽车，90% 是人类驾驶员，其中会有冲突，但如果是 100% 自动驾驶，

### [30:12](https://www.youtube.com/watch?v=Sk_TYpA6DWA&t=1812s) · b000036

道路显然会好得多，也安全得多。我不知道，我只是假设，别引用我这句话。&gt;&gt; 好的，那么我们开始深入讨论一些这样的 agentic models，对吧？先从语言智能体（language agents）和数字智能体（digital agents）开始。呃，然后再转向一些更具身的 agents。但很多相同的原理都适用，对吧？当然，对这些 language agents 的需求非常大，对吧？人们为工作、盈利、创造力而做的许多任务，都在电脑上完成，对吧？其中很多都在电脑上的各种应用程序、各种网站上完成，对吧？所有这些 AI 研究之所以开始，是因为在电脑上自动完成许多琐碎任务的机会太大了，可以节省人们的时间，让他们去做更复杂、

### [31:08](https://www.youtube.com/watch?v=Sk_TYpA6DWA&t=1868s) · b000037

更有趣的任务，对吧？比如，查看和检查你在 AWS 上使用了多少额度，或者在不同浏览器上设置不同配置，或者把数据录入电子表格，然后组织、可视化这些数据，以及制作 PowerPoint。我想有人总结过，可能有 80% 的劳动力都在做某些可以合理地由 AI agents 自动完成的任务。所以，这就是最初的设定，嗯，第一批环境设计所针对的场景。web arena \[字幕疑误，可能指 WebArena\] 是一个很早期的环境，用户只需给这些 AI agents 下指令。例如，呃，如果你要做这个网购任务，对吧？也许你的任务是购买一副评分至少 4.5 星的耳机，并寄给你，然后把这个

### [32:05](https://www.youtube.com/watch?v=Sk_TYpA6DWA&t=1925s) · b000038

指令交给 agent。Agent 应该能够从视觉上看到网页上有什么，对吧？哪些是耳机，各有多少星、多少条评价，以及价格。Agent 应该能够点击、滚动、输入，做你会在这个网页上做的所有事情，对吧？所以理想情况下，它应该搜索耳机，进行筛选，查看星级，加入购物车。那里可能已经保存了你的地址，然后结账，也许就在结账之前，向用户确认这确实是他们想要的东西。

### [32:41](https://www.youtube.com/watch?v=Sk_TYpA6DWA&t=1961s) · b000039

这就是 AI agents 的愿景，而 web arena 环境是朝这个方向迈出的一大步。他们从各种网站获取数据，比如网购、Reddit、GitLab，呃，所有这些环境基本上都是实际网站的克隆，对吧？因为如果你真的使用，比如 Amazon 或 GitHub，过一段时间可能就会因为流量太大而被封禁。所以，它是网站的一种克隆。不过，他们会记录数据，以获得真实的场景，来自人们实际会购买的产品，或者人们在 GitHub 上实际提交的 pull requests。这些任务对人来说很容易。人类能以 78% 的成功率完成它们，实际上我想，在他们开展用户研究时，成功率甚至更高。大多数失败只是人们忘了在

### [33:36](https://www.youtube.com/watch?v=Sk_TYpA6DWA&t=2016s) · b000040

最后一步点击结账，或者犯了预订错误。所以，这些任务对人而言相当简单，而在当时，2014 \[字幕疑误，年份可能有误\] 年，这对 LLM agents 相当困难，它们的成功率大约只有 14%。对吧？这些 agents 的第一次迭代完全基于文本运行。因此，它们不是实际看到网站，而是使用 HTML 来操作，对吧？你们大概都知道 HTML。它非常杂乱，有很多标签、很多冗余字符。嗯，空间布局完全没有传达出来，对吧？没有人能看着 HTML 告诉你图像的左上角或右下角有什么。上下文长度（context length）非常大，对吧？一个 HTML 页面，如果只用文本存储，很容易就占满 100k tokens，对吧？所以，即使是 context length 最长的模型，也无法真正

### [34:31](https://www.youtube.com/watch?v=Sk_TYpA6DWA&t=2071s) · b000041

存储多个页面之间的多个链接。所以，人们开始关注如何超越仅仅使用语言模型和基于 HTML 操作的 LM agents，转向能够看到和感知这些网站，以及它们的空间信息、颜色信息、整体用户界面（user interface）和布局的多模态智能体（multimodal agents）。呃，就像人能做到的那样，对吧？把这个网站和 HTML 比较一下。当然，我们是这样操作的。如果有一个模型能看这幅图像，你只需要用一个视觉编码器（visual encoder）进行编码，得到一个表征，而不必花费 100k tokens 来处理 HTML。

### [35:18](https://www.youtube.com/watch?v=Sk_TYpA6DWA&t=2118s) · b000042

所以，在 web arena 之后，出现了 visual web arena \[字幕疑误，可能指 VisualWebArena\]。visual web arena 是一个基准（benchmark），沿用了 web arena 的一些流程，对吧？所以任务非常类似。有网页浏览、评论、网购、编程。嗯，任务非常相似。但现在，所有这些任务都需要视觉信息，对吧？目标是训练 vision language model agents，使其能够处理这些视觉网站，并基于视觉解决任务。因此，它旨在对这些 multimodel agents \[字幕疑误，可能指 multimodal agents\] 进行基准评测，并跟踪它们的进展。它仍然可以访问不同的信息来源。有原始视觉输出，有 HTML，还有一种介于二者之间的东西，叫作网站的无障碍树（accessibility tree），它是某种中间形式。它像是清理过的 HTML 版本，让

### [36:13](https://www.youtube.com/watch?v=Sk_TYpA6DWA&t=2173s) · b000043

人更容易阅读。所以他们也对这些方法进行了基准评测。在这里，你可以看到很多面向网页的 AI agents 能够执行的动作列表，对吧？比如点击某个元素、将鼠标悬停（hover）在某个元素上，这有时和点击不同，呃，打开新标签页、在标签页之间来回切换、滚动浏览不同网站。嗯，这些是不同的任务。这就是这些 agents 的动作空间（action space）。

### [36:44](https://www.youtube.com/watch?v=Sk_TYpA6DWA&t=2204s) · b000044

所以，Web Arena 包含跨不同网站的各种任务，购物、Reddit、Losify \[字幕疑误，可能指某网站名称\]，呃，一些讨价还价的网站。这些是按难度划分的任务分布，对吧？简单任务，人类用几个动作、点击几次就能解决。困难任务需要更多点击。还有视觉难度。比如，这是通过这些网站上有多少物体和物体边界框来衡量的。网站越杂乱，视觉难度就越大。这里是 visual web arena 中的一个例子。现在你有一些视觉输入，任务中有视觉输入，网站上也有视觉输入。比如，假设你在一个社交活动上和某人聊天，想保留对方的联系方式。于是你拍了对方名牌的照片，你的任务是购买最便宜的

### [37:42](https://www.youtube.com/watch?v=Sk_TYpA6DWA&t=2262s) · b000045

彩色照片打印机，并把它寄到图像中显示的 Emily 家，对吧？图像甚至是倒过来的，上面有地址。所以，模型应该依次搜索打印机、彩色打印机，按最便宜排序，下单，然后，呃，把它寄到你新认识的人的住处。对吧？所以，你必须填写从图像中推断出的地址。

### [38:23](https://www.youtube.com/watch?v=Sk_TYpA6DWA&t=2303s) · b000046

好的。那么，如何评估，对吧？很多这样的 agents 是这样评估的。你有这些输入任务、网站，有任务，然后让 agent 去操作，基本上 agent 必须自行报告它已经完成任务。一旦完成，很多方法基本上会进行自动评估，对吧？它们基本上使用 reg x \[字幕疑误，可能指 regex，正则表达式\] 或 if else 语句之类的东西，检查动作的最终状态、agent 所处的最终状态是否符合预期。所以，比如，如果你要搜索某个东西，基本上就会检查你搜索得到的输出和你给出的搜索词之间是否精确匹配。对吧？如果你试图导航到某个 URL，就检查 URL 是否正确，以及

### [39:21](https://www.youtube.com/watch?v=Sk_TYpA6DWA&t=2361s) · b000047

它是否包含，比如价格为 5,000。它会检查这个。所以，基本上就是进行所有这些最终检查，确认它满足任务的规格要求。这就会是最终的 reward function。在 visual arena \[字幕疑误，可能指 VisualWebArena\] 之后，很多其他环境也发布了。OS atlas \[字幕疑误，可能指 OS-Atlas\] 就是其中之一，它甚至超越了简单网站，扩展到各种电脑操作系统。呃，比如包括，当你使用浏览器时，对吧，Linux，抱歉，是你的桌面，Linux 桌面、Mac OS 桌面、Windows 桌面。也包括手机上不同的用户界面、应用程序、你可能使用的浏览器。所有这些形式的视觉信息都包含在这个 benchmark 中，并且为这些不同环境定义了各种任务。

### [40:19](https://www.youtube.com/watch?v=Sk_TYpA6DWA&t=2419s) · b000048

好的。关于这些不同的网页 agent 环境，有什么问题吗？请说。&gt;&gt; 我想，在前一个例子里，假设它最终学到的是某个特定的、更便宜的打印机，然后市场上出现了一款新的、更便宜的打印机。它会回到原来的那个，还是它实际上学到了寻找最便宜 people \[字幕疑误，可能指 printer，打印机\] 的路径？&gt;&gt; 啊，好问题。当前的 agents，不会，对吧？因为这些 agents，我的意思是，如果你委派任务，给它们这个任务，它执行了，并搜索到了今天最便宜的打印机，呃，它们不会主动到下周提醒你市场上又出现了一款便宜的打印机。那大概也没什么意义，因为你已经买了打印机。嗯，所以我们还没有这种更主动的 agents，对吧？我的意思是，这会引出非常

### [41:15](https://www.youtube.com/watch?v=Sk_TYpA6DWA&t=2475s) · b000049

有趣的研究问题，也就是，当 agents 一直运行时，如何节省时间和 cute \[字幕疑误，可能指 compute，计算资源\]。现在你给它们提示，它们会消耗 token，所以它们不能每次都搜索、查找新打印机的消息，对吧？还有，它们什么时候响应，什么时候主动向你提出建议？在这个例子里，你显然已经买了打印机，所以可能不想再买一台。但如果，呃，纸变便宜了呢？它们会让你买吗？我的意思是，这样你就进入了所有这些广告问题，对吧？这大概是 Open AI \[字幕疑误，可能指 OpenAI\] 未来赚钱的方式。它们不得不诉诸广告。&gt;&gt; 是的。有没有类似愿望清单 agents 之类的东西，就是在 markdown 文件里列出现在想买的东西，有没有一种架构可以根据你的目标来检查，也就是买这个东西，但不是在一个特定的

### [42:10](https://www.youtube.com/watch?v=Sk_TYpA6DWA&t=2530s) · b000050

价格，然后它就持续扫描互联网。&gt;&gt; 是的。&gt;&gt; 对。我的意思是，这和另一位同学的问题类似，我认为这是可能的。嗯，从计算角度看，如何指派 agent 持续搜索、不断查看你的愿望清单，这会带来一些计算方面的挑战。但如果一开始就有一份清单，那大概会更容易，对吧？因为它不必搜索所有东西，你只需持续监测价格或打印机，所以我会认为，这应该很有可能构建出来。是的。

### [42:49](https://www.youtube.com/watch?v=Sk_TYpA6DWA&t=2569s) · b000051

&gt;&gt; 请说。&gt;&gt; 嗯，我不知道它们是什么。你愿意多讲一点吗？&gt;&gt; 那叫什么？数据抓取（data scraping）。&gt;&gt; 对。有人用 a sounds \[字幕疑误，含义不明\] 抓取这类东西的信号，因为可能是在抓取打印机信息，也可能是在抓取其他信息。是的，我的意思是，我相信设置一个机器人（bot）很容易，它只需把一个搜索词附加到 Google search、Google news 或 Twitter 上，每小时搜索一次并刷新你的信息流。所以你可能根本不需要 agentic models 来做这个。

### [43:37](https://www.youtube.com/watch?v=Sk_TYpA6DWA&t=2617s) · b000052

很好。好的。所以，我们看了一些新的环境，对吧？基于语言的环境、视觉环境。我们看到 accessibility trees 和 HTML 通常没有必要，通常会带来大量过多的上下文 tokens，而处理图像自然得多，对吧？直接看网站。但当然，处理这些网站很困难，对吧？它们和自然图像非常不同。所以，我们还没有像针对 imageet \[字幕疑误，可能指 ImageNet\] 那样真正完善的编码器。我们有不错的编码器，但对于某些网站，我们没有真正好的编码器，尤其是用户界面、设计模式和不同文本都特别小的时候。嗯，为网站设计 visual encoders 仍面临很多挑战，但尽管如此，已经取得了很多

### [44:31](https://www.youtube.com/watch?v=Sk_TYpA6DWA&t=2671s) · b000053

不错的进展。呃，这个 S Soom \[字幕疑误，可能指 SoM\] 叫作标记集合（set of marks），是一种不错的方法。你可以把它理解为针对网站的物体识别（object recognition）。它会遍历并查看你网站上的所有文本、所有链接、所有可以点击的位置，以及所有嵌入图像。对吧？所以，在这种情况下，基本上就是对网站进行 object recognition 和分割（segmentation）。对，这些都是预训练模型高亮出的 set of marks，同时还标出了数字以及这些东西所在的位置。所以，这可以是一个不错的表征，对吧？嗯，它让模型能够基本上在自己的 action space 中决定，应该点击其中哪个，或者放大哪个，或者点击哪个。给定这个原始网页，你可以先运行

### [45:27](https://www.youtube.com/watch?v=Sk_TYpA6DWA&t=2727s) · b000054

这些 set of marks 模型，解析网页，得到所有可能的动作，然后把这个特定查询，也就是你应该完成的任务，交给 agent，agent 就可以输出一个具体动作。这里是一些基线 agents。嗯，纯文本 agents 的表现不是特别好，完成率是 10%。文本加图像描述（captions），就是取网站，用最好的 image captioning 模型给它生成描述，把一切转换成文本，再让 LLM agent 在这些文本上运行，大约是 15%。Multimodal models 基本上就是适配器（adapter）风格的模型，有 LLM agent，把网站变成图像，再适配到 LLM agents 中。所以更高一些，也许是 18%。在这些视觉表征之上加上 set of marks，会再好一点。现在大概接近 19%。当然，与人的

### [46:24](https://www.youtube.com/watch?v=Sk_TYpA6DWA&t=2784s) · b000055

表现相比仍有很大差距，人类几乎，呃，超过 80、85%。对。还有，你可以更仔细地查看这些结果，但闭源模型（closed source models）仍然表现最好。例如，以 GP4 \[字幕疑误，可能指 GPT-4\] 作为主干（backbone），以及一些基于 clip-like 模型的视觉 backbones。Blip 只是对 clip 模型的一种修改。嗯，这些取得了最好的结果。所以 closed source models 在这些 agents 任务上仍然相当不错。总体最佳的是使用视觉和 set of marks 的 multimodal model。也就是编码器在这些网页之上进行物体检测（object detection），取得了 16% 的表现。

### [47:14](https://www.youtube.com/watch?v=Sk_TYpA6DWA&t=2834s) · b000056

仍然有很多不错的成功例子。这里的任务是，你在这个 Reddit 上，不喜欢某人在这个 subreddit 发的一篇帖子，能帮我屏蔽他吗？模型能够进入主页，搜索 subreddit，导航到论坛列表，寻找你要找的特定内容，找到个人资料，点击屏蔽按钮，并确认屏蔽该用户。所以有一些成功的例子，甚至能解决这些六步的 agentic tasks，这其实相当困难。

### [47:55](https://www.youtube.com/watch?v=Sk_TYpA6DWA&t=2875s) · b000057

好的。那么主要挑战有哪些？仍然是今天还面临的主要挑战。也许最大的挑战是，agents 如何进行这种长时程推理与规划（long horizon reasoning and planning）。这些任务仍然相对简单，六、七个任务，而且局限于特定网站。呃，但现实世界中的任务可能长得多，尤其是在现实世界中，尤其是涉及不同网站、涉及人的时候。这些任务需要更多的规划步骤，并执行每一步。如果最初的规划不正确，模型如何重新规划（replan）、回溯（backtrack）并再次尝试？对吧？当它们受到干扰、卡住时，如何判断，呃，在推理时（inference time），如何解决不同问题、成功摆脱卡住的状态？所以 long horizon reasoning and planning

### [48:53](https://www.youtube.com/watch?v=Sk_TYpA6DWA&t=2933s) · b000058

也许是 agent 领域最大的挑战之一。另一个重大挑战，也是视觉处理，或者进一步说多模态处理的失败。对吧？LLM 部分通常负责 reasoning 和 planning，而其他模态负责感知（perception），对吧？我们看到了一些例子，即使是这些视觉网站，对不同方法而言也很难处理，而这还没有涉及现实世界视觉、现实世界机器人学，以及现实世界各种传感器的复杂性。所以，最大的挑战是基于语言的 long horizon reasoning and planning，以及从多模态视角看，如何对这些其他模态进行 perception。

### [49:41](https://www.youtube.com/watch?v=Sk_TYpA6DWA&t=2981s) · b000059

&gt;&gt; 有问题吗？请说。&gt;&gt; 嗯，今天，或者大概 20 年前，开始使用，开始把最初的网站适配到移动端，对吧？像 mobile.com，我想会是一个稍作修改的网站。你有没有数据，比如 agents 在什么样的网站上做得好，让我们能有某种直觉，哪些视觉线索更有效，哪种布局更有效，这样就可能出现一批新网站，如果我的 agent 浏览它，看到的是稍微不同的版本。&gt;&gt; 是的，这是个很有意思的问题。嗯，我知道这是一个活跃的研究领域，但我并没有跟上具体细节，对吧？看到人们尝试构建，

### [50:38](https://www.youtube.com/watch?v=Sk_TYpA6DWA&t=3038s) · b000060

嗯，首先我看到人们整理越来越多专门用于评测和训练 agents 的数据集。我给了这些例子，但这些并没有很好地整理网站或用户界面，对吧？有些人整个职业生涯都在人机交互（human-computer interaction, HCI）和数据可视化（data visualization）领域设计布局，对吧？前端布局。现在，他们开始整理前端布局可能呈现的不同 tonomies \[字幕疑误，可能指 taxonomies，分类体系\]，并研究哪些更合适、能让 AI 模型取得更高表现。呃，所以我相信他们在这方面有一些令人兴奋的发现。对。当然，与此同时，这不能影响人对它的感知。所以，也许最终会有人类版本的网站，也有 AI 版本的网站，对吧？那是另一种。&gt;&gt; 当然。&gt;&gt; 你怎么 swear \[字幕疑误，可能指 square，解释这种看似矛盾的情况\]，

### [51:34](https://www.youtube.com/watch?v=Sk_TYpA6DWA&t=3094s) · b000061

LM agents 这么擅长前端开发，却这么不擅长网站？我觉得它们很擅长 sex \[字幕疑误，可能指 text，文本\]。&gt;&gt; 我不知道。有人觉得自己能回答这个问题吗？&gt;&gt; 文本在哪里？很好。Twitter 文本，但像导航网站。&gt;&gt; 也许吧。是的。但如果这些 LM coding agents 是以文本形式输出网站的 HTML，那么问题就是，为什么它们不能像生成 HTML 一样轻松地处理 HTML，对吧？嗯，是的，我不确定。

### [52:26](https://www.youtube.com/watch?v=Sk_TYpA6DWA&t=3146s) · b000062

好的，接下来是 reasoning 和 planning。这又与我们上周讨论的内容联系起来，也就是这些目标中有很多，对吧？这些目标非常复杂，需要 long horizon planning。因此，如今大多数 agents 都有一个专门负责 planning 的模块，对吧？它把这些复杂目标拆解为高层规划（high-level plans），一次一个步骤。有了这个 high-level plan，就可以把它与观察到的网页结合起来，理想情况下进行一些非常强大的视觉处理，可以在视觉空间中，也可以在更适合 agents 的其他抽象空间中，得到网页的表征。给定 plan，再结合这个表征，一起提出一个低层动作（low-level action）。对吧？High-level plans 可能是，比如导航到某个网站，或者某种更容易理解、语义上更有意义的事情；low-level

### [53:23](https://www.youtube.com/watch?v=Sk_TYpA6DWA&t=3203s) · b000063

actions 实际上会是，比如点击搜索栏所在的这个坐标，并输入这些字符。这些是 agent 真正可以执行的 low-level actions。嗯，然后你会递归（recurse），对吧？通过进入该动作带你到达的下一个观察到的网页，查看下一个 high-level plan，再得到下一个 low-level action，来进行 recurse。这些就是人们通常在基于网页的 agents 中开发的循环。呃，我举个例子。如果没有 reasoning，你可能给模型一个任务：在低于 $60 的预算内，从这个 Nintendo Switch 收纳包类别中购买评分最高的产品。对吧？模型接收这个指令。如果它不 planning，只想一步完成所有事情，它试着搜索某个东西，然后出于某种原因卡住了。它困惑了，不知道该做什么，于是停了下来。

### [54:20](https://www.youtube.com/watch?v=Sk_TYpA6DWA&t=3260s) · b000064

而理想情况下，这是一个带 planning 组件的模型。首先，你会拿到任务，把它拆开，说先搜索 Nintendo Switch 收纳包，然后按某个价格进行筛选，然后比如说继续结账。这样模型就能够逐一执行这些步骤。对吧？第一个动作是搜索，然后是点击，再一次点击加入购物车，然后再一次点击结账。这就是逐一规划各个步骤的力量，让模型能更系统地执行这些动作。如何 planning？我已经在 reasoning 领域给了很多例子，对吧？你可以直接做 zero-shot；如果有例如人们标注的真实规划（ground truth plans），可以做监督微调（SFT）；也可以做 reinforcement learning，给定这些最终奖励，作为

### [55:15](https://www.youtube.com/watch?v=Sk_TYpA6DWA&t=3315s) · b000065

激励来推断这些中间的逐步规划。这里我只是展示更多例子，嗯，其中一些混合了基于 prompting 的方法，有些混合了工具使用，这些都是提高 web agents 规划能力的一些重要论文。

### [55:39](https://www.youtube.com/watch?v=Sk_TYpA6DWA&t=3339s) · b000066

好的，

### [55:45](https://www.youtube.com/watch?v=Sk_TYpA6DWA&t=3345s) · b000067

我们讨论了 fully autonomous agents 和 human loop agents \[字幕疑误，可能指 human-in-the-loop agents\] 之间的一些区别。很自然，我们有时希望这些 agents 完成所有事情，但有时候 agents 也可以只生成不同步骤，让人来检查它们是否走在正确方向上。所以，比如，呃，这是一个难题：这个在线市场中无线耳机的价格范围是多少？对吧？模型可能开始 planning，搜索无线耳机，尝试寻找价格范围，但网站上并没有直接标注价格范围。对吧？于是模型卡住了。理想情况下，人类标注的 plan 应该是搜索耳机，然后按价格从低到高排序。对吧？有一个从低到高的排序按钮，然后取第一个商品，再次点击排序，改为从高到低，取第一个商品。这样你就得到了最低价和最高价，然后

### [56:42](https://www.youtube.com/watch?v=Sk_TYpA6DWA&t=3402s) · b000068

返回这两个数字，对吧？这就是理想的人类 plan 会做的事情。所以，不 planning 的模型会答错，因为你无法直接搜索价格范围。即使给模型一些例子，它也只会找到最低价或最高价中的一个，而不是两个。这是我们开发的一种方法，将一些少样本规划（few-shot plans）与人工澄清（human clarification）结合起来。所以模型可能第一步 plan 做对了，然后在 ban \[字幕疑误，可能指 plan，规划\] 第二步时遇到困难。于是你给模型一次人类示范（human demonstration）。也就是拿人类标注的正确第二步，交给模型，向模型展示。对吧？你必须先把耳机从低到高排序，然后模型就可以继续正确生成剩下的

### [57:39](https://www.youtube.com/watch?v=Sk_TYpA6DWA&t=3459s) · b000069

plan，对吧？它会自动学会还必须把耳机从高到低排序。所以，即使只从人类 plan 中提供一步澄清，也能把模型引向正确方向，让模型完成任务的其余部分。

### [58:00](https://www.youtube.com/watch?v=Sk_TYpA6DWA&t=3480s) · b000070

&gt;&gt; 是的。抱歉，我知道这些问题有点，呃，但当你在使用 cloud code \[字幕疑误，可能指 Claude Code\] 之类的 planning modes 时，它请求这些澄清，是基于某种低置信度（low confidence）吗？也就是它生成这个 plan，然后根据那一组中的某种表面 confidence，进行这种具体的干预、干预。&gt;&gt; 完全正确。好问题。嗯，这正好关联到我的下一张幻灯片，也就是模型什么时候应该交由人来处理（defer），或者向人请求澄清，对吧？当然，我不知道 cloud code \[字幕疑误，可能指 Claude Code\] 是如何工作的，或者，我想现在有了泄露，我们确实知道了。呃，所以，很多判断模型何时 defer 的方法，基本上就是估计不确定性（uncertainty），对吧？什么是 uncertainty？基本上就是，当模型，模型总会输出某个东西，对吧？理想情况下，模型不确定时会说“我不知道”。但很多模型还没有这种能力，而这是一种非常困难的

### [58:57](https://www.youtube.com/watch?v=Sk_TYpA6DWA&t=3537s) · b000071

能力。不过，uncertainty 基本上是指，模型输出某个东西时，它在这一点上有多一致。所以，一种衡量 uncertainty 的方法，就是用不同的温度（temperature），呃，temperature 设置，多次重新采样模型。也就是同一个 temperature 设置，多次重新采样。如果模型在多次样本中总是说同样的内容，那么你可以凭经验把它看作模型相当有 confidence，因为它可以重复。它总是这么说。如果你多次重新采样模型，每次它说的都不一样，那么你可以把这当作模型不是特别有 confidence 的一种近似判断，对吧？呃，同样的道理也适用于分类器（classifiers），对吧？看你的 softmax classifier 是否非常尖锐。所以，从 softmax 多次 sampling，会得到相同输出；或者，如果 softmax 更均匀，那么你每次从模型采样新输出时，都会得到不同输出。所以，不确定性估计（uncertainty estimation）

### [59:53](https://www.youtube.com/watch?v=Sk_TYpA6DWA&t=3593s) · b000072

对于判断模型何时应该 defer 并向人寻求 clarification，非常关键。这种 sampling 方法也很好，因为它只要求对模型有黑盒访问（blackbox access）。你不需要看到模型内部，只需要能从它采样，对吧？缺点是更慢。如果你能完全访问模型，就可以查看最后一层的 token probabilities。这样回答了问题吗？&gt;&gt; 呃，是的，我想最后一部分有些问题，如果你正在构建一个 rafter \[字幕疑误，可能指 wrapper，封装层\]，&gt;&gt; 对吧？&gt;&gt; 它们必须采用基于 sampling 的方法，对吧？嗯，多次 sampling，看看它们说什么。而且现在这越来越常见，对吧？不仅为估计 uncertainty 重新采样很常见，为 RL 训练重新采样也非常常见。嗯，为各种推理时搜索（inference time search）重新采样。所以

### [1:00:52](https://www.youtube.com/watch?v=Sk_TYpA6DWA&t=3652s) · b000073

非常常见。这就是为什么现在这些模型使用这么多 tokens，而且这么慢。&gt;&gt; 是的。

### [1:01:04](https://www.youtube.com/watch?v=Sk_TYpA6DWA&t=3664s) · b000074

还有其他问题吗？&gt;&gt; 好的。呃，说到 inference time search，这也是人们正试图加入这些模型的一项关键能力，对吧？Agentic models。我们从宏观上看到了模型如何将复杂指令分解为各个 plans，有时模型会 refers to search \[字幕疑误，可能指 resorts to search，转而使用搜索\]，对吧？因为你不能总是只依赖行动之前的 planning。实际执行任务时，可能会有不同的结果。如果你不确定，可以两种都试一下，看看哪种能带你得到正确结果，对吧？这对于让方法在现实世界中稳健运行非常重要。这里是一个示例任务，也相当困难：我买过这个产品多少次？这就要求模型首先

### [1:01:55](https://www.youtube.com/watch?v=Sk_TYpA6DWA&t=3715s) · b000075

导航到“我的账户”，查看，呃，“我的订单”，对吧？呃，进入“我的订单”，也可以尝试点击“我的可下载产品”或“我的愿望清单”。模型应该知道、理解，那不是正确的搜索路径，对吧？在“我的订单”里，有很多可以尝试的事情。比如，模型可以实际尝试查看每个订单，然后必须点击进去，检查它是否与我询问的那个产品相同。然后它必须遍历所有这些订单。对吧？这就是为什么你能看出，这是个相当困难的任务。所以，每个订单它都应该点击，对其中一些要计数，对另一些则不该计数，因为那是不同的产品。所以，这完全是一个复杂的实时搜索问题，其中某些轨迹，模型应该用某个价值

### [1:02:51](https://www.youtube.com/watch?v=Sk_TYpA6DWA&t=3771s) · b000076

函数（value function）进行剪枝（prune）。你可以把这个函数看作奖励，用来估计沿这条搜索路径走下去有多大可能解决任务。另一些路径也会被 prune，还有一些会继续搜索。这里有个好例子，对吧？横轴是你搜索的次数，在这里，搜索基本上指的是，呃，以这种 uncertainty 的方式，从模型中采样动作轨迹（action trajectories）的次数。所以，你每次 sampling，采样四次基本上就意味着给 agent 四次尝试，对吧？采样四条 trajectories，每次模型会并行尝试这四条，只要四条里有任何一条成功，就取成功的那条，对吧？绿色线是我们起步时的模型，也就是 Gemini 加 set of marks，红色线是

### [1:03:47](https://www.youtube.com/watch?v=Sk_TYpA6DWA&t=3827s) · b000077

当时最先进的（state-of-the-art）模型，那时是 GPT4V 加 visual encoder。从一次 sampling 开始，正好就是模型的起点。但如果你采样更多次，然后只取这个 best of n，对吧？majority best of n，那么最终，采样次数越多，你就会看到这条单调上升的轨迹，因为在这些样本中获得一条成功轨迹的可能性越来越大。对吧？这是非常初步、很有希望的结果，这些研究者展示了其中一些结果。但这也意味着，一个关键研究问题是，如何决定高效地采样什么，让模型的表现不至于随着样本数增加而缓慢增长，而是随着样本数增加而增长得快得多。这要求模型学到一个好的 value function，对吧？确定优先搜索什么，还需要一个好的排序函数（ranking function），来

### [1:04:42](https://www.youtube.com/watch?v=Sk_TYpA6DWA&t=3882s) · b000078

判断哪些 trajectories 是最好的。好的，这个，呃，叫作 best of end sampling \[字幕疑误，可能指 best-of-n sampling\]。嗯，是的，如今也非常非常重要。

### [1:05:04](https://www.youtube.com/watch?v=Sk_TYpA6DWA&t=3904s) · b000079

好的，最后，最后还有一件事我想展示。我们当然已经讨论了基础 agents，具备高层任务 planning、humor in the loop clarification \[字幕疑误，可能指 human-in-the-loop clarification，人在回路中的澄清\]、searching strategy 的 agents，也就是多次采样输出。显然，记忆（memory）对这些 agents 会非常关键，对吧？呃，这些 agents 的运行跨度越来越长，如果它们在搜索和使用 human feedback，这些内容都会增加模型的 context length。我们知道，随着这些模型的 context length 增加，对吧？inference 会越来越慢，它随 context length 按 n 的平方增长。更关键的是，你往往会遗忘信息，可能忘掉很久以前上下文中的信息。所以如今很多人正在把 memory 整合进这些

### [1:05:59](https://www.youtube.com/watch?v=Sk_TYpA6DWA&t=3959s) · b000080

模型。理想情况下，基于 memory 的 agent 能动态决定何时把东西存入 memory，更重要的是，何时从 memory 中丢弃东西，这样即使 agent 运行很长时间，memory 使用量和上下文窗口（context window）也大致保持恒定。\[清嗓子\] 所以，我组里一些人做的一件事，就是构建这个内存高效的 agent，基本上是在 agent 的 context window 中加入一个内部状态（internal state），这个 internal state 会不断用最新信息更新，而且在某个时刻，agent 也会决定丢弃这个 internal state。它看起来是这样的。每次从 perm t minus one \[字幕疑误，可能指 time t minus one，时刻 t - 1\] 到 t 的迭代，都会取之前的查询和

### [1:06:55](https://www.youtube.com/watch?v=Sk_TYpA6DWA&t=4015s) · b000081

信息，以及 t - 1 时刻的上下文，把它们存入 t 时刻的 internal state，对吧？然后这个过程递归进行，t 时刻的 internal state 用于执行下一步决策；下一步决策完成后，会把所有查询和当前状态重新存入 t + 1 时刻的 internal state。所以 internal state 的容量或长度始终固定，每一步都在不断更新和移除。可视化来看就是这样。左边现有的模型总是不断累积越来越多的信息，而我们的模型只保留一个 internal state，并强制模型丢弃之前的信息。

### [1:07:49](https://www.youtube.com/watch?v=Sk_TYpA6DWA&t=4069s) · b000082

所以，在回答多个问题时，你可以看到它能够更快地处理文档，保持更短的状态，并更准确地回答更多问题。

### [1:08:05](https://www.youtube.com/watch?v=Sk_TYpA6DWA&t=4085s) · b000083

好的，我们时间快到了。嗯，关于这个 memory agent，有什么问题吗？&gt;&gt; 是的，请说。&gt;&gt; 对。所以，当你有一个 internal stage \[字幕疑误，可能指 internal state，内部状态\] 时，它是像 markdown 文件那样压缩它看到的内容，还是一个表示它正在做什么的实际向量（vector）？它不是 markdown 文件。它只是文本，对吧？上下文文本。对。呃，我们最近有一些工作，把其中一些方法扩展到更多 agentic workflows，现在你可以访问各种 markdown 文件。你可以访问一些总结代码，等等。所以，这让它更加高效，而且也适用于多个 agents。它们可以各自不断读取和

### [1:09:02](https://www.youtube.com/watch?v=Sk_TYpA6DWA&t=4142s) · b000084

写入这个共享记忆（shared memory），而这个 shared memory 有这个，呃，这个 markdown 文件。很令人兴奋。好的。好。最后还有一点我想提到，就是向现实世界的扩展。对吧？我的意思是，大多数原理仍然适用。你有机器人看到的视觉输入，对吧？有人给这些 agents 的自然语言指令，还有这些想让你采取各种形式动作的 agents，对吧？视觉输入进入视觉 Transformer（vision transformer），并适配到 llama 模型中。这些就是 adapter 风格的方法。呃，这是一个 vision language model，最大的区别是，现在输出的是动作，对吧？不是文本输出，而是动作输出。在这种情况下，动作输出通常指机器人上的各种自由度（degrees of freedom），你的关节、力或转矩

### [1:09:59](https://www.youtube.com/watch?v=Sk_TYpA6DWA&t=4199s) · b000085

角度。呃，这些都是数值输出，对吧？所以这叫作 VA \[字幕疑误，可能指 VLA\]，视觉语言输入和动作输出。呃，所以它继承了基于语言的 reasoning 的许多优点，从基础语言模型快速 fine-tuning，通过再次 fine-tuning 动作解码器（action decoder），快速适配不同类型的机器人，对吧？你可以做 Laura \[字幕疑误，可能指 LoRA\]，可以做量化（quantization），以及语言模型上的所有标准技术，让这些模型高效运行。所以这些叫作 VLA 模型。嗯，最重要的部分，对吧？我可以，我把论文放在这里。我不是机器人领域的人，但最重要的部分也许是 action d decoder，或者他们称之为 d tokenizer \[字幕疑误，可能指 detokenizer，反词元化器\]，对吧？基本上创新就在这里。嗯，据我理解，让语言模型输出数字非常困难，

### [1:10:56](https://www.youtube.com/watch?v=Sk_TYpA6DWA&t=4256s) · b000086

对吧？你们大概都知道，即使只是让它把几个数字相加，或者做矩阵，呃，或者不同小数的乘法，往往也很困难。所以，这个动作反词元化器（action detokenizer）如今是用某种扩散模型（diffusion model）实现的，对吧？大家应该记得，diffusion model 是一种更适合连续数据（continuous data）的生成模型（generative model）。我们介绍 diffusion models 时看到，它们可以 defy images \[字幕疑误，可能指 denoise images，对图像去噪\]。它们可以使用 calcium noise \[字幕疑误，可能指 Gaussian noise，高斯噪声\]，解码并对图像像素进行 d noiseise \[字幕疑误，可能指 denoise，去噪\]。呃，所以 diffusion models 非常适合 continuous data。因此，很多这些 action detoizers \[字幕疑误，可能指 action detokenizers\] 实际上使用 diffusion models，基本上输出这些连续动作空间，比如机器人的角度、关节和旋转的变化。不过除此之外，其他一切都一样，对吧？你有视觉输入，有自然语言指令，你

### [1:11:54](https://www.youtube.com/watch?v=Sk_TYpA6DWA&t=4314s) · b000087

有这些连续动作输出。这整个系统可以训练。通常，vision encoder 可以 fine-tuning，使其适应你的 robotic seeds \[字幕疑误，可能指 robotic scenes，机器人场景\]。Adapter，也就是把视觉表征接入语言模型的部分，会进行 fine-tuning。语言模型本身的大部分会被冻结，而使用 fusion model \[字幕疑误，可能指 diffusion model\] 的 action decoder 也会进行训练或 fine-tuning。很好。对。所以还有更多例子。这篇论文包含大规模的视觉语言输入和真实动作（ground truth actions）数据，包含开源代码，也包含各种针对不同任务 fine-tuning 模型的方法。

### [1:12:47](https://www.youtube.com/watch?v=Sk_TYpA6DWA&t=4367s) · b000088

对。好的。就这些。总结一下，我们看了几个 AI agents 的例子，从仅处理语言的 agents，到 digital agents 和 embodied agents。这些只是视觉输入空间和 action space 不同的各种例子。我们看了一些 LLM 和这些 workflows 中部分组件的例子，对吧？我们强调的一些关键点，包括这些模型的 planning 能力，对吧？接收长指令，使用与上周所见类似的方法，也就是 SFT、prompting 或 reinforcement learning，让模型输出逐步的动作。对吧？所以这种 reasoning 非常重要。视觉表征非常重要，仍然是一个重大挑战。呃，如何让它更多地采用 human in the loop，以及它如何使用 search 尝试不同 trajectories，

### [1:13:44](https://www.youtube.com/watch?v=Sk_TYpA6DWA&t=4424s) · b000089

而这是提高表现的一种好方法。对吧？我们也看了一些如何交互的例子，可以自主运行，也可以保留 human loop \[字幕疑误，可能指 human in the loop\]。好的，还剩几分钟。关于这些还有最后的问题吗？如果没有，嗯，记得提交你们的项目期中报告，并留意本周稍后发布的作业 4。好的。谢谢大家。
