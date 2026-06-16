---
name: triton-max-contiguous
description: Hint that elements form contiguous groups in memory
metadata:
  languages: triton
  versions: '2.1'
  revision: 1
  updated-on: '2026-06-16'
  source: official
  tags: triton,gpu,compiler,hint,contiguous
---

# tl.max-contiguous

Informs the compiler that consecutive `group_size` elements are contiguous, enabling vectorized loads/stores.

## Syntax

```python
tl.max_contiguous(value, group_size)
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| value | tensor | Value the hint applies to |
| group_size | int | Size of contiguous groups |

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

tl.max_contiguous(ptr, BLOCK)  # hint: consecutive addresses
```
