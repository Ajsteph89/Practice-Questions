# create a function that takes a list of strings, 
# and returns a dictionary that records a count of the number of occurneces for each duplicate value

# then create a new list that doesn't contain any duplicates


fruits = ['apple', 'mango', 'pear', 'kiwi', 'banana', 'apple', 'mango', 'orange', 'strawberry', 'mango', 'kiwi', 'grapefruit']


def solution(fruits):
    dict = {}
    for x in fruits:
        if x not in dict:
            dict[x] = 1
        else:
            dict[x] += 1
    return(dict)


print(solution(fruits))


def noDupes(fruits):
    new = []
    for x in fruits:
        if x not in new:
            new.append(x)
    return(new)

print(noDupes(fruits))