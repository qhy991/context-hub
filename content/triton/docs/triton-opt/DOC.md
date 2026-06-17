---
name: triton-opt
description: Inspect and lower Triton kernels through their IR passes (TTIR/TTGIR/MLIR)
metadata:
  languages: triton
  versions: '2.1'
  revision: 1
  updated-on: '2026-06-17'
  source: official
  tags: triton,gpu,compiler,ir,mlir,debug,tooling,command-line
---

# triton-opt — inspect Triton IR / lowering passes

`triton-opt` is the MLIR-based optimizer/inspector that ships with Triton. It
runs individual compiler passes on a Triton MLIR module so you can see exactly how
a `@triton.jit` kernel lowers from TTIR → TTGIR → (LLVMIR/PTX). It is the primary
tool for debugging *why* a kernel generates the PTX/SASS it does — register
pressure, shared-memory layout, num_warps/num_stages effects — without launching
on a GPU.

## When to use it

- A kernel is correct but slower than expected and you suspect the generated code
  (e.g. spills, a missed fusion, wrong tiling in IR).
- You want to see the effect of `num_warps`, `num_stages`, or a `tl.*` rewrite on
  the lowered IR without a full run.
- You are writing a compiler-aware kernel and need to read TTIR/TTGIR directly.

## Syntax

```bash
# Dump all lowering passes on a Triton IR module
triton-opt --default-kernel-options "num_warps=4" module.mlir

# Run a specific pass and print the result
triton-opt --convert-triton-to-llvmir module.mlir

# Get IR out of a real kernel instead of hand-writing MLIR:
# set TRITON_KERNEL_DUMP_DIR (see triton-env-vars), then feed the dumped .ttir
```

## Producing IR from a real kernel

```bash
export TRITON_KERNEL_DUMP_DIR=/tmp/ir
python run_kernel.py        # writes *.ttir, *.ttgir, *.ll, *.ptx under /tmp/ir
ls /tmp/ir
# Then inspect / transform with triton-opt:
triton-opt /tmp/ir/<kernel>.ttgir
```

## Common passes to inspect

| Pass / IR | Tells you |
|-----------|-----------|
| `.ttir` (TTIR) | The high-level block/`tl.*` form — closest to what you wrote. |
| `.ttgir` (TTGIR) | GPU-shape: warps, shared memory, num_stages pipelining. |
| `--tritongpu-pipeline` | Software-pipelining / async-cp decisions. |
| `--tritongpu-optimize-thread-locality` / occupancy passes | Register/occupancy trade-offs. |
| `.ll` / `.ptx` | Final lowered code; compare against [proton](../triton-proton/DOC.md) hotspots. |

## Common pitfalls

- `num_warps` / `num_stages` are passed as kernel options, not inferred from the
  IR — supply them explicitly (`--default-kernel-options`) or they default and
  the output won't match your runtime kernel.
- IR is point-release-sensitive. A `.ttgir` dumped under one Triton version may
  not round-trip through `triton-opt` on another.
- Reading IR is the slow path; reach for it only when [proton](../triton-proton/DOC.md)
  points at a specific region you need to explain.

## Triton Version

Triton 2.1+ (pass names evolve across releases; `triton-opt --help` lists the
passes available in your install).

## Target Architecture

NVIDIA GPU (SM 7.0+), AMD GPU (the IR is architecture-neutral; final lowering is
backend-specific).

## Related Instructions

- [triton-env-vars](../triton-env-vars/DOC.md)
- [triton-proton](../triton-proton/DOC.md)

## Example

```bash
# Dump IR for a kernel, then read the GPU-shape (TTGIR) to see pipelining.
TRITON_KERNEL_DUMP_DIR=/tmp/ir python matmul_demo.py
triton-opt /tmp/ir/matmul_kernel__*.ttgir | less
# Look for: #triton_gpu.pipeline, shared-memory layouts, num_stages.
```
