---
name: triton-where
description: Select elements from two tensors based on a condition (ternary operator)
metadata:
  languages: triton
  versions: '2.1'
  revision: 1
  updated-on: '2026-06-16'
  source: official
  tags: triton,gpu,where,select,condition
---

# tl.where

Returns elements from `x` where `condition` is True, and from `y` where `condition` is False. This is the element-wise ternary operator: `output = condition ? x : y`. All three inputs must be broadcastable to the same shape.

## Syntax

```python
tl.where(condition, x, y)
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| condition | Block (bool) | Boolean condition tensor |
| x | Block | Values when condition is True |
| y | Block | Values when condition is False |

## Returns

| Type | Description |
|------|-------------|
| Block | Tensor with selected elements from x or y |

## Triton Version

Triton 2.1+

## Target Architecture

NVIDIA GPU (SM 7.0+), AMD GPU (CDNA2+), Intel GPU

## Related Instructions

- [tl.load](../triton-load/DOC.md) (mask parameter)
- [tl.clamp](../triton-clamp/DOC.md)

## Example

```python
import triton.language as tl

# Replace negative values with 0
clipped = tl.where(x > 0, x, 0.0)
```
