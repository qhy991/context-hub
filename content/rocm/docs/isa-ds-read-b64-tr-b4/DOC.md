---
name: isa-ds-read-b64-tr-b4
description: "Read 64 bits of data per lane from data share. Interpret the data as a matrix with 4 bit elements and transpose the matrix. Store the result into vector registers."
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

# DS_READ_B64_TR_B4

Read 64 bits of data per lane from data share. Interpret the data as a matrix with 4 bit elements and transpose the matrix. Store the result into vector registers.

## Encoding

Encoding: `ENC_DS`
Opcode: `224`


## Operands

| Field | Type | Size | Direction | Implicit |
|-------|------|------|-----------|----------|
| VDST | VGPR_OR_ACCVGPR | 64bit | out | no |
| ADDR | VGPR | 32bit | in | no |
|  | DSMEM | 64bit | in | yes |


## References

- [AMD CDNA 4 ISA Reference Guide](https://www.amd.com/content/dam/amd/en/documents/instinct-tech-docs/instruction-set-architectures/)
- [AMD Machine-Readable ISA](https://gpuopen.com/machine-readable-isa/)
