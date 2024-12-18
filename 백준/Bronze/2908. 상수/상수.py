import math

a,b = input().split()
a = int(a)
b = int(b)

a100 = int(a/100)
a10 = int((a%100)/10)
a1 = a%10

b100 = int(b/100)
b10 = int((b%100)/10)
b1 = b%10

A = a1*100 + a10*10 + a100
B = b1*100 + b10*10 + b100

if (A > B):
    print(A)
else:
    print(B)