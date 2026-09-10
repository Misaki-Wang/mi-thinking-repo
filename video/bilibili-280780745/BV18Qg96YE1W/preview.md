# 游凯超：vLLM、开源 Infra 与 Co-design

- 作者：张小珺商业访谈录；嘉宾：游凯超，简介介绍为 Inferact 联合创始人兼首席科学家。
- 原题：对游凯超3小时访谈：开源Infra、和模型Co-design 、从社区到公司、“如果vLLM失败，我们会后悔一辈子”。
- 发布：2026-07-28；时长：02:59:09。
- 来源：[Bilibili 原视频](https://www.bilibili.com/video/BV18Qg96YE1W/)。
- 阅读：[中文讲稿](transcript.zh-CN.md) · [系列目录](../README.md) · [学习指引](../GUIDANCE.md)。

> 预览依据视频简介与官方分段，非全文人工校对。社区历程和组织取舍来自作者简介与访谈，技术预测归属于嘉宾。

## 先抓住的问题

简介围绕两条线展开：vLLM 如何从开源研究项目走向社区与公司，以及模型、Infra 和 Harness Engineering 为什么需要讨论联合设计。适合与 Kimi 技术领读配对，关注模型选择如何进入系统实现。

## 官方分段导航

- [00:02:18 · 从算法到机器学习系统](https://www.bilibili.com/video/BV18Qg96YE1W/?t=138)：记录研究视角的变化。
- [00:37:56 · vLLM 的诞生](https://www.bilibili.com/video/BV18Qg96YE1W/?t=2276)：了解简介提到的校园项目背景。
- [01:07:25 · 维护者的坚持](https://www.bilibili.com/video/BV18Qg96YE1W/?t=4045)：阅读项目选择与个人投入的讨论。
- [01:20:11 · 开源治理](https://www.bilibili.com/video/BV18Qg96YE1W/?t=4811)：作者分段标题为“仁慈的独裁者”，留意它在社区治理中的具体含义。
- [01:37:16 · 从社区到创业](https://www.bilibili.com/video/BV18Qg96YE1W/?t=5836)：对照开放社区与商业组织的目标。
- [01:52:56 · 模型与 Infra 的 Co-design](https://www.bilibili.com/video/BV18Qg96YE1W/?t=6776)：查找联合设计涉及哪些参与方和约束。
- [02:15:10 · Token 与电力](https://www.bilibili.com/video/BV18Qg96YE1W/?t=8110)：保留嘉宾讨论效率时采用的单位与前提。
- [02:35:41 · 技术预测](https://www.bilibili.com/video/BV18Qg96YE1W/?t=9341)：单独标记预测与当时已观察到的现象。

## 学习时可以追问

1. 一项模型设计进入推理系统时，会增加哪些实现和运维约束？讲解有没有给出具体案例？
2. 社区维护者与商业组织分别服务谁，冲突通过什么机制处理？
3. 讨论 Token 与电力时，指标是在描述成本、效率还是需求？这些指标是否可直接比较？

## 术语与检索线索

`vLLM`、`Inferact`、`AI Infra`、`Co-design`、`Harness Engineering`、`Token`、`Open Source`。原简介将模型、系统与 Harness Engineering 放在联合设计的讨论背景中，具体接口与方法需回到讲稿核对。
