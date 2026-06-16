---
name: triton-log
description: Element-wise natural logarithm
metadata:
  languages: triton
  versions: '2.1'
  revision: 1
  updated-on: '2026-06-16'
  source: official
  tags: triton,gpu,math,log,logarithm
---

# tl.log

Element-wise natural logarithm (base e).

## Syntax

```python
tl.log(x)
```

## Description

Computes `ln(x)` for each element of the input tensor. Uses hardware-accelerated approximations on GPU. Commonly used in loss functions like cross-entropy, and in log-space probability computations.

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| x | Block | Input tensor (must be positive) |

## Returns

| Type | Description |
|------|-------------|
| Block | `ln(x)` for each element |

## Semantics

```pseudo
for each element:
    output[i] = ln(input[i])
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

# Cross-entropy loss: -sum(y * log(p))
logits = tl.load(logits_ptr + offsets, mask=mask)
labels = tl.load(labels_ptr + offsets, mask=mask)
log_probs = tl.log(tl.softmax(logits, axis=0))
loss = -tl.sum(labels * log_probs)
```