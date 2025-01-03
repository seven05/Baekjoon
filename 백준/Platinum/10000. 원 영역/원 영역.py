import sys

n = int(sys.stdin.readline().strip())
circles = []

# 원의 왼쪽은 '(' 모양의 괄호 오른쪽은 ')' 모양의 괄호로 만든다.
for i in range(n):
  x, r = map(int, sys.stdin.readline().split())
  circles.append((x-r, '('))
  circles.append((x+r, ')'))
# 좌표기준으로 오름 차순으로 정렬하되 좌표가 같으면 ')'모양이 앞에 오게 정렬한다.
circles = sorted(circles, key= lambda x:(x[0], -ord(x[1])))
stack = []
# 스택에는 좌표, 괄호 모양, 상태값이 들어감
answer = 1
for i in range(n*2):
  position, bracket = circles[i]
  if len(stack) == 0:
    stack.append({'pos':position,'bracket':bracket,'status':0})
    continue
  # status 0: 기본값 ->
  # status 1: 원 안의 원이 연결 되어 있는 지 확인
  # 괄호가 닫히면 status 값을 확인하고 0 이면 +1 1이면 +2
  if bracket == ')':
    if stack[-1]['status'] == 0:
      answer +=1
    elif stack[-1]['status'] == 1:
      answer +=2
    stack.pop()
    # 원이 이어져 있는지 확인
    if i != n*2-1:
      if circles[i+1][0] != position:
        stack[-1]['status'] = 0
  else:
    if stack[-1]['pos'] == position:
      # 좌표값이 같으면 원이 접해있는 상태
      stack[-1]['status'] = 1
      stack.append({'pos':position,'bracket':bracket,'status':0})
    else:
      # 좌표값이 같지 않으면 원이접하지 않음
      stack.append({'pos':position,'bracket':bracket,'status':0})

print(answer)