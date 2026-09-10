# Bilibili → Markdown → 学习网站

本流程只处理明确选定、可正常访问的视频。完整讲稿发布需要对本次清单单独确认授权；公开视频、可下载音频、弹幕均不等于再发布许可。禁止把弹幕作为讲稿来源。

网站构建仍然只需要 Python 标准库。采集与模型识别在独立工具环境运行，不给网站添加模型依赖。

## 1. 固定目录快照

在安装了 [yt-dlp](https://github.com/yt-dlp/yt-dlp) 的独立 Python 环境运行：

```sh
python scripts/bilibili_inventory.py --uid 280780745 --sample BV1KZ8X6uEPL --limit 10
```

默认私密工作目录为 `.work/bilibili-280780745/`。保留获取时间、BVID/CID、作者、发布时间、时长及来源，不把历史快照称作持续更新的“最新”。遇到登录或平台访问限制时保留失败状态，不导入浏览器凭据或绕过访问限制。

## 2. 获取音频与校验

```sh
python scripts/download_bilibili_audio.py --sample-only
python scripts/download_bilibili_audio.py --remaining-only
```

需要 `ffprobe`。默认 `bestaudio`，最多两路并发，先检查样本。不同音轨必须使用不同输出目录，例如：

```sh
python scripts/download_bilibili_audio.py --format 30216 --output-root .work/bilibili-280780745/audio30216
```

`30216` 是 Bilibili 返回的另一条原始 AAC 音轨，不是本工具二次压缩。不同格式的 SHA-256 不可混用。下载完成后检查纯音频、时长、大小及哈希；远端推理时再次核对实际输入。CDN 地址来自服务响应，具有时效性，不写进公开仓库，也不手动修改签名。

## 3. ASR 与原始记录

先检查空闲 GPU，再解码为 16 kHz mono PCM。模型、缓存、临时文件均放在本任务隔离目录。H200 无法连接时，可使用实际检查为空闲的 A800；0% utilization 并不等于显存空闲。

保留实际模型、版本、音轨哈希、处理区间与原始输出。Whisper JSON 可直接渲染；其他 ASR 必须无损转换为以下结构，不能编造 Whisper 的置信指标：

```json
{"language":"zh","model":"actual-model-name","text":"全部识别文字","segments":[{"id":0,"start":0.0,"end":30.0,"text":"原始识别片段"}]}
```

如果 `start/end` 是音频切块边界而不是强制对齐结果，必须明确写入时间精度说明。保存全部片段，包括空片段、疑似重复及无法确认的术语；不得用推测的发言者身份或语言模型续写补齐音频。

本次提供的 [transcribe_qwen_audio.py](transcribe_qwen_audio.py) 使用 [Qwen3-ASR](https://github.com/QwenLM/Qwen3-ASR) 官方 Transformers 后端与本地下载的 `Qwen/Qwen3-ASR-1.7B`。它不联网下载模型，不负责选择空闲 GPU。调用者需先用 ffmpeg 解码并核对音频 SHA-256、测量时长，再通过 `--input`、`--model`、`--gpu`、`--source-sha256`、`--expected-duration`、`--output-dir` 传入；完整参数见 `python3 scripts/transcribe_qwen_audio.py --help`。

该实现按约 60 秒的低能量边界连续切块，保留真实起止位置与末尾补零记录；默认最多 8 个片段同批识别，4096 new tokens 上限，检查每个输出的 EOS。未正常结束的片段缩短后有限重试，失败记录保留，最终分块必须恰好覆盖全部输入且不重叠、不漏段。没有使用术语长词表 prompt：短片段试验显示它既能修正拼写，也可能改变说话者实际说出的名称。输出中的 `timestamp_kind: audio_chunk` 使公开讲稿明确标注非逐字对齐。

## 4. 渲染、检查、导出

```sh
python3 scripts/render_bilibili_transcripts.py --model turbo --provider openai-whisper
```

这只是 Whisper 的参数示例。使用其他引擎时，必须传实际 `--provider`、`--model`、`--asr-root` 和 `--audio-root`；测量时长可针对单一 `--bvid` 用 `--audio-duration` 传入。默认输入为私密 `asr/BVID/source.json`，输出为 `transcripts/BVID/` 中的 Markdown、原文段落 JSON 和校验记录。

模型比较应使用同一音频片段，并区分“模型间文字一致度”与有人工真值的准确率。自动规则能查出丢段、时间回退、重复等问题，不能证明专业术语完全正确。

授权记录放在私密工作目录，包含 `confirmed: true`、`confirmed_at`、原始确认 `statement`、`uploader_id`，以及与目录顺序一致的完整 `bvids` 清单。只有已有真实确认才创建该记录。导出命令：

```sh
python3 scripts/export_bilibili_transcripts.py --authorization .work/bilibili-280780745/publication-authorization.json
python3 -m unittest discover -s tests -v
node --test tests/test_reader_js.mjs
python3 scripts/build_site.py --base /mi-thinking-repo/
python3 scripts/build_sync_reader.py
```

导出器在写文件前检查全清单授权、作者、原始片段逐字核对、渲染文件哈希及重新渲染结果。网站再次核对授权与每份 Markdown 的 SHA-256。仅公开允许的 Markdown 与来源清单，原音频、原始模型输出、日志和临时下载地址留在 `.work/`。

推送 `main` 后由现有 GitHub Pages 工作流发布；最后检查线上目录、讲稿、Markdown 下载、搜索与手机布局，不能只凭本地文件存在宣称发布成功。
