# There exists a staircase with N steps, and you can climb up either 1 or 2 steps at a time. Given N, write a function that returns the number of unique ways you can climb the staircase. The order of the steps matters.
# For example, if N is 4, then there are 5 unique ways:
# 1, 1, 1, 1
# 2, 1, 1
# 1, 2, 1
# 1, 1, 2
# 2, 2


import itertools

N = 4
step = [1, 2]

def staircase(N, step):
    count = 0 

    while N > 0:
        opts = list(map(list, itertools.product(step, repeat=N)))
        for x in opts:
            if (sum(x)==4):
                count+=1
        N-=1
        
    return(count)


print(staircase(N, step))



