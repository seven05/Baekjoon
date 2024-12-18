import sys
data = sys.stdin.readline().strip()
# print(data)
stack=[]
cnt = 0
for i in range(len(data)):
    if data[i] == "(":
        stack.append("(")
    else :
        if data[i-1]=="(":
            stack.pop()
            cnt+=len(stack) # 현재의 쇠막대기 카운팅
            
        else :
            stack.pop()
            cnt+=1 # 두 번째 경우인 나머지 부분
print(cnt)