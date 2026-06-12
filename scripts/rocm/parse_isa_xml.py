#!/usr/bin/env python3
"""
Parse AMD Machine-Readable ISA XML → context-hub DOC.md files.

Usage:
    python3 parse_isa_xml.py --xml amdgpu_isa_cdna4.xml --outdir ../../content/rocm/docs

The XML spec is downloadable from https://gpuopen.com/machine-readable-isa/
"""

import argparse
import os
import re
import xml.etree.ElementTree as ET
from pathlib import Path

# ── Architecture mapping ──────────────────────────────────────────────

ARCH_MAP = {
    "cdna1": {"gfx": "gfx908", "gpu": "MI100"},
    "cdna2": {"gfx": "gfx90a", "gpu": "MI250/MI210"},
    "cdna3": {"gfx": "gfx940,gfx942", "gpu": "MI300X/MI300A"},
    "cdna4": {"gfx": "gfx950", "gpu": "MI350X/MI355X"},
}

# Instruction classification
HW_UNIT_MAP = {
    "v_mfma": "matrix-core",
    "v_dot": "matrix-core",
    "v_mac": "simd-unit",
    "v_mad": "simd-unit",
    "v_add": "simd-unit",
    "v_mul": "simd-unit",
    "v_mov_dpp": "simd-unit",
    "v_perm": "simd-unit",
    "ds_read": "lds",
    "ds_write": "lds",
    "ds_": "lds",
    "flat_load": "memory-controller",
    "flat_store": "memory-controller",
    "global_load": "memory-controller",
    "global_store": "memory-controller",
    "s_load": "scalar-unit",
    "s_store": "scalar-unit",
    "s_waitcnt": "scheduler",
    "s_barrier": "scheduler",
    "exp": "export-unit",
}

ISA_CATEGORY_MAP = {
    "v_mfma": "compute",
    "v_dot": "compute",
    "v_mac": "compute",
    "v_mad": "compute",
    "v_add": "compute",
    "v_mul": "compute",
    "v_fma": "compute",
    "v_mov": "compute",
    "v_cmp": "flow",
    "v_cndmask": "flow",
    "v_branch": "flow",
    "ds_read": "memory",
    "ds_write": "memory",
    "ds_": "memory",
    "flat_": "memory",
    "global_": "memory",
    "s_load": "memory",
    "s_store": "memory",
    "s_waitcnt": "synchronization",
    "s_barrier": "synchronization",
    "s_sendmsg": "synchronization",
}

INSTRUCTION_TYPE_MAP = {
    "v_mfma": "VOP3P",
    "v_dot": "VOP3P",
    "v_mac": "VOP2/VOP3",
    "v_mad": "VOP3",
    "v_add": "VOP2",
    "v_mul": "VOP2",
    "v_mov": "VOP1",
    "v_mov_dpp": "VOP1_DPP",
    "ds_": "DS",
    "flat_": "FLAT",
    "global_": "GLOBAL",
    "s_": "SOP",
    "exp_": "EXP",
}


def classify_instruction(name: str) -> dict:
    """Classify an instruction by its prefix."""
    name_lower = name.lower()
    hw_unit = "unknown"
    isa_category = "unknown"
    instruction_type = "unknown"

    for prefix, unit in HW_UNIT_MAP.items():
        if name_lower.startswith(prefix):
            hw_unit = unit
            break

    for prefix, cat in ISA_CATEGORY_MAP.items():
        if name_lower.startswith(prefix):
            isa_category = cat
            break

    for prefix, itype in INSTRUCTION_TYPE_MAP.items():
        if name_lower.startswith(prefix):
            instruction_type = itype
            break

    return {
        "hw_unit": hw_unit,
        "isa_category": isa_category,
        "instruction_type": instruction_type,
    }


def slugify(name: str) -> str:
    """Convert instruction name to filesystem slug."""
    # v_mfma_f32_16x16x4f32 → isa-v-mfma-f32-16x16x4f32
    slug = name.lower().strip()
    slug = re.sub(r"[^a-z0-9_]", "-", slug)
    slug = re.sub(r"_+", "-", slug)
    slug = re.sub(r"-+", "-", slug)
    slug = slug.strip("-")
    return f"isa-{slug}"


def determine_architectures(xml_filename: str) -> str:
    """Determine which architectures this XML covers."""
    for arch_key in ARCH_MAP:
        if arch_key in xml_filename.lower():
            # Also include earlier archs if they support the instruction
            idx = list(ARCH_MAP.keys()).index(arch_key)
            all_archs = list(ARCH_MAP.keys())[: idx + 1]
            return ",".join(all_archs)
    return "cdna1,cdna2,cdna3,cdna4"


