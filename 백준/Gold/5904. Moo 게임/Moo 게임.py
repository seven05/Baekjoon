import sys
sys.setrecursionlimit(1000000)
N = int(sys.stdin.readline().strip())
K = 0
Length = 3
while Length < N:
    K += 1
    Length = 2 * Length + (K + 3) 
# print(K)
def find_n(k,n,length):
    global prev_len
    if k == 0:
        return "moo"[n-1]   
    prev_len = (length-(k+3)) // 2
    mid_len = k + 3
    if n < prev_len:
        return find_n(k - 1, n,prev_len)
    elif n < prev_len + mid_len:
        if n == prev_len+1:
            return "m"
        else:
            return "o"
    else:
        return find_n(k - 1, n - prev_len - mid_len,prev_len)

print(find_n(K,N,Length))