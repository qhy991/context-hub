---
name: triton-umulhi
description: High N bits of the 2N-bit product of two N-bit integers
metadata:
  languages: triton
  versions: '2.1'
  revision: 1
  updated-on: '2026-06-16'
  source: official
  tags: triton,gpu,math,umulhi,integer
---

# tl.umulhi

Returns the most significant N bits of the 2N-bit product of two N-bit unsigned integers. This discards the lower N bits of the product. Useful for high-precision integer arithmetic and hash functions.

## Syntax

```python
tl.umulhi(x, y)
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| x | Block | First operand (unsigned integer) |
| y | Block | Second operand (unsigned integer) |

## Returns

| Type | Description |
|------|-------------|
| Block | High N bits of `x * y` |

## Triton Version

Triton 2.1+

## Target Architecture

NVIDIA GPU (SM 7.0+), AMD GPU (CDNA2+), Intel GPU

## Related Instructions

- [tl.mul](../triton-mul/DOC.md)

## Example

```python
import triton.language as tl

hi = tl.umulhi(a, b)  # upper half of product
```
