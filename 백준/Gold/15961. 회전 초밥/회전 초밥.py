# 시간초과 해결법 못떠올려서 찾아봄
import sys

N, d, k, c = map(int, sys.stdin.readline().split())
belts = [int(sys.stdin.readline().strip()) for _ in range(N)]

# 풀이 찾아보고 적은코드
# 슬라이딩 윈도우 구현을 위해 처음 k-1개를 뒤에 덧붙임
belts += belts[:k-1]

freq = [0] * (d+1)  # 각 초밥이 현재 윈도우에 몇 개 있는지
current_cnt = 0     # 현재 윈도우의 '서로 다른' 초밥 수

# 초기 윈도우 설정 (0 ~ k-1)
for i in range(k):
    if freq[belts[i]] == 0:
        current_cnt += 1
    freq[belts[i]] += 1

result = current_cnt
# 쿠폰 적용 여부 확인
if freq[c] == 0:
    result = max(result, current_cnt + 1)

# 슬라이딩 윈도우 이동 (총 N-1번 이동 가능, 이미 k개를 잡았으므로)
left = 0
for right in range(k, N + k - 1):
    # 맨 왼쪽 제거
    freq[belts[left]] -= 1
    if freq[belts[left]] == 0:
        current_cnt -= 1
    left += 1

    # 새 초밥 추가
    if freq[belts[right]] == 0:
        current_cnt += 1
    freq[belts[right]] += 1

    # 최대 종류 업데이트
    if freq[c] == 0:
        result = max(result, current_cnt + 1)
    else:
        result = max(result, current_cnt)

print(result)

# 시간초과 ()
# max_cnt = 0
# for start in range(N):
#     temp_set = set()
#     for offset in range(k):
#         temp_set.add(belts[(start + offset) % N])
#     curr_cnt = len(temp_set)
#     if c not in temp_set:
#         curr_cnt += 1
#     max_cnt = max(max_cnt, curr_cnt)
# print(max_cnt)