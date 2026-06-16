---
name: triton-slice
description: Extract a slice from a tensor
metadata:
  languages: triton
  versions: '2.1'
  revision: 1
  updated-on: '2026-06-16'
  source: official
  tags: triton,gpu,slice,indexing
---

# tl.slice

Extracts a contiguous slice from `input` along `axis`, from `start` (inclusive) to `end` (exclusive). Returns a tensor of shape `input.shape` with the sliced axis reduced to `end - start` elements.

## Syntax

```python
tl.slice(input, start, end, axis=0)
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| input | Block | Input tensor |
| start | int | Start index (inclusive) |
| end | int | End index (exclusive) |
| axis | int | Axis to slice along (default 0) |

## Returns

| Type | Description |
|------|-------------|
| Block | Sliced tensor |

## Triton Version

Triton 2.1+

## Target Architecture

NVIDIA GPU (SM 7.0+), AMD GPU (CDNA2+), Intel GPU

## Related Instructions

- [tl.view](../triton-view/DOC.md)
- [tl.reshape](../triton-reshape/DOC.md)

## Example

```python
import triton.language as tl

subset = tl.slice(x, start=0, end=4, axis=0)  # first 4 rows
```
