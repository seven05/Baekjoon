import sys
N = int(sys.stdin.readline().strip())
num = list(map(int,sys.stdin.readline().split()))
# print(N,num)
num.sort()
cnt = 0
for i in range(N):
    left = 0
    right = N-1    
    if i == 0:
        left += 1
    if i == N-1:
        right -= 1
    while left < right:
        compare = num[left] + num[right]
        if compare > num[i]:
            right -= 1
            if right == i:
                right -= 1   
        elif compare < num[i]:
            left += 1
            if left == i:
                left += 1     
        else:
            cnt += 1
            break
print(cnt)