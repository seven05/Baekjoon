import math
import sys

N = input()
N = int(N)

a = list(map(int, sys.stdin.readline().split()))
# print(N,a)
count = 0
for i in range(N):
    if (a[i] == 1):
        count = count
    elif (a[i] == 2):
        count += 1
    elif (a[i]%2 == 0):
        count = count
    else:
        chk = True
        for j in range(1,math.floor(math.sqrt(a[i])+1)):
            if(j == 1):
                chk = True
            elif(a[i]%j == 0):
                chk = False
                break
        if(chk == True):
            count += 1
print(count)