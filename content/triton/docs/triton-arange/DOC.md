---
name: triton-arange
description: Returns a contiguous range of values
metadata:
  languages: triton
  versions: '2.1'
  revision: 1
  updated-on: '2026-06-16'
  source: official
  tags: triton,gpu,creation,arange,indexing
---

# tl.arange

Returns a contiguous range of values from start to end (exclusive).

## Syntax

```python
tl.arange(start, end)
```

## Description

Creates a 1D tensor containing values `[start, start+1, ..., end-1]`. This is the fundamental building block for computing memory offsets in Triton kernels. Typically used with `program_id` to compute per-block data slices.

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| start | int | Start value (inclusive) |
| end | int | End value (exclusive) |

## Returns

| Type | Description |
|------|-------------|
| Block | 1D tensor of `[start, end)` with int32 dtype |

## Semantics

```pseudo
output = [start, start+1, ..., end-1]
```

## Triton Version

Triton 2.1+

## Target Architecture

NVIDIA GPU (SM 7.0+), AMD GPU (CDNA2+), Intel GPU

## Related Instructions

- [tl.zeros](../triton-zeros/DOC.md)
- [tl.full](../triton-full/DOC.md)
- [tl.program_id](../triton-program-id/DOC.md)

## Example

```python
import triton.language as tl

@triton.jit
def kernel(x_ptr, out_ptr, N, BLOCK: tl.constexpr):
    pid = tl.program_id(0)
    # offsets = [pid*BLOCK, pid*BLOCK+1, ..., pid*BLOCK+BLOCK-1]
    offsets = pid * BLOCK + tl.arange(0, BLOCK)
    mask = offsets < N
    x = tl.load(x_ptr + offsets, mask=mask)
    tl.store(out_ptr + offsets, x * 2, mask=mask)
```