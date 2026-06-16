---
name: triton-erf
description: Element-wise error function (Gaussian error function)
metadata:
  languages: triton
  versions: '2.1'
  revision: 1
  updated-on: '2026-06-16'
  source: official
  tags: triton,gpu,math,erf,special
---

# tl.erf

Computes the error function `erf(x) = 2/√π ∫₀ˣ e^(-t²) dt`. Commonly used in GELU activation and probability computations.

## Syntax

```python
tl.erf(x)
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| x | Block | Input tensor |

## Returns

| Type | Description |
|------|-------------|
| Block | `erf(x)` element-wise |

## Triton Version

Triton 2.1+

## Target Architecture

NVIDIA GPU (SM 7.0+), AMD GPU (CDNA2+), Intel GPU

## Related Instructions

- [tl.exp](../triton-exp/DOC.md)
- [tl.sigmoid](../triton-sigmoid/DOC.md)

## Example

```python
import triton.language as tl

# GELU activation: x * Φ(x) ≈ 0.5 * x * (1 + erf(x/sqrt(2)))
# gelu = 0.5 * x * (1 + tl.erf(x * 0.7071067811865475))
```
