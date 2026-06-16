---
name: triton-join
description: Join two tensors in a new minor dimension
metadata:
  languages: triton
  versions: '2.1'
  revision: 1
  updated-on: '2026-06-16'
  source: official
  tags: triton,gpu,shape,join,concatenate
---

# tl.join

Joins tensors `a` and `b` along a new, innermost dimension of size 2. Two tensors of shape (4, 8) produce a tensor of shape (4, 8, 2). Inverse of `tl.split`.

## Syntax

```python
tl.join(a, b)
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| a | Block | First input tensor |
| b | Block | Second input tensor |

## Returns

| Type | Description |
|------|-------------|
| Block | Joined tensor with new last dimension of size 2 |

## Triton Version

Triton 2.1+

## Target Architecture

NVIDIA GPU (SM 7.0+), AMD GPU (CDNA2+), Intel GPU

## Related Instructions

- [tl.split](../triton-split/DOC.md)
- [tl.cat](../triton-cat/DOC.md)

## Example

```python
import triton.language as tl

pair = tl.join(x, y)  # (4,8) + (4,8) -> (4,8,2)
```
