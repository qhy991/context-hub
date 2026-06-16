---
name: triton-store
description: Store data from registers to global or shared memory
metadata:
  languages: triton
  versions: '2.1'
  revision: 1
  updated-on: '2026-06-16'
  source: official
  tags: triton,gpu,memory,store,vector
---

# tl.store

Store a block of data from registers to DRAM or shared memory.

## Syntax

```python
tl.store(pointer, value, mask=None, boundary_check=(), cache_modifier="", eviction_policy="")
```

## Description

Writes `value` to the addresses specified by `pointer`. `mask` blocks out-of-bounds writes. `boundary_check` selects which dimensions are bounds-checked. `cache_modifier` controls write-through vs. write-back caching (e.g., `".wb"`, `".cg"`, `".cs"`, `".wt"`). `eviction_policy` provides cache eviction hints.

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| pointer | Block | 1D/2D/Nd pointer tensor of addresses |
| value | Block | Data tensor to write |
| mask | Block (optional) | Boolean mask; True = write, False = skip |
| boundary_check | tuple | Dimensions to bounds-check (0, 1, …) |
| cache_modifier | str | Cache hint: `""`, `".wb"`, `".cg"`, `".cs"`, `".wt"` |
| eviction_policy | str | Eviction hint: `""`, `"evict_first"`, `"evict_last"` |

## Semantics

```pseudo
for each element in value tensor:
    if mask is None or mask[element] == True:
        DRAM[pointer[element]] = value[element]
```

## Triton Version

Triton 2.1+

## Target Architecture

NVIDIA GPU (SM 7.0+), AMD GPU (CDNA2+ / RDNA3+), Intel GPU

## Related Instructions

- [tl.load](../triton-load/DOC.md)
- [tl.atomic_xchg](../triton-atomic-xchg/DOC.md)

## Example

```python
import triton.language as tl

# Store result back to global memory
out = x + y  # computation in registers
tl.store(out_ptr + offsets, out, mask=mask)
```