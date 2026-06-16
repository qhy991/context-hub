---
name: triton-atomic-xor
description: Atomic bitwise XOR at a memory location
metadata:
  languages: triton
  versions: '2.1'
  revision: 1
  updated-on: '2026-06-16'
  source: official
  tags: triton,gpu,atomic,xor,bitwise
---

# tl.atomic-xor

Atomically performs a bitwise XOR between `val` and the value at `pointer`. Useful for toggle operations and parity tracking.

## Syntax

```python
tl.atomic_xor(pointer, val, mask=None, sem=None, scope=None)
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| pointer | Block | Address tensor |
| val | Block | Value for XOR |
| mask | Block (optional) | Boolean mask |
| sem | str (optional) | Memory semantics |
| scope | str (optional) | Visibility scope |

## Returns

| Type | Description |
|------|-------------|
| Block | Old value before the XOR |

## Triton Version

Triton 2.1+

## Target Architecture

NVIDIA GPU (SM 7.0+), AMD GPU (CDNA2+), Intel GPU

## Example

```python
import triton.language as tl

tl.atomic_xor(parity_ptr, 1, sem="relaxed")  # toggle
```
