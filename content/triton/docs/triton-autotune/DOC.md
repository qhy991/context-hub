---
name: triton-autotune
description: Auto-tune a Triton kernel over a config space
metadata:
  languages: triton
  versions: '2.1'
  revision: 1
  updated-on: '2026-06-16'
  source: official
  tags: triton,gpu,autotune,performance,programming-model
---

# triton.autotune

Decorator for auto-tuning a `triton.jit`'d kernel over a set of configurations.

## Syntax

```python
@triton.autotune(
    configs=[triton.Config(...), ...],
    key=['M', 'N', 'K'],
    prune_configs_by={'early_config_prune': early_prune_fn},
    warmup=25,
    rep=100
)
@triton.jit
def kernel_fn(...):
    ...
```

## Description

`triton.autotune` benchmarks all candidate `triton.Config` objects on the first invocation and caches the best config for each combination of `key` argument values. On subsequent calls with the same key values, the cached best config is used directly. The `prune_configs_by` dict maps function names to pruning functions that can remove configs before benchmarking.

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| configs | list[triton.Config] | Candidate configurations to benchmark |
| key | list[str] | Argument names whose values trigger re-evaluation |
| prune_configs_by | dict (optional) | `{name: fn}` to prune configs before benchmarking |
| reset_to_zero | list[str] (optional) | Arguments to reset to zero before each benchmark |
| restore_value | list[str] (optional) | Arguments to restore after benchmarking |
| pre_hook | callable (optional) | Called before each kernel invocation |
| post_hook | callable (optional) | Called after each kernel invocation |
| warmup | int | Warmup iterations (default 25) |
| rep | int | Benchmark repetitions (default 100) |
| use_cuda_graph | bool | Use CUDA graphs for benchmarking (default False) |
| cache_results | bool | Cache autotune results to disk (default False) |

## Triton Version

Triton 2.1+

## Target Architecture

NVIDIA GPU (SM 7.0+), AMD GPU (CDNA2+ / RDNA3+)

## Related Instructions

- [triton.jit](../triton-jit/DOC.md)
- [triton.Config](../triton-config/DOC.md)

## Example

```python
import triton
import triton.language as tl

@triton.autotune(
    configs=[
        triton.Config({'BLOCK_M': 128, 'BLOCK_N': 256, 'BLOCK_K': 32}, num_warps=8),
        triton.Config({'BLOCK_M': 256, 'BLOCK_N': 128, 'BLOCK_K': 32}, num_warps=8),
    ],
    key=['M', 'N', 'K'],
)
@triton.jit
def matmul_kernel(a_ptr, b_ptr, c_ptr, M, N, K,
                  BLOCK_M: tl.constexpr, BLOCK_N: tl.constexpr, BLOCK_K: tl.constexpr):
    ...
```