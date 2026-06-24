---
name: ascendc-alloctensor
description: Allocate a tensor from a queue's memory pool
metadata:
  languages: ascendc
  versions: '8.0'
  revision: 1
  updated-on: '2026-06-14'
  source: official
  tags: ascend,npu,ascendc,queue,memory,pipeline
---

# AllocTensor

Allocates an empty LocalTensor from a `TQue`.

## Syntax

```cpp
template <TPosition pos, typename T>
LocalTensor<T> TQue<pos, 1>::AllocTensor()
```

## Description

Obtains a memory block from the queue's internal buffer allocation pool to be written to. Must be paired with `EnQue` after writing or `FreeTensor` to release.

## Example

```cpp
TQue<QuePosition::VECIN, 1> inQueue;
LocalTensor<half> tensor = inQueue.AllocTensor<half>();
// ... write data ...
inQueue.EnQue(tensor);
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| T | Template | The data type of the tensor (e.g. `half`, `float`) |

## Semantics

`AllocTensor` claims a portion of the memory from a TQue (Queue). It must always be matched with a corresponding `FreeTensor` when the compute block is finished to prevent deadlocks in the MTE (Memory Transfer Engine) pipelines.

## Example
```cpp
#include "kernel_operator.h"
using namespace AscendC;

__aicore__ inline void ProcessQueue() {
    TPipe pipe;
    TQue<QuePosition::VECIN, 1> inQueueX;
    pipe.InitBuffer(inQueueX, 1, 256 * sizeof(half));

    // Allocate the tensor from the queue
    LocalTensor<half> xLocal = inQueueX.AllocTensor<half>();
    
    // ... use xLocal ...

    // Free the tensor back to the queue
    inQueueX.FreeTensor(xLocal);
}
```
