---
name: isa-v-cvt-scalef32-pk-fp4-bf16
description: "Scale a packed 2-component BF16 float input using the exponent provided by the second single-precision float input, then convert the values to a packed FP4 float value with round toward nearest even semantics. Store the result into 8 bits of a vector register using OPSEL[3:2] to determine which byte of the destination to overwrite."
metadata:
  languages: hip
  architectures: cdna4
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

# V_CVT_SCALEF32_PK_FP4_BF16

Scale a packed 2-component BF16 float input using the exponent provided by the second single-precision float input, then convert the values to a packed FP4 float value with round toward nearest even semantics. Store the result into 8 bits of a vector register using OPSEL[3:2] to determine which byte of the destination to overwrite.

## Encoding

Encoding: `ENC_VOP3`
Opcode: `589`


## Operands

| Field | Type | Size | Direction | Implicit |
|-------|------|------|-----------|----------|
| VDST | VGPR | 8bit | out | no |
| SRC0 | SRC_NOLIT | 32bit | in | no |
| SRC1 | SRC_SIMPLE | 32bit | in | no |


## References

- [AMD CDNA 4 ISA Reference Guide](https://www.amd.com/content/dam/amd/en/documents/instinct-tech-docs/instruction-set-architectures/)
- [AMD Machine-Readable ISA](https://gpuopen.com/machine-readable-isa/)
