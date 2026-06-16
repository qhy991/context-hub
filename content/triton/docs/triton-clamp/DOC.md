---
name: triton-clamp
description: Clamp tensor values to a [min, max] range
metadata:
  languages: triton
  versions: '2.1'
  revision: 1
  updated-on: '2026-06-16'
  source: official
  tags: triton,gpu,math,clamp,range
---

# tl.clamp

Clamps each element of `x` to the range `[min_val, max_val]`. Equivalent to `tl.minimum(tl.maximum(x, min_val), max_val)`.

## Syntax

```python
tl.clamp(x, min_val, max_val)
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| x | Block | Input tensor |
| min_val | scalar | Lower bound |
| max_val | scalar | Upper bound |

## Returns

| Type | Description |
|------|-------------|
| Block | Clamped tensor with values in `[min_val, max_val]` |

## Triton Version

Triton 2.1+

## Target Architecture

NVIDIA GPU (SM 7.0+), AMD GPU (CDNA2+), Intel GPU

## Related Instructions

- [tl.maximum](../triton-maximum/DOC.md)
- [tl.minimum](../triton-minimum/DOC.md)

## Example

```python
import triton.language as tl

clipped = tl.clamp(x, 0.0, 1.0)  # clip to [0, 1]
```
