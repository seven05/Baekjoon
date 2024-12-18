import sys

data =[]
for i in range(10):
    data.append(int(sys.stdin.readline().strip()))
# print(data)
last_sum = 0
def mario():
    global last_sum
    for i in range(10):
        if abs(100-last_sum) == abs(100-(last_sum+data[i])):
            return last_sum+data[i]
        if (abs(100-last_sum) < abs(100-(last_sum+data[i]))):
            return last_sum
        last_sum += data[i]
    return last_sum
print(mario())