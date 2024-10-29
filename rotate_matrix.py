def rotate_clockwise(matrix):
    """ 
    Time: O(N^2) where N is the dimension of the matrix
    Space: O(1)
    """
    # Transpose the matrix
    for i in range(len(matrix)):
        for j in range(i, len(matrix)):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Reverse each row
    for i in range(len(matrix)):
        matrix[i] = matrix[i][::-1]

    return matrix

if __name__=='__main__':
    
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]] 
    matrix = rotate_clockwise(matrix) # [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
    print(matrix)