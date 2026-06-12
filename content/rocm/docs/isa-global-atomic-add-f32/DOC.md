---
name: isa-global-atomic-add-f32
description: "Add a single-precision float value in the data register to a location in the global aperture. Store the original value from global aperture into a vector register iff the SC0 bit is set."
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

# GLOBAL_ATOMIC_ADD_F32

Add a single-precision float value in the data register to a location in the global aperture. Store the original value from global aperture into a vector register iff the SC0 bit is set.

## Encoding

Encoding: `ENC_FLAT_GLBL`
Opcode: `77`


## Operands

| Field | Type | Size | Direction | Implicit |
|-------|------|------|-----------|----------|
| VDST | VGPR_OR_ACCVGPR | 32bit | out | no |
| ADDR | VGPR | 64bit | in | no |
| DATA | VGPR_OR_ACCVGPR | 32bit | in | no |
| SADDR | SREG | 64bit | in | no |
|  | GPUMEM | 32bit | out | yes |
|  | SDST_M0 | 32bit | in | yes |


## References

- [AMD CDNA 4 ISA Reference Guide](https://www.amd.com/content/dam/amd/en/documents/instinct-tech-docs/instruction-set-architectures/)
- [AMD Machine-Readable ISA](https://gpuopen.com/machine-readable-isa/)
