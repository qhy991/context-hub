---
name: triton-view
description: Return a tensor with a different shape but same underlying elements
metadata:
  languages: triton
  versions: '2.1'
  revision: 1
  updated-on: '2026-06-16'
  source: official
  tags: triton,gpu,shape,view
---

# tl.view

Returns a tensor with a different shape but the same underlying elements.

## Syntax

```python
tl.view(tensor, shape)
```

## Description

Returns a view of `tensor` with the given shape. The total number of elements must remain the same. This is a zero-cost operation — no data is copied. Useful for reshaping data between different computation phases without extra memory transfers.

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| tensor | Block | Input tensor |
| shape | tuple | New shape (must have same number of elements) |

## Returns

| Type | Description |
|------|-------------|
| Block | Tensor with new shape, sharing the same data |

## Triton Version

Triton 2.1+

## Target Architecture

NVIDIA GPU (SM 7.0+), AMD GPU (CDNA2+), Intel GPU

## Related Instructions

- [tl.reshape](../triton-reshape/DOC.md)
- [tl.trans](../triton-trans/DOC.md)
- [tl.broadcast_to](../triton-broadcast-to/DOC.md)

## Example

```python
import triton.language as tl

# Load a flat buffer and view as 2D
x = tl.load(x_ptr + offsets)  # shape (BLOCK_M * BLOCK_N,)
x_2d = tl.view(x, (BLOCK_M, BLOCK_N))

# View back to 1D
x_flat = tl.view(x_2d, (BLOCK_M * BLOCK_N,))
```