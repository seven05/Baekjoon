import sys

N = int(sys.stdin.readline().strip())
def draw_star(n):
    if n == 1:
        return ['*']
    star = draw_star(n//3)
    pattern = []
    for i in range(3):
        for j in star:
            if i == 1:
                pattern.append(j+' '*(n//3)+j)
            else:
                pattern.append(j*3)
    return pattern

result = draw_star(N)
for line in result:
    print(line)