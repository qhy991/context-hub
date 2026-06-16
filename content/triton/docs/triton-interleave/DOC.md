---
name: triton-interleave
description: Interleave two tensors along the last dimension
metadata:
  languages: triton
  versions: '2.1'
  revision: 1
  updated-on: '2026-06-16'
  source: official
  tags: triton,gpu,shape,interleave
---

# tl.interleave

Interleaves the values of `a` and `b` along their last dimension. If `a` and `b` have shape (M, N), the result has shape (M, 2N) where elements from `a` and `b` alternate. This is useful for constructing complex numbers from real/imaginary pairs.

## Syntax

```python
tl.interleave(a, b)
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| a | Block | First input tensor |
| b | Block | Second input tensor |

## Returns

| Type | Description |
|------|-------------|
| Block | Interleaved tensor with last dim doubled |

## Triton Version

Triton 2.1+

## Target Architecture

NVIDIA GPU (SM 7.0+), AMD GPU (CDNA2+), Intel GPU

## Related Instructions

- [tl.join](../triton-join/DOC.md)
- [tl.split](../triton-split/DOC.md)

## Example

```python
import triton.language as tl

complex = tl.interleave(real, imag)  # [r1,i1, r2,i2, ...]
```
