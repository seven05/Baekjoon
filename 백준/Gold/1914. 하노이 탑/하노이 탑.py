import sys
import math

N = input()
N = int(N)
print((2**N)-1)
def hanoi(n,s,e):
    if(n>1):
        hanoi(n-1,s,6-s-e)
    print(s,e)
    if(n>1):
        hanoi(n-1,6-s-e,e)
if(N <= 20):
    hanoi(N,1,3)