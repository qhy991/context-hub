---
name: triton-autotune-tuning
description: Practical autotuning — config spaces, pruning, heuristics, num_warps/num_stages
metadata:
  languages: triton
  versions: '2.1'
  revision: 1
  updated-on: '2026-06-17'
  source: official
  tags: triton,gpu,autotune,performance,tuning,programming-model
---

# Practical Triton autotuning

`triton.autotune` (see [triton-autotune](../triton-autotune/DOC.md)) benchmarks a
config space and caches the best per `key`. This entry covers *how to choose that
space well* — the part that decides whether autotuning helps or just burns time.

## The four knobs a `triton.Config` controls

| Knob | Typical effect |
|------|----------------|
| `BLOCK_*` tile sizes | The dominant lever. Larger tiles raise arithmetic intensity but cost registers/shared memory and can spill or cut occupancy. |
| `num_warps` | Threads per block in warps. More warps = more parallelism / latency hiding, but fewer registers per thread. |
| `num_stages` | Software-pipelining stages for global→shared loads. Higher stages hide global latency via more shared-memory buffering. |
| `num_ctas` | Co-operating CTAs (persistent / split-K styles) where supported. |

```python
triton.Config(
    {'BLOCK_M': 128, 'BLOCK_N': 128, 'BLOCK_K': 64},
    num_warps=8, num_stages=3,
)
```

## Designing the config space

- **Powers-of-two, geometric spread.** Tile dims as `[64,128,256]` etc., not a
  dense sweep — autotune time scales with `|configs| × |key-values|`.
- **Pair tiles with warps sensibly.** A 256-wide tile with `num_warps=1` starves
  the SM; include matching `(tile, warps)` combinations.
- **Bound by shared memory.** `BLOCK_M*BLOCK_N*dtype_bytes` (per stage) must fit
  the SM's shared memory; over-large configs silently spill. Let `prune_configs_by`
  kill infeasible ones before benchmarking.
- **`num_stages` is memory-bound-kernel sensitive.** For a memory-bound kernel,
  extra stages add shared-memory pressure for little gain; for a compute-bound
  loop with a global load, more stages are the win.

## Pruning before benchmarking

`prune_configs_by={'early_config_prune': fn, 'perf_model': fn}` lets you drop
configs cheaply:

```python
def early_prune(config, named_args, **_):
    # Kill configs whose shared memory exceeds the device limit.
    bm = config.kwargs['BLOCK_M']; bn = config.kwargs['BLOCK_N']
    bytes_per_stage = bm * bn * 2          # fp16
    max_smem = 96 * 1024                   # device-dependent
    return None if bytes_per_stage * config.num_stages > max_smem else config

@triton.autotune(configs=big_space, key=['M','N'],
                 prune_configs_by={'early_config_prune': early_prune})
```

A prune fn returns `None` to drop, or the (possibly mutated) config to keep.

## Heuristics — decouple meta from search

`triton.heuristics` picks a `constexpr` from a Python function of the runtime
args, *before* autotune, so the search space is shaped per problem size:

```python
@triton.heuristics({'BLOCK_K': lambda args: 64 if args['K'] >= 128 else 32})
@triton.autotune(configs=[...], key=['M','N'])
@triton.jit
def matmul(...): ...
```

Use heuristics for things you can decide from shape/dtype alone (e.g. small-K
shortcuts), and reserve autotune for what genuinely needs measurement.

## Persistent kernels (out-of-autotune option)

For memory-bound / launch-bound kernels, a **persistent** (megakernel) launch
that keeps blocks resident and streams work can beat any tiled autotuned config —
at the cost of more complex indexing. Consider it when autotune plateaus and the
roofline says you're launch/occupancy-bound, not compute-bound.

## Common pitfalls

- **Forgetting `key`.** Without `key`, autotune re-benchmarks every call →
  effectively no caching. `key` should be the args whose value changes the best
  config (shapes, not strides unless they matter).
- **Tuning a cold cache in production.** First call pays the whole autotune bill.
  Pre-warm (`TRITON_CACHE_DIR` shared across deploy) or `cache_results=True`.
- **Tuning tiny kernels.** Autotune overhead can exceed the kernel; for sub-microsecond
  kernels, hand-pick one config instead.

## Triton Version

Triton 2.1+ (`prune_configs_by`, `heuristics`, `num_stages`, persistent patterns).

## Target Architecture

NVIDIA GPU (SM 7.0+), AMD GPU (CDNA2+ / RDNA3+).

## Related Instructions

- [triton-autotune](../triton-autotune/DOC.md)
- [triton-config](../triton-config/DOC.md)
- [triton-proton](../triton-proton/DOC.md)

## Example

```python
configs = [
    triton.Config({'BM':m,'BN':n,'BK':k}, num_warps=w, num_stages=s)
    for m in [64,128,256] for n in [64,128,256] for k in [32,64]
    for w in [4,8] for s in [2,3,4]
]

def early_prune(cfg, named_args, **_):
    if cfg.kwargs['BM']*cfg.kwargs['BN']*2*cfg.num_stages > 96*1024:
        return None
    if cfg.kwargs['BK'] > 64 and cfg.kwargs['BM'] < 128:
        return None
    return cfg

@triton.autotune(configs, key=['M','N'],
                 prune_configs_by={'early_config_prune': early_prune},
                 restore_value=['C'])            # C is overwritten during bench
@triton.jit
def matmul(...): ...
```
