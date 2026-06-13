# ROCm Content for context-hub

GPU instruction, API, and optimization documentation for AMD ROCm — CDNA (MI100–MI350X) and RDNA3.5 APU (gfx1151) architectures.

## Coverage

| Category | Count | Source |
|----------|-------|--------|
| ISA Instructions (MFMA, DPP, DS, FLAT...) | growing | [Machine-Readable ISA XML](https://gpuopen.com/machine-readable-isa/) |
| HIP Runtime API | growing | [HIP Doxygen](https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/index.html) |
| HIP Driver API | growing | [HIP Driver Doxygen](https://rocm.docs.amd.com/projects/HIP/en/develop/doxygen/html/group___driver.html) |
| Optimization Guides | growing | [ROCm Docs](https://rocm.docs.amd.com/) |
| Architecture Features | growing | [CDNA Whitepapers](https://gpuopen.com/amd-gpu-architecture-programming-documentation/) |

## Supported Architectures

| Architecture | GFX | GPU | Matrix Cores | FP8 | Scaled MFMA |
|-------------|-----|-----|-------------|-----|-------------|
| CDNA1 | gfx908 | MI100 | ✓ | — | — |
| CDNA2 | gfx90a | MI250X | ✓ | ✓ | — |
| CDNA3 | gfx940/gfx942 | MI300X/A | ✓ (dual CMA) | ✓ | — |
| CDNA4 | gfx950 | MI350X | ✓ (dual CMA) | ✓ | ✓ |
| RDNA3.5 (APU) | gfx1151 | Ryzen AI Max+ 395 / Radeon 8060S | WMMA (no MFMA) | — | — |

> **CDNA vs RDNA3.5**: CDNA parts are HBM, wave64, Matrix-Core (MFMA). The
> RDNA3.5 APU is **unified DDR5, wave32, WMMA (no MFMA)** and behaves very
> differently — most decode kernels are DDR5-bandwidth-bound. CDNA-tuned kernels
> do not transfer; see `arch-rdna35-apu` and `opt-hip-vs-cuda-gotchas`.

## Directory Structure

```
content/rocm/docs/
├── isa-v-mfma-*          # MFMA matrix instructions
├── isa-v-mov-dpp         # DPP cross-lane operations
├── isa-ds-read*          # LDS read instructions
├── hip-hipMalloc         # HIP Runtime API
├── opt-bank-conflict*    # Optimization guides (CDNA + RDNA)
├── opt-hip-vs-cuda-*     # Portability gotchas (measured on gfx1151)
├── arch-cdna4-*          # CDNA architecture features
└── arch-rdna35-apu       # RDNA3.5 APU (gfx1151) architecture
```

## Ingesting New Content

### From Machine-Readable ISA XML

```bash
# Full CDNA ISA refresh (download + merge per-arch availability)
bash scripts/rocm/refresh_isa.sh

# Or parse a single architecture XML:
python3 scripts/rocm/parse_isa_xml.py \
    --xml /tmp/amdgpu_isa_specs/amdgpu_isa_cdna4.xml \
    --outdir content/rocm/docs
```

### From HIP API Documentation

```bash
python3 scripts/rocm/scrape_hip_api.py --outdir content/rocm/docs
python3 scripts/rocm/validate.py
```

### Build and Search

```bash
# Build registry and search index
chub build content/

# Search
chub search "mfma fp16"
chub search "lds bank conflict"
chub search "hipMalloc"

# Get specific entry
chub get rocm/isa-v-mfma-f32-16x16x16f16
```

## Frontmatter Schema Extension

ROCm entries extend the base context-hub schema with architecture-specific fields:

```yaml
metadata:
  languages: hip                    # hip | assembly | triton
  architectures: cdna3,cdna4       # cdna1 | cdna2 | cdna3 | cdna4
  isa_category: compute             # compute | memory | flow | synchronization | runtime
  instruction_type: VOP3P           # VOP1 | VOP2 | VOP3 | VOP3P | DS | FLAT | SOP
  hw_unit: matrix-core              # matrix-core | simd-unit | lds | memory-controller | scalar-unit
  symbol_kind: function             # (HIP API entries) function | typedef | enum
```

## See Also

- [ROCm Documentation](https://rocm.docs.amd.com/)
- [AMD Machine-Readable ISA](https://gpuopen.com/machine-readable-isa/)
- [Composable Kernel Library](https://github.com/ROCm/composable_kernel)
- [ROCm-KernelWiki-Q](https://github.com/qhy991/ROCm-KernelWiki-Q) — Knowledge graph companion
