# LLM-as-a-Judge 论文调研

本目录包含对用户指定的 6 篇 LLM-as-a-Judge 相关论文（原始链接 7 条，2509.20293 重复，去重后 6 篇）的调研成果。

## 论文清单与逐篇总结

| # | arXiv ID | 标题 | 总结 |
|---|---|---|---|
| 1 | [2509.20293](https://arxiv.org/abs/2509.20293) | When Judgment Becomes Noise: How Design Failures in LLM Judge Benchmarks Silently Undermine Validity | [summaries/2509.20293.md](summaries/2509.20293.md) |
| 2 | [2406.13439](https://arxiv.org/abs/2406.13439) | Finding Blind Spots in Evaluator LLMs with Interpretable Checklists | [summaries/2406.13439.md](summaries/2406.13439.md) |
| 3 | [2402.10669](https://arxiv.org/abs/2402.10669) | Humans or LLMs as the Judge? A Study on Judgement Biases | [summaries/2402.10669.md](summaries/2402.10669.md) |
| 4 | [2506.13639](https://arxiv.org/abs/2506.13639) | An Empirical Study of LLM-as-a-Judge: How Design Choices Impact Evaluation Reliability | [summaries/2506.13639.md](summaries/2506.13639.md) |
| 5 | [2410.13341](https://arxiv.org/abs/2410.13341) | Limits to scalable evaluation at the frontier: LLM as Judge won't beat twice the data | [summaries/2410.13341.md](summaries/2410.13341.md) |
| 6 | [2503.05061](https://arxiv.org/abs/2503.05061) | No Free Labels: Limitations of LLM-as-a-Judge Without Human Grounding | [summaries/2503.05061.md](summaries/2503.05061.md) |

## 核心产出

- **综合调研报告（带逐条论文溯源）**：[report/LLM-as-a-Judge_综合调研报告.md](report/LLM-as-a-Judge_综合调研报告.md)
  - 第 1–5 章对应用户的 5 个问题（解决什么问题 / 实验范式与 Judge 工作方式 / 效果如何 / baseline / insight），每章均含 6 篇论文的整合结论与溯源
  - 第 6 章为论文定位矩阵，第 7 章为实践建议清单，第 8 章为溯源索引
- 每篇总结按统一模板撰写：0 基本信息 / 1 解决什么问题 / 2 方法·实验范式（LLM 如何作为 Judge）/ 3 效果如何（含具体数字与表号）/ 4 实验对比的 Baseline / 5 Insights / 6 溯源锚点 + 论文定位一句话

## 概念文档库（面向非专业读者）

报告与 6 份总结中出现的关键术语/指标（如 Cohen's κ、ASR、ELO、样本效率因子、各偏差等）均已加**链接**指向概念文档。库入口：[concepts/README.md](concepts/README.md)，共 **43 个文件**（索引 + 42 篇概念文档），按 A–G 七类组织：

- **A 框架与打分范式** | **B 一致性与对齐指标** | **C 偏差与攻击** | **D 基准诊断与统计** | **E 排名与评测机制** | **F 理论极限与去偏** | **G 替代评测方法与基准**

统一阅读结构：这是什么（定义）→ 通俗直觉 → 数值/结果怎么读 → 为什么重要（隐藏含义）→ 出现在哪些论文 → 相关概念（互链）。

## 目录结构

- `html/`：论文全文 HTML（arXiv 原生版）
- `text/`：HTML 转换后的纯文本（精读与溯源用）
- `summaries/`：逐篇结构化总结（6 份，已内嵌概念链接）
- `report/`：综合调研报告（已内嵌概念链接）
- `concepts/`：概念文档库（42 篇 + 索引）
- `convert.py`：HTML→文本转换脚本（可复现）
- `link_concepts.py`：术语→概念库链接注入脚本（可复现）
- `verify_links.py`：概念链接完整性校验脚本（可复现）

## 调研方法说明

1. 抓取 arXiv 摘要识别论文（去重后 6 篇唯一）
2. 下载全文并转纯文本（便于检索与引用锚点）
3. 每篇由独立子代理通读全文（含附录），按 5 个问题模板产出总结；关键数字另经 grep/HTML 原文核验（纯文本转换丢失的数值已从本地 HTML 恢复）
4. 综合报告由父代理整合撰写，所有论断标注 [arXiv编号 章节/表/图] 溯源
