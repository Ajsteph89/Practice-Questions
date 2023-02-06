# Given an array of integers, calculate the ratios of its elements that are positive, negative, and zero. Print the decimal value of each fraction on a new line with  places after the decimal.

# Note: This challenge introduces precision problems. The test cases are scaled to six decimal places, though answers with absolute error of up to  are acceptable.

# Example

# There are  elements, two positive, two negative and one zero. Their ratios are ,  and . Results are printed as:

# 0.400000
# 0.400000
# 0.200000
# Function Description

# Complete the plusMinus function in the editor below.

# plusMinus has the following parameter(s):

# int arr[n]: an array of integers
# Print
# Print the ratios of positive, negative and zero values in the array. Each value should be printed on a separate line with  digits after the decimal. The function should not return a value.

# Input Format

# The first line contains an integer, , the size of the array.
# The second line contains  space-separated integers that describe .

# Constraints



# Output Format

# Print the following  lines, each to  decimals:

# proportion of positive values
# proportion of negative values
# proportion of zeros


arr = [-4, 3, -9, 0, 4, 1]

def plusMinus(arr):
    pos = 0
    neg = 0
    zed = 0
    for x in arr:
        if x > 0:
            pos +=1
        elif x < 0:
            neg +=1
        else:
            zed +=1
    
    bottom = len(arr)
    plus = pos/bottom
    minus = neg/bottom
    zero = zed/bottom
    

    print("{:.6f}".format(plus))
    print("{:.6f}".format(minus))
    print("{:.6f}".format(zero))


plusMinus(arr)