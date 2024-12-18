import math

x,y,w,h = input().split()

x = int(x)
y = int(y)
w = int(w)
h = int(h)

a = int((w/2)-abs(x-(w/2)))
b = int((h/2)-abs(y-(h/2)))

if(a>b):
    print(b)
else:
    print(a)