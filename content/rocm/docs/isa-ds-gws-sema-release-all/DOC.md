---
name: isa-ds-gws-sema-release-all
description: "GDS Only: The GWS resource (rid) indicated processes this opcode by updating the counter and labeling the specified resource as a semaphore."
metadata:
  languages: hip
  architectures: cdna1,cdna2,cdna3
  versions: 'CDNA3+'
  revision: 1
  updated-on: '2026-06-12'
  source: official
  tags: rocm,gpu,ds,isa,lds,memory
  isa_category: memory
  instruction_type: DS
  hw_unit: lds
  func_group: VMEM
  arch_name: AMD CDNA 3
---

# DS_GWS_SEMA_RELEASE_ALL

GDS Only: The GWS resource (rid) indicated processes this opcode by updating the counter and labeling the specified resource as a semaphore.

## Encoding

Encoding: `ENC_DS`
Opcode: `152`



## References

- [AMD CDNA 3 ISA Reference Guide](https://www.amd.com/content/dam/amd/en/documents/instinct-tech-docs/instruction-set-architectures/)
- [AMD Machine-Readable ISA](https://gpuopen.com/machine-readable-isa/)
