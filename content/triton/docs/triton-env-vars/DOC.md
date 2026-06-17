---
name: triton-env-vars
description: Triton environment variables for debug, caching, and execution control
metadata:
  languages: triton
  versions: '2.1'
  revision: 1
  updated-on: '2026-06-17'
  source: official
  tags: triton,gpu,environment,debug,cache,tooling,command-line
---

# Triton environment variables

Shell-level knobs that change how Triton compiles, caches, and executes kernels.
Set them in the shell before launching Python. They are essential for debugging
correctness, forcing recompilation, and driving profiling.

## Syntax

```bash
export TRITON_INTERPRET=1     # run on CPU interpreter (no GPU needed)
export TRITON_CACHE_DIR=/path # override the autotune/compile cache location
export TRITON_DEBUG=1         # emit extra runtime debug info
python run.py
```

## Variables

| Variable | Values | Effect |
|----------|--------|--------|
| `TRITON_INTERPRET` | `0` / `1` | `1` executes `@triton.jit` kernels in a Python-level CPU interpreter. Correctness only — no GPU, ~no speed. Used to validate kernel logic without a GPU and to single-step `tl.*` ops. |
| `TRITON_CACHE_DIR` | path | Directory for compiled kernels + autotune results. Override to share a cache across runs, isolate it per experiment, or clear it (`rm -rf` then re-run) to force recompile/retune. |
| `TRITON_DEBUG` | `0` / `1` | Enables additional runtime diagnostics (e.g. IR/launch info). Verbose; use only while debugging. |
| `TRITON_PRINT_AUTOTUNING` | `0` / `1` | Print which config `triton.autotune` selects after benchmarking. |
| `TRITON_F32_DEFAULT` | `ieee` / `tf32` | Default precision for `tl.float32` dot products. `tf32` enables TF32 tensor cores (faster, lower precision) unless the op opts out. |
| `TRITON_DEFAULT_COMPILER` | e.g. `triton` | Selects the compiler backend when more than one is available. |
| `TRITON_KERNEL_DUMP_DIR` | path | Dump generated PTX/LLVMIR/TTIR to this dir for offline inspection (pair with [triton-opt](../triton-opt/DOC.md)). |

> Exact set varies by Triton point release; run `python -c "import triton; print([v for v in dir(triton.runtime) if 'CACHE' in v or 'DEBUG' in v])"` or check the installed version's docs for the authoritative list.

## Common pitfalls

- **Stale autotune cache.** If you change a kernel's body but `TRITON_CACHE_DIR`
  keeps an old entry keyed on a stable signature, Triton may reuse the old tuned
  config. Clear the cache or bump the signature when iterating on structure.
- **`TRITON_INTERPRET=1` silently hides GPU-specific bugs.** It's great for logic
  checks but never validates shared-memory layout, bank conflicts, or occupancy.
- **`TRITON_F32_DEFAULT=tf32` changes numerics.** A "correct" kernel can drift
  tolerance once TF32 is on; set it explicitly in tests, not implicitly.

## Triton Version

Triton 2.1+ (most variables present since 2.0; TF32 default since 2.1).

## Target Architecture

NVIDIA GPU (SM 7.0+), AMD GPU. `TRITON_INTERPRET` is CPU-only and GPU-agnostic.

## Related Instructions

- [triton-opt](../triton-opt/DOC.md)
- [triton-proton](../triton-proton/DOC.md)
- [triton-autotune](../triton-autotune/DOC.md)

## Example

```bash
# 1) Logic-check a kernel with no GPU, then 2) profile it cleanly on GPU.
TRITON_INTERPRET=1 python -m pytest test_kernel.py        # CPU correctness
TRITON_CACHE_DIR=/tmp/tc_fresh rm -rf /tmp/tc_fresh        # fresh tune
TRITON_CACHE_DIR=/tmp/tc_fresh TRITON_PRINT_AUTOTUNING=1 \
  python -m triton.profiler.viewer --profile -- python bench_kernel.py
```
