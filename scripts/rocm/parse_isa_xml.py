#!/usr/bin/env python3
"""
Parse AMD Machine-Readable ISA XML → context-hub DOC.md files.

XML structure (from AMD GPUOpen):
  <Spec>
    <Document>...</Document>
    <ISA>
      <Architecture>
        <ArchitectureName>AMD CDNA 4</ArchitectureName>
        <ArchitectureId>3</ArchitectureId>
      </Architecture>
      <Encodings>...</Encodings>
      <Instructions>
        <Instruction>
          <InstructionFlags>...</InstructionFlags>
          <InstructionName>DS_ADD_U32</InstructionName>
          <Description>Add two unsigned 32-bit ...</Description>
          <InstructionEncodings>
            <InstructionEncoding>
              <EncodingName>ENC_DS</EncodingName>
              <Operands>
                <Operand Input="true" Output="false" ...>
                  <FieldName>ADDR</FieldName>
                  <DataFormatName>FMT_NUM_B32</DataFormatName>
                  <OperandType>OPR_VGPR</OperandType>
                  <OperandSize>32</OperandSize>
                </Operand>
              </Operands>
            </InstructionEncoding>
          </InstructionEncodings>
          <FunctionalGroup>
            <Name>VMEM</Name>
            <FunctionalSubgroups>
              <Subgroup>ATOMIC</Subgroup>
              <Subgroup>DATA_SHARE</Subgroup>
            </FunctionalSubgroups>
          </FunctionalGroup>
        </Instruction>
      </Instructions>
      <DataFormats>...</DataFormats>
      <OperandTypes>...</OperandTypes>
      <FunctionalGroups>...</FunctionalGroups>
    </ISA>
  </Spec>

Usage:
    python3 parse_isa_xml.py --xml amdgpu_isa_cdna4.xml --outdir ../../content/rocm/docs
    python3 parse_isa_xml.py --xml /tmp/amdgpu_isa_specs/amdgpu_isa_cdna3.xml --outdir ../../content/rocm/docs

Download XML from: https://gpuopen.com/download/machine-readable-isa/latest/
"""

import argparse
import os
import re
import xml.etree.ElementTree as ET
from datetime import date
from pathlib import Path

# ── Architecture mapping ──────────────────────────────────────────────

ARCH_MAP = {
    "cdna1": {"gfx": "gfx908", "gpu": "MI100"},
    "cdna2": {"gfx": "gfx90a", "gpu": "MI250/MI210"},
    "cdna3": {"gfx": "gfx940,gfx942", "gpu": "MI300X/MI300A"},
    "cdna4": {"gfx": "gfx950", "gpu": "MI350X/MI355X"},
    "rdna1": {"gfx": "gfx1010", "gpu": "RX 5700"},
    "rdna2": {"gfx": "gfx1030", "gpu": "RX 6800"},
    "rdna3": {"gfx": "gfx1100", "gpu": "RX 7900"},
    "rdna3_5": {"gfx": "gfx1150", "gpu": "RX 9070"},
    "rdna4": {"gfx": "gfx1200", "gpu": "RX 9060"},
}

# Instruction classification by name prefix
HW_UNIT_MAP = [
    ("V_MFMA", "matrix-core"),
    ("V_SMFMAC", "matrix-core"),
    ("V_DOT", "matrix-core"),
    ("V_MAC", "simd-unit"),
    ("V_MAD", "simd-unit"),
    ("V_ADD", "simd-unit"),
    ("V_SUB", "simd-unit"),
    ("V_MUL", "simd-unit"),
    ("V_FMA", "simd-unit"),
    ("V_MOV_DPP", "simd-unit"),
    ("V_MOV", "simd-unit"),
    ("V_PERM", "simd-unit"),
    ("V_CMP", "flow"),
    ("V_CNDMASK", "flow"),
    ("DS_READ", "lds"),
    ("DS_WRITE", "lds"),
    ("DS_", "lds"),
    ("FLAT_", "memory-controller"),
    ("GLOBAL_", "memory-controller"),
    ("BUFFER_", "memory-controller"),
    ("S_LOAD", "scalar-unit"),
    ("S_STORE", "scalar-unit"),
    ("S_WAITCNT", "scheduler"),
    ("S_BARRIER", "scheduler"),
    ("S_", "scalar-unit"),
    ("EXP_", "export-unit"),
    ("V_", "simd-unit"),
]

