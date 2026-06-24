---
name: isa-v-mfma-f32-32x32x2f32
description: "Multiply the 32x2 matrix in the first input by the 2x32 matrix in the second input and add the 32x32 matrix in the third input using fused multiply add. Store the resulting matrix into vector registers."
metadata:
  languages: hip
  architectures: cdna1,cdna2
  versions: 'CDNA2+'
  revision: 2
  updated-on: '2026-06-12'
  source: official
  tags: rocm,gpu,v,isa,matrix-core,compute,mfma
  isa_category: compute
  instruction_type: VOP3P
  hw_unit: matrix-core
  func_group: VALU
  arch_name: AMD CDNA 2
---

# V_MFMA_F32_32X32X2F32

Multiply the 32x2 matrix in the first input by the 2x32 matrix in the second input and add the 32x32 matrix in the third input using fused multiply add. Store the resulting matrix into vector registers.

## Encoding

Encoding: `VOP3P_MFMA`
Opcode: `68`


## Operands

| Field | Type | Size | Direction | Implicit |
|-------|------|------|-----------|----------|
| VDST | VGPR_OR_ACCVGPR | 512bit | out | no |
| SRC0 | SRC_VGPR_OR_ACCVGPR | 32bit | in | no |
| SRC1 | SRC_VGPR_OR_ACCVGPR | 32bit | in | no |
| SRC2 | SRC_VGPR_OR_ACCVGPR_OR_CONST | 512bit | in | no |


## References

- [AMD CDNA 2 ISA Reference Guide](https://www.amd.com/content/dam/amd/en/documents/instinct-tech-docs/instruction-set-architectures/)
- [AMD Machine-Readable ISA](https://gpuopen.com/machine-readable-isa/)

## Semantics
Matrix-Fused Multiply-Add for 32x32x2 single-precision tiles, accumulating into fp32. Reduces memory bandwidth pressure for operations bounded by throughput at fp32 precision.

## Example
```cpp
__device__ void mfma_32x32x2_fp32(float32_t& d_out, float2_t a, float2_t b, float32_t c) {
    d_out = __builtin_amdgcn_mfma_f32_32x32x2f32(a, b, c, 0, 0, 0);
}
```
