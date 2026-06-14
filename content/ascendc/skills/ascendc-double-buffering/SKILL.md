---
name: ascendc-double-buffering
description: Ascend C pattern for Ping-Pong Double Buffering
metadata:
  languages: ascendc
  versions: '8.0'
  revision: 1
  updated-on: '2026-06-14'
  source: official
  tags: ascend,npu,ascendc,optimization,pipeline,skill
---

# Double Buffering (Ping-Pong Buffer) in Ascend C

Double Buffering is a critical optimization technique in Ascend C that hides latency by overlapping Data Movement (MTE2/MTE3) and Vector/Cube Computations. 

## The Problem

If a single buffer is used, the compute unit must wait for the data to be fully loaded from Global Memory before it can start. Similarly, the store operation must wait for computation to finish. 

## The Solution

By allocating `DEPTH=2` in your `TQue`, Ascend C automatically handles a ping-pong mechanism. While the compute unit is processing buffer `0`, the DMA unit (DataCopy) is already loading data into buffer `1`.

## Code Pattern

```cpp
#include "kernel_operator.h"
using namespace ascendc;

class KernelDoubleBuffer {
public:
    __aicore__ inline KernelDoubleBuffer() {}
    __aicore__ inline void Init(GM_ADDR x, GM_ADDR y, uint32_t totalLength, uint32_t tileLength) {
        // ... set parameters ...
        // Initialize Queue with Depth 2
        inQueueX.Init(2); // Ping-Pong buffer
        outQueueY.Init(2);

        // Pipe memory alloc...
    }

    __aicore__ inline void Process() {
        int32_t loopCount = this->totalLength / this->tileLength;
        for (int32_t i = 0; i < loopCount; i++) {
            CopyIn(i);
            Compute(i);
            CopyOut(i);
        }
    }

private:
    __aicore__ inline void CopyIn(int32_t progress) {
        LocalTensor<half> xLocal = inQueueX.AllocTensor<half>();
        DataCopy(xLocal, xGlobal[progress * tileLength], tileLength);
        inQueueX.EnQue(xLocal);
    }

    __aicore__ inline void Compute(int32_t progress) {
        LocalTensor<half> xLocal = inQueueX.DeQue<half>();
        LocalTensor<half> yLocal = outQueueY.AllocTensor<half>();
        
        // Element-wise operations
        Exp(yLocal, xLocal, tileLength);
        
        inQueueX.FreeTensor(xLocal);
        outQueueY.EnQue(yLocal);
    }

    __aicore__ inline void CopyOut(int32_t progress) {
        LocalTensor<half> yLocal = outQueueY.DeQue<half>();
        DataCopy(yGlobal[progress * tileLength], yLocal, tileLength);
        outQueueY.FreeTensor(yLocal);
    }

private:
    GlobalTensor<half> xGlobal;
    GlobalTensor<half> yGlobal;
    TQue<QuePosition::VECIN, 2> inQueueX; // Depth=2 enables Double Buffering
    TQue<QuePosition::VECOUT, 2> outQueueY;
    uint32_t tileLength;
    uint32_t totalLength;
};
```

## Key Takeaways

1. `TQue.Init(2)` is the enabler for Double Buffering. 
2. Ensure you have properly split your work into `tiles` so that the pipeline can continuously stream data.
3. The hardware handles the barrier synchronization implicitly via the queue's `EnQue` and `DeQue` semantics.
