numbers = [1, 3, 5]

# return true for dupes and false if not

def checkDupes(nums):
    checks = []
    for x in nums:
        if x not in checks:
            checks.append(x)
        elif x in checks:
            return True
    if nums == checks:
        return False
            
print(checkDupes(numbers))