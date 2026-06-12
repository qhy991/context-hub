---
name: isa-s-scratch-store-dword
description: "Store 32 bits of data from a scalar register into the scalar scratch aperture."
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
  func_group: SMEM
  arch_name: AMD CDNA 4
---

# S_SCRATCH_STORE_DWORD

Store 32 bits of data from a scalar register into the scalar scratch aperture.

## Encoding

Encoding: `ENC_SMEM`
Opcode: `21`


## Operands

| Field | Type | Size | Direction | Implicit |
|-------|------|------|-----------|----------|
| SDATA | SREG | 32bit | in | no |
| SBASE | SREG | 64bit | in | no |
| SOFFSET | SMEM_OFFSET | 32bit | in | no |
|  | GPUMEM | 32bit | out | yes |


## References

- [AMD CDNA 4 ISA Reference Guide](https://www.amd.com/content/dam/amd/en/documents/instinct-tech-docs/instruction-set-architectures/)
- [AMD Machine-Readable ISA](https://gpuopen.com/machine-readable-isa/)
