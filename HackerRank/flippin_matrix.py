# find the maximum value in the top left quadrant of the matrix by only being able to flip (mirror) columns and rows order
matrix = [
    [112, 42, 83, 119], 
    [56, 125, 56, 49],
    [15, 78, 101, 43],
    [62, 98, 114, 108]
]

def matrixFlip(matrix):
    length= len(matrix)
    total = 0

    for x in range(length//2):
        for y in range(length//2):
            total += max(matrix[x][y], matrix[x][length-y-1], matrix[length-x-1][y], matrix[length-x-1][length-y-1])

    return total


print(matrixFlip(matrix))