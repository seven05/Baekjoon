import sys
sys.setrecursionlimit(1000000)
A,B,C = map(int,sys.stdin.readline().split())
# print(A,B,C)

def func(a,b,c):
    if b == 0:
        return 1
    if b % 2 == 0:
        half = func(a,b//2,c)
        return (half * half) % c
    else:
        return (a * func(a,b-1,c))%c
result = func(A,B,C)
print(result)