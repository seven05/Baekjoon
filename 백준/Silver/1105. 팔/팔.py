import sys

L, R = map(str, sys.stdin.readline().split())
def solve():
    if len(L) != len(R):
        print(0)
        return
    
    cnt = 0
    for i in range(len(L)):
        if L[i] != R[i]:
            print(cnt)
            return
        else:
            if L[i] == '8':
                cnt += 1
    print(cnt)
solve()
###############
# 시간초과
# L, R = map(int, sys.stdin.readline().split())
## print(L,R)
# min_cnt = 11
# for i in range(L,R+1):
#     cnt = 0 
#     while(i>0):
#         tmp = i%10
#         if (tmp == 8):
#             cnt += 1
#         i -= tmp
#         i /= 10
#     if (cnt < min_cnt):
#         min_cnt = cnt
# print(min_cnt)
