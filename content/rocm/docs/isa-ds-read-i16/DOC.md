---
name: isa-ds-read-i16
description: "Load 16 bits of signed data from a data share, sign extend to 32 bits and store the result into a vector register."
metadata:
  languages: hip
  architectures: cdna1,cdna2,cdna3,cdna4
  versions: 'CDNA4+'
  revision: 1
  updated-on: '2026-06-12'
  source: official
  tags: rocm,gpu,ds,isa,lds,memory
  isa_category: memory
  instruction_type: DS
  hw_unit: lds
  func_group: VMEM
  arch_name: AMD CDNA 4
---

# DS_READ_I16

Load 16 bits of signed data from a data share, sign extend to 32 bits and store the result into a vector register.

## Encoding

Encoding: `ENC_DS`
Opcode: `59`


## Operands

| Field | Type | Size | Direction | Implicit |
|-------|------|------|-----------|----------|
| VDST | VGPR_OR_ACCVGPR | 32bit | out | no |
| ADDR | VGPR | 32bit | in | no |
|  | DSMEM | 16bit | in | yes |


## References

- [AMD CDNA 4 ISA Reference Guide](https://www.amd.com/content/dam/amd/en/documents/instinct-tech-docs/instruction-set-architectures/)
- [AMD Machine-Readable ISA](https://gpuopen.com/machine-readable-isa/)
