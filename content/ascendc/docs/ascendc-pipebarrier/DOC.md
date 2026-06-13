---
name: ascendc-pipebarrier
description: Pipeline barrier synchronization
metadata:
  languages: ascendc
  versions: '8.0'
  revision: 1
  updated-on: '2026-06-13'
  source: official
  tags: ascend,npu,ascendc,sync,pipeline,barrier
---

# PipeBarrier

Pipeline barrier synchronization.

## Syntax

```cpp
template <PIPE_LEVEL level>
void PipeBarrier()
```

## Description

Synchronizes operations within the AICore pipeline at different levels. The AscendC programming model uses a multi-stage pipeline (CopyIn → Compute → CopyOut) that can execute concurrently. PipeBarrier ensures completion of operations at a specified pipeline level before proceeding, preventing data hazards and ensuring correct execution order.

## Hardware Unit

Pipeline Control Unit

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| level | PIPE_LEVEL | Pipeline level to synchronize (e.g., PIPE_ALL, PIPE_V, PIPE_MTE) |

## Supported Data Types

N/A (synchronization primitive)

## Semantics

```pseudo
// Block until all operations at the specified level complete
wait_until(level_operations_done)
```

## CANN Version

CANN 8.0+

## Target Architecture

Ascend NPU (Atlas series)

## Related Instructions

- [SyncAll](../ascendc-syncall/DOC.md) - cross-AICore synchronization

## Example

```cpp
using namespace ascendc;

// Stage 1: Copy data from Global to Local memory
DataCopy(local_A, global_A, 1024);
DataCopy(local_B, global_B, 1024);

// Ensure data transfer complete before computation
PipeBarrier<PIPE_MTE>();

// Stage 2: Compute on data in UB
Add(local_C, local_A, local_B, 1024);

// Ensure computation complete before copy-out
PipeBarrier<PIPE_V>();

// Stage 3: Copy result back to Global memory
DataCopy(global_C, local_C, 1024);
```