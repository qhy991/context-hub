---
name: isa-tbuffer-store-format-d16-xyzw
description: "Convert 64 bits of data from vector input registers into 4-component formatted data and store the data into a buffer surface. The instruction specifies the data format of the surface, overriding the resource descriptor."
metadata:
  languages: hip
  architectures: cdna1,cdna2,cdna3,cdna4
  versions: 'CDNA4+'
  revision: 1
  updated-on: '2026-06-12'
  source: official
  tags: rocm,gpu,tbuffer,isa,unknown,unknown
  isa_category: unknown
  instruction_type: unknown
  hw_unit: unknown
  func_group: VMEM
  arch_name: AMD CDNA 4
---

# TBUFFER_STORE_FORMAT_D16_XYZW

Convert 64 bits of data from vector input registers into 4-component formatted data and store the data into a buffer surface. The instruction specifies the data format of the surface, overriding the resource descriptor.

## Encoding

Encoding: `ENC_MTBUF`
Opcode: `15`


## Operands

| Field | Type | Size | Direction | Implicit |
|-------|------|------|-----------|----------|
| VDATA | VGPR_OR_ACCVGPR | 64bit | in | no |
| VADDR | VGPR | 64bit | in | no |
| SRSRC | SREG | 128bit | in | no |
| SOFFSET | SSRC_NOLIT | 32bit | in | no |
|  | GPUMEM | 128bit | out | yes |


## References

- [AMD CDNA 4 ISA Reference Guide](https://www.amd.com/content/dam/amd/en/documents/instinct-tech-docs/instruction-set-architectures/)
- [AMD Machine-Readable ISA](https://gpuopen.com/machine-readable-isa/)
