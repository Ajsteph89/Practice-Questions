from heapq import nlargest

nums = [1,1,1,2,2,3]
k = 2


def topKFrequent(nums, k):
    elementsDict = {}
    for x in nums:
        if x not in elementsDict:
            elementsDict[x] = 1
        else:
            elementsDict[x] += 1
    print(elementsDict)

    res = nlargest(k, elementsDict, key=elementsDict.get)

    print(res)

topKFrequent(nums, k)