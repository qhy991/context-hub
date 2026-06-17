---
name: triton-proton
description: Profile Triton kernels with the Proton profiler (per-line / per-SASS attribution)
metadata:
  languages: triton
  versions: '2.1'
  revision: 1
  updated-on: '2026-06-17'
  source: official
  tags: triton,gpu,profiling,proton,performance,tooling,command-line
---

# proton — profiling Triton kernels

`proton` is Triton's native profiler (ships with Triton). It produces per-kernel,
and optionally per-line/per-instruction, timing and hardware-counter attribution
for `@triton.jit` kernels — the profiling counterpart to a CPU profiler, but for
GPU kernels written in Triton.

## When to use it

- A Triton kernel is slower than its roofline predicts and you need to know
  *where* (memory stall? low occupancy? tensor-core underuse?).
- You want to attribute cycles back to specific `tl.*` lines or SASS rather than
  whole-kernel averages.
- You are autotuning and want to compare configs with hard counter data, not just
  wall-clock.

## Syntax (Python API)

```python
from triton.profiler import proton

proton.start()
# ... run the kernel many times (warmup + measurement) ...
proton.stop()

proton.profile_dir = "./profiles"            # where artifacts are written
proton.print()                                # human-readable summary
```

## Command-line usage

Profile a script end-to-end and dump a `.json` / SQLite trace:

```bash
# Basic: profile `python train.py`, write a profile under the current dir
python -m triton.profiler.viewer --profile -- python train.py

# Profile a single function in a module
python -m triton.profiler.viewer --profile train.py:train_step

# Open the interactive viewer over an existing profile
python -m triton.profiler.viewer profile.json
```

## What it captures

| Surface | Notes |
|---------|-------|
| Per-kernel time | wall time + launch count |
| Hardware counters | SM throughput, DRAM bytes, tensor-core activity, stall reasons (where supported) |
| Source attribution | maps counters to `tl.*` lines / SASS when profiling in that mode |
| Triton-specific metadata | grid, num_warps, num_stages, config from `triton.autotune` |

## Common pitfalls

- **Warm up first.** Profile after compilation + autotuning have settled, or you
  measure the compile/autotune cost, not the kernel.
- **`TRITON_INTERPRET` must be off.** Interpret mode runs on CPU and produces no
  useful GPU profile (see [triton-env-vars](../triton-env-vars/DOC.md)).
- **Overhead scales with attribution depth.** Per-line/per-SASS is far more
  expensive than per-kernel; use the coarse mode first.
- **Counter availability is hardware-dependent.** Some stall reasons / tensor-core
  counters need specific SM architectures.

## Triton Version

Triton 2.1+ (proton API stabilized in the 2.x line; CLI flags vary slightly by
point release — check `python -m triton.profiler.viewer --help`).

## Target Architecture

NVIDIA GPU (SM 7.0+; best on SM 8.0+), AMD GPU (limited).

## Related Instructions

- [triton.autotune](../triton-autotune/DOC.md)
- [triton-env-vars](../triton-env-vars/DOC.md)
- [triton-opt](../triton-opt/DOC.md)

## Example

```python
from triton.profiler import proton
import torch, triton, triton.language as tl

@triton.autotune(configs=[triton.Config({'BM':128,'BN':128}, num_warps=8)], key=['M','N'])
@triton.jit
def k(...): ...

# warm up + autotune
for _ in range(3):
    k(...)

proton.start()
for _ in range(50):
    k(...)
proton.stop()
proton.print()
```
