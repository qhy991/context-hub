---
name: triton-xor-sum
description: Compute XOR sum (parity) along an axis
metadata:
  languages: triton
  versions: '2.1'
  revision: 1
  updated-on: '2026-06-16'
  source: official
  tags: triton,gpu,reduction,xor,parity
---

# tl.xor-sum

Computes the XOR (exclusive OR) of all elements along the specified axis. This computes parity — the result is 1 if an odd number of bits are set. Only for integer types.

## Syntax

```python
tl.xor_sum(input, axis=None, keep_dims=False)
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| input | Block | Integer tensor to reduce |
| axis | int (optional) | Axis along which to reduce |
| keep_dims | bool | Retain reduced axis (default False) |

## Returns

| Type | Description |
|------|-------------|
| Block | XOR of elements along axis |

## Triton Version

Triton 2.1+

## Target Architecture

NVIDIA GPU (SM 7.0+), AMD GPU (CDNA2+), Intel GPU

## Related Instructions

- [tl.sum](../triton-sum/DOC.md)
- [tl.reduce_or](../triton-reduce-or/DOC.md)

## Example

```python
import triton.language as tl

parity = tl.xor_sum(bits, axis=0)  # XOR reduction
```
