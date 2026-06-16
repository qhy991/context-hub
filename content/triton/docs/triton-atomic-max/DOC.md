---
name: triton-atomic-max
description: Atomic maximum operation at a memory location
metadata:
  languages: triton
  versions: '2.1'
  revision: 1
  updated-on: '2026-06-16'
  source: official
  tags: triton,gpu,memory,atomic,max
---

# tl.atomic_max

Performs an atomic maximum at the memory location specified by pointer.

## Syntax

```python
tl.atomic_max(pointer, val, mask=None, sem=None, scope=None)
```

## Description

Atomically updates `pointer` to `max(old_value, val)`. Returns the old value. Useful for computing global maxima across thread blocks without a separate reduction pass.

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
DRAM[pointer] = max(old, val)
return old
```

## Triton Version

Triton 2.1+

## Target Architecture

NVIDIA GPU (SM 6.0+), AMD GPU (CDNA2+), Intel GPU

## Related Instructions

- [tl.atomic_min](../triton-atomic-min/DOC.md)
- [tl.atomic_add](../triton-atomic-add/DOC.md)
- [tl.max](../triton-max/DOC.md)

## Example

```python
import triton.language as tl

# Track global maximum value across all blocks
local_max = tl.max(tl.load(data_ptr + offsets, mask=mask))
tl.atomic_max(global_max_ptr, local_max, sem="relaxed")
```