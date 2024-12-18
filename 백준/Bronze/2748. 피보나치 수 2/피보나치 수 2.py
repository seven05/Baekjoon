import sys
N = int(sys.stdin.readline().strip())
memo = [0]*95
def fifo(n):
    if (n<=1):
        return n 
    else:
        if(memo[n] > 0):
            return memo[n]
        memo[n] = fifo(n-1) + fifo(n-2)
        return memo[n]
print(fifo(N))