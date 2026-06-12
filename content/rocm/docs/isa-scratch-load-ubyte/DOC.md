---
name: isa-scratch-load-ubyte
description: "Load 8 bits of unsigned data from the scratch aperture, zero extend to 32 bits and store the result into a vector register."
metadata:
  languages: hip
  architectures: cdna1,cdna2,cdna3,cdna4
  versions: 'CDNA4+'
  revision: 4
  updated-on: '2026-06-12'
  source: official
  tags: rocm,gpu,scratch,isa
  isa_category: memory
  instruction_type: DS
  hw_unit: lds
  func_group: VMEM
  arch_name: AMD CDNA 4
---

# SCRATCH_LOAD_UBYTE

Load 8 bits of unsigned data from the scratch aperture, zero extend to 32 bits and store the result into a vector register.

## Encoding

Encoding: `ENC_FLAT_SCRATCH`
Opcode: `16`


## Operands

| Field | Type | Size | Direction | Implicit |
|-------|------|------|-----------|----------|
| VDST | VGPR_OR_ACCVGPR | 32bit | out | no |
| ADDR | VGPR | 32bit | in | no |
| SADDR | SREG | 32bit | in | no |
|  | FLAT_SCRATCH | 64bit | in | yes |
|  | GPUMEM | 8bit | in | yes |
|  | SDST_M0 | 32bit | in | yes |


## References

- [AMD CDNA 4 ISA Reference Guide](https://www.amd.com/content/dam/amd/en/documents/instinct-tech-docs/instruction-set-architectures/)
- [AMD Machine-Readable ISA](https://gpuopen.com/machine-readable-isa/)
