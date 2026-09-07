# Modern generative AI · Diffusion、flow matching 与可控生成

2026-03-12 · Week 6.2 · 来源：61 页 slides + 视频字幕。视频后段快速介绍 flow matching；控制方法与部分跨模态例子以 slides 补充，不能假设所有页都在视频中完整讲解。

## 三分钟预览

本讲接续 VAE，把逐步加噪与去噪看成分层潜变量过程，再转向连续时间的向量场视角。预览时先固定三个问题：模型预测的量是什么、训练用什么目标、采样需要多少次网络计算。最后考虑条件控制和质量评估。

## 来源导航

| 主题 | Slides | 视频 |
|---|---|---|
| VAE 回顾与连续潜变量 | [第 15–23 页](https://mit-mi.github.io/mmai-course/spring2026/schedule/lec6.2%20-%20more%20generative%20AI.pdf#page=15) | [03:17 起的课程导入](https://www.youtube.com/watch?v=LGBQ0c_4HBA&t=197s) |
| 加噪、去噪及预测参数化 | [第 24–29 页](https://mit-mi.github.io/mmai-course/spring2026/schedule/lec6.2%20-%20more%20generative%20AI.pdf#page=24) | [50:17 起](https://www.youtube.com/watch?v=LGBQ0c_4HBA&t=3017s) |
| 连续时间与 flow matching | [第 30–35 页](https://mit-mi.github.io/mmai-course/spring2026/schedule/lec6.2%20-%20more%20generative%20AI.pdf#page=30) | [65:46 起](https://www.youtube.com/watch?v=LGBQ0c_4HBA&t=3946s) |
| 跨模态生成、指标与 guidance | [第 36–57 页](https://mit-mi.github.io/mmai-course/spring2026/schedule/lec6.2%20-%20more%20generative%20AI.pdf#page=36) | slides 补充材料 |

## 核心机制

- **diffusion 的正向过程通常预先规定。** 从数据逐步加入噪声，训练反向恢复所需的网络。与普通 VAE 对比时，关注哪些分布可学习、哪些噪声日程固定，而不只看 encoder/decoder 的框图相似。
- **预测 x、noise 或 velocity 不应混写。** 各参数化的转换与噪声日程相关。实现中必须让训练 target 与采样公式一致；“网络预测干净图像”只是其中一种表述。
- **flow matching 学的是向量场。** 沿时间积分 `dx/dt = vθ(x,t)` 把初始分布输运到目标分布。Euler 更新只是一个数值求解例子；实际成本还取决于函数求值次数（NFE）、步长与允许误差。
- **latent diffusion 同时使用压缩与生成。** autoencoder 把像素映射到 latent，diffusion 在 latent 中建模。需要分别分析重建质量与生成质量。
- **文本、音频、视频并非直接套用像素噪声。** 文本离散 token 需要匹配其空间的 corruption/decoding；视频还要检查 temporal coherence、physical consistency；多模态输出必须相互同步。
- **CFG 调整条件影响。** classifier-free guidance 把有条件与无条件预测结合。较强条件不等于全面更好，需要同时看多样性、伪影和内容遵循。
- **单一分数不够。** 第 49 页列出 FID、CLIP Score、precision/recall 与 aesthetic score。FID 依赖特征与评估协议，CLIP Score 也不直接测量关系、计数或事实正确性。

## 两个必要的边界

Slides 的 VAE / diffusion / flow matching 对照表是教学概括。“flow matching 更快”必须在模型、采样器、NFE 与输出质量条件下比较；不能把 ODE 和 diffusion 看成互斥世界。表里的 FID 阈值也不宜脱离数据集作为通用合格线。

## 自测与练习

列一个对照表：representation、training target、conditioning、sampler、NFE、evaluation。分别填一个 latent diffusion 和 flow matching 实例。随后设计两组语义相同但关系相反的 prompt，检查生成结果是否区分主客体关系。

继续阅读 [本讲 Readings guidance](readings.md)，其中已标出课表的一处论文链接错配。
