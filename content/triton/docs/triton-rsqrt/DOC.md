---
name: triton-rsqrt
description: Element-wise inverse square root
metadata:
  languages: triton
  versions: '2.1'
  revision: 1
  updated-on: '2026-06-16'
  source: official
  tags: triton,gpu,math,rsqrt,sqrt
---

# tl.rsqrt

Computes `1/√x` for each element. Uses hardware-accelerated approximation. Common in RMS normalization.

## Syntax

```python
tl.rsqrt(x)
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| x | Block | Input tensor (must be positive) |

## Returns

| Type | Description |
|------|-------------|
| Block | `1/√x` element-wise |

## Triton Version

Triton 2.1+

## Target Architecture

NVIDIA GPU (SM 7.0+), AMD GPU (CDNA2+), Intel GPU

## Related Instructions

- [tl.sqrt](../triton-sqrt/DOC.md)
- [tl.sqrt_rn](../triton-sqrt-rn/DOC.md)

## Example

```python
import triton.language as tl

rms = tl.rsqrt(mean_square + eps)  # 1/sqrt(x)
```
