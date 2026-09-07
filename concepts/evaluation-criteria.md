# 评估标准（Evaluation Criteria：评估轴与分数描述）

## 这是什么（定义）
写给 judge 的"评分依据"，由两部分组成：
- **评估轴（evaluation axes）**：要考察哪些维度，如正确性（correctness）、完整性（completeness）、安全性（safety）、简洁性（conciseness）、风格（style）。
- **分数描述（score descriptions）**：每个分数档（如 1–5 分）分别代表什么水平，如"5 分=完全正确且完整，1 分=重大错误"。

## 通俗直觉
"按什么标准打分、几分对应什么水平"——相当于给 judge 的阅卷细则。没有细则，judge 只能凭感觉。

## 数值/结果怎么读
- 去掉评估标准，GPT-4o 与人类相关从 0.666 跌到 0.591；去掉参考只跌到 0.638——**标准的权重 > 参考**（[2506.13639] Table 1）。
- 只保留 1 分和 5 分的描述、去掉中间档描述，效果与全量描述几乎相同（[2506.13639] Figure 2）——中间分数描述的必要性存疑。
- EvalBiasBench 上去掉标准会明显伤一致性（α 0.865→0.839）：**对"应该惩罚有偏回答"的显式标准是稳定打分的必要条件**（[2506.13639] Table 1）。

## 为什么重要（隐藏含义）
- 定义了标准 ≠ judge 会执行标准：Arena-Hard Auto 上 judge 的总体判定很大比例无法由其 5 个评估轴的打分解释（[未解释方差](explained-variance.md) 最高 90%），说明 judge"嘴上答应、实际不照做"（[2509.20293] Table 1；[模式遵循度](schematic-adherence.md)）。
- 标准之间的关系：5 个评估轴得分高度相关（>0.93），几乎可以互相代替（[因子塌缩](factor-analysis.md)）——"多维评估"常常是"单维评估"换了说法。
- Safe/安全轴被系统性忽略，偏差率最高达 33%–40%（[2509.20293] Table 5）。

## 出现在哪些论文
[2506.13639]（核心自变量）、[2509.20293]（评估轴诊断）、[2406.13439]（Rubric/Axis 策略）。

## 相关概念
[单答案评分](single-answer-grading.md) · [模式遵循度](schematic-adherence.md) · [因子分析](factor-analysis.md) · [参考引导评测](reference-guided-eval.md)
