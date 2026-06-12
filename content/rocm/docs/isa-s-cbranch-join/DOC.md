---
name: isa-s-cbranch-join
description: "Conditional branch join point (end of conditional branch block)."
metadata:
  languages: hip
  architectures: cdna1,cdna2,cdna3,cdna4
  versions: 'CDNA4+'
  revision: 4
  updated-on: '2026-06-12'
  source: official
  tags: rocm,gpu,s,isa,scalar-unit,flow
  isa_category: flow
  instruction_type: SOP
  hw_unit: scalar-unit
  func_group: SALU
  arch_name: AMD CDNA 4
---

# S_CBRANCH_JOIN

Conditional branch join point (end of conditional branch block).

## Encoding

Encoding: `ENC_SOP1`
Opcode: `46`


## Operands

| Field | Type | Size | Direction | Implicit |
|-------|------|------|-----------|----------|
| SSRC0 | SREG | 32bit | in | no |
|  | SDST_EXEC | 64bit | out | yes |
|  | PC | 64bit | out | yes |
| LITERAL | SREG | 32bit | in | no |


## Flags

- IsBranch
- IsConditionalBranch
- IsIndirectBranch

## References

- [AMD CDNA 4 ISA Reference Guide](https://www.amd.com/content/dam/amd/en/documents/instinct-tech-docs/instruction-set-architectures/)
- [AMD Machine-Readable ISA](https://gpuopen.com/machine-readable-isa/)
