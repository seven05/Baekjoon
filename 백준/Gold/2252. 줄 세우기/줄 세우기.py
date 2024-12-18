import sys
from collections import deque

N,M = map(int,sys.stdin.readline().split())
graph = [[] for _ in range(N + 1)]
# print(graph)
indegree = [0] * (N + 1)
for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    indegree[b] += 1

queue = deque()
for i in range(1, N + 1):
    if indegree[i] == 0:
        queue.append(i)
result = []
while queue:
    node = queue.popleft()
    result.append(node)
    for next_node in graph[node]:
        indegree[next_node] -= 1
        if indegree[next_node] == 0:
            queue.append(next_node)
print(' '.join(map(str, result)))

# Dfs로 된다한거같아서 찾아는 봄
# visited = [False] * (N + 1)
# result = []

# def dfs(node):
#     global result
#     visited[node] = True
#     for next_node in graph[node]:
#         if not visited[next_node]:
#             dfs(next_node)
#     result.append(node)

# for i in range(1, N + 1):
#     if not visited[i]:
#         dfs(i)

# print(' '.join(map(str, reversed(result))))