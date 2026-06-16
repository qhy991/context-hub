---
name: triton-randint4x
description: Generate 4x random int32 values per element
metadata:
  languages: triton
  versions: '2.1'
  revision: 1
  updated-on: '2026-06-16'
  source: official
  tags: triton,gpu,random,randint4x,integer
---

# tl.randint4x

Generates 4 independent random int32 values per input element.

## Syntax

```python
r0, r1, r2, r3 = tl.randint4x(seed, offset)
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| seed | tl.uint32 | Random seed |
| offset | Block (uint32) | Per-element offsets |

## Returns

| Type | Description |
|------|-------------|
| Block | Tuple of 4 Block tensors of random int32 |

## Triton Version

Triton 2.1+

## Target Architecture

NVIDIA GPU (SM 7.0+), AMD GPU (CDNA2+), Intel GPU

## Example

```python
import triton.language as tl

r0, r1, r2, r3 = tl.randint4x(seed, offs)
```
