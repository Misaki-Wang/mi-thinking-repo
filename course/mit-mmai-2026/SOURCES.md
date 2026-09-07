# 来源、勘误与处理状态

资料核验日期：2026-09-07。主来源为 [官方课表](https://mit-mi.github.io/mmai-course/spring2026/schedule/)、[Paul Liang 频道](https://www.youtube.com/@paulliang279/videos) 及课程链接的讲义、notebook、论文与作者页面。

## 覆盖

- 29 个课表记录，24 个教学单元。
- 23 份可获取教学材料：22 个 PDF 与 1 个 Colab notebook；合计 1,214 页或 notebook cells。页数只用于资源检查，不代表每页都包含独立知识点。
- 13 个匹配的 Spring 2026 视频，英文字幕 1,089 段，总视频时长 15 小时 14 分 48 秒。
- 92 条课表 reading 记录，按 URL 去首尾空白合并为 87 个来源；这些 URL 仍可能指向同一论文的不同形式。全部来源身份已核对，不代表每篇论文已通读与复现。

## 需要知道的课表问题

| 位置 | 发现 | 档案处理 |
|---|---|---|
| Week 3.2 | Fusion 链接实际是 HAIM 医疗多模态演示稿 | 按真实 PDF 总结，保留课表题目 |
| Week 5.1 | Scaling Instruction-Finetuned Language Models 链到 LoRA | 保留原链接；提供标题匹配的 [2210.11416 候选](https://arxiv.org/abs/2210.11416) |
| Week 5.1 | Quantization 教程重复列出 | guidance 阅读一次，catalog 保留两次出现 |
| Week 5.2 | Native Multimodal Scaling Laws 标题重复拼接 | 展示可读标题并保留原记录 |
| Week 6.2 | Flow/Diffusion Connections 链到 RNN sparsity | 提供 [2411.07625v1 候选](https://arxiv.org/abs/2411.07625v1)，注明版本与标题变化 |
| Week 10.2 | LLaVA-Med 链到 BiomedCLIP | 提供 [2306.00890 候选](https://arxiv.org/abs/2306.00890)，教师原意未另行确认 |
| Week 11.1、11.2 | slides URL 404，真实文件名多出空格 | 以官网仓库文件树核验后恢复链接，保留 original/resolved 两者 |
| Week 12.2 | slides 404，官网文件树与频道均无对应材料 | 仅写 syllabus-based 准备建议，明确不算 lecture summary |

候选更正并非教师确认；用于避免读错，不静默更换原始课表记录。不同论文版本或标题变体也保留证据。

## Slides 与视频不完全同步

部分视频会先补讲上一讲，部分 slides 后段没有在录制内容中展开。例如 Week 4.1 的部分内容延续到 Week 4.2 视频；Week 14.2 视频在 OpenTouch 后收尾，slides 后续 HAI guideline 等是额外材料。各讲预览区分来源覆盖。视频时间链接定位到相关字幕块起点，PDF 页码按文件实际页序。

Notebook 也包含值得审查的细节，例如 data split、baseline 样本和训练/评估频次的代码与文字差异；本档案给出学习检查，不声称已经运行这些训练任务。

## 发布与处理边界

课程网站仓库有 MIT License，但视频与第三方论文的授权需分别判断。本次视频 metadata 未提供 Creative Commons 标记。公开网站提供原创摘要、阅读问题、术语表、出处和时间/页码链接；原始 PDF、notebook、完整字幕及处理中间状态留在本地忽略目录。

完整中文逐字译稿的处理状态为 **paused_permission_needed**；此前单讲试运行的中文译稿单独保留，不能算作整门课程译完。已为后续处理设定保留专业英文术语、模型名、缩写和疑似 ASR 错误提示的翻译规则。

## 可追踪记录

- [catalog.json](catalog.json)：官方题目、日期、Readings、视频映射、恢复后的 slides URL 和资源证据。
- [reading-sources.json](reading-sources.json)：论文/页面的真实标题、来源身份、证据粒度、错链候选。
- [transcript-status.json](transcript-status.json)：每个视频的字幕来源、段落数、哈希与翻译状态。

原始材料的观点与数字属于其作者；本网站由 Codex 整理为学习辅助笔记，不是 MIT 官方课程网站，也不代表对所有论文结论的独立验证。
