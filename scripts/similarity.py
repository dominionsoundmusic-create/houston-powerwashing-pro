#!/usr/bin/env python3
"""Similarity check across pages of the same type.

Compares only the page-specific content (the data-content block plus the FAQ answers),
not the shared header, form or footer. Reports:
  - any run of RUN or more identical consecutive words shared by two pages of the same type
  - the share of 8-word shingles two pages have in common

Usage: python3 scripts/similarity.py [--dist DIR] [--run 12]
Exit code 1 if any pair shares a long run or more than 12% of shingles.
"""
import argparse
import re
import sys
from html import unescape
from itertools import combinations
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
GROUPS = {"service": "services", "guide": "guides", "city": "service-areas"}


def content_words(raw):
    m = re.search(r'<div class="page-content"[^>]*>(.*?)<section class="band band--navy cta"', raw, re.S)
    chunk = m.group(1) if m else raw
    chunk = re.sub(r"<!--.*?-->", " ", chunk, flags=re.S)
    chunk = re.sub(r'<aside class="sources".*?</aside>', " ", chunk, flags=re.S)
    chunk = re.sub(r'<ul class="pill-list">.*?</ul>', " ", chunk, flags=re.S)
    chunk = re.sub(r'<div class="cards">.*?</div>\s*</article>\s*</div>', " ", chunk, flags=re.S)
    chunk = re.sub(r'<div class="note">\s*<p><strong>How this line works.*?</div>', " ", chunk, flags=re.S)
    chunk = re.sub(r'<ol class="how-strip">.*?</ol>', " ", chunk, flags=re.S)
    chunk = re.sub(r'<div class="note note--amber">.*?</div>', " ", chunk, flags=re.S)
    text = unescape(re.sub(r"<[^>]+>", " ", chunk))
    return re.findall(r"[a-z0-9']+", text.lower())


def longest_common_run(a, b):
    """Longest run of identical consecutive words (dynamic programming on word lists)."""
    best, best_end = 0, 0
    prev = [0] * (len(b) + 1)
    for i in range(1, len(a) + 1):
        cur = [0] * (len(b) + 1)
        ai = a[i - 1]
        for j in range(1, len(b) + 1):
            if ai == b[j - 1]:
                cur[j] = prev[j - 1] + 1
                if cur[j] > best:
                    best, best_end = cur[j], i
        prev = cur
    return best, " ".join(a[best_end - best:best_end])


def shingles(words, n=8):
    return {" ".join(words[i:i + n]) for i in range(len(words) - n + 1)}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dist", default=str(ROOT / "dist"))
    ap.add_argument("--run", type=int, default=12)
    args = ap.parse_args()
    dist = Path(args.dist)
    bad = 0
    for kind, folder in GROUPS.items():
        pages = {}
        for f in sorted((dist / folder).glob("*/index.html")):
            pages[f.parent.name] = content_words(f.read_text())
        print(f"\n== {kind} pages ({len(pages)}) ==")
        for (a, wa), (b, wb) in combinations(pages.items(), 2):
            run, phrase = longest_common_run(wa, wb)
            sa, sb = shingles(wa), shingles(wb)
            overlap = len(sa & sb) / max(1, min(len(sa), len(sb)))
            flag = run >= args.run or overlap > 0.12
            if flag:
                bad += 1
                print(f"FLAG {a} vs {b}: longest shared run {run} words, shingle overlap {overlap:.1%}")
                print(f"     \"{phrase[:160]}\"")
        words = {k: len(v) for k, v in pages.items()}
        print("unique-content words:", words)
    print(f"\n{bad} flagged pairs")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
