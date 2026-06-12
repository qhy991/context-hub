---
name: isa-global-load-dwordx2
description: "Load 64 bits of data from the global aperture into a vector register."
metadata:
  languages: hip
  architectures: cdna1,cdna2,cdna3,cdna4
  versions: 'CDNA4+'
  revision: 1
  updated-on: '2026-06-12'
  source: official
  tags: rocm,gpu,global,isa,memory-controller,memory
  isa_category: memory
  instruction_type: GLOBAL
  hw_unit: memory-controller
  func_group: VMEM
  arch_name: AMD CDNA 4
---

# GLOBAL_LOAD_DWORDX2

Load 64 bits of data from the global aperture into a vector register.

## Encoding

Encoding: `ENC_FLAT_GLBL`
Opcode: `21`


## Operands

| Field | Type | Size | Direction | Implicit |
|-------|------|------|-----------|----------|
| VDST | VGPR_OR_ACCVGPR | 64bit | out | no |
| ADDR | VGPR | 64bit | in | no |
| SADDR | SREG | 64bit | in | no |
|  | GPUMEM | 64bit | in | yes |
|  | SDST_M0 | 32bit | in | yes |


## References

- [AMD CDNA 4 ISA Reference Guide](https://www.amd.com/content/dam/amd/en/documents/instinct-tech-docs/instruction-set-architectures/)
- [AMD Machine-Readable ISA](https://gpuopen.com/machine-readable-isa/)
