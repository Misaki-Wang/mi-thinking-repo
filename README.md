# MI Thinking

我的学习笔记：课程、研究阅读与持续思考。

- [学习网站](https://misaki-wang.github.io/mi-thinking-repo/)
- [Course · 课程](course/README.md)
- [Blog · 思考](blog/README.md)
- [Paper · 论文](paper/README.md)

## 当前归档

[MIT Modeling: MultiModal AI · Spring 2026](course/mit-mmai-2026/README.md)：24 个教学单元的入口、23 份可获取教学材料的原创预览、逐讲 Readings guidance、全课学习路线与中英术语表。唯一缺失的 Agents tutorial 保留明确的资料缺口与准备建议。

- [先读 GUIDANCE](course/mit-mmai-2026/GUIDANCE.md)
- [专业术语 TERMS](course/mit-mmai-2026/TERMS.md)
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

公开仓库包含原创学习摘要与 guidance。下载的完整字幕、PDF、notebook 和处理中间文件放在本地忽略目录 `.work/`；完整中文逐字译稿与公开再分发仍待内容授权确认，不算作本次已完成的公开内容。具体状态见课程来源页。
