---
name: isa-ds-write-b32
description: "Store 32 bits of data from a vector input register into a data share."
metadata:
  languages: hip
  architectures: cdna1,cdna2,cdna3,cdna4
  versions: 'CDNA4+'
  revision: 4
  updated-on: '2026-06-12'
  source: official
  tags: rocm,gpu,ds,isa,lds,memory
  isa_category: memory
  instruction_type: DS
  hw_unit: lds
  func_group: VMEM
  arch_name: AMD CDNA 4
---

# DS_WRITE_B32

Store 32 bits of data from a vector input register into a data share.

## Encoding

Encoding: `ENC_DS`
Opcode: `13`


## Operands

| Field | Type | Size | Direction | Implicit |
|-------|------|------|-----------|----------|
| ADDR | VGPR | 32bit | in | no |
| DATA0 | VGPR_OR_ACCVGPR | 32bit | in | no |
|  | DSMEM | 32bit | out | yes |


## References

- [AMD CDNA 4 ISA Reference Guide](https://www.amd.com/content/dam/amd/en/documents/instinct-tech-docs/instruction-set-architectures/)
- [AMD Machine-Readable ISA](https://gpuopen.com/machine-readable-isa/)

## Semantics
Writes a 32-bit (dword) value to Local Data Share (LDS). Often used to stage global memory data into shared memory for cooperative thread block processing.

## Example
```cpp
__device__ void write_lds(uint32_t lds_offset, float val) {
    asm volatile(
        "ds_write_b32 %0, %1 offset:0" 
        : : "v"(lds_offset), "v"(val)
    );
}
```
