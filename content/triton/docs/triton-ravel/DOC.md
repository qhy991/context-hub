---
name: triton-ravel
description: Return a contiguous flattened view of a tensor
metadata:
  languages: triton
  versions: '2.1'
  revision: 1
  updated-on: '2026-06-16'
  source: official
  tags: triton,gpu,shape,ravel,flatten
---

# tl.ravel

Returns a contiguous flattened (1D) view of `x`. If `can_reorder=True`, the compiler may reorder elements for optimization.

## Syntax

```python
tl.ravel(x, can_reorder=False)
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| x | Block | Input tensor |
| can_reorder | bool | Allow reordering (default False) |

## Returns

| Type | Description |
|------|-------------|
| Block | 1D tensor with same elements |

## Triton Version

Triton 2.1+

## Target Architecture

NVIDIA GPU (SM 7.0+), AMD GPU (CDNA2+), Intel GPU

## Related Instructions

- [tl.view](../triton-view/DOC.md)
- [tl.reshape](../triton-reshape/DOC.md)

## Example

```python
import triton.language as tl

flat = tl.ravel(x)  # (M,N) -> (M*N,)
```
