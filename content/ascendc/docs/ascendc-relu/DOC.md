---
name: ascendc-relu
description: ReLU activation function
metadata:
  languages: ascendc
  versions: '8.0'
  revision: 1
  updated-on: '2026-06-13'
  source: official
  tags: ascend,npu,ascendc,vector,activation
---

# Relu

ReLU (Rectified Linear Unit) activation function.

## Syntax

```cpp
template <typename T>
void Relu(LocalTensor<T>& dst, LocalTensor<T>& src, int32_t count)
```

## Description

Applies the ReLU activation function to each element in the source tensor. ReLU outputs the input if positive, otherwise outputs zero: `max(0, x)`. This operation is performed on the Vector unit and is commonly used in neural networks as an activation function.

## Hardware Unit

Vector Unit

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| dst | LocalTensor<T>& | Destination tensor storing the ReLU result |
| src | LocalTensor<T>& | Source tensor |
| count | int32_t | Number of elements to compute |

## Supported Data Types

- float16 (half)
- float32 (float)

## Semantics

```pseudo
for i in 0..count-1:
    dst[i] = max(0, src[i])
```

## CANN Version

CANN 8.0+

## Target Architecture

Ascend NPU (Atlas series)

## Related Instructions

- [Sigmoid](../ascendc-sigmoid/DOC.md)
- [GELU](../ascendc-gelu/DOC.md)
- [Max](../ascendc-max/DOC.md)

## Example

```cpp
using namespace ascendc;

// Allocate tensors in UB (Unified Buffer)
LocalTensor<float> src = src_buffer;
LocalTensor<float> dst = dst_buffer;
int32_t count = 1024;

// ReLU activation
Relu(dst, src, count);

// dst[i] = max(0, src[i]) for all i in [0, count)
```