---
name: triton-static-print
description: Print values at compile time (debug utility)
metadata:
  languages: triton
  versions: '2.1'
  revision: 1
  updated-on: '2026-06-16'
  source: official
  tags: triton,gpu,debug,static-print,compile-time
---

# tl.static-print

Prints values at JIT compile time. Useful for debugging kernel parameter values.

## Syntax

```python
tl.static_print(*values)
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| *values | any | Values to print at compile time |

## Returns

| Type | Description |
|------|-------------|
| Block | None |

## Triton Version

Triton 2.1+

## Target Architecture

NVIDIA GPU (SM 7.0+), AMD GPU (CDNA2+), Intel GPU

## Example

```python
import triton.language as tl

tl.static_print("BLOCK_M =", BLOCK_M, "num_warps =", num_warps)
```
