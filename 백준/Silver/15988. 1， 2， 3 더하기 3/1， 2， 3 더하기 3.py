import sys

T = int(sys.stdin.readline().strip())
num = []
for _ in range(T):
    num.append(int(sys.stdin.readline().strip()))
# print(num)
max_num = max(num)
dp = [0] * (max_num+1)
dp[1] = 1
dp[2] = 2
dp[3] = 4

for i in range(4,max_num+1):
    dp[i] = (dp[i-1] + dp[i-2] + dp[i-3])%1000000009

for i in num:
    print(dp[i]%1000000009)