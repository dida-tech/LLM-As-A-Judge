#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Insert concept-library markdown links into report & summaries.
- Single-pass regex alternation (longest-first) => no nested links.
- Existing markdown links/code spans protected via placeholders.
- Heading lines ('#...') skipped to keep outlines clean."""

import re, os, sys

BASE = "/home/da/workspace/papers/LLM-As-A-Judge"

TERMS = [
    ("LLM-as-a-Judge", "llm-as-a-judge.md"),
    ("Single Answer Grading", "single-answer-grading.md"),
    ("单答案评分", "single-answer-grading.md"),
    ("成对比较", "pairwise-comparison.md"),
    ("pairwise", "pairwise-comparison.md"),
    ("单答案/成对/参考式", "reference-guided-eval.md"),
    ("参考引导", "reference-guided-eval.md"),
    ("gold reference", "reference-quality.md"),
    ("Wrong reference", "reference-quality.md"),
    ("Human reference", "reference-quality.md"),
    ("Self reference", "reference-quality.md"),
    ("参考质量", "reference-quality.md"),
    ("参考答案", "reference-quality.md"),
    ("评分描述", "evaluation-criteria.md"),
    ("评估轴", "evaluation-criteria.md"),
    ("评估标准", "evaluation-criteria.md"),
    ("Pearson", "correlation-coefficient.md"),
    ("Spearman", "correlation-coefficient.md"),
    ("相关系数", "correlation-coefficient.md"),
    ("与人类对齐", "correlation-coefficient.md"),
    ("Cohen's kappa", "cohens-kappa.md"),
    ("Cohen's Kappa", "cohens-kappa.md"),
    ("Cohen's κ", "cohens-kappa.md"),
    ("κ", "cohens-kappa.md"),
    ("Krippendorff's alpha", "krippendorff-alpha.md"),
    ("Krippendorff", "krippendorff-alpha.md"),
    ("未检出率", "undetected-rate.md"),
    ("Agreement", "agreement.md"),
    ("位置偏差", "position-bias.md"),
    ("冗长偏差", "length-bias.md"),
    ("长度偏差", "length-bias.md"),
    ("Length", "length-bias.md"),
    ("自偏好偏差", "self-preference-bias.md"),
    ("自偏好", "self-preference-bias.md"),
    ("self-preference", "self-preference-bias.md"),
    ("权威偏差", "authority-bias.md"),
    ("Authority", "authority-bias.md"),
    ("美学偏差", "beauty-bias.md"),
    ("富格式", "beauty-bias.md"),
    ("rich content", "beauty-bias.md"),
    ("Beauty", "beauty-bias.md"),
    ("性别偏差", "gender-bias.md"),
    ("Gender", "gender-bias.md"),
    ("错误信息监督偏差", "misinformation-oversight-bias.md"),
    ("Misinformation Oversight", "misinformation-oversight-bias.md"),
    ("Prompt 攻击", "prompt-attack.md"),
    ("prompt 攻击", "prompt-attack.md"),
    ("分数不变", "score-invariant-perturbation.md"),
    ("Score-Invariant", "score-invariant-perturbation.md"),
    ("score-invariant", "score-invariant-perturbation.md"),
    ("SI", "score-invariant-perturbation.md"),
    ("FBI", "perturbation-meta-evaluation.md"),
    ("干预实验", "perturbation-meta-evaluation.md"),
    ("R²", "explained-variance.md"),
    ("未解释方差", "explained-variance.md"),
    ("解释方差", "explained-variance.md"),
    ("schematic adherence", "schematic-adherence.md"),
    ("模式遵循度", "schematic-adherence.md"),
    ("因子塌缩", "factor-analysis.md"),
    ("因子分析", "factor-analysis.md"),
    ("Factor", "factor-analysis.md"),
    ("psychometric validity", "psychometric-validity.md"),
    ("心理测量效度", "psychometric-validity.md"),
    ("Cronbach", "psychometric-validity.md"),
    ("HTMT", "psychometric-validity.md"),
    ("CLR", "psychometric-validity.md"),
    ("bootstrap", "bootstrap-ci.md"),
    ("Bootstrap", "bootstrap-ci.md"),
    ("Bloom", "bloom-taxonomy.md"),
    ("ELO", "elo-rating.md"),
    ("Bradley", "elo-rating.md"),
    ("传递性", "elo-rating.md"),
    ("Chain-of-Thought", "chain-of-thought.md"),
    ("Chain of Thought", "chain-of-thought.md"),
    ("CoT", "chain-of-thought.md"),
    ("greedy", "decoding-strategies.md"),
    ("Greedy", "decoding-strategies.md"),
    ("解码策略", "decoding-strategies.md"),
    ("解码", "decoding-strategies.md"),
    ("self-consistency", "self-consistency.md"),
    ("自一致性", "self-consistency.md"),
    ("ground-truth", "ground-truth-and-proxy.md"),
    ("ground truth", "ground-truth-and-proxy.md"),
    ("真值标注", "ground-truth-and-proxy.md"),
    ("真值标签", "ground-truth-and-proxy.md"),
    ("样本效率因子", "sample-efficiency-factor.md"),
    ("sample efficiency factor", "sample-efficiency-factor.md"),
    ("τ", "sample-efficiency-factor.md"),
    ("Attack Successful Rate", "attack-success-rate.md"),
    ("ASR", "attack-success-rate.md"),
    ("PPI", "prediction-powered-inference.md"),
    ("去偏方法", "debiasing.md"),
    ("去偏", "debiasing.md"),
    ("debiasing", "debiasing.md"),
    ("Cramér-Rao", "cramer-rao-bound.md"),
    ("BLEU", "traditional-auto-metrics.md"),
    ("ROUGE", "traditional-auto-metrics.md"),
    ("METEOR", "traditional-auto-metrics.md"),
    ("BERTScore", "traditional-auto-metrics.md"),
    ("奖励模型", "reward-model.md"),
    ("reward model", "reward-model.md"),
    ("嵌入相似度", "embedding-similarity.md"),
    ("embedding models", "embedding-similarity.md"),
    ("余弦相似度", "embedding-similarity.md"),
    ("(C)MT-Bench", "llm-evaluation-benchmarks.md"),
    ("MT-Bench", "llm-evaluation-benchmarks.md"),
    ("Arena-Hard Auto", "llm-evaluation-benchmarks.md"),
    ("Arena-Hard", "llm-evaluation-benchmarks.md"),
    ("Chatbot Arena", "llm-evaluation-benchmarks.md"),
    ("AlpacaEval", "llm-evaluation-benchmarks.md"),
    ("MMLU", "llm-evaluation-benchmarks.md"),
    ("TruthfulQA", "llm-evaluation-benchmarks.md"),
    ("BIGGEN-Bench", "llm-evaluation-benchmarks.md"),
    ("EvalBiasBench", "llm-evaluation-benchmarks.md"),
    ("BFF-Bench", "llm-evaluation-benchmarks.md"),
]

TERMS.sort(key=lambda t: len(t[0]), reverse=True)
PATTERN = re.compile("|".join(re.escape(t) for t, _ in TERMS))
TERM_MAP = {t: r for t, r in TERMS}

LINK_OR_CODE = re.compile("\\[[^\\]]*\\]\\([^)]*\\)|" + chr(96) + "[^" + chr(96) + "]*" + chr(96))

def protect(line):
    subs = {}
    def rep(m):
        key = "\x00%d\x00" % len(subs)
        subs[key] = m.group(0)
        return key
    return LINK_OR_CODE.sub(rep, line), subs

def link_line(line):
    line, subs = protect(line)
    def cb(m):
        return "[%s](../concepts/%s)" % (m.group(0), TERM_MAP[m.group(0)])
    line = PATTERN.sub(cb, line)
    for k, v in subs.items():
        line = line.replace(k, v)
    return line

def link_text(text):
    out = []
    for line in text.split("\n"):
        if line.lstrip().startswith("#"):
            out.append(line)
        else:
            out.append(link_line(line))
    return "\n".join(out)

def main():
    total = 0
    for t in sys.argv[1:]:
        p = os.path.join(BASE, t)
        if not os.path.exists(p):
            print("MISSING:", p); continue
        txt = open(p, encoding="utf-8").read()
        new = link_text(txt)
        n = new.count("../concepts/")
        open(p, "w", encoding="utf-8").write(new)
        total += n
        print("%s: +%d concept links (%d -> %d bytes)" % (t, n, len(txt), len(new)))
    print("TOTAL links:", total)

if __name__ == "__main__":
    main()
