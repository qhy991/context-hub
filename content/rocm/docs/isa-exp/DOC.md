---
name: isa-exp
description: "Export graphics data to the next stage of the render pipeline. The target and up to four channels of data are specified as operands."
metadata:
  languages: hip
  architectures: cdna1
  versions: 'CDNA1+'
  revision: 1
  updated-on: '2026-06-12'
  source: official
  tags: rocm,gpu,exp,isa
  isa_category: export
  instruction_type: EXP
  hw_unit: export-unit
  func_group: EXPORT
  arch_name: AMD CDNA 1
---

# EXP

Export graphics data to the next stage of the render pipeline. The target and up to four channels of data are specified as operands.

## Encoding

Encoding: `ENC_EXP`
Opcode: `0`


## Operands

| Field | Type | Size | Direction | Implicit |
|-------|------|------|-----------|----------|
| TGT | TGT | 128bit | out | no |
| VSRC0 | VGPR | 32bit | in | no |
| VSRC1 | VGPR | 32bit | in | no |
| VSRC2 | VGPR | 32bit | in | no |
| VSRC3 | VGPR | 32bit | in | no |
|  | SDST_EXEC | 64bit | in | yes |


## References

- [AMD CDNA 1 ISA Reference Guide](https://www.amd.com/content/dam/amd/en/documents/instinct-tech-docs/instruction-set-architectures/)
- [AMD Machine-Readable ISA](https://gpuopen.com/machine-readable-isa/)
