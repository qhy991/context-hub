---
name: isa-v-interp-p1lv-f16
description: "Given a single-precision float I coordinate in a vector register, a half-precision float P0 value in another vector register, and an attribute specifier, load a half-precision float parameter value from the local data share, compute the first part of parameter interpolation and store the intermediate result into a vector register. Use V_INTERP_P2_F16 to complete the operation."
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

# V_INTERP_P1LV_F16

Given a single-precision float I coordinate in a vector register, a half-precision float P0 value in another vector register, and an attribute specifier, load a half-precision float parameter value from the local data share, compute the first part of parameter interpolation and store the intermediate result into a vector register. Use V_INTERP_P2_F16 to complete the operation.

## Encoding

Encoding: `ENC_VOP3`
Opcode: `629`


## Operands

| Field | Type | Size | Direction | Implicit |
|-------|------|------|-----------|----------|
| VDST | VGPR | 32bit | out | no |
| SRC1 | SRC_VGPR | 32bit | in | no |
| SRC0 | ATTR | 16bit | in | no |
| SRC2 | SRC_VGPR | 16bit | in | no |


## References

- [AMD CDNA 1 ISA Reference Guide](https://www.amd.com/content/dam/amd/en/documents/instinct-tech-docs/instruction-set-architectures/)
- [AMD Machine-Readable ISA](https://gpuopen.com/machine-readable-isa/)
