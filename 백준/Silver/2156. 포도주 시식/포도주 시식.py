import sys

N = int(sys.stdin.readline().strip())
wine = [0]*(N+1)
for i in range(1, N+1):
    wine[i] = int(sys.stdin.readline().strip())

if N == 1:
    print(wine[1])
elif N == 2:
    print(wine[1]+wine[2])
else:
    dp = [0]*(N+1)
    dp[1] = wine[1]
    dp[2] = wine[1]+wine[2]
    dp[3] = max(dp[2],dp[1]+wine[3],wine[2]+wine[3])

    for i in range(4,N+1):
        dp[i] = max(dp[i-1],dp[i-2]+wine[i],dp[i-3]+wine[i-1]+wine[i])
    
    print(dp[N])
