import sys
from collections import deque

DR = [-1, 1, 0, 0]
DC = [0, 0, -1, 1]

N, M, fuel = map(int, sys.stdin.readline().split())
Map = []
for _ in range(N):
    Map.append(list(map(int,sys.stdin.readline().split())))
tr,tc = map(int,sys.stdin.readline().split())
tr -= 1
tc -= 1

sonim = {}
for _ in range(M):
    sr,sc,dr,dc = map(int,sys.stdin.readline().split())
    sonim[(sr-1,sc-1)] = (dr-1,dc-1)

# (start_r, start_c)에서 시작해 각 칸까지의 최단거리를
# dist[r][c] 형태로 리턴하는 함수.
# 도달 불가능하면 dist[r][c]는 -1로 남긴다.
def bfs(start_r, start_c, N, grid):
    dist = [[-1]*N for _ in range(N)]
    queue = deque()
    queue.append((start_r, start_c))
    dist[start_r][start_c] = 0
    while queue:
        r, c = queue.popleft()
        for i in range(4):
            nr = r + DR[i]
            nc = c + DC[i]
            if 0 <= nr < N and 0 <= nc < N: 
                if grid[nr][nc] == 0 and dist[nr][nc] == -1: # 벽이 아니고 + 방문X
                    dist[nr][nc] = dist[r][c] + 1
                    queue.append((nr, nc))
    return dist

def solve(tr, tc, fuel):
    for _ in range(M):
        # 현재 택시 위치에서 모든 칸까지 거리 계산
        dist_map = bfs(tr, tc, N, Map)

        # 택시에서 가장 가까운 승객 찾기
        min_dist = 10**8
        pick_r, pick_c = -1, -1
        for (sr, sc) in sonim:
            d = dist_map[sr][sc]
            if d != -1 and d < min_dist:
                min_dist = d
                pick_r, pick_c = sr, sc
            elif d != -1 and d == min_dist:
                if sr < pick_r or (sr == pick_r and sc < pick_c):
                    pick_r, pick_c = sr, sc

        # 승객을 찾지 못했거나, 연료 부족하면 실패
        if pick_r == -1 or min_dist > fuel:
            return -1

        fuel -= min_dist
        tr, tc = pick_r, pick_c

        # 승객 목적지까지 이동
        dest_r, dest_c = sonim[(pick_r, pick_c)]
        dist_map = bfs(tr, tc, N, Map)
        dist_to_dest = dist_map[dest_r][dest_c]

        # 목적지까지 갈 수 없거나, 연료 부족하면 실패
        if dist_to_dest == -1 or dist_to_dest > fuel:
            return -1

        fuel -= dist_to_dest
        fuel += dist_to_dest * 2

        tr, tc = dest_r, dest_c
        del sonim[(pick_r, pick_c)]

    # 모든 승객 이동 성공 시 남은 연료 출력
    return fuel

final_fuel = solve(tr, tc, fuel)
print(final_fuel)