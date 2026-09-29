# CME 295 Autumn 2025 · 来源与整理记录

[回课程目录](README.md) · [学习路线](GUIDANCE.md)

## 来源

- [Stanford CME 295：2025 syllabus](https://cme295.stanford.edu/syllabus/2025/)：授课日期、讲题、slides 链接、视频章节时长和考试节点。
- [Stanford Online：Autumn 2025 playlist](https://www.youtube.com/playlist?list=PLoROMvodv4rOCXd21gf0CF4xr35yINeOy)：9 个官方公开视频。playlist 标题、Stanford Online 频道、视频 ID 和时长均已核对。
- 视频逐字稿使用各视频页提供的 `en-US` 英文字幕轨；工具检测 9 讲均为 manual captions（非自动生成字幕）。Codex 按字幕分段制作中文翻译和双语稿，保留视频时间链接；完整性、来源、授权及文件 SHA-256 见 [TRANSCRIPTS](TRANSCRIPTS.md) 与 [transcript-status.json](transcript-status.json)。字幕可能含有原始字幕编辑/识别误差，译文未经逐句人工校订。
- Slides 为 Stanford 官方 fall25-cme295-lecture1.pdf 至 lecture9.pdf。共 1,205 页，逐页文字层与页数均已核对；原 PDF 保留官方链接，未复制进公开目录。用户于 2026-09-30 确认已获得这九套 slides 的渲染图公开发布授权；图片是未裁切的原页渲染，逐页来源和 SHA-256 见同步阅读器的 `slides-index.json`。
- 课程主页列出的教材为 [Super Study Guide: Transformers & Large Language Models](https://superstudy.guide)。本归档只保留书籍链接，没有复制教材内容。

## 归档口径

- 采集整理日期：2026-09-29。归档版本：Autumn 2025。
- 用户于 2026-09-29 明确确认已获得 Stanford Online CME 295 Autumn 2025 九讲逐字转写与公开发布授权。此用户确认不是 Creative Commons 许可声明；视频原有 license metadata 未作推断或修改。
- 用户于 2026-09-30 另行确认已获得 Stanford CME 295 Autumn 2025 九套 slides 渲染图的公开发布授权。这是对本次指定材料的用户授权记录，不声明任何第三方图表或论文图片另有 Creative Commons 许可。
- 日期以 2025 syllabus 的授课日期为准。Stanford Online 后续才把录像上传至 YouTube；视频上传日期不替代上课日期。
- syllabus 没有列出逐讲 assigned readings。各讲 readings.md 是从课件实际出现的引用中挑选的补充阅读，不代表教师指定必读。
- 每讲预览以 slides 页码、视频章节导航组织。未将视频内容扩写成逐字稿或完整录像总结。
- 九讲逐字稿保留英文字幕、Codex 中文译文和双语对照三个 Markdown 版本。由于来源有完整英文字幕，本轮未使用 Whisper 或 GPU。
- [讲稿 × Slides 同步阅读器](https://misaki-wang.github.io/mi-thinking-repo/reader/stanford-cme295-2025/index.html)使用页面文字与时间戳检索做初始对应，不是逐帧/人工校准；未匹配项明确显示为空，读者可在浏览器本地逐段校正并导出。
- 逐讲结构核验覆盖 1,885/1,885 个中英段落、段落 ID 顺序、视频与秒级时间戳链接以及发布 Markdown 正文，未发现结构错误。8 条数字启发式提示均逐段复核为正确的中文数量级换算（如 110 million → 1.1 亿），不是遗漏数字；译文未做逐句人工事实校订。
- YouTube 时间链接使用公开章节起点，不代表逐字对齐。
- 本地保留的 slides PDF 的页数与 SHA-256 用于来源版本复核。原 PDF 和抽取文本留在本机忽略目录 .work/。
- 课程主页当前可能显示新学期内容；本归档固定在用户指定的 2025 版本。
- 用户给出的 2025 schedule 地址在本次检索器中返回拒绝访问；课表日期、标题和 topics 来自该 Stanford 页面仍可读的公开索引快照，并与 9 套官方 PDF 的封面编号/内容和 Stanford Online playlist 9 个条目逐一对应。每套 PDF 通过官方直链获取；videos 的 ID、标题、频道和时长从官方 playlist 元数据核对。

## 课程结构

1. Transformer 与 NLP 基础
2. Position representations、normalization、attention variants、BERT
3. LLM、MoE、decoding、prompting 与 inference optimization
4. Pretraining、parallelism、FlashAttention、SFT 与 LoRA
5. Preference data、reward modeling、PPO 与 DPO
6. Reasoning、RLVR、GRPO 与 scaling
7. RAG、检索指标、tool calling、MCP 与 agents
8. Metrics、LLM-as-a-Judge、bias、agent evaluation 与 benchmarks
9. ViT、VLM、diffusion、hardware 与 open research questions

考试节点：Midterm 2025-10-24；Final 2025-12-10。课件写明 Midterm 覆盖 lectures 1–4，Final 覆盖 lectures 5–9。
