---
name: isa-s-load-dword
description: "Load 32 bits of data from the scalar memory into a scalar register."
metadata:
  languages: hip
  architectures: cdna1,cdna2,cdna3,cdna4
  versions: 'CDNA4+'
  revision: 1
  updated-on: '2026-06-12'
  source: official
  tags: rocm,gpu,s,isa,scalar-unit,memory
  isa_category: memory
  instruction_type: SOP
  hw_unit: scalar-unit
  func_group: SMEM
  arch_name: AMD CDNA 4
---

# S_LOAD_DWORD

Load 32 bits of data from the scalar memory into a scalar register.

## Encoding

Encoding: `ENC_SMEM`
Opcode: `0`


## Operands

| Field | Type | Size | Direction | Implicit |
|-------|------|------|-----------|----------|
| SDATA | SREG | 32bit | out | no |
| SBASE | SREG | 64bit | in | no |
| SOFFSET | SMEM_OFFSET | 32bit | in | no |
|  | GPUMEM | 32bit | in | yes |


## References

- [AMD CDNA 4 ISA Reference Guide](https://www.amd.com/content/dam/amd/en/documents/instinct-tech-docs/instruction-set-architectures/)
- [AMD Machine-Readable ISA](https://gpuopen.com/machine-readable-isa/)
