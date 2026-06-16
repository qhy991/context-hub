---
name: triton-fma
description: "Fused multiply-add: x * y + z in a single instruction"
metadata:
  languages: triton
  versions: '2.1'
  revision: 1
  updated-on: '2026-06-16'
  source: official
  tags: triton,gpu,math,fma,fused
---

# tl.fma

Computes `x * y + z` in a single fused multiply-add operation. This is faster and more accurate than separate multiply and add. Maps to FMA/FMAD/FMULADD GPU instructions.

## Syntax

```python
tl.fma(x, y, z)
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| x | Block | First factor |
| y | Block | Second factor |
| z | Block | Addend |

## Returns

| Type | Description |
|------|-------------|
| Block | `x * y + z` (fused, single rounding) |

## Triton Version

Triton 2.1+

## Target Architecture

NVIDIA GPU (SM 7.0+), AMD GPU (CDNA2+), Intel GPU

## Related Instructions

- [tl.add](../triton-add/DOC.md)
- [tl.mul](../triton-mul/DOC.md)

## Example

```python
import triton.language as tl

# FMA: accumulates in a single instruction
acc = tl.fma(a, b, acc)  # acc = a * b + acc
```
