---
name: triton-argmin
description: Returns the indices of the minimum values along an axis
metadata:
  languages: triton
  versions: '2.1'
  revision: 1
  updated-on: '2026-06-16'
  source: official
  tags: triton,gpu,reduction,argmin,index
---

# tl.argmin

Returns the indices of the minimum values along the given axis.

## Syntax

```python
tl.argmin(input, axis, keep_dims=False)
```

## Description

Computes the indices of the minimum values along the specified axis. This is equivalent to calling `tl.min(input, axis, return_indices=True)` and extracting the index component.

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| input | Block | Input tensor |
| axis | int | Axis along which to find argmin |
| keep_dims | bool | Whether to retain the reduced axis (default False) |

## Returns

| Type | Description |
|------|-------------|
| Block | Tensor of indices (int32) of the minimum values |

## Triton Version

Triton 2.1+

## Target Architecture

NVIDIA GPU (SM 7.0+), AMD GPU (CDNA2+), Intel GPU

## Related Instructions

- [tl.argmax](../triton-argmax/DOC.md)
- [tl.min](../triton-min/DOC.md)

## Example

```python
import triton.language as tl

# Find the index of the minimum value per row
x = tl.load(x_ptr + offsets)
min_idx = tl.argmin(x, axis=1)
```