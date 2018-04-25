# function to rotate N x N matrix to 90 degree
def rotate(matrix):
    # if length of matrix is zero or matrix is not N x N, return false
    if len(matrix) == 0 or len(matrix) != len(matrix[0]):
        return False
    n = len(matrix)
    for layer in range(n // 2):
        first = layer
        last = n - 1 - layer
        for i in range(last):
            offset = i - first
            top = matrix[first][i]  # save top
            # left -> top
            matrix[first][i] = matrix[last - offset][first]
            # bottom -> left
            matrix[last - offset][first] = matrix[last][last - offset]
            # right -> bottom
            matrix[last][last - offset] = matrix[i][last]
            # top -> right
            matrix[i][last] = top
    return True
