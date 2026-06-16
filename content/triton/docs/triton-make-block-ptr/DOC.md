---
name: triton-make-block-ptr
description: "Deprecated — create a block pointer, use tl.make_tensor_descriptor instead"
metadata:
  languages: triton
  versions: '2.1'
  revision: 1
  updated-on: '2026-06-16'
  source: official
  tags: triton,gpu,memory,block-ptr,deprecated
---

# tl.make-block-ptr

Deprecated in favor of `tl.make_tensor_descriptor`. Returns a pointer to a sub-block of a parent tensor, supporting 2D/3D tiles with efficient hardware boundary checks on Hopper+.

## Syntax

```python
tl.make_block_ptr(base, shape, strides, offsets, block_shape, order)
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| base | tensor | Base pointer |
| shape | tuple | Parent tensor shape |
| strides | tuple | Strides of parent tensor |
| offsets | tuple | Starting offsets |
| block_shape | tuple | Shape of the block |
| order | tuple | Data layout order |

## Returns

| Type | Description |
|------|-------------|
| Block | Block pointer for use with `.load()` / `.store()` / `.advance()` |

## Triton Version

Triton 2.1+

## Target Architecture

NVIDIA GPU (SM 7.0+), AMD GPU (CDNA2+), Intel GPU

## Example

```python
import triton.language as tl

blk = tl.make_block_ptr(a_ptr, (M,K), (K,1), (0,0), (BLOCK_M,BLOCK_K), (1,0))
a = tl.load(blk)
blk = tl.advance(blk, (0, BLOCK_K))
```
