---
name: triton-rand
description: Generate random float32 values from U(0,1) distribution
metadata:
  languages: triton
  versions: '2.1'
  revision: 1
  updated-on: '2026-06-16'
  source: official
  tags: triton,gpu,random,rand,uniform
---

# tl.rand

Generates uniformly distributed random float32 values in [0, 1) using Philox counter-based PRNG. `seed` provides the random seed, `offset` provides per-element offsets to generate independent streams. This is deterministic: same seed + offset produces same value.

## Syntax

```python
tl.rand(seed, offset)
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| seed | tl.uint32 | Random seed (scalar) |
| offset | Block (uint32) | Per-element offsets for independent streams |

## Returns

| Type | Description |
|------|-------------|
| Block | Block of U(0,1) float32 random values |

## Triton Version

Triton 2.1+

## Target Architecture

NVIDIA GPU (SM 7.0+), AMD GPU (CDNA2+), Intel GPU

## Related Instructions

- [tl.randn](../triton-randn/DOC.md)
- [tl.randint](../triton-randint/DOC.md)
- [tl.rand4x](../triton-rand4x/DOC.md)

## Example

```python
import triton.language as tl

seed = tl.program_id(0)
offs = pid * BLOCK + tl.arange(0, BLOCK)
r = tl.rand(seed, offs)  # uniform [0,1)
```
