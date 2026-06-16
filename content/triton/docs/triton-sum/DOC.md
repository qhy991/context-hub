---
name: triton-sum
description: Compute the sum of elements along a given axis
metadata:
  languages: triton
  versions: '2.1'
  revision: 1
  updated-on: '2026-06-16'
  source: official
  tags: triton,gpu,reduction,sum
---

# tl.sum

Returns the sum of all elements in the input tensor along the provided axis.

## Syntax

```python
tl.sum(input, axis, keep_dims=False)
```

## Description

Computes the element-wise sum along the specified axis. This is a reduction operation that collapses the given dimension. When `keep_dims=True`, the reduced axis is retained with size 1.

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| input | Block | Input tensor to reduce |
| axis | int | Axis along which to reduce |
| keep_dims | bool | Whether to retain the reduced axis (default False) |

## Returns

| Type | Description |
|------|-------------|
| Block | Reduced tensor with the specified axis summed |

## Semantics

```pseudo
for each slice along axis:
    result[..., 0, ...] = sum(input[..., :, ...])
```

## Triton Version

Triton 2.1+

## Target Architecture

NVIDIA GPU (SM 7.0+), AMD GPU (CDNA2+), Intel GPU

## Related Instructions

- [tl.max](../triton-max/DOC.md)
- [tl.min](../triton-min/DOC.md)
- [tl.reduce](../triton-reduce/DOC.md)

## Example

```python
import triton.language as tl

# Softmax: subtract max for numerical stability, then exp, sum, divide
x = tl.load(x_ptr + offsets, mask=mask)
x_max = tl.max(x, axis=0, keep_dims=True)
x_exp = tl.exp(x - x_max)
x_sum = tl.sum(x_exp, axis=0, keep_dims=True)
softmax = x_exp / x_sum
```