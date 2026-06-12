---
name: isa-v-mfma-f32-16x16x16f16
description: "Matrix Fused Multiply-Add: 16x16x16 F16 input, F32 accumulation. Primary instruction for mixed-precision FP16 GEMM."
metadata:
  languages: hip
  architectures: cdna1,cdna2,cdna3,cdna4
  versions: 'CDNA1+'
  revision: 1
  updated-on: '2026-06-12'
  source: official
  tags: rocm,gpu,mfma,isa,matrix-core,compute,gemm,fp16,cdna
  isa_category: compute
  instruction_type: VOP3P
  hw_unit: matrix-core
---

# v_mfma_f32_16x16x16f16

Matrix Fused Multiply-Accumulate: FP16 inputs with F32 accumulation. The most commonly used MFMA variant for deep learning workloads.

## Syntax

```asm
v_mfma_f32_16x16x16f16 v[0:15], v[0:7], v[8:15], v[0:15]
```

## Operands

| Operand | Type | Count | Description |
|---------|------|-------|-------------|
| v[dst:dst+15] | VGPR | 16 | 16x16 F32 accumulator |
| srcA | VGPR | 8 | 16x16 FP16 input matrix A (packed as 8 VGPRs, 2xf16 per VGPR) |
| srcB | VGPR | 8 | 16x16 FP16 input matrix B (packed as 8 VGPRs) |
| v[src:src+15] | VGPR | 16 | Previous F32 accumulator |

## Description

Computes `D += A * B` where:
- A is 16x16 FP16 matrix (8 VGPRs, 2 elements packed per register)
- B is 16x16 FP16 matrix (8 VGPRs, 2 elements packed per register)
- D is 16x16 F32 accumulator (16 VGPRs)

**This is the workhorse instruction for FP16 GEMM on AMD GPUs** — equivalent to NVIDIA's `wmma.mma.sync` or `wgmma.mma_async` with FP16 inputs.

## Compute Density

| Metric | Value |
|--------|-------|
| Input elements | 2 × 16×16 = 512 FP16 values |
| FLOPs per instruction | 2 × 16×16×16 = 8192 FLOPs |
| VGPR input | 16 (8+8) |
| VGPR output | 16 |
| FLOPs/VGPR ratio | 512 (very high) |

## Architecture Throughput

| Architecture | Peak TFLOPS (FP16) | Notes |
|-------------|-------------------|-------|
| MI100 (CDNA1) | 184.6 | |
| MI250X (CDNA2) | 383.0 | |
| MI300X (CDNA3) | 654.7 | Dual CMA |
| MI350X (CDNA4) | ~900+ | Enhanced CMA |

## HIP Example

```c
#include <rocwmma/rocwmma.h>

using namespace rocwmma;

// 16x16x16 FP16 GEMM tile
fragment<matrix_a, 16, 16, 16, half, row_major> a_frag;
fragment<matrix_b, 16, 16, 16, half, col_major> b_frag;
fragment<accumulator, 16, 16, 16, float> c_frag;

fill_fragment(c_frag, 0.0f);
load_matrix_sync(a_frag, a_ptr + k * 16, 16);  // K-dimension stride
load_matrix_sync(b_frag, b_ptr + k * 16, 16);
mma_sync(c_frag, a_frag, b_frag, c_frag);
// c_frag now holds 16x16 F32 results
```

## Data Layout

FP16 input matrices are packed 2-per-VGPR:
```
VGPR[0] = [A[0][0], A[0][1]]  // two fp16 values
VGPR[1] = [A[0][2], A[0][3]]
...
VGPR[7] = [A[7][14], A[7][15]]  // 8 VGPRs for 16x16 fp16
```

## Performance Tips

1. **Double buffer**: Load next A/B tiles while computing current MFMA
2. **Interleave with DS reads**: Hide memory latency with compute
3. **Use CK library**: Composable Kernel handles tiling automatically
4. **Prefer over 32x32x8 variant** when register pressure is a concern

## See Also

- `v_mfma_f32_32x32x8f16` — Larger tile variant
- `v_mfma_f32_16x16x32f8f6f4` — FP8 input variant (CDNA3+)
- [Matrix Core Programming CDNA3/CDNA4](https://rocm.blogs.amd.com/software-tools-optimization/matrix-cores-cdna/README.html)
- [Composable Kernel Library](https://github.com/ROCm/composable_kernel)

## References

- [CDNA4 ISA Reference Guide](https://www.amd.com/content/dam/amd/en/documents/instinct-tech-docs/instruction-set-architectures/amd-instinct-cdna4-instruction-set-architecture.pdf)
- [AMD Machine-Readable ISA](https://gpuopen.com/machine-readable-isa/)
