import sys
from collections import deque
N = int(sys.stdin.readline().strip())  # 부품수
M = int(sys.stdin.readline().strip())  # 부품간의 관계 
connect = [[] for _ in range(N + 1)]
needs = [[0] * (N + 1) for _ in range(N + 1)]
degree = [0] * (N + 1)
for _ in range(M):
    x, y, k = map(int,sys.stdin.readline().split())
    connect[y].append((x, k))  # y -> x (y를 만들기 위해 x가 k개 필요)
    degree[x] += 1
# print(connect)
q = deque()
for i in range(1, N + 1):
    # 진입 차수가 0인걸 넣어준다.
    if degree[i] == 0:
        q.append(i)
while q:
    now = q.popleft()
    # 현 제품의 다음 단계 번호, 현 제품이 얼마나 필요한지
    for next, next_need in connect[now]:
        # 만약 현 제품이 기본 부품이면
        if needs[now].count(0) == N + 1:
            needs[next][now] += next_need
        # 현 제품이 중간 부품이면
        else:
            for i in range(1, N + 1):
                needs[next][i] += needs[now][i] * next_need
        # 차수 -1
        degree[next] -= 1
        if degree[next] == 0:
            # 차수 0이면 큐에 넣음
            q.append(next)
for x in enumerate(needs[N]):
    if x[1] > 0:
        print(*x)
# print(needs)