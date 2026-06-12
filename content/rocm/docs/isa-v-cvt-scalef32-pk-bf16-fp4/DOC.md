---
name: isa-v-cvt-scalef32-pk-bf16-fp4
description: "Convert from a packed 2-component FP4 float input to a packed BF16 float value, then scale the packed values using the exponent provided by the second single-precision float input. Store the result into a vector register. The value to convert is loaded from 8 bits of the input using OPSEL[1:0] to determine which byte to read."
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

# V_CVT_SCALEF32_PK_BF16_FP4

Convert from a packed 2-component FP4 float input to a packed BF16 float value, then scale the packed values using the exponent provided by the second single-precision float input. Store the result into a vector register. The value to convert is loaded from 8 bits of the input using OPSEL[1:0] to determine which byte to read.

## Encoding

Encoding: `ENC_VOP3`
Opcode: `593`


## Operands

| Field | Type | Size | Direction | Implicit |
|-------|------|------|-----------|----------|
| VDST | VGPR | 32bit | out | no |
| SRC0 | SRC_NOLIT | 8bit | in | no |
| SRC1 | SRC_SIMPLE | 32bit | in | no |


## References

- [AMD CDNA 4 ISA Reference Guide](https://www.amd.com/content/dam/amd/en/documents/instinct-tech-docs/instruction-set-architectures/)
- [AMD Machine-Readable ISA](https://gpuopen.com/machine-readable-isa/)
