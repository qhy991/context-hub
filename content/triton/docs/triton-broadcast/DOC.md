---
name: triton-broadcast
description: Broadcast two tensors to a common compatible shape
metadata:
  languages: triton
  versions: '2.1'
  revision: 1
  updated-on: '2026-06-16'
  source: official
  tags: triton,gpu,shape,broadcast
---

# tl.broadcast

Tries to broadcast `input` and `other` to a common compatible shape following NumPy broadcasting rules. Returns the broadcasted pair. This is a convenience function for element-wise operations where shapes don't match.

## Syntax

```python
tl.broadcast(input, other)
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| input | Block | First input tensor |
| other | Block | Second input tensor |

## Returns

| Type | Description |
|------|-------------|
| Block | Tuple of two broadcasted tensors with compatible shapes |

## Triton Version

Triton 2.1+

## Target Architecture

NVIDIA GPU (SM 7.0+), AMD GPU (CDNA2+), Intel GPU

## Example

```python
import triton.language as tl

x_b, y_b = tl.broadcast(row, col)  # match shapes
```
