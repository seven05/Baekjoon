import sys
from collections import deque

N = int(sys.stdin.readline().strip())
board = []
for _ in range(N):
    board.append(list(map(int,sys.stdin.readline().strip())))
# print(borad)
visited = [[False] * N for _ in range(N)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def check_danji_size(x,y):
    queue = deque([(x, y)])
    visited[x][y] = True
    size = 1
    while queue:
        cx, cy = queue.popleft()
        for i in range(4):  
            nx, ny = cx + dx[i], cy + dy[i]
            if 0 <= nx < N and 0 <= ny < N:  
                if not visited[nx][ny] and board[nx][ny] == 1:  
                    visited[nx][ny] = True
                    queue.append((nx, ny))
                    size += 1
    return size

danji_cnt = 0
danji_size = []

for i in range(N):
    for j in range(N):
        if board[i][j] == 1 and not visited[i][j]:
            danji_cnt += 1
            danji_size.append(check_danji_size(i,j))

danji_size.sort()
print(danji_cnt)
for size in danji_size:
    print(size)