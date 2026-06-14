---
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
