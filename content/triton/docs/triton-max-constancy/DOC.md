---
name: triton-max-constancy
description: Hint that elements form groups of constant values
metadata:
  languages: triton
  versions: '2.1'
  revision: 1
  updated-on: '2026-06-16'
  source: official
  tags: triton,gpu,compiler,hint,constant
---

# tl.max-constancy

Informs the compiler that consecutive elements form groups of `group_size` with the same value, enabling broadcast optimization.

## Syntax

```python
tl.max_constancy(value, group_size)
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| value | tensor | Value the hint applies to |
| group_size | int | Size of constant groups |

## Returns

| Type | Description |
|------|-------------|
| Block | None (compiler hint) |

## Triton Version

Triton 2.1+

## Target Architecture

NVIDIA GPU (SM 7.0+), AMD GPU (CDNA2+), Intel GPU

## Example

```python
import triton.language as tl

row_idx = offs_m[:, None]
tl.max_constancy(row_idx, BLOCK_N)  # constant across columns
```
