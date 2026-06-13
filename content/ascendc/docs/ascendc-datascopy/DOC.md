---
name: ascendc-datascopy
description: Copy data between Global and Local memory
metadata:
  languages: ascendc
  versions: '8.0'
  revision: 1
  updated-on: '2026-06-13'
  source: official
  tags: ascend,npu,ascendc,mte,memory,datamovement
---

# DataCopy

Copy data between Global and Local memory.

## Syntax

```cpp
// Global to Local (CopyIn)
template <typename T>
void DataCopy(LocalTensor<T>& dst, GlobalTensor<T>& src, int32_t count)

// Local to Global (CopyOut)
template <typename T>
void DataCopy(GlobalTensor<T>& dst, LocalTensor<T>& src, int32_t count)
```

## Description

Copies data between Global Memory (HBM) and Local Memory (UB - Unified Buffer). This is a fundamental operation in the AscendC programming model for the CopyIn/Compute/CopyOut pipeline. The MTE (Memory Transfer Engine) unit handles these transfers efficiently while the Vector unit computes on data already in UB.

## Hardware Unit

MTE (Memory Transfer Engine)

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| dst | LocalTensor<T>& or GlobalTensor<T>& | Destination tensor |
| src | GlobalTensor<T>& or LocalTensor<T>& | Source tensor |
| count | int32_t | Number of elements to copy |

## Supported Data Types

- float16 (half)
- float32 (float)
- int32_t
- int16_t
- int8_t
- int4_t

## Semantics

```pseudo
// Memory transfer: no computation, just data movement
for i in 0..count-1:
    dst[i] = src[i]  // Direct memory copy
```

## CANN Version

CANN 8.0+

## Target Architecture

Ascend NPU (Atlas series)

## Related Instructions

- [DataCopyPad](../ascendc-datascopypad/DOC.md)

## Example

```cpp
using namespace ascendc;

// CopyIn: Global Memory → Local Memory (UB)
GlobalTensor<float> global_src = global_buffer;
LocalTensor<float> local_dst = local_buffer;
DataCopy(local_dst, global_src, 1024);

// Compute on data in UB...
Add(local_dst, local_dst, local_dst, 1024);

// CopyOut: Local Memory (UB) → Global Memory
GlobalTensor<float> global_dst = output_buffer;
DataCopy(global_dst, local_dst, 1024);
```