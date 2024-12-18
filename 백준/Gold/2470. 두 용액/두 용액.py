import sys

N = int(sys.stdin.readline().strip())
data = list(map(int,sys.stdin.readline().split()))
data.sort()
def find_closest(n, liquid):
    liquid.sort()  # 용액을 정렬합니다.
    left, right = 0, n - 1
    closest_sum = float('inf')  # 초기값을 무한대로 설정
    best1 ,best2 = 0,0 # 가장 가까운 쌍을 저장할 변수

    while left < right:
        current_sum = liquid[left] + liquid[right]

        # 현재 쌍의 합이 0에 가까운지 확인
        if abs(current_sum) < abs(closest_sum):
            closest_sum = current_sum
            best1,best2 = liquid[left], liquid[right]

        # 합이 0보다 크면, 오른쪽 포인터를 왼쪽으로 이동
        if current_sum > 0:
            right -= 1
        # 합이 0보다 작으면, 왼쪽 포인터를 오른쪽으로 이동
        else:
            left += 1

    return best1,best2

result1,result2 = find_closest(N,data)
print(result1,result2)
