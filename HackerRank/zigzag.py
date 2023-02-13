
# given an array of n numbers make the array start in ascending and then midway start descending 

a = [2,3,5,1,4]
n = len(a)


def findZigZagSequence(a, n):
    a.sort()
    mid = int((n + 1)/2)-1 #need to add the -1 
    print(mid)
    a[mid], a[n-1] = a[n-1], a[mid]

    st = mid + 1
    ed = n - 2 # need to decrement by 2 instead of 1
    while(st <= ed):
        a[st], a[ed] = a[ed], a[st]
        st = st + 1
        ed = ed - 1 # need to decrement and not increment

    for i in range(n):
        if i == n-1:
            print(a[i])
        else:
            print(a[i], end = ' ')
    return
