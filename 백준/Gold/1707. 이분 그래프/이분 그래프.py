import sys
sys.setrecursionlimit(1000000)
from collections import defaultdict

def dfs(node,color):
    color_arr[node] = color
    for neighbor in graph[node]:
        if color_arr[neighbor] == 0:
            if not dfs(neighbor,-color):
                return False
        elif color_arr[neighbor] == color:
            return False
    return True

def bipartite():
    for i in range(1,V+1):
        if color_arr[i] == 0:
            if not dfs(i,1):
                return False
    return True

K = int(sys.stdin.readline().strip())
for _ in range(K):
    V,E = map(int,sys.stdin.readline().split())
    graph = [[]for _ in range(V+1)]
    color_arr = [0] * (V+1)
    for _ in range(E):
        a, b = map(int, sys.stdin.readline().split())
        graph[a].append(b)
        graph[b].append(a)
    if bipartite():
        print("YES")
    else:
        print("NO")