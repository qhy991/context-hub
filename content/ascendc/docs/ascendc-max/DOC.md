---
name: ascendc-max
description: Element-wise maximum of two tensors
metadata:
  languages: ascendc
  versions: '8.0'
  revision: 1
  updated-on: '2026-06-13'
  source: official
  tags: ascend,npu,ascendc,vector,simd,elementwise
---

# Max

Element-wise maximum of two tensors.

## Syntax

```cpp
template <typename T>
void Max(LocalTensor<T>& dst, LocalTensor<T>& src0, LocalTensor<T>& src1, int32_t count)
```

## Description

Performs element-wise maximum comparison between two source tensors. Each element in `dst` is computed as `max(src0[i], src1[i])`. This operation is executed on the Vector unit for efficient parallel comparison operations.

## Hardware Unit

Vector Unit

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| dst | LocalTensor<T>& | Destination tensor storing the maximum result |
| src0 | LocalTensor<T>& | First source tensor |
| src1 | LocalTensor<T>& | Second source tensor |
| count | int32_t | Number of elements to compute |

## Supported Data Types

- float16 (half)
- float32 (float)
- int32_t
- int16_t
- int8_t

## Semantics

```pseudo
for i in 0..count-1:
    dst[i] = max(src0[i], src1[i])
```

## CANN Version

CANN 8.0+

## Target Architecture

Ascend NPU (Atlas series)

## Related Instructions

- [Min](../ascendc-min/DOC.md)
- [ReduceMax](../ascendc-reducemax/DOC.md)

## Example

```cpp
using namespace ascendc;

// Allocate tensors in UB (Unified Buffer)
LocalTensor<float> src0 = src0_buffer;
LocalTensor<float> src1 = src1_buffer;
LocalTensor<float> dst = dst_buffer;
int32_t count = 1024;

// Element-wise maximum
Max(dst, src0, src1, count);

// dst[i] = max(src0[i], src1[i]) for all i in [0, count)
```