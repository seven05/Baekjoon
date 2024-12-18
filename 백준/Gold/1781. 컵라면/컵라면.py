#복습필요
import sys
import heapq
N = int(sys.stdin.readline().strip())

problem_list = []
for _ in range(N):
    problem_list.append(list(map(int,sys.stdin.readline().split())))
problem_list.sort(key= lambda x:x[0])
#힙을 활용하여 데드 라인 내에서 최대 컵라면 수를 구함
cup_ramen_heap = []
for problem in problem_list:
    heapq.heappush(cup_ramen_heap, problem[1]) #problem[1]은 각 문제의 컵라면 개수
    #이때 len(cup_ramen_heap)이 문제를 푸는데 걸리는 시간이라고 생각하는 것이 중요하다.
    #1문제 풀때 시간이 1 흐르니까
    if len(cup_ramen_heap) > problem[0]:  #problem[0]은 각 문제의 데드라인, 데드라인을 초과하는 문제는 힙에서 제거
    #데드라인을 초과했을 때, 가장 컵라면을 적게 받는 문제를 제거
        heapq.heappop(cup_ramen_heap)
#이렇게 되면 len(cup_ramen_heap)시간 내에 얻을 수 있는 가장 많은 양의 컵라면이 heapq에 담긴다.
print(sum(cup_ramen_heap))