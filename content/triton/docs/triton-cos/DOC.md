---
name: triton-cos
description: Element-wise cosine
metadata:
  languages: triton
  versions: '2.1'
  revision: 1
  updated-on: '2026-06-16'
  source: official
  tags: triton,gpu,math,cos,trigonometry
---

# tl.cos

Computes the cosine of each element. Uses hardware-accelerated approximation.

## Syntax

```python
tl.cos(x)
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| x | Block | Input tensor (radians) |

## Returns

| Type | Description |
|------|-------------|
| Block | `cos(x)` element-wise |

## Triton Version

Triton 2.1+

## Target Architecture

NVIDIA GPU (SM 7.0+), AMD GPU (CDNA2+), Intel GPU

## Related Instructions

- [tl.sin](../triton-sin/DOC.md)

## Example

```python
import triton.language as tl

c = tl.cos(theta)  # element-wise cosine
```
