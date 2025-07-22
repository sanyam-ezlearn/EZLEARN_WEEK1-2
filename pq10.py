'''Transpose Matrix Problem'''
def transpose(matrix):
    n = len(matrix)
    m = len(matrix[0])

    transposed = [[0 for j in range(n)] for i in range(m)]

    for i in range(n):
        for j in range(m):
            transposed[j][i] = matrix[i][j]

    return transposed

matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(transpose(matrix))