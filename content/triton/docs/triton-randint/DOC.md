---
name: triton-randint
description: Generate random int32 values using Philox PRNG
metadata:
  languages: triton
  versions: '2.1'
  revision: 1
  updated-on: '2026-06-16'
  source: official
  tags: triton,gpu,random,randint,integer
---

# tl.randint

Generates random int32 values using Philox counter-based PRNG. Deterministic for same seed+offset.

## Syntax

```python
tl.randint(seed, offset)
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| seed | tl.uint32 | Random seed (scalar) |
| offset | Block (uint32) | Per-element offsets |

## Returns

| Type | Description |
|------|-------------|
| Block | Block of random int32 values |

## Triton Version

Triton 2.1+

## Target Architecture

NVIDIA GPU (SM 7.0+), AMD GPU (CDNA2+), Intel GPU

## Example

```python
import triton.language as tl

r_int = tl.randint(seed, offs)  # random int32
```
