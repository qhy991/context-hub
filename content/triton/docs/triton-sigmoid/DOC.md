---
name: triton-sigmoid
description: "Element-wise sigmoid activation: 1 / (1 + exp(-x))"
metadata:
  languages: triton
  versions: '2.1'
  revision: 1
  updated-on: '2026-06-16'
  source: official
  tags: triton,gpu,math,sigmoid,activation
---

# tl.sigmoid

Computes the sigmoid function `σ(x) = 1 / (1 + e^(-x))` for each element. Maps input to the range (0, 1). Common in binary classification and gate mechanisms.

## Syntax

```python
tl.sigmoid(x)
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| x | Block | Input tensor |

## Returns

| Type | Description |
|------|-------------|
| Block | `σ(x)` element-wise, values in (0, 1) |

## Triton Version

Triton 2.1+

## Target Architecture

NVIDIA GPU (SM 7.0+), AMD GPU (CDNA2+), Intel GPU

## Related Instructions

- [tl.softmax](../triton-softmax/DOC.md)
- [tl.exp](../triton-exp/DOC.md)

## Example

```python
import triton.language as tl

gate = tl.sigmoid(x)  # sigmoid activation
```
