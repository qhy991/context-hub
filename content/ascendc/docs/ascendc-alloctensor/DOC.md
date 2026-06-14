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
