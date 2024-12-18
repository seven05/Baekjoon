import sys
N,B = map(int,sys.stdin.readline().split())
A = []
for i in range(N):
    A.append(list(map(int,sys.stdin.readline().split())))
# print(A)
# print(result)
def matrix_mult(m1,m2):
    result = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            sum = 0
            for k in range(N):
                sum += (m1[i][k] * m2[k][j])%1000
            result[i][j] = sum % 1000
    return result
# print(matrix_mult(A,A,N))
def func(a,b):
    if b == 0:
        return [[1 if i == j else 0 for j in range(N)] for i in range(N)]
    if b % 2 == 0:
        half = func(a,b//2)
        return matrix_mult(half,half)
    else:
        return matrix_mult(a,func(a,b-1))
ans = func(A,B)
for i in ans:
    for j in i:
        print(j,end=" ")
    print()