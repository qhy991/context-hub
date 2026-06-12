---
name: isa-image-load-mip-pck
description: "Load a texel from a user-specified miplevel in an image surface and store the result into a vector register. 8- and 16-bit components are zero-extended. The format specified in the resource descriptor is ignored. No sampling is performed."
metadata:
  languages: hip
  architectures: cdna1,cdna2
  versions: 'CDNA2+'
  revision: 1
  updated-on: '2026-06-12'
  source: official
  tags: rocm,gpu,image,isa,unknown,unknown
  isa_category: unknown
  instruction_type: unknown
  hw_unit: unknown
  func_group: VMEM
  arch_name: AMD CDNA 2
---

# IMAGE_LOAD_MIP_PCK

Load a texel from a user-specified miplevel in an image surface and store the result into a vector register. 8- and 16-bit components are zero-extended. The format specified in the resource descriptor is ignored. No sampling is performed.

## Encoding

Encoding: `ENC_MIMG`
Opcode: `4`


## Operands

| Field | Type | Size | Direction | Implicit |
|-------|------|------|-----------|----------|
| VDATA | VGPR_OR_ACCVGPR | 128bit | out | no |
| VADDR | VGPR | 128bit | in | no |
| SRSRC | SREG | 256bit | in | no |


## References

- [AMD CDNA 2 ISA Reference Guide](https://www.amd.com/content/dam/amd/en/documents/instinct-tech-docs/instruction-set-architectures/)
- [AMD Machine-Readable ISA](https://gpuopen.com/machine-readable-isa/)
