import heapq
import sys


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    ans[start] = 0

    while q:
        d, n = heapq.heappop(q)
        if ans[n] < d:
            continue
        for i in arr[n]:
            if d+i[1] < ans[i[0]]:
                ans[i[0]] = d+i[1]
                heapq.heappush(q, (d+i[1], i[0]))


input = sys.stdin.readline
INF = 10**9
N, M = map(int, input().split())
arr = [[] for _ in range(N+1)]
ans = [INF]*(N+1)
for _ in range(M):
    a, b, c = map(int, input().split())
    arr[a].append([b, c])
    arr[b].append([a, c])
dijkstra(1)
print(ans[N])