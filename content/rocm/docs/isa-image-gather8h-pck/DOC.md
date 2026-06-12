---
name: isa-image-gather8h-pck
description: "Gather all components of 8 texels from a 8x1 row vector on an image surface. Store the result into vector registers. The DMASK selects how many channels to write."
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

# IMAGE_GATHER8H_PCK

Gather all components of 8 texels from a 8x1 row vector on an image surface. Store the result into vector registers. The DMASK selects how many channels to write.

## Encoding

Encoding: `ENC_MIMG`
Opcode: `75`


## Operands

| Field | Type | Size | Direction | Implicit |
|-------|------|------|-----------|----------|
| VDATA | VGPR | 128bit | out | no |
| VADDR | VGPR | 96bit | in | no |
| SRSRC | SREG | 256bit | in | no |
| SSAMP | SREG | 128bit | in | no |


## References

- [AMD CDNA 1 ISA Reference Guide](https://www.amd.com/content/dam/amd/en/documents/instinct-tech-docs/instruction-set-architectures/)
- [AMD Machine-Readable ISA](https://gpuopen.com/machine-readable-isa/)
