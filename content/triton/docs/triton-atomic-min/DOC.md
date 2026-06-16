---
name: triton-atomic-min
description: Atomic minimum operation at a memory location
metadata:
  languages: triton
  versions: '2.1'
  revision: 1
  updated-on: '2026-06-16'
  source: official
  tags: triton,gpu,memory,atomic,min
---

# tl.atomic_min

Performs an atomic minimum at the memory location specified by pointer.

## Syntax

```python
tl.atomic_min(pointer, val, mask=None, sem=None, scope=None)
```

## Description

Atomically updates `pointer` to `min(old_value, val)`. Returns the old value. Useful for computing global minima across thread blocks.

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| pointer | Block | Address tensor |
| val | Block | Value to compare |
| mask | Block (optional) | Boolean mask |
| sem | str (optional) | Memory semantics |
| scope | str (optional) | Visibility scope |

## Semantics

```pseudo
old = DRAM[pointer]
DRAM[pointer] = min(old, val)
return old
```

## Triton Version

Triton 2.1+

## Target Architecture

NVIDIA GPU (SM 6.0+), AMD GPU (CDNA2+), Intel GPU

## Related Instructions

- [tl.atomic_max](../triton-atomic-max/DOC.md)
- [tl.atomic_add](../triton-atomic-add/DOC.md)
- [tl.min](../triton-min/DOC.md)

## Example

```python
import triton.language as tl

# Track global minimum value across all blocks
local_min = tl.min(tl.load(data_ptr + offsets, mask=mask))
tl.atomic_min(global_min_ptr, local_min, sem="relaxed")
```