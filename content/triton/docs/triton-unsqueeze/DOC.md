---
name: triton-unsqueeze
description: Insert a length-1 dimension at the specified position
metadata:
  languages: triton
  versions: '2.1'
  revision: 1
  updated-on: '2026-06-16'
  source: official
  tags: triton,gpu,shape,unsqueeze
---

# tl.unsqueeze

Adds a dimension of size 1 at the specified position. Inverse of `tl.squeeze`.

## Syntax

```python
tl.unsqueeze(x, dim)
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| x | Block | Input tensor |
| dim | int | Position to insert new axis |

## Returns

| Type | Description |
|------|-------------|
| Block | Tensor with additional size-1 dimension |

## Triton Version

Triton 2.1+

## Target Architecture

NVIDIA GPU (SM 7.0+), AMD GPU (CDNA2+), Intel GPU

## Related Instructions

- [tl.squeeze](../triton-squeeze/DOC.md)
- [tl.expand_dims](../triton-expand-dims/DOC.md)

## Example

```python
import triton.language as tl

expanded = tl.unsqueeze(x, dim=0)  # (N,) -> (1, N)
```
