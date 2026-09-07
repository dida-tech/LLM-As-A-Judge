# LLM-as-a-Judge 概念文档库

面向非专业读者的概念索引。每个重要评估指标/概念一篇文档，统一结构：**这是什么（定义）→ 通俗直觉 → 数值/结果怎么读 → 为什么重要（隐藏含义）→ 出现在哪些论文 → 相关概念**。

## A. 框架与打分范式
| 概念 | 文档 | 一句话 |
|---|---|---|
| LLM-as-a-Judge 框架 | [llm-as-a-judge.md](llm-as-a-judge.md) | 用强 LLM 当自动评估器的总框架 |
| 单答案评分 | [single-answer-grading.md](single-answer-grading.md) | 一个回答给 1–5 分 |
| 成对比较 | [pairwise-comparison.md](pairwise-comparison.md) | 两个回答选更优 |
| 参考引导评测（含参考类型） | [reference-guided-eval.md](reference-guided-eval.md) | 打参考答案让 judge 对照打分 |
| 评估标准（评估轴/分数描述） | [evaluation-criteria.md](evaluation-criteria.md) | 明确"按什么打分"的说明 |

## B. 一致性与对齐指标
| 概念 | 文档 | 一句话 |
|---|---|---|
| 相关系数（含与人类对齐） | [correlation-coefficient.md](correlation-coefficient.md) | judge 分数与人类分数是否同涨同跌 |
| Cohen's κ | [cohens-kappa.md](cohens-kappa.md) | 分类判断的一致率（扣除偶然一致） |
| Krippendorff's alpha | [krippendorff-alpha.md](krippendorff-alpha.md) | 多次评分之间的一致性（含随机对照） |
| 未检出率 | [undetected-rate.md](undetected-rate.md) | judge 漏掉质量下降的比例 |
| 攻击成功率（ASR） | [attack-success-rate.md](attack-success-rate.md) | 偏好被扰动带偏的比例，越高越易被骗 |
| Agreement 一致率 | [agreement.md](agreement.md) | judge 与人类"意见相同"的比例（注意其局限） |

## C. 偏差与攻击
| 概念 | 文档 | 一句话 |
|---|---|---|
| Judge 偏差总论 | [judge-bias.md](judge-bias.md) | judge 系统性偏好某类答案的总体概念 |
| 位置偏差 | [position-bias.md](position-bias.md) | 排在前面/后面的答案更受青睐 |
| 冗长/长度偏差 | [length-bias.md](length-bias.md) | 更长的答案更受青睐 |
| 自偏好偏差 | [self-preference-bias.md](self-preference-bias.md) | judge 偏爱自己生成的答案 |
| 权威偏差（假引用） | [authority-bias.md](authority-bias.md) | 引用/权威信号让人盲目相信 |
| 美学偏差（富格式） | [beauty-bias.md](beauty-bias.md) | emoji/排版等干扰注意力的信号 |
| 性别偏差 | [gender-bias.md](gender-bias.md) | 对性别相关内容的不公判断 |
| 错误信息监督偏差 | [misinformation-oversight-bias.md](misinformation-oversight-bias.md) | 对事实性错误视而不见 |
| Prompt 攻击 | [prompt-attack.md](prompt-attack.md) | 用提示词骗过 judge |
| 分数不变扰动（SI） | [score-invariant-perturbation.md](score-invariant-perturbation.md) | 不应影响分数却可能误导的扰动 |
| 扰动式元评测 | [perturbation-meta-evaluation.md](perturbation-meta-evaluation.md) | 用扰动检验 judge 敏感性的评测方法 |

## D. 基准诊断与统计
| 概念 | 文档 | 一句话 |
|---|---|---|
| 解释方差 R² | [explained-variance.md](explained-variance.md) | 打分能被已知因素解释的比例 |
| 模式遵循度 | [schematic-adherence.md](schematic-adherence.md) | judge 是否按自己写的 rubric 打分 |
| 因子分析与因子塌缩 | [factor-analysis.md](factor-analysis.md) | 多个维度是否真的相互独立 |
| 心理测量效度（α/CLR/HTMT） | [psychometric-validity.md](psychometric-validity.md) | 像检验问卷一样检验基准 |
| Bootstrap 置信区间 | [bootstrap-ci.md](bootstrap-ci.md) | 重抽样估计不确定性 |
| Bloom 认知分类学 | [bloom-taxonomy.md](bloom-taxonomy.md) | 按认知层次系统地出题 |

## E. 排名与评测机制
| 概念 | 文档 | 一句话 |
|---|---|---|
| ELO 评分与 Bradley-Terry | [elo-rating.md](elo-rating.md) | 用成对胜负算分数的排名方法 |
| Chain-of-Thought (CoT) | [chain-of-thought.md](chain-of-thought.md) | 先写推理再给结论 |
| 解码策略（greedy/采样/聚合） | [decoding-strategies.md](decoding-strategies.md) | 生成分数答案时的随机性与聚合 |
| 自一致性 | [self-consistency.md](self-consistency.md) | 多次采样多数投票 |
| 真值标签 vs 代理标签 | [ground-truth-and-proxy.md](ground-truth-and-proxy.md) | 人类标注与模型判断的关系 |

## F. 理论极限与去偏
| 概念 | 文档 | 一句话 |
|---|---|---|
| 样本效率因子 τ | [sample-efficiency-factor.md](sample-efficiency-factor.md) | 去偏后标注需求缩小几倍 |
| PPI（Prediction-Powered Inference） | [prediction-powered-inference.md](prediction-powered-inference.md) | 用模型预测增强小样本统计 |
| 去偏方法 | [debiasing.md](debiasing.md) | 矫正 judge 系统偏差的手段 |
| Cramér-Rao 界 | [cramer-rao-bound.md](cramer-rao-bound.md) | 无偏估计器精度的理论下限 |

## G. 替代评测方法与基准
| 概念 | 文档 | 一句话 |
|---|---|---|
| 传统自动指标（BLEU/ROUGE 等） | [traditional-auto-metrics.md](traditional-auto-metrics.md) | 词面重叠类打分 |
| 奖励模型 | [reward-model.md](reward-model.md) | 训练出来的质量打分器 |
| 嵌入相似度 | [embedding-similarity.md](embedding-similarity.md) | 向量空间里的语义相似度 |
| 主流 LLM 评测基准 | [llm-evaluation-benchmarks.md](llm-evaluation-benchmarks.md) | MT-Bench/Arena-Hard/MMLU 等是什么 |
| 参考质量 | [reference-quality.md](reference-quality.md) | 参考答案本身的对错与好坏 |

> 用法：在报告/总结中看到加粗或陌生的术语，点击链接跳到对应文档。文档间通过"相关概念"互相引用。
