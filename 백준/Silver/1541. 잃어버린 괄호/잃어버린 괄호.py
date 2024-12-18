import sys

data = str(sys.stdin.readline().strip())
result = []
modified_data = ""
last_position = 0

for i in range(len(data)):
    if data[i] == '-':
        result.append(i)
    if len(result) != 0 and (i == len(data) - 1 or (i < len(data) - 1 and data[i + 1] == '-')):
        # 이전 - 위치부터 현재 위치까지를 괄호로 감싸기
        start = result[-1] + 1
        end = i + 1
        modified_data += data[last_position:start] + '(' + data[start:end] + ')'
        last_position = end
# 마지막 남은 부분 이어붙이기
modified_data += data[last_position:]
# print(modified_data)
# print(eval(modified_data)) 이걸쓰면 앞이 0으로 쓰일때 에러가 생김
terms = modified_data.split('-')
total = 0
total += sum(map(int, terms[0].strip('()').split('+')))
for term in terms[1:]:
    total -= sum(map(int, term.strip('()').split('+')))
print(total)