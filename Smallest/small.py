# find the smallest integer not in A

A = [1, 3, 6, 4, 1, 2]

def solution(A):
    A.sort()
    for i in A:
        if i < 0:
            return(1)  
        elif i+1 not in A:
            return(i+1)


print(solution(A))