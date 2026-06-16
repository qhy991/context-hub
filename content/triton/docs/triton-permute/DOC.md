---
name: triton-permute
description: Permute the dimensions of a tensor
metadata:
  languages: triton
  versions: '2.1'
  revision: 1
  updated-on: '2026-06-16'
  source: official
  tags: triton,gpu,shape,permute,transpose
---

# tl.permute

Permutes the dimensions of `input` according to `dims`. Different from `tl.trans` in that `permute` requires explicit dimension ordering. Same effect as `tl.trans(input, dims[0], dims[1], ...)`.

## Syntax

```python
tl.permute(input, *dims)
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| input | Block | Input tensor |
| *dims | int... | New dimension ordering |

## Returns

| Type | Description |
|------|-------------|
| Block | Permuted tensor |

## Triton Version

Triton 2.1+

## Target Architecture

NVIDIA GPU (SM 7.0+), AMD GPU (CDNA2+), Intel GPU

## Related Instructions

- [tl.trans](../triton-trans/DOC.md)
- [tl.view](../triton-view/DOC.md)

## Example

```python
import triton.language as tl

x_perm = tl.permute(x, 2, 0, 1)  # 3D permute
```
