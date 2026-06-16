---
name: triton-sub
description: Element-wise subtraction of two tensors
metadata:
  languages: triton
  versions: '2.1'
  revision: 1
  updated-on: '2026-06-16'
  source: official
  tags: triton,gpu,math,sub,arithmetic
---

# tl.sub

Element-wise subtraction of two tensors.

## Syntax

```python
tl.sub(x, y)
```

Also available via the `-` operator:
```python
result = x - y
```

## Description

Computes the element-wise difference of `x` and `y`. Supports broadcasting of compatible shapes.

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| x | Block | First input tensor |
| y | Block | Second input tensor (subtracted from x) |

## Returns

| Type | Description |
|------|-------------|
| Block | `x - y` element-wise |

## Triton Version

Triton 2.1+

## Target Architecture

NVIDIA GPU (SM 7.0+), AMD GPU (CDNA2+), Intel GPU

## Related Instructions

- [tl.add](../triton-add/DOC.md)
- [tl.mul](../triton-mul/DOC.md)

## Example

```python
import triton.language as tl

x = tl.load(x_ptr + offsets, mask=mask)
y = tl.load(y_ptr + offsets, mask=mask)
diff = x - y  # or: tl.sub(x, y)
tl.store(out_ptr + offsets, diff, mask=mask)
```