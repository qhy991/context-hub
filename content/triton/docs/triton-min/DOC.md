---
name: triton-min
description: Compute the minimum of elements along a given axis
metadata:
  languages: triton
  versions: '2.1'
  revision: 1
  updated-on: '2026-06-16'
  source: official
  tags: triton,gpu,reduction,min
---

# tl.min

Returns the minimum of all elements in the input tensor along the provided axis.

## Syntax

```python
tl.min(input, axis, return_indices=False, keep_dims=False)
```

## Description

Computes the element-wise minimum along the specified axis. When `return_indices=True`, also returns the indices of the minimum values. This is a reduction operation that collapses the given dimension.

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| input | Block | Input tensor to reduce |
| axis | int | Axis along which to reduce |
| return_indices | bool | Whether to also return argmin indices (default False) |
| keep_dims | bool | Whether to retain the reduced axis (default False) |

## Returns

| Type | Description |
|------|-------------|
| Block | Reduced tensor with the specified axis mined |

## Triton Version

Triton 2.1+

## Target Architecture

NVIDIA GPU (SM 7.0+), AMD GPU (CDNA2+), Intel GPU

## Related Instructions

- [tl.max](../triton-max/DOC.md)
- [tl.sum](../triton-sum/DOC.md)
- [tl.argmin](../triton-argmin/DOC.md)

## Example

```python
import triton.language as tl

# Find minimum value per row
x = tl.load(x_ptr + offsets)
row_min = tl.min(x, axis=1, keep_dims=True)
```