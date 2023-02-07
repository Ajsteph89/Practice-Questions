# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

# You must implement a solution with a linear runtime complexity and use only constant extra space.



nums = [4,1,2,1,2]

def singleNumber(nums):
    counts = {x:nums.count(x) for x in nums}
    x = min(counts, key=counts.get)
    
    if counts[x] == 1:
        return x
    else:
        return -1

print(singleNumber(nums))