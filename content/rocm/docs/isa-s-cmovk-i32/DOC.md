---
name: isa-s-cmovk-i32
description: "Move the sign extension of a literal 16-bit constant into a scalar register iff SCC is nonzero."
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

# S_CMOVK_I32

Move the sign extension of a literal 16-bit constant into a scalar register iff SCC is nonzero.

## Encoding

Encoding: `ENC_SOPK`
Opcode: `1`


## Operands

| Field | Type | Size | Direction | Implicit |
|-------|------|------|-----------|----------|
| SDST | SDST | 32bit | out | no |
| SIMM16 | SIMM16 | 16bit | in | no |
|  | SSRC_SPECIAL_SCC | 1bit | in | yes |


## References

- [AMD CDNA 4 ISA Reference Guide](https://www.amd.com/content/dam/amd/en/documents/instinct-tech-docs/instruction-set-architectures/)
- [AMD Machine-Readable ISA](https://gpuopen.com/machine-readable-isa/)
