# Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

nums = [-1, 0, 3, 5, 9, 12]
target = 9



def search(nums, target):
    if target in nums:
        return nums.index(target)
    else:
        return nums[0]


print(search(nums, target))