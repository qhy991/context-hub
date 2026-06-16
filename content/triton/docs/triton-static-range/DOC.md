---
name: triton-static-range
description: Static range iterator (compile-time unrolled)
metadata:
  languages: triton
  versions: '2.1'
  revision: 1
  updated-on: '2026-06-16'
  source: official
  tags: triton,gpu,range,iterator,static
---

# tl.static-range

Like `tl.range` but start/end/step must be compile-time constants. Fully unrolled.

## Syntax

```python
for i in tl.static_range(start, end, step=1):
    ...
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| start | int (constexpr) | Start value |
| end | int (constexpr) | End value (exclusive) |
| step | int (constexpr) | Step size (default 1) |

## Returns

| Type | Description |
|------|-------------|
| Block | Compile-time loop iterator |

## Triton Version

Triton 2.1+

## Target Architecture

NVIDIA GPU (SM 7.0+), AMD GPU (CDNA2+), Intel GPU

## Example

```python
import triton.language as tl

for i in tl.static_range(0, 4):
    tl.static_print("iteration", i)
```
