---
name: triton-maximum
description: Element-wise maximum of two tensors
metadata:
  languages: triton
  versions: '2.1'
  revision: 1
  updated-on: '2026-06-16'
  source: official
  tags: triton,gpu,math,maximum,compare
---

# tl.maximum

Element-wise maximum of two tensors.

## Syntax

```python
tl.maximum(x, y)
```

## Description

Returns the element-wise maximum of `x` and `y`. For reduction along an axis, use `tl.max`.

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| x | Block | First input tensor |
| y | Block | Second input tensor |

## Returns

| Type | Description |
|------|-------------|
| Block | `max(x, y)` element-wise |

## Related Instructions

- [tl.minimum](../triton-minimum/DOC.md)
- [tl.max](../triton-max/DOC.md)

## Example

```python
import triton.language as tl

x = tl.load(x_ptr + offsets, mask=mask)
y = tl.load(y_ptr + offsets, mask=mask)
upper = tl.maximum(x, y)  # element-wise max
```