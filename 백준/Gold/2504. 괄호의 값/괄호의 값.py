import sys

data = list(sys.stdin.readline().strip())
# print(data)

def cal_stack(data):
    stack = []
    for i in data:
        if i == "(" or i == "[":  # 여는 괄호는 스택에추가
            stack.append(i)
        elif i == ")":          # 닫는 괄호따라서 x2 x3이 바껴야하므로 두개로 분리
            if not stack:       # 비어있으면 0
                return 0
            tmp = 0
            while stack:
                top = stack.pop()
                if top == "(":     # 여는 괄호만나면 stack 계산값을 넣기
                    stack.append(2 if tmp == 0 else tmp*2)  # () 이거는 2
                    break
                elif top == "[":    # 얘 만나면 잘못된거니깐 0
                    return 0 
                else:
                    tmp += top
            else:               # 앞에가 비어있으면 잘못된거
                return 0
        elif i == "]":          
            if not stack:
                return 0
            tmp = 0
            while stack:
                top = stack.pop()
                if top == "[":
                    stack.append(3 if tmp == 0 else tmp*3)  # [] 이거는 3
                    break
                elif top == "(":
                    return 0 
                else:
                    tmp += top
            else:
                return 0 
    result = 0
    for j in stack:     # 위에꺼 다돌고도 여는 괄호있으면 잘못된거니깐 확인
        if j == '(' or j == '[':
            return 0
        result += j     # 스택에 있는 숫자값들 다 더하기 
    return result

print(cal_stack(data))