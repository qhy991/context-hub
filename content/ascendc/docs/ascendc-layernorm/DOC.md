---
name: ascendc-layernorm
description: Layer normalization operation
metadata:
  languages: ascendc
  versions: '8.0'
  revision: 1
  updated-on: '2026-06-13'
  source: official
  tags: ascend,npu,ascendc,vector,normalization
---

# LayerNorm

Layer normalization operation.

## Syntax

```cpp
template <typename T>
void LayerNorm(LocalTensor<T>& dst, LocalTensor<T>& src, LocalTensor<T>& gamma, LocalTensor<T>& beta, int32_t count)
```

## Description

Applies layer normalization to the input tensor. LayerNorm normalizes the input to have zero mean and unit variance, then applies scale (gamma) and shift (beta) parameters. The operation involves multiple steps: compute mean → subtract mean → compute variance → normalize → scale and shift. This is executed on the Vector unit.

## Hardware Unit

Vector Unit

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| dst | LocalTensor<T>& | Destination tensor storing normalized result |
| src | LocalTensor<T>& | Source tensor |
| gamma | LocalTensor<T>& | Scale parameter |
| beta | LocalTensor<T>& | Shift parameter |
| count | int32_t | Number of elements to normalize |

## Supported Data Types

- float16 (half)
- float32 (float)

## Semantics

```pseudo
// Multi-step implementation
mean = ReduceSum(src) / count
centered = src - mean
variance = ReduceSum(centered * centered) / count
normalized = centered / sqrt(variance + epsilon)
dst = gamma * normalized + beta
```

## CANN Version

CANN 8.0+

## Target Architecture

Ascend NPU (Atlas series)

## Related Instructions

- [ReduceSum](../ascendc-reducesum/DOC.md)
- [Sqrt](../ascendc-sqrt/DOC.md)
- [Mul](../ascendc-mul/DOC.md)
- [Add](../ascendc-add/DOC.md)

## Example

```cpp
using namespace ascendc;

// Allocate tensors in UB (Unified Buffer)
LocalTensor<float> src = src_buffer;
LocalTensor<float> gamma = gamma_buffer;
LocalTensor<float> beta = beta_buffer;
LocalTensor<float> dst = dst_buffer;
int32_t count = 1024;

// Layer normalization
LayerNorm(dst, src, gamma, beta, count);

// Result: normalized and scaled output
```