import sys
N = int(sys.stdin.readline().strip())
memo = [0]*((10**6)+1)
def tile(n):
    global memo
    memo[0]= 0
    memo[1]= 1
    memo[2]= 2
    if n > 2:
        for i in range(3,n+1):
            memo[i]=(memo[i-1]+memo[i-2]) % 15746
    return memo[n]
print(tile(N))