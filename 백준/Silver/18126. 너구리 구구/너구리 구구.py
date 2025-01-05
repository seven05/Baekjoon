import sys
from collections import deque
N = int(sys.stdin.readline().strip())
graph = [[] for _ in range(N+1)]
for _ in range(N-1):
    A, B, C = map(int, input().split())
    graph[A].append((B, C))
    graph[B].append((A, C))
dist = [-1] * (N+1)
dist[1] = 0
#BFS
queue = deque([1])
while queue:
    curr = queue.popleft()
    for (next_room, length) in graph[curr]:
        if dist[next_room] == -1:
            dist[next_room] = dist[curr] + length
            queue.append(next_room)
print(max(dist))

#DFS
def dfs(start, graph, dist):
    for (next_room, length) in graph[start]:
        if dist[next_room] == -1:
            dist[next_room] = dist[start] + length
            dfs(next_room, graph, dist)
# dfs(1,graph,dist)
# print(max(dist))