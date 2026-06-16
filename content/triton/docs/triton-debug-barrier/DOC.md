---
name: triton-debug-barrier
description: Synchronization barrier for all threads in a block
metadata:
  languages: triton
  versions: '2.1'
  revision: 1
  updated-on: '2026-06-16'
  source: official
  tags: triton,gpu,sync,barrier,debug
---

# tl.debug_barrier

Inserts a barrier to synchronize all threads within a block.

## Syntax

```python
tl.debug_barrier()
```

## Description

Inserts a `__syncthreads()` barrier that ensures all threads in the block reach the same point before any proceed. This is essential for correctness when threads share data through shared memory. In TMA-based kernels, it's used between TMA loads and computation to ensure the async copy has completed.

## Hardware Unit

Synchronization Unit (intra-block)

## Parameters

None

## Triton Version

Triton 2.1+

## Target Architecture

NVIDIA GPU (SM 7.0+), AMD GPU (CDNA2+), Intel GPU

## Related Instructions

- [tl.device_assert](../triton-device-assert/DOC.md)

## Example

```python
import triton.language as tl

@triton.jit
def tma_matmul_kernel(a_desc, b_desc, c_desc, ...):
    for k in range(0, K, BLOCK_K):
        a = a_desc.load([offs_am, k])
        b = b_desc.load([k, offs_bn])
        tl.debug_barrier()  # Wait for TMA async copy to complete
        accumulator = tl.dot(a, b, accumulator)
        tl.debug_barrier()  # Wait for shared memory consumers to finish
```