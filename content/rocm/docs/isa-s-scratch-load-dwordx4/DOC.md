---
name: isa-s-scratch-load-dwordx4
description: "Load 128 bits of data from the scalar scratch aperture into a scalar register."
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

# S_SCRATCH_LOAD_DWORDX4

Load 128 bits of data from the scalar scratch aperture into a scalar register.

## Encoding

Encoding: `ENC_SMEM`
Opcode: `7`


## Operands

| Field | Type | Size | Direction | Implicit |
|-------|------|------|-----------|----------|
| SDATA | SREG | 128bit | out | no |
| SBASE | SREG | 64bit | in | no |
| SOFFSET | SMEM_OFFSET | 32bit | in | no |
|  | GPUMEM | 128bit | in | yes |


## References

- [AMD CDNA 4 ISA Reference Guide](https://www.amd.com/content/dam/amd/en/documents/instinct-tech-docs/instruction-set-architectures/)
- [AMD Machine-Readable ISA](https://gpuopen.com/machine-readable-isa/)
