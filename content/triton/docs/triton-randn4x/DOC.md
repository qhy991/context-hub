---
name: triton-randn4x
description: Generate 4x random N(0,1) float32 values per element
metadata:
  languages: triton
  versions: '2.1'
  revision: 1
  updated-on: '2026-06-16'
  source: official
  tags: triton,gpu,random,randn4x,normal
---

# tl.randn4x

Generates 4 independent Gaussian values per element.

## Syntax

```python
r0, r1, r2, r3 = tl.randn4x(seed, offset)
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| seed | tl.uint32 | Random seed |
| offset | Block (uint32) | Per-element offsets |

## Returns

| Type | Description |
|------|-------------|
| Block | Tuple of 4 Block tensors, each N(0,1) float32 |

## Triton Version

Triton 2.1+

## Target Architecture

NVIDIA GPU (SM 7.0+), AMD GPU (CDNA2+), Intel GPU

## Example

```python
import triton.language as tl

n0, n1, n2, n3 = tl.randn4x(seed, offs)
```
