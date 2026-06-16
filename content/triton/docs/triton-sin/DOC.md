---
name: triton-sin
description: Element-wise sine
metadata:
  languages: triton
  versions: '2.1'
  revision: 1
  updated-on: '2026-06-16'
  source: official
  tags: triton,gpu,math,sin,trigonometry
---

# tl.sin

Computes the sine of each element. Uses hardware-accelerated approximation.

## Syntax

```python
tl.sin(x)
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| x | Block | Input tensor (radians) |

## Returns

| Type | Description |
|------|-------------|
| Block | `sin(x)` element-wise |

## Triton Version

Triton 2.1+

## Target Architecture

NVIDIA GPU (SM 7.0+), AMD GPU (CDNA2+), Intel GPU

## Related Instructions

- [tl.cos](../triton-cos/DOC.md)

## Example

```python
import triton.language as tl

s = tl.sin(theta)  # element-wise sine
```
