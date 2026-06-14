---
name: ascendc-ln
description: Natural logarithm of a tensor
metadata:
  languages: ascendc
  versions: '8.0'
  revision: 1
  updated-on: '2026-06-14'
  source: official
  tags: ascend,npu,ascendc,vector,simd,math
---

# Ln

Computes the natural logarithm of a tensor element-wise.

## Syntax

```cpp
template <typename T>
void Ln(LocalTensor<T>& dst, LocalTensor<T>& src, int32_t count)
```

## Description

Performs element-wise natural logarithm (`ln(x)`) computation on the source tensor and stores the result in the destination tensor. This operation is performed on the Vector unit.

## Hardware Unit

Vector Unit

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| dst | LocalTensor<T>& | Destination tensor storing the log result |
| src | LocalTensor<T>& | Source tensor |
| count | int32_t | Number of elements to compute |

## Supported Data Types

- float16 (half)
- float32 (float)

## Target Architecture

Ascend NPU (Atlas series)
