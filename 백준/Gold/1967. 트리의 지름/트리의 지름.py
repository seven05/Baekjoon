import sys
from collections import deque
 
n = int(sys.stdin.readline().strip())
tree = [[] for _ in range(n + 1)]
 
for _ in range(n - 1):
    p, c, d = map(int,sys.stdin.readline().split())
    tree[p].append((c, d))
    tree[c].append((p, d))
# print(tree)

def bfs(start):
    visited = [-1] * (n + 1)
    visited[start] = 0
    queue = deque()
    queue.append(start)
    
    while queue:
        cur = queue.popleft()
        for next, next_d in tree[cur]:
            if visited[next] == -1:
                queue.append(next)
                visited[next] = visited[cur] + next_d
    m = max(visited)
    return [visited.index(m), m]
 
print(bfs(bfs(1)[0])[1])