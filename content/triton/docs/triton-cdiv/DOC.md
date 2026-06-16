---
name: triton-cdiv
description: Ceiling division — ceil(x / div)
metadata:
  languages: triton
  versions: '2.1'
  revision: 1
  updated-on: '2026-06-16'
  source: official
  tags: triton,gpu,math,cdiv,ceiling,division
---

# tl.cdiv

Computes `ceil(x / div)` for each element. Commonly used to compute grid sizes: `grid = tl.cdiv(N, BLOCK)`. Both `x` and `div` must be integer types.

## Syntax

```python
tl.cdiv(x, div)
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| x | Block | Numerator (integer) |
| div | Block | Divisor (integer) |

## Returns

| Type | Description |
|------|-------------|
| Block | `ceil(x / div)` element-wise (integer) |

## Triton Version

Triton 2.1+

## Target Architecture

NVIDIA GPU (SM 7.0+), AMD GPU (CDNA2+), Intel GPU

## Related Instructions

- [tl.fdiv](../triton-fdiv/DOC.md)
- [tl.div_rn](../triton-div-rn/DOC.md)

## Example

```python
import triton.language as tl

import triton
grid_size = triton.cdiv(N, BLOCK)  # host-side
grid = tl.cdiv(N, BLOCK)  # device-side
```
