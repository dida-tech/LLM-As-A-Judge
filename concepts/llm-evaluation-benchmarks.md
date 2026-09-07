# 主流 LLM 评测基准（Benchmarks 速查）

## 这是什么（定义）
评估 LLM 的标准考试集。本调研涉及的基准分两类：

**开放式/偏好类（依赖 LLM judge）**：
- **MT-Bench**：80 个多轮聊天问题，人类或 LLM 按 1–10 单答案评分；[2503.05061] 用其数学/推理子集并修正出 (C)MT-Bench。
- **Chatbot Arena / Arena-Hard**：众包或过滤后的真实用户请求，成对比较 → [ELO](elo-rating.md) 榜单；Arena-Hard Auto 是自动化版本（[2509.20293] 的分析对象）。
- **AlpacaEval 2.0**：成对比较 + 长度控制（防 [冗长偏差](length-bias.md)）。
- **BIGGEN-Bench**：9 类开放式任务，每实例含人工细粒度评分准则（[2506.13639] 用）。
- **EvalBiasBench / OffsetBias**：指令跟随+设计"正确 vs 有偏"对照，测 judge 对偏差内容的一致性（[2506.13639] 用）。

**封闭/知识类（标准答案，不依赖 judge）**：
- **MMLU / TruthfulQA**：多选题/判断题，有确定答案（[2410.13341] 的实验场地）；TruthfulQA 评"事实真实性"。
- **BFF-Bench**：本调研新增——160 道金融/商业难题，专家手写参考（[2503.05061]）。

## 数值/结果怎么读
- 基准的选择决定了结论的适用范围：**在 MMLU 这类闭卷题上 judge 很可靠（标准答案驱动），在 Arena-Hard 这类开放题上误差巨大**（[2509.20293]）。
- 参考质量是隐藏变量：MT-Bench 官方参考答案 **37.5% 有错**（[2503.05061] §3.2）——在错误的参考上训练评测，等于用错标准答案。
- 排名类榜单慎读：它们把噪声通过 [ELO](elo-rating.md) 变成高置信数字。

## 为什么重要（隐藏含义）
- "模型 A 在 Arena-Hard 上第 1" 这句话的可靠性，取决于基准的 judge、参考、聚合三层质量——读榜单时先问这三层。
- 评测结论**永远标注了边界条件**（什么题、什么 judge、什么参考）；跨越边界外推是非专业的表现。

## 出现在哪些论文
六篇全部（[2506.13639] 用 BIGGEN/EvalBias；[2503.05061] 造 BFF-Bench；(C)MT-Bench；[2410.13341] 用 MMLU/MT-Bench/TruthfulQA；[2509.20293] 用 Arena-Hard Auto；[2402.10669] 自造 Bloom 题库）。

## 相关概念
[LLM-as-a-Judge](llm-as-a-judge.md) · [ELO 评分](elo-rating.md) · [参考质量](reference-quality.md) · [Bloom 分类学](bloom-taxonomy.md)
