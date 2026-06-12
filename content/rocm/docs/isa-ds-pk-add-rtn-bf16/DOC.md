---
name: isa-ds-pk-add-rtn-bf16
description: "Add a packed 2-component BF16 float value in the data register to a location in a data share. Store the original value from data share into a vector register."
metadata:
  languages: hip
  architectures: cdna1,cdna2,cdna3,cdna4
  versions: 'CDNA4+'
  revision: 1
  updated-on: '2026-06-12'
  source: official
  tags: rocm,gpu,ds,isa,lds,memory,low-precision
  isa_category: memory
  instruction_type: DS
  hw_unit: lds
  func_group: VMEM
  arch_name: AMD CDNA 4
---

# DS_PK_ADD_RTN_BF16

Add a packed 2-component BF16 float value in the data register to a location in a data share. Store the original value from data share into a vector register.

## Encoding

Encoding: `ENC_DS`
Opcode: `184`


## Operands

| Field | Type | Size | Direction | Implicit |
|-------|------|------|-----------|----------|
| VDST | VGPR_OR_ACCVGPR | 32bit | out | no |
| ADDR | VGPR | 32bit | in | no |
| DATA0 | VGPR_OR_ACCVGPR | 32bit | in | no |
|  | DSMEM | 32bit | out | yes |


## References

- [AMD CDNA 4 ISA Reference Guide](https://www.amd.com/content/dam/amd/en/documents/instinct-tech-docs/instruction-set-architectures/)
- [AMD Machine-Readable ISA](https://gpuopen.com/machine-readable-isa/)
