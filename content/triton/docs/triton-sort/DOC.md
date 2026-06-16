---
name: triton-sort
description: Sort a tensor along a specified dimension
metadata:
  languages: triton
  versions: '2.1'
  revision: 1
  updated-on: '2026-06-16'
  source: official
  tags: triton,gpu,sort,ordering
---

# tl.sort

Sorts the elements of `x` along dimension `dim`. When `descending=True`, sorts from largest to smallest. When `dim` is None, sorts the flattened tensor.

## Syntax

```python
tl.sort(x, dim=None, descending=False)
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| x | Block | Input tensor |
| dim | int (optional) | Dimension to sort along |
| descending | bool | Sort in descending order (default False) |

## Returns

| Type | Description |
|------|-------------|
| Block | Sorted tensor |

## Triton Version

Triton 2.1+

## Target Architecture

NVIDIA GPU (SM 7.0+), AMD GPU (CDNA2+), Intel GPU

## Related Instructions

- [tl.topk](../triton-topk/DOC.md)

## Example

```python
import triton.language as tl

sorted_x = tl.sort(x, dim=0)  # sort each column
```
