import sys

N,M = map(int,sys.stdin.readline().split())
Map = []
for _ in range(N):
    Map.append(list(map(int,sys.stdin.readline().split())))
# print(N,M,Map)

home = []
kfc = []
for r in range(N):
    for c in range(N):
        if Map[r][c] == 1:
            home.append((r,c))
        elif Map[r][c] == 2:
            kfc.append((r,c))

def get_combi(arr, M):
    results = []
    combi = []

    def backtrack(start_index):
        if len(combi) == M:
            results.append(combi[:])
            return
        
        for i in range(start_index, len(arr)):
            combi.append(arr[i])
            backtrack(i + 1)
            combi.pop()

    backtrack(0)
    return results

kfc_combi = get_combi(kfc,M)
min_kfc_dist = 10**8

for subset in kfc_combi:
    curr_kfc_dist = 0
    for hr, hc in home:
        home_kfc_dist = 101
        for cr,cc in subset:
            dist = abs(hr-cr)+abs(hc-cc)
            if dist < home_kfc_dist:
                home_kfc_dist = dist
        curr_kfc_dist += home_kfc_dist
    min_kfc_dist = min(min_kfc_dist,curr_kfc_dist)

print(min_kfc_dist)