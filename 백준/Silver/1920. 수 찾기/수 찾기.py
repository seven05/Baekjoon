import sys

N = int(sys.stdin.readline().strip())
A = list(map(int,sys.stdin.readline().split()))
M = int(sys.stdin.readline().strip())
X = list(map(int,sys.stdin.readline().split()))

# print(N,A,M,X)

A.sort()
def num_search(s,e,n):
    if s > e:
        return 0
    chk = (s+e)//2
    if A[chk] == n :
        return 1
    elif A[chk] > n:
        return num_search(s,chk-1,n)
    else:
        return num_search(chk+1,e,n)
for i in X:
    print(num_search(0,N-1,i))