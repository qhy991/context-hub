---
name: isa-buffer-atomic-sub-x2
description: "Subtract an unsigned 64-bit integer value stored in the data register from a value stored in a location in a buffer surface. Store the original value from buffer surface into a vector register iff the SC0 bit is set."
metadata:
  languages: hip
  architectures: cdna1,cdna2,cdna3,cdna4
  versions: 'CDNA4+'
  revision: 1
  updated-on: '2026-06-12'
  source: official
  tags: rocm,gpu,buffer,isa,memory-controller,memory,atomic
  isa_category: memory
  instruction_type: MTBUF/MUBUF
  hw_unit: memory-controller
  func_group: VMEM
  arch_name: AMD CDNA 4
---

# BUFFER_ATOMIC_SUB_X2

Subtract an unsigned 64-bit integer value stored in the data register from a value stored in a location in a buffer surface. Store the original value from buffer surface into a vector register iff the SC0 bit is set.

## Encoding

Encoding: `ENC_MUBUF`
Opcode: `99`


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
