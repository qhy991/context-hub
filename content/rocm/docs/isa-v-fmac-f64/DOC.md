---
name: isa-v-fmac-f64
description: "Multiply two floating point inputs and accumulate the result into the destination register using fused multiply add."
metadata:
  languages: hip
  architectures: cdna2,cdna3,cdna4
  versions: 'CDNA4+'
  revision: 3
  updated-on: '2026-06-12'
  source: official
  tags: rocm,gpu,v,isa,simd-unit,compute
  isa_category: compute
  instruction_type: VOP
  hw_unit: simd-unit
  func_group: VALU
  arch_name: AMD CDNA 4
---

# V_FMAC_F64

Multiply two floating point inputs and accumulate the result into the destination register using fused multiply add.

## Encoding

Encoding: `ENC_VOP2`
Opcode: `4`


## Operands

| Field | Type | Size | Direction | Implicit |
|-------|------|------|-----------|----------|
| VDST | VGPR | 64bit | out | no |
| SRC0 | SRC | 64bit | in | no |
| VSRC1 | VGPR | 64bit | in | no |
| LITERAL | SRC | 64bit | in | no |
| VSRC0 | VGPR | 64bit | in | no |
| SRC0 | SRC_NOLIT | 64bit | in | no |
| SRC1 | SRC_SIMPLE | 64bit | in | no |


## References

- [AMD CDNA 4 ISA Reference Guide](https://www.amd.com/content/dam/amd/en/documents/instinct-tech-docs/instruction-set-architectures/)
- [AMD Machine-Readable ISA](https://gpuopen.com/machine-readable-isa/)
