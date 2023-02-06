# find the median number of a list

arr = [0,1,2,4,6,5,3]

def findMedian(arr):
    # Write your code here
    arr.sort()

    middle =int((len(arr)-1)/2)
    
    print(arr[middle])


findMedian(arr)