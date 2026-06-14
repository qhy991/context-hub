---
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
