---
name: isa-image-sample-d-o
description: "Sample texels from an image surface using texel coordinates provided by the address input registers and store the result into vector registers. Additional data for user derivatives, user offsets are provided by the address registers."
metadata:
  languages: hip
  architectures: cdna1
  versions: 'CDNA1+'
  revision: 1
  updated-on: '2026-06-12'
  source: official
  tags: rocm,gpu,image,isa
  isa_category: memory
  instruction_type: MIMG
  hw_unit: texture-unit
  func_group: VMEM
  arch_name: AMD CDNA 1
---

# IMAGE_SAMPLE_D_O

Sample texels from an image surface using texel coordinates provided by the address input registers and store the result into vector registers. Additional data for user derivatives, user offsets are provided by the address registers.

## Encoding

Encoding: `ENC_MIMG`
Opcode: `50`


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
