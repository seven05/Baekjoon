import sys
N= int(sys.stdin.readline().strip())
data=[]
for i in range(N):
    data.append(list(map(int, sys.stdin.readline().split())))
# print(data)
paper_color = [0,0,0,0]
def paper(n,x,y):
    global paper_color
    if n == 1:
        # print("test")
        if data[x][y] == -1:
            paper_color[2] += 1
        elif data[x][y] == 0:
            paper_color[0] += 1
        else:
            paper_color[1] += 1
        return
    s_color = 3
    n_color = 3
    if data[x][y] == -1:
        s_color = 2
    elif data[x][y] == 0:
        s_color = 0
    else:
        s_color = 1
    check = True
    for i in range(n):
        for j in range(n):
            if data[x+i][y+j] == -1:
                n_color = 2
            elif data[x+i][y+j] == 0:
                n_color = 0
            else:
                n_color = 1
            if s_color != n_color:
                check = False
                break
        if check == False:
            break
    split_3 = n//3
    if check == True:
        paper_color[s_color] +=1
    else:
        paper(split_3,x,y)
        paper(split_3,x+split_3,y)
        paper(split_3,x+split_3*2,y)
        paper(split_3,x,y+split_3)
        paper(split_3,x+split_3,y+split_3)
        paper(split_3,x+split_3*2,y+split_3)
        paper(split_3,x,y+split_3*2)
        paper(split_3,x+split_3,y+split_3*2)
        paper(split_3,x+split_3*2,y+split_3*2)
    
paper(N,0,0)
# print(paper_color)
print(paper_color[2])
print(paper_color[0])
print(paper_color[1]) 