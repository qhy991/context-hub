---
name: triton-full
description: Returns a tensor filled with a scalar value
metadata:
  languages: triton
  versions: '2.1'
  revision: 1
  updated-on: '2026-06-16'
  source: official
  tags: triton,gpu,creation,full,initialization
---

# tl.full

Returns a tensor filled with a scalar value of the given shape and dtype.

## Syntax

```python
tl.full(shape, value, dtype=tl.float32)
```

## Description

Creates a tensor of the specified shape and dtype, with every element set to `value`. Useful for initializing buffers to a constant value (e.g., `-inf` for masked softmax, or `1.0` for multiplicative accumulators).

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| shape | tuple | Shape of the output tensor |
| value | scalar | Fill value |
| dtype | tl.dtype | Data type (default tl.float32) |

## Returns

| Type | Description |
|------|-------------|
| Block | Tensor filled with `value` |

## Triton Version

Triton 2.1+

## Target Architecture

NVIDIA GPU (SM 7.0+), AMD GPU (CDNA2+), Intel GPU

## Related Instructions

- [tl.zeros](../triton-zeros/DOC.md)
- [tl.arange](../triton-arange/DOC.md)

## Example

```python
import triton.language as tl

# Initialize with -inf for masked attention
neg_inf = tl.full((BLOCK_M, BLOCK_N), float('-inf'), dtype=tl.float32)

# Initialize product accumulator with 1.0
ones = tl.full((BLOCK_M, BLOCK_N), 1.0, dtype=tl.float32)
```