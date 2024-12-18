import sys
# from itertools import permutations
# 중복제거 + 리스트에 담지않는 최적화 생각해보기

n= int(sys.stdin.readline().strip())
nums = (list(map(int, sys.stdin.readline().split())))
add, sub, mul, div = map(int,sys.stdin.readline().split())
# print(add,sub,mul,div)
def dfs(i, res, add, sub, mul, div):
    global max_val, min_val
    if i == n:
        max_val = max(max_val, res)
        min_val = min(min_val, res)
        return
    if add:
        dfs(i + 1, res + nums[i], add - 1, sub, mul, div)
    if sub:
        dfs(i + 1, res - nums[i], add, sub - 1, mul, div)
    if mul:
        dfs(i + 1, res * nums[i], add, sub, mul - 1, div)
    if div:
        if res < 0:
            dfs(i + 1, -(-res // nums[i]), add, sub, mul, div - 1)
        else:
            dfs(i + 1, res // nums[i], add, sub, mul, div - 1)

max_val = -1000000000
min_val = 1000000000

dfs(1, nums[0], add, sub, mul, div)

print(max_val)
print(min_val)