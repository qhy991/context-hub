---
name: isa-ds-read-b32
description: "Load 32 bits of data from a data share into a vector register."
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

# DS_READ_B32

Load 32 bits of data from a data share into a vector register.

## Encoding

Encoding: `ENC_DS`
Opcode: `54`


## Operands

| Field | Type | Size | Direction | Implicit |
|-------|------|------|-----------|----------|
| VDST | VGPR_OR_ACCVGPR | 32bit | out | no |
| ADDR | VGPR | 32bit | in | no |
|  | DSMEM | 32bit | in | yes |


## References

- [AMD CDNA 4 ISA Reference Guide](https://www.amd.com/content/dam/amd/en/documents/instinct-tech-docs/instruction-set-architectures/)
- [AMD Machine-Readable ISA](https://gpuopen.com/machine-readable-isa/)

## Semantics
Reads a 32-bit (dword) value from Local Data Share (LDS). Uses an address specified in a VGPR and an optional immediate offset. The LDS is the shared memory on AMD GPUs, characterized by high bandwidth and low latency, mapped into a single compute unit.

## Example
```cpp
// Using inline assembly to perform LDS read
__device__ float read_lds(uint32_t lds_offset) {
    float val;
    asm volatile(
        "ds_read_b32 %0, %1 offset:0" 
        : "=v"(val) : "v"(lds_offset)
    );
    return val;
}
```
