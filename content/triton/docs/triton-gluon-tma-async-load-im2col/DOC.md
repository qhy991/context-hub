---
name: triton-gluon-tma-async-load-im2col
description: TMA async load with im2col transformation for convolution (Gluon experimental)
metadata:
  languages: triton
  versions: '3.0'
  revision: 1
  updated-on: '2026-06-16'
  source: official
  tags: triton,gpu,gluon,experimental,tma,im2col,convolution,hopper
---

# tl.gluon.nvidia.hopper.tma.async_load_im2col

Asynchronously load data from global memory to shared memory using TMA with im2col transformation.

## Syntax

```python
from triton.experimental.gluon.language.nvidia.hopper import tma

tma.async_load_im2col(tensor_desc, coord, offsets, barrier, result, pred=True, multicast=False)
```

## Description

Like `async_load`, but with an im2col (image-to-column) transformation applied during the TMA copy. This is optimized for convolution operations where input feature maps need to be rearranged into matrix columns for efficient matrix multiplication. The `tensor_desc` must be created with `tensor_descriptor_im2col` type.

## Hardware Unit

Tensor Memory Accelerator (TMA) with im2col mode

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| tensor_desc | tensor_descriptor_im2col | Im2col descriptor for the source tensor |
| coord | list[tensor] | Starting coordinates |
| offsets | list[tensor] | Im2col offset parameters |
| barrier | mbarrier | Mbarrier for synchronization |
| result | shared_mem | Destination shared memory buffer |
| pred | bool | Predication flag (default True) |
| multicast | bool | Enable cluster multicast (default False) |

## Triton Version

Triton 3.0+ (experimental)

## Target Architecture

NVIDIA GPU (SM 9.0+ Hopper / SM 10.0+ Blackwell)

## Related Instructions

- [async_load](../triton-gluon-tma-async-load/DOC.md)
- [make_tensor_descriptor](../triton-gluon-tma-make-tensor-desc/DOC.md)

## Example

```python
from triton.experimental.gluon.language.nvidia.hopper import tma, mbarrier

# Create im2col descriptor for convolution
desc = tma.make_tensor_descriptor(
    input_ptr, shape=[H, W, C], strides=[W*C, C, 1],
    block_shape=[BLOCK_H, BLOCK_W, BLOCK_C],
    layout=shared_layout
)

barrier = mbarrier.allocate_mbarrier()
tile = tl.allocate_shared_memory((BLOCK_H, BLOCK_W, BLOCK_C), dtype=tl.float16)

# TMA im2col load
tma.async_load_im2col(desc, [h, w, c], im2col_offsets, barrier, tile)
mbarrier.wait(barrier)
```