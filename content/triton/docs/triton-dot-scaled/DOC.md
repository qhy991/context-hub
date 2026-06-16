---
name: triton-dot-scaled
description: Matrix product with micro-scaling format (MXFP) quantization
metadata:
  languages: triton
  versions: '3.0'
  revision: 1
  updated-on: '2026-06-16'
  source: official
  tags: triton,gpu,linear-algebra,dot,mxfp,quantization
---

# tl.dot_scaled

Returns the matrix product of two blocks in micro-scaling format.

## Syntax

```python
tl.dot_scaled(a, a_scale, b, b_scale, acc=None, out_dtype=tl.float32)
```

## Description

Computes the matrix product of two blocks where each operand is accompanied by a scaling factor. This supports MXFP (Microscaling Floating Point) formats like MXFP8 and MXFP6, where elements are shared-exponent quantized. The scaling factors are applied before the matrix multiply, enabling efficient low-precision inference.

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| a | Block | Left operand in scaled format (e.g., fp8_e4m3) |
| a_scale | Block | Per-block scaling factor for A |
| b | Block | Right operand in scaled format (e.g., fp8_e4m3) |
| b_scale | Block | Per-block scaling factor for B |
| acc | Block (optional) | Accumulator |
| out_dtype | tl.dtype | Output data type (default tl.float32) |

## Semantics

```pseudo
A_scaled = a * a_scale
B_scaled = b * b_scale
C = A_scaled × B_scaled
if acc is not None:
    C = C + acc
return C
```

## Triton Version

Triton 3.0+

## Target Architecture

NVIDIA GPU (SM 10.0+ / Blackwell with MXFP support)

## Related Instructions

- [tl.dot](../triton-dot/DOC.md)

## Example

```python
import triton.language as tl

# Block-scaled matmul with fp8
a = tl.load(a_ptrs)           # fp8_e4m3
a_scale = tl.load(a_scale_ptrs)  # fp8 block scale
b = tl.load(b_ptrs)           # fp8_e4m3
b_scale = tl.load(b_scale_ptrs)  # fp8 block scale

accumulator = tl.dot_scaled(a, a_scale, b, b_scale, accumulator)
```