# Write an algorithm to determine if a number n is happy.

# A happy number is a number defined by the following process:

# Starting with any positive integer, replace the number by the sum of the squares of its digits.
# Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
# Those numbers for which this process ends in 1 are happy.
# Return true if n is a happy number, and false if not.

import math

n = 1111111

def isHappy(n):
    count = 0
    while count <= 10:
        digits = [int(d) for d in str(n)]
        squares = []
        for x in digits:
            squares.append(int(math.pow(x,2)))

        n = sum(squares)

        count +=1
        
        if n == 1:
            return True
        elif count == 10:
            return False


print(isHappy(n))