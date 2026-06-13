#!/usr/bin/env python3
"""
Surgically enrich HIP DOC.md entries that have stub descriptions or are
functions missing a signature, pulling authoritative content from the HIP
Doxygen pages.

Unlike a full ``scrape_hip_api.py`` run (which regenerates every file and would
clobber curated entries), this script only touches docs whose description is a
generic stub, or functions that lack a ``## Signature`` block. Everything else
is left byte-for-byte unchanged. Safe to re-run (idempotent).

Usage:
    python3 enrich_hip_gaps.py                 # apply
    python3 enrich_hip_gaps.py --dry-run       # report only
"""

from __future__ import annotations

import argparse
import re
from pathlib import Path

from scrape_hip_api import fetch_url, MODULES, parse_api_page

DOCS_DIR = Path(__file__).resolve().parents[2] / "content" / "rocm" / "docs"
BASE = "https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html"

# A description is a "stub" if it is the scraper's generic fallback rather than
# real prose pulled from the docs.
STUB_RE = re.compile(
    r"^(HIP API:|.*HIP Runtime API function\.?$)", re.IGNORECASE
)


def build_index() -> dict:
    index: dict[str, dict] = {}
    for path, _name in MODULES:
        try:
            html = fetch_url(f"{BASE}/{path}")
        except Exception as exc:  # noqa: BLE001 - best-effort scrape
            print(f"  WARN fetch {path}: {exc}")
            continue
        for func in parse_api_page(html):
            if func["name"] in index:
                continue
            if func["description"] or func["signature"]:
                index[func["name"]] = func
    return index


def build_sections(func: dict, body: str) -> str:
    """Return markdown for Signature/Parameters/Returns not already present."""
    out = ""
    if func.get("signature") and "## Signature" not in body:
        out += f"\n## Signature\n\n```c\n{func['signature']};\n```\n"
    if func.get("params") and "## Parameters" not in body:
        out += "\n## Parameters\n\n| Direction | Parameter | Description |\n"
        out += "|-----------|-----------|-------------|\n"
        for p in func["params"]:
            out += f"| {p.get('direction', '')} | `{p['name']}` | {p.get('desc', '')} |\n"
    if func.get("return_desc") and "## Returns" not in body:
        out += f"\n## Returns\n\n{func['return_desc']}\n"
    return out


def enrich_doc(path: Path, func: dict) -> bool:
    text = path.read_text(encoding="utf-8")
    m = re.match(r"^(---\n.*?\n---\n)(.*)$", text, re.DOTALL)
    if not m:
        return False
    front, body = m.group(1), m.group(2)
    desc = func["description"].strip()

    new_front = re.sub(
        r'(?m)^description:\s*".*"$',
        f'description: "{desc.replace(chr(92), chr(92) * 2).replace(chr(34), chr(92) + chr(34))}"',
        front,
        count=1,
    )

    # Replace the intro paragraph (everything between the "# Title" heading and
    # the first "## " section) with the real description, then splice in any
    # missing Signature/Parameters/Returns sections ahead of the existing ones.
    hm = re.match(r"(\n*# [^\n]+\n)(.*?)(\n## .*)$", body, re.DOTALL)
    if hm:
        heading, _old_intro, rest = hm.group(1), hm.group(2), hm.group(3)
        sections = build_sections(func, body)
        new_body = f"{heading}\n{desc}\n{sections}{rest}"
    else:
        sections = build_sections(func, body)
        new_body = re.sub(
            r"(\n# [^\n]+\n)(.*?)(\n## )",
            lambda mm: f"{mm.group(1)}\n{desc}\n{sections}{mm.group(3)}",
            body,
            count=1,
            flags=re.DOTALL,
        )

    new_text = new_front + new_body
    if new_text == text:
        return False
    path.write_text(new_text, encoding="utf-8")
    return True


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    print("Building authoritative index from HIP Doxygen ...")
    index = build_index()
    print(f"  indexed {len(index)} symbols\n")

    changed = 0
    skipped_no_source = []
    for doc in sorted(DOCS_DIR.glob("hip-*/DOC.md")):
        text = doc.read_text(encoding="utf-8")
        dm = re.search(r'(?m)^description:\s*"(.*)"$', text)
        desc = dm.group(1) if dm else ""
        body = text.split("---", 2)[-1]
        is_stub = bool(STUB_RE.match(desc))
        # real function with no signature in the doc
        name_guess = None
        nm = re.search(r"(?m)^name:\s*hip-(.+)$", text)
        missing_sig = "## Signature" not in body and "## Parameters" not in body

        if not (is_stub or missing_sig):
            continue

        # Resolve the original CamelCase symbol name from the index by
        # case-insensitive match on the lowercased slug.
        slug = nm.group(1) if nm else doc.parent.name[4:]
        match = next((index[k] for k in index if k.lower() == slug), None)
        if not match:
            if is_stub:
                skipped_no_source.append(slug)
            continue

        # Only replace the description when the current one is a generic stub
        # AND the source description is genuinely informative (not a bare echo
        # of the symbol name, e.g. "hipJitOption"). Never overwrite a curated
        # non-stub description, even if the scrape differs.
        src_desc = match["description"].strip()
        echo = re.sub(r"[^a-z0-9]", "", src_desc.lower()) == match["name"].lower()
        better_desc = is_stub and bool(src_desc) and not echo
        adds_sig = missing_sig and (match.get("signature") or match.get("params"))
        if not (better_desc or adds_sig):
            continue
        # If we're only here to add a signature, keep the existing description.
        if not better_desc:
            match = {**match, "description": desc}

        if args.dry_run:
            print(f"  WOULD enrich {slug}: desc='{match['description'][:50]}' "
                  f"sig={'Y' if match.get('signature') else '-'}")
            changed += 1
            continue
        if enrich_doc(doc, match):
            changed += 1
            print(f"  enriched {slug}")

    print(f"\n{'Would enrich' if args.dry_run else 'Enriched'}: {changed} docs")
    if skipped_no_source:
        print(f"Stubs with no Doxygen source (left as-is): {', '.join(skipped_no_source)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
