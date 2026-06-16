---
name: triton-bitonic-merge
description: Bitonic merge step for bitonic sort networks
metadata:
  languages: triton
  versions: '2.1'
  revision: 1
  updated-on: '2026-06-16'
  source: official
  tags: triton,gpu,sort,bitonic,merge
---

# tl.bitonic-merge

Performs a bitonic merge operation — a key building block of bitonic sorting networks. The input must be a bitonic sequence (first increasing then decreasing, or vice versa). After merge, the sequence is sorted. This is more efficient than `tl.sort` for power-of-two sizes.

## Syntax

```python
tl.bitonic_merge(x, dim=None, descending=False)
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| x | Block | Bitonic sequence to merge |
| dim | int (optional) | Dimension to merge along |
| descending | bool | Sort in descending order (default False) |

## Returns

| Type | Description |
|------|-------------|
| Block | Sorted (merged) tensor |

## Triton Version

Triton 2.1+

## Target Architecture

NVIDIA GPU (SM 7.0+), AMD GPU (CDNA2+), Intel GPU

## Related Instructions

- [tl.sort](../triton-sort/DOC.md)

## Example

```python
import triton.language as tl

sorted = tl.bitonic_merge(bitonic_seq, dim=0)
```
