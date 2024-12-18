import sys

N, K = map(int,sys.stdin.readline().split())
data = list(map(int,sys.stdin.readline().split()))
# print(data)
count = 0
table = []
for i in range(K):
    if data[i] in table:        # 이미 사용중이면 pass
        continue
    if len(table) < N:          # 빈자리가 있으면 pass
        table.append(data[i])
        continue
    after_use = []              # 남은 전자기기 인덱스를 담아두고 제일 멀리있는것을 구분할 리스트
    after_table = data[i:]      # 남은 전자기기 리스트
    for j in range(N):          # 사용중인 전자기기 뒤에서 쓰는지 확인
        if table[j] not in after_table:
            after_use.append(101)
            continue
        after_use.append(after_table.index(table[j]))
    plug_out = after_use.index(max(after_use))  # 제일 나중에 사용하는 전자기기 인덱스
    del table[plug_out]         # 제일 나중에 사용하는 전자기기 제거
    table.append(data[i])       # 지금 사용할 전자기기 사용
    count += 1                  # 플러그 빼는 횟수 증가
print(count)