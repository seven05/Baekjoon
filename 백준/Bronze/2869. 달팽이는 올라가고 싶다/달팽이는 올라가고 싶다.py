import math

A,B,V = input().split()
A = int(A)
B = int(B)
V = int(V)

result = (math.ceil((V-A)/(A-B)))+1
print(int(result))