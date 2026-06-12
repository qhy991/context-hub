---
name: isa-v-fma-f16
description: "Multiply two half-precision float inputs and add a third input using fused multiply add, and store the result into a vector register."
metadata:
  languages: hip
  architectures: cdna1,cdna2,cdna3,cdna4
  versions: 'CDNA4+'
  revision: 1
  updated-on: '2026-06-12'
  source: official
  tags: rocm,gpu,v,isa,simd-unit,compute,low-precision
  isa_category: compute
  instruction_type: VOP
  hw_unit: simd-unit
  func_group: VALU
  arch_name: AMD CDNA 4
---

# V_FMA_F16

Multiply two half-precision float inputs and add a third input using fused multiply add, and store the result into a vector register.

## Encoding

Encoding: `ENC_VOP3`
Opcode: `518`


## Operands

| Field | Type | Size | Direction | Implicit |
|-------|------|------|-----------|----------|
| VDST | VGPR | 16bit | out | no |
| SRC0 | SRC_NOLIT | 16bit | in | no |
| SRC1 | SRC_SIMPLE | 16bit | in | no |
| SRC2 | SRC_SIMPLE | 16bit | in | no |


## References

- [AMD CDNA 4 ISA Reference Guide](https://www.amd.com/content/dam/amd/en/documents/instinct-tech-docs/instruction-set-architectures/)
- [AMD Machine-Readable ISA](https://gpuopen.com/machine-readable-isa/)
