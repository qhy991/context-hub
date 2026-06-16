---
name: triton-cast
description: Cast a tensor to a different data type
metadata:
  languages: triton
  versions: '2.1'
  revision: 1
  updated-on: '2026-06-16'
  source: official
  tags: triton,gpu,type,cast,convert
---

# tl.cast

Casts a tensor to the given `dtype`. `fp_downcast_rounding` controls rounding mode for floating-point downcasts: `"rtne"` (round to nearest even) or `"rtz"` (round toward zero). When `bitcast=True`, reinterprets the bits without numeric conversion.

## Syntax

```python
tl.cast(input, dtype, fp_downcast_rounding=None, bitcast=False)
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| input | Block | Input tensor |
| dtype | tl.dtype | Target data type |
| fp_downcast_rounding | str (optional) | Rounding mode for fp downcast: `"rtne"`, `"rtz"` |
| bitcast | bool | If True, reinterpret bits instead of converting (default False) |

## Returns

| Type | Description |
|------|-------------|
| Block | Tensor cast to `dtype` |

## Triton Version

Triton 2.1+

## Target Architecture

NVIDIA GPU (SM 7.0+), AMD GPU (CDNA2+), Intel GPU

## Related Instructions

- [tl.load](../triton-load/DOC.md)

## Example

```python
import triton.language as tl

x_fp16 = tl.cast(x, tl.float16)  # cast to float16
x_int = tl.cast(x, tl.int32)  # cast to int32
```
