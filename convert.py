#!/usr/bin/env python3
# Convert arXiv native HTML to readable plain text: strip tags, keep structure.
import html, re, sys, os
from html.parser import HTMLParser

class TextExtractor(HTMLParser):
    def __init__(self):
        super().__init__()
        self.parts = []
        self.skip = 0
    def handle_starttag(self, tag, attrs):
        if tag in ('script','style','svg','math','nav','header','footer','button','form'):
            self.skip += 1
        if tag in ('h1','h2','h3','h4','h5','p','div','section','article','li','tr','br','figcaption','table','ul','ol'):
            self.parts.append('\n')
        if tag in ('td','th'):
            self.parts.append(' | ')
    def handle_endtag(self, tag):
        if tag in ('script','style','svg','math','nav','header','footer','button','form'):
            self.skip = max(0, self.skip-1)
        if tag in ('h1','h2','h3','h4','h5','p','div','section','li','tr','figcaption','table','ul','ol'):
            self.parts.append('\n')
    def handle_data(self, data):
        if self.skip == 0:
            self.parts.append(data)

def convert(path_in, path_out):
    raw = open(path_in, encoding='utf-8', errors='replace').read()
    m = re.search(r'<h1', raw)
    if m:
        raw = raw[m.start():]
    m2 = re.search(r'</article>|</main>', raw)
    if m2:
        raw = raw[:m2.end()]
    p = TextExtractor()
    p.feed(raw)
    text = ''.join(p.parts)
    text = re.sub(r'\n{3,}', '\n\n', text)
    text = text.replace('\u00a0', ' ')
    lines = []
    for l in text.split('\n'):
        l = l.rstrip()
        if l.strip() == '':
            if lines and lines[-1] != '':
                lines.append('')
        else:
            lines.append(l)
    open(path_out, 'w', encoding='utf-8').write('\n'.join(lines))

if __name__ == '__main__':
    ids = sys.argv[1:]
    for pid in ids:
        src = f"/home/da/workspace/papers/LLM-As-A-Judge/html/{pid}_native.html"
        dst = f"/home/da/workspace/papers/LLM-As-A-Judge/text/{pid}.txt"
        os.makedirs(os.path.dirname(dst), exist_ok=True)
        if os.path.exists(src):
            convert(src, dst)
            print(f"{pid}: {os.path.getsize(dst)} bytes")
        else:
            print(f"{pid}: missing source")
