# MI Thinking

我的学习笔记：课程、研究阅读与持续思考。

- [学习网站](https://misaki-wang.github.io/mi-thinking-repo/)
- [Course · 课程](course/README.md)
- [Blog · 思考](blog/README.md)
- [Paper · 论文](paper/README.md)

## 当前归档

[MIT Modeling: MultiModal AI · Spring 2026](course/mit-mmai-2026/README.md)：24 个教学单元的入口、23 份可获取教学材料的原创预览、逐讲 Readings guidance、全课学习路线与中英术语表。13 个公开视频的 1,089 段已全部完成中文翻译，提供 39 份英文、中文和双语 Markdown。唯一缺失的 Agents tutorial 保留明确的资料缺口与准备建议。

- [先读 GUIDANCE](course/mit-mmai-2026/GUIDANCE.md)
- [全部讲稿 · 中文 / English / 双语](course/mit-mmai-2026/TRANSCRIPTS.md)
- [专业术语 TERMS](course/mit-mmai-2026/TERMS.md)
- [全文讲稿与翻译说明](course/mit-mmai-2026/TRANSLATION.md)
- [来源、勘误与完整性](course/mit-mmai-2026/SOURCES.md)

## 更新与预览

内容保存在 Markdown 文件中，网站由 Python 标准库构建，无额外运行依赖。课程放入 `course/`，独立思考放入 `blog/`，论文阅读放入 `paper/`。新增 Markdown 文件后，网站会自动生成页面、导航与搜索记录。

```sh
python3 scripts/build_site.py
python3 -m unittest discover -s tests -v
```

推送到 main 后，GitHub Actions 自动构建并发布 GitHub Pages。生成的 docs 不提交，源 Markdown 是可维护的记录。

本地预览：

```sh
python3 scripts/build_site.py --base / --output .site-preview
python3 -m http.server 8000 --directory .site-preview
```

## 材料约定

学习笔记保留原始出处、页码或视频时间位置，并区分讲义内容、视频内容与个人学习建议。模型名、算法名、数据集、公式符号保留英文；核心术语按 [TERMS](course/mit-mmai-2026/TERMS.md) 统一。

公开仓库包含原创学习摘要、guidance，以及经维护者确认授权后整理的英文、中文和双语讲稿。讲稿按段落与时间戳对应；专业英文术语保留。原始字幕文件、PDF、notebook 和运行中间文件保存在本地忽略目录 `.work/`，逐讲完成情况见网站与 [来源记录](course/mit-mmai-2026/SOURCES.md)。
