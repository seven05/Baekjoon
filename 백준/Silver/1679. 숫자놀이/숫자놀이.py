import sys

N = int(sys.stdin.readline().strip())
data = list(map(int,sys.stdin.readline().split()))
K = int(sys.stdin.readline().strip())
nums = set(data)
max = data[-1]*K
dp = [float('inf')]*(max+1)
dp[0] = 1
for i in range(1,max+1):
    if i in nums:
        dp[i] = 1
    else:
        for j in range(1, i//2 +1):
            dp[i] = min(dp[i],dp[j] + dp[i-j])
    if dp[i] > K:
        if i % 2 == 0:
            print("holsoon win at",i)
            break
        else:
            print("jjaksoon win at",i)
            break