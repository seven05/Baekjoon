import sys

N= int(sys.stdin.readline().strip())
# print(N)
data=[]
for i in range(N):
    data.append(list(map(int, sys.stdin.readline().split())))
# print(data)
city = [i for i in range(N)]
# print(city)
visited = [0] * N
explore=[]
costs = []
def dfs(depth):
    if depth == N:
        temp = 0
        for j in range(N):
            if j < N-1:
                cost = data[explore[j]][explore[j+1]]
            else:
                cost = data[explore[j]][explore[0]]
            if(cost != 0) :
                temp += cost
            else:
                temp += 1000001
        costs.append(temp)
        # print(explore,temp)
        return
    for i in range(N):
        if visited[i]:
            continue
        explore.append(city[i])
        visited[i] = 1
        # print(explore)
        dfs(depth + 1)
        visited[i] = 0
        explore.pop()
dfs(0)
# print(costs)
print(min(costs))