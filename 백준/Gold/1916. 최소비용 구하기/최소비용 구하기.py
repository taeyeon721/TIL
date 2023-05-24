import sys
import heapq
input = sys.stdin.readline

N = int(input())
M = int(input())
INF = 10**9
g = [[] for _ in range(N+1)]
dist = [INF]*(N+1)
for _ in range(M):
    a, b, w = map(int, input().split())
    g[a].append((w, b))

S, E = map(int, input().split())

heap = []


def dijkstra(start):
    dist[start] = 0
    heapq.heappush(heap, (0, start))

    while heap:
        wei, now = heapq.heappop(heap)
        if dist[now] < wei:
            continue
        for w, b in g[now]:
            nw = w+wei
            if dist[b] > nw:
                dist[b] = nw
                heapq.heappush(heap, (nw, b))


dijkstra(S)
print(dist[E])