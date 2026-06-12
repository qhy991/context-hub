---
name: isa-s-cbranch-i-fork
description: "Conditional branch using branch-stack."
metadata:
  languages: hip
  architectures: cdna1,cdna2,cdna3,cdna4
  versions: 'CDNA4+'
  revision: 1
  updated-on: '2026-06-12'
  source: official
  tags: rocm,gpu,s,isa,scalar-unit,flow
  isa_category: flow
  instruction_type: SOP
  hw_unit: scalar-unit
  func_group: SALU
  arch_name: AMD CDNA 4
---

# S_CBRANCH_I_FORK

Conditional branch using branch-stack.

## Encoding

Encoding: `ENC_SOPK`
Opcode: `16`


## Operands

| Field | Type | Size | Direction | Implicit |
|-------|------|------|-----------|----------|
| SDST | SDST | 64bit | in | no |
| SIMM16 | LABEL | 16bit | in | no |


## Flags

- IsBranch
- IsConditionalBranch

## References

- [AMD CDNA 4 ISA Reference Guide](https://www.amd.com/content/dam/amd/en/documents/instinct-tech-docs/instruction-set-architectures/)
- [AMD Machine-Readable ISA](https://gpuopen.com/machine-readable-isa/)
