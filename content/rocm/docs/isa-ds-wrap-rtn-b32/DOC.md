---
name: isa-ds-wrap-rtn-b32
description: "Given a minuend from a location in data share and a subtrahend from a vector register, subtract the two values iff the result is nonnegative; otherwise add a value from a second vector register to the memory location."
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

# DS_WRAP_RTN_B32

Given a minuend from a location in data share and a subtrahend from a vector register, subtract the two values iff the result is nonnegative; otherwise add a value from a second vector register to the memory location.

## Encoding

Encoding: `ENC_DS`
Opcode: `52`


## Operands

| Field | Type | Size | Direction | Implicit |
|-------|------|------|-----------|----------|
| VDST | VGPR_OR_ACCVGPR | 32bit | out | no |
| ADDR | VGPR | 32bit | in | no |
| DATA0 | VGPR_OR_ACCVGPR | 32bit | in | no |
| DATA1 | VGPR_OR_ACCVGPR | 32bit | in | no |
|  | DSMEM | 32bit | out | yes |


## References

- [AMD CDNA 4 ISA Reference Guide](https://www.amd.com/content/dam/amd/en/documents/instinct-tech-docs/instruction-set-architectures/)
- [AMD Machine-Readable ISA](https://gpuopen.com/machine-readable-isa/)
