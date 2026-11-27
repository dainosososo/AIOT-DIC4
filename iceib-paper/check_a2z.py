#!/usr/bin/env python3
"""Check iceib-paper/main.tex against the OpenSpec changes 000_abstract..006_references.

Usage:  python iceib-paper/check_a2z.py [iceib-paper/main.tex]

Exit codes
  0  structure OK and ready to submit
  1  structure problems (missing / out-of-order A2Z codes, wrong sections,
     citation mismatch, abstract too long, main.txt differs from main.tex,
     a number in Sec. IV that is not in the measured results JSON)
  2  structure OK, but submission blockers remain ([TBD] or author placeholders)
"""
import hashlib
import json
import re
import sys
from pathlib import Path

A2Z_ORDER = list("ABCDEFGHIJKLMNO") + ["P" + c for c in "ABCDEFGHIJKLM"] + list("QRSTUVWXYZ")
EXPECTED_SECTIONS = ["Introduction", "Related Work", "Proposed Design", "Experiment", "Conclusion"]
AUTHOR_PLACEHOLDERS = ["Author Name", "[University]", "[Department]", "[email address]", "[City]"]
ABSTRACT_MAX_WORDS = 250


def strip_comments(text):
    return "\n".join(re.sub(r"(?<!\\)%.*", "", line) for line in text.splitlines())


def abstract_words(body):
    m = re.search(r"\\begin\{abstract\}(.*?)\\end\{abstract\}", body, re.S)
    if not m:
        return -1
    t = re.sub(r"\\[a-zA-Z]+\*?(\[[^\]]*\])?", " ", m.group(1))
    t = re.sub(r"[{}$\\~]", " ", t)
    return len([w for w in t.split() if re.search(r"[A-Za-z0-9]", w)])


def measured_numbers(root):
    """All percentages / ms values that appear in the measured result files."""
    vals = set()
    for p in (root / "experiments").glob("results_real_eval*.json"):
        def walk(o):
            if isinstance(o, dict):
                for v in o.values():
                    walk(v)
            elif isinstance(o, list):
                for v in o:
                    walk(v)
            elif isinstance(o, (int, float)) and not isinstance(o, bool):
                vals.add(round(float(o), 1))
        walk(json.loads(p.read_text(encoding="utf-8")))
    return vals


def main():
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).with_name("main.tex")
    raw = path.read_text(encoding="utf-8")
    body = strip_comments(raw)
    problems, blockers = [], []

    found = re.findall(r"%\s*\[A2Z:([A-Z]{1,2})\]", raw)
    unknown = sorted({c for c in found if c not in A2Z_ORDER})
    if unknown:
        problems.append(f"unknown A2Z codes: {', '.join(unknown)}")
    missing = [c for c in A2Z_ORDER if c not in found]
    if missing:
        problems.append(f"missing A2Z codes: {', '.join(missing)}")
    first = []
    for c in found:
        if c in A2Z_ORDER and c not in first:
            first.append(c)
    if first != [c for c in A2Z_ORDER if c in first]:
        problems.append(f"A2Z codes out of order: {' '.join(first)}")

    sections = re.findall(r"\\section\{([^}]*)\}", body)
    if sections != EXPECTED_SECTIONS:
        problems.append(f"sections are {sections}, expected {EXPECTED_SECTIONS}")

    n = abstract_words(body)
    if n < 0:
        problems.append("no abstract environment")
    elif n > ABSTRACT_MAX_WORDS:
        problems.append(f"abstract has {n} words (max {ABSTRACT_MAX_WORDS})")

    cited = set()
    for group in re.findall(r"\\cite\{([^}]*)\}", body):
        cited.update(k.strip() for k in group.split(","))
    bib = set(re.findall(r"\\bibitem\{([^}]*)\}", body))
    if cited - bib:
        problems.append(f"\\cite without \\bibitem: {', '.join(sorted(cited - bib))}")
    if bib - cited:
        problems.append(f"\\bibitem never cited: {', '.join(sorted(bib - cited))}")

    # No fabricated metrics: every "xx.x" in the results table must be measured.
    root = path.resolve().parent.parent
    measured = measured_numbers(root)
    tab = re.search(r"\\label\{tab:results\}(.*?)\\end\{tabular\}", body, re.S)
    if tab and measured:
        for v in re.findall(r"(?<![\d.v])(\d+\.\d)(?![\d])", tab.group(1)):
            if round(float(v), 1) not in measured:
                problems.append(f"results table value {v} not found in experiments/results_real_eval*.json")

    twin = path.with_suffix(".txt")
    if twin.exists():
        same = hashlib.sha256(twin.read_bytes()).digest() == hashlib.sha256(path.read_bytes()).digest()
        twin_status = "identical" if same else "DIFFERENT"
        if not same:
            problems.append(f"{twin.name} differs from {path.name} (copy main.tex to main.txt)")
    else:
        twin_status = "missing"
        problems.append(f"{twin.name} is missing (copy main.tex to main.txt)")

    tbd = [i + 1 for i, l in enumerate(body.splitlines()) if ("\\TBD" in l or "[TBD]" in l) and "\\newcommand" not in l]
    if tbd:
        blockers.append(f"[TBD] on {len(tbd)} line(s): {tbd[:15]}")
    ph = [p for p in AUTHOR_PLACEHOLDERS if p in body]
    if ph:
        blockers.append(f"author placeholders remain: {', '.join(ph)}")

    print(f"Checked {path}")
    print(f"  A2Z codes found: {len(set(found) & set(A2Z_ORDER))}/{len(A2Z_ORDER)}")
    print(f"  sections: {sections}")
    print(f"  abstract words: {n}")
    print(f"  references: {len(bib)} bibitems, {len(cited)} cited keys")
    print(f"  main.txt vs main.tex (SHA-256): {twin_status}")
    for p in problems:
        print(f"STRUCTURE: {p}")
    for b in blockers:
        print(f"NOT READY TO SUBMIT: {b}")
    if problems:
        return 1
    if blockers:
        return 2
    print("OK: ready to submit")
    return 0


if __name__ == "__main__":
    sys.exit(main())
