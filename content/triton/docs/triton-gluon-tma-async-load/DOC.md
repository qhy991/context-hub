---
name: triton-gluon-tma-async-load
description: Asynchronously load data from global memory to shared memory using TMA (Gluon experimental)
metadata:
  languages: triton
  versions: '3.0'
  revision: 1
  updated-on: '2026-06-16'
  source: official
  tags: triton,gpu,gluon,experimental,tma,async-load,hopper
---

# tl.gluon.nvidia.hopper.tma.async_load

Asynchronously load data from global memory to shared memory using TMA (Tensor Memory Accelerator).

## Syntax

```python
from triton.experimental.gluon.language.nvidia.hopper import tma

tma.async_load(tensor_desc, coord, barrier, result, pred=True, multicast=False)
```

## Description

Initiates an asynchronous TMA copy from global memory to shared memory. The source is defined by `tensor_desc` at the position `coord`. The destination is `result` (a shared memory buffer). `barrier` is an mbarrier used for synchronization — threads call `mbarrier.wait()` before accessing the loaded data. `multicast` enables broadcast to multiple CTAs within a cluster. This is the lowest-level TMA API in Triton, exposed through the `triton.experimental.gluon` namespace.

## Hardware Unit

Tensor Memory Accelerator (TMA)

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| tensor_desc | tensor_descriptor | Descriptor for the source tensor in global memory |
| coord | list[tensor] | Starting coordinates/offsets for each dimension |
| barrier | mbarrier | Mbarrier for synchronization |
| result | shared_mem | Destination shared memory buffer |
| pred | bool | Predication flag (default True) |
| multicast | bool | Enable cluster multicast (default False) |

## Triton Version

Triton 3.0+ (experimental)

## Target Architecture

NVIDIA GPU (SM 9.0+ Hopper / SM 10.0+ Blackwell)

## Related Instructions

- [async_store](../triton-gluon-tma-async-store/DOC.md)
- [async_load_im2col](../triton-gluon-tma-async-load-im2col/DOC.md)
- [store_wait](../triton-gluon-tma-async-store-wait/DOC.md)
- [mbarrier](../triton-gluon-mbarrier/DOC.md)

## Example

```python
from triton.experimental.gluon.language.nvidia.hopper import tma, mbarrier

# Create tensor descriptor
a_desc = tma.make_tensor_descriptor(a_ptr, shape=[M, K], strides=[K, 1],
                                     block_shape=[BLOCK_M, BLOCK_K], layout=shared_layout)

# Allocate mbarrier and shared memory
barrier = mbarrier.allocate_mbarrier()
result = tl.allocate_shared_memory((BLOCK_M, BLOCK_K), dtype=tl.float16)

# Async TMA load
tma.async_load(a_desc, [offs_am, offs_k], barrier, result)

# Wait for completion before using data
mbarrier.wait(barrier)
```