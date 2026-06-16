---
name: triton-sqrt-rn
description: Precise square root with IEEE round-to-nearest-even
metadata:
  languages: triton
  versions: '2.1'
  revision: 1
  updated-on: '2026-06-16'
  source: official
  tags: triton,gpu,math,sqrt,ieee,precision
---

# tl.sqrt-rn

Computes the square root with IEEE-compliant round-to-nearest-even rounding. Use this when precision is critical. `tl.sqrt` is faster but may have ULP differences. FP32 only.

## Syntax

```python
tl.sqrt_rn(x)
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| x | Block | Input tensor (fp32) |

## Returns

| Type | Description |
|------|-------------|
| Block | `√x` with IEEE round-to-nearest-even |

## Triton Version

Triton 2.1+

## Target Architecture

NVIDIA GPU (SM 7.0+), AMD GPU (CDNA2+), Intel GPU

## Related Instructions

- [tl.sqrt](../triton-sqrt/DOC.md)
- [tl.rsqrt](../triton-rsqrt/DOC.md)

## Example

```python
import triton.language as tl

precise_sqrt = tl.sqrt_rn(x)  # IEEE-compliant sqrt
```
