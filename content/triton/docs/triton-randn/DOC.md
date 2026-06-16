---
name: triton-randn
description: Generate random float32 values from N(0,1) distribution
metadata:
  languages: triton
  versions: '2.1'
  revision: 1
  updated-on: '2026-06-16'
  source: official
  tags: triton,gpu,random,randn,normal,gaussian
---

# tl.randn

Generates normally distributed random float32 values ~ N(0,1) using Box-Muller transform on Philox PRNG values.

## Syntax

```python
tl.randn(seed, offset)
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| seed | tl.uint32 | Random seed (scalar) |
| offset | Block (uint32) | Per-element offsets |

## Returns

| Type | Description |
|------|-------------|
| Block | Block of N(0,1) float32 random values |

## Triton Version

Triton 2.1+

## Target Architecture

NVIDIA GPU (SM 7.0+), AMD GPU (CDNA2+), Intel GPU

## Example

```python
import triton.language as tl

noise = tl.randn(seed, offs)  # Gaussian noise
```
