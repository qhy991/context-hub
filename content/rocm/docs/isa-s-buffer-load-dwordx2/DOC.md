---
name: isa-s-buffer-load-dwordx2
description: "Load 64 bits of data from a scalar buffer surface into a scalar register."
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
  func_group: SMEM
  arch_name: AMD CDNA 4
---

# S_BUFFER_LOAD_DWORDX2

Load 64 bits of data from a scalar buffer surface into a scalar register.

## Encoding

Encoding: `ENC_SMEM`
Opcode: `9`


## Operands

| Field | Type | Size | Direction | Implicit |
|-------|------|------|-----------|----------|
| SDATA | SREG | 64bit | out | no |
| SBASE | SREG | 128bit | in | no |
| SOFFSET | SMEM_OFFSET | 32bit | in | no |
|  | GPUMEM | 64bit | in | yes |


## References

- [AMD CDNA 4 ISA Reference Guide](https://www.amd.com/content/dam/amd/en/documents/instinct-tech-docs/instruction-set-architectures/)
- [AMD Machine-Readable ISA](https://gpuopen.com/machine-readable-isa/)
