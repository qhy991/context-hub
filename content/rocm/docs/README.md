# ROCm Content for context-hub

GPU instruction, API, and optimization documentation for AMD ROCm / CDNA architectures.

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

## Directory Structure

```
content/rocm/docs/
├── isa-v-mfma-*          # MFMA matrix instructions
├── isa-v-mov-dpp         # DPP cross-lane operations
├── isa-ds-read*          # LDS read instructions
├── hip-hipMalloc         # HIP Runtime API
├── opt-bank-conflict*    # Optimization guides
└── arch-cdna4-*          # Architecture features
```

## Ingesting New Content

### From Machine-Readable ISA XML

```bash
# Download XML from https://gpuopen.com/machine-readable-isa/
# Then run:
python3 scripts/rocm/parse_isa_xml.py \
    --xml ~/Downloads/amdgpu_isa_cdna4.xml \
    --outdir content/rocm/docs
```

### From HIP API Documentation

```bash
# TODO: Add Doxygen scraper script
# python3 scripts/rocm/scrape_hip_api.py --url https://rocm.docs.amd.com/...
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
```

## See Also

- [ROCm Documentation](https://rocm.docs.amd.com/)
- [AMD Machine-Readable ISA](https://gpuopen.com/machine-readable-isa/)
- [Composable Kernel Library](https://github.com/ROCm/composable_kernel)
- [ROCm-KernelWiki-Q](https://github.com/user/ROCm-KernelWiki-Q) — Knowledge graph companion
