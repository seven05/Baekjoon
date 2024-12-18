import sys
N = int(sys.stdin.readline())
data = []
for i in range(N):
    data.append(sys.stdin.readline().strip())
result =[]
for i in data:
    if i in result:
        continue
    else:
        result.append(i)
# print(result)
result = sorted(sorted(result),key=len)

for i in result:
    print(i)