ISA_CATEGORY_MAP = [
    ("V_MFMA", "compute"),
    ("V_SMFMAC", "compute"),
    ("V_DOT", "compute"),
    ("V_MAC", "compute"),
    ("V_MAD", "compute"),
    ("V_ADD", "compute"),
    ("V_SUB", "compute"),
    ("V_MUL", "compute"),
    ("V_FMA", "compute"),
    ("V_", "compute"),
    ("DS_", "memory"),
    ("FLAT_", "memory"),
    ("GLOBAL_", "memory"),
    ("BUFFER_", "memory"),
    ("S_LOAD", "memory"),
    ("S_STORE", "memory"),
    ("S_WAITCNT", "synchronization"),
    ("S_BARRIER", "synchronization"),
    ("S_", "flow"),
    ("EXP_", "export"),
]

INSTRUCTION_TYPE_MAP = [
    ("V_MFMA", "VOP3P"),
    ("V_SMFMAC", "VOP3P"),
    ("V_DOT", "VOP3P"),
    ("V_MOV_DPP", "VOP1_DPP"),
    ("V_PERMLANE", "VOP1"),
    ("DS_", "DS"),
    ("FLAT_", "FLAT"),
    ("GLOBAL_", "GLOBAL"),
    ("BUFFER_", "MTBUF/MUBUF"),
    ("S_", "SOP"),
    ("EXP_", "EXP"),
    ("V_", "VOP"),
]

# Functional group → category mapping
FUNCGROUP_CATEGORY = {
    "COMPUTE": "compute",
    "VMEM": "memory",
    "DS": "memory",
    "SALU": "flow",
    "SMRD": "memory",
    "EXPORT": "export",
    "BRANCH": "flow",
    "WAITCNT": "synchronization",
}


def classify_instruction(name: str, funcgroup: str = "") -> dict:
    """Classify an instruction by its name prefix and functional group."""
    name_upper = name.upper()

    hw_unit = "unknown"
    for prefix, unit in HW_UNIT_MAP:
        if name_upper.startswith(prefix):
            hw_unit = unit
            break

    isa_category = "unknown"
    for prefix, cat in ISA_CATEGORY_MAP:
        if name_upper.startswith(prefix):
            isa_category = cat
            break
    # Override with functional group if available
    if funcgroup and funcgroup in FUNCGROUP_CATEGORY:
        # Name-based classification takes priority for specificity
        pass

    instruction_type = "unknown"
    for prefix, itype in INSTRUCTION_TYPE_MAP:
        if name_upper.startswith(prefix):
            instruction_type = itype
            break

    return {
        "hw_unit": hw_unit,
        "isa_category": isa_category,
        "instruction_type": instruction_type,
    }


def slugify(name: str) -> str:
    """Convert instruction name to filesystem slug."""
    slug = name.lower().strip()
    slug = re.sub(r"[^a-z0-9_]", "-", slug)
    slug = re.sub(r"_+", "-", slug)
    slug = re.sub(r"-+", "-", slug)
    slug = slug.strip("-")
    return f"isa-{slug}"


CDNA_ARCH_ORDER = ["cdna1", "cdna2", "cdna3", "cdna4"]
RDNA_ARCH_ORDER = ["rdna1", "rdna2", "rdna3", "rdna3_5", "rdna4"]


def determine_architectures(xml_filename: str) -> tuple[str, str]:
    """Map an ISA XML filename to the architecture it describes."""
    filename_lower = xml_filename.lower()
    for arch_key in ARCH_MAP:
        if arch_key in filename_lower:
            return arch_key, f"{arch_key.upper()}+"
    return "cdna1", "CDNA1+"


def read_existing_architectures(doc_path: str) -> set[str]:
    if not os.path.exists(doc_path):
        return set()
    with open(doc_path, encoding="utf-8") as handle:
        content = handle.read()
    match = re.search(r"architectures: ([^\n]+)", content)
    if not match:
        return set()
    return {item.strip() for item in match.group(1).split(",") if item.strip()}


