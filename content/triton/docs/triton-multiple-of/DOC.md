---
name: triton-multiple-of
description: Hint to the compiler that a value is a multiple of a given number
metadata:
  languages: triton
  versions: '2.1'
  revision: 1
  updated-on: '2026-06-16'
  source: official
  tags: triton,gpu,compiler,hint,alignment
---

# tl.multiple-of

Informs the compiler that `value` is a multiple of `divisor`, enabling pointer alignment and loop optimizations.

## Syntax

```python
tl.multiple_of(value, divisor)
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| value | tensor | Value the hint applies to |
| divisor | int | The divisor |

## Returns

| Type | Description |
|------|-------------|
| Block | None (compiler hint) |

## Triton Version

Triton 2.1+

## Target Architecture

NVIDIA GPU (SM 7.0+), AMD GPU (CDNA2+), Intel GPU

## Example

```python
import triton.language as tl

tl.multiple_of(x_ptr, 16)  # hint: 16-byte aligned pointer
```
