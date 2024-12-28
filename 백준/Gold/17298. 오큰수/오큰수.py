import sys

N = int(sys.stdin.readline().strip())
A = list(map(int, sys.stdin.readline().split()))
# print(N,A)

ans = [-1] * N
stack = []
for i in range(N):
    while stack and A[stack[-1]] < A[i]:
        ans[stack.pop()] = A[i]
    stack.append(i)
print(*ans)