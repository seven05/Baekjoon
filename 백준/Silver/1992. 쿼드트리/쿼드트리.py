import sys

N = int(sys.stdin.readline().strip())
data=[]
for i in range(N):
    data.append(list(map(int,sys.stdin.readline().strip())))
# print(data)

def quad_tree(x,y,n):
    # n = 1 인경우는 무조건 값이 같아서 처리됨
    s_num = data[x][y]
    check = True
    for i in range(x,x+n):
        for j in range(y,y+n):
            if data[i][j] != s_num:
                check = False
                break
        if check != True:
            break
    if check:
        return str(s_num)
    half = n // 2
    first_side = quad_tree(x,y,half)
    second_side = quad_tree(x,y+half,half)
    third_side = quad_tree(x+half,y,half)
    fourth_side = quad_tree(x+half,y+half,half)

    return '(' + first_side + second_side + third_side + fourth_side + ')'

print(quad_tree(0,0,N))