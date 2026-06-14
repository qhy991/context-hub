---
name: arch-rdna35-unified-memory
description: "RDNA3.5 APU unified memory (gfx1151 / Ryzen AI Max+ 395): shared LPDDR5X pool, VRAM carveout vs GART/GTT, zero-copy host pointers (hipHostMalloc / hipMallocManaged), and bandwidth budgeting (~256 GB/s theoretical, ~212 GB/s measured)."
metadata:
  languages: hip
  architectures: rdna3_5
  versions: 'RDNA3.5'
  revision: 1
  updated-on: '2026-06-14'
  source: community
  tags: rocm,gpu,architecture,rdna3_5,gfx1151,apu,unified-memory,uma,gtt,gart,zero-copy,bandwidth-bound
  isa_category: architecture
  instruction_type: guide
  hw_unit: memory-controller
---

# RDNA3.5 APU Unified Memory (gfx1151)

The Ryzen AI Max+ 395 / Strix Halo APU — RDNA3.5, gfx id `gfx1151`, Radeon 8060S
iGPU (40 RDNA3.5 CUs) — has **no dedicated VRAM**. The CPU, the iGPU, and the OS
all draw from **one physical LPDDR5X pool** (Unified Memory Architecture, UMA).
"VRAM" versus "system RAM" on this part is a *mapping and accounting* distinction
inside one pool, not two physically separate memories. That single fact reshapes
how you allocate, copy, and budget bandwidth for kernels — see
[[arch-rdna35-apu]] for the broader hardware picture and [[arch-amd-395-soc]] for
the SoC-level view.

