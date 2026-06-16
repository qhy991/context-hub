---
name: triton-exp
description: Element-wise exponential function
metadata:
  languages: triton
  versions: '2.1'
  revision: 1
  updated-on: '2026-06-16'
  source: official
  tags: triton,gpu,math,exp,exponential
---

# tl.exp

Element-wise exponential function.

## Syntax

```python
tl.exp(x)
```

## Description

Computes `e^x` for each element of the input tensor. Uses fast hardware-accelerated approximations on GPU. This is a core operation in softmax, attention mechanisms, and many activation functions.

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| x | Block | Input tensor |

## Returns

| Type | Description |
|------|-------------|
| Block | `exp(x)` for each element |

## Semantics

```pseudo
for each element:
    output[i] = exp(input[i])
```

## Triton Version

Triton 2.1+

## Target Architecture

NVIDIA GPU (SM 7.0+), AMD GPU (CDNA2+), Intel GPU

## Related Instructions

- [tl.log](../triton-log/DOC.md)
- [tl.sqrt](../triton-sqrt/DOC.md)
- [tl.softmax](../triton-softmax/DOC.md)

## Example

```python
import triton.language as tl

# Softmax: exp(x - max) / sum(exp(x - max))
x = tl.load(x_ptr + offsets, mask=mask)
x_max = tl.max(x, axis=0, keep_dims=True)
x_exp = tl.exp(x - x_max)
x_sum = tl.sum(x_exp, axis=0, keep_dims=True)
softmax = x_exp / x_sum
```