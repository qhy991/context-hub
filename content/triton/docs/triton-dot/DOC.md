---
name: triton-dot
description: Matrix product of two blocks via Tensor Core or MMA instructions
metadata:
  languages: triton
  versions: '2.1'
  revision: 1
  updated-on: '2026-06-16'
  source: official
  tags: triton,gpu,linear-algebra,dot,matmul,tensor-core
---

# tl.dot

Returns the matrix product of two blocks.

## Syntax

```python
tl.dot(a, b, acc=None, out_dtype=tl.float32, allow_tf32=True, max_num_imprecise_acc=None)
```

## Description

Computes the matrix product of two blocks. On NVIDIA GPUs, this maps to Tensor Core operations (wmma/mma instructions) for float16 and bfloat16 inputs. On AMD GPUs, it maps to MFMA instructions. The result is accumulated with `acc` if provided, enabling tile-based tiled matrix multiplication. `input_precision` controls the internal precision of the Tensor Core operation.

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| a | Block | Left operand (M × K) |
| b | Block | Right operand (K × N) |
| acc | Block (optional) | Accumulator to add the result to |
| out_dtype | tl.dtype | Output data type (default tl.float32) |
| allow_tf32 | bool | Allow TF32 precision (default True) |
| max_num_imprecise_acc | int (optional) | Max number of imprecise accumulations |

## Semantics

```pseudo
C = a × b
if acc is not None:
    C = C + acc
return C
```

## Triton Version

Triton 2.1+

## Target Architecture

NVIDIA GPU (SM 7.0+ with Tensor Cores), AMD GPU (CDNA2+ with MFMA)

## Related Instructions

- [tl.dot_scaled](../triton-dot-scaled/DOC.md)
- [tl.reduce](../triton-reduce/DOC.md)

## Example

```python
import triton.language as tl

@triton.jit
def matmul_tile_kernel(a_ptr, b_ptr, c_ptr, M, N, K,
                        BLOCK_M: tl.constexpr, BLOCK_N: tl.constexpr, BLOCK_K: tl.constexpr):
    pid_m = tl.program_id(0)
    pid_n = tl.program_id(1)

    offs_m = pid_m * BLOCK_M + tl.arange(0, BLOCK_M)
    offs_n = pid_n * BLOCK_N + tl.arange(0, BLOCK_N)
    offs_k = tl.arange(0, BLOCK_K)

    a_ptrs = a_ptr + offs_m[:, None] * K + offs_k[None, :]
    b_ptrs = b_ptr + offs_k[:, None] * N + offs_n[None, :]

    accumulator = tl.zeros((BLOCK_M, BLOCK_N), dtype=tl.float32)
    for k in range(0, K, BLOCK_K):
        a = tl.load(a_ptrs, mask=offs_m[:, None] < M)
        b = tl.load(b_ptrs, mask=offs_n[None, :] < N)
        accumulator = tl.dot(a, b, accumulator)
        a_ptrs += BLOCK_K
        b_ptrs += BLOCK_K

    c_ptrs = c_ptr + offs_m[:, None] * N + offs_n[None, :]
    tl.store(c_ptrs, accumulator, mask=offs_m[:, None] < M)
```