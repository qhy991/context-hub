---
name: isa-ds-gws-barrier
description: "GDS Only: The GWS resource indicated processes this opcode by queueing it until barrier is satisfied. The number of waves needed is passed in as DATA of first valid thread."
metadata:
  languages: hip
  architectures: cdna1,cdna2,cdna3
  versions: 'CDNA3+'
  revision: 3
  updated-on: '2026-06-12'
  source: official
  tags: rocm,gpu,ds,isa,lds,memory
  isa_category: memory
  instruction_type: DS
  hw_unit: lds
  func_group: VMEM
  arch_name: AMD CDNA 3
---

# DS_GWS_BARRIER

GDS Only: The GWS resource indicated processes this opcode by queueing it until barrier is satisfied. The number of waves needed is passed in as DATA of first valid thread.

## Encoding

Encoding: `ENC_DS`
Opcode: `157`


## Operands

| Field | Type | Size | Direction | Implicit |
|-------|------|------|-----------|----------|
| ADDR | VGPR | 32bit | in | no |


## References

- [AMD CDNA 3 ISA Reference Guide](https://www.amd.com/content/dam/amd/en/documents/instinct-tech-docs/instruction-set-architectures/)
- [AMD Machine-Readable ISA](https://gpuopen.com/machine-readable-isa/)
