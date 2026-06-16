---
name: triton-cat
description: Concatenate two tensors along a dimension
metadata:
  languages: triton
  versions: '2.1'
  revision: 1
  updated-on: '2026-06-16'
  source: official
  tags: triton,gpu,shape,cat,concatenate
---

# tl.cat

Concatenates `input` and `other` along dimension `dim`. Both tensors must have the same shape except in the concatenation dimension. `can_reorder` allows the compiler to reorder elements for optimization.

## Syntax

```python
tl.cat(input, other, can_reorder=False, dim=0)
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| input | Block | First input tensor |
| other | Block | Second input tensor |
| can_reorder | bool | Allow compiler to reorder elements (default False) |
| dim | int | Dimension to concatenate along (default 0) |

## Returns

| Type | Description |
|------|-------------|
| Block | Concatenated tensor |

## Triton Version

Triton 2.1+

## Target Architecture

NVIDIA GPU (SM 7.0+), AMD GPU (CDNA2+), Intel GPU

## Related Instructions

- [tl.join](../triton-join/DOC.md)
- [tl.split](../triton-split/DOC.md)

## Example

```python
import triton.language as tl

combined = tl.cat(x, y, dim=0)  # concat along first axis
```
