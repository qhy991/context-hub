---
name: isa-s-bcnt1-i32-b32
description: "Count the number of \"1\" bits in a scalar input, store the result into a scalar register and set SCC iff the result is nonzero."
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

# S_BCNT1_I32_B32

Count the number of "1" bits in a scalar input, store the result into a scalar register and set SCC iff the result is nonzero.

## Encoding

Encoding: `ENC_SOP1`
Opcode: `12`


## Operands

| Field | Type | Size | Direction | Implicit |
|-------|------|------|-----------|----------|
| SDST | SDST | 32bit | out | no |
| SSRC0 | SSRC | 32bit | in | no |
|  | SSRC_SPECIAL_SCC | 1bit | out | yes |
| LITERAL | SSRC | 32bit | in | no |


## References

- [AMD CDNA 4 ISA Reference Guide](https://www.amd.com/content/dam/amd/en/documents/instinct-tech-docs/instruction-set-architectures/)
- [AMD Machine-Readable ISA](https://gpuopen.com/machine-readable-isa/)
