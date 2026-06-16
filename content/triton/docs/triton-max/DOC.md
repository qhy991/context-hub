---
name: triton-max
description: Compute the maximum of elements along a given axis
metadata:
  languages: triton
  versions: '2.1'
  revision: 1
  updated-on: '2026-06-16'
  source: official
  tags: triton,gpu,reduction,max
---

# tl.max

Returns the maximum of all elements in the input tensor along the provided axis.

## Syntax

```python
tl.max(input, axis, return_indices=False, keep_dims=False)
```

## Description

Computes the element-wise maximum along the specified axis. When `return_indices=True`, also returns the indices of the maximum values. This is a reduction operation that collapses the given dimension.

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| input | Block | Input tensor to reduce |
| axis | int | Axis along which to reduce |
| return_indices | bool | Whether to also return argmax indices (default False) |
| keep_dims | bool | Whether to retain the reduced axis (default False) |

## Returns

| Type | Description |
|------|-------------|
| Block | Reduced tensor with the specified axis maxed |

## Semantics

```pseudo
for each slice along axis:
    result[..., 0, ...] = max(input[..., :, ...])
```

## Triton Version

Triton 2.1+

## Target Architecture

NVIDIA GPU (SM 7.0+), AMD GPU (CDNA2+), Intel GPU

## Related Instructions

- [tl.min](../triton-min/DOC.md)
- [tl.sum](../triton-sum/DOC.md)
- [tl.argmax](../triton-argmax/DOC.md)

## Example

```python
import triton.language as tl

# Softmax: subtract max for numerical stability
x = tl.load(x_ptr + offsets, mask=mask)
x_max = tl.max(x, axis=0, keep_dims=True)
x_exp = tl.exp(x - x_max)
x_sum = tl.sum(x_exp, axis=0, keep_dims=True)
softmax = x_exp / x_sum
```