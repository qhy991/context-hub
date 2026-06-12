---
name: isa-s-cmpk-eq-i32
description: "Set SCC to 1 iff scalar input is equal to the sign extension of a literal 16-bit constant."
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

# S_CMPK_EQ_I32

Set SCC to 1 iff scalar input is equal to the sign extension of a literal 16-bit constant.

## Encoding

Encoding: `ENC_SOPK`
Opcode: `2`


## Operands

| Field | Type | Size | Direction | Implicit |
|-------|------|------|-----------|----------|
| SDST | SDST | 32bit | in | no |
| SIMM16 | SIMM16 | 16bit | in | no |
|  | SSRC_SPECIAL_SCC | 1bit | out | yes |


## References

- [AMD CDNA 4 ISA Reference Guide](https://www.amd.com/content/dam/amd/en/documents/instinct-tech-docs/instruction-set-architectures/)
- [AMD Machine-Readable ISA](https://gpuopen.com/machine-readable-isa/)
