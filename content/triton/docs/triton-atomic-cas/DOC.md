---
name: triton-atomic-cas
description: Atomic compare-and-swap at a memory location
metadata:
  languages: triton
  versions: '2.1'
  revision: 1
  updated-on: '2026-06-16'
  source: official
  tags: triton,gpu,memory,atomic,cas,compare-and-swap
---

# tl.atomic_cas

Performs an atomic compare-and-swap at the memory location specified by pointer.

## Syntax

```python
tl.atomic_cas(pointer, cmp, val, mask=None, sem=None, scope=None)
```

## Description

Atomically compares the value at `pointer` with `cmp`. If they are equal, writes `val` to the address. Otherwise, no write occurs. The original value at `pointer` is always returned. This is the fundamental building block for implementing locks, mutexes, and custom atomic operations.

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| pointer | Block | Address tensor |
| cmp | Block | Expected value to compare against |
| val | Block | New value to write if comparison succeeds |
| mask | Block (optional) | Boolean mask |
| sem | str (optional) | Memory semantics: `"acq_rel"`, `"acquire"`, `"release"`, `"relaxed"` |
| scope | str (optional) | Visibility scope: `"gpu"`, `"cta"`, `"sys"` |

## Semantics

```pseudo
old = DRAM[pointer]
if old == cmp:
    DRAM[pointer] = val
return old
```

## Triton Version

Triton 2.1+

## Target Architecture

NVIDIA GPU (SM 6.0+), AMD GPU (CDNA2+), Intel GPU

## Related Instructions

- [tl.atomic_add](../triton-atomic-add/DOC.md)
- [tl.atomic_xchg](../triton-atomic-xchg/DOC.md)

## Example

```python
import triton.language as tl

@triton.jit
def mutex_lock(mutex_ptr, BLOCK: tl.constexpr):
    # Spin until we acquire the lock (CAS 0 → 1)
    while tl.atomic_cas(mutex_ptr, 0, 1, sem="acq_rel") != 0:
        pass  # busy-wait

@triton.jit
def mutex_unlock(mutex_ptr):
    tl.atomic_xchg(mutex_ptr, 0, sem="release")
```