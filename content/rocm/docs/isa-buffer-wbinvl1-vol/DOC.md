---
name: isa-buffer-wbinvl1-vol
description: "Write back and invalidate the shader L1 only for lines that are marked volatile. Returns ACK to shader."
metadata:
  languages: hip
  architectures: cdna1,cdna2
  versions: 'CDNA2+'
  revision: 2
  updated-on: '2026-06-12'
  source: official
  tags: rocm,gpu,buffer,isa,memory-controller,memory
  isa_category: memory
  instruction_type: MTBUF/MUBUF
  hw_unit: memory-controller
  func_group: VMEM
  arch_name: AMD CDNA 2
---

# BUFFER_WBINVL1_VOL

Write back and invalidate the shader L1 only for lines that are marked volatile. Returns ACK to shader.

## Encoding

Encoding: `ENC_MUBUF`
Opcode: `63`



## References

- [AMD CDNA 2 ISA Reference Guide](https://www.amd.com/content/dam/amd/en/documents/instinct-tech-docs/instruction-set-architectures/)
- [AMD Machine-Readable ISA](https://gpuopen.com/machine-readable-isa/)
