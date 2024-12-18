import sys
import math

N = input()
N = int(N)

count = 0
for i in range(1,N+1):
    if (i < 100):
        count += 1
    else:
        n100 = int(i/100)
        n10 = int((i%100)/10)
        n1 = i%10
        if((n100 - n10) == (n10 -n1)):
            count +=1
print(count)
        