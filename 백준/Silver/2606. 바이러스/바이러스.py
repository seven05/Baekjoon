import sys
N = int(sys.stdin.readline().strip())
M = int(sys.stdin.readline().strip())
graph = {i: [] for i in range(1, N + 1)}
# print(graph) {1: [], 2: [], 3: [], 4: []}
for _ in range(M):
    a, b = map(int,sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)
# print(graph)
def dfs(graph, v, visited):
    visited[v] = True
    for neighbor in graph[v]:
        if not visited[neighbor]:
            dfs(graph, neighbor, visited)

visited = [False] * (N + 1)
dfs(graph,1,visited)
count = 0
for i in visited:
    if i == True:
        count += 1
print(count-1)