---
name: ascendc-reducesum
description: Sum reduction along tensor elements
metadata:
  languages: ascendc
  versions: '8.0'
  revision: 1
  updated-on: '2026-06-13'
  source: official
  tags: ascend,npu,ascendc,vector,reduction
---

# ReduceSum

Sum reduction along tensor elements.

## Syntax

```cpp
template <typename T>
void ReduceSum(LocalTensor<T>& dst, LocalTensor<T>& src, int32_t count)
```

## Description

Performs a sum reduction over all elements in the source tensor, computing the total sum. The result is stored in the destination tensor as a scalar value. This operation is executed on the Vector unit using efficient reduction algorithms.

## Hardware Unit

Vector Unit

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| dst | LocalTensor<T>& | Destination tensor storing the scalar sum result |
| src | LocalTensor<T>& | Source tensor |
| count | int32_t | Number of elements to reduce |

## Supported Data Types

- float16 (half)
- float32 (float)
- int32_t

## Semantics

```pseudo
sum = 0
for i in 0..count-1:
    sum = sum + src[i]
dst[0] = sum
```

## CANN Version

CANN 8.0+

## Target Architecture

Ascend NPU (Atlas series)

## Related Instructions

- [ReduceMax](../ascendc-reducemax/DOC.md)
- [Add](../ascendc-add/DOC.md)

## Example

```cpp
using namespace ascendc;

// Allocate tensors in UB (Unified Buffer)
LocalTensor<float> src = src_buffer;
LocalTensor<float> dst = dst_buffer;  // Scalar result
int32_t count = 1024;

// Sum reduction
ReduceSum(dst, src, count);

// dst[0] = sum of all src[i] for i in [0, count)
```