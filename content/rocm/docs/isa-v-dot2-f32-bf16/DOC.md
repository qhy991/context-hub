---
name: isa-v-dot2-f32-bf16
description: "Calculate the dot product of BF16 float 2-vectors from the first and second inputs, convert the product to single-precision float format, add the third input and store the result into a vector register."
metadata:
  languages: hip
  architectures: cdna4
  versions: 'CDNA4+'
  revision: 1
  updated-on: '2026-06-12'
  source: official
  tags: rocm,gpu,v,isa,matrix-core,compute,low-precision
  isa_category: compute
  instruction_type: VOP3P
  hw_unit: matrix-core
  func_group: VALU
  arch_name: AMD CDNA 4
---

# V_DOT2_F32_BF16

Calculate the dot product of BF16 float 2-vectors from the first and second inputs, convert the product to single-precision float format, add the third input and store the result into a vector register.

## Encoding

Encoding: `ENC_VOP3P`
Opcode: `26`


## Operands

| Field | Type | Size | Direction | Implicit |
|-------|------|------|-----------|----------|
| VDST | VGPR | 32bit | out | no |
| SRC0 | SRC_NOLIT | 32bit | in | no |
| SRC1 | SRC_SIMPLE | 32bit | in | no |
| SRC2 | SRC_SIMPLE | 32bit | in | no |


## References

- [AMD CDNA 4 ISA Reference Guide](https://www.amd.com/content/dam/amd/en/documents/instinct-tech-docs/instruction-set-architectures/)
- [AMD Machine-Readable ISA](https://gpuopen.com/machine-readable-isa/)
