---
name: isa-tbuffer-load-format-d16-xyzw
description: "Load 4-component formatted data from a buffer surface, convert the data to packed 16 bit integral or floating point format, then store the result into a vector register. The instruction specifies the data format of the surface, overriding the resource descriptor."
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

# TBUFFER_LOAD_FORMAT_D16_XYZW

Load 4-component formatted data from a buffer surface, convert the data to packed 16 bit integral or floating point format, then store the result into a vector register. The instruction specifies the data format of the surface, overriding the resource descriptor.

## Encoding

Encoding: `ENC_MTBUF`
Opcode: `11`


## Operands

| Field | Type | Size | Direction | Implicit |
|-------|------|------|-----------|----------|
| VDATA | VGPR_OR_ACCVGPR | 64bit | out | no |
| VADDR | VGPR | 64bit | in | no |
| SRSRC | SREG | 128bit | in | no |
| SOFFSET | SSRC_NOLIT | 32bit | in | no |
|  | GPUMEM | 128bit | in | yes |


## References

- [AMD CDNA 4 ISA Reference Guide](https://www.amd.com/content/dam/amd/en/documents/instinct-tech-docs/instruction-set-architectures/)
- [AMD Machine-Readable ISA](https://gpuopen.com/machine-readable-isa/)
