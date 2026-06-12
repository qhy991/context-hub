---
name: isa-v-sqrt-f16
description: "Calculate the square root of the half-precision float input using IEEE rules and store the result into a vector register."
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

# V_SQRT_F16

Calculate the square root of the half-precision float input using IEEE rules and store the result into a vector register.

## Encoding

Encoding: `ENC_VOP1`
Opcode: `62`


## Operands

| Field | Type | Size | Direction | Implicit |
|-------|------|------|-----------|----------|
| VDST | VGPR | 16bit | out | no |
| SRC0 | SRC | 16bit | in | no |
| LITERAL | SRC | 16bit | in | no |
| VSRC0 | VGPR | 16bit | in | no |
| VSRC0 | SRC_SIMPLE | 16bit | in | no |
| SRC0 | SRC_NOLIT | 16bit | in | no |


## References

- [AMD CDNA 4 ISA Reference Guide](https://www.amd.com/content/dam/amd/en/documents/instinct-tech-docs/instruction-set-architectures/)
- [AMD Machine-Readable ISA](https://gpuopen.com/machine-readable-isa/)
