import numpy as np
import scipy.sparse as sp


def generate_sparse_matrix(size, density):
    # Generate a random sparse matrix
    matrix = sp.random(size, size, density=density, format='coo', dtype=np.float64)
    
    return matrix

def save_coo_to_files(matrix, row_file, col_file, val_file, dim_file):
    # Save row indices
    np.savetxt(row_file, matrix.row, fmt='%d')
    
    # Save column indices
    np.savetxt(col_file, matrix.col, fmt='%d')
    
    # Save values
    np.savetxt(val_file, matrix.data, fmt='%.6f')

    # Save dimensions (number of rows, number of columns)
    with open(dim_file, 'w') as f:
        f.write(f"{matrix.shape[0]} {matrix.shape[1]}\n")

if __name__ == "__main__":
    # Generate a 16384x16384 sparse matrix with 0.1% non-zero elements
    problem_size = 16384
    density= 0.000125 #0.001 0.0005 0.00025 0.000125
    sparse_matrix = generate_sparse_matrix(problem_size, density)

    # Vector 
    vector = np.random.rand(problem_size)
    np.savetxt("vec.txt", vector, fmt='%.6f')

    # Multiply together 
    result_vector = sparse_matrix.multiply(vector);

    # total sum in the vector
    print(f"Total sum of the vector {np.sum(result_vector)}")


    # Save the matrix components to files
    save_coo_to_files(sparse_matrix, 'row_indices.txt', 'col_indices.txt', 'values.txt', 'dims.txt')

    print("COO matrix saved to text files (row_indices.txt, col_indices.txt, values.txt)")
