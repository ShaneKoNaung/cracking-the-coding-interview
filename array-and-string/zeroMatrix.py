import copy


# Write an algorithm such that if an element in an MxN matrix is 0, its entire row and column are set to 0
def zeroMatrix(matrix):
    result_maxtrix = copy.deepcopy(matrix)  # deepcopy the given matrix
    for i in range(len(matrix)):  # iterate through the given matrix
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                setzero(i, j, result_maxtrix)  # change the rows and columns of copy matrix
    return result_maxtrix


# set all element in the row i and row j to zero
def setzero(i, j, matrix):
    for column in range(len(matrix[0])):
        matrix[i][column] = 0
    for row in range(len(matrix)):
        matrix[row][j] = 0


def test(m1, m2):
    if zeroMatrix(m1) == m2:
        print("test passed.")
    else:
        print("test failed.")


m1 = [[1, 2, 3, 4],
      [1, 2, 3, 4],
      [1, 2, 3, 4],
      [1, 2, 3, 4]]
test(m1, m1)
m1 = [[1, 2, 3, 4],
      [1, 0, 3, 4],
      [1, 2, 0, 4],
      [1, 2, 3, 4],
      [1, 2, 3, 4]]
m2 = [[1, 0, 0, 4],
      [0, 0, 0, 0],
      [0, 0, 0, 0],
      [1, 0, 0, 4],
      [1, 0, 0, 4]]
test(m1, m2)
