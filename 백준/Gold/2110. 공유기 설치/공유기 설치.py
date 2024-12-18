import sys

N,C = map(int,sys.stdin.readline().split())
data = []
for i in range(N):
    data.append(int(sys.stdin.readline().strip()))
# print(data)
data.sort()

def can_install_routers(houses, distance, routers):
    count = 1
    last_installed = houses[0]

    for i in range(1, len(houses)):
        if houses[i] - last_installed >= distance:
            count += 1
            last_installed = houses[i]
            if count == routers:
                return True
    return False

def max_min_distance(houses, routers):
    houses.sort()
    left = 1  # 최소 거리
    right = houses[-1] - houses[0]  # 최대 거리
    best_distance = 0

    while left <= right:
        mid = (left + right) // 2
        if can_install_routers(houses, mid, routers):
            best_distance = mid  # 가능한 경우, 거리 기록
            left = mid + 1  # 더 큰 거리 탐색
        else:
            right = mid - 1  # 더 작은 거리 탐색

    return best_distance

# 입력 받
# 최적의 최소 거리 찾기
result = max_min_distance(data, C)
print(result)
