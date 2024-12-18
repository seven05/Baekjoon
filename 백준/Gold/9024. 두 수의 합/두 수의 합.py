import sys

T = int(sys.stdin.readline().strip())
# def func(n,k,arr):

# for i in range(T):
#     globals()['N_%d',i],globals()['K_%d',i] = map(int,sys.stdin.readline().split())
#     globals()['data_%d',i] = list(map(int,sys.stdin.readline().split()))
#     globals()['data_%d',i].sort()
    # print(globals()['data_%d',i])
# print(globals()['data_%d',0])
# print(globals()['data_%d',1])
# print(globals()['data_%d',2])
# print(globals()['data_%d',3])

def find_pair(k,arr):
    pl,pr = 0,len(arr)-1
    closest_diff = float('inf')
    closest_cnt = 0
    while pl < pr:
        current_sum = arr[pl]+arr[pr] 
        current_diff = abs(current_sum - k)
        if current_diff < closest_diff :
            closest_diff = current_diff
            closest_cnt = 1
        elif current_diff == closest_diff:
            closest_cnt += 1
        if current_sum > k:
            pr -= 1
        elif current_sum <= k:
            pl += 1
    return closest_cnt
result = []
for i in range(T):
    N,K = map(int,sys.stdin.readline().split())
    data = list(map(int,sys.stdin.readline().split()))
    data.sort()
    result.append(find_pair(K,data))
for j in range(T):   
    print(result[j])