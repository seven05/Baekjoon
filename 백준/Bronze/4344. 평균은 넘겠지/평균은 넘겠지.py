import sys  
import math
n = input()
n = int(n)
for i in range(n):
    (globals()['input'+str(i)]) = list(map(int, sys.stdin.readline().split()))
    # print(globals()['a'+str(i)])
for i in range(n):
    num = (globals()['input'+str(i)])[0]
    # print("num:"+str(num))
    score = (globals()['input'+str(i)])
    # print("score:"+str(score))
    del score[0]
    sum = 0
    for j in range(num):
        sum += score[j]
    avg = sum / num
    # print("sum:"+str(sum))
    # print("avg:"+str(avg))
    count = 0
    for k in range(num):
        if (score[k] > avg):
            count += 1
    result = (count/num)*100
    # print("result:"+str(result))
    print("{:.3f}".format(result)+"%")
    