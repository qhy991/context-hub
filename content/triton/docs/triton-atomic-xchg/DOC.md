---
name: triton-atomic-xchg
description: Atomic exchange (swap) at a memory location
metadata:
  languages: triton
  versions: '2.1'
  revision: 1
  updated-on: '2026-06-16'
  source: official
  tags: triton,gpu,memory,atomic,xchg,swap
---

# tl.atomic_xchg

Performs an atomic exchange at the memory location specified by pointer.

## Syntax

```python
tl.atomic_xchg(pointer, val, mask=None, sem=None, scope=None)
```

## Description

Atomically writes `val` to `pointer` and returns the old value. This is an unconditional swap — no comparison is performed. Useful for setting flags, releasing locks, and implementing simple state machines in shared memory.

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| pointer | Block | Address tensor |
| val | Block | New value to write |
| mask | Block (optional) | Boolean mask |
| sem | str (optional) | Memory semantics: `"acq_rel"`, `"acquire"`, `"release"`, `"relaxed"` |
| scope | str (optional) | Visibility scope: `"gpu"`, `"cta"`, `"sys"` |

## Semantics

```pseudo
old = DRAM[pointer]
DRAM[pointer] = val
return old
```

## Triton Version

Triton 2.1+

## Target Architecture

NVIDIA GPU (SM 6.0+), AMD GPU (CDNA2+), Intel GPU

## Related Instructions

- [tl.atomic_cas](../triton-atomic-cas/DOC.md)
- [tl.atomic_add](../triton-atomic-add/DOC.md)

## Example

```python
import triton.language as tl

# Release a lock by atomically setting it to 0
tl.atomic_xchg(mutex_ptr, 0, sem="release")

# Reset a counter and get the old value
old_count = tl.atomic_xchg(counter_ptr, 0, sem="acq_rel")
```