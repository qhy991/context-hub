---
name: ascendc-sqrt
description: Element-wise square root function
metadata:
  languages: ascendc
  versions: '8.0'
  revision: 1
  updated-on: '2026-06-13'
  source: official
  tags: ascend,npu,ascendc,vector,math
---

# Sqrt

Element-wise square root function.

## Syntax

```cpp
template <typename T>
void Sqrt(LocalTensor<T>& dst, LocalTensor<T>& src, int32_t count)
```

## Description

Computes the square root for each element in the source tensor. Each element in `dst` is computed as `sqrt(src[i])`. This operation is performed on the Vector unit using hardware-accelerated mathematical functions.

## Hardware Unit

Vector Unit

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| dst | LocalTensor<T>& | Destination tensor storing the square root result |
| src | LocalTensor<T>& | Source tensor |
| count | int32_t | Number of elements to compute |

## Supported Data Types

- float16 (half)
- float32 (float)

## Semantics

```pseudo
for i in 0..count-1:
    dst[i] = sqrt(src[i])
```

## CANN Version

CANN 8.0+

## Target Architecture

Ascend NPU (Atlas series)

## Related Instructions

- [Exp](../ascendc-exp/DOC.md)
- [Div](../ascendc-div/DOC.md)

## Example

```cpp
using namespace ascendc;

// Allocate tensors in UB (Unified Buffer)
LocalTensor<float> src = src_buffer;
LocalTensor<float> dst = dst_buffer;
int32_t count = 1024;

// Element-wise square root
Sqrt(dst, src, count);

// dst[i] = sqrt(src[i]) for all i in [0, count)
```