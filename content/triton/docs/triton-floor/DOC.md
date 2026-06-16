---
name: triton-floor
description: Element-wise floor (round down to nearest integer)
metadata:
  languages: triton
  versions: '2.1'
  revision: 1
  updated-on: '2026-06-16'
  source: official
  tags: triton,gpu,math,floor,rounding
---

# tl.floor

Rounds each element of `x` down to the nearest integer. Maps to the GPU floor instruction.

## Syntax

```python
tl.floor(x)
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| x | Block | Input tensor |

## Returns

| Type | Description |
|------|-------------|
| Block | `floor(x)` element-wise |

## Triton Version

Triton 2.1+

## Target Architecture

NVIDIA GPU (SM 7.0+), AMD GPU (CDNA2+), Intel GPU

## Related Instructions

- [tl.ceil](../triton-ceil/DOC.md)

## Example

```python
import triton.language as tl

rounded_down = tl.floor(x)  # floor(x)
```
