# """
# An ideal number is a positive integer with only 3 and 5 as prime divisors.
# It can be expressed in the form of 3^x * 5^y, where x and y are non-negative integers.
# For example, 15, 45, and 75 are ideal numbers by 6, 10, and 21 are not.

# Find the number of ideal integers within the given segement [low, high] inclusive.

# Example:
# low = 200
# high = 405

# Power       of 3        of 5
# 0           1           1
# 1           3           5
# 2           9           25
# 3           27          125
# 4           81          625
# 5           243         3125
# 6           729         15625

# There are 4 ideal integers in the range [200, 405] inclusive:
# 3^2 * 5^2 = 9 * 25 = 225
# 3^5 * 5^0 = 243 * 1 = 243

# 3^1 * 5^3 = 3 * 125 = 375
# 3^4 * 5^1 = 81 * 5 = 405


# Function Description
# Complete the function getidealNums in the editor.

# getidealNums has the following parameter(s):
#     int low: an integer, the lower range limit, inclusive
#     int high: an integer, the upper range limit, inclusive

# Returns
#     int: the number of ideal integers in the inclusive range

# Constraints 1 <= low <= high <= 2 * 10^9

# Sample Case 0
# Sample input for custom testing

# STDIN       Function
# -----       --------
# 1       >>  low = 1
# 1       >>  high = 1

# Sample Output
# 1

# Explanation

# Only 1 ideal integer in [1, 1] can be expressed as 3^x * 5^y: 1 = 3^0*5^0

# Sample Case 1
# Sample input for custom testing

# STDIN       Function
# -----       --------
# 400000  >>  low = 400000
# 500000 >>   high = 500000

# Sample Output
# 3

# Explanation:

# 421875 = 3^3 * 5^6
# 455625 = 3^6 * 5^4
# 492075 = 3^9 * 5^2
# """

# between the range of numbers find numbers divisible by 5 and 3 that when multiplied together are within the low-high range

import math, itertools


low = 200
high = 405

def getIdealNums(low,high):
    three = []
    five = []
    x = 0
    y = 0
    while math.pow(3, x) <= high:
        three.append(int(math.pow(3, x)))
        x+=1
    while math.pow(5, y) <= high:
        five.append(int(math.pow(5, y)))
        y+=1

    options = [three, five]
    combos = [p for p in itertools.product(*options)]
    
    count = 0
    for x in range(low, high +1):
        for y in combos:
            if math.prod(y) == x:
                count +=1
        
    return count


print(getIdealNums(low,high))