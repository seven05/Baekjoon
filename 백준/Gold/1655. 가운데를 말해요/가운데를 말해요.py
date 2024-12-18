import sys
import heapq
N = int(sys.stdin.readline().strip())
data=[]
for i in range(N):
    data.append(int(sys.stdin.readline().strip()))
# print(data)

min_heap = []   # 중간값보다 큰값들
max_heap = []   # 중간값보다 같거나 작은값들
# 이렇게 나눠서 루트끼리만 비교해서 교환한다음에 최대힙의 루트를 출력하면됨
for num in data:

    heapq.heappush(max_heap,-num)   # heapq가 최소힙형태라 음수로 저장해야 최대힙으로 쓸수있음
    if min_heap:
        if -max_heap[0] > min_heap[0]: # 최대힙의 루트노드랑 최소힙의 루트노드를 비교해서
            heapq.heappush(min_heap,-(heapq.heappop(max_heap)))

    if len(max_heap) < len(min_heap) : # max_heap의 루트를 최종적으로 출력하려면 작으면 안됨
        heapq.heappush(max_heap,-(heapq.heappop(min_heap)))
    elif len(max_heap) > len(min_heap)+1: # 1개보다 더많아도 안됨
        heapq.heappush(min_heap,-(heapq.heappop(max_heap)))
    
    print(-(max_heap[0]))