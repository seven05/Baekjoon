import sys

N,M = map(int,sys.stdin.readline().split())
# print(N,M)
data = list(map(int, sys.stdin.readline().split()))
# print(data)
data.sort()
# print(data)
sum_max = 0 
for i in range(N):
    for j in range(i+1,N):
        for k in range(j+1,N):
            pick_sum = data[i]+data[j]+data[k]
            if (pick_sum <= M and pick_sum > sum_max):
                sum_max = pick_sum
print(sum_max)