---
name: ascendc-cos
description: Cosine function of a tensor
metadata:
  languages: ascendc
  versions: '8.0'
  revision: 1
  updated-on: '2026-06-14'
  source: official
  tags: ascend,npu,ascendc,vector,simd,math
---

# Cos

Computes the cosine of a tensor element-wise.

## Syntax

```cpp
template <typename T>
void Cos(LocalTensor<T>& dst, LocalTensor<T>& src, int32_t count)
```

## Description

Performs element-wise cosine computation on the source tensor and stores the result in the destination tensor. The input values should typically be in radians.

## Hardware Unit

Vector Unit

## Supported Data Types

- float16 (half)
- float32 (float)
