---
name: ascendc-add
description: Element-wise addition of two tensors
metadata:
  languages: ascendc
  versions: '8.0'
  revision: 1
  updated-on: '2026-06-13'
  source: official
  tags: ascend,npu,ascendc,vector,simd,elementwise
---

# Add

Element-wise addition of two tensors.

## Syntax

```cpp
template <typename T>
void Add(LocalTensor<T>& dst, LocalTensor<T>& src0, LocalTensor<T>& src1, int32_t count)
```

## Description

Performs element-wise addition of two source tensors and stores the result in the destination tensor. Each element in `dst` is computed as `src0[i] + src1[i]`. This operation is performed on the Vector unit, allowing for high-throughput parallel computation.

## Hardware Unit

Vector Unit

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| dst | LocalTensor<T>& | Destination tensor storing the addition result |
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
    dst[i] = src0[i] + src1[i]
```

## CANN Version

CANN 8.0+

## Target Architecture

Ascend NPU (Atlas series)

## Related Instructions

- [Sub](../ascendc-sub/DOC.md)
- [Mul](../ascendc-mul/DOC.md)
- [Div](../ascendc-div/DOC.md)

## Example

```cpp
using namespace ascendc;

// Allocate tensors in UB (Unified Buffer)
LocalTensor<float> src0 = src0_buffer;
LocalTensor<float> src1 = src1_buffer;
LocalTensor<float> dst = dst_buffer;
int32_t count = 1024;

// Element-wise addition
Add(dst, src0, src1, count);

// dst[i] = src0[i] + src1[i] for all i in [0, count)
```