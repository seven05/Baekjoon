import sys

N = int(sys.stdin.readline().strip())
data = []
for i in range(N):
    data.append(list(map(int,sys.stdin.readline().split())))
data.sort()
# print(data)

def get_distance(p1,p2): # 거리 제곱
    return (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2

def find_closet_dist(points):
    if len(points) < 2:
        return float('inf')
    elif len(points) == 2:
        return get_distance(points[0], points[1])
    else:
        mid = len(points) // 2
        min_dist = min(find_closet_dist(points[:mid]), find_closet_dist(points[mid:]))
        target_x = []
        # 중간선을 기준으로 min_dist 거리 내에 있는 점들을 모음
        for i in range(len(points)):
            if (points[mid][0] - points[i][0])**2 < min_dist:
                target_x.append(points[i])
        # 모은 점들을 y좌표를 기준으로 정렬
        target_x.sort(key=lambda x: x[1])
        # 중간선 근처의 점들 사이에서 최소 거리를 찾음
        for i in range(len(target_x) - 1):
            for j in range(i + 1, len(target_x)):
                if (target_x[i][1] - target_x[j][1])**2 < min_dist:
                    min_dist = min(min_dist, get_distance(target_x[i], target_x[j]))
                else:
                    break
        return min_dist
print(find_closet_dist(data))