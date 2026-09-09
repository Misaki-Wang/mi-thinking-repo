# 讲稿 × Slides · 独立同步阅读器

[打开同步阅读页](https://misaki-wang.github.io/mi-thinking-repo/reader/mit-mmai-2026/index.html)

这是新增的实验阅读页，使用独立 HTML、CSS、JavaScript 与数据目录。原有课程预览、讲稿、Readings、Blog 和 Paper 页面没有改动。

## 使用

- 左侧点击或滚动讲稿，右侧切换到该段建议对应的 slide。
- 右侧翻页、选择页码或缩略图，左侧跳到该页已关联的讲稿。一个 slide 对应多段时，优先保留当前段，否则定位第一段；也可点击“本页讲稿”的时间按钮。
- 可切换中文、英文或双语；取消“双向同步”即可分别浏览。
- 点击“校对本段”会固定当前段落，再浏览目标 slide 并保存；点击候选页也会先进入固定段落的校对模式，不会直接修改关联。
- 校对仅保存在当前浏览器，可按章节导入/导出 JSON；“恢复自动对应”支持撤销。
- 地址包含章节、段落与 slide 位置，可复制链接继续阅读。

## 对应关系的边界

当前覆盖 13 讲、1,089 个中英对应段落、723 个实际 PDF 页面。初版为 639 个段落提供建议关联（包含 36 处图文校核），其余 450 段显示暂无可靠对应。数量是关联覆盖度，不是准确率。

自动关联基于英文内容与 slide 文本、前后讲授顺序及已有预览导航线索，不是逐帧视频识别。一个约一分钟的讲稿段落可能讲到多张 slides；重复构图、动画页、纯图示、课堂提问和未讲内容可能无法唯一对应。翻到未关联的 slide 会明确提示，保留独立浏览位置。

Week 4.2 和 Week 5.1 包含前一讲的补充内容，因此阅读器会同时提供相关的前一份 PDF，并显示原始讲义名称和原始页码。Week 14.2 的后续未讲附录仍可浏览，但不伪造对应的课堂讲稿。

图文校核是内容层面的估计，并未逐帧确认屏幕时间；用户在本机保存的校对会覆盖初始建议。来源、页码与作者标记保留在 slide 图片中，原始 PDF 可从阅读页打开。

## 构建与维护

```sh
python3 scripts/build_site.py
python3 scripts/build_sync_reader.py
python3 -m unittest discover -s tests -v
node --test tests/test_reader_js.mjs
```

`build_sync_reader.py` 只向 `docs/reader/mit-mmai-2026/` 添加页面、分讲 JSON 与图片，不写入其他网站文件。线上构建只需要 Python 标准库和已提交的 Markdown、关联数据及 WebP，无需下载模型或访问本地 `.work`。

重新生成关联可运行 `scripts/align_slides.py`；重新渲染 slides 使用 `scripts/render_reader_slides.py`，其离线预处理需已有 pypdfium2 与 Pillow。原始 PDF 与字幕缓存保存在本地 `.work`；关联 JSON 记录输入哈希，以发现过期的内容对应关系。

关联数据位于 `reader/mit-mmai-2026/alignments/`，有证据的图文修订位于 `alignment-review.json`。修改建议数据后重新打包即可；无需修改原始译稿。
