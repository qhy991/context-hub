---
name: isa-buffer-inv
description: "Invalidate CU and/or L2 cache depending on sc0 and sc1 bits. Returns ACK to shader."
metadata:
  languages: hip
  architectures: cdna1,cdna2,cdna3,cdna4
  versions: 'CDNA4+'
  revision: 1
  updated-on: '2026-06-12'
  source: official
  tags: rocm,gpu,buffer,isa,memory-controller,memory
  isa_category: memory
  instruction_type: MTBUF/MUBUF
  hw_unit: memory-controller
  func_group: VMEM
  arch_name: AMD CDNA 4
---

# BUFFER_INV

Invalidate CU and/or L2 cache depending on sc0 and sc1 bits. Returns ACK to shader.

## Encoding

Encoding: `ENC_MUBUF`
Opcode: `41`



## References

- [AMD CDNA 4 ISA Reference Guide](https://www.amd.com/content/dam/amd/en/documents/instinct-tech-docs/instruction-set-architectures/)
- [AMD Machine-Readable ISA](https://gpuopen.com/machine-readable-isa/)
