import sys

N = int(sys.stdin.readline().strip())
data = []
for _ in range(N):
    data.append(list(map(int,sys.stdin.readline().split())))
# print(data)
# 회의가 끝나는시간 기준으로 정렬 -> 그다음 시작시간 기준
sorted_data = sorted(data,key=lambda x: (x[1], x[0]))
# print(sorted_data)
result = 0
last_end_time = 0

for start, end in sorted_data:
    if start >= last_end_time:  # 현재 회의의 시작 시간이 이전 회의의 종료 시간과 같거나 클 때만 선택
        last_end_time = end  # 현재 회의의 종료 시간을 갱신
        result += 1  # 선택된 회의 수를 증가

print(result)