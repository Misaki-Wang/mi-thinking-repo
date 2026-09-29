# Lecture 4 · 补充阅读：预训练、系统与 parameter-efficient tuning

slides 引用这些论文来讲 compute/data scaling、显存和 attention IO。

## 建议顺序

1. [Scaling Laws for Neural Language Models](https://arxiv.org/abs/2001.08361) · Kaplan et al., 2020；[Training Compute-Optimal Large Language Models](https://arxiv.org/abs/2203.15556) · Hoffmann et al., 2022。对比 compute allocation 的问题设定和结论，不把经验 scaling law 当作普遍定理。
2. [ZeRO: Memory Optimizations Toward Training Trillion Parameter Models](https://arxiv.org/abs/1910.02054) · Rajbhandari et al., 2019。对应 data parallelism 章节，逐项追踪 optimizer states、gradients 与 parameters 的切分。
3. [FlashAttention: Fast and Memory-Efficient Exact Attention with IO-Awareness](https://arxiv.org/abs/2205.14135) · Dao et al., 2022。配合 slides 45–71 看 tiling、HBM/SRAM 与 forward/backward 重计算。
4. [LoRA](https://arxiv.org/abs/2106.09685) · Hu et al., 2021；进阶可读 [QLoRA](https://arxiv.org/abs/2305.14314) · Dettmers et al., 2023。对照训练参数量、显存占用与低秩更新的假设。

## 读后检查

把 data parallelism、ZeRO、model parallelism、FlashAttention、LoRA 放入“减少复制 / 切分模型 / 降低 IO / 减少可训练参数”等机制表，逐项定位它们优化训练流程的哪一环。
