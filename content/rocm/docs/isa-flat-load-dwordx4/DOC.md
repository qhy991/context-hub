---
name: isa-flat-load-dwordx4
description: "Load 128 bits of data from the flat aperture into a vector register."
metadata:
  languages: hip
  architectures: cdna1,cdna2,cdna3,cdna4
  versions: 'CDNA4+'
  revision: 1
  updated-on: '2026-06-12'
  source: official
  tags: rocm,gpu,flat,isa,memory-controller,memory
  isa_category: memory
  instruction_type: FLAT
  hw_unit: memory-controller
  func_group: VMEM
  arch_name: AMD CDNA 4
---

# FLAT_LOAD_DWORDX4

Load 128 bits of data from the flat aperture into a vector register.

## Encoding

Encoding: `ENC_FLAT`
Opcode: `23`


## Operands

| Field | Type | Size | Direction | Implicit |
|-------|------|------|-----------|----------|
| VDST | VGPR_OR_ACCVGPR | 128bit | out | no |
| ADDR | VGPR | 64bit | in | no |
|  | FLAT_SCRATCH | 64bit | in | yes |
|  | GPUMEM | 128bit | in | yes |
|  | SDST_M0 | 32bit | in | yes |


## References

- [AMD CDNA 4 ISA Reference Guide](https://www.amd.com/content/dam/amd/en/documents/instinct-tech-docs/instruction-set-architectures/)
- [AMD Machine-Readable ISA](https://gpuopen.com/machine-readable-isa/)
