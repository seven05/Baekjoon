import sys

N = int(sys.stdin.readline().strip())

deck = list(i for i in range(1,N+1))
start = 0
while len(deck)-start > 1:
    start += 1                  # pop
    deck.append(deck[start])    # 맨뒤로
    start += 1                  # pop
print(deck[start])