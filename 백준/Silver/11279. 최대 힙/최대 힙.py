import sys

N = int(sys.stdin.readline().strip())
data=[]
for i in range(N):
    data.append(int(sys.stdin.readline().strip()))
# print(data)
result_heap = []
def heap_insert(heap, x):
    # 새 값을 힙에 추가
    heap.append(x)
    idx = len(heap) - 1
    # 부모 노드와 비교해가며 올바른 위치를 찾기
    while idx > 0:
        parent = (idx - 1) // 2
        if heap[idx] > heap[parent]:
            # 부모보다 크다면 자리 교환
            heap[idx], heap[parent] = heap[parent], heap[idx]
            idx = parent
        else:
            break

def heap_delete(heap):
    if len(heap) == 0:
        return 0
    max_value = heap[0]
    heap[0] = heap[-1]
    heap.pop()
    idx = 0
    while True:
        left_child = 2 * idx + 1
        right_child = 2 * idx + 2
        largest = idx
        # 왼쪽 자식이 현재 노드보다 크다면 교환할 후보로 설정
        if left_child < len(heap) and heap[left_child] > heap[largest]:
            largest = left_child
        # 오른쪽 자식이 현재까지 가장 큰 노드보다 크다면 교환할 후보로 설정
        if right_child < len(heap) and heap[right_child] > heap[largest]:
            largest = right_child
        # 교환할 노드가 없다면 종료
        if largest == idx:
            break
        # 현재 노드와 가장 큰 자식 노드를 교환
        heap[idx], heap[largest] = heap[largest], heap[idx]
        idx = largest
    return max_value

for i in data:
    if i == 0 :
        print(heap_delete(result_heap))
    else:
        heap_insert(result_heap,i)