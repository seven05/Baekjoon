import sys
import math
data = []
n = int(sys.stdin.readline())
k = int(sys.stdin.readline())
for i in range(n):
    data.append(sys.stdin.readline().strip())
# print(n,k)
# print(data)
# print(data[0]+data[1])
pick=[]
def permutation(arr, r):
    used = [0 for _ in range(len(arr))]
    def generate(chosen, used):
        if len(chosen) == r:
            pair = ""
            for k in range(r):
                pair += chosen[k]
            pick.append(pair)
            # print(pair)
            return 
        for i in range(len(arr)):
            if not used[i]:
                chosen.append(arr[i])
                used[i] = 1
                generate(chosen, used)
                used[i] = 0
                chosen.pop()
    generate([], used)
permutation(data,k)
# print(pick)
result = []
for val in pick:
    if val not in result:
        result.append(val)
# print(result)
print(len(result))
