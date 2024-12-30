import sys

N = int(sys.stdin.readline().strip())
candy_borad = []
for _ in range(N):
    candy_borad.append(list(sys.stdin.readline().strip())) # 이렇게 해야 문자열이 아니라 문자로 들어가서 이중배열로 접근가능
# print(N,candy_borad)
# print(candy_borad[1][1])
def check_max_len(board):
    num = len(board)
    max_len = 0
    for i in range(num):
        cnt = 1
        for j in range(1,num):
            if board[i][j] == board[i][j-1]:
                cnt += 1
                max_len = max(max_len,cnt)
            else:
                cnt = 1
    for j in range(num):
        cnt = 1
        for i in range(1,num):
            if board[i][j] == board[i-1][j]:
                cnt += 1
                max_len = max(max_len,cnt)
            else:
                cnt = 1
        max_len = max(max_len,cnt)
    return max_len

ans = 0
for r in range(N):
    for c in range(N):
        for dr,dc in [(1,0),(0,1),(-1,0),(0,-1)]:
            nr = r+dr
            nc = c+dc

            if(0 <= nr < N and 0 <= nc < N and candy_borad[r][c] != candy_borad[nr][nc]):
                candy_borad[r][c], candy_borad[nr][nc] = candy_borad[nr][nc], candy_borad[r][c]
                max_val = check_max_len(candy_borad)
                ans = max(ans,max_val)
                candy_borad[r][c], candy_borad[nr][nc] = candy_borad[nr][nc], candy_borad[r][c]
print(ans)