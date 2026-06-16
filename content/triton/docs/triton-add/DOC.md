---
name: triton-add
description: Element-wise addition of two tensors
metadata:
  languages: triton
  versions: '2.1'
  revision: 1
  updated-on: '2026-06-16'
  source: official
  tags: triton,gpu,math,add,arithmetic
---

# tl.add

Element-wise addition of two tensors.

## Syntax

```python
tl.add(x, y)
```

Also available via the `+` operator:
```python
result = x + y
```

## Description

Computes the element-wise sum of `x` and `y`. Supports broadcasting of compatible shapes. This maps directly to a single GPU add instruction.

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| x | Block | First input tensor |
| y | Block | Second input tensor |

## Returns

| Type | Description |
|------|-------------|
| Block | `x + y` element-wise |

## Semantics

```pseudo
for each element:
    output[i] = x[i] + y[i]
```

## Triton Version

Triton 2.1+

## Target Architecture

NVIDIA GPU (SM 7.0+), AMD GPU (CDNA2+), Intel GPU

## Related Instructions

- [tl.sub](../triton-sub/DOC.md)
- [tl.mul](../triton-mul/DOC.md)

## Example

```python
import triton.language as tl

x = tl.load(x_ptr + offsets, mask=mask)
y = tl.load(y_ptr + offsets, mask=mask)
out = tl.add(x, y)  # or simply: x + y
tl.store(out_ptr + offsets, out, mask=mask)
```