# Lecture 6 – Large Multimodal Models (MIT How to AI Almost Anything/Multimodal AI, Spring 2026)

_中文讲稿_

- Channel: Paul Liang
- Source: [YouTube](https://www.youtube.com/watch?v=H9nvkyTsrnI)
- Duration: 1:10:26
- Caption source: automatic
- Status: complete
- Chinese translation: 84/84
- Translation provider: codex
- Generated: 2026-09-07T07:55:53+00:00

## 讲稿

### [00:00](https://www.youtube.com/watch?v=H9nvkyTsrnI&t=0s) · b000001

好了，各位。2:35。我们开始吧。欢迎回来。呃，快速回顾一下接下来这一周的作业安排。作业 2 明天截止。希望大家都在推进。如果需要帮助，呃，今天和明天可以来我的答疑时间，或者助教的答疑时间。嗯，作业截止、截止、截止之后，我们会再次挑选一些同学，在这周四的课堂上展示自己的作业。呃，还是那句话，没有压力，只是分享你感兴趣的东西，和班上的其他同学分享。所以就在这周四。很遗憾，我要出差，临时有些行程安排。不过，我们会在前 30 分钟做这些展示，然后助教 vault \[字幕疑误，可能为人名\] 会深入讲解多模态 LLS \[字幕疑误，可能指 LLMs\] 的一些实现。这些会帮助你们完成作业三，作业三将会

### [00:55](https://www.youtube.com/watch?v=H9nvkyTsrnI&t=55s) · b000002

在本周晚些时候发布。好。所以记得周四来上课，参加作业 2 的这些展示，并学习这个关于 multimodel lls \[字幕疑误，可能指 multimodal LLMs\] 的详细教程和实现。多模态大语言模型（multimodal LLMs）将是今天讲座的内容和重点，我们会先从概念层面讨论，周四再深入实现细节。不过，还是让我快速回顾一下到目前为止课堂上学过的内容，然后用前 30 分钟完成关于多模态对齐（multimodal alignment）的讨论。我们从多模态学习（multimodal learning）的两个关键概念开始，第一个是融合（fusion），第二个是对齐（alignment）。回想一下，fusion 的关键区别在于，它确实是把不同的数据模态，无论在特征层面还是原始数据层面，接收进来并合并成一个表示，对吧？这个表示，我们称之为 fields \[字幕疑误，可能指 fused\] 或联合表示（joint representation），应该捕捉

### [01:52](https://www.youtube.com/watch?v=H9nvkyTsrnI&t=112s) · b000003

你的两个数据集之间发生和呈现不同交互的方式。所以从视觉上看，大概是这样。我们看过很多进行 fusion 的方式，包括加法式、乘法式、带有动态权重的方式，在特征层面和原始数据层面都可以。因此，核心就是接收两种不同的模态，学习一个结合这些信息的单一表示。然后我们转向 alignment，其目标略有不同。通常，目标是让模态保持分离，让表示保持分离，但通过识别一个模态的哪些部分与另一个模态的哪些部分对齐，为它们赋予上下文。因此我们看到，在第一种比较简单的情况下，我们假设各个模态可以轻松地离散化成独立元素。例如，句子中的单词，呃，某张图像中的对象区域。然后，alignment 的目标基本上就是学习这种匹配：单词的哪些部分

### [02:48](https://www.youtube.com/watch?v=H9nvkyTsrnI&t=168s) · b000004

与图像的哪些部分对齐。今天我会继续讨论 alignment，把这种离散对齐（discrete alignment）扩展到连续对齐（continuous alignment）。对于音频、视频和传感器等许多数据模态，如何分割成独立元素并不十分明确，这让 alignment 更具挑战性。最后，我们还强调，有些类型的 alignment 以对齐本身为最终目标，对吧？无论在离散还是连续的情况下，学习这种匹配就是最终目标。还有 alignment 的另一个子部分，学习这些连接只是学习更好表示的中间步骤。因此我们称之为上下文化表示（contextualized representations），它将引出一些 transformer，尤其是多模态 transformer：它们学习 alignment，但主要用它来学习更好的下游表示。

### [03:41](https://www.youtube.com/watch?v=H9nvkyTsrnI&t=221s) · b000005

再次快速回顾上周关于 discrete alignment 的内容。呃，我们主要讲了 contrasted learning \[字幕疑误，可能指 contrastive learning，对比学习\] 这个算法。它的目标还是，如果你有分割得很清楚的边界，比如一个句子和一张图像，或者一个单词和一个对象区域，你会学习两个独立的表示 Z1、Z2，一个用于语言，一个用于视觉。所以这与 fusion 不同，因为你没有学习一个合并的表示，而是让这两个表示保持分离，对吧？关键当然在于，通过它们之间的某种相似度函数（similarity function）来学习 alignment。这就是这两个表示之间有一个箭头的原因。这些相似度函数通常类似于余弦相似度（cosine similarity）。我们也看过将 cosine similarity 扩展到其他相似度度量的方式，而且不仅在样本层面，也包括分布层面的相似度度量。

### [04:36](https://www.youtube.com/watch?v=H9nvkyTsrnI&t=276s) · b000006

学习这种 a line representation \[字幕疑误，可能指 aligned representation，对齐表示\] 的一种简单方式，是假设你有正数据和负数据。正样本对（positive pairs）来自联合分布（joint distribution），也就是图像和它们实际对应的描述。你希望最大化它们之间的相似度，因此把这两个表示拉得更近。这就是分子上的这一项。与这些正样本相对，你还有负样本（negative samples）。负样本是从边缘分布（marginal distributions）中采样的。也就是随机采样一张图像，再随机采样一条描述。它们很可能并不对应，而你希望最小化这些表示的相似度。所以你要把它们推得很远，这就是这里底部的那一项，对所有负样本对求和，降低这些表示的相似度。

### [05:31](https://www.youtube.com/watch?v=H9nvkyTsrnI&t=331s) · b000007

我们还看到，呃，实际上可以给出一些具体论证，说明这些类型的 contrastive learning 和基于 alignment 的表示学习（representation learning）方法，本质上捕捉了两个模态之间的互信息（mutual information）。这是一种形式化的看法。它是来自联合分布的数据的比率。换句话说，正样本对除以边缘分布乘积的比率。也就是说，随机采样图像和文本，构成负样本对。contrastive learning、clip、其他基于 alignment 的度量，主要捕捉的就是这种 mutual information，这当然很好。然后我们讨论了，如果表示、你学到的信息主要位于共享空间内，那么这就是学习表示的一种很好的方法，对吧？如果信息超出了这个

### [06:29](https://www.youtube.com/watch?v=H9nvkyTsrnI&t=389s) · b000008

共享空间，它可能就不好用了，这意味着 alignment 没有给你足够的信号。如果这个共享空间太大，它也不好用，在这种情况下，alignment 给你的表示带来了过多信号和过多噪声。以上都是对上周 alignment 讨论和前一周 fusion 讨论的回顾。在进入今天讲座的内容之前，大家对回顾部分有什么问题吗？有。&gt;&gt; 能再多讲一点为什么重叠太多会成为问题吗，如果你的目标只是，嗯，alignment。比如，我理解，如果你试图构建表示，重叠太多会有很多噪声，但如果目标只是 alignment，那么是不是应该重叠越多越好——&gt;&gt; 正是如此，所以我说重叠太多不好时，我的意思是，如果

### [07:24](https://www.youtube.com/watch?v=H9nvkyTsrnI&t=444s) · b000009

alignment 学到的共享区域远多于任务所需。回想上一页幻灯片，我们有一个圆，里面标着标签 Y。呃，所以如果标签 y 相对于通过 alignment 学到的全部共享信息来说太小，那么你的对齐表示就捕捉了太多噪声。当然，如果你不关心 why \[字幕疑误，可能指 Y\]，只是关心对齐数据，那么目标就是在数据存在共享信息的范围内尽可能对齐数据。很好。所以，正如我们提到的，当你关心的内容超出共享信息时，这就可能带来麻烦，这让我们简短地转向表示 fision \[字幕疑误，可能指 fission，裂解\]。因此，有时可以结合 fusion 和 alignment，学习比最初的

### [08:21](https://www.youtube.com/watch?v=H9nvkyTsrnI&t=501s) · b000010

数据模态数量更多的表示，对吧？所以我们称之为 fision \[字幕疑误，可能指 fission\]。看待 fision 有不同方式。一种很直观的方式是，也许你学习某个负责捕捉共享信息的表示，如果这对任务来说不够，那么也可以学习更多表示，负责捕捉不直接位于共享区域中的独有信息。因此我们称之为模态层面的 fision。这意味着，如果有两个模态，你就有三个这样的，呃，三个表示，而且还可以进一步深入，对吧？可以做得更加细粒度，对吧？学习解耦的（disentangled）、聚类的（clustered）表示，让每个表示分别负责数据中一种不同的细小变化，显然有很多优点，但我不会详细展开。所以，这些 contrastive learning 扩展背后的直觉是，你可能想学习一些

### [09:17](https://www.youtube.com/watch?v=H9nvkyTsrnI&t=557s) · b000011

两个模态中都有的东西。例如，如果你有图像和文本，那么通常描述会提到人物，也会提到对象。因此，基于 alignment 的方法会学到这些。这就是中间的部分。然后，有些东西是语言独有的。例如，特定的句法结构、特定的语法，甚至特定的语言，对吧？这些更偏向语言独有的信息。还有一些信息是视觉独有的。例如，纹理、深度、透视方面的内容，这些都没有直接在描述中表达出来，对吧？因此，这些是图像独有的信息。所以已经有一系列工作被提出，来扩展 contrastive learning。这是我们的工作之一，叫作因子化对比学习（factorized contrastive learning）。你可以这样理解：中间有这种

### [10:14](https://www.youtube.com/watch?v=H9nvkyTsrnI&t=614s) · b000012

图像和文本之间的 alignment，对吧？你取图像，取描述，最大化图像与文本之间的正样本对，最小化负样本对，对吧？直观上，这就是学习重叠部分的方式。如何决定什么来学习图像中的独有信息呢？按照同样的逻辑，你会定义图像和同一图像的数据增强（augmentations），对吧？因此，图像的某些增强构成正样本对。例如，某些旋转、裁剪和平移。这些对应正样本对，而其他一些，比如随机采样的其他图像，就是负样本对。因此可以仅在图像内部进行这种自对比学习（self-contrastive learning），对称地，也可以在文本内部进行这种 self-contrastive learning。比如，取一条描述，把某些单词替换成语义相近的词，或者

### [11:10](https://www.youtube.com/watch?v=H9nvkyTsrnI&t=670s) · b000013

比如把现在时改成过去时。这些都是文本增强时的正样本对例子，你也可以考虑负样本对，也就是随机采样的其他描述。因此，这就构成了语言中的 self-contrastive learning。现在你有了这样一种图景，其中有三个表示。一个负责视觉与语言的重叠部分，一个只负责视觉，一个只负责语言。有什么

### [11:47](https://www.youtube.com/watch?v=H9nvkyTsrnI&t=707s) · b000014

问题吗？好。很直观，嗯，已经证明效果不错，也能处理这样一些场景：比如你的标签、你的任务不只是需要中间的信息，还需要每个模态中的独有信息。我会过一遍，所以这是 alignment 的一个扩展。我还会讲几个这些经典的基于 alignment 的方法的扩展。我会讲得比较快。如果你感兴趣，主要是给你指出适当的参考资料，如果它与你的研究、作业和项目相关。另一个扩展是全局对齐（global alignment）的思想。我们看到，在这种 discrete alignment 的情况下，通常需要局部层面的监督，对吧？比如你想知道，这张图像对应这条描述，或者

### [12:45](https://www.youtube.com/watch?v=H9nvkyTsrnI&t=765s) · b000015

更进一步，这个单词对应图像中的这个区域。因此，你需要在试图对齐的两个模态之间有这种配对数据。这就是如何得到正样本对，如何得到负样本对。当然，在许多场景中，很难获得这种配对数据。可能会有这样的场景：你有一批图像，另外有一批文本，你不知道它们之间如何匹配，但你仍然想学习这种 alignment。那么怎么办？我们称之为 global alignment，因为现在你试图在全局上对齐两个分布，你在每个分布中都有样本，但没有具体的单个配对。实现这一点的一种通用方式，是联合优化：既优化针对给定 alignment 学到的表示，又找出最优的 alignment 是什么。

### [13:41](https://www.youtube.com/watch?v=H9nvkyTsrnI&t=821s) · b000016

好，我这是什么意思？如果我知道，如果我能找到一种 alignment，这两个数据模态的一种配对，那么就可以做经典的 contrasted learning \[字幕疑误，可能指 contrastive learning\]，对吧？也就是目前为止我们看到的，假设我们知道它们之间如何配对。但当我们不知道如何配对时，可以尝试对不同的可能配对进行联合优化，从而既找到正确配对，也找到对应这个配对的正确对齐表示。好。所以要联合完成这件事。具体怎么做，我不会深入太多细节。有一些研究领域专门关注这个问题，但本质上，可以把它看作某种图匹配（graph matching）问题：比如给定四张图像和四条描述，你不知道它们如何配对。你可以在所有可能的配对中搜索，

### [14:38](https://www.youtube.com/watch?v=H9nvkyTsrnI&t=878s) · b000017

对吧？在最朴素的情况下，搜索所有可能的配对。因此，每种配对可以看作一侧四个元素与另一侧四个元素之间的 bjection \[字幕疑误，可能指 bijection，双射\]。所以这就是一个参数，即分配 f，一种 a 和 b 之间的二部图分配或 bjection 分配。而对于每个可能的分配，你都可以计算该分配的权重。例如，如果这个点和这个点匹配在一起，你就会试着找出这两个点的相似度，因为它们会被当作正样本对。然后你把这两个点之间的权重加起来，假设它们是正样本对，对吧？所以这些就是相似度权重，你本质上是在所有

### [15:34](https://www.youtube.com/watch?v=H9nvkyTsrnI&t=934s) · b000018

可能的排列，以及 A 和 B 之间所有可能的点分配中，优化出最相似的、相似度最高的那个。有一些高效的方法可以求解这个问题、它的松弛形式（relaxations）。显然，精确问题有点像 empty hard \[字幕疑误，可能指 NP-hard\]。不过，也有一些方法，不必检查所有分配，而是使用线性规划（linear programming），基本上是设置变量 Xig。Xig 表示这两个是一个正样本对，有连接时应该是 one，否则是 zero。你可以把这些权重中的每一个再次看作这些正样本对的相似度函数，本质上就是最大化权重乘以 x，x 是表示哪些元素互相配对的变量。在某些松弛条件下，可以把它看作一个 linear programming 问题，通过单纯形算法（simplex algorithm）求解。再次强调，这里的细节不是特别重要。如果

### [16:32](https://www.youtube.com/watch?v=H9nvkyTsrnI&t=992s) · b000019

你愿意，可以进一步阅读。关键思想仍然是，Contrasted learning \[字幕疑误，可能指 contrastive learning\] 和 alignment 要求你在想要对齐数据的分辨率上拥有配对数据。当做不到时，你可以联合优化：一边在数据中搜索不同配对，一边在假设某个特定配对的前提下学习这些对齐表示。可以把这两部分一起训练，希望在收敛时，你既学到了数据中的配对，也学到了该配对对应的对齐表示。

### [17:09](https://www.youtube.com/watch?v=H9nvkyTsrnI&t=1029s) · b000020

我再讲一页幻灯片，然后停下来回答问题。另一种扩展方式是，不只看一对一映射（one-to-one mappings），还可以看软映射（soft mappings）。也就是，对于一侧的每个元素，它在另一侧对齐到的元素分布是什么。嗯，soft mappings，而不是 one-to-one mappings。同样，也有形式化的研究方式。你可以搜索一个叫作最优传输（optimal transport）的领域，它基本上研究的是：两个模态之间怎样进行适当的权重软分配（soft assignment），才能最大化该分配的某个特定相似度函数。再次强调，这叫 optimal transport。它可以相当高效地求解。

### [17:57](https://www.youtube.com/watch?v=H9nvkyTsrnI&t=1077s) · b000021

大家对此有什么问题吗？

### [18:05](https://www.youtube.com/watch?v=H9nvkyTsrnI&t=1085s) · b000022

我没有深入太多细节，因为知道这些是有益的，而且在某些确实没有配对数据的特定应用中，它会很有用，但它不是如今整个多模态学习中最有用的算法。所以我想把时间花在更常用的东西上。我还想强调其他几个简短的扩展。一个是连续情况，对吧？我们看到，在离散情况下，对齐元素要容易得多。在连续情况下，还需要额外处理一个问题，基本上就是分割数据。那么怎么做？视频领域已经有成熟的算法，有将视频分割成动作的成熟算法。也就是找到那些

### [19:00](https://www.youtube.com/watch?v=H9nvkyTsrnI&t=1140s) · b000023

由视频中的边界表示的离散动作。对于时间序列数据（time series data），有基于变点检测（change point detection）的成熟方法。这些算法本质上会告诉你，时间序列数据中哪些变化在语义上有意义，哪些其他位置只是噪声，并不对应任何语义上有意义的变化。它们可以帮助你处理连续数据、找到合适的边界，然后就可以开始 alignment。

### [19:31](https://www.youtube.com/watch?v=H9nvkyTsrnI&t=1171s) · b000024

离散化（discretization）是另一个关键概念。如果你有连续数据，一种方式基本上就是学习聚类（clusters）。这里有一种非常流行的语音预训练（speech pre-training）方法。大家知道，语音数据是高度连续的。所以，如果想做掩码预训练（masked pre-training），就必须把目标从对离散 token 集的掩码预测（masked prediction）扩展到连续预测。但连续预测通常很难，对吧？连续回归（continuous regression）通常很难。大多数回归方法最后只是学到了平均信号，而不是信号的边界。因此，许多基于语音的预训练方法，首先接收连续信号，然后在表示、在表示空间中做一些聚类，K means clustering。一旦完成 K means clustering，我就会把预测

### [20:28](https://www.youtube.com/watch?v=H9nvkyTsrnI&t=1228s) · b000025

目标替换为聚类 ID（cluster ids），而不是连续语音信号本身。这意味着，当我开始把这些序列模型（sequence models）应用到语音上并学习表示时，我会遮住某些内容，然后预测那段特定连续信号属于哪个 cluster ID，而不是预测信号本身。

### [21:02](https://www.youtube.com/watch?v=H9nvkyTsrnI&t=1262s) · b000026

VQVA \[字幕疑误，可能指 VQ-VAE\] 是另一个例子，也就是向量量化变分自编码器（vector quantized variational auto autoenccoders \[字幕疑误，可能指 vector quantized variational autoencoders\]）。在如今几乎所有处理图像、视频、音频和各种连续数据的生成模型（generative models）中，你基本上是在学习表示：先对数据编码，然后在表示空间里做一些聚类、聚类或者量化（quantization），使这些表示不再是连续的，而是映射到一组离散 ID。因此，最后确实会映射到一组离散数字，比如 98、390。当然，离散 token 的数量通常非常大，大约在 2,000 到 5,000s 的数量级，但它会被映射到这个离散集合，然后再解码回图像。所以你可以把这些，嗯，这些

### [21:57](https://www.youtube.com/watch?v=H9nvkyTsrnI&t=1317s) · b000027

token 中的每一个看作视觉 token（visual token），对吧？就像模型中有文本 token（text tokens），大约有 70,000 个文本 token 的词汇表一样。这些图像里有 8,000 个 visual tokens。这些使图像模型更容易训练，更重要的是，使文本与这些模型之间更容易对齐，对吧？因为如今给这些模型提供提示的方式，是输入一些文本。例如，生成一张猫的图像。这会由一个 transformer 模型编码成 text tokens，然后这些 text tokens 与中间表示中的 visual tokens 对齐，接着再解码成图像。所以仍然必须把它们转换为离散形式，才能在这些离散 token 上进行 alignment。

### [22:54](https://www.youtube.com/watch?v=H9nvkyTsrnI&t=1374s) · b000028

好了。关于处理 continuous alignment 的方式，有什么问题吗？

### [23:10](https://www.youtube.com/watch?v=H9nvkyTsrnI&t=1390s) · b000029

好，在开始讲这些大型基础模型（foundation models）之前，alignment 的最后一个扩展，是隐式或涌现式对齐（implicit or emergent alignment）这个思想。到目前为止，我们看到的所有内容都采用显式对齐（explicit alignment），对吧？你有两个数据模态，为每个模态学习特征，然后定义一个函数，即相似度函数，明确地训练它，把正样本对拉近，把负样本对推远，对吧？所以你是在使用某个目标函数显式地施加 alignment。对于 implicit alignment 这一研究方向，多年来我看到过零散的论文，但也许是 2024 年这篇叫作 the platonic representation hypothesis 的论文，真正尝试让它更加形式化。它基本上指出，呃，这个假说指出，neuronet networks \[字幕疑误，可能指 neural networks，神经网络\] 在

### [24:06](https://www.youtube.com/watch?v=H9nvkyTsrnI&t=1446s) · b000030

不同的数据和模态上，用不同目标训练时，其表示状态正趋向于一个共享的现实统计模型。这个思想是，即使没有显式地强迫这些模型趋于一致，它们也在趋于一致，对吧？即使这些模型是独立训练的，它们也以某种方式逐渐趋同，表示空间越来越对齐。那么有什么证据呢？好，这里有一张图，横轴上，首先，这上面的每一个东西都是不同的语言模型。Bloom 语言模型，这些是一些开源语言模型，open llama 语言模型，然后是从 13、33 到 65 billion 的 llama 模型。因此，这些都是语言模型。你可以看到，特意选择了这些

### [25:00](https://www.youtube.com/watch?v=H9nvkyTsrnI&t=1500s) · b000031

开源语言模型，因为其中一些需要访问模型内部的隐藏表示（hidden representations）。所以它们是开源模型。好，这些全都是语言模型。这里的每个点叫作 Dino 模型。Dino 是一个计算机视觉（computer vision）模型，是对象识别（object recognition）和其他一些视觉任务中的最先进模型。横轴是语言性能（language performance），所以你看到，这些语言模型按它们在 NLP 任务上的表现排序。好。meta 的一些较大的 llama 模型，在语言性能方面更好。最关键的是，纵轴显示了与 dino v2 的 alignment。在这里，alignment 是某种相似度函数，我稍后会讲，但它是我们讨论过的相似度函数之一，基本上衡量的是：对于这些语言模型，我取出它们的隐藏表示；对于这些 Dino 模型，

### [25:57](https://www.youtube.com/watch?v=H9nvkyTsrnI&t=1557s) · b000032

Dino V2 模型，我取出隐藏表示，然后给定某个配对的图像描述数据集，语言表示与视觉表示之间的相似度是多少。你可以看到，随着语言性能越来越好，这个 alignment 也越来越好；同时，这些 dino 模型从小变大，也隐含着视觉性能越来越好。好，所以 alignment 在增加，但关键当然是，llama 和 dino 一开始从来没有被显式对齐过，对吧？一个是由 meta 训练的，Dino 是由其他一些人训练的，对吧？它们是完全独立的模型，架构完全不同，一开始从未对齐过。但是，随着语言模型变得更好，以语言性能衡量，以及这些视觉模型变得更好，以视觉性能衡量，它们的 alignment 分数在

### [26:52](https://www.youtube.com/watch?v=H9nvkyTsrnI&t=1612s) · b000033

随时间提高。因此，这就是他们的，这就是提出该假说的实证发现：这些表示正在趋同，尽管它们来自不同的模型，这些模型在不同数据、不同模态上完全独立地训练。&gt;&gt; 问题。&gt;&gt; 这是不是意味着，随着规模扩大，所有模型都会成为世界模型（world models）？如果你相信这个表示，呃，这个假说，那么也许是的。当然，这是一个假说，对吧？有实证证据，一些实证证据支持它，也有反对它的证据。我会展示其他一些后续工作，它们说这可能对某些超参数（hyperparameters）相当敏感。不过，说是这样也并不牵强，你知道，随着这些模型持续训练、规模扩大，在世界的不同视角上表现越来越好，

### [27:49](https://www.youtube.com/watch?v=H9nvkyTsrnI&t=1669s) · b000034

它们最终也许会趋向同一个 world model，对吧？每个模型都在学习那个 world model 的一个切片。关于这些，关于这些发现，还有其他问题吗？好。这些只是，嗯，这些是其他观察结果，对吧？例如，他们展示了 alignment 分数通常随语言性能提高而上升，与 clip、MAE 的 alignment 更好；MAE 是 mass autoenccoders \[字幕疑误，可能指 masked autoencoders，掩码自编码器\]，还有 imageet \[字幕疑误，可能指 ImageNet\] 预训练模型、其他 clip 模型。看起来，随着这些语言模型变得更好，它们以某种方式与这些视觉模型越来越相似。请说。&gt;&gt; 是的，所以，也许我稍后会弄明白。我没跟上你刚才说它们是否会彼此对齐的部分，还是说实际上只是根据它们的相似性来评判。

### [28:47](https://www.youtube.com/watch?v=H9nvkyTsrnI&t=1727s) · b000035

&gt;&gt; 所以，它们只是根据嵌入（embeddings）的相似性来评判。这些模型从未被训练成彼此对齐，对吧？Llama 在预训练时只是进行下一个 token 预测（next token prediction），之后再进行某种微调（fine-tuning）、指令微调（instruction tuning）。Dino 被训练来做对象识别。所以它们是完全独立的模型，从未被训练成相互对齐。这就是我们说这种 alignment 是 emergent 或 implicit 的原因。嗯，是的，这里只是更多证据。语言性能变好，alignment 就变好。简单说明一下所使用的相似度函数。这里使用的是全局相似度（global similarity），我们之前看到过：比如在图像中有三个概念，对吧，苹果、橙子和大象，而在文字中有

### [29:42](https://www.youtube.com/watch?v=H9nvkyTsrnI&t=1782s) · b000036

苹果、橙子、大象，这种 alignment 并不真正关心苹果图像是否接近“苹果”这个词，不关心这一点。它只关心，在图像中，苹果和橙子彼此接近，而大象很远；另外在文本中，苹果和橙子彼此接近，而大象很远。因此，它并不真正捕捉局部相似性（local similarities），而是捕捉两者中语义上有意义的概念的全局分布。实际操作上，他们称这些为核（kernels）。基本上，对于图像 embeddings，所有图像 embeddings，我首先找到的基本上是它们之间的 coariance matrix \[字幕疑误，可能指 covariance matrix，协方差矩阵\]，对吧？这就是这个 kernel 所做的事情，基本上有一个 coarance matrix \[字幕疑误，可能指 covariance matrix\]，告诉我所有这些图像表示相对于彼此如何分布。然后对于文本 embeddings，我计算所有这些文本 embeddings 相对于彼此如何

### [30:40](https://www.youtube.com/watch?v=H9nvkyTsrnI&t=1840s) · b000037

分布。有点像 coariance matrix \[字幕疑误，可能指 covariance matrix\]。一旦你有了这两个分别训练的矩阵，alignment 的度量就是这两者彼此有多相似。好。所以它是在更全局的层面衡量 alignment，对吧？跨越一批文本和一批图像。最后，我会用这个简短视频结束 alignment 的讨论。这个视频出来后，有点像是在反驳 platonic representations 中的一些发现，同时补充了一些新发现，只是想说明，这还是一个开放的领域，实际上没人真正知道发生了什么，也不知道 alignment 到底是不是涌现出来的。所以我来播放这个视频。

### [31:52](https://www.youtube.com/watch?v=H9nvkyTsrnI&t=1912s) · b000038

正如我们所见，语言模型越来越大、越来越好，alignment 也在增加。但他们展示的是，经过这种校准（calibration）之后，存在一些混杂因素（confounders），alignment 实际上消失了。Global alignment 消失了，但令人惊讶的是，局部对齐（local alignment）仍然存在。所以你就给这个假说另起一个名字。

### [32:26](https://www.youtube.com/watch?v=H9nvkyTsrnI&t=1946s) · b000039

所以也许，这大概就是关键收获：之前在 platonic representations 中，我们看到，你取 A 的所有 embeddings，计算它们的 kernel 协方差，考察全局结构；然后对 B 计算整个全局结构，再计算某种相似度。他们说，其中有一些 confounders，大部分 alignment 和相似性都会消失，但这些局部结构仍然存在。所以你把范围限制在一个小邻域内，考察哪些点彼此靠近，这种局部相似性仍然与另一个 embedding 空间中的局部相似性相似。因此 global alignment 消失了，而 local alignment 仍然存在。这基本上就是说，有时在 alignment 中，相似度函数的概念以及你测量的内容，实际上会对最终得到的表示和结果产生非常大的影响，所以必须非常小心。请说，

### [33:22](https://www.youtube.com/watch?v=H9nvkyTsrnI&t=2002s) · b000040

&gt;&gt; 在这种情况下，calibration 是什么意思？嗯，它基本上是一种扰——你可以查看论文中的更多细节，但基本上，它对模型进行了扰动，使 global、global alignment 有点被破坏了，但 local alignment 仍然保留。它是一种，嗯，是的，基本上是把全局结构与局部结构解耦的方法。关于 alignment，还有最后的问题吗？好，总结一下，我们先看了 alignment 的介绍。我们看了最重要的概念，即如何使用 contrastive learning 等方法显式地对齐数据。我们展示了它与 mutual information 的关系、它什么时候会成功，以及有哪些潜在风险。然后，我们讨论了 alignment 的一些扩展，比如当

### [34:18](https://www.youtube.com/watch?v=H9nvkyTsrnI&t=2058s) · b000041

你没有精确配对时，需要做 optimal transport，或者在学习 alignment 的同时学习分配和映射，还有一些对连续场景的扩展。最后，我们还看到了一些非常令人兴奋、但也令人困惑的近期现象，即隐式涌现的 alignment，对吧？关于 alignment，最后还有什么问题吗？

### [34:52](https://www.youtube.com/watch?v=H9nvkyTsrnI&t=2092s) · b000042

好，我们进入下一个主题，也是今天讲座的重点：大型多模态基础模型（large multimodal foundation models）。会涵盖一些多模态 transformer、foundation models、适配它们的关键方式，以及从文本生成（text generation）走向多模态生成（multimodal generation）。不过先回顾一下，除非你一直与世隔绝，否则大家都知道什么是大语言模型。它们凭借在海量数据上进行 pre-tuned \[字幕疑误，可能指 pre-trained，预训练\]，经过 fine-tuning 和 instruction tuning，如今又被适配用于 test reasoning \[字幕疑误，可能指 test-time reasoning，测试时推理\]，能够回答任意问题。它们可以进行多轮开放式对话。它们可以执行任何经典的 NLP 任务，无论是翻译、词性标注（part of speech tagging）、文档摘要等等。如今它们还连接了工具和搜索，因此可以检索新闻、进行计算，并实时操作你的电脑。而凭借如今

### [35:49](https://www.youtube.com/watch?v=H9nvkyTsrnI&t=2149s) · b000043

更好的测试时推理（test time inference）和 reasoning 能力，它们可以完成更难的多步骤任务，比如解决非常难的数学题，编写大量代码、检查代码、编写测试用例等等，对吧？当然，这些能力即使在今天也仍在提升。所以，现实世界中的大多数场景当然不只是使用大语言模型，而是使用这些大型多模态模型，因为文本往往不是这些模型需要关注的唯一输入。它们需要看图像、看视频，需要访问电脑，无论是 JSON 表示、文档还是其他文件。因此，显然大家对这些大型多模态模型很感兴趣。为了说明我认为它们会走向哪里，我会举几个例子，说明我们可能希望它们做什么，假设除了文本之外，它们还能看到和听到这段视频

### [36:44](https://www.youtube.com/watch?v=H9nvkyTsrnI&t=2204s) · b000044

中的内容。所以我来播放这段简短的视频。&gt;&gt; 能看着你的大脑运转，真是一种荣幸。&gt;&gt; 能看着你的大脑运转，真是一种荣幸。显然，你们所有人都能回答，而我们也可能希望大型多模态模型回答各种问题，对吧？从基本的分类问题，比如穿灰色衬衫的男人是什么语气：他在讽刺，有点无礼。到开放式问题，比如能否描述他们之间的关系。这些模型应该能够识别出，他们其实是 Big Bang Theory 中的角色，这样做是为了通过讽刺和无礼制造幽默，但他们实际上彼此是很好的朋友，并解释为什么。所以要通过领域知识（domain knowledge）来解释，也许甚至引用之前的剧集。现在，就有了推理和解释这个概念，不仅通过文本，还通过

### [37:41](https://www.youtube.com/watch?v=H9nvkyTsrnI&t=2261s) · b000045

引用之前的视觉剧集片段或之前的听觉信息。你还能让这些模型生成内容吗？以此作为一个场景，但生成更多后续视频，对吧？沿着他们的故事线，生成未来的剧集，甚至可能提出反事实问题（counterfactual questions）。我们用动画呈现，如果这个人来自另一种文化，会作何反应。他们会觉得被冒犯，还是仍然觉得同样幽默？这些都是如今一些多模态模型能够解决的任务，也许，直到最后这两项之前。当然，我们也看到，统一多模态理解与生成（unified multimodal understanding and generation）任务正在快速进步。所以在我看来，大多数模型的运作方式分为几个步骤。显然，它们接收多模态数据。我现在展示的是文本、音频和视频，不过当然还可以有更多扩展，可以是任何东西。它们

### [38:38](https://www.youtube.com/watch?v=H9nvkyTsrnI&t=2318s) · b000046

必须学习多模态表示，将它们结合起来，学习它们之间的交互与 alignment。我们看到的所有这些基本多模态概念，都必须包含在这个表示中。然后，它们还必须能够继续探查这些表示。你可以提出问题，得到相应答案；可以交给它其他任务，它也可能生成其他模态作为回应。而这些会在与用户的交互中持续多轮，对吧？所以，要构建这些模型，我认为有三个关键部分。第一个关键部分，就是利用这些大规模预训练的 foundation models 学习多模态表示，学习这些强大的表示。另一个关键部分是，一旦有了这些表示，你如何快速地

### [39:33](https://www.youtube.com/watch?v=H9nvkyTsrnI&t=2373s) · b000047

对一个可能已经预训练过的大语言模型进行条件化（condition），让它关注、查看、理解这些表示？这样，下一次你向这个模型提问时，它就不只是回答你的问题，而是真的在查看提问所针对的视频表示。因此，我们将其称为通过多模态文本生成（multimodal text generation）来适配大语言模型。最后，除了用文本回答问题，它是否还能产生其他模态的输出？对吧？例如，能否突出展示之前的剧集片段？能否生成下一帧？这些任务也都涉及生成多模态数据。所以第三部分是支持文本和图像生成，更广泛地说，支持 multimodal generation，对吧？当然，很明显，这是一条通向通用人工智能（AGI）的路径，因为它必须包含多模态输入表示、多模态输出，以及

### [40:29](https://www.youtube.com/watch?v=H9nvkyTsrnI&t=2429s) · b000048

当然，在长时间内与人进行多次交互。&gt;&gt; 关于这个示意图有什么问题吗？有。&gt;&gt; 我有。也许不是关于 sematic \[字幕疑误，可能指 schematic，示意图\] 的，这可能是一个很傻的问题，但它要怎样识别那是在讽刺？它不能，会通过 boss voice processing \[字幕疑误，可能指某种语音处理\] 来做 multimodelled \[字幕疑误，可能指 multimodal，多模态\] 吗？是视觉交互吗？考虑到他，特别是 Sheldon，他的表情非常没有情绪——&gt;&gt; 对。&gt;&gt; 再加上字幕，比如给有听力障碍的人看的 CC captions，那么它怎么识别那是在讽刺？&gt;&gt; 当然，我会用数据来训练这个模型，对吧？模型将能够得到输入。不过，在这种情况下，大概是原始视频和原始音频。通过原始视频，它能看到你们在这里看到的一切。通过原始音频，它能听到语气

### [41:27](https://www.youtube.com/watch?v=H9nvkyTsrnI&t=2487s) · b000049

，而语气是判断讽刺的重要指标。而且大概，我的意思是，如果用这些预训练知识把模型训练好，它就会通过人脸识别（facial recognition）识别出，这些来自 big bang theory 的语境，对吧？在这种情况下，已经有一个先验（prior），即这些人经常彼此开玩笑、互相讽刺。是的，我会讲一些细节。所以，这个示意图是：如何首先学习这些表示，让它们非常强大，理想情况下通过自监督（self-supervised）预训练；如何适配 LLM，使它真正关注并理解这些表示；以及如何从 text generation 走向 multimodal generation。第一个问题，当然，毫不意外，如今学习这些多模态表示的主要方式，就是通过

### [42:24](https://www.youtube.com/watch?v=H9nvkyTsrnI&t=2544s) · b000050

transformer，对吧？这些数据中的大多数，尤其是流式多模态数据（streaming multimodal data），例如输入某个聊天机器人的文本，都可以看作 token 序列。静态图像是图像块（patches）的序列，视频是帧（frames）的序列。同样，音频、传感数据如今也都被看作不同元素的序列。因此，可以使用 transformer 的自注意力（self attention），基本上学习这些元素之间的 alignment，学习它们彼此对齐和交互的不同方式，并以此为下游任务（downstream tasks）学习更好的表示。这正是我们所说的这一类子挑战，即 contextualized representations：我们希望学习单词的部分、面部的部分与声音的部分之间的 alignment。但不只是学习这些 alignment 并交给用户，而是要利用这些 alignment 学习这些

### [43:20](https://www.youtube.com/watch?v=H9nvkyTsrnI&t=2600s) · b000051

更好的下游表示，从而更好地进行分类、检测、问答，以及与人交互。这就是我们所说的 contextualized representations 的一个具体例子。如今，一种流行的做法是使用这些多模态 transformer。早些年我们在这里做过一些早期工作。从高层面看，它是单模态 transformer（unimodal transformers）的扩展，你们大多数人可能已经熟悉了，而且我们也在课程第二周讲过，对吧？关键公式还是在这里。从示意图来看，可能发生的是：假设有一些文本输入，一些上下文或提示，或者某个人说的话。为简单起见，我假设只有三个单词，三个单词。所以这是 X1，必须与 W

### [44:18](https://www.youtube.com/watch?v=H9nvkyTsrnI&t=2658s) · b000052

Q 相乘。你可以把它看作一种投影（projection），把文本输入原本所在的维度空间映射到某个共同的 D 维空间，在该空间进行 multimodal alignment。所以，这是从某个文本 token 空间到这个 D 维空间的线性变换（linear transformation）WQ，而且这个线性变换会被学习，是一个可学习参数（learnable parameter）。另一侧，可能有视觉或听觉信息。在这个例子中，序列长度是 four，而不是 three。它可以与文本长度不同。因此，这可能包含声音重读、翻白眼，以及其他一些非语言特征（non-verbal features）的信息。所以这是 x2 的转置，它也会乘以某个可学习参数 wk。这个参数会把非语言输入原本的

### [45:13](https://www.youtube.com/watch?v=H9nvkyTsrnI&t=2713s) · b000053

维度映射到同样的 d 维表示空间，与这里的 d 相同，并在这个空间进行 multimodal alignment。好。所以现在你有 3x dx4，转置后做这个乘法，如这里 \[哼鼻声\] 所示。这个乘法是在维度向量上进行的。所以，在这个多模态嵌入状态的维度上进行的乘法，给出了这个 3x4 矩阵。它可以看作多模态注意力矩阵（multimodal attention matrix）。在这个例子中，它是一个视觉到语言注意力矩阵（vision to language attention matrix），基本上告诉你 alignment 的模式，对吧？三个单词中的哪些应该与四个非语言表达中的每一个对齐，以捕捉它们之间信息量最大的交互。因此，这是一个 3x4 的加权外积（weighted outer product）。我们

### [46:10](https://www.youtube.com/watch?v=H9nvkyTsrnI&t=2770s) · b000054

之前看过所有这些常数。这里用 D 的平方根做归一化（normalization），所以方差会按 one overd \[字幕疑误，可能指 1/D\] 降下来。这样，这些数值的大小就不会随着维度增加而增长过快。softmax 基本上把每一行变成一组非负且总和为 one 的数。因此有一个归一化常数，使这些注意力值（attention values）更容易解释，也让训练更稳定。完成后，你基本上就学到了它们之间的 alignment，对吧？这里 privilege 与声音重读的对齐值是 7 \[字幕疑误，可能指 0.7\]。所以这个配对很重要。而单词 privilege 与翻白眼的对齐值是 point three。所以那个配对也很重要。当一个人过度重读 privilege，或在说完后翻白眼，它的含义就会改变。同样，也许单词

### [47:04](https://www.youtube.com/watch?v=H9nvkyTsrnI&t=2824s) · b000055

mind 也会发生变化，需要与声音重读对齐。好。所以，这就是学到的 alignment，这个 3x4 的 alignment 是作为一个潜在步骤（latent step）学到的，对吧？这不像 discrete alignment 那样，是你所需的全部，而只是某个中间步骤。然后，这个中间步骤被用于真正学习更好的表示。那么，它可能是什么样？你会有非语言特征的另一份副本，通过某种变换再次进入这个维度空间，大小是 4 by d。所以现在你有一个 3x4 的注意力矩阵，乘以 4 byD 的特征，得到最终的 3xd 输出，对吧？怎么解释这个输出呢？有三个，因此它是语言的新表示，三个单词各有一个。

### [48:01](https://www.youtube.com/watch?v=H9nvkyTsrnI&t=2881s) · b000056

对于第一个单词 privilege，它查看与四个非语言特征对应的四个 alignment 权重，取 7 \[字幕疑误，可能指 0.7\] 乘以声音重读特征，再取 .3 乘以翻白眼特征。因此，这就是 privilege 的一个新表示，以存在声音重读和翻白眼这一事实作为上下文。同样，单词 mind 的下一个特征，通过与声音重读之间为 one 的权重获得上下文。这个过程会对三个单词逐一进行。

### [48:37](https://www.youtube.com/watch?v=H9nvkyTsrnI&t=2917s) · b000057

所以，这是一个语言表示，现在已经利用四个 alignment 权重和四个 verbal features \[字幕疑误，可能指 non-verbal features，非语言特征\] 进行了上下文化。然后，这个语言表示可以用来预测任务结果，在这里就是讽刺。所以，这里唯一的监督来自：视频作为输入，对吧？三个单词、四个非语言表达，以及讽刺标签。你有一批讽刺视频和非讽刺视频。而所有这些都在潜在空间（latent space）中训练，对吧？所以 alignment 在 latent space 中完成，而这个 alignment 带来了更好的表示，对下游任务有用。这就是我们称之为对齐表示（aligned representation）的原因。

### [49:30](https://www.youtube.com/watch?v=H9nvkyTsrnI&t=2970s) · b000058

对此有什么问题吗？请说。

### [49:45](https://www.youtube.com/watch?v=H9nvkyTsrnI&t=2985s) · b000059

时间上的 alignment。&gt;&gt; 呃，很好的问题。所以，这确实是一个时间维度，对吧？有三个单词，随着时间依次说出。就是一个人按顺序说出的单词。这些则是按顺序呈现的非语言表达。所以，你先重读那个词，再翻白眼。当然，我在这里省略了一点，但这也是 transformer 的标准做法：严格来说，要对每个元素应用位置编码（position encoding），对吧？position encoding 是这种类似余弦波的东西，基本上标识这里是时间 zero，这里是时间 four。一旦有了它，这个注意力矩阵就确实捕捉了时间维度，对吧？它捕捉到 I rolling \[字幕疑误，可能指 eye rolling，翻白眼\] 是第四步，是在说出那个

### [50:39](https://www.youtube.com/watch?v=H9nvkyTsrnI&t=3039s) · b000060

请说。&gt;&gt; 像视觉语言特征（vision language features）这样的东西，tokenization \[清嗓子\] 能细到什么程度？因为可以想象，有些细微的面部表情，可能无法被当前的 open space \[字幕含义不明\] 捕捉到。&gt;&gt; 是的，是的。我的意思是，这是一个开放问题，对吧？很难像文本那样，为图像设计一个固定的分词器（tokenizer）。所以不同上下文会取决于不同的东西。有时候你只有一帧人脸图像，这时有机会做更细粒度的 tokenization。但如果是视频，就有多个帧构成的时间维度，可能无法在每一帧内部做大量 tokenization。这也与特征提取（feature extraction）方法兼容。所以，这可能不是原始数据，但如果有非常好的语音模型，能够

### [51:35](https://www.youtube.com/watch?v=H9nvkyTsrnI&t=3095s) · b000061

把声音重读提取为一个概念，或者有人脸关键点模型（facial landmark models），把眼部运动识别为离散概念，那么它们也可以作为这些下游 transformer 的输入。我来展示一个例子。这比我刚才展示的更细一些。但在这个例子中，这是在图像和描述上训练的视觉与文本 transformer。你有这些图像，也有这些描述，基本上只是训练它，比如做一些 fusion 和检索（retrieval）。这里展示的是，每个单词对应的注意力分数、在图像像素上的 alignment 分数，对吧？这些就是它们所采用的 visual tokens 的分辨率。然后你就开始看到，当模型接收

### [52:32](https://www.youtube.com/watch?v=H9nvkyTsrnI&t=3152s) · b000062

单词 flowers 时，查看它与 image patches 的 alignment 分数，它确实突出了花朵。它确实突出了墙壁。在查看、处理单词 cloudy 时，它在看背景。当输入 token 是 rug 时，它会突出地毯，还有 plant，等等。所以，这些多模态 transformer 中的 alignment 分数具有相当不错的可解释性。

### [53:07](https://www.youtube.com/watch?v=H9nvkyTsrnI&t=3187s) · b000063

好。那么，在许多预训练模型中，通常如何使用这些模型呢？一般来说，对于图像、图像流，有仅视觉的 transformer，在视觉内部做 self attention；对于文本流，在文本内部做 self attention，学习特征。然后有这些交叉流（cross streams），对吧？也就是视觉到语言的 attention，以及语言到视觉的 attention。两者并不相同，对吧？它们可以不同，然后被用于下游任务。所以这些是 cross model transformers \[字幕疑误，可能指 cross-modal transformers，跨模态 transformer\] 和 unimodal transformers。有时人们发现，可以把这些多模态 transformer 与更多 alignment 目标结合起来。例如这个模型，是最早的视觉语言模型（vision language models）之一，输入一批图像和 image patches，以及带有 text tokens 的文本。它们进入

### [54:04](https://www.youtube.com/watch?v=H9nvkyTsrnI&t=3244s) · b000064

这个多模态 transformer，学习表示。看看他们设计了哪些目标，对吧？一个目标是 mass language modeling \[字幕疑误，可能指 masked language modeling，掩码语言建模\]。你向模型展示图像区域和描述的一部分，模型必须根据语言上下文，同时查看视觉上下文，来预测 mass tokens \[字幕疑误，可能指 masked tokens，被掩码的 token\]。然后还有反过来的方式：向模型展示完整描述和图像的部分区域，图像中有一些位置被掩码（masking）。这时模型必须根据图像剩余部分，同时参考文本，预测图像中哪些内容被遮住了。你可以把这些看作 local alignment，然后还有更全局的 alignment。你有完整的、完整的图像块和完整描述，它们有一些正样本对和负样本对，并尝试区分它们。所以，遮住单词、遮住图像，以及

### [55:01](https://www.youtube.com/watch?v=H9nvkyTsrnI&t=3301s) · b000065

询问一个句子是否与整张图像匹配。有一篇 line before fuse \[字幕疑误，可能指 Align before Fuse\] 论文，是我们布置的阅读材料。你可以把它看作类似 clip、clip 的 contrastive learning。图像和文本输入后，各自学习一些特征，图像特征和文本特征。然后利用图像文本 contrastive learning，先通过正样本对和负样本对来对齐这些特征。在这些特征已经被某个对比模型预先对齐之后，它们再进入多模态 transformer。

### [55:48](https://www.youtube.com/watch?v=H9nvkyTsrnI&t=3348s) · b000066

好，所以有各种各样的方法来做这些事情。嗯，我个人觉得这个领域相当混乱，而且非常依赖实证，关于哪些 alignment、哪些 embeddings 在哪里完成，并没有太多结构可言。不过，把整个领域呈现出来还是有益的。有什么问题吗？

### [56:16](https://www.youtube.com/watch?v=H9nvkyTsrnI&t=3376s) · b000067

好了，我们进入第二部分。正如刚才讨论的，第一部分主要是把不同的数据模态当作序列。一旦把它们当作序列，这些多模态 transformer 就是很好的方法，可以学习哪些元素与哪些其他元素对齐，并利用这一点学习下游表示。不过，只有在你能适配语言模型，让它真正关注、查看这些表示以解决任务时，这才有用。所以，这里有一种通用做法，叫作适配器（adapters）。这些 adapters 的工作方式是：通常，你可能有一个预训练语言模型。好。理想情况下，你想让这个预训练语言模型保持冻结（frozen），不要过多更新它，因为它已经包含了大量强大的信息，而且你大概也不可能对它进行 fine-tuning 或任何调整。假设你还关心另一个数据模态，比如

### [57:14](https://www.youtube.com/watch?v=H9nvkyTsrnI&t=3434s) · b000068

图像。这些 adaptors 的工作方式是，先取这张图像，从中提取一些特征，对吧？也许用预训练的 CNN 或 vision transformer，提取一些特征。现在，语言模型并不能理解这些特征，它们甚至不符合语言模型的输入维度。但你可以设计这些 adapters。它们非常简单、轻量，有时甚至可以只是线性变换，基本上把这些 image embeddings 转换到某个与语言模型输入维度一致的 embedding 维度。好，在这里就是 token embedding 的大小。然后，把这些经过适配的表示作为前缀（prefix），添加到你输入的语言上下文前面。这样基本上就得到了这个适配后的语言模型，对吧？它仍然保留大部分预训练 elevation \[字幕疑误，可能指 information，信息\]，唯一的变化是一个 adapter，

### [58:11](https://www.youtube.com/watch?v=H9nvkyTsrnI&t=3491s) · b000069

你把它加在开头，将这些 image embeddings 投影到语言模型可以接收的 token embedding 空间。那么如何训练呢？先给它图像，进行适配，再给它描述，然后进行自回归预测（autoregressive prediction）：给定这张图像和描述中的前文，预测下一个词。因此，在某个时刻，它会学会一边看图像，一边预测“水中的红船”。完成后，实际上可以非常快。在这个例子中，它极其轻量。这个 adapter 通常只是一个线性变换，所以训练效率很高。完成后，你就可以给它其他新图像，向它提问，它就可以开始正确回答。回答是蓝色。你可以做上下文学习（in context learning）。比如，给它一张图像，问它一个问题：“谁发明了这个？”并提供

### [59:09](https://www.youtube.com/watch?v=H9nvkyTsrnI&t=3549s) · b000070

答案 the right brothers \[字幕疑误，可能指 the Wright brothers\]。然后给它一张新图像和问题：“谁发明了这个？”答案处留空。这就是一种 in context learning，对吧？你提供一个例子作为前缀，然后提供下一个例子的指令，模型就能回答 Steve Jobs。现在也可以做两个示例的 in context learning。比如，给它这张苹果图像，获得这个特征表示，并把它适配成前缀。然后给它一条描述，说“这是一个 DAX”，其中 DAX 是一个编造的词。再给它第二个例子，一张橙子图像，说“这是一个 blickicket”，其中 blickicket 同样是编造的词。这些就是 incontext prompts，用于 incontext learning 的两个示例。然后给它第三张苹果图像，问“这是什么？”模型通过这种模式映射

### [1:00:04](https://www.youtube.com/watch?v=H9nvkyTsrnI&t=3604s) · b000071

识别出这是一个 dax。所以，这是两个示例的 in context learning。&gt;&gt; 请说。&gt;&gt; 像这样的任务，会在多大程度上受到训练数据中已经有这种发展性任务的影响？这在认知科学中是一个经典的发展性任务。&gt;&gt; 是的。&gt;&gt; 它是从那里学来的，还是确实在学习这个表示？&gt;&gt; 嗯，它可能知道这是一种图像绑定的发展性任务，但它仍然必须真正计算这些图像在 embeddings 中的相似度。所以，它成功做到了这一点。它仍然必须完成这些 image embeddings 与这两个新词之间的绑定（binding），也就是符号绑定问题（symbol binding problem）、符号落地问题（symbol grounding problem）。所以它在这方面是成功的。这只是一个快速的展示方式，首先说明，这些特征确实被模型使用了，对吧？这个 adapter 已经

### [1:01:01](https://www.youtube.com/watch?v=H9nvkyTsrnI&t=3661s) · b000072

成功了，而且模型能够完成这个自然语言绑定问题。不过我同意，是的，模型大概知道这是什么任务。好。所以，这些适配后的语言模型确实很关键，而且其中大多数如今仍在使用。正如你们大概知道的，如今大多数 Frontier 模型、语言模型都更好了。它们经过预训练，保持冻结。如今主要的重点确实在于拥有非常好的视觉编码器（visual encoders），以及把它们很好地适配到这些预训练语言模型中。所以你可以看到这样的例子：这是一个非常早期的模型，叫作 Flamingo，是一些 Gemini 模型的前身。你可以给它一张图像，问图中发生了什么，它会说，这是一张两只泰迪熊在月球上的图片。它们在做什么？它们在交谈。它们在使用什么物体？看起来像一台电脑。所以，

### [1:01:59](https://www.youtube.com/watch?v=H9nvkyTsrnI&t=3719s) · b000073

图像的 grounding 和描述都相当不错。这个例子中，你可以问模型这是什么。模型会说：“这是一个贴着贴纸的 Apple。”贴纸上写着，贴纸上写着 iPod。呃，这是一个玩笑，因为以前的图像识别模型，如果给它这张图像，它实际上会说这是 Apple iPod 手机，而不是识别出这是一个用于对抗的 Apple，上面贴着写有 iPod 的贴纸。

### [1:02:31](https://www.youtube.com/watch?v=H9nvkyTsrnI&t=3751s) · b000074

所以，在此基础上，因为这个框架如此简单，已经出现了大量适配语言模型的开源实现。Mini GPD4 \[字幕疑误，可能指 MiniGPT-4\] 就是一个例子，非常简单。图像输入后，由预训练且冻结的 Q former 和 VIT 编码。这些是图像表示学习模型，会输出一些特征。这个特征经过一个线性层（linear layer），基本上只是改变维度，从图像特征的 embedding 维度转换到语言模型的 token 维度，就是一个线性变换。然后语言模型是 Vikuna \[字幕疑误，可能指 Vicuna\]，这是一个冻结的模型。嗯，是的，是开源的 llama 适配语言模型之一。因此，这里面唯一需要训练的，就是这个橙色的线性变换，对吧？要使它成功，有两种方式，或者说，两个训练阶段。第一阶段是 alignment。所以我给它一批

### [1:03:26](https://www.youtube.com/watch?v=H9nvkyTsrnI&t=3806s) · b000075

图像，并给它相应的描述。我会说，这是一个看起来像火烈鸟的紫色小图标。这是一个看起来像另一种图标的泰迪熊。因此，我只是给它一批图像和描述，让这个线性层基本上学会从视觉特征到描述图像的 token embeddings 的映射。所以，这是使用配对图像文本数据进行 alignment。你可以把它看作预训练，这样第二阶段就是 fine-tuning 或 instruction tuning，对吧？Instruction tuning 基本上让模型对下游任务有用，因为模型在预训练时见过的一切都只是给图像生成描述。识别这是一个火烈鸟图标，识别这是其他东西。它只能为图像生成描述。但有时你希望这些模型真正做些有用的事情。例如，假设你

### [1:04:23](https://www.youtube.com/watch?v=H9nvkyTsrnI&t=3863s) · b000076

知道它是一个助手，你可能想问它一个问题：“你觉得这个标志设计怎么样？”假设你是一名平面设计师，希望模型说，这个标志简单、极简，设计得很好，诸如此类。所以这些才是你希望模型完成的指令，对吧？因此，在第二阶段 instruction tuning 中，你要做的是给模型提供图像、希望模型完成的示例指令，以及人类专家对这些指令给出的完成结果（completions），对吧？你可能会请平面设计师实际帮你标注其中一些。然后你提供图像、提供指令，让模型预测这个结果。所以，第一阶段可以看作只是对齐图像和文本的预训练。第二阶段可以看作针对人们实际可能用模型完成的指令和任务进行适配。

### [1:05:20](https://www.youtube.com/watch?v=H9nvkyTsrnI&t=3920s) · b000077

有什么问题吗？

### [1:05:26](https://www.youtube.com/watch?v=H9nvkyTsrnI&t=3926s) · b000078

而且这确实有效，效果好得令人惊讶。看起来，只需要一个线性层，就能在非常不同的视觉预训练表示与某种能被语言模型作为输入理解的表示之间建立映射。再看一些例子。Llama adapter 是人们开发的一个大规模开源框架。我基本上把各种不同模态适配进 llama 开源模型。因此，他们适配了点云（point clouds）。你可以说，根据这个 3D point cloud 生成图像。这些 3D point clouds 输入后，你为 3D point clouds 定义一个编码器，对吧？得到某个特征，再将其适配为 llama 的输入。显然，他们在输出端也做了一些事情，所以它不只是生成文本，也可以生成图像。我们稍后会讲。所以你可以适配 3D point

### [1:06:23](https://www.youtube.com/watch?v=H9nvkyTsrnI&t=3983s) · b000079

clouds。在这个例子中，你也可以适配不同语言。可以添加一些 adapter tokens，模型就能够开始理解不同语言。

### [1:06:37](https://www.youtube.com/watch?v=H9nvkyTsrnI&t=3997s) · b000080

好，所以还是让我区分一下这些模型的预训练阶段与 instruction quing \[字幕疑误，可能指 instruction tuning\] 阶段。预训练阶段通常涉及大量图像描述对，对吧？这是最容易获得的大规模数据。多年来，越来越大的图像描述数据集不断发布，目前最大的一个是 data comp \[字幕疑误，可能指 DataComp\]，有 12 billion 对图像和描述。这基本上让你能够学习这些 adapters，接收图像，而模型被训练来只是给它生成描述、描述它。你可以把它看作 alignment 问题。第二阶段，instruction tuning 或 fine-tuning，对吧？在这个场景中，你确实希望模型执行有用的任务，因为我们不希望这些视觉语言模型总是只生成描述。你可能要求它们看着

### [1:07:34](https://www.youtube.com/watch?v=H9nvkyTsrnI&t=4054s) · b000081

某张图像来解数学题，能够诊断某些 X 光片，根据 X 光片诊断患者病情。因此，人们整理了一批这类指令数据集（instruction data sets），其中包含图像、某个任务，以及某个完成结果，即正确答案，也许还包括对为什么这是该任务正确答案的解释。这些通常用于第二阶段训练。

### [1:08:02](https://www.youtube.com/watch?v=H9nvkyTsrnI&t=4082s) · b000082

好。我们只剩五分钟了。所以，第三阶段需要更多时间，我就不进入第三阶段了，在这里结束讲座，看看大家对今天讲的内容有什么问题。总结一下到目前为止的内容，我们回顾了 fusion，回顾了 alignment，然后开始讨论这些大型多模态模型。在第一步中，你有所有这些不同的数据模态，往往把它们当作序列，对吧？这是一种非常自然的数据形式，尤其是因为我们经常随着时间与这些模型交互。一旦有了序列，这些多模态 transformer 就是对齐序列中元素、并利用 alignment 学习更好表示的好方法。这扩展了我们在 alignment 中讨论的内容：alignment 并不是最终目标，而是某个中间步骤，

### [1:08:59](https://www.youtube.com/watch?v=H9nvkyTsrnI&t=4139s) · b000083

通过了解元素彼此如何对齐，来学习更好的表示。然后，我们讨论了第二部分：有了这些表示后，如何把它们注入语言模型，对吧？我们看到了这个相当通用的框架，主要是保持语言模型冻结。它已经非常好了，不想过多更新它。你也没有资源去更新它。无论如何，也可以让这些表示保持冻结，只学习这个线性映射，也就是我们所说的 adapter，将这些表示映射到语言模型输入空间。然后，基本上可以分两个阶段训练它，对吧？这是一个到语言模型输入空间的线性映射。先使用图像和描述进行预训练，然后开始使用图像、指令任务，以及这些指令的完成结果进行 fine-tuning。

### [1:09:54](https://www.youtube.com/watch?v=H9nvkyTsrnI&t=4194s) · b000084

然后，等大家回来时，我们会讨论第三部分，也就是把多模态输入到文本输出，扩展成同时具有多模态输出。这样就有了真正交互式的多模态输入输出系统。好了。嗯，好，如果没有其他问题，大家可以走了。如果大家对作业或项目有任何问题，我会留下来答疑。谢谢大家。
