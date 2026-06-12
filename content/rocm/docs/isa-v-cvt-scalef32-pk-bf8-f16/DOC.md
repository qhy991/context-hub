---
name: isa-v-cvt-scalef32-pk-bf8-f16
description: "Scale a packed 2-component half-precision float input using the exponent provided by the second single-precision float input, then convert the values to a packed BF8 float value with round toward nearest even semantics. Store the result into 16 bits of a vector register using OPSEL."
metadata:
  languages: hip
  architectures: cdna1,cdna2,cdna3,cdna4
  versions: 'CDNA4+'
  revision: 1
  updated-on: '2026-06-12'
  source: official
  tags: rocm,gpu,v,isa,simd-unit,compute,low-precision,fp8
  isa_category: compute
  instruction_type: VOP
  hw_unit: simd-unit
  func_group: VALU
  arch_name: AMD CDNA 4
---

# V_CVT_SCALEF32_PK_BF8_F16

Scale a packed 2-component half-precision float input using the exponent provided by the second single-precision float input, then convert the values to a packed BF8 float value with round toward nearest even semantics. Store the result into 16 bits of a vector register using OPSEL.

## Encoding

Encoding: `ENC_VOP3`
Opcode: `577`


## Operands

| Field | Type | Size | Direction | Implicit |
|-------|------|------|-----------|----------|
| VDST | VGPR | 16bit | out | no |
| SRC0 | SRC_NOLIT | 32bit | in | no |
| SRC1 | SRC_SIMPLE | 32bit | in | no |


## References

- [AMD CDNA 4 ISA Reference Guide](https://www.amd.com/content/dam/amd/en/documents/instinct-tech-docs/instruction-set-architectures/)
- [AMD Machine-Readable ISA](https://gpuopen.com/machine-readable-isa/)
