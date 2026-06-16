---
name: triton-map-elementwise
description: "Apply a function element-wise across input tensors"
metadata:
  languages: triton
  versions: '2.1'
  revision: 1
  updated-on: '2026-06-16'
  source: official
  tags: triton,gpu,functional,map,element-wise
---

# tl.map_elementwise

Apply a function element-wise across one or more input tensors.

## Syntax

```python
tl.map_elementwise(fn, *args)
```

## Description

Applies `fn` element-wise to the input tensors in `*args`. Each element in the output is the result of applying `fn` to the corresponding elements of the inputs. This is a functional programming primitive that enables custom element-wise operations beyond the built-in math ops. The function `fn` must be a pure, side-effect-free callable operating on scalar values.

`map_elementwise` compiles to a single kernel instruction per element, without launching a separate function call. This is more efficient than calling a separate `@triton.jit` function for per-element operations.

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| fn | callable | Element-wise function taking N scalar inputs and returning 1 output |
| *args | tensor... | One or more input tensors of matching shapes |

## Returns

| Type | Description |
|------|-------------|
| Block | Tensor where each element = fn(args[0][i], args[1][i], ...) |

## Semantics

```pseudo
for each element i:
    output[i] = fn(input0[i], input1[i], ...)
```

## Triton Version

Triton 2.1+

## Target Architecture

NVIDIA GPU (SM 7.0+), AMD GPU (CDNA2+), Intel GPU

## Related Instructions

- [tl.inline_asm_elementwise](../triton-inline-asm-elementwise/DOC.md)

## Example

```python
import triton.language as tl

# Custom activation: leaky ReLU
def leaky_relu(x):
    return tl.maximum(x, 0.01 * x)
# Equivalent to: x if x > 0 else 0.01 * x

x = tl.load(x_ptr + offsets, mask=mask)
out = tl.map_elementwise(leaky_relu, x)
tl.store(out_ptr + offsets, out, mask=mask)

# Or with multiple inputs: custom binary op
def safe_div(a, b):
    return a / tl.maximum(b, 1e-8)

result = tl.map_elementwise(safe_div, numerator, denominator)
```