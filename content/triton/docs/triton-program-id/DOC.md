---
name: triton-program-id
description: Returns the current program instance ID along a grid axis
metadata:
  languages: triton
  versions: '2.1'
  revision: 1
  updated-on: '2026-06-16'
  source: official
  tags: triton,gpu,indexing,program-id,grid
---

# tl.program_id

Returns the id of the current program instance along the given axis.

## Syntax

```python
tl.program_id(axis)
```

## Description

Returns the index of the current program instance (thread block) along the specified grid axis. This is the fundamental mechanism for data-parallel decomposition in Triton: each program instance uses `program_id` to compute its slice of the input data. Valid axes are 0, 1, or 2, corresponding to the (x, y, z) dimensions of the launch grid.

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| axis | int | Grid axis: 0 (x), 1 (y), or 2 (z) |

## Returns

| Type | Description |
|------|-------------|
| tl.int32 | Scalar program ID along the given axis |

## Semantics

```pseudo
pid = grid_index_along_axis[axis]
# pid ∈ [0, num_programs(axis) - 1]
```

## Triton Version

Triton 2.1+

## Target Architecture

NVIDIA GPU (SM 7.0+), AMD GPU (CDNA2+ / RDNA3+), Intel GPU

## Related Instructions

- [tl.num_programs](../triton-num-programs/DOC.md)
- [tl.arange](../triton-arange/DOC.md)

## Example

```python
import triton.language as tl

@triton.jit
def kernel(x_ptr, out_ptr, N, BLOCK: tl.constexpr):
    # 1D grid: pid gives the block offset
    pid = tl.program_id(0)
    offsets = pid * BLOCK + tl.arange(0, BLOCK)
    mask = offsets < N
    x = tl.load(x_ptr + offsets, mask=mask)
    tl.store(out_ptr + offsets, x * 2, mask=mask)
```