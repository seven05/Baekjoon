import sys

T = int(sys.stdin.readline().strip())
for _ in range(T):
    N = int(sys.stdin.readline().strip())
    data = []
    for _ in range(N):
        data.append(list(map(int,sys.stdin.readline().split())))
    sorted_data = sorted(data,key=lambda x:x[0])
    # print(sorted_data)
    cut_line = sorted_data[0][1]
    result = 1
    for i in range(1,N):
        if sorted_data[i][1] <= cut_line:
            result += 1
            cut_line = sorted_data[i][1]
    print(result)