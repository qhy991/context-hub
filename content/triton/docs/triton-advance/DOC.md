---
name: triton-advance
description: Advance a block pointer by specified offsets
metadata:
  languages: triton
  versions: '2.1'
  revision: 1
  updated-on: '2026-06-16'
  source: official
  tags: triton,gpu,memory,advance,block-ptr
---

# tl.advance

Advances a block pointer (created by `tl.make_block_ptr`) by `offsets` in each dimension. Returns a new block pointer pointing to the next tile. Used in tiled loops to slide the window forward without recomputing addresses.

## Syntax

```python
tl.advance(base, offsets)
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| base | block_ptr | Block pointer to advance |
| offsets | tuple | Per-dimension step offsets |

## Returns

| Type | Description |
|------|-------------|
| Block | New block pointer at the advanced position |

## Triton Version

Triton 2.1+

## Target Architecture

NVIDIA GPU (SM 7.0+), AMD GPU (CDNA2+), Intel GPU

## Example

```python
import triton.language as tl

blk = tl.advance(blk, (0, BLOCK_K))  # move to next K tile
```
