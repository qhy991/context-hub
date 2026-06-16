---
name: triton-atomic-and
description: Atomic bitwise AND at a memory location
metadata:
  languages: triton
  versions: '2.1'
  revision: 1
  updated-on: '2026-06-16'
  source: official
  tags: triton,gpu,atomic,and,bitwise
---

# tl.atomic-and

Atomically performs a bitwise AND between `val` and the value at `pointer`. Only the bits set in `val` can be cleared.

## Syntax

```python
tl.atomic_and(pointer, val, mask=None, sem=None, scope=None)
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| pointer | Block | Address tensor |
| val | Block | Value for AND |
| mask | Block (optional) | Boolean mask |
| sem | str (optional) | Memory semantics |
| scope | str (optional) | Visibility scope |

## Returns

| Type | Description |
|------|-------------|
| Block | Old value before the AND |

## Triton Version

Triton 2.1+

## Target Architecture

NVIDIA GPU (SM 7.0+), AMD GPU (CDNA2+), Intel GPU

## Example

```python
import triton.language as tl

tl.atomic_and(flags_ptr, ~bit_to_clear, sem="relaxed")
```
