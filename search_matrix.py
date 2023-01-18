# You are given an m x n integer matrix matrix with the following two properties:

# Each row is sorted in non-decreasing order.
# The first integer of each row is greater than the last integer of the previous row.
# Given an integer target, return true if target is in matrix or false otherwise.

matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]] 
target = 3


def searchMatrix(matrix, target):
    return any(target in x for x in matrix)

print(searchMatrix(matrix, target))