def determine_version(xml_filename: str) -> str:
    """Determine the minimum architecture version."""
    for arch_key in ARCH_MAP:
        if arch_key in xml_filename.lower():
            return f"{arch_key.upper()}+"
    return "CDNA1+"


def extract_instruction_docs(xml_path: str, out_dir: str, arch_hint: str = None):
    """Parse ISA XML and generate DOC.md files for each instruction."""

    tree = ET.parse(xml_path)
    root = tree.getroot()

    xml_name = os.path.basename(xml_path)
    architectures = arch_hint or determine_architectures(xml_name)
    version = determine_version(xml_name)

    count = 0
    errors = 0

    # Navigate XML structure to find instructions
    # AMD ISA XML typically has: <architecture> → <instructions> → <instruction>
    for instr_elem in root.iter():
        # Try multiple possible XML structures
        tag = instr_elem.tag.split("}")[-1] if "}" in instr_elem.tag else instr_elem.tag

        if tag not in ("instruction", "Instruction", "inst"):
            continue

        # Extract instruction name
        name = None
        description = ""
        encoding = ""
        operands = []

        # Try different attribute names
        name = (
            instr_elem.get("name")
            or instr_elem.get("Name")
            or instr_elem.get("id")
            or instr_elem.findtext("name")
            or instr_elem.findtext("Name")
        )

        if not name:
            continue

        # Skip non-compute instructions that aren't useful for kernel dev
        if any(skip in name.lower() for skip in ["s_set_gpr_idx", "s_cbranch", "s_cselect"]):
            continue

        # Extract description
        desc_elem = (
            instr_elem.find("description")
            or instr_elem.find("Description")
            or instr_elem.find("desc")
        )
        if desc_elem is not None and desc_elem.text:
            description = desc_elem.text.strip()

        # Classify
        classification = classify_instruction(name)
        slug = slugify(name)

        # Generate DOC.md
        doc_dir = os.path.join(out_dir, slug)
        os.makedirs(doc_dir, exist_ok=True)

        doc_content = f"""---
name: {slug}
description: "{description or name + ' instruction'}"
metadata:
  languages: hip
  architectures: {architectures}
  versions: '{version}'
  revision: 1
  updated-on: '{__import__("datetime").date.today().isoformat()}'
  source: official
  tags: rocm,gpu,{','.join(name.lower().split('_')[:2])},isa,{classification['hw_unit']},{classification['isa_category']},cdna
  isa_category: {classification['isa_category']}
  instruction_type: {classification['instruction_type']}
  hw_unit: {classification['hw_unit']}
---

# {name}

{description or f"AMD GPU instruction: {name}"}

> Auto-extracted from `{xml_name}` (AMD Machine-Readable ISA XML).

## References

- [CDNA4 ISA Reference Guide](https://www.amd.com/content/dam/amd/en/documents/instinct-tech-docs/instruction-set-architectures/amd-instinct-cdna4-instruction-set-architecture.pdf)
- [AMD Machine-Readable ISA](https://gpuopen.com/machine-readable-isa/)
"""

        doc_path = os.path.join(doc_dir, "DOC.md")
        with open(doc_path, "w") as f:
            f.write(doc_content)

        count += 1

    return count, errors


def main():
    parser = argparse.ArgumentParser(
        description="Parse AMD ISA XML → context-hub DOC.md files"
    )
    parser.add_argument(
        "--xml",
        required=True,
        help="Path to AMD ISA XML file (e.g., amdgpu_isa_cdna4.xml)",
    )
    parser.add_argument(
        "--outdir",
        default="../../content/rocm/docs",
        help="Output directory for DOC.md files",
    )
    parser.add_argument(
        "--arch",
        default=None,
        help="Override architecture string (e.g., 'cdna3,cdna4')",
    )
    parser.add_argument(
        "--filter",
        default=None,
        help="Only process instructions matching this regex",
    )

    args = parser.parse_args()

    if not os.path.exists(args.xml):
        print(f"Error: XML file not found: {args.xml}")
        print("Download from https://gpuopen.com/machine-readable-isa/")
        return 1

    out_dir = os.path.abspath(args.outdir)
    os.makedirs(out_dir, exist_ok=True)

    print(f"Parsing: {args.xml}")
    print(f"Output:  {out_dir}")

    count, errors = extract_instruction_docs(args.xml, out_dir, args.arch)

    print(f"\nDone: {count} instructions extracted, {errors} errors")
    print(f"\nNext step: cd {os.path.dirname(out_dir)} && chub build content/")

    return 0


if __name__ == "__main__":
    exit(main())
