---
name: triton-atomic-add
description: Atomic floating-point addition to global or shared memory
metadata:
  languages: triton
  versions: '2.1'
  revision: 1
  updated-on: '2026-06-16'
  source: official
  tags: triton,gpu,memory,atomic,add,reduction
---

# tl.atomic_add

Performs an atomic add at the memory location specified by pointer.

## Syntax

```python
tl.atomic_add(pointer, val, mask=None, sem=None, scope=None)
```

## Description

Atomically adds `val` to the value at `pointer`. The operation is guaranteed to be atomic with respect to other atomic operations across all thread blocks. `sem` specifies the memory semantics (e.g., `"acq_rel"`, `"relaxed"`). `scope` specifies the visibility scope (e.g., `"gpu"`, `"cta"`).

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| pointer | Block | Address tensor to atomically add to |
| val | Block | Value to add |
| mask | Block (optional) | Boolean mask |
| sem | str (optional) | Memory semantics: `"acq_rel"`, `"acquire"`, `"release"`, `"relaxed"` |
| scope | str (optional) | Visibility scope: `"gpu"`, `"cta"`, `"sys"` |

## Semantics

```pseudo
old = DRAM[pointer]
DRAM[pointer] = old + val
return old  # Typically ignored in Triton
```

## Triton Version

Triton 2.1+

## Target Architecture

NVIDIA GPU (SM 6.0+), AMD GPU (CDNA2+), Intel GPU

## Related Instructions

- [tl.atomic_cas](../triton-atomic-cas/DOC.md)
- [tl.atomic_xchg](../triton-atomic-xchg/DOC.md)
- [tl.sum](../triton-sum/DOC.md)

## Example

```python
import triton.language as tl

@triton.jit
def histogram_kernel(data_ptr, hist_ptr, N, BLOCK: tl.constexpr):
    pid = tl.program_id(0)
    offsets = pid * BLOCK + tl.arange(0, BLOCK)
    mask = offsets < N
    data = tl.load(data_ptr + offsets, mask=mask)
    # Atomically increment histogram bin
    tl.atomic_add(hist_ptr + data, 1, mask=mask, sem="relaxed")
```