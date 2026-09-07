# Multimodal generation · 从生成接口到 VAE

2026-03-10 · Week 6.1 · 来源：34 页 slides + 视频英文字幕。

## 三分钟预览

先区分“找出已有图像”与“产生新图像”，再把生成问题写成概率分布。潜变量（latent variable）提供一种建模隐藏变化因素的方法；Gaussian mixture model（GMM）帮助建立直觉，VAE 则用 encoder、decoder 和变分近似扩展到复杂数据。

## 来源导航

| 主题 | Slides | 视频 |
|---|---|---|
| 检索与生成的输出接口 | [第 8–13 页](https://mit-mi.github.io/mmai-course/spring2026/schedule/lec6.1%20-%20generative%20AI.pdf#page=8) | [22:58 起](https://www.youtube.com/watch?v=KlHIR7lT-mo&t=1378s) |
| 概率建模、likelihood 与采样 | [第 20–21 页](https://mit-mi.github.io/mmai-course/spring2026/schedule/lec6.1%20-%20generative%20AI.pdf#page=20) | [50:08 起](https://www.youtube.com/watch?v=KlHIR7lT-mo&t=3008s) |
| 潜变量与隐含变化因素 | [第 22–28 页](https://mit-mi.github.io/mmai-course/spring2026/schedule/lec6.1%20-%20generative%20AI.pdf#page=22) | [53:41 起](https://www.youtube.com/watch?v=KlHIR7lT-mo&t=3221s) |
| VAE encoder / decoder / reparameterization | [第 29–32 页](https://mit-mi.github.io/mmai-course/spring2026/schedule/lec6.1%20-%20generative%20AI.pdf#page=29) | 以 slides 公式为准 |

## 概念主线

1. **retrieval 与 generation 是两种不同决策。** 前者在固定候选集合中选择，后者学习数据分布并生成新样本。已有素材的真实来源也不保证检索结果与当前问题相关。
2. **从分类条件到生成分布。** 分类常写 `p(y | x)`，无条件生成写 `p(x)`，文本条件图像生成写 `p(image | text)`。首先指出观察变量与条件，才能比较训练目标。
3. **visual token 是表示选择。** 第 17–18 页以离散码本和自回归 token 生成为例；压缩到有限代码有利于把某些连续预测转成分类，但也引入重建瓶颈。
4. **GMM 展示边缘分布如何变复杂。** 先选 component，再从对应 Gaussian 采样。每个条件分布简单，混合起来仍能表达多峰结构；EM 在估计 component responsibility 与更新参数之间交替。
5. **VAE 中 encoder 与 decoder 方向相反。** encoder 近似 `q(z | x)`，decoder 建模 `p(x | z)`；先验 `p(z)` 允许从潜空间采样后生成。第 30 页的 reparameterization 为 `z = μ + σ ⊙ ε`，其中 `ε ~ N(0,I)`。
6. **目标有两种相互约束的需求。** ELBO 包含重建项与 KL 正则：鼓励从 z 恢复 x，也让 posterior 接近 prior。重建好不意味着随机采样好；潜变量也不会仅靠这个目标就自动对应清晰、独立的人类概念。

## 阅读时校正简化说法

Slides 第 19 页把发展概括为用 diffusion 替换 VAE。实际讨论 latent diffusion 时，autoencoder 仍可能用于压缩，diffusion 在其 latent space 内学习分布。理解时分开“压缩表示”和“生成分布”两层，不把这句话当作所有架构的定义。

## 自测与练习

- 画出训练时 x → encoder → z → decoder 与采样时 z → decoder 两条路径。
- 如果 KL 项权重过大或过小，分别检查哪些现象？
- 用同一个文本条件比较一次 retrieval 与 generation，分别记录相关性、真实性来源和覆盖范围。

继续阅读 [本讲 Readings guidance](readings.md)。
