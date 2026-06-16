---
name: triton-make-tensor-descriptor
description: Create a tensor descriptor for TMA-based load/store (SM 9.0+)
metadata:
  languages: triton
  versions: '3.0'
  revision: 1
  updated-on: '2026-06-16'
  source: official
  tags: triton,gpu,tma,descriptor,hopper,blackwell
---

# tl.make_tensor_descriptor

Create a tensor descriptor object for TMA (Tensor Memory Accelerator) operations.

## Syntax

```python
tl.make_tensor_descriptor(base, shape, strides, block_shape, padding_option="zero")
```

## Description

Creates a tensor descriptor that describes a tile of a tensor in global memory. The descriptor is consumed by `.load()` and `.store()` methods on the descriptor object to perform hardware-accelerated TMA transfers. TMA provides asynchronous, high-bandwidth data movement between global and shared memory on NVIDIA Hopper (SM 9.0+) and Blackwell (SM 10.0+) GPUs.

`tl.make_block_ptr` is deprecated in favor of this API.

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| base | pointer | Base pointer to the tensor in global memory |
| shape | tuple | Shape of the full tensor |
| strides | tuple | Strides of the full tensor |
| block_shape | tuple | Shape of the tile to load/store |
| padding_option | str | Padding mode: `"zero"` (default) |

## Returns

| Type | Description |
|------|-------------|
| tensor_descriptor | Descriptor object with `.load(offsets)` and `.store(offsets, value)` methods |

## Semantics

```pseudo
desc = create_descriptor(base, shape, strides, block_shape)
# On each iteration:
tile = desc.load([row_offset, col_offset])  # TMA async copy G→S
```

## Triton Version

Triton 3.0+

## Target Architecture

NVIDIA GPU (SM 9.0+ Hopper / SM 10.0+ Blackwell)

## Related Instructions

- [tl.load_tensor_descriptor](../triton-load-tensor-desc/DOC.md)
- [tl.store_tensor_descriptor](../triton-store-tensor-desc/DOC.md)
- [TensorDescriptor (host-side)](../triton-tensor-desc-class/DOC.md)

## Example

```python
import triton.language as tl

@triton.jit
def tma_matmul_kernel(a_ptr, b_ptr, c_ptr, M, N, K,
                       BLOCK_M: tl.constexpr, BLOCK_N: tl.constexpr, BLOCK_K: tl.constexpr):
    pid_m = tl.program_id(0)
    pid_n = tl.program_id(1)

    # Create descriptors for TMA tiles
    a_desc = tl.make_tensor_descriptor(
        a_ptr, shape=[M, K], strides=[K, 1],
        block_shape=[BLOCK_M, BLOCK_K])
    b_desc = tl.make_tensor_descriptor(
        b_ptr, shape=[K, N], strides=[N, 1],
        block_shape=[BLOCK_K, BLOCK_N])
    c_desc = tl.make_tensor_descriptor(
        c_ptr, shape=[M, N], strides=[N, 1],
        block_shape=[BLOCK_M, BLOCK_N])

    offs_am = pid_m * BLOCK_M
    offs_bn = pid_n * BLOCK_N
    accumulator = tl.zeros((BLOCK_M, BLOCK_N), dtype=tl.float32)

    for k in range(0, K, BLOCK_K):
        a = a_desc.load([offs_am, k])       # TMA load
        b = b_desc.load([k, offs_bn])       # TMA load
        accumulator = tl.dot(a, b, accumulator)
        tl.debug_barrier()

    c_desc.store([offs_am, offs_bn], accumulator)  # TMA store
```