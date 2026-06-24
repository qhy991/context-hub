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

## Example
```cpp
#include "kernel_operator.h"
using namespace AscendC;

extern "C" __global__ __aicore__ void kernel_cos(GM_ADDR x, GM_ADDR y, uint32_t totalLength) {
    TPipe pipe;
    TQue<QuePosition::VECIN, 1> inQueueX;
    TQue<QuePosition::VECOUT, 1> outQueueY;
    pipe.InitBuffer(inQueueX, 1, totalLength * sizeof(half));
    pipe.InitBuffer(outQueueY, 1, totalLength * sizeof(half));

    GlobalTensor<half> xGm;
    GlobalTensor<half> yGm;
    xGm.SetGlobalBuffer((__gm__ half*)x, totalLength);
    yGm.SetGlobalBuffer((__gm__ half*)y, totalLength);

    LocalTensor<half> xLocal = inQueueX.AllocTensor<half>();
    LocalTensor<half> yLocal = outQueueY.AllocTensor<half>();
    
    DataCopy(xLocal, xGm, totalLength);
    Cos(yLocal, xLocal, totalLength);
    DataCopy(yGm, yLocal, totalLength);

    inQueueX.FreeTensor(xLocal);
    outQueueY.FreeTensor(yLocal);
}
```
