import os

base_path = "/Users/haiyan-mini/Agent4Kernel/context-hub/content/rocm/docs"
skills_path = "/Users/haiyan-mini/Agent4Kernel/context-hub/content/rocm/skills"

docs_content = {
    "rocblas-sgemm": """---
name: rocblas-sgemm
description: Single precision general matrix-matrix multiplication in rocBLAS
metadata:
  languages: cpp,hip
  versions: '6.0'
  revision: 1
  updated-on: '2026-06-14'
  source: official
  tags: rocm,amd,hip,rocblas,gemm,math
---

# rocblas_sgemm

Performs a single precision general matrix-matrix multiplication.

## Syntax

```cpp
rocblas_status rocblas_sgemm(rocblas_handle handle,
                             rocblas_operation transA,
                             rocblas_operation transB,
                             rocblas_int m,
                             rocblas_int n,
                             rocblas_int k,
                             const float* alpha,
                             const float* A,
                             rocblas_int lda,
                             const float* B,
                             rocblas_int ldb,
                             const float* beta,
                             float* C,
                             rocblas_int ldc);
```

## Description

`rocblas_sgemm` performs the matrix-matrix operation:
`C = alpha * op(A) * op(B) + beta * C`
where `op(X)` is either `op(X) = X` or `op(X) = X^T`.

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| handle | rocblas_handle | Handle to the rocBLAS library context |
| transA | rocblas_operation | Specifies the operation applied to A (e.g., rocblas_operation_none, rocblas_operation_transpose) |
| transB | rocblas_operation | Specifies the operation applied to B |
| m | rocblas_int | Number of rows of matrix op(A) and C |
| n | rocblas_int | Number of columns of matrix op(B) and C |
| k | rocblas_int | Number of columns of op(A) and rows of op(B) |
| alpha | const float* | Scalar multiplier for A*B |
| A | const float* | Pointer to matrix A |
| lda | rocblas_int | Leading dimension of A |
| B | const float* | Pointer to matrix B |
| ldb | rocblas_int | Leading dimension of B |
| beta | const float* | Scalar multiplier for C |
| C | float* | Pointer to matrix C |
| ldc | rocblas_int | Leading dimension of C |

## Return Value

`rocblas_status_success` if successful, otherwise an error code.
""",
    "rccl-allreduce": """---
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
""",
    "hipcub-block-reduce": """---
name: hipcub-block-reduce
description: Block-wide reduction utility in hipCUB
metadata:
  languages: cpp,hip
  versions: '6.0'
  revision: 1
  updated-on: '2026-06-14'
  source: official
  tags: rocm,amd,hip,hipcub,reduce,block
---

# hipcub::BlockReduce

A stateful abstraction for performing block-wide reduction operations across threads in a HIP thread block.

## Syntax

```cpp
template <
    typename T,
    int BLOCK_DIM_X,
    hipcub::BlockReduceAlgorithm ALGORITHM = hipcub::BLOCK_REDUCE_WARP_REDUCTIONS,
    int BLOCK_DIM_Y = 1,
    int BLOCK_DIM_Z = 1>
class BlockReduce;
```

## Description

Equivalent to `cub::BlockReduce` in CUDA. Allows all threads in a block to cooperatively reduce a set of values (e.g., sum, max) to a single value.

## Example

```cpp
#include <hipcub/hipcub.hpp>

__global__ void BlockSumKernel(int* d_in, int* d_out) {
    // Specialize BlockReduce for a 1D block of 128 threads
    typedef hipcub::BlockReduce<int, 128> BlockReduceT;

    // Allocate shared memory for BlockReduce
    __shared__ typename BlockReduceT::TempStorage temp_storage;

    // Obtain a segment of consecutive items that are blocked across threads
    int thread_data = d_in[threadIdx.x];

    // Compute the block-wide sum for thread0
    int aggregate = BlockReduceT(temp_storage).Sum(thread_data);

    if (threadIdx.x == 0) {
        d_out[blockIdx.x] = aggregate;
    }
}
```
"""
}

