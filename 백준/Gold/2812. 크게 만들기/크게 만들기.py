import sys

N,K = map(int,sys.stdin.readline().split())
data = list(map(int,sys.stdin.readline().strip()))
# print(data)
stack = []
cnt = K
for i in range(N):
    while cnt > 0 and stack and stack[-1] < data[i]: # 숫자를 가장 크게 만드는건 앞자리를 큰숫자로만 남기는것
        stack.pop()
        cnt -= 1
    stack.append(data[i])
stack = stack[:N-K]     #앞에서 작은숫자가 큰숫자보다 앞에있는 경우가 없어서 제거되지않았을때 최종적인숫자가 N-K자리여야함
if stack:
    for j in stack:
        print(j,end="")
else:          # N==K인 경우가 있을까봐 넣었는데 안넣었을때 통과하지 못하는지 모르겠음
    print(0)