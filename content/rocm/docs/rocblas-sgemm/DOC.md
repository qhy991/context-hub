---
name: rocblas-sgemm
description: Single precision general matrix-matrix multiplication in rocBLAS
metadata:
  languages: cpp,hip
  versions: '6.0'
  revision: 1
  updated-on: '2026-06-14'
  source: official
  tags: rocm,amd,hip,rocblas,gemm,math
---

# rocblas_sgemm

Performs a single precision general matrix-matrix multiplication.

## Syntax

```cpp
rocblas_status rocblas_sgemm(rocblas_handle handle,
                             rocblas_operation transA,
                             rocblas_operation transB,
                             rocblas_int m,
                             rocblas_int n,
                             rocblas_int k,
                             const float* alpha,
                             const float* A,
                             rocblas_int lda,
                             const float* B,
                             rocblas_int ldb,
                             const float* beta,
                             float* C,
                             rocblas_int ldc);
```

## Description

`rocblas_sgemm` performs the matrix-matrix operation:
`C = alpha * op(A) * op(B) + beta * C`
where `op(X)` is either `op(X) = X` or `op(X) = X^T`.

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| handle | rocblas_handle | Handle to the rocBLAS library context |
| transA | rocblas_operation | Specifies the operation applied to A (e.g., rocblas_operation_none, rocblas_operation_transpose) |
| transB | rocblas_operation | Specifies the operation applied to B |
| m | rocblas_int | Number of rows of matrix op(A) and C |
| n | rocblas_int | Number of columns of matrix op(B) and C |
| k | rocblas_int | Number of columns of op(A) and rows of op(B) |
| alpha | const float* | Scalar multiplier for A*B |
| A | const float* | Pointer to matrix A |
| lda | rocblas_int | Leading dimension of A |
| B | const float* | Pointer to matrix B |
| ldb | rocblas_int | Leading dimension of B |
| beta | const float* | Scalar multiplier for C |
| C | float* | Pointer to matrix C |
| ldc | rocblas_int | Leading dimension of C |

## Return Value

`rocblas_status_success` if successful, otherwise an error code.
