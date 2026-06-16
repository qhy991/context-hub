---
name: triton-ceil
description: Element-wise ceiling (round up to nearest integer)
metadata:
  languages: triton
  versions: '2.1'
  revision: 1
  updated-on: '2026-06-16'
  source: official
  tags: triton,gpu,math,ceil,rounding
---

# tl.ceil

Rounds each element of `x` up to the nearest integer. Maps to the GPU ceil instruction.

## Syntax

```python
tl.ceil(x)
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| x | Block | Input tensor |

## Returns

| Type | Description |
|------|-------------|
| Block | `ceil(x)` element-wise |

## Triton Version

Triton 2.1+

## Target Architecture

NVIDIA GPU (SM 7.0+), AMD GPU (CDNA2+), Intel GPU

## Related Instructions

- [tl.floor](../triton-floor/DOC.md)

## Example

```python
import triton.language as tl

rounded_up = tl.ceil(x)  # ceil(x)
```
