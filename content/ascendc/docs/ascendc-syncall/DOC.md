---
name: ascendc-syncall
description: Cross-AICore synchronization
metadata:
  languages: ascendc
  versions: '8.0'
  revision: 1
  updated-on: '2026-06-13'
  source: official
  tags: ascend,npu,ascendc,sync,multicore
---

# SyncAll

Cross-AICore synchronization.

## Syntax

```cpp
void SyncAll()
```

## Description

Synchronizes all AICores within an AI Core cluster. This is a collective operation that ensures all participating AICores reach the synchronization point before any proceed. It's essential for coordinating multi-core operations and ensuring data consistency when cores share or exchange data.

## Hardware Unit

Synchronization Unit (cross-core)

## Parameters

None

## Supported Data Types

N/A (synchronization primitive)

## Semantics

```pseudo
// Collective barrier: wait until all AICores reach this point
arrive_at_barrier()
wait_until(all_AICores_arrived)
proceed()
```

## CANN Version

CANN 8.0+

## Target Architecture

Ascend NPU (Atlas series)

## Related Instructions

- [PipeBarrier](../ascendc-pipebarrier/DOC.md) - intra-AICore synchronization

## Example

```cpp
using namespace ascendc;

// Each AICore computes its partition
LocalTensor<float> local_result = result_buffer;
LocalTensor<float> local_data = data_buffer;
int32_t my_count = 1024;  // Partition size

// Compute on local partition
Add(local_result, local_data, local_data, my_count);

// Ensure all cores complete their partitions
SyncAll();

// Now safe to use or combine results from all cores
```