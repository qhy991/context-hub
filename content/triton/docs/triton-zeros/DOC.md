---
name: triton-zeros
description: Returns a tensor filled with zeros
metadata:
  languages: triton
  versions: '2.1'
  revision: 1
  updated-on: '2026-06-16'
  source: official
  tags: triton,gpu,creation,zeros,initialization
---

# tl.zeros

Returns a tensor filled with zeros of the given shape and dtype.

## Syntax

```python
tl.zeros(shape, dtype=tl.float32)
```

## Description

Creates a tensor of the specified shape and dtype, initialized to zero. Typically used to initialize accumulators before tiled computation loops (e.g., matrix multiplication accumulator, running sum).

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| shape | tuple | Shape of the output tensor |
| dtype | tl.dtype | Data type (default tl.float32) |

## Returns

| Type | Description |
|------|-------------|
| Block | Zero-filled tensor of the given shape and dtype |

## Triton Version

Triton 2.1+

## Target Architecture

NVIDIA GPU (SM 7.0+), AMD GPU (CDNA2+), Intel GPU

## Related Instructions

- [tl.full](../triton-full/DOC.md)
- [tl.arange](../triton-arange/DOC.md)

## Example

```python
import triton.language as tl

# Initialize accumulator for tiled matmul
accumulator = tl.zeros((BLOCK_M, BLOCK_N), dtype=tl.float32)
for k in range(0, K, BLOCK_K):
    a = tl.load(a_ptrs)
    b = tl.load(b_ptrs)
    accumulator = tl.dot(a, b, accumulator)
    a_ptrs += BLOCK_K
    b_ptrs += BLOCK_K
```