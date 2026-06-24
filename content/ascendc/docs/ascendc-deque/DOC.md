---
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

## Semantics

```cpp
LocalTensor<T> tensor = queue.DeQue<T>();
// Pop a tensor from the front of the queue and return its handle. 
// Blocks if the queue is empty.
```

## Example

```cpp
TQue<QuePosition::VECIN, 1> inQueue;
LocalTensor<half> tensor = inQueue.DeQue<half>();
// ... process data ...
inQueue.FreeTensor(tensor); // Return memory after use
```
