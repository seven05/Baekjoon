# 시간초과로 답 확인함

import sys
r=sys.stdin.readline

class Polution:
    def __init__(self, x, p):
        self.x = x
        self.p = p

n = int(r())
a = []
for _ in range(n):
    x, p = map(int,r().split())
    a.append(Polution(x, p))

a.sort(key = lambda e : e.x)

usedCount = 1
bottomUp = a[0].p
for i in range(n-1):
    bottomUp += usedCount * (a[i+1].x - a[i].x) + a[i+1].p
    usedCount += 1

usedCount = 1
topDown = a[n-1].p
for i in range(n-1, 0, -1):
    topDown += usedCount * (a[i].x - a[i-1].x) + a[i-1].p
    usedCount += 1

ans = bottomUp
for i in range(n):
    ans = min(ans, bottomUp - a[i].p - (a[n-1].x - a[i].x))

for i in range(n-1, -1, -1):
    ans = min(ans, topDown - a[i].p - (a[i].x - a[0].x))

ans = min(ans, bottomUp - a[-1].p - (n - 1) * (a[-1].x - a[-2].x))
ans = min(ans, topDown - a[0].p - (n - 1) * (a[1].x - a[0].x))

print(ans)

# 시간초과
# import sys

# N = int(sys.stdin.readline().strip())
# M = []
# for _ in range(N):
#     M.append(list(map(int, sys.stdin.readline().split())))
# print(N,M)
# def total_usage(B,start_x):
#     B_sorted = sorted(B, key=lambda t: abs(t[0] - start_x))
    
#     usage_count = 0       
#     current_pos = start_x
#     total_spent = 0      
    
#     for (x_i, p_i) in B_sorted:
#         dist = abs(x_i - current_pos)
#         total_spent += dist * usage_count
#         current_pos = x_i
#         total_spent += p_i
#         usage_count += 1

#     return total_spent

# INF = 10**10
# answer = INF

# for skip_idx in range(N):
#     B = []
#     for i in range(N):
#         if i == skip_idx:
#             continue
#         B.append(M[i])
    
#     for start_M in B:
#         start_x = start_M[0]
#         cost = total_usage(B, start_x)
#         answer = min(answer, cost)

# print(answer)