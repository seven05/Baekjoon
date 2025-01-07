import sys

N = int(sys.stdin.readline().strip())
ans = 0
stair = [0]*(N+1)
for i in range(1,N+1):
    stair[i] = int(sys.stdin.readline().strip())
# print(stair)

if N == 1:
    ans = stair[1]
else:
    dp = [0]*(N+1)
    dp[1] = stair[1]
    dp[2] = stair[1]+stair[2]

    if N == 2:
        ans = dp[2]
    else:
        for i in range(3,N+1):
            dp[i] = max(dp[i-2]+stair[i],dp[i-3]+stair[i-1]+stair[i])
        ans = dp[N]

print(ans)
