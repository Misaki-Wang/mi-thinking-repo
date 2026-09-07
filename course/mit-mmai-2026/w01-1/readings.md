# W01-1 · Reading guidance：建立术语地图

目标：读完后能用共同语言比较不同年代的 multimodal research，并为自己的项目标出核心挑战。下列三项完整保留课程表 Readings；P1/P2 是本归档建议的阅读顺序，不是教师公布的 required/optional 标记。本次核验了三篇论文的作者原始 arXiv 摘要和题录，**尚未逐页审阅全文**；以下明确区分已支持的主张与需要你到正文检查的问题。

## P1 · Foundations and Trends in Multimodal Machine Learning: Principles, Challenges, and Open Questions

[论文](https://arxiv.org/abs/2209.03430) · 证据：primary abstract。

带着问题读：为什么“多种输入”不足以定义一个好的研究问题？摘要以 heterogeneity、connections、interactions 三个原则解释多模态的特殊性，再提出 representation、alignment、reasoning、generation、transference、quantification 六类挑战。优先寻找正文中这三个原则和六类挑战的定义，用自己的数据各举一例；模型清单可以暂时略读。

提取与检查：每个术语写成“研究对象＋想解决的困难”，避免仅抄名词。特别检查 fusion、coordination、fission 如何落入 representation；再选一个开放问题，写出什么实验结果会支持或削弱它。不要把综述分类当成互斥的模型分类：一个系统可能同时涉及多类挑战。

## P1 · Multimodal Machine Learning: A Survey and Taxonomy

[论文](https://arxiv.org/abs/1705.09406) · 证据：primary abstract。

带着问题读：2017 年的五类挑战与新综述有什么变化？摘要列出 representation、translation、alignment、fusion、co-learning，并说明这种 taxonomy 超越单纯 early/late fusion。优先围绕这些分类阅读，挑一个当年的研究例子映射到新框架。

提取与检查：下面的映射是学习用的概念对应，不是两篇论文宣称的一一等价。正文中应检查每个术语的范围，尤其 translation 与更广义 generation、co-learning 与 transference 之间有哪些边界差异。

| 2017 术语 | 对照新综述时的阅读问题 |
| --- | --- |
| Fusion | 哪些方法被放进 representation，哪些还涉及 alignment？ |
| Translation | 它覆盖哪些 generation 情形，又不覆盖哪些？ |
| Co-learning | 它与 transference 的训练/测试模态设定有什么联系？ |

## P2 · Representation Learning: A Review and New Perspectives

[论文](https://arxiv.org/abs/1206.5538) · 证据：primary abstract。

带着问题读：同样的原始数据，为什么换一种 representation 会改变学习难度？摘要将这一点与 explanatory factors of variation 是否被纠缠或隐藏联系起来，并讨论 probabilistic models、auto-encoders、manifold learning 和 deep networks。先找 representation 的目标、priors 与 factors of variation 的讨论，再选择一种熟悉的方法深入。

提取与检查：为“场景中对象身份”和“光照/视角”各写一个因子，判断你的任务希望保留、忽略还是单独表示它。再检查一个 reconstruction objective 是否可能很好地重建输入，却没有凸显目标标签。这里是阅读问题，不是摘要已经证明的普遍定理。

## 读后比较与交付

前两篇回答“多模态研究有哪些问题”，第三篇回答“信息怎样变成可学习的表示”。先用第三篇解释一个坏表示，再用新综述判断问题属于 heterogeneity、alignment 还是 task interaction；最后用旧综述观察术语演化。

提交一页 Markdown：三原则各 1 个例子、六挑战各 1 句话、旧新 taxonomy 的 3 个对应关系、你的项目最重要的 2 个挑战，以及 1 个你目前无法从摘要回答、必须查全文的问题。回到 [课程预览](preview.md) 对照来源定位。
