---
name: isa-scratch-load-dwordx2
description: "Load 64 bits of data from the scratch aperture into a vector register."
metadata:
  languages: hip
  architectures: cdna1,cdna2,cdna3,cdna4
  versions: 'CDNA4+'
  revision: 1
  updated-on: '2026-06-12'
  source: official
  tags: rocm,gpu,scratch,isa,unknown,unknown
  isa_category: unknown
  instruction_type: unknown
  hw_unit: unknown
  func_group: VMEM
  arch_name: AMD CDNA 4
---

# SCRATCH_LOAD_DWORDX2

Load 64 bits of data from the scratch aperture into a vector register.

## Encoding

Encoding: `ENC_FLAT_SCRATCH`
Opcode: `21`


## Operands

| Field | Type | Size | Direction | Implicit |
|-------|------|------|-----------|----------|
| VDST | VGPR_OR_ACCVGPR | 64bit | out | no |
| ADDR | VGPR | 32bit | in | no |
| SADDR | SREG | 32bit | in | no |
|  | FLAT_SCRATCH | 64bit | in | yes |
|  | GPUMEM | 64bit | in | yes |
|  | SDST_M0 | 32bit | in | yes |


## References

- [AMD CDNA 4 ISA Reference Guide](https://www.amd.com/content/dam/amd/en/documents/instinct-tech-docs/instruction-set-architectures/)
- [AMD Machine-Readable ISA](https://gpuopen.com/machine-readable-isa/)
