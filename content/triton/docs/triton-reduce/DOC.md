---
name: triton-reduce
description: Generic reduction with a custom combine function
metadata:
  languages: triton
  versions: '2.1'
  revision: 1
  updated-on: '2026-06-16'
  source: official
  tags: triton,gpu,reduction,combine,generic
---

# tl.reduce

Applies a combine function to all elements in the input tensor along the provided axis.

## Syntax

```python
tl.reduce(input, axis, combine_fn, keep_dims=False)
```

## Description

A generic reduction operation that applies a user-provided `combine_fn` to elements along the specified axis. The `combine_fn` must be associative and commutative (e.g., `tl.add`, `tl.maximum`, `tl.minimum`). Triton compiles this into efficient warp-level reduction primitives.

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| input | Block | Input tensor to reduce |
| axis | int | Axis along which to reduce |
| combine_fn | callable | Associative/commutative binary function |
| keep_dims | bool | Whether to retain the reduced axis (default False) |

## Returns

| Type | Description |
|------|-------------|
| Block | Reduced tensor |

## Semantics

```pseudo
result = input[..., 0, ...]
for each element along axis:
    result = combine_fn(result, input[..., idx, ...])
return result
```

## Triton Version

Triton 2.1+

## Target Architecture

NVIDIA GPU (SM 7.0+), AMD GPU (CDNA2+), Intel GPU

## Related Instructions

- [tl.sum](../triton-sum/DOC.md)
- [tl.max](../triton-max/DOC.md)

## Example

```python
import triton.language as tl

# Custom reduction: product along axis
x = tl.load(x_ptr + offsets)
product = tl.reduce(x, axis=0, combine_fn=lambda a, b: a * b)

# Built-in reductions are equivalent to:
# tl.sum(x, axis)    == tl.reduce(x, axis, tl.add)
# tl.max(x, axis)    == tl.reduce(x, axis, tl.maximum)
```