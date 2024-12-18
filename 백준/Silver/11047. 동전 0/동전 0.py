import sys
N,K = map(int,sys.stdin.readline().split())
coins = []
for _ in range(N):
    coins.append(int(sys.stdin.readline().strip()))
result = 0
for coin in reversed(coins):
    # print(coin)
    result += K//coin
    K = K % coin
print(result)