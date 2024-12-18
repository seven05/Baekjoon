import sys
sys.setrecursionlimit(1000000)
from collections import defaultdict
N = int(sys.stdin.readline().strip())
graph = defaultdict(list)
for _ in range(N-1):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(node, parent):
    parents[node] = parent
    for neighbor in graph[node]:
        if neighbor != parent:
            dfs(neighbor, node)

parents = [0] * (N + 1)
dfs(1, 0)
for i in range(2, N + 1):
    print(parents[i])