---
name: isa-s-movreld-b32
description: "Move data from a scalar input into a relatively-indexed scalar register."
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

# S_MOVRELD_B32

Move data from a scalar input into a relatively-indexed scalar register.

## Encoding

Encoding: `ENC_SOP1`
Opcode: `44`


## Operands

| Field | Type | Size | Direction | Implicit |
|-------|------|------|-----------|----------|
| SDST | SREG | 32bit | out | no |
| SSRC0 | SSRC | 32bit | in | no |
|  | SDST_M0 | 32bit | in | yes |
| LITERAL | SSRC | 32bit | in | no |


## References

- [AMD CDNA 4 ISA Reference Guide](https://www.amd.com/content/dam/amd/en/documents/instinct-tech-docs/instruction-set-architectures/)
- [AMD Machine-Readable ISA](https://gpuopen.com/machine-readable-isa/)
