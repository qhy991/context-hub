---
name: isa-v-cvt-scalef32-pk32-fp6-f16
description: "Scale a packed 32-component half-precision float input using the exponent provided by the second single-precision float input, then convert the values to a packed 32-component FP6 float value. Store the result into a vector register."
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

# V_CVT_SCALEF32_PK32_FP6_F16

Scale a packed 32-component half-precision float input using the exponent provided by the second single-precision float input, then convert the values to a packed 32-component FP6 float value. Store the result into a vector register.

## Encoding

Encoding: `ENC_VOP3`
Opcode: `600`


## Operands

| Field | Type | Size | Direction | Implicit |
|-------|------|------|-----------|----------|
| VDST | VGPR | 192bit | out | no |
| SRC0 | SRC_VGPR | 512bit | in | no |
| SRC1 | SRC_SIMPLE | 32bit | in | no |


## References

- [AMD CDNA 4 ISA Reference Guide](https://www.amd.com/content/dam/amd/en/documents/instinct-tech-docs/instruction-set-architectures/)
- [AMD Machine-Readable ISA](https://gpuopen.com/machine-readable-isa/)
