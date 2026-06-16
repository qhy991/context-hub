---
name: triton-expand-dims
description: Insert new length-1 dimensions into a tensor
metadata:
  languages: triton
  versions: '2.1'
  revision: 1
  updated-on: '2026-06-16'
  source: official
  tags: triton,gpu,shape,expand-dims
---

# tl.expand-dims

Inserts new dimensions of size 1 at the positions specified by `axis`. Axis indices are relative to the resulting tensor shape. Useful for broadcasting alignment.

## Syntax

```python
tl.expand_dims(input, axis)
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| input | Block | Input tensor |
| axis | int or list[int] | Position(s) to insert new axis |

## Returns

| Type | Description |
|------|-------------|
| Block | Tensor with additional size-1 dimensions |

## Triton Version

Triton 2.1+

## Target Architecture

NVIDIA GPU (SM 7.0+), AMD GPU (CDNA2+), Intel GPU

## Related Instructions

- [tl.squeeze](../triton-squeeze/DOC.md)
- [tl.broadcast_to](../triton-broadcast-to/DOC.md)

## Example

```python
import triton.language as tl

x_exp = tl.expand_dims(x, axis=0)  # (N,) -> (1, N)
x_exp = tl.expand_dims(x, axis=[0, -1])  # (M,N) -> (1,M,N,1)
```
