---
name: triton-load-tensor-desc
description: Load a block of data from a tensor descriptor via TMA
metadata:
  languages: triton
  versions: '3.0'
  revision: 1
  updated-on: '2026-06-16'
  source: official
  tags: triton,gpu,tma,descriptor,load,hopper
---

# tl.load_tensor_descriptor

Load a block of data from a tensor descriptor.

## Syntax

```python
tl.load_tensor_descriptor(desc, offsets)
```

## Description

Loads a block of data from the tensor descriptor `desc` starting at the given element offsets. This is a convenience wrapper around the descriptor's `.load(offsets)` method. On Hopper+ GPUs, this uses TMA (Tensor Memory Accelerator) for asynchronous high-bandwidth data movement from global to shared memory.

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| desc | tensor_descriptor | Descriptor created by `tl.make_tensor_descriptor` |
| offsets | list | Starting element offsets for each dimension |

## Returns

| Type | Description |
|------|-------------|
| Block | Loaded tile of data |

## Triton Version

Triton 3.0+

## Target Architecture

NVIDIA GPU (SM 9.0+ Hopper / SM 10.0+ Blackwell)

## Related Instructions

- [tl.make_tensor_descriptor](../triton-make-tensor-descriptor/DOC.md)
- [tl.store_tensor_descriptor](../triton-store-tensor-desc/DOC.md)

## Example

```python
import triton.language as tl

a_block = tl.load_tensor_descriptor(a_desc, [offs_am, offs_k])
# Equivalent to:
# a_block = a_desc.load([offs_am, offs_k])
```