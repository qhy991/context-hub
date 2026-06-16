---
name: triton-reduce-or
description: Compute logical OR reduction along an axis
metadata:
  languages: triton
  versions: '2.1'
  revision: 1
  updated-on: '2026-06-16'
  source: official
  tags: triton,gpu,reduction,or,logical
---

# tl.reduce-or

Computes the logical OR of all elements along the specified axis. Only operates on integer types (int1, int8, etc.). Equivalent to `tl.reduce(input, axis, tl.bitwise_or)`.

## Syntax

```python
tl.reduce_or(input, axis, keep_dims=False)
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| input | Block | Integer tensor to reduce |
| axis | int | Axis along which to reduce |
| keep_dims | bool | Retain reduced axis (default False) |

## Returns

| Type | Description |
|------|-------------|
| Block | Reduced tensor with logical OR |

## Triton Version

Triton 2.1+

## Target Architecture

NVIDIA GPU (SM 7.0+), AMD GPU (CDNA2+), Intel GPU

## Related Instructions

- [tl.reduce](../triton-reduce/DOC.md)
- [tl.xor_sum](../triton-xor-sum/DOC.md)

## Example

```python
import triton.language as tl

any_true = tl.reduce_or(mask, axis=0)  # any element True?
```
