---
name: isa-v-smfmac-f32-16x16x64-bf8-bf8
description: "Multiply the 16x64 sparse matrix in the first input by the 64x16 matrix in the second input and accumulate the result into the 16x16 matrix stored in the destination registers using fused multiply add. Sparse indexes for the first matrix are given in the third input."
metadata:
  languages: hip
  architectures: cdna1,cdna2,cdna3,cdna4
  versions: 'CDNA4+'
  revision: 1
  updated-on: '2026-06-12'
  source: official
  tags: rocm,gpu,v,isa,matrix-core,compute,matrix-core,mfma,fp8
  isa_category: compute
  instruction_type: VOP3P
  hw_unit: matrix-core
  func_group: VALU
  arch_name: AMD CDNA 4
---

# V_SMFMAC_F32_16X16X64_BF8_BF8

Multiply the 16x64 sparse matrix in the first input by the 64x16 matrix in the second input and accumulate the result into the 16x16 matrix stored in the destination registers using fused multiply add. Sparse indexes for the first matrix are given in the third input.

## Encoding

Encoding: `VOP3P_MFMA`
Opcode: `120`


## Operands

| Field | Type | Size | Direction | Implicit |
|-------|------|------|-----------|----------|
| VDST | VGPR_OR_ACCVGPR | 128bit | out | no |
| SRC0 | SRC_VGPR_OR_ACCVGPR | 64bit | in | no |
| SRC1 | SRC_VGPR_OR_ACCVGPR | 128bit | in | no |
| SRC2 | SRC_VGPR | 32bit | in | no |


## References

- [AMD CDNA 4 ISA Reference Guide](https://www.amd.com/content/dam/amd/en/documents/instinct-tech-docs/instruction-set-architectures/)
- [AMD Machine-Readable ISA](https://gpuopen.com/machine-readable-isa/)
