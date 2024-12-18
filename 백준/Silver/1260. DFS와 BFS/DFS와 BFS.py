import sys
from collections import deque

N,M,V = map(int,sys.stdin.readline().split())
graph = {i: [] for i in range(1, N + 1)}
# print(graph) {1: [], 2: [], 3: [], 4: []}
for _ in range(M):
    a, b = map(int,sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a) 
# print(graph) {1: [2, 3, 4], 2: [1, 4], 3: [1, 4], 4: [1, 2, 3]}

def dfs(graph, start, visited):
    visited[start] = True
    print(start, end=' ')  # 방문한 곳 출력
    for neighbor in sorted(graph[start]):
        if not visited[neighbor]:
            dfs(graph, neighbor, visited)

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        print(v, end=' ')  # 방문한 곳 출력
        for neighbor in sorted(graph[v]):
            if not visited[neighbor]:
                queue.append(neighbor)
                visited[neighbor] = True

visited = [False] * (N + 1)
dfs(graph, V, visited)
print()
visited = [False] * (N + 1)
bfs(graph, V, visited)