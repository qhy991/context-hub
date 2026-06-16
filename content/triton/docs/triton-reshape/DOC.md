---
name: triton-reshape
description: Return a tensor with the provided shape
metadata:
  languages: triton
  versions: '2.1'
  revision: 1
  updated-on: '2026-06-16'
  source: official
  tags: triton,gpu,shape,reshape
---

# tl.reshape

Returns a tensor with the provided shape.

## Syntax

```python
tl.reshape(tensor, shape)
```

## Description

Returns a tensor with the given shape. The total number of elements must remain the same. Similar to `tl.view`, but may reorder elements to ensure contiguity when needed.

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| tensor | Block | Input tensor |
| shape | tuple | New shape (must have same number of elements) |

## Returns

| Type | Description |
|------|-------------|
| Block | Reshaped tensor |

## Triton Version

Triton 2.1+

## Target Architecture

NVIDIA GPU (SM 7.0+), AMD GPU (CDNA2+), Intel GPU

## Related Instructions

- [tl.view](../triton-view/DOC.md)
- [tl.trans](../triton-trans/DOC.md)

## Example

```python
import triton.language as tl

# Reshape 1D load to 2D for matrix math
x = tl.load(x_ptr + offsets)  # shape (BLOCK_M * BLOCK_K,)
x_2d = tl.reshape(x, (BLOCK_M, BLOCK_K))
```