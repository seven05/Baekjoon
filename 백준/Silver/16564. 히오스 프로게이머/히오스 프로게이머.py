import sys

N,K = map(int,sys.stdin.readline().split())
Levels = []
for i in range(N):
    Levels.append(int(sys.stdin.readline().strip()))
Levels.sort()
# print(Levels)
def max_level(levels):
    # 최소 레벨과 최대 목표 레벨 설정
    low, high = min(levels), (max(levels) + K)

    while low <= high:
        mid = (low + high) // 2

        # mid 레벨까지 올리는 데 필요한 작업 횟수 계산
        required_operations = sum(max(0, mid - level) for level in levels)

        # 필요한 작업 횟수가 K보다 작거나 같으면 더 높은 레벨도 가능
        if required_operations <= K:
            low = mid + 1
        else:
            high = mid - 1

    # 가능한 최대 레벨(high) 반환
    return high
print(max_level(Levels))