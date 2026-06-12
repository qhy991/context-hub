---
name: isa-ds-write2st64-b64
description: "Store 64 bits of data from one vector input register and then 64 bits of data from a second vector input register into a data share. Treat each offset as an index and multiply by a stride of 64 elements (256 bytes) to generate an offset for each DS address."
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

# DS_WRITE2ST64_B64

Store 64 bits of data from one vector input register and then 64 bits of data from a second vector input register into a data share. Treat each offset as an index and multiply by a stride of 64 elements (256 bytes) to generate an offset for each DS address.

## Encoding

Encoding: `ENC_DS`
Opcode: `79`


## Operands

| Field | Type | Size | Direction | Implicit |
|-------|------|------|-----------|----------|
| ADDR | VGPR | 32bit | in | no |
| DATA0 | VGPR_OR_ACCVGPR | 64bit | in | no |
| DATA1 | VGPR_OR_ACCVGPR | 64bit | in | no |
|  | DSMEM | 64bit | out | yes |


## References

- [AMD CDNA 4 ISA Reference Guide](https://www.amd.com/content/dam/amd/en/documents/instinct-tech-docs/instruction-set-architectures/)
- [AMD Machine-Readable ISA](https://gpuopen.com/machine-readable-isa/)
