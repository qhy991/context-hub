---
name: ascendc-exp
description: Element-wise exponential function
metadata:
  languages: ascendc
  versions: '8.0'
  revision: 1
  updated-on: '2026-06-13'
  source: official
  tags: ascend,npu,ascendc,vector,math,activation
---

# Exp

Element-wise exponential function.

## Syntax

```cpp
template <typename T>
void Exp(LocalTensor<T>& dst, LocalTensor<T>& src, int32_t count)
```

## Description

Computes the exponential function (e^x) for each element in the source tensor. Each element in `dst` is computed as `exp(src[i])`. This operation is performed on the Vector unit using optimized hardware acceleration for mathematical functions.

## Hardware Unit

Vector Unit

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| dst | LocalTensor<T>& | Destination tensor storing the exponential result |
| src | LocalTensor<T>& | Source tensor |
| count | int32_t | Number of elements to compute |

## Supported Data Types

- float16 (half)
- float32 (float)

## Semantics

```pseudo
for i in 0..count-1:
    dst[i] = exp(src[i])
```

## CANN Version

CANN 8.0+

## Target Architecture

Ascend NPU (Atlas series)

## Related Instructions

- [Sqrt](../ascendc-sqrt/DOC.md)
- [Sigmoid](../ascendc-sigmoid/DOC.md)
- [Softmax](../ascendc-softmax/DOC.md)

## Example

```cpp
using namespace ascendc;

// Allocate tensors in UB (Unified Buffer)
LocalTensor<float> src = src_buffer;
LocalTensor<float> dst = dst_buffer;
int32_t count = 1024;

// Element-wise exponential
Exp(dst, src, count);

// dst[i] = exp(src[i]) for all i in [0, count)
```