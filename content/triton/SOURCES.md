# Triton Documentation Sources

## Overview

120 DOC.md entries covering the Triton GPU programming language APIs, based on
the official Triton source code and documentation as of June 2026.

## Primary Sources

| Source | URL | Content Extracted |
|--------|-----|-------------------|
| Triton language `__init__.py` | https://github.com/triton-lang/triton/blob/main/python/triton/language/__init__.py | Complete `__all__` export list (144 names) |
| Triton language `core.py` | https://github.com/triton-lang/triton/blob/main/python/triton/language/core.py | Function signatures, docstrings, parameter types for: program_id, num_programs, arange, full, broadcast, broadcast_to, trans, permute, cat, join, split, view, reshape, expand_dims, cast, dot, dot_scaled, load, store, make_block_ptr, advance, make_tensor_descriptor, atomic operations, load_tensor_descriptor, store_tensor_descriptor |
| Triton language `standard.py` | https://github.com/triton-lang/triton/blob/main/python/triton/language/standard.py | Reductions (max, min, sum, argmax, argmin, xor_sum, reduce_or), scans (cumsum, cumprod), sort, topk, bitonic_merge, ravel, swizzle2d, zeros, zeros_like, sigmoid, softmax, cdiv, flip, interleave, squeeze, unsqueeze |
| Triton language `math.py` | https://github.com/triton-lang/triton/blob/main/python/triton/language/math.py | Math ops: abs, exp, exp2, log, log2, sqrt, sqrt_rn, rsqrt, cos, sin, erf, fdiv, div_rn, ceil, floor, fma, umulhi |
| Triton top-level module | https://triton-lang.org/main/python-api/triton.html | `triton.jit`, `triton.autotune`, `triton.Config` signatures |
| Triton language API reference | https://triton-lang.org/main/python-api/triton.language.html | API descriptions, usage patterns |
| Triton Persistent Matmul tutorial | https://triton-lang.org/main/getting-started/tutorials/09-persistent-matmul.html | TMA descriptor host-side API (`TensorDescriptor` class), `desc.load()`, `desc.store()` patterns |
| Triton docs index | https://triton-lang.org/main/index.html | Module navigation structure |

## Gluon Experimental Sources

| Source | URL | Content Extracted |
|--------|-----|-------------------|
| Hopper TMA module | https://github.com/triton-lang/triton/blob/main/python/triton/experimental/gluon/language/nvidia/hopper/tma.py | `async_load`, `async_load_im2col`, `async_store`, `store_wait`, `make_tensor_descriptor`, async atomic ops, `tensor_descriptor` class |
| Hopper mbarrier module | https://github.com/triton-lang/triton/blob/main/python/triton/experimental/gluon/language/nvidia/hopper/mbarrier.py | `allocate_mbarrier`, `init`, `expect`, `arrive`, `wait`, `invalidate` |
| Hopper cluster module | https://github.com/triton-lang/triton/blob/main/python/triton/experimental/gluon/language/nvidia/hopper/cluster.py | `arrive`, `wait`, `barrier` |
| Hopper `__init__.py` | https://github.com/triton-lang/triton/blob/main/python/triton/experimental/gluon/language/nvidia/hopper/__init__.py | `warpgroup_mma`, `warpgroup_mma_wait`, `fence_async_shared`, `async_store` (shared memory variant) |
| AMD TDM module | https://github.com/triton-lang/triton/blob/main/python/triton/experimental/gluon/language/amd/gfx1250/tdm.py | `async_load`, `async_store`, `async_wait`, `async_scatter`, `async_gather`, `prefetch`, `update_tensor_descriptor` |
| Host-side TensorDescriptor | https://github.com/triton-lang/triton/blob/main/python/triton/tools/tensor_descriptor.py | `TensorDescriptor` class: `from_tensor()`, constructor parameters, `block_shape` |

## Coverage Summary

| Category | Count | Status |
|----------|-------|--------|
| `triton.language.__all__` total names | 144 | — |
| Type system / internal (skipped) | 40 | Not documented (dtype, tensor, pointer_type, etc.) |
| **Documentable public APIs** | **104** | **100% covered** |
| Gluon Experimental (Hopper TMA) | 10 | 100% covered |
| Additional extensions | 6 | autotune, config, gdc, TensorDescriptor |

## Methodology

1. Extracted the complete `__all__` list from `triton/language/__init__.py` as ground truth
2. Cross-referenced each name against Triton source files (`core.py`, `standard.py`, `math.py`) for function signatures and docstrings
3. Used official tutorial pages and API reference pages for host-side APIs
4. Filtered out type-system entries (dtype variants, pointer_type, etc.) that don't require standalone instruction docs
5. Each DOC.md follows the project's established format (YAML frontmatter + body) consistent with ascendc/, rocm/, and cuda/ entries
6. Validated all entries via `scripts/build_registry.py --validate`

## Date

Generated and reviewed: 2026-06-16