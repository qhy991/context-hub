---
name: triton-mul
description: Element-wise multiplication of two tensors
metadata:
  languages: triton
  versions: '2.1'
  revision: 1
  updated-on: '2026-06-16'
  source: official
  tags: triton,gpu,math,mul,arithmetic
---

# tl.mul

Element-wise multiplication of two tensors.

## Syntax

```python
tl.mul(x, y)
```

Also available via the `*` operator:
```python
result = x * y
```

## Description

Computes the element-wise product of `x` and `y`. Supports broadcasting of compatible shapes.

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| x | Block | First input tensor |
| y | Block | Second input tensor |

## Returns

| Type | Description |
|------|-------------|
| Block | `x * y` element-wise |

## Triton Version

Triton 2.1+

## Target Architecture

NVIDIA GPU (SM 7.0+), AMD GPU (CDNA2+), Intel GPU

## Related Instructions

- [tl.add](../triton-add/DOC.md)
- [tl.fma](../triton-fma/DOC.md)

## Example

```python
import triton.language as tl

x = tl.load(x_ptr + offsets, mask=mask)
scale = tl.load(scale_ptr + offsets, mask=mask)
scaled = x * scale  # or: tl.mul(x, scale)
```