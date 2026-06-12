---
name: isa-image-atomic-umax
description: "Select the maximum of two unsigned 32-bit integer inputs, given two values stored in the data register and a location in an image surface. Update the image surface with the selected value. Store the original value from image surface into a vector register iff the GLC bit is set."
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

# IMAGE_ATOMIC_UMAX

Select the maximum of two unsigned 32-bit integer inputs, given two values stored in the data register and a location in an image surface. Update the image surface with the selected value. Store the original value from image surface into a vector register iff the GLC bit is set.

## Encoding

Encoding: `ENC_MIMG`
Opcode: `23`


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
