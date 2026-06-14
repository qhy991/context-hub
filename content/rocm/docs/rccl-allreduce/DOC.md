---
name: rccl-allreduce
description: RCCL collective operation for AllReduce
metadata:
  languages: cpp,hip
  versions: '6.0'
  revision: 1
  updated-on: '2026-06-14'
  source: official
  tags: rocm,amd,hip,rccl,communication,mpi,distributed
---

# ncclAllReduce / rcclAllReduce

Reduces data from all ranks in a communicator and distributes the result back to all ranks.

## Syntax

```cpp
ncclResult_t ncclAllReduce(const void* sendbuff,
                           void* recvbuff,
                           size_t count,
                           ncclDataType_t datatype,
                           ncclRedOp_t op,
                           ncclComm_t comm,
                           hipStream_t stream);
```
*(Note: RCCL uses the same API signatures as NCCL for compatibility)*

## Description

Performs a reduction (e.g., sum, min, max) of `sendbuff` arrays across all GPUs in the communicator `comm` and writes the result to `recvbuff` on all GPUs.

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| sendbuff | const void* | Pointer to send buffer |
| recvbuff | void* | Pointer to receive buffer (can be same as sendbuff for in-place) |
| count | size_t | Number of elements in buffer |
| datatype | ncclDataType_t | Data type (e.g., ncclFloat32, ncclHalf) |
| op | ncclRedOp_t | Reduction operation (e.g., ncclSum, ncclMax) |
| comm | ncclComm_t | RCCL communicator |
| stream | hipStream_t | HIP stream to execute the operation on |

## Best Practices

- Ensure the `hipStream_t` is properly synchronized if mixing compute and communication.
- RCCL operations are asynchronous with respect to the host.
