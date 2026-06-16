---
name: triton-softmax
description: Element-wise softmax function along a given axis
metadata:
  languages: triton
  versions: '2.1'
  revision: 1
  updated-on: '2026-06-16'
  source: official
  tags: triton,gpu,math,softmax,activation
---

# tl.softmax

Element-wise softmax function along a given axis.

## Syntax

```python
tl.softmax(x, axis=None)
```

## Description

Computes the softmax function along the specified axis. The implementation is numerically stable: it subtracts the maximum value before exponentiating to avoid overflow. Softmax normalizes values to sum to 1, producing a probability distribution.

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| x | Block | Input tensor |
| axis | int (optional) | Axis along which to compute softmax |

## Returns

| Type | Description |
|------|-------------|
| Block | `softmax(x)` — probability distribution summing to 1 |

## Semantics

```pseudo
x_max = max(x, axis, keep_dims=True)
x_exp = exp(x - x_max)
x_sum = sum(x_exp, axis, keep_dims=True)
output = x_exp / x_sum
```

## Triton Version

Triton 2.1+

## Target Architecture

NVIDIA GPU (SM 7.0+), AMD GPU (CDNA2+), Intel GPU

## Related Instructions

- [tl.exp](../triton-exp/DOC.md)
- [tl.sum](../triton-sum/DOC.md)
- [tl.max](../triton-max/DOC.md)

## Example

```python
import triton.language as tl

# Fused softmax kernel
@triton.jit
def softmax_kernel(x_ptr, out_ptr, N, BLOCK: tl.constexpr):
    offsets = tl.program_id(0) * BLOCK + tl.arange(0, BLOCK)
    mask = offsets < N
    x = tl.load(x_ptr + offsets, mask=mask, other=-float('inf'))
    output = tl.softmax(x)
    tl.store(out_ptr + offsets, output, mask=mask)
```