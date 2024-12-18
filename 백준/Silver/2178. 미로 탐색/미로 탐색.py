import sys
from collections import deque
N,M = map(int,sys.stdin.readline().split())
maze=[]
for _ in range(N):
    maze.append(list(map(int,sys.stdin.readline().strip())))
# print(maze)
def bfs(maze,n,m):
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    que = deque([(0,0)])
    while que:
        x,y = que.popleft()
        if x == n-1 and y == m-1:
            return maze[x][y]
        for i in range(4):
            nx,ny = x+dx[i],y+dy[i]
            if 0<=nx<n and 0<=ny<m and maze[nx][ny] == 1:
                maze[nx][ny] = maze[x][y] + 1
                que.append((nx,ny))

print(bfs(maze,N,M))