import sys  
n = input()
n = int(n)  
a = [sys.stdin.readline() for i in range(n)]  
# print(a)
# print(a[0][9])
# if(a[0][9] == "\n"):
#     print("ASD")
for i in range(n):
    j = 0
    score = 0
    count = 0
    while(True):
        if(a[i][j] == "\n"):
            break
        if(a[i][j] == "O"):
            count += 1
            score += count
        if(a[i][j] == "X"):
            count = 0
        j += 1
    print(score)