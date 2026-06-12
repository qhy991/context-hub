---
name: isa-scratch-load-lds-ushort
description: "Load 16 bits of untyped data from the scratch aperture, zero extend to 32 bits and store the result into a data share."
metadata:
  languages: hip
  architectures: cdna3,cdna4
  versions: 'CDNA4+'
  revision: 2
  updated-on: '2026-06-12'
  source: official
  tags: rocm,gpu,scratch,isa
  isa_category: memory
  instruction_type: DS
  hw_unit: lds
  func_group: VMEM
  arch_name: AMD CDNA 4
---

# SCRATCH_LOAD_LDS_USHORT

Load 16 bits of untyped data from the scratch aperture, zero extend to 32 bits and store the result into a data share.

## Encoding

Encoding: `ENC_FLAT_SCRATCH`
Opcode: `40`


## Operands

| Field | Type | Size | Direction | Implicit |
|-------|------|------|-----------|----------|
| VDST | VGPR_OR_ACCVGPR | 32bit | out | no |
| ADDR | VGPR | 32bit | in | no |
| SADDR | SREG | 32bit | in | no |
|  | FLAT_SCRATCH | 64bit | in | yes |
|  | SDST_M0 | 32bit | in | yes |


## References

- [AMD CDNA 4 ISA Reference Guide](https://www.amd.com/content/dam/amd/en/documents/instinct-tech-docs/instruction-set-architectures/)
- [AMD Machine-Readable ISA](https://gpuopen.com/machine-readable-isa/)
