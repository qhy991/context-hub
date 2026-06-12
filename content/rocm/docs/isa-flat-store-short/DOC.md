---
name: isa-flat-store-short
description: "Store 16 bits of data from a vector register into the flat aperture."
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

# FLAT_STORE_SHORT

Store 16 bits of data from a vector register into the flat aperture.

## Encoding

Encoding: `ENC_FLAT`
Opcode: `26`


## Operands

| Field | Type | Size | Direction | Implicit |
|-------|------|------|-----------|----------|
| ADDR | VGPR | 64bit | in | no |
| DATA | VGPR_OR_ACCVGPR | 32bit | in | no |
|  | GPUMEM | 16bit | out | yes |
|  | FLAT_SCRATCH | 64bit | in | yes |
|  | SDST_M0 | 32bit | in | yes |


## References

- [AMD CDNA 4 ISA Reference Guide](https://www.amd.com/content/dam/amd/en/documents/instinct-tech-docs/instruction-set-architectures/)
- [AMD Machine-Readable ISA](https://gpuopen.com/machine-readable-isa/)
