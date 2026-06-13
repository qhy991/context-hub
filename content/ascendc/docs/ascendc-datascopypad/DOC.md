---
name: ascendc-datascopypad
description: Copy data with padding support
metadata:
  languages: ascendc
  versions: '8.0'
  revision: 1
  updated-on: '2026-06-13'
  source: official
  tags: ascend,npu,ascendc,mte,memory,datamovement,padding
---

# DataCopyPad

Copy data with padding support.

## Syntax

```cpp
template <typename T>
void DataCopyPad(LocalTensor<T>& dst, GlobalTensor<T>& src, int32_t count, uint16_t pad_value)

template <typename T>
void DataCopyPad(GlobalTensor<T>& dst, LocalTensor<T>& src, int32_t count, uint16_t pad_value)
```

## Description

Copies data between Global Memory (HBM) and Local Memory (UB) with automatic padding for alignment requirements. This is useful when the data size is not a multiple of the hardware's preferred alignment (e.g., 32 or 256 elements). The MTE unit handles the transfer and fills padding positions with the specified pad value.

## Hardware Unit

MTE (Memory Transfer Engine)

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| dst | LocalTensor<T>& or GlobalTensor<T>& | Destination tensor |
| src | GlobalTensor<T>& or LocalTensor<T>& | Source tensor |
| count | int32_t | Number of elements to copy |
| pad_value | uint16_t | Value to use for padding positions |

## Supported Data Types

- float16 (half)
- float32 (float)
- int32_t
- int16_t
- int8_t

## Semantics

```pseudo
// Copy with automatic padding
aligned_count = align_up(count, alignment)
for i in 0..count-1:
    dst[i] = src[i]  // Copy actual data
for i in count..aligned_count-1:
    dst[i] = pad_value  // Fill padding
```

## CANN Version

CANN 8.0+

## Target Architecture

Ascend NPU (Atlas series)

## Related Instructions

- [DataCopy](../ascendc-datascopy/DOC.md)

## Example

```cpp
using namespace ascendc;

// Copy with padding for non-aligned data
GlobalTensor<float> global_src = global_buffer;
LocalTensor<float> local_dst = local_buffer;
int32_t count = 1000;  // Not 32-aligned
uint16_t pad_value = 0;

// Copy with automatic padding to next alignment boundary
DataCopyPad(local_dst, global_src, count, pad_value);

// Compute on aligned data...
Add(local_dst, local_dst, local_dst, 1024);
```