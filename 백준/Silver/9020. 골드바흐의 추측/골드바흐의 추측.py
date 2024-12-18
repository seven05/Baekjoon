import math
import sys

n = input()
n = int(n)
a = []
for i in range(n):
    a.append(list(map(int,sys.stdin.readline().split())))

def check(num):
    chk = False
    if(num == 2):
        chk = True
    else:
        for i in range(1,math.floor(math.sqrt(num)+1)):
            if(i == 1):
                chk = True
            elif(num%i == 0):
                chk = False
                break
    if(chk == True):
        return True
    else:
        return False
    
for i in range(n):
    N = a[i][0]
    A = int(N/2)
    B = int(N/2)
    while(True):
        if (check(A) == True):
            if(check(B) == True):
                print(A,B)
                break
            else:
                A = A-1
                B = B+1
        else:
            A = A-1
            B = B+1