skills_content = {
    "rocm-wavefront-programming": """---
name: rocm-wavefront-programming
description: Understanding and utilizing Wavefront operations in HIP
metadata:
  languages: cpp,hip
  versions: '6.0'
  revision: 1
  updated-on: '2026-06-14'
  source: official
  tags: rocm,amd,hip,wavefront,warp,shuffle,skill
---

# Wavefront Programming in ROCm (HIP)

In CUDA, threads are grouped into "Warps" (typically 32 threads). In ROCm/AMD GPUs, threads are grouped into "Wavefronts" (Waves). A critical difference is that the Wavefront size is architecture-dependent:
- **CDNA (MI100, MI200, MI300)**: Wave64 (64 threads per wavefront)
- **RDNA (RX 6000, RX 7000)**: Wave32 (32 threads per wavefront, though some modes emulate 64)

## `warpSize` vs `wavefrontSize`

When writing portable HIP code, never hardcode `32` or `64`. Instead, use the built-in variable:
```cpp
// Incorrect (assumes CUDA warp size)
int lane_id = threadIdx.x % 32;

// Correct (portable across AMD and NVIDIA via HIP)
int lane_id = threadIdx.x % warpSize; 
```

## Cross-Lane Shuffle Operations

HIP provides `__shfl_*` primitives identical to CUDA, but they operate over the entire wavefront.

```cpp
// Broadcasts value from lane 'srcLane' to all lanes in the wavefront
int val = __shfl(data, srcLane, warpSize);

// Shifts data down by 'delta' lanes
int val_down = __shfl_down(data, delta, warpSize);

// XOR shuffle (useful for butterfly reductions)
int val_xor = __shfl_xor(data, laneMask, warpSize);
```

### Wavefront Reduction Example

```cpp
__device__ float wave_reduce_sum(float val) {
    // Iterate log2(warpSize) times
    for (int offset = warpSize / 2; offset > 0; offset /= 2) {
        val += __shfl_down(val, offset, warpSize);
    }
    return val; // Lane 0 holds the final sum
}
```

## Built-in Wavefront Functions

ROCm provides specific built-ins for wavefront-level voting and execution masks:
- `__ballot(predicate)`: Returns a 64-bit integer (on Wave64) representing the active lanes where `predicate` is true.
- `__any(predicate)`: Returns true if any active lane evaluates `predicate` to true.
- `__all(predicate)`: Returns true if all active lanes evaluate `predicate` to true.
""",

    "rocm-lds-bank-conflicts": """---
name: rocm-lds-bank-conflicts
description: Optimizing Local Data Share (LDS) usage to avoid bank conflicts
metadata:
  languages: cpp,hip
  versions: '6.0'
  revision: 1
  updated-on: '2026-06-14'
  source: official
  tags: rocm,amd,hip,lds,shared-memory,optimization,skill
---

# Local Data Share (LDS) Bank Conflicts in ROCm

LDS (Local Data Share) in AMD GPUs is the equivalent of Shared Memory in NVIDIA GPUs. It is divided into memory banks to allow simultaneous parallel access by multiple threads in a wavefront.

## Bank Structure (CDNA Architecture)

In CDNA architectures (like MI200/MI300):
- LDS is divided into **32 banks**.
- Each bank is **4 bytes (32 bits)** wide.
- Successive 4-byte words are assigned to successive banks.

## What is a Bank Conflict?

A bank conflict occurs when multiple threads within the same wavefront access different addresses that map to the *same* memory bank. When this happens, the memory requests are serialized, significantly degrading performance.

*(Note: If all threads access the exact same address, it triggers a broadcast mechanism and does NOT cause a bank conflict).*

## Example of a Bank Conflict

```cpp
__shared__ float smem[1024];

// Stride of 32 elements (32 * 4 bytes = 128 bytes)
// Thread 0 accesses smem[0] -> Bank 0
// Thread 1 accesses smem[32] -> Bank 0
// ... Conflict!
float val = smem[threadIdx.x * 32]; 
```

## Solution: Memory Padding

The most common technique to resolve LDS bank conflicts is padding. By changing the stride so it is relatively prime to the number of banks (32), you ensure that threads hit different banks.

### Fixing the conflict with padding:

```cpp
// Add 1 to the stride to offset the bank mapping
__shared__ float smem_padded[32][33]; 

// Thread 0 accesses smem_padded[0][0] (linear index 0) -> Bank 0
// Thread 1 accesses smem_padded[1][0] (linear index 33) -> Bank 1
// Conflict avoided!
float val = smem_padded[threadIdx.x][0];
```

## Tools to Detect Conflicts

Use `rocprof` to profile your kernel and look for high values in the `LDS_BANK_CONFLICT` metric. If this counter is high, investigate your shared memory access patterns.
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

print("ROCm documentation and skills generation complete.")
