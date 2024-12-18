import sys
N = int(sys.stdin.readline())
data = []
for i in range(N):
    data.append(int(sys.stdin.readline().strip()))
# print(data)
def insertion_sort(a) -> None:
    """단순 삽입 정렬"""
    n = len(a)
    for i in range(1, n):
        j = i
        tmp = a[i]
        while j > 0 and a[j - 1] > tmp:
            a[j] = a[j - 1]
            j -= 1
        a[j] = tmp

insertion_sort(data)

for i in range(N):
    print(data[i])