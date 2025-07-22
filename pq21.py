'''Pascal’s Triangle '''
def generate(numRows):
    triangle = [[1]]
    row = 0
    while numRows > len(triangle):
        row = row + 1
        triangle.append([1] * (row + 1))
        for i in range(1, row):
            triangle[row][i] = triangle[row - 1][i - 1] + triangle[row -1][i]
    return triangle

print(generate(5))

