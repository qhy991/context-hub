---
name: isa-ds-read-b96-tr-b6
description: "Read 96 bits of data per lane from data share. Interpret the data as a matrix with 6 bit elements and transpose the matrix. Store the result into vector registers."
metadata:
  languages: hip
  architectures: cdna4
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

# DS_READ_B96_TR_B6

Read 96 bits of data per lane from data share. Interpret the data as a matrix with 6 bit elements and transpose the matrix. Store the result into vector registers.

## Encoding

Encoding: `ENC_DS`
Opcode: `225`


## Operands

| Field | Type | Size | Direction | Implicit |
|-------|------|------|-----------|----------|
| VDST | VGPR_OR_ACCVGPR | 96bit | out | no |
| ADDR | VGPR | 32bit | in | no |
|  | DSMEM | 96bit | in | yes |


## References

- [AMD CDNA 4 ISA Reference Guide](https://www.amd.com/content/dam/amd/en/documents/instinct-tech-docs/instruction-set-architectures/)
- [AMD Machine-Readable ISA](https://gpuopen.com/machine-readable-isa/)
