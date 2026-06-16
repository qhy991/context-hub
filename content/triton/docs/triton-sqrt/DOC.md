---
name: triton-sqrt
description: Fast square root (element-wise)
metadata:
  languages: triton
  versions: '2.1'
  revision: 1
  updated-on: '2026-06-16'
  source: official
  tags: triton,gpu,math,sqrt,square-root
---

# tl.sqrt

Fast square root (element-wise).

## Syntax

```python
tl.sqrt(x)
```

## Description

Computes the square root of each element using a fast hardware approximation. This is the fast path — for IEEE-compliant rounding, use `tl.sqrt_rn(x)` instead. Commonly used in RMS normalization, gradient normalization, and distance computations.

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| x | Block | Input tensor (must be non-negative) |

## Returns

| Type | Description |
|------|-------------|
| Block | `sqrt(x)` for each element |

## Semantics

```pseudo
for each element:
    output[i] = sqrt(input[i])  # fast approximation
```

## Triton Version

Triton 2.1+

## Target Architecture

NVIDIA GPU (SM 7.0+), AMD GPU (CDNA2+), Intel GPU

## Related Instructions

- [tl.exp](../triton-exp/DOC.md)
- [tl.log](../triton-log/DOC.md)
- [tl.abs](../triton-abs/DOC.md)

## Example

```python
import triton.language as tl

# RMS normalization
x = tl.load(x_ptr + offsets, mask=mask)
rms = tl.sqrt(tl.sum(x * x, axis=0) / N + eps)
y = x / rms
tl.store(out_ptr + offsets, y, mask=mask)
```