import sys

M,N,L = map(int,sys.stdin.readline().split())
hunters = list(map(int,sys.stdin.readline().split()))
hunters.sort()
animals = []
for i in range(N):
    animals.append(list(map(int,sys.stdin.readline().split())))
# print(hunters,animals)
count = 0
for x, y in animals:
    if y > L:
        continue
    left, right = 0, len(hunters) - 1
    while left <= right:
        mid = (left + right) // 2
        if hunters[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    if left < len(hunters) :
        closed_hunter = hunters[left]
    else: 
        closed_hunter = float('inf')
    if left > 0:
        previous_hunter = hunters[left-1]
        if abs(previous_hunter - x) + y <= L:
            count += 1
            continue
    if abs(closed_hunter - x) + y <= L:
       count += 1
    
print(count)