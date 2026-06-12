---
name: isa-v-cvt-sr-f16-f32
description: "Convert from a single-precision float input to a half-precision value with stochastic rounding using seed data from the second input. Store the result into 16 bits of a vector register using OPSEL to determine which word of the destination to overwrite."
metadata:
  languages: hip
  architectures: cdna1,cdna2,cdna3,cdna4
  versions: 'CDNA4+'
  revision: 1
  updated-on: '2026-06-12'
  source: official
  tags: rocm,gpu,v,isa,simd-unit,compute,low-precision
  isa_category: compute
  instruction_type: VOP
  hw_unit: simd-unit
  func_group: VALU
  arch_name: AMD CDNA 4
---

# V_CVT_SR_F16_F32

Convert from a single-precision float input to a half-precision value with stochastic rounding using seed data from the second input. Store the result into 16 bits of a vector register using OPSEL to determine which word of the destination to overwrite.

## Encoding

Encoding: `ENC_VOP3`
Opcode: `678`


## Operands

| Field | Type | Size | Direction | Implicit |
|-------|------|------|-----------|----------|
| VDST | VGPR | 16bit | out | no |
| SRC0 | SRC_NOLIT | 32bit | in | no |
| SRC1 | SRC_SIMPLE | 32bit | in | no |


## References

- [AMD CDNA 4 ISA Reference Guide](https://www.amd.com/content/dam/amd/en/documents/instinct-tech-docs/instruction-set-architectures/)
- [AMD Machine-Readable ISA](https://gpuopen.com/machine-readable-isa/)
