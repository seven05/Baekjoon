import sys

T = int(sys.stdin.readline().strip())
for _ in range(T):
    N = int(sys.stdin.readline().strip())
    coins = list(map(int,sys.stdin.readline().split()))
    M = int(sys.stdin.readline().strip())
    # print(N,coins,M)
    dp = [0]*(M+1)
    dp[0] = 1
    for val in coins:
        for i in range(M, 0, -1):
            j = 1
            while i >= j * val:
                dp[i] += dp[i - j * val]
                j += 1
    print(dp[M])