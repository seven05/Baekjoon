import sys
from itertools import combinations
N = int(sys.stdin.readline().strip())
ans = []
if N >= 1023:
    print(-1)
else:
    for i in range(1, 11):
        # 0부터 9까지 숫자 중에서 i개를 고르는 모든 조합 
        for j in combinations(range(0, 10), i):
            # 이 튜플을 리스트로 변환한 뒤 역순으로 정렬
            # -> 감소하는 수를 만들기 위해 자리수가 가장 큰 곳에 큰 숫자가 오도록
            tmp = sorted(list(j), reverse = True)
            # tmp=[9,5,0] -> "950" -> int("950") = 950
            ans.append(int("".join(map(str,tmp))))
    ans.sort()
    print(ans[N])