---
name: triton-log2
description: Element-wise base-2 logarithm
metadata:
  languages: triton
  versions: '2.1'
  revision: 1
  updated-on: '2026-06-16'
  source: official
  tags: triton,gpu,math,log2,logarithm
---

# tl.log2

Computes `log₂(x)` for each element. Uses hardware-accelerated approximation.

## Syntax

```python
tl.log2(x)
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| x | Block | Input tensor (must be positive) |

## Returns

| Type | Description |
|------|-------------|
| Block | `log₂(x)` element-wise |

## Triton Version

Triton 2.1+

## Target Architecture

NVIDIA GPU (SM 7.0+), AMD GPU (CDNA2+), Intel GPU

## Related Instructions

- [tl.log](../triton-log/DOC.md)
- [tl.exp2](../triton-exp2/DOC.md)

## Example

```python
import triton.language as tl

bits = tl.log2(x)  # log2(x)
```
