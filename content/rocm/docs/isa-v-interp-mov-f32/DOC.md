---
name: isa-v-interp-mov-f32
description: "Given an attribute specifier and a parameter ID (P0, P10 or P20), load one of the parameter values from the local data share into a vector register."
metadata:
  languages: hip
  architectures: cdna1
  versions: 'CDNA1+'
  revision: 1
  updated-on: '2026-06-12'
  source: official
  tags: rocm,gpu,v,isa,simd-unit,compute
  isa_category: compute
  instruction_type: VOP
  hw_unit: simd-unit
  func_group: VALU
  arch_name: AMD CDNA 1
---

# V_INTERP_MOV_F32

Given an attribute specifier and a parameter ID (P0, P10 or P20), load one of the parameter values from the local data share into a vector register.

## Encoding

Encoding: `ENC_VINTRP`
Opcode: `2`


## Operands

| Field | Type | Size | Direction | Implicit |
|-------|------|------|-----------|----------|
| VDST | VGPR | 32bit | out | no |
| VSRC | PARAM | 32bit | in | no |
| ATTR | ATTR | 32bit | in | no |
|  | SDST_M0 | 32bit | in | yes |
| SRC1 | PARAM | 32bit | in | no |
| SRC0 | ATTR | 32bit | in | no |


## References

- [AMD CDNA 1 ISA Reference Guide](https://www.amd.com/content/dam/amd/en/documents/instinct-tech-docs/instruction-set-architectures/)
- [AMD Machine-Readable ISA](https://gpuopen.com/machine-readable-isa/)
