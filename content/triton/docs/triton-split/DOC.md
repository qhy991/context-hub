---
name: triton-split
description: Split a tensor into two along the last dimension (size must be 2)
metadata:
  languages: triton
  versions: '2.1'
  revision: 1
  updated-on: '2026-06-16'
  source: official
  tags: triton,gpu,shape,split
---

# tl.split

Splits a tensor along its last dimension, which must have size 2. Returns a tuple of two tensors. Inverse of `tl.join`.

## Syntax

```python
a, b = tl.split(tensor)
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| tensor | Block | Input tensor (last dim must be 2) |

## Returns

| Type | Description |
|------|-------------|
| Block | Tuple of two tensors, each with last dim size 1 |

## Triton Version

Triton 2.1+

## Target Architecture

NVIDIA GPU (SM 7.0+), AMD GPU (CDNA2+), Intel GPU

## Related Instructions

- [tl.join](../triton-join/DOC.md)
- [tl.cat](../triton-cat/DOC.md)

## Example

```python
import triton.language as tl

x, y = tl.split(pair)  # (4,8,2) -> (4,8), (4,8)
```
