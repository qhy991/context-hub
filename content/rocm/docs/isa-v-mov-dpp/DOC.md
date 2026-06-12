---
name: isa-v-mov-dpp
description: "Data-Parallel Primitive (DPP) move: cross-lane data movement within a wavefront. Core mechanism for warp-level reductions and shuffles on AMD GPUs."
metadata:
  languages: hip
  architectures: cdna1,cdna2,cdna3,cdna4
  versions: 'GCN3+'
  revision: 1
  updated-on: '2026-06-12'
  source: official
  tags: rocm,gpu,dpp,isa,cross-lane,compute,cdna,wavefront
  isa_category: compute
  instruction_type: VOP1_DPP
  hw_unit: simd-unit
---

# v_mov_dpp

Data-Parallel Primitive move instruction. Moves vector data between lanes (threads) within a wavefront using programmable permutation patterns.

## Syntax

```asm
v_mov_dpp v5, v0  quad_perm:[0,1,2,3]  row_mask:0xf  bank_mask:0xf  bound_ctrl:1
v_mov_dpp v5, v0  row_shl:1            row_mask:0xf  bank_mask:0xf
v_mov_dpp v5, v0  wave_ror:1           row_mask:0xf  bank_mask:0xf
v_mov_dpp v5, v0  row_mirror           row_mask:0xf  bank_mask:0xf
```

## Operands

| Operand | Description |
|---------|-------------|
| vdst | Destination VGPR (per-lane result) |
| vsrc | Source VGPR (per-lane input) |
| dpp_ctrl | Permutation mode (see below) |
| row_mask | 4-bit mask selecting which rows participate |
| bank_mask | 4-bit mask selecting which banks participate |
| bound_ctrl:0/1 | 0=inactive lanes get 0, 1=keep original value |

## Permutation Modes

| Mode | Syntax | Description |
|------|--------|-------------|
| **Quad perm** | `quad_perm:[q0,q1,q2,q3]` | Shuffle within groups of 4 lanes |
| **Row shift left** | `row_shl:N` | Shift all lanes left by N (0-15) |
| **Row shift right** | `row_shr:N` | Shift all lanes right by N (0-15) |
| **Row rotate right** | `row_ror:N` | Rotate lanes right by N (0-15) |
| **Wave rotate right** | `wave_ror:N` | Rotate across entire wavefront |
| **Row mirror** | `row_mirror` | Mirror within rows |
| **Row half mirror** | `row_half_mirror` | Mirror within half-rows |

## CUDA Equivalence

| CUDA | AMD DPP |
|------|---------|
| `__shfl_sync(mask, var, srcLane, width)` | `v_mov_dpp` with `quad_perm` or `wave_ror` |
| `__shfl_up_sync(mask, var, delta, width)` | `v_mov_dpp` with `row_shr:delta` |
| `__shfl_down_sync(mask, var, delta, width)` | `v_mov_dpp` with `row_shl:delta` |
| `__shfl_xor_sync(mask, var, laneMask, width)` | `v_mov_bperm` (bypass LDS) |

## HIP Intrinsic

```c
// HIP provides built-in warp shuffle functions (mapped to DPP)
float val = __shfl(float_val, src_lane);       // → v_mov_dpp wave_ror
float val = __shfl_up(float_val, delta);        // → v_mov_dpp row_shr
float val = __shfl_down(float_val, delta);      // → v_mov_dpp row_shl
float val = __shfl_xor(float_val, lane_mask);   // → ds_bpermute

// Direct DPP control (via inline asm)
float result;
asm volatile("v_mov_dpp %0, %1 row_shl:1 row_mask:0xf bank_mask:0xf"
    : "=v"(result) : "v"(input));
```

## Common Patterns

### Warp-Level Reduction (Sum)
```c
// Sum reduction across wavefront using DPP
float sum = value;
sum += __shfl_xor(sum, 32);  // MI300: 64-lane wavefront
sum += __shfl_xor(sum, 16);
sum += __shfl_xor(sum, 8);
sum += __shfl_xor(sum, 4);
sum += __shfl_xor(sum, 2);
sum += __shfl_xor(sum, 1);
```

### Quad-Level Shuffle
```c
// Shuffle within group of 4 threads (optimal for MFMA tiling)
asm volatile("v_mov_dpp %0, %1 quad_perm:[1,2,3,0] row_mask:0xf bank_mask:0xf"
    : "=v"(result) : "v"(input));
```

## Performance Notes

- DPP instructions use LDS routing hardware but **do not access LDS memory**
- Latency: ~4 cycles (same as simple VALU)
- No bank conflicts (hardware routing)
- Can be freely interleaved with MFMA instructions for latency hiding

## Architecture Support

| Architecture | Support | Notes |
|-------------|---------|-------|
| GCN 3+ | ✓ | Original DPP |
| CDNA1-4 | ✓ | Full DPP support |
| RDNA 1-4 | ✓ | Available in compute shaders |

## See Also

- `ds_bpermute_b32` — Arbitrary lane-to-lane via LDS bypass
- `v_permlane16_b32` — Static permutation (faster for fixed patterns)
- [AMD GCN Cross-Lane Operations](https://gpuopen.com/learn/amd-gcn-assembly-cross-lane-operations/)
- [SCALE: CUDA Shuffles to DPP](https://scale-lang.com/posts/2026-01-19-optimizing-cuda-shuffles)

## References

- [CDNA4 ISA Reference Guide](https://www.amd.com/content/dam/amd/en/documents/instinct-tech-docs/instruction-set-architectures/amd-instinct-cdna4-instruction-set-architecture.pdf)
- [AMD Machine-Readable ISA](https://gpuopen.com/machine-readable-isa/)
