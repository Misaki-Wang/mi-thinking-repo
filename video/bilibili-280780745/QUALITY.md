# 转写与质量记录

本次快照包含 10 期，参考音频合计 29:32:29。保留 1,786 个原始识别片段，整理为 1,784 个阅读段落。

完整指所选音频均经过识别、所有输出片段保留；不代表每个发音都被正确识别。全文未逐句人工校对。中英混合术语、人名、数字、重复和静音幻觉仍需结合原视频确认。

| 视频 | ASR 模型 | 阅读段落 | 自动提示 |
| --- | --- | ---: | ---: |
| [BV1XNtJ6UEmm](BV1XNtJ6UEmm/transcript.zh-CN.md) | Qwen/Qwen3-ASR-1.7B | 154 | 81 |
| [BV1KZ8X6uEPL](BV1KZ8X6uEPL/transcript.zh-CN.md) | Qwen/Qwen3-ASR-1.7B | 125 | 65 |
| [BV1fmgj66EtD](BV1fmgj66EtD/transcript.zh-CN.md) | Qwen/Qwen3-ASR-1.7B | 218 | 98 |
| [BV18Qg96YE1W](BV18Qg96YE1W/transcript.zh-CN.md) | Qwen/Qwen3-ASR-1.7B | 181 | 80 |
| [BV1nB3u6tERu](BV1nB3u6tERu/transcript.zh-CN.md) | Qwen/Qwen3-ASR-1.7B | 285 | 80 |
| [BV1cRK86zEpQ](BV1cRK86zEpQ/transcript.zh-CN.md) | Qwen/Qwen3-ASR-1.7B | 110 | 66 |
| [BV12bNB6vEtt](BV12bNB6vEtt/transcript.zh-CN.md) | Qwen/Qwen3-ASR-1.7B | 225 | 129 |
| [BV1HfEy6jEUx](BV1HfEy6jEUx/transcript.zh-CN.md) | Qwen/Qwen3-ASR-1.7B | 181 | 98 |
| [BV1dyE86bENz](BV1dyE86bENz/transcript.zh-CN.md) | Qwen/Qwen3-ASR-1.7B | 218 | 106 |
| [BV1d4GU6wEDo](BV1d4GU6wEDo/transcript.zh-CN.md) | Qwen/Qwen3-ASR-1.7B | 87 | 44 |

## 可追溯与公开范围

- 自动提示包括低能量分块稍长于 60 秒的边界记录，不是已确认错误的总数。
- 时间定位方式记录在各稿与 manifest 中；audio_chunk 表示连续音频分块起点，不是逐字强制对齐。
- 每段时间戳可跳回原视频；未猜测发言者身份，未把弹幕当字幕。
- 音频、原始 ASR JSON、模型日志与逐段检查记录保留本地，不上传 GitHub。
- 仓库 manifest.json 记录 Markdown、原始 ASR 与音频的 SHA-256，网站只发布经校验的讲稿。
- 发布依据：用户于 2026-09-10 明确确认已获得授权，可发布完整讲稿。原作者与原视频链接保留。
- 时间戳覆盖率及自动提示数量都不是准确率；未进行人工标注的 WER/CER 评估。

[可复用工具链与运行说明](https://github.com/Misaki-Wang/mi-thinking-repo/blob/main/scripts/BILIBILI_WORKFLOW.md)
