# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

# You must implement a solution with a linear runtime complexity and use only constant extra space.

from collections import Counter

nums = [4,1,2,1,2]

def singleNumber(nums):
    count = Counter(nums)
    return min(count, key=count.get)

print(singleNumber(nums))