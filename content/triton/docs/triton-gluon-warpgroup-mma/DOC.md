---
name: triton-gluon-warpgroup-mma
description: Warpgroup matrix multiply-accumulate on Hopper Tensor Cores (Gluon experimental)
metadata:
  languages: triton
  versions: '3.0'
  revision: 1
  updated-on: '2026-06-16'
  source: official
  tags: triton,gpu,gluon,experimental,warpgroup,mma,tensor-core,hopper
---

# tl.gluon.nvidia.hopper.warpgroup_mma

Warpgroup-level matrix multiply-accumulate on Hopper Tensor Cores.

## Syntax

```python
from triton.experimental.gluon.language.nvidia.hopper import warpgroup_mma, warpgroup_mma_wait

# Initialize accumulator
acc = warpgroup_mma_init(shape, dtype)

# MMA operation
accumulator = warpgroup_mma(a, b, accumulator, mma_type)

# Wait for MMA to complete
warpgroup_mma_wait(groups=1)
```

## Description

The Hopper SM introduces warpgroup-level MMA (wgmma) instructions that span all 4 warps of a warpgroup. This provides higher throughput than the per-warp `tl.dot` on older architectures. `warpgroup_mma_init` allocates an accumulator in the warpgroup's distributed register file. `warpgroup_mma_wait` synchronizes completion of pending MMA operations.

## Hardware Unit

Tensor Core (Hopper Warpgroup MMA)

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| a | tensor | Left operand matrix |
| b | tensor | Right operand matrix |
| accumulator | warpgroup_accumulator | Accumulator from `warpgroup_mma_init` |
| mma_type | constexpr | MMA instruction variant |
| groups | int | Number of pending MMA groups to wait on |

## Triton Version

Triton 3.0+ (experimental)

## Target Architecture

NVIDIA GPU (SM 9.0+ Hopper / SM 10.0+ Blackwell)

## Related Instructions

- [tl.dot](../triton-dot/DOC.md)
- [async_load](../triton-gluon-tma-async-load/DOC.md)

## Example

```python
from triton.experimental.gluon.language.nvidia.hopper import (
    warpgroup_mma, warpgroup_mma_wait, warpgroup_mma_init
)

# Initialize accumulator
acc = warpgroup_mma_init((BLOCK_M, BLOCK_N), dtype=tl.float32)

# Async TMA load + warpgroup MMA pipeline
for k in range(0, K, BLOCK_K):
    tma.async_load(a_desc, [offs_am, k], barrier, a_buf)
    tma.async_load(b_desc, [k, offs_bn], barrier, b_buf)
    mbarrier.wait(barrier)
    acc = warpgroup_mma(a_buf, b_buf, acc)
    warpgroup_mma_wait(1)
```