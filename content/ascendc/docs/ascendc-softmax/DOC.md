---
name: ascendc-softmax
description: Softmax activation along last dimension
metadata:
  languages: ascendc
  versions: '8.0'
  revision: 1
  updated-on: '2026-06-13'
  source: official
  tags: ascend,npu,ascendc,vector,softmax,activation
---

# Softmax

Softmax activation function along the last dimension.

## Syntax

```cpp
template <typename T>
void SoftMax(LocalTensor<T>& dst, LocalTensor<T>& src, int32_t count)
```

## Description

Applies the softmax activation function along the last dimension of the input tensor. Softmax normalizes values to sum to 1, producing a probability distribution. The operation is performed in multiple passes: find maximum → compute exponentials → sum exponentials → divide by sum. This is executed on the Vector unit.

## Hardware Unit

Vector Unit

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| dst | LocalTensor<T>& | Destination tensor storing softmax result |
| src | LocalTensor<T>& | Source tensor |
| count | int32_t | Number of elements to compute |

## Supported Data Types

- float16 (half)
- float32 (float)

## Semantics

```pseudo
// Multi-pass implementation
max_val = ReduceMax(src)
exp_tensor = Exp(src - max_val)
sum_exp = ReduceSum(exp_tensor)
dst = exp_tensor / sum_exp
```

## CANN Version

CANN 8.0+

## Target Architecture

Ascend NPU (Atlas series)

## Related Instructions

- [Exp](../ascendc-exp/DOC.md)
- [ReduceSum](../ascendc-reducesum/DOC.md)
- [ReduceMax](../ascendc-reducemax/DOC.md)
- [Sigmoid](../ascendc-sigmoid/DOC.md)

## Example

```cpp
using namespace ascendc;

// Allocate tensors in UB (Unified Buffer)
LocalTensor<float> src = src_buffer;
LocalTensor<float> dst = dst_buffer;
int32_t count = 1024;

// Softmax activation
SoftMax(dst, src, count);

// Result: probability distribution summing to 1.0
```