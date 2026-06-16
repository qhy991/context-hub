---
name: triton-div-rn
description: Precise division with IEEE round-to-nearest-even
metadata:
  languages: triton
  versions: '2.1'
  revision: 1
  updated-on: '2026-06-16'
  source: official
  tags: triton,gpu,math,division,ieee,precision
---

# tl.div-rn

Precise division with IEEE-compliant round-to-nearest-even rounding. Slower than `tl.fdiv` but guarantees correct rounding. FP32 and FP64 only.

## Syntax

```python
tl.div_rn(x, y)
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| x | Block | Numerator |
| y | Block | Denominator |

## Returns

| Type | Description |
|------|-------------|
| Block | `x / y` with IEEE round-to-nearest-even |

## Triton Version

Triton 2.1+

## Target Architecture

NVIDIA GPU (SM 7.0+), AMD GPU (CDNA2+), Intel GPU

## Related Instructions

- [tl.fdiv](../triton-fdiv/DOC.md)
- [tl.cdiv](../triton-cdiv/DOC.md)

## Example

```python
import triton.language as tl

precise_div = tl.div_rn(x, y)  # IEEE-compliant division
```
