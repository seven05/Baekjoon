import sys

# 입력받기
N, M = map(int, sys.stdin.readline().split())
tree = list(map(int, sys.stdin.readline().split()))

# 나무의 높이 정렬
tree.sort()

# prefix_sum 배열 생성
prefix_sum = [0] * (N + 1)
for i in range(1, N + 1):
    prefix_sum[i] = prefix_sum[i - 1] + tree[i - 1]

# 이진 탐색을 위한 함수
def wood_length(mid):
    # mid 이상의 나무들의 시작 인덱스를 이진 탐색으로 찾기
    left, right = 0, N - 1
    while left <= right:
        mid_point = (left + right) // 2
        if tree[mid_point] >= mid:
            right = mid_point - 1
        else:
            left = mid_point + 1
    
    idx = left  # mid 이상의 나무들이 시작되는 인덱스
    return prefix_sum[N] - prefix_sum[idx] - mid * (N - idx)

# 이진 탐색을 위한 변수 초기화
start, end = 0, tree[-1]

# 이진 탐색 수행
while start <= end:
    mid = (start + end) // 2
    total = wood_length(mid)
    
    if total >= M:
        start = mid + 1
    else:
        end = mid - 1

# 최종적으로 end가 가장 높은 톱의 높이
print(end)
