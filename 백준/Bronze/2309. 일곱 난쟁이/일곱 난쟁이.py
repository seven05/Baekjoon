import sys

data=[]
for i in range(9):
    data.append((sys.stdin.readline().strip()))
# print(data)
total=0
for i in data:
        total += int(i)
for i in range(9):
    check = False
    for j in range(i+1,9):
        # print(i,j)
        if (total - int(data[i]) - int(data[j])) == 100 :
            del data[j]
            del data[i]
            check = True
            break
    if check == True:
         break
# print(data)
int_data = [int(x) for x in data]  
# print(int_data)
int_data.sort()
for i in range(7):
    print(int_data[i])