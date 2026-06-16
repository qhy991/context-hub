---
name: triton-trans
description: Permute the dimensions of a tensor
metadata:
  languages: triton
  versions: '2.1'
  revision: 1
  updated-on: '2026-06-16'
  source: official
  tags: triton,gpu,shape,transpose,permute
---

# tl.trans

Permute the dimensions of a tensor.

## Syntax

```python
tl.trans(input, perm=None)
```

## Description

Returns a tensor with dimensions permuted according to `perm`. When `perm` is None (default), reverses all dimensions. When `perm` is provided, it specifies the new order of dimensions. This is a zero-cost metadata operation — no data is moved.

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| input | Block | Input tensor |
| perm | tuple (optional) | Permutation of dimensions (e.g., (1, 0) for 2D transpose) |

## Returns

| Type | Description |
|------|-------------|
| Block | Transposed tensor |

## Semantics

```pseudo
output[i_perm[0], i_perm[1], ...] = input[i_0, i_1, ...]
```

## Triton Version

Triton 2.1+

## Target Architecture

NVIDIA GPU (SM 7.0+), AMD GPU (CDNA2+), Intel GPU

## Related Instructions

- [tl.view](../triton-view/DOC.md)
- [tl.reshape](../triton-reshape/DOC.md)

## Example

```python
import triton.language as tl

# Standard 2D transpose
x = tl.load(x_ptr + offsets)  # shape (M, N)
x_t = tl.trans(x)  # shape (N, M)

# In matmul, transpose B matrix for KxN → NxK
a = tl.load(a_ptrs)  # (BLOCK_M, BLOCK_K)
b = tl.load(b_ptrs)  # (BLOCK_N, BLOCK_K)
accumulator = tl.dot(a, tl.trans(b), accumulator)  # A × B^T
```