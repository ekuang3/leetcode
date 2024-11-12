def transpose_matrix(matrix):
    """
    Transpose a given 2D matrix (list of lists).
    
    Time: O(n^2), where n is the number of rows (or columns) in the square matrix.
    Space: O(n^2) due to the new transposed matrix storage.
    """
    return [[matrix[i][j] for i in range(len(matrix))] for j in range(len(matrix[0]))]

if __name__=='__main__':

    # Original 3x3 matrix
    matrix = [
                [1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]
            ]

    res = transpose_matrix(matrix) # [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
    print(res)