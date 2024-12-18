import sys
N = int(sys.stdin.readline())

data = [0]*10001

for i in range(N):
    x = int(sys.stdin.readline().strip())
    data[x] += 1
for i in range(1,10001):
    if data[i] == 0:
        continue
    else:
        for j in range(data[i]):
            print(i)
