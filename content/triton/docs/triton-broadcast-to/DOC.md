---
name: triton-broadcast-to
description: Broadcast a tensor to a new shape
metadata:
  languages: triton
  versions: '2.1'
  revision: 1
  updated-on: '2026-06-16'
  source: official
  tags: triton,gpu,shape,broadcast
---

# tl.broadcast_to

Broadcast a tensor to a new shape.

## Syntax

```python
tl.broadcast_to(tensor, shape)
```

## Description

Expands `tensor` to `shape` following NumPy broadcasting rules. Dimensions of size 1 are stretched to match the target shape. This is commonly used to align row and column vectors for element-wise operations in matrix computations.

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| tensor | Block | Input tensor to broadcast |
| shape | tuple | Target shape |

## Returns

| Type | Description |
|------|-------------|
| Block | Broadcasted tensor of the target shape |

## Semantics

```pseudo
# NumPy-compatible broadcasting rules
for each dimension from right to left:
    if input_dim == 1 and target_dim > 1:
        replicate along that dimension
    elif input_dim == target_dim:
        keep as is
    else:
        error
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

# Row vector broadcast to match matrix columns
offs_m = tl.arange(0, BLOCK_M)[:, None]  # shape (BLOCK_M, 1)
offs_n = tl.arange(0, BLOCK_N)[None, :]  # shape (1, BLOCK_N)

# Broadcast for 2D mask
mask = (offs_m < M) & (offs_n < N)  # broadcasts to (BLOCK_M, BLOCK_N)

# Explicit broadcast
row = tl.arange(0, BLOCK_N)
tile = tl.broadcast_to(row[None, :], (BLOCK_M, BLOCK_N))
```