def merge_architectures(*arch_sets: set[str]) -> str:
    merged: set[str] = set()
    for arch_set in arch_sets:
        merged |= arch_set
    ordered = [arch for arch in CDNA_ARCH_ORDER if arch in merged]
    ordered += [arch for arch in RDNA_ARCH_ORDER if arch in merged]
    extra = sorted(merged - set(ordered))
    return ",".join(ordered + extra)


def parse_operands(encoding_elem) -> list[dict]:
    """Parse operands from an InstructionEncoding element."""
    operands = []
    ops_elem = encoding_elem.find("Operands")
    if ops_elem is None:
        return operands

    for op in ops_elem.findall("Operand"):
        operand = {
            "field": op.findtext("FieldName", ""),
            "data_format": op.findtext("DataFormatName", ""),
            "type": op.findtext("OperandType", ""),
            "size": op.findtext("OperandSize", ""),
            "is_input": op.get("Input", "false") == "true",
            "is_output": op.get("Output", "false") == "true",
            "is_implicit": op.get("IsImplicit", "false") == "true",
        }
        operands.append(operand)
    return operands


def extract_instruction_docs(xml_path: str, out_dir: str, filter_re: str = None):
    """Parse ISA XML and generate DOC.md files for each instruction."""

    tree = ET.parse(xml_path)
    root = tree.getroot()

    xml_name = os.path.basename(xml_path)
    architecture, version = determine_architectures(xml_name)
    today = date.today().isoformat()

    # Extract architecture name from XML
    arch_name = "Unknown"
    isa_elem = root.find("ISA")
    if isa_elem is not None:
        arch_elem = isa_elem.find("Architecture")
        if arch_elem is not None:
            arch_name = arch_elem.findtext("ArchitectureName", "Unknown")

    # Find instructions
    instructions_elem = None
    if isa_elem is not None:
        instructions_elem = isa_elem.find("Instructions")

    if instructions_elem is None:
        print(f"ERROR: No <Instructions> element found in {xml_name}")
        return 0, 0

    count = 0
    skipped = 0
    filter_pattern = re.compile(filter_re, re.IGNORECASE) if filter_re else None

    for instr_elem in instructions_elem.findall("Instruction"):
        name = instr_elem.findtext("InstructionName", "")
        if not name:
            continue

        # Apply filter
        if filter_pattern and not filter_pattern.search(name):
            skipped += 1
            continue

        # Extract description
        description = instr_elem.findtext("Description", "").strip()
        if not description:
            description = f"{name} instruction"

        # Extract functional group
        funcgroup = ""
        fg_elem = instr_elem.find("FunctionalGroup")
        if fg_elem is not None:
            funcgroup = fg_elem.findtext("Name", "")

        # Extract instruction flags
        flags = {}
        flags_elem = instr_elem.find("InstructionFlags")
        if flags_elem is not None:
            for flag in flags_elem:
                flags[flag.tag] = flag.text

        # Extract encodings and operands
        encodings = []
        enc_elem = instr_elem.find("InstructionEncodings")
        if enc_elem is not None:
            for enc in enc_elem.findall("InstructionEncoding"):
                enc_data = {
                    "name": enc.findtext("EncodingName", ""),
                    "opcode": enc.findtext("Opcode", ""),
                    "condition": enc.findtext("EncodingCondition", ""),
                    "operands": parse_operands(enc),
                }
                encodings.append(enc_data)

        # Classify
        classification = classify_instruction(name, funcgroup)
        slug = slugify(name)

        # Generate tags
        prefix = name.split("_")[0].lower() if "_" in name else name[:3].lower()
        name_parts = name.lower().replace("_", ",").split(",")
        tags = f"rocm,gpu,{prefix},isa,{classification['hw_unit']},{classification['isa_category']}"
        # Add extra meaningful tags
        if "mfma" in name.lower():
            tags += ",matrix-core,mfma"
        if "dpp" in name.lower():
            tags += ",dpp,cross-lane"
        if "f16" in name.lower() or "bf16" in name.lower():
            tags += ",low-precision"
        if "f8" in name.lower() or "fp8" in name.lower():
            tags += ",fp8"
        if "atomic" in name.lower():
            tags += ",atomic"

        # Build operands table
        operands_md = ""
        all_operands = []
        for enc in encodings:
            all_operands.extend(enc["operands"])

        if all_operands:
            operands_md = "\n## Operands\n\n"
            operands_md += "| Field | Type | Size | Direction | Implicit |\n"
            operands_md += "|-------|------|------|-----------|----------|\n"
            seen = set()
            for op in all_operands:
                key = (op["field"], op["type"])
                if key in seen:
                    continue
                seen.add(key)
                direction = "in" if op["is_input"] else "out"
                if op["is_input"] and op["is_output"]:
                    direction = "in/out"
                implicit = "yes" if op["is_implicit"] else "no"
                operands_md += f"| {op['field']} | {op['type'].replace('OPR_', '')} | {op['size']}bit | {direction} | {implicit} |\n"

        # Build encoding info
        encoding_md = ""
        if encodings:
            encoding_md = f"\n## Encoding\n\n"
            encoding_md += f"Encoding: `{encodings[0]['name']}`\n"
            if encodings[0]['opcode']:
                encoding_md += f"Opcode: `{encodings[0]['opcode']}`\n"

        # Build flags info
        flags_md = ""
        if flags:
            true_flags = [k for k, v in flags.items() if v == "TRUE"]
            if true_flags:
                flags_md = f"\n## Flags\n\n"
                for f in true_flags:
                    flags_md += f"- {f}\n"

        # Escape description for YAML
        desc_escaped = description.replace('"', '\\"').replace("\n", " ")

        # Generate DOC.md
        doc_content = f"""---
name: {slug}
description: "{desc_escaped}"
metadata:
  languages: hip
  architectures: {architecture}
  versions: '{version}'
  revision: 1
  updated-on: '{today}'
  source: official
  tags: {tags}
  isa_category: {classification['isa_category']}
  instruction_type: {classification['instruction_type']}
  hw_unit: {classification['hw_unit']}
  func_group: {funcgroup}
  arch_name: {arch_name}
---

# {name}

{description}
{encoding_md}
{operands_md}
{flags_md}
## References

- [{arch_name} ISA Reference Guide](https://www.amd.com/content/dam/amd/en/documents/instinct-tech-docs/instruction-set-architectures/)
- [AMD Machine-Readable ISA](https://gpuopen.com/machine-readable-isa/)
"""

        doc_dir = os.path.join(out_dir, slug)
        os.makedirs(doc_dir, exist_ok=True)

        doc_path = os.path.join(doc_dir, "DOC.md")
        merged_architectures = merge_architectures(
            {architecture},
            read_existing_architectures(doc_path),
        )
        revision = 1
        if os.path.exists(doc_path):
            with open(doc_path, encoding="utf-8") as handle:
                existing = handle.read()
            revision_match = re.search(r"revision: (\d+)", existing)
            if revision_match:
                revision = int(revision_match.group(1)) + 1
            doc_content = re.sub(
                r"architectures: [^\n]+",
                f"architectures: {merged_architectures}",
                doc_content,
                count=1,
            )
            doc_content = re.sub(
                r"revision: \d+",
                f"revision: {revision}",
                doc_content,
                count=1,
            )

        with open(doc_path, "w", encoding="utf-8") as handle:
            handle.write(doc_content)

        count += 1

    return count, skipped


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
        help="Output directory for DOC.md files (default: ../../content/rocm/docs)",
    )
    parser.add_argument(
        "--filter",
        default=None,
        help="Only process instructions matching this regex (e.g., 'MFMA|DPP|DS_READ')",
    )

    args = parser.parse_args()

    if not os.path.exists(args.xml):
        print(f"Error: XML file not found: {args.xml}")
        print("Download from https://gpuopen.com/download/machine-readable-isa/latest/")
        return 1

    out_dir = os.path.abspath(args.outdir)
    os.makedirs(out_dir, exist_ok=True)

    print(f"XML:     {args.xml}")
    print(f"Output:  {out_dir}")
    if args.filter:
        print(f"Filter:  {args.filter}")
    print()

    count, skipped = extract_instruction_docs(args.xml, out_dir, args.filter)

    print(f"\nDone: {count} instructions extracted, {skipped} skipped by filter")
    print(f"Output directory: {out_dir}")
    print(f"\nNext steps:")
    print(f"  cd {os.path.dirname(out_dir)}")
    print(f"  chub build content/")

    return 0


if __name__ == "__main__":
    exit(main())
