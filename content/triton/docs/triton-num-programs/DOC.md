---
name: triton-num-programs
description: Returns the total number of program instances along a grid axis
metadata:
  languages: triton
  versions: '2.1'
  revision: 1
  updated-on: '2026-06-16'
  source: official
  tags: triton,gpu,indexing,num-programs,grid
---

# tl.num_programs

Returns the number of program instances launched along the given axis.

## Syntax

```python
tl.num_programs(axis)
```

## Description

Returns the total number of program instances (thread blocks) along the specified grid axis. Together with `tl.program_id`, this is used to compute per-block data ranges and handle boundary conditions. Valid axes are 0, 1, or 2.

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| axis | int | Grid axis: 0 (x), 1 (y), or 2 (z) |

## Returns

| Type | Description |
|------|-------------|
| tl.int32 | Total number of programs along the given axis |

## Semantics

```pseudo
nprogs = grid_size_along_axis[axis]
# Each program's pid = 0, 1, ..., nprogs - 1
```

## Triton Version

Triton 2.1+

## Target Architecture

NVIDIA GPU (SM 7.0+), AMD GPU (CDNA2+ / RDNA3+), Intel GPU

## Related Instructions

- [tl.program_id](../triton-program-id/DOC.md)

## Example

```python
import triton.language as tl

@triton.jit
def vector_add_kernel(x_ptr, y_ptr, out_ptr, N, BLOCK: tl.constexpr):
    pid = tl.program_id(0)
    nprogs = tl.num_programs(0)
    # Each block handles N / nprogs elements (strided access)
    for i in range(pid, N, nprogs * BLOCK):
        offsets = i + tl.arange(0, BLOCK)
        mask = offsets < N
        x = tl.load(x_ptr + offsets, mask=mask)
        y = tl.load(y_ptr + offsets, mask=mask)
        tl.store(out_ptr + offsets, x + y, mask=mask)
```