> **Provenance.** Platform identity (gfx1151, 40 CU, LPDDR5X-8000 / 256-bit /
> 256 GB/s theoretical) and the UMA / GART / GTT *model* are **VENDOR** facts
> (AMD spec; ROCm Strix Halo system-optimization page). The **achievable**
> bandwidth (~212 GB/s), CPU→GPU copy (~84 GB/s), and the example 8 GB GART +
> 110 GB GTT split are **COMMUNITY-MEASURED** (llm-tracker.info). The kernel-6.16.9
> VRAM-visibility fix is **COMMUNITY-MEASURED** (ROCm issue #5444). Where a clause
> is **INFERRED** from UMA it is labeled as such. Do not read any number here as a
> vendor *peak* unless it is marked VENDOR.

## One Pool, Two Accounting Views

The BIOS **"UMA Frame Buffer Size"** carves out a fixed block at boot that is
reported as dedicated VRAM and hidden from the OS. Everything else stays as
system RAM that the driver can map into the GPU's address space on demand. Two
driver concepts govern that mapping:

- **GART** — "the amount of platform address space (system RAM or MMIO) that can
  be mapped into the GPU virtual address space." **[VENDOR]**
- **GTT** — "the amount of system RAM that can be mapped into GPU virtual address
  spaces for user processes." The **default GTT limit is ≈ 50% of total system
  RAM.** **[VENDOR]**

When the GTT limit exceeds the BIOS VRAM carveout, the `amdgpu` driver satisfies
"VRAM" allocations from GTT (GTT-backed allocations). Because the memory is
physically shared, there is **no discrete-GPU-style VRAM-vs-system speed gap**,
and the ROCm docs note that "AI frameworks work more efficiently with GTT-backed
allocations." The practical recommendation is therefore to **keep the BIOS VRAM
reservation small** (the ROCm page gives 0.5 GB as the example) and let the driver
serve the GPU from GTT. **[VENDOR]**

| Region | What it is | How it is sized | Notes |
|--------|-----------|-----------------|-------|
| VRAM carveout | BIOS UMA Frame Buffer block, reported as dedicated VRAM, hidden from OS | BIOS "UMA Frame Buffer Size" | Keep small (example: **0.5 GB**) **[VENDOR]** |
| GART | Platform address space (sys RAM / MMIO) mappable into GPU VA | driver | Vendor definition above **[VENDOR]** |
| GTT | System RAM mappable into GPU VA for user processes | `ttm pages_limit`; default **≈ 50% of system RAM** | Preferred backing for AI frameworks **[VENDOR]** |
| Example split (128 GB box) | **8 GB GART + 110 GB GTT** | reporter's config | Example carveout, *not* a fixed spec **[COMMUNITY-MEASURED]** |

The GTT/TTM page limit is the vendor-grounded knob:
`/sys/module/ttm/parameters/pages_limit` (TTM = Translation Table Manager).
**[VENDOR]** A separate `amdgpu.gttsize` kernel-cmdline parameter circulates in
community guides but is **not** in the ROCm doc — prefer `ttm pages_limit`, and if
you must cite `gttsize` attribute it to community guides, not to AMD.

### Visibility gotcha (kernel ≤ 6.15.x)

On Linux kernels **6.15.x and earlier**, ROCm/HIP could report only **~15.5 GB**
usable to the GPU even with a large BIOS carveout (one reporter's box set to 96 GB
showed ~15.5 GB to `rocminfo` while sysfs showed the full 96 GB). The fix is a
**kernel upgrade to 6.16.9 or later** (a kernel-level UMA/HSA pool fix, not a ROCm
bug); after that the full pool becomes visible. Treat the 96 GB / 15.5 GB numbers
as that reporter's config, not a universal spec. **[COMMUNITY-MEASURED]** (ROCm
issue #5444).

## Bandwidth Budgeting

One pool also means **one bandwidth budget**, shared with the CPU. Plan kernels
against the *achievable* figure, not the theoretical peak:

| Quantity | Value | Provenance |
|----------|-------|------------|
| Theoretical (LPDDR5X-8000, 256-bit bus) | **256 GB/s** | **[VENDOR]** |
| Achievable (`rocm_bandwidth_test`) | **~212 GB/s** (~83% of theoretical) | **[COMMUNITY-MEASURED]** |
| CPU→GPU copy | **~84 GB/s** | **[COMMUNITY-MEASURED]** |
| FP16/BF16 theoretical | **59.4 TFLOPS** | **[COMMUNITY-MEASURED]** |
| FP16/BF16 measured (hipBLASLt) | **36.9 TFLOPS** | **[COMMUNITY-MEASURED]** |

For end-to-end context, community llama.cpp Llama-2-7B Q4_0 token-generation on
this part: HIP ~48.72 t/s, Vulkan ~52.22 t/s, Vulkan+FA ~52.73 t/s,
HIP+WMMA+FA ~50.88 t/s. **[COMMUNITY-MEASURED]** (llm-tracker.info).

> **Do not confuse roofline figures.** The in-house exp-amd-395 kernel profile
> uses a ~80 GB/s DDR5 number as a *working roofline-crossover assumption* (a
> sibling session instead assumed ~60 GB/s), **not** a `rocm_bandwidth_test`
> measurement. Use the community **~212 GB/s** for the APU's achievable pool
> bandwidth; reserve the ~80 GB/s value for the profile's internal bottleneck
> math. **[IN-HOUSE-MEASURED, hedge]**

## Zero-Copy and Managed Allocation (HIP)

Because there is no separate device pool, you can skip explicit `hipMemcpy`
host↔device traffic for many access patterns. Two HIP mechanisms matter:

- **`hipHostMalloc`** — pinned host memory the GPU can access directly over the
  CPU↔GPU interconnect with **no explicit copy (zero-copy)**. On a discrete GPU
  every access traverses PCIe; on this UMA APU the "device" memory *is* the same
  LPDDR5X pool, so the copy disappears — but page-table mapping, coherence, and
  cache effects still cost. By default this memory is **coherent (not GPU-cached)**;
  coherence is controllable via allocation flags and the **`HIP_HOST_COHERENT`**
  environment variable. Non-coherent host memory can be GPU-cached but cannot be
  synchronized while a kernel is running. **[VENDOR]**
- **`hipMallocManaged`** — unified/managed memory backed by **HMM (Heterogeneous
  Memory Management)**. If HMM is unsupported, managed allocation **falls back to
  system memory**; a managed-memory capability check is advised. On a UMA APU,
  managed memory and host memory resolve to the **same physical pool** — treat HMM
  here as the *HIP API mechanism*, with same-pool resolution **[INFERRED]** from
  UMA + the documented fallback, not a confirmed gfx1151 measurement. **[VENDOR]**

```cpp
#include <hip/hip_runtime.h>

// Zero-copy: pinned host memory the GPU reads directly — no hipMemcpy needed.
float *buf = nullptr;
size_t n = 1 << 20;
hipHostMalloc(&buf, n * sizeof(float), hipHostMallocDefault); // coherent by default
for (size_t i = 0; i < n; ++i) buf[i] = static_cast<float>(i);

my_kernel<<<grid, block>>>(buf, n);   // GPU dereferences the host pointer directly
hipDeviceSynchronize();
// buf is already up to date on the CPU side — no device->host copy.
hipHostFree(buf);

// Managed/unified path (capability-checked).
int managed = 0;
hipDeviceGetAttribute(&managed, hipDeviceAttributeManagedMemory, /*device=*/0);
if (managed) {
    float *m = nullptr;
    hipMallocManaged(&m, n * sizeof(float)); // same physical pool on a UMA APU
    // ... use m from CPU and GPU ...
    hipFree(m);
}
```

## Implications for Kernels

1. **Prefer zero-copy over explicit H2D/D2H copies.** There is no PCIe hop to
   amortize. A staging `hipMalloc` + `hipMemcpy` round trip mostly buys you
   page-pinning and coherence semantics you can already get from `hipHostMalloc`.
2. **The pool is shared, so CPU activity steals GPU bandwidth.** A busy CPU (or
   thermal coupling on the shared package) eats into the same ~212 GB/s the kernel
   needs. Budget for *contended* bandwidth, not the quiet-system number.
3. **Low-arithmetic-intensity kernels are bandwidth-bound here.** Decode-time
   attention and quantized GEMV starve the ALUs waiting on LPDDR5X; the lever is
   memory-traffic reduction, not ILP/occupancy. See
   [[opt-rdna-apu-flash-attention]] for the bandwidth-bound flash-attention case
   study and [[opt-rdna-apu-moe-matmul]] for the MoE quantized-matmul path that
   dominates decode.
4. **LDS spends from the same budget.** gfx1151 has 64 KB LDS per CU; trading it
   for occupancy regresses on bandwidth-bound kernels (see
   [[opt-bank-conflict-avoidance]]).
5. **Size the carveout/GTT for headroom.** Keep the BIOS VRAM reservation small
   (e.g. 0.5 GB), raise GTT via `ttm pages_limit` when a model needs more than the
   default ~50% of system RAM, and on kernels ≤ 6.15.x upgrade to 6.16.9+ so the
   full pool is actually visible to ROCm.

## See Also

- [[arch-rdna35-apu]] — the RDNA3.5 APU hardware overview (wave32, no MFMA)
- [[arch-amd-395-soc]] — Ryzen AI Max+ 395 SoC: CPU + iGPU + NPU
- [[opt-rdna-apu-flash-attention]] — bandwidth-bound flash-attention case study
- [[opt-rdna-apu-moe-matmul]] — MoE quantized matmul (the decode bottleneck)
- [[opt-bank-conflict-avoidance]] — LDS bank model
- [[opt-hip-vs-cuda-gotchas]] — portable HIP-vs-CUDA pitfalls
- [[arch-amd-gpu-families]] — RDNA vs CDNA family map

## References

- [ROCm Strix Halo system optimization (vendor)](https://rocm.docs.amd.com/en/latest/how-to/system-optimization/strixhalo.html)
- [HIP Programming Manual (vendor)](https://rocm.docs.amd.com/projects/HIP/en/docs-6.2.0/how-to/programming_manual.html)
- [ROCm issue #5444 — VRAM visibility / kernel-6.16.9 fix (community)](https://github.com/ROCm/ROCm/issues/5444)
- [llm-tracker.info — Strix Halo GPU Performance (community-measured)](https://llm-tracker.info/AMD-Strix-Halo-(Ryzen-AI-Max+-395)-GPU-Performance)
- `AKW-Exp/exp-amd-395/20260611-175052/kernel-profile.md` — in-house profile (working ~80 GB/s roofline; 64 KB LDS)
