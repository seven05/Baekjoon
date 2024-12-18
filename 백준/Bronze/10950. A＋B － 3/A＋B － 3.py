T = input()
T = int(T)
for i in range(T):
    globals()['a'+str(i)],globals()['b'+str(i)] = input().split()
for j in range(T):
    print(int(globals()['a'+str(j)]) + int(globals()['b'+str(j)]))