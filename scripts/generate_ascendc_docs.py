import os

base_path = "/Users/haiyan-mini/Agent4Kernel/context-hub/content/ascendc/docs"
skills_path = "/Users/haiyan-mini/Agent4Kernel/context-hub/content/ascendc/skills"

docs_content = {
    "ascendc-ln": """---
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
""",
    "ascendc-sin": """---
name: ascendc-sin
description: Sine function of a tensor
metadata:
  languages: ascendc
  versions: '8.0'
  revision: 1
  updated-on: '2026-06-14'
  source: official
  tags: ascend,npu,ascendc,vector,simd,math
---

# Sin

Computes the sine of a tensor element-wise.

## Syntax

```cpp
template <typename T>
void Sin(LocalTensor<T>& dst, LocalTensor<T>& src, int32_t count)
```

## Description

Performs element-wise sine computation on the source tensor and stores the result in the destination tensor. The input values should typically be in radians.

## Hardware Unit

Vector Unit

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| dst | LocalTensor<T>& | Destination tensor storing the sine result |
| src | LocalTensor<T>& | Source tensor (input in radians) |
| count | int32_t | Number of elements to compute |

## Supported Data Types

- float16 (half)
- float32 (float)
""",
    "ascendc-cos": """---
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
""",
    "ascendc-cast": """---
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
""",
    "ascendc-enque": """---
name: ascendc-enque
description: Enqueue a local tensor to a queue
metadata:
  languages: ascendc
  versions: '8.0'
  revision: 1
  updated-on: '2026-06-14'
  source: official
  tags: ascend,npu,ascendc,queue,memory,pipeline
---

# EnQue

Pushes a LocalTensor into a `TQue`.

## Syntax

```cpp
template <TPosition pos, typename T>
void TQue<pos, 1>::EnQue(LocalTensor<T>& tensor)
```

## Description

Used in Ascend C pipeline programming. Enqueues a `LocalTensor` containing valid data into the asynchronous queue so that the next pipeline stage (or hardware unit) can access it.

## Example

```cpp
TQue<QuePosition::VECIN, 1> inQueue;
LocalTensor<half> tensor = inQueue.AllocTensor<half>();
// ... fill tensor with data ...
inQueue.EnQue(tensor); // Send to Vector unit
```
""",
    "ascendc-deque": """---
name: ascendc-deque
description: Dequeue a local tensor from a queue
metadata:
  languages: ascendc
  versions: '8.0'
  revision: 1
  updated-on: '2026-06-14'
  source: official
  tags: ascend,npu,ascendc,queue,memory,pipeline
---

# DeQue

Pops a LocalTensor from a `TQue`.

## Syntax

```cpp
template <TPosition pos, typename T>
LocalTensor<T> TQue<pos, 1>::DeQue()
```

## Description

Used in Ascend C pipeline programming. Dequeues a `LocalTensor` from the queue for processing. This is a blocking operation if the queue is empty.

## Example

```cpp
TQue<QuePosition::VECIN, 1> inQueue;
LocalTensor<half> tensor = inQueue.DeQue<half>();
// ... process data ...
inQueue.FreeTensor(tensor); // Return memory after use
```
""",
    "ascendc-alloctensor": """---
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
""",
    "ascendc-freetensor": """---
name: ascendc-freetensor
description: Free a tensor back to the queue's memory pool
metadata:
  languages: ascendc
  versions: '8.0'
  revision: 1
  updated-on: '2026-06-14'
  source: official
  tags: ascend,npu,ascendc,queue,memory,pipeline
---

# FreeTensor

Releases a LocalTensor back to the queue.

## Syntax

```cpp
template <TPosition pos, typename T>
void TQue<pos, 1>::FreeTensor(LocalTensor<T>& tensor)
```

## Description

Returns a previously dequeued `LocalTensor` back to the memory pool of the queue once processing is complete, enabling memory reuse.

## Example

```cpp
TQue<QuePosition::VECIN, 1> inQueue;
LocalTensor<half> tensor = inQueue.DeQue<half>();
// ... process data ...
inQueue.FreeTensor(tensor); // Free memory block
```
"""
}

skills_content = {
    "ascendc-double-buffering": """---
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
"""
}

# Create docs
for doc_name, content in docs_content.items():
    dpath = os.path.join(base_path, doc_name)
    os.makedirs(dpath, exist_ok=True)
    with open(os.path.join(dpath, "DOC.md"), "w") as f:
        f.write(content)

# Create skills
for skill_name, content in skills_content.items():
    spath = os.path.join(skills_path, skill_name)
    os.makedirs(spath, exist_ok=True)
    with open(os.path.join(spath, "SKILL.md"), "w") as f:
        f.write(content)

print("Ascend C documentation and skills generation complete.")
