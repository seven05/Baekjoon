import sys
N = input()
N = int(N)
a = [sys.stdin.readline().split() for i in range(N)]
# print(a)

for i in range(N):
    num = int(a[i][0])
    text = a[i][1]
    # print(text[0])
    result = ""
    for j in text:
        for k in range(num):
            result += j
    print(result)