---
name: isa-ds-ordered-count
description: "GDS-only. Add (count_bits(exec_mask)) to one of 4 dedicated ordered-count counters (aka 'packers'). Additional bits of instr.offset field are overloaded to hold packer-id, 'last'."
metadata:
  languages: hip
  architectures: cdna1
  versions: 'CDNA1+'
  revision: 1
  updated-on: '2026-06-12'
  source: official
  tags: rocm,gpu,ds,isa,lds,memory
  isa_category: memory
  instruction_type: DS
  hw_unit: lds
  func_group: VMEM
  arch_name: AMD CDNA 1
---

# DS_ORDERED_COUNT

GDS-only. Add (count_bits(exec_mask)) to one of 4 dedicated ordered-count counters (aka 'packers'). Additional bits of instr.offset field are overloaded to hold packer-id, 'last'.

## Encoding

Encoding: `ENC_DS`
Opcode: `191`


## Operands

| Field | Type | Size | Direction | Implicit |
|-------|------|------|-----------|----------|
| VDST | VGPR | 32bit | out | no |
| ADDR | VGPR | 32bit | in | no |
|  | DSMEM | 32bit | out | yes |
|  | SDST_M0 | 32bit | in | yes |


## References

- [AMD CDNA 1 ISA Reference Guide](https://www.amd.com/content/dam/amd/en/documents/instinct-tech-docs/instruction-set-architectures/)
- [AMD Machine-Readable ISA](https://gpuopen.com/machine-readable-isa/)
