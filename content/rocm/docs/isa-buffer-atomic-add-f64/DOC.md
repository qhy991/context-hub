---
name: isa-buffer-atomic-add-f64
description: "Add a double-precision float value in the data register to a location in a buffer surface. Store the original value from buffer surface into a vector register iff the SC0 bit is set."
metadata:
  languages: hip
  architectures: cdna2,cdna3,cdna4
  versions: 'CDNA4+'
  revision: 3
  updated-on: '2026-06-12'
  source: official
  tags: rocm,gpu,buffer,isa,memory-controller,memory,atomic
  isa_category: memory
  instruction_type: MTBUF/MUBUF
  hw_unit: memory-controller
  func_group: VMEM
  arch_name: AMD CDNA 4
---

# BUFFER_ATOMIC_ADD_F64

Add a double-precision float value in the data register to a location in a buffer surface. Store the original value from buffer surface into a vector register iff the SC0 bit is set.

## Encoding

Encoding: `ENC_MUBUF`
Opcode: `79`


## Operands

| Field | Type | Size | Direction | Implicit |
|-------|------|------|-----------|----------|
| VDATA | VGPR_OR_ACCVGPR | 64bit | out | no |
| VADDR | VGPR | 64bit | in | no |
| SRSRC | SREG | 128bit | in | no |
| SOFFSET | SSRC_NOLIT | 32bit | in | no |
|  | GPUMEM | 64bit | out | yes |


## References

- [AMD CDNA 4 ISA Reference Guide](https://www.amd.com/content/dam/amd/en/documents/instinct-tech-docs/instruction-set-architectures/)
- [AMD Machine-Readable ISA](https://gpuopen.com/machine-readable-isa/)
