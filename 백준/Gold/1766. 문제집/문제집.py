import sys
input = sys.stdin.readline
import heapq

def topology_sort():
    while heap:
        current = heapq.heappop(heap)
        result.append(current)

        if len(graph[current]) == 0:
            continue

        for next in graph[current]:
            indegree[next] -= 1
            if indegree[next] == 0:
                heapq.heappush(heap, next)

    for i in result:
        print(i, end = ' ')

if __name__ == '__main__':
    N, M = map(int, input().split())
    graph = [[] for i in range(N + 1)]
    indegree = [0] * (N + 1)

    for i in range(M):
        a, b = map(int, input().split())
        graph[a].append(b)
        indegree[b] += 1

    heap = []

    result = []

    for i in range(1, N + 1):
        if indegree[i] == 0:
            heapq.heappush(heap, i)

    topology_sort()