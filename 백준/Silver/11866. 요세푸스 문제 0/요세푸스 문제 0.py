import sys

N,K = map(int,sys.stdin.readline().split())
# print(N,K)
circle = [i for i in range(1,N+1)]
result = []
start = K-1
while len(circle)>1:
    result.append(circle[start])
    circle.pop(start)
    start = (start + K-1)%len(circle)
result.append(circle[0])
output = '<' + ', '.join(map(str, result)) + '>'
print(output)