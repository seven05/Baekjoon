import sys
import math

W,H = map(int,sys.stdin.readline().split())
N = int(sys.stdin.readline())
data = []
for i in range(N):
    data.append(list(map(int,sys.stdin.readline().split())))
# print(X,Y,N)
# print(data)
X=[0,W]
Y=[0,H]
for i in data:
    if(i[0] == 0):
        Y.append(i[1])
    else:
        X.append(i[1])
X.sort()
Y.sort()
# print(X)
# print(Y)
w_max = 0
for i in range(len(X)-1):
    d = X[i+1]-X[i]
    if(d > w_max):
        w_max = d
h_max = 0
for i in range(len(Y)-1):
    d = Y[i+1]-Y[i]
    if(d > h_max):
        h_max = d
print(w_max*h_max)