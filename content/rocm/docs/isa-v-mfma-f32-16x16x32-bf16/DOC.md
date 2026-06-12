---
name: isa-v-mfma-f32-16x16x32-bf16
description: "Multiply the 16x32 matrix in the first input by the 32x16 matrix in the second input and add the 16x16 matrix in the third input using fused multiply add. Store the resulting matrix into vector registers."
metadata:
  languages: hip
  architectures: cdna1,cdna2,cdna3,cdna4
  versions: 'CDNA4+'
  revision: 1
  updated-on: '2026-06-12'
  source: official
  tags: rocm,gpu,v,isa,matrix-core,compute,matrix-core,mfma,low-precision
  isa_category: compute
  instruction_type: VOP3P
  hw_unit: matrix-core
  func_group: VALU
  arch_name: AMD CDNA 4
---

# V_MFMA_F32_16X16X32_BF16

Multiply the 16x32 matrix in the first input by the 32x16 matrix in the second input and add the 16x16 matrix in the third input using fused multiply add. Store the resulting matrix into vector registers.

## Encoding

Encoding: `VOP3P_MFMA`
Opcode: `53`


## Operands

| Field | Type | Size | Direction | Implicit |
|-------|------|------|-----------|----------|
| VDST | VGPR_OR_ACCVGPR | 128bit | out | no |
| SRC0 | SRC_VGPR_OR_ACCVGPR | 128bit | in | no |
| SRC1 | SRC_VGPR_OR_ACCVGPR | 128bit | in | no |
| SRC2 | SRC_VGPR_OR_ACCVGPR_OR_CONST | 128bit | in | no |


## References

- [AMD CDNA 4 ISA Reference Guide](https://www.amd.com/content/dam/amd/en/documents/instinct-tech-docs/instruction-set-architectures/)
- [AMD Machine-Readable ISA](https://gpuopen.com/machine-readable-isa/)
