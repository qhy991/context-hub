---
name: triton-cumsum
description: Cumulative sum along an axis (prefix sum / scan)
metadata:
  languages: triton
  versions: '2.1'
  revision: 1
  updated-on: '2026-06-16'
  source: official
  tags: triton,gpu,scan,cumsum,cumulative
---

# tl.cumsum

Computes the cumulative sum (inclusive scan) along the specified axis. When `reverse=True`, computes the suffix sum instead of the prefix sum. `dtype` overrides the output type.

## Syntax

```python
tl.cumsum(input, axis=0, reverse=False, dtype=None)
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| input | Block | Input tensor |
| axis | int | Axis to scan along (default 0) |
| reverse | bool | If True, compute suffix sum (default False) |
| dtype | tl.dtype (optional) | Output data type override |

## Returns

| Type | Description |
|------|-------------|
| Block | Cumulative sum along axis |

## Triton Version

Triton 2.1+

## Target Architecture

NVIDIA GPU (SM 7.0+), AMD GPU (CDNA2+), Intel GPU

## Related Instructions

- [tl.cumprod](../triton-cumprod/DOC.md)
- [tl.sum](../triton-sum/DOC.md)

## Example

```python
import triton.language as tl

prefix = tl.cumsum(x, axis=0)  # prefix sum
suffix = tl.cumsum(x, axis=1, reverse=True)  # suffix sum
```
