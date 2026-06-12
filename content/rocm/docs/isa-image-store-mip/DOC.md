---
name: isa-image-store-mip
description: "Store a texel from a vector register to a user-specified miplevel in an image surface. The texel data is converted using the format conversion specified by the resource descriptor prior to storage."
metadata:
  languages: hip
  architectures: cdna1,cdna2
  versions: 'CDNA2+'
  revision: 2
  updated-on: '2026-06-12'
  source: official
  tags: rocm,gpu,image,isa
  isa_category: memory
  instruction_type: MIMG
  hw_unit: texture-unit
  func_group: VMEM
  arch_name: AMD CDNA 2
---

# IMAGE_STORE_MIP

Store a texel from a vector register to a user-specified miplevel in an image surface. The texel data is converted using the format conversion specified by the resource descriptor prior to storage.

## Encoding

Encoding: `ENC_MIMG`
Opcode: `9`


## Operands

| Field | Type | Size | Direction | Implicit |
|-------|------|------|-----------|----------|
| VDATA | VGPR_OR_ACCVGPR | 128bit | in | no |
| VADDR | VGPR | 128bit | in | no |
| SRSRC | SREG | 256bit | in | no |


## References

- [AMD CDNA 2 ISA Reference Guide](https://www.amd.com/content/dam/amd/en/documents/instinct-tech-docs/instruction-set-architectures/)
- [AMD Machine-Readable ISA](https://gpuopen.com/machine-readable-isa/)
