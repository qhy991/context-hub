---
name: triton-expect-zero
description: Hint that a tensor is expected to be all zeros
metadata:
  languages: triton
  versions: '2.1'
  revision: 1
  updated-on: '2026-06-16'
  source: official
  tags: triton,gpu,compiler,hint,zero
---

# tl.expect-zero

Informs the compiler that tensor `x` is likely all zeros, enabling optimization.

## Syntax

```python
tl.expect_zero(x)
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| x | Block | Tensor expected to be zero |

## Returns

| Type | Description |
|------|-------------|
| Block | None (compiler hint) |

## Triton Version

Triton 2.1+

## Target Architecture

NVIDIA GPU (SM 7.0+), AMD GPU (CDNA2+), Intel GPU

## Example

```python
import triton.language as tl

tl.expect_zero(accumulator)
```
