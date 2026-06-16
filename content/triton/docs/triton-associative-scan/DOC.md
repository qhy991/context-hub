---
name: triton-associative-scan
description: Generic associative scan with carry propagation
metadata:
  languages: triton
  versions: '2.1'
  revision: 1
  updated-on: '2026-06-16'
  source: official
  tags: triton,gpu,scan,associative,generic
---

# tl.associative-scan

Applies an associative `combine_fn` along `axis`, propagating a carry from one element to the next. Unlike `tl.cumsum` which uses addition, this supports any associative binary operation. Used in state-space models (SSMs), RNN inference, and prefix computation.

## Syntax

```python
tl.associative_scan(input, axis, combine_fn, reverse=False)
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| input | Block | Input tensor to scan |
| axis | int | Axis along which to scan |
| combine_fn | callable | Associative binary function (e.g., `lambda a, b: a * b`) |
| reverse | bool | Scan in reverse direction (default False) |

## Returns

| Type | Description |
|------|-------------|
| Block | Result of the associative scan |

## Triton Version

Triton 2.1+

## Target Architecture

NVIDIA GPU (SM 7.0+), AMD GPU (CDNA2+), Intel GPU

## Related Instructions

- [tl.cumsum](../triton-cumsum/DOC.md)
- [tl.cumprod](../triton-cumprod/DOC.md)

## Example

```python
import triton.language as tl

# SSM state propagation
state = tl.associative_scan(x, axis=1, combine_fn=lambda a, b: a * b + x)
```
