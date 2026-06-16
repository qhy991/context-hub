---
name: triton-store-tensor-desc
description: Store a block of data to a tensor descriptor via TMA
metadata:
  languages: triton
  versions: '3.0'
  revision: 1
  updated-on: '2026-06-16'
  source: official
  tags: triton,gpu,tma,descriptor,store,hopper
---

# tl.store_tensor_descriptor

Store a block of data to a tensor descriptor.

## Syntax

```python
tl.store_tensor_descriptor(desc, offsets, value)
```

## Description

Stores `value` to the tensor descriptor `desc` at the given element offsets. This is a convenience wrapper around the descriptor's `.store(offsets, value)` method. On Hopper+ GPUs, this uses TMA for asynchronous data movement from shared to global memory.

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| desc | tensor_descriptor | Descriptor created by `tl.make_tensor_descriptor` |
| offsets | list | Starting element offsets for each dimension |
| value | Block | Data to store |

## Triton Version

Triton 3.0+

## Target Architecture

NVIDIA GPU (SM 9.0+ Hopper / SM 10.0+ Blackwell)

## Related Instructions

- [tl.make_tensor_descriptor](../triton-make-tensor-descriptor/DOC.md)
- [tl.load_tensor_descriptor](../triton-load-tensor-desc/DOC.md)

## Example

```python
import triton.language as tl

tl.store_tensor_descriptor(c_desc, [offs_cm, offs_cn], accumulator)
# Equivalent to:
# c_desc.store([offs_cm, offs_cn], accumulator)
```