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

## Example
```cpp
#include "kernel_operator.h"
using namespace AscendC;

class KernelLayerNorm {
public:
    __aicore__ inline KernelLayerNorm() {}
    __aicore__ inline void Init(GM_ADDR x, GM_ADDR y, uint32_t totalLength) {
        this->totalLength = totalLength;
        xGm.SetGlobalBuffer((__gm__ half*)x, totalLength);
        yGm.SetGlobalBuffer((__gm__ half*)y, totalLength);
        pipe.InitBuffer(inQueueX, 1, totalLength * sizeof(half));
        pipe.InitBuffer(outQueueY, 1, totalLength * sizeof(half));
    }
    __aicore__ inline void Process() {
        LocalTensor<half> xLocal = inQueueX.AllocTensor<half>();
        LocalTensor<half> yLocal = outQueueY.AllocTensor<half>();
        DataCopy(xLocal, xGm, totalLength);
        
        // Simplified LayerNorm behavior
        LayerNorm(yLocal, xLocal, totalLength);
        
        DataCopy(yGm, yLocal, totalLength);
        inQueueX.FreeTensor(xLocal);
        outQueueY.FreeTensor(yLocal);
    }
private:
    TPipe pipe;
    TQue<QuePosition::VECIN, 1> inQueueX;
    TQue<QuePosition::VECOUT, 1> outQueueY;
    GlobalTensor<half> xGm;
    GlobalTensor<half> yGm;
    uint32_t totalLength;
};
```
