import sys

N = int(sys.stdin.readline().strip())
command = []
for i in range(N):
    command.append(list(sys.stdin.readline().split()))
# print(command)
stack = []
def push(x):
    stack.append(x)

def empty():
    if len(stack) == 0 :
        return 1
    else:
        return 0

def pop():
    if empty():
        return -1
    else:
        tmp = stack[-1]
        del stack[-1]
        return tmp
    
def size():
    return len(stack)

def top():
    if empty():
        return -1
    else:
        return stack[-1]

for i in range(N):
    if command[i][0] == "push":
        push(command[i][1])
    elif command[i][0] == "pop":
        print(pop())
    elif command[i][0] == "size":
        print(size())
    elif command[i][0] == "empty":
        print(empty())
    else:
        print(top())