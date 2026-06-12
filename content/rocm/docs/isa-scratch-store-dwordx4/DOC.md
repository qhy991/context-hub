---
name: isa-scratch-store-dwordx4
description: "Store 128 bits of data from vector input registers into the scratch aperture."
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

# SCRATCH_STORE_DWORDX4

Store 128 bits of data from vector input registers into the scratch aperture.

## Encoding

Encoding: `ENC_FLAT_SCRATCH`
Opcode: `31`


## Operands

| Field | Type | Size | Direction | Implicit |
|-------|------|------|-----------|----------|
| ADDR | VGPR | 32bit | in | no |
| DATA | VGPR_OR_ACCVGPR | 128bit | in | no |
| SADDR | SREG | 32bit | in | no |
|  | GPUMEM | 128bit | out | yes |
|  | FLAT_SCRATCH | 64bit | in | yes |
|  | SDST_M0 | 32bit | in | yes |


## References

- [AMD CDNA 4 ISA Reference Guide](https://www.amd.com/content/dam/amd/en/documents/instinct-tech-docs/instruction-set-architectures/)
- [AMD Machine-Readable ISA](https://gpuopen.com/machine-readable-isa/)
