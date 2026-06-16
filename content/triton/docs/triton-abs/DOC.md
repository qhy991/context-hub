---
name: triton-abs
description: Element-wise absolute value
metadata:
  languages: triton
  versions: '2.1'
  revision: 1
  updated-on: '2026-06-16'
  source: official
  tags: triton,gpu,math,abs,absolute
---

# tl.abs

Element-wise absolute value.

## Syntax

```python
tl.abs(x)
```

## Description

Computes the absolute value `|x|` for each element of the input tensor. Maps directly to a single GPU instruction.

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| x | Block | Input tensor |

## Returns

| Type | Description |
|------|-------------|
| Block | `|x|` for each element |

## Semantics

```pseudo
for each element:
    output[i] = |input[i]|
```

## Triton Version

Triton 2.1+

## Target Architecture

NVIDIA GPU (SM 7.0+), AMD GPU (CDNA2+), Intel GPU

## Related Instructions

- [tl.exp](../triton-exp/DOC.md)
- [tl.sqrt](../triton-sqrt/DOC.md)

## Example

```python
import triton.language as tl

# L1 loss
x = tl.load(x_ptr + offsets, mask=mask)
y = tl.load(y_ptr + offsets, mask=mask)
l1_loss = tl.sum(tl.abs(x - y))
```