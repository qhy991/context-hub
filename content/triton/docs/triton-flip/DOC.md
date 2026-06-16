---
name: triton-flip
description: Flip a tensor along a dimension (reverse order)
metadata:
  languages: triton
  versions: '2.1'
  revision: 1
  updated-on: '2026-06-16'
  source: official
  tags: triton,gpu,shape,flip,reverse
---

# tl.flip

Flips a tensor `x` along the specified dimension `dim`, reversing the order of elements. When `dim` is None, flips along all dimensions.

## Syntax

```python
tl.flip(x, dim=None)
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| x | Block | Input tensor |
| dim | int (optional) | Dimension to flip (None = all dims) |

## Returns

| Type | Description |
|------|-------------|
| Block | Flipped tensor |

## Triton Version

Triton 2.1+

## Target Architecture

NVIDIA GPU (SM 7.0+), AMD GPU (CDNA2+), Intel GPU

## Related Instructions

- [tl.permute](../triton-permute/DOC.md)

## Example

```python
import triton.language as tl

reversed_x = tl.flip(x, dim=0)  # reverse along first axis
```
