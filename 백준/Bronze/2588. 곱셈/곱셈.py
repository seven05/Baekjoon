import math

a = input()
b = input()
a = int(a)
b = int(b)

# a100 = int(a/100)
# a10 = int((a%100)/10)
# a1 = a%10

b100 = int(b/100)
b10 = int((b%100)/10)
b1 = b%10
#print(a,a100,a10,a1)
c = a*b1
d = a*b10
e = a*b100

print(c)
print(d)
print(e)
print(a*b)