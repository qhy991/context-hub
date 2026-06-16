---
name: triton-topk
description: Return the k largest or smallest elements along a dimension
metadata:
  languages: triton
  versions: '2.1'
  revision: 1
  updated-on: '2026-06-16'
  source: official
  tags: triton,gpu,sort,topk,selection
---

# tl.topk

Returns the `k` largest (when `descending=True`) or smallest (when `descending=False`) elements of the input tensor along the specified dimension. Commonly used in attention mechanisms (e.g., top-k sparse attention) and beam search.

## Syntax

```python
tl.topk(x, k, dim=None, descending=True)
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| x | Block | Input tensor |
| k | int (constexpr) | Number of elements to select |
| dim | int (optional) | Dimension to select along |
| descending | bool | Select largest (True) or smallest (False) (default True) |

## Returns

| Type | Description |
|------|-------------|
| Block | Tensor with k elements along the selected dimension |

## Triton Version

Triton 2.1+

## Target Architecture

NVIDIA GPU (SM 7.0+), AMD GPU (CDNA2+), Intel GPU

## Related Instructions

- [tl.sort](../triton-sort/DOC.md)

## Example

```python
import triton.language as tl

# Top-k sparse attention: keep only k largest scores
top_scores = tl.topk(scores, k=32, dim=-1, descending=True)
```
