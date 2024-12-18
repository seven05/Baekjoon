import sys
from collections import deque

N = int(sys.stdin.readline().strip())
M = int(sys.stdin.readline().strip())
graph = [[float('inf')] * N for _ in range(N)]
for _ in range(M):
    s, e, c = map(int,sys.stdin.readline().split())
    if c < graph[s-1][e-1]:
        graph[s-1][e-1] = c
S,E = map(int,sys.stdin.readline().split())
# print(graph)
# print(N,M,S,E)
def bfs(n,s,e,graph):
    min_cost = [float('inf')]*n
    min_cost[s] = 0
    que = deque([s])
    while que:
        cur_city = que.popleft()
        for next_city in range(n):
            if graph[cur_city][next_city] != float('inf'):
                cost = min_cost[cur_city] + graph[cur_city][next_city]
                if cost < min_cost[next_city]:
                    min_cost[next_city] = cost
                    que.append(next_city)
    return min_cost[e]
answer = bfs(N,S-1,E-1,graph)
print(answer)