import sys
N,M = map(int,sys.stdin.readline().split())
data = []
for _ in range(N):
    data.append(list(map(int,sys.stdin.readline().split())))
# print(data)
dp = [0]*(M+1)
for W, V, C in data:
    k = 1
    while C > 0:
        num = min(k, C)
        C -= num
        for w in range(M, W * num - 1, -1):
            dp[w] = max(dp[w], dp[w - W * num] + V * num)
        k *= 2
print(dp[M])