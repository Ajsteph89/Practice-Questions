# Given a square matrix, calculate the absolute difference between the sums of its diagonals.

# For example, the square matrix  is shown below:

arr = [
    [1, 2, 3],
    [4, 5, 6],
    [9, 8, 9]
]

def diagonalDifference(arr):
    primary = 0
    secondary = 0 
    n = len(arr)
    
    for i in range(0, n):
        primary += arr[i][i]
        secondary += arr[i][n - i - 1]


    print(abs(primary - secondary))


diagonalDifference(arr)