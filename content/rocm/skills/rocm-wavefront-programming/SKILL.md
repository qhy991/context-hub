---
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
