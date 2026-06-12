---
name: isa-global-atomic-sub-x2
description: "Subtract an unsigned 64-bit integer value stored in the data register from a value stored in a location in the global aperture. Store the original value from global aperture into a vector register iff the SC0 bit is set."
metadata:
  languages: hip
  architectures: cdna1,cdna2,cdna3,cdna4
  versions: 'CDNA4+'
  revision: 1
  updated-on: '2026-06-12'
  source: official
  tags: rocm,gpu,global,isa,memory-controller,memory,atomic
  isa_category: memory
  instruction_type: GLOBAL
  hw_unit: memory-controller
  func_group: VMEM
  arch_name: AMD CDNA 4
---

# GLOBAL_ATOMIC_SUB_X2

Subtract an unsigned 64-bit integer value stored in the data register from a value stored in a location in the global aperture. Store the original value from global aperture into a vector register iff the SC0 bit is set.

## Encoding

Encoding: `ENC_FLAT_GLBL`
Opcode: `99`


## Operands

| Field | Type | Size | Direction | Implicit |
|-------|------|------|-----------|----------|
| VDST | VGPR_OR_ACCVGPR | 64bit | out | no |
| ADDR | VGPR | 64bit | in | no |
| DATA | VGPR_OR_ACCVGPR | 64bit | in | no |
| SADDR | SREG | 64bit | in | no |
|  | GPUMEM | 64bit | out | yes |
|  | SDST_M0 | 32bit | in | yes |


## References

- [AMD CDNA 4 ISA Reference Guide](https://www.amd.com/content/dam/amd/en/documents/instinct-tech-docs/instruction-set-architectures/)
- [AMD Machine-Readable ISA](https://gpuopen.com/machine-readable-isa/)
