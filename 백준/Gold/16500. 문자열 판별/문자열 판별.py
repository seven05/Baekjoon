import sys
S = sys.stdin.readline().strip()
N = int(sys.stdin.readline().strip())
A = []
for _ in range(N):
    A.append(sys.stdin.readline().strip())
# print(S,A)
dp = [False]*(len(S)+1) # 시작값을 넣다보니 맨 뒤에 하나 더 필요함
dp[0] = True # dp는 항상 시작값이 필요
for i in range(len(S) + 1):
    if dp[i]:  # dp[i]가 True인 경우에만 진행
        for word in A:
            if S[i:i + len(word)] == word:
                dp[i + len(word)] = True
if dp[len(S)]:
    print(1)
else:
    print(0)