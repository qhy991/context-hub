---
name: ascendc-cast
description: Type conversion of a tensor
metadata:
  languages: ascendc
  versions: '8.0'
  revision: 1
  updated-on: '2026-06-14'
  source: official
  tags: ascend,npu,ascendc,vector,simd,cast
---

# Cast

Casts a tensor from one data type to another element-wise.

## Syntax

```cpp
template <typename dstT, typename srcT>
void Cast(LocalTensor<dstT>& dst, LocalTensor<srcT>& src, RoundMode roundMode, int32_t count)
```

## Description

Performs an element-wise cast of data types from `srcT` to `dstT`. Commonly used for precision switching (e.g., float32 to float16, int32 to float32).

## Semantics

```cpp
for (int i = 0; i < count; i++) {
    dst[i] = static_cast<dstT>(src[i]); // Apply roundMode if needed
}
```

## Hardware Unit

Vector Unit

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| dst | LocalTensor<dstT>& | Destination tensor |
| src | LocalTensor<srcT>& | Source tensor |
| roundMode | RoundMode | Rounding mode (e.g., ROUND_HALF_EVEN, ROUND_HALF_UP) |
| count | int32_t | Number of elements to cast |

## Supported Data Types

- Conversions between float16, float32, int32_t, int16_t, int8_t, uint8_t

## Example
```cpp
#include "kernel_operator.h"
using namespace AscendC;

extern "C" __global__ __aicore__ void kernel_cast(GM_ADDR x, GM_ADDR y, uint32_t totalLength) {
    TPipe pipe;
    TQue<QuePosition::VECIN, 1> inQueueX;
    TQue<QuePosition::VECOUT, 1> outQueueY;
    pipe.InitBuffer(inQueueX, 1, totalLength * sizeof(half));
    pipe.InitBuffer(outQueueY, 1, totalLength * sizeof(float)); // Casting from half to float

    GlobalTensor<half> xGm;
    GlobalTensor<float> yGm;
    xGm.SetGlobalBuffer((__gm__ half*)x, totalLength);
    yGm.SetGlobalBuffer((__gm__ float*)y, totalLength);

    LocalTensor<half> xLocal = inQueueX.AllocTensor<half>();
    LocalTensor<float> yLocal = outQueueY.AllocTensor<float>();
    
    DataCopy(xLocal, xGm, totalLength);
    Cast(yLocal, xLocal, RoundMode::CAST_NONE, totalLength);
    DataCopy(yGm, yLocal, totalLength);

    inQueueX.FreeTensor(xLocal);
    outQueueY.FreeTensor(yLocal);
}
```
