import sys

K = int(sys.stdin.readline().strip())
data = []
for i in range(K):
    data.append(int(sys.stdin.readline().strip()))
# print(data)
stack = []
for j in data:
    if j == 0:
        del stack[-1]
    else:
        stack.append(j)
result = 0
for k in stack:
    result += k
print(result)