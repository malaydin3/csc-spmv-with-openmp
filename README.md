# Sparse Matrix-Vector Multiplication (SpMV) in C++ using CSC Format and OpenMP

This project implements Sparse Matrix-Vector Multiplication (SpMV) in C++ using Compressed Sparse Column (CSC) format. It reads a matrix provided in the Coordinate (COO) format and converts it to CSC format for efficient multiplication with a dense vector. The implementation leverages OpenMP for parallel processing, with three variants of SpMV:

1. **Serial**: Basic serial multiplication.
2. **Naive Parallel**: Parallelized across columns with race conditions managed by atomic operations.
3. **Column Coloring Parallel**: A parallel implementation that avoids race conditions by grouping non-conflicting columns.

## Requirements

- **C++ compiler** with OpenMP support (e.g., `g++`).
- **Input matrix** files in COO format (generated from Python, using SciPy).

## Files

- `csc_spmv.cpp`: Main code for reading input, converting COO to CSC, and performing SpMV.
- `row_indices.txt`, `col_indices.txt`, `values.txt`, `dims.txt`: Text files with the matrix data in COO format.
- `vec.txt`: Text file with the dense vector to be multiplied.

## Matrix Data Files

The matrix is assumed to be stored in a series of text files, created by an external Python script (e.g., `coo_matrix_generator.py` using SciPy):

1. **`row_indices.txt`**: Contains the row indices for non-zero values.
2. **`col_indices.txt`**: Contains the column indices for non-zero values.
3. **`values.txt`**: Contains the non-zero values of the matrix.
4. **`dims.txt`**: Contains the matrix dimensions as `num_rows num_columns`.
5. **`vec.txt`**: Contains the elements of the dense vector.

## Compilation

To compile the code, run:
```bash
g++ -fopenmp csc_spmv.cpp -o csc_spmv.out