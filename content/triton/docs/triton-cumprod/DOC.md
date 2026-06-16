---
name: triton-cumprod
description: Cumulative product along an axis (prefix product / scan)
metadata:
  languages: triton
  versions: '2.1'
  revision: 1
  updated-on: '2026-06-16'
  source: official
  tags: triton,gpu,scan,cumprod,cumulative
---

# tl.cumprod

Computes the cumulative product (inclusive scan) along the specified axis. When `reverse=True`, computes the suffix product instead of the prefix product.

## Syntax

```python
tl.cumprod(input, axis=0, reverse=False)
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| input | Block | Input tensor |
| axis | int | Axis to scan along (default 0) |
| reverse | bool | If True, compute suffix product (default False) |

## Returns

| Type | Description |
|------|-------------|
| Block | Cumulative product along axis |

## Triton Version

Triton 2.1+

## Target Architecture

NVIDIA GPU (SM 7.0+), AMD GPU (CDNA2+), Intel GPU

## Related Instructions

- [tl.cumsum](../triton-cumsum/DOC.md)
- [tl.sum](../triton-sum/DOC.md)

## Example

```python
import triton.language as tl

prefix_prod = tl.cumprod(x, axis=0)  # prefix product
```
