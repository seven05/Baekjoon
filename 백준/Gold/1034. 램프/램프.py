import sys

N,M = map(int,sys.stdin.readline().split())
lamp = [(sys.stdin.readline().strip())for _ in range(N)]
K = int(sys.stdin.readline().strip())
# print(table)
max_cnt = 0
for col in range(N):
    zero_count = 0
    for num in lamp[col]:
        if num == '0':
            zero_count += 1
    col_lamp_cnt = 0
    if zero_count <= K and zero_count%2 == K%2:
        for col2 in range(N):  
            if lamp[col] == lamp[col2]:  
                col_lamp_cnt += 1 
                
    max_cnt = max(max_cnt, col_lamp_cnt)  
    
print(max_cnt)