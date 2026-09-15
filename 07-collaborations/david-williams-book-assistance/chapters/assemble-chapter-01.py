#!/usr/bin/env python3
"""Assemble Chapter 1 from the verified split Markdown artifacts.

Run from repository root:
  python 07-collaborations/david-williams-book-assistance/chapters/assemble-chapter-01.py

The script preserves the canonical opening, removes continuation metadata, repairs the
single truncation join, appends sections 7-19 and references, and overwrites the
canonical chapter. It aborts if the expected truncation markers are absent.
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parent
CANON = ROOT / "01-the-timing-problem.md"
A = ROOT / "01-the-timing-problem-continuation-a.md"
B = ROOT / "01-the-timing-problem-continuation-b.md"

canon = CANON.read_text(encoding="utf-8")
a = A.read_text(encoding="utf-8")
b = B.read_text(encoding="utf-8")

canon_tail = "If source rocks can be shown to expel the required volumes through late-stage"
a_marker = "late-stage mechanisms under conditions demonstrably comparable"
sec7 = "## 7. The Monterey Formation: An Independent Test Case"
sec11 = "## 11. Sand Injectites and Remobilized Sediment"

if not canon.rstrip().endswith(canon_tail):
    raise SystemExit("Canonical file no longer has the expected truncation tail; refusing to assemble.")
if a_marker not in a or sec7 not in a:
    raise SystemExit("Continuation A does not match expected structure.")
if sec11 not in b:
    raise SystemExit("Continuation B does not match expected structure.")

# A begins with continuation metadata. Keep only the prose beginning after the repeated
# phrase 'late-stage', because canonical already ends with that phrase.
a_body = a[a.index(a_marker) + len("late-stage "):]
# B begins with continuation metadata; Section 11 is the manuscript start point.
b_body = b[b.index(sec11):]

assembled = canon.rstrip() + " " + a_body.strip() + "\n\n" + b_body.strip() + "\n"

required = [
    "# Chapter 1: The Timing Problem",
    sec7,
    sec11,
    "## 19. Conclusion: Petroleum Systems Have Memory",
    "## References cited in Chapter 1 working draft",
    "Chapter 2 begins with the most immediate physical evidence",
]
for marker in required:
    if marker not in assembled:
        raise SystemExit(f"Missing required marker: {marker}")

for bad in ["# Chapter 1 Continuation A", "# Chapter 1 Continuation B", "Integration note:"]:
    if bad in assembled:
        raise SystemExit(f"Continuation artifact leaked into assembled manuscript: {bad}")

CANON.write_text(assembled, encoding="utf-8")
words = len(assembled.split())
print(f"assembled={CANON}")
print(f"words={words}")
print(f"characters={len(assembled)}")
print("integrity=PASS")
