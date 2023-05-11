# Given an array of integers return an array answer[] such that answer[i] is equal to the product of all elements of nums except nums[i]

from math import prod
nums = [1, 2, 3, 4]
# answer = [0,0,9,0,0]

def productExceptSelf(nums):
    answer = []

    for i in range(len(nums)):
        noI = [x for x in nums]
        del noI[i]
        answer.append(prod(noI))
    
    print(answer)



productExceptSelf(nums)