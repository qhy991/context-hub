---
name: ascendc-gelu
description: GELU activation function approximation
metadata:
  languages: ascendc
  versions: '8.0'
  revision: 1
  updated-on: '2026-06-13'
  source: official
  tags: ascend,npu,ascendc,vector,activation
---

# GELU

GELU (Gaussian Error Linear Unit) activation function.

## Syntax

```cpp
template <typename T>
void Gelu(LocalTensor<T>& dst, LocalTensor<T>& src, int32_t count)
```

## Description

Applies the GELU activation function to each element in the source tensor. GELU is a smooth, non-monotonic activation function that outperforms ReLU in many transformer models. The implementation uses an efficient approximation: `x * Φ(x)` where Φ is the cumulative distribution function of the standard normal distribution. This operation is performed on the Vector unit.

## Hardware Unit

Vector Unit

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| dst | LocalTensor<T>& | Destination tensor storing GELU result |
| src | LocalTensor<T>& | Source tensor |
| count | int32_t | Number of elements to compute |

## Supported Data Types

- float16 (half)
- float32 (float)

## Semantics

```pseudo
// Approximation: GELU(x) ≈ 0.5 * x * (1 + tanh(√(2/π) * (x + 0.044715 * x³)))
for i in 0..count-1:
    x = src[i]
    cube = x * x * x
    tanh_input = sqrt(2.0 / PI) * (x + 0.044715 * cube)
    dst[i] = 0.5 * x * (1 + tanh(tanh_input))
```

## CANN Version

CANN 8.0+

## Target Architecture

Ascend NPU (Atlas series)

## Related Instructions

- [Relu](../ascendc-relu/DOC.md)
- [Sigmoid](../ascendc-sigmoid/DOC.md)
- [Mul](../ascendc-mul/DOC.md)

## Example

```cpp
using namespace ascendc;

// Allocate tensors in UB (Unified Buffer)
LocalTensor<float> src = src_buffer;
LocalTensor<float> dst = dst_buffer;
int32_t count = 1024;

// GELU activation
Gelu(dst, src, count);

// Smooth activation commonly used in transformers
```