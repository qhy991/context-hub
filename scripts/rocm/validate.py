#!/usr/bin/env python3
"""Validate ROCm context-hub DOC.md entries."""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DOCS_DIR = ROOT / "content" / "rocm" / "docs"

REQUIRED_FRONTMATTER = ("name", "description", "metadata")
REQUIRED_METADATA = (
    "languages",
    "architectures",
    "source",
    "tags",
    "isa_category",
    "instruction_type",
    "hw_unit",
)
VALID_ARCHITECTURES = {
    "cdna1",
    "cdna2",
    "cdna3",
    "cdna4",
    "rdna1",
    "rdna2",
    "rdna3",
    "rdna3_5",
    "rdna4",
}


def parse_frontmatter(text: str) -> dict[str, str]:
    match = re.match(r"^---\n(.*?)\n---", text, re.DOTALL)
    if not match:
        return {}

    fields: dict[str, str] = {}
    for line in match.group(1).splitlines():
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        fields[key.strip()] = value.strip().strip("'\"")
    return fields


def validate_doc(path: Path) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []
    text = path.read_text(encoding="utf-8")
    fm = parse_frontmatter(text)

    if not fm:
        errors.append("missing frontmatter")
        return errors, warnings

    for key in REQUIRED_FRONTMATTER:
        if key not in fm:
            errors.append(f"missing frontmatter field: {key}")

    metadata_block = re.search(
        r"metadata:\n((?:  .+\n)+)",
        text,
    )
    if not metadata_block:
        errors.append("missing metadata block")
    else:
        metadata_lines = {
            line.split(":", 1)[0].strip(): line.split(":", 1)[1].strip()
            for line in metadata_block.group(1).splitlines()
            if ":" in line
        }
        for key in REQUIRED_METADATA:
            if key not in metadata_lines:
                errors.append(f"missing metadata field: {key}")

        archs = {
            item.strip()
            for item in metadata_lines.get("architectures", "").split(",")
            if item.strip()
        }
        invalid = sorted(archs - VALID_ARCHITECTURES)
        if invalid:
            errors.append(f"invalid architectures: {', '.join(invalid)}")

    body = text.split("---", 2)[-1]
    if path.parent.name.startswith("hip-"):
        if "## Parameters" not in body and "## Signature" not in body:
            warnings.append("HIP entry missing signature/parameters")
        if len(body.strip()) < 250:
            warnings.append("HIP entry body looks sparse")

    slug = path.parent.name
    if fm.get("name") and fm["name"] != slug:
        warnings.append(f"name '{fm['name']}' does not match directory '{slug}'")

    return errors, warnings


def main() -> int:
    if not DOCS_DIR.exists():
        print(f"Missing docs directory: {DOCS_DIR}")
        return 1

    docs = sorted(DOCS_DIR.glob("*/DOC.md"))
    total_errors = 0
    total_warnings = 0

    for doc in docs:
        errors, warnings = validate_doc(doc)
        rel = doc.relative_to(ROOT)
        for error in errors:
            print(f"ERROR {rel}: {error}")
            total_errors += 1
        for warning in warnings:
            print(f"WARN  {rel}: {warning}")
            total_warnings += 1

    print("=" * 60)
    print(f"Validated: {len(docs)} docs")
    print(f"Errors:    {total_errors}")
    print(f"Warnings:  {total_warnings}")
    print("=" * 60)
    return 1 if total_errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
