import sys
N,X = sys.stdin.readline().split()
N = int(N)
X = int(X)
#print(N,X)
A = []
result = []
A = list(map(int, sys.stdin.readline().split()))
for i in range(N):
    if (A[i] < X):
        result.append(A[i])
for j in result:
    print(j,end=" ")