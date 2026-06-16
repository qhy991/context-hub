---
name: triton-zeros-like
description: Return a tensor of zeros with the same shape and dtype as input
metadata:
  languages: triton
  versions: '2.1'
  revision: 1
  updated-on: '2026-06-16'
  source: official
  tags: triton,gpu,creation,zeros-like
---

# tl.zeros-like

Creates a tensor of zeros with the same shape and dtype as the input tensor. Equivalent to `tl.zeros(input.shape, input.dtype)`.

## Syntax

```python
tl.zeros_like(input)
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| input | Block | Tensor whose shape and dtype to match |

## Returns

| Type | Description |
|------|-------------|
| Block | Zero tensor matching input shape and dtype |

## Triton Version

Triton 2.1+

## Target Architecture

NVIDIA GPU (SM 7.0+), AMD GPU (CDNA2+), Intel GPU

## Related Instructions

- [tl.zeros](../triton-zeros/DOC.md)
- [tl.full](../triton-full/DOC.md)

## Example

```python
import triton.language as tl

z = tl.zeros_like(x)  # same shape and type as x, all zeros
```
