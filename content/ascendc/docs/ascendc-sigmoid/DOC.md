---
name: ascendc-sigmoid
description: Sigmoid activation function
metadata:
  languages: ascendc
  versions: '8.0'
  revision: 1
  updated-on: '2026-06-13'
  source: official
  tags: ascend,npu,ascendc,vector,activation
---

# Sigmoid

Sigmoid activation function.

## Syntax

```cpp
template <typename T>
void Sigmoid(LocalTensor<T>& dst, LocalTensor<T>& src, int32_t count)
```

## Description

Applies the sigmoid activation function to each element in the source tensor. Sigmoid squashes values to the range (0, 1) using the formula: `1 / (1 + exp(-x))`. This operation is performed on the Vector unit and is commonly used in neural networks for binary classification or gating mechanisms.

## Hardware Unit

Vector Unit

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| dst | LocalTensor<T>& | Destination tensor storing the sigmoid result |
| src | LocalTensor<T>& | Source tensor |
| count | int32_t | Number of elements to compute |

## Supported Data Types

- float16 (half)
- float32 (float)

## Semantics

```pseudo
for i in 0..count-1:
    dst[i] = 1 / (1 + exp(-src[i]))
```

## CANN Version

CANN 8.0+

## Target Architecture

Ascend NPU (Atlas series)

## Related Instructions

- [Relu](../ascendc-relu/DOC.md)
- [GELU](../ascendc-gelu/DOC.md)
- [Softmax](../ascendc-softmax/DOC.md)

## Example

```cpp
using namespace ascendc;

// Allocate tensors in UB (Unified Buffer)
LocalTensor<float> src = src_buffer;
LocalTensor<float> dst = dst_buffer;
int32_t count = 1024;

// Sigmoid activation
Sigmoid(dst, src, count);

// dst[i] = 1 / (1 + exp(-src[i])) for all i in [0, count)
```