import sys
from collections import deque
M, N, H = map(int,sys.stdin.readline().split())
tomato = []
queue = deque()
for z in range(H):
    box = []
    for y in range(N):
        row = list(map(int, input().split()))
        box.append(row)
        for x in range(M):
            if row[x] == 1:  # 익은 토마토라면
                queue.append((x, y, z))  # 큐에 추가 (BFS 시작점)
    tomato.append(box)
dx = [1, -1, 0, 0, 0, 0] 
dy = [0, 0, 1, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]
while queue:
    x, y, z = queue.popleft()
    for i in range(6):
        nx,ny,nz = x + dx[i],y + dy[i],z + dz[i]
        if 0 <= nx < M and 0 <= ny < N and 0 <= nz < H and tomato[nz][ny][nx] == 0: # 상자의 범위 내 + 아직 익지 않은 토마토일 경우
            tomato[nz][ny][nx] = tomato[z][y][x] + 1  # 일 수를 증가시켜 익게 만든다.
            queue.append((nx, ny, nz))  # 새로 익은 토마토를 큐에 추가
max_days = 0
for z in range(H):
    for y in range(N):
        for x in range(M):
            if tomato[z][y][x] == 0:  # 익지 않은 토마토가 존재하면
                print(-1)
                exit()
            max_days = max(max_days, tomato[z][y][x])
print(max_days - 1) # 첫 시작이 1