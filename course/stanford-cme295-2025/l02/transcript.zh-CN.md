# Stanford CME295 Transformers &amp; LLMs \| Autumn 2025 \| Lecture 2 - Transformer-Based Models &amp; Tricks

_中文讲稿_

- Channel: Stanford Online
- Source: [YouTube](https://www.youtube.com/watch?v=yT84Y5zCnaA)
- Duration: 1:47:19
- Caption source: manual
- Status: complete
- Chinese translation: 217/217
- Translation provider: codex
- Generated: 2026-09-29T15:39:24+00:00

## 讲稿

### [00:05](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=5s) · b000001

好。大家好。欢迎来到 CME 295 第 2 讲。开始之前，我想先提醒大家两件安排上的事情。第一件是，我和 Shervine 回看了第 1 讲的录像。我们实在没法忽视音频效果不太理想的问题。所以这次课我们会换一套设备配置。

### [00:35](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=35s) · b000002

不过这样有一个问题，就是我的声音不会通过扩音设备传到教室各处。所以我想问一下。大家都能听清楚我说话吗，包括后面的同学？好的，很好。太好了。这是第 1 点。第 2 点是关于期末考试。目前期末考试暂定的日期是星期三，我记得是 12 月 10 日。不过先提醒大家，我们正在看看有没有办法把它移到那一周早一些的时候。

### [01:06](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=66s) · b000003

所以等确定下来，我们会……但目前这件事仍然待定（TBD）。不过我们一定会通知大家。好。先把这些放到一边，我们进入今天的主题。不过在这之前，和往常一样，我们先快速回顾一下前面几期讲过的内容。如果大家还记得，第 1 讲主要介绍了自注意力（self-attention）的概念。

### [01:38](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=98s) · b000004

如果大家还记得，self-attention 就是每个词元（token）都通过注意力（attention）机制关注序列中所有其他 token。我们用到了查询（query）、键（key）和值（value）这些记号。这里的想法是，query 通过与 key 比较，来询问哪些其他 token 与自己最相似。

### [02:09](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=129s) · b000005

然后完成这一步以后，基本上我们就会取对应的 value。我们看到，self-attention 机制可以用这个公式表示，也就是 softmax(query × key 的转置 / √dk) × v。我希望大家对这个公式已经比较熟悉了。要知道，这个公式经过了高度优化。这些都是大型矩阵乘法，而硬件非常擅长做这些运算，针对这些运算的优化也非常充分。

### [02:48](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=168s) · b000006

说这些是为了说明，我们还介绍了 transformer 的架构，大家可以在右边看到。如果大家还记得，transformer 由两个主要部分组成：左边的编码器（encoder）和右边的解码器（decoder）。transformer 最初是在机器翻译（machine translation）的背景下提出的。所以你可以把左边理解为处理源语言的输入文本，比如英语。

### [03:25](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=205s) · b000007

右边则负责解码出目标语言的译文，比如法语。而这个多头注意力（multi-head attention）层就是执行 self-attention 机制的地方。我记得当时有很多问题是关于——它叫 multi-head attention 层，所以里面有多个头（head）。这些 head 对应什么呢？

### [03:55](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=235s) · b000008

在 transformer 论文，也就是《Attention is All You Need》这篇论文里，有这样一幅图，它实际上表示的就是这些 head。你可以把每个 head 看成模型学习一种投影方式的机会，用这种方式把输入投影成 query、key 或 value。再说清楚一点，比如对于 query 和 key，这就相当于每一个 head。

### [04:29](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=269s) · b000009

所以这些小方框的数量基本上就是 head 的数量。为了更直观地理解这是什么意思，我还想展示一下论文里展示的内容，也就是一种解释各个 head 在做什么的方式。我们有一个叫注意力图（attention map）的概念，它基本上试图表示每个 query 的值，点积 query 的值。

### [05:10](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=310s) · b000010

在这个例子中，我们关心的是，哪个其他 token 与 token its 最相似。所以我们要查看这些量：代表 its 的 query，与所有其他 key 做点积（dot product）。然后看看哪些 key 会让 query 乘以 key 的点积取得较高的值。

### [05:47](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=347s) · b000011

这样做之后，你看到的，或者说论文里观察到的，就是 application 和 law 这两个词被突出显示，因为它们具有较高的注意力权重（attention weight）。这里的 attention weight 指的是 its 的 query 与这些 token 各自的 key 的点积。我想也有一种解释这些结果的方式。这里你可以看到，被突出显示的 token 是 law 和 application，这基本上是合理的，因为 token its 指的是 law。

### [06:28](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=388s) · b000012

所以，模型基本上需要学会如何把这些词与前面出现的内容联系起来。而 its 也指向 application，这也是解释为什么会出现这种情况的另一种方式。这里作者选择展示这些数值在不同 head 下的情况。例如，左边这些是 head 的强度，比如说第一个 head 的强度。

### [07:00](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=420s) · b000013

然后第二个 head 显示，law 的强度非常高。所以简单来说，我想这些 head 可能会学到不同的方式，来判断哪些词比较重要。嗯。

### [07:30](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=450s) · b000014

问得很好。问题是，我们进行所有这些计算时，它们是否会经过不同的多层感知机（MLPs）。答案是，我们会为它们分别设置不同的投影矩阵（projection matrices）。

### [07:48](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=468s) · b000015

之前我们有一个详细例子，实际讲过这一过程，每个 head 都会有自己的投影。这些计算会并行进行。所以每个 head 都会在这里得到一个结果，然后将这些结果拼接（concatenate）起来，再通过输出矩阵进行一次投影。是的，简单来说，它的并行程度很高。

### [08:20](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=500s) · b000016

基本上就是一些投影。这里有一些矩阵乘法和 softmax。这样讲清楚了吗？好。关于这个还有其他问题吗？

### [08:38](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=518s) · b000017

好。我想这只是用来说明一下我们在第 1 讲中的讨论。当时有一些关于这些 attention head 以及它们作用的问题。我想，查看 attention map 是理解它们含义的一种方式。好。说到这里，我强烈建议大家读一下 transformers 论文，也就是《Attention is All You Need》。

### [09:09](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=549s) · b000018

这篇论文的信息密度非常高，只有几页。但我希望借助第 1 讲学到的内容，大家能够消化其中的内容，并理解它。好。接下来我们正式开始今天要讨论的核心内容。令人有些惊讶的是，这个在 2017 年提出的 transformer 架构，多年来一直保持着重要地位。

### [09:47](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=587s) · b000019

其中有几个组件发生了一些小变化。我们会看看具体是哪些。所以确实有一些细微的变体。不过总体而言，我们将会看到，今天的模型或多或少都基于最初的 transformer 架构。我们打算把这节课分成两部分。第一部分由我来讲，内容是 transformer 中哪些部分比较重要，以及这些部分发生了哪些变化。

### [10:20](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=620s) · b000020

第二部分，Shervine 会讲一下，我想是当今模型的命名体系，以及它们与原始 transformer 的关系。好。我们先从这个架构中的第一个重要概念开始，也就是位置嵌入（position embedding）。如果大家还记得，这里我们让各个 token 以直接的方式与所有其他 token 交互。

### [10:54](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=654s) · b000021

也就是说，它们之间有直接连接。但与循环神经网络（RNNs）之类的结构不同，RNNs 存在顺序依赖，每次处理一个 token，而在这里，基本上就失去了一个 token 先于另一个 token 被处理的概念。因此你会丢失这种位置信息。所以，我们需要以某种方式量化各个位置上的 token，并尝试在 transformer 处理输入时注入这些信息。

### [11:40](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=700s) · b000022

那要怎么做呢？原始 transformer 论文的作者选择设置专门的嵌入（embedding）。我说专门的，意思就是每个位置都有一个 embedding。位置 1 有一个 embedding，位置 2 有一个 embedding，以此类推。他们选择把这个 embedding 加到输入 token 的 embedding 上。

### [12:14](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=734s) · b000023

例如，如果我说 a cute teddy bear is reading（一只可爱的泰迪熊正在阅读），这是位置 1，表示 token a，再加上表示第一个位置的 embedding。嗯。

### [12:39](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=759s) · b000024

这是个很好的问题。问题是，position embedding 是学习得到的，还是静态的？两种都有，也就是说，作者两种都试过。我们马上会看第二种是什么。不过这里先假设它们是学习得到的。这是什么意思呢？意思就是你基本上需要为每个位置学习 embedding。而这种方法的问题在于，你会非常依赖训练集中的内容。

### [13:16](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=796s) · b000025

例如，像这里，如果你有一些文本，其中某种内容总是出现在位置 2，那么学到的 embedding 就会把这种偏差也学进去。这是它的一个局限。第二个局限是，你只能学习到训练集中出现的最大位置。假设你用长度最多为，比如说 512 的序列来训练 transformer。

### [13:51](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=831s) · b000026

那你只能学习到这个位置为止的 position embedding。对吧？

### [14:06](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=846s) · b000027

是的。问题是，我想，如何对它进行参数化？我想做法是，先为可学习的 position embedding 留出占位，比如位置 1 到 512。然后在训练时，让这些权重通过常规的梯度下降（gradient descent）之类的方法学习。所以这就是第一种方法。但正如我刚才提到的，它有局限，因为你只能学习训练集中最大位置以内的位置的 embedding。

### [14:48](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=888s) · b000028

例如，在推理（inference）时，如果出现了一个超出训练集所包含位置的位置，那么你没有学过它。所以需要想办法推断它的值。这就是第二个局限。不过从优点来看，我想你就是让模型去学习。我们也已经看到，在从数据中学习这件事上，gradient descent 能发挥很大的作用。

### [15:19](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=919s) · b000029

是的。基于这些原因，作者表示，这些方法表现不错，另一种方法也表现不错。第二种方法有所不同，它为 position embedding 的每个维度设定一个人为指定的公式。我们现在就来看。第一种方法是，每个位置有一个 embedding，然后直接学习它。

### [15:56](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=956s) · b000030

第二种方法是，每个位置也有一个 embedding，但不去学习它，而是使用预先确定的内容。我们会看到，作者选择的是使用正弦（sine）和余弦（cosine）的表达式。你可能觉得很奇怪，他们为什么这么选？不过我们会看到这样做为什么合理。这里的思路是，对于某个给定位置，比如 m，设置一个大小为 d model 的向量。

### [16:36](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=996s) · b000031

所以 d 需要与 token embedding 的维度一致，因为你要把它们相加。接下来，对于每个索引，都根据这些公式计算相应的值。那么这些公式是什么呢？基本上就是某个量乘以 m 的 sine。我们会看看那个量是什么意思。第二个则是某个量乘以 m 的 cosine。

### [17:11](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=1031s) · b000032

有谁还记得三角函数公式？

### [17:17](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=1037s) · b000033

好。大家都记得。那么在深入之前，我们先简化一下记号。假设你刚才看到的那个很大的量实际上就是类似 omega 的东西。假设它是作为 i 的函数的 omega，再乘以 m。把 omega i 记作这个量，也就是 10,000 的负 2i 除以 d model 次方。假设你按这种方式构造 embedding。

### [17:50](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=1070s) · b000034

接下来，我想让大家思考一下，这为什么合理。因为仔细想想，你希望位置的表示方式能反映这样一个事实：距离较近的词，比距离较远的词更可能相关。所以，如果两个词只相隔一个位置，而另外两个词相隔 10,000 个位置，你希望相隔一个位置的那一对比另一对更相似。

### [18:34](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=1114s) · b000035

我们来看看这个公式是否合理。假设有两个 position embedding，一个位于位置 m，另一个位于位置 n。再假设你根据这个预先确定的公式计算所有值。如果你还记得三角函数公式，cosine(a − b) 等于 cosine(a) cosine(b) 加上 sine(a) sine(b)。

### [19:12](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=1152s) · b000036

对吧？那么，如果你把 cosine(omega i × (m − n)) 展开，就会得到这个式子。它就是我刚才提到的恒等式。而这个量，恰好就是对这两个 position embedding 做点积时出现的一项。

### [19:43](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=1183s) · b000037

对吧？因为在这里，对位置 m 和位置 n 做点积时，你会取第一个位置，把它们相乘，再加上第二个位置相乘的结果，以此类推。然后到这里，就是这个量的 sign \[字幕疑误，可能指 sine\] 乘以这个量的 sine，再加上这个量的 cosine 乘以这个量的 cosine，也就是这个量。所以最终你会发现，对这些 embedding 做点积，得到的是一组 cosine 的和，它们都是 m 与 n 之间相对距离的函数。

### [20:32](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=1232s) · b000038

是的。

### [20:42](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=1242s) · b000039

顺便问一下，你说的“一对”是什么意思？

### [21:01](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=1261s) · b000040

完全正确，是的。问题是，它们越近，就越相似。这就是这种 embedding 表达方式想要近似或模拟的直觉。这样一来，你得到的点积就是 m 和 n 的函数，准确地说，是它们之间相对距离的函数。再提醒一下，我为什么关心点积？

### [21:31](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=1291s) · b000041

因为如果你还记得，在 embedding 的世界里，当我们试图量化两个 embedding 的相似程度时，通常会用到它们的点积。一般会用余弦相似度（cosine similarity）。cosine similarity 就是点积除以各个 embedding 的范数（norm）。所以基本上还是点积，对吧？这就是我们关心点积的原因。在这里我们看到，很好，它是两者相对距离的函数。

### [22:06](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=1326s) · b000042

具体来说，如果你还记得三角函数课，cosine(0) 等于 1。而这个数越大，它的 cosine 值就越小。当然，它是周期性的，所以我说的并不一定成立。超过 pi 之后，变化方向就反过来了。

### [22:38](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=1358s) · b000043

不过，我想表达的是，当 m 等于 n 时，基本上得到的是一组 cosine(0) 的和。此时这个量达到最大值。所以当 m 等于 n 时，这个量最大。这基本上意味着，如果你看这个位置本身，它与自身最相似。这符合我们的直觉。

### [23:10](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=1390s) · b000044

现在把 embedding 的数值画出来，就会得到这幅图。这里图中的 y 轴，基本上表示每个位置的所有 embedding，比如说 50 个位置。而 x 轴基本上表示某个向量在多个维度上的取值。例如，如果你取第一行，看到的就是第一个位置，或者编号为 0 的位置，取决于你如何为向量编索引。

### [23:48](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=1428s) · b000045

你看到的是位置 0 的 embedding 的所有数值。你会发现，在较低的维度上，这个值非常频繁地上下变化，也就是频率更高。而当维度较高时，这个值要过很久才会上下变化，也就是频率更低。

### [24:22](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=1462s) · b000046

这就与我提到的 omega i 有关，就是这个 omega i。当 i 较小时，也就是维度较低时，omega i 非常大。当 i 较大时，它就非常小。所以它基本上决定了 cosine 和 sine 变化的快慢。

### [24:52](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=1492s) · b000047

好。这就是原作者尝试的方法。他们表示，也就是他们观察到，使用这些方法与使用学习得到的 embedding 相比，结果相当。不过这里有一个很大的优势，因为它能够扩展到任意序列长度，而不只是训练时见过的序列长度。这也是这种方法可能更值得采用的原因之一。

### [25:26](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=1526s) · b000048

是的，这就是背后的直觉，也是作者的选择。现在快进到 2025 年。我想你可能会问，我们还在用这个吗？答案是，某种程度上是的。我们仍然沿用这个想法：希望远处的——我是说，token 比近处的 token 更不相似。不过我们不再像他们那样注入 embedding。接下来会解释为什么。

### [25:56](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=1556s) · b000049

因为如果你还记得，我们关心的是，在 self-attention 计算中确定 token 之间的相似程度。self-attention 计算在哪里发生？在 attention 层。但这里我刚才说了什么？我说，计算这些 embedding，然后把它们加在这里。可实际上，我们希望在 attention 层中体现这种相似性。

### [26:35](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=1595s) · b000050

你有问题吗？嗯。

### [26:40](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=1600s) · b000051

在这第一种方法里，是的。问题是，它是否加到了输入特征上？是的。

### [26:47](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=1607s) · b000052

对，直接相加。对，对。但问题是，我们主要希望这些直觉在 multi-head attention 层里成立。所以这也是人们尝试不同变体的原因之一，尤其是让这些 position embedding 直接作用于 attention 层，而不是输入。

### [27:22](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=1642s) · b000053

因为如果你在输入端做这件事——就在这里，可以，没问题——它大致上会进入这个 attention 层，但这个过程有点间接。所以我们希望直接调整 attention 公式，使它反映这样一个想法：我们希望近处的 token 比远处的 token 更相似。

### [27:52](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=1672s) · b000054

具体做法是，如果你还记得，self-attention 层基本上就是 softmax(qk 的转置 / √d) × v。所以我们想在这个 softmax 里面加一点东西，因为这里正是量化一个 token 与另一个 token 相似程度的地方。你想加一点东西，来反映这样一个事实：相对于其他 token，有些 token 应该与这个 token 更相似。

### [28:32](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=1712s) · b000055

有几种方法尝试了这方面的变体。对于了解 T5 论文的同学，我们稍后会讲到它，他们尝试了相对位置偏置（relative position bias），通过学习上面公式中的偏置项（bias term）来实现。

### [29:04](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=1744s) · b000056

他们的做法是，假设位置 m 和 n 之间有一个给定的距离。他们的想法是，那就学习它。基本上，把所有 m − n 分到一些桶里，也就是分桶（bucketize）。然后让模型学习这些量，再把它们注入 softmax。

### [29:34](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=1774s) · b000057

嗯。

### [29:43](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=1783s) · b000058

问题是，相对于最终的概率，把 bias 放在这里是否会造成问题？因为概率之和必须等于 1。其实，你可以在 softmax 里面做任何事情，因为 softmax 最终都会将它归一化。

### [29:59](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=1799s) · b000059

所以你可以把 bias 理解为：对于距离较远的内容，它可能比距离较近的内容更加负。T5 说，那就学习这些 bias。另一个思路来自这篇《Train Short, Test Long》论文，它提出了一种叫 ALiBi 的方法。我记得 ALiBi 是带线性偏置的注意力（Attention with linear bias）的缩写。

### [30:30](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=1830s) · b000060

他们的做法是，与其学习这些 bias，不如直接使用一个确定性的公式，把它写成两个位置相对差值的函数。他们就是这么说的。他们也有一些结果。所有这些论文总是相互比较，看看哪一种性能更好。

### [31:01](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=1861s) · b000061

但实际情况是，在当今模型中，大多数模型用的是另一种 position embedding 方法。我们现在就来看。这种方法依靠将 query 和 key 向量旋转某个角度。你可以这样理解：有一个 query，有一个 key，假设它们处于二维（2D）空间中。

### [31:37](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=1897s) · b000062

接下来，把 query 旋转某个角度，这个角度是它所在位置的函数。再把 key 向量旋转某个角度，这个角度是它所在位置 n 的函数。顺便问一下，这要怎么做呢？我本来不该把这个展示出来的。假设你有一个向量，想要旋转这个向量，因为我已经把答案放在幻灯片上了。

### [32:09](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=1929s) · b000063

不过，如果只想从直觉角度讨论这件事，你会怎么做呢？

### [32:21](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=1941s) · b000064

在座有谁做过，我不知道，空间中的旋转？嗯。

### [32:33](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=1953s) · b000065

对，没错。矩阵乘法。你会用到一个叫旋转矩阵（rotation matrix）的量。rotation matrix 的表达式如下。在 2D 平面里，它基本上是一个 2 × 2 矩阵，元素依次是这个角度的 cosine、负 sine、sine 和 cosine。我看一下时间。证明它确实有效其实很简单，但我们可能会没时间。

### [33:04](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=1984s) · b000066

你们想让我快速展示一下，它确实能旋转向量吗？好。提醒一下，这里我们想证明的是，可以用矩阵乘法旋转 2D 空间中的一个向量。假设有下面这个向量。它可以用两个维度来量化，比如 x 和 y。

### [33:42](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=2022s) · b000067

你可以用这个来表示 2D 空间中的向量，对吧？不过，如果你把向量的范数记作 R，把它与 x 轴的夹角记作 phi，也可以把 v 写成 R 乘以由 cosine(phi) 和 sine(phi) 组成的向量。

### [34:21](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=2061s) · b000068

对吧？所以，如果把 rotation matrix 与这个 phi 相乘 \[原文如此，此处可能指向量 v\]，得到的就是一些 cosine、负 sine、sine 和 cosine 之间的乘法。我把这道练习留给大家。不过可以证明，旋转矩阵乘以这个 v，可以表示为 R 乘以由 cosine(theta + phi) 和 sine(theta + phi) 组成的向量。

### [35:09](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=2109s) · b000069

这就是一个简短的证明。我把 rotation matrix 与 v 的乘法留给你们做。你会得到这些三角恒等式，它们会导出这个公式。这基本上证明了，把这个矩阵与这个向量相乘，就相当于把向量旋转这个角度。嗯。问题是，为什么要这么做？

### [35:40](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=2140s) · b000070

这是个很好的问题。下一页幻灯片就会讲。所以这里只是一个小引子。回到这个方法，我们想做的是量化 token 之间的相似度，并让近处的 token 比远处的 token 更相似。之前那些方法的问题是——第一种方法，也就是学习得到的 embedding，总会存在过拟合（overfitting）问题。

### [36:18](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=2178s) · b000071

因为学习这些 bias 时，总会依赖你使用的训练集。也许你的数据集里，相邻 token 确实相似，但这种相似方式与推理时看到的情况不同。而 ALiBi 方法虽然没有可学习的部分，但它的限制很强，因为说到底，它的公式非常简单，就是 n 和 m 之间的相对差值。

### [36:49](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=2209s) · b000072

所以，人们尝试了不同方式，想构造出某种东西，也就是一个 embedding，来体现我们希望较远位置比较近位置更不相似这一点。在这个方法中，我们又回到作者所提出的 sine 和 cosine 的世界，从 cosine 和 sine 函数的角度来思考相似性。

### [37:24](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=2244s) · b000073

这就是一个小引子。他们的方法叫 RoPE。不知道你们是否听说过。它代表旋转位置嵌入（Rotary Position Embeddings）。接下来我们会看到这个方法——我们为什么关心它呢？它有两个很好的特点。第一个是，如果旋转 query 和 key，最终得到的量会是两者相对距离的函数。

### [37:59](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=2279s) · b000074

这会非常好，也正是我把这个写在黑板上的原因。顺便说一下，不知道你们能不能看清，但我们没有时间深入数学细节。如果你想回家把这些表达式写出来，这就是基础。

### [38:19](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=2299s) · b000075

具体来说，如果你还记得 attention 公式，里面有 query 乘以 key 的转置。如果把 query 旋转角度 m，把 key 旋转角度 n，最终得到的公式会包含一个 rotation matrix，其角度是 theta 和，我想是 n − m。

### [38:53](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=2333s) · b000076

这很好，因为它是这两个位置相对距离的函数。

### [39:01](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=2341s) · b000077

好，那我为什么这么详细地讲这个？因为现在大多数模型都使用 RoPE，所以它很重要。另外一点是，要从直觉上理解它为什么有效，可能有点难。但希望我最开始关于 sine 和 cosine 的解释能帮助大家建立这种直觉。说到这里，由 query 和 key 给出的 attention weight 的上界，会呈现出一种长期衰减。

### [39:48](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=2388s) · b000078

意思是，当 n − m 很大时，我们确实会看到这个上界越来越小。当然，你也能看到这些小幅振荡，它也不完美。不过，关于上界长期衰减这件事，我们确实有一些数学结果。

### [40:18](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=2418s) · b000079

好。关于这个有什么问题吗？嗯，嗯。

### [40:38](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=2438s) · b000080

完全正确，是的。问题是，相对距离是不是体现在 rotation matrix 里——是的，是的。

### [40:49](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=2449s) · b000081

哦，是的。

### [40:53](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=2453s) · b000082

这是个很好的问题。问题是，theta 是什么？theta 实际上是固定的。还记得我在这里讲过的 omega 吗？这里。它基本上是 i 和 d 的某个函数。我刚才讲得确实比较快。我展示的是 2D 空间中的情况，但这里我们处于 d 维空间，而且 d 大于 2。所以这一点我很快就带过去了。

### [41:25](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=2485s) · b000083

扩展这个方法的方式，就是把这些 2D 空间按块组织起来。theta 通常是某个固定设定的函数，但也是 i 的函数，这里的 i 是维度，基本上在 1 到 d / 2 之间。它是 i 的函数，同时也是 d 的函数。你会看到，这个 theta 大致等于 omega i，就是这一个，差不多，差不多。

### [42:04](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=2524s) · b000084

什么？

### [42:07](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=2527s) · b000085

哦，问题是，这样它就和潜在维度（latent dimension）的维数相同了？这里涉及矩阵乘法，所以维度必须匹配。所以我想，你的答案——对。

### [42:30](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=2550s) · b000086

这样讲清楚了吗？

### [42:34](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=2554s) · b000087

那我就当作是清楚了。我在这上面花了不少时间，因为我觉得它确实很重要。很多模型都在用它。而且背后的直觉确实不是特别明显。希望这些讲解有所帮助。以上就是 position embedding。嗯。哦，是的。对，问题是，这条曲线怎么得到？我认为这实际上是一条通过数学推导得到的曲线。

### [43:09](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=2589s) · b000088

它有点复杂，我们就不把公式写出来了。如果你感兴趣，在这篇 RoFormer 论文里有一个附录，他们从数学上证明了它被某个量上界约束。这里展示的就是那个量。对，问得很好。

### [43:29](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=2609s) · b000089

好。position embedding 是 transformer 中发生了一些变化的部分。我们看到了它如何变化，以及为什么变化。现在来看 transformer 中另一个也发生了一些变化的组件，也就是层归一化（layer normalization）。如果大家还记得，transformer 架构还是由 encoder、decoder，以及它们内部的组件组成的。

### [44:02](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=2642s) · b000090

这里有一些方框写着 add 和 norm。它们是什么意思？基本上，我们取输入，以及这个子层（sublayer）的输出，把它们加起来，然后归一化。这是作者使用的一个小技巧。实践表明，它能够改善收敛（convergence），让收敛更快。

### [44:40](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=2680s) · b000091

思路如下：如果有一个向量，它的分量有时可能特别大，有时可能特别小。这里的想法是，把向量的分量归一化到某个范围，也就是某个归一化的范围。做法是，取这个向量，减去计算得到的均值，基本上就是它各分量的总和，然后基本上用它的标准差进行归一化。

### [45:20](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=2720s) · b000092

接下来，你要学习两个量：一个是 gamma，用作重新缩放的因子；另一个是 beta，也是需要学习的项。让模型学习这两个量。正如我所说，在实践中，这样做有助于训练稳定性，并缩短收敛时间。

### [45:53](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=2753s) · b000093

这是原始 transformer 论文使用的一种技术。我想指出，自那以后发生了一些变化。我们从对输入与子层输出之和进行归一化，变成了把输入与“归一化后的输入经过子层的结果”相加。换句话说，我们改变了归一化所在的位置。

### [46:28](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=2788s) · b000094

在 transformer 论文中，使用的是现在称为后置归一化（post-norm）的版本。如今，我们使用前置归一化（pre-norm）版本，也就是把 LayerNorm 放在向量进入子层之前。这里的子层可以是 attention 层，也可以是前馈网络（FFN）。

### [46:56](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=2816s) · b000095

不仅如此，还有另一个变化。如今人们不使用 LayerNorm，而使用另一种叫 RMSNorm 的方法——RMS，也就是均方根（Root Mean Square），Normalization，也就是归一化。它基本上是刚才那种方法的变体。不再计算这个，而是用 x 各分量的均方根对 x 进行归一化，并学习 gamma，只学习 gamma。

### [47:34](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=2854s) · b000096

为什么这么做？基本上，他们证明了两者的收敛性质相当。但这里需要学习的参数更少，所以基本上会更快。嗯。

### [48:12](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=2892s) · b000097

好问题。问题是，归一化背后的直觉是什么？直觉是，如果看一下模型，它有好几层。在某些层里，你的向量——更准确地说是激活值（activation）——你知道，这个从这里传到这里的向量基本上就叫 activation。有时 activation 在一部分分量上出现极端值，有时在另一部分。如果这些 activation 变化太大，模型通常就难以学习各层中的权重。

### [48:54](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=2934s) · b000098

所以思路是，把 activation 各分量的值带到某个范围内，使它们不会在某个方向偏得太远。如果你感兴趣，有一个关键词叫内部协变量偏移（internal covariate shift），基本上就是我刚才描述的这种现象的名称。是的，这就是直觉。

### [49:24](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=2964s) · b000099

嗯。

### [49:27](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=2967s) · b000100

哦，很好，非常好的问题。问题是，这与批归一化（batch normalization）有什么区别？batch normalization 是沿另一个维度归一化，也就是 batch 的维度。假设你有一组向量。你会针对每个分量，参照其他向量在相同维度上的所有分量进行归一化。

### [49:57](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=2997s) · b000101

所以你可以把它看成另一种归一化方式。不过，对于这些基于 transformer 的模型，人们通常使用 LayerNorm，可能是因为经验上它效果更好。同时也是因为 BatchNorm 还依赖 batch，这可能导致训练和推理之间存在差异。基本上就是这个原因。

### [50:30](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=3030s) · b000102

好，很好。我们已经看了 position embedding，也看了 layer normalization。现在来看 transformer 的第三个重要组件，也就是 attention。尤其是，有一件事我之前没有特别强调：做 self-attention 时，基本上是在让每个 token 与所有其他 token 交互。所以如果看一张展示所有交互的矩阵，这里有 n，也就是序列长度。

### [51:06](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=3066s) · b000103

对于这个序列长度，基本上有 O(n²) 的复杂度，这非常大，尤其当 n 变得更长时。所以，人们尝试用更容易处理的计算来近似这个 O(n²) 计算，同时不损失性能。2020 年发表了一篇论文《LongFormer》。它做的就是通过限制 attention 作用的窗口，尝试不同的 attention 版本。

### [51:42](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=3102s) · b000104

这里不再让每个 token 与所有 token 交互，而是让每个 token 只与它的邻域交互。嗯。

### [51:55](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=3115s) · b000105

哦，又是个很好的问题。问题是，是在计算完 attention 矩阵之后再做这件事吗？你是指 softmax，对吧，softmax？你提出了一个很好的点：如果已经对所有内容算了 softmax，为什么还要这么做？实际上，有很多实现采用了一些巧妙的——它叫分块（tiling）——一些巧妙的操作，避免执行你在 softmax 中看到的那个巨大的矩阵运算。

### [52:30](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=3150s) · b000106

再说一次，我想，就是对 qk 的转置除以 d 做 softmax。你不会把整个东西都算出来。基本上，你会采用一些巧妙的计算方式。

### [52:54](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=3174s) · b000107

是的，问题是，它是否可以类比卷积（convolutions）？我们马上就会讲到。它与视觉领域中的一些东西确实有相似之处。我们马上会看到。

### [53:11](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=3191s) · b000108

好。如今，像这样的局部注意力（local attention），人们会使用滑动窗口注意力（sliding window attention）这个术语。他们使用这个术语时，指的就是这种方式，基本上把 attention 限制在相邻 token 上。如今的做法是，有些层采用 local attention，另一些层采用全局注意力（global attention）。

### [53:44](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=3224s) · b000109

这些层会交错排列。根据模型的不同，人们通常会尝试不同的组合。没有一套固定的配方，但这是现在经常采用的做法。这里的窗口，我是说，为了便于说明，我画的窗口非常小。不过现在序列长度可能非常大，所以可以把这个窗口理解为几千的量级。

### [54:20](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=3260s) · b000110

再举一个例子。回到你提到的与卷积的比较。有一些架构，这里我用 mistral 举例，它每一层都使用 sliding window attention。不过仔细想想，这里的 token 可以关注到那里的 token，然后那里的 token 又可以关注到更远处的 token，以此类推。

### [54:53](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=3293s) · b000111

所以仔细想想，这类似于计算机视觉（computer vision）中的感受野（receptive field）概念。不知道你是否熟悉，或者是否来自 computer vision 领域。如果是，这里的意思就是，取一个 token，思考它实际上与哪些其他 token 发生过交互。这基本上也是人们有时会问的问题。

### [55:25](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=3325s) · b000112

做卷积时，人们会问，好，这个值实际上看到了哪些值？所以你也可以这样理解。好，第一种变体是，不做完整的 n × n attention，而有时采用 local attention。第二种变体与这些都是正交的，也就是不再为每个 head 设置一个投影矩阵，而是跨 head 共享投影矩阵。

### [56:10](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=3370s) · b000113

这里的想法是，假设有 h 个 head。你会为 query 设置一定数量的投影矩阵。然后，把 key 和 value 的投影矩阵分组，让多个 head 共享它们。

### [56:34](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=3394s) · b000114

现在你可能会问，为什么共享 key 和 value 的投影矩阵，却不共享 query 的？这是你正在想的问题吗？这里，我想，人们做这些事情就是为了试试看是否有效。直观上，你可以把 query 理解为，它基本上在询问某个东西是否与另一个东西相似。而你可以用不同的方式问自己这个问题。

### [57:06](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=3426s) · b000115

所以保留这种多样性可能有道理。不过，选择对 key 和 value 的投影矩阵进行分组，而不对 query 这么做的一个核心原因是，在解码时，你要在当前词与之前所有词之间计算 attention。换句话说，每次生成一个新词，都要让这个词关注之前所有的词。

### [57:43](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=3463s) · b000116

所以 key 和 value 会被反复用到。每次想要解码一些内容，都需要一遍又一遍地关注所有其他内容。我想下一讲会讲到一个叫键值缓存（KV cache）的东西，它基本上保存 key 和 value 的数值。而我们希望这个 cache 不要变得太大。

### [58:16](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=3496s) · b000117

所以，跨 head 共享投影矩阵，就可以节省一点空间、一点内存。这就是原因。大致能理解吗？

### [58:33](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=3513s) · b000118

好，很好。说到这里，关于具体共享多少投影矩阵，也有一些变体。有一个极端情况，就是全部 h 个 head 都共享同一组 v 和 k 的投影矩阵。这种方法叫多查询注意力（Multi-Query Attention，MQA）。

### [59:04](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=3544s) · b000119

还有一种介于两者之间的情况，共享 g 组投影矩阵，g 是分组数量，也就是 v 和 k 分别有 g 个投影矩阵。每组的大小，比如说，是 h / g。这种叫分组查询注意力（Group Query Attention，GQA）\[字幕疑误，可能指 Grouped Query Attention\]。然后还有你在 transformer 中已经很熟悉的情况，就是每个 head 都有自己的 query 投影、key 投影和 value 投影矩阵。

### [59:45](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=3585s) · b000120

这就是标准的 multi-head attention。

### [59:53](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=3593s) · b000121

好。那么我先停一下，看看我刚才讲的是否清楚。我马上就要交给 Shervine。不过在这之前，我想确认一下，我讨论的内容大家大致能理解。对。

### [1:00:21](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=3621s) · b000122

那么问题是，我们会把这个应用于自注意力（self-attention）和交叉注意力（cross-attention）吗？我不想提前剧透。所以我稍后会讲到一些内容。不过，我的 trans 在哪儿？\[字幕疑误，可能指 transformer\] 如果你看看 Transformer 架构，我们很快就会看到，我们最关心的是解码器（decoder）里的部分，因为如今的模型实际上舍弃了编码器（encoder）。我们还没有讲到这个，不过我先告诉大家。

### [1:00:52](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=3652s) · b000123

所以，这通常会用在 decoder 中的掩码自注意力（masked self-attention）上。不过这项技术可以应用于所有注意力层。但我想说的是，现代的大语言模型（LLMs）是仅解码器（decoder-only）模型，基本上只有 Transformer 的 decoder 部分。我们马上就会看到，也就是 masked self-attention。所以我就不多说了，因为 Shervine 会讲这部分。

### [1:01:25](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=3685s) · b000124

不过，对，这只是提前看一下我们接下来要讲的内容。好，对。

### [1:01:36](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=3696s) · b000125

对。

### [1:01:41](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=3701s) · b000126

好问题。那么问题是，你怎么知道应该用哪一种？我会说，选择始终由几个因素决定。一个是效果如何。第二个是，你有多在意延迟、成本之类的事情。所以，这确实取决于你的模型有多大，你想节省多少，比如计算量，以及你的输入长度是多少，比如输入长度比较短的情况。所以这里我们想做的，是避免为整个 O(n²) 的东西做所有这些事情。

### [1:02:15](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=3735s) · b000127

所以我想，这些因素都会起作用。因此我会说，答案并不直接。不过我会说，很多最近的模型倾向于共享投影矩阵（projection matrices）。所以通常来说，你会看到的是 GQA。但并非所有模型都是这样。

### [1:02:36](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=3756s) · b000128

好。时间快不够了。所以我请 Shervine 来讲第二部分。谢谢。好的，很好。谢谢你，Afshine。那么我们继续这节课，更深入地了解 Transformer 领域中的各种模型。接着，我们会深入研究一种对分类场景非常有用的特定架构。首先，我们回到上次一起看过的架构，也就是这种传统的 encoder/decoder 架构，其中两个组件都有。

### [1:03:19](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=3799s) · b000129

2017 年最初的 Transformer 论文采用的就是这个架构。不过后来，你也会看到更多在它的基础上构建的架构。这里我们要讲的是 T5 模型家族。T5 这篇论文的名字是多个 T 的缩写。第一个是 transfer，然后是 text-to-text、transformers。

### [1:03:49](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=3829s) · b000130

这就是 T5 这个名字的来源。然后它又衍生出了多个版本。T5 就相当于最初的基础版论文。接着有了 mT5。m 代表多语言（multilingual），它对训练数据以及所用词表做了更多工作。然后还有 ByT5，它是这类方法中的一种免分词器（tokenizer-free）方法，舍弃了分词这一步。

### [1:04:26](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=3866s) · b000131

取而代之的是，基本上直接在字节（byte）层面操作。所以 By 就像 byte。这样一来，词表大小就小得多。不是大约 O(30k)，而是 2 的 8 次方。一个字节是 8 位（bits）。然后你可以用字节表示每个字符。这就是他们的做法。

### [1:04:55](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=3895s) · b000132

好的，很好。关于 T5 家族，我还想提一点，它的目标函数（objective function）与最初的 Transformer 有一些不同。最初的 Transformer 在训练任务中做的是下一个词元预测（next token prediction）。但 T5 家族采用的是所谓的片段破坏（span corruption）任务。基本上，你会把句子作为 encoder 的输入。

### [1:05:29](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=3929s) · b000133

但你不会把所有内容都放进 encoder，而是会留下一些空白。这就是我们所说的 span corruption。span corruption 可以是缺失一个或多个词元（tokens）。如果要举个例子，比如，我的泰迪熊很可爱，而且正在阅读。那么你可以有「我的泰迪熊」，接着一个被破坏的片段，再接「正在阅读」。这就是一种可能的 encoder 输入。

### [1:06:03](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=3963s) · b000134

然后你最多可以有 n 个——我是说，n 是被破坏片段数量的参数。所以这里会有 n 个这样的 token。T5 家族把它们称为哨兵词元（sentinel tokens）。因此，如果你看到 sentinel tokens，它们代表的是一段被破坏的 tokens。它们出现在 encoder 这里。而 decoder 的工作就是依次找出这些片段。

### [1:06:33](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=3993s) · b000135

所以，你从一个表示第一个被破坏片段的 token 开始。然后开始解码过程，直到它预测出下一个 sentinel token，一直到 n 加 1，1 \[字幕疑误，末尾的 1 可能重复\]。两个相邻 sentinel tokens 之间解码出来的 tokens，就对应于恢复出的被破坏片段。所以这段插话基本上是在说明，相对于 next token prediction 目标函数的一个变化。

### [1:07:08](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=4028s) · b000136

对。

### [1:07:27](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=4047s) · b000137

对。那么问题是，能否详细解释一下解码过程？你关于重建所说的完全正确。sentinel tokens 表示一些缺失的文本。因此，你想解码出来的就是那些缺失文本。所以 decoder 的输出就是每个重建出来的片段。如果你想知道训练是如何进行的，会使用教师强制（teacher forcing）机制，把所有内容输入 decoder，然后尝试一次性重建全部内容。

### [1:08:00](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=4080s) · b000138

那么还有其他问题吗？

### [1:08:07](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=4087s) · b000139

很好。

### [1:08:10](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=4090s) · b000140

现在我们要讲另一类 Transformer，基本上你有这种 encoder/decoder 结构，但把 decoder 舍弃，只处理 encoder。你可能会跟我说，好吧，嘿，这样没法做生成。而我会回答你，对，这正是它的用意。

### [1:08:37](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=4117s) · b000141

它提供 encoder 表示，可以用于更偏向分类的任务。比如情感提取（sentiment extraction）、词元分类（token classification），这些过去使用特定语言模型完成的任务，都可以用 Transformer 的 encoder 部分来做。稍后，我们会进一步深入了解三个关键的仅编码器（encoder-only）模型。BERT，我会说它是这个领域的核心模型；还有另外两种架构，DistilBERT 和 RoBERTa，它们探索了不同的改进方向。

### [1:09:20](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=4160s) · b000142

所以看一看会很有帮助。好的，很好。还有最后一类。正如 Afshine 刚刚提到的，two days LLMs \[字幕疑误，可能指 today's LLMs，即如今的 LLMs\] 完全移除了 encoder 部分。没有 encoder，就不会有堆叠的 encoders 末端产生的编码器嵌入（encoder embeddings）可以输入 cross-attention。所以这个模块也完全消失了。

### [1:09:52](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=4192s) · b000143

因此，堆叠起来的每个 decoder 内部只有 masked self-attention 和一个前馈网络（FFN）。对，这基本上是后来流行起来的做法。因为如果看看这些模型各自的流行程度，早期流行的是这种类似 Transformer 的架构，当时的主要假设是，encoder 部分对于获得 decoder 的表示非常有用。

### [1:10:28](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=4228s) · b000144

但随着时间推移，人们意识到，计算预算最好只投入 decoder。随后，更多投入转向了我认为最容易扩展和泛化的任务——下一个词预测（next-word prediction）——相较之下，我刚刚提到的 T5 任务可能更需要专门设计。你需要破坏一些内容。

### [1:10:59](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=4259s) · b000145

所以它更复杂。而 next-word prediction 可以说是你能做的最简单的事情。事实证明，它的效果非常出色，而且与充当有帮助的聊天机器人的任务很契合，而这基本上就是 two days 的应用 \[字幕疑误，可能指 today's applications，即如今的应用\]。至于 decoder-only 架构，我今天不会讲。不过，它会成为接下来几节课的核心内容，届时我们会越来越多地讨论 LLMs。

### [1:11:35](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=4295s) · b000146

好的，太好了。现在我们可以按之前说的，深入了解 encoder-only 架构以及 BERT。首先，我们来看 BERT 是什么意思。BERT 是一个缩写，表示来自 Transformers 的双向编码器表示（Bidirectional Encoder Representations from Transformers）。我们会一起看看，这个缩写的各个部分分别对应什么。

### [1:12:08](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=4328s) · b000147

先从 encoder 部分开始，这最容易理解。正如我们所说，我们只是去掉了 decoder。因此，来自 Transformer 的这个 encoder，基本上就是字面意思。现在看另一部分，为什么我们会谈到双向性（bidirectionality）？这是因为，这篇论文的结果很出色：给定一个输入，我们能够得到输出表示，其中每个 token 都关注了所有内容。

### [1:12:51](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=4371s) · b000148

情况确实如此。因为我们只有 encoder，所以这个 self-attention 层确实会关注其他每一个 token。这与 masked self-attention 不同，我们说过，其中的掩码（mask）让注意力机制具有因果性（causal）。所以每个 token 可以关注自身以及它之前的 tokens。顺便说一下，这也是作者在论文中大量讨论的内容，他们说 GPT 出来了，但 GPT 并不是真正双向的。

### [1:13:30](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=4410s) · b000149

而这些可以用于分类任务的编码，确实是双向的。有问题吗？对。

### [1:13:50](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=4430s) · b000150

对，没错。那么问题是，没有 mask 时，每个 token 都可以关注其他每个 token。完全正确。mask 的作用恰恰就是阻止 tokens 与它们之后的 tokens 建立连接。对。好的，很好。我想介绍一下这篇论文的背景。当时自然语言处理（NLP）领域正蓬勃发展。同一年还有另一篇里程碑式的论文，叫 ELMo，也就是来自语言模型的嵌入（Embeddings from Language Models）。

### [1:14:24](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=4464s) · b000151

我会说，那篇论文发表的时机有点不巧，因为它确实在构建双向表示方面提出了新的见解。但恰好它与 Transformer，与这类基于 Transformer 的同一研究路线，出现在同一年。所以它有点被掩盖了。简单介绍一下 ELMo 的主要思路，它基于双向长短期记忆网络（bidirectional LSTM），包含多个彼此堆叠的层。

### [1:15:01](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=4501s) · b000152

基本上，借助这种架构，你可以为每个词构建双向表示。那么，为什么它没有像 BERT 那么流行呢？因为它有之前模型同样的缺点，基本上由于这种循环性（recurrence），很难扩展。我想，你们很多人在想到 ELMo 和 BERT 时，首先想到的不是这些论文，因为它们是《芝麻街》（Sesame Street）里的角色。

### [1:15:40](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=4540s) · b000153

我长大的地方不认识《芝麻街》。所以对我而言，ELMo 和 BERT 就是论文的名字。但对你们来说，首先想到的可能是那些角色。所以我觉得这挺有趣。研究人员通常也挺爱玩。他们会尝试让缩写符合某个主题。所以如果你看看论文名字，会觉得挺有意思。

### [1:16:11](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=4571s) · b000154

好的，很好。为了深入了解我刚才提到的 encoder-only 模型的目标，你有一组 tokens 作为输入。这里的目标是执行一些任务，这些任务可能侧重于把某种表示投影到某个地方，通常就是分类任务。而 BERT 在这里的工作方式很具体。你会看到，这里有两类具有结构性作用的 tokens。

### [1:16:46](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=4606s) · b000155

首先是 CLS token，CLS 代表分类（classification）。它基本上是放在序列开头的占位 token，经过整个注意力、投影以及整个 encoder 机制之后，最终会被投影成一个可以用于分类的嵌入（embedding）。所以 CLS 就是某种占位符，用来承载整个输入的双向信息。

### [1:17:23](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=4643s) · b000156

另一个值得了解的 token 是这个 SEP token。它就像分隔符（separator）。我们很快就会看到它所对应的目标函数。它的目的是分隔两个句子。对。这就是非常概括的介绍。这个模型还有一点非常值得关注，就是它有多阶段训练（multi-stage training）这个概念。

### [1:17:56](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=4676s) · b000157

你不是一次性完成模型训练，而是分多个阶段进行。第一阶段的目的是与目标任务对齐。这就是我们所说的预训练（pre-training）。我们会详细看到，这种 pre-training 使用两个目标函数，分别是 MLM 和 NSP。MLM 代表掩码语言模型（Masked Language Model），NSP 则是下一句预测（Next Sentence Prediction）。

### [1:18:30](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=4710s) · b000158

masked language model 是让模型学习输入内部结构的一种方式。而 NSP 可以看作一种判断句子顺序是否合理的方式。我们会分别深入了解一下，不过，这是作者假设有助于学习高质量通用 embeddings 的一组目标函数。

### [1:19:03](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=4743s) · b000159

好。我想提到的第二点是，当你完成这些之后，还会有进一步的阶段，保留已经学到的 embeddings。然后在它上面接入另一个网络，通常是线性投影（linear projection），把学到的 embeddings 针对某个目标任务进行微调（fine-tuning）。这就是我们所说的 fine-tuning。对。

### [1:19:46](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=4786s) · b000160

对。那么问题是，这里依然只有一个 encoder 吗？因为 next-sentence prediction 看起来可能是 decoder 的任务。实际上，我马上会详细解释。next-sentence prediction 任务其实是把两个句子一前一后放在一起，预测它们是否真的连续。所以这是一个分类任务。对，这一点提得很好。我们很快就会详细看到。

### [1:20:17](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=4817s) · b000161

在详细介绍之前，我会讨论一下这种方法通常具有的优点和缺点。优点方面，这种 pre-training 机制可以在基本没有标注的数据上完成。你仍然有这个 next-sentence prediction 任务。但这是你可以控制的，因为你知道哪些句子彼此相接。所以你知道，这是自监督的（self-supervised）。

### [1:20:51](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=4851s) · b000162

至于 masked language model 任务，我们会看到它的具体内容。但它也是无监督的（unsupervised）。所以，这是一种从无标注数据中学习有意思的 embeddings 的非常有趣的方法。实际中，我们看到这些无标注数据能让模型学到有用的表示。然后，你只需要很少的数据就能在此基础上继续构建。因此，在 fine-tuning 阶段，你从已经学到的这些很好的 embeddings 出发，只需要调整少量权重。

### [1:21:30](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=4890s) · b000163

这通常能带来超越当时最先进水平（state of the art）的表现。至于缺点，当然，由于没有 decoder，所有文本生成任务都做不了。此外，这个两阶段过程，以及我们需要进一步调整 embeddings 这一点，也可以被看作一种 over hurdled \[字幕疑误，可能指额外障碍或负担\]。也就是说，与一些可以一次完成的更传统的方法相比，这种方法可能存在这样的问题。

### [1:22:08](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=4928s) · b000164

这可以被看作一个缺点。好的，很好。这里我列了一些变体的名字。稍后我们会深入了解其中两个。

### [1:22:24](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=4944s) · b000165

好。我想让大家关注最初的 Transformer。我们会一步一步看它发生了哪些变化，以及我们如何得到 BERT 架构。这就是上周我们在最初的 Transformer 论文中看到的内容。而 BERT 所做的，是提取其中的 encoder 部分，基本上接上我刚才提到的这些新目标函数，同时在表示 tokens 方面采用一些新的技巧。

### [1:23:00](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=4980s) · b000166

我想我们会逐一讲解。首先，有趣的一点是，它使用一种名为 WordPiece 的特定分词器（tokenizer）。你可以把它看成一种在训练集上学习的 tokenizer，所依据的合并规则会使似然（likelihood）最大化。基本上，你有一个庞大的训练集，然后训练一个 tokenizer，把原子 tokens 合并起来，构建目标词表。

### [1:23:38](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=5018s) · b000167

关于数量级，我提到了 O(30k)。通常，我想这就是他们在这篇论文中选择的大小。一般来说，这类论文中的词表大小在 10 的 4 次方、10 的 5 次方这个数量级，除了我们看到的免 token 方法，比如 ByT5，它的 tokens 集合非常有限，比如 2 的 8 次方，也就是 256。除了这个特例，通常都是这个数量级。

### [1:24:18](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=5058s) · b000168

基本上，我们会使用我提到的那些 tokens。比如，在开头放 CLS token，它会承载整个序列的双向表示。然后，用 SEP tokens 分隔两个句子，以进行 next-sentence prediction 任务。还有一点我暂时没讲到。我想，也许可以在深入讲解时再讨论。

### [1:24:53](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=5093s) · b000169

为了开展这个 masked language model 任务，当然需要遮蔽一些 tokens。所以，我们会看到这类 mask 的具体应用方法，放在哪里，以及以什么频率应用。我们也会从输出的角度来看，基于得到的表示，我们的任务是什么。这里我先快速略过，不过很快就会再回来讲。

### [1:25:24](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=5124s) · b000170

好的，很好。关于输入 embeddings，有一个很大的新变化——那么哪些保持不变？你仍然有庞大的 embedding 字典查找，为每个 token 提供要学习的 embedding。然后，你会把我们上节课看到的、Afshine 在本节课前面也讲过的位置编码（positional encoding）加上去，它既可以是硬编码的，也可以是学习得到的。

### [1:25:56](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=5156s) · b000171

我想这里的作者用的是硬编码版本，但我不太确定。不过通常性能大致相同。但这里有个新东西。它引入了一种新的编码，叫分段编码（segment encoding），仍然会以相加的方式加到 tokens 上，区别在于这里只有两种可能的编码。

### [1:26:26](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=5186s) · b000172

segment A 表示第一个句子，segment B 表示第二个句子。它的设想是帮助 NSP 任务，表示那些可能有助于刻画一个句子先于另一个句子的特征。至少这是作者采用的假设。我们会看到，后来这个假设受到了质疑。不过，这是这里引入的关键概念之一。

### [1:26:59](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=5219s) · b000173

到目前为止有问题吗？对。

### [1:27:28](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=5248s) · b000174

对，这一点很好。那么问题是，segment encoding 到底有什么作用？它基本上是学习出来的。你有两个索引，基本上就是两个可以学习的 embeddings。你只需把它们加上去，句子第一部分的 tokens 加 segment A，第二部分加 segment B。然后通过梯度下降（gradient descent）学习它。你不需要对它做什么。我想这边还有一个问题？对。

### [1:28:07](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=5287s) · b000175

没错。那么问题是，同一句子中的每个 token 都会具有相同的 segment encoding 吗？是的，对。好的，太好了。我发现我可能需要稍微加快一点。第二点我想强调的是，我们采用了 Transformer 的 encoder 部分。这里没有新东西，完全一样。我们有 self-attention，后面接这些 FFN。

### [1:28:37](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=5317s) · b000176

编码的双向性质就是从这里获得的。基本上，我们假设，同时使用 MLM 和 NSP 进行训练，会帮助我们在这个 encoder 中学到有用的 projection matrices，使其适用于任何分类任务。

### [1:29:01](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=5341s) · b000177

好的，很好。按照之前说的，我要更详细地讲一下这个 MLM 任务会做什么。看输入时，你基本上会有一个输入句子，然后随机替换一些 tokens。可能会替换为 mask token，这种情况占 80%。有 10% 的情况下，为这个 MLM 目标函数选中的 tokens 完全不会被替换。

### [1:29:39](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=5379s) · b000178

我们相当于在说，它还是同一个 token，只要预测这个相同的 token。还有 10% 的情况下，它会被换成某个随机的其他词。最终，你会得到一个用于执行 MLM 任务的 token 子集。这就是它的组成方式。好的，很好。这里的直觉基本上是，要预测一个 token 是什么，你就需要了解它的上下文。

### [1:30:10](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=5410s) · b000179

所以，我们会迫使模型学习它左右两侧周围的内容。这就是这种架构的双向性质实际发挥作用的地方。

### [1:30:24](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=5424s) · b000180

好的，很好。现在我们要讲 next-sentence prediction 任务。基本过程是从给定语料库中选择两个句子，50% 的情况下把它们按顺序并列呈现，其余时候则以某种随机顺序呈现。目标是在 CLS token 之上使用一个分类头（classification head），判断 A 和 B 是否连续。

### [1:30:58](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=5458s) · b000181

这就是它所做的全部事情。这里的假设是，它也有助于学到一些有用的 embeddings。

### [1:31:09](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=5469s) · b000182

好的，很好。这里我会介绍论文中使用的符号。我推荐大家阅读这篇论文。它非常值得读，《Attention is All You Need》也是。我会说，这是一篇里程碑式的论文。我想它有 170k 次引用，确实令人印象深刻。基本上，我们在最初的 Transformer 论文中称为 n 的量，现在称为 L。H，也就是之前称为 d model 的量，是 embeddings 的维度。

### [1:31:43](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=5503s) · b000183

A 是注意力头（attention heads）的数量，之前称为小写 h。这里展示这些新符号只是供参考，给大家说明一下对应关系。当然，我和 Afshine 会继续沿用原来的符号，保持一致，所以这里只是提供信息。还有一点有趣的是，当你在 Hugging Face 这样的模型仓库中查看 BERT 模型时，通常会发现它有多个版本。

### [1:32:17](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=5537s) · b000184

有时你会看到 case、uncased 这样的名称 \[字幕疑误，case 可能指 cased\]。这表示对数据进行了哪种预处理，是只包含小写词，还是会区分大小写。所以根据你关心的任务，这可能是一个需要选择的方面。好的，很好。我还给出了论文中为这些量选择的数值的大致数量级。

### [1:32:51](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=5571s) · b000185

如果我没记错，我想最初的 Transformer 有 12 个堆叠的 encoders 和 decoders。所以我想，这里的一些数字就是取自那里。

### [1:33:08](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=5588s) · b000186

所以，对，数量级是 1 亿个参数。

### [1:33:16](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=5596s) · b000187

到目前为止有问题吗？

### [1:33:21](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=5601s) · b000188

好的，很好。现在我们要讲 fine-tuning 阶段，目标基本上是拿来 pre-training 阶段学到的内容，然后冻结那些权重。不再重新训练同样的权重，而是在 CLS token 或你关心的 tokens 之上放一个用于分类的线性层。然后，你会学习那里的线性 embeddings。

### [1:33:54](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=5634s) · b000189

你会有一个分类任务。你既可以冻结所有这些预训练权重，只训练这些少量权重，也可以重新训练整个模型。我想有多种分类方案。其中一些选择会受到这些因素的影响：你愿意重新训练多大一部分网络，以及分类任务与原始 pre-training 任务有多大不同。

### [1:34:23](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=5663s) · b000190

好的，很好。举几个目标任务的 fine-tuning 例子，可以做 sentiment extraction，在 CLS token 上面构建一个分类层。我们还给出了其他例子，比如问答（question answering），基本上给你某个输入，模型的目标是检测回答片段的起点和终点。所以它基本上是 token 级别的某种目标函数。

### [1:34:59](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=5699s) · b000191

好的，很好。现在我建议深入看一个具体例子。我们最喜欢的例子，这只泰迪熊太可爱了。来看看 BERT 实际上是如何工作的。基本上，在 uncased 设置下，你会取这个句子，进行预处理，把所有内容都转成小写。然后，基于 tokenizer 学到的分词机制，应用 WordPiece 算法。

### [1:35:38](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=5738s) · b000192

比如这里，显然它学到了所有这些合并规则。所以这些就是出现在词表中的 tokens。然后，正如我之前说的，在开头加上 CLS token。接着加上 SEP token。还有这些 PAD tokens，基本上用于把序列填充到末尾。因为训练时是按批次（batch）进行的，而批次由长度固定的矩阵组成。

### [1:36:13](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=5773s) · b000193

对。我们就像上次深入讲解 Transformer 时一样，来深入看一看。这里有学习得到的 embeddings。它是一个庞大的查找表，把每个 token 的索引对应到学到的表示。你会加上 token 的位置嵌入（position embedding）。这里还有一个新东西——分段嵌入（segment embedding）。就像我们说的，它是一个加到每个 token 上的 embedding。

### [1:36:47](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=5807s) · b000194

相同的 embedding 会加到相同的 tokens 上。所以所有这些 tokens 都有相同的 segment A。然后，另一个 embedding B 会加到 segment B 的所有 tokens 上。好的，很好。现在，类似 Transformer，你得到了具有位置感知和上下文感知能力的东西——还没有上下文感知，不过这里已经有分段感知了。好的，很好。基本上，它会经过这个 encoder 架构。

### [1:37:22](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=5842s) · b000195

然后，在最后，对于 sentiment extraction，我们不关心除 CLS token 以外的各个 token 对应的 embeddings。因为我们关心的是 CLS token 的输出 embedding，在它上面接一个线性层，用来学习某个分类任务。

### [1:37:50](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=5870s) · b000196

这里有问题吗？

### [1:37:55](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=5875s) · b000197

所以，除了 CLS token 之外，我们舍弃所有输出 embeddings，这一点大家能理解吗？对，嗯。

### [1:38:21](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=5901s) · b000198

对，那么问题是，这个 FFN 是什么，对吗？这个 FFN 对应什么？基本上，你有一个从输出 embedding 的维度到目标任务的映射。比如，它可以是正面或负面的分类。你有一个具有某种宽度的隐藏层（hidden layer）。通常会用两个矩阵，学习从输入到那个隐藏层，再从隐藏层到输出的投影。

### [1:38:51](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=5931s) · b000199

然后，基于这里学到的 embeddings，学习这些权重，以完成分类任务。

### [1:38:59](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=5939s) · b000200

对，好问题。这正是我在等的问题。那么问题是，为什么我们要丢弃其他所有输出 embeddings？这里不需要它们。我们正在做一个分类任务。我们约定在某个 token，比如 CLS token，之上进行操作。这个 token 的神奇之处在于，encoder 中的所有这些 self-attention 机制已经把其他各个 token 的表示混合到了这个表示中，因此输出 embeddings 具有上下文感知能力。

### [1:39:39](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=5979s) · b000201

所以基本上，这是一个面向分类的 embedding。我们说的要接入那个线性层的，就是它。当我说丢弃其他所有 embeddings 时，实际上指的是分类这种情况。但如果是在 token 级别做分类，那么每一个都可能用到。比如我提到问答时，如果你想检测一个给定 token 是否是答案的开头、答案结尾的开头 \[字幕疑误，可能指答案的开头或结尾\]，通常会有两个 FFN，分别预测答案的起点和终点。

### [1:40:23](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=6023s) · b000202

你会把它应用到每一个这样的 embedding 上。

### [1:40:29](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=6029s) · b000203

还有其他问题吗？对。

### [1:40:37](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=6037s) · b000204

那么问题是，CLS 的查询（query）、键（key）和值（value）是什么？它的过程与其他所有 tokens 相同。这里，你为 CLS token 学习一个 embedding 表示。它会被投影成 query，投影成 key，投影成 value，完成所有注意力计算。最后，你得到这个基本上已经关注过其他所有 tokens 的 embedding。所以答案就是，它和其他 tokens 一样。

### [1:41:11](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=6071s) · b000205

对。把它当作一个 token 就行，它可以是任何 token，过程都一样。好的，太好了。我看到我们还剩五分钟。我会快速讲完剩下的内容。BERT 的一个优点，也是 ELMo 的优点，就是 embeddings 是具有上下文信息的。在这里你可以看到，基于这些学到的 embeddings，学习任何你想做的分类任务都很容易。

### [1:41:43](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=6103s) · b000206

这种灵活性很受欢迎。它在业界被广泛使用。如今，只要涉及情感检测（sentiment detection）或其他分类相关任务，使用类似 BERT 的模型就很常见。现在我来讲一下它的局限性。正如你在原始论文中看到的，我想上下文长度是 512。

### [1:42:16](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=6136s) · b000207

因此，在这篇早期论文中，它通常是受限的。Afshine 提到了一些技术，说明如何进一步增大上下文大小，而不让复杂度基本上完全飙升。还有一些近似方法，比如计算局部注意力（local attention）等。使用这些技巧，可以在将计算需求保持在合理范围内的同时，增大上下文。

### [1:42:50](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=6170s) · b000208

我还会讲另外两个局限性，我们将看看其他模型如何尝试解决它们。一个是延迟可能被认为较高。BERT base 仍然有 1.1 亿个参数，相当多。有没有办法让它更小、更快？第二个是，你有 MLM 和 NSP 这两个目标函数。它们真的都有用吗？

### [1:43:21](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=6201s) · b000209

有没有办法简化 pre-training 过程？我们马上会看到如何做。

### [1:43:30](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=6210s) · b000210

首先，关于我们提到的第二个局限性，基本上就是对成本的敏感性。这里有谁听说过蒸馏（distillation）？

### [1:43:49](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=6229s) · b000211

很好，有几个人。我想快速展示一下 Hinton、Vinyals 和 Jeff Dean 的这段话，我觉得很有启发性。一个值得具备的思维方式是，认识到给定模型输出的分布，对于了解它学到了什么其实非常有帮助。所以，软目标（soft targets）包含了几乎全部知识。这句话出自他们的一次讲座。

### [1:44:23](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=6263s) · b000212

基本上，他们后来开创了 distillation 这个概念。你很快就会在实践中发现，学习一个模型的分布，比直接学习硬标签（hard labels）更有帮助。这里有教师模型（teacher model）和学生模型（student model）的概念。distillation 的目标基本上是让较小模型的输出分布直接对应更复杂的模型，而不是 hard labels。

### [1:45:00](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=6300s) · b000213

为此使用的最小化目标函数是 KL 散度（KL divergence），它基本上是在说，在由教师，也就是教师 T，所描述的世界中，用学生 S 建模会有多糟。它基本上是在评估学生分布会有多接近 T 所描述的世界。

### [1:45:30](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=6330s) · b000214

这里有趣的一点是，如果你的 yT 分布只是一个 hard label，就会得到交叉熵损失（cross-entropy loss）。也就是说，如果只有一个位置是 1，其他所有位置都是 0，那么就得到负的 log yS，这很有意思。然后，DistilBERT 的作者所做的是——顺便说一下，这篇论文非常简洁，大概只有四页，但影响非常大。

### [1:46:00](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=6360s) · b000215

它说，如果把层数减少 2 \[原文表述有歧义，可能指减至一半\]，就能获得很大收益，同时性能几乎不变，这非常了不起。他们基本上用 distillation 来保留这种性能。因此，除了减少层数之外，distillation 就是关键。最后，我要讲 RoBERTa。它研究发现，移除 NSP 目标函数，几乎不会导致性能下降。

### [1:46:36](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=6396s) · b000216

所以他们就把它去掉了。还加入了一些技巧，比如动态进行遮蔽（masking）。例如，对于某段给定文本，在每个训练轮次（epoch），也就是每次看到相同文本时，都会改变 masking。他们还采用了一些数据策略，因为他们发现模型的训练远远不够。所以，他们大幅增加了数据的多样性和规模。结果发现，在相同基准测试（benchmarks）上的性能提高了不少。

### [1:47:10](https://www.youtube.com/watch?v=yT84Y5zCnaA&t=6430s) · b000217

今天就到这里。谢谢大家。周末愉快。
