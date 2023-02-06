import itertools


nums = [10, 15, 3, 7]
target = 13


def twoSum(nums, target):
    for i in range(len(nums)):
        for x in range(len(nums)):
            if nums[i] + nums[x] == target and i != x:
                print(i, x)
                print(True)

twoSum(nums, target)

def alternative(nums, target):
    for i in itertools.combinations(nums, 2):
        if sum(i) == target:
            return(True)
    return(False)

alternative(nums, target)

