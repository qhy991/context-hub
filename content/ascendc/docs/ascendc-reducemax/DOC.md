---
name: ascendc-reducemax
description: Maximum reduction along tensor elements
metadata:
  languages: ascendc
  versions: '8.0'
  revision: 1
  updated-on: '2026-06-13'
  source: official
  tags: ascend,npu,ascendc,vector,reduction
---

# ReduceMax

Maximum reduction along tensor elements.

## Syntax

```cpp
template <typename T>
void ReduceMax(LocalTensor<T>& dst, LocalTensor<T>& src, int32_t count)
```

## Description

Performs a maximum reduction over all elements in the source tensor, finding the largest value. The result is stored in the destination tensor as a scalar value. This operation is executed on the Vector unit using efficient reduction algorithms.

## Hardware Unit

Vector Unit

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| dst | LocalTensor<T>& | Destination tensor storing the scalar maximum result |
| src | LocalTensor<T>& | Source tensor |
| count | int32_t | Number of elements to reduce |

## Supported Data Types

- float16 (half)
- float32 (float)
- int32_t
- int16_t
- int8_t

## Semantics

```pseudo
max_val = -infinity
for i in 0..count-1:
    max_val = max(max_val, src[i])
dst[0] = max_val
```

## CANN Version

CANN 8.0+

## Target Architecture

Ascend NPU (Atlas series)

## Related Instructions

- [ReduceSum](../ascendc-reducesum/DOC.md)
- [Max](../ascendc-max/DOC.md)

## Example

```cpp
using namespace ascendc;

// Allocate tensors in UB (Unified Buffer)
LocalTensor<float> src = src_buffer;
LocalTensor<float> dst = dst_buffer;  // Scalar result
int32_t count = 1024;

// Maximum reduction
ReduceMax(dst, src, count);

// dst[0] = max of all src[i] for i in [0, count)
```