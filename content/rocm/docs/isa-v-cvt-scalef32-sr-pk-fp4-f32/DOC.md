---
name: isa-v-cvt-scalef32-sr-pk-fp4-f32
description: "Scale a packed 2-component single-precision float input using the exponent provided by the third single-precision float input, then convert the values to a packed FP4 float value with stochastic rounding using seed data from the second input. Store the result into 8 bits of a vector register using OPSEL[3:2] to determine which byte of the destination to overwrite."
metadata:
  languages: hip
  architectures: cdna4
  versions: 'CDNA4+'
  revision: 1
  updated-on: '2026-06-12'
  source: official
  tags: rocm,gpu,v,isa,simd-unit,compute
  isa_category: compute
  instruction_type: VOP
  hw_unit: simd-unit
  func_group: VALU
  arch_name: AMD CDNA 4
---

# V_CVT_SCALEF32_SR_PK_FP4_F32

Scale a packed 2-component single-precision float input using the exponent provided by the third single-precision float input, then convert the values to a packed FP4 float value with stochastic rounding using seed data from the second input. Store the result into 8 bits of a vector register using OPSEL[3:2] to determine which byte of the destination to overwrite.

## Encoding

Encoding: `ENC_VOP3`
Opcode: `574`


## Operands

| Field | Type | Size | Direction | Implicit |
|-------|------|------|-----------|----------|
| VDST | VGPR | 8bit | out | no |
| SRC0 | SRC_VGPR | 64bit | in | no |
| SRC1 | SRC_SIMPLE | 32bit | in | no |
| SRC2 | SRC_SIMPLE | 32bit | in | no |


## References

- [AMD CDNA 4 ISA Reference Guide](https://www.amd.com/content/dam/amd/en/documents/instinct-tech-docs/instruction-set-architectures/)
- [AMD Machine-Readable ISA](https://gpuopen.com/machine-readable-isa/)
