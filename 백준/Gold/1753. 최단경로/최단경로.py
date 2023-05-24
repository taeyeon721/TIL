import sys
import heapq
input = sys.stdin.readline

INF = 10**9
V, E = map(int, input().split())
K = int(input())
distance = [INF]*(V+1)
heap = []
graph = [[] for _ in range(V+1)]

for _ in range(E):
    a, b, w = map(int, input().split())
    graph[a].append((w, b))


def dijkstra(start):
    distance[start] = 0
    heapq.heappush(heap, (0, start))
    while heap:
        weight, now = heapq.heappop(heap)
        if distance[now]<weight:
            continue
        for w, b in graph[now]:
            nw = w+weight
            if nw < distance[b]:
                distance[b] = nw
                heapq.heappush(heap,(nw, b))


dijkstra(K)
for i in range(1, V+1):
    print(distance[i] if distance[i] != INF else 'INF')