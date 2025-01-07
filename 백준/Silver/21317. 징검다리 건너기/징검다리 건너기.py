import sys

N = int(sys.stdin.readline().strip())
small = [0]*(N+1)
big = [0]*(N+1)
for i in range(1, N):
    s, b = map(int, sys.stdin.readline().split())
    small[i] = s
    big[i] = b
K = int(sys.stdin.readline().strip())

dp = [[100001]*2 for _ in range(N+1)]
dp[1][0] = 0

for i in range(2, N+1):
    for j in (0, 1):
        # 작은 점프
        if i-1 >= 1 and dp[i-1][j] != 100001:
            dp[i][j] = min(dp[i][j], dp[i-1][j] + small[i-1])
        # 큰 점프
        if i-2 >= 1 and dp[i-2][j] != 100001:
            dp[i][j] = min(dp[i][j], dp[i-2][j] + big[i-2])
        # 매우 큰 점프
        if j == 1:  
            if i-3 >= 1 and dp[i-3][0] != 100001:
                dp[i][1] = min(dp[i][1], dp[i-3][0] + K)

ans = min(dp[N][0], dp[N][1])
print(ans)