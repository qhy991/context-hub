---
name: triton-range
description: Iterator that counts upward indefinitely (compile-time unrolled)
metadata:
  languages: triton
  versions: '2.1'
  revision: 1
  updated-on: '2026-06-16'
  source: official
  tags: triton,gpu,range,iterator,loop
---

# tl.range

An iterator for compile-time unrolled loops. Unlike Python's `range`, `tl.range` is evaluated at compile time and each iteration generates separate instructions. Used for tiled computation loops (e.g., iterating over K dimension in matrix multiply). The `warp_specialize` parameter enables warp specialization.

## Syntax

```python
for k in tl.range(start, end, step=1):
    ...
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| start | int | Start value |
| end | int | End value (exclusive) |
| step | int | Step size (default 1) |
| warp_specialize | bool | Enable warp specialization (default False) |

## Returns

| Type | Description |
|------|-------------|
| Block | Compile-time loop iterator |

## Triton Version

Triton 2.1+

## Target Architecture

NVIDIA GPU (SM 7.0+), AMD GPU (CDNA2+), Intel GPU

## Related Instructions

- [tl.arange](../triton-arange/DOC.md)
- [tl.static_range](../triton-static-range/DOC.md)

## Example

```python
import triton.language as tl

for k in tl.range(0, K, BLOCK_K):
    a = tl.load(a_ptrs)
    b = tl.load(b_ptrs)
    acc = tl.dot(a, b, acc)
    a_ptrs += BLOCK_K
    b_ptrs += BLOCK_K
```
