---
name: triton-squeeze
description: Remove length-1 dimensions from a tensor
metadata:
  languages: triton
  versions: '2.1'
  revision: 1
  updated-on: '2026-06-16'
  source: official
  tags: triton,gpu,shape,squeeze
---

# tl.squeeze

Removes the specified dimension of size 1. The dimension must have size 1, otherwise the behaviour is undefined. Inverse of `tl.unsqueeze`.

## Syntax

```python
tl.squeeze(x, dim)
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| x | Block | Input tensor |
| dim | int | Dimension to remove (must be size 1) |

## Returns

| Type | Description |
|------|-------------|
| Block | Tensor with specified dim removed |

## Triton Version

Triton 2.1+

## Target Architecture

NVIDIA GPU (SM 7.0+), AMD GPU (CDNA2+), Intel GPU

## Related Instructions

- [tl.unsqueeze](../triton-unsqueeze/DOC.md)
- [tl.expand_dims](../triton-expand-dims/DOC.md)

## Example

```python
import triton.language as tl

squeezed = tl.squeeze(x, dim=0)  # (1,N) -> (N,)
```
