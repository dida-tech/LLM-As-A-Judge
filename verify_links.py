#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import glob, os
BASE = "/home/da/workspace/papers/LLM-As-A-Judge"
# docs: report + summaries + concepts (all md under report/, summaries/, concepts/)
files = glob.glob(os.path.join(BASE, "report", "*.md")) +         glob.glob(os.path.join(BASE, "summaries", "*.md")) +         glob.glob(os.path.join(BASE, "concepts", "*.md"))
missing, total = [], 0
for p in files:
    txt = open(p, encoding="utf-8").read()
    n = txt.count("../concepts/") + txt.count("](concepts/")
    total += n
    for marker in ("../concepts/", "concepts/"):
        pos = 0
        while True:
            j = txt.find(marker, pos)
            if j < 0:
                break
            # only treat as link-like if preceded by ']('
            if j >= 2 and txt[j-2:j] == "](":
                k = txt.find(")", j)
                if k < 0:
                    missing.append((os.path.relpath(p, BASE), txt[j:j+40])); break
                rel = txt[j + len(marker):k]
                tgt = os.path.join(BASE, "concepts", rel)
                if not os.path.exists(tgt):
                    missing.append((os.path.relpath(p, BASE), rel))
                pos = k + 1
            else:
                pos = j + 1
    print(os.path.relpath(p, BASE), "->", n, "concept refs")
print("TOTAL refs:", total)
print("MISSING:", missing if missing else "NONE")
