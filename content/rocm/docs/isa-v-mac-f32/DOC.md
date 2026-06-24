---
name: isa-v-mac-f32
description: "Multiply two floating point inputs and accumulate the result into the destination register."
metadata:
  languages: hip
  architectures: cdna1,cdna2
  versions: 'CDNA2+'
  revision: 2
  updated-on: '2026-06-12'
  source: official
  tags: rocm,gpu,v,isa,simd-unit,compute
  isa_category: compute
  instruction_type: VOP
  hw_unit: simd-unit
  func_group: VALU
  arch_name: AMD CDNA 2
---

# V_MAC_F32

Multiply two floating point inputs and accumulate the result into the destination register.

## Encoding

Encoding: `ENC_VOP2`
Opcode: `22`


## Operands

| Field | Type | Size | Direction | Implicit |
|-------|------|------|-----------|----------|
| VDST | VGPR | 32bit | out | no |
| SRC0 | SRC | 32bit | in | no |
| VSRC1 | VGPR | 32bit | in | no |
| LITERAL | SRC | 32bit | in | no |
| VSRC0 | VGPR | 32bit | in | no |
| SRC0 | SRC_NOLIT | 32bit | in | no |
| SRC1 | SRC_SIMPLE | 32bit | in | no |


## References

- [AMD CDNA 2 ISA Reference Guide](https://www.amd.com/content/dam/amd/en/documents/instinct-tech-docs/instruction-set-architectures/)
- [AMD Machine-Readable ISA](https://gpuopen.com/machine-readable-isa/)

## Semantics
Vector Multiply-Add. Conceptually similar to fmac but does not guarantee fused rounding (may round the multiplication before addition depending on legacy hardware behavior, though often synonymous in modern ISAs).

## Example
```cpp
__device__ void v_mac(float& acc, float a, float b) {
    asm volatile(
        "v_mac_f32 %0, %1, %2" 
        : "+v"(acc) : "v"(a), "v"(b)
    );
}
```
