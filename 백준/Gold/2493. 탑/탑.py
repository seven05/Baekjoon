import sys

N = int(sys.stdin.readline().strip())
data = list(map(int,sys.stdin.readline().split()))
# print(data)

stack = []      #스택에는 [탑의 인덱스 , 탑의 높이] 형태로 담아서 저장함
result = []     #출력은 탑의 인덱스에 맞게 갯수를 담아서 출력해야하므로 따로 만듬
for i in range(N):
    #스택에 현재 검사중인 탑보다 낮은거면 다제거 (스택 비어있는데 pop하면 인덱스 에러 나니깐 제외)
    while stack and stack[-1][1] < data[i]: #이거 순서 반대로 하면 인덱스 에러뜸 스택 비어있을때 때문에
        stack.pop()

    if stack:
        result.append(stack[-1][0]+1) #여기에 +1 안하면 몇 번째를 묻는거라 1씩 모자름
    else:
        result.append(0)
    
    stack.append([i,data[i]])
for i in result:     
    print(i,end=" ")