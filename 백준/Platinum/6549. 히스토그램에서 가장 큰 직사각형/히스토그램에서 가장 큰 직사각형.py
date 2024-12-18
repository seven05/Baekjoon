def largest_rectangle_area(histogram):
    stack = []
    max_area = 0
    index = 0
    
    while index < len(histogram):
        # 스택이 비어있거나 현재 막대가 스택의 맨 위 막대보다 높다면
        if not stack or histogram[index] >= histogram[stack[-1]]:
            stack.append(index)
            index += 1
        else:
            # 스택의 맨 위 요소를 pop하여 넓이를 계산합니다.
            top_of_stack = stack.pop()
            # 스택이 비어있으면 현재 인덱스만큼이 너비가 됩니다.
            width = index if not stack else index - stack[-1] - 1
            # 최대 넓이를 업데이트합니다.
            max_area = max(max_area, histogram[top_of_stack] * width)
    
    # 모든 요소를 처리한 후에도 스택에 남은 높이들에 대해 넓이를 계산합니다.
    while stack:
        top_of_stack = stack.pop()
        width = index if not stack else index - stack[-1] - 1
        max_area = max(max_area, histogram[top_of_stack] * width)
    
    return max_area

# 입력을 처리하는 부분
import sys

if __name__ == "__main__":
    while True:
        histogram = list(map(int, sys.stdin.readline().strip().split()))
        if histogram[0] == 0:
            break
        print(largest_rectangle_area(histogram[1:]))