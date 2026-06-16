---
name: triton-swizzle2d
description: Transform row-major indices to column-major for shared memory access
metadata:
  languages: triton
  versions: '2.1'
  revision: 1
  updated-on: '2026-06-16'
  source: official
  tags: triton,gpu,swizzle,shared-memory,bank-conflict
---

# tl.swizzle2d

Transforms row-major 2D indices into column-major indices for groups of `size_g` rows. This is a shared memory bank conflict avoidance technique. By swizzling the memory layout, accesses that would hit the same bank are redistributed across banks.

## Syntax

```python
tl.swizzle2d(i, j, size_i, size_j, size_g)
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| i | Block | Row indices |
| j | Block | Column indices |
| size_i | int | Number of rows |
| size_j | int | Number of columns |
| size_g | int | Group size for row grouping |

## Returns

| Type | Description |
|------|-------------|
| Block | Swizzled index tensor |

## Triton Version

Triton 2.1+

## Target Architecture

NVIDIA GPU (SM 7.0+), AMD GPU (CDNA2+), Intel GPU

## Related Instructions

- [tl.load](../triton-load/DOC.md)
- [tl.store](../triton-store/DOC.md)

## Example

```python
import triton.language as tl

# Avoid bank conflicts when loading matrix
swizzled_idx = tl.swizzle2d(row_idx, col_idx, M, N, 8)
```
