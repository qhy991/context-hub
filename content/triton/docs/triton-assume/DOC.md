---
name: triton-assume
description: Hint to the compiler that a condition is always true
metadata:
  languages: triton
  versions: '2.1'
  revision: 1
  updated-on: '2026-06-16'
  source: official
  tags: triton,gpu,compiler,assume,hint
---

# tl.assume

Tells the compiler to assume that `condition` is always true. Enables optimizations not otherwise possible. Undefined behaviour if false at runtime.

## Syntax

```python
tl.assume(condition)
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| condition | bool | Condition the compiler can assume is true |

## Returns

| Type | Description |
|------|-------------|
| Block | None (compiler hint only) |

## Triton Version

Triton 2.1+

## Target Architecture

NVIDIA GPU (SM 7.0+), AMD GPU (CDNA2+), Intel GPU

## Example

```python
import triton.language as tl

tl.assume(N % BLOCK == 0)  # assume aligned; skip boundary checks
```
