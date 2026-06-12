---
name: isa-v-interp-p2-f16
description: "Given a single-precision float J coordinate in a vector register, an attribute specifier and the result of a prior V_INTERP_P1_F32 in another vector register, load a half-precision float parameter value from the local data share, compute the second part of parameter interpolation and store the final result as a half-precision float value into a vector register."
metadata:
  languages: hip
  architectures: cdna1
  versions: 'CDNA1+'
  revision: 1
  updated-on: '2026-06-12'
  source: official
  tags: rocm,gpu,v,isa,simd-unit,compute,low-precision
  isa_category: compute
  instruction_type: VOP
  hw_unit: simd-unit
  func_group: VALU
  arch_name: AMD CDNA 1
---

# V_INTERP_P2_F16

Given a single-precision float J coordinate in a vector register, an attribute specifier and the result of a prior V_INTERP_P1_F32 in another vector register, load a half-precision float parameter value from the local data share, compute the second part of parameter interpolation and store the final result as a half-precision float value into a vector register.

## Encoding

Encoding: `ENC_VOP3`
Opcode: `631`


## Operands

| Field | Type | Size | Direction | Implicit |
|-------|------|------|-----------|----------|
| VDST | VGPR | 16bit | out | no |
| SRC1 | SRC_VGPR | 32bit | in | no |
| SRC0 | ATTR | 16bit | in | no |
| SRC2 | SRC_VGPR | 32bit | in | no |


## References

- [AMD CDNA 1 ISA Reference Guide](https://www.amd.com/content/dam/amd/en/documents/instinct-tech-docs/instruction-set-architectures/)
- [AMD Machine-Readable ISA](https://gpuopen.com/machine-readable-isa/)
