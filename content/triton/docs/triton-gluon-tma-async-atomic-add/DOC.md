---
name: triton-gluon-tma-async-atomic-add
description: TMA-based asynchronous atomic addition (Gluon experimental)
metadata:
  languages: triton
  versions: '3.0'
  revision: 1
  updated-on: '2026-06-16'
  source: official
  tags: triton,gpu,gluon,experimental,tma,atomic,hopper
---

# tl.gluon.nvidia.hopper.tma.async_atomic_add

TMA-based asynchronous atomic addition at a memory location.

## Syntax

```python
from triton.experimental.gluon.language.nvidia.hopper import tma

tma.async_atomic_add(tensor_desc, coord, value)
```

## Description

Performs an atomic addition using TMA hardware. Unlike `tl.atomic_add` which uses the LSU atomic subunit, this uses the TMA unit for asynchronous atomic operations. The TMA provides higher throughput for batched atomic operations on Hopper+ GPUs. Also available: `async_atomic_min`, `async_atomic_max`, `async_atomic_and`, `async_atomic_or`, `async_atomic_xor`.

## Hardware Unit

Tensor Memory Accelerator (TMA) — Atomic Subunit

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| tensor_desc | tensor_descriptor | Descriptor for the target tensor |
| coord | list[tensor] | Target coordinates |
| value | tensor | Value to atomically add |

## Triton Version

Triton 3.0+ (experimental)

## Target Architecture

NVIDIA GPU (SM 9.0+ Hopper / SM 10.0+ Blackwell)

## Related Instructions

- [async_load](../triton-gluon-tma-async-load/DOC.md)
- [tl.atomic_add](../triton-atomic-add/DOC.md)

## Example

```python
from triton.experimental.gluon.language.nvidia.hopper import tma

# TMA histogram accumulation
hist_desc = tma.make_tensor_descriptor(hist_ptr, shape=[NUM_BINS], strides=[1],
                                        block_shape=[1], layout=shared_layout)
tma.async_atomic_add(hist_desc, [bin_idx], 1)
```