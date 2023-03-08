# Write a function that takes a list of elements as a parameter. The function should return a dictionary containing the frequency of each element in the list.
# Input = [“code”, “code”, “momentum”, 1]
# Output = {“code”:2, “momentum”:1, 1:1}
# Input = [0,0,0,0,0]
# Output = {0:5}

from collections import Counter

Input =  ['code', 'code', 'momentum', 1]

# def counts(input):
#     return dict(Counter(input))

# print(counts(Input))

# alternate

def counts(input):
    count = {}
    for item in input:
        if item not in count:
            count[item] = 1
        elif item in count:
            count[item] += 1
    return count


print(counts(Input))