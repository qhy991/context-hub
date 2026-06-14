---
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
