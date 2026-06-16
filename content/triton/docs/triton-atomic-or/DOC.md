---
name: triton-atomic-or
description: Atomic bitwise OR at a memory location
metadata:
  languages: triton
  versions: '2.1'
  revision: 1
  updated-on: '2026-06-16'
  source: official
  tags: triton,gpu,atomic,or,bitwise
---

# tl.atomic-or

Atomically performs a bitwise OR between `val` and the value at `pointer`. Used to atomically set flags or combine bitmasks across threads.

## Syntax

```python
tl.atomic_or(pointer, val, mask=None, sem=None, scope=None)
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| pointer | Block | Address tensor |
| val | Block | Value for OR |
| mask | Block (optional) | Boolean mask |
| sem | str (optional) | Memory semantics |
| scope | str (optional) | Visibility scope |

## Returns

| Type | Description |
|------|-------------|
| Block | Old value before the OR |

## Triton Version

Triton 2.1+

## Target Architecture

NVIDIA GPU (SM 7.0+), AMD GPU (CDNA2+), Intel GPU

## Example

```python
import triton.language as tl

tl.atomic_or(flags_ptr, error_flag, sem="release")
```
