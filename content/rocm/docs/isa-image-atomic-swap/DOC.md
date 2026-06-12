---
name: isa-image-atomic-swap
description: "Swap an unsigned 32-bit integer value in the data register with a location in an image surface. Store the original value from image surface into a vector register iff the GLC bit is set."
metadata:
  languages: hip
  architectures: cdna1,cdna2
  versions: 'CDNA2+'
  revision: 2
  updated-on: '2026-06-12'
  source: official
  tags: rocm,gpu,image,isa,atomic
  isa_category: memory
  instruction_type: MIMG
  hw_unit: texture-unit
  func_group: VMEM
  arch_name: AMD CDNA 2
---

# IMAGE_ATOMIC_SWAP

Swap an unsigned 32-bit integer value in the data register with a location in an image surface. Store the original value from image surface into a vector register iff the GLC bit is set.

## Encoding

Encoding: `ENC_MIMG`
Opcode: `16`


## Operands

| Field | Type | Size | Direction | Implicit |
|-------|------|------|-----------|----------|
| VDATA | VGPR_OR_ACCVGPR | 128bit | out | no |
| VADDR | VGPR | 128bit | in | no |
| SRSRC | SREG | 256bit | in | no |
|  | GPUMEM | 32bit | out | yes |


## References

- [AMD CDNA 2 ISA Reference Guide](https://www.amd.com/content/dam/amd/en/documents/instinct-tech-docs/instruction-set-architectures/)
- [AMD Machine-Readable ISA](https://gpuopen.com/machine-readable-isa/)
