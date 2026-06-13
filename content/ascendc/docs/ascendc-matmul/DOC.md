---
name: ascendc-matmul
description: Matrix multiplication via Cube unit
metadata:
  languages: ascendc
  versions: '8.0'
  revision: 1
  updated-on: '2026-06-13'
  source: official
  tags: ascend,npu,ascendc,cube,matmul,matrix
---

# Matmul

Matrix multiplication using the Cube unit.

## Syntax

```cpp
template <typename T>
class Matmul {
public:
    void Init(int32_t m, int32_t n, int32_t k);
    void Launch(LocalTensor<T>& dst, LocalTensor<T>& a, LocalTensor<T>& b);
};
```

## Description

Performs matrix multiplication using the dedicated Cube unit. The Cube unit is specialized for matrix operations and provides high-throughput matrix multiplication. Input matrices must be in NZ format (Ascend's native layout format). The Matmul API class encapsulates initialization and execution phases.

## Hardware Unit

Cube Unit

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| m | int32_t | Number of rows in matrix A and result C |
| n | int32_t | Number of columns in matrix B and result C |
| k | int32_t | Number of columns in A and rows in B (inner dimension) |
| dst | LocalTensor<T>& | Destination tensor (m × n) |
| a | LocalTensor<T>& | Left matrix (m × k) in NZ format |
| b | LocalTensor<T>& | Right matrix (k × n) in NZ format |

## Supported Data Types

- float16 (half) - primary type for Cube
- int8_t (with accumulation)

## Semantics

```pseudo
// Standard matrix multiplication
// C = A × B
for i in 0..m-1:
    for j in 0..n-1:
        sum = 0
        for p in 0..k-1:
            sum = sum + A[i][p] * B[p][j]
        C[i][j] = sum
```

## CANN Version

CANN 8.0+

## Target Architecture

Ascend NPU (Atlas series)

## Related Instructions

- [DataCopy](../ascendc-datascopy/DOC.md) - for loading matrices

## Example

```cpp
using namespace ascendc;

// Initialize Matmul for 128×128 × 128×128
Matmul<float16> matmul;
matmul.Init(128, 128, 128);

// Load matrices A and B in NZ format
LocalTensor<float16> A = A_buffer;
LocalTensor<float16> B = B_buffer;
LocalTensor<float16> C = C_buffer;

// Execute matrix multiplication
matmul.Launch(C, A, B);

// C = A × B (128 × 128)
```