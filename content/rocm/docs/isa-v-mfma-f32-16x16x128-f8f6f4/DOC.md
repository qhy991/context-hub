---
name: isa-v-mfma-f32-16x16x128-f8f6f4
description: "Multiply the 16x128 matrix in the first input by the 128x16 matrix in the second input and add the 16x16 matrix in the third input using fused multiply add. Store the resulting matrix into vector registers."
metadata:
  languages: hip
  architectures: cdna4
  versions: 'CDNA4+'
  revision: 1
  updated-on: '2026-06-12'
  source: official
  tags: rocm,gpu,v,isa,matrix-core,compute,mfma,fp8
  isa_category: compute
  instruction_type: VOP3P
  hw_unit: matrix-core
  func_group: VALU
  arch_name: AMD CDNA 4
---

# V_MFMA_F32_16X16X128_F8F6F4

Multiply the 16x128 matrix in the first input by the 128x16 matrix in the second input and add the 16x16 matrix in the third input using fused multiply add. Store the resulting matrix into vector registers.

## Encoding

Encoding: `VOP3P_MFMA`
Opcode: `45`


## Operands

| Field | Type | Size | Direction | Implicit |
|-------|------|------|-----------|----------|
| VDST | VGPR_OR_ACCVGPR | 128bit | out | no |
| SRC0 | SRC_VGPR_OR_ACCVGPR | 256bit | in | no |
| SRC1 | SRC_VGPR_OR_ACCVGPR | 256bit | in | no |
| SRC2 | SRC_VGPR_OR_ACCVGPR_OR_CONST | 128bit | in | no |


## References

- [AMD CDNA 4 ISA Reference Guide](https://www.amd.com/content/dam/amd/en/documents/instinct-tech-docs/instruction-set-architectures/)
- [AMD Machine-Readable ISA](https://gpuopen.com/machine-readable-isa/)

## Semantics
Matrix-Fused Multiply-Add using emerging FP8 formats. Processes an exceptionally deep 128-element dimension per step to heavily amortize register loading costs, accelerating transformer inference.

## Example
```cpp
// Conceptual usage for FP8 matrix operations
__device__ void mfma_16x16x128_fp8(float& d_out, uint32_t a[4], uint32_t b[4], float c) {
    d_out = __builtin_amdgcn_mfma_f32_16x16x128_f8f6f4(a, b, c, 0, 0, 0);
}
```
