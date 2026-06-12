---
name: isa-v-interp-p2-f32
description: "Given the J coordinate in a vector register, an attribute specifier and the result of a prior V_INTERP_P1_F32 in the destination vector register, load parameter data from the local data share, compute the second part of parameter interpolation and store the final result into a vector register."
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

# V_INTERP_P2_F32

Given the J coordinate in a vector register, an attribute specifier and the result of a prior V_INTERP_P1_F32 in the destination vector register, load parameter data from the local data share, compute the second part of parameter interpolation and store the final result into a vector register.

## Encoding

Encoding: `ENC_VINTRP`
Opcode: `1`


## Operands

| Field | Type | Size | Direction | Implicit |
|-------|------|------|-----------|----------|
| VDST | VGPR | 32bit | out | no |
| VSRC | VGPR | 32bit | in | no |
| ATTR | ATTR | 32bit | in | no |
|  | SDST_M0 | 32bit | in | yes |
| SRC1 | SRC_VGPR | 32bit | in | no |
| SRC0 | ATTR | 32bit | in | no |


## References

- [AMD CDNA 1 ISA Reference Guide](https://www.amd.com/content/dam/amd/en/documents/instinct-tech-docs/instruction-set-architectures/)
- [AMD Machine-Readable ISA](https://gpuopen.com/machine-readable-isa/)
