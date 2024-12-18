import sys
import math

A = int(sys.stdin.readline())
B = int(sys.stdin.readline())
C = int(sys.stdin.readline())
# print(A,B,C)
N = A*B*C
result = [0,0,0,0,0,0,0,0,0,0]
while(True):
    num = int(N%10)
    # print(num)
    result[num] += 1
    if(N/10 < 1):
        break
    N = N/10
for i in range(10):
    print(result[i])
