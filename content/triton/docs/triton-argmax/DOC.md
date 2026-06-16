---
name: triton-argmax
description: Returns the indices of the maximum values along an axis
metadata:
  languages: triton
  versions: '2.1'
  revision: 1
  updated-on: '2026-06-16'
  source: official
  tags: triton,gpu,reduction,argmax,index
---

# tl.argmax

Returns the indices of the maximum values along the given axis.

## Syntax

```python
tl.argmax(input, axis, keep_dims=False)
```

## Description

Computes the indices of the maximum values along the specified axis. This is equivalent to calling `tl.max(input, axis, return_indices=True)` and extracting the index component.

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| input | Block | Input tensor |
| axis | int | Axis along which to find argmax |
| keep_dims | bool | Whether to retain the reduced axis (default False) |

## Returns

| Type | Description |
|------|-------------|
| Block | Tensor of indices (int32) of the maximum values |

## Triton Version

Triton 2.1+

## Target Architecture

NVIDIA GPU (SM 7.0+), AMD GPU (CDNA2+), Intel GPU

## Related Instructions

- [tl.argmin](../triton-argmin/DOC.md)
- [tl.max](../triton-max/DOC.md)

## Example

```python
import triton.language as tl

# Find the index of the maximum value per row
x = tl.load(x_ptr + offsets)
max_idx = tl.argmax(x, axis=1)
```