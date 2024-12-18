import sys
N= int(sys.stdin.readline().strip())
data=[]
for i in range(N):
    data.append(list(map(int, sys.stdin.readline().split())))
# print(data)
paper_color = [0,0,0]
def paper(n,x,y):
    global paper_color
    if n == 1:
        # print("test")
        if data[x][y] == 0:
            paper_color[0] += 1
        else:
            paper_color[1] += 1
        return
    s_color = 2
    n_color = 2
    if data[x][y] == 0:
        # print("white test")
        s_color = 0
    else:
        # print("blue test")
        s_color = 1
    check = True
    for i in range(n):
        for j in range(n):
            if  data[x+i][y+j] == 0:
                n_color = 0
            else:
                n_color = 1
            if s_color != n_color:
                check = False
                break
        if check == False:
            break
    half = int(n/2)
    if check == True:
        paper_color[s_color] +=1
    else:
        paper(half,x,y)
        paper(half,x+half,y)
        paper(half,x,y+half)
        paper(half,x+half,y+half)
    
paper(N,0,0)
# print(paper_color)
print(paper_color[0])
print(paper_color[1])