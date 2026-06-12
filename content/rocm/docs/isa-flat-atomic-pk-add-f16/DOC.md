---
name: isa-flat-atomic-pk-add-f16
description: "Add a packed 2-component half-precision float value in the data register to a location in the flat aperture. Store the original value from flat aperture into a vector register iff the SC0 bit is set."
metadata:
  languages: hip
  architectures: cdna3,cdna4
  versions: 'CDNA4+'
  revision: 2
  updated-on: '2026-06-12'
  source: official
  tags: rocm,gpu,flat,isa,memory-controller,memory,low-precision,atomic
  isa_category: memory
  instruction_type: FLAT
  hw_unit: memory-controller
  func_group: VMEM
  arch_name: AMD CDNA 4
---

# FLAT_ATOMIC_PK_ADD_F16

Add a packed 2-component half-precision float value in the data register to a location in the flat aperture. Store the original value from flat aperture into a vector register iff the SC0 bit is set.

## Encoding

Encoding: `ENC_FLAT`
Opcode: `78`


## Operands

| Field | Type | Size | Direction | Implicit |
|-------|------|------|-----------|----------|
| VDST | VGPR_OR_ACCVGPR | 32bit | out | no |
| ADDR | VGPR | 64bit | in | no |
| DATA | VGPR_OR_ACCVGPR | 32bit | in | no |
|  | GPUMEM | 32bit | out | yes |
|  | FLAT_SCRATCH | 64bit | in | yes |
|  | SDST_M0 | 32bit | in | yes |


## References

- [AMD CDNA 4 ISA Reference Guide](https://www.amd.com/content/dam/amd/en/documents/instinct-tech-docs/instruction-set-architectures/)
- [AMD Machine-Readable ISA](https://gpuopen.com/machine-readable-isa/)
