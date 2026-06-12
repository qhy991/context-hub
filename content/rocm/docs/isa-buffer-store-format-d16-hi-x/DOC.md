---
name: isa-buffer-store-format-d16-hi-x
description: "Convert 16 bits of data from the high 16 bits of a 32-bit vector input register into 1-component formatted data and store the data into a buffer surface. The instruction specifies the data format of the surface, overriding the resource descriptor."
metadata:
  languages: hip
  architectures: cdna1,cdna2,cdna3,cdna4
  versions: 'CDNA4+'
  revision: 1
  updated-on: '2026-06-12'
  source: official
  tags: rocm,gpu,buffer,isa,memory-controller,memory
  isa_category: memory
  instruction_type: MTBUF/MUBUF
  hw_unit: memory-controller
  func_group: VMEM
  arch_name: AMD CDNA 4
---

# BUFFER_STORE_FORMAT_D16_HI_X

Convert 16 bits of data from the high 16 bits of a 32-bit vector input register into 1-component formatted data and store the data into a buffer surface. The instruction specifies the data format of the surface, overriding the resource descriptor.

## Encoding

Encoding: `ENC_MUBUF`
Opcode: `39`


## Operands

| Field | Type | Size | Direction | Implicit |
|-------|------|------|-----------|----------|
| VDATA | VGPR_OR_ACCVGPR | 32bit | in | no |
| VADDR | VGPR | 64bit | in | no |
| SRSRC | SREG | 128bit | in | no |
| SOFFSET | SSRC_NOLIT | 32bit | in | no |
|  | GPUMEM | 32bit | out | yes |


## References

- [AMD CDNA 4 ISA Reference Guide](https://www.amd.com/content/dam/amd/en/documents/instinct-tech-docs/instruction-set-architectures/)
- [AMD Machine-Readable ISA](https://gpuopen.com/machine-readable-isa/)
