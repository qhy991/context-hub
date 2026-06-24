---
name: isa-v-mfma-f32-32x32x64-f8f6f4
description: "Multiply the 32x64 matrix in the first input by the 64x32 matrix in the second input and add the 32x32 matrix in the third input using fused multiply add. Store the resulting matrix into vector registers."
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

# V_MFMA_F32_32X32X64_F8F6F4

Multiply the 32x64 matrix in the first input by the 64x32 matrix in the second input and add the 32x32 matrix in the third input using fused multiply add. Store the resulting matrix into vector registers.

## Encoding

Encoding: `VOP3P_MFMA`
Opcode: `46`


## Operands

| Field | Type | Size | Direction | Implicit |
|-------|------|------|-----------|----------|
| VDST | VGPR_OR_ACCVGPR | 512bit | out | no |
| SRC0 | SRC_VGPR_OR_ACCVGPR | 256bit | in | no |
| SRC1 | SRC_VGPR_OR_ACCVGPR | 256bit | in | no |
| SRC2 | SRC_VGPR_OR_ACCVGPR_OR_CONST | 512bit | in | no |


## References

- [AMD CDNA 4 ISA Reference Guide](https://www.amd.com/content/dam/amd/en/documents/instinct-tech-docs/instruction-set-architectures/)
- [AMD Machine-Readable ISA](https://gpuopen.com/machine-readable-isa/)

## Semantics
Matrix-Fused Multiply-Add using FP8 for large 32x32 matrix tiles with an inner dimension of 64. Drastically increases computational density on CDNA3/4 architectures.

## Example
```cpp
// Conceptual usage for FP8 32x32x64
__device__ void mfma_32x32x64_fp8(float& d_out, uint32_t a[2], uint32_t b[2], float c) {
    d_out = __builtin_amdgcn_mfma_f32_32x32x64_f8f6f4(a, b, c, 0, 0, 0);
}
```
