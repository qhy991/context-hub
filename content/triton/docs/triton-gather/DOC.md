---
name: triton-gather
description: Gather elements from a tensor along a dimension using index tensor
metadata:
  languages: triton
  versions: '2.1'
  revision: 1
  updated-on: '2026-06-16'
  source: official
  tags: triton,gpu,gather,indexing
---

# tl.gather

Gathers values along dimension `dim` from `input` at positions specified by `index`. This is like NumPy's `np.take` or PyTorch's `torch.gather`. Each element in `index` selects one element from `input` along the specified dimension.

## Syntax

```python
tl.gather(input, dim, index)
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| input | Block | Source tensor |
| dim | int | Dimension along which to index |
| index | Block (int) | Indices of values to gather |

## Returns

| Type | Description |
|------|-------------|
| Block | Gathered tensor with same rank as input |

## Triton Version

Triton 2.1+

## Target Architecture

NVIDIA GPU (SM 7.0+), AMD GPU (CDNA2+), Intel GPU

## Related Instructions

- [tl.load](../triton-load/DOC.md)
- [tl.histogram](../triton-histogram/DOC.md)

## Example

```python
import triton.language as tl

selected = tl.gather(embeddings, dim=0, index=token_ids)
```
