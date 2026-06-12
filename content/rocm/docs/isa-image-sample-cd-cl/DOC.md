---
name: isa-image-sample-cd-cl
description: "Sample texels from an image surface using texel coordinates provided by the address input registers and store the result into vector registers. Additional data for coarse derivatives, LOD clamp are provided by the address registers."
metadata:
  languages: hip
  architectures: cdna1
  versions: 'CDNA1+'
  revision: 1
  updated-on: '2026-06-12'
  source: official
  tags: rocm,gpu,image,isa,unknown,unknown
  isa_category: unknown
  instruction_type: unknown
  hw_unit: unknown
  func_group: VMEM
  arch_name: AMD CDNA 1
---

# IMAGE_SAMPLE_CD_CL

Sample texels from an image surface using texel coordinates provided by the address input registers and store the result into vector registers. Additional data for coarse derivatives, LOD clamp are provided by the address registers.

## Encoding

Encoding: `ENC_MIMG`
Opcode: `105`


## Operands

| Field | Type | Size | Direction | Implicit |
|-------|------|------|-----------|----------|
| VDATA | VGPR | 128bit | out | no |
| VADDR | VGPR | 320bit | in | no |
| SRSRC | SREG | 256bit | in | no |
| SSAMP | SREG | 128bit | in | no |


## References

- [AMD CDNA 1 ISA Reference Guide](https://www.amd.com/content/dam/amd/en/documents/instinct-tech-docs/instruction-set-architectures/)
- [AMD Machine-Readable ISA](https://gpuopen.com/machine-readable-isa/)
