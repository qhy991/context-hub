---
name: triton-minimum
description: Element-wise minimum of two tensors
metadata:
  languages: triton
  versions: '2.1'
  revision: 1
  updated-on: '2026-06-16'
  source: official
  tags: triton,gpu,math,minimum,compare
---

# tl.minimum

Returns the element-wise minimum of `x` and `y`. For reduction along an axis, use `tl.min`.

## Syntax

```python
tl.minimum(x, y)
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| x | Block | First input tensor |
| y | Block | Second input tensor |

## Returns

| Type | Description |
|------|-------------|
| Block | `min(x, y)` element-wise |

## Triton Version

Triton 2.1+

## Target Architecture

NVIDIA GPU (SM 7.0+), AMD GPU (CDNA2+), Intel GPU

## Related Instructions

- [tl.maximum](../triton-maximum/DOC.md)
- [tl.min](../triton-min/DOC.md)

## Example

```python
import triton.language as tl

lower = tl.minimum(x, y)  # element-wise min
```
