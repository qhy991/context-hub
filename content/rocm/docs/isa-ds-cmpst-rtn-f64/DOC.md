---
name: isa-ds-cmpst-rtn-f64
description: "Compare a double-precision float value in the data comparison register with a location in a data share, and modify the memory location with a value in the data source register if the comparison is equal."
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

# DS_CMPST_RTN_F64

Compare a double-precision float value in the data comparison register with a location in a data share, and modify the memory location with a value in the data source register if the comparison is equal.

## Encoding

Encoding: `ENC_DS`
Opcode: `113`


## Operands

| Field | Type | Size | Direction | Implicit |
|-------|------|------|-----------|----------|
| VDST | VGPR_OR_ACCVGPR | 64bit | out | no |
| ADDR | VGPR | 32bit | in | no |
| DATA0 | VGPR_OR_ACCVGPR | 64bit | in | no |
| DATA1 | VGPR_OR_ACCVGPR | 64bit | in | no |
|  | DSMEM | 64bit | out | yes |


## References

- [AMD CDNA 4 ISA Reference Guide](https://www.amd.com/content/dam/amd/en/documents/instinct-tech-docs/instruction-set-architectures/)
- [AMD Machine-Readable ISA](https://gpuopen.com/machine-readable-isa/)
