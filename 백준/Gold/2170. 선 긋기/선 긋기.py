import sys

N = int(sys.stdin.readline().strip())
segments = []

for _ in range(N):
    x, y = map(int,sys.stdin.readline().split())
    segments.append((x, y))

segments.sort(key=lambda seg: seg[0])
merged_start, merged_end = segments[0]
total_length = 0

for i in range(1, N):
    cur_start, cur_end = segments[i]
        
    if cur_start <= merged_end:
        if cur_end > merged_end:
            merged_end = cur_end
    else:
        total_length += (merged_end - merged_start)
        merged_start, merged_end = cur_start, cur_end

total_length += (merged_end - merged_start)

print(total_length)