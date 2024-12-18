import sys
N = int(sys.stdin.readline().strip())

if N % 4 == 0 or N % 4 == 2:
    print("CY")
else:
    print("SK")