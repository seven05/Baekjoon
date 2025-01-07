import sys
import math

N,M,K = map(int,sys.stdin.readline().split())
# print(N,M,K)
ans = 0 
if K == 0:
    ans = math.factorial(N-1+M-1)/(math.factorial(N-1)*math.factorial(M-1))
else:
    y = K // M
    x = K - M*y
    # print(x,y)
    first = math.factorial(x-1+y)/(math.factorial(x-1)*math.factorial(y))
    # print(first)
    second = math.factorial(M-x+N-y-1)/(math.factorial(M-x)*math.factorial(N-y-1))
    # print(second)
    ans = first * second
ans = int(ans)
print(ans)