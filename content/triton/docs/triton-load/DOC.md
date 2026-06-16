---
name: triton-load
description: Load data from global or shared memory into registers
metadata:
  languages: triton
  versions: '2.1'
  revision: 1
  updated-on: '2026-06-16'
  source: official
  tags: triton,gpu,memory,load,vector
---

# tl.load

Load a block of data from DRAM or shared memory into registers.

## Syntax

```python
tl.load(pointer, mask=None, other=None, boundary_check=(), cache_modifier="", eviction_policy="")
```

## Description

Loads a tensor from memory into registers. `pointer` is an address tensor (1D/2D/Nd) that returns the address of each element. `mask` blocks out-of-bounds accesses. `other` fills masked-out positions (default 0). `boundary_check` selects which dimensions are bounds-checked. `cache_modifier` controls L1/L2 caching (e.g., `".ca"`, `".cg"`, `".cs"`). `eviction_policy` controls cache eviction hints.

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| pointer | Block | 1D/2D/Nd pointer tensor of addresses |
| mask | Block (optional) | Boolean mask; True = valid, False = masked |
| other | float (optional) | Fill value for masked-out positions |
| boundary_check | tuple | Dimensions to bounds-check (0, 1, …) |
| cache_modifier | str | Cache hint: `""`, `".ca"`, `".cg"`, `".cs"`, `".wt"` |
| eviction_policy | str | Eviction hint: `""`, `"evict_first"`, `"evict_last"` |

## Semantics

```pseudo
for each element in output tensor:
    if mask is None or mask[element] == True:
        output[element] = DRAM[pointer[element]]
    else:
        output[element] = other  # default 0
```

## Triton Version

Triton 2.1+

## Target Architecture

NVIDIA GPU (SM 7.0+), AMD GPU (CDNA2+ / RDNA3+), Intel GPU

## Related Instructions

- [tl.store](../triton-store/DOC.md)
- [tl.atomic_add](../triton-atomic-add/DOC.md)

## Example

```python
import triton.language as tl

@triton.jit
def vector_add_kernel(x_ptr, y_ptr, out_ptr, N, BLOCK: tl.constexpr):
    pid = tl.program_id(0)
    offsets = pid * BLOCK + tl.arange(0, BLOCK)
    mask = offsets < N
    x = tl.load(x_ptr + offsets, mask=mask)
    y = tl.load(y_ptr + offsets, mask=mask)
    out = x + y
    tl.store(out_ptr + offsets, out, mask=mask)
```