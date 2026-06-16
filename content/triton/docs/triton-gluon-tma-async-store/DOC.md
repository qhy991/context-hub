---
name: triton-gluon-tma-async-store
description: Asynchronously store data from shared memory to global memory using TMA (Gluon experimental)
metadata:
  languages: triton
  versions: '3.0'
  revision: 1
  updated-on: '2026-06-16'
  source: official
  tags: triton,gpu,gluon,experimental,tma,async-store,hopper
---

# tl.gluon.nvidia.hopper.tma.async_store

Asynchronously store data from shared memory to global memory using TMA.

## Syntax

```python
from triton.experimental.gluon.language.nvidia.hopper import tma

tma.async_store(tensor_desc, coord, src)
```

## Description

Initiates an asynchronous TMA copy from shared memory to global memory. The destination is defined by `tensor_desc` at the position `coord`. The source `src` is a shared memory buffer. Use `tma.store_wait()` to ensure all pending stores have completed before the kernel exits.

## Hardware Unit

Tensor Memory Accelerator (TMA)

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| tensor_desc | tensor_descriptor | Descriptor for the destination tensor in global memory |
| coord | list[tensor] | Starting coordinates/offsets for each dimension |
| src | shared_mem | Source shared memory buffer |

## Triton Version

Triton 3.0+ (experimental)

## Target Architecture

NVIDIA GPU (SM 9.0+ Hopper / SM 10.0+ Blackwell)

## Related Instructions

- [async_load](../triton-gluon-tma-async-load/DOC.md)
- [store_wait](../triton-gluon-tma-async-store-wait/DOC.md)

## Example

```python
from triton.experimental.gluon.language.nvidia.hopper import tma

# Create output descriptor
c_desc = tma.make_tensor_descriptor(c_ptr, shape=[M, N], strides=[N, 1],
                                     block_shape=[BLOCK_M, BLOCK_N], layout=shared_layout)

# Async TMA store
tma.async_store(c_desc, [offs_cm, offs_cn], result)

# Wait for all stores to complete before kernel exit
tma.store_wait(pending_stores)
```