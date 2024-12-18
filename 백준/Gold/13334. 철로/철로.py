import sys
import heapq

N = int(sys.stdin.readline().strip())
data=[]
for i in range(N):
    h,o = map(int,sys.stdin.readline().split())
    data.append([min(h,o),max(h,o)])
D = int(sys.stdin.readline().strip())
# print(data)
data.sort(key=lambda x: (x[1], x[0])) 
# 끝점 기준으로 정렬 그래야 시작지점을 최소힙으로 검사해서 가장 멀리있는것부터 검사가 가능하기때문에
start_heap = []
max_cnt = 0

for points in data:
    start, end = points
    heapq.heappush(start_heap,start)
    rail_start = end - D        # 선로의 왼쪽 끝점을 계산
    while start_heap and start_heap[0] < rail_start: # 선로의 한계보다 더 왼쪽으로 먼곳은 pop
        heapq.heappop(start_heap)
    max_cnt = max(max_cnt, len(start_heap))

print(max_cnt)