---
name: triton-config
description: Kernel configuration specifying block sizes, warps, and pipeline stages
metadata:
  languages: triton
  versions: '2.1'
  revision: 1
  updated-on: '2026-06-16'
  source: official
  tags: triton,gpu,config,autotune,programming-model
---

# triton.Config

Kernel configuration object used with `triton.autotune` to define block sizes and execution parameters.

## Syntax

```python
triton.Config(kwargs, num_warps=4, num_stages=2, num_ctas=1, maxnreg=None, enable_warp_specialization=False)
```

## Description

A `triton.Config` bundles the kernel's compile-time constants (`kwargs`) with execution parameters like warp count and pipeline stages. Each config is benchmarked by `triton.autotune` to find the best-performing combination for a given input shape.

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| kwargs | dict | Compile-time constant values (e.g., `{'BLOCK_M': 128}`) |
| num_warps | int | Number of warps per block (default 4) |
| num_stages | int | Number of pipeline stages for software pipelining (default 2) |
| num_ctas | int | Number of CTAs per cluster (default 1) |
| maxnreg | int (optional) | Maximum number of registers per thread |
| enable_warp_specialization | bool | Enable warp specialization (default False) |

## Triton Version

Triton 2.1+

## Target Architecture

NVIDIA GPU (SM 7.0+), AMD GPU (CDNA2+ / RDNA3+)

## Related Instructions

- [triton.autotune](../triton-autotune/DOC.md)
- [triton.jit](../triton-jit/DOC.md)

## Example

```python
import triton

# Config with large blocks for compute-bound kernels
config1 = triton.Config(
    {'BLOCK_M': 128, 'BLOCK_N': 256, 'BLOCK_K': 32},
    num_warps=8,
    num_stages=3
)

# Config with more warps for memory-bound kernels
config2 = triton.Config(
    {'BLOCK_M': 64, 'BLOCK_N': 128, 'BLOCK_K': 32},
    num_warps=4,
    num_stages=4
)
```