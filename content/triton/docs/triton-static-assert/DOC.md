---
name: triton-static-assert
description: Assert a condition at compile time
metadata:
  languages: triton
  versions: '2.1'
  revision: 1
  updated-on: '2026-06-16'
  source: official
  tags: triton,gpu,debug,static-assert,compile-time
---

# tl.static-assert

Asserts that `condition` is true at JIT compile time. Must be evaluable at compile time.

## Syntax

```python
tl.static_assert(condition, message="")
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| condition | bool (constexpr) | Condition to check |
| message | str | Error message on failure |

## Returns

| Type | Description |
|------|-------------|
| Block | None (compile-time check) |

## Triton Version

Triton 2.1+

## Target Architecture

NVIDIA GPU (SM 7.0+), AMD GPU (CDNA2+), Intel GPU

## Example

```python
import triton.language as tl

tl.static_assert(BLOCK % 16 == 0, "BLOCK must be multiple of 16")
```
