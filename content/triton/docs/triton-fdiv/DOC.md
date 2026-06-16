---
name: triton-fdiv
description: Fast floating-point division (element-wise)
metadata:
  languages: triton
  versions: '2.1'
  revision: 1
  updated-on: '2026-06-16'
  source: official
  tags: triton,gpu,math,fdiv,division
---

# tl.fdiv

Fast division using hardware approximation. When `ieee_rounding=False` (default), uses the fastest available GPU division. Use `tl.div_rn` for IEEE-compliant rounding.

## Syntax

```python
tl.fdiv(x, y, ieee_rounding=False)
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| x | Block | Numerator |
| y | Block | Denominator |
| ieee_rounding | bool | Whether to use IEEE rounding (default False) |

## Returns

| Type | Description |
|------|-------------|
| Block | `x / y` element-wise |

## Triton Version

Triton 2.1+

## Target Architecture

NVIDIA GPU (SM 7.0+), AMD GPU (CDNA2+), Intel GPU

## Related Instructions

- [tl.div_rn](../triton-div-rn/DOC.md)
- [tl.cdiv](../triton-cdiv/DOC.md)

## Example

```python
import triton.language as tl

result = tl.fdiv(x, y)  # fast division
```
