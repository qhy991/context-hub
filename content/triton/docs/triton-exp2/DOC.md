---
name: triton-exp2
description: Element-wise base-2 exponential
metadata:
  languages: triton
  versions: '2.1'
  revision: 1
  updated-on: '2026-06-16'
  source: official
  tags: triton,gpu,math,exp2,exponential
---

# tl.exp2

Computes `2^x` for each element. Uses hardware-accelerated approximation.

## Syntax

```python
tl.exp2(x)
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| x | Block | Input tensor |

## Returns

| Type | Description |
|------|-------------|
| Block | `2^x` element-wise |

## Triton Version

Triton 2.1+

## Target Architecture

NVIDIA GPU (SM 7.0+), AMD GPU (CDNA2+), Intel GPU

## Related Instructions

- [tl.exp](../triton-exp/DOC.md)
- [tl.log2](../triton-log2/DOC.md)

## Example

```python
import triton.language as tl

pow2 = tl.exp2(x)  # 2^x
```
