import sys   
count = 1
a = list(map(int,[sys.stdin.readline() for i in range(9)]))
num = a[0]
#print(a)
for i in range(8):
    if(a[i+1] > num):
        count = i+2
        num = a[i+1]
print(num)
print(count)