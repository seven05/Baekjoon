import sys
from collections import deque
ans = []
def distance(a,b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])

T = int(sys.stdin.readline().strip())
for _ in range(T):
    n = int(sys.stdin.readline().strip())
    home = list(map(int,sys.stdin.readline().split()))
    stores = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
    rock = list(map(int,sys.stdin.readline().split()))
    # ans.append([T,n,home,stores,rock])
    points = [home] + stores + [rock]
    visited = [False] * (n+2)
    queue = deque([0])
    visited[0] = True

    while queue:
        curr = queue.popleft()
        if curr == n+1:
            ans.append("happy")
            break

        for n_point in range(n+2):
            if not visited[n_point] and distance(points[curr],points[n_point]) <= 1000:
                visited[n_point] = True
                queue.append(n_point)
    else:
        ans.append("sad")

for i in ans:
    print(i)