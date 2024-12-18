n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]

# DP 테이블 초기화
dp = [float('inf')] * (k + 1)
dp[0] = 0  # 0원을 만들기 위해 필요한 동전 수는 0개

# DP 테이블 갱신
for coin in coins:
    for i in range(coin, k + 1):
        dp[i] = min(dp[i], dp[i - coin] + 1)

# 결과 출력
if dp[k] == float('inf'):
    print(-1)
else:
    print(dp[k])
