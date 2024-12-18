import sys
import heapq
N = int(sys.stdin.readline().strip())
data=[]
for i in range(N):
    data.append(int(sys.stdin.readline().strip()))
heapq.heapify(data)     # 이거 안했다가 4%에서 틀렸습니다. 뜸
result = 0
while len(data) > 1 : # 힙 루트에 있는 애가 제일 최소쌍이므로 heappop을 두번해서 더하고 결과에 추가함
    A = heapq.heappop(data)
    B = heapq.heappop(data)
    C = A + B
    result += C
    heapq.heappush(data,C)